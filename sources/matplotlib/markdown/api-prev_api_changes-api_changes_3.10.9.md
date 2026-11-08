[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.9.html#main-content)

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
    

API Changes for 3.10.9[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.9.html#api-changes-for-3-10-9 "Link to this heading")

====================================================================================================================================================

Deprecations[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.9.html#deprecations "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

### Arbitrary code in `axes.prop_cycle` rcParam strings[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.9.html#arbitrary-code-in-axes-prop-cycle-rcparam-strings "Link to this heading")

The `axes.prop_cycle` rcParam accepts Python expressions that are evaluated in a limited context. The evaluation context has been further limited and some expressions that previously worked (list comprehensions, for example) no longer will. This change is made without a deprecation period to improve security. The previously documented cycler operations at [https://matplotlib.org/cycler/](https://matplotlib.org/cycler/)
 are still supported.

This change was originally slated for v3.11.0 of Matplotlib, but was additionally backported due to the security implications.

On this page