[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label_text.html#main-content)

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
    

matplotlib.axis.Axis.set\_label\_text[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label_text.html#matplotlib-axis-axis-set-label-text "Link to this heading")

========================================================================================================================================================================================

Axis.set\_label\_text(_label_, _fontdict\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L2026-L2052)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_label_text.html#matplotlib.axis.Axis.set_label_text "Link to this definition")

Set the text value of the axis label.

Parameters:

**label**str

Text string.

**fontdict**dict

Text properties.

Discouraged

The use of _fontdict_ is discouraged. Parameters should be passed as individual keyword arguments or using dictionary-unpacking `set_label_text(..., **fontdict)`.

**\*\*kwargs**

Merged into fontdict.

On this page