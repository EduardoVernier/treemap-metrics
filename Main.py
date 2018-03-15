import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import sys
import math

import Metrics

action = sys.argv[1]
dataset_id = sys.argv[2]


if action == 'cache_metrics':
    Metrics.compute_and_cache_metrics(dataset_id)
