[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#main-content)

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
    

matplotlib.pyplot.subplot2grid[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib-pyplot-subplot2grid "Link to this heading")

=======================================================================================================================================================================

matplotlib.pyplot.subplot2grid(_shape_, _loc_, _rowspan\=1_, _colspan\=1_, _fig\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L2074-L2123)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid "Link to this definition")

Create a subplot at a specific location inside a regular grid.

Parameters:

**shape**(int, int)

Number of rows and of columns of the grid in which to place axis.

**loc**(int, int)

Row number and column number of the axis location within the grid.

**rowspan**int, default: 1

Number of rows for the axis to span downwards.

**colspan**int, default: 1

Number of columns for the axis to span to the right.

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, optional

Figure to place the subplot in. Defaults to the current figure.

**\*\*kwargs**

Additional keyword arguments are handed to [`add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
.

Returns:

[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The Axes of the subplot. The returned Axes can actually be an instance of a subclass, such as [`projections.polar.PolarAxes`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes "matplotlib.projections.polar.PolarAxes")
 for polar projections.

Notes

The following call

ax \= subplot2grid((nrows, ncols), (row, col), rowspan, colspan)

is identical to

fig \= gcf()
gs \= fig.add\_gridspec(nrows, ncols)
ax \= fig.add\_subplot(gs\[row:row+rowspan, col:col+colspan\])

Examples using `matplotlib.pyplot.subplot2grid`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#examples-using-matplotlib-pyplot-subplot2grid "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_subplot2grid_thumb.png)

[subplot2grid](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot2grid.html)

subplot2grid

![](https://matplotlib.org/stable/_images/sphx_glr_demo_tight_layout_thumb.png)

[Resize Axes with tight layout](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_tight_layout.html)

Resize Axes with tight layout

![](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_thumb.png)

[Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html)

Arranging multiple Axes in a Figure

![](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_thumb.png)

[Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html)

Constrained layout guide

![](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_thumb.png)

[Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html)

Tight layout guide

On this page