"""
Example for a Matplotlib plot with the following features:
    - Logarithmic axis.
    - Custom axis ticks.
"""

__author__ = "Thomas Guillod"
__copyright__ = "Thomas Guillod - Dartmouth College"
__license__ = "Mozilla Public License Version 2.0"

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
import utils_mpl

# ###########################################################
# Plot global parameters and define dummy data
# ###########################################################

# set global parameters
utils_mpl.set_global()

# create the output folder
os.makedirs("render", exist_ok=True)

# define dummy data
data = np.loadtxt("plot_data/impedance.txt")

# get the axis ticks
xticks = np.power(10.0, np.linspace(3, 8, 6))
yticks = np.power(10.0, np.linspace(0, 5, 6))

# ###########################################################
# Definition of the line plot
# ###########################################################

# create a figure with a determined size
(fig, ax) = utils_mpl.get_fig(size=(3.5, 3.0), dpi=200)

# add reference curves
ax.axvspan(1e3, 4e5, facecolor="green", alpha=0.2)
ax.axvspan(4e5, 1e8, facecolor="orange", alpha=0.2)
ax.plot(data[:, 0], data[:, 1], "r", lw=1.5)

# get the axes transformations
ax.set_xscale("log")
ax.set_yscale("log")

# set the x-axis limit and format
utils_mpl.set_x_axis(ax, bnd=xticks, add_offset=0.0)
fmt = tkr.LogFormatterMathtext()
utils_mpl.set_format(ax.xaxis, ticks=xticks, fmt=fmt)

# # set the y-axis limit and format
utils_mpl.set_y_axis(ax, bnd=yticks, add_fact=1.0)
fmt = tkr.LogFormatterMathtext()
utils_mpl.set_format(ax.yaxis, ticks=yticks, fmt=fmt)

# set the legend and labels
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Impedance (Ohm)")
ax.set_title("Impedance")

# set the grid
utils_mpl.set_grid(fig, ax, major=True, minor=True)

# save the plot for Inkscape
utils_mpl.save_svg(fig, "render/meas_impedance.svg")

# ###########################################################
# Show the plots
# ###########################################################

# show the plot for inspection
plt.show()
