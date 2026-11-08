[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.align_titles.html#main-content)

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
    

matplotlib.figure.SubFigure.align\_titles[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.align_titles.html#matplotlib-figure-subfigure-align-titles "Link to this heading")

======================================================================================================================================================================================================

SubFigure.align\_titles(_axs\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1488-L1533)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.align_titles.html#matplotlib.figure.SubFigure.align_titles "Link to this definition")

Align the titles of subplots in the same subplot row if title alignment is being done automatically (i.e. the title position is not manually set).

Alignment persists for draw events after this is called.

Parameters:

**axs**list of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

Optional list of (or ndarray) [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 to align the titles. Default is to align all Axes on the figure.

See also

[`matplotlib.figure.Figure.align_xlabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_xlabels.html#matplotlib.figure.Figure.align_xlabels "matplotlib.figure.Figure.align_xlabels")

[`matplotlib.figure.Figure.align_ylabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_ylabels.html#matplotlib.figure.Figure.align_ylabels "matplotlib.figure.Figure.align_ylabels")

[`matplotlib.figure.Figure.align_labels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_labels.html#matplotlib.figure.Figure.align_labels "matplotlib.figure.Figure.align_labels")

Notes

This assumes that all Axes in `axs` are from the same [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
, so that their [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
 positions correspond to figure positions.

Examples

Example with titles:

fig, axs \= plt.subplots(1, 2)
axs\[0\].set\_aspect('equal')
axs\[0\].set\_title('Title 0')
axs\[1\].set\_title('Title 1')
fig.align\_titles()

On this page