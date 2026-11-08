[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.suptitle.html#main-content)

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
    

matplotlib.figure.SubFigure.suptitle[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.suptitle.html#matplotlib-figure-subfigure-suptitle "Link to this heading")

=========================================================================================================================================================================================

SubFigure.suptitle(_t_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L390-L398)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.suptitle.html#matplotlib.figure.SubFigure.suptitle "Link to this definition")

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

Examples using `matplotlib.figure.SubFigure.suptitle`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.suptitle.html#examples-using-matplotlib-figure-subfigure-suptitle "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_subfigures_thumb.png)

[Figure subfigures](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html)

Figure subfigures

![](https://matplotlib.org/stable/_images/sphx_glr_tick-formatters_thumb.png)

[Tick formatters](https://matplotlib.org/stable/gallery/ticks/tick-formatters.html)

Tick formatters

![](https://matplotlib.org/stable/_images/sphx_glr_petroff10_thumb.png)

[Petroff style sheets](https://matplotlib.org/stable/gallery/style_sheets/petroff10.html)

Petroff style sheets

![](https://matplotlib.org/stable/_images/sphx_glr_axes_ticks_thumb.png)

[Axis ticks](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html)

Axis ticks

On this page