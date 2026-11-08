[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#main-content)

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
    

matplotlib.pyplot.subplots\_adjust[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib-pyplot-subplots-adjust "Link to this heading")

=================================================================================================================================================================================

matplotlib.pyplot.subplots\_adjust(_left\=None_, _bottom\=None_, _right\=None_, _top\=None_, _wspace\=None_, _hspace\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L2963-L2974)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "Link to this definition")

Adjust the subplot layout parameters.

Unset parameters are left unmodified; initial values are given by `[rcParams["figure.subplot.[name]"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.subplot.[name]#rcparam-figure-subplot-left) `.

([`Source code`](https://matplotlib.org/stable/_downloads/01c30d8647018decc739b3ad375ac00c/figure_subplots_adjust.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/07ae48f7411dfab5beadc024d3832c50/figure_subplots_adjust.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/362a080aae6b1dfd85262cfa1d98085f/figure_subplots_adjust.png)
)

[![](https://matplotlib.org/stable/_images/api-_as_gen-figure_subplots_adjust.2x.png)](https://matplotlib.org/stable/_images/api-_as_gen-figure_subplots_adjust.2x.png)

Parameters:

**left**float, optional

The position of the left edge of the subplots, as a fraction of the figure width.

**right**float, optional

The position of the right edge of the subplots, as a fraction of the figure width.

**bottom**float, optional

The position of the bottom edge of the subplots, as a fraction of the figure height.

**top**float, optional

The position of the top edge of the subplots, as a fraction of the figure height.

**wspace**float, optional

The width of the padding between subplots, as a fraction of the average Axes width.

**hspace**float, optional

The height of the padding between subplots, as a fraction of the average Axes height.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`Figure.subplots_adjust`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
.

Examples using `matplotlib.pyplot.subplots_adjust`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#examples-using-matplotlib-pyplot-subplots-adjust "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_irregulardatagrid_thumb.png)

[Contour plot of irregularly spaced data](https://matplotlib.org/stable/gallery/images_contours_and_fields/irregulardatagrid.html)

Contour plot of irregularly spaced data

![](https://matplotlib.org/stable/_images/sphx_glr_customized_violin_thumb.png)

[Violin plot customization](https://matplotlib.org/stable/gallery/statistics/customized_violin.html)

Violin plot customization

![](https://matplotlib.org/stable/_images/sphx_glr_subplots_adjust_thumb.png)

[Subplots spacings and margins](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_adjust.html)

Subplots spacings and margins

![](https://matplotlib.org/stable/_images/sphx_glr_text_fontdict_thumb.png)

[Controlling style of text and labels using a dictionary](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_fontdict.html)

Controlling style of text and labels using a dictionary

![](https://matplotlib.org/stable/_images/sphx_glr_demo_parasite_axes2_thumb.png)

[Parasite axis demo](https://matplotlib.org/stable/gallery/axisartist/demo_parasite_axes2.html)

Parasite axis demo

![](https://matplotlib.org/stable/_images/sphx_glr_table_demo_thumb.png)

[Table Demo](https://matplotlib.org/stable/gallery/misc/table_demo.html)

Table Demo

![](https://matplotlib.org/stable/_images/sphx_glr_pyplot_thumb.png)

[Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)

Pyplot tutorial

On this page