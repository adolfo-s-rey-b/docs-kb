[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_axes.html#main-content)

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
    

matplotlib.figure.Figure.get\_axes[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_axes.html#matplotlib-figure-figure-get-axes "Link to this heading")

=================================================================================================================================================================================

Figure.get\_axes()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L2813-L2825)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_axes.html#matplotlib.figure.Figure.get_axes "Link to this definition")

List of Axes in the Figure. You can access and modify the Axes in the Figure through this list.

Do not modify the list itself. Instead, use [`add_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
, [`add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
 or [`delaxes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.delaxes.html#matplotlib.figure.Figure.delaxes "matplotlib.figure.Figure.delaxes")
 to add or remove an Axes.

Note: The [`Figure.axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.axes.html#matplotlib.figure.Figure.axes "matplotlib.figure.Figure.axes")
 property and [`get_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_axes.html#matplotlib.figure.Figure.get_axes "matplotlib.figure.Figure.get_axes")
 method are equivalent.

Examples using `matplotlib.figure.Figure.get_axes`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_axes.html#examples-using-matplotlib-figure-figure-get-axes "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_subplots_demo_thumb.png)

[Create multiple subplots using plt.subplots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html)

Create multiple subplots using plt.subplots

![](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_thumb.png)

[Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html)

Arranging multiple Axes in a Figure

On this page