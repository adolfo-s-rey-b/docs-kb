[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.html#main-content)

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
    

mpl\_toolkits.axes\_grid1.inset\_locator[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.html#module-mpl_toolkits.axes_grid1.inset_locator "Link to this heading")

======================================================================================================================================================================================================

A collection of functions and objects for creating or placing inset axes.

Classes[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.html#classes "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`AnchoredLocatorBase`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.AnchoredLocatorBase.html#mpl_toolkits.axes_grid1.inset_locator.AnchoredLocatorBase "mpl_toolkits.axes_grid1.inset_locator.AnchoredLocatorBase")<br>(bbox\_to\_anchor, ...\[, ...\]) |     |
| [`AnchoredSizeLocator`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.AnchoredSizeLocator.html#mpl_toolkits.axes_grid1.inset_locator.AnchoredSizeLocator "mpl_toolkits.axes_grid1.inset_locator.AnchoredSizeLocator")<br>(bbox\_to\_anchor, x\_size, ...) |     |
| [`AnchoredZoomLocator`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.AnchoredZoomLocator.html#mpl_toolkits.axes_grid1.inset_locator.AnchoredZoomLocator "mpl_toolkits.axes_grid1.inset_locator.AnchoredZoomLocator")<br>(parent\_axes, zoom, loc) |     |
| [`BboxConnector`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.BboxConnector.html#mpl_toolkits.axes_grid1.inset_locator.BboxConnector "mpl_toolkits.axes_grid1.inset_locator.BboxConnector")<br>(bbox1, bbox2, loc1\[, loc2\]) | Connect two bboxes with a straight line. |
| [`BboxConnectorPatch`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.BboxConnectorPatch.html#mpl_toolkits.axes_grid1.inset_locator.BboxConnectorPatch "mpl_toolkits.axes_grid1.inset_locator.BboxConnectorPatch")<br>(bbox1, bbox2, loc1a, ...) | Connect two bboxes with a quadrilateral. |
| [`BboxPatch`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.BboxPatch.html#mpl_toolkits.axes_grid1.inset_locator.BboxPatch "mpl_toolkits.axes_grid1.inset_locator.BboxPatch")<br>(bbox, \*\*kwargs) | Patch showing the shape bounded by a Bbox. |

Functions[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.html#functions "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`inset_axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.inset_axes "mpl_toolkits.axes_grid1.inset_locator.inset_axes")<br>(parent\_axes, width, height\[, ...\]) | Create an inset axes with a given width and height. |
| [`mark_inset`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.mark_inset.html#mpl_toolkits.axes_grid1.inset_locator.mark_inset "mpl_toolkits.axes_grid1.inset_locator.mark_inset")<br>(parent\_axes, inset\_axes, loc1, ...) | Draw a box to mark the location of an area represented by an inset axes. |
| [`zoomed_inset_axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.zoomed_inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.zoomed_inset_axes "mpl_toolkits.axes_grid1.inset_locator.zoomed_inset_axes")<br>(parent\_axes, zoom\[, loc, ...\]) | Create an anchored inset axes by scaling a parent axes. |

On this page