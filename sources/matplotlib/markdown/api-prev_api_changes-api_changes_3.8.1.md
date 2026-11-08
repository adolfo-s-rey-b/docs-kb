[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.1.html#main-content)

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
    

API Changes for 3.8.1[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.1.html#api-changes-for-3-8-1 "Link to this heading")

=================================================================================================================================================

Behaviour[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.1.html#behaviour "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

### Default behaviour of `hexbin` with _C_ provided requires at least 1 point[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.1.html#default-behaviour-of-hexbin-with-c-provided-requires-at-least-1-point "Link to this heading")

The behaviour changed in 3.8.0 to be inclusive of _mincnt_. However, that resulted in errors or warnings with some reduction functions, so now the default is to require at least 1 point to call the reduction function. This effectively restores the default behaviour to match that of Matplotlib 3.7 and before.

Deprecations[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.1.html#deprecations "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

### Deprecations removed in `contour`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.1.html#deprecations-removed-in-contour "Link to this heading")

`contour.allsegs`, `contour.allkinds`, and `contour.find_nearest_contour` are no longer marked for deprecation.

Development[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.1.html#development "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

### Minimum version of setuptools bumped to 64[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.8.1.html#minimum-version-of-setuptools-bumped-to-64 "Link to this heading")

To comply with requirements of `setuptools_scm`, the minimum version of `setuptools` has been increased from 42 to 64.

On this page