[Skip to main content](https://matplotlib.org/stable/users/explain/artists/artist_intro.html#main-content)

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
    

Introduction to Artists[#](https://matplotlib.org/stable/users/explain/artists/artist_intro.html#introduction-to-artists "Link to this heading")

=================================================================================================================================================

Almost all objects you interact with on a Matplotlib plot are called "Artist" (and are subclasses of the [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 class). [Figure](https://matplotlib.org/stable/users/explain/figure/index.html)
 and [Axes](https://matplotlib.org/stable/users/explain/axes/index.html)
 are Artists, and generally contain [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 Artists and Artists that contain data or annotation information.

Creating Artists[#](https://matplotlib.org/stable/users/explain/artists/artist_intro.html#creating-artists "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

Usually we do not instantiate Artists directly, but rather use a plotting method on [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
. Some examples of plotting methods and the Artist object they create is given below:

| Axes helper method | Artist |
| --- | --- |
| [`annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")<br> - text annotations | [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation") |
| [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")<br> - bar charts | [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle") |
| [`errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")<br> - error bar plots | [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")<br> and [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle") |
| [`fill`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill.html#matplotlib.axes.Axes.fill "matplotlib.axes.Axes.fill")<br> - shared area | [`Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon") |
| [`hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")<br> - histograms | [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle") |
| [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")<br> - image data | [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage") |
| [`legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")<br> - Axes legend | [`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend") |
| [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")<br> - xy plots | [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D") |
| [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")<br> - scatter charts | [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection") |
| [`text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")<br> - text | [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text") |

As an example, we can save the Line2D Artist returned from [`axes.Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
:

In \[209\]: import matplotlib.pyplot as plt
In \[210\]: import matplotlib.artist as martist
In \[211\]: import numpy as np

In \[212\]: fig, ax \= plt.subplots()
In \[213\]: x, y \= np.random.rand(2, 100)
In \[214\]: lines \= ax.plot(x, y, '-', label\='example')
In \[215\]: print(lines)
\[<matplotlib.lines.Line2D at 0xd378b0c>\]

Note that `plot` returns a \_list\_ of lines because you can pass in multiple x, y pairs to plot. The line has been added to the Axes, and we can retrieve the Artist via [`get_lines()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_lines.html#matplotlib.axes.Axes.get_lines "matplotlib.axes.Axes.get_lines")
:

In \[216\]: print(ax.get\_lines())
<a list of 1 Line2D objects>
In \[217\]: print(ax.get\_lines()\[0\])
Line2D(example)

Changing Artist properties[#](https://matplotlib.org/stable/users/explain/artists/artist_intro.html#changing-artist-properties "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

Getting the `lines` object gives us access to all the properties of the Line2D object. So if we want to change the _linewidth_ after the fact, we can do so using [`Artist.set`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set.html#matplotlib.artist.Artist.set "matplotlib.artist.Artist.set")
.

fig, ax \= plt.subplots(figsize\=(4, 2.5))
x \= np.arange(0, 13, 0.2)
y \= np.sin(x)
lines \= ax.plot(x, y, '-', label\='example', linewidth\=0.2, color\='blue')
lines\[0\].set(color\='green', linewidth\=2)

([`Source code`](https://matplotlib.org/stable/_downloads/1a8701f2eac32dbe6c650b7d7f927fc8/artist_intro-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/b8c4ae84b5dd5abc57c71d07a21726a0/artist_intro-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/559271a3800084d8d4cd363da1ff0063/artist_intro-1.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-artists-artist_intro-1.2x.png)](https://matplotlib.org/stable/_images/users-explain-artists-artist_intro-1.2x.png)

We can interrogate the full list of settable properties with [`matplotlib.artist.getp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.getp.html#matplotlib.artist.getp "matplotlib.artist.getp")
:

In \[218\]: martist.getp(lines\[0\])
agg\_filter = None
alpha = None
animated = False
antialiased or aa = True
bbox = Bbox(x0=0.004013842290585101, y0=0.013914221641967...
children = \[\]
clip\_box = TransformedBbox(     Bbox(x0=0.0, y0=0.0, x1=1.0, ...
clip\_on = True
clip\_path = None
color or c = blue
dash\_capstyle = butt
dash\_joinstyle = round
data = (array(\[0.91377845, 0.58456834, 0.36492019, 0.0379...\
drawstyle or ds = default\
figure = Figure(550x450)\
fillstyle = full\
gapcolor = None\
gid = None\
in\_layout = True\
label = example\
linestyle or ls = -\
linewidth or lw = 2.0\
marker = None\
markeredgecolor or mec = blue\
markeredgewidth or mew = 1.0\
markerfacecolor or mfc = blue\
markerfacecoloralt or mfcalt = none\
markersize or ms = 6.0\
markevery = None\
mouseover = False\
path = Path(array(\[\[0.91377845, 0.51224793\],        \[0.58...\
path\_effects = \[\]\
picker = None\
pickradius = 5\
rasterized = False\
sketch\_params = None\
snap = None\
solid\_capstyle = projecting\
solid\_joinstyle = round\
tightbbox = Bbox(x0=70.4609002763619, y0=54.321277798941786, x...\
transform = CompositeGenericTransform(     TransformWrapper(  ...\
transformed\_clip\_path\_and\_affine = (None, None)\
url = None\
visible = True\
window\_extent = Bbox(x0=70.4609002763619, y0=54.321277798941786, x...\
xdata = \[0.91377845 0.58456834 0.36492019 0.03796664 0.884...\
xydata = \[\[0.91377845 0.51224793\]  \[0.58456834 0.9820474 \] ...\
ydata = \[0.51224793 0.9820474  0.24469912 0.61647032 0.483...\
zorder = 2\
\
Note most Artists also have a distinct list of setters; e.g. [`Line2D.set_color`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_color "matplotlib.lines.Line2D.set_color")\
 or [`Line2D.set_linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linewidth "matplotlib.lines.Line2D.set_linewidth")\
.\
\
Changing Artist data[#](https://matplotlib.org/stable/users/explain/artists/artist_intro.html#changing-artist-data "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------------------\
\
In addition to styling properties like _color_ and _linewidth_, the Line2D object has a _data_ property. You can set the data after the line has been created using [`Line2D.set_data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_data "matplotlib.lines.Line2D.set_data")\
. This is often used for Animations, where the same line is shown evolving over time (see [Animations using Matplotlib](https://matplotlib.org/stable/users/explain/animations/index.html)\
)\
\
fig, ax \= plt.subplots(figsize\=(4, 2.5))\
x \= np.arange(0, 13, 0.2)\
y \= np.sin(x)\
lines \= ax.plot(x, y, '-', label\='example')\
lines\[0\].set\_data(\[x, np.cos(x)\])\
\
([`Source code`](https://matplotlib.org/stable/_downloads/d71a2584f43d90694b4cca45140e9fd3/artist_intro-2.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/9685ea2547e12d8c3b704c4267427764/artist_intro-2.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/ed5d470f717beb61ad5452858c2d19a4/artist_intro-2.png)\
)\
\
[![](https://matplotlib.org/stable/_images/users-explain-artists-artist_intro-2.2x.png)](https://matplotlib.org/stable/_images/users-explain-artists-artist_intro-2.2x.png)\
\
Manually adding Artists[#](https://matplotlib.org/stable/users/explain/artists/artist_intro.html#manually-adding-artists "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------------------------\
\
Not all Artists have helper methods, or you may want to use a low-level method for some reason. For example the [`patches.Circle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")\
 Artist does not have a helper, but we can still create and add to an Axes using the [`axes.Axes.add_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")\
 method:\
\
import matplotlib.patches as mpatches\
\
fig, ax \= plt.subplots(figsize\=(4, 2.5))\
circle \= mpatches.Circle((0.5, 0.5), 0.25, ec\="none")\
ax.add\_artist(circle)\
clipped\_circle \= mpatches.Circle((1, 0.5), 0.125, ec\="none", facecolor\='C1')\
ax.add\_artist(clipped\_circle)\
ax.set\_aspect(1)\
\
([`Source code`](https://matplotlib.org/stable/_downloads/be2aa1da675d5302c594303a90b84071/artist_intro-3.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/305ba783c7019eef16a94ebbfce9c408/artist_intro-3.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/2caa736903ff39ee1742b52f755a3bfa/artist_intro-3.png)\
)\
\
[![](https://matplotlib.org/stable/_images/users-explain-artists-artist_intro-3.2x.png)](https://matplotlib.org/stable/_images/users-explain-artists-artist_intro-3.2x.png)\
\
The Circle takes the center and radius of the Circle as arguments to its constructor; optional arguments are passed as keyword arguments.\
\
Note that when we add an Artist manually like this, it doesn't necessarily adjust the axis limits like most of the helper methods do, so the Artists can be clipped, as is the case above for the `clipped_circle` patch.\
\
See [Reference for Matplotlib artists](https://matplotlib.org/stable/gallery/shapes_and_collections/artist_reference.html#artist-reference)\
 for other patches.\
\
Removing Artists[#](https://matplotlib.org/stable/users/explain/artists/artist_intro.html#removing-artists "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------------------\
\
Sometimes we want to remove an Artist from a figure without re-specifying the whole figure from scratch. Most Artists have a usable _remove_ method that will remove the Artist from its Axes list. For instance `lines[0].remove()` would remove the _Line2D_ artist created in the example above.\
\
On this page