[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.1.1.html#main-content)

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
    

API Changes for 3.1.1[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.1.1.html#api-changes-for-3-1-1 "Link to this heading")

=================================================================================================================================================

[Behavior changes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.1.1.html#id1)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.1.1.html#behavior-changes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Locator.nonsingular return order[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.1.1.html#locator-nonsingular-return-order "Link to this heading")

[`Locator.nonsingular`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator.nonsingular "matplotlib.ticker.Locator.nonsingular")
 (introduced in mpl 3.1) now returns a range `v0, v1` with `v0 <= v1`. This behavior is consistent with the implementation of `nonsingular` by the [`LogLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator "matplotlib.ticker.LogLocator")
 and [`LogitLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogitLocator "matplotlib.ticker.LogitLocator")
 subclasses.

On this page