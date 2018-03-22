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

    ar_matrix, technique_acronyms = make_ar_matrix(dataset_ids)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    mat = ax.matshow(ar_matrix, cmap=plt.cm.viridis)
    ax.set_xticklabels(dataset_ids, rotation='vertical')
    ax.set_xticks(range(len(dataset_ids)), minor=False)
    ax.set_yticklabels(technique_acronyms)
    ax.set_yticks(range(len(technique_acronyms)), minor=False)

    fig.colorbar(mat)
    plt.show()
    a = 1


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
