"""
Example for a Matplotlib plot with the waveform measurements.
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
data = np.loadtxt("plot_data/waveform.gz")
t_vec = data[:, 0]
I_vec = data[:, 1]
V_vec = data[:, 2]

# downsampling
t_vec = t_vec[::5]
I_vec = I_vec[::5]
V_vec = V_vec[::5]

# # get the axis ticks
xticks = np.linspace(-15, +15, 7)
yticks_voltage = np.linspace(-450, +450, 5)
yticks_current = np.linspace(-100, +100, 5)

# ###########################################################
# Definition of the line plot
# ###########################################################

# create a figure with a determined size
(fig, axb) = utils_mpl.get_fig(size=(3.5, 3.0), dpi=200)
axt = axb.twinx()

# add reference curves
axb.plot(1e6 * t_vec, 1e0 * V_vec, "r", lw=1.0)
axt.plot(1e6 * t_vec, 1e0 * I_vec, "g", lw=1.0)

# # set the x-axis limit and format
utils_mpl.set_x_axis(axb, bnd=xticks, margin=0.05, log=False)
utils_mpl.set_format(axb.xaxis, ticks=xticks, fmt="${x:+.0f}$")

# set the y-axis limit and format
utils_mpl.set_y_axis(axb, bnd=yticks_voltage, margin=0.1, log=False)
utils_mpl.set_format(axb.yaxis, ticks=yticks_voltage, fmt="${x:+.0f}$")
utils_mpl.set_y_axis(axt, bnd=yticks_current, margin=0.1, log=False)
utils_mpl.set_format(axt.yaxis, ticks=yticks_current, fmt="${x:+.0f}$")

# set the legend and labels
axb.set_xlabel("Time (us)")
axb.set_ylabel("Voltage (V)")
axt.set_ylabel("Current (A)")
axb.set_title("Waveform")

# set the grid
utils_mpl.set_grid(fig, axb, major=True, minor=True)

# save the plot for Inkscape
utils_mpl.save_svg(fig, "render/meas_waveform.svg")

# ###########################################################
# Show the plots
# ###########################################################

# show the plot for inspection
plt.show()
