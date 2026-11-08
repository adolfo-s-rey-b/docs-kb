[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_current_fig_manager.html#main-content)

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
    

matplotlib.pyplot.get\_current\_fig\_manager[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_current_fig_manager.html#matplotlib-pyplot-get-current-fig-manager "Link to this heading")

===========================================================================================================================================================================================================

matplotlib.pyplot.get\_current\_fig\_manager()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L1217-L1231)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_current_fig_manager.html#matplotlib.pyplot.get_current_fig_manager "Link to this definition")

Return the figure manager of the current figure.

The figure manager is a container for the actual backend-depended window that displays the figure on screen.

If no current figure exists, a new one is created, and its figure manager is returned.

Returns:

[`FigureManagerBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase "matplotlib.backend_bases.FigureManagerBase")
 or backend-dependent subclass thereof

On this page