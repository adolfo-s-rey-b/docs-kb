[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.1.html#main-content)

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
    

API Changes for 3.9.1[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.1.html#api-changes-for-3-9-1 "Link to this heading")

=================================================================================================================================================

Development[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.1.html#development "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

### Documentation-specific custom Sphinx roles are now semi-public[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.9.1.html#documentation-specific-custom-sphinx-roles-are-now-semi-public "Link to this heading")

For third-party packages that derive types from Matplotlib, our use of custom roles may prevent Sphinx from building their docs. These custom Sphinx roles are now public solely for the purposes of use within projects that derive from Matplotlib types. See [`matplotlib.sphinxext.roles`](https://matplotlib.org/stable/api/sphinxext_roles.html#module-matplotlib.sphinxext.roles "matplotlib.sphinxext.roles")
 for details.

On this page