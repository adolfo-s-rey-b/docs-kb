[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.zoomed_inset_axes.html#main-content)

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
    

mpl\_toolkits.axes\_grid1.inset\_locator.zoomed\_inset\_axes[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.zoomed_inset_axes.html#mpl-toolkits-axes-grid1-inset-locator-zoomed-inset-axes "Link to this heading")

=======================================================================================================================================================================================================================================================

mpl\_toolkits.axes\_grid1.inset\_locator.zoomed\_inset\_axes(_parent\_axes_, _zoom_, _loc\='upper right'_, _bbox\_to\_anchor\=None_, _bbox\_transform\=None_, _axes\_class\=None_, _axes\_kwargs\=None_, _borderpad\=0.5_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/inset_locator.py#L382-L456)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.zoomed_inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.zoomed_inset_axes "Link to this definition")

Create an anchored inset axes by scaling a parent axes. For usage, also see [the examples](https://matplotlib.org/stable/gallery/axes_grid1/inset_locator_demo2.html)
.

Parameters:

**parent\_axes**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

Axes to place the inset axes.

**zoom**float

Scaling factor of the data axes. _zoom_ > 1 will enlarge the coordinates (i.e., "zoomed in"), while _zoom_ < 1 will shrink the coordinates (i.e., "zoomed out").

**loc**str, default: 'upper right'

Location to place the inset axes. Valid locations are 'upper left', 'upper center', 'upper right', 'center left', 'center', 'center right', 'lower left', 'lower center', 'lower right'. For backward compatibility, numeric values are accepted as well. See the parameter _loc_ of [`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 for details.

**bbox\_to\_anchor**tuple or [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")
, optional

Bbox that the inset axes will be anchored to. If None, _parent\_axes.bbox_ is used. If a tuple, can be either \[left, bottom, width, height\], or \[left, bottom\]. If the kwargs _width_ and/or _height_ are specified in relative units, the 2-tuple \[left, bottom\] cannot be used. Note that the units of the bounding box are determined through the transform in use. When using _bbox\_to\_anchor_ it almost always makes sense to also specify a _bbox\_transform_. This might often be the axes transform _parent\_axes.transAxes_.

**bbox\_transform**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
, optional

Transformation for the bbox that contains the inset axes. If None, a [`transforms.IdentityTransform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform")
 is used (i.e. pixel coordinates). This is useful when not providing any argument to _bbox\_to\_anchor_. When using _bbox\_to\_anchor_ it almost always makes sense to also specify a _bbox\_transform_. This might often be the axes transform _parent\_axes.transAxes_. Inversely, when specifying the axes- or figure-transform here, be aware that not specifying _bbox\_to\_anchor_ will use _parent\_axes.bbox_, the units of which are in display (pixel) coordinates.

**axes\_class**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 type, default: [`HostAxes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.parasite_axes.HostAxes.html#mpl_toolkits.axes_grid1.parasite_axes.HostAxes "mpl_toolkits.axes_grid1.parasite_axes.HostAxes")

The type of the newly created inset axes.

**axes\_kwargs**dict, optional

Keyword arguments to pass to the constructor of the inset axes. Valid arguments include:

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

**borderpad**float, default: 0.5

Padding between inset axes and the bbox\_to\_anchor. The units are axes font size, i.e. for a default font size of 10 points _borderpad = 0.5_ is equivalent to a padding of 5 points.

Returns:

**inset\_axes**_axes\_class_

Inset axes object created.

Examples using `mpl_toolkits.axes_grid1.inset_locator.zoomed_inset_axes`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.zoomed_inset_axes.html#examples-using-mpl-toolkits-axes-grid1-inset-locator-zoomed-inset-axes "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_inset_locator_demo2_thumb.png)

[Inset locator demo 2](https://matplotlib.org/stable/gallery/axes_grid1/inset_locator_demo2.html)

Inset locator demo 2

On this page