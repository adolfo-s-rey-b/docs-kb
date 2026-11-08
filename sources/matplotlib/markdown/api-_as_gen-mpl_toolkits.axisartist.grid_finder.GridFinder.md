[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.GridFinder.html#main-content)

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
    

mpl\_toolkits.axisartist.grid\_finder.GridFinder[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.GridFinder.html#mpl-toolkits-axisartist-grid-finder-gridfinder "Link to this heading")

=========================================================================================================================================================================================================================

class mpl\_toolkits.axisartist.grid\_finder.GridFinder(_transform_, _extreme\_finder\=None_, _grid\_locator1\=None_, _grid\_locator2\=None_, _tick\_formatter1\=None_, _tick\_formatter2\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/grid_finder.py#L129-L267)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.GridFinder.html#mpl_toolkits.axisartist.grid_finder.GridFinder "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Internal helper for [`GridHelperCurveLinear`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear.html#mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear "mpl_toolkits.axisartist.grid_helper_curvelinear.GridHelperCurveLinear")
, with the same constructor parameters; should not be directly instantiated.

get\_grid\_info(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/grid_finder.py#L172-L223)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.GridFinder.html#mpl_toolkits.axisartist.grid_finder.GridFinder.get_grid_info "Link to this definition")

Compute positioning information for grid lines and ticks, given the axes' data _bbox_.

get\_transform()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/grid_finder.py#L244-L245)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.GridFinder.html#mpl_toolkits.axisartist.grid_finder.GridFinder.get_transform "Link to this definition")

inv\_transform\_xy(_x_, _y_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/grid_finder.py#L253-L256)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.GridFinder.html#mpl_toolkits.axisartist.grid_finder.GridFinder.inv_transform_xy "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.11: Use grid\_finder.get\_transform().inverted() instead.

set\_transform(_aux\_trans_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/grid_finder.py#L235-L242)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.GridFinder.html#mpl_toolkits.axisartist.grid_finder.GridFinder.set_transform "Link to this definition")

transform\_xy(_x_, _y_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/grid_finder.py#L249-L251)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.GridFinder.html#mpl_toolkits.axisartist.grid_finder.GridFinder.transform_xy "Link to this definition")

\[_Deprecated_\]

Notes

Deprecated since version 3.11: Use grid\_finder.get\_transform() instead.

update(_\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/grid_finder.py#L258-L267)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.GridFinder.html#mpl_toolkits.axisartist.grid_finder.GridFinder.update "Link to this definition")

update\_transform(_aux\_trans_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/grid_finder.py#L235-L242)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.GridFinder.html#mpl_toolkits.axisartist.grid_finder.GridFinder.update_transform "Link to this definition")

On this page