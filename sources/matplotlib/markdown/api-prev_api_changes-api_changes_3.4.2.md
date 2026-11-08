[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.2.html#main-content)

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
    

API Changes for 3.4.2[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.2.html#api-changes-for-3-4-2 "Link to this heading")

=================================================================================================================================================

Behaviour changes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.2.html#behaviour-changes "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

### Rename first argument to `subplot_mosaic`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.4.2.html#rename-first-argument-to-subplot-mosaic "Link to this heading")

Both [`Figure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
, and [`pyplot.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
 have had the first position argument renamed from _layout_ to _mosaic_. This is because we are considering to consolidate _constrained\_layout_ and _tight\_layout_ keyword arguments in the Figure creation functions of [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 into a single _layout_ keyword argument which would collide.

As this API is provisional, we are changing this with no deprecation period.

On this page