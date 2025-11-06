"""
Collection of small utils to create figures with PyVista:
    - Setup nice default parameters.
    - Trim the output PNG files.
"""

__author__ = "Thomas Guillod"
__copyright__ = "Thomas Guillod - Dartmouth College"
__license__ = "Mozilla Public License Version 2.0"

import pyvista as pv
import PIL.Image as img


def set_global():
    """
    Set the global PyVista options.
    """

    pv.set_plot_theme("document")
    pv.global_theme.transparent_background = True
    pv.global_theme.show_scalar_bar = False
    pv.global_theme.show_vertices = False
    pv.global_theme.show_edges = False
    pv.render_points_as_spheres = True


def get_crop(filename, margin=0):
    """
    Function for removing the transparent border from images.
    The original file is overwritten.

    Parameters
    ----------
    filename : str
        Path of the filename to be cropped.
    margin : int
        Margin (in pixels) for the cropping.
    """

    # open the image
    input_img = img.open(filename)

    # get the bounding box and crop
    bbox = input_img.getbbox()
    image = input_img.crop(bbox)

    # get the new size
    (width, height) = image.size

    # create the new image
    output_img = img.new("RGBA", (width + 2 * margin, height + 2 * margin), (0, 0, 0, 0))

    # add the cropped image with the margin as offset
    output_img.paste(image, (margin, margin))

    # overwrite the original image
    output_img.save(filename)
