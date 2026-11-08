 

 Ctrl+K

Site Navigation

*   [Installing](https://seaborn.pydata.org/installing.html)
    
*   [Gallery](https://seaborn.pydata.org/examples/index.html)
    
*   [Tutorial](https://seaborn.pydata.org/tutorial.html)
    
*   [API](https://seaborn.pydata.org/api.html)
    
*   [Releases](https://seaborn.pydata.org/whatsnew/index.html)
    
*   [Citing](https://seaborn.pydata.org/citing.html)
    
*   [FAQ](https://seaborn.pydata.org/faq.html)
    

*   [GitHub](https://github.com/mwaskom/seaborn "GitHub")
    
*   [StackOverflow](https://stackoverflow.com/tags/seaborn "StackOverflow")
    
*   [Twitter](https://twitter.com/michaelwaskom "Twitter")
    

On this page

seaborn.objects.Plot.on[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.on.html#seaborn-objects-plot-on "Permalink to this heading")

==================================================================================================================================================

Plot.on(_target_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.on.html#seaborn.objects.Plot.on "Permalink to this definition")

Provide existing Matplotlib figure or axes for drawing the plot.

When using this method, you will also need to explicitly call a method that triggers compilation, such as [`Plot.show()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.show.html#seaborn.objects.Plot.show "seaborn.objects.Plot.show")
 or [`Plot.save()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.save.html#seaborn.objects.Plot.save "seaborn.objects.Plot.save")
. If you want to postprocess using matplotlib, you’d need to call [`Plot.plot()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.plot.html#seaborn.objects.Plot.plot "seaborn.objects.Plot.plot")
 first to compile the plot without rendering it.

Parameters:

**target**Axes, SubFigure, or Figure

Matplotlib object to use. Passing [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.8.2)")
 will add artists without otherwise modifying the figure. Otherwise, subplots will be created within the space of the given [`matplotlib.figure.Figure`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure "(in Matplotlib v3.8.2)")
 or [`matplotlib.figure.SubFigure`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.SubFigure "(in Matplotlib v3.8.2)")
.

Examples

Passing a [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.8.2)")
 object provides functionality closest to seaborn’s axes-level plotting functions. Notice how the resulting image looks different from others created with [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot")
. This is because the plot theme uses the global rcParams at the time the axes were created, rather than [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot")
 defaults:

p \= so.Plot(diamonds, "carat", "price").add(so.Dots())
f, ax \= plt.subplots()
p.on(ax).show()

Copy to clipboard

[![../_images/objects.Plot.on_2_0.png](https://seaborn.pydata.org/_images/objects.Plot.on_2_0.png)](https://seaborn.pydata.org/_images/objects.Plot.on_2_0.png)

Alternatively, calling [`matplotlib.pyplot.figure()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "(in Matplotlib v3.8.2)")
 will defer axes creation to [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot")
, which will apply the default theme (and any customizations specified with [`Plot.theme()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.theme.html#seaborn.objects.Plot.theme "seaborn.objects.Plot.theme")
):

f \= plt.figure()
p.on(f).show()

Copy to clipboard

[![../_images/objects.Plot.on_4_0.png](https://seaborn.pydata.org/_images/objects.Plot.on_4_0.png)](https://seaborn.pydata.org/_images/objects.Plot.on_4_0.png)

Creating a [`matplotlib.figure.Figure`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure "(in Matplotlib v3.8.2)")
 object will bypass `pyplot` altogether. This may be useful for embedding [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot")
 figures in a GUI application:

f \= mpl.figure.Figure()
p.on(f).plot()

Copy to clipboard

[![../_images/objects.Plot.on_6_0.png](https://seaborn.pydata.org/_images/objects.Plot.on_6_0.png)](https://seaborn.pydata.org/_images/objects.Plot.on_6_0.png)

Using [`Plot.on`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.on.html#seaborn.objects.Plot.on "seaborn.objects.Plot.on")
 also provides access to the underlying matplotlib objects, which may be useful for deep customization. But it requires a careful attention to the order of operations by which the [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot")
 is specified, compiled, customized, and displayed:

f \= mpl.figure.Figure()
res \= p.on(f).plot()

ax \= f.axes\[0\]
rect \= mpl.patches.Rectangle(
    xy\=(0, 1), width\=.4, height\=.1,
    color\="C1", alpha\=.2,
    transform\=ax.transAxes, clip\_on\=False,
)
ax.add\_artist(rect)
ax.text(
    x\=rect.get\_width() / 2, y\=1 + rect.get\_height() / 2,
    s\="Diamonds: very sparkly!", size\=12,
    ha\="center", va\="center", transform\=ax.transAxes,
)

res

Copy to clipboard

[![../_images/objects.Plot.on_8_0.png](https://seaborn.pydata.org/_images/objects.Plot.on_8_0.png)](https://seaborn.pydata.org/_images/objects.Plot.on_8_0.png)

Matplotlib 3.4 introduced the concept of [`matplotlib.figure.Figure.subfigures()`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure.subfigures "(in Matplotlib v3.8.2)")
, which make it easier to composite multiple arrangements of subplots. These can also be passed to [`Plot.on()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.on.html#seaborn.objects.Plot.on "seaborn.objects.Plot.on")
,

f \= mpl.figure.Figure(figsize\=(7, 4), dpi\=100, layout\="constrained")
sf1, sf2 \= f.subfigures(1, 2)

p.on(sf1).plot()
(
    so.Plot(diamonds, x\="price")
    .add(so.Bars(), so.Hist())
    .facet(row\="cut")
    .scale(x\="log")
    .share(y\=False)
    .on(sf2)
)

Copy to clipboard

[![../_images/objects.Plot.on_10_0.png](https://seaborn.pydata.org/_images/objects.Plot.on_10_0.png)](https://seaborn.pydata.org/_images/objects.Plot.on_10_0.png)