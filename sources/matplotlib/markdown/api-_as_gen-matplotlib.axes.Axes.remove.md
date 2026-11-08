[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.remove.html#main-content)

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
    

matplotlib.axes.Axes.remove[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.remove.html#matplotlib-axes-axes-remove "Link to this heading")

==============================================================================================================================================================

Axes.remove()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L235-L270)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.remove.html#matplotlib.axes.Axes.remove "Link to this definition")

Remove the artist from the figure if possible.

The effect will not be visible until the figure is redrawn, e.g., with [`FigureCanvasBase.draw_idle`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw_idle "matplotlib.backend_bases.FigureCanvasBase.draw_idle")
. Call [`relim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.relim.html#matplotlib.axes.Axes.relim "matplotlib.axes.Axes.relim")
 to update the Axes limits if desired.

Note: there is no support for removing the artist's legend entry.

Examples using `matplotlib.axes.Axes.remove`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.remove.html#examples-using-matplotlib-axes-axes-remove "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_and_subplots_thumb.png)

[Combine two subplots using subplots and GridSpec](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_and_subplots.html)

Combine two subplots using subplots and GridSpec

![](https://matplotlib.org/stable/_images/sphx_glr_subfigures_thumb.png)

[Figure subfigures](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html)

Figure subfigures

On this page