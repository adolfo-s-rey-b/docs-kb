[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiverkey.html#main-content)

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
    

matplotlib.pyplot.quiverkey[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiverkey.html#matplotlib-pyplot-quiverkey "Link to this heading")

==============================================================================================================================================================

matplotlib.pyplot.quiverkey(_Q_, _X_, _Y_, _U_, _label_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L4100-L4104)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiverkey.html#matplotlib.pyplot.quiverkey "Link to this definition")

Add a key to a quiver plot.

The positioning of the key depends on _X_, _Y_, _coordinates_, and _labelpos_. If _labelpos_ is 'N' or 'S', _X_, _Y_ give the position of the middle of the key arrow. If _labelpos_ is 'E', _X_, _Y_ positions the head, and if _labelpos_ is 'W', _X_, _Y_ positions the tail; in either of these two cases, _X_, _Y_ is somewhere in the middle of the arrow+label key object.

Parameters:

**Q**[`Quiver`](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.Quiver.html#matplotlib.quiver.Quiver "matplotlib.quiver.Quiver")

A [`Quiver`](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.Quiver.html#matplotlib.quiver.Quiver "matplotlib.quiver.Quiver")
 object as returned by a call to [`quiver()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html#matplotlib.axes.Axes.quiver "matplotlib.axes.Axes.quiver")
.

**X, Y**float

The location of the key.

**U**float

The length of the key.

**label**str

The key label (e.g., length and units of the key).

**angle**float, default: 0

The angle of the key arrow, in degrees anti-clockwise from the horizontal axis.

**coordinates**{'axes', 'figure', 'data', 'inches'}, default: 'axes'

Coordinate system and units for _X_, _Y_: 'axes' and 'figure' are normalized coordinate systems with (0, 0) in the lower left and (1, 1) in the upper right; 'data' are the axes data coordinates (used for the locations of the vectors in the quiver plot itself); 'inches' is position in the figure in inches, with (0, 0) at the lower left corner.

**color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

Overrides face and edge colors from _Q_.

**labelpos**{'N', 'S', 'E', 'W'}

Position the label above, below, to the right, to the left of the arrow, respectively.

**labelsep**float, default: 0.1

Distance in inches between the arrow and the label.

**labelcolor**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, default: `[rcParams["text.color"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.color#rcparam-text-color) ` (default: `'black'`)

Label color.

**fontproperties**dict, optional

A dictionary with keyword arguments accepted by the [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 initializer: _family_, _style_, _variant_, _size_, _weight_.

**zorder**float

The zorder of the key. The default is 0.1 above _Q_.

**\*\*kwargs**

Any additional keyword arguments are used to override vector properties taken from _Q_.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.quiverkey`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiverkey.html#matplotlib.axes.Axes.quiverkey "matplotlib.axes.Axes.quiverkey")
.

Examples using `matplotlib.pyplot.quiverkey`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiverkey.html#examples-using-matplotlib-pyplot-quiverkey "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_quiver_simple_demo_thumb.png)

[Quiver Simple Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/quiver_simple_demo.html)

Quiver Simple Demo

![](https://matplotlib.org/stable/_images/sphx_glr_quiver_demo_thumb.png)

[Advanced quiver and quiverkey functions](https://matplotlib.org/stable/gallery/images_contours_and_fields/quiver_demo.html)

Advanced quiver and quiverkey functions

On this page