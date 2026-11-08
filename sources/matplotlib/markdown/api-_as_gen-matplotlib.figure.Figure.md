[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#main-content)

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
    

matplotlib.figure.Figure[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib-figure-figure "Link to this heading")

=====================================================================================================================================================

class matplotlib.figure.Figure(_figsize\=None_, _dpi\=None_, _\*_, _facecolor\=None_, _edgecolor\=None_, _linewidth\=0.0_, _frameon\=None_, _subplotpars\=None_, _tight\_layout\=None_, _constrained\_layout\=None_, _layout\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L2430-L3671)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "Link to this definition")

The top level container for all the plot elements.

See [`matplotlib.figure`](https://matplotlib.org/stable/api/figure_api.html#module-matplotlib.figure "matplotlib.figure")
 for an index of class methods.

Attributes:

**patch**

The [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 instance representing the figure background patch.

**suppressComposite**

For multiple images, the figure will make composite images depending on the renderer option\_image\_nocomposite function. If _suppressComposite_ is a boolean, this will override the renderer.

Parameters:

**figsize**(float, float) or (float, float, str), default: `[rcParams["figure.figsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.figsize#rcparam-figure-figsize) ` (default: `[6.4, 4.8]`)

The figure dimensions. This can be

*   a tuple `(width, height, unit)`, where _unit_ is one of "in" (inch), "cm" (centimenter), "px" (pixel).
    
*   a tuple `(width, height)`, which is interpreted in inches, i.e. as `(width, height, "in")`.
    

One of _width_ or _height_ may be `None`; the respective value is taken from `[rcParams["figure.figsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.figsize#rcparam-figure-figsize) ` (default: `[6.4, 4.8]`).

**dpi**float, default: `[rcParams["figure.dpi"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.dpi#rcparam-figure-dpi) ` (default: `100.0`)

Dots per inch.

**facecolor**default: `[rcParams["figure.facecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.facecolor#rcparam-figure-facecolor) ` (default: `'white'`)

The figure patch facecolor.

**edgecolor**default: `[rcParams["figure.edgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.edgecolor#rcparam-figure-edgecolor) ` (default: `'white'`)

The figure patch edge color.

**linewidth**float

The linewidth of the frame (i.e. the edge linewidth of the figure patch).

**frameon**bool, default: `[rcParams["figure.frameon"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.frameon#rcparam-figure-frameon) ` (default: `True`)

If `False`, suppress drawing the figure background patch.

**subplotpars**[`SubplotParams`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotParams.html#matplotlib.gridspec.SubplotParams "matplotlib.gridspec.SubplotParams")

Subplot parameters. If not given, the default subplot parameters `[rcParams["figure.subplot.*"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.subplot.*#rcparam-figure-subplot-left) ` are used.

**tight\_layout**bool or dict, default: `[rcParams["figure.autolayout"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.autolayout#rcparam-figure-autolayout) ` (default: `False`)

Whether to use the tight layout mechanism. See [`set_tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_tight_layout.html#matplotlib.figure.Figure.set_tight_layout "matplotlib.figure.Figure.set_tight_layout")
.

Discouraged

The use of this parameter is discouraged. Please use `layout='tight'` instead for the common case of `tight_layout=True` and use [`set_tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_tight_layout.html#matplotlib.figure.Figure.set_tight_layout "matplotlib.figure.Figure.set_tight_layout")
 otherwise.

**constrained\_layout**bool, default: `[rcParams["figure.constrained_layout.use"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.constrained_layout.use#rcparam-figure-constrained-layout-use) ` (default: `False`)

This is equal to `layout='constrained'`.

Discouraged

The use of this parameter is discouraged. Please use `layout='constrained'` instead.

**layout**{'constrained', 'compressed', 'tight', 'none', [`LayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine "matplotlib.layout_engine.LayoutEngine")
, None}, default: None

The layout mechanism for positioning of plot elements to avoid overlapping Axes decorations (labels, ticks, etc). Note that layout managers can have significant performance penalties.

*   'constrained': The constrained layout solver adjusts Axes sizes to avoid overlapping Axes decorations. Can handle complex plot layouts and colorbars, and is thus recommended.
    
    See [Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#constrainedlayout-guide)
     for examples.
    
*   'compressed': uses the same algorithm as 'constrained', but removes extra space between fixed-aspect-ratio Axes. Best for simple grids of Axes.
    
*   'tight': Use the tight layout mechanism. This is a relatively simple algorithm that adjusts the subplot parameters so that decorations do not overlap.
    
    See [Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#tight-layout-guide)
     for examples.
    
*   'none': Do not use a layout engine.
    
*   A [`LayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine "matplotlib.layout_engine.LayoutEngine")
     instance. Builtin layout classes are [`ConstrainedLayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.ConstrainedLayoutEngine "matplotlib.layout_engine.ConstrainedLayoutEngine")
     and [`TightLayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.TightLayoutEngine "matplotlib.layout_engine.TightLayoutEngine")
    , more easily accessible by 'constrained' and 'tight'. Passing an instance allows third parties to provide their own layout engine.
    

If not given, fall back to using the parameters _tight\_layout_ and _constrained\_layout_, including their config defaults `[rcParams["figure.autolayout"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.autolayout#rcparam-figure-autolayout) ` (default: `False`) and `[rcParams["figure.constrained_layout.use"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.constrained_layout.use#rcparam-figure-constrained-layout-use) ` (default: `False`).

Other Parameters:

**\*\*kwargs**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 properties, optional

| Property | Description |
| --- | --- |
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
| [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
| [`canvas`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_canvas.html#matplotlib.figure.Figure.set_canvas "matplotlib.figure.Figure.set_canvas") | FigureCanvas |
| [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
| [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
| [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
| [`constrained_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_constrained_layout.html#matplotlib.figure.Figure.set_constrained_layout "matplotlib.figure.Figure.set_constrained_layout") | unknown |
| [`constrained_layout_pads`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_constrained_layout_pads.html#matplotlib.figure.Figure.set_constrained_layout_pads "matplotlib.figure.Figure.set_constrained_layout_pads") | unknown |
| [`dpi`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_dpi.html#matplotlib.figure.Figure.set_dpi "matplotlib.figure.Figure.set_dpi") | float |
| [`edgecolor`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_edgecolor "matplotlib.figure.FigureBase.set_edgecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`facecolor`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_facecolor "matplotlib.figure.FigureBase.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`figheight`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_figheight.html#matplotlib.figure.Figure.set_figheight "matplotlib.figure.Figure.set_figheight") | float |
| [`figure`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_figure "matplotlib.figure.FigureBase.set_figure") | unknown |
| [`figwidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_figwidth.html#matplotlib.figure.Figure.set_figwidth "matplotlib.figure.Figure.set_figwidth") | float |
| [`frameon`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_frameon "matplotlib.figure.FigureBase.set_frameon") | bool |
| [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
| [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
| [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
| [`layout_engine`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_layout_engine.html#matplotlib.figure.Figure.set_layout_engine "matplotlib.figure.Figure.set_layout_engine") | {'constrained', 'compressed', 'tight', 'none', [`LayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine "matplotlib.layout_engine.LayoutEngine")<br>, None} |
| [`linewidth`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_linewidth "matplotlib.figure.FigureBase.set_linewidth") | number |
| [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
| [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
| [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
| [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
| [`size_inches`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_size_inches.html#matplotlib.figure.Figure.set_size_inches "matplotlib.figure.Figure.set_size_inches") | (float, float) or float |
| [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
| [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
| [`tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_tight_layout.html#matplotlib.figure.Figure.set_tight_layout "matplotlib.figure.Figure.set_tight_layout") | unknown |
| [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
| [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
| [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
| [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

On this page