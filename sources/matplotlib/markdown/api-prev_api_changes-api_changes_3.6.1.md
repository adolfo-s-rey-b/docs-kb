[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.1.html#main-content)

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
    

API Changes for 3.6.1[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.1.html#api-changes-for-3-6-1 "Link to this heading")

=================================================================================================================================================

Deprecations[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.1.html#deprecations "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

### Colorbars for orphaned mappables are deprecated, but no longer raise[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.6.1.html#colorbars-for-orphaned-mappables-are-deprecated-but-no-longer-raise "Link to this heading")

Before 3.6.0, Colorbars for mappables that do not have a parent Axes would steal space from the current Axes. 3.6.0 raised an error on this, but without a deprecation cycle. For 3.6.1 this is reverted; the current Axes is used, but a deprecation warning is shown instead. In this undetermined case, users and libraries should explicitly specify what Axes they want space to be stolen from: `fig.colorbar(mappable, ax=plt.gca())`.

On this page