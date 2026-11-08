[Skip to main content](https://matplotlib.org/stable/api/markers_api.html#main-content)

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
    

`matplotlib.markers`[#](https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers "Link to this heading")

=============================================================================================================================

Functions to handle markers; used by the marker functionality of [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
, [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
, and [`errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
.

All possible markers are defined here:

| marker | symbol | description |
| --- | --- | --- |
| `"."` | ![m00](https://matplotlib.org/stable/_images/m00.png) | point |
| `","` | ![m01](https://matplotlib.org/stable/_images/m01.png) | pixel |
| `"o"` | ![m02](https://matplotlib.org/stable/_images/m02.png) | circle |
| `"v"` | ![m03](https://matplotlib.org/stable/_images/m03.png) | triangle\_down |
| `"^"` | ![m04](https://matplotlib.org/stable/_images/m04.png) | triangle\_up |
| `"<"` | ![m05](https://matplotlib.org/stable/_images/m05.png) | triangle\_left |
| `">"` | ![m06](https://matplotlib.org/stable/_images/m06.png) | triangle\_right |
| `"1"` | ![m07](https://matplotlib.org/stable/_images/m07.png) | tri\_down |
| `"2"` | ![m08](https://matplotlib.org/stable/_images/m08.png) | tri\_up |
| `"3"` | ![m09](https://matplotlib.org/stable/_images/m09.png) | tri\_left |
| `"4"` | ![m10](https://matplotlib.org/stable/_images/m10.png) | tri\_right |
| `"8"` | ![m11](https://matplotlib.org/stable/_images/m11.png) | octagon |
| `"s"` | ![m12](https://matplotlib.org/stable/_images/m12.png) | square |
| `"p"` | ![m13](https://matplotlib.org/stable/_images/m13.png) | pentagon |
| `"P"` | ![m23](https://matplotlib.org/stable/_images/m23.png) | plus (filled) |
| `"*"` | ![m14](https://matplotlib.org/stable/_images/m14.png) | star |
| `"h"` | ![m15](https://matplotlib.org/stable/_images/m15.png) | hexagon1 |
| `"H"` | ![m16](https://matplotlib.org/stable/_images/m16.png) | hexagon2 |
| `"+"` | ![m17](https://matplotlib.org/stable/_images/m17.png) | plus |
| `"x"` | ![m18](https://matplotlib.org/stable/_images/m18.png) | x   |
| `"X"` | ![m24](https://matplotlib.org/stable/_images/m24.png) | x (filled) |
| `"D"` | ![m19](https://matplotlib.org/stable/_images/m19.png) | diamond |
| `"d"` | ![m20](https://matplotlib.org/stable/_images/m20.png) | thin\_diamond |
| `"\|"` | ![m21](https://matplotlib.org/stable/_images/m21.png) | vline |
| `"_"` | ![m22](https://matplotlib.org/stable/_images/m22.png) | hline |
| `0` (`TICKLEFT`) | ![m25](https://matplotlib.org/stable/_images/m25.png) | tickleft |
| `1` (`TICKRIGHT`) | ![m26](https://matplotlib.org/stable/_images/m26.png) | tickright |
| `2` (`TICKUP`) | ![m27](https://matplotlib.org/stable/_images/m27.png) | tickup |
| `3` (`TICKDOWN`) | ![m28](https://matplotlib.org/stable/_images/m28.png) | tickdown |
| `4` (`CARETLEFT`) | ![m29](https://matplotlib.org/stable/_images/m29.png) | caretleft |
| `5` (`CARETRIGHT`) | ![m30](https://matplotlib.org/stable/_images/m30.png) | caretright |
| `6` (`CARETUP`) | ![m31](https://matplotlib.org/stable/_images/m31.png) | caretup |
| `7` (`CARETDOWN`) | ![m32](https://matplotlib.org/stable/_images/m32.png) | caretdown |
| `8` (`CARETLEFTBASE`) | ![m33](https://matplotlib.org/stable/_images/m33.png) | caretleft (centered at base) |
| `9` (`CARETRIGHTBASE`) | ![m34](https://matplotlib.org/stable/_images/m34.png) | caretright (centered at base) |
| `10` (`CARETUPBASE`) | ![m35](https://matplotlib.org/stable/_images/m35.png) | caretup (centered at base) |
| `11` (`CARETDOWNBASE`) | ![m36](https://matplotlib.org/stable/_images/m36.png) | caretdown (centered at base) |
| `"none"` or `"None"` |     | nothing |
| `" "` or `""` |     | nothing |
| `"$...$"` | ![m37](https://matplotlib.org/stable/_images/m37.png) | Render the string using mathtext. E.g `"$f$"` for marker showing the letter `f`. |
| `verts` |     | A list of (x, y) pairs used for Path vertices. The center of the marker is located at (0, 0) and the size is normalized, such that the created path is encapsulated inside the unit cell. |
| `path` |     | A [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")<br> instance. |
| `(numsides, 0, angle)` |     | A regular polygon with `numsides` sides, rotated by `angle`. |
| `(numsides, 1, angle)` |     | A star-like symbol with `numsides` sides, rotated by `angle`. |
| `(numsides, 2, angle)` |     | An asterisk with `numsides` sides, rotated by `angle`. |

Note that special symbols can be defined via the [STIX math font](https://matplotlib.org/stable/users/explain/text/mathtext.html#mathtext)
, e.g. `"$\u266B$"`. For an overview over the STIX font symbols refer to the [STIX font table](http://www.stixfonts.org/allGlyphs.html)
. Also see the [STIX Fonts](https://matplotlib.org/stable/gallery/text_labels_and_annotations/stix_fonts_demo.html)
.

Integer numbers from `0` to `11` create lines and triangles. Those are equally accessible via capitalized variables, like `CARETDOWNBASE`. Hence the following are equivalent:

plt.plot(\[1, 2, 3\], marker\=11)
plt.plot(\[1, 2, 3\], marker\=matplotlib.markers.CARETDOWNBASE)

Markers join and cap styles can be customized by creating a new instance of MarkerStyle. A MarkerStyle can also have a custom [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 allowing it to be arbitrarily rotated or offset.

Examples showing the use of markers:

*   [Marker reference](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html)
    
*   [Marker examples](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_star_poly.html)
    
*   [Mapping marker properties to multivariate data](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multivariate_marker_plot.html)
    

Classes[#](https://matplotlib.org/stable/api/markers_api.html#classes "Link to this heading")

----------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`MarkerStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")<br>(marker\[, fillstyle, transform, ...\]) | A class representing marker types. |

On this page