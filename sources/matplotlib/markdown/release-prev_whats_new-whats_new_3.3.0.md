[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#main-content)

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
    

[What's new in Matplotlib 3.3.0 (Jul 16, 2020)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id1)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#what-s-new-in-matplotlib-3-3-0-jul-16-2020 "Link to this heading")

================================================================================================================================================================================================================================================================================

For a list of all of the issues and pull requests since the last revision, see the [GitHub statistics for 3.11.2 (Sep 10, 2026)](https://matplotlib.org/stable/release/github_stats.html#github-stats)
.

[Figure and Axes creation / management](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id2)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#figure-and-axes-creation-management "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Provisional API for composing semantic axes layouts from text or nested lists](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id3)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#provisional-api-for-composing-semantic-axes-layouts-from-text-or-nested-lists "Link to this heading")

The [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 class has a provisional method to generate complex grids of named [`axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 based on nested list input or ASCII art:

axd \= plt.figure(constrained\_layout\=True).subplot\_mosaic(
    \[\['.', 'histx'\],\
     \['histy', 'scat'\]\]
)
for k, ax in axd.items():
    ax.text(0.5, 0.5, k,
            ha\='center', va\='center', fontsize\=36,
            color\='darkgrey')

([`Source code`](https://matplotlib.org/stable/_downloads/b011b48c0b74a5b7626a04e0cc5b49e8/whats_new_3-3-0-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/05bc782a223cd6d577933ddbbf97a0a3/whats_new_3-3-0-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/47977594cfa7f487f22ec2ffd8cefb3e/whats_new_3-3-0-1.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-1.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-1.2x.png)

or as a string (with single-character Axes labels):

axd \= plt.figure(constrained\_layout\=True).subplot\_mosaic(
    """
    TTE
    L.E
    """)
for k, ax in axd.items():
    ax.text(0.5, 0.5, k,
            ha\='center', va\='center', fontsize\=36,
            color\='darkgrey')

([`Source code`](https://matplotlib.org/stable/_downloads/a4708de553f1167697c19ef1deccd7e7/whats_new_3-3-0-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/d0eb52067c78ff05f9a09fad45cee1ca/whats_new_3-3-0-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/e92eeee2591eed255f3f6ccff4e6720c/whats_new_3-3-0-2.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-2.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-2.2x.png)

See [Complex and semantic figure composition (subplot\_mosaic)](https://matplotlib.org/stable/users/explain/axes/mosaic.html#mosaic)
 for more details and examples.

### [`GridSpec.subplots()`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id4)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#gridspec-subplots "Link to this heading")

The [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 class gained a [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#matplotlib.gridspec.GridSpecBase.subplots "matplotlib.gridspec.GridSpecBase.subplots")
 method, so that one can write

fig.add\_gridspec(2, 2, height\_ratios\=\[3, 1\]).subplots()

as an alternative to

fig.subplots(2, 2, gridspec\_kw\={"height\_ratios": \[3, 1\]})

### [New `Axes.sharex`, `Axes.sharey` methods](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id5)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#new-axes-sharex-axes-sharey-methods "Link to this heading")

These new methods allow sharing axes _immediately_ after creating them. Note that behavior is indeterminate if axes are not shared immediately after creation.

For example, they can be used to selectively link some axes created all together using [`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
:

fig \= plt.figure(constrained\_layout\=True)
axd \= fig.subplot\_mosaic(\[\['.', 'histx'\], \['histy', 'scat'\]\],
                         gridspec\_kw\={'width\_ratios': \[1, 7\],
                                      'height\_ratios': \[2, 7\]})

axd\['histx'\].sharex(axd\['scat'\])
axd\['histy'\].sharey(axd\['scat'\])

([`Source code`](https://matplotlib.org/stable/_downloads/5d84abc4aa7ca0587081e19fa3913031/whats_new_3-3-0-3.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/052437384312cb7c3e74c8dfd26727a8/whats_new_3-3-0-3.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/400146466c63b157c2da85e96a63d04c/whats_new_3-3-0-3.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-3.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-3.2x.png)

### [tight\_layout now supports suptitle](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id6)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#tight-layout-now-supports-suptitle "Link to this heading")

Previous versions did not consider [`Figure.suptitle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
, so it may overlap with other artists after calling [`tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
:

([`Source code`](https://matplotlib.org/stable/_downloads/9494ef56bb99cd77b2b0e5fb4a40b731/whats_new_3-3-0-4.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/d0c04018e869d09b8f1a9cab4706c4d8/whats_new_3-3-0-4.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/d53643ff8747d33d5e0ffebd42cb5cc2/whats_new_3-3-0-4.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-4.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-4.2x.png)

From now on, the `suptitle` will be considered:

([`Source code`](https://matplotlib.org/stable/_downloads/e4f749b279901dfe7542de0c21a101b0/whats_new_3-3-0-5.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/f74be3abe2ac66d0944e0784c2177555/whats_new_3-3-0-5.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/094fa51111eaef3f2c7191d2e48e3e72/whats_new_3-3-0-5.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-5.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-5.2x.png)

### [Setting axes box aspect](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id7)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#setting-axes-box-aspect "Link to this heading")

It is now possible to set the aspect of an axes box directly via [`set_box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect")
. The box aspect is the ratio between axes height and axes width in physical units, independent of the data limits. This is useful to, e.g., produce a square plot, independent of the data it contains, or to have a non-image plot with the same axes dimensions next to an image plot with fixed (data-)aspect.

For use cases check out the [Axes box aspect](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_box_aspect.html)
 example.

[Colors and colormaps](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id8)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#colors-and-colormaps "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Turbo colormap](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id9)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#turbo-colormap "Link to this heading")

Turbo is an improved rainbow colormap for visualization, created by the Google AI team for computer vision and machine learning. Its purpose is to display depth and disparity data. Please see the [Google AI Blog](https://ai.googleblog.com/2019/08/turbo-improved-rainbow-colormap-for.html)
 for further details.

([`Source code`](https://matplotlib.org/stable/_downloads/301de1d2ca6c6cca257061aac2d1d45e/whats_new_3-3-0-6.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/6eb95cf7194ad2ef9cd8c2c8b29c80be/whats_new_3-3-0-6.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/b2d1600ee09ab827714c73f1ca03a569/whats_new_3-3-0-6.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-6.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-6.2x.png)

### [`colors.BoundaryNorm` supports _extend_ keyword argument](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id10)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#colors-boundarynorm-supports-extend-keyword-argument "Link to this heading")

[`BoundaryNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
 now has an _extend_ keyword argument, analogous to _extend_ in [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
. When set to 'both', 'min', or 'max', it maps the corresponding out-of-range values to [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
 lookup-table indices near the appropriate ends of their range so that the colors for out-of range values are adjacent to, but distinct from, their in-range neighbors. The colorbar inherits the _extend_ argument from the norm, so with `extend='both'`, for example, the colorbar will have triangular extensions for out-of-range values with colors that differ from adjacent in-range colors.

([`Source code`](https://matplotlib.org/stable/_downloads/9223513407ed8bdc1bccea1640e49224/whats_new_3-3-0-7.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/388102fc6adc6ddfb25466de1881d841/whats_new_3-3-0-7.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/808efa1a1a47e8f67b58ff45c86d7e14/whats_new_3-3-0-7.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-7.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-7.2x.png)

### [Text color for legend labels](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id11)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#text-color-for-legend-labels "Link to this heading")

The text color of legend labels can now be set by passing a parameter `labelcolor` to [`legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
. The `labelcolor` keyword can be:

*   A single color (either a string or RGBA tuple), which adjusts the text color of all the labels.
    
*   A list or tuple, allowing the text color of each label to be set individually.
    
*   `linecolor`, which sets the text color of each label to match the corresponding line color.
    
*   `markerfacecolor`, which sets the text color of each label to match the corresponding marker face color.
    
*   `markeredgecolor`, which sets the text color of each label to match the corresponding marker edge color.
    

([`Source code`](https://matplotlib.org/stable/_downloads/98a52b3d954f6701f6c477128a97b7d0/whats_new_3-3-0-8.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/a8cd49ae20412f1b4f0a4fe25eb78295/whats_new_3-3-0-8.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/e0e3773d64aecceb11a0aa8d7a09cd04/whats_new_3-3-0-8.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-8.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-8.2x.png)

### [Pcolor and Pcolormesh now accept `shading='nearest'` and `'auto'`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id12)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#pcolor-and-pcolormesh-now-accept-shading-nearest-and-auto "Link to this heading")

Previously [`axes.Axes.pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor")
 and [`axes.Axes.pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
 handled the situation where _x_ and _y_ have the same (respective) size as _C_ by dropping the last row and column of _C_, and _x_ and _y_ are regarded as the edges of the remaining rows and columns in _C_. However, many users want _x_ and _y_ centered on the rows and columns of _C_.

To accommodate this, `shading='nearest'` and `shading='auto'` are new allowed strings for the _shading_ keyword argument. `'nearest'` will center the color on _x_ and _y_ if _x_ and _y_ have the same dimensions as _C_ (otherwise an error will be thrown). `shading='auto'` will choose 'flat' or 'nearest' based on the size of _X_, _Y_, _C_.

If `shading='flat'` then _X_, and _Y_ should have dimensions one larger than _C_. If _X_ and _Y_ have the same dimensions as _C_, then the previous behavior is used and the last row and column of _C_ are dropped, and a DeprecationWarning is emitted.

Users can also specify this by the new `[rcParams["pcolor.shading"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=pcolor.shading#rcparam-pcolor-shading) ` (default: `'auto'`) in their `.matplotlibrc` or via [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
.

See [pcolormesh](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolormesh_grids.html)
 for examples.

[Titles, ticks, and labels](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id13)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#titles-ticks-and-labels "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Align labels to Axes edges](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id14)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#align-labels-to-axes-edges "Link to this heading")

[`set_xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
, [`set_ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
 and `ColorbarBase.set_label` support a parameter `loc` for simplified positioning. For the xlabel, the supported values are 'left', 'center', or 'right'. For the ylabel, the supported values are 'bottom', 'center', or 'top'.

The default is controlled via `[rcParams["xaxis.labellocation"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xaxis.labellocation#rcparam-xaxis-labellocation) ` (default: `'center'`) and `[rcParams["yaxis.labellocation"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=yaxis.labellocation#rcparam-yaxis-labellocation) ` (default: `'center'`); the Colorbar label takes the rcParam based on its orientation.

([`Source code`](https://matplotlib.org/stable/_downloads/5e0049866ca6c2163813ec2ad19d0781/whats_new_3-3-0-9.py)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-9_00.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-9_00.2x.png)

([`2x.png`](https://matplotlib.org/stable/_downloads/9812bcca4623d04ce765e7d1a965452e/whats_new_3-3-0-9_00.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/1fcda19729a6545bd094c6fd4263e5c4/whats_new_3-3-0-9_00.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-9_01.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-9_01.2x.png)

([`2x.png`](https://matplotlib.org/stable/_downloads/40e5d1e053e48fc50846a38da74117ea/whats_new_3-3-0-9_01.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/df789cd5c2172c0d61d887db0e0160ac/whats_new_3-3-0-9_01.png)
)

### [Allow tick formatters to be set with str or function inputs](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id15)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#allow-tick-formatters-to-be-set-with-str-or-function-inputs "Link to this heading")

[`set_major_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
 and [`set_minor_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_formatter.html#matplotlib.axis.Axis.set_minor_formatter "matplotlib.axis.Axis.set_minor_formatter")
 now accept [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 or function inputs in addition to [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
 instances. For a [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 a [`StrMethodFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.StrMethodFormatter "matplotlib.ticker.StrMethodFormatter")
 is automatically generated and used. For a function a [`FuncFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter")
 is automatically generated and used. In other words,

ax.xaxis.set\_major\_formatter('{x} km')
ax.xaxis.set\_minor\_formatter(lambda x, pos: str(x\-5))

are shortcuts for:

import matplotlib.ticker as mticker

ax.xaxis.set\_major\_formatter(mticker.StrMethodFormatter('{x} km'))
ax.xaxis.set\_minor\_formatter(
    mticker.FuncFormatter(lambda x, pos: str(x\-5))

([`Source code`](https://matplotlib.org/stable/_downloads/e8e08167ca67120fd847d6952bbe126d/whats_new_3-3-0-10.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/69059d9f7a76c7645886495c51667709/whats_new_3-3-0-10.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/df0afa7c0716d366e77143e04e04459f/whats_new_3-3-0-10.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-10.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-10.2x.png)

### [`Axes.set_title` gains a _y_ keyword argument to control auto positioning](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id16)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#axes-set-title-gains-a-y-keyword-argument-to-control-auto-positioning "Link to this heading")

[`set_title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
 tries to auto-position the title to avoid any decorators on the top x-axis. This is not always desirable so now _y_ is an explicit keyword argument of [`set_title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
. It defaults to _None_ which means to use auto-positioning. If a value is supplied (i.e. the pre-3.0 default was `y=1.0`) then auto-positioning is turned off. This can also be set with the new rcParameter `[rcParams["axes.titley"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.titley#rcparam-axes-titley) ` (default: `None`).

([`Source code`](https://matplotlib.org/stable/_downloads/e60490ea54758e2c243e9a12b2b68405/whats_new_3-3-0-11.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/5e28f05bb27ea4d0f0ce924a2ee70546/whats_new_3-3-0-11.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/f80d889d43b7ce70625fa316f1366b18/whats_new_3-3-0-11.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-11.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-11.2x.png)

### [Offset text is now set to the top when using `axis.tick_top()`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id17)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#offset-text-is-now-set-to-the-top-when-using-axis-tick-top "Link to this heading")

Solves the issue that the power indicator (e.g., 1e4) stayed on the bottom, even if the ticks were on the top.

### [Set zorder of contour labels](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id18)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#set-zorder-of-contour-labels "Link to this heading")

[`clabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.clabel.html#matplotlib.axes.Axes.clabel "matplotlib.axes.Axes.clabel")
 now accepts a _zorder_ keyword argument making it easier to set the _zorder_ of contour labels. If not specified, the default _zorder_ of clabels used to always be 3 (i.e. the default _zorder_ of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
) irrespective of the _zorder_ passed to [`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
/[`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
. The new default _zorder_ for clabels has been changed to (`2 + zorder` passed to [`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
 / [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
).

[Other changes](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id19)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#other-changes "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [New `Axes.axline` method](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id20)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#new-axes-axline-method "Link to this heading")

A new [`axline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axline.html#matplotlib.axes.Axes.axline "matplotlib.axes.Axes.axline")
 method has been added to draw infinitely long lines that pass through two points.

fig, ax \= plt.subplots()

ax.axline((.1, .1), slope\=5, color\='C0', label\='by slope')
ax.axline((.1, .2), (.8, .7), color\='C3', label\='by points')

ax.legend()

([`Source code`](https://matplotlib.org/stable/_downloads/1cb1447185d07d48b76d5e005ec06804/whats_new_3-3-0-12.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/f8724256c0cab135457fcd7702f6f1af/whats_new_3-3-0-12.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/a910db1103b42a1176a3e977d8946457/whats_new_3-3-0-12.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-12.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-12.2x.png)

### [`imshow` now coerces 3D arrays with depth 1 to 2D](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id21)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#imshow-now-coerces-3d-arrays-with-depth-1-to-2d "Link to this heading")

Starting from this version arrays of size MxNx1 will be coerced into MxN for displaying. This means commands like `plt.imshow(np.random.rand(3, 3, 1))` will no longer return an error message that the image shape is invalid.

### [Better control of `Axes.pie` normalization](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id22)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#better-control-of-axes-pie-normalization "Link to this heading")

Previously, [`Axes.pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
 would normalize its input _x_ if `sum(x) > 1`, but would do nothing if the sum were less than 1. This can be confusing, so an explicit keyword argument _normalize_ has been added. By default, the old behavior is preserved.

By passing _normalize_, one can explicitly control whether any rescaling takes place or whether partial pies should be created. If normalization is disabled, and `sum(x) > 1`, then an error is raised.

([`Source code`](https://matplotlib.org/stable/_downloads/f6bbe9cff87cab9bd930822a704b4020/whats_new_3-3-0-13.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/56fc68a6a7e9ef1a00708654a0590183/whats_new_3-3-0-13.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/1c6d11b3eb85b8eeaf0c253bf6c5fdb0/whats_new_3-3-0-13.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-13.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-13.2x.png)

### [Dates use a modern epoch](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id23)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#dates-use-a-modern-epoch "Link to this heading")

Matplotlib converts dates to days since an epoch using [`dates.date2num`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.date2num "matplotlib.dates.date2num")
 (via [`matplotlib.units`](https://matplotlib.org/stable/api/units_api.html#module-matplotlib.units "matplotlib.units")
). Previously, an epoch of `0000-12-31T00:00:00` was used so that `0001-01-01` was converted to 1.0. An epoch so distant in the past meant that a modern date was not able to preserve microseconds because 2000 years times the 2^(-52) resolution of a 64-bit float gives 14 microseconds.

Here we change the default epoch to the more reasonable UNIX default of `1970-01-01T00:00:00` which for a modern date has 0.35 microsecond resolution. (Finer resolution is not possible because we rely on [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")
 for the date locators). Access to the epoch is provided by [`get_epoch`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.get_epoch "matplotlib.dates.get_epoch")
, and there is a new `[rcParams["date.epoch"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=date.epoch#rcparam-date-epoch) ` (default: `'1970-01-01T00:00:00'`) rcParam. The user may also call [`set_epoch`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.set_epoch "matplotlib.dates.set_epoch")
, but it must be set _before_ any date conversion or plotting is used.

If you have data stored as ordinal floats in the old epoch, you can convert them to the new ordinal using the following formula:

new\_ordinal \= old\_ordinal + mdates.date2num(np.datetime64('0000-12-31'))

### [Lines now accept `MarkerStyle` instances as input](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id24)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#lines-now-accept-markerstyle-instances-as-input "Link to this heading")

Similar to [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
, [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
 and [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 now accept [`MarkerStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
 instances as input for the _marker_ parameter:

plt.plot(..., marker\=matplotlib.markers.MarkerStyle("D"))

[Fonts](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id25)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#fonts "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Simple syntax to select fonts by absolute path](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id26)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#simple-syntax-to-select-fonts-by-absolute-path "Link to this heading")

Fonts can now be selected by passing an absolute [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")
 to the _font_ keyword argument of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
.

### [Improved font weight detection](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id27)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#improved-font-weight-detection "Link to this heading")

Matplotlib is now better able to determine the weight of fonts from their metadata, allowing to differentiate between fonts within the same family more accurately.

[rcParams improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id28)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#rcparams-improvements "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [`matplotlib.rc_context` can be used as a decorator](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id29)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#matplotlib-rc-context-can-be-used-as-a-decorator "Link to this heading")

[`matplotlib.rc_context`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_context "matplotlib.rc_context")
 can now be used as a decorator (technically, it is now implemented as a [`contextlib.contextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager "(in Python v3.14)")
), e.g.,

@rc\_context({"lines.linewidth": 2})
def some\_function(...):
    ...

### [rcParams for controlling default "raise window" behavior](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id30)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#rcparams-for-controlling-default-raise-window-behavior "Link to this heading")

The new config option `[rcParams["figure.raise_window"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.raise_window#rcparam-figure-raise-window) ` (default: `True`) allows disabling of the raising of the plot window when calling [`show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
 or [`pause`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pause.html#matplotlib.pyplot.pause "matplotlib.pyplot.pause")
. The `MacOSX` backend is currently not supported.

### [Add generalized `mathtext.fallback` to rcParams](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id31)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#add-generalized-mathtext-fallback-to-rcparams "Link to this heading")

New `[rcParams["mathtext.fallback"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=mathtext.fallback#rcparam-mathtext-fallback) ` (default: `'cm'`) rcParam. Takes "cm", "stix", "stixsans" or "none" to turn fallback off. The rcParam _mathtext.fallback\_to\_cm_ is deprecated, but if used, will override new fallback.

### [Add `contour.linewidth` to rcParams](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id32)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#add-contour-linewidth-to-rcparams "Link to this heading")

The new config option `[rcParams["contour.linewidth"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=contour.linewidth#rcparam-contour-linewidth) ` (default: `None`) allows to control the default line width of contours as a float. When set to `None`, the line widths fall back to `[rcParams["lines.linewidth"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=lines.linewidth#rcparam-lines-linewidth) ` (default: `1.5`). The config value is overridden as usual by the _linewidths_ argument passed to [`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
 when it is not set to `None`.

[3D Axes improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id33)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#d-axes-improvements "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [`Axes3D` no longer distorts the 3D plot to match the 2D aspect ratio](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id34)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#axes3d-no-longer-distorts-the-3d-plot-to-match-the-2d-aspect-ratio "Link to this heading")

Plots made with [`Axes3D`](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.axes3d.Axes3D")
 were previously stretched to fit a square bounding box. As this stretching was done after the projection from 3D to 2D, it resulted in distorted images if non-square bounding boxes were used. As of 3.3, this no longer occurs.

Currently, modes of setting the aspect (via [`set_aspect`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_aspect.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_aspect "mpl_toolkits.mplot3d.axes3d.Axes3D.set_aspect")
) in data space are not supported for Axes3D but may be in the future. If you want to simulate having equal aspect in data space, set the ratio of your data limits to match the value of [`get_box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_box_aspect.html#matplotlib.axes.Axes.get_box_aspect "matplotlib.axes.Axes.get_box_aspect")
. To control these ratios use the [`set_box_aspect`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect "mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect")
 method which accepts the ratios as a 3-tuple of X:Y:Z. The default aspect ratio is 4:4:3.

### [3D axes now support minor ticks](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id35)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#d-axes-now-support-minor-ticks "Link to this heading")

ax \= plt.figure().add\_subplot(projection\='3d')

ax.scatter(\[0, 1, 2\], \[1, 3, 5\], \[30, 50, 70\])

ax.set\_xticks(\[0.25, 0.75, 1.25, 1.75\], minor\=True)
ax.set\_xticklabels(\['a', 'b', 'c', 'd'\], minor\=True)

ax.set\_yticks(\[1.5, 2.5, 3.5, 4.5\], minor\=True)
ax.set\_yticklabels(\['A', 'B', 'C', 'D'\], minor\=True)

ax.set\_zticks(\[35, 45, 55, 65\], minor\=True)
ax.set\_zticklabels(\[r'$\\alpha$', r'$\\beta$', r'$\\delta$', r'$\\gamma$'\],
                   minor\=True)

ax.tick\_params(which\='major', color\='C0', labelcolor\='C0', width\=5)
ax.tick\_params(which\='minor', color\='C1', labelcolor\='C1', width\=3)

([`Source code`](https://matplotlib.org/stable/_downloads/cc0ee9397df05a6cfe40628acaf15991/whats_new_3-3-0-14.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/56abd02e9bf7dcb80c19b898f36dce83/whats_new_3-3-0-14.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/2172446d38143f05f9136c3c7b55c3fe/whats_new_3-3-0-14.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-14.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-3-0-14.2x.png)

### [Home/Forward/Backward buttons now work with 3D axes](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id36)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#home-forward-backward-buttons-now-work-with-3d-axes "Link to this heading")

[Interactive tool improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id37)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#interactive-tool-improvements "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [More consistent toolbar behavior across backends](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id38)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#more-consistent-toolbar-behavior-across-backends "Link to this heading")

Toolbar features are now more consistent across backends. The history buttons will auto-disable when there is no further action in a direction. The pan and zoom buttons will be marked active when they are in use.

In NbAgg and WebAgg, the toolbar buttons are now grouped similarly to other backends. The WebAgg toolbar now uses the same icons as other backends.

### [Toolbar icons are now styled for dark themes](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id39)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#toolbar-icons-are-now-styled-for-dark-themes "Link to this heading")

On dark themes, toolbar icons will now be inverted. When using the GTK3Agg backend, toolbar icons are now symbolic, and both foreground and background colors will follow the theme. Tooltips should also behave correctly.

### [Cursor text now uses a number of significant digits matching pointing precision](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id40)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#cursor-text-now-uses-a-number-of-significant-digits-matching-pointing-precision "Link to this heading")

Previously, the x/y position displayed by the cursor text would usually include far more significant digits than the mouse pointing precision (typically one pixel). This is now fixed for linear scales.

### [GTK / Qt zoom rectangle now black and white](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id41)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#gtk-qt-zoom-rectangle-now-black-and-white "Link to this heading")

This makes it visible even over a dark background.

### [Event handler simplifications](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id42)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#event-handler-simplifications "Link to this heading")

The [`backend_bases.key_press_handler`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.key_press_handler "matplotlib.backend_bases.key_press_handler")
 and [`backend_bases.button_press_handler`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.button_press_handler "matplotlib.backend_bases.button_press_handler")
 event handlers can now be directly connected to a canvas with `canvas.mpl_connect("key_press_event", key_press_handler)` and `canvas.mpl_connect("button_press_event", button_press_handler)`, rather than having to write wrapper functions that fill in the (now optional) _canvas_ and _toolbar_ parameters.

[Functions to compute a Path's size](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id43)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#functions-to-compute-a-path-s-size "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Various functions were added to [`BezierSegment`](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.BezierSegment "matplotlib.bezier.BezierSegment")
 and [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 to allow computation of the shape/size of a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 and its composite Bezier curves.

In addition to the fixes below, [`BezierSegment`](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.BezierSegment "matplotlib.bezier.BezierSegment")
 has gained more documentation and usability improvements, including properties that contain its dimension, degree, control\_points, and more.

### [Better interface for Path segment iteration](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id44)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#better-interface-for-path-segment-iteration "Link to this heading")

[`iter_bezier`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.iter_bezier "matplotlib.path.Path.iter_bezier")
 iterates through the [`BezierSegment`](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.BezierSegment "matplotlib.bezier.BezierSegment")
's that make up the Path. This is much more useful typically than the existing [`iter_segments`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.iter_segments "matplotlib.path.Path.iter_segments")
 function, which returns the absolute minimum amount of information possible to reconstruct the Path.

### [Fixed bug that computed a Path's Bbox incorrectly](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id45)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#fixed-bug-that-computed-a-path-s-bbox-incorrectly "Link to this heading")

Historically, [`get_extents`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.get_extents "matplotlib.path.Path.get_extents")
 has always simply returned the Bbox of a curve's control points, instead of the Bbox of the curve itself. While this is a correct upper bound for the path's extents, it can differ dramatically from the Path's actual extents for non-linear Bezier curves.

[Backend-specific improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id46)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#backend-specific-improvements "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [`savefig()` gained a _backend_ keyword argument](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id47)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#savefig-gained-a-backend-keyword-argument "Link to this heading")

The _backend_ keyword argument to `savefig` can now be used to pick the rendering backend without having to globally set the backend; e.g., one can save PDFs using the pgf backend with `savefig("file.pdf", backend="pgf")`.

### [The SVG backend can now render hatches with transparency](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id48)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#the-svg-backend-can-now-render-hatches-with-transparency "Link to this heading")

The SVG backend now respects the hatch stroke alpha. Useful applications are, among others, semi-transparent hatches as a subtle way to differentiate columns in bar plots.

### [SVG supports URLs on more artists](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id49)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#svg-supports-urls-on-more-artists "Link to this heading")

URLs on more artists (i.e., from [`Artist.set_url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url")
) will now be saved in SVG files, namely, `Tick`s and `Line2D`s are now supported.

### [Images in SVG will no longer be blurred in some viewers](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id50)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#images-in-svg-will-no-longer-be-blurred-in-some-viewers "Link to this heading")

A style is now supplied to images without interpolation (`imshow(..., interpolation='none'`) so that SVG image viewers will no longer perform interpolation when rendering themselves.

### [Saving SVG now supports adding metadata](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id51)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#saving-svg-now-supports-adding-metadata "Link to this heading")

When saving SVG files, metadata can now be passed which will be saved in the file using [Dublin Core](https://www.dublincore.org/specifications/dublin-core/)
 and [RDF](https://www.w3.org/1999/.status/PR-rdf-syntax-19990105/status)
. A list of valid metadata can be found in the documentation for [`FigureCanvasSVG.print_svg`](https://matplotlib.org/stable/api/backend_svg_api.html#matplotlib.backends.backend_svg.FigureCanvasSVG.print_svg "matplotlib.backends.backend_svg.FigureCanvasSVG.print_svg")
.

### [Saving PDF metadata via PGF now consistent with PDF backend](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id52)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#saving-pdf-metadata-via-pgf-now-consistent-with-pdf-backend "Link to this heading")

When saving PDF files using the PGF backend, passed metadata will be interpreted in the same way as with the PDF backend. Previously, this metadata was only accepted by the PGF backend when saving a multi-page PDF with [`backend_pgf.PdfPages`](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.PdfPages "matplotlib.backends.backend_pgf.PdfPages")
, but is now allowed when saving a single figure, as well.

### [NbAgg and WebAgg no longer use jQuery & jQuery UI](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#id53)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.3.0.html#nbagg-and-webagg-no-longer-use-jquery-jquery-ui "Link to this heading")

Instead, they are implemented using vanilla JavaScript. Please report any issues with browsers.

On this page