[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.2.html#main-content)

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
    

API Changes in 1.5.2[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.2.html#api-changes-in-1-5-2 "Link to this heading")

===============================================================================================================================================

Default Behavior Changes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.2.html#default-behavior-changes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

### Changed default `autorange` behavior in boxplots[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_1.5.2.html#changed-default-autorange-behavior-in-boxplots "Link to this heading")

Prior to v1.5.2, the whiskers of boxplots would extend to the minimum and maximum values if the quartiles were all equal (i.e., Q1 = median = Q3). This behavior has been disabled by default to restore consistency with other plotting packages.

To restore the old behavior, simply set `autorange=True` when calling `plt.boxplot`.

On this page