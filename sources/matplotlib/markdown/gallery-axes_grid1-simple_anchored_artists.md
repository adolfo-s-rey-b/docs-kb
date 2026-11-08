[Skip to main content](https://matplotlib.org/stable/gallery/axes_grid1/simple_anchored_artists.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axes_grid1/simple_anchored_artists.html#sphx-glr-download-gallery-axes-grid1-simple-anchored-artists-py)
 to download the full example code.

Simple Anchored Artists[#](https://matplotlib.org/stable/gallery/axes_grid1/simple_anchored_artists.html#simple-anchored-artists "Link to this heading")

=========================================================================================================================================================

This example illustrates the use of the anchored helper classes found in [`matplotlib.offsetbox`](https://matplotlib.org/stable/api/offsetbox_api.html#module-matplotlib.offsetbox "matplotlib.offsetbox")
 and in [`mpl_toolkits.axes_grid1`](https://matplotlib.org/stable/api/toolkits/axes_grid1.html#module-mpl_toolkits.axes_grid1 "mpl_toolkits.axes_grid1")
. An implementation of a similar figure, but without use of the toolkit, can be found in [Anchored Artists](https://matplotlib.org/stable/gallery/misc/anchored_artists.html)
.

![simple anchored artists](https://matplotlib.org/stable/_images/sphx_glr_simple_anchored_artists_001_2_00x.png)

import matplotlib.pyplot as plt

def draw\_text([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
):
    """
    Draw two text-boxes, anchored by different corners to the upper-left
    corner of the figure.
    """
    from matplotlib.offsetbox import [AnchoredText](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredText "matplotlib.offsetbox.AnchoredText")
    at \= [AnchoredText](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredText "matplotlib.offsetbox.AnchoredText")
("Figure 1a",
                      loc\='upper left', prop\=dict(size\=8), frameon\=True,
                      )
    at.patch.set\_boxstyle("round,pad=0.,rounding\_size=0.2")
    [ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
(at)

    at2 \= [AnchoredText](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredText "matplotlib.offsetbox.AnchoredText")
("Figure 1(b)",
                       loc\='lower left', prop\=dict(size\=8), frameon\=True,
                       bbox\_to\_anchor\=(0., 1.),
                       bbox\_transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
                       )
    at2.patch.set\_boxstyle("round,pad=0.,rounding\_size=0.2")
    [ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
(at2)

def draw\_circle([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
):
    """
    Draw a circle in axis coordinates
    """
    from matplotlib.patches import [Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
    from mpl\_toolkits.axes\_grid1.anchored\_artists import [AnchoredDrawingArea](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea")
    ada \= [AnchoredDrawingArea](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea")
(20, 20, 0, 0,
                              loc\='upper right', pad\=0., frameon\=False)
    p \= [Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
((10, 10), 10)
    ada.da.add\_artist(p)
    [ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
(ada)

def draw\_sizebar([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
):
    """
    Draw a horizontal bar with length of 0.1 in data coordinates,
    with a fixed label underneath.
    """
    from mpl\_toolkits.axes\_grid1.anchored\_artists import [AnchoredSizeBar](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar "mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar")
    asb \= [AnchoredSizeBar](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar "mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar")
([ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
,
                          0.1,
                          r"1$^{\\prime}$",
                          loc\='lower center',
                          pad\=0.1, borderpad\=0.5, sep\=5,
                          frameon\=False)
    [ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
(asb)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.set\_aspect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
(1.)

draw\_text([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
draw\_circle([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
draw\_sizebar([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: simple_anchored_artists.ipynb`](https://matplotlib.org/stable/_downloads/60a275fed4e33280111ae513fc2e5c8d/simple_anchored_artists.ipynb)

[`Download Python source code: simple_anchored_artists.py`](https://matplotlib.org/stable/_downloads/7aa510be32a5c72df8a01d67a5890deb/simple_anchored_artists.py)

[`Download zipped: simple_anchored_artists.zip`](https://matplotlib.org/stable/_downloads/eeede8248af1d1b094f3bdac859e26c5/simple_anchored_artists.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)