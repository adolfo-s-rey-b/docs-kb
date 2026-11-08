[Skip to main content](https://matplotlib.org/stable/gallery/axes_grid1/demo_edge_colorbar.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axes_grid1/demo_edge_colorbar.html#sphx-glr-download-gallery-axes-grid1-demo-edge-colorbar-py)
 to download the full example code.

Per-row or per-column colorbars[#](https://matplotlib.org/stable/gallery/axes_grid1/demo_edge_colorbar.html#per-row-or-per-column-colorbars "Link to this heading")

====================================================================================================================================================================

This example shows how to use one common colorbar for each row or column of an image grid.

![demo edge colorbar](https://matplotlib.org/stable/_images/sphx_glr_demo_edge_colorbar_001_2_00x.png)

import matplotlib.pyplot as plt

from matplotlib import cbook
from mpl\_toolkits.axes\_grid1 import [AxesGrid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")

def get\_demo\_image():
    z \= [cbook.get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
("axes\_grid/bivariate\_normal.npy")  \# 15x15 array
    return z, (\-3, 4, \-4, 3)

def demo\_bottom\_cbar([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
):
    """
    A grid of 2x2 images with a colorbar for each column.
    """
    grid \= [AxesGrid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, 121,  \# similar to subplot(121)
                    nrows\_ncols\=(2, 2),
                    axes\_pad\=0.10,
                    share\_all\=True,
                    label\_mode\="1",
                    cbar\_location\="bottom",
                    cbar\_mode\="edge",
                    cbar\_pad\=0.25,
                    cbar\_size\="15%",
                    direction\="column"
                    )

    Z, extent \= get\_demo\_image()
    cmaps \= \["autumn", "summer"\]
    for i in range(4):
        im \= grid\[i\].imshow(Z, extent\=extent, cmap\=cmaps\[i//2\])
        if i % 2:
            grid.cbar\_axes\[i//2\].colorbar(im)

    for cax in grid.cbar\_axes:
        cax.axis\[cax.orientation\].set\_label("Bar")

    \# This affects all Axes as share\_all = True.
    grid.axes\_llc.set\_xticks(\[\-2, 0, 2\])
    grid.axes\_llc.set\_yticks(\[\-2, 0, 2\])

def demo\_right\_cbar([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
):
    """
    A grid of 2x2 images. Each row has its own colorbar.
    """
    grid \= [AxesGrid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.ImageGrid")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, 122,  \# similar to subplot(122)
                    nrows\_ncols\=(2, 2),
                    axes\_pad\=0.10,
                    label\_mode\="1",
                    share\_all\=True,
                    cbar\_location\="right",
                    cbar\_mode\="edge",
                    cbar\_size\="7%",
                    cbar\_pad\="2%",
                    )
    Z, extent \= get\_demo\_image()
    cmaps \= \["spring", "winter"\]
    for i in range(4):
        im \= grid\[i\].imshow(Z, extent\=extent, cmap\=cmaps\[i//2\])
        if i % 2:
            grid.cbar\_axes\[i//2\].colorbar(im)

    for cax in grid.cbar\_axes:
        cax.axis\[cax.orientation\].set\_label('Foo')

    \# This affects all Axes because we set share\_all = True.
    grid.axes\_llc.set\_xticks(\[\-2, 0, 2\])
    grid.axes\_llc.set\_yticks(\[\-2, 0, 2\])

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()

demo\_bottom\_cbar([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
)
demo\_right\_cbar([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: demo_edge_colorbar.ipynb`](https://matplotlib.org/stable/_downloads/756a9dd7cf31f2e15bd35724d7a53ade/demo_edge_colorbar.ipynb)

[`Download Python source code: demo_edge_colorbar.py`](https://matplotlib.org/stable/_downloads/c58f7f66a7206520d8eef2c5a8a20d72/demo_edge_colorbar.py)

[`Download zipped: demo_edge_colorbar.zip`](https://matplotlib.org/stable/_downloads/9ac9f25ffafd4c4eeb8a8812d0d4ef12/demo_edge_colorbar.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)