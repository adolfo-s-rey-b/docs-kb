[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.GridlinesCollection.html#main-content)

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
    

mpl\_toolkits.axisartist.axis\_artist.GridlinesCollection[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.GridlinesCollection.html#mpl-toolkits-axisartist-axis-artist-gridlinescollection "Link to this heading")

====================================================================================================================================================================================================================================================

class mpl\_toolkits.axisartist.axis\_artist.GridlinesCollection(_\*args_, _which\='major'_, _axis\='both'_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L623-L677)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.GridlinesCollection.html#mpl_toolkits.axisartist.axis_artist.GridlinesCollection "Link to this definition")

Bases: [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")

Collection of grid lines.

Parameters:

**which**{"major", "minor"}

Which grid to consider.

**axis**{"both", "x", "y"}

Which axis to consider.

**\*args, \*\*kwargs**

Passed to [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
.

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L672-L677)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.GridlinesCollection.html#mpl_toolkits.axisartist.axis_artist.GridlinesCollection.draw "Link to this definition")

Draw the Artist (and its children) using the given renderer.

This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")
 returns False).

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass.

Notes

This method is overridden in the Artist subclasses.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _antialiased\=<UNSET>_, _array\=<UNSET>_, _axis\=<UNSET>_, _capstyle\=<UNSET>_, _clim\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _cmap\=<UNSET>_, _color\=<UNSET>_, _colors\=<UNSET>_, _edgecolor\=<UNSET>_, _facecolor\=<UNSET>_, _gapcolor\=<UNSET>_, _gid\=<UNSET>_, _grid\_helper\=<UNSET>_, _hatch\=<UNSET>_, _hatch\_linewidth\=<UNSET>_, _hatchcolor\=<UNSET>_, _in\_layout\=<UNSET>_, _joinstyle\=<UNSET>_, _label\=<UNSET>_, _linestyle\=<UNSET>_, _linewidth\=<UNSET>_, _mouseover\=<UNSET>_, _norm\=<UNSET>_, _offset\_transform\=<UNSET>_, _offsets\=<UNSET>_, _path\_effects\=<UNSET>_, _paths\=<UNSET>_, _picker\=<UNSET>_, _pickradius\=<UNSET>_, _rasterized\=<UNSET>_, _segments\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _urls\=<UNSET>_, _verts\=<UNSET>_, _visible\=<UNSET>_, _which\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.GridlinesCollection.html#mpl_toolkits.axisartist.axis_artist.GridlinesCollection.set "Link to this definition")

Set multiple properties at once.

a.set(a\=A, b\=B, c\=C)

is equivalent to

a.set\_a(A)
a.set\_b(B)
a.set\_c(C)

In addition to the full property names, aliases are also supported, e.g. `set(lw=2)` is equivalent to `set(linewidth=2)`, but it is an error to pass both simultaneously.

The order of the individual setter calls matches the order of parameters in `set()`. However, most properties do not depend on each other so that order is rarely relevant.

Supported properties are

> | Property | Description |
> | --- | --- |
> | [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
> | [`alpha`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_alpha "matplotlib.collections.Collection.set_alpha") | array-like or float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`antialiased`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased")<br> or [`aa`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased")<br> or [`antialiaseds`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased") | bool or list of bools |
> | [`array`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ScalarMappable.set_array "matplotlib.colorizer._ScalarMappable.set_array") | array-like or None |
> | [`axis`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.GridlinesCollection.html#mpl_toolkits.axisartist.axis_artist.GridlinesCollection.set_axis "mpl_toolkits.axisartist.axis_artist.GridlinesCollection.set_axis") | {"both", "x", "y"} |
> | [`capstyle`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_capstyle "matplotlib.collections.Collection.set_capstyle") | [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")<br> or {'butt', 'projecting', 'round'} |
> | [`clim`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_clim "matplotlib.colorizer._ColorizerInterface.set_clim") | (vmin: float, vmax: float) |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`cmap`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_cmap "matplotlib.colorizer._ColorizerInterface.set_cmap") | [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")<br> or str or None |
> | [`color`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection.set_color "matplotlib.collections.LineCollection.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`colors`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection.set_color "matplotlib.collections.LineCollection.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`edgecolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor")<br> or [`ec`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor")<br> or [`edgecolors`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or 'face' |
> | [`facecolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor")<br> or [`facecolors`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`gapcolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection.set_gapcolor "matplotlib.collections.LineCollection.set_gapcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or None |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`grid_helper`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.GridlinesCollection.html#mpl_toolkits.axisartist.axis_artist.GridlinesCollection.set_grid_helper "mpl_toolkits.axisartist.axis_artist.GridlinesCollection.set_grid_helper") | [`GridHelperBase`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.GridHelperBase.html#mpl_toolkits.axisartist.axislines.GridHelperBase "mpl_toolkits.axisartist.axislines.GridHelperBase")<br> subclass |
> | [`hatch`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_hatch "matplotlib.collections.Collection.set_hatch") | {'/', '\\', '\|', '-', '+', 'x', 'o', 'O', '.', '\*'} |
> | [`hatch_linewidth`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_hatch_linewidth "matplotlib.collections.Collection.set_hatch_linewidth") | unknown |
> | [`hatchcolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_hatchcolor "matplotlib.collections.Collection.set_hatchcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or 'edge' |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`joinstyle`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_joinstyle "matplotlib.collections.Collection.set_joinstyle") | [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")<br> or {'miter', 'round', 'bevel'} |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`linestyle`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle")<br> or [`dashes`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle")<br> or [`linestyles`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle")<br> or [`ls`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle") | {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq) or list thereof |
> | [`linewidth`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth")<br> or [`linewidths`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth")<br> or [`lw`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth") | float or list of floats |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`norm`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_norm "matplotlib.colorizer._ColorizerInterface.set_norm") | [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")<br> or str or None |
> | [`offset_transform`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offset_transform "matplotlib.collections.Collection.set_offset_transform")<br> or [`transOffset`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offset_transform "matplotlib.collections.Collection.set_offset_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`offsets`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offsets "matplotlib.collections.Collection.set_offsets") | (N, 2) or (2,) array-like |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`paths`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection.set_segments "matplotlib.collections.LineCollection.set_segments") | unknown |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`pickradius`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_pickradius "matplotlib.collections.Collection.set_pickradius") | float |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`segments`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection.set_segments "matplotlib.collections.LineCollection.set_segments") | unknown |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`urls`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_urls "matplotlib.collections.Collection.set_urls") | list of str or None |
> | [`verts`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection.set_segments "matplotlib.collections.LineCollection.set_segments") | unknown |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`which`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.GridlinesCollection.html#mpl_toolkits.axisartist.axis_artist.GridlinesCollection.set_which "mpl_toolkits.axisartist.axis_artist.GridlinesCollection.set_which") | {"major", "minor"} |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_axis(_axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L652-L660)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.GridlinesCollection.html#mpl_toolkits.axisartist.axis_artist.GridlinesCollection.set_axis "Link to this definition")

Select axis.

Parameters:

**axis**{"both", "x", "y"}

set\_grid\_helper(_grid\_helper_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L662-L670)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.GridlinesCollection.html#mpl_toolkits.axisartist.axis_artist.GridlinesCollection.set_grid_helper "Link to this definition")

Set grid helper.

Parameters:

**grid\_helper**[`GridHelperBase`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.GridHelperBase.html#mpl_toolkits.axisartist.axislines.GridHelperBase "mpl_toolkits.axisartist.axislines.GridHelperBase")
 subclass

set\_which(_which_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/axis_artist.py#L642-L650)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.GridlinesCollection.html#mpl_toolkits.axisartist.axis_artist.GridlinesCollection.set_which "Link to this definition")

Select major or minor grid lines.

Parameters:

**which**{"major", "minor"}

On this page