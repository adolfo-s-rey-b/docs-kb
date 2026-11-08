[Skip to main content](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl-toolkits-mplot3d-axes3d-axes3d "Link to this heading")

=================================================================================================================================================================

class mpl\_toolkits.mplot3d.axes3d.Axes3D(_fig_, _rect\=None_, _\*args_, _elev\=30_, _azim\=\-60_, _roll\=0_, _shareview\=None_, _sharez\=None_, _proj\_type\='persp'_, _focal\_length\=None_, _box\_aspect\=None_, _computed\_zorder\=True_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L61-L4324)
[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "Link to this definition")

Bases: [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes._axes.Axes")

3D Axes object.

Note

As a user, you do not instantiate Axes directly, but use Axes creation methods instead; e.g. from [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 or [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
: [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
, [`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
 or [`Figure.add_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
.

Note

Some of the inherited behavior of Axes is not applicable to 3d and will raise an [`UnsupportedError`](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.UnsupportedError "matplotlib._api.UnsupportedError")
.

Parameters:

**fig**Figure

The parent figure.

**rect**tuple (left, bottom, width, height), default: (0, 0, 1, 1)

The `(left, bottom, width, height)` Axes position.

**elev**float, default: 30

The elevation angle in degrees rotates the camera above and below the x-y plane, with a positive angle corresponding to a location above the plane.

**azim**float, default: -60

The azimuthal angle in degrees rotates the camera about the z axis, with a positive angle corresponding to a right-handed rotation. In other words, a positive azimuth rotates the camera about the origin from its location along the +x axis towards the +y axis.

**roll**float, default: 0

The roll angle in degrees rotates the camera about the viewing axis. A positive angle spins the camera clockwise, causing the scene to rotate counter-clockwise.

**shareview**Axes3D, optional

Other Axes to share view angles with. Note that it is not possible to unshare axes.

**sharez**Axes3D, optional

Other Axes to share z-limits with. Note that it is not possible to unshare axes.

**proj\_type**{'persp', 'ortho'}

The projection type, default 'persp'.

**focal\_length**float, default: None

For a projection type of 'persp', the focal length of the virtual camera. Must be > 0. If None, defaults to 1. For a projection type of 'ortho', must be set to either None or infinity (numpy.inf). If None, defaults to infinity. The focal length can be computed from a desired Field Of View via the equation: focal\_length = 1/tan(FOV/2)

**box\_aspect**3-tuple of floats, default: None

Changes the physical dimensions of the Axes3D, such that the ratio of the axis lengths in display units is x:y:z. If None, defaults to 4:4:3

**computed\_zorder**bool, default: True

If True, the draw order is computed based on the average position along the view direction for supported artist types (currently Collections and Patches only). Set to False if you want to manually control the order in which Artists are drawn on top of each other using their _zorder_ attribute. This can be used for fine-tuning if the automatic order does not produce the desired result. Note however, that a manual order will only be correct for a limited view angle. If the figure is rotated by the user, it will look wrong from certain angles.

**\*\*kwargs**

Other optional keyword arguments:

| Property | Description |
| --- | --- |
| [`adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#matplotlib.axes.Axes.set_adjustable "matplotlib.axes.Axes.set_adjustable") | {'box', 'datalim'} |
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
| [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
| [`anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "matplotlib.axes.Axes.set_anchor") | (float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', ...} |
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
| [`aspect`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_aspect.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_aspect "mpl_toolkits.mplot3d.axes3d.Axes3D.set_aspect") | unknown |
| [`autoscale_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscale_on.html#matplotlib.axes.Axes.set_autoscale_on "matplotlib.axes.Axes.set_autoscale_on") | bool |
| [`autoscalex_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscalex_on.html#matplotlib.axes.Axes.set_autoscalex_on "matplotlib.axes.Axes.set_autoscalex_on") | unknown |
| [`autoscaley_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscaley_on.html#matplotlib.axes.Axes.set_autoscaley_on "matplotlib.axes.Axes.set_autoscaley_on") | unknown |
| [`autoscalez_on`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_autoscalez_on.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_autoscalez_on "mpl_toolkits.mplot3d.axes3d.Axes3D.set_autoscalez_on") | unknown |
| [`axes_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axes_locator.html#matplotlib.axes.Axes.set_axes_locator "matplotlib.axes.Axes.set_axes_locator") | Callable\[\[Axes, Renderer\], Bbox\] |
| [`axisbelow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axisbelow.html#matplotlib.axes.Axes.set_axisbelow "matplotlib.axes.Axes.set_axisbelow") | bool or 'line' |
| [`box_aspect`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect "mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect") | 3-tuple of floats or None |
| [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
| [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
| [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
| [`facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
| [`forward_navigation_events`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_forward_navigation_events.html#matplotlib.axes.Axes.set_forward_navigation_events "matplotlib.axes.Axes.set_forward_navigation_events") | bool or "auto" |
| [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
| [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
| [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
| [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
| [`navigate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate.html#matplotlib.axes.Axes.set_navigate "matplotlib.axes.Axes.set_navigate") | bool |
| [`navigate_mode`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate_mode.html#matplotlib.axes.Axes.set_navigate_mode "matplotlib.axes.Axes.set_navigate_mode") | unknown |
| [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
| [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
| [`position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib.axes.Axes.set_position "matplotlib.axes.Axes.set_position") | \[left, bottom, width, height\] or [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox") |
| [`proj_type`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_proj_type.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_proj_type "mpl_toolkits.mplot3d.axes3d.Axes3D.set_proj_type") | {'persp', 'ortho'} |
| [`prop_cycle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle "matplotlib.axes.Axes.set_prop_cycle") | [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)") |
| [`rasterization_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html#matplotlib.axes.Axes.set_rasterization_zorder "matplotlib.axes.Axes.set_rasterization_zorder") | float or None |
| [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
| [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
| [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
| [`subplotspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_subplotspec.html#matplotlib.axes.Axes.set_subplotspec "matplotlib.axes.Axes.set_subplotspec") | unknown |
| [`title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title") | unknown |
| [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
| [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
| [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
| [`xbound`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xbound.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_xbound "mpl_toolkits.mplot3d.axes3d.Axes3D.set_xbound") | unknown |
| [`xinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xinverted.html#matplotlib.axes.Axes.set_xinverted "matplotlib.axes.Axes.set_xinverted") | unknown |
| [`xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel") | str |
| [`xlim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim "mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim")<br> or [`xlim3d`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim "mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim") | (left: float, right: float) |
| [`xmargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xmargin.html#matplotlib.axes.Axes.set_xmargin "matplotlib.axes.Axes.set_xmargin") | float greater than -0.5 |
| [`xscale`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xscale.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_xscale "mpl_toolkits.mplot3d.axes3d.Axes3D.set_xscale") | {"linear", "log", "symlog", "logit", ...} |
| [`xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels") | unknown |
| [`xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks") | unknown |
| [`ybound`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_ybound.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_ybound "mpl_toolkits.mplot3d.axes3d.Axes3D.set_ybound") | unknown |
| [`yinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yinverted.html#matplotlib.axes.Axes.set_yinverted "matplotlib.axes.Axes.set_yinverted") | unknown |
| [`ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel") | str |
| [`ylim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim "mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim")<br> or [`ylim3d`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim "mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim") | (bottom: float, top: float) |
| [`ymargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html#matplotlib.axes.Axes.set_ymargin "matplotlib.axes.Axes.set_ymargin") | float greater than -0.5 |
| [`yscale`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_yscale.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_yscale "mpl_toolkits.mplot3d.axes3d.Axes3D.set_yscale") | {"linear", "log", "symlog", "logit", ...} |
| [`yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels") | unknown |
| [`yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks") | unknown |
| [`zbound`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zbound.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zbound "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zbound") | unknown |
| [`zinverted`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zinverted.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zinverted "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zinverted") | unknown |
| [`zlabel`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlabel.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlabel "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlabel") | unknown |
| [`zlim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim")<br> or [`zlim3d`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim") | (bottom: float, top: float) |
| [`zmargin`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zmargin.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zmargin "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zmargin") | float greater than -0.5 |
| [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |
| [`zscale`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zscale.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zscale "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zscale") | {"linear", "log", "symlog", "logit", ...} |
| [`zticklabels`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zticklabels.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zticklabels "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zticklabels") | unknown |
| [`zticks`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zticks.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zticks "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zticks") | unknown |

Plotting[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#plotting "Link to this heading")

------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`plot`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot "mpl_toolkits.mplot3d.axes3d.Axes3D.plot") | Plot 2D or 3D data. |
| [`scatter`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.scatter.html#mpl_toolkits.mplot3d.axes3d.Axes3D.scatter "mpl_toolkits.mplot3d.axes3d.Axes3D.scatter") | Create a scatter plot. |
| [`bar`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.bar.html#mpl_toolkits.mplot3d.axes3d.Axes3D.bar "mpl_toolkits.mplot3d.axes3d.Axes3D.bar") | Add 2D bar(s). |
| [`bar3d`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.bar3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D.bar3d "mpl_toolkits.mplot3d.axes3d.Axes3D.bar3d") | Generate a 3D barplot. |
| [`plot_surface`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface "mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface") | Create a surface plot. |
| [`plot_wireframe`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe "mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe") | Plot a 3D wireframe. |
| [`plot_trisurf`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf "mpl_toolkits.mplot3d.axes3d.Axes3D.plot_trisurf") | Plot a triangulated surface. |
| [`fill_between`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.fill_between.html#mpl_toolkits.mplot3d.axes3d.Axes3D.fill_between "mpl_toolkits.mplot3d.axes3d.Axes3D.fill_between") | Fill the area between two 3D curves. |
| [`clabel`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.clabel.html#mpl_toolkits.mplot3d.axes3d.Axes3D.clabel "mpl_toolkits.mplot3d.axes3d.Axes3D.clabel") | Currently not implemented for 3D Axes, and returns _None_. |
| [`contour`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.contour.html#mpl_toolkits.mplot3d.axes3d.Axes3D.contour "mpl_toolkits.mplot3d.axes3d.Axes3D.contour") | Create a 3D contour plot. |
| [`tricontour`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.tricontour.html#mpl_toolkits.mplot3d.axes3d.Axes3D.tricontour "mpl_toolkits.mplot3d.axes3d.Axes3D.tricontour") | Create a 3D contour plot. |
| [`contourf`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.contourf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.contourf "mpl_toolkits.mplot3d.axes3d.Axes3D.contourf") | Create a 3D filled contour plot. |
| [`tricontourf`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.tricontourf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.tricontourf "mpl_toolkits.mplot3d.axes3d.Axes3D.tricontourf") | Create a 3D filled contour plot. |
| [`quiver`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.quiver.html#mpl_toolkits.mplot3d.axes3d.Axes3D.quiver "mpl_toolkits.mplot3d.axes3d.Axes3D.quiver") | Plot a 3D field of arrows. |
| [`voxels`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.voxels.html#mpl_toolkits.mplot3d.axes3d.Axes3D.voxels "mpl_toolkits.mplot3d.axes3d.Axes3D.voxels") | Plot a set of filled voxels |
| [`errorbar`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.errorbar.html#mpl_toolkits.mplot3d.axes3d.Axes3D.errorbar "mpl_toolkits.mplot3d.axes3d.Axes3D.errorbar") | Plot lines and/or markers with errorbars around them. |
| [`stem`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.stem.html#mpl_toolkits.mplot3d.axes3d.Axes3D.stem "mpl_toolkits.mplot3d.axes3d.Axes3D.stem") | Create a 3D stem plot. |

Text and annotations[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#text-and-annotations "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`text`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.text.html#mpl_toolkits.mplot3d.axes3d.Axes3D.text "mpl_toolkits.mplot3d.axes3d.Axes3D.text") | Add the text _s_ to the 3D Axes at location _x_, _y_, _z_ in data coordinates. |
| [`text2D`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.text2D.html#mpl_toolkits.mplot3d.axes3d.Axes3D.text2D "mpl_toolkits.mplot3d.axes3d.Axes3D.text2D") | Add text to the Axes. |

Clearing[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#clearing "Link to this heading")

------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`clear`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.clear.html#mpl_toolkits.mplot3d.axes3d.Axes3D.clear "mpl_toolkits.mplot3d.axes3d.Axes3D.clear") | Clear the Axes. |

Appearance[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#appearance "Link to this heading")

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`set_axis_off`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_axis_off.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_axis_off "mpl_toolkits.mplot3d.axes3d.Axes3D.set_axis_off") | Hide all visual components of the x- and y-axis. |
| [`set_axis_on`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_axis_on.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_axis_on "mpl_toolkits.mplot3d.axes3d.Axes3D.set_axis_on") | Do not hide all visual components of the x- and y-axis. |
| [`grid`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.grid.html#mpl_toolkits.mplot3d.axes3d.Axes3D.grid "mpl_toolkits.mplot3d.axes3d.Axes3D.grid") | Set / unset 3D grid. |

Axis[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#axis "Link to this heading")

----------------------------------------------------------------------------------------------------

### Axis limits and direction[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#axis-limits-and-direction "Link to this heading")

|     |     |
| --- | --- |
| [`get_zaxis`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_zaxis.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_zaxis "mpl_toolkits.mplot3d.axes3d.Axes3D.get_zaxis") | Return the `ZAxis` ([`Axis`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis "mpl_toolkits.mplot3d.axis3d.Axis")<br>) instance. |
| [`get_xlim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_xlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_xlim "mpl_toolkits.mplot3d.axes3d.Axes3D.get_xlim") | Return the x-axis view limits. |
| [`set_xlim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim "mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim") | Set the 3D x-axis view limits. |
| [`get_ylim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_ylim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_ylim "mpl_toolkits.mplot3d.axes3d.Axes3D.get_ylim") | Return the y-axis view limits. |
| [`set_ylim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim "mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim") | Set the 3D y-axis view limits. |
| [`get_zlim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_zlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_zlim "mpl_toolkits.mplot3d.axes3d.Axes3D.get_zlim") | Return the 3D z-axis view limits. |
| [`set_zlim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim") | Set the 3D z-axis view limits. |
| [`get_w_lims`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_w_lims.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_w_lims "mpl_toolkits.mplot3d.axes3d.Axes3D.get_w_lims") | Get 3D world limits. |
| [`get_xinverted`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_xinverted.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_xinverted "mpl_toolkits.mplot3d.axes3d.Axes3D.get_xinverted") | Return whether the xaxis is oriented in the "inverse" direction. |
| [`set_xinverted`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xinverted.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_xinverted "mpl_toolkits.mplot3d.axes3d.Axes3D.set_xinverted") | Set whether the xaxis is oriented in the "inverse" direction. |
| [`invert_xaxis`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.invert_xaxis.html#mpl_toolkits.mplot3d.axes3d.Axes3D.invert_xaxis "mpl_toolkits.mplot3d.axes3d.Axes3D.invert_xaxis") | \[_Discouraged_\] Invert the x-axis. |
| [`xaxis_inverted`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.xaxis_inverted.html#mpl_toolkits.mplot3d.axes3d.Axes3D.xaxis_inverted "mpl_toolkits.mplot3d.axes3d.Axes3D.xaxis_inverted") | \[_Discouraged_\] Return whether the xaxis is oriented in the "inverse" direction. |
| [`get_yinverted`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_yinverted.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_yinverted "mpl_toolkits.mplot3d.axes3d.Axes3D.get_yinverted") | Return whether the yaxis is oriented in the "inverse" direction. |
| [`set_yinverted`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_yinverted.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_yinverted "mpl_toolkits.mplot3d.axes3d.Axes3D.set_yinverted") | Set whether the yaxis is oriented in the "inverse" direction. |
| [`invert_yaxis`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.invert_yaxis.html#mpl_toolkits.mplot3d.axes3d.Axes3D.invert_yaxis "mpl_toolkits.mplot3d.axes3d.Axes3D.invert_yaxis") | \[_Discouraged_\] Invert the y-axis. |
| [`yaxis_inverted`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.yaxis_inverted.html#mpl_toolkits.mplot3d.axes3d.Axes3D.yaxis_inverted "mpl_toolkits.mplot3d.axes3d.Axes3D.yaxis_inverted") | \[_Discouraged_\] Return whether the yaxis is oriented in the "inverse" direction. |
| [`get_zinverted`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_zinverted.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_zinverted "mpl_toolkits.mplot3d.axes3d.Axes3D.get_zinverted") | Return whether the zaxis is oriented in the "inverse" direction. |
| [`set_zinverted`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zinverted.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zinverted "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zinverted") | Set whether the zaxis is oriented in the "inverse" direction. |
| [`invert_zaxis`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.invert_zaxis.html#mpl_toolkits.mplot3d.axes3d.Axes3D.invert_zaxis "mpl_toolkits.mplot3d.axes3d.Axes3D.invert_zaxis") | \[_Discouraged_\] Invert the z-axis. |
| [`zaxis_inverted`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.zaxis_inverted.html#mpl_toolkits.mplot3d.axes3d.Axes3D.zaxis_inverted "mpl_toolkits.mplot3d.axes3d.Axes3D.zaxis_inverted") | \[_Discouraged_\] Return whether the zaxis is oriented in the "inverse" direction. |
| [`get_xbound`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_xbound.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_xbound "mpl_toolkits.mplot3d.axes3d.Axes3D.get_xbound") | Return the lower and upper x-axis bounds, in increasing order. |
| [`set_xbound`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xbound.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_xbound "mpl_toolkits.mplot3d.axes3d.Axes3D.set_xbound") | Set the lower and upper numerical bounds of the x-axis. |
| [`get_ybound`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_ybound.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_ybound "mpl_toolkits.mplot3d.axes3d.Axes3D.get_ybound") | Return the lower and upper y-axis bounds, in increasing order. |
| [`set_ybound`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_ybound.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_ybound "mpl_toolkits.mplot3d.axes3d.Axes3D.set_ybound") | Set the lower and upper numerical bounds of the y-axis. |
| [`get_zbound`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_zbound.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_zbound "mpl_toolkits.mplot3d.axes3d.Axes3D.get_zbound") | Return the lower and upper z-axis bounds, in increasing order. |
| [`set_zbound`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zbound.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zbound "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zbound") | Set the lower and upper numerical bounds of the z-axis. |

### Axis labels and title[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#axis-labels-and-title "Link to this heading")

|     |     |
| --- | --- |
| [`set_zlabel`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlabel.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlabel "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlabel") | Set zlabel. |
| [`get_zlabel`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_zlabel.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_zlabel "mpl_toolkits.mplot3d.axes3d.Axes3D.get_zlabel") | Get the z-label text string. |
| [`set_title`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_title.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_title "mpl_toolkits.mplot3d.axes3d.Axes3D.set_title") | Set a title for the Axes. |

### Axis scales[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#axis-scales "Link to this heading")

|     |     |
| --- | --- |
| [`set_xscale`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xscale.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_xscale "mpl_toolkits.mplot3d.axes3d.Axes3D.set_xscale") | Set the x-axis scale. |
| [`set_yscale`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_yscale.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_yscale "mpl_toolkits.mplot3d.axes3d.Axes3D.set_yscale") | Set the y-axis scale. |
| [`set_zscale`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zscale.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zscale "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zscale") | Set the z-axis scale. |
| [`get_zscale`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_zscale.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_zscale "mpl_toolkits.mplot3d.axes3d.Axes3D.get_zscale") | Return the zaxis' scale (as a str). |

### Autoscaling and margins[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#autoscaling-and-margins "Link to this heading")

|     |     |
| --- | --- |
| [`get_zmargin`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_zmargin.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_zmargin "mpl_toolkits.mplot3d.axes3d.Axes3D.get_zmargin") | Retrieve autoscaling margin of the z-axis. |
| [`set_zmargin`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zmargin.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zmargin "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zmargin") | Set padding of Z data limits prior to autoscaling. |
| [`margins`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.margins.html#mpl_toolkits.mplot3d.axes3d.Axes3D.margins "mpl_toolkits.mplot3d.axes3d.Axes3D.margins") | Set or retrieve autoscaling margins. |
| [`autoscale`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.autoscale.html#mpl_toolkits.mplot3d.axes3d.Axes3D.autoscale "mpl_toolkits.mplot3d.axes3d.Axes3D.autoscale") | Convenience method for simple axis view autoscaling. |
| [`autoscale_view`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.autoscale_view.html#mpl_toolkits.mplot3d.axes3d.Axes3D.autoscale_view "mpl_toolkits.mplot3d.axes3d.Axes3D.autoscale_view") | Autoscale the view limits using the data limits. |
| [`set_autoscalez_on`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_autoscalez_on.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_autoscalez_on "mpl_toolkits.mplot3d.axes3d.Axes3D.set_autoscalez_on") | Set whether the zaxis is autoscaled when drawing or by [`Axes.autoscale_view`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")<br>. |
| [`get_autoscalez_on`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_autoscalez_on.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_autoscalez_on "mpl_toolkits.mplot3d.axes3d.Axes3D.get_autoscalez_on") | Return whether the zaxis is autoscaled. |
| [`auto_scale_xyz`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.auto_scale_xyz.html#mpl_toolkits.mplot3d.axes3d.Axes3D.auto_scale_xyz "mpl_toolkits.mplot3d.axes3d.Axes3D.auto_scale_xyz") |     |

### Aspect ratio[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#aspect-ratio "Link to this heading")

|     |     |
| --- | --- |
| [`set_aspect`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_aspect.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_aspect "mpl_toolkits.mplot3d.axes3d.Axes3D.set_aspect") | Set the aspect ratios. |
| [`set_box_aspect`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect "mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect") | Set the Axes box aspect. |
| [`apply_aspect`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.apply_aspect.html#mpl_toolkits.mplot3d.axes3d.Axes3D.apply_aspect "mpl_toolkits.mplot3d.axes3d.Axes3D.apply_aspect") | Adjust the Axes for a specified data aspect ratio. |

### Ticks[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#ticks "Link to this heading")

|     |     |
| --- | --- |
| [`tick_params`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.tick_params.html#mpl_toolkits.mplot3d.axes3d.Axes3D.tick_params "mpl_toolkits.mplot3d.axes3d.Axes3D.tick_params") | Convenience method for changing the appearance of ticks and tick labels. |
| [`set_zticks`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zticks.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zticks "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zticks") | Set the zaxis' tick locations and optionally tick labels. |
| [`get_zticks`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_zticks.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_zticks "mpl_toolkits.mplot3d.axes3d.Axes3D.get_zticks") | Return the zaxis' tick locations in data coordinates. |
| [`set_zticklabels`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zticklabels.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zticklabels "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zticklabels") | \[_Discouraged_\] Set the zaxis' tick labels with list of string labels. |
| [`get_zticklines`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_zticklines.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_zticklines "mpl_toolkits.mplot3d.axes3d.Axes3D.get_zticklines") | Return the zaxis' tick lines as a list of [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")<br>. |
| [`get_zgridlines`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_zgridlines.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_zgridlines "mpl_toolkits.mplot3d.axes3d.Axes3D.get_zgridlines") | Return the zaxis' grid lines as a list of [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")<br>. |
| [`get_zminorticklabels`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_zminorticklabels.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_zminorticklabels "mpl_toolkits.mplot3d.axes3d.Axes3D.get_zminorticklabels") | Return the zaxis' minor tick labels, as a list of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")<br>. |
| [`get_zmajorticklabels`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_zmajorticklabels.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_zmajorticklabels "mpl_toolkits.mplot3d.axes3d.Axes3D.get_zmajorticklabels") | Return the zaxis' major tick labels, as a list of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")<br>. |
| [`zaxis_date`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.zaxis_date.html#mpl_toolkits.mplot3d.axes3d.Axes3D.zaxis_date "mpl_toolkits.mplot3d.axes3d.Axes3D.zaxis_date") | Set up axis ticks and labels to treat data along the zaxis as dates. |

Units[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#units "Link to this heading")

------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`convert_zunits`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.convert_zunits.html#mpl_toolkits.mplot3d.axes3d.Axes3D.convert_zunits "mpl_toolkits.mplot3d.axes3d.Axes3D.convert_zunits") | For artists in an Axes, if the zaxis has units support, convert _z_ using zaxis unit type |

Adding artists[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#adding-artists "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`add_collection3d`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.add_collection3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D.add_collection3d "mpl_toolkits.mplot3d.axes3d.Axes3D.add_collection3d") | Add a 3D collection object to the plot. |

Sharing[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#sharing "Link to this heading")

----------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`sharez`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.sharez.html#mpl_toolkits.mplot3d.axes3d.Axes3D.sharez "mpl_toolkits.mplot3d.axes3d.Axes3D.sharez") | Share the z-axis with _other_. |
| [`shareview`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.shareview.html#mpl_toolkits.mplot3d.axes3d.Axes3D.shareview "mpl_toolkits.mplot3d.axes3d.Axes3D.shareview") | Share the view angles with _other_. |

Interactive[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#interactive "Link to this heading")

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`can_zoom`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.can_zoom.html#mpl_toolkits.mplot3d.axes3d.Axes3D.can_zoom "mpl_toolkits.mplot3d.axes3d.Axes3D.can_zoom") | Return whether this Axes supports the zoom box button functionality. |
| [`can_pan`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.can_pan.html#mpl_toolkits.mplot3d.axes3d.Axes3D.can_pan "mpl_toolkits.mplot3d.axes3d.Axes3D.can_pan") | Return whether this Axes supports any pan/zoom button functionality. |
| [`disable_mouse_rotation`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.disable_mouse_rotation.html#mpl_toolkits.mplot3d.axes3d.Axes3D.disable_mouse_rotation "mpl_toolkits.mplot3d.axes3d.Axes3D.disable_mouse_rotation") | Disable mouse buttons for 3D rotation, panning, and zooming. |
| [`mouse_init`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.mouse_init.html#mpl_toolkits.mplot3d.axes3d.Axes3D.mouse_init "mpl_toolkits.mplot3d.axes3d.Axes3D.mouse_init") | Set the mouse buttons for 3D rotation and zooming. |
| [`drag_pan`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.drag_pan.html#mpl_toolkits.mplot3d.axes3d.Axes3D.drag_pan "mpl_toolkits.mplot3d.axes3d.Axes3D.drag_pan") | Called when the mouse moves during a pan operation. |
| [`format_zdata`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.format_zdata.html#mpl_toolkits.mplot3d.axes3d.Axes3D.format_zdata "mpl_toolkits.mplot3d.axes3d.Axes3D.format_zdata") | Return _z_ string formatted. |
| [`format_coord`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.format_coord.html#mpl_toolkits.mplot3d.axes3d.Axes3D.format_coord "mpl_toolkits.mplot3d.axes3d.Axes3D.format_coord") | Return a string giving the current view rotation angles, or the x, y, z coordinates of the point on the nearest axis pane underneath the mouse cursor, depending on the mouse button pressed. |

Projection and perspective[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#projection-and-perspective "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`view_init`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.view_init.html#mpl_toolkits.mplot3d.axes3d.Axes3D.view_init "mpl_toolkits.mplot3d.axes3d.Axes3D.view_init") | Set the elevation and azimuth of the Axes in degrees (not radians). |
| [`set_proj_type`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_proj_type.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_proj_type "mpl_toolkits.mplot3d.axes3d.Axes3D.set_proj_type") | Set the projection type. |
| [`get_proj`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_proj.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_proj "mpl_toolkits.mplot3d.axes3d.Axes3D.get_proj") | Create the projection matrix from the current viewing position. |
| [`set_top_view`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_top_view.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_top_view "mpl_toolkits.mplot3d.axes3d.Axes3D.set_top_view") |     |

Drawing[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#drawing "Link to this heading")

----------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`draw`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.draw.html#mpl_toolkits.mplot3d.axes3d.Axes3D.draw "mpl_toolkits.mplot3d.axes3d.Axes3D.draw") | Draw the Artist (and its children) using the given renderer. |
| [`get_tightbbox`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_tightbbox.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_tightbbox "mpl_toolkits.mplot3d.axes3d.Axes3D.get_tightbbox") | Return the tight bounding box of the Axes, including axis and their decorators (xlabel, title, etc). |

Aliases and deprecated methods[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#aliases-and-deprecated-methods "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`set_zlim3d`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim3d "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim3d") | Alias for [`set_zlim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim")<br>. |
| [`stem3D`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.stem3D.html#mpl_toolkits.mplot3d.axes3d.Axes3D.stem3D "mpl_toolkits.mplot3d.axes3d.Axes3D.stem3D") | Create a 3D stem plot. |
| [`text3D`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.text3D.html#mpl_toolkits.mplot3d.axes3d.Axes3D.text3D "mpl_toolkits.mplot3d.axes3d.Axes3D.text3D") | Add the text _s_ to the 3D Axes at location _x_, _y_, _z_ in data coordinates. |

Other[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#other "Link to this heading")

------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`get_axis_position`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_axis_position.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_axis_position "mpl_toolkits.mplot3d.axes3d.Axes3D.get_axis_position") |     |
| [`add_contour_set`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.add_contour_set.html#mpl_toolkits.mplot3d.axes3d.Axes3D.add_contour_set "mpl_toolkits.mplot3d.axes3d.Axes3D.add_contour_set") |     |
| [`add_contourf_set`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.add_contourf_set.html#mpl_toolkits.mplot3d.axes3d.Axes3D.add_contourf_set "mpl_toolkits.mplot3d.axes3d.Axes3D.add_contourf_set") |     |
| [`update_datalim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.update_datalim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.update_datalim "mpl_toolkits.mplot3d.axes3d.Axes3D.update_datalim") | Not implemented in [`Axes3D`](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.axes3d.Axes3D")<br>. |

Sample 3D data[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#sample-3d-data "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`axes3d.get_test_data`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.get_test_data.html#mpl_toolkits.mplot3d.axes3d.get_test_data "mpl_toolkits.mplot3d.axes3d.get_test_data") | Return a tuple X, Y, Z with a test data set. |

### Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D`[#](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d "Link to this heading")

![](https://matplotlib.org/stable/_images/sphx_glr_2dcollections3d_thumb.png)

[Plot 2D data on 3D plot](https://matplotlib.org/stable/gallery/mplot3d/2dcollections3d.html)

Plot 2D data on 3D plot

![](https://matplotlib.org/stable/_images/sphx_glr_3d_bars_thumb.png)

[Demo of 3D bar charts](https://matplotlib.org/stable/gallery/mplot3d/3d_bars.html)

Demo of 3D bar charts

![](https://matplotlib.org/stable/_images/sphx_glr_axlim_clip_thumb.png)

[Clip the data to the axes view limits](https://matplotlib.org/stable/gallery/mplot3d/axlim_clip.html)

Clip the data to the axes view limits

![](https://matplotlib.org/stable/_images/sphx_glr_bars3d_thumb.png)

[Create 2D bar graphs in different planes](https://matplotlib.org/stable/gallery/mplot3d/bars3d.html)

Create 2D bar graphs in different planes

![](https://matplotlib.org/stable/_images/sphx_glr_box3d_thumb.png)

[3D box surface plot](https://matplotlib.org/stable/gallery/mplot3d/box3d.html)

3D box surface plot

![](https://matplotlib.org/stable/_images/sphx_glr_contour3d_thumb.png)

[Plot contour (level) curves in 3D](https://matplotlib.org/stable/gallery/mplot3d/contour3d.html)

Plot contour (level) curves in 3D

![](https://matplotlib.org/stable/_images/sphx_glr_contour3d_2_thumb.png)

[Plot contour (level) curves in 3D using the extend3d option](https://matplotlib.org/stable/gallery/mplot3d/contour3d_2.html)

Plot contour (level) curves in 3D using the extend3d option

![](https://matplotlib.org/stable/_images/sphx_glr_contour3d_3_thumb.png)

[Project contour profiles onto a graph](https://matplotlib.org/stable/gallery/mplot3d/contour3d_3.html)

Project contour profiles onto a graph

![](https://matplotlib.org/stable/_images/sphx_glr_contourf3d_thumb.png)

[Filled contours](https://matplotlib.org/stable/gallery/mplot3d/contourf3d.html)

Filled contours

![](https://matplotlib.org/stable/_images/sphx_glr_contourf3d_2_thumb.png)

[Project filled contour onto a graph](https://matplotlib.org/stable/gallery/mplot3d/contourf3d_2.html)

Project filled contour onto a graph

![](https://matplotlib.org/stable/_images/sphx_glr_custom_shaded_3d_surface_thumb.png)

[Custom hillshading in a 3D surface plot](https://matplotlib.org/stable/gallery/mplot3d/custom_shaded_3d_surface.html)

Custom hillshading in a 3D surface plot

![](https://matplotlib.org/stable/_images/sphx_glr_errorbar3d_thumb.png)

[3D errorbars](https://matplotlib.org/stable/gallery/mplot3d/errorbar3d.html)

3D errorbars

![](https://matplotlib.org/stable/_images/sphx_glr_fillbetween3d_thumb.png)

[Fill between 3D lines](https://matplotlib.org/stable/gallery/mplot3d/fillbetween3d.html)

Fill between 3D lines

![](https://matplotlib.org/stable/_images/sphx_glr_fillunder3d_thumb.png)

[Fill under 3D line graphs](https://matplotlib.org/stable/gallery/mplot3d/fillunder3d.html)

Fill under 3D line graphs

![](https://matplotlib.org/stable/_images/sphx_glr_hist3d_thumb.png)

[Create 3D histogram of 2D data](https://matplotlib.org/stable/gallery/mplot3d/hist3d.html)

Create 3D histogram of 2D data

![](https://matplotlib.org/stable/_images/sphx_glr_imshow3d_thumb.png)

[2D images in 3D](https://matplotlib.org/stable/gallery/mplot3d/imshow3d.html)

2D images in 3D

![](https://matplotlib.org/stable/_images/sphx_glr_lines3d_thumb.png)

[Parametric curve](https://matplotlib.org/stable/gallery/mplot3d/lines3d.html)

Parametric curve

![](https://matplotlib.org/stable/_images/sphx_glr_lorenz_attractor_thumb.png)

[Lorenz attractor](https://matplotlib.org/stable/gallery/mplot3d/lorenz_attractor.html)

Lorenz attractor

![](https://matplotlib.org/stable/_images/sphx_glr_mixed_subplots_thumb.png)

[2D and 3D Axes in same figure](https://matplotlib.org/stable/gallery/mplot3d/mixed_subplots.html)

2D and 3D Axes in same figure

![](https://matplotlib.org/stable/_images/sphx_glr_offset_thumb.png)

[Automatic text offsetting](https://matplotlib.org/stable/gallery/mplot3d/offset.html)

Automatic text offsetting

![](https://matplotlib.org/stable/_images/sphx_glr_pathpatch3d_thumb.png)

[Draw flat objects in 3D plot](https://matplotlib.org/stable/gallery/mplot3d/pathpatch3d.html)

Draw flat objects in 3D plot

![](https://matplotlib.org/stable/_images/sphx_glr_polys3d_thumb.png)

[Generate 3D polygons](https://matplotlib.org/stable/gallery/mplot3d/polys3d.html)

Generate 3D polygons

![](https://matplotlib.org/stable/_images/sphx_glr_projections_thumb.png)

[3D plot projection types](https://matplotlib.org/stable/gallery/mplot3d/projections.html)

3D plot projection types

![](https://matplotlib.org/stable/_images/sphx_glr_quiver3d_thumb.png)

[3D quiver plot](https://matplotlib.org/stable/gallery/mplot3d/quiver3d.html)

3D quiver plot

![](https://matplotlib.org/stable/_images/sphx_glr_scales3d_thumb.png)

[Scales on 3D (Log, Symlog, etc.)](https://matplotlib.org/stable/gallery/mplot3d/scales3d.html)

Scales on 3D (Log, Symlog, etc.)

![](https://matplotlib.org/stable/_images/sphx_glr_scatter3d_thumb.png)

[3D scatterplot](https://matplotlib.org/stable/gallery/mplot3d/scatter3d.html)

3D scatterplot

![](https://matplotlib.org/stable/_images/sphx_glr_stem3d_demo_thumb.png)

[3D stem](https://matplotlib.org/stable/gallery/mplot3d/stem3d_demo.html)

3D stem

![](https://matplotlib.org/stable/_images/sphx_glr_subplot3d_thumb.png)

[3D plots as subplots](https://matplotlib.org/stable/gallery/mplot3d/subplot3d.html)

3D plots as subplots

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_thumb.png)

[3D surface (colormap)](https://matplotlib.org/stable/gallery/mplot3d/surface3d.html)

3D surface (colormap)

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_2_thumb.png)

[3D surface (solid color)](https://matplotlib.org/stable/gallery/mplot3d/surface3d_2.html)

3D surface (solid color)

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_3_thumb.png)

[3D surface (checkerboard)](https://matplotlib.org/stable/gallery/mplot3d/surface3d_3.html)

3D surface (checkerboard)

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_radial_thumb.png)

[3D surface with polar coordinates](https://matplotlib.org/stable/gallery/mplot3d/surface3d_radial.html)

3D surface with polar coordinates

![](https://matplotlib.org/stable/_images/sphx_glr_text3d_thumb.png)

[Text annotations in 3D](https://matplotlib.org/stable/gallery/mplot3d/text3d.html)

Text annotations in 3D

![](https://matplotlib.org/stable/_images/sphx_glr_tricontour3d_thumb.png)

[Triangular 3D contour plot](https://matplotlib.org/stable/gallery/mplot3d/tricontour3d.html)

Triangular 3D contour plot

![](https://matplotlib.org/stable/_images/sphx_glr_tricontourf3d_thumb.png)

[Triangular 3D filled contour plot](https://matplotlib.org/stable/gallery/mplot3d/tricontourf3d.html)

Triangular 3D filled contour plot

![](https://matplotlib.org/stable/_images/sphx_glr_trisurf3d_thumb.png)

[Triangular 3D surfaces](https://matplotlib.org/stable/gallery/mplot3d/trisurf3d.html)

Triangular 3D surfaces

![](https://matplotlib.org/stable/_images/sphx_glr_trisurf3d_2_thumb.png)

[More triangular 3D surfaces](https://matplotlib.org/stable/gallery/mplot3d/trisurf3d_2.html)

More triangular 3D surfaces

![](https://matplotlib.org/stable/_images/sphx_glr_voxels_thumb.png)

[3D voxel / volumetric plot](https://matplotlib.org/stable/gallery/mplot3d/voxels.html)

3D voxel / volumetric plot

![](https://matplotlib.org/stable/_images/sphx_glr_voxels_numpy_logo_thumb.png)

[3D voxel plot of the NumPy logo](https://matplotlib.org/stable/gallery/mplot3d/voxels_numpy_logo.html)

3D voxel plot of the NumPy logo

![](https://matplotlib.org/stable/_images/sphx_glr_voxels_rgb_thumb.png)

[3D voxel / volumetric plot with RGB colors](https://matplotlib.org/stable/gallery/mplot3d/voxels_rgb.html)

3D voxel / volumetric plot with RGB colors

![](https://matplotlib.org/stable/_images/sphx_glr_voxels_torus_thumb.png)

[3D voxel / volumetric plot with cylindrical coordinates](https://matplotlib.org/stable/gallery/mplot3d/voxels_torus.html)

3D voxel / volumetric plot with cylindrical coordinates

![](https://matplotlib.org/stable/_images/sphx_glr_wire3d_thumb.png)

[3D wireframe plot](https://matplotlib.org/stable/gallery/mplot3d/wire3d.html)

3D wireframe plot

![](https://matplotlib.org/stable/_images/sphx_glr_wire3d_animation_thumb.gif)

[Animate a 3D wireframe plot](https://matplotlib.org/stable/gallery/mplot3d/wire3d_animation.html)

Animate a 3D wireframe plot

![](https://matplotlib.org/stable/_images/sphx_glr_wire3d_zero_stride_thumb.png)

[3D wireframe plots in one direction](https://matplotlib.org/stable/gallery/mplot3d/wire3d_zero_stride.html)

3D wireframe plots in one direction

![](https://matplotlib.org/stable/_images/sphx_glr_random_walk_thumb.gif)

[Animated 3D random walk](https://matplotlib.org/stable/gallery/animation/random_walk.html)

Animated 3D random walk

![](https://matplotlib.org/stable/_images/sphx_glr_bar3d_simple_thumb.png)

[bar3d(x, y, z, dx, dy, dz)](https://matplotlib.org/stable/plot_types/3D/bar3d_simple.html)

bar3d(x, y, z, dx, dy, dz)

![](https://matplotlib.org/stable/_images/sphx_glr_fill_between3d_simple_thumb.png)

[fill\_between(x1, y1, z1, x2, y2, z2)](https://matplotlib.org/stable/plot_types/3D/fill_between3d_simple.html)

fill\_between(x1, y1, z1, x2, y2, z2)

![](https://matplotlib.org/stable/_images/sphx_glr_plot3d_simple_thumb.png)

[plot(xs, ys, zs)](https://matplotlib.org/stable/plot_types/3D/plot3d_simple.html)

plot(xs, ys, zs)

![](https://matplotlib.org/stable/_images/sphx_glr_quiver3d_simple_thumb.png)

[quiver(X, Y, Z, U, V, W)](https://matplotlib.org/stable/plot_types/3D/quiver3d_simple.html)

quiver(X, Y, Z, U, V, W)

![](https://matplotlib.org/stable/_images/sphx_glr_scatter3d_simple_thumb.png)

[scatter(xs, ys, zs)](https://matplotlib.org/stable/plot_types/3D/scatter3d_simple.html)

scatter(xs, ys, zs)

![](https://matplotlib.org/stable/_images/sphx_glr_stem3d_thumb.png)

[stem(x, y, z)](https://matplotlib.org/stable/plot_types/3D/stem3d.html)

stem(x, y, z)

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_simple_thumb.png)

[plot\_surface(X, Y, Z)](https://matplotlib.org/stable/plot_types/3D/surface3d_simple.html)

plot\_surface(X, Y, Z)

![](https://matplotlib.org/stable/_images/sphx_glr_trisurf3d_simple_thumb.png)

[plot\_trisurf(x, y, z)](https://matplotlib.org/stable/plot_types/3D/trisurf3d_simple.html)

plot\_trisurf(x, y, z)

![](https://matplotlib.org/stable/_images/sphx_glr_voxels_simple_thumb.png)

[voxels(\[x, y, z\], filled)](https://matplotlib.org/stable/plot_types/3D/voxels_simple.html)

voxels(\[x, y, z\], filled)

![](https://matplotlib.org/stable/_images/sphx_glr_wire3d_simple_thumb.png)

[plot\_wireframe(X, Y, Z)](https://matplotlib.org/stable/plot_types/3D/wire3d_simple.html)

plot\_wireframe(X, Y, Z)

On this page