[Skip to main content](https://matplotlib.org/stable/api/projections/polar.html#main-content)

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
    

`matplotlib.projections.polar`[#](https://matplotlib.org/stable/api/projections/polar.html#module-matplotlib.projections.polar "Link to this heading")

=======================================================================================================================================================

class matplotlib.projections.polar.InvertedPolarTransform(_axis\=None_, _use\_rmin\=True_, _\*_, _apply\_theta\_transforms\=<deprecated parameter>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L181-L222)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.InvertedPolarTransform "Link to this definition")

Bases: [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

The inverse of the polar transform, mapping Cartesian coordinate space _x_ and _y_ back to _theta_ and _r_.

Parameters:

**axis**[`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
, optional

Axis associated with this transform. This is used to get the minimum radial limit.

**use\_rmin**[`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
, optional

If `True`, add the minimum radial axis limit after transforming from Cartesian coordinates. _axis_ must also be specified for this to take effect.

has\_inverse \= True[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.InvertedPolarTransform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

input\_dims \= 2[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.InvertedPolarTransform.input_dims "Link to this definition")

The number of input dimensions of this transform. Must be overridden (with integers) in the subclass.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L220-L222)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.InvertedPolarTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

output\_dims \= 2[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.InvertedPolarTransform.output_dims "Link to this definition")

The number of output dimensions of this transform. Must be overridden (with integers) in the subclass.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L210-L218)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.InvertedPolarTransform.transform_non_affine "Link to this definition")

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

class matplotlib.projections.polar.PolarAffine(_scale\_transform_, _limits_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L133-L178)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAffine "Link to this definition")

Bases: [`Affine2DBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase "matplotlib.transforms.Affine2DBase")

The affine part of the polar projection.

Scales the output so that maximum radius rests on the edge of the Axes circle and the origin is mapped to (0.5, 0.5). The transform applied is the same to x and y components and given by:

\\\[x\_{1} = 0.5 \\left \[ \\frac{x\_{0}}{(r\_{\\max} - r\_{\\min})} + 1 \\right \]\\\]

\\(r\_{\\min}, r\_{\\max}\\) are the minimum and maximum radial limits after any scaling (e.g. log scaling) has been removed.

Parameters:

**scale\_transform**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

Scaling transform for the data. This is used to remove any scaling from the radial view limits.

**limits**[`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")

View limits of the data. The only part of its bounds that is used is the y limits (for the radius limits).

get\_matrix()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L167-L178)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAffine.get_matrix "Link to this definition")

Get the matrix for the affine part of this transform.

class matplotlib.projections.polar.PolarAxes(_\*args_, _theta\_offset\=0_, _theta\_direction\=1_, _rlabel\_position\=22.5_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L772-L1503)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes "Link to this definition")

Bases: [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes._axes.Axes")

A polar graph projection, where the input dimensions are _theta_, _r_.

Theta starts pointing east and goes anti-clockwise.

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

class InvertedPolarTransform(_axis\=None_, _use\_rmin\=True_, _\*_, _apply\_theta\_transforms\=<deprecated parameter>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L181-L222)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.InvertedPolarTransform "Link to this definition")

Bases: [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

The inverse of the polar transform, mapping Cartesian coordinate space _x_ and _y_ back to _theta_ and _r_.

Parameters:

**axis**[`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
, optional

Axis associated with this transform. This is used to get the minimum radial limit.

**use\_rmin**[`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
, optional

If `True`, add the minimum radial axis limit after transforming from Cartesian coordinates. _axis_ must also be specified for this to take effect.

has\_inverse \= True[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.InvertedPolarTransform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

input\_dims \= 2[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.InvertedPolarTransform.input_dims "Link to this definition")

The number of input dimensions of this transform. Must be overridden (with integers) in the subclass.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L220-L222)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.InvertedPolarTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

output\_dims \= 2[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.InvertedPolarTransform.output_dims "Link to this definition")

The number of output dimensions of this transform. Must be overridden (with integers) in the subclass.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L210-L218)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.InvertedPolarTransform.transform_non_affine "Link to this definition")

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

class PolarAffine(_scale\_transform_, _limits_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L133-L178)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.PolarAffine "Link to this definition")

Bases: [`Affine2DBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase "matplotlib.transforms.Affine2DBase")

The affine part of the polar projection.

Scales the output so that maximum radius rests on the edge of the Axes circle and the origin is mapped to (0.5, 0.5). The transform applied is the same to x and y components and given by:

\\\[x\_{1} = 0.5 \\left \[ \\frac{x\_{0}}{(r\_{\\max} - r\_{\\min})} + 1 \\right \]\\\]

\\(r\_{\\min}, r\_{\\max}\\) are the minimum and maximum radial limits after any scaling (e.g. log scaling) has been removed.

Parameters:

**scale\_transform**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

Scaling transform for the data. This is used to remove any scaling from the radial view limits.

**limits**[`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")

View limits of the data. The only part of its bounds that is used is the y limits (for the radius limits).

get\_matrix()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L167-L178)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.PolarAffine.get_matrix "Link to this definition")

Get the matrix for the affine part of this transform.

