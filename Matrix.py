import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import Parser

acronyms = {
    'ApproximationTreeMap': 'APP',
    'HilbertTreeMap': 'HIL',
    'IncrementalLayoutWithMoves': 'LM4',
    'IncrementalLayoutWithoutMoves': 'LM0',
    'MooreTreeMap': 'MOO',
    'PivotByMiddle': 'PBM',
    'PivotBySize': 'PBZ',
    'PivotBySplit': 'PBS',
    'SliceAndDice': 'SND',
    'SpiralTreeMap': 'SPI',
    'SquarifiedTreeMap': 'SQR',
    'StripTreeMap': 'STR'
}


def plot(dataset_ids):
    # Plot AR matrix
    ar_matrix, technique_acronyms = make_ar_matrix(dataset_ids)
    plot_matrix(ar_matrix, dataset_ids, technique_acronyms, 'ar')

    # Plot CT matrix
    ct_matrix, technique_acronyms = make_ct_matrix(dataset_ids)
    plot_matrix(ct_matrix, dataset_ids, technique_acronyms, 'ct')

    # Plot RPC matrix
    rpc_matrix, technique_acronyms = make_rpc_matrix(dataset_ids)
    plot_matrix(rpc_matrix, dataset_ids, technique_acronyms, 'rpc')


def plot_matrix(matrix, dataset_ids, technique_acronyms, metric_id):

    fig = plt.figure()
    ax = fig.add_subplot(111)
    if metric_id == 'ar':
        mat = ax.matshow(matrix, cmap=plt.cm.viridis)
    else:
        mat = ax.matshow(matrix, cmap=plt.cm.viridis_r)  # Invert colormap for instability

    # Ticks, labels and grids
    ax.set_xticklabels(dataset_ids, rotation='vertical')
    ax.set_xticks(range(len(dataset_ids)), minor=False)
    ax.set_yticklabels(technique_acronyms)
    ax.set_yticks(range(len(technique_acronyms)), minor=False)
    ax.set_xticks([x - 0.5 for x in plt.gca().get_xticks()][1:], minor='true')
    ax.set_yticks([y - 0.5 for y in plt.gca().get_yticks()][1:], minor='true')
    plt.grid(which='minor', color='#999999', linestyle='-', linewidth=1)
    ax.tick_params(axis=u'both', which=u'both', length=0)

    # Add the text
    x_start = 0.0
    x_end = len(dataset_ids)
    y_start = 0.0
    y_end = len(technique_acronyms)

    jump_x = (x_end - x_start) / (2.0 * len(dataset_ids))
    jump_y = (y_end - y_start) / (2.0 * len(technique_acronyms))
    x_positions = np.linspace(start=x_start-0.5, stop=x_end-0.5, num=len(dataset_ids), endpoint=False)
    y_positions = np.linspace(start=y_start-0.5, stop=y_end-0.5, num=len(technique_acronyms), endpoint=False)

    for y_index, y in enumerate(y_positions):
        for x_index, x in enumerate(x_positions):
            label = "{0:.3f}".format(matrix[y_index, x_index]).lstrip('0')
            text_x = x + jump_x
            text_y = y + jump_y
            ax.text(text_x, text_y, label, color='black', ha='center', va='center', fontsize=9)

    fig.colorbar(mat)
    fig.tight_layout()
    fig.savefig('matrix-'+ metric_id +'.png', dpi=600)
    # plt.show()


def make_ct_matrix(dataset_ids):
    technique_ids = []
    all_means = []
    for dataset_id in dataset_ids:
        ct_df = Parser.read_ct_metric(dataset_id)

        dataset_means = np.array([])
        technique_list = sorted(ct_df)
        if len(technique_ids) == 0:
            technique_acronyms = [acronyms[d] for d in technique_list]

        for i, technique_id in enumerate(technique_list):
            technique_means = []
            for revision in range(int(len(ct_df[technique_id].columns) / 2)):
                df = ct_df[technique_id]
                r_col = df.columns[2 * revision]
                b_col = df.columns[2 * revision + 1]

                diff = df[[r_col, b_col]].max(axis=1) - df[b_col]
                diff = diff.dropna()
                diff_mean = diff.mean()

                technique_means.append(diff_mean)

            dataset_means = np.append(dataset_means, np.mean(technique_means))
        all_means.append(dataset_means)

    return np.array(all_means).transpose(), technique_acronyms  # Transpose matrix so each row is a technique and each column a dataset


def make_rpc_matrix(dataset_ids):

    technique_ids = []
    all_means = []
    for dataset_id in dataset_ids:
        rpc_df = Parser.read_rpc_metric(dataset_id)

        dataset_means = np.array([])
        technique_list = sorted(rpc_df)
        if len(technique_ids) == 0:
            technique_acronyms = [acronyms[d] for d in technique_list]

        for i, technique_id in enumerate(technique_list):
            technique_means = []
            for revision in range(int(len(rpc_df[technique_id].columns) / 2)):
                df = rpc_df[technique_id]
                r_col = df.columns[2 * revision]
                b_col = df.columns[2 * revision + 1]

                diff = df[[r_col, b_col]].max(axis=1) - df[b_col]
                diff = diff.dropna()
                diff_mean = diff.mean()

                technique_means.append(diff_mean)

            dataset_means = np.append(dataset_means, np.mean(technique_means))
        all_means.append(dataset_means)

    return np.array(all_means).transpose(), technique_acronyms  # Transpose matrix so each row is a technique and each column a dataset


def make_ar_matrix(dataset_ids):

    technique_ids = []
    all_means = []
    for dataset_id in dataset_ids:
        ar_df = Parser.read_aspect_ratios(dataset_id)

        dataset_means = np.array([])
        technique_list = sorted(ar_df)
        if len(technique_ids) == 0:
            technique_acronyms = [acronyms[d] for d in technique_list]

        for i, technique_id in enumerate(technique_list):
            technique_means = []
            for revision in range(int(len(ar_df[technique_id].columns) / 2)):
                df = ar_df[technique_id]
                w_col = df.columns[2 * revision]
                ar_col = df.columns[2 * revision + 1]

                u_avg = ar_df[technique_id][ar_col].mean(axis=0)
                w_avg = np.average(ar_df[technique_id][ar_col].dropna(), weights=ar_df[technique_id][w_col].dropna())

                technique_means.append((u_avg + w_avg) / 2)

            dataset_means = np.append(dataset_means, np.mean(technique_means))
        all_means.append(dataset_means)

    return np.array(all_means).transpose(), technique_acronyms  # Transpose matrix so each row is a technique and each column a dataset
