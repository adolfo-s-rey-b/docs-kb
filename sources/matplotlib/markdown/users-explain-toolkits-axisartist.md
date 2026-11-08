[Skip to main content](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#main-content)

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
    

The axisartist toolkit[#](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#the-axisartist-toolkit "Link to this heading")

==============================================================================================================================================

Warning

_axisartist_ uses a custom Axes class (derived from the Matplotlib's original Axes class). As a side effect, some commands (mostly tick-related) do not work.

The _axisartist_ contains a custom Axes class that is meant to support curvilinear grids (e.g., the world coordinate system in astronomy). Unlike Matplotlib's original Axes class which uses Axes.xaxis and Axes.yaxis to draw ticks, ticklines, etc., axisartist uses a special artist (AxisArtist) that can handle ticks, ticklines, etc. for curved coordinate systems.

[![../../../_images/sphx_glr_demo_floating_axis_001.png](https://matplotlib.org/stable/_images/sphx_glr_demo_floating_axis_001.png)](https://matplotlib.org/gallery/axisartist/demo_floating_axis.html)

Since it uses special artists, some Matplotlib commands that work on Axes.xaxis and Axes.yaxis may not work.

axisartist[#](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#axisartist-users-guide-index "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

The _axisartist_ module provides a custom (and very experimental) Axes class, where each axis (left, right, top, and bottom) have a separate associated artist which is responsible for drawing the axis-line, ticks, ticklabels, and labels. You can also create your own axis, which can pass through a fixed position in the axes coordinate, or a fixed position in the data coordinate (i.e., the axis floats around when viewlimit changes).

The axes class, by default, has its xaxis and yaxis invisible, and has 4 additional artists which are responsible for drawing the 4 axis spines in "left", "right", "bottom", and "top". They are accessed as ax.axis\["left"\], ax.axis\["right"\], and so on, i.e., ax.axis is a dictionary that contains artists (note that ax.axis is still a callable method and it behaves as an original Axes.axis method in Matplotlib).

To create an Axes,

import mpl\_toolkits.axisartist as AA
fig \= plt.figure()
fig.add\_axes((0.1, 0.1, 0.8, 0.8), axes\_class\=AA.Axes)

or to create a subplot

fig.add\_subplot(111, axes\_class\=AA.Axes)
\# Given that 111 is the default, one can also do
fig.add\_subplot(axes\_class\=AA.Axes)

For example, you can hide the right and top spines using:

ax.axis\["right"\].set\_visible(False)
ax.axis\["top"\].set\_visible(False)

[![../../../_images/sphx_glr_simple_axisline3_001.png](https://matplotlib.org/stable/_images/sphx_glr_simple_axisline3_001.png)](https://matplotlib.org/gallery/axisartist/simple_axisline3.html)

It is also possible to add a horizontal axis. For example, you may have an horizontal axis at y=0 (in data coordinate).

ax.axis\["y=0"\] \= ax.new\_floating\_axis(nth\_coord\=0, value\=0)

[![../../../_images/sphx_glr_simple_axisartist1_001.png](https://matplotlib.org/stable/_images/sphx_glr_simple_axisartist1_001.png)](https://matplotlib.org/gallery/axisartist/simple_axisartist1.html)

Or a fixed axis with some offset

\# make new (right-side) yaxis, but with some offset
ax.axis\["right2"\] \= ax.new\_fixed\_axis(loc\="right", offset\=(20, 0))

### axisartist with ParasiteAxes[#](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#axisartist-with-parasiteaxes "Link to this heading")

Most commands in the axes\_grid1 toolkit can take an axes\_class keyword argument, and the commands create an Axes of the given class. For example, to create a host subplot with axisartist.Axes,

import mpl\_toolkits.axisartist as AA
from mpl\_toolkits.axes\_grid1 import host\_subplot

host \= host\_subplot(111, axes\_class\=AA.Axes)

Here is an example that uses ParasiteAxes.

[![../../../_images/sphx_glr_demo_parasite_axes2_001.png](https://matplotlib.org/stable/_images/sphx_glr_demo_parasite_axes2_001.png)](https://matplotlib.org/gallery/axisartist/demo_parasite_axes2.html)

### Curvilinear grid[#](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#curvilinear-grid "Link to this heading")

The motivation behind the AxisArtist module is to support a curvilinear grid and ticks.

[![../../../_images/sphx_glr_demo_curvelinear_grid_001.png](https://matplotlib.org/stable/_images/sphx_glr_demo_curvelinear_grid_001.png)](https://matplotlib.org/gallery/axisartist/demo_curvelinear_grid.html)

### Floating Axes[#](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#floating-axes "Link to this heading")

AxisArtist also supports a Floating Axes whose outer axes are defined as floating axis.

[![../../../_images/sphx_glr_demo_floating_axes_001.png](https://matplotlib.org/stable/_images/sphx_glr_demo_floating_axes_001.png)](https://matplotlib.org/gallery/axisartist/demo_floating_axes.html)

axisartist namespace[#](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#axisartist-namespace "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

The _axisartist_ namespace includes a derived Axes implementation. The biggest difference is that the artists responsible to draw axis line, ticks, ticklabel and axis labels are separated out from the Matplotlib's Axis class, which are much more than artists in the original Matplotlib. This change was strongly motivated to support curvilinear grid. Here are a few things that mpl\_toolkits.axisartist.Axes is different from original Axes from Matplotlib.

*   Axis elements (axis line(spine), ticks, ticklabel and axis labels) are drawn by an AxisArtist instance. Unlike Axis, left, right, top and bottom axis are drawn by separate artists. And each of them may have different tick location and different tick labels.
    
*   gridlines are drawn by a Gridlines instance. The change was motivated that in curvilinear coordinate, a gridline may not cross axis-lines (i.e., no associated ticks). In the original Axes class, gridlines are tied to ticks.
    
*   ticklines can be rotated if necessary (i.e, along the gridlines)
    

In summary, all these changes was to support

*   a curvilinear grid.
    
*   a floating axis
    

[![../../../_images/sphx_glr_demo_floating_axis_001.png](https://matplotlib.org/stable/_images/sphx_glr_demo_floating_axis_001.png)](https://matplotlib.org/gallery/axisartist/demo_floating_axis.html)

_mpl\_toolkits.axisartist.Axes_ class defines a _axis_ attribute, which is a dictionary of AxisArtist instances. By default, the dictionary has 4 AxisArtist instances, responsible for drawing of left, right, bottom and top axis.

xaxis and yaxis attributes are still available, however they are set to not visible. As separate artists are used for rendering axis, some axis-related method in Matplotlib may have no effect. In addition to AxisArtist instances, the mpl\_toolkits.axisartist.Axes will have _gridlines_ attribute (Gridlines), which obviously draws grid lines.

In both AxisArtist and Gridlines, the calculation of tick and grid location is delegated to an instance of GridHelper class. mpl\_toolkits.axisartist.Axes class uses GridHelperRectlinear as a grid helper. The GridHelperRectlinear class is a wrapper around the _xaxis_ and _yaxis_ of Matplotlib's original Axes, and it was meant to work as the way how Matplotlib's original axes works. For example, tick location changes using set\_ticks method and etc. should work as expected. But change in artist properties (e.g., color) will not work in general, although some effort has been made so that some often-change attributes (color, etc.) are respected.

AxisArtist[#](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#id2 "Link to this heading")

---------------------------------------------------------------------------------------------------------------

AxisArtist can be considered as a container artist with following attributes which will draw ticks, labels, etc.

*   line
    
*   major\_ticks, major\_ticklabels
    
*   minor\_ticks, minor\_ticklabels
    
*   offsetText
    
*   label
    

### line[#](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#line "Link to this heading")

Derived from Line2D class. Responsible for drawing a spinal(?) line.

### major\_ticks, minor\_ticks[#](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#major-ticks-minor-ticks "Link to this heading")

Derived from Line2D class. Note that ticks are markers.

### major\_ticklabels, minor\_ticklabels[#](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#major-ticklabels-minor-ticklabels "Link to this heading")

Derived from Text. Note that it is not a list of Text artist, but a single artist (similar to a collection).

### axislabel[#](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#axislabel "Link to this heading")

Derived from Text.

Default AxisArtists[#](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#default-axisartists "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

By default, following for axis artists are defined.:

ax.axis\["left"\], ax.axis\["bottom"\], ax.axis\["right"\], ax.axis\["top"\]

The ticklabels and axislabel of the top and the right axis are set to not visible.

For example, if you want to change the color attributes of major\_ticklabels of the bottom x-axis

ax.axis\["bottom"\].major\_ticklabels.set\_color("b")

Similarly, to make ticklabels invisible

ax.axis\["bottom"\].major\_ticklabels.set\_visible(False)

AxisArtist provides a helper method to control the visibility of ticks, ticklabels, and label. To make ticklabel invisible,

ax.axis\["bottom"\].toggle(ticklabels\=False)

To make all of ticks, ticklabels, and (axis) label invisible

ax.axis\["bottom"\].toggle(all\=False)

To turn all off but ticks on

ax.axis\["bottom"\].toggle(all\=False, ticks\=True)

To turn all on but (axis) label off

ax.axis\["bottom"\].toggle(all\=True, label\=False)

ax.axis's \_\_getitem\_\_ method can take multiple axis names. For example, to turn ticklabels of "top" and "right" axis on,

ax.axis\["top", "right"\].toggle(ticklabels\=True)

Note that `ax.axis["top", "right"]` returns a simple proxy object that translate above code to something like below.

for n in \["top", "right"\]:
    ax.axis\[n\].toggle(ticklabels\=True)

So, any return values in the for loop are ignored. And you should not use it anything more than a simple method.

Like the list indexing ":" means all items, i.e.,

ax.axis\[:\].major\_ticks.set\_color("r")

changes tick color in all axis.

HowTo[#](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#howto "Link to this heading")

------------------------------------------------------------------------------------------------------------

1.  Changing tick locations and label.
    
    Same as the original Matplotlib's axes:
    
    ax.set\_xticks(\[1, 2, 3\])
    
2.  Changing axis properties like color, etc.
    
    Change the properties of appropriate artists. For example, to change the color of the ticklabels:
    
    ax.axis\["left"\].major\_ticklabels.set\_color("r")
    
3.  To change the attributes of multiple axis:
    
    ax.axis\["left", "bottom"\].major\_ticklabels.set\_color("r")
    
    or to change the attributes of all axis:
    
    ax.axis\[:\].major\_ticklabels.set\_color("r")
    
4.  To change the tick size (length), use `axis.major_ticks.set_ticksize`.
    
    To change the direction of the ticks, use `axis.major_ticks.set_tick_direction`.
    
    To change the pad between ticks and ticklabels, use `axis.major_ticklabels.set_pad`.
    
    To change the pad between ticklabels and axis label, use `axis.label.set_pad`.
    

Rotation and alignment of TickLabels[#](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#rotation-and-alignment-of-ticklabels "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This is also quite different from standard Matplotlib and can be confusing. When you want to rotate the ticklabels, first consider using "set\_axis\_direction" method.

ax1.axis\["left"\].major\_ticklabels.set\_axis\_direction("top")
ax1.axis\["right"\].label.set\_axis\_direction("left")

[![../../../_images/sphx_glr_simple_axis_direction01_001.png](https://matplotlib.org/stable/_images/sphx_glr_simple_axis_direction01_001.png)](https://matplotlib.org/gallery/axisartist/simple_axis_direction01.html)

The parameter for set\_axis\_direction is one of \["left", "right", "bottom", "top"\].

You must understand some underlying concept of directions.

*   There is a reference direction which is defined as the direction of the axis line with increasing coordinate. For example, the reference direction of the left x-axis is from bottom to top.
    
    The direction, text angle, and alignments of the ticks, ticklabels and axis-label is determined with respect to the reference direction
    
*   _label\_direction_ and _ticklabel\_direction_ are either the right-hand side (+) of the reference direction or the left-hand side (-).
    
*   ticks are by default drawn toward the opposite direction of the ticklabels.
    
*   text rotation of ticklabels and label is determined in reference to the _ticklabel\_direction_ or _label\_direction_, respectively. The rotation of ticklabels and label is anchored.
    

[![../../../_images/sphx_glr_axis_direction_001.png](https://matplotlib.org/stable/_images/sphx_glr_axis_direction_001.png)](https://matplotlib.org/gallery/axisartist/axis_direction.html)

On the other hand, there is a concept of "axis\_direction". This is a default setting of above properties for each, "bottom", "left", "top", and "right" axis.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |`axislabel` property defaults[#](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#id3 "Link to this table")
| reference direction | label direction | label rotation | horizontal alignment | vertical alignment |
| --- | --- | --- | --- | --- |
| left | '-' | 180 | right | center |
| bottom | '+' | 0   | center | top |
| right | '+' | 0   | right | center |
| top | '-' | 180 | center | bottom |

|     |     |     |     |     |
| --- | --- | --- | --- | --- |`ticklabel` property defaults[#](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#id4 "Link to this table")
| reference direction | label direction | label rotation | horizontal alignment | vertical alignment |
| --- | --- | --- | --- | --- |
| left | '-' | 90  | right | center |
| bottom | '+' | 0   | center | baseline |
| right | '+' | \-90 | right | center |
| top | '-' | 180 | center | baseline |

And, 'set\_axis\_direction("top")' means to adjust the text rotation etc, for settings suitable for "top" axis. The concept of axis direction can be more clear with curved axis.

[![../../../_images/sphx_glr_demo_axis_direction_001.png](https://matplotlib.org/stable/_images/sphx_glr_demo_axis_direction_001.png)](https://matplotlib.org/gallery/axisartist/demo_axis_direction.html)

The axis\_direction can be adjusted in the AxisArtist level, or in the level of its child artists, i.e., ticks, ticklabels, and axis-label.

ax1.axis\["left"\].set\_axis\_direction("top")

changes axis\_direction of all the associated artist with the "left" axis, while

ax1.axis\["left"\].major\_ticklabels.set\_axis\_direction("top")

changes the axis\_direction of only the major\_ticklabels. Note that set\_axis\_direction in the AxisArtist level changes the ticklabel\_direction and label\_direction, while changing the axis\_direction of ticks, ticklabels, and axis-label does not affect them.

If you want to make ticks outward and ticklabels inside the axes, use [`AxisArtist.invert_ticklabel_direction`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.invert_ticklabel_direction "mpl_toolkits.axisartist.axis_artist.AxisArtist.invert_ticklabel_direction")
:

ax.axis\[:\].invert\_ticklabel\_direction()

A related method is [`Ticks.set_tick_direction`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.Ticks.html#mpl_toolkits.axisartist.axis_artist.Ticks.set_tick_direction "mpl_toolkits.axisartist.axis_artist.Ticks.set_tick_direction")
. It can make ticks point "in", "out", or "inout" (crossing the axis halfway):

ax.axis\[:\].major\_ticks.set\_tick\_direction("inout")

[![../../../_images/sphx_glr_simple_axis_direction03_001.png](https://matplotlib.org/stable/_images/sphx_glr_simple_axis_direction03_001.png)](https://matplotlib.org/gallery/axisartist/simple_axis_direction03.html)

So, in summary,

*   AxisArtist's methods
    
    *   [`set_axis_direction`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.set_axis_direction "mpl_toolkits.axisartist.axis_artist.AxisArtist.set_axis_direction")
        : "left", "right", "bottom", or "top"
        
    *   [`set_ticklabel_direction`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.set_ticklabel_direction "mpl_toolkits.axisartist.axis_artist.AxisArtist.set_ticklabel_direction")
        : "+" or "-"
        
    *   [`set_axislabel_direction`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.set_axislabel_direction "mpl_toolkits.axisartist.axis_artist.AxisArtist.set_axislabel_direction")
        : "+" or "-"
        
    *   [`invert_ticklabel_direction`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist.invert_ticklabel_direction "mpl_toolkits.axisartist.axis_artist.AxisArtist.invert_ticklabel_direction")
        
*   Ticks' methods (major\_ticks and minor\_ticks)
    
    *   [`set_tick_direction`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.Ticks.html#mpl_toolkits.axisartist.axis_artist.Ticks.set_tick_direction "mpl_toolkits.axisartist.axis_artist.Ticks.set_tick_direction")
        : "in", "out", or "inout"
        
    *   [`set_ticksize`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.Ticks.html#mpl_toolkits.axisartist.axis_artist.Ticks.set_ticksize "mpl_toolkits.axisartist.axis_artist.Ticks.set_ticksize")
        : size in points
        
*   TickLabels' methods (major\_ticklabels and minor\_ticklabels)
    
    *   [`set_axis_direction`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.TickLabels.html#mpl_toolkits.axisartist.axis_artist.TickLabels.set_axis_direction "mpl_toolkits.axisartist.axis_artist.TickLabels.set_axis_direction")
        : "left", "right", "bottom", or "top"
        
    *   [`set_rotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation "matplotlib.text.Text.set_rotation")
        : angle with respect to the reference direction
        
    *   [`set_horizontalalignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_horizontalalignment "matplotlib.text.Text.set_horizontalalignment")
         and [`set_verticalalignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_verticalalignment "matplotlib.text.Text.set_verticalalignment")
        : see below
        
*   AxisLabel' methods (label)
    
    *   [`set_axis_direction`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisLabel.html#mpl_toolkits.axisartist.axis_artist.AxisLabel.set_axis_direction "mpl_toolkits.axisartist.axis_artist.AxisLabel.set_axis_direction")
        : "left", "right", "bottom", or "top"
        
    *   [`set_rotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation "matplotlib.text.Text.set_rotation")
        : angle with respect to the reference direction
        
    *   [`set_horizontalalignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_horizontalalignment "matplotlib.text.Text.set_horizontalalignment")
         and [`set_verticalalignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_verticalalignment "matplotlib.text.Text.set_verticalalignment")
        

### Adjusting ticklabels alignment[#](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#adjusting-ticklabels-alignment "Link to this heading")

Alignment of TickLabels are treated specially. See below

[![../../../_images/sphx_glr_demo_ticklabel_alignment_001.png](https://matplotlib.org/stable/_images/sphx_glr_demo_ticklabel_alignment_001.png)](https://matplotlib.org/gallery/axisartist/demo_ticklabel_alignment.html)

### Adjusting pad[#](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#adjusting-pad "Link to this heading")

To change the pad between ticks and ticklabels

ax.axis\["left"\].major\_ticklabels.set\_pad(10)

Or ticklabels and axis-label

ax.axis\["left"\].label.set\_pad(10)

[![../../../_images/sphx_glr_simple_axis_pad_001.png](https://matplotlib.org/stable/_images/sphx_glr_simple_axis_pad_001.png)](https://matplotlib.org/gallery/axisartist/simple_axis_pad.html)

GridHelper[#](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#gridhelper "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

To actually define a curvilinear coordinate, you have to use your own grid helper. A generalised version of grid helper class is supplied and this class should suffice in most of cases. A user may provide two functions which defines a transformation (and its inverse pair) from the curved coordinate to (rectilinear) image coordinate. Note that while ticks and grids are drawn for curved coordinate, the data transform of the axes itself (ax.transData) is still rectilinear (image) coordinate.

from mpl\_toolkits.axisartist.grid\_helper\_curvelinear \\
     import GridHelperCurveLinear
from mpl\_toolkits.axisartist import Axes

\# from curved coordinate to rectlinear coordinate.
def tr(x, y):
    x, y \= np.asarray(x), np.asarray(y)
    return x, y\-x

\# from rectlinear coordinate to curved coordinate.
def inv\_tr(x, y):
    x, y \= np.asarray(x), np.asarray(y)
    return x, y+x

grid\_helper \= GridHelperCurveLinear((tr, inv\_tr))

fig.add\_subplot(axes\_class\=Axes, grid\_helper\=grid\_helper)

You may use Matplotlib's Transform instance instead (but a inverse transformation must be defined). Often, coordinate range in a curved coordinate system may have a limited range, or may have cycles. In those cases, a more customized version of grid helper is required.

import mpl\_toolkits.axisartist.angle\_helper as angle\_helper

\# PolarAxes.PolarTransform takes radian. However, we want our coordinate
\# system in degree
tr \= Affine2D().scale(np.pi/180., 1.) + PolarAxes.PolarTransform()

\# extreme finder: find a range of coordinate.
\# 20, 20: number of sampling points along x, y direction
\# The first coordinate (longitude, but theta in polar)
\#   has a cycle of 360 degree.
\# The second coordinate (latitude, but radius in polar)  has a minimum of 0
extreme\_finder \= angle\_helper.ExtremeFinderCycle(20, 20,
                                                 lon\_cycle\=360,
                                                 lat\_cycle\=None,
                                                 lon\_minmax\=None,
                                                 lat\_minmax\=(0, np.inf),
                                                 )

\# Find a grid values appropriate for the coordinate (degree,
\# minute, second). The argument is an approximate number of grids.
grid\_locator1 \= angle\_helper.LocatorDMS(12)

\# And also uses an appropriate formatter.  Note that the acceptable Locator
\# and Formatter classes are different than that of Matplotlib's, and you
\# cannot directly use Matplotlib's Locator and Formatter here (but may be
\# possible in the future).
tick\_formatter1 \= angle\_helper.FormatterDMS()

grid\_helper \= GridHelperCurveLinear(tr,
                                    extreme\_finder\=extreme\_finder,
                                    grid\_locator1\=grid\_locator1,
                                    tick\_formatter1\=tick\_formatter1
                                    )

Again, the _transData_ of the axes is still a rectilinear coordinate (image coordinate). You may manually do conversion between two coordinates, or you may use Parasite Axes for convenience.:

ax1 \= SubplotHost(fig, 1, 2, 2, grid\_helper\=grid\_helper)

\# A parasite axes with given transform
ax2 \= ax1.get\_aux\_axes(tr, "equal")
\# note that ax2.transData == tr + ax1.transData
\# Anything you draw in ax2 will match the ticks and grids of ax1.

[![../../../_images/sphx_glr_demo_curvelinear_grid_001.png](https://matplotlib.org/stable/_images/sphx_glr_demo_curvelinear_grid_001.png)](https://matplotlib.org/gallery/axisartist/demo_curvelinear_grid.html)

FloatingAxis[#](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#floatingaxis "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

A floating axis is an axis one of whose data coordinate is fixed, i.e, its location is not fixed in Axes coordinate but changes as axes data limits changes. A floating axis can be created using _new\_floating\_axis_ method. However, it is your responsibility that the resulting AxisArtist is properly added to the axes. A recommended way is to add it as an item of Axes's axis attribute.:

\# floating axis whose first (index starts from 0) coordinate
\# (theta) is fixed at 60

ax1.axis\["lat"\] \= axis \= ax1.new\_floating\_axis(0, 60)
axis.label.set\_text(r"$\\theta = 60^{\\circ}$")
axis.label.set\_visible(True)

See the first example of this page.

Current limitations and TODO's[#](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#current-limitations-and-todo-s "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

The code need more refinement. Here is an incomplete list of issues and TODO's

*   No easy way to support a user customized tick location (for curvilinear grid). A new Locator class needs to be created.
    
*   FloatingAxis may have coordinate limits, e.g., a floating axis of x = 0, but y only spans from 0 to 1.
    
*   The location of axislabel of FloatingAxis needs to be optionally given as a coordinate value. ex, a floating axis of x=0 with label at y=1
    

On this page