class PolarTransform(_axis\=None_, _use\_rmin\=True_, _\*_, _apply\_theta\_transforms\=<deprecated parameter>_, _scale\_transform\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L18-L130)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.PolarTransform "Link to this definition")

Bases: [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

The base polar transform.

This transform maps polar coordinates \\(\\theta, r\\) into Cartesian coordinates \\(x, y = r \\cos(\\theta), r \\sin(\\theta)\\) (but does not fully transform into Axes coordinates or handle positioning in screen space).

This transformation is designed to be applied to data after any scaling along the radial axis (e.g. log-scaling) has been applied to the input data.

Path segments at a fixed radius are automatically transformed to circular arcs as long as `path._interpolation_steps > 1`.

Parameters:

**axis**[`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
, optional

Axis associated with this transform. This is used to get the minimum radial limit.

**use\_rmin**[`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
, optional

If `True`, subtract the minimum radial axis limit before transforming to Cartesian coordinates. _axis_ must also be specified for this to take effect.

has\_inverse \= True[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.PolarTransform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

input\_dims \= 2[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.PolarTransform.input_dims "Link to this definition")

The number of input dimensions of this transform. Must be overridden (with integers) in the subclass.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L128-L130)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.PolarTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

output\_dims \= 2[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.PolarTransform.output_dims "Link to this definition")

The number of output dimensions of this transform. Must be overridden (with integers) in the subclass.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L66-L72)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.PolarTransform.transform_non_affine "Link to this definition")

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

transform\_path\_non\_affine(_path_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L74-L126)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.PolarTransform.transform_path_non_affine "Link to this definition")

Apply the non-affine part of this transform to [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 _path_, returning a new [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
.

`transform_path(path)` is equivalent to `transform_path_affine(transform_path_non_affine(values))`.

class RadialLocator(_base_, _axes\=<deprecated parameter>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L429-L476)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.RadialLocator "Link to this definition")

Bases: [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")

Used to locate radius ticks.

Ensures that all ticks are strictly positive. For all other tasks, it delegates to the base [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")
 (which may be different depending on the scale of the _r_\-axis).

nonsingular(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L463-L469)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.RadialLocator.nonsingular "Link to this definition")

Adjust a range as needed to avoid singularities.

This method gets called during autoscaling, with `(v0, v1)` set to the data limits on the Axes if the Axes contains any data, or `(-inf, +inf)` if not.

*   If `v0 == v1` (possibly up to some floating point slop), this method returns an expanded interval around this value.
    
*   If `(v0, v1) == (-inf, +inf)`, this method returns appropriate default view limits.
    
*   Otherwise, `(v0, v1)` is returned without modification.
    

set\_axis(_axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L443-L444)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.RadialLocator.set_axis "Link to this definition")

view\_limits(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L471-L476)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.RadialLocator.view_limits "Link to this definition")

Select a scale for the range from vmin to vmax.

Subclasses should override this method to change locator behaviour.

class ThetaFormatter[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L225-L235)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.ThetaFormatter "Link to this definition")

Bases: [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")

Used to format the _theta_ tick labels. Converts the native unit of radians into degrees and adds a degree symbol.

class ThetaLocator(_base_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L261-L287)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.ThetaLocator "Link to this definition")

Bases: [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")

Used to locate theta ticks.

This will work the same as the base locator except in the case that the view spans the entire circle. In such cases, the previously used default locations of every 45 degrees are returned.

set\_axis(_axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L274-L276)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.ThetaLocator.set_axis "Link to this definition")

view\_limits(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L285-L287)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.ThetaLocator.view_limits "Link to this definition")

Select a scale for the range from vmin to vmax.

Subclasses should override this method to change locator behaviour.

can\_pan()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1445-L1453)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.can_pan "Link to this definition")

Return whether this Axes supports the pan/zoom button functionality.

For a polar Axes, this is slightly misleading. Both panning and zooming are performed by the same button. Panning is performed in azimuth while zooming is done along the radial.

can\_zoom()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1437-L1443)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.can_zoom "Link to this definition")

Return whether this Axes supports the zoom box button functionality.

A polar Axes does not support zoom boxes.

clear()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L792-L813)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.clear "Link to this definition")

Clear the Axes.

drag\_pan(_button_, _key_, _x_, _y_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1478-L1503)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.drag_pan "Link to this definition")

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

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L963-L1009)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.draw "Link to this definition")

Draw the Artist (and its children) using the given renderer.

This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")
 returns False).

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass.

Notes

This method is overridden in the Artist subclasses.

end\_pan()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1475-L1476)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.end_pan "Link to this definition")

Called when a pan operation completes (when the mouse button is up.)

Notes

This is intended to be overridden by new projection types.

format\_coord(_theta_, _r_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1384-L1426)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.format_coord "Link to this definition")

Return a format string formatting the _x_, _y_ coordinates.

get\_data\_ratio()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1428-L1433)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.get_data_ratio "Link to this definition")

Return the aspect ratio of the data itself. For a polar plot, this should always be 1.0

get\_rlabel\_position()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1231-L1238)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.get_rlabel_position "Link to this definition")

Returns:

float

The theta position of the radius labels in degrees.

get\_rmax()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1155-L1162)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.get_rmax "Link to this definition")

Returns:

float

Outer radial limit.

