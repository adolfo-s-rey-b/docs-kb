[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.format_cursor_data.html#main-content)

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
    

matplotlib.axes.Axes.format\_cursor\_data[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.format_cursor_data.html#matplotlib-axes-axes-format-cursor-data "Link to this heading")

====================================================================================================================================================================================================

Axes.format\_cursor\_data(_data_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1413-L1443)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.format_cursor_data.html#matplotlib.axes.Axes.format_cursor_data "Link to this definition")

Return a string representation of _data_.

Note

This method is intended to be overridden by artist subclasses. As an end-user of Matplotlib you will most likely not call this method yourself.

The default implementation converts ints and floats and arrays of ints and floats into a comma-separated string enclosed in square brackets, unless the artist has an associated colorbar, in which case scalar values are formatted using the colorbar's formatter.

See also

[`get_cursor_data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_cursor_data.html#matplotlib.axes.Axes.get_cursor_data "matplotlib.axes.Axes.get_cursor_data")

On this page