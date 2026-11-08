[Skip to main content](https://matplotlib.org/stable/api/gridspec_api.html#main-content)

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
    

`matplotlib.gridspec`[#](https://matplotlib.org/stable/api/gridspec_api.html#module-matplotlib.gridspec "Link to this heading")

================================================================================================================================

[`gridspec`](https://matplotlib.org/stable/api/gridspec_api.html#module-matplotlib.gridspec "matplotlib.gridspec")
 contains classes that help to layout multiple [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in a grid-like pattern within a figure.

The [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 specifies the overall grid structure. Individual cells within the grid are referenced by [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
s.

Often, users need not access this module directly, and can use higher-level methods like [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
, [`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
 and [`subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
. See the tutorial [Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#arranging-axes)
 for a guide.

Classes[#](https://matplotlib.org/stable/api/gridspec_api.html#classes "Link to this heading")

-----------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")<br>(nrows, ncols\[, figure, left, ...\]) | A grid layout to place subplots within a figure. |
| [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")<br>(gridspec, num1\[, num2\]) | The location of a subplot in a [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")<br>. |
| [`GridSpecBase`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#matplotlib.gridspec.GridSpecBase "matplotlib.gridspec.GridSpecBase")<br>(nrows, ncols\[, height\_ratios, ...\]) | A base class of GridSpec that specifies the geometry of the grid that a subplot will be placed. |
| [`GridSpecFromSubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")<br>(nrows, ncols, ...\[, ...\]) | GridSpec whose subplot layout parameters are inherited from the location specified by a given SubplotSpec. |
| [`SubplotParams`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotParams.html#matplotlib.gridspec.SubplotParams "matplotlib.gridspec.SubplotParams")<br>(\[left, bottom, right, top, ...\]) | Parameters defining the positioning of a subplots grid in a figure. |

On this page