get\_rmin()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1174-L1181)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.get_rmin "Link to this definition")

Returns:

float

The inner radial limit.

get\_rorigin()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1193-L1199)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.get_rorigin "Link to this definition")

Returns:

float

get\_rsign()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1201-L1202)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.get_rsign "Link to this definition")

get\_theta\_direction()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1133-L1143)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.get_theta_direction "Link to this definition")

Get the direction in which theta increases.

\-1:

Theta increases in the clockwise direction

1:

Theta increases in the counterclockwise direction

get\_theta\_offset()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1080-L1084)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.get_theta_offset "Link to this definition")

Get the offset for the location of 0 in radians.

get\_thetamax()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1031-L1033)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.get_thetamax "Link to this definition")

Return the maximum theta limit in degrees.

get\_thetamin()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1039-L1041)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.get_thetamin "Link to this definition")

Get the minimum theta limit in degrees.

get\_xaxis\_text1\_transform(_pad_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L928-L929)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.get_xaxis_text1_transform "Link to this definition")

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

get\_xaxis\_text2\_transform(_pad_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L931-L932)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.get_xaxis_text2_transform "Link to this definition")

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

get\_xaxis\_transform(_which\='grid'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L924-L926)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.get_xaxis_transform "Link to this definition")

Get the transformation used for drawing x-axis labels, ticks and gridlines. The x-direction is in data coordinates and the y-direction is in axis coordinates.

Note

This transformation is primarily used by the [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 class, and is meant to be overridden by new kinds of projections that may need to place axis elements in different locations.

Parameters:

**which**{'grid', 'tick1', 'tick2'}

get\_yaxis\_text1\_transform(_pad_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L942-L952)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.get_yaxis_text1_transform "Link to this definition")

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

get\_yaxis\_text2\_transform(_pad_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L954-L961)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.get_yaxis_text2_transform "Link to this definition")

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

get\_yaxis\_transform(_which\='grid'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L934-L940)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.get_yaxis_transform "Link to this definition")

Get the transformation used for drawing y-axis labels, ticks and gridlines. The x-direction is in axis coordinates and the y-direction is in data coordinates.

Note

