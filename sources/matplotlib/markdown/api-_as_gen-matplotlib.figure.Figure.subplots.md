[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#main-content)

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
    

matplotlib.figure.Figure.subplots[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib-figure-figure-subplots "Link to this heading")

================================================================================================================================================================================

Figure.subplots(_nrows\=1_, _ncols\=1_, _\*_, _sharex\=False_, _sharey\=False_, _squeeze\=True_, _width\_ratios\=None_, _height\_ratios\=None_, _subplot\_kw\=None_, _gridspec\_kw\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L792-L928)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "Link to this definition")

Add a set of subplots to this figure.

This utility wrapper makes it convenient to create common layouts of subplots in a single call.

Parameters:

**nrows, ncols**int, default: 1

Number of rows/columns of the subplot grid.

**sharex, sharey**bool or {'none', 'all', 'row', 'col'}, default: False

Controls sharing of x-axis (_sharex_) or y-axis (_sharey_):

*   True or 'all': x- or y-axis will be shared among all subplots.
    
*   False or 'none': each subplot x- or y-axis will be independent.
    
*   'row': each subplot row will share an x- or y-axis.
    
*   'col': each subplot column will share an x- or y-axis.
    

When subplots have a shared x-axis along a column, only the x tick labels of the bottom subplot are created. Similarly, when subplots have a shared y-axis along a row, only the y tick labels of the first column subplot are created. To later turn other subplots' ticklabels on, use [`tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
.

When subplots have a shared axis that has units, calling [`Axis.set_units`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_units.html#matplotlib.axis.Axis.set_units "matplotlib.axis.Axis.set_units")
 will update each axis with the new units.

Note that it is not possible to unshare axes.

**squeeze**bool, default: True

*   If True, extra dimensions are squeezed out from the returned array of Axes:
    
    *   if only one subplot is constructed (nrows=ncols=1), the resulting single Axes object is returned as a scalar.
        
    *   for Nx1 or 1xM subplots, the returned object is a 1D numpy object array of Axes objects.
        
    *   for NxM, subplots with N>1 and M>1 are returned as a 2D array.
        
*   If False, no squeezing at all is done: the returned Axes object is always a 2D array containing Axes instances, even if it ends up being 1x1.
    

**width\_ratios**array-like of length _ncols_, optional

Defines the relative widths of the columns. Each column gets a relative width of `width_ratios[i] / sum(width_ratios)`. If not given, all columns will have the same width. Equivalent to `gridspec_kw={'width_ratios': [...]}`.

**height\_ratios**array-like of length _nrows_, optional

Defines the relative heights of the rows. Each row gets a relative height of `height_ratios[i] / sum(height_ratios)`. If not given, all rows will have the same height. Equivalent to `gridspec_kw={'height_ratios': [...]}`.

**subplot\_kw**dict, optional

Dict with keywords passed to the [`Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
 call used to create each subplot.

**gridspec\_kw**dict, optional

Dict with keywords passed to the [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 constructor used to create the grid the subplots are placed on.

Returns:

[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 or array of Axes

Either a single [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 object or an array of Axes objects if more than one subplot was created. The dimensions of the resulting array can be controlled with the _squeeze_ keyword, see above.

See also

[`pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")

[`Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")

[`pyplot.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")

Examples

\# First create some toy data:
x \= np.linspace(0, 2\*np.pi, 400)
y \= np.sin(x\*\*2)

\# Create a figure
fig \= plt.figure()

\# Create a subplot
ax \= fig.subplots()
ax.plot(x, y)
ax.set\_title('Simple plot')

\# Create two subplots and unpack the output array immediately
ax1, ax2 \= fig.subplots(1, 2, sharey\=True)
ax1.plot(x, y)
ax1.set\_title('Sharing Y axis')
ax2.scatter(x, y)

\# Create four polar Axes and access them through the returned array
axes \= fig.subplots(2, 2, subplot\_kw\=dict(projection\='polar'))
axes\[0, 0\].plot(x, y)
axes\[1, 1\].scatter(x, y)

\# Share an X-axis with each column of subplots
fig.subplots(2, 2, sharex\='col')

\# Share a Y-axis with each row of subplots
fig.subplots(2, 2, sharey\='row')

\# Share both X- and Y-axes with all subplots
fig.subplots(2, 2, sharex\='all', sharey\='all')

\# Note that this is the same as
fig.subplots(2, 2, sharex\=True, sharey\=True)

Examples using `matplotlib.figure.Figure.subplots`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#examples-using-matplotlib-figure-figure-subplots "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_histogram_cumulative_thumb.png)

[Cumulative distributions](https://matplotlib.org/stable/gallery/statistics/histogram_cumulative.html)

Cumulative distributions

![](https://matplotlib.org/stable/_images/sphx_glr_asinh_demo_thumb.png)

[Asinh scale](https://matplotlib.org/stable/gallery/scales/asinh_demo.html)

Asinh scale

![](https://matplotlib.org/stable/_images/sphx_glr_demo_text_rotation_mode_thumb.png)

[Text rotation mode](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_text_rotation_mode.html)

Text rotation mode

![](https://matplotlib.org/stable/_images/sphx_glr_rectangle_selector_thumb.png)

[Rectangle and ellipse selectors](https://matplotlib.org/stable/gallery/widgets/rectangle_selector.html)

Rectangle and ellipse selectors

![](https://matplotlib.org/stable/_images/sphx_glr_leftventricle_bullseye_thumb.png)

[Left ventricle bullseye](https://matplotlib.org/stable/gallery/specialty_plots/leftventricle_bullseye.html)

Left ventricle bullseye

![](https://matplotlib.org/stable/_images/sphx_glr_mosaic_thumb.png)

[Complex and semantic figure composition (subplot\_mosaic)](https://matplotlib.org/stable/users/explain/axes/mosaic.html)

Complex and semantic figure composition (subplot\_mosaic)

On this page