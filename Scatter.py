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
    averages = collect_averages(dataset_ids)
    brewer = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a','#919114', '#b15928']

    fig = plt.figure(figsize=(10,10))
    for technique in sorted(acronyms):
        df = averages[(averages['technique'] == acronyms[technique])]
        colors = [brewer[i] for i in df['label'].values]
        labels = df['technique'].iloc[0]

        x_mean = df['inst'].mean()
        y_mean = df['ar'].mean()
        #plt.scatter(df['inst'], df['ar'], s=60, c=colors, label=labels, edgecolors=None)

        for i, point in df.iterrows():
            x_line = [x_mean, point['inst']]
            y_line = [y_mean, point['ar']]
            # Lines
            # plt.plot(x_line, y_line, c=colors[0], zorder=1)
            # Labels
            plt.text(point['inst'], point['ar'], str(int(i/len(acronyms))), color='black', ha='center', va='center', fontsize=7)
        # Points
        # plt.scatter(x_mean, y_mean, s=80, c=colors, label=labels, linewidth=2, zorder=10)

    plt.xlim(xmin=0, xmax=0.35)
    plt.ylim(ymin=0, ymax=1)
    plt.legend(loc=4)

    fig.savefig("scatter/scatter-l.svg")
    fig.savefig("scatter/scatter-l.png", dpi=500)
    # plt.show()

    return None


def collect_averages(dataset_ids):
    results = []
    for dataset_id in dataset_ids:
        inst_dict = instability_average(dataset_id)
        ar_dict = ar_average(dataset_id)

        technique_list = sorted(ar_dict)
        for i, technique in enumerate(technique_list):
            results.append([dataset_id, acronyms[technique], i, ar_dict[technique], inst_dict[technique]])


    df = pd.DataFrame(results, columns=['dataset', 'technique', 'label', 'ar', 'inst'])
    return df


def instability_average(dataset_id):
    ct_df = Parser.read_ct_metric(dataset_id)
    rpc_df = Parser.read_rpc_metric(dataset_id)

    means = {}

    technique_list = sorted(rpc_df)
    for i, technique_id in enumerate(technique_list):
        technique_means = []
        for revision in range(int(len(rpc_df[technique_id].columns) / 2)):
            r_col = rpc_df[technique_id].columns[2 * revision]
            b_col = rpc_df[technique_id].columns[2 * revision + 1]
            diff = rpc_df[technique_id][[r_col, b_col]].max(axis=1) - rpc_df[technique_id][b_col]
            ct_mean = diff.dropna().mean()

            r_col = ct_df[technique_id].columns[2 * revision]
            b_col = ct_df[technique_id].columns[2 * revision + 1]
            diff = ct_df[technique_id][[r_col, b_col]].max(axis=1) - ct_df[technique_id][b_col]
            rpc_mean = diff.dropna().mean()

            technique_means.append((ct_mean + rpc_mean) / 2)

        means[technique_id] = np.mean(technique_means)

    return means


def ar_average(dataset_id):
    ar_df = Parser.read_aspect_ratios(dataset_id)
    means = {}

    technique_list = sorted(ar_df)
    for i, technique_id in enumerate(technique_list):
        technique_means = []
        for revision in range(int(len(ar_df[technique_id].columns) / 2)):
            df = ar_df[technique_id]
            w_col = df.columns[2 * revision]
            ar_col = df.columns[2 * revision + 1]

            u_avg = ar_df[technique_id][ar_col].mean(axis=0)
            w_avg = np.average(ar_df[technique_id][ar_col].dropna(), weights=ar_df[technique_id][w_col].dropna())

            technique_means.append((u_avg + w_avg)/2)

        means[technique_id] = np.mean(technique_means)

    return means
