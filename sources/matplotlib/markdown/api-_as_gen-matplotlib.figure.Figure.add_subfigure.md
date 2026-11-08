[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subfigure.html#main-content)

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
    

matplotlib.figure.Figure.add\_subfigure[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subfigure.html#matplotlib-figure-figure-add-subfigure "Link to this heading")

================================================================================================================================================================================================

Figure.add\_subfigure(_subplotspec_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1680-L1708)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subfigure.html#matplotlib.figure.Figure.add_subfigure "Link to this definition")

Add a [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
 to the figure as part of a subplot arrangement.

Parameters:

**subplotspec**[`gridspec.SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")

Defines the region in a parent gridspec where the subfigure will be placed.

Returns:

[`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")

Other Parameters:

**\*\*kwargs**

Are passed to the [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
 object.

See also

[`Figure.subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")

Examples using `matplotlib.figure.Figure.add_subfigure`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subfigure.html#examples-using-matplotlib-figure-figure-add-subfigure "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_subfigures_thumb.png)

[Figure subfigures](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html)

Figure subfigures

On this page