This transformation is primarily used by the [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 class, and is meant to be overridden by new kinds of projections that may need to place axis elements in different locations.

Parameters:

**which**{'grid', 'tick1', 'tick2'}

name \= 'polar'[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.name "Link to this definition")

set(_\*_, _adjustable\=<UNSET>_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _anchor\=<UNSET>_, _animated\=<UNSET>_, _aspect\=<UNSET>_, _autoscale\_on\=<UNSET>_, _autoscalex\_on\=<UNSET>_, _autoscaley\_on\=<UNSET>_, _axes\_locator\=<UNSET>_, _axisbelow\=<UNSET>_, _box\_aspect\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _facecolor\=<UNSET>_, _forward\_navigation\_events\=<UNSET>_, _frame\_on\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _navigate\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _position\=<UNSET>_, _prop\_cycle\=<UNSET>_, _rasterization\_zorder\=<UNSET>_, _rasterized\=<UNSET>_, _rgrids\=<UNSET>_, _rlabel\_position\=<UNSET>_, _rlim\=<UNSET>_, _rmax\=<UNSET>_, _rmin\=<UNSET>_, _rorigin\=<UNSET>_, _rscale\=<UNSET>_, _rticks\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _subplotspec\=<UNSET>_, _theta\_direction\=<UNSET>_, _theta\_offset\=<UNSET>_, _theta\_zero\_location\=<UNSET>_, _thetagrids\=<UNSET>_, _thetalim\=<UNSET>_, _thetamax\=<UNSET>_, _thetamin\=<UNSET>_, _title\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _xbound\=<UNSET>_, _xinverted\=<UNSET>_, _xlabel\=<UNSET>_, _xlim\=<UNSET>_, _xmargin\=<UNSET>_, _xscale\=<UNSET>_, _xticklabels\=<UNSET>_, _xticks\=<UNSET>_, _ybound\=<UNSET>_, _yinverted\=<UNSET>_, _ylabel\=<UNSET>_, _ylim\=<UNSET>_, _ymargin\=<UNSET>_, _yscale\=<UNSET>_, _yticklabels\=<UNSET>_, _yticks\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set "Link to this definition")

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
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`navigate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate.html#matplotlib.axes.Axes.set_navigate "matplotlib.axes.Axes.set_navigate") | bool |
> | [`navigate_mode`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate_mode.html#matplotlib.axes.Axes.set_navigate_mode "matplotlib.axes.Axes.set_navigate_mode") | unknown |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib.axes.Axes.set_position "matplotlib.axes.Axes.set_position") | \[left, bottom, width, height\] or [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox") |
> | [`prop_cycle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle "matplotlib.axes.Axes.set_prop_cycle") | [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)") |
> | [`rasterization_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html#matplotlib.axes.Axes.set_rasterization_zorder "matplotlib.axes.Axes.set_rasterization_zorder") | float or None |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`rgrids`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rgrids "matplotlib.projections.polar.PolarAxes.set_rgrids") | tuple with floats |
> | [`rlabel_position`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rlabel_position "matplotlib.projections.polar.PolarAxes.set_rlabel_position") | number |
> | [`rlim`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rlim "matplotlib.projections.polar.PolarAxes.set_rlim") | unknown |
> | [`rmax`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rmax "matplotlib.projections.polar.PolarAxes.set_rmax") | float |
> | [`rmin`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rmin "matplotlib.projections.polar.PolarAxes.set_rmin") | float |
> | [`rorigin`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rorigin "matplotlib.projections.polar.PolarAxes.set_rorigin") | float |
> | [`rscale`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rscale "matplotlib.projections.polar.PolarAxes.set_rscale") | unknown |
> | [`rticks`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rticks "matplotlib.projections.polar.PolarAxes.set_rticks") | unknown |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`subplotspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_subplotspec.html#matplotlib.axes.Axes.set_subplotspec "matplotlib.axes.Axes.set_subplotspec") | unknown |
> | [`theta_direction`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_theta_direction "matplotlib.projections.polar.PolarAxes.set_theta_direction") | unknown |
> | [`theta_offset`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_theta_offset "matplotlib.projections.polar.PolarAxes.set_theta_offset") | unknown |
> | [`theta_zero_location`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_theta_zero_location "matplotlib.projections.polar.PolarAxes.set_theta_zero_location") | str |
> | [`thetagrids`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_thetagrids "matplotlib.projections.polar.PolarAxes.set_thetagrids") | tuple with floats, degrees |
> | [`thetalim`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_thetalim "matplotlib.projections.polar.PolarAxes.set_thetalim") | unknown |
> | [`thetamax`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_thetamax "matplotlib.projections.polar.PolarAxes.set_thetamax") | unknown |
> | [`thetamin`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_thetamin "matplotlib.projections.polar.PolarAxes.set_thetamin") | unknown |
> | [`title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title") | str |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`xbound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xbound.html#matplotlib.axes.Axes.set_xbound "matplotlib.axes.Axes.set_xbound") | (lower: float, upper: float) |
> | [`xinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xinverted.html#matplotlib.axes.Axes.set_xinverted "matplotlib.axes.Axes.set_xinverted") | unknown |
> | [`xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel") | str |
> | [`xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim") | (left: float, right: float) |
> | [`xmargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xmargin.html#matplotlib.axes.Axes.set_xmargin "matplotlib.axes.Axes.set_xmargin") | float greater than -0.5 |
> | [`xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale") | unknown |
> | [`xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels") | unknown |
> | [`xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks") | unknown |
> | [`ybound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ybound.html#matplotlib.axes.Axes.set_ybound "matplotlib.axes.Axes.set_ybound") | (lower: float, upper: float) |
> | [`yinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yinverted.html#matplotlib.axes.Axes.set_yinverted "matplotlib.axes.Axes.set_yinverted") | unknown |
> | [`ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel") | str |
> | [`ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim") | (bottom: float, top: float) |
> | [`ymargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html#matplotlib.axes.Axes.set_ymargin "matplotlib.axes.Axes.set_ymargin") | float greater than -0.5 |
> | [`yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale") | unknown |
> | [`yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels") | unknown |
> | [`yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks") | unknown |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_rgrids(_radii_, _labels\=None_, _angle\=None_, _fmt\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1318-L1382)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rgrids "Link to this definition")

Set the radial gridlines on a polar plot.

Parameters:

**radii**tuple with floats

The radii for the radial gridlines

**labels**tuple with strings or None

The labels to use at each radial gridline. The [`matplotlib.ticker.ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
 will be used if None.

**angle**float

The angular position of the radius labels in degrees.

**fmt**str or None

Format string used in [`matplotlib.ticker.FormatStrFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FormatStrFormatter "matplotlib.ticker.FormatStrFormatter")
. For example '%f'.

Returns:

**lines**list of [`lines.Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")

The radial gridlines.

**labels**list of [`text.Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

The tick labels.

Other Parameters:

**\*\*kwargs**

_kwargs_ are optional [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties for the labels.

Warning

This only sets the properties of the current ticks. Ticks are not guaranteed to be persistent. Various operations can create, delete and modify the Tick instances. There is an imminent risk that these settings can get lost if you work on the figure further (including also panning/zooming on a displayed figure).

Use [`set_tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params")
 instead if possible.

See also

[`PolarAxes.set_thetagrids`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_thetagrids "matplotlib.projections.polar.PolarAxes.set_thetagrids")

[`Axis.get_gridlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_gridlines.html#matplotlib.axis.Axis.get_gridlines "matplotlib.axis.Axis.get_gridlines")

[`Axis.get_ticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_ticklabels.html#matplotlib.axis.Axis.get_ticklabels "matplotlib.axis.Axis.get_ticklabels")

set\_rlabel\_position(_value_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1240-L1249)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rlabel_position "Link to this definition")

Update the theta position of the radius labels.

Parameters:

**value**number

The angular position of the radius labels in degrees.

set\_rlim(_bottom\=None_, _top\=None_, _\*_, _emit\=True_, _auto\=False_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1204-L1229)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rlim "Link to this definition")

Set the radial axis view limits.

This function behaves like [`Axes.set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
, but additionally supports _rmin_ and _rmax_ as aliases for _bottom_ and _top_.

See also

[`Axes.set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")

set\_rmax(_rmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1145-L1153)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rmax "Link to this definition")

Set the outer radial limit.

Parameters:

**rmax**float

set\_rmin(_rmin_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1164-L1172)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rmin "Link to this definition")

Set the inner radial limit.

Parameters:

**rmin**float

set\_rorigin(_rorigin_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1183-L1191)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rorigin "Link to this definition")

Update the radial origin.

Parameters:

**rorigin**float

set\_rscale(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1251-L1252)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rscale "Link to this definition")

set\_rticks(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1254-L1255)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rticks "Link to this definition")

set\_theta\_direction(_direction_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1112-L1131)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_theta_direction "Link to this definition")

Set the direction in which theta increases.

clockwise, -1:

Theta increases in the clockwise direction

counterclockwise, anticlockwise, 1:

Theta increases in the counterclockwise direction

set\_theta\_offset(_offset_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1072-L1078)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_theta_offset "Link to this definition")

Set the offset for the location of 0 in radians.

set\_theta\_zero\_location(_loc_, _offset\=0.0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1086-L1110)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_theta_zero_location "Link to this definition")

Set the location of theta's zero.

This simply calls [`set_theta_offset`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_theta_offset "matplotlib.projections.polar.PolarAxes.set_theta_offset")
 with the correct value in radians.

Parameters:

**loc**str

May be one of "N", "NW", "W", "SW", "S", "SE", "E", or "NE".

**offset**float, default: 0

An offset in degrees to apply from the specified _loc_. **Note:** this offset is _always_ applied counter-clockwise regardless of the direction setting.

set\_thetagrids(_angles_, _labels\=None_, _fmt\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1257-L1316)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_thetagrids "Link to this definition")

Set the theta gridlines in a polar plot.

Parameters:

**angles**tuple with floats, degrees

The angles of the theta gridlines.

**labels**tuple with strings or None

The labels to use at each theta gridline. The [`projections.polar.ThetaFormatter`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.ThetaFormatter "matplotlib.projections.polar.ThetaFormatter")
 will be used if None.

**fmt**str or None

Format string used in [`matplotlib.ticker.FormatStrFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FormatStrFormatter "matplotlib.ticker.FormatStrFormatter")
. For example '%f'. Note that the angle that is used is in radians.

Returns:

**lines**list of [`lines.Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")

The theta gridlines.

**labels**list of [`text.Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

The tick labels.

Other Parameters:

**\*\*kwargs**

_kwargs_ are optional [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties for the labels.

Warning

This only sets the properties of the current ticks. Ticks are not guaranteed to be persistent. Various operations can create, delete and modify the Tick instances. There is an imminent risk that these settings can get lost if you work on the figure further (including also panning/zooming on a displayed figure).

Use [`set_tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params")
 instead if possible.

See also

[`PolarAxes.set_rgrids`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rgrids "matplotlib.projections.polar.PolarAxes.set_rgrids")

[`Axis.get_gridlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_gridlines.html#matplotlib.axis.Axis.get_gridlines "matplotlib.axis.Axis.get_gridlines")

[`Axis.get_ticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_ticklabels.html#matplotlib.axis.Axis.get_ticklabels "matplotlib.axis.Axis.get_ticklabels")

set\_thetalim(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1043-L1070)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_thetalim "Link to this definition")

Set the minimum and maximum theta values.

Can take the following signatures:

*   `set_thetalim(minval, maxval)`: Set the limits in radians.
    
*   `set_thetalim(thetamin=minval, thetamax=maxval)`: Set the limits in degrees.
    

where minval and maxval are the minimum and maximum limits. Values are wrapped in to the range \\(\[0, 2\\pi\]\\) (in radians), so for example it is possible to do `set_thetalim(-np.pi / 2, np.pi / 2)` to have an axis symmetric around 0. A ValueError is raised if the absolute angle difference is larger than a full circle.

set\_thetamax(_thetamax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1027-L1029)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_thetamax "Link to this definition")

Set the maximum theta limit in degrees.

set\_thetamin(_thetamin_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1035-L1037)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_thetamin "Link to this definition")

Set the minimum theta limit in degrees.

start\_pan(_x_, _y_, _button_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L1455-L1473)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.start_pan "Link to this definition")

Called when a pan operation has started.

Parameters:

**x, y**float

The mouse coordinates in display coords.

**button**[`MouseButton`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton "matplotlib.backend_bases.MouseButton")

The pressed mouse button.

Notes

This is intended to be overridden by new projection types.

class matplotlib.projections.polar.PolarTransform(_axis\=None_, _use\_rmin\=True_, _\*_, _apply\_theta\_transforms\=<deprecated parameter>_, _scale\_transform\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L18-L130)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarTransform "Link to this definition")

Bases: [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

The base polar transform.

This transform maps polar coordinates \\(\\theta, r\\) into Cartesian coordinates \\(x, y = r \\cos(\\theta), r \\sin(\\theta)\\) (but does not fully transform into Axes coordinates or handle positioning in screen space).

This transformation is designed to be applied to data after any scaling along the radial axis (e.g. log-scaling) has been applied to the input data.

Path segments at a fixed radius are automatically transformed to circular arcs as long as `path._interpolation_steps > 1`.

Parameters:

**axis**[`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
, optional

Axis associated with this transform. This is used to get the minimum radial limit.

**use\_rmin**[`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
, optional

If `True`, subtract the minimum radial axis limit before transforming to Cartesian coordinates. _axis_ must also be specified for this to take effect.

has\_inverse \= True[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarTransform.has_inverse "Link to this definition")

True if this transform has a corresponding inverse transform.

input\_dims \= 2[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarTransform.input_dims "Link to this definition")

The number of input dimensions of this transform. Must be overridden (with integers) in the subclass.

inverted()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L128-L130)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarTransform.inverted "Link to this definition")

Return the corresponding inverse transformation.

It holds `x == self.inverted().transform(self.transform(x))`.

The return value of this method should be treated as temporary. An update to _self_ does not cause a corresponding update to its inverted copy.

output\_dims \= 2[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarTransform.output_dims "Link to this definition")

The number of output dimensions of this transform. Must be overridden (with integers) in the subclass.

transform\_non\_affine(_values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L66-L72)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarTransform.transform_non_affine "Link to this definition")

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

