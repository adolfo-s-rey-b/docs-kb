[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.add_gridspec.html#main-content)

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
    

matplotlib.figure.SubFigure.add\_gridspec[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.add_gridspec.html#matplotlib-figure-subfigure-add-gridspec "Link to this heading")

======================================================================================================================================================================================================

SubFigure.add\_gridspec(_nrows\=1_, _ncols\=1_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1564-L1609)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.add_gridspec.html#matplotlib.figure.SubFigure.add_gridspec "Link to this definition")

Low-level API for creating a [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 that has this figure as a parent.

This is a low-level API, allowing you to create a gridspec and subsequently add subplots based on the gridspec. Most users do not need that freedom and should use the higher-level methods [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
 or [`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
.

Parameters:

**nrows**int, default: 1

Number of rows in grid.

**ncols**int, default: 1

Number of columns in grid.

Returns:

[`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")

Other Parameters:

**\*\*kwargs**

Keyword arguments are passed to [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
.

See also

[`matplotlib.pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")

Examples

Adding a subplot that spans two rows:

fig \= plt.figure()
gs \= fig.add\_gridspec(2, 2)
ax1 \= fig.add\_subplot(gs\[0, 0\])
ax2 \= fig.add\_subplot(gs\[1, 0\])
\# spans two rows:
ax3 \= fig.add\_subplot(gs\[:, 1\])

On this page