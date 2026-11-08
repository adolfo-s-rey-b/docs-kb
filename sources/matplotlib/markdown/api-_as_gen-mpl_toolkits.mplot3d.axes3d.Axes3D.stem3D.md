[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.stem3D.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.stem3D[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.stem3D.html#mpl-toolkits-mplot3d-axes3d-axes3d-stem3d "Link to this heading")

=========================================================================================================================================================================================================

Axes3D.stem3D(_x_, _y_, _z_, _\*_, _linefmt\='C0-'_, _markerfmt\='C0o'_, _basefmt\='C3-'_, _bottom\=0_, _label\=None_, _orientation\='z'_, _axlim\_clip\=False_, _data\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L4202-L4322)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.stem3D.html#mpl_toolkits.mplot3d.axes3d.Axes3D.stem3D "Link to this definition")

Create a 3D stem plot.

A stem plot draws lines perpendicular to a baseline, and places markers at the heads. By default, the baseline is defined by _x_ and _y_, and stems are drawn vertically from _bottom_ to _z_.

Parameters:

**x, y, z**array-like

The positions of the heads of the stems. The stems are drawn along the _orientation_\-direction from the baseline at _bottom_ (in the _orientation_\-coordinate) to the heads. By default, the _x_ and _y_ positions are used for the baseline and _z_ for the head position, but this can be changed by _orientation_.

**linefmt**str, default: 'C0-'

A string defining the properties of the vertical lines. Usually, this will be a color or a color and a linestyle:

| Character | Line Style |
| --- | --- |
| `'-'` | solid line |
| `'--'` | dashed line |
| `'-.'` | dash-dot line |
| `':'` | dotted line |

Note: While it is technically possible to specify valid formats other than color or color and linestyle (e.g. 'rx' or '-.'), this is beyond the intention of the method and will most likely not result in a reasonable plot.

**markerfmt**str, default: 'C0o'

A string defining the properties of the markers at the stem heads.

**basefmt**str, default: 'C3-'

A format string defining the properties of the baseline.

**bottom**float, default: 0

The position of the baseline, in _orientation_\-coordinates.

**label**str, optional

The label to use for the stems in legends.

**orientation**{'x', 'y', 'z'}, default: 'z'

The direction along which stems are drawn.

**axlim\_clip**bool, default: False

Whether to hide stems that are outside the axes limits.

Added in version 3.10.

**data**indexable object, optional

If given, all parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`.

Returns:

[`StemContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.StemContainer "matplotlib.container.StemContainer")

The container may be treated like a tuple (_markerline_, _stemlines_, _baseline_)

Examples

([`Source code`](https://matplotlib.org/stable/_downloads/1fbb58d502ed9a7088a2ade19d7ca1c6/stem3d_demo.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/637be93b7e35f366da0dee31146666a9/stem3d_demo_00_00.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/5834e9146e5baeb85a4dfb152d32dac4/stem3d_demo_00_00.png)
)

[![](https://matplotlib.org/stable/_images/api-_as_gen-stem3d_demo_00_00.2x.png)](https://matplotlib.org/stable/_images/api-_as_gen-stem3d_demo_00_00.2x.png)

([`2x.png`](https://matplotlib.org/stable/_downloads/e770d4d7793563a0145db1144561f216/stem3d_demo_01_00.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/e16fd027b183d3cec3d1cac953925761/stem3d_demo_01_00.png)
)

[![](https://matplotlib.org/stable/_images/api-_as_gen-stem3d_demo_01_00.2x.png)](https://matplotlib.org/stable/_images/api-_as_gen-stem3d_demo_01_00.2x.png)

([`2x.png`](https://matplotlib.org/stable/_downloads/6c3417f2564c72a4e9426cdfd2837f71/stem3d_demo_02_00.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/aa75822728ded904624b8810c33fb310/stem3d_demo_02_00.png)
)

[![](https://matplotlib.org/stable/_images/api-_as_gen-stem3d_demo_02_00.2x.png)](https://matplotlib.org/stable/_images/api-_as_gen-stem3d_demo_02_00.2x.png)

On this page