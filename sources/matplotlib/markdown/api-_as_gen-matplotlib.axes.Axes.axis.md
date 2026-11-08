[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#main-content)

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
    

matplotlib.axes.Axes.axis[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib-axes-axes-axis "Link to this heading")

========================================================================================================================================================

Axes.axis(_arg\=None_, _/_, _\*_, _emit\=True_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L2146-L2282)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib.axes.Axes.axis "Link to this definition")

Convenience method to get or set some axis properties.

Call signatures:

xmin, xmax, ymin, ymax \= axis()
xmin, xmax, ymin, ymax \= axis(\[xmin, xmax, ymin, ymax\])
xmin, xmax, ymin, ymax \= axis(option)
xmin, xmax, ymin, ymax \= axis(\*\*kwargs)

Parameters:

**xmin, xmax, ymin, ymax**float, optional

The axis limits to be set. This can also be achieved using

ax.set(xlim\=(xmin, xmax), ylim\=(ymin, ymax))

**option**bool or str

If a bool, turns axis lines and labels on or off. If a string, possible values are:

| Value | Description |
| --- | --- |
| 'off' or [`False`](https://docs.python.org/3/library/constants.html#False "(in Python v3.14)") | Hide all axis decorations, i.e. axis labels, spines, tick marks, tick labels, and grid lines. This is the same as [`set_axis_off()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_off.html#matplotlib.axes.Axes.set_axis_off "matplotlib.axes.Axes.set_axis_off")<br>. |
| 'on' or [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)") | Do not hide all axis decorations, i.e. axis labels, spines, tick marks, tick labels, and grid lines. This is the same as [`set_axis_on()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_on.html#matplotlib.axes.Axes.set_axis_on "matplotlib.axes.Axes.set_axis_on")<br>. |
| 'equal' | Set equal scaling (i.e., make circles circular) by changing the axis limits. This is the same as `ax.set_aspect('equal', adjustable='datalim')`. Explicit data limits may not be respected in this case. |
| 'scaled' | Set equal scaling (i.e., make circles circular) by changing dimensions of the plot box. This is the same as `ax.set_aspect('equal', adjustable='box', anchor='C')`. Additionally, further autoscaling will be disabled. |
| 'tight' | Set limits just large enough to show all data, then disable further autoscaling. |
| 'auto' | Automatic scaling (fill plot box with data). |
| 'image' | 'scaled' with axis limits equal to data limits. |
| 'square' | Square plot; similar to 'scaled', but initially forcing `xmax-xmin == ymax-ymin`. |

**emit**bool, default: True

Whether observers are notified of the axis limit change. This option is passed on to [`set_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
 and [`set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
.

Returns:

**xmin, xmax, ymin, ymax**float

The axis limits.

See also

[`matplotlib.axes.Axes.set_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")

[`matplotlib.axes.Axes.set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")

Notes

For 3D Axes, this method additionally takes _zmin_, _zmax_ as parameters and likewise returns them.

Examples using `matplotlib.axes.Axes.axis`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#examples-using-matplotlib-axes-axes-axis "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_fill_thumb.png)

[Filled polygon](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill.html)

Filled polygon

![](https://matplotlib.org/stable/_images/sphx_glr_image_clip_path_thumb.png)

[Clipping images with patches](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_clip_path.html)

Clipping images with patches

![](https://matplotlib.org/stable/_images/sphx_glr_plot_streamplot_thumb.png)

[Streamplot](https://matplotlib.org/stable/gallery/images_contours_and_fields/plot_streamplot.html)

Streamplot

![](https://matplotlib.org/stable/_images/sphx_glr_bar_of_pie_thumb.png)

[Bar of pie](https://matplotlib.org/stable/gallery/pie_and_polar_charts/bar_of_pie.html)

Bar of pie

![](https://matplotlib.org/stable/_images/sphx_glr_hatch_style_reference_thumb.png)

[Hatch style reference](https://matplotlib.org/stable/gallery/shapes_and_collections/hatch_style_reference.html)

Hatch style reference

![](https://matplotlib.org/stable/_images/sphx_glr_path_patch_thumb.png)

[PathPatch object](https://matplotlib.org/stable/gallery/shapes_and_collections/path_patch.html)

PathPatch object

![](https://matplotlib.org/stable/_images/sphx_glr_color_cycle_default_thumb.png)

[Colors in the default property cycle](https://matplotlib.org/stable/gallery/color/color_cycle_default.html)

Colors in the default property cycle

![](https://matplotlib.org/stable/_images/sphx_glr_ggplot_thumb.png)

[ggplot style sheet](https://matplotlib.org/stable/gallery/style_sheets/ggplot.html)

ggplot style sheet

![](https://matplotlib.org/stable/_images/sphx_glr_parasite_simple2_thumb.png)

[Parasite Simple2](https://matplotlib.org/stable/gallery/axes_grid1/parasite_simple2.html)

Parasite Simple2

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axisline4_thumb.png)

[Simple Axisline4](https://matplotlib.org/stable/gallery/axes_grid1/simple_axisline4.html)

Simple Axisline4

![](https://matplotlib.org/stable/_images/sphx_glr_axis_direction_thumb.png)

[Axis Direction](https://matplotlib.org/stable/gallery/axisartist/axis_direction.html)

Axis Direction

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axis_direction_thumb.png)

[axis\_direction demo](https://matplotlib.org/stable/gallery/axisartist/demo_axis_direction.html)

axis\_direction demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axisline_style_thumb.png)

[Axis line styles](https://matplotlib.org/stable/gallery/axisartist/demo_axisline_style.html)

Axis line styles

![](https://matplotlib.org/stable/_images/sphx_glr_demo_floating_axes_thumb.png)

[floating\_axes features](https://matplotlib.org/stable/gallery/axisartist/demo_floating_axes.html)

floating\_axes features

![](https://matplotlib.org/stable/_images/sphx_glr_demo_parasite_axes_thumb.png)

[Parasite Axes demo](https://matplotlib.org/stable/gallery/axisartist/demo_parasite_axes.html)

Parasite Axes demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_parasite_axes2_thumb.png)

[Parasite axis demo](https://matplotlib.org/stable/gallery/axisartist/demo_parasite_axes2.html)

Parasite axis demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_ticklabel_alignment_thumb.png)

[Ticklabel alignment](https://matplotlib.org/stable/gallery/axisartist/demo_ticklabel_alignment.html)

Ticklabel alignment

![](https://matplotlib.org/stable/_images/sphx_glr_demo_ticklabel_direction_thumb.png)

[Ticklabel direction](https://matplotlib.org/stable/gallery/axisartist/demo_ticklabel_direction.html)

Ticklabel direction

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axis_direction01_thumb.png)

[Simple axis direction](https://matplotlib.org/stable/gallery/axisartist/simple_axis_direction01.html)

Simple axis direction

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axis_direction03_thumb.png)

[Simple axis tick label and tick directions](https://matplotlib.org/stable/gallery/axisartist/simple_axis_direction03.html)

Simple axis tick label and tick directions

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axis_pad_thumb.png)

[Simple axis pad](https://matplotlib.org/stable/gallery/axisartist/simple_axis_pad.html)

Simple axis pad

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axisartist1_thumb.png)

[Custom spines with axisartist](https://matplotlib.org/stable/gallery/axisartist/simple_axisartist1.html)

Custom spines with axisartist

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axisline_thumb.png)

[Simple Axisline](https://matplotlib.org/stable/gallery/axisartist/simple_axisline.html)

Simple Axisline

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axisline3_thumb.png)

[Simple Axisline3](https://matplotlib.org/stable/gallery/axisartist/simple_axisline3.html)

Simple Axisline3

![](https://matplotlib.org/stable/_images/sphx_glr_packed_bubbles_thumb.png)

[Packed-bubble chart](https://matplotlib.org/stable/gallery/misc/packed_bubbles.html)

Packed-bubble chart

![](https://matplotlib.org/stable/_images/sphx_glr_tickedstroke_demo_thumb.png)

[TickedStroke patheffect](https://matplotlib.org/stable/gallery/misc/tickedstroke_demo.html)

TickedStroke patheffect

![](https://matplotlib.org/stable/_images/sphx_glr_ishikawa_diagram_thumb.png)

[Ishikawa Diagram](https://matplotlib.org/stable/gallery/specialty_plots/ishikawa_diagram.html)

Ishikawa Diagram

![](https://matplotlib.org/stable/_images/sphx_glr_quick_start_thumb.png)

[Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)

Quick start guide

![](https://matplotlib.org/stable/_images/sphx_glr_colors_thumb.png)

[Specifying colors](https://matplotlib.org/stable/users/explain/colors/colors.html)

Specifying colors

![](https://matplotlib.org/stable/_images/sphx_glr_text_intro_thumb.png)

[Text in Matplotlib](https://matplotlib.org/stable/users/explain/text/text_intro.html)

Text in Matplotlib

On this page