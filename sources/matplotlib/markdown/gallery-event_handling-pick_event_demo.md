[Skip to main content](https://matplotlib.org/stable/gallery/event_handling/pick_event_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/event_handling/pick_event_demo.html#sphx-glr-download-gallery-event-handling-pick-event-demo-py)
 to download the full example code.

Pick event demo[#](https://matplotlib.org/stable/gallery/event_handling/pick_event_demo.html#pick-event-demo "Link to this heading")

=====================================================================================================================================

You can enable picking by setting the "picker" property of an artist (for example, a Matplotlib Line2D, Text, Patch, Polygon, AxesImage, etc.)

There are a variety of meanings of the picker property:

*   _None_ - picking is disabled for this artist (default)
    
*   bool - if _True_ then picking will be enabled and the artist will fire a pick event if the mouse event is over the artist.
    
    Setting `pickradius` will add an epsilon tolerance in points and the artist will fire off an event if its data is within epsilon of the mouse event. For some artists like lines and patch collections, the artist may provide additional data to the pick event that is generated, for example, the indices of the data within epsilon of the pick event
    
*   function - if picker is callable, it is a user supplied function which determines whether the artist is hit by the mouse event.
    
    hit, props \= picker(artist, mouseevent)
    
    to determine the hit test. If the mouse event is over the artist, return hit=True and props is a dictionary of properties you want added to the PickEvent attributes.
    

After you have enabled an artist for picking by setting the "picker" property, you need to connect to the figure canvas pick\_event to get pick callbacks on mouse press events. For example,

def pick\_handler(event):
    mouseevent \= event.mouseevent
    artist \= event.artist
    \# now do something with this...

The pick event (matplotlib.backend\_bases.PickEvent) which is passed to your callback is always fired with two attributes:

mouseevent

the mouse event that generate the pick event.

The mouse event in turn has attributes like x and y (the coordinates in display space, such as pixels from left, bottom) and xdata, ydata (the coords in data space). Additionally, you can get information about which buttons were pressed, which keys were pressed, which Axes the mouse is over, etc. See matplotlib.backend\_bases.MouseEvent for details.

artist

the matplotlib.artist that generated the pick event.

Additionally, certain artists like Line2D and PatchCollection may attach additional metadata like the indices into the data that meet the picker criteria (for example, all the points in the line that are within the specified epsilon tolerance)

The examples below illustrate each of these methods.

Note

These examples exercises the interactive capabilities of Matplotlib, and this will not appear in the static documentation. Please run this code on your machine to see the interactivity.

You can copy and paste individual parts, or download the entire example using the link at the bottom of the page.

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import [rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")

from matplotlib.image import [AxesImage](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
from matplotlib.lines import [Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
from matplotlib.patches import [Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
from matplotlib.text import [Text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

Simple picking, lines, rectangles and text[#](https://matplotlib.org/stable/gallery/event_handling/pick_event_demo.html#simple-picking-lines-rectangles-and-text "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 1)
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('click on points, rectangles or text', picker\=True)
[ax1.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('ylabel', picker\=True, bbox\=dict(facecolor\='red'))
[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(100), 'o', picker\=True, pickradius\=5)

\# Pick the rectangle.
[ax2.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
(range(10), [rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(10), picker\=True)
for [label](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 in [ax2.get\_xticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticklabels.html#matplotlib.axes.Axes.get_xticklabels "matplotlib.axes.Axes.get_xticklabels")
():  \# Make the xtick labels pickable.
    [label.set\_picker](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker")
(True)

def onpick1(event):
    if isinstance(event.artist, [Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
):
        thisline \= event.artist
        xdata \= thisline.get\_xdata()
        ydata \= thisline.get\_ydata()
        ind \= event.ind
        print('onpick1 line:', [np.column\_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")
(\[xdata\[ind\], ydata\[ind\]\]))
    elif isinstance(event.artist, [Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
):
        patch \= event.artist
        print('onpick1 patch:', patch.get\_path())
    elif isinstance(event.artist, [Text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
):
        text \= event.artist
        print('onpick1 text:', text.get\_text())

[fig.canvas.mpl\_connect](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "matplotlib.backend_bases.FigureCanvasBase.mpl_connect")
('pick\_event', onpick1)

![click on points, rectangles or text](https://matplotlib.org/stable/_images/sphx_glr_pick_event_demo_001_2_00x.png)

Picking with a custom hit test function[#](https://matplotlib.org/stable/gallery/event_handling/pick_event_demo.html#picking-with-a-custom-hit-test-function "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can define custom pickers by setting picker to a callable function. The function has the signature:

hit, props \= func(artist, mouseevent)

to determine the hit test. If the mouse event is over the artist, return `hit=True` and `props` is a dictionary of properties you want added to the [`PickEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.PickEvent "matplotlib.backend_bases.PickEvent")
 attributes.

def line\_picker([line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, mouseevent):
    """
    Find the points within a certain distance from the mouseclick in
    data coords and attach some extra attributes, pickx and picky
    which are the data points that were picked.
    """
    if mouseevent.xdata is None:
        return False, dict()
    xdata \= [line.get\_xdata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_xdata "matplotlib.lines.Line2D.get_xdata")
()
    ydata \= [line.get\_ydata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_ydata "matplotlib.lines.Line2D.get_ydata")
()
    maxd \= 0.05
    d \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(
        (xdata \- mouseevent.xdata)\*\*2 + (ydata \- mouseevent.ydata)\*\*2)

    ind, \= [np.nonzero](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")
(d <= maxd)
    if len(ind):
        pickx \= xdata\[ind\]
        picky \= ydata\[ind\]
        props \= dict(ind\=ind, pickx\=pickx, picky\=picky)
        return True, props
    else:
        return False, dict()

def onpick2(event):
    print('onpick2 line:', event.pickx, event.picky)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('custom picker for line data')
[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(100), [rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(100), 'o', picker\=line\_picker)
[fig.canvas.mpl\_connect](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "matplotlib.backend_bases.FigureCanvasBase.mpl_connect")
('pick\_event', onpick2)

![custom picker for line data](https://matplotlib.org/stable/_images/sphx_glr_pick_event_demo_002_2_00x.png)

Picking on a scatter plot[#](https://matplotlib.org/stable/gallery/event_handling/pick_event_demo.html#picking-on-a-scatter-plot "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

A scatter plot is backed by a [`PathCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
.

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [c](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(4, 100)

def onpick3(event):
    ind \= event.ind
    print('onpick3 scatter:', ind, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[ind\], [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[ind\])

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 100\*[s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [c](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, picker\=True)
[fig.canvas.mpl\_connect](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "matplotlib.backend_bases.FigureCanvasBase.mpl_connect")
('pick\_event', onpick3)

![pick event demo](https://matplotlib.org/stable/_images/sphx_glr_pick_event_demo_003_2_00x.png)

Picking images[#](https://matplotlib.org/stable/gallery/event_handling/pick_event_demo.html#picking-images "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

Images plotted using [`Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 are [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 objects.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(10, 5), extent\=(1, 2, 1, 2), picker\=True)
[ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(5, 10), extent\=(3, 4, 1, 2), picker\=True)
[ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(20, 25), extent\=(1, 2, 3, 4), picker\=True)
[ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(30, 12), extent\=(3, 4, 3, 4), picker\=True)
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(0, 5), ylim\=(0, 5))

def onpick4(event):
    artist \= event.artist
    if isinstance(artist, [AxesImage](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
):
        im \= artist
        A \= im.get\_array()
        print('onpick4 image', A.shape)

[fig.canvas.mpl\_connect](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "matplotlib.backend_bases.FigureCanvasBase.mpl_connect")
('pick\_event', onpick4)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![pick event demo](https://matplotlib.org/stable/_images/sphx_glr_pick_event_demo_004_2_00x.png)

**Total running time of the script:** (0 minutes 1.653 seconds)

[`Download Jupyter notebook: pick_event_demo.ipynb`](https://matplotlib.org/stable/_downloads/fb7854f020c3c47549c6e1331492135c/pick_event_demo.ipynb)

[`Download Python source code: pick_event_demo.py`](https://matplotlib.org/stable/_downloads/97bcffbb1f60980e1ed023c1abf6b9f3/pick_event_demo.py)

[`Download zipped: pick_event_demo.zip`](https://matplotlib.org/stable/_downloads/47bb3a400978c10aa3ccc82b15ff8829/pick_event_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page