[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#main-content)

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
    

matplotlib.pyplot.xlabel[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib-pyplot-xlabel "Link to this heading")

=====================================================================================================================================================

matplotlib.pyplot.xlabel(_xlabel_, _fontdict\=None_, _labelpad\=None_, _\*_, _loc\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L4584-L4595)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "Link to this definition")

Set the label for the x-axis.

Parameters:

**xlabel**str

The label text.

**labelpad**float, default: `[rcParams["axes.labelpad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.labelpad#rcparam-axes-labelpad) ` (default: `4.0`)

Spacing in points from the Axes bounding box including ticks and tick labels. If None, the previous value is left as is.

**loc**{'left', 'center', 'right'}, default: `[rcParams["xaxis.labellocation"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xaxis.labellocation#rcparam-xaxis-labellocation) ` (default: `'center'`)

The label position. This is a high-level alternative for passing parameters _x_ and _horizontalalignment_.

Other Parameters:

**\*\*kwargs**[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties

[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties control the appearance of the label.

See also

[`text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")

Documents the properties supported by [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.set_xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
.

Examples using `matplotlib.pyplot.xlabel`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#examples-using-matplotlib-pyplot-xlabel "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_subplot_thumb.png)

[Multiple subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot.html)

Multiple subplots

![](https://matplotlib.org/stable/_images/sphx_glr_custom_scale_thumb.png)

[Custom scale](https://matplotlib.org/stable/gallery/scales/custom_scale.html)

Custom scale

![](https://matplotlib.org/stable/_images/sphx_glr_text_fontdict_thumb.png)

[Controlling style of text and labels using a dictionary](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_fontdict.html)

Controlling style of text and labels using a dictionary

![](https://matplotlib.org/stable/_images/sphx_glr_plot_solarizedlight2_thumb.png)

[Solarized Light stylesheet](https://matplotlib.org/stable/gallery/style_sheets/plot_solarizedlight2.html)

Solarized Light stylesheet

![](https://matplotlib.org/stable/_images/sphx_glr_pyplot_simple_thumb.png)

[Basic plot](https://matplotlib.org/stable/gallery/pyplots/pyplot_simple.html)

Basic plot

![](https://matplotlib.org/stable/_images/sphx_glr_findobj_demo_thumb.png)

[Findobj Demo](https://matplotlib.org/stable/gallery/misc/findobj_demo.html)

Findobj Demo

![](https://matplotlib.org/stable/_images/sphx_glr_pyplot_thumb.png)

[Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)

Pyplot tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_quick_start_thumb.png)

[Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)

Quick start guide

On this page