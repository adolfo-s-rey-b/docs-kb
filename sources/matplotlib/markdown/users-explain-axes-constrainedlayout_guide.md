[Skip to main content](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#sphx-glr-download-users-explain-axes-constrainedlayout-guide-py)
 to download the full example code.

Constrained layout guide[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#constrained-layout-guide "Link to this heading")

===========================================================================================================================================================

Use _constrained layout_ to fit plots within your figure cleanly.

_Constrained layout_ automatically adjusts subplots so that decorations like tick labels, legends, and colorbars do not overlap, while still preserving the logical layout requested by the user.

_Constrained layout_ is similar to [Tight layout](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#tight-layout-guide)
, but is substantially more flexible. It handles colorbars placed on multiple Axes ([Placing colorbars](https://matplotlib.org/stable/users/explain/axes/colorbar_placement.html#colorbar-placement)
) nested layouts ([`subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
) and Axes that span rows or columns ([`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
), striving to align spines from Axes in the same row or column. In addition, [Compressed layout](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#compressed-layout)
 will try and move fixed aspect-ratio Axes closer together. These features are described in this document, as well as some [implementation details](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#cl-notes-on-algorithm)
 discussed at the end.

_Constrained layout_ typically needs to be activated before any Axes are added to a figure. Two ways of doing so are

*   using the respective argument to [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
    , [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
    , [`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
     e.g.:
    
    [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
    (layout\="constrained")
    
*   activate it via [rcParams](https://matplotlib.org/stable/users/explain/customizing.html#customizing-with-dynamic-rc-settings)
    , like:
    
    [plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
    \['figure.constrained\_layout.use'\] \= True
    

Those are described in detail throughout the following sections.

Warning

Calling [`tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
 will turn off _constrained layout_!

Simple example[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#simple-example "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

With the default Axes positioning, the axes title, axis labels, or tick labels can sometimes go outside the figure area, and thus get clipped.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.colors as mcolors
import matplotlib.gridspec as gridspec

[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['savefig.facecolor'\] \= "0.8"
[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['figure.figsize'\] \= 4.5, 4.
[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['figure.max\_open\_warning'\] \= 50

def example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, fontsize\=12, hide\_labels\=False):
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[1, 2\])

    [ax.locator\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.locator_params.html#matplotlib.axes.Axes.locator_params "matplotlib.axes.Axes.locator_params")
(nbins\=3)
    if hide\_labels:
        [ax.set\_xticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels")
(\[\])
        [ax.set\_yticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels")
(\[\])
    else:
        [ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('x-label', fontsize\=fontsize)
        [ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('y-label', fontsize\=fontsize)
        [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Title', fontsize\=fontsize)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(layout\=None)
example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, fontsize\=24)

![Title](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_001_2_00x.png)

To prevent this, the location of Axes needs to be adjusted. For subplots, this can be done manually by adjusting the subplot parameters using [`Figure.subplots_adjust`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
. However, specifying your figure with the `layout="constrained"` keyword argument will do the adjusting automatically.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(layout\="constrained")
example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, fontsize\=24)

![Title](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_002_2_00x.png)

When you have multiple subplots, often you see labels of different Axes overlapping each other.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, layout\=None)
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

![Title, Title, Title, Title](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_003_2_00x.png)

Specifying `layout="constrained"` in the call to `plt.subplots` causes the layout to be properly constrained.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, layout\="constrained")
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

![Title, Title, Title, Title](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_004_2_00x.png)

Colorbars[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#colorbars "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

If you create a colorbar with [`Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
, you need to make room for it. _Constrained layout_ does this automatically. Note that if you specify `use_gridspec=True` it will be ignored because this option is made for improving the layout via `tight_layout`.

Note

For the [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
 keyword arguments (`pc_kwargs`) we use a dictionary to keep the calls consistent across this document.

[arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(100).reshape((10, 10))
[norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
 \= [mcolors.Normalize](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
(vmin\=0., vmax\=100.)
\# see note above: this makes all pcolormesh calls consistent:
[pc\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {'rasterized': True, 'cmap': 'viridis', 'norm': [norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
}
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(4, 4), layout\="constrained")
[im](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= [ax.pcolormesh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \*\*[pc\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([im](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, shrink\=0.6)

![constrainedlayout guide](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_005_2_00x.png)

If you specify a list of Axes (or other iterable container) to the `ax` argument of `colorbar`, _constrained layout_ will take space from the specified Axes.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, figsize\=(4, 4), layout\="constrained")
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    [im](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= [ax.pcolormesh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \*\*[pc\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([im](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, shrink\=0.6)

![constrainedlayout guide](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_006_2_00x.png)

If you specify a list of Axes from inside a grid of Axes, the colorbar will steal space appropriately, and leave a gap, but all subplots will still be the same size.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(3, 3, figsize\=(4, 4), layout\="constrained")
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    [im](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= [ax.pcolormesh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \*\*[pc\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([im](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1:, 1\], shrink\=0.8)
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([im](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, \-1\], shrink\=0.6)

![constrainedlayout guide](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_007_2_00x.png)

Suptitle[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#suptitle "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

_Constrained layout_ can also make room for [`suptitle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, figsize\=(4, 4), layout\="constrained")
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    [im](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= [ax.pcolormesh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \*\*[pc\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([im](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, shrink\=0.6)
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Big Suptitle')

![Big Suptitle](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_008_2_00x.png)

Legends[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#legends "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

Legends can be placed outside of their parent axes. _Constrained layout_ is designed to handle this for [`Axes.legend()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
. However, _constrained layout_ does _not_ handle legends being created via [`Figure.legend()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html#matplotlib.figure.Figure.legend "matplotlib.figure.Figure.legend")
 (yet).

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(layout\="constrained")
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(10), label\='This is a plot')
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(loc\='center left', bbox\_to\_anchor\=(0.8, 0.5))

![constrainedlayout guide](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_009_2_00x.png)

However, this will steal space from a subplot layout:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(4, 2), layout\="constrained")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].plot([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(10))
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].plot([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(10), label\='This is a plot')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].legend(loc\='center left', bbox\_to\_anchor\=(0.8, 0.5))

![constrainedlayout guide](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_010_2_00x.png)

In order for a legend or other artist to _not_ steal space from the subplot layout, we can `leg.set_in_layout(False)`. Of course this can mean the legend ends up cropped, but can be useful if the plot is subsequently called with `fig.savefig('outname.png', bbox_inches='tight')`. Note, however, that the legend's `get_in_layout` status will have to be toggled again to make the saved file work, and we must manually trigger a draw if we want _constrained layout_ to adjust the size of the Axes before printing.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(4, 2), layout\="constrained")

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].plot([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(10))
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].plot([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(10), label\='This is a plot')
[leg](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].legend(loc\='center left', bbox\_to\_anchor\=(0.8, 0.5))
[leg.set\_in\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout")
(False)
\# trigger a draw so that constrained layout is executed once
\# before we turn it off when printing....
[fig.canvas.draw](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw "matplotlib.backend_bases.FigureCanvasBase.draw")
()
\# we want the legend included in the bbox\_inches='tight' calcs.
[leg.set\_in\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout")
(True)
\# we don't want the layout to change at this point.
[fig.set\_layout\_engine](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_layout_engine.html#matplotlib.figure.Figure.set_layout_engine "matplotlib.figure.Figure.set_layout_engine")
('none')
try:
    [fig.savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
('../../../doc/\_static/constrained\_layout\_1b.png',
                bbox\_inches\='tight', dpi\=100)
except FileNotFoundError:
    \# this allows the script to keep going if run interactively and
    \# the directory above doesn't exist
    pass

![constrainedlayout guide](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_011_2_00x.png)

The saved file looks like:

![../../../_images/constrained_layout_1b.png](https://matplotlib.org/stable/_images/constrained_layout_1b.png)

A better way to get around this awkwardness is to simply use the legend method provided by [`Figure.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html#matplotlib.figure.Figure.legend "matplotlib.figure.Figure.legend")
:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(4, 2), layout\="constrained")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].plot([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(10))
[lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].plot([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(10), label\='This is a plot')
[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[l.get\_label() for l in [lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\]
[leg](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 \= [fig.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html#matplotlib.figure.Figure.legend "matplotlib.figure.Figure.legend")
([lines](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, loc\='center left',
                 bbox\_to\_anchor\=(0.8, 0.5), bbox\_transform\=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].transAxes)
try:
    [fig.savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
('../../../doc/\_static/constrained\_layout\_2b.png',
                bbox\_inches\='tight', dpi\=100)
except FileNotFoundError:
    \# this allows the script to keep going if run interactively and
    \# the directory above doesn't exist
    pass

![constrainedlayout guide](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_012_2_00x.png)

The saved file looks like:

![../../../_images/constrained_layout_2b.png](https://matplotlib.org/stable/_images/constrained_layout_2b.png)

Padding and spacing[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#padding-and-spacing "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

Padding between Axes is controlled in the horizontal by _w\_pad_ and _wspace_, and vertical by _h\_pad_ and _hspace_. These can be edited via [`set`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.ConstrainedLayoutEngine.set "matplotlib.layout_engine.ConstrainedLayoutEngine.set")
. _w/h\_pad_ are the minimum space around the Axes in units of inches:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, layout\="constrained")
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, hide\_labels\=True)
[fig.get\_layout\_engine](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_layout_engine.html#matplotlib.figure.Figure.get_layout_engine "matplotlib.figure.Figure.get_layout_engine")
().set(w\_pad\=4 / 72, h\_pad\=4 / 72, hspace\=0,
                            wspace\=0)

![constrainedlayout guide](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_013_2_00x.png)

Spacing between subplots is further set by _wspace_ and _hspace_. These are specified as a fraction of the size of the subplot group as a whole. If these values are smaller than _w\_pad_ or _h\_pad_, then the fixed pads are used instead. Note in the below how the space at the edges doesn't change from the above, but the space between subplots does.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, layout\="constrained")
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, hide\_labels\=True)
[fig.get\_layout\_engine](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_layout_engine.html#matplotlib.figure.Figure.get_layout_engine "matplotlib.figure.Figure.get_layout_engine")
().set(w\_pad\=4 / 72, h\_pad\=4 / 72, hspace\=0.2,
                            wspace\=0.2)

![constrainedlayout guide](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_014_2_00x.png)

If there are more than two columns, the _wspace_ is shared between them, so here the wspace is divided in two, with a _wspace_ of 0.1 between each column:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 3, layout\="constrained")
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, hide\_labels\=True)
[fig.get\_layout\_engine](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_layout_engine.html#matplotlib.figure.Figure.get_layout_engine "matplotlib.figure.Figure.get_layout_engine")
().set(w\_pad\=4 / 72, h\_pad\=4 / 72, hspace\=0.2,
                            wspace\=0.2)

![constrainedlayout guide](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_015_2_00x.png)

GridSpecs also have optional _hspace_ and _wspace_ keyword arguments, that will be used instead of the pads set by _constrained layout_:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, layout\="constrained",
                        gridspec\_kw\={'wspace': 0.3, 'hspace': 0.2})
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, hide\_labels\=True)
\# this has no effect because the space set in the gridspec trumps the
\# space set in \*constrained layout\*.
[fig.get\_layout\_engine](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_layout_engine.html#matplotlib.figure.Figure.get_layout_engine "matplotlib.figure.Figure.get_layout_engine")
().set(w\_pad\=4 / 72, h\_pad\=4 / 72, hspace\=0.0,
                            wspace\=0.0)

![constrainedlayout guide](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_016_2_00x.png)

### Spacing with colorbars[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#spacing-with-colorbars "Link to this heading")

Colorbars are placed a distance _pad_ from their parent, where _pad_ is a fraction of the width of the parent(s). The spacing to the next subplot is then given by _w/hspace_.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, layout\="constrained")
[pads](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[0, 0.05, 0.1, 0.2\]
for [pad](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in zip([pads](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
):
    [pc](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= [ax.pcolormesh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \*\*[pc\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
    [fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([pc](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, shrink\=0.6, [pad](https://docs.python.org/3/library/functions.html#float "builtins.float")
\=[pad](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
    [ax.set\_xticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels")
(\[\])
    [ax.set\_yticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels")
(\[\])
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
(f'pad: {[pad](https://docs.python.org/3/library/functions.html#float "builtins.float")
}')
[fig.get\_layout\_engine](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_layout_engine.html#matplotlib.figure.Figure.get_layout_engine "matplotlib.figure.Figure.get_layout_engine")
().set(w\_pad\=2 / 72, h\_pad\=2 / 72, hspace\=0.2,
                            wspace\=0.2)

![pad: 0, pad: 0.05, pad: 0.1, pad: 0.2](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_017_2_00x.png)

rcParams[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#rcparams "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

There are five [rcParams](https://matplotlib.org/stable/users/explain/customizing.html#customizing-with-dynamic-rc-settings)
 that can be set, either in a script or in the `matplotlibrc` file. They all have the prefix `figure.constrained_layout`:

*   _use_: Whether to use _constrained layout_. Default is False
    
*   _w\_pad_, _h\_pad_: Padding around Axes objects. Float representing inches. Default is 3./72. inches (3 pts)
    
*   _wspace_, _hspace_: Space between subplot groups. Float representing a fraction of the subplot widths being separated. Default is 0.02.
    

[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['figure.constrained\_layout.use'\] \= True
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, figsize\=(3, 3))
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

![Title, Title, Title, Title](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_018_2_00x.png)

Use with GridSpec[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#use-with-gridspec "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

_Constrained layout_ is meant to be used with [`subplots()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
, [`subplot_mosaic()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
, or [`GridSpec()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 with [`add_subplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
.

Note that in what follows `layout="constrained"`

[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['figure.constrained\_layout.use'\] \= False
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained")

[gs1](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
 \= [gridspec.GridSpec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
(2, 1, figure\=[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
)
[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs1](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
\[0\])
[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs1](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
\[1\])

example\_plot([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

![Title, Title](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_019_2_00x.png)

More complicated gridspec layouts are possible. Note here we use the convenience functions [`add_gridspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_gridspec.html#matplotlib.figure.Figure.add_gridspec "matplotlib.figure.Figure.add_gridspec")
 and [`subgridspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec.subgridspec "matplotlib.gridspec.SubplotSpec.subgridspec")
.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained")

[gs0](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 \= [fig.add\_gridspec](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_gridspec.html#matplotlib.figure.Figure.add_gridspec "matplotlib.figure.Figure.add_gridspec")
(1, 2)

[gs1](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
 \= [gs0](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[0\].subgridspec(2, 1)
[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs1](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
\[0\])
[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs1](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
\[1\])

example\_plot([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

[gs2](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
 \= [gs0](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[1\].subgridspec(3, 1)

for [ss](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
 in [gs2](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
:
    [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([ss](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
)
    example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("")
    [ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
("")

[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
("x-label", fontsize\=12)

![Title, Title](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_020_2_00x.png)

Note that in the above the left and right columns don't have the same vertical extent. If we want the top and bottom of the two grids to line up then they need to be in the same gridspec. We need to make this figure larger as well in order for the Axes not to collapse to zero height:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(4, 6), layout\="constrained")

[gs0](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 \= [fig.add\_gridspec](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_gridspec.html#matplotlib.figure.Figure.add_gridspec "matplotlib.figure.Figure.add_gridspec")
(6, 2)

[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs0](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[:3, 0\])
[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs0](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[3:, 0\])

example\_plot([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs0](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[0:2, 1\])
example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, hide\_labels\=True)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs0](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[2:4, 1\])
example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, hide\_labels\=True)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs0](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[4:, 1\])
example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, hide\_labels\=True)
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Overlapping Gridspecs')

![Overlapping Gridspecs, Title, Title](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_021_2_00x.png)

This example uses two gridspecs to have the colorbar only pertain to one set of pcolors. Note how the left column is wider than the two right-hand columns because of this. Of course, if you wanted the subplots to be the same size you only needed one gridspec. Note that the same effect can be achieved using [`subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained")
[gs0](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 \= [fig.add\_gridspec](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_gridspec.html#matplotlib.figure.Figure.add_gridspec "matplotlib.figure.Figure.add_gridspec")
(1, 2, figure\=[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, width\_ratios\=\[1, 2\])
[gs\_left](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
 \= [gs0](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[0\].subgridspec(2, 1)
[gs\_right](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
 \= [gs0](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[1\].subgridspec(2, 2)

for [gs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 in [gs\_left](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
:
    [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
)
    example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= \[\]
for [gs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 in [gs\_right](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
:
    [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
)
    [pcm](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax.pcolormesh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \*\*[pc\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
    [ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('x-label')
    [ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('y-label')
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('title')
    [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 += \[[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
\]
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Nested plots using subgridspec')
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([pcm](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

![Nested plots using subgridspec, Title, Title, title, title, title, title](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_022_2_00x.png)

Rather than using subgridspecs, Matplotlib now provides [`subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
 which also work with _constrained layout_:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained")
[sfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [fig.subfigures](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
(1, 2, width\_ratios\=\[1, 2\])

[axs\_left](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [sfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].subplots(2, 1)
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs\_left.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

[axs\_right](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [sfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].subplots(2, 2)
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs\_right.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    [pcm](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax.pcolormesh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \*\*[pc\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
    [ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('x-label')
    [ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('y-label')
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('title')
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([pcm](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axs\_right](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Nested plots using subfigures')

![Nested plots using subfigures, Title, Title, title, title, title, title](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_023_2_00x.png)

Manually setting Axes positions[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#manually-setting-axes-positions "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There can be good reasons to manually set an Axes position. A manual call to [`set_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib.axes.Axes.set_position "matplotlib.axes.Axes.set_position")
 will set the Axes so _constrained layout_ has no effect on it anymore. (Note that _constrained layout_ still leaves the space for the Axes that is moved).

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, layout\="constrained")
example\_plot([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\], fontsize\=12)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_position(\[0.2, 0.2, 0.4, 0.4\])

![Title](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_024_2_00x.png)

Grids of fixed aspect-ratio Axes: "compressed" layout[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#grids-of-fixed-aspect-ratio-axes-compressed-layout "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_Constrained layout_ operates on the grid of "original" positions for Axes. However, when Axes have fixed aspect ratios, one side is usually made shorter, and leaves large gaps in the shortened direction. In the following, the Axes are square, but the figure quite wide so there is a horizontal gap:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, figsize\=(5, 3),
                        sharex\=True, sharey\=True, layout\="constrained")
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
("fixed-aspect plots, layout='constrained'")

![fixed-aspect plots, layout='constrained'](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_025_2_00x.png)

One obvious way of fixing this is to make the figure size more square, however, closing the gaps exactly requires trial and error. For simple grids of Axes we can use `layout="compressed"` to do the job for us:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, figsize\=(5, 3),
                        sharex\=True, sharey\=True, layout\='compressed')
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
("fixed-aspect plots, layout='compressed'")

![fixed-aspect plots, layout='compressed'](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_026_2_00x.png)

Compressed layout will also attempt to size colorbars to match the size of the fixed-aspect-ratio parent Axes as the figure is resized or the aspect ratio changes. In the following figure, the colorbar is taller than its parent Axes:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(layout\='constrained', figsize\=(3, 3))
[pcm](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(10, 10), cmap\='viridis')
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Colorbar with layout='constrained'", fontsize\='medium')
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([pcm](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

![Colorbar with layout='constrained'](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_027_2_00x.png)

Compressed layout ensures that the height of the colorbar matches the height of its parent Axes, maintaining a consistent appearance:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(layout\='compressed', figsize\=(3, 3))
[pcm](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(10, 10), cmap\='viridis')
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Colorbar with layout='compressed'", fontsize\='medium')
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([pcm](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

![Colorbar with layout='compressed'](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_028_2_00x.png)

If the Axes is zoomed in or out, or the figure is resized, the colorbar will dynamically resize to match the parent Axes. Whether this behavior is desired depends on the specific application:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(layout\='compressed', figsize\=(3, 3))
[pcm](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(10, 10), cmap\='viridis')
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\[4, 8\])
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Layout='compressed' with zoom", fontsize\='medium')
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([pcm](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

![Layout='compressed' with zoom](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_029_2_00x.png)

Manually turning off _constrained layout_[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#manually-turning-off-constrained-layout "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_Constrained layout_ usually adjusts the Axes positions on each draw of the figure. If you want to get the spacing provided by _constrained layout_ but not have it update, then do the initial draw and then call `fig.set_layout_engine('none')`. This is potentially useful for animations where the tick labels may change length.

Note that _constrained layout_ is turned off for `ZOOM` and `PAN` GUI events for the backends that use the toolbar. This prevents the Axes from changing position during zooming and panning.

Limitations[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#limitations "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

### Incompatible functions[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#incompatible-functions "Link to this heading")

_Constrained layout_ will work with [`pyplot.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
, but only if the number of rows and columns is the same for each call. The reason is that each call to [`pyplot.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
 will create a new [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 instance if the geometry is not the same, and _constrained layout_. So the following works fine:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained")

[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 2, 1)
[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 2, 3)
\# third Axes that spans both rows in second column:
[ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 2, (2, 4))

example\_plot([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
[plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
('Homogeneous nrows, ncols')

![Homogeneous nrows, ncols, Title, Title, Title](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_030_2_00x.png)

but the following leads to a poor layout:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained")

[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 2, 1)
[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 2, 3)
[ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(1, 2, 2)

example\_plot([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
example\_plot([ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
[plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
('Mixed nrows, ncols')

![Mixed nrows, ncols, Title, Title, Title](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_031_2_00x.png)

Similarly, [`subplot2grid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid "matplotlib.pyplot.subplot2grid")
 works with the same limitation that nrows and ncols cannot change for the layout to look good.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained")

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
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('subplot2grid')

![subplot2grid, Title, Title, Title, Title](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_032_2_00x.png)

### Other caveats[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#other-caveats "Link to this heading")

*   _Constrained layout_ only considers ticklabels, axis labels, titles, and legends. Thus, other artists may be clipped and also may overlap.
    
*   It assumes that the extra space needed for ticklabels, axis labels, and titles is independent of original location of Axes. This is often true, but there are rare cases where it is not.
    
*   There are small differences in how the backends handle rendering fonts, so the results will not be pixel-identical.
    
*   An artist using Axes coordinates that extend beyond the Axes boundary will result in unusual layouts when added to an Axes. This can be avoided by adding the artist directly to the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
     using [`add_artist()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_artist.html#matplotlib.figure.Figure.add_artist "matplotlib.figure.Figure.add_artist")
    . See [`ConnectionPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")
     for an example.
    

Debugging[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#debugging "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

_Constrained layout_ can fail in somewhat unexpected ways. Because it uses a constraint solver the solver can find solutions that are mathematically correct, but that aren't at all what the user wants. The usual failure mode is for all sizes to collapse to their smallest allowable value. If this happens, it is for one of two reasons:

1.  There was not enough room for the elements you were requesting to draw.
    
2.  There is a bug - in which case open an issue at [matplotlib/matplotlib#issues](https://github.com/matplotlib/matplotlib/issues)
    .
    

If there is a bug, please report with a self-contained example that does not require outside data or dependencies (other than numpy).

Notes on the algorithm[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#notes-on-the-algorithm "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

The algorithm for the constraint is relatively straightforward, but has some complexity due to the complex ways we can lay out a figure.

Layout in Matplotlib is carried out with gridspecs via the [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 class. A gridspec is a logical division of the figure into rows and columns, with the relative width of the Axes in those rows and columns set by _width\_ratios_ and _height\_ratios_.

In _constrained layout_, each gridspec gets a _layoutgrid_ associated with it. The _layoutgrid_ has a series of `left` and `right` variables for each column, and `bottom` and `top` variables for each row, and further it has a margin for each of left, right, bottom and top. In each row, the bottom/top margins are widened until all the decorators in that row are accommodated. Similarly, for columns and the left/right margins.

### Simple case: one Axes[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#simple-case-one-axes "Link to this heading")

For a single Axes the layout is straight forward. There is one parent layoutgrid for the figure consisting of one column and row, and a child layoutgrid for the gridspec that contains the Axes, again consisting of one row and column. Space is made for the "decorations" on each side of the Axes. In the code, this is accomplished by the entries in `do_constrained_layout()` like:

gridspec.\_layoutgrid\[0, 0\].edit\_margin\_min('left',
      \-bbox.x0 + pos.x0 + w\_pad)

where `bbox` is the tight bounding box of the Axes, and `pos` its position. Note how the four margins encompass the Axes decorations.

from matplotlib.\_layoutgrid import plot\_children

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(layout\="constrained")
example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, fontsize\=24)
plot\_children([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
)

![Title](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_033_2_00x.png)

### Simple case: two Axes[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#simple-case-two-axes "Link to this heading")

When there are multiple Axes they have their layouts bound in simple ways. In this example the left Axes has much larger decorations than the right, but they share a bottom margin, which is made large enough to accommodate the larger xlabel. Same with the shared top margin. The left and right margins are not shared, and hence are allowed to be different.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, layout\="constrained")
example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[0\], fontsize\=32)
example\_plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[1\], fontsize\=8)
plot\_children([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
)

![Title, Title](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_034_2_00x.png)

### Two Axes and colorbar[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#two-axes-and-colorbar "Link to this heading")

A colorbar is simply another item that expands the margin of the parent layoutgrid cell:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, layout\="constrained")
[im](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[0\].pcolormesh([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \*\*[pc\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([im](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[0\], shrink\=0.6)
[im](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[1\].pcolormesh([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \*\*[pc\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
plot\_children([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
)

![constrainedlayout guide](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_035_2_00x.png)

### Colorbar associated with a Gridspec[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#colorbar-associated-with-a-gridspec "Link to this heading")

If a colorbar belongs to more than one cell of the grid, then it makes a larger margin for each:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, layout\="constrained")
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    [im](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= [ax.pcolormesh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \*\*[pc\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([im](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, shrink\=0.6)
plot\_children([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
)

![constrainedlayout guide](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_036_2_00x.png)

### Uneven sized Axes[#](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#uneven-sized-axes "Link to this heading")

There are two ways to make Axes have an uneven size in a Gridspec layout, either by specifying them to cross Gridspecs rows or columns, or by specifying width and height ratios.

The first method is used here. Note that the middle `top` and `bottom` margins are not affected by the left-hand column. This is a conscious decision of the algorithm, and leads to the case where the two right-hand Axes have the same height, but it is not 1/2 the height of the left-hand Axes. This is consistent with how `gridspec` works without _constrained layout_.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained")
[gs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 \= [gridspec.GridSpec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
(2, 2, figure\=[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[:, 0\])
[im](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= [ax.pcolormesh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \*\*[pc\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[0, 1\])
[im](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= [ax.pcolormesh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \*\*[pc\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[1, 1\])
[im](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= [ax.pcolormesh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \*\*[pc\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
plot\_children([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
)

![constrainedlayout guide](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_037_2_00x.png)

One case that requires finessing is if margins do not have any artists constraining their width. In the case below, the right margin for column 0 and the left margin for column 3 have no margin artists to set their width, so we take the maximum width of the margin widths that do have artists. This makes all the Axes have the same size:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained")
[gs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 \= [fig.add\_gridspec](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_gridspec.html#matplotlib.figure.Figure.add_gridspec "matplotlib.figure.Figure.add_gridspec")
(2, 4)
[ax00](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[0, 0:2\])
[ax01](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[0, 2:\])
[ax10](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[1, 1:3\])
example\_plot([ax10](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, fontsize\=14)
plot\_children([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Title](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_038_2_00x.png)

**Total running time of the script:** (0 minutes 31.333 seconds)

[`Download Jupyter notebook: constrainedlayout_guide.ipynb`](https://matplotlib.org/stable/_downloads/d8fb94404027dee6079d090b146898f6/constrainedlayout_guide.ipynb)

[`Download Python source code: constrainedlayout_guide.py`](https://matplotlib.org/stable/_downloads/146e58e6a4cefef33f4b840761f89ef9/constrainedlayout_guide.py)

[`Download zipped: constrainedlayout_guide.zip`](https://matplotlib.org/stable/_downloads/6c977ac381a0ef4cf37b664777deefa1/constrainedlayout_guide.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page