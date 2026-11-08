[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.matshow.html#main-content)

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
    

matplotlib.axes.Axes.matshow[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.matshow.html#matplotlib-axes-axes-matshow "Link to this heading")

=================================================================================================================================================================

Axes.matshow(_Z_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L8812-L8861)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.matshow.html#matplotlib.axes.Axes.matshow "Link to this definition")

Plot the values of a 2D matrix or array as color-coded image.

The matrix will be shown the way it would be printed, with the first row at the top. Row and column numbering is zero-based.

Parameters:

**Z**(M, N) array-like

The matrix to be displayed.

Returns:

[`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")

Other Parameters:

**\*\*kwargs**[`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 arguments

See also

[`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")

More general function to plot data on a 2D regular raster.

Notes

This is just a convenience function wrapping [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 to set useful defaults for displaying a matrix. In particular:

*   Set `origin='upper'`.
    
*   Set `interpolation='nearest'`.
    
*   Set `aspect='equal'`.
    
*   Ticks are placed to the left and above.
    
*   Ticks are formatted to show integer indices.
    

On this page