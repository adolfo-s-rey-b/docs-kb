[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.2.html#main-content)

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
    

API Changes for 3.5.2[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.2.html#api-changes-for-3-5-2 "Link to this heading")

=================================================================================================================================================

[QuadMesh mouseover defaults to False](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.2.html#id1)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.2.html#quadmesh-mouseover-defaults-to-false "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

New in 3.5, [`QuadMesh.get_cursor_data`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh.get_cursor_data "matplotlib.collections.QuadMesh.get_cursor_data")
 allows display of data values under the cursor. However, this can be very slow for large meshes, so by `.QuadMesh.set_mouseover` defaults to _False_.

On this page