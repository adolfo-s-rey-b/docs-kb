[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#main-content)

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
    

matplotlib.markers.MarkerStyle[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib-markers-markerstyle "Link to this heading")

=======================================================================================================================================================================

class matplotlib.markers.MarkerStyle(_marker_, _fillstyle\=None_, _transform\=None_, _capstyle\=None_, _joinstyle\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/markers.py#L150-L907)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A class representing marker types.

Instances are immutable. If you need to change anything, create a new instance.

Attributes:

**markers**dict

All known markers.

**filled\_markers**tuple

All known filled markers. This is a subset of _markers_.

**fillstyles**tuple

The supported fillstyles.

Parameters:

**marker**str, array-like, Path, MarkerStyle

*   Another instance of [`MarkerStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
     copies the details of that _marker_.
    
*   For other possible marker values, see the module docstring [`matplotlib.markers`](https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers "matplotlib.markers")
    .
    

**fillstyle**str, default: `[rcParams["markers.fillstyle"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=markers.fillstyle#rcparam-markers-fillstyle) ` (default: `'full'`)

One of 'full', 'left', 'right', 'bottom', 'top', 'none'.

**transform**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
, optional

Transform that will be combined with the native transform of the marker.

**capstyle**[`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")
 or %(CapStyle)s, optional

Cap style that will override the default cap style of the marker.

**joinstyle**[`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")
 or %(JoinStyle)s, optional

Join style that will override the default join style of the marker.

filled\_markers \= ('.', 'o', 'v', '^', '<', '>', '8', 's', 'p', '\*', 'h', 'H', 'D', 'd', 'P', 'X')[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle.filled_markers "Link to this definition")

fillstyles \= ('full', 'left', 'right', 'bottom', 'top', 'none')[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle.fillstyles "Link to this definition")

get\_alt\_path()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/markers.py#L354-L361)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle.get_alt_path "Link to this definition")

Return a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 for the alternate part of the marker.

For unfilled markers, this is _None_; for filled markers, this is the area to be drawn with _markerfacecoloralt_.

get\_alt\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/markers.py#L363-L371)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle.get_alt_transform "Link to this definition")

Return the transform to be applied to the [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 from [`MarkerStyle.get_alt_path()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle.get_alt_path "matplotlib.markers.MarkerStyle.get_alt_path")
.

get\_capstyle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/markers.py#L292-L293)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle.get_capstyle "Link to this definition")

get\_fillstyle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/markers.py#L272-L273)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle.get_fillstyle "Link to this definition")

get\_joinstyle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/markers.py#L289-L290)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle.get_joinstyle "Link to this definition")

get\_marker()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/markers.py#L295-L296)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle.get_marker "Link to this definition")

get\_path()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/markers.py#L335-L342)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle.get_path "Link to this definition")

Return a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 for the primary part of the marker.

For unfilled markers this is the whole marker, for filled markers, this is the area to be drawn with _markerfacecolor_.

get\_snap\_threshold()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/markers.py#L373-L374)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle.get_snap_threshold "Link to this definition")

get\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/markers.py#L344-L352)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle.get_transform "Link to this definition")

Return the transform to be applied to the [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 from [`MarkerStyle.get_path()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle.get_path "matplotlib.markers.MarkerStyle.get_path")
.

get\_user\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/markers.py#L376-L379)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle.get_user_transform "Link to this definition")

Return user supplied part of marker transform.

is\_filled()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/markers.py#L269-L270)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle.is_filled "Link to this definition")

markers \= {' ': 'nothing', '': 'nothing', '\*': 'star', '+': 'plus', ',': 'pixel', '.': 'point', '1': 'tri\_down', '2': 'tri\_up', '3': 'tri\_left', '4': 'tri\_right', '8': 'octagon', '<': 'triangle\_left', '>': 'triangle\_right', 'D': 'diamond', 'H': 'hexagon2', 'None': 'nothing', 'P': 'plus\_filled', 'X': 'x\_filled', '^': 'triangle\_up', '\_': 'hline', 'd': 'thin\_diamond', 'h': 'hexagon1', 'none': 'nothing', 'o': 'circle', 'p': 'pentagon', 's': 'square', 'v': 'triangle\_down', 'x': 'x', '|': 'vline', 0: 'tickleft', 1: 'tickright', 10: 'caretupbase', 11: 'caretdownbase', 2: 'tickup', 3: 'tickdown', 4: 'caretleft', 5: 'caretright', 6: 'caretup', 7: 'caretdown', 8: 'caretleftbase', 9: 'caretrightbase'}[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle.markers "Link to this definition")

rotated(_\*_, _deg\=None_, _rad\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/markers.py#L397-L424)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle.rotated "Link to this definition")

Return a new version of this marker rotated by specified angle.

Parameters:

**deg**float, optional

Rotation angle in degrees.

**rad**float, optional

Rotation angle in radians.

**.. note:: You must specify exactly one of deg or rad.**

scaled(_sx_, _sy\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/markers.py#L426-L446)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle.scaled "Link to this definition")

Return new marker scaled by specified scale factors.

If _sy_ is not given, the same scale is applied in both the _x_\- and _y_\-directions.

Parameters:

**sx**float

_X_\-direction scaling factor.

**sy**float, optional

_Y_\-direction scaling factor.

transformed(_transform_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/markers.py#L381-L395)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle.transformed "Link to this definition")

Return a new version of this marker with the transform applied.

Parameters:

**transform**[`Affine2D`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")

Transform will be combined with current user supplied transform.

Examples using `matplotlib.markers.MarkerStyle`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#examples-using-matplotlib-markers-markerstyle "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_marker_reference_thumb.png)

[Marker reference](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html)

Marker reference

![](https://matplotlib.org/stable/_images/sphx_glr_multivariate_marker_plot_thumb.png)

[Mapping marker properties to multivariate data](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multivariate_marker_plot.html)

Mapping marker properties to multivariate data

![](https://matplotlib.org/stable/_images/sphx_glr_ellipse_arrow_thumb.png)

[Ellipse with orientation arrow demo](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_arrow.html)

Ellipse with orientation arrow demo

On this page