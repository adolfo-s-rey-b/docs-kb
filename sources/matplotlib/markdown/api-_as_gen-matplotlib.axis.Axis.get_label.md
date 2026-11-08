[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_label.html#main-content)

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
    

matplotlib.axis.Axis.get\_label[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_label.html#matplotlib-axis-axis-get-label "Link to this heading")

========================================================================================================================================================================

Axis.get\_label()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L1517-L1526)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_label.html#matplotlib.axis.Axis.get_label "Link to this definition")

\[_Discouraged_\] Return the axis label as a Text instance.

Discouraged

This overrides [`Artist.get_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_label.html#matplotlib.artist.Artist.get_label "matplotlib.artist.Artist.get_label")
, which is for legend labels, with a new semantic. It is recommended to use the attribute `Axis.label` instead.

On this page