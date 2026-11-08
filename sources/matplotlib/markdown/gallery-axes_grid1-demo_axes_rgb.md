[Skip to main content](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_rgb.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_rgb.html#sphx-glr-download-gallery-axes-grid1-demo-axes-rgb-py)
 to download the full example code.

Show RGB channels using RGBAxes[#](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_rgb.html#show-rgb-channels-using-rgbaxes "Link to this heading")

===============================================================================================================================================================

[`RGBAxes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_rgb.RGBAxes.html#mpl_toolkits.axes_grid1.axes_rgb.RGBAxes "mpl_toolkits.axes_grid1.axes_rgb.RGBAxes")
 creates a layout of 4 Axes for displaying RGB channels: one large Axes for the RGB image and 3 smaller Axes for the R, G, B channels.

*   ![demo axes rgb](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_rgb_001_2_00x.png)
*   ![demo axes rgb](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_rgb_002_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cbook
from mpl\_toolkits.axes\_grid1.axes\_rgb import [RGBAxes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_rgb.RGBAxes.html#mpl_toolkits.axes_grid1.axes_rgb.RGBAxes "mpl_toolkits.axes_grid1.axes_rgb.RGBAxes")
, [make\_rgb\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_rgb.make_rgb_axes.html#mpl_toolkits.axes_grid1.axes_rgb.make_rgb_axes "mpl_toolkits.axes_grid1.axes_rgb.make_rgb_axes")

def get\_rgb():
    Z \= [cbook.get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
("axes\_grid/bivariate\_normal.npy")
    Z\[Z < 0\] \= 0.
    Z \= Z / Z.max()

    R \= Z\[:13, :13\]
    G \= Z\[2:, 2:\]
    B \= Z\[:13, 2:\]

    return R, G, B

def make\_cube(r, g, b):
    ny, nx \= r.shape
    R \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((ny, nx, 3))
    R\[:, :, 0\] \= r
    G \= [np.zeros\_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")
(R)
    G\[:, :, 1\] \= g
    B \= [np.zeros\_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")
(R)
    B\[:, :, 2\] \= b

    RGB \= R + G + B

    return R, G, B, RGB

def demo\_rgb1():
    fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
    ax \= [RGBAxes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_rgb.RGBAxes.html#mpl_toolkits.axes_grid1.axes_rgb.RGBAxes "mpl_toolkits.axes_grid1.axes_rgb.RGBAxes")
(fig, \[0.1, 0.1, 0.8, 0.8\], pad\=0.0)
    r, g, b \= get\_rgb()
    ax.imshow\_rgb(r, g, b)

def demo\_rgb2():
    fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
    ax\_r, ax\_g, ax\_b \= [make\_rgb\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_rgb.make_rgb_axes.html#mpl_toolkits.axes_grid1.axes_rgb.make_rgb_axes "mpl_toolkits.axes_grid1.axes_rgb.make_rgb_axes")
(ax, pad\=0.02)

    r, g, b \= get\_rgb()
    im\_r, im\_g, im\_b, im\_rgb \= make\_cube(r, g, b)
    ax.imshow(im\_rgb)
    ax\_r.imshow(im\_r)
    ax\_g.imshow(im\_g)
    ax\_b.imshow(im\_b)

    for ax in fig.axes:
        ax.tick\_params(direction\='in', color\='w')
        ax.spines\[:\].set\_color("w")

demo\_rgb1()
demo\_rgb2()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 1.138 seconds)

[`Download Jupyter notebook: demo_axes_rgb.ipynb`](https://matplotlib.org/stable/_downloads/c9fef393db074eeb1b3e493b4a4b8bee/demo_axes_rgb.ipynb)

[`Download Python source code: demo_axes_rgb.py`](https://matplotlib.org/stable/_downloads/d4f8e826c13bbb870ffee065e8625f5d/demo_axes_rgb.py)

[`Download zipped: demo_axes_rgb.zip`](https://matplotlib.org/stable/_downloads/27a208375a52671f733d4e531bd1d6b1/demo_axes_rgb.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)