transform\_path\_non\_affine(_path_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L74-L126)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarTransform.transform_path_non_affine "Link to this definition")

Apply the non-affine part of this transform to [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 _path_, returning a new [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
.

`transform_path(path)` is equivalent to `transform_path_affine(transform_path_non_affine(values))`.

class matplotlib.projections.polar.RadialAxis(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L672-L695)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.RadialAxis "Link to this definition")

Bases: [`YAxis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.YAxis "matplotlib.axis.YAxis")

A radial Axis.

This overrides certain properties of a [`YAxis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.YAxis "matplotlib.axis.YAxis")
 to provide special-casing for a radial axis.

Parameters:

**axes**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 to which the created Axis belongs.

**pickradius**float

The acceptance radius for containment tests. See also [`Axis.contains`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.contains.html#matplotlib.axis.Axis.contains "matplotlib.axis.Axis.contains")
.

**clear**bool, default: True

Whether to clear the Axis on creation. This is not required, e.g., when creating an Axis as part of an Axes, as `Axes.clear` will call `Axis.clear`. .. versionadded:: 3.8

axis\_name \= 'radius'[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.RadialAxis.axis_name "Link to this definition")

Read-only name identifying the axis.

clear()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L692-L695)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.RadialAxis.clear "Link to this definition")

