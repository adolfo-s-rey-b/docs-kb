[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#main-content)

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
    

[What's new in Matplotlib 3.1 (May 18, 2019)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id1)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#what-s-new-in-matplotlib-3-1-may-18-2019 "Link to this heading")

============================================================================================================================================================================================================================================================================

For a list of all of the issues and pull requests since the last revision, see the [GitHub statistics for 3.11.2 (Sep 10, 2026)](https://matplotlib.org/stable/release/github_stats.html#github-stats)
.

[New Features](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id2)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#new-features "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id3)
[`ConciseDateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter "matplotlib.dates.ConciseDateFormatter")
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#concisedateformatter "Link to this heading")

The automatic date formatter used by default can be quite verbose. A new formatter can be accessed that tries to make the tick labels appropriately concise.

([`Source code`](https://matplotlib.org/stable/_downloads/345f72da6199f37f5a120f1972e5b880/whats_new_3-1-0-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/406dcd20f05e50c268803e26ab5fc5c4/whats_new_3-1-0-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/7f4471c1188736d0c5b070269bc262b5/whats_new_3-1-0-1.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-1-0-1.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-1-0-1.2x.png)

### [Secondary x/y Axis support](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id4)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#secondary-x-y-axis-support "Link to this heading")

A new method provides the ability to add a second axis to an existing axes via [`Axes.secondary_xaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.secondary_xaxis.html#matplotlib.axes.Axes.secondary_xaxis "matplotlib.axes.Axes.secondary_xaxis")
 and [`Axes.secondary_yaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.secondary_yaxis.html#matplotlib.axes.Axes.secondary_yaxis "matplotlib.axes.Axes.secondary_yaxis")
. See [Secondary Axis](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/secondary_axis.html)
 for examples.

([`Source code`](https://matplotlib.org/stable/_downloads/f1bd00882afe0a52a0954cf9f80cf06d/whats_new_3-1-0-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/3e465c3d8f5e59f3186636d381d69be1/whats_new_3-1-0-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/371e2082b6c5e3feac9b1e0eee70553a/whats_new_3-1-0-2.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-1-0-2.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-1-0-2.2x.png)

### [](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id5)
[`FuncScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncScale "matplotlib.scale.FuncScale")
 for arbitrary axes scales[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#funcscale-for-arbitrary-axes-scales "Link to this heading")

A new [`FuncScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncScale "matplotlib.scale.FuncScale")
 class was added (and [`FuncTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.FuncTransform "matplotlib.scale.FuncTransform")
) to allow the user to have arbitrary scale transformations without having to write a new subclass of [`ScaleBase`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")
. This can be accessed by:

ax.set\_yscale('function', functions\=(forward, inverse))

where `forward` and `inverse` are callables that return the scale transform and its inverse. See the last example in [Scales overview](https://matplotlib.org/stable/gallery/scales/scales.html)
.

### [Legend for scatter](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id6)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#legend-for-scatter "Link to this heading")

A new method for creating legends for scatter plots has been introduced. Previously, in order to obtain a legend for a [`scatter()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
 plot, one could either plot several scatters, each with an individual label, or create proxy artists to show in the legend manually. Now, [`PathCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
 provides a method [`legend_elements()`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection.legend_elements "matplotlib.collections.PathCollection.legend_elements")
 to obtain the handles and labels for a scatter plot in an automated way. This makes creating a legend for a scatter plot as easy as

([`Source code`](https://matplotlib.org/stable/_downloads/333a8576b38d767402385e566d85b9ce/whats_new_3-1-0-3.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/e789f7a6418bceb0fbcc4b11a89813e7/whats_new_3-1-0-3.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/c0332a1a43c79ebbe4622db89ab52758/whats_new_3-1-0-3.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-1-0-3.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-1-0-3.2x.png)

An example can be found in [Automated legend creation](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html#automatedlegendcreation)
.

### [Matplotlib no longer requires framework app build on MacOSX backend](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id7)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#matplotlib-no-longer-requires-framework-app-build-on-macosx-backend "Link to this heading")

Previous versions of matplotlib required a Framework build of python to work. The app type was updated to no longer require this, so the MacOSX backend should work with non-framework python.

This also adds support for the MacOSX backend for PyPy3.

[Figure, FigureCanvas, and Backends](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id8)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#figure-figurecanvas-and-backends "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Figure.frameon is now a direct proxy for the Figure patch visibility state](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id9)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#figure-frameon-is-now-a-direct-proxy-for-the-figure-patch-visibility-state "Link to this heading")

Accessing `Figure.frameon` (including via `get_frameon` and `set_frameon` now directly forwards to the visibility of the underlying Rectangle artist (`Figure.patch.get_frameon`, `Figure.patch.set_frameon`).

### [_pil\_kwargs_ argument added to savefig](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id10)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#pil-kwargs-argument-added-to-savefig "Link to this heading")

Matplotlib uses Pillow to handle saving to the JPEG and TIFF formats. The [`savefig()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 function gained a _pil\_kwargs_ keyword argument, which can be used to forward arguments to Pillow's [`PIL.Image.Image.save`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save "(in Pillow (PIL Fork) v12.3.0)")
.

The _pil\_kwargs_ argument can also be used when saving to PNG. In that case, Matplotlib also uses Pillow's [`PIL.Image.Image.save`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save "(in Pillow (PIL Fork) v12.3.0)")
 instead of going through its own builtin PNG support.

### [Add `inaxes` method to](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id11)
 [`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#add-inaxes-method-to-figurecanvasbase "Link to this heading")

The [`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")
 class has now an [`inaxes`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.inaxes "matplotlib.backend_bases.FigureCanvasBase.inaxes")
 method to check whether a point is in an axes and returns the topmost axes, else None.

### [cairo backend defaults to pycairo instead of cairocffi](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id12)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#cairo-backend-defaults-to-pycairo-instead-of-cairocffi "Link to this heading")

This leads to faster import/runtime performance in some cases. The backend will fall back to cairocffi in case pycairo isn't available.

[Axes and Artists](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id13)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#axes-and-artists "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [axes\_grid1 and axisartist Axes no longer draw spines twice](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id14)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#axes-grid1-and-axisartist-axes-no-longer-draw-spines-twice "Link to this heading")

Previously, spines of [`axes_grid1`](https://matplotlib.org/stable/api/toolkits/axes_grid1.html#module-mpl_toolkits.axes_grid1 "mpl_toolkits.axes_grid1")
 and [`axisartist`](https://matplotlib.org/stable/api/toolkits/axisartist.html#module-mpl_toolkits.axisartist "mpl_toolkits.axisartist")
 Axes would be drawn twice, leading to a "bold" appearance. This is no longer the case.

### [Return type of ArtistInspector.get\_aliases changed](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id15)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#return-type-of-artistinspector-get-aliases-changed "Link to this heading")

[`ArtistInspector.get_aliases`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector.get_aliases "matplotlib.artist.ArtistInspector.get_aliases")
 previously returned the set of aliases as `{fullname: {alias1: None, alias2: None, ...}}`. The dict-to-None mapping was used to simulate a set in earlier versions of Python. It has now been replaced by a set, i.e. `{fullname: {alias1, alias2, ...}}`.

This value is also stored in `ArtistInspector.aliasd`, which has likewise changed.

### [](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id16)
[`ConnectionPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")
 accepts arbitrary transforms[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#connectionpatch-accepts-arbitrary-transforms "Link to this heading")

Alternatively to strings like `"data"` or `"axes fraction"`, [`ConnectionPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")
 now accepts any [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 as input for the _coordsA_ and _coordsB_ arguments. This allows to draw lines between points defined in different user defined coordinate systems. Also see [Using ConnectionPatch](https://matplotlib.org/stable/users/explain/text/annotations.html#using-connectionpatch)
.

### [mplot3d Line3D now allows {set,get}\_data\_3d](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id17)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#mplot3d-line3d-now-allows-set-get-data-3d "Link to this heading")

Lines created with the 3d projection in mplot3d can now access the data using [`get_data_3d()`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3D.html#mpl_toolkits.mplot3d.art3d.Line3D.get_data_3d "mpl_toolkits.mplot3d.art3d.Line3D.get_data_3d")
 which returns a tuple of array\_likes containing the (x, y, z) data. The equivalent [`set_data_3d`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3D.html#mpl_toolkits.mplot3d.art3d.Line3D.set_data_3d "mpl_toolkits.mplot3d.art3d.Line3D.set_data_3d")
 can be used to modify the data of an existing Line3D.

### [`Axes3D.voxels` now shades the resulting voxels](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id18)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#axes3d-voxels-now-shades-the-resulting-voxels "Link to this heading")

The [`Axes3D.voxels`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.voxels.html#mpl_toolkits.mplot3d.axes3d.Axes3D.voxels "mpl_toolkits.mplot3d.axes3d.Axes3D.voxels")
 method now takes a _shade_ parameter that defaults to [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
. This shades faces based on their orientation, behaving just like the matching parameters to [`plot_trisurf()`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf "mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf")
 and [`bar3d()`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.bar3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D.bar3d "mpl_toolkits.mplot3d.axes3d.Axes3D.bar3d")
. The plot below shows how this affects the output.

([`Source code`](https://matplotlib.org/stable/_downloads/242f32f281110a1d7b1dc4d5ce345b0b/whats_new_3-1-0-4.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/cb95355c62540e5a2601201ce5eeb89b/whats_new_3-1-0-4.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/f5ade04a0cd343b7a24901b17f219dfa/whats_new_3-1-0-4.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-1-0-4.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-1-0-4.2x.png)

[Axis and Ticks](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id19)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#axis-and-ticks "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Added](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id20)
 [`Axis.get_inverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_inverted.html#matplotlib.axis.Axis.get_inverted "matplotlib.axis.Axis.get_inverted")
 and [`Axis.set_inverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_inverted.html#matplotlib.axis.Axis.set_inverted "matplotlib.axis.Axis.set_inverted")
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#added-axis-get-inverted-and-axis-set-inverted "Link to this heading")

The [`Axis.get_inverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_inverted.html#matplotlib.axis.Axis.get_inverted "matplotlib.axis.Axis.get_inverted")
 and [`Axis.set_inverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_inverted.html#matplotlib.axis.Axis.set_inverted "matplotlib.axis.Axis.set_inverted")
 methods query and set whether the axis uses "inverted" orientation (i.e. increasing to the left for the x-axis and to the bottom for the y-axis).

They perform tasks similar to [`Axes.xaxis_inverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.xaxis_inverted.html#matplotlib.axes.Axes.xaxis_inverted "matplotlib.axes.Axes.xaxis_inverted")
, [`Axes.yaxis_inverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.yaxis_inverted.html#matplotlib.axes.Axes.yaxis_inverted "matplotlib.axes.Axes.yaxis_inverted")
, [`Axes.invert_xaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.invert_xaxis.html#matplotlib.axes.Axes.invert_xaxis "matplotlib.axes.Axes.invert_xaxis")
, and [`Axes.invert_yaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.invert_yaxis.html#matplotlib.axes.Axes.invert_yaxis "matplotlib.axes.Axes.invert_yaxis")
, with the specific difference that [`Axis.set_inverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_inverted.html#matplotlib.axis.Axis.set_inverted "matplotlib.axis.Axis.set_inverted")
 makes it easier to set the inversion of an axis regardless of whether it had previously been inverted before.

### [Adjust default minor tick spacing](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id21)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#adjust-default-minor-tick-spacing "Link to this heading")

Default minor tick spacing was changed from 0.625 to 0.5 for major ticks spaced 2.5 units apart.

### [](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id22)
[`EngFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.EngFormatter "matplotlib.ticker.EngFormatter")
 now accepts _usetex_, _useMathText_ as keyword only arguments[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#engformatter-now-accepts-usetex-usemathtext-as-keyword-only-arguments "Link to this heading")

A public API has been added to [`EngFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.EngFormatter "matplotlib.ticker.EngFormatter")
 to control how the numbers in the ticklabels will be rendered. By default, _useMathText_ evaluates to `[rcParams["axes.formatter.use_mathtext"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.use_mathtext#rcparam-axes-formatter-use-mathtext) ` (default: `False`) and _usetex_ evaluates to `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`).

If either is [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
 then the numbers will be encapsulated by `$` signs. When using `TeX` this implies that the numbers will be shown in TeX's math font. When using mathtext, the `$` signs around numbers will ensure Unicode rendering (as implied by mathtext). This will make sure that the minus signs in the ticks are rendered as the Unicode minus (U+2212) when using mathtext (without relying on the [`fix_minus`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter.fix_minus "matplotlib.ticker.Formatter.fix_minus")
 method).

[Animation and Interactivity](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id23)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#animation-and-interactivity "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Support for forward/backward mouse buttons](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id24)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#support-for-forward-backward-mouse-buttons "Link to this heading")

Figure managers now support a `button_press` event for mouse buttons, similar to the `key_press` events. This allows binding actions to mouse buttons (see [`MouseButton`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton "matplotlib.backend_bases.MouseButton")
) The first application of this mechanism is support of forward/backward mouse buttons in figures created with the Qt5 backend.

### [_progress\_callback_ argument to](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id25)
 [`save()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.save "matplotlib.animation.Animation.save")
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#progress-callback-argument-to-save "Link to this heading")

The method [`Animation.save`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.save "matplotlib.animation.Animation.save")
 gained an optional _progress\_callback_ argument to notify the saving progress.

### [Add `cache_frame_data` keyword-only argument into](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id26)
 [`animation.FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#add-cache-frame-data-keyword-only-argument-into-animation-funcanimation "Link to this heading")

[`matplotlib.animation.FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 has been caching frame data by default; however, this caching is not ideal in certain cases e.g. When [`FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 needs to be only drawn(not saved) interactively and memory required by frame data is quite large. By adding _cache\_frame\_data_ keyword-only argument, users can now disable this caching; thereby, this new argument provides a fix for issue [#8528](https://github.com/matplotlib/matplotlib/issues/8528/)
.

### [Endless Looping GIFs with PillowWriter](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id27)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#endless-looping-gifs-with-pillowwriter "Link to this heading")

We acknowledge that most people want to watch a GIF more than once. Saving an animation as a GIF with PillowWriter now produces an endless looping GIF.

### [Adjusted](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id28)
 [`matplotlib.widgets.Slider`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "matplotlib.widgets.Slider")
 to have vertical orientation[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#adjusted-matplotlib-widgets-slider-to-have-vertical-orientation "Link to this heading")

The [`matplotlib.widgets.Slider`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "matplotlib.widgets.Slider")
 widget now takes an optional argument _orientation_ which indicates the direction (`'horizontal'` or `'vertical'`) that the slider should take.

### [Improved formatting of image values under cursor when a colorbar is present](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id29)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#improved-formatting-of-image-values-under-cursor-when-a-colorbar-is-present "Link to this heading")

When a colorbar is present, its formatter is now used to format the image values under the mouse cursor in the status bar. For example, for an image displaying the values 10,000 and 10,001, the statusbar will now (using default settings) display the values as `10000` and `10001`), whereas both values were previously displayed as `1e+04`.

### [MouseEvent button attribute is now an IntEnum](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id30)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#mouseevent-button-attribute-is-now-an-intenum "Link to this heading")

The `button` attribute of [`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")
 instances can take the values None, 1 (left button), 2 (middle button), 3 (right button), "up" (scroll), and "down" (scroll). For better legibility, the 1, 2, and 3 values are now represented using the [`enum.IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python v3.14)")
 class [`matplotlib.backend_bases.MouseButton`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton "matplotlib.backend_bases.MouseButton")
, with the values [`MouseButton.LEFT`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton.LEFT "matplotlib.backend_bases.MouseButton.LEFT")
 (`== 1`), [`MouseButton.MIDDLE`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton.MIDDLE "matplotlib.backend_bases.MouseButton.MIDDLE")
 (`== 2`), and [`MouseButton.RIGHT`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton.RIGHT "matplotlib.backend_bases.MouseButton.RIGHT")
 (`== 3`).

[Configuration, Install, and Development](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id31)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#configuration-install-and-development "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [The MATPLOTLIBRC environment variable can now point to any "file" path](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id32)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#the-matplotlibrc-environment-variable-can-now-point-to-any-file-path "Link to this heading")

This includes device files; in particular, on Unix systems, one can set `MATPLOTLIBRC` to `/dev/null` to ignore the user's matplotlibrc file and fall back to Matplotlib's defaults.

As a reminder, if `MATPLOTLIBRC` points to a directory, Matplotlib will try to load the matplotlibrc file from `$MATPLOTLIBRC/matplotlibrc`.

### [Allow LaTeX code `pgf.preamble` and `text.latex.preamble` in MATPLOTLIBRC file](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id33)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#allow-latex-code-pgf-preamble-and-text-latex-preamble-in-matplotlibrc-file "Link to this heading")

Previously, the rc file keys `[rcParams["pgf.preamble"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=pgf.preamble#rcparam-pgf-preamble) ` (default: `''`) and `[rcParams["text.latex.preamble"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.latex.preamble#rcparam-text-latex-preamble) ` (default: `''`) were parsed using commas as separators. This would break valid LaTeX code, such as:

\\usepackage\[protrusion\=true, expansion\=false\]{microtype}

The parsing has been modified to pass the complete line to the LaTeX system, keeping all commas. Passing a list of strings from within a Python script still works as it used to.

### [New logging API](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#id34)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.1.0.html#new-logging-api "Link to this heading")

[`matplotlib.set_loglevel`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.set_loglevel "matplotlib.set_loglevel")
 / [`pyplot.set_loglevel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.set_loglevel.html#matplotlib.pyplot.set_loglevel "matplotlib.pyplot.set_loglevel")
 can be called to display more (or less) detailed logging output.

On this page