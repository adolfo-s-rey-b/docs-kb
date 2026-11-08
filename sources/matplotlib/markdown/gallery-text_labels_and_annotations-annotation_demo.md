[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_demo.html#main-content)

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
    

Note

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_demo.html#sphx-glr-download-gallery-text-labels-and-annotations-annotation-demo-py)
 to download the full example code.

Annotate plots[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_demo.html#annotate-plots "Link to this heading")

================================================================================================================================================

The following examples show ways to annotate plots in Matplotlib. This includes highlighting specific points of interest and using various visual tools to call attention to this point. For a more complete and in-depth description of the annotation and text tools in Matplotlib, see the [tutorial on annotation](https://matplotlib.org/stable/users/explain/text/annotations.html#annotations)
.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import [Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
from matplotlib.text import [OffsetFrom](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.OffsetFrom "matplotlib.text.OffsetFrom")

Specifying text points and annotation points[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_demo.html#specifying-text-points-and-annotation-points "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You must specify an annotation point `xy=(x, y)` to annotate this point. Additionally, you may specify a text point `xytext=(x, y)` for the location of the text for this annotation. Optionally, you can specify the coordinate system of _xy_ and _xytext_ with one of the following strings for _xycoords_ and _textcoords_ (default is 'data'):

'figure points'   : points from the lower left corner of the figure
'figure pixels'   : pixels from the lower left corner of the figure
'figure fraction' : (0, 0) is lower left of figure and (1, 1) is upper right
'axes points'     : points from lower left corner of the Axes
'axes pixels'     : pixels from lower left corner of the Axes
'axes fraction'   : (0, 0) is lower left of Axes and (1, 1) is upper right
'offset points'   : Specify an offset (in points) from the xy value
'offset pixels'   : Specify an offset (in pixels) from the xy value
'data'            : use the Axes data coordinate system

Note: for physical coordinate systems (points or pixels) the origin is the (bottom, left) of the figure or Axes.

Optionally, you can specify arrow properties which draws and arrow from the text to the annotated point by giving a dictionary of arrow properties

Valid keys are:

width : the width of the arrow in points
frac  : the fraction of the arrow length occupied by the head
headwidth : the width of the base of the arrow head in points
shrink : move the tip and base some percent away from the
         annotated point and [text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
any key for matplotlib.patches.polygon  (e.g., facecolor)

\# Create our figure and data we'll use for plotting
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(4, 4))

[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 5.0, 0.01)
[s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# Plot a line and add some simple annotations
[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('figure pixels',
            xy\=(10, 10), xycoords\='figure pixels')
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('figure points',
            xy\=(107, 110), xycoords\='figure points',
            fontsize\=12)
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('figure fraction',
            xy\=(.025, .975), xycoords\='figure fraction',
            horizontalalignment\='left', verticalalignment\='top',
            fontsize\=20)

\# The following examples show off how these arrows are drawn.

[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('point offset from data',
            xy\=(3, 1), xycoords\='data',
            xytext\=(\-10, 90), textcoords\='offset points',
            arrowprops\=dict(facecolor\='black', shrink\=0.05),
            horizontalalignment\='center', verticalalignment\='bottom')

[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('axes fraction',
            xy\=(2, 1), xycoords\='data',
            xytext\=(0.36, 0.68), textcoords\='axes fraction',
            arrowprops\=dict(facecolor\='black', shrink\=0.05),
            horizontalalignment\='right', verticalalignment\='top')

\# You may also use negative points or pixels to specify from (right, top).
\# E.g., (-10, 10) is 10 points to the left of the right side of the Axes and 10
\# points above the bottom

[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('pixel offset from axes fraction',
            xy\=(1, 0), xycoords\='axes fraction',
            xytext\=(\-20, 20), textcoords\='offset pixels',
            horizontalalignment\='right',
            verticalalignment\='bottom')

[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(\-1, 5), ylim\=(\-3, 5))

![annotation demo](https://matplotlib.org/stable/_images/sphx_glr_annotation_demo_001_2_00x.png)

Using multiple coordinate systems and axis types[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_demo.html#using-multiple-coordinate-systems-and-axis-types "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can specify the _xypoint_ and the _xytext_ in different positions and coordinate systems, and optionally turn on a connecting line and mark the point with a marker. Annotations work on polar Axes too.

In the example below, the _xy_ point is in native coordinates (_xycoords_ defaults to 'data'). For a polar Axes, this is in (theta, radius) space. The text in the example is placed in the fractional figure coordinate system. Text keyword arguments like horizontal and vertical alignment are respected.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(subplot\_kw\=dict(projection\='polar'), figsize\=(3, 3))
[r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 1, 0.001)
[theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 2\*2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[ind](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 800
[thisr](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [thistheta](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[ind](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], [theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[ind](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[[thistheta](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")\
\], \[[thisr](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")\
\], 'o')
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('a polar annotation',
            xy\=([thistheta](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [thisr](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
),  \# theta, radius
            xytext\=(0.05, 0.05),    \# fraction, fraction
            textcoords\='figure fraction',
            arrowprops\=dict(facecolor\='black', shrink\=0.05),
            horizontalalignment\='left',
            verticalalignment\='bottom')

![annotation demo](https://matplotlib.org/stable/_images/sphx_glr_annotation_demo_002_2_00x.png)

You can also use polar notation on a cartesian Axes. Here the native coordinate system ('data') is cartesian, so you need to specify the xycoords and textcoords as 'polar' if you want to use (theta, radius).

[el](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
 \= [Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
((0, 0), 10, 20, facecolor\='r', alpha\=0.5)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(subplot\_kw\=dict(aspect\='equal'))
[ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([el](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
)
[el.set\_clip\_box](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box")
([ax.bbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")
)
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('the top',
            xy\=([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
/2., 10.),      \# theta, radius
            xytext\=([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
/3, 20.),   \# theta, radius
            xycoords\='polar',
            textcoords\='polar',
            arrowprops\=dict(facecolor\='black', shrink\=0.05),
            horizontalalignment\='left',
            verticalalignment\='bottom',
            clip\_on\=True)  \# clip to the Axes bounding box

[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=\[\-20, 20\], ylim\=\[\-20, 20\])

![annotation demo](https://matplotlib.org/stable/_images/sphx_glr_annotation_demo_003_2_00x.png)

Customizing arrow and bubble styles[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_demo.html#customizing-arrow-and-bubble-styles "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The arrow between _xytext_ and the annotation point, as well as the bubble that covers the annotation text, are highly customizable. Below are a few parameter options as well as their resulting output.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(8, 5))

[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 5.0, 0.01)
[s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, lw\=3)

[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
(
    'straight',
    xy\=(0, 1), xycoords\='data',
    xytext\=(\-50, 30), textcoords\='offset points',
    arrowprops\=dict(arrowstyle\="->"))
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
(
    'arc3,\\nrad 0.2',
    xy\=(0.5, \-1), xycoords\='data',
    xytext\=(\-80, \-60), textcoords\='offset points',
    arrowprops\=dict(arrowstyle\="->",
                    connectionstyle\="arc3,rad=.2"))
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
(
    'arc,\\nangle 50',
    xy\=(1., 1), xycoords\='data',
    xytext\=(\-90, 50), textcoords\='offset points',
    arrowprops\=dict(arrowstyle\="->",
                    connectionstyle\="arc,angleA=0,armA=50,rad=10"))
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
(
    'arc,\\narms',
    xy\=(1.5, \-1), xycoords\='data',
    xytext\=(\-80, \-60), textcoords\='offset points',
    arrowprops\=dict(
        arrowstyle\="->",
        connectionstyle\="arc,angleA=0,armA=40,angleB=-90,armB=30,rad=7"))
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
(
    'angle,\\nangle 90',
    xy\=(2., 1), xycoords\='data',
    xytext\=(\-70, 30), textcoords\='offset points',
    arrowprops\=dict(arrowstyle\="->",
                    connectionstyle\="angle,angleA=0,angleB=90,rad=10"))
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
(
    'angle3,\\nangle -90',
    xy\=(2.5, \-1), xycoords\='data',
    xytext\=(\-80, \-60), textcoords\='offset points',
    arrowprops\=dict(arrowstyle\="->",
                    connectionstyle\="angle3,angleA=0,angleB=-90"))
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
(
    'angle,\\nround',
    xy\=(3., 1), xycoords\='data',
    xytext\=(\-60, 30), textcoords\='offset points',
    bbox\=dict(boxstyle\="round", fc\="0.8"),
    arrowprops\=dict(arrowstyle\="->",
                    connectionstyle\="angle,angleA=0,angleB=90,rad=10"))
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
(
    'angle,\\nround4',
    xy\=(3.5, \-1), xycoords\='data',
    xytext\=(\-70, \-80), textcoords\='offset points',
    size\=20,
    bbox\=dict(boxstyle\="round4,pad=.5", fc\="0.8"),
    arrowprops\=dict(arrowstyle\="->",
                    connectionstyle\="angle,angleA=0,angleB=-90,rad=10"))
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
(
    'angle,\\nshrink',
    xy\=(4., 1), xycoords\='data',
    xytext\=(\-60, 30), textcoords\='offset points',
    bbox\=dict(boxstyle\="round", fc\="0.8"),
    arrowprops\=dict(arrowstyle\="->",
                    shrinkA\=0, shrinkB\=10,
                    connectionstyle\="angle,angleA=0,angleB=90,rad=10"))
\# You can pass an empty string to get only annotation arrows rendered
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('', xy\=(4., 1.), xycoords\='data',
            xytext\=(4.5, \-1), textcoords\='data',
            arrowprops\=dict(arrowstyle\="<->",
                            connectionstyle\="bar",
                            ec\="k",
                            shrinkA\=5, shrinkB\=5))

[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(\-1, 5), ylim\=(\-4, 3))

![annotation demo](https://matplotlib.org/stable/_images/sphx_glr_annotation_demo_004_2_00x.png)

We'll create another figure so that it doesn't get too cluttered

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[el](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
 \= [Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
((2, \-1), 0.5, 0.5)
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([el](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
)

[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('$->$',
            xy\=(2., \-1), xycoords\='data',
            xytext\=(\-150, \-140), textcoords\='offset points',
            bbox\=dict(boxstyle\="round", fc\="0.8"),
            arrowprops\=dict(arrowstyle\="->",
                            patchB\=[el](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
,
                            connectionstyle\="angle,angleA=90,angleB=0,rad=10"))
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('arrow\\nfancy',
            xy\=(2., \-1), xycoords\='data',
            xytext\=(\-100, 60), textcoords\='offset points',
            size\=20,
            arrowprops\=dict(arrowstyle\="fancy",
                            fc\="0.6", ec\="none",
                            patchB\=[el](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
,
                            connectionstyle\="angle3,angleA=0,angleB=-90"))
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('arrow\\nsimple',
            xy\=(2., \-1), xycoords\='data',
            xytext\=(100, 60), textcoords\='offset points',
            size\=20,
            arrowprops\=dict(arrowstyle\="simple",
                            fc\="0.6", ec\="none",
                            patchB\=[el](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
,
                            connectionstyle\="arc3,rad=0.3"))
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('wedge',
            xy\=(2., \-1), xycoords\='data',
            xytext\=(\-100, \-100), textcoords\='offset points',
            size\=20,
            arrowprops\=dict(arrowstyle\="wedge,tail\_width=0.7",
                            fc\="0.6", ec\="none",
                            patchB\=[el](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
,
                            connectionstyle\="arc3,rad=-0.3"))
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('bubble,\\ncontours',
            xy\=(2., \-1), xycoords\='data',
            xytext\=(0, \-70), textcoords\='offset points',
            size\=20,
            bbox\=dict(boxstyle\="round",
                      fc\=(1.0, 0.7, 0.7),
                      ec\=(1., .5, .5)),
            arrowprops\=dict(arrowstyle\="wedge,tail\_width=1.",
                            fc\=(1.0, 0.7, 0.7), ec\=(1., .5, .5),
                            patchA\=None,
                            patchB\=[el](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
,
                            relpos\=(0.2, 0.8),
                            connectionstyle\="arc3,rad=-0.1"))
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('bubble',
            xy\=(2., \-1), xycoords\='data',
            xytext\=(55, 0), textcoords\='offset points',
            size\=20, va\="center",
            bbox\=dict(boxstyle\="round", fc\=(1.0, 0.7, 0.7), ec\="none"),
            arrowprops\=dict(arrowstyle\="wedge,tail\_width=1.",
                            fc\=(1.0, 0.7, 0.7), ec\="none",
                            patchA\=None,
                            patchB\=[el](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
,
                            relpos\=(0.2, 0.5)))

[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(\-1, 5), ylim\=(\-5, 3))

![annotation demo](https://matplotlib.org/stable/_images/sphx_glr_annotation_demo_005_2_00x.png)

More examples of coordinate systems[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_demo.html#more-examples-of-coordinate-systems "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Below we'll show a few more examples of coordinate systems and how the location of annotations may be specified.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2)

[bbox\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(boxstyle\="round", fc\="0.8")
[arrow\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(arrowstyle\="->")

\# Here we'll demonstrate the extents of the coordinate system and how
\# we place annotating text.

[ax1.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('figure fraction : 0, 0', xy\=(0, 0), xycoords\='figure fraction',
             xytext\=(20, 20), textcoords\='offset points',
             ha\="left", va\="bottom",
             bbox\=[bbox\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
,
             arrowprops\=[arrow\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

[ax1.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('figure fraction : 1, 1', xy\=(1, 1), xycoords\='figure fraction',
             xytext\=(\-20, \-20), textcoords\='offset points',
             ha\="right", va\="top",
             bbox\=[bbox\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
,
             arrowprops\=[arrow\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

[ax1.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('axes fraction : 0, 0', xy\=(0, 0), xycoords\='axes fraction',
             xytext\=(20, 20), textcoords\='offset points',
             ha\="left", va\="bottom",
             bbox\=[bbox\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
,
             arrowprops\=[arrow\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

[ax1.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('axes fraction : 1, 1', xy\=(1, 1), xycoords\='axes fraction',
             xytext\=(\-20, \-20), textcoords\='offset points',
             ha\="right", va\="top",
             bbox\=[bbox\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
,
             arrowprops\=[arrow\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

\# It is also possible to generate draggable annotations

[an1](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
 \= [ax1.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('Drag me 1', xy\=(.5, .7), xycoords\='data',
                   ha\="center", va\="center",
                   bbox\=[bbox\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

[an2](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
 \= [ax1.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('Drag me 2', xy\=(.5, .5), xycoords\=[an1](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
,
                   xytext\=(.5, .3), textcoords\='axes fraction',
                   ha\="center", va\="center",
                   bbox\=[bbox\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
,
                   arrowprops\=dict(patchB\=[an1.get\_bbox\_patch](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_bbox_patch "matplotlib.text.Text.get_bbox_patch")
(),
                                   connectionstyle\="arc3,rad=0.2",
                                   \*\*[arrow\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
))
[an1](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
.draggable()
[an2](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
.draggable()

[an3](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
 \= [ax1.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('', xy\=(.5, .5), xycoords\=[an2](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
,
                   xytext\=(.5, .5), textcoords\=[an1](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
,
                   ha\="center", va\="center",
                   bbox\=[bbox\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
,
                   arrowprops\=dict(patchA\=[an1.get\_bbox\_patch](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_bbox_patch "matplotlib.text.Text.get_bbox_patch")
(),
                                   patchB\=[an2.get\_bbox\_patch](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_bbox_patch "matplotlib.text.Text.get_bbox_patch")
(),
                                   connectionstyle\="arc3,rad=0.2",
                                   \*\*[arrow\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
))

\# Finally we'll show off some more complex annotation and placement

[text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
 \= [ax2.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('xy=(0, 1)\\nxycoords=("data", "axes fraction")',
                    xy\=(0, 1), xycoords\=("data", 'axes fraction'),
                    xytext\=(0, \-20), textcoords\='offset points',
                    ha\="center", va\="top",
                    bbox\=[bbox\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
,
                    arrowprops\=[arrow\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

[ax2.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('xy=(0.5, 0)\\nxycoords=artist',
             xy\=(0.5, 0.), xycoords\=[text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
,
             xytext\=(0, \-20), textcoords\='offset points',
             ha\="center", va\="top",
             bbox\=[bbox\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
,
             arrowprops\=[arrow\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

[ax2.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('xy=(0.8, 0.5)\\nxycoords=ax1.transData',
             xy\=(0.8, 0.5), xycoords\=[ax1.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
,
             xytext\=(10, 10),
             textcoords\=[OffsetFrom](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.OffsetFrom "matplotlib.text.OffsetFrom")
([ax2.bbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")
, (0, 0), "points"),
             ha\="left", va\="bottom",
             bbox\=[bbox\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
,
             arrowprops\=[arrow\_args](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

[ax2.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=\[\-2, 2\], ylim\=\[\-2, 2\])
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![annotation demo](https://matplotlib.org/stable/_images/sphx_glr_annotation_demo_006_2_00x.png)

**Total running time of the script:** (0 minutes 3.590 seconds)

[`Download Jupyter notebook: annotation_demo.ipynb`](https://matplotlib.org/stable/_downloads/b612fc5ce4b8f662c0ab4a08ad25f697/annotation_demo.ipynb)

[`Download Python source code: annotation_demo.py`](https://matplotlib.org/stable/_downloads/d9affd4778c6449c175e11db4270dc15/annotation_demo.py)

[`Download zipped: annotation_demo.zip`](https://matplotlib.org/stable/_downloads/3d9b64363d2db6b20ba234cf5b975bc8/annotation_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page