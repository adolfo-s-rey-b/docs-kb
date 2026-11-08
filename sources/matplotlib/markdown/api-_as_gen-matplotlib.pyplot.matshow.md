[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.matshow.html#main-content)

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
    

matplotlib.pyplot.matshow[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.matshow.html#matplotlib-pyplot-matshow "Link to this heading")

========================================================================================================================================================

matplotlib.pyplot.matshow(_A_, _fignum\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L2773-L2831)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.matshow.html#matplotlib.pyplot.matshow "Link to this definition")

Display a 2D array as a matrix in a new figure window.

The origin is set at the upper left hand corner. The indexing is `(row, column)` so that the first index runs vertically and the second index runs horizontally in the figure:

A\[0, 0\]   ⋯ A\[0, M-1\]
   ⋮             ⋮
A\[N-1, 0\] ⋯ A\[N-1, M-1\]

The aspect ratio of the figure window is that of the array, unless this would make an excessively short or narrow figure.

Tick labels for the xaxis are placed on top.

Parameters:

**A**2D array-like

The matrix to be displayed.

**fignum**None or int

If _None_, create a new, appropriately sized figure window.

If 0, use the current Axes (creating one if there is none, without ever adjusting the figure size).

Otherwise, create a new Axes on the figure with the given number (creating it at the appropriate size if it does not exist, but not adjusting the figure size otherwise). Note that this will be drawn on top of any preexisting Axes on the figure.

Returns:

[`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")

Other Parameters:

**\*\*kwargs**[`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 arguments

Examples using `matplotlib.pyplot.matshow`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.matshow.html#examples-using-matplotlib-pyplot-matshow "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_matshow_thumb.png)

[Visualize matrices with matshow](https://matplotlib.org/stable/gallery/images_contours_and_fields/matshow.html)

Visualize matrices with matshow

On this page