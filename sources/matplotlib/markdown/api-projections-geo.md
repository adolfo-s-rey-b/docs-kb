[Skip to main content](https://matplotlib.org/stable/api/projections/geo.html#main-content)

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
    

`matplotlib.projections.geo`[#](https://matplotlib.org/stable/api/projections/geo.html#module-matplotlib.projections.geo "Link to this heading")

=================================================================================================================================================

class matplotlib.projections.geo.AitoffAxes(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L255-L298)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.AitoffAxes "Link to this definition")

Bases: [`GeoAxes`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes "matplotlib.projections.geo.GeoAxes")

Build an Axes in a figure.

Parameters:

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

The Axes is built in the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 _fig_.

**\*args**

`*args` can be a single `(left, bottom, width, height)` rectangle or a single [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
. This specifies the rectangle (in figure coordinates) where the Axes is positioned.

`*args` can also consist of three numbers or a single three-digit number; in the latter case, the digits are considered as independent numbers. The numbers are interpreted as `(nrows, ncols, index)`: `(nrows, ncols)` specifies the size of an array of subplots, and `index` is the 1-based index of the subplot being created. Finally, `*args` can also directly be a [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
 instance.

**sharex, sharey**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, optional

The x- or y-[`axis`](https://matplotlib.org/stable/api/axis_api.html#module-matplotlib.axis "matplotlib.axis")
 is shared with the x- or y-axis in the input [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
. Note that it is not possible to unshare axes.

**frameon**bool, default: True

Whether the Axes frame is visible.

**box\_aspect**float, optional

Set a fixed aspect for the Axes box, i.e. the ratio of height to width. See [`set_box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect")
 for details.

**forward\_navigation\_events**bool or "auto", default: "auto"

Control whether pan/zoom events are passed through to Axes below this one. "auto" is _True_ for axes with an invisible patch and _False_ otherwise.

**\*\*kwargs**

Other optional keyword arguments:

| Property | Description |
| --- | --- |
| [`adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#matplotlib.axes.Axes.set_adjustable "matplotlib.axes.Axes.set_adjustable") | {'box', 'datalim'} |
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
| [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
| [`anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "matplotlib.axes.Axes.set_anchor") | (float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', ...} |
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
| [`aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect") | {'auto', 'equal'} or float |
| [`autoscale_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscale_on.html#matplotlib.axes.Axes.set_autoscale_on "matplotlib.axes.Axes.set_autoscale_on") | bool |
| [`autoscalex_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscalex_on.html#matplotlib.axes.Axes.set_autoscalex_on "matplotlib.axes.Axes.set_autoscalex_on") | unknown |
| [`autoscaley_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscaley_on.html#matplotlib.axes.Axes.set_autoscaley_on "matplotlib.axes.Axes.set_autoscaley_on") | unknown |
| [`axes_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axes_locator.html#matplotlib.axes.Axes.set_axes_locator "matplotlib.axes.Axes.set_axes_locator") | Callable\[\[Axes, Renderer\], Bbox\] |
| [`axisbelow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axisbelow.html#matplotlib.axes.Axes.set_axisbelow "matplotlib.axes.Axes.set_axisbelow") | bool or 'line' |
| [`box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect") | float or None |
| [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
| [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
| [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
| [`facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
| [`forward_navigation_events`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_forward_navigation_events.html#matplotlib.axes.Axes.set_forward_navigation_events "matplotlib.axes.Axes.set_forward_navigation_events") | bool or "auto" |
| [`frame_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_frame_on.html#matplotlib.axes.Axes.set_frame_on "matplotlib.axes.Axes.set_frame_on") | bool |
| [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
| [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
| [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
| [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
| [`navigate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate.html#matplotlib.axes.Axes.set_navigate "matplotlib.axes.Axes.set_navigate") | bool |
| [`navigate_mode`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate_mode.html#matplotlib.axes.Axes.set_navigate_mode "matplotlib.axes.Axes.set_navigate_mode") | unknown |
| [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
| [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
| [`position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib.axes.Axes.set_position "matplotlib.axes.Axes.set_position") | \[left, bottom, width, height\] or [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox") |
| [`prop_cycle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle "matplotlib.axes.Axes.set_prop_cycle") | [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)") |
| [`rasterization_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html#matplotlib.axes.Axes.set_rasterization_zorder "matplotlib.axes.Axes.set_rasterization_zorder") | float or None |
| [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
| [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
| [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
| [`subplotspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_subplotspec.html#matplotlib.axes.Axes.set_subplotspec "matplotlib.axes.Axes.set_subplotspec") | unknown |
| [`title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title") | str |
| [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
| [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
| [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
| [`xbound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xbound.html#matplotlib.axes.Axes.set_xbound "matplotlib.axes.Axes.set_xbound") | (lower: float, upper: float) |
| [`xinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xinverted.html#matplotlib.axes.Axes.set_xinverted "matplotlib.axes.Axes.set_xinverted") | unknown |
| [`xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel") | str |
| [`xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim") | (left: float, right: float) |
| [`xmargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xmargin.html#matplotlib.axes.Axes.set_xmargin "matplotlib.axes.Axes.set_xmargin") | float greater than -0.5 |
| [`xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale") | unknown |
| [`xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels") | unknown |
| [`xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks") | unknown |
| [`ybound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ybound.html#matplotlib.axes.Axes.set_ybound "matplotlib.axes.Axes.set_ybound") | (lower: float, upper: float) |
| [`yinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yinverted.html#matplotlib.axes.Axes.set_yinverted "matplotlib.axes.Axes.set_yinverted") | unknown |
| [`ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel") | str |
| [`ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim") | (bottom: float, top: float) |
| [`ymargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html#matplotlib.axes.Axes.set_ymargin "matplotlib.axes.Axes.set_ymargin") | float greater than -0.5 |
| [`yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale") | unknown |
| [`yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels") | unknown |
| [`yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks") | unknown |
| [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

Returns:

[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The new [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 object.

class AitoffTransform(_resolution_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L258-L278)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.AitoffAxes.AitoffTransform "Link to this definition")

Bases: `_GeoTransform`

The base Aitoff transform.

Create a new geographical transform.

Resolution is the number of steps to interpolate between each input line segment to approximate its path in curved space.

has\_inverse \= True[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.AitoffAxes.AitoffTransform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L276-L278)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.AitoffAxes.AitoffTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L261-L274)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.AitoffAxes.AitoffTransform.transform_non_affine "Link to this definition")

Apply only the non-affine part of this transformation.

`transform(values)` is always equivalent to `transform_affine(transform_non_affine(values))`.

In non-affine transformations, this is generally equivalent to `transform(values)`. In affine transformations, this is always a no-op.

Parameters:

**values**array

The input values as an array of length [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
 or shape (N, [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
).

Returns:

array

The output values as an array of length [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
 or shape (N, [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
), depending on the input.

class InvertedAitoffTransform(_resolution_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L280-L289)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.AitoffAxes.InvertedAitoffTransform "Link to this definition")

Bases: `_GeoTransform`

Create a new geographical transform.

Resolution is the number of steps to interpolate between each input line segment to approximate its path in curved space.

has\_inverse \= True[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.AitoffAxes.InvertedAitoffTransform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L287-L289)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.AitoffAxes.InvertedAitoffTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L282-L285)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.AitoffAxes.InvertedAitoffTransform.transform_non_affine "Link to this definition")

Apply only the non-affine part of this transformation.

`transform(values)` is always equivalent to `transform_affine(transform_non_affine(values))`.

In non-affine transformations, this is generally equivalent to `transform(values)`. In affine transformations, this is always a no-op.

Parameters:

**values**array

The input values as an array of length [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
 or shape (N, [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
).

Returns:

array

The output values as an array of length [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
 or shape (N, [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
), depending on the input.

name \= 'aitoff'[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.AitoffAxes.name "Link to this definition")

set(_\*_, _adjustable\=<UNSET>_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _anchor\=<UNSET>_, _animated\=<UNSET>_, _aspect\=<UNSET>_, _autoscale\_on\=<UNSET>_, _autoscalex\_on\=<UNSET>_, _autoscaley\_on\=<UNSET>_, _axes\_locator\=<UNSET>_, _axisbelow\=<UNSET>_, _box\_aspect\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _facecolor\=<UNSET>_, _forward\_navigation\_events\=<UNSET>_, _frame\_on\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _latitude\_grid\=<UNSET>_, _longitude\_grid\=<UNSET>_, _longitude\_grid\_ends\=<UNSET>_, _mouseover\=<UNSET>_, _navigate\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _position\=<UNSET>_, _prop\_cycle\=<UNSET>_, _rasterization\_zorder\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _subplotspec\=<UNSET>_, _title\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _xbound\=<UNSET>_, _xinverted\=<UNSET>_, _xlabel\=<UNSET>_, _xlim\=<UNSET>_, _xmargin\=<UNSET>_, _xscale\=<UNSET>_, _xticklabels\=<UNSET>_, _xticks\=<UNSET>_, _ybound\=<UNSET>_, _yinverted\=<UNSET>_, _ylabel\=<UNSET>_, _ylim\=<UNSET>_, _ymargin\=<UNSET>_, _yscale\=<UNSET>_, _yticklabels\=<UNSET>_, _yticks\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.AitoffAxes.set "Link to this definition")

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
> | [`adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#matplotlib.axes.Axes.set_adjustable "matplotlib.axes.Axes.set_adjustable") | {'box', 'datalim'} |
> | [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "matplotlib.axes.Axes.set_anchor") | (float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', ...} |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect") | {'auto', 'equal'} or float |
> | [`autoscale_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscale_on.html#matplotlib.axes.Axes.set_autoscale_on "matplotlib.axes.Axes.set_autoscale_on") | bool |
> | [`autoscalex_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscalex_on.html#matplotlib.axes.Axes.set_autoscalex_on "matplotlib.axes.Axes.set_autoscalex_on") | unknown |
> | [`autoscaley_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscaley_on.html#matplotlib.axes.Axes.set_autoscaley_on "matplotlib.axes.Axes.set_autoscaley_on") | unknown |
> | [`axes_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axes_locator.html#matplotlib.axes.Axes.set_axes_locator "matplotlib.axes.Axes.set_axes_locator") | Callable\[\[Axes, Renderer\], Bbox\] |
> | [`axisbelow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axisbelow.html#matplotlib.axes.Axes.set_axisbelow "matplotlib.axes.Axes.set_axisbelow") | bool or 'line' |
> | [`box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect") | float or None |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`forward_navigation_events`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_forward_navigation_events.html#matplotlib.axes.Axes.set_forward_navigation_events "matplotlib.axes.Axes.set_forward_navigation_events") | bool or "auto" |
> | [`frame_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_frame_on.html#matplotlib.axes.Axes.set_frame_on "matplotlib.axes.Axes.set_frame_on") | bool |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`latitude_grid`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_latitude_grid "matplotlib.projections.geo.GeoAxes.set_latitude_grid") | unknown |
> | [`longitude_grid`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_longitude_grid "matplotlib.projections.geo.GeoAxes.set_longitude_grid") | unknown |
> | [`longitude_grid_ends`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_longitude_grid_ends "matplotlib.projections.geo.GeoAxes.set_longitude_grid_ends") | unknown |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`navigate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate.html#matplotlib.axes.Axes.set_navigate "matplotlib.axes.Axes.set_navigate") | bool |
> | [`navigate_mode`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate_mode.html#matplotlib.axes.Axes.set_navigate_mode "matplotlib.axes.Axes.set_navigate_mode") | unknown |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib.axes.Axes.set_position "matplotlib.axes.Axes.set_position") | \[left, bottom, width, height\] or [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox") |
> | [`prop_cycle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle "matplotlib.axes.Axes.set_prop_cycle") | [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)") |
> | [`rasterization_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html#matplotlib.axes.Axes.set_rasterization_zorder "matplotlib.axes.Axes.set_rasterization_zorder") | float or None |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`subplotspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_subplotspec.html#matplotlib.axes.Axes.set_subplotspec "matplotlib.axes.Axes.set_subplotspec") | unknown |
> | [`title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title") | str |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`xbound`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xlim "matplotlib.projections.geo.GeoAxes.set_xlim") | unknown |
> | [`xinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xinverted.html#matplotlib.axes.Axes.set_xinverted "matplotlib.axes.Axes.set_xinverted") | unknown |
> | [`xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel") | str |
> | [`xlim`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xlim "matplotlib.projections.geo.GeoAxes.set_xlim") | unknown |
> | [`xmargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xmargin.html#matplotlib.axes.Axes.set_xmargin "matplotlib.axes.Axes.set_xmargin") | float greater than -0.5 |
> | [`xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale") | unknown |
> | [`xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels") | unknown |
> | [`xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks") | unknown |
> | [`ybound`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xlim "matplotlib.projections.geo.GeoAxes.set_xlim") | unknown |
> | [`yinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yinverted.html#matplotlib.axes.Axes.set_yinverted "matplotlib.axes.Axes.set_yinverted") | unknown |
> | [`ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel") | str |
> | [`ylim`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xlim "matplotlib.projections.geo.GeoAxes.set_xlim") | unknown |
> | [`ymargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html#matplotlib.axes.Axes.set_ymargin "matplotlib.axes.Axes.set_ymargin") | float greater than -0.5 |
> | [`yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale") | unknown |
> | [`yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels") | unknown |
> | [`yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks") | unknown |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

class matplotlib.projections.geo.GeoAxes(_fig_, _\*args_, _facecolor\=None_, _frameon\=True_, _sharex\=None_, _sharey\=None_, _label\=''_, _xscale\=None_, _yscale\=None_, _box\_aspect\=None_, _forward\_navigation\_events\='auto'_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L15-L229)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes "Link to this definition")

Bases: [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes._axes.Axes")

An abstract base class for geographic projections.

Build an Axes in a figure.

Parameters:

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

The Axes is built in the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 _fig_.

**\*args**

`*args` can be a single `(left, bottom, width, height)` rectangle or a single [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
. This specifies the rectangle (in figure coordinates) where the Axes is positioned.

`*args` can also consist of three numbers or a single three-digit number; in the latter case, the digits are considered as independent numbers. The numbers are interpreted as `(nrows, ncols, index)`: `(nrows, ncols)` specifies the size of an array of subplots, and `index` is the 1-based index of the subplot being created. Finally, `*args` can also directly be a [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
 instance.

**sharex, sharey**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, optional

The x- or y-[`axis`](https://matplotlib.org/stable/api/axis_api.html#module-matplotlib.axis "matplotlib.axis")
 is shared with the x- or y-axis in the input [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
. Note that it is not possible to unshare axes.

**frameon**bool, default: True

Whether the Axes frame is visible.

**box\_aspect**float, optional

Set a fixed aspect for the Axes box, i.e. the ratio of height to width. See [`set_box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect")
 for details.

**forward\_navigation\_events**bool or "auto", default: "auto"

Control whether pan/zoom events are passed through to Axes below this one. "auto" is _True_ for axes with an invisible patch and _False_ otherwise.

**\*\*kwargs**

Other optional keyword arguments:

| Property | Description |
| --- | --- |
| [`adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#matplotlib.axes.Axes.set_adjustable "matplotlib.axes.Axes.set_adjustable") | {'box', 'datalim'} |
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
| [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
| [`anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "matplotlib.axes.Axes.set_anchor") | (float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', ...} |
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
| [`aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect") | {'auto', 'equal'} or float |
| [`autoscale_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscale_on.html#matplotlib.axes.Axes.set_autoscale_on "matplotlib.axes.Axes.set_autoscale_on") | bool |
| [`autoscalex_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscalex_on.html#matplotlib.axes.Axes.set_autoscalex_on "matplotlib.axes.Axes.set_autoscalex_on") | unknown |
| [`autoscaley_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscaley_on.html#matplotlib.axes.Axes.set_autoscaley_on "matplotlib.axes.Axes.set_autoscaley_on") | unknown |
| [`axes_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axes_locator.html#matplotlib.axes.Axes.set_axes_locator "matplotlib.axes.Axes.set_axes_locator") | Callable\[\[Axes, Renderer\], Bbox\] |
| [`axisbelow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axisbelow.html#matplotlib.axes.Axes.set_axisbelow "matplotlib.axes.Axes.set_axisbelow") | bool or 'line' |
| [`box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect") | float or None |
| [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
| [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
| [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
| [`facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
| [`forward_navigation_events`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_forward_navigation_events.html#matplotlib.axes.Axes.set_forward_navigation_events "matplotlib.axes.Axes.set_forward_navigation_events") | bool or "auto" |
| [`frame_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_frame_on.html#matplotlib.axes.Axes.set_frame_on "matplotlib.axes.Axes.set_frame_on") | bool |
| [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
| [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
| [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
| [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
| [`navigate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate.html#matplotlib.axes.Axes.set_navigate "matplotlib.axes.Axes.set_navigate") | bool |
| [`navigate_mode`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate_mode.html#matplotlib.axes.Axes.set_navigate_mode "matplotlib.axes.Axes.set_navigate_mode") | unknown |
| [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
| [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
| [`position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib.axes.Axes.set_position "matplotlib.axes.Axes.set_position") | \[left, bottom, width, height\] or [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox") |
| [`prop_cycle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle "matplotlib.axes.Axes.set_prop_cycle") | [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)") |
| [`rasterization_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html#matplotlib.axes.Axes.set_rasterization_zorder "matplotlib.axes.Axes.set_rasterization_zorder") | float or None |
| [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
| [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
| [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
| [`subplotspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_subplotspec.html#matplotlib.axes.Axes.set_subplotspec "matplotlib.axes.Axes.set_subplotspec") | unknown |
| [`title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title") | str |
| [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
| [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
| [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
| [`xbound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xbound.html#matplotlib.axes.Axes.set_xbound "matplotlib.axes.Axes.set_xbound") | (lower: float, upper: float) |
| [`xinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xinverted.html#matplotlib.axes.Axes.set_xinverted "matplotlib.axes.Axes.set_xinverted") | unknown |
| [`xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel") | str |
| [`xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim") | (left: float, right: float) |
| [`xmargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xmargin.html#matplotlib.axes.Axes.set_xmargin "matplotlib.axes.Axes.set_xmargin") | float greater than -0.5 |
| [`xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale") | unknown |
| [`xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels") | unknown |
| [`xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks") | unknown |
| [`ybound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ybound.html#matplotlib.axes.Axes.set_ybound "matplotlib.axes.Axes.set_ybound") | (lower: float, upper: float) |
| [`yinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yinverted.html#matplotlib.axes.Axes.set_yinverted "matplotlib.axes.Axes.set_yinverted") | unknown |
| [`ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel") | str |
| [`ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim") | (bottom: float, top: float) |
| [`ymargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html#matplotlib.axes.Axes.set_ymargin "matplotlib.axes.Axes.set_ymargin") | float greater than -0.5 |
| [`yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale") | unknown |
| [`yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels") | unknown |
| [`yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks") | unknown |
| [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

Returns:

[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The new [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 object.

RESOLUTION \= 75[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.RESOLUTION "Link to this definition")

class ThetaFormatter(_round\_to\=1.0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L18-L28)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.ThetaFormatter "Link to this definition")

Bases: [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")

Used to format the theta tick labels. Converts the native unit of radians into degrees and adds a degree symbol.

can\_pan()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L214-L220)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.can_pan "Link to this definition")

Return whether this Axes supports the pan/zoom button functionality.

This Axes object does not support interactive pan/zoom.

can\_zoom()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L206-L212)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.can_zoom "Link to this definition")

Return whether this Axes supports the zoom box button functionality.

This Axes object does not support interactive zoom box.

clear()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L37-L55)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.clear "Link to this definition")

Clear the Axes.

drag\_pan(_button_, _key_, _x_, _y_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L228-L229)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.drag_pan "Link to this definition")

Called when the mouse moves during a pan operation.

Parameters:

**button**[`MouseButton`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton "matplotlib.backend_bases.MouseButton")

The pressed mouse button.

**key**str or None

The pressed key, if any.

**x, y**float

The mouse coordinates in display coords.

Notes

This is intended to be overridden by new projection types.

end\_pan()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L225-L226)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.end_pan "Link to this definition")

Called when a pan operation completes (when the mouse button is up.)

Notes

This is intended to be overridden by new projection types.

format\_coord(_lon_, _lat_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L164-L170)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.format_coord "Link to this definition")

Return a format string formatting the coordinate.

get\_data\_ratio()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L200-L202)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.get_data_ratio "Link to this definition")

Return the aspect ratio of the data itself.

get\_xaxis\_text1\_transform(_pad_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L120-L121)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.get_xaxis_text1_transform "Link to this definition")

Returns:

**transform**Transform

The transform used for drawing x-axis labels, which will add _pad\_points_ of padding (in points) between the axis and the label. The x-direction is in data coordinates and the y-direction is in axis coordinates

**valign**{'center', 'top', 'bottom', 'baseline', 'center\_baseline'}

The text vertical alignment.

**halign**{'center', 'left', 'right'}

The text horizontal alignment.

Notes

This transformation is primarily used by the [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 class, and is meant to be overridden by new kinds of projections that may need to place axis elements in different locations.

get\_xaxis\_text2\_transform(_pad_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L123-L124)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.get_xaxis_text2_transform "Link to this definition")

Returns:

**transform**Transform

The transform used for drawing secondary x-axis labels, which will add _pad\_points_ of padding (in points) between the axis and the label. The x-direction is in data coordinates and the y-direction is in axis coordinates

**valign**{'center', 'top', 'bottom', 'baseline', 'center\_baseline'}

The text vertical alignment.

**halign**{'center', 'left', 'right'}

The text horizontal alignment.

Notes

This transformation is primarily used by the [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 class, and is meant to be overridden by new kinds of projections that may need to place axis elements in different locations.

get\_xaxis\_transform(_which\='grid'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L116-L118)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.get_xaxis_transform "Link to this definition")

Get the transformation used for drawing x-axis labels, ticks and gridlines. The x-direction is in data coordinates and the y-direction is in axis coordinates.

Note

This transformation is primarily used by the [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 class, and is meant to be overridden by new kinds of projections that may need to place axis elements in different locations.

Parameters:

**which**{'grid', 'tick1', 'tick2'}

get\_yaxis\_text1\_transform(_pad_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L130-L131)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.get_yaxis_text1_transform "Link to this definition")

Returns:

**transform**Transform

The transform used for drawing y-axis labels, which will add _pad\_points_ of padding (in points) between the axis and the label. The x-direction is in axis coordinates and the y-direction is in data coordinates

**valign**{'center', 'top', 'bottom', 'baseline', 'center\_baseline'}

The text vertical alignment.

**halign**{'center', 'left', 'right'}

The text horizontal alignment.

Notes

This transformation is primarily used by the [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 class, and is meant to be overridden by new kinds of projections that may need to place axis elements in different locations.

get\_yaxis\_text2\_transform(_pad_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L133-L134)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.get_yaxis_text2_transform "Link to this definition")

Returns:

**transform**Transform

The transform used for drawing secondary y-axis labels, which will add _pad\_points_ of padding (in points) between the axis and the label. The x-direction is in axis coordinates and the y-direction is in data coordinates

**valign**{'center', 'top', 'bottom', 'baseline', 'center\_baseline'}

The text vertical alignment.

**halign**{'center', 'left', 'right'}

The text horizontal alignment.

Notes

This transformation is primarily used by the [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 class, and is meant to be overridden by new kinds of projections that may need to place axis elements in different locations.

get\_yaxis\_transform(_which\='grid'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L126-L128)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.get_yaxis_transform "Link to this definition")

Get the transformation used for drawing y-axis labels, ticks and gridlines. The x-direction is in axis coordinates and the y-direction is in data coordinates.

Note

This transformation is primarily used by the [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 class, and is meant to be overridden by new kinds of projections that may need to place axis elements in different locations.

Parameters:

**which**{'grid', 'tick1', 'tick2'}

invert\_xaxis()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L157-L160)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.invert_xaxis "Link to this definition")

Not supported. Please consider using Cartopy.

invert\_yaxis()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L157-L160)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.invert_yaxis "Link to this definition")

Not supported. Please consider using Cartopy.

set(_\*_, _adjustable\=<UNSET>_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _anchor\=<UNSET>_, _animated\=<UNSET>_, _aspect\=<UNSET>_, _autoscale\_on\=<UNSET>_, _autoscalex\_on\=<UNSET>_, _autoscaley\_on\=<UNSET>_, _axes\_locator\=<UNSET>_, _axisbelow\=<UNSET>_, _box\_aspect\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _facecolor\=<UNSET>_, _forward\_navigation\_events\=<UNSET>_, _frame\_on\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _latitude\_grid\=<UNSET>_, _longitude\_grid\=<UNSET>_, _longitude\_grid\_ends\=<UNSET>_, _mouseover\=<UNSET>_, _navigate\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _position\=<UNSET>_, _prop\_cycle\=<UNSET>_, _rasterization\_zorder\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _subplotspec\=<UNSET>_, _title\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _xbound\=<UNSET>_, _xinverted\=<UNSET>_, _xlabel\=<UNSET>_, _xlim\=<UNSET>_, _xmargin\=<UNSET>_, _xscale\=<UNSET>_, _xticklabels\=<UNSET>_, _xticks\=<UNSET>_, _ybound\=<UNSET>_, _yinverted\=<UNSET>_, _ylabel\=<UNSET>_, _ylim\=<UNSET>_, _ymargin\=<UNSET>_, _yscale\=<UNSET>_, _yticklabels\=<UNSET>_, _yticks\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set "Link to this definition")

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
> | [`adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#matplotlib.axes.Axes.set_adjustable "matplotlib.axes.Axes.set_adjustable") | {'box', 'datalim'} |
> | [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "matplotlib.axes.Axes.set_anchor") | (float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', ...} |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect") | {'auto', 'equal'} or float |
> | [`autoscale_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscale_on.html#matplotlib.axes.Axes.set_autoscale_on "matplotlib.axes.Axes.set_autoscale_on") | bool |
> | [`autoscalex_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscalex_on.html#matplotlib.axes.Axes.set_autoscalex_on "matplotlib.axes.Axes.set_autoscalex_on") | unknown |
> | [`autoscaley_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscaley_on.html#matplotlib.axes.Axes.set_autoscaley_on "matplotlib.axes.Axes.set_autoscaley_on") | unknown |
> | [`axes_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axes_locator.html#matplotlib.axes.Axes.set_axes_locator "matplotlib.axes.Axes.set_axes_locator") | Callable\[\[Axes, Renderer\], Bbox\] |
> | [`axisbelow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axisbelow.html#matplotlib.axes.Axes.set_axisbelow "matplotlib.axes.Axes.set_axisbelow") | bool or 'line' |
> | [`box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect") | float or None |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`forward_navigation_events`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_forward_navigation_events.html#matplotlib.axes.Axes.set_forward_navigation_events "matplotlib.axes.Axes.set_forward_navigation_events") | bool or "auto" |
> | [`frame_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_frame_on.html#matplotlib.axes.Axes.set_frame_on "matplotlib.axes.Axes.set_frame_on") | bool |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`latitude_grid`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_latitude_grid "matplotlib.projections.geo.GeoAxes.set_latitude_grid") | unknown |
> | [`longitude_grid`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_longitude_grid "matplotlib.projections.geo.GeoAxes.set_longitude_grid") | unknown |
> | [`longitude_grid_ends`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_longitude_grid_ends "matplotlib.projections.geo.GeoAxes.set_longitude_grid_ends") | unknown |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`navigate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate.html#matplotlib.axes.Axes.set_navigate "matplotlib.axes.Axes.set_navigate") | bool |
> | [`navigate_mode`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate_mode.html#matplotlib.axes.Axes.set_navigate_mode "matplotlib.axes.Axes.set_navigate_mode") | unknown |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib.axes.Axes.set_position "matplotlib.axes.Axes.set_position") | \[left, bottom, width, height\] or [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox") |
> | [`prop_cycle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle "matplotlib.axes.Axes.set_prop_cycle") | [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)") |
> | [`rasterization_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html#matplotlib.axes.Axes.set_rasterization_zorder "matplotlib.axes.Axes.set_rasterization_zorder") | float or None |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`subplotspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_subplotspec.html#matplotlib.axes.Axes.set_subplotspec "matplotlib.axes.Axes.set_subplotspec") | unknown |
> | [`title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title") | str |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`xbound`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xlim "matplotlib.projections.geo.GeoAxes.set_xlim") | unknown |
> | [`xinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xinverted.html#matplotlib.axes.Axes.set_xinverted "matplotlib.axes.Axes.set_xinverted") | unknown |
> | [`xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel") | str |
> | [`xlim`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xlim "matplotlib.projections.geo.GeoAxes.set_xlim") | unknown |
> | [`xmargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xmargin.html#matplotlib.axes.Axes.set_xmargin "matplotlib.axes.Axes.set_xmargin") | float greater than -0.5 |
> | [`xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale") | unknown |
> | [`xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels") | unknown |
> | [`xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks") | unknown |
> | [`ybound`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xlim "matplotlib.projections.geo.GeoAxes.set_xlim") | unknown |
> | [`yinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yinverted.html#matplotlib.axes.Axes.set_yinverted "matplotlib.axes.Axes.set_yinverted") | unknown |
> | [`ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel") | str |
> | [`ylim`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xlim "matplotlib.projections.geo.GeoAxes.set_xlim") | unknown |
> | [`ymargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html#matplotlib.axes.Axes.set_ymargin "matplotlib.axes.Axes.set_ymargin") | float greater than -0.5 |
> | [`yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale") | unknown |
> | [`yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels") | unknown |
> | [`yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks") | unknown |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_latitude\_grid(_degrees_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L181-L188)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_latitude_grid "Link to this definition")

Set the number of degrees between each latitude grid.

set\_longitude\_grid(_degrees_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L172-L179)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_longitude_grid "Link to this definition")

Set the number of degrees between each longitude grid.

set\_longitude\_grid\_ends(_degrees_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L190-L198)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_longitude_grid_ends "Link to this definition")

Set the latitude(s) at which to stop drawing the longitude grids.

set\_xbound(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L148-L151)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xbound "Link to this definition")

Not supported. Please consider using Cartopy.

set\_xlim(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L148-L151)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xlim "Link to this definition")

Not supported. Please consider using Cartopy.

set\_xscale(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L142-L144)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xscale "Link to this definition")

Set the xaxis' scale.

Parameters:

**value**str or [`ScaleBase`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")

The axis scale type to apply. Valid string values are the names of scale classes ("linear", "log", "function",...). These may be the names of any of the [built-in scales](https://matplotlib.org/stable/api/scale_api.html#builtin-scales)
 or of any custom scales registered using [`matplotlib.scale.register_scale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.register_scale "matplotlib.scale.register_scale")
.

**\*\*kwargs**

If _value_ is a string, keywords are passed to the instantiation method of the respective class.

set\_ybound(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L148-L151)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_ybound "Link to this definition")

Not supported. Please consider using Cartopy.

set\_ylim(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L148-L151)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_ylim "Link to this definition")

Not supported. Please consider using Cartopy.

set\_yscale(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L142-L144)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_yscale "Link to this definition")

Set the yaxis' scale.

Parameters:

**value**str or [`ScaleBase`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")

The axis scale type to apply. Valid string values are the names of scale classes ("linear", "log", "function",...). These may be the names of any of the [built-in scales](https://matplotlib.org/stable/api/scale_api.html#builtin-scales)
 or of any custom scales registered using [`matplotlib.scale.register_scale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.register_scale "matplotlib.scale.register_scale")
.

**\*\*kwargs**

If _value_ is a string, keywords are passed to the instantiation method of the respective class.

start\_pan(_x_, _y_, _button_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L222-L223)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.start_pan "Link to this definition")

Called when a pan operation has started.

Parameters:

**x, y**float

The mouse coordinates in display coords.

**button**[`MouseButton`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton "matplotlib.backend_bases.MouseButton")

The pressed mouse button.

Notes

This is intended to be overridden by new projection types.

class matplotlib.projections.geo.HammerAxes(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L301-L343)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.HammerAxes "Link to this definition")

Bases: [`GeoAxes`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes "matplotlib.projections.geo.GeoAxes")

Build an Axes in a figure.

Parameters:

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

The Axes is built in the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 _fig_.

**\*args**

`*args` can be a single `(left, bottom, width, height)` rectangle or a single [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
. This specifies the rectangle (in figure coordinates) where the Axes is positioned.

`*args` can also consist of three numbers or a single three-digit number; in the latter case, the digits are considered as independent numbers. The numbers are interpreted as `(nrows, ncols, index)`: `(nrows, ncols)` specifies the size of an array of subplots, and `index` is the 1-based index of the subplot being created. Finally, `*args` can also directly be a [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
 instance.

**sharex, sharey**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, optional

The x- or y-[`axis`](https://matplotlib.org/stable/api/axis_api.html#module-matplotlib.axis "matplotlib.axis")
 is shared with the x- or y-axis in the input [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
. Note that it is not possible to unshare axes.

**frameon**bool, default: True

Whether the Axes frame is visible.

**box\_aspect**float, optional

Set a fixed aspect for the Axes box, i.e. the ratio of height to width. See [`set_box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect")
 for details.

**forward\_navigation\_events**bool or "auto", default: "auto"

Control whether pan/zoom events are passed through to Axes below this one. "auto" is _True_ for axes with an invisible patch and _False_ otherwise.

**\*\*kwargs**

Other optional keyword arguments:

| Property | Description |
| --- | --- |
| [`adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#matplotlib.axes.Axes.set_adjustable "matplotlib.axes.Axes.set_adjustable") | {'box', 'datalim'} |
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
| [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
| [`anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "matplotlib.axes.Axes.set_anchor") | (float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', ...} |
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
| [`aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect") | {'auto', 'equal'} or float |
| [`autoscale_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscale_on.html#matplotlib.axes.Axes.set_autoscale_on "matplotlib.axes.Axes.set_autoscale_on") | bool |
| [`autoscalex_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscalex_on.html#matplotlib.axes.Axes.set_autoscalex_on "matplotlib.axes.Axes.set_autoscalex_on") | unknown |
| [`autoscaley_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscaley_on.html#matplotlib.axes.Axes.set_autoscaley_on "matplotlib.axes.Axes.set_autoscaley_on") | unknown |
| [`axes_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axes_locator.html#matplotlib.axes.Axes.set_axes_locator "matplotlib.axes.Axes.set_axes_locator") | Callable\[\[Axes, Renderer\], Bbox\] |
| [`axisbelow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axisbelow.html#matplotlib.axes.Axes.set_axisbelow "matplotlib.axes.Axes.set_axisbelow") | bool or 'line' |
| [`box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect") | float or None |
| [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
| [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
| [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
| [`facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
| [`forward_navigation_events`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_forward_navigation_events.html#matplotlib.axes.Axes.set_forward_navigation_events "matplotlib.axes.Axes.set_forward_navigation_events") | bool or "auto" |
| [`frame_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_frame_on.html#matplotlib.axes.Axes.set_frame_on "matplotlib.axes.Axes.set_frame_on") | bool |
| [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
| [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
| [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
| [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
| [`navigate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate.html#matplotlib.axes.Axes.set_navigate "matplotlib.axes.Axes.set_navigate") | bool |
| [`navigate_mode`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate_mode.html#matplotlib.axes.Axes.set_navigate_mode "matplotlib.axes.Axes.set_navigate_mode") | unknown |
| [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
| [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
| [`position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib.axes.Axes.set_position "matplotlib.axes.Axes.set_position") | \[left, bottom, width, height\] or [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox") |
| [`prop_cycle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle "matplotlib.axes.Axes.set_prop_cycle") | [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)") |
| [`rasterization_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html#matplotlib.axes.Axes.set_rasterization_zorder "matplotlib.axes.Axes.set_rasterization_zorder") | float or None |
| [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
| [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
| [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
| [`subplotspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_subplotspec.html#matplotlib.axes.Axes.set_subplotspec "matplotlib.axes.Axes.set_subplotspec") | unknown |
| [`title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title") | str |
| [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
| [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
| [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
| [`xbound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xbound.html#matplotlib.axes.Axes.set_xbound "matplotlib.axes.Axes.set_xbound") | (lower: float, upper: float) |
| [`xinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xinverted.html#matplotlib.axes.Axes.set_xinverted "matplotlib.axes.Axes.set_xinverted") | unknown |
| [`xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel") | str |
| [`xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim") | (left: float, right: float) |
| [`xmargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xmargin.html#matplotlib.axes.Axes.set_xmargin "matplotlib.axes.Axes.set_xmargin") | float greater than -0.5 |
| [`xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale") | unknown |
| [`xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels") | unknown |
| [`xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks") | unknown |
| [`ybound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ybound.html#matplotlib.axes.Axes.set_ybound "matplotlib.axes.Axes.set_ybound") | (lower: float, upper: float) |
| [`yinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yinverted.html#matplotlib.axes.Axes.set_yinverted "matplotlib.axes.Axes.set_yinverted") | unknown |
| [`ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel") | str |
| [`ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim") | (bottom: float, top: float) |
| [`ymargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html#matplotlib.axes.Axes.set_ymargin "matplotlib.axes.Axes.set_ymargin") | float greater than -0.5 |
| [`yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale") | unknown |
| [`yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels") | unknown |
| [`yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks") | unknown |
| [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

Returns:

[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The new [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 object.

class HammerTransform(_resolution_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L304-L320)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.HammerAxes.HammerTransform "Link to this definition")

Bases: `_GeoTransform`

The base Hammer transform.

Create a new geographical transform.

Resolution is the number of steps to interpolate between each input line segment to approximate its path in curved space.

has\_inverse \= True[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.HammerAxes.HammerTransform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L318-L320)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.HammerAxes.HammerTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L307-L316)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.HammerAxes.HammerTransform.transform_non_affine "Link to this definition")

Apply only the non-affine part of this transformation.

`transform(values)` is always equivalent to `transform_affine(transform_non_affine(values))`.

In non-affine transformations, this is generally equivalent to `transform(values)`. In affine transformations, this is always a no-op.

Parameters:

**values**array

The input values as an array of length [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
 or shape (N, [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
).

Returns:

array

The output values as an array of length [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
 or shape (N, [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
), depending on the input.

class InvertedHammerTransform(_resolution_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L322-L334)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.HammerAxes.InvertedHammerTransform "Link to this definition")

Bases: `_GeoTransform`

Create a new geographical transform.

Resolution is the number of steps to interpolate between each input line segment to approximate its path in curved space.

has\_inverse \= True[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.HammerAxes.InvertedHammerTransform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L332-L334)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.HammerAxes.InvertedHammerTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L324-L330)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.HammerAxes.InvertedHammerTransform.transform_non_affine "Link to this definition")

Apply only the non-affine part of this transformation.

`transform(values)` is always equivalent to `transform_affine(transform_non_affine(values))`.

In non-affine transformations, this is generally equivalent to `transform(values)`. In affine transformations, this is always a no-op.

Parameters:

**values**array

The input values as an array of length [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
 or shape (N, [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
).

Returns:

array

The output values as an array of length [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
 or shape (N, [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
), depending on the input.

name \= 'hammer'[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.HammerAxes.name "Link to this definition")

set(_\*_, _adjustable\=<UNSET>_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _anchor\=<UNSET>_, _animated\=<UNSET>_, _aspect\=<UNSET>_, _autoscale\_on\=<UNSET>_, _autoscalex\_on\=<UNSET>_, _autoscaley\_on\=<UNSET>_, _axes\_locator\=<UNSET>_, _axisbelow\=<UNSET>_, _box\_aspect\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _facecolor\=<UNSET>_, _forward\_navigation\_events\=<UNSET>_, _frame\_on\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _latitude\_grid\=<UNSET>_, _longitude\_grid\=<UNSET>_, _longitude\_grid\_ends\=<UNSET>_, _mouseover\=<UNSET>_, _navigate\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _position\=<UNSET>_, _prop\_cycle\=<UNSET>_, _rasterization\_zorder\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _subplotspec\=<UNSET>_, _title\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _xbound\=<UNSET>_, _xinverted\=<UNSET>_, _xlabel\=<UNSET>_, _xlim\=<UNSET>_, _xmargin\=<UNSET>_, _xscale\=<UNSET>_, _xticklabels\=<UNSET>_, _xticks\=<UNSET>_, _ybound\=<UNSET>_, _yinverted\=<UNSET>_, _ylabel\=<UNSET>_, _ylim\=<UNSET>_, _ymargin\=<UNSET>_, _yscale\=<UNSET>_, _yticklabels\=<UNSET>_, _yticks\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.HammerAxes.set "Link to this definition")

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
> | [`adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#matplotlib.axes.Axes.set_adjustable "matplotlib.axes.Axes.set_adjustable") | {'box', 'datalim'} |
> | [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "matplotlib.axes.Axes.set_anchor") | (float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', ...} |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect") | {'auto', 'equal'} or float |
> | [`autoscale_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscale_on.html#matplotlib.axes.Axes.set_autoscale_on "matplotlib.axes.Axes.set_autoscale_on") | bool |
> | [`autoscalex_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscalex_on.html#matplotlib.axes.Axes.set_autoscalex_on "matplotlib.axes.Axes.set_autoscalex_on") | unknown |
> | [`autoscaley_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscaley_on.html#matplotlib.axes.Axes.set_autoscaley_on "matplotlib.axes.Axes.set_autoscaley_on") | unknown |
> | [`axes_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axes_locator.html#matplotlib.axes.Axes.set_axes_locator "matplotlib.axes.Axes.set_axes_locator") | Callable\[\[Axes, Renderer\], Bbox\] |
> | [`axisbelow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axisbelow.html#matplotlib.axes.Axes.set_axisbelow "matplotlib.axes.Axes.set_axisbelow") | bool or 'line' |
> | [`box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect") | float or None |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`forward_navigation_events`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_forward_navigation_events.html#matplotlib.axes.Axes.set_forward_navigation_events "matplotlib.axes.Axes.set_forward_navigation_events") | bool or "auto" |
> | [`frame_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_frame_on.html#matplotlib.axes.Axes.set_frame_on "matplotlib.axes.Axes.set_frame_on") | bool |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`latitude_grid`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_latitude_grid "matplotlib.projections.geo.GeoAxes.set_latitude_grid") | unknown |
> | [`longitude_grid`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_longitude_grid "matplotlib.projections.geo.GeoAxes.set_longitude_grid") | unknown |
> | [`longitude_grid_ends`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_longitude_grid_ends "matplotlib.projections.geo.GeoAxes.set_longitude_grid_ends") | unknown |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`navigate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate.html#matplotlib.axes.Axes.set_navigate "matplotlib.axes.Axes.set_navigate") | bool |
> | [`navigate_mode`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate_mode.html#matplotlib.axes.Axes.set_navigate_mode "matplotlib.axes.Axes.set_navigate_mode") | unknown |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib.axes.Axes.set_position "matplotlib.axes.Axes.set_position") | \[left, bottom, width, height\] or [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox") |
> | [`prop_cycle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle "matplotlib.axes.Axes.set_prop_cycle") | [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)") |
> | [`rasterization_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html#matplotlib.axes.Axes.set_rasterization_zorder "matplotlib.axes.Axes.set_rasterization_zorder") | float or None |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`subplotspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_subplotspec.html#matplotlib.axes.Axes.set_subplotspec "matplotlib.axes.Axes.set_subplotspec") | unknown |
> | [`title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title") | str |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`xbound`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xlim "matplotlib.projections.geo.GeoAxes.set_xlim") | unknown |
> | [`xinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xinverted.html#matplotlib.axes.Axes.set_xinverted "matplotlib.axes.Axes.set_xinverted") | unknown |
> | [`xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel") | str |
> | [`xlim`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xlim "matplotlib.projections.geo.GeoAxes.set_xlim") | unknown |
> | [`xmargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xmargin.html#matplotlib.axes.Axes.set_xmargin "matplotlib.axes.Axes.set_xmargin") | float greater than -0.5 |
> | [`xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale") | unknown |
> | [`xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels") | unknown |
> | [`xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks") | unknown |
> | [`ybound`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xlim "matplotlib.projections.geo.GeoAxes.set_xlim") | unknown |
> | [`yinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yinverted.html#matplotlib.axes.Axes.set_yinverted "matplotlib.axes.Axes.set_yinverted") | unknown |
> | [`ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel") | str |
> | [`ylim`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xlim "matplotlib.projections.geo.GeoAxes.set_xlim") | unknown |
> | [`ymargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html#matplotlib.axes.Axes.set_ymargin "matplotlib.axes.Axes.set_ymargin") | float greater than -0.5 |
> | [`yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale") | unknown |
> | [`yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels") | unknown |
> | [`yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks") | unknown |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

class matplotlib.projections.geo.LambertAxes(_\*args_, _center\_longitude\=0_, _center\_latitude\=0_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L416-L511)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.LambertAxes "Link to this definition")

Bases: [`GeoAxes`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes "matplotlib.projections.geo.GeoAxes")

Build an Axes in a figure.

Parameters:

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

The Axes is built in the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 _fig_.

**\*args**

`*args` can be a single `(left, bottom, width, height)` rectangle or a single [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
. This specifies the rectangle (in figure coordinates) where the Axes is positioned.

`*args` can also consist of three numbers or a single three-digit number; in the latter case, the digits are considered as independent numbers. The numbers are interpreted as `(nrows, ncols, index)`: `(nrows, ncols)` specifies the size of an array of subplots, and `index` is the 1-based index of the subplot being created. Finally, `*args` can also directly be a [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
 instance.

**sharex, sharey**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, optional

The x- or y-[`axis`](https://matplotlib.org/stable/api/axis_api.html#module-matplotlib.axis "matplotlib.axis")
 is shared with the x- or y-axis in the input [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
. Note that it is not possible to unshare axes.

**frameon**bool, default: True

Whether the Axes frame is visible.

**box\_aspect**float, optional

Set a fixed aspect for the Axes box, i.e. the ratio of height to width. See [`set_box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect")
 for details.

**forward\_navigation\_events**bool or "auto", default: "auto"

Control whether pan/zoom events are passed through to Axes below this one. "auto" is _True_ for axes with an invisible patch and _False_ otherwise.

**\*\*kwargs**

Other optional keyword arguments:

| Property | Description |
| --- | --- |
| [`adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#matplotlib.axes.Axes.set_adjustable "matplotlib.axes.Axes.set_adjustable") | {'box', 'datalim'} |
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
| [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
| [`anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "matplotlib.axes.Axes.set_anchor") | (float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', ...} |
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
| [`aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect") | {'auto', 'equal'} or float |
| [`autoscale_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscale_on.html#matplotlib.axes.Axes.set_autoscale_on "matplotlib.axes.Axes.set_autoscale_on") | bool |
| [`autoscalex_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscalex_on.html#matplotlib.axes.Axes.set_autoscalex_on "matplotlib.axes.Axes.set_autoscalex_on") | unknown |
| [`autoscaley_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscaley_on.html#matplotlib.axes.Axes.set_autoscaley_on "matplotlib.axes.Axes.set_autoscaley_on") | unknown |
| [`axes_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axes_locator.html#matplotlib.axes.Axes.set_axes_locator "matplotlib.axes.Axes.set_axes_locator") | Callable\[\[Axes, Renderer\], Bbox\] |
| [`axisbelow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axisbelow.html#matplotlib.axes.Axes.set_axisbelow "matplotlib.axes.Axes.set_axisbelow") | bool or 'line' |
| [`box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect") | float or None |
| [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
| [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
| [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
| [`facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
| [`forward_navigation_events`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_forward_navigation_events.html#matplotlib.axes.Axes.set_forward_navigation_events "matplotlib.axes.Axes.set_forward_navigation_events") | bool or "auto" |
| [`frame_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_frame_on.html#matplotlib.axes.Axes.set_frame_on "matplotlib.axes.Axes.set_frame_on") | bool |
| [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
| [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
| [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
| [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
| [`navigate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate.html#matplotlib.axes.Axes.set_navigate "matplotlib.axes.Axes.set_navigate") | bool |
| [`navigate_mode`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate_mode.html#matplotlib.axes.Axes.set_navigate_mode "matplotlib.axes.Axes.set_navigate_mode") | unknown |
| [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
| [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
| [`position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib.axes.Axes.set_position "matplotlib.axes.Axes.set_position") | \[left, bottom, width, height\] or [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox") |
| [`prop_cycle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle "matplotlib.axes.Axes.set_prop_cycle") | [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)") |
| [`rasterization_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html#matplotlib.axes.Axes.set_rasterization_zorder "matplotlib.axes.Axes.set_rasterization_zorder") | float or None |
| [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
| [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
| [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
| [`subplotspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_subplotspec.html#matplotlib.axes.Axes.set_subplotspec "matplotlib.axes.Axes.set_subplotspec") | unknown |
| [`title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title") | str |
| [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
| [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
| [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
| [`xbound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xbound.html#matplotlib.axes.Axes.set_xbound "matplotlib.axes.Axes.set_xbound") | (lower: float, upper: float) |
| [`xinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xinverted.html#matplotlib.axes.Axes.set_xinverted "matplotlib.axes.Axes.set_xinverted") | unknown |
| [`xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel") | str |
| [`xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim") | (left: float, right: float) |
| [`xmargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xmargin.html#matplotlib.axes.Axes.set_xmargin "matplotlib.axes.Axes.set_xmargin") | float greater than -0.5 |
| [`xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale") | unknown |
| [`xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels") | unknown |
| [`xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks") | unknown |
| [`ybound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ybound.html#matplotlib.axes.Axes.set_ybound "matplotlib.axes.Axes.set_ybound") | (lower: float, upper: float) |
| [`yinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yinverted.html#matplotlib.axes.Axes.set_yinverted "matplotlib.axes.Axes.set_yinverted") | unknown |
| [`ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel") | str |
| [`ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim") | (bottom: float, top: float) |
| [`ymargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html#matplotlib.axes.Axes.set_ymargin "matplotlib.axes.Axes.set_ymargin") | float greater than -0.5 |
| [`yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale") | unknown |
| [`yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels") | unknown |
| [`yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks") | unknown |
| [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

Returns:

[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The new [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 object.

class InvertedLambertTransform(_center\_longitude_, _center\_latitude_, _resolution_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L458-L487)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.LambertAxes.InvertedLambertTransform "Link to this definition")

Bases: `_GeoTransform`

Create a new geographical transform.

Resolution is the number of steps to interpolate between each input line segment to approximate its path in curved space.

has\_inverse \= True[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.LambertAxes.InvertedLambertTransform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L482-L487)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.LambertAxes.InvertedLambertTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L465-L480)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.LambertAxes.InvertedLambertTransform.transform_non_affine "Link to this definition")

Apply only the non-affine part of this transformation.

`transform(values)` is always equivalent to `transform_affine(transform_non_affine(values))`.

In non-affine transformations, this is generally equivalent to `transform(values)`. In affine transformations, this is always a no-op.

Parameters:

**values**array

The input values as an array of length [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
 or shape (N, [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
).

Returns:

array

The output values as an array of length [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
 or shape (N, [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
), depending on the input.

class LambertTransform(_center\_longitude_, _center\_latitude_, _resolution_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L419-L456)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.LambertAxes.LambertTransform "Link to this definition")

Bases: `_GeoTransform`

The base Lambert transform.

Create a new Lambert transform. Resolution is the number of steps to interpolate between each input line segment to approximate its path in curved Lambert space.

has\_inverse \= True[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.LambertAxes.LambertTransform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L451-L456)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.LambertAxes.LambertTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L432-L449)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.LambertAxes.LambertTransform.transform_non_affine "Link to this definition")

Apply only the non-affine part of this transformation.

`transform(values)` is always equivalent to `transform_affine(transform_non_affine(values))`.

In non-affine transformations, this is generally equivalent to `transform(values)`. In affine transformations, this is always a no-op.

Parameters:

**values**array

The input values as an array of length [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
 or shape (N, [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
).

Returns:

array

The output values as an array of length [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
 or shape (N, [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
), depending on the input.

clear()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L497-L500)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.LambertAxes.clear "Link to this definition")

Clear the Axes.

name \= 'lambert'[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.LambertAxes.name "Link to this definition")

set(_\*_, _adjustable\=<UNSET>_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _anchor\=<UNSET>_, _animated\=<UNSET>_, _aspect\=<UNSET>_, _autoscale\_on\=<UNSET>_, _autoscalex\_on\=<UNSET>_, _autoscaley\_on\=<UNSET>_, _axes\_locator\=<UNSET>_, _axisbelow\=<UNSET>_, _box\_aspect\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _facecolor\=<UNSET>_, _forward\_navigation\_events\=<UNSET>_, _frame\_on\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _latitude\_grid\=<UNSET>_, _longitude\_grid\=<UNSET>_, _longitude\_grid\_ends\=<UNSET>_, _mouseover\=<UNSET>_, _navigate\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _position\=<UNSET>_, _prop\_cycle\=<UNSET>_, _rasterization\_zorder\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _subplotspec\=<UNSET>_, _title\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _xbound\=<UNSET>_, _xinverted\=<UNSET>_, _xlabel\=<UNSET>_, _xlim\=<UNSET>_, _xmargin\=<UNSET>_, _xscale\=<UNSET>_, _xticklabels\=<UNSET>_, _xticks\=<UNSET>_, _ybound\=<UNSET>_, _yinverted\=<UNSET>_, _ylabel\=<UNSET>_, _ylim\=<UNSET>_, _ymargin\=<UNSET>_, _yscale\=<UNSET>_, _yticklabels\=<UNSET>_, _yticks\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.LambertAxes.set "Link to this definition")

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
> | [`adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#matplotlib.axes.Axes.set_adjustable "matplotlib.axes.Axes.set_adjustable") | {'box', 'datalim'} |
> | [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "matplotlib.axes.Axes.set_anchor") | (float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', ...} |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect") | {'auto', 'equal'} or float |
> | [`autoscale_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscale_on.html#matplotlib.axes.Axes.set_autoscale_on "matplotlib.axes.Axes.set_autoscale_on") | bool |
> | [`autoscalex_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscalex_on.html#matplotlib.axes.Axes.set_autoscalex_on "matplotlib.axes.Axes.set_autoscalex_on") | unknown |
> | [`autoscaley_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscaley_on.html#matplotlib.axes.Axes.set_autoscaley_on "matplotlib.axes.Axes.set_autoscaley_on") | unknown |
> | [`axes_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axes_locator.html#matplotlib.axes.Axes.set_axes_locator "matplotlib.axes.Axes.set_axes_locator") | Callable\[\[Axes, Renderer\], Bbox\] |
> | [`axisbelow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axisbelow.html#matplotlib.axes.Axes.set_axisbelow "matplotlib.axes.Axes.set_axisbelow") | bool or 'line' |
> | [`box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect") | float or None |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`forward_navigation_events`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_forward_navigation_events.html#matplotlib.axes.Axes.set_forward_navigation_events "matplotlib.axes.Axes.set_forward_navigation_events") | bool or "auto" |
> | [`frame_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_frame_on.html#matplotlib.axes.Axes.set_frame_on "matplotlib.axes.Axes.set_frame_on") | bool |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`latitude_grid`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_latitude_grid "matplotlib.projections.geo.GeoAxes.set_latitude_grid") | unknown |
> | [`longitude_grid`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_longitude_grid "matplotlib.projections.geo.GeoAxes.set_longitude_grid") | unknown |
> | [`longitude_grid_ends`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_longitude_grid_ends "matplotlib.projections.geo.GeoAxes.set_longitude_grid_ends") | unknown |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`navigate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate.html#matplotlib.axes.Axes.set_navigate "matplotlib.axes.Axes.set_navigate") | bool |
> | [`navigate_mode`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate_mode.html#matplotlib.axes.Axes.set_navigate_mode "matplotlib.axes.Axes.set_navigate_mode") | unknown |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib.axes.Axes.set_position "matplotlib.axes.Axes.set_position") | \[left, bottom, width, height\] or [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox") |
> | [`prop_cycle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle "matplotlib.axes.Axes.set_prop_cycle") | [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)") |
> | [`rasterization_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html#matplotlib.axes.Axes.set_rasterization_zorder "matplotlib.axes.Axes.set_rasterization_zorder") | float or None |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`subplotspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_subplotspec.html#matplotlib.axes.Axes.set_subplotspec "matplotlib.axes.Axes.set_subplotspec") | unknown |
> | [`title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title") | str |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`xbound`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xlim "matplotlib.projections.geo.GeoAxes.set_xlim") | unknown |
> | [`xinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xinverted.html#matplotlib.axes.Axes.set_xinverted "matplotlib.axes.Axes.set_xinverted") | unknown |
> | [`xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel") | str |
> | [`xlim`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xlim "matplotlib.projections.geo.GeoAxes.set_xlim") | unknown |
> | [`xmargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xmargin.html#matplotlib.axes.Axes.set_xmargin "matplotlib.axes.Axes.set_xmargin") | float greater than -0.5 |
> | [`xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale") | unknown |
> | [`xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels") | unknown |
> | [`xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks") | unknown |
> | [`ybound`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xlim "matplotlib.projections.geo.GeoAxes.set_xlim") | unknown |
> | [`yinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yinverted.html#matplotlib.axes.Axes.set_yinverted "matplotlib.axes.Axes.set_yinverted") | unknown |
> | [`ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel") | str |
> | [`ylim`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xlim "matplotlib.projections.geo.GeoAxes.set_xlim") | unknown |
> | [`ymargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html#matplotlib.axes.Axes.set_ymargin "matplotlib.axes.Axes.set_ymargin") | float greater than -0.5 |
> | [`yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale") | unknown |
> | [`yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels") | unknown |
> | [`yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks") | unknown |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

class matplotlib.projections.geo.MollweideAxes(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L346-L413)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.MollweideAxes "Link to this definition")

Bases: [`GeoAxes`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes "matplotlib.projections.geo.GeoAxes")

Build an Axes in a figure.

Parameters:

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

The Axes is built in the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 _fig_.

**\*args**

`*args` can be a single `(left, bottom, width, height)` rectangle or a single [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
. This specifies the rectangle (in figure coordinates) where the Axes is positioned.

`*args` can also consist of three numbers or a single three-digit number; in the latter case, the digits are considered as independent numbers. The numbers are interpreted as `(nrows, ncols, index)`: `(nrows, ncols)` specifies the size of an array of subplots, and `index` is the 1-based index of the subplot being created. Finally, `*args` can also directly be a [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
 instance.

**sharex, sharey**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, optional

The x- or y-[`axis`](https://matplotlib.org/stable/api/axis_api.html#module-matplotlib.axis "matplotlib.axis")
 is shared with the x- or y-axis in the input [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
. Note that it is not possible to unshare axes.

**frameon**bool, default: True

Whether the Axes frame is visible.

**box\_aspect**float, optional

Set a fixed aspect for the Axes box, i.e. the ratio of height to width. See [`set_box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect")
 for details.

**forward\_navigation\_events**bool or "auto", default: "auto"

Control whether pan/zoom events are passed through to Axes below this one. "auto" is _True_ for axes with an invisible patch and _False_ otherwise.

**\*\*kwargs**

Other optional keyword arguments:

| Property | Description |
| --- | --- |
| [`adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#matplotlib.axes.Axes.set_adjustable "matplotlib.axes.Axes.set_adjustable") | {'box', 'datalim'} |
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
| [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
| [`anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "matplotlib.axes.Axes.set_anchor") | (float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', ...} |
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
| [`aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect") | {'auto', 'equal'} or float |
| [`autoscale_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscale_on.html#matplotlib.axes.Axes.set_autoscale_on "matplotlib.axes.Axes.set_autoscale_on") | bool |
| [`autoscalex_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscalex_on.html#matplotlib.axes.Axes.set_autoscalex_on "matplotlib.axes.Axes.set_autoscalex_on") | unknown |
| [`autoscaley_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscaley_on.html#matplotlib.axes.Axes.set_autoscaley_on "matplotlib.axes.Axes.set_autoscaley_on") | unknown |
| [`axes_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axes_locator.html#matplotlib.axes.Axes.set_axes_locator "matplotlib.axes.Axes.set_axes_locator") | Callable\[\[Axes, Renderer\], Bbox\] |
| [`axisbelow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axisbelow.html#matplotlib.axes.Axes.set_axisbelow "matplotlib.axes.Axes.set_axisbelow") | bool or 'line' |
| [`box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect") | float or None |
| [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
| [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
| [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
| [`facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
| [`forward_navigation_events`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_forward_navigation_events.html#matplotlib.axes.Axes.set_forward_navigation_events "matplotlib.axes.Axes.set_forward_navigation_events") | bool or "auto" |
| [`frame_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_frame_on.html#matplotlib.axes.Axes.set_frame_on "matplotlib.axes.Axes.set_frame_on") | bool |
| [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
| [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
| [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
| [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
| [`navigate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate.html#matplotlib.axes.Axes.set_navigate "matplotlib.axes.Axes.set_navigate") | bool |
| [`navigate_mode`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate_mode.html#matplotlib.axes.Axes.set_navigate_mode "matplotlib.axes.Axes.set_navigate_mode") | unknown |
| [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
| [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
| [`position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib.axes.Axes.set_position "matplotlib.axes.Axes.set_position") | \[left, bottom, width, height\] or [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox") |
| [`prop_cycle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle "matplotlib.axes.Axes.set_prop_cycle") | [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)") |
| [`rasterization_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html#matplotlib.axes.Axes.set_rasterization_zorder "matplotlib.axes.Axes.set_rasterization_zorder") | float or None |
| [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
| [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
| [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
| [`subplotspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_subplotspec.html#matplotlib.axes.Axes.set_subplotspec "matplotlib.axes.Axes.set_subplotspec") | unknown |
| [`title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title") | str |
| [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
| [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
| [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
| [`xbound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xbound.html#matplotlib.axes.Axes.set_xbound "matplotlib.axes.Axes.set_xbound") | (lower: float, upper: float) |
| [`xinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xinverted.html#matplotlib.axes.Axes.set_xinverted "matplotlib.axes.Axes.set_xinverted") | unknown |
| [`xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel") | str |
| [`xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim") | (left: float, right: float) |
| [`xmargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xmargin.html#matplotlib.axes.Axes.set_xmargin "matplotlib.axes.Axes.set_xmargin") | float greater than -0.5 |
| [`xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale") | unknown |
| [`xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels") | unknown |
| [`xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks") | unknown |
| [`ybound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ybound.html#matplotlib.axes.Axes.set_ybound "matplotlib.axes.Axes.set_ybound") | (lower: float, upper: float) |
| [`yinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yinverted.html#matplotlib.axes.Axes.set_yinverted "matplotlib.axes.Axes.set_yinverted") | unknown |
| [`ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel") | str |
| [`ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim") | (bottom: float, top: float) |
| [`ymargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html#matplotlib.axes.Axes.set_ymargin "matplotlib.axes.Axes.set_ymargin") | float greater than -0.5 |
| [`yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale") | unknown |
| [`yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels") | unknown |
| [`yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks") | unknown |
| [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

Returns:

[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The new [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 object.

class InvertedMollweideTransform(_resolution_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L390-L404)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.MollweideAxes.InvertedMollweideTransform "Link to this definition")

Bases: `_GeoTransform`

Create a new geographical transform.

Resolution is the number of steps to interpolate between each input line segment to approximate its path in curved space.

has\_inverse \= True[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.MollweideAxes.InvertedMollweideTransform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L402-L404)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.MollweideAxes.InvertedMollweideTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L392-L400)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.MollweideAxes.InvertedMollweideTransform.transform_non_affine "Link to this definition")

Apply only the non-affine part of this transformation.

`transform(values)` is always equivalent to `transform_affine(transform_non_affine(values))`.

In non-affine transformations, this is generally equivalent to `transform(values)`. In affine transformations, this is always a no-op.

Parameters:

**values**array

The input values as an array of length [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
 or shape (N, [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
).

Returns:

array

The output values as an array of length [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
 or shape (N, [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
), depending on the input.

class MollweideTransform(_resolution_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L349-L388)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.MollweideAxes.MollweideTransform "Link to this definition")

Bases: `_GeoTransform`

The base Mollweide transform.

Create a new geographical transform.

Resolution is the number of steps to interpolate between each input line segment to approximate its path in curved space.

has\_inverse \= True[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.MollweideAxes.MollweideTransform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L386-L388)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.MollweideAxes.MollweideTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/geo.py#L352-L384)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.MollweideAxes.MollweideTransform.transform_non_affine "Link to this definition")

Apply only the non-affine part of this transformation.

`transform(values)` is always equivalent to `transform_affine(transform_non_affine(values))`.

In non-affine transformations, this is generally equivalent to `transform(values)`. In affine transformations, this is always a no-op.

Parameters:

**values**array

The input values as an array of length [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
 or shape (N, [`input_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.input_dims "matplotlib.transforms.Transform.input_dims")
).

Returns:

array

The output values as an array of length [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
 or shape (N, [`output_dims`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.output_dims "matplotlib.transforms.Transform.output_dims")
), depending on the input.

name \= 'mollweide'[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.MollweideAxes.name "Link to this definition")

set(_\*_, _adjustable\=<UNSET>_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _anchor\=<UNSET>_, _animated\=<UNSET>_, _aspect\=<UNSET>_, _autoscale\_on\=<UNSET>_, _autoscalex\_on\=<UNSET>_, _autoscaley\_on\=<UNSET>_, _axes\_locator\=<UNSET>_, _axisbelow\=<UNSET>_, _box\_aspect\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _facecolor\=<UNSET>_, _forward\_navigation\_events\=<UNSET>_, _frame\_on\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _latitude\_grid\=<UNSET>_, _longitude\_grid\=<UNSET>_, _longitude\_grid\_ends\=<UNSET>_, _mouseover\=<UNSET>_, _navigate\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _position\=<UNSET>_, _prop\_cycle\=<UNSET>_, _rasterization\_zorder\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _subplotspec\=<UNSET>_, _title\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _xbound\=<UNSET>_, _xinverted\=<UNSET>_, _xlabel\=<UNSET>_, _xlim\=<UNSET>_, _xmargin\=<UNSET>_, _xscale\=<UNSET>_, _xticklabels\=<UNSET>_, _xticks\=<UNSET>_, _ybound\=<UNSET>_, _yinverted\=<UNSET>_, _ylabel\=<UNSET>_, _ylim\=<UNSET>_, _ymargin\=<UNSET>_, _yscale\=<UNSET>_, _yticklabels\=<UNSET>_, _yticks\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.MollweideAxes.set "Link to this definition")

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
> | [`adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#matplotlib.axes.Axes.set_adjustable "matplotlib.axes.Axes.set_adjustable") | {'box', 'datalim'} |
> | [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "matplotlib.axes.Axes.set_anchor") | (float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', ...} |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect") | {'auto', 'equal'} or float |
> | [`autoscale_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscale_on.html#matplotlib.axes.Axes.set_autoscale_on "matplotlib.axes.Axes.set_autoscale_on") | bool |
> | [`autoscalex_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscalex_on.html#matplotlib.axes.Axes.set_autoscalex_on "matplotlib.axes.Axes.set_autoscalex_on") | unknown |
> | [`autoscaley_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscaley_on.html#matplotlib.axes.Axes.set_autoscaley_on "matplotlib.axes.Axes.set_autoscaley_on") | unknown |
> | [`axes_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axes_locator.html#matplotlib.axes.Axes.set_axes_locator "matplotlib.axes.Axes.set_axes_locator") | Callable\[\[Axes, Renderer\], Bbox\] |
> | [`axisbelow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axisbelow.html#matplotlib.axes.Axes.set_axisbelow "matplotlib.axes.Axes.set_axisbelow") | bool or 'line' |
> | [`box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect") | float or None |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`forward_navigation_events`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_forward_navigation_events.html#matplotlib.axes.Axes.set_forward_navigation_events "matplotlib.axes.Axes.set_forward_navigation_events") | bool or "auto" |
> | [`frame_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_frame_on.html#matplotlib.axes.Axes.set_frame_on "matplotlib.axes.Axes.set_frame_on") | bool |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`latitude_grid`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_latitude_grid "matplotlib.projections.geo.GeoAxes.set_latitude_grid") | unknown |
> | [`longitude_grid`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_longitude_grid "matplotlib.projections.geo.GeoAxes.set_longitude_grid") | unknown |
> | [`longitude_grid_ends`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_longitude_grid_ends "matplotlib.projections.geo.GeoAxes.set_longitude_grid_ends") | unknown |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`navigate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate.html#matplotlib.axes.Axes.set_navigate "matplotlib.axes.Axes.set_navigate") | bool |
> | [`navigate_mode`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate_mode.html#matplotlib.axes.Axes.set_navigate_mode "matplotlib.axes.Axes.set_navigate_mode") | unknown |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib.axes.Axes.set_position "matplotlib.axes.Axes.set_position") | \[left, bottom, width, height\] or [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox") |
> | [`prop_cycle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle "matplotlib.axes.Axes.set_prop_cycle") | [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)") |
> | [`rasterization_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html#matplotlib.axes.Axes.set_rasterization_zorder "matplotlib.axes.Axes.set_rasterization_zorder") | float or None |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`subplotspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_subplotspec.html#matplotlib.axes.Axes.set_subplotspec "matplotlib.axes.Axes.set_subplotspec") | unknown |
> | [`title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title") | str |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`xbound`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xlim "matplotlib.projections.geo.GeoAxes.set_xlim") | unknown |
> | [`xinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xinverted.html#matplotlib.axes.Axes.set_xinverted "matplotlib.axes.Axes.set_xinverted") | unknown |
> | [`xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel") | str |
> | [`xlim`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xlim "matplotlib.projections.geo.GeoAxes.set_xlim") | unknown |
> | [`xmargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xmargin.html#matplotlib.axes.Axes.set_xmargin "matplotlib.axes.Axes.set_xmargin") | float greater than -0.5 |
> | [`xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale") | unknown |
> | [`xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels") | unknown |
> | [`xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks") | unknown |
> | [`ybound`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xlim "matplotlib.projections.geo.GeoAxes.set_xlim") | unknown |
> | [`yinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yinverted.html#matplotlib.axes.Axes.set_yinverted "matplotlib.axes.Axes.set_yinverted") | unknown |
> | [`ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel") | str |
> | [`ylim`](https://matplotlib.org/stable/api/projections/geo.html#matplotlib.projections.geo.GeoAxes.set_xlim "matplotlib.projections.geo.GeoAxes.set_xlim") | unknown |
> | [`ymargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html#matplotlib.axes.Axes.set_ymargin "matplotlib.axes.Axes.set_ymargin") | float greater than -0.5 |
> | [`yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale") | unknown |
> | [`yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels") | unknown |
> | [`yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks") | unknown |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

On this page