[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#main-content)

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
    

matplotlib.pyplot.title[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib-pyplot-title "Link to this heading")

==================================================================================================================================================

matplotlib.pyplot.title(_label_, _fontdict\=None_, _loc\=None_, _pad\=None_, _\*_, _y\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L4570-L4580)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "Link to this definition")

Set a title for the Axes.

Set one of the three available Axes titles. The available titles are positioned above the Axes in the center, flush with the left edge, and flush with the right edge.

Parameters:

**label**str

Text to use for the title

**fontdict**dict

Discouraged

The use of _fontdict_ is discouraged. Parameters should be passed as individual keyword arguments or using dictionary-unpacking `set_title(..., **fontdict)`.

A dictionary controlling the appearance of the title text, the default _fontdict_ is:

{'fontsize': rcParams\['axes.titlesize'\],
 'fontweight': rcParams\['axes.titleweight'\],
 'color': rcParams\['axes.titlecolor'\],
 'verticalalignment': 'baseline',
 'horizontalalignment': loc}

**loc**{'center', 'left', 'right'}, default: `[rcParams["axes.titlelocation"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.titlelocation#rcparam-axes-titlelocation) ` (default: `'center'`)

Which title to set.

**y**float, default: `[rcParams["axes.titley"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.titley#rcparam-axes-titley) ` (default: `None`)

Vertical Axes location for the title (1.0 is the top). If None (the default) and `[rcParams["axes.titley"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.titley#rcparam-axes-titley) ` (default: `None`) is also None, y is determined automatically to avoid decorators on the Axes.

**pad**float, default: `[rcParams["axes.titlepad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.titlepad#rcparam-axes-titlepad) ` (default: `6.0`)

The offset of the title from the top of the Axes, in points.

Returns:

[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

The matplotlib text instance representing the title

Other Parameters:

**\*\*kwargs**[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties

Other keyword arguments are text properties, see [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 for a list of valid text properties.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.set_title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
.

Examples using `matplotlib.pyplot.title`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#examples-using-matplotlib-pyplot-title "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_stairs_demo_thumb.png)

[Stairs Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stairs_demo.html)

Stairs Demo

![](https://matplotlib.org/stable/_images/sphx_glr_step_demo_thumb.png)

[Step Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/step_demo.html)

Step Demo

![](https://matplotlib.org/stable/_images/sphx_glr_masked_demo_thumb.png)

[Plotting masked and NaN values](https://matplotlib.org/stable/gallery/lines_bars_and_markers/masked_demo.html)

Plotting masked and NaN values

![](https://matplotlib.org/stable/_images/sphx_glr_subplot_thumb.png)

[Multiple subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot.html)

Multiple subplots

![](https://matplotlib.org/stable/_images/sphx_glr_geo_demo_thumb.png)

[Geographic Projections](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/geo_demo.html)

Geographic Projections

![](https://matplotlib.org/stable/_images/sphx_glr_custom_scale_thumb.png)

[Custom scale](https://matplotlib.org/stable/gallery/scales/custom_scale.html)

Custom scale

![](https://matplotlib.org/stable/_images/sphx_glr_text_fontdict_thumb.png)

[Controlling style of text and labels using a dictionary](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_fontdict.html)

Controlling style of text and labels using a dictionary

![](https://matplotlib.org/stable/_images/sphx_glr_titles_demo_thumb.png)

[Title positioning](https://matplotlib.org/stable/gallery/text_labels_and_annotations/titles_demo.html)

Title positioning

![](https://matplotlib.org/stable/_images/sphx_glr_plot_solarizedlight2_thumb.png)

[Solarized Light stylesheet](https://matplotlib.org/stable/gallery/style_sheets/plot_solarizedlight2.html)

Solarized Light stylesheet

![](https://matplotlib.org/stable/_images/sphx_glr_style_sheets_reference_thumb.png)

[Style sheets reference](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)

Style sheets reference

![](https://matplotlib.org/stable/_images/sphx_glr_pyplot_simple_thumb.png)

[Basic plot](https://matplotlib.org/stable/gallery/pyplots/pyplot_simple.html)

Basic plot

![](https://matplotlib.org/stable/_images/sphx_glr_pyplot_two_subplots_thumb.png)

[Two subplots using pyplot](https://matplotlib.org/stable/gallery/pyplots/pyplot_two_subplots.html)

Two subplots using pyplot

![](https://matplotlib.org/stable/_images/sphx_glr_ginput_manual_clabel_sgskip_thumb.png)

[Interactive functions](https://matplotlib.org/stable/gallery/event_handling/ginput_manual_clabel_sgskip.html)

Interactive functions

![](https://matplotlib.org/stable/_images/sphx_glr_svg_histogram_sgskip_thumb.svg)

[SVG Histogram](https://matplotlib.org/stable/gallery/user_interfaces/svg_histogram_sgskip.html)

SVG Histogram

![](https://matplotlib.org/stable/_images/sphx_glr_findobj_demo_thumb.png)

[Findobj Demo](https://matplotlib.org/stable/gallery/misc/findobj_demo.html)

Findobj Demo

![](https://matplotlib.org/stable/_images/sphx_glr_multipage_pdf_thumb.svg)

[Multipage PDF](https://matplotlib.org/stable/gallery/misc/multipage_pdf.html)

Multipage PDF

![](https://matplotlib.org/stable/_images/sphx_glr_set_and_get_thumb.png)

[Set and get properties](https://matplotlib.org/stable/gallery/misc/set_and_get.html)

Set and get properties

![](https://matplotlib.org/stable/_images/sphx_glr_table_demo_thumb.png)

[Table Demo](https://matplotlib.org/stable/gallery/misc/table_demo.html)

Table Demo

![](https://matplotlib.org/stable/_images/sphx_glr_zorder_demo_thumb.png)

[Zorder Demo](https://matplotlib.org/stable/gallery/misc/zorder_demo.html)

Zorder Demo

![](https://matplotlib.org/stable/_images/sphx_glr_sankey_basics_thumb.png)

[The Sankey class](https://matplotlib.org/stable/gallery/specialty_plots/sankey_basics.html)

The Sankey class

![](https://matplotlib.org/stable/_images/sphx_glr_pyplot_thumb.png)

[Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)

Pyplot tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_quick_start_thumb.png)

[Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)

Quick start guide

On this page