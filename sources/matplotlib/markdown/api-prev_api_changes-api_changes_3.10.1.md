[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.1.html#main-content)

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
    

API Changes for 3.10.1[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.1.html#api-changes-for-3-10-1 "Link to this heading")

====================================================================================================================================================

Behaviour[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.1.html#behaviour "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

### _alpha_ parameter handling on images[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.1.html#alpha-parameter-handling-on-images "Link to this heading")

When passing and array to `imshow(..., alpha=...)`, the parameter was silently ignored if the image data was an RGB or RBGA image or if `[rcParams["image.interpolation_stage"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.interpolation_stage#rcparam-image-interpolation-stage) ` (default: `'auto'`) resolved to "rbga".

This is now fixed, and the alpha array overwrites any previous transparency information.

On this page