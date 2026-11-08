[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.gca.html#main-content)

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
    

matplotlib.figure.Figure.gca[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.gca.html#matplotlib-figure-figure-gca "Link to this heading")

=================================================================================================================================================================

Figure.gca()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1716-L1727)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.gca.html#matplotlib.figure.Figure.gca "Link to this definition")

Get the current Axes.

If there is currently no Axes on this Figure, a new one is created using [`Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
. (To test whether there is currently an Axes on a Figure, check whether `figure.axes` is empty. To test whether there is currently a Figure on the pyplot figure stack, check whether [`pyplot.get_fignums()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_fignums.html#matplotlib.pyplot.get_fignums "matplotlib.pyplot.get_fignums")
 is empty.)

On this page