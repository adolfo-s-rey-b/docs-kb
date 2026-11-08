[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#main-content)

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
    

matplotlib.axes.Axes.add\_collection[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib-axes-axes-add-collection "Link to this heading")

=======================================================================================================================================================================================

Axes.add\_collection(_collection_, _autolim\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L2395-L2448)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "Link to this definition")

Add a [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
 to the Axes; return the collection.

Parameters:

**collection**[`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")

The collection to add.

**autolim**bool

Whether to update data and view limits.

If _False_, the collection does not take part in any limit operations.

Changed in version 3.11: Since 3.11 `autolim=True` matches the standard behavior of other `add_[artist]` methods: Axes data and view limits are both updated in the method, and the collection will be considered in future data limit updates through [`relim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.relim.html#matplotlib.axes.Axes.relim "matplotlib.axes.Axes.relim")
.

Prior to matplotlib 3.11 this was only a one-time update of the data limits. Updating view limits required an explicit call to [`autoscale_view`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")
, and collections did not take part in [`relim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.relim.html#matplotlib.axes.Axes.relim "matplotlib.axes.Axes.relim")
.

As an implementation detail, the value "\_datalim\_only" is supported to smooth the internal transition from pre-3.11 behavior. This is not a public interface and will be removed again in the future.

Examples using `matplotlib.axes.Axes.add_collection`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#examples-using-matplotlib-axes-axes-add-collection "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_multicolored_line_thumb.png)

[Multicolored lines](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html)

Multicolored lines

![](https://matplotlib.org/stable/_images/sphx_glr_eventcollection_demo_thumb.png)

[EventCollection Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/eventcollection_demo.html)

EventCollection Demo

![](https://matplotlib.org/stable/_images/sphx_glr_errorbars_and_boxes_thumb.png)

[Create boxes from error bars using PatchCollection](https://matplotlib.org/stable/gallery/statistics/errorbars_and_boxes.html)

Create boxes from error bars using PatchCollection

![](https://matplotlib.org/stable/_images/sphx_glr_collections_thumb.png)

[Line, Poly and RegularPoly Collection](https://matplotlib.org/stable/gallery/shapes_and_collections/collections.html)

Line, Poly and RegularPoly Collection

![](https://matplotlib.org/stable/_images/sphx_glr_ellipse_collection_thumb.png)

[Ellipse Collection](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_collection.html)

Ellipse Collection

![](https://matplotlib.org/stable/_images/sphx_glr_line_collection_thumb.png)

[Plot multiple lines using a LineCollection](https://matplotlib.org/stable/gallery/shapes_and_collections/line_collection.html)

Plot multiple lines using a LineCollection

![](https://matplotlib.org/stable/_images/sphx_glr_patch_collection_thumb.png)

[Circles, Wedges and Polygons](https://matplotlib.org/stable/gallery/shapes_and_collections/patch_collection.html)

Circles, Wedges and Polygons

![](https://matplotlib.org/stable/_images/sphx_glr_lasso_demo_thumb.png)

[Lasso Demo](https://matplotlib.org/stable/gallery/event_handling/lasso_demo.html)

Lasso Demo

![](https://matplotlib.org/stable/_images/sphx_glr_artist_tests_thumb.png)

[Artist tests](https://matplotlib.org/stable/gallery/units/artist_tests.html)

Artist tests

On this page