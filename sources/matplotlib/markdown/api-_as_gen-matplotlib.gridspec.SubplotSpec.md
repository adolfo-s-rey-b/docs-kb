[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#main-content)

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
    

matplotlib.gridspec.SubplotSpec[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib-gridspec-subplotspec "Link to this heading")

==========================================================================================================================================================================

class matplotlib.gridspec.SubplotSpec(_gridspec_, _num1_, _num2\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L531-L738)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

The location of a subplot in a [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
.

Note

Likely, you will never instantiate a [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
 yourself. Instead, you will typically obtain one from a [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 using item-access.

Parameters:

**gridspec**[`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")

The GridSpec, which the subplot is referencing.

**num1, num2**int

The subplot will occupy the _num1_\-th cell of the given _gridspec_. If _num2_ is provided, the subplot will span between _num1_\-th cell and _num2_\-th cell **inclusive**.

The index starts from 0.

property colspan[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec.colspan "Link to this definition")

The columns spanned by this subplot, as a [`range`](https://docs.python.org/3/library/stdtypes.html#range "(in Python v3.14)")
 object.

get\_geometry()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L620-L629)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec.get_geometry "Link to this definition")

Return the subplot geometry as tuple `(n_rows, n_cols, start, stop)`.

The indices _start_ and _stop_ define the range of the subplot within the [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
. _stop_ is inclusive (i.e. for a single cell `start == stop`).

get\_gridspec()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L617-L618)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec.get_gridspec "Link to this definition")

get\_position(_figure_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L658-L672)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec.get_position "Link to this definition")

Update the subplot position from `figure.subplotpars`.

get\_topmost\_subplotspec()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L674-L682)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec.get_topmost_subplotspec "Link to this definition")

Return the topmost [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
 instance associated with the subplot.

is\_first\_col()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L652-L653)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec.is_first_col "Link to this definition")

is\_first\_row()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L646-L647)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec.is_first_row "Link to this definition")

is\_last\_col()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L655-L656)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec.is_last_col "Link to this definition")

is\_last\_row()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L649-L650)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec.is_last_row "Link to this definition")

property num2[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec.num2 "Link to this definition")

property rowspan[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec.rowspan "Link to this definition")

The rows spanned by this subplot, as a [`range`](https://docs.python.org/3/library/stdtypes.html#range "(in Python v3.14)")
 object.

subgridspec(_nrows_, _ncols_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L698-L738)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec.subgridspec "Link to this definition")

Create a GridSpec within this subplot.

The created [`GridSpecFromSubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
 will have this [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
 as a parent.

Parameters:

**nrows**int

Number of rows in grid.

**ncols**int

Number of columns in grid.

Returns:

[`GridSpecFromSubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")

Other Parameters:

**\*\*kwargs**

All other parameters are passed to [`GridSpecFromSubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
.

See also

[`matplotlib.pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")

Examples

Adding three subplots in the space occupied by a single subplot:

fig \= plt.figure()
gs0 \= fig.add\_gridspec(3, 1)
ax1 \= fig.add\_subplot(gs0\[0\])
ax2 \= fig.add\_subplot(gs0\[1\])
gssub \= gs0\[2\].subgridspec(1, 3)
for i in range(3):
    fig.add\_subplot(gssub\[0, i\])

Examples using `matplotlib.gridspec.SubplotSpec`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#examples-using-matplotlib-gridspec-subplotspec "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_thumb.png)

[Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html)

Arranging multiple Axes in a Figure

![](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_thumb.png)

[Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html)

Constrained layout guide

On this page