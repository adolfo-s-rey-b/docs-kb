[Skip to main content](https://matplotlib.org/stable/tutorials/artists.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/tutorials/artists.html#sphx-glr-download-tutorials-artists-py)
 to download the full example code.

Artist tutorial[#](https://matplotlib.org/stable/tutorials/artists.html#artist-tutorial "Link to this heading")

================================================================================================================

Using Artist objects to render on the canvas.

There are three layers to the Matplotlib API.

*   the `matplotlib.backend_bases.FigureCanvas` is the area onto which the figure is drawn
    
*   the `matplotlib.backend_bases.Renderer` is the object which knows how to draw on the `matplotlib.backend_bases.FigureCanvas`
    
*   and the [`matplotlib.artist.Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
     is the object that knows how to use a renderer to paint onto the canvas.
    

The `matplotlib.backend_bases.FigureCanvas` and `matplotlib.backend_bases.Renderer` handle all the details of talking to user interface toolkits like [wxPython](https://www.wxpython.org/)
 or drawing languages like PostScript®, and the `Artist` handles all the high level constructs like representing and laying out the figure, text, and lines. The typical user will spend 95% of their time working with the `Artists`.

There are two types of `Artists`: primitives and containers. The primitives represent the standard graphical objects we want to paint onto our canvas: [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
, [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
, [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, etc., and the containers are places to put them ([`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
, [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 and [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
). The standard use is to create a [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 instance, use the `Figure` to create one or more [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 instances, and use the `Axes` instance helper methods to create the primitives. In the example below, we create a `Figure` instance using [`matplotlib.pyplot.figure()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
, which is a convenience method for instantiating `Figure` instances and connecting them with a GUI framework so that they can be shown in a window on the screen:

import matplotlib.pyplot as plt
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
ax \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(2, 1, 1) \# two rows, one column, first plot

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 is probably the most important class in the Matplotlib API, and the one you will be working with most of the time. This is because the `Axes` is the plotting area into which most of the objects go, and the `Axes` has many special helper methods ([`plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
, [`text()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
, [`hist()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
, [`imshow()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
) to create the most common graphics primitives ([`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
, [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
, [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, respectively). These helper methods will take your data (e.g., `numpy` arrays and strings) and create primitive `Artist` instances as needed (e.g., `Line2D`), add them to the relevant containers, and draw them when requested. If you want to create an `Axes` at an arbitrary location, simply use the [`add_axes()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
 method which takes a list of `[left, bottom, width, height]` values in 0-1 relative figure coordinates:

fig2 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= fig2.add\_axes((0.15, 0.1, 0.7, 0.3))

Continuing with our example:

import numpy as np
[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 1.0, 0.01)
[s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= ax.plot([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\='blue', lw\=2)

In this example, `ax` is the `Axes` instance created by the `fig.add_subplot` call above and when you call `ax.plot`, it creates a `Line2D` instance and adds it to the `Axes`. In the interactive [IPython](https://ipython.org/)
 session below, you can see that the `Axes.lines` list is length one and contains the same line that was returned by the `line, = ax.plot...` call:

In \[101\]: ax.lines\[0\]
Out\[101\]: <matplotlib.lines.Line2D at 0x19a95710>

In \[102\]: [line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
Out\[102\]: <matplotlib.lines.Line2D at 0x19a95710>

If you make subsequent calls to `ax.plot` then additional lines will be added to the list. You can remove a line later by calling its `remove` method:

[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 \= ax.lines\[0\]
[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
.remove()

The Axes also has helper methods to configure and decorate the x-axis and y-axis tick, tick labels and axis labels:

xtext \= ax.set\_xlabel('my xdata')  \# returns a Text instance
ytext \= ax.set\_ylabel('my ydata')

When you call [`ax.set_xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
, it passes the information on the [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 instance of the [`XAxis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.XAxis "matplotlib.axis.XAxis")
. Each `Axes` instance contains an [`XAxis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.XAxis "matplotlib.axis.XAxis")
 and a [`YAxis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.YAxis "matplotlib.axis.YAxis")
 instance, which handle the layout and drawing of the ticks, tick labels and axis labels.

Try creating the figure below.

import matplotlib.pyplot as plt
import numpy as np

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(top\=0.8)
[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(211)
[ax1.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('Voltage \[V\]')
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('A sine wave')

[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 1.0, 0.01)
[s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\='blue', lw\=2)

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0.15, 0.1, 0.7, 0.3))
[n](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [patches](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
 \= [ax2.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
([np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(1000), 50,
                            facecolor\='yellow', edgecolor\='yellow')
[ax2.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('Time \[s\]')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![A sine wave](https://matplotlib.org/stable/_images/sphx_glr_artists_001_2_00x.png)

Customizing your objects[#](https://matplotlib.org/stable/tutorials/artists.html#customizing-your-objects "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

Every element in the figure is represented by a Matplotlib [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
, and each has an extensive list of properties to configure its appearance. The figure itself contains a [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 exactly the size of the figure, which you can use to set the background color and transparency of the figures. Likewise, each [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 bounding box (the standard white box with black edges in the typical Matplotlib plot, has a `Rectangle` instance that determines the color, transparency, and other properties of the Axes. These instances are stored as member variables `Figure.patch` and `Axes.patch` ("Patch" is a name inherited from MATLAB, and is a 2D "patch" of color on the figure, e.g., rectangles, circles and polygons). Every Matplotlib `Artist` has the following properties

| Property | Description |
| --- | --- |
| alpha | The transparency - a scalar from 0-1 |
| animated | A boolean that is used to facilitate animated drawing |
| axes | The Axes that the Artist lives in, possibly None |
| clip\_box | The bounding box that clips the Artist |
| clip\_on | Whether clipping is enabled |
| clip\_path | The path the artist is clipped to |
| contains | A picking function to test whether the artist contains the pick point |
| figure | The figure instance the artist lives in, possibly None |
| label | A text label (e.g., for auto-labeling) |
| picker | A python object that controls object picking |
| transform | The transformation |
| visible | A boolean whether the artist should be drawn |
| zorder | A number which determines the drawing order |
| rasterized | Boolean; Turns vectors into raster graphics (for compression & EPS transparency) |

Each of the properties is accessed with an old-fashioned setter or getter (yes we know this irritates Pythonistas and we plan to support direct access via properties or traits but it hasn't been done yet). For example, to multiply the current alpha by a half:

a \= o.get\_alpha()
o.set\_alpha(0.5\*a)

If you want to set a number of properties at once, you can also use the `set` method with keyword arguments. For example:

o.set(alpha\=0.5, zorder\=2)

If you are working interactively at the python shell, a handy way to inspect the `Artist` properties is to use the [`matplotlib.artist.getp()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.getp.html#matplotlib.artist.getp "matplotlib.artist.getp")
 function (simply [`getp()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.getp.html#matplotlib.pyplot.getp "matplotlib.pyplot.getp")
 in pyplot), which lists the properties and their values. This works for classes derived from `Artist` as well, e.g., `Figure` and `Rectangle`. Here are the `Figure` rectangle properties mentioned above:

In \[149\]: matplotlib.artist.getp([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
.patch)
  agg\_filter = None
  alpha = None
  animated = False
  antialiased or aa = False
  bbox = Bbox(x0=0.0, y0=0.0, x1=1.0, y1=1.0)
  capstyle = butt
  children = \[\]
  clip\_box = None
  clip\_on = True
  clip\_path = None
  contains = None
  data\_transform = BboxTransformTo(     TransformedBbox(         Bbox...
  edgecolor or ec = (1.0, 1.0, 1.0, 1.0)
  extents = Bbox(x0=0.0, y0=0.0, x1=640.0, y1=480.0)
  facecolor or fc = (1.0, 1.0, 1.0, 1.0)
  figure = Figure(640x480)
  fill = True
  gid = None
  hatch = None
  height = 1
  in\_layout = False
  joinstyle = miter
  label =
  linestyle or ls = solid
  linewidth or lw = 0.0
  patch\_transform = CompositeGenericTransform(     BboxTransformTo(   ...
  path = Path(array(\[\[0., 0.\],        \[1., 0.\],        \[1.,...\
  path\_effects = \[\]\
  picker = None\
  rasterized = None\
  sketch\_params = None\
  snap = None\
  transform = CompositeGenericTransform(     CompositeGenericTra...\
  transformed\_clip\_path\_and\_affine = (None, None)\
  url = None\
  verts = \[\[  0.   0.\]  \[640.   0.\]  \[640. 480.\]  \[  0. 480....\
  visible = True\
  width = 1\
  window\_extent = Bbox(x0=0.0, y0=0.0, x1=640.0, y1=480.0)\
  x = 0\
  xy = (0, 0)\
  y = 0\
  zorder = 1\
\
The docstrings for all of the classes also contain the `Artist` properties, so you can consult the interactive "help" or the [matplotlib.artist](https://matplotlib.org/stable/api/artist_api.html#artist-api)\
 for a listing of properties for a given object.\
\
Object containers[#](https://matplotlib.org/stable/tutorials/artists.html#object-containers "Link to this heading")\
\
--------------------------------------------------------------------------------------------------------------------\
\
Now that we know how to inspect and set the properties of a given object we want to configure, we need to know how to get at that object. As mentioned in the introduction, there are two kinds of objects: primitives and containers. The primitives are usually the things you want to configure (the font of a [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
 instance, the width of a [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
) although the containers also have some properties as well -- for example the [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
 [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")\
 is a container that contains many of the primitives in your plot, but it also has properties like the `xscale` to control whether the xaxis is 'linear' or 'log'. In this section we'll review where the various container objects store the `Artists` that you want to get at.\
\
### Figure container[#](https://matplotlib.org/stable/tutorials/artists.html#figure-container "Link to this heading")\
\
The top level container `Artist` is the [`matplotlib.figure.Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, and it contains everything in the figure. The background of the figure is a [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")\
 which is stored in `Figure.patch`. As you add subplots ([`add_subplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")\
) and Axes ([`add_axes()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")\
) to the figure these will be appended to the [`Figure.axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.axes.html#matplotlib.figure.Figure.axes "matplotlib.figure.Figure.axes")\
. These are also returned by the methods that create them:\
\
In \[156\]: [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")\
()\
\
In \[157\]: [ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")\
(211)\
\
In \[158\]: [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")\
((0.1, 0.1, 0.7, 0.3))\
\
In \[159\]: [ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
Out\[159\]: <Axes:>\
\
In \[160\]: print([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
.axes)\
\[<Axes: >, <Axes: >\]\
\
Because the figure maintains the concept of the "current Axes" (see [`Figure.gca`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.gca.html#matplotlib.figure.Figure.gca "matplotlib.figure.Figure.gca")\
 and [`Figure.sca`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.sca.html#matplotlib.figure.Figure.sca "matplotlib.figure.Figure.sca")\
) to support the pylab/pyplot state machine, you should not insert or remove Axes directly from the Axes list, but rather use the [`add_subplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")\
 and [`add_axes()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")\
 methods to insert, and the [`Axes.remove`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.remove.html#matplotlib.artist.Artist.remove "matplotlib.artist.Artist.remove")\
 method to delete. You are free however, to iterate over the list of Axes or index into it to get access to `Axes` instances you want to customize. Here is an example which turns all the Axes grids on:\
\
for ax in [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
.axes:\
    ax.grid(True)\
\
The figure also has its own `images`, `lines`, `patches` and `text` attributes, which you can use to add primitives directly. When doing so, the default coordinate system for the `Figure` will simply be in pixels (which is not usually what you want). If you instead use Figure-level methods to add Artists (e.g., using [`Figure.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")\
 to add text), then the default coordinate system will be "figure coordinates" where (0, 0) is the bottom-left of the figure and (1, 1) is the top-right of the figure.\
\
As with all `Artist`s, you can control this coordinate system by setting the transform property. You can explicitly use "figure coordinates" by setting the `Artist` transform to `fig.transFigure`:\
\
import matplotlib.lines as lines\
\
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")\
()\
\
[l1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
 \= [lines.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
(\[0, 1\], \[0, 1\], transform\=[fig.transFigure](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")\
, figure\=[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
)\
[l2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
 \= [lines.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
(\[0, 1\], \[1, 0\], transform\=[fig.transFigure](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")\
, figure\=[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
)\
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
.lines.extend(\[[l1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
, [l2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
\])\
\
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")\
()\
\
![artists](https://matplotlib.org/stable/_images/sphx_glr_artists_002_2_00x.png)\
\
Here is a summary of the Artists the Figure contains\
\
| Figure attribute | Description |\
| --- | --- |\
| axes | A list of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")<br> instances |\
| patch | The [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")<br> background |\
| images | A list of [`FigureImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.FigureImage "matplotlib.image.FigureImage")<br> patches - useful for raw pixel display |\
| legends | A list of Figure [`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")<br> instances (different from `Axes.get_legend()`) |\
| lines | A list of Figure [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")<br> instances (rarely used, see `Axes.lines`) |\
| patches | A list of Figure [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")<br>s (rarely used, see `Axes.patches`) |\
| texts | A list Figure [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")<br> instances |\
\
### Axes container[#](https://matplotlib.org/stable/tutorials/artists.html#axes-container "Link to this heading")\
\
The [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
 is the center of the Matplotlib universe -- it contains the vast majority of all the `Artists` used in a figure with many helper methods to create and add these `Artists` to itself, as well as helper methods to access and customize the `Artists` it contains. Like the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, it contains a [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")\
 `matplotlib.axes.Axes.patch` which is a [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")\
 for Cartesian coordinates and a [`Circle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")\
 for polar coordinates; this patch determines the shape, background and border of the plotting region:\
\
ax \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")\
()\
rect \= ax.patch  \# a Rectangle instance\
rect.set\_facecolor('green')\
\
When you call a plotting method, e.g., the canonical [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")\
 and pass in arrays or lists of values, the method will create a [`matplotlib.lines.Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
 instance, update the line with all the `Line2D` properties passed as keyword arguments, add the line to the `Axes`, and return it to you:\
\
In \[213\]: x, y \= np.random.rand(2, 100)\
\
In \[214\]: [line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
, \= ax.plot(x, y, '-', color\='blue', linewidth\=2)\
\
`plot` returns a list of lines because you can pass in multiple x, y pairs to plot, and we are unpacking the first element of the length one list into the line variable. The line has been added to the `Axes.lines` list:\
\
In \[229\]: print(ax.lines)\
\[<matplotlib.lines.Line2D at 0xd378b0c>\]\
\
Similarly, methods that create patches, like [`bar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")\
 creates a list of rectangles, will add the patches to the `Axes.patches` list:\
\
In \[233\]: [n](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, rectangles \= ax.hist([np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")\
(1000), 50)\
\
In \[234\]: rectangles\
Out\[234\]: <BarContainer object of 50 artists>\
\
In \[235\]: print(len(ax.[patches](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")\
))\
Out\[235\]: 50\
\
You should not add objects directly to the `Axes.lines` or `Axes.patches` lists, because the `Axes` needs to do a few things when it creates and adds an object:\
\
*   It sets the `figure` and `axes` property of the `Artist`;\
    \
*   It sets the default `Axes` transformation (unless one is already set);\
    \
*   It inspects the data contained in the `Artist` to update the data structures controlling auto-scaling, so that the view limits can be adjusted to contain the plotted data.\
    \
\
You can, nonetheless, create objects yourself and add them directly to the `Axes` using helper methods like [`add_line`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_line.html#matplotlib.axes.Axes.add_line "matplotlib.axes.Axes.add_line")\
 and [`add_patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")\
. Here is an annotated interactive session illustrating what is going on:\
\
In \[262\]: [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, ax \= plt.subplots()\
\
\# create a rectangle instance\
In \[263\]: rect \= matplotlib.[patches](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")\
.Rectangle((1, 1), width\=5, height\=12)\
\
\# by default the Axes instance is None\
In \[264\]: print(rect.axes)\
None\
\
\# and the transformation instance is set to the "identity transform"\
In \[265\]: print(rect.get\_data\_transform())\
IdentityTransform()\
\
\# now we add the Rectangle to the Axes\
In \[266\]: ax.add\_patch(rect)\
\
\# and notice that the ax.add\_patch method has set the Axes\
\# instance\
In \[267\]: print(rect.axes)\
Axes(0.125,0.1;0.775x0.8)\
\
\# and the transformation has been set too\
In \[268\]: print(rect.get\_data\_transform())\
CompositeGenericTransform(\
    TransformWrapper(\
        BlendedAffine2D(\
            IdentityTransform(),\
            IdentityTransform())),\
    CompositeGenericTransform(\
        BboxTransformFrom(\
            TransformedBbox(\
                Bbox(x0=0.0, y0=0.0, x1=1.0, y1=1.0),\
                TransformWrapper(\
                    BlendedAffine2D(\
                        IdentityTransform(),\
                        IdentityTransform())))),\
        BboxTransformTo(\
            TransformedBbox(\
                Bbox(x0=0.125, y0=0.10999999999999999, x1=0.9, y1=0.88),\
                BboxTransformTo(\
                    TransformedBbox(\
                        Bbox(x0=0.0, y0=0.0, x1=6.4, y1=4.8),\
                        Affine2D(\
                            \[\[100.   0.   0.\]\
                             \[  0. 100.   0.\]\
                             \[  0.   0.   1.\]\])))))))\
\
\# the default Axes transformation is ax.transData\
In \[269\]: print(ax.transData)\
CompositeGenericTransform(\
    TransformWrapper(\
        BlendedAffine2D(\
            IdentityTransform(),\
            IdentityTransform())),\
    CompositeGenericTransform(\
        BboxTransformFrom(\
            TransformedBbox(\
                Bbox(x0=0.0, y0=0.0, x1=1.0, y1=1.0),\
                TransformWrapper(\
                    BlendedAffine2D(\
                        IdentityTransform(),\
                        IdentityTransform())))),\
        BboxTransformTo(\
            TransformedBbox(\
                Bbox(x0=0.125, y0=0.10999999999999999, x1=0.9, y1=0.88),\
                BboxTransformTo(\
                    TransformedBbox(\
                        Bbox(x0=0.0, y0=0.0, x1=6.4, y1=4.8),\
                        Affine2D(\
                            \[\[100.   0.   0.\]\
                             \[  0. 100.   0.\]\
                             \[  0.   0.   1.\]\])))))))\
\
\# notice that the xlimits of the Axes have not been changed\
In \[270\]: print(ax.get\_xlim())\
(0.0, 1.0)\
\
\# but the data limits have been updated to encompass the rectangle\
In \[271\]: print(ax.dataLim.bounds)\
(1.0, 1.0, 5.0, 12.0)\
\
\# we can manually invoke the auto-scaling machinery\
In \[272\]: ax.autoscale\_view()\
\
\# and now the xlim are updated to encompass the rectangle, plus margins\
In \[273\]: print(ax.get\_xlim())\
(0.75, 6.25)\
\
\# we have to manually force a figure draw\
In \[274\]: [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
.canvas.draw()\
\
There are many, many `Axes` helper methods for creating primitive `Artists` and adding them to their respective containers. The table below summarizes a small sampling of them, the kinds of `Artist` they create, and where they store them\
\
| Axes helper method | Artist | Container |\
| --- | --- | --- |\
| [`annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")<br> - text annotations | [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation") | ax.texts |\
| [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")<br> - bar charts | [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle") | ax.patches |\
| [`errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")<br> - error bar plots | [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")<br> and [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle") | ax.lines and ax.patches |\
| [`fill`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill.html#matplotlib.axes.Axes.fill "matplotlib.axes.Axes.fill")<br> - shared area | [`Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon") | ax.patches |\
| [`hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")<br> - histograms | [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle") | ax.patches |\
| [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")<br> - image data | [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage") | ax.images |\
| [`legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")<br> - Axes legend | [`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend") | ax.get\_legend() |\
| [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")<br> - xy plots | [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D") | ax.lines |\
| [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")<br> - scatter charts | [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection") | ax.collections |\
| [`text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")<br> - text | [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text") | ax.texts |\
\
In addition to all of these `Artists`, the `Axes` contains two important `Artist` containers: the [`XAxis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.XAxis "matplotlib.axis.XAxis")\
 and [`YAxis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.YAxis "matplotlib.axis.YAxis")\
, which handle the drawing of the ticks and labels. These are stored as instance variables `matplotlib.axes.Axes.xaxis` and `matplotlib.axes.Axes.yaxis`. The `XAxis` and `YAxis` containers will be detailed below, but note that the `Axes` contains many helper methods which forward calls on to the [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")\
 instances, so you often do not need to work with them directly unless you want to. For example, you can set the font color of the `XAxis` ticklabels using the `Axes` helper method:\
\
ax.tick\_params(axis\='x', labelcolor\='orange')\
\
Below is a summary of the Artists that the [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
 contains\
\
| Axes attribute | Description |\
| --- | --- |\
| artists | An [`ArtistList`](https://matplotlib.org/stable/api/axes_api.html#matplotlib.axes.Axes.ArtistList "matplotlib.axes.Axes.ArtistList")<br> of [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")<br> instances |\
| patch | [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")<br> instance for Axes background |\
| collections | An [`ArtistList`](https://matplotlib.org/stable/api/axes_api.html#matplotlib.axes.Axes.ArtistList "matplotlib.axes.Axes.ArtistList")<br> of [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")<br> instances |\
| images | An [`ArtistList`](https://matplotlib.org/stable/api/axes_api.html#matplotlib.axes.Axes.ArtistList "matplotlib.axes.Axes.ArtistList")<br> of [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage") |\
| lines | An [`ArtistList`](https://matplotlib.org/stable/api/axes_api.html#matplotlib.axes.Axes.ArtistList "matplotlib.axes.Axes.ArtistList")<br> of [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")<br> instances |\
| patches | An [`ArtistList`](https://matplotlib.org/stable/api/axes_api.html#matplotlib.axes.Axes.ArtistList "matplotlib.axes.Axes.ArtistList")<br> of [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")<br> instances |\
| texts | An [`ArtistList`](https://matplotlib.org/stable/api/axes_api.html#matplotlib.axes.Axes.ArtistList "matplotlib.axes.Axes.ArtistList")<br> of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")<br> instances |\
| xaxis | A [`matplotlib.axis.XAxis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.XAxis "matplotlib.axis.XAxis")<br> instance |\
| yaxis | A [`matplotlib.axis.YAxis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.YAxis "matplotlib.axis.YAxis")<br> instance |\
\
The legend can be accessed by [`get_legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_legend.html#matplotlib.axes.Axes.get_legend "matplotlib.axes.Axes.get_legend")\
,\
\
### Axis containers[#](https://matplotlib.org/stable/tutorials/artists.html#axis-containers "Link to this heading")\
\
The [`matplotlib.axis.Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")\
 instances handle the drawing of the tick lines, the grid lines, the tick labels and the axis label. You can configure the left and right ticks separately for the y-axis, and the upper and lower ticks separately for the x-axis. The `Axis` also stores the data and view intervals used in auto-scaling, panning and zooming, as well as the [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")\
 and [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")\
 instances which control where the ticks are placed and how they are represented as strings.\
\
Each `Axis` object contains a [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.label.html#matplotlib.axis.Axis.label "matplotlib.axis.Axis.label")\
 attribute (this is what [`set_xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")\
 / [`set_ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")\
 modifies internally) as well as a list of major and minor ticks. The ticks are [`axis.XTick`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.XTick "matplotlib.axis.XTick")\
 and [`axis.YTick`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.YTick "matplotlib.axis.YTick")\
 instances, which contain the actual line and text primitives that render the ticks and ticklabels. Because the ticks are dynamically created and modified as needed (e.g., when panning and zooming), directly working on the ticks and their parts (tick lines, tick labels, grid lines) is discouraged. Instead, the high-level concepts tick locators, tick formatters and style configuration via [`tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")\
 should be used. See [Axis ticks](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html#user-axes-ticks)\
 for details.\
\
Here is a summary of some of the useful accessor methods of the `Axis` (these have corresponding setters where useful, such as [`set_major_formatter()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")\
.)\
\
| Axis accessor method | Description |\
| --- | --- |\
| [`get_scale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_scale.html#matplotlib.axis.Axis.get_scale "matplotlib.axis.Axis.get_scale") | The scale of the Axis, e.g., 'log' or 'linear' |\
| [`get_view_interval`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_view_interval.html#matplotlib.axis.Axis.get_view_interval "matplotlib.axis.Axis.get_view_interval") | The interval instance of the Axis view limits |\
| [`get_data_interval`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_data_interval.html#matplotlib.axis.Axis.get_data_interval "matplotlib.axis.Axis.get_data_interval") | The interval instance of the Axis data limits |\
| [`get_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_label.html#matplotlib.axis.Axis.get_label "matplotlib.axis.Axis.get_label") | The Axis label - a [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")<br> instance |\
| [`get_major_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_major_locator.html#matplotlib.axis.Axis.get_major_locator "matplotlib.axis.Axis.get_major_locator") | The [`ticker.Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")<br> instance for major ticks |\
| [`get_major_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_major_formatter.html#matplotlib.axis.Axis.get_major_formatter "matplotlib.axis.Axis.get_major_formatter") | The [`ticker.Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")<br> instance for major ticks |\
| [`get_minor_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_minor_locator.html#matplotlib.axis.Axis.get_minor_locator "matplotlib.axis.Axis.get_minor_locator") | The [`ticker.Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")<br> instance for minor ticks |\
| [`get_minor_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_minor_formatter.html#matplotlib.axis.Axis.get_minor_formatter "matplotlib.axis.Axis.get_minor_formatter") | The [`ticker.Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")<br> instance for minor ticks |\
| [`get_tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_tick_params.html#matplotlib.axis.Axis.get_tick_params "matplotlib.axis.Axis.get_tick_params") | Styling of ticks, ticklabels and gridlines |\
| [`grid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.grid.html#matplotlib.axis.Axis.grid "matplotlib.axis.Axis.grid") | Turn the grid on or off for the major or minor ticks |\
\
The full Axis API can be found at [matplotlib.axis](https://matplotlib.org/stable/api/axis_api.html)\
.\
\
[`Download Jupyter notebook: artists.ipynb`](https://matplotlib.org/stable/_downloads/56bd96eb0622b01c5aa6181b709e5b07/artists.ipynb)\
\
[`Download Python source code: artists.py`](https://matplotlib.org/stable/_downloads/06c5ad24d3e2f8f5f8e4b4f328fcdf3f/artists.py)\
\
[`Download zipped: artists.zip`](https://matplotlib.org/stable/_downloads/b9606377da33a54f18aac7481dd532f6/artists.zip)\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
On this page