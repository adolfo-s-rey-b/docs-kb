[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.91.2.html#main-content)

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
    

Changes for 0.91.2[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.91.2.html#changes-for-0-91-2 "Link to this heading")

============================================================================================================================================

*   For `csv2rec`, checkrows=0 is the new default indicating all rows will be checked for type inference
    
*   A warning is issued when an image is drawn on log-scaled axes, since it will not log-scale the image data.
    
*   Moved `rec2gtk` to `matplotlib.toolkits.gtktools`
    
*   Moved `rec2excel` to `matplotlib.toolkits.exceltools`
    
*   Removed, dead/experimental ExampleInfo, Namespace and Importer code from [`matplotlib`](https://matplotlib.org/stable/index.html#module-matplotlib "matplotlib")