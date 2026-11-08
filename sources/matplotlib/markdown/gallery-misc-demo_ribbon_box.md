[Skip to main content](https://matplotlib.org/stable/gallery/misc/demo_ribbon_box.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/misc/demo_ribbon_box.html#sphx-glr-download-gallery-misc-demo-ribbon-box-py)
 to download the full example code.

Ribbon box[#](https://matplotlib.org/stable/gallery/misc/demo_ribbon_box.html#ribbon-box "Link to this heading")

=================================================================================================================

![demo ribbon box](https://matplotlib.org/stable/_images/sphx_glr_demo_ribbon_box_001_2_00x.png)

from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cbook
from matplotlib import colors as mcolors
from matplotlib.image import [AxesImage](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
from matplotlib.transforms import Bbox, [BboxTransformTo](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
, [TransformedBbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")

class RibbonBox:

    \# Image.open reads this image as 8-bit; divide by 255 to convert to 0-1.
    original\_image \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
([Image.open](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open "PIL.Image.open")
(
        [cbook.get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
("Minduka\_Present\_Blue\_Pack.png"))) / 255
    cut\_location \= 70
    b\_and\_h \= original\_image\[:, :, 2:3\]
    color \= original\_image\[:, :, 2:3\] \- original\_image\[:, :, 0:1\]
    alpha \= original\_image\[:, :, 3:4\]
    nx \= original\_image.shape\[1\]

    def \_\_init\_\_(self, color):
        rgb \= [mcolors.to\_rgb](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_rgb.html#matplotlib.colors.to_rgb "matplotlib.colors.to_rgb")
(color)
        self.im \= [np.dstack](https://numpy.org/doc/stable/reference/generated/numpy.dstack.html#numpy.dstack "numpy.dstack")
(
            \[self.b\_and\_h \- self.color \* (1 \- [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")\
(rgb)), self.alpha\])

    def get\_stretched\_image(self, stretch\_factor):
        stretch\_factor \= max(stretch\_factor, 1)
        ny, nx, nch \= self.im.shape
        ny2 \= int(ny\*stretch\_factor)
        return [np.vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
(
            \[self.im\[:self.cut\_location\],\
             [np.broadcast\_to](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_to.html#numpy.broadcast_to "numpy.broadcast_to")\
(\
                 self.im\[self.cut\_location\], (ny2 \- ny, nx, nch)),\
             self.im\[self.cut\_location:\]\])

class RibbonBoxImage([AxesImage](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
):
    zorder \= 1

    def \_\_init\_\_(self, ax, bbox, color, \*, extent\=(0, 1, 0, 1), \*\*kwargs):
        super().\_\_init\_\_(ax, extent\=extent, \*\*kwargs)
        self.\_bbox \= bbox
        self.\_ribbonbox \= RibbonBox(color)
        self.set\_transform([BboxTransformTo](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
(bbox))

    def draw(self, renderer):
        stretch\_factor \= self.\_bbox.height / self.\_bbox.width

        ny \= int(stretch\_factor\*self.\_ribbonbox.nx)
        if self.get\_array() is None or self.get\_array().shape\[0\] != ny:
            arr \= self.\_ribbonbox.get\_stretched\_image(stretch\_factor)
            self.set\_array(arr)

        super().draw(renderer)

def main():
    fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

    years \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(2004, 2009)
    heights \= \[7900, 8100, 7900, 6900, 2800\]
    box\_colors \= \[\
        (0.8, 0.2, 0.2),\
        (0.2, 0.8, 0.2),\
        (0.2, 0.2, 0.8),\
        (0.7, 0.5, 0.8),\
        (0.3, 0.8, 0.7),\
    \]

    for year, h, bc in zip(years, heights, box\_colors):
        bbox0 \= [Bbox.from\_extents](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.from_extents "matplotlib.transforms.Bbox.from_extents")
(year \- 0.4, 0., year + 0.4, h)
        bbox \= [TransformedBbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")
(bbox0, ax.transData)
        ax.add\_artist([RibbonBoxImage](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
(ax, bbox, bc, interpolation\="bicubic"))
        ax.annotate(str(h), (year, h), va\="bottom", ha\="center")

    ax.set\_xlim(years\[0\] \- 0.5, years\[\-1\] + 0.5)
    ax.set\_ylim(0, 10000)

    background\_gradient \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((2, 2, 4))
    background\_gradient\[:, :, :3\] \= \[1, 1, 0\]
    background\_gradient\[:, :, 3\] \= \[\[0.1, 0.3\], \[0.3, 0.5\]\]  \# alpha channel
    ax.imshow(background\_gradient, interpolation\="bicubic", zorder\=0.1,
              extent\=(0, 1, 0, 1), transform\=ax.transAxes)

    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

main()

**Total running time of the script:** (0 minutes 1.244 seconds)

[`Download Jupyter notebook: demo_ribbon_box.ipynb`](https://matplotlib.org/stable/_downloads/fbc9867e285b8ab4c9399fe4a3a15829/demo_ribbon_box.ipynb)

[`Download Python source code: demo_ribbon_box.py`](https://matplotlib.org/stable/_downloads/c7b27332a2e53923edb7ffb5315d4fa3/demo_ribbon_box.py)

[`Download zipped: demo_ribbon_box.zip`](https://matplotlib.org/stable/_downloads/fd0034c22f2ecddd0c9099c9bc4c99a9/demo_ribbon_box.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)