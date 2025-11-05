"""
Example for a Matplotlib plot with the following features:
    - Histogram.
    - Transparency.
"""

__author__ = "Thomas Guillod"
__copyright__ = "Thomas Guillod - Dartmouth College"
__license__ = "Mozilla Public License Version 2.0"

import os
import numpy as np
import matplotlib.pyplot as plt
import utils_mpl

# ###########################################################
# Plot global parameters and define dummy data
# ###########################################################

# set global parameters
utils_mpl.set_global()

# create the output folder
os.makedirs("render", exist_ok=True)

# define dummy data
x = np.random.rayleigh(size=500)
y = np.random.normal(size=500)

# get the axis ticks
xticks = np.linspace(-2.0, +3.0, 6)
yticks = np.linspace(0.0, 150.0, 6)

# ###########################################################
# Definition of the line plot
# ###########################################################

# create a figure with a determined size
(fig, ax) = utils_mpl.get_fig(size=(3.5, 3.0), dpi=200)

# add the histograms
plt.hist(x, color="r", label="x", alpha=0.5)
plt.hist(y, color="g", label="y", alpha=0.5)

# set the x-axis limit and format
utils_mpl.set_x_axis(ax, bnd=xticks, add_offset=0.1)
utils_mpl.set_format(ax.xaxis, ticks=xticks, fmt="${x:+.1f}$")

# set the y-axis limit and format
utils_mpl.set_y_axis(ax, bnd=yticks, add_offset=0.0)
utils_mpl.set_format(ax.yaxis, ticks=yticks, fmt="${x:.0f}$")

# set the legend and labels
ax.set_axisbelow(True)
ax.legend(loc="upper right")
ax.set_xlabel("x-axis (unit)")
ax.set_ylabel("y-axis (unit)")
ax.set_title("Plot Title")

# set the grid
utils_mpl.set_grid(fig, ax, major=True, minor=False)

# save the plot for Inkscape
utils_mpl.save_svg(fig, "render/hyst.svg")

# ###########################################################
# Show the plots
# ###########################################################

# show the plot for inspection
plt.show()
