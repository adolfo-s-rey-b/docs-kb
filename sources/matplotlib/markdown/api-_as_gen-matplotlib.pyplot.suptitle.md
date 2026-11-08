[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#main-content)

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
    

matplotlib.pyplot.suptitle[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib-pyplot-suptitle "Link to this heading")

===========================================================================================================================================================

matplotlib.pyplot.suptitle(_t_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L2978-L2980)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "Link to this definition")

Add a centered super title to the figure.

Parameters:

**t**str

The super title text.

**x**float, default: 0.5

The x location of the text in figure coordinates.

**y**float, default: 0.98

The y location of the text in figure coordinates.

**horizontalalignment, ha**{'center', 'left', 'right'}, default: center

The horizontal alignment of the text relative to (_x_, _y_).

**verticalalignment, va**{'top', 'center', 'bottom', 'baseline'}, default: top

The vertical alignment of the text relative to (_x_, _y_).

**fontsize, size**default: `[rcParams["figure.titlesize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.titlesize#rcparam-figure-titlesize) ` (default: `'large'`)

The font size of the text. See [`Text.set_size`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_size "matplotlib.text.Text.set_size")
 for possible values.

**fontweight, weight**default: `[rcParams["figure.titleweight"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.titleweight#rcparam-figure-titleweight) ` (default: `'normal'`)

The font weight of the text. See [`Text.set_weight`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_weight "matplotlib.text.Text.set_weight")
 for possible values.

Returns:

text

The [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 instance of the super title.

Other Parameters:

**fontproperties**None or dict, optional

A dict of font properties. If _fontproperties_ is given the default values for font size and weight are taken from the [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 defaults. `[rcParams["figure.titlesize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.titlesize#rcparam-figure-titlesize) ` (default: `'large'`) and `[rcParams["figure.titleweight"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.titleweight#rcparam-figure-titleweight) ` (default: `'normal'`) are ignored in this case.

**\*\*kwargs**

Additional kwargs are [`matplotlib.text.Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`Figure.suptitle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
.

Examples using `matplotlib.pyplot.suptitle`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#examples-using-matplotlib-pyplot-suptitle "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_nested_thumb.png)

[Nested Gridspecs](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_nested.html)

Nested Gridspecs

![](https://matplotlib.org/stable/_images/sphx_glr_pyplot_thumb.png)

[Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)

Pyplot tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_thumb.png)

[Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html)

Constrained layout guide

On this page