[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.2.html#main-content)

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
    

API Changes for 3.9.2[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.2.html#api-changes-for-3-9-2 "Link to this heading")

=================================================================================================================================================

Development[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.2.html#development "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

### Windows wheel runtime bundling made static[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.2.html#windows-wheel-runtime-bundling-made-static "Link to this heading")

In 3.7.0, the MSVC runtime DLL was bundled in wheels to enable importing Matplotlib on systems that do not have it installed. However, this could cause inconsistencies with other wheels that did the same, and trigger random crashes depending on import order. See [this issue](https://github.com/matplotlib/matplotlib/issues/28551)
 for further details.

Since 3.9.2, wheels now bundle the MSVC runtime DLL statically to avoid such issues.

On this page