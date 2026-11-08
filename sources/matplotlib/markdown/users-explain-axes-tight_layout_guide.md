[Skip to main content](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#sphx-glr-download-users-explain-axes-tight-layout-guide-py)
 to download the full example code.

Tight layout guide[#](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#tight-layout-guide "Link to this heading")

==========================================================================================================================================

How to use tight-layout to fit plots within your figure cleanly.

Tip

_tight\_layout_ was the first layout engine in Matplotlib. The more modern and more capable [Constrained Layout](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#constrainedlayout-guide)
 should typically be used instead.

_tight\_layout_ automatically adjusts subplot params so that the subplot(s) fits in to the figure area. This is an experimental feature and may not work for some cases. It only checks the extents of ticklabels, axis labels, and titles.

Simple example[#](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#simple-example "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

With the default Axes positioning, the axes title, axis labels, or tick labels can sometimes go outside the figure area, and thus get clipped.

import matplotlib.pyplot as plt
import numpy as np

[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['savefig.facecolor'\] \= "0.8"

def example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
, fontsize\=12):
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[1, 2\])

    [ax.locator\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.locator_params.html#matplotlib.axes.Axes.locator_params "matplotlib.axes.Axes.locator_params")
(nbins\=3)
    [ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('x-label', fontsize\=fontsize)
    [ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('y-label', fontsize\=fontsize)
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Title', fontsize\=fontsize)

[plt.close](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close")
('all')
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
, fontsize\=24)

![Title](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_001_2_00x.png)

To prevent this, the location of Axes needs to be adjusted. For subplots, this can be done manually by adjusting the subplot parameters using [`Figure.subplots_adjust`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
. [`Figure.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
 does this automatically.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
, fontsize\=24)
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

![Title](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_002_2_00x.png)

Note that [`matplotlib.pyplot.tight_layout()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
 will only adjust the subplot params when it is called. In order to perform this adjustment each time the figure is redrawn, you can call `fig.set_tight_layout(True)`, or, equivalently, set `[rcParams["figure.autolayout"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.autolayout#rcparam-figure-autolayout) ` (default: `False`) to `True`.

When you have multiple subplots, often you see labels of different Axes overlapping each other.

[plt.close](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close")
('all')

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, (([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
), ([ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax4](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, ncols\=2)
example\_plot([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax4](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

![Title, Title, Title, Title](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_003_2_00x.png)

[`tight_layout()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
 will also adjust spacing between subplots to minimize the overlaps.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, (([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
), ([ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax4](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, ncols\=2)
example\_plot([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax4](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

![Title, Title, Title, Title](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_004_2_00x.png)

[`tight_layout()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
 can take keyword arguments of _pad_, _w\_pad_ and _h\_pad_. These control the extra padding around the figure border and between subplots. The pads are specified in fraction of fontsize.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, (([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
), ([ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax4](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, ncols\=2)
example\_plot([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax4](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
(pad\=0.4, w\_pad\=0.5, h\_pad\=1.0)

![Title, Title, Title, Title](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_005_2_00x.png)

[`tight_layout()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
 will work even if the sizes of subplots are different as far as their grid specification is compatible. In the example below, _ax1_ and _ax2_ are subplots of a 2x2 grid, while _ax3_ is of a 1x2 grid.

[plt.close](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close")
('all')
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()

[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(221)
[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(223)
[ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(122)

example\_plot([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

![Title, Title, Title](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_006_2_00x.png)

It works with subplots created with [`subplot2grid()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid "matplotlib.pyplot.subplot2grid")
. In general, subplots created from the gridspec ([Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#arranging-axes)
) will work.

[plt.close](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close")
('all')
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()

[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplot2grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid "matplotlib.pyplot.subplot2grid")
((3, 3), (0, 0))
[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplot2grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid "matplotlib.pyplot.subplot2grid")
((3, 3), (0, 1), colspan\=2)
[ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplot2grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid "matplotlib.pyplot.subplot2grid")
((3, 3), (1, 0), colspan\=2, rowspan\=2)
[ax4](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplot2grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid "matplotlib.pyplot.subplot2grid")
((3, 3), (1, 2), rowspan\=2)

example\_plot([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax4](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

![Title, Title, Title, Title](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_007_2_00x.png)

Although not thoroughly tested, it seems to work for subplots with aspect != "auto" (e.g., Axes with images).

[arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(100).reshape((10, 10))

[plt.close](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close")
('all')
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(5, 4))

[ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
 \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
()
[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, interpolation\="none")

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

![tight layout guide](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_008_2_00x.png)

Caveats[#](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#caveats "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

*   [`tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
     considers all artists on the Axes by default. To remove an artist from the layout calculation you can call [`Artist.set_in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout")
    .
    
*   `tight_layout` assumes that the extra space needed for artists is independent of the original location of Axes. This is often true, but there are rare cases where it is not.
    
*   `pad=0` can clip some texts by a few pixels. This may be a bug or a limitation of the current algorithm, and it is not clear why it happens. Meanwhile, use of pad larger than 0.3 is recommended.
    
*   The algorithm of `tight_layout` does not necessarily converge, i.e. calling `tight_layout` multiple times can lead to slight variations in the layout between the calls.
    

Use with GridSpec[#](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#use-with-gridspec "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

GridSpec has its own [`GridSpec.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec.tight_layout "matplotlib.gridspec.GridSpec.tight_layout")
 method (the pyplot api [`pyplot.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
 also works).

import matplotlib.gridspec as gridspec

[plt.close](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close")
('all')
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()

[gs1](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 \= [gridspec.GridSpec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
(2, 1)
[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs1](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[0\])
[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs1](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[1\])

example\_plot([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

[gs1.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec.tight_layout "matplotlib.gridspec.GridSpec.tight_layout")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
)

![Title, Title](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_009_2_00x.png)

You may provide an optional _rect_ parameter, which specifies the bounding box that the subplots will be fit inside. The coordinates are in normalized figure coordinates and default to (0, 0, 1, 1) (the whole figure).

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()

[gs1](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 \= [gridspec.GridSpec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
(2, 1)
[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs1](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[0\])
[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs1](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[1\])

example\_plot([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

[gs1.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec.tight_layout "matplotlib.gridspec.GridSpec.tight_layout")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, rect\=\[0, 0, 0.5, 1.0\])

![Title, Title](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_010_2_00x.png)

However, we do not recommend that this be used to manually construct more complicated layouts, like having one GridSpec in the left and one in the right side of the figure. For these use cases, one should instead take advantage of [Nested Gridspecs](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_nested.html)
, or the [Figure subfigures](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html)
.

Legends and annotations[#](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#legends-and-annotations "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

Pre Matplotlib 2.2, legends and annotations were excluded from the bounding box calculations that decide the layout. Subsequently, these artists were added to the calculation, but sometimes it is undesirable to include them. For instance in this case it might be good to have the Axes shrink a bit to make room for the legend:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(4, 3))
[lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(range(10), label\='A simple plot')
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(bbox\_to\_anchor\=(0.7, 0.5), loc\='center left',)
[fig.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![tight layout guide](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_011_2_00x.png)

However, sometimes this is not desired (quite often when using `fig.savefig('outname.png', bbox_inches='tight')`). In order to remove the legend from the bounding box calculation, we simply set its bounding `leg.set_in_layout(False)` and the legend will be ignored.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(4, 3))
[lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(range(10), label\='B simple plot')
[leg](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 \= [ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(bbox\_to\_anchor\=(0.7, 0.5), loc\='center left',)
[leg.set\_in\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout")
(False)
[fig.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![tight layout guide](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_012_2_00x.png)

Use with AxesGrid1[#](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#use-with-axesgrid1 "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

Limited support for [`mpl_toolkits.axes_grid1`](https://matplotlib.org/stable/api/toolkits/axes_grid1.html#module-mpl_toolkits.axes_grid1 "mpl_toolkits.axes_grid1")
 is provided.

from mpl\_toolkits.axes\_grid1 import [Grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid "mpl_toolkits.axes_grid1.Grid")

[plt.close](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close")
('all')
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid "mpl_toolkits.axes_grid1.Grid")
 \= [Grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid "mpl_toolkits.axes_grid1.Grid")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, rect\=111, nrows\_ncols\=(2, 2),
            axes\_pad\=0.25, label\_mode\='L',
            )

for [ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
 in [grid](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.Grid.html#mpl_toolkits.axes_grid1.axes_grid.Grid "mpl_toolkits.axes_grid1.Grid")
:
    example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
)
[ax.title.set\_visible](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible")
(False)

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

![Title, Title, Title, Title](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_013_2_00x.png)

Colorbar[#](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#colorbar "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

If you create a colorbar with [`Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
, the created colorbar is drawn in a Subplot as long as the parent Axes is also a Subplot, so [`Figure.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
 will work.

[plt.close](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close")
('all')
[arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(100).reshape((10, 10))
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(4, 4))
[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, interpolation\="none")

[plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
)

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

![tight layout guide](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_014_2_00x.png)

Another option is to use the AxesGrid1 toolkit to explicitly create an Axes for the colorbar.

from mpl\_toolkits.axes\_grid1 import make\_axes\_locatable

[plt.close](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close")
('all')
[arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(100).reshape((10, 10))
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(4, 4))
[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, interpolation\="none")

[divider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider "mpl_toolkits.axes_grid1.axes_divider.AxesDivider")
 \= make\_axes\_locatable([plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
())
[cax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [divider.append\_axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider.append_axes "mpl_toolkits.axes_grid1.axes_divider.AxesDivider.append_axes")
("right", "5%", pad\="3%")
[plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [cax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[cax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

![tight layout guide](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_015_2_00x.png)

**Total running time of the script:** (0 minutes 9.082 seconds)

[`Download Jupyter notebook: tight_layout_guide.ipynb`](https://matplotlib.org/stable/_downloads/67637a15e988705b11dd468352a88a46/tight_layout_guide.ipynb)

[`Download Python source code: tight_layout_guide.py`](https://matplotlib.org/stable/_downloads/62805330204ab5e346c3479bd0886ba1/tight_layout_guide.py)

[`Download zipped: tight_layout_guide.zip`](https://matplotlib.org/stable/_downloads/ca09e05e9d7a01f3de38988b922f9dec/tight_layout_guide.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page