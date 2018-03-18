import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import sys
import math

import KDE
import Metrics
import Parser

action = sys.argv[1]
dataset_id = sys.argv[2]


if action == 'cache-metrics':
    Metrics.compute_and_cache_metrics(dataset_id)

elif action == 'kde-real-baseline':
    # Read a dataset's metric values (either CT or RPC) from disk
    ct_values = Parser.read_ct_metric(dataset_id)
    KDE.plot_real_vs_baseline(ct_values)