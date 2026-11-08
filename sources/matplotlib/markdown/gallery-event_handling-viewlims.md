[Skip to main content](https://matplotlib.org/stable/gallery/event_handling/viewlims.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

Note

[Go to the end](https://matplotlib.org/stable/gallery/event_handling/viewlims.html#sphx-glr-download-gallery-event-handling-viewlims-py)
 to download the full example code.

Viewlims[#](https://matplotlib.org/stable/gallery/event_handling/viewlims.html#viewlims "Link to this heading")

================================================================================================================

Creates two identical panels. Zooming in on the right panel will show a rectangle in the first panel, denoting the zoomed region.

Note

This example exercises the interactive capabilities of Matplotlib, and this will not appear in the static documentation. Please run this code on your machine to see the interactivity.

You can copy and paste individual parts, or download the entire example using the link at the bottom of the page.

![Zoom here](https://matplotlib.org/stable/_images/sphx_glr_viewlims_001_2_00x.png)

import functools

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import [Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")

\# A class that will regenerate a fractal set as we zoom in, so that you
\# can actually see the increasing detail.  A box in the left panel will show
\# the area to which we are zoomed.
class MandelbrotDisplay:
    def \_\_init\_\_(self, h\=500, w\=500, niter\=50, radius\=2., power\=2):
        self.height \= h
        self.width \= w
        self.niter \= niter
        self.radius \= radius
        self.power \= power

    def compute\_image(self, xlim, ylim):
        self.x \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\*xlim, self.width)
        self.y \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\*ylim, self.height).reshape(\-1, 1)
        c \= self.x + 1.0j \* self.y
        threshold\_time \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((self.height, self.width))
        z \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(threshold\_time.shape, dtype\=complex)
        mask \= [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
(threshold\_time.shape, dtype\=bool)
        for i in range(self.niter):
            z\[mask\] \= z\[mask\]\*\*self.power + c\[mask\]
            mask \= ([np.abs](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(z) < self.radius)
            threshold\_time += mask
        return threshold\_time

    def ax\_update(self, ax):
        ax.set\_autoscale\_on(False)  \# Otherwise, infinite loop
        \# Get the number of points from the number of pixels in the window
        self.width, self.height \= ax.patch.get\_window\_extent().size.round().astype(int)
        \# Update the image object with our new data and extent
        ax.images\[\-1\].set(data\=self.compute\_image(ax.get\_xlim(), ax.get\_ylim()),
                          extent\=(\*ax.get\_xlim(), \*ax.get\_ylim()))
        ax.figure.canvas.draw\_idle()

md \= MandelbrotDisplay()

[fig1](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax\_full](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax\_zoom](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2)
[ax\_zoom.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
(\[\[0\]\], origin\="lower")  \# Empty initial image.
[ax\_zoom.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Zoom here")

[rect](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 \= [Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
(
    \[0, 0\], 0, 0, facecolor\="none", edgecolor\="black", linewidth\=1.0)
[ax\_full.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([rect](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
)

def update\_rect([rect](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
, ax):  \# Let the rectangle track the bounds of the zoom axes.
    xlo, xhi \= ax.get\_xlim()
    ylo, yhi \= ax.get\_ylim()
    [rect.set\_bounds](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_bounds "matplotlib.patches.Rectangle.set_bounds")
((xlo, ylo, xhi \- xlo, yhi \- ylo))
    ax.figure.canvas.draw\_idle()

\# Connect for changing the view limits.
[ax\_zoom.callbacks.connect](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry.connect "matplotlib.cbook.CallbackRegistry.connect")
("xlim\_changed", [functools.partial](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
(update\_rect, [rect](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
))
[ax\_zoom.callbacks.connect](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry.connect "matplotlib.cbook.CallbackRegistry.connect")
("ylim\_changed", [functools.partial](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
(update\_rect, [rect](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
))

[ax\_zoom.callbacks.connect](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry.connect "matplotlib.cbook.CallbackRegistry.connect")
("xlim\_changed", md.ax\_update)
[ax\_zoom.callbacks.connect](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry.connect "matplotlib.cbook.CallbackRegistry.connect")
("ylim\_changed", md.ax\_update)

\# Initialize: trigger image computation by setting view limits; set colormap limits;
\# copy image to full view.
[ax\_zoom.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(\-2, .5), ylim\=(\-1.25, 1.25))
[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax\_zoom](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.images\[0\]
[ax\_zoom](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.images\[0\].set(clim\=([im.get\_array](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ScalarMappable.get_array "matplotlib.colorizer._ScalarMappable.get_array")
().min(), [im.get\_array](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ScalarMappable.get_array "matplotlib.colorizer._ScalarMappable.get_array")
().max()))
[ax\_full.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([im.get\_array](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ScalarMappable.get_array "matplotlib.colorizer._ScalarMappable.get_array")
(), extent\=[im.get\_extent](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage.get_extent "matplotlib.image.AxesImage.get_extent")
(), origin\="lower")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: viewlims.ipynb`](https://matplotlib.org/stable/_downloads/fd881b23f437800cddc8578ef3d34d96/viewlims.ipynb)

[`Download Python source code: viewlims.py`](https://matplotlib.org/stable/_downloads/b6082016b560fa99854e3efaf1afb469/viewlims.py)

[`Download zipped: viewlims.zip`](https://matplotlib.org/stable/_downloads/eaf109b9907b26b096e53dbd900af60c/viewlims.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)