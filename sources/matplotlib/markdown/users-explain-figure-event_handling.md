[Skip to main content](https://matplotlib.org/stable/users/explain/figure/event_handling.html#main-content)

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
    

Event handling and picking[#](https://matplotlib.org/stable/users/explain/figure/event_handling.html#event-handling-and-picking "Link to this heading")

========================================================================================================================================================

Matplotlib works with a number of user interface toolkits (wxpython, tkinter, qt, gtk, and macOS) and in order to support features like interactive panning and zooming of figures, it is helpful to the developers to have an API for interacting with the figure via key presses and mouse movements that is "GUI neutral" so we don't have to repeat a lot of code across the different user interfaces. Although the event handling API is GUI neutral, it is based on the GTK model, which was the first user interface Matplotlib supported. The events that are triggered are also a bit richer vis-a-vis Matplotlib than standard GUI events, including information like which [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 the event occurred in. The events also understand the Matplotlib coordinate system, and report event locations in both pixel and data coordinates.

Event connections[#](https://matplotlib.org/stable/users/explain/figure/event_handling.html#event-connections "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

To receive events, you need to write a callback function and then connect your function to the event manager, which is part of the [`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")
. Here is a simple example that prints the location of the mouse click and which button was pressed:

fig, ax \= plt.subplots()
ax.plot(np.random.rand(10))

def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))

cid \= fig.canvas.mpl\_connect('button\_press\_event', onclick)

The [`FigureCanvasBase.mpl_connect`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "matplotlib.backend_bases.FigureCanvasBase.mpl_connect")
 method returns a connection id (an integer), which can be used to disconnect the callback via

fig.canvas.mpl\_disconnect(cid)

Note

The canvas retains only weak references to instance methods used as callbacks. Therefore, you need to retain a reference to instances owning such methods. Otherwise the instance will be garbage-collected and the callback will vanish.

This does not affect free functions used as callbacks.

Here are the events that you can connect to, the class instances that are sent back to you when the event occurs, and the event descriptions:

| Event name | Class | Description |
| --- | --- | --- |
| 'button\_press\_event' | [`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent") | mouse button is pressed |
| 'button\_release\_event' | [`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent") | mouse button is released |
| 'close\_event' | [`CloseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.CloseEvent "matplotlib.backend_bases.CloseEvent") | figure is closed |
| 'draw\_event' | [`DrawEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.DrawEvent "matplotlib.backend_bases.DrawEvent") | canvas has been drawn (but screen widget not updated yet) |
| 'key\_press\_event' | [`KeyEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.KeyEvent "matplotlib.backend_bases.KeyEvent") | key is pressed |
| 'key\_release\_event' | [`KeyEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.KeyEvent "matplotlib.backend_bases.KeyEvent") | key is released |
| 'motion\_notify\_event' | [`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent") | mouse moves |
| 'pick\_event' | [`PickEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.PickEvent "matplotlib.backend_bases.PickEvent") | artist in the canvas is selected |
| 'resize\_event' | [`ResizeEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.ResizeEvent "matplotlib.backend_bases.ResizeEvent") | figure canvas is resized |
| 'scroll\_event' | [`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent") | mouse scroll wheel is rolled |
| 'figure\_enter\_event' | [`LocationEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.LocationEvent "matplotlib.backend_bases.LocationEvent") | mouse enters a new figure |
| 'figure\_leave\_event' | [`LocationEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.LocationEvent "matplotlib.backend_bases.LocationEvent") | mouse leaves a figure |
| 'axes\_enter\_event' | [`LocationEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.LocationEvent "matplotlib.backend_bases.LocationEvent") | mouse enters a new axes |
| 'axes\_leave\_event' | [`LocationEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.LocationEvent "matplotlib.backend_bases.LocationEvent") | mouse leaves an axes |

Note

When connecting to 'key\_press\_event' and 'key\_release\_event' events, you may encounter inconsistencies between the different user interface toolkits that Matplotlib works with. This is due to inconsistencies/limitations of the user interface toolkit. The following table shows some basic examples of what you may expect to receive as key(s) (using a QWERTY keyboard layout) from the different user interface toolkits, where a comma separates different keys:

| Key(s) Pressed | Tkinter | Qt  | macosx | WebAgg | GTK | WxPython |
| --- | --- | --- | --- | --- | --- | --- |
| Shift+2 | shift, @ | shift, @ | shift, @ | shift, @ | shift, @ | shift, shift+2 |
| Shift+F1 | shift, shift+f1 | shift, shift+f1 | shift, shift+f1 | shift, shift+f1 | shift, shift+f1 | shift, shift+f1 |
| Shift | shift | shift | shift | shift | shift | shift |
| Control | control | control | control | control | control | control |
| Alt | alt | alt | alt | alt | alt | alt |
| AltGr | iso\_level3\_shift | _nothing_ |     | alt | iso\_level3\_shift | _nothing_ |
| CapsLock | caps\_lock | caps\_lock | caps\_lock | caps\_lock | caps\_lock | caps\_lock |
| CapsLock+a | caps\_lock, A | caps\_lock, a | caps\_lock, a | caps\_lock, A | caps\_lock, A | caps\_lock, a |
| a   | a   | a   | a   | a   | a   | a   |
| Shift+a | shift, A | shift, A | shift, A | shift, A | shift, A | shift, A |
| CapsLock+Shift+a | caps\_lock, shift, a | caps\_lock, shift, A | caps\_lock, shift, A | caps\_lock, shift, a | caps\_lock, shift, a | caps\_lock, shift, A |
| Ctrl+Shift+Alt | control, ctrl+shift, ctrl+meta | control, ctrl+shift, ctrl+meta | control, ctrl+shift, ctrl+alt+shift | control, ctrl+shift, ctrl+meta | control, ctrl+shift, ctrl+meta | control, ctrl+shift, ctrl+alt |
| Ctrl+Shift+a | control, ctrl+shift, ctrl+a | control, ctrl+shift, ctrl+A | control, ctrl+shift, ctrl+A | control, ctrl+shift, ctrl+A | control, ctrl+shift, ctrl+A | control, ctrl+shift, ctrl+A |
| F1  | f1  | f1  | f1  | f1  | f1  | f1  |
| Ctrl+F1 | control, ctrl+f1 | control, ctrl+f1 | control, _nothing_ | control, ctrl+f1 | control, ctrl+f1 | control, ctrl+f1 |

Matplotlib attaches some keypress callbacks by default for interactivity; they are documented in the [Navigation keyboard shortcuts](https://matplotlib.org/stable/users/explain/figure/interactive.html#key-event-handling)
 section.

Event attributes[#](https://matplotlib.org/stable/users/explain/figure/event_handling.html#event-attributes "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

All Matplotlib events inherit from the base class [`matplotlib.backend_bases.Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")
, which stores the attributes:

`name`

the event name

`canvas`

the FigureCanvas instance generating the event

`guiEvent`

the GUI event that triggered the Matplotlib event

The most common events that are the bread and butter of event handling are key press/release events and mouse press/release and movement events. The [`KeyEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.KeyEvent "matplotlib.backend_bases.KeyEvent")
 and [`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")
 classes that handle these events are both derived from the LocationEvent, which has the following attributes

`x`, `y`

mouse x and y position in pixels from left and bottom of canvas

`inaxes`

the [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 instance over which the mouse is, if any; else None

`xdata`, `ydata`

mouse x and y position in data coordinates, if the mouse is over an axes

Let's look a simple example of a canvas, where a simple line segment is created every time a mouse is pressed:

from matplotlib import pyplot as plt

class LineBuilder:
    def \_\_init\_\_(self, line):
        self.line \= line
        self.xs \= list(line.get\_xdata())
        self.ys \= list(line.get\_ydata())
        self.cid \= line.figure.canvas.mpl\_connect('button\_press\_event', self)

    def \_\_call\_\_(self, event):
        print('click', event)
        if event.inaxes != self.line.axes:
            return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set\_data(self.xs, self.ys)
        self.line.figure.canvas.draw()

fig, ax \= plt.subplots()
ax.set\_title('click to build line segments')
line, \= ax.plot(\[0\], \[0\])  \# empty line
linebuilder \= LineBuilder(line)

plt.show()

The [`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")
 that we just used is a [`LocationEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.LocationEvent "matplotlib.backend_bases.LocationEvent")
, so we have access to the data and pixel coordinates via `(event.x, event.y)` and `(event.xdata, event.ydata)`. In addition to the `LocationEvent` attributes, it also has:

`button`

the button pressed: None, [`MouseButton`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton "matplotlib.backend_bases.MouseButton")
, 'up', or 'down' (up and down are used for scroll events)

`key`

the key pressed: None, any character, 'shift', 'win', or 'control'

### Draggable rectangle exercise[#](https://matplotlib.org/stable/users/explain/figure/event_handling.html#draggable-rectangle-exercise "Link to this heading")

Write a draggable rectangle class that is initialized with a [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 instance but will move its `xy` location when dragged.

Hint: You will need to store the original `xy` location of the rectangle which is stored as `rect.xy` and connect to the press, motion and release mouse events. When the mouse is pressed, check to see if the click occurs over your rectangle (see `.Rectangle.contains`) and if it does, store the rectangle xy and the location of the mouse click in data coordinates. In the motion event callback, compute the deltax and deltay of the mouse movement, and add those deltas to the origin of the rectangle you stored, then redraw the figure. On the button release event, just reset all the button press data you stored as None.

Here is the solution:

import numpy as np
import matplotlib.pyplot as plt

class DraggableRectangle:
    def \_\_init\_\_(self, rect):
        self.rect \= rect
        self.press \= None

    def connect(self):
        """Connect to all the events we need."""
        self.cidpress \= self.rect.figure.canvas.mpl\_connect(
            'button\_press\_event', self.on\_press)
        self.cidrelease \= self.rect.figure.canvas.mpl\_connect(
            'button\_release\_event', self.on\_release)
        self.cidmotion \= self.rect.figure.canvas.mpl\_connect(
            'motion\_notify\_event', self.on\_motion)

    def on\_press(self, event):
        """Check whether mouse is over us; if so, store some data."""
        if event.inaxes != self.rect.axes:
            return
        contains, attrd \= self.rect.contains(event)
        if not contains:
            return
        print('event contains', self.rect.xy)
        self.press \= self.rect.xy, (event.xdata, event.ydata)

    def on\_motion(self, event):
        """Move the rectangle if the mouse is over us."""
        if self.press is None or event.inaxes != self.rect.axes:
            return
        (x0, y0), (xpress, ypress) \= self.press
        dx \= event.xdata \- xpress
        dy \= event.ydata \- ypress
        \# print(f'x0={x0}, xpress={xpress}, event.xdata={event.xdata}, '
        \#       f'dx={dx}, x0+dx={x0+dx}')
        self.rect.set\_x(x0+dx)
        self.rect.set\_y(y0+dy)

        self.rect.figure.canvas.draw()

    def on\_release(self, event):
        """Clear button press information."""
        self.press \= None
        self.rect.figure.canvas.draw()

    def disconnect(self):
        """Disconnect all callbacks."""
        self.rect.figure.canvas.mpl\_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl\_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl\_disconnect(self.cidmotion)

fig, ax \= plt.subplots()
rects \= ax.bar(range(10), 20\*np.random.rand(10))
drs \= \[\]
for rect in rects:
    dr \= DraggableRectangle(rect)
    dr.connect()
    drs.append(dr)

plt.show()

**Extra credit**: Use blitting to make the animated drawing faster and smoother.

Extra credit solution:

\# Draggable rectangle with blitting.
import numpy as np
import matplotlib.pyplot as plt

class DraggableRectangle:
    lock \= None  \# only one can be animated at a time

    def \_\_init\_\_(self, rect):
        self.rect \= rect
        self.press \= None
        self.background \= None

    def connect(self):
        """Connect to all the events we need."""
        self.cidpress \= self.rect.figure.canvas.mpl\_connect(
            'button\_press\_event', self.on\_press)
        self.cidrelease \= self.rect.figure.canvas.mpl\_connect(
            'button\_release\_event', self.on\_release)
        self.cidmotion \= self.rect.figure.canvas.mpl\_connect(
            'motion\_notify\_event', self.on\_motion)

    def on\_press(self, event):
        """Check whether mouse is over us; if so, store some data."""
        if (event.inaxes != self.rect.axes
                or DraggableRectangle.lock is not None):
            return
        contains, attrd \= self.rect.contains(event)
        if not contains:
            return
        print('event contains', self.rect.xy)
        self.press \= self.rect.xy, (event.xdata, event.ydata)
        DraggableRectangle.lock \= self

        \# draw everything but the selected rectangle and store the pixel buffer
        canvas \= self.rect.figure.canvas
        axes \= self.rect.axes
        self.rect.set\_animated(True)
        canvas.draw()
        self.background \= canvas.copy\_from\_bbox(self.rect.axes.bbox)

        \# now redraw just the rectangle
        axes.draw\_artist(self.rect)

        \# and blit just the redrawn area
        canvas.blit(axes.bbox)

    def on\_motion(self, event):
        """Move the rectangle if the mouse is over us."""
        if (event.inaxes != self.rect.axes
                or DraggableRectangle.lock is not self):
            return
        (x0, y0), (xpress, ypress) \= self.press
        dx \= event.xdata \- xpress
        dy \= event.ydata \- ypress
        self.rect.set\_x(x0+dx)
        self.rect.set\_y(y0+dy)

        canvas \= self.rect.figure.canvas
        axes \= self.rect.axes
        \# restore the background region
        canvas.restore\_region(self.background)

        \# redraw just the current rectangle
        axes.draw\_artist(self.rect)

        \# blit just the redrawn area
        canvas.blit(axes.bbox)

    def on\_release(self, event):
        """Clear button press information."""
        if DraggableRectangle.lock is not self:
            return

        self.press \= None
        DraggableRectangle.lock \= None

        \# turn off the rect animation property and reset the background
        self.rect.set\_animated(False)
        self.background \= None

        \# redraw the full figure
        self.rect.figure.canvas.draw()

    def disconnect(self):
        """Disconnect all callbacks."""
        self.rect.figure.canvas.mpl\_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl\_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl\_disconnect(self.cidmotion)

fig, ax \= plt.subplots()
rects \= ax.bar(range(10), 20\*np.random.rand(10))
drs \= \[\]
for rect in rects:
    dr \= DraggableRectangle(rect)
    dr.connect()
    drs.append(dr)

plt.show()

Mouse enter and leave[#](https://matplotlib.org/stable/users/explain/figure/event_handling.html#mouse-enter-and-leave "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

If you want to be notified when the mouse enters or leaves a figure or axes, you can connect to the figure/axes enter/leave events. Here is a simple example that changes the colors of the axes and figure background that the mouse is over:

"""
Illustrate the figure and axes enter and leave events by changing the
frame colors on enter and leave
"""
import matplotlib.pyplot as plt

def enter\_axes(event):
    print('enter\_axes', event.inaxes)
    event.inaxes.patch.set\_facecolor('yellow')
    event.canvas.draw()

def leave\_axes(event):
    print('leave\_axes', event.inaxes)
    event.inaxes.patch.set\_facecolor('white')
    event.canvas.draw()

def enter\_figure(event):
    print('enter\_figure', event.canvas.figure)
    event.canvas.figure.patch.set\_facecolor('red')
    event.canvas.draw()

def leave\_figure(event):
    print('leave\_figure', event.canvas.figure)
    event.canvas.figure.patch.set\_facecolor('grey')
    event.canvas.draw()

fig1, axs \= plt.subplots(2)
fig1.suptitle('mouse hover over figure or axes to trigger events')

fig1.canvas.mpl\_connect('figure\_enter\_event', enter\_figure)
fig1.canvas.mpl\_connect('figure\_leave\_event', leave\_figure)
fig1.canvas.mpl\_connect('axes\_enter\_event', enter\_axes)
fig1.canvas.mpl\_connect('axes\_leave\_event', leave\_axes)

fig2, axs \= plt.subplots(2)
fig2.suptitle('mouse hover over figure or axes to trigger events')

fig2.canvas.mpl\_connect('figure\_enter\_event', enter\_figure)
fig2.canvas.mpl\_connect('figure\_leave\_event', leave\_figure)
fig2.canvas.mpl\_connect('axes\_enter\_event', enter\_axes)
fig2.canvas.mpl\_connect('axes\_leave\_event', leave\_axes)

plt.show()

Object picking[#](https://matplotlib.org/stable/users/explain/figure/event_handling.html#object-picking "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

You can enable picking by setting the `picker` property of an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 (such as [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
, [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
, [`Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
, [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, etc.)

The `picker` property can be set using various types:

`None`

Picking is disabled for this artist (default).

`boolean`

If True, then picking will be enabled and the artist will fire a pick event if the mouse event is over the artist.

`callable`

If picker is a callable, it is a user supplied function which determines whether the artist is hit by the mouse event. The signature is `hit, props = picker(artist, mouseevent)` to determine the hit test. If the mouse event is over the artist, return `hit = True`; `props` is a dictionary of properties that become additional attributes on the [`PickEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.PickEvent "matplotlib.backend_bases.PickEvent")
.

The artist's `pickradius` property can additionally be set to a tolerance value in points (there are 72 points per inch) that determines how far the mouse can be and still trigger a mouse event.

After you have enabled an artist for picking by setting the `picker` property, you need to connect a handler to the figure canvas pick\_event to get pick callbacks on mouse press events. The handler typically looks like

def pick\_handler(event):
    mouseevent \= event.mouseevent
    artist \= event.artist
    \# now do something with this...

The [`PickEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.PickEvent "matplotlib.backend_bases.PickEvent")
 passed to your callback always has the following attributes:

`mouseevent`

The [`MouseEvent`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")
 that generate the pick event. See [event-attributes](https://matplotlib.org/stable/users/explain/figure/event_handling.html#event-attributes)
 for a list of useful attributes on the mouse event.

`artist`

The [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 that generated the pick event.

Additionally, certain artists like [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 and [`PatchCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection "matplotlib.collections.PatchCollection")
 may attach additional metadata, like the indices of the data that meet the picker criteria (e.g., all the points in the line that are within the specified `pickradius` tolerance).

### Simple picking example[#](https://matplotlib.org/stable/users/explain/figure/event_handling.html#simple-picking-example "Link to this heading")

In the example below, we enable picking on the line and set a pick radius tolerance in points. The `onpick` callback function will be called when the pick event it within the tolerance distance from the line, and has the indices of the data vertices that are within the pick distance tolerance. Our `onpick` callback function simply prints the data that are under the pick location. Different Matplotlib Artists can attach different data to the PickEvent. For example, `Line2D` attaches the ind property, which are the indices into the line data under the pick point. See `.Line2D.pick` for details on the `PickEvent` properties of the line.

import numpy as np
import matplotlib.pyplot as plt

fig, ax \= plt.subplots()
ax.set\_title('click on points')

line, \= ax.plot(np.random.rand(100), 'o',
                picker\=True, pickradius\=5)  \# 5 points tolerance

def onpick(event):
    thisline \= event.artist
    xdata \= thisline.get\_xdata()
    ydata \= thisline.get\_ydata()
    ind \= event.ind
    points \= tuple(zip(xdata\[ind\], ydata\[ind\]))
    print('onpick points:', points)

fig.canvas.mpl\_connect('pick\_event', onpick)

plt.show()

### Picking exercise[#](https://matplotlib.org/stable/users/explain/figure/event_handling.html#picking-exercise "Link to this heading")

Create a data set of 100 arrays of 1000 Gaussian random numbers and compute the sample mean and standard deviation of each of them (hint: NumPy arrays have a mean and std method) and make an xy marker plot of the 100 means vs. the 100 standard deviations. Connect the line created by the plot command to the pick event, and plot the original time series of the data that generated the clicked on points. If more than one point is within the tolerance of the clicked on point, you can use multiple subplots to plot the multiple time series.

Exercise solution:

"""
Compute the mean and stddev of 100 data sets and plot mean vs. stddev.
When you click on one of the (mean, stddev) points, plot the raw dataset
that generated that point.
"""

import numpy as np
import matplotlib.pyplot as plt

X \= np.random.rand(100, 1000)
xs \= np.mean(X, axis\=1)
ys \= np.std(X, axis\=1)

fig, ax \= plt.subplots()
ax.set\_title('click on point to plot time series')
line, \= ax.plot(xs, ys, 'o', picker\=True, pickradius\=5)  \# 5 points tolerance

def onpick(event):
    if event.artist != line:
        return
    n \= len(event.ind)
    if not n:
        return
    fig, axs \= plt.subplots(n, squeeze\=False)
    for dataind, ax in zip(event.ind, axs.flat):
        ax.plot(X\[dataind\])
        ax.text(0.05, 0.9,
                f"$\\\\mu$={xs\[dataind\]:1.3f}\\n$\\\\sigma$={ys\[dataind\]:1.3f}",
                transform\=ax.transAxes, verticalalignment\='top')
        ax.set\_ylim(\-0.5, 1.5)
    fig.show()
    return True

fig.canvas.mpl\_connect('pick\_event', onpick)
plt.show()

On this page