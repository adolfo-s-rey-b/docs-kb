[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.1.html#main-content)

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
    

API Changes for 3.0.1[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.0.1.html#api-changes-for-3-0-1 "Link to this heading")

=================================================================================================================================================

`matplotlib.tight_layout.auto_adjust_subplotpars` can return `None` now if the new subplotparams will collapse axes to zero width or height. This prevents `tight_layout` from being executed. Similarly `matplotlib.tight_layout.get_tight_layout_figure` will return None.

To improve import (startup) time, private modules are now imported lazily. These modules are no longer available at these locations:

*   `matplotlib.backends.backend_agg._png`
    
*   `matplotlib.contour._contour`
    
*   `matplotlib.image._png`
    
*   `matplotlib.mathtext._png`
    
*   `matplotlib.testing.compare._png`
    
*   `matplotlib.texmanager._png`
    
*   `matplotlib.tri.triangulation._tri`
    
*   `matplotlib.tri.triangulation._qhull`
    
*   `matplotlib.tri.tricontour._tri`
    
*   `matplotlib.tri.trifinder._tri`