Clear the axis.

This resets axis properties to their default values:

*   the label
    
*   the scale
    
*   locators, formatters and ticks
    
*   major and minor grid
    
*   units
    
*   registered callbacks
    

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _converter\=<UNSET>_, _data\_interval\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _inverted\=<UNSET>_, _label\=<UNSET>_, _label\_coords\=<UNSET>_, _label\_position\=<UNSET>_, _label\_text\=<UNSET>_, _major\_formatter\=<UNSET>_, _major\_locator\=<UNSET>_, _minor\_formatter\=<UNSET>_, _minor\_locator\=<UNSET>_, _mouseover\=<UNSET>_, _offset\_position\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _pickradius\=<UNSET>_, _rasterized\=<UNSET>_, _remove\_overlapping\_locs\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _tick\_params\=<UNSET>_, _ticklabels\=<UNSET>_, _ticks\=<UNSET>_, _ticks\_position\=<UNSET>_, _transform\=<UNSET>_, _units\=<UNSET>_, _url\=<UNSET>_, _view\_interval\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.RadialAxis.set "Link to this definition")

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
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`converter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_converter.html#matplotlib.axis.Axis.set_converter "matplotlib.axis.Axis.set_converter") | [`ConversionInterface`](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.ConversionInterface "matplotlib.units.ConversionInterface") |
> | [`data_interval`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_data_interval.html#matplotlib.axis.Axis.set_data_interval "matplotlib.axis.Axis.set_data_interval") | unknown |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`inverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_inverted.html#matplotlib.axis.Axis.set_inverted "matplotlib.axis.Axis.set_inverted") | unknown |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label.html#matplotlib.axis.Axis.set_label "matplotlib.axis.Axis.set_label") | unknown |
> | [`label_coords`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label_coords.html#matplotlib.axis.Axis.set_label_coords "matplotlib.axis.Axis.set_label_coords") | unknown |
> | [`label_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.YAxis.set_label_position.html#matplotlib.axis.YAxis.set_label_position "matplotlib.axis.YAxis.set_label_position") | {'left', 'right'} |
> | [`label_text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label_text.html#matplotlib.axis.Axis.set_label_text "matplotlib.axis.Axis.set_label_text") | str |
> | [`major_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter") | [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")<br>, `str`, or function |
> | [`major_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator") | unknown |
> | [`minor_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_formatter.html#matplotlib.axis.Axis.set_minor_formatter "matplotlib.axis.Axis.set_minor_formatter") | [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")<br>, `str`, or function |
> | [`minor_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_locator.html#matplotlib.axis.Axis.set_minor_locator "matplotlib.axis.Axis.set_minor_locator") | [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator") |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`offset_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.YAxis.set_offset_position.html#matplotlib.axis.YAxis.set_offset_position "matplotlib.axis.YAxis.set_offset_position") | {'left', 'right'} |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`pickradius`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_pickradius.html#matplotlib.axis.Axis.set_pickradius "matplotlib.axis.Axis.set_pickradius") | float |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`remove_overlapping_locs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_remove_overlapping_locs.html#matplotlib.axis.Axis.set_remove_overlapping_locs "matplotlib.axis.Axis.set_remove_overlapping_locs") | unknown |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params") | unknown |
> | [`ticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticklabels.html#matplotlib.axis.Axis.set_ticklabels "matplotlib.axis.Axis.set_ticklabels") | sequence of str or of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")<br>s |
> | [`ticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticks.html#matplotlib.axis.Axis.set_ticks "matplotlib.axis.Axis.set_ticks") | 1D array-like |
> | [`ticks_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.YAxis.set_ticks_position.html#matplotlib.axis.YAxis.set_ticks_position "matplotlib.axis.YAxis.set_ticks_position") | {'left', 'right', 'both', 'default', 'none'} |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`units`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_units.html#matplotlib.axis.Axis.set_units "matplotlib.axis.Axis.set_units") | units tag |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`view_interval`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_view_interval.html#matplotlib.axis.Axis.set_view_interval "matplotlib.axis.Axis.set_view_interval") | unknown |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_major\_locator(_locator_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L687-L690)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.RadialAxis.set_major_locator "Link to this definition")

Set the locator of the major ticker.

Parameters:

**locator**[`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")

class matplotlib.projections.polar.RadialLocator(_base_, _axes\=<deprecated parameter>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L429-L476)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.RadialLocator "Link to this definition")

Bases: [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")

Used to locate radius ticks.

Ensures that all ticks are strictly positive. For all other tasks, it delegates to the base [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")
 (which may be different depending on the scale of the _r_\-axis).

nonsingular(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L463-L469)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.RadialLocator.nonsingular "Link to this definition")

Adjust a range as needed to avoid singularities.

This method gets called during autoscaling, with `(v0, v1)` set to the data limits on the Axes if the Axes contains any data, or `(-inf, +inf)` if not.

*   If `v0 == v1` (possibly up to some floating point slop), this method returns an expanded interval around this value.
    
*   If `(v0, v1) == (-inf, +inf)`, this method returns appropriate default view limits.
    
*   Otherwise, `(v0, v1)` is returned without modification.
    

set\_axis(_axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L443-L444)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.RadialLocator.set_axis "Link to this definition")

view\_limits(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L471-L476)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.RadialLocator.view_limits "Link to this definition")

Select a scale for the range from vmin to vmax.

Subclasses should override this method to change locator behaviour.

class matplotlib.projections.polar.RadialTick(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L521-L669)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.RadialTick "Link to this definition")

Bases: [`YTick`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.YTick "matplotlib.axis.YTick")

A radial-axis tick.

This subclass of [`YTick`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.YTick "matplotlib.axis.YTick")
 provides radial ticks with some small modification to their re-positioning such that ticks are rotated based on axes limits. This results in ticks that are correctly perpendicular to the spine. Labels are also rotated to be perpendicular to the spine, when 'auto' rotation is enabled.

Parameters:

**loc**

The tick location in data coords.

**size**

The tick size in points.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _pad\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.RadialTick.set "Link to this definition")

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
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`pad`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Tick.set_pad.html#matplotlib.axis.Tick.set_pad "matplotlib.axis.Tick.set_pad") | float |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Tick.set_url.html#matplotlib.axis.Tick.set_url "matplotlib.axis.Tick.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

update\_position(_loc_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L591-L669)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.RadialTick.update_position "Link to this definition")

Set the location of tick in data coords with scalar _loc_.

class matplotlib.projections.polar.ThetaAxis(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L382-L426)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.ThetaAxis "Link to this definition")

