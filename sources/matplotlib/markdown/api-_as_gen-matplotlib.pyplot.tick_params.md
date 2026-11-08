[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tick_params.html#main-content)

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
    

matplotlib.pyplot.tick\_params[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tick_params.html#matplotlib-pyplot-tick-params "Link to this heading")

=====================================================================================================================================================================

matplotlib.pyplot.tick\_params(_axis\='both'_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L4394-L4396)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tick_params.html#matplotlib.pyplot.tick_params "Link to this definition")

Change the appearance of ticks, tick labels, and gridlines.

Tick properties that are not explicitly set using the keyword arguments remain unchanged unless _reset_ is True. For the current style settings, see [`Axis.get_tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_tick_params.html#matplotlib.axis.Axis.get_tick_params "matplotlib.axis.Axis.get_tick_params")
.

Parameters:

**axis**{'x', 'y', 'both'}, default: 'both'

The axis to which the parameters are applied.

**which**{'major', 'minor', 'both'}, default: 'major'

The group of ticks to which the parameters are applied.

**reset**bool, default: False

Whether to reset the ticks to defaults before updating them.

Other Parameters:

**direction**{'in', 'out', 'inout'}

Puts ticks inside the Axes, outside the Axes, or both.

**length**float

Tick length in points.

**width**float

Tick width in points.

**color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

Tick color.

**pad**float

Distance in points between tick and label.

**labelsize**float or str

Tick label font size in points or as a string (e.g., 'large').

**labelcolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

Tick label color.

**labelfontfamily**str

Tick label font.

**colors**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

Tick color and label color.

**zorder**float

Tick and label zorder.

**bottom, top, left, right**bool

Whether to draw the respective ticks.

**labelbottom, labeltop, labelleft, labelright**bool

Whether to draw the respective tick labels.

**labelrotation**float

Tick label rotation angle in degrees. See [`Text.set_rotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation "matplotlib.text.Text.set_rotation")
.

**labelrotation\_mode**{'default', 'anchor', 'xtick', 'ytick'}

Tick label rotation mode. See [`Text.set_rotation_mode`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation_mode "matplotlib.text.Text.set_rotation_mode")
.

**grid\_color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

Gridline color.

**grid\_alpha**float

Transparency of gridlines: 0 (transparent) to 1 (opaque).

**grid\_linewidth**float

Width of gridlines in points.

**grid\_linestyle**str

Any valid [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 line style spec.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
.

Examples

ax.tick\_params(direction\='out', length\=6, width\=2, colors\='r',
               grid\_color\='r', grid\_alpha\=0.5)

This will make all major ticks be red, pointing out of the box, and with dimensions 6 points by 2 points. Tick labels will also be red. Gridlines will be red and translucent.

Examples using `matplotlib.pyplot.tick_params`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tick_params.html#examples-using-matplotlib-pyplot-tick-params "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_two_scales_thumb.png)

[Plots with different scales](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)

Plots with different scales

![](https://matplotlib.org/stable/_images/sphx_glr_ticklabels_rotation_thumb.png)

[Rotated tick labels](https://matplotlib.org/stable/gallery/ticks/ticklabels_rotation.html)

Rotated tick labels

On this page