[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#main-content)

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
    

matplotlib.figure.SubFigure[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib-figure-subfigure "Link to this heading")

==============================================================================================================================================================

class matplotlib.figure.SubFigure(_parent_, _subplotspec_, _\*_, _facecolor\=None_, _edgecolor\=None_, _linewidth\=0.0_, _frameon\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L2222-L2427)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "Link to this definition")

Logical figure that can be placed inside a figure.

See [SubFigure](https://matplotlib.org/stable/api/figure_api.html#figure-api-subfigure)
 for an index of methods on this class. Typically instantiated using [`Figure.add_subfigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subfigure.html#matplotlib.figure.Figure.add_subfigure "matplotlib.figure.Figure.add_subfigure")
 or [`SubFigure.add_subfigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.add_subfigure.html#matplotlib.figure.SubFigure.add_subfigure "matplotlib.figure.SubFigure.add_subfigure")
, or [`SubFigure.subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.subfigures.html#matplotlib.figure.SubFigure.subfigures "matplotlib.figure.SubFigure.subfigures")
. A subfigure has the same methods as a figure except for those particularly tied to the size or dpi of the figure, and is confined to a prescribed region of the figure. For example the following puts two subfigures side-by-side:

fig \= plt.figure()
sfigs \= fig.subfigures(1, 2)
axsL \= sfigs\[0\].subplots(1, 2)
axsR \= sfigs\[1\].subplots(2, 1)

See [Figure subfigures](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html)

Parameters:

**parent**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")

Figure or subfigure that contains the SubFigure. SubFigures can be nested.

**subplotspec**[`gridspec.SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")

Defines the region in a parent gridspec where the subfigure will be placed.

**facecolor**default: `"none"`

The figure patch face color; transparent by default.

**edgecolor**default: `[rcParams["figure.edgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.edgecolor#rcparam-figure-edgecolor) ` (default: `'white'`)

The figure patch edge color.

**linewidth**float

The linewidth of the frame (i.e. the edge linewidth of the figure patch).

**frameon**bool, default: `[rcParams["figure.frameon"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.frameon#rcparam-figure-frameon) ` (default: `True`)

If `False`, suppress drawing the figure background patch.

Other Parameters:

**\*\*kwargs**[`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
 properties, optional

| Property | Description |
| --- | --- |
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
| [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
| [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
| [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
| [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
| [`dpi`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.set_dpi.html#matplotlib.figure.SubFigure.set_dpi "matplotlib.figure.SubFigure.set_dpi") | float |
| [`edgecolor`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_edgecolor "matplotlib.figure.FigureBase.set_edgecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`facecolor`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_facecolor "matplotlib.figure.FigureBase.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`figure`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_figure "matplotlib.figure.FigureBase.set_figure") | unknown |
| [`frameon`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_frameon "matplotlib.figure.FigureBase.set_frameon") | bool |
| [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
| [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
| [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
| [`linewidth`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_linewidth "matplotlib.figure.FigureBase.set_linewidth") | number |
| [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
| [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
| [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
| [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
| [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
| [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
| [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
| [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
| [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
| [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

On this page