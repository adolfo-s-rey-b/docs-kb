[Skip to main content](https://matplotlib.org/stable/tutorials/coding_shortcuts.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/tutorials/coding_shortcuts.html#sphx-glr-download-tutorials-coding-shortcuts-py)
 to download the full example code.

Coding shortcuts[#](https://matplotlib.org/stable/tutorials/coding_shortcuts.html#coding-shortcuts "Link to this heading")

===========================================================================================================================

Matplotlib's primary and universal API is the [Axes interface](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#api-interfaces)
. While it is clearly structured and powerful, it can sometimes feel overly verbose and thus cumbersome to write. This page collects patterns for condensing the code of the Axes-based API and achieving the same results with less typing for many simpler plots.

Note

The [pyplot interface](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 is an alternative more compact interface, and was historically modeled to be similar to MATLAB. It remains a valid approach for those who want to use it. However, it has the disadvantage that it achieves its brevity through implicit assumptions that you have to understand.

Since it follows a different paradigm, switching between the Axes interface and the pyplot interface requires a shift of the mental model, and some code rewrite, if the code develops to a point at which pyplot no longer provides enough flexibility.

This tutorial goes the other way round, starting from the standard verbose Axes interface and using its capabilities for shortcuts when you don't need all the generality.

Let's assume we want to make a plot of the number of daylight hours per day over the year in London.

The standard approach with the Axes interface looks like this.

import matplotlib.pyplot as plt
import numpy as np

[day](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(365)
[hours](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 4.276 \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* ([day](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 80)/365) + 12.203

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([day](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [hours](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\="orange")
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
("day")
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
("daylight hours")
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("London")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![London](https://matplotlib.org/stable/_images/sphx_glr_coding_shortcuts_001_2_00x.png)

Note that we've included `plt.show()` here. This is needed to show the plot window when running from a command line or in a Python script. If you run a Jupyter notebook, this command is automatically executed at the end of each cell.

For the rest of the tutorial, we'll assume that we are in a notebook and leave this out for brevity. Depending on your context you may still need it.

If you instead want to save to a file, use `fig.savefig("daylight.png")`.

Collect Axes properties into a single `set()` call[#](https://matplotlib.org/stable/tutorials/coding_shortcuts.html#collect-axes-properties-into-a-single-set-call "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The properties of Matplotlib Artists can be modified through their respective `set_*()` methods. Artists additionally have a generic `set()` method, that takes keyword arguments and is equivalent to calling all the respective `set_*()` methods.

[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
("day")
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
("daylight hours")

can also be written as

[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlabel\="day", ylabel\="daylight hours")

This is the most simple and effective reduction you can do. With that we can shorten the above plot to

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([day](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [hours](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\="orange")
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlabel\="day", ylabel\="daylight hours", title\="London")

![London](https://matplotlib.org/stable/_images/sphx_glr_coding_shortcuts_002_2_00x.png)

This works as long as you only need to pass one parameter to the `set_*()` function. The individual functions are still necessary if you want more control, e.g. `set_title("London", fontsize=16)`.

Not storing a reference to the figure[#](https://matplotlib.org/stable/tutorials/coding_shortcuts.html#not-storing-a-reference-to-the-figure "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Another nuisance of `fig, ax = plt.subplots()` is that you always create a `fig` variable, even if you don't use it. A slightly shorter version would be using the standard variable for unused value in Python (`_`): `_, ax = plt.subplots()`. However, that's only marginally better.

You can work around this by separating figure and Axes creation and chaining them

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
().add\_subplot()

This is a bit cleaner logically and has the slight advantage that you could set figure properties inline as well; e.g. `plt.figure(facecolor="lightgoldenrod")`. But it has the disadvantage that it's longer than `fig, ax = plt.subplots()`.

You can still obtain the figure from the Axes if needed, e.g.

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.figure.savefig("daylight\_hours.png")

The example code now looks like this:

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
().add\_subplot()
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([day](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [hours](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\="orange")
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlabel\="day", ylabel\="daylight hours", title\="London")

![London](https://matplotlib.org/stable/_images/sphx_glr_coding_shortcuts_003_2_00x.png)

Define Axes properties during axes creation[#](https://matplotlib.org/stable/tutorials/coding_shortcuts.html#define-axes-properties-during-axes-creation "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `set_*` methods as well as `set` modify existing objects. You can alternatively define them right at creation. Since you typically don't instantiate classes yourself in Matplotlib, but rather call some factory function that creates the object and wires it up correctly with the plot, this may seem less obvious. But in fact you just pass the desired properties to the factory functions. You are likely doing this already in some places without realizing. Consider the function to create a line

[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(x, y, color\="orange")

This is equivalent to

line, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(x, y)
line.set\_color("orange")

The same can be done with functions that create Axes.

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
().add\_subplot(xlabel\="day", ylabel\="daylight hours", title\="London")
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([day](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [hours](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\="orange")

![London](https://matplotlib.org/stable/_images/sphx_glr_coding_shortcuts_004_2_00x.png)

Important

The Axes properties are only accepted as keyword arguments by [`Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
, which creates a single Axes.

For [`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
 and [`pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
, you'd have to pass the properties as a dict via the keyword argument `subplot_kw`. The limitation here is that such parameters are given to all Axes. For example, if you need two subplots (`fig, (ax1, ax2) = plt.subplots(1, 2)`) with different labels, you have to set them individually.

Defining Axes properties during creation is best used for single subplots or when all subplots share the same properties.

Using implicit figure creation[#](https://matplotlib.org/stable/tutorials/coding_shortcuts.html#using-implicit-figure-creation "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

You can go even further by tapping into the pyplot logic and use [`pyplot.axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")
 to create the axes:

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")
(xlabel\="day", ylabel\="daylight hours", title\="London")
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([day](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [hours](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\="orange")

![London](https://matplotlib.org/stable/_images/sphx_glr_coding_shortcuts_005_2_00x.png)

Warning

When using this, you have to be aware of the implicit figure semantics of pyplot. `plt.axes()` will only create a new figure if no figure exists. Otherwise, it will add the Axes to the current existing figure, which is likely not what you want.

Not storing a reference to the Axes[#](https://matplotlib.org/stable/tutorials/coding_shortcuts.html#not-storing-a-reference-to-the-axes "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

If you only need to visualize one dataset, you can append the plot command directly to the Axes creation. This may be useful e.g. in notebooks, where you want to create a plot with some configuration, but as little distracting code as possible:

[plt.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")
(xlabel\="day", ylabel\="daylight hours").plot([day](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [hours](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\="orange")

![coding shortcuts](https://matplotlib.org/stable/_images/sphx_glr_coding_shortcuts_006_2_00x.png)

**Total running time of the script:** (0 minutes 3.542 seconds)

[`Download Jupyter notebook: coding_shortcuts.ipynb`](https://matplotlib.org/stable/_downloads/e757099ca1509506df5d9209b70e7013/coding_shortcuts.ipynb)

[`Download Python source code: coding_shortcuts.py`](https://matplotlib.org/stable/_downloads/6b75d2b62ece6161c7d0bbdf8ec11998/coding_shortcuts.py)

[`Download zipped: coding_shortcuts.zip`](https://matplotlib.org/stable/_downloads/37b6aede29992aec306d607b0a131e66/coding_shortcuts.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page