[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.3.html#main-content)

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
    

API Changes for 3.5.3[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.3.html#api-changes-for-3-5-3 "Link to this heading")

=================================================================================================================================================

[Passing _linefmt_ positionally is undeprecated](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.3.html#id1)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.3.html#passing-linefmt-positionally-is-undeprecated "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Positional use of all formatting parameters in [`stem`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stem.html#matplotlib.axes.Axes.stem "matplotlib.axes.Axes.stem")
 has been deprecated since Matplotlib 3.5. This deprecation is relaxed so that one can still pass _linefmt_ positionally, i.e. `stem(x, y, 'r')`.

On this page