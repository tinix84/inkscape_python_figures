"""
Example for a Matplotlib plot with the following features:
    - Scatter plot
    - Colorbar

The vector scatter plot would create unreasonably large file.
Therefore, the plot is divided into two parts.
A vector plot with the axes, labels, ticks, legend, etc.
A raster plot with the scatter plot dots (payload).
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
x = np.random.rand(100000)
y = np.random.rand(100000)
z = np.random.rand(100000)

# define the colormap
cmap = "viridis"

# get the colormap and axis ticks
cticks = np.linspace(0.0, 1.0, 5)
xticks = np.linspace(0.0, 1.0, 5)
yticks = np.linspace(0.0, 1.0, 5)

# ###########################################################
# Definition of the vector plot
# ###########################################################

# create a figure with a determined size
(fig, ax) = utils_mpl.get_fig(size=(3.5, 3.0), dpi=200)

# dummy scatter plot
scr = ax.scatter(np.nan, np.nan, 1.0, 1.0, cmap=cmap)

# set the colorbar limit and format
cb = fig.colorbar(scr)
utils_mpl.set_cbar(scr, bnd=cticks, add_offset=0.1)
utils_mpl.set_format(cb.ax.yaxis, ticks=cticks, fmt="${x:.2f}$")

# set the x-axis limit and format
utils_mpl.set_x_axis(ax, bnd=xticks, add_offset=0.1)
utils_mpl.set_format(ax.xaxis, ticks=xticks, fmt="${x:.2f}$")

# set the y-axis limit and format
utils_mpl.set_y_axis(ax, bnd=yticks, add_offset=0.1)
utils_mpl.set_format(ax.yaxis, ticks=yticks, fmt="${x:.2f}$")

# set global properties
cb.set_label("c-axis (unit)")
ax.set_xlabel("x-axis (unit)")
ax.set_ylabel("y-axis (unit)")
ax.set_title("Plot Title")

# set the grid
utils_mpl.set_grid(fig, ax, major=True, minor=False)

# save the plot for Inkscape
utils_mpl.save_svg(fig, "render/cmap_vector.svg")

# ###########################################################
# Definition of the raster plot
# ###########################################################

# clone the axes parameters
(size, xlim, ylim) = utils_mpl.get_fig_clone(fig, ax)
clim = scr.get_clim()

# create a figure for the raster data
(fig, ax) = utils_mpl.get_fig(size=(3.5, 3.0), dpi=200)

# plot the data
scr = ax.scatter(x, y, c=z, s=8.0, cmap=cmap)

# clone the axes parameters
utils_mpl.set_fig_clone(fig, ax, size, xlim, ylim)
scr.set_clim(clim)

# save the plot for Inkscape
utils_mpl.save_png(fig, "render/cmap_raster.png", dpi=500)

# ###########################################################
# Show the plots
# ###########################################################

# show the plot for inspection
plt.show()
