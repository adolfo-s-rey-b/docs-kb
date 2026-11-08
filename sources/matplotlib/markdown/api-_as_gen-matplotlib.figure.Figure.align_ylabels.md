[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_ylabels.html#main-content)

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
    

matplotlib.figure.Figure.align\_ylabels[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_ylabels.html#matplotlib-figure-figure-align-ylabels "Link to this heading")

================================================================================================================================================================================================

Figure.align\_ylabels(_axs\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1427-L1486)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_ylabels.html#matplotlib.figure.Figure.align_ylabels "Link to this definition")

Align the ylabels of subplots in the same subplot column if label alignment is being done automatically (i.e. the label position is not manually set).

Alignment persists for draw events after this is called.

If a label is on the left, it is aligned with labels on Axes that also have their label on the left and that have the same left-most subplot column. If the label is on the right, it is aligned with labels on Axes with the same right-most column.

Parameters:

**axs**list of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

Optional list (or [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
) of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 to align the ylabels. Default is to align all Axes on the figure.

See also

[`matplotlib.figure.Figure.align_xlabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_xlabels.html#matplotlib.figure.Figure.align_xlabels "matplotlib.figure.Figure.align_xlabels")

[`matplotlib.figure.Figure.align_titles`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_titles.html#matplotlib.figure.Figure.align_titles "matplotlib.figure.Figure.align_titles")

[`matplotlib.figure.Figure.align_labels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_labels.html#matplotlib.figure.Figure.align_labels "matplotlib.figure.Figure.align_labels")

Notes

This assumes that all Axes in `axs` are from the same [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
, so that their [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
 positions correspond to figure positions.

Examples

Example with large yticks labels:

fig, axs \= plt.subplots(2, 1)
axs\[0\].plot(np.arange(0, 1000, 50))
axs\[0\].set\_ylabel('YLabel 0')
axs\[1\].set\_ylabel('YLabel 1')
fig.align\_ylabels()

Examples using `matplotlib.figure.Figure.align_ylabels`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_ylabels.html#examples-using-matplotlib-figure-figure-align-ylabels "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_align_labels_demo_thumb.png)

[Align labels and titles](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/align_labels_demo.html)

Align labels and titles

On this page