Bases: [`XAxis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.XAxis "matplotlib.axis.XAxis")

A theta Axis.

This overrides certain properties of an [`XAxis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.XAxis "matplotlib.axis.XAxis")
 to provide special-casing for an angular axis.

Parameters:

**axes**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 to which the created Axis belongs.

**pickradius**float

The acceptance radius for containment tests. See also [`Axis.contains`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.contains.html#matplotlib.axis.Axis.contains "matplotlib.axis.Axis.contains")
.

**clear**bool, default: True

Whether to clear the Axis on creation. This is not required, e.g., when creating an Axis as part of an Axes, as `Axes.clear` will call `Axis.clear`. .. versionadded:: 3.8

axis\_name \= 'theta'[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.ThetaAxis.axis_name "Link to this definition")

Read-only name identifying the axis.

clear()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L399-L403)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.ThetaAxis.clear "Link to this definition")

Clear the axis.

This resets axis properties to their default values:

*   the label
    
*   the scale
    
*   locators, formatters and ticks
    
*   major and minor grid
    
*   units
    
*   registered callbacks
    

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _converter\=<UNSET>_, _data\_interval\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _inverted\=<UNSET>_, _label\=<UNSET>_, _label\_coords\=<UNSET>_, _label\_position\=<UNSET>_, _label\_text\=<UNSET>_, _major\_formatter\=<UNSET>_, _major\_locator\=<UNSET>_, _minor\_formatter\=<UNSET>_, _minor\_locator\=<UNSET>_, _mouseover\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _pickradius\=<UNSET>_, _rasterized\=<UNSET>_, _remove\_overlapping\_locs\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _tick\_params\=<UNSET>_, _ticklabels\=<UNSET>_, _ticks\=<UNSET>_, _ticks\_position\=<UNSET>_, _transform\=<UNSET>_, _units\=<UNSET>_, _url\=<UNSET>_, _view\_interval\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.ThetaAxis.set "Link to this definition")

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
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`converter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_converter.html#matplotlib.axis.Axis.set_converter "matplotlib.axis.Axis.set_converter") | [`ConversionInterface`](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.ConversionInterface "matplotlib.units.ConversionInterface") |
> | [`data_interval`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_data_interval.html#matplotlib.axis.Axis.set_data_interval "matplotlib.axis.Axis.set_data_interval") | unknown |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`inverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_inverted.html#matplotlib.axis.Axis.set_inverted "matplotlib.axis.Axis.set_inverted") | unknown |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label.html#matplotlib.axis.Axis.set_label "matplotlib.axis.Axis.set_label") | unknown |
> | [`label_coords`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label_coords.html#matplotlib.axis.Axis.set_label_coords "matplotlib.axis.Axis.set_label_coords") | unknown |
> | [`label_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.set_label_position.html#matplotlib.axis.XAxis.set_label_position "matplotlib.axis.XAxis.set_label_position") | {'top', 'bottom'} |
> | [`label_text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label_text.html#matplotlib.axis.Axis.set_label_text "matplotlib.axis.Axis.set_label_text") | str |
> | [`major_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter") | [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")<br>, `str`, or function |
> | [`major_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator") | [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator") |
> | [`minor_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_formatter.html#matplotlib.axis.Axis.set_minor_formatter "matplotlib.axis.Axis.set_minor_formatter") | [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")<br>, `str`, or function |
> | [`minor_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_locator.html#matplotlib.axis.Axis.set_minor_locator "matplotlib.axis.Axis.set_minor_locator") | [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator") |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`pickradius`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_pickradius.html#matplotlib.axis.Axis.set_pickradius "matplotlib.axis.Axis.set_pickradius") | float |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`remove_overlapping_locs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_remove_overlapping_locs.html#matplotlib.axis.Axis.set_remove_overlapping_locs "matplotlib.axis.Axis.set_remove_overlapping_locs") | unknown |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params") | unknown |
> | [`ticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticklabels.html#matplotlib.axis.Axis.set_ticklabels "matplotlib.axis.Axis.set_ticklabels") | sequence of str or of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")<br>s |
> | [`ticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticks.html#matplotlib.axis.Axis.set_ticks "matplotlib.axis.Axis.set_ticks") | 1D array-like |
> | [`ticks_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.set_ticks_position.html#matplotlib.axis.XAxis.set_ticks_position "matplotlib.axis.XAxis.set_ticks_position") | {'top', 'bottom', 'both', 'default', 'none'} |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`units`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_units.html#matplotlib.axis.Axis.set_units "matplotlib.axis.Axis.set_units") | units tag |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`view_interval`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_view_interval.html#matplotlib.axis.Axis.set_view_interval "matplotlib.axis.Axis.set_view_interval") | unknown |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

class matplotlib.projections.polar.ThetaFormatter[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L225-L235)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.ThetaFormatter "Link to this definition")

Bases: [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")

Used to format the _theta_ tick labels. Converts the native unit of radians into degrees and adds a degree symbol.

class matplotlib.projections.polar.ThetaLocator(_base_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L261-L287)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.ThetaLocator "Link to this definition")

Bases: [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")

Used to locate theta ticks.

This will work the same as the base locator except in the case that the view spans the entire circle. In such cases, the previously used default locations of every 45 degrees are returned.

set\_axis(_axis_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L274-L276)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.ThetaLocator.set_axis "Link to this definition")

view\_limits(_vmin_, _vmax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L285-L287)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.ThetaLocator.view_limits "Link to this definition")

Select a scale for the range from vmin to vmax.

Subclasses should override this method to change locator behaviour.

class matplotlib.projections.polar.ThetaTick(_axes_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L290-L379)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.ThetaTick "Link to this definition")

Bases: [`XTick`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.XTick "matplotlib.axis.XTick")

A theta-axis tick.

This subclass of [`XTick`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.XTick "matplotlib.axis.XTick")
 provides angular ticks with some small modification to their re-positioning such that ticks are rotated based on tick location. This results in ticks that are correctly perpendicular to the arc spine.

When 'auto' rotation is enabled, labels are also rotated to be parallel to the spine. The label padding is also applied here since it's not possible to use a generic axes transform to produce tick-specific padding.

Parameters:

**loc**

The tick location in data coords.

**size**

The tick size in points.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _pad\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.ThetaTick.set "Link to this definition")

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
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`pad`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Tick.set_pad.html#matplotlib.axis.Tick.set_pad "matplotlib.axis.Tick.set_pad") | float |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Tick.set_url.html#matplotlib.axis.Tick.set_url "matplotlib.axis.Tick.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

update\_position(_loc_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/polar.py#L335-L379)
[#](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.ThetaTick.update_position "Link to this definition")

Set the location of tick in data coords with scalar _loc_.

On this page