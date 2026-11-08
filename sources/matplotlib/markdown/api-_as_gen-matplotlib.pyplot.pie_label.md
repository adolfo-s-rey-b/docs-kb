[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie_label.html#main-content)

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
    

matplotlib.pyplot.pie\_label[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie_label.html#matplotlib-pyplot-pie-label "Link to this heading")

===============================================================================================================================================================

matplotlib.pyplot.pie\_label(_container_, _/_, _labels_, _\*_, _distance\=0.6_, _textprops\=None_, _rotate\=False_, _alignment\='auto'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L4013-L4031)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie_label.html#matplotlib.pyplot.pie_label "Link to this definition")

Label a pie chart.

Added in version 3.11.

Adds labels to wedges in the given [`PieContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
.

Parameters:

**container**[`PieContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")

Container with all the wedges, likely returned from [`pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html#matplotlib.pyplot.pie "matplotlib.pyplot.pie")
.

**labels**str or list of str

A sequence of strings providing the labels for each wedge, or a format string with `absval` and/or `frac` placeholders. For example, to label each wedge with its value and the percentage in brackets:

labels\="{absval:d} ({frac:.0%})"

**distance**float, default: 0.6

The radial position of the labels, relative to the pie radius. Values > 1 are outside the wedge and values < 1 are inside the wedge.

**textprops**dict, default: None

Dict of arguments to pass to the [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 objects.

**rotate**bool, default: False

Rotate each label to the angle of the corresponding slice if true.

**alignment**{'center', 'outer', 'auto'}, default: 'auto'

Controls the horizontal alignment of the text objects relative to their nominal position.

*   'center': The labels are centered on their points.
    
*   'outer': Labels are aligned away from the center of the pie, i.e., labels on the left side of the pie are right-aligned and labels on the right side are left-aligned.
    
*   'auto': Translates to 'outer' if _distance_ > 1 (so that the labels do not overlap the wedges) and 'center' if _distance_ < 1.
    

If _rotate_ is True, the vertical alignment is also affected in an analogous way.

*   'center': The labels are centered on their points.
    
*   'outer': Labels are aligned away from the center of the pie, i.e., labels on the top half of the pie are bottom-aligned and labels on the bottom half are top-aligned.
    

Returns:

list

A list of the label [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 instances.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.pie_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie_label.html#matplotlib.axes.Axes.pie_label "matplotlib.axes.Axes.pie_label")
.

Examples using `matplotlib.pyplot.pie_label`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie_label.html#examples-using-matplotlib-pyplot-pie-label "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_pie_and_donut_labels_thumb.png)

[A pie and a donut with labels](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html)

A pie and a donut with labels

![](https://matplotlib.org/stable/_images/sphx_glr_pie_label_thumb.png)

[Labeling pie charts](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_label.html)

Labeling pie charts

On this page