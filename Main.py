import sys

import KDE
import Metrics
import Parser
import Boxplots

action = sys.argv[1]
dataset_id = sys.argv[2]


if action == 'cache-metrics':
    Metrics.compute_and_cache_metrics(dataset_id)

elif action == 'kde-real-baseline':
    # Read a dataset's metric values (either CT or RPC) from disk
    ct_values = Parser.read_ct_metric(dataset_id)
    KDE.plot_real_vs_baseline(ct_values, dataset_id, 'ct', True)
    print('---')

    # KDE.plot_real_vs_baseline(ct_values, dataset_id, 'ct', False)
    # rpc_values = Parser.read_rpc_metric(dataset_id)
    # print('---')

    # KDE.plot_real_vs_baseline(rpc_values, dataset_id, 'rpc', True)
    # KDE.plot_real_vs_baseline(rpc_values, dataset_id, 'rpc', False)
    # print('---')

elif 'time-boxplots':
    ar_values = Parser.read_aspect_ratios(dataset_id)
    Boxplots.plot_ar(ar_values, dataset_id)
    ct_values = Parser.read_ct_metric(dataset_id)
    Boxplots.plot_instability(ct_values, dataset_id, 'ct')
    rpc_values = Parser.read_rpc_metric(dataset_id)
    Boxplots.plot_instability(rpc_values, dataset_id, 'rpc')

