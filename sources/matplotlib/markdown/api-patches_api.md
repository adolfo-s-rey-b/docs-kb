[Skip to main content](https://matplotlib.org/stable/api/patches_api.html#main-content)

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
    

`matplotlib.patches`[#](https://matplotlib.org/stable/api/patches_api.html#matplotlib-patches "Link to this heading")

======================================================================================================================

Inheritance diagram of matplotlib.patches

Patches are [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
s with a face color and an edge color.

Classes[#](https://matplotlib.org/stable/api/patches_api.html#classes "Link to this heading")

----------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Annulus`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Annulus.html#matplotlib.patches.Annulus "matplotlib.patches.Annulus")<br>(xy, r, width\[, angle\]) | An elliptical annulus. |
| [`Arc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")<br>(xy, width, height, \*\[, angle, theta1, ...\]) | An elliptical arc, i.e. a segment of an ellipse. |
| [`Arrow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arrow.html#matplotlib.patches.Arrow "matplotlib.patches.Arrow")<br>(x, y, dx, dy, \*\[, width\]) | An arrow patch. |
| [`ArrowStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle "matplotlib.patches.ArrowStyle")<br>(stylename, \*\*kwargs) | [`ArrowStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle "matplotlib.patches.ArrowStyle")<br> is a container class which defines several arrowstyle classes, which is used to create an arrow path along a given path. |
| [`BoxStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle "matplotlib.patches.BoxStyle")<br>(stylename, \*\*kwargs) | [`BoxStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle "matplotlib.patches.BoxStyle")<br> is a container class which defines several boxstyle classes, which are used for [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")<br>. |
| [`Circle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")<br>(xy\[, radius\]) | A circle patch. |
| [`CirclePolygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.CirclePolygon.html#matplotlib.patches.CirclePolygon "matplotlib.patches.CirclePolygon")<br>(xy\[, radius, resolution\]) | A polygon-approximation of a circle patch. |
| [`ConnectionPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")<br>(xyA, xyB, coordsA\[, ...\]) | A patch that connects two points (possibly in different Axes). |
| [`ConnectionStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionStyle.html#matplotlib.patches.ConnectionStyle "matplotlib.patches.ConnectionStyle")<br>(stylename, \*\*kwargs) | [`ConnectionStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionStyle.html#matplotlib.patches.ConnectionStyle "matplotlib.patches.ConnectionStyle")<br> is a container class which defines several connectionstyle classes, which is used to create a path between two points. |
| [`Ellipse`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")<br>(xy, width, height, \*\[, angle\]) | A scale-free ellipse. |
| [`FancyArrow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")<br>(x, y, dx, dy, \*\[, width, ...\]) | Like Arrow, but lets you set head width and head height independently. |
| [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")<br>(\[posA, posB, path, ...\]) | A fancy arrow patch. |
| [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")<br>(xy, width, height\[, ...\]) | A fancy box around a rectangle with lower left at _xy_ = (_x_, _y_) with specified width and height. |
| [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")<br>(\*\[, edgecolor, facecolor, color, ...\]) | A patch is a 2D artist with a face color and an edge color. |
| [`PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")<br>(path, \*\*kwargs) | A general polycurve path patch. |
| [`StepPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.StepPatch.html#matplotlib.patches.StepPatch "matplotlib.patches.StepPatch")<br>(values, edges, \*\[, orientation, ...\]) | A path patch describing a stepwise constant function. |
| [`Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")<br>(xy, \*\[, closed\]) | A general polygon patch. |
| [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")<br>(xy, width, height, \*\[, angle, ...\]) | A rectangle defined via an anchor point _xy_ and its _width_ and _height_. |
| [`RegularPolygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.RegularPolygon.html#matplotlib.patches.RegularPolygon "matplotlib.patches.RegularPolygon")<br>(xy, numVertices, \*\[, radius, ...\]) | A regular polygon patch. |
| [`Shadow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Shadow.html#matplotlib.patches.Shadow "matplotlib.patches.Shadow")<br>(patch, ox, oy, \*\[, shade\]) | Create a shadow of the given _patch_. |
| [`Wedge`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html#matplotlib.patches.Wedge "matplotlib.patches.Wedge")<br>(center, r, theta1, theta2, \*\[, width\]) | Wedge shaped patch. |

Functions[#](https://matplotlib.org/stable/api/patches_api.html#functions "Link to this heading")

--------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`bbox_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.bbox_artist.html#matplotlib.patches.bbox_artist "matplotlib.patches.bbox_artist")<br>(artist, renderer\[, props, fill\]) | A debug function to draw a rectangle around the bounding box returned by an artist's [`Artist.get_window_extent`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_window_extent.html#matplotlib.artist.Artist.get_window_extent "matplotlib.artist.Artist.get_window_extent")<br> to test whether the artist is returning the correct bbox. |
| [`draw_bbox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.draw_bbox.html#matplotlib.patches.draw_bbox "matplotlib.patches.draw_bbox")<br>(bbox, renderer\[, color, trans\]) | A debug function to draw a rectangle around the bounding box returned by an artist's [`Artist.get_window_extent`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_window_extent.html#matplotlib.artist.Artist.get_window_extent "matplotlib.artist.Artist.get_window_extent")<br> to test whether the artist is returning the correct bbox. |

On this page