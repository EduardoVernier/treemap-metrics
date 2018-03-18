import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm, Normalize
from matplotlib import cm
from scipy import stats
import random


def plot_real_vs_baseline(values):

    nrow = 6
    ncol = 2
    fig, axs = plt.subplots(nrow, ncol, sharex=True, sharey=True, figsize=(10, 30))
    fig.tight_layout()

    technique_list = sorted(values)

    for i, technique_id in enumerate(technique_list):
        print(technique_id)
        ax = fig.axes[i]
        full_df = values[technique_id]
        real_series = full_df.iloc[:, ::2].stack().values
        baseline_series = full_df.iloc[:, 1::2].stack().values
        baseline_series += np.random.normal(0, .001, baseline_series.shape) # Adding a little bit of noise to the baseline

        # Plot all points in black with alpha
        ax.scatter(real_series, baseline_series, color='k', s=5, alpha=.1)

        # Plot points with color density
        sample_size = 5000 if len(real_series) > 5000 else len(real_series)
        matrix = pd.DataFrame([real_series, baseline_series]).sample(sample_size, axis=1).as_matrix()
        dens = stats.gaussian_kde(matrix)
        dens_pt = dens(matrix)
        colours = make_colors(dens_pt, 'inferno', len(real_series) > 5000)
        ax.scatter(matrix[0], matrix[1], color=colours, s=5, alpha=.25)

    plt.show()
    return None


def make_colors(vals, cmap, log):
    if log:
        norm = LogNorm(vmin=vals.min(), vmax=vals.max()*5)
    else:
        norm = Normalize(vmin=vals.min(), vmax=vals.max())
    return [cm.ScalarMappable(norm=norm, cmap=cmap).to_rgba(val) for val in vals]
