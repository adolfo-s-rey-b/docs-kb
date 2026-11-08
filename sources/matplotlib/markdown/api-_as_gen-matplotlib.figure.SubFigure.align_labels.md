[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.align_labels.html#main-content)

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
    

matplotlib.figure.SubFigure.align\_labels[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.align_labels.html#matplotlib-figure-subfigure-align-labels "Link to this heading")

======================================================================================================================================================================================================

SubFigure.align\_labels(_axs\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1535-L1562)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.align_labels.html#matplotlib.figure.SubFigure.align_labels "Link to this definition")

Align the xlabels and ylabels of subplots with the same subplots row or column (respectively) if label alignment is being done automatically (i.e. the label position is not manually set).

Alignment persists for draw events after this is called.

Parameters:

**axs**list of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

Optional list (or [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
) of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 to align the labels. Default is to align all Axes on the figure.

See also

[`matplotlib.figure.Figure.align_xlabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_xlabels.html#matplotlib.figure.Figure.align_xlabels "matplotlib.figure.Figure.align_xlabels")

[`matplotlib.figure.Figure.align_ylabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_ylabels.html#matplotlib.figure.Figure.align_ylabels "matplotlib.figure.Figure.align_ylabels")

[`matplotlib.figure.Figure.align_titles`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_titles.html#matplotlib.figure.Figure.align_titles "matplotlib.figure.Figure.align_titles")

Notes

This assumes that all Axes in `axs` are from the same [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
, so that their [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
 positions correspond to figure positions.

On this page