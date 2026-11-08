[Skip to main content](https://matplotlib.org/stable/tutorials/lifecycle.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/tutorials/lifecycle.html#sphx-glr-download-tutorials-lifecycle-py)
 to download the full example code.

The Lifecycle of a Plot[#](https://matplotlib.org/stable/tutorials/lifecycle.html#the-lifecycle-of-a-plot "Link to this heading")

==================================================================================================================================

This tutorial aims to show the beginning, middle, and end of a single visualization using Matplotlib. We'll begin with some raw data and end by saving a figure of a customized visualization. Along the way we try to highlight some neat features and best-practices using Matplotlib.

Note

This tutorial is based on [this excellent blog post](https://pbpython.com/effective-matplotlib.html)
 by Chris Moffitt. It was transformed into this tutorial by Chris Holdgraf.

Our data[#](https://matplotlib.org/stable/tutorials/lifecycle.html#our-data "Link to this heading")

----------------------------------------------------------------------------------------------------

We'll use the data from the post from which this tutorial was derived. It contains sales information for a number of companies.

import matplotlib.pyplot as plt
import numpy as np

[data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}
[group\_data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= list([data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.values())
[group\_names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= list([data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.keys())
[group\_mean](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
([group\_data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

Getting started[#](https://matplotlib.org/stable/tutorials/lifecycle.html#getting-started "Link to this heading")

------------------------------------------------------------------------------------------------------------------

This data is naturally visualized as a barplot, with one bar per group. To do this with the object-oriented approach, we first generate an instance of [`figure.Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 and [`axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
. The Figure is like a canvas, and the Axes is a part of that canvas on which we will make a particular visualization.

Note

Figures can have multiple Axes on them. For information on how to do this, see the [Tight Layout tutorial](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#tight-layout-guide)
.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

![lifecycle](https://matplotlib.org/stable/_images/sphx_glr_lifecycle_001_2_00x.png)

Now that we have an Axes instance, we can plot on top of it.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
([group\_names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [group\_data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

![lifecycle](https://matplotlib.org/stable/_images/sphx_glr_lifecycle_002_2_00x.png)

Controlling the style[#](https://matplotlib.org/stable/tutorials/lifecycle.html#controlling-the-style "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

There are many styles available in Matplotlib in order to let you tailor your visualization to your needs. To see a list of styles, we can use [`style`](https://matplotlib.org/stable/api/style_api.html#module-matplotlib.style "matplotlib.style")
.

print([plt.style.available](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

\['Solarize\_Light2', 'bmh', 'classic', 'dark\_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'petroff10', 'petroff6', 'petroff8', 'seaborn-v0\_8', 'seaborn-v0\_8-bright', 'seaborn-v0\_8-colorblind', 'seaborn-v0\_8-dark', 'seaborn-v0\_8-dark-palette', 'seaborn-v0\_8-darkgrid', 'seaborn-v0\_8-deep', 'seaborn-v0\_8-muted', 'seaborn-v0\_8-notebook', 'seaborn-v0\_8-paper', 'seaborn-v0\_8-pastel', 'seaborn-v0\_8-poster', 'seaborn-v0\_8-talk', 'seaborn-v0\_8-ticks', 'seaborn-v0\_8-white', 'seaborn-v0\_8-whitegrid', 'tableau-colorblind10'\]

You can activate a style with the following:

plt.style.use('fivethirtyeight')

Now let's remake the above plot to see how it looks:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
([group\_names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [group\_data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

![lifecycle](https://matplotlib.org/stable/_images/sphx_glr_lifecycle_003_2_00x.png)

The style controls many things, such as color, linewidths, backgrounds, etc.

Customizing the plot[#](https://matplotlib.org/stable/tutorials/lifecycle.html#customizing-the-plot "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

Now we've got a plot with the general look that we want, so let's fine-tune it so that it's ready for print. First let's rotate the labels on the x-axis so that they show up more clearly. We can gain access to these labels with the [`axes.Axes.get_xticklabels()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticklabels.html#matplotlib.axes.Axes.get_xticklabels "matplotlib.axes.Axes.get_xticklabels")
 method:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
([group\_names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [group\_data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [ax.get\_xticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticklabels.html#matplotlib.axes.Axes.get_xticklabels "matplotlib.axes.Axes.get_xticklabels")
()

![lifecycle](https://matplotlib.org/stable/_images/sphx_glr_lifecycle_004_2_00x.png)

If we'd like to set the property of many items at once, it's useful to use the [`pyplot.setp()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
 function. This will take a list (or many lists) of Matplotlib objects, and attempt to set some style element of each one.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
([group\_names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [group\_data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [ax.get\_xticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticklabels.html#matplotlib.axes.Axes.get_xticklabels "matplotlib.axes.Axes.get_xticklabels")
()
[plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
([labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, rotation\=45, horizontalalignment\='right')

![lifecycle](https://matplotlib.org/stable/_images/sphx_glr_lifecycle_005_2_00x.png)

It looks like this cut off some of the labels on the bottom. We can tell Matplotlib to automatically make room for elements in the figures that we create. To do this we set the `autolayout` value of our rcParams. For more information on controlling the style, layout, and other features of plots with rcParams, see [Customizing Matplotlib with style sheets and rcParams](https://matplotlib.org/stable/users/explain/customizing.html#customizing)
.

[plt.rcParams.update](https://docs.python.org/3/library/stdtypes.html#dict.update "builtins.dict.update")
({'figure.autolayout': True})

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
([group\_names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [group\_data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [ax.get\_xticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticklabels.html#matplotlib.axes.Axes.get_xticklabels "matplotlib.axes.Axes.get_xticklabels")
()
[plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
([labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, rotation\=45, horizontalalignment\='right')

![lifecycle](https://matplotlib.org/stable/_images/sphx_glr_lifecycle_006_2_00x.png)

Next, we add labels to the plot. To do this with the OO interface, we can use the [`Artist.set()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set.html#matplotlib.artist.Artist.set "matplotlib.artist.Artist.set")
 method to set properties of this Axes object.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
([group\_names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [group\_data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [ax.get\_xticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticklabels.html#matplotlib.axes.Axes.get_xticklabels "matplotlib.axes.Axes.get_xticklabels")
()
[plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
([labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, rotation\=45, horizontalalignment\='right')
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(\-10000, 140000), xlabel\='Total Revenue', ylabel\='Company',
       title\='Company Revenue')

![Company Revenue](https://matplotlib.org/stable/_images/sphx_glr_lifecycle_007_2_00x.png)

We can also adjust the size of this plot using the [`pyplot.subplots()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
 function. We can do this with the _figsize_ keyword argument.

Note

While indexing in NumPy follows the form (row, column), the _figsize_ keyword argument follows the form (width, height). This follows conventions in visualization, which unfortunately are different from those of linear algebra.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(8, 4))
[ax.barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
([group\_names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [group\_data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [ax.get\_xticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticklabels.html#matplotlib.axes.Axes.get_xticklabels "matplotlib.axes.Axes.get_xticklabels")
()
[plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
([labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, rotation\=45, horizontalalignment\='right')
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(\-10000, 140000), xlabel\='Total Revenue', ylabel\='Company',
       title\='Company Revenue')

![Company Revenue](https://matplotlib.org/stable/_images/sphx_glr_lifecycle_008_2_00x.png)

For labels, we can specify custom formatting guidelines in the form of functions. Below we define a function that takes an integer as input, and returns a string as an output. When used with [`Axis.set_major_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
 or [`Axis.set_minor_formatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_minor_formatter.html#matplotlib.axis.Axis.set_minor_formatter "matplotlib.axis.Axis.set_minor_formatter")
, they will automatically create and use a [`ticker.FuncFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter")
 class.

For this function, the `x` argument is the original tick label and `pos` is the tick position. We will only use `x` here but both arguments are needed.

def currency(x, pos):
    """The two arguments are the value and tick position"""
    if x \>= 1e6:
        s \= f'${x\*1e-6:1.1f}M'
    else:
        s \= f'${x\*1e-3:1.0f}K'
    return s

We can then apply this function to the labels on our plot. To do this, we use the `xaxis` attribute of our Axes. This lets you perform actions on a specific axis on our plot.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 8))
[ax.barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
([group\_names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [group\_data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [ax.get\_xticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticklabels.html#matplotlib.axes.Axes.get_xticklabels "matplotlib.axes.Axes.get_xticklabels")
()
[plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
([labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, rotation\=45, horizontalalignment\='right')

[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(\-10000, 140000), xlabel\='Total Revenue', ylabel\='Company',
       title\='Company Revenue')
[ax.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
(currency)

![Company Revenue](https://matplotlib.org/stable/_images/sphx_glr_lifecycle_009_2_00x.png)

Combining multiple visualizations[#](https://matplotlib.org/stable/tutorials/lifecycle.html#combining-multiple-visualizations "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

It is possible to draw multiple plot elements on the same instance of [`axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
. To do this we simply need to call another one of the plot methods on that Axes object.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(8, 8))
[ax.barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
([group\_names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [group\_data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [ax.get\_xticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticklabels.html#matplotlib.axes.Axes.get_xticklabels "matplotlib.axes.Axes.get_xticklabels")
()
[plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
([labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, rotation\=45, horizontalalignment\='right')

\# Add a vertical line, here we set the style in the function call
[ax.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html#matplotlib.axes.Axes.axvline "matplotlib.axes.Axes.axvline")
([group\_mean](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, ls\='--', color\='r')

\# Annotate new companies
for [group](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in \[3, 5, 8\]:
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(145000, [group](https://docs.python.org/3/library/functions.html#int "builtins.int")
, "New Company", fontsize\=10,
            verticalalignment\="center")

\# Now we move our title up since it's getting a little cramped
[ax.title.set](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set "matplotlib.text.Text.set")
(y\=1.05)

[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(\-10000, 140000), xlabel\='Total Revenue', ylabel\='Company',
       title\='Company Revenue')
[ax.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
(currency)
[ax.set\_xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
(\[0, 25e3, 50e3, 75e3, 100e3, 125e3\])
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(right\=.1)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Company Revenue](https://matplotlib.org/stable/_images/sphx_glr_lifecycle_010_2_00x.png)

Saving our plot[#](https://matplotlib.org/stable/tutorials/lifecycle.html#saving-our-plot "Link to this heading")

------------------------------------------------------------------------------------------------------------------

Now that we're happy with the outcome of our plot, we want to save it to disk. There are many file formats we can save to in Matplotlib. To see a list of available options, use:

print([fig.canvas.get\_supported\_filetypes](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.get_supported_filetypes "matplotlib.backend_bases.FigureCanvasBase.get_supported_filetypes")
())

{'eps': 'Encapsulated Postscript', 'gif': 'Graphics Interchange Format', 'jpg': 'Joint Photographic Experts Group', 'jpeg': 'Joint Photographic Experts Group', 'pdf': 'Portable Document Format', 'pgf': 'PGF code for LaTeX', 'png': 'Portable Network Graphics', 'ps': 'Postscript', 'raw': 'Raw RGBA bitmap', 'rgba': 'Raw RGBA bitmap', 'svg': 'Scalable Vector Graphics', 'svgz': 'Scalable Vector Graphics', 'tif': 'Tagged Image File Format', 'tiff': 'Tagged Image File Format', 'webp': 'WebP Image Format', 'avif': 'AV1 Image File Format'}

We can then use the [`figure.Figure.savefig()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 in order to save the figure to disk. Note that there are several useful flags we show below:

*   `transparent=True` makes the background of the saved figure transparent if the format supports it.
    
*   `dpi=80` controls the resolution (dots per square inch) of the output.
    
*   `bbox_inches="tight"` fits the bounds of the figure to our plot.
    

\# Uncomment this line to save the figure.
\# fig.savefig('sales.png', transparent=False, dpi=80, bbox\_inches="tight")

**Total running time of the script:** (0 minutes 6.286 seconds)

[`Download Jupyter notebook: lifecycle.ipynb`](https://matplotlib.org/stable/_downloads/7de294e08c64b9d855f6e791ded043ab/lifecycle.ipynb)

[`Download Python source code: lifecycle.py`](https://matplotlib.org/stable/_downloads/e60e5e546a1c3950925a111a58079660/lifecycle.py)

[`Download zipped: lifecycle.zip`](https://matplotlib.org/stable/_downloads/0939e56d5bab3e8cca2af154196d3e36/lifecycle.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page