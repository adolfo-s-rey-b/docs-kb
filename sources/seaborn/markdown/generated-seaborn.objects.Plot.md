 

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

seaborn.objects.Plot[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn-objects-plot "Permalink to this heading")

=========================================================================================================================================

_class_ seaborn.objects.Plot(_\*args_, _data\=None_, _x\=None_, _y\=None_, _color\=None_, _alpha\=None_, _fill\=None_, _marker\=None_, _pointsize\=None_, _stroke\=None_, _linewidth\=None_, _linestyle\=None_, _fillcolor\=None_, _fillalpha\=None_, _edgewidth\=None_, _edgestyle\=None_, _edgecolor\=None_, _edgealpha\=None_, _text\=None_, _halign\=None_, _valign\=None_, _offset\=None_, _fontsize\=None_, _xmin\=None_, _xmax\=None_, _ymin\=None_, _ymax\=None_, _group\=None_)[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "Permalink to this definition")

An interface for declaratively specifying statistical graphics.

Plots are constructed by initializing this class and adding one or more layers, comprising a `Mark` and optional `Stat` or `Move`. Additionally, faceting variables or variable pairings may be defined to divide the space into multiple subplots. The mappings from data values to visual properties can be parametrized using scales, although the plot will try to infer good defaults when scales are not explicitly defined.

The constructor accepts a data source (a [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "(in pandas v2.2.0)")
 or dictionary with columnar values) and variable assignments. Variables can be passed as keys to the data source or directly as data vectors. If multiple data-containing objects are provided, they will be index-aligned.

The data source and variables defined in the constructor will be used for all layers in the plot, unless overridden or disabled when adding a layer.

The following variables can be defined in the constructor:

[x](https://seaborn.pydata.org/tutorial/properties.html#coordinate-property)
, [y](https://seaborn.pydata.org/tutorial/properties.html#coordinate-property)
, [color](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [alpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)
, [fill](https://seaborn.pydata.org/tutorial/properties.html#fill-property)
, [marker](https://seaborn.pydata.org/tutorial/properties.html#marker-property)
, [pointsize](https://seaborn.pydata.org/tutorial/properties.html#pointsize-property)
, [stroke](https://seaborn.pydata.org/tutorial/properties.html#stroke-property)
, [linewidth](https://seaborn.pydata.org/tutorial/properties.html#linewidth-property)
, [linestyle](https://seaborn.pydata.org/tutorial/properties.html#linestyle-property)
, [fillcolor](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [fillalpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)
, [edgewidth](https://seaborn.pydata.org/tutorial/properties.html#edgewidth-property)
, [edgestyle](https://seaborn.pydata.org/tutorial/properties.html#linestyle-property)
, [edgecolor](https://seaborn.pydata.org/tutorial/properties.html#color-property)
, [edgealpha](https://seaborn.pydata.org/tutorial/properties.html#alpha-property)
, [text](https://seaborn.pydata.org/tutorial/properties.html#property-property)
, [halign](https://seaborn.pydata.org/tutorial/properties.html#horizontalalignment-property)
, [valign](https://seaborn.pydata.org/tutorial/properties.html#verticalalignment-property)
, [offset](https://seaborn.pydata.org/tutorial/properties.html#offset-property)
, [fontsize](https://seaborn.pydata.org/tutorial/properties.html#fontsize-property)
, [xmin](https://seaborn.pydata.org/tutorial/properties.html#coordinate-property)
, [xmax](https://seaborn.pydata.org/tutorial/properties.html#coordinate-property)
, [ymin](https://seaborn.pydata.org/tutorial/properties.html#coordinate-property)
, [ymax](https://seaborn.pydata.org/tutorial/properties.html#coordinate-property)
, [group](https://seaborn.pydata.org/tutorial/properties.html#property-property)

The `data`, `x`, and `y` variables can be passed as positional arguments or using keywords. Whether the first positional argument is interpreted as a data source or `x` variable depends on its type.

The methods of this class return a copy of the instance; use chaining to build up a plot through multiple calls. Methods can be called in any order.

Most methods only add information to the plot spec; no actual processing happens until the plot is shown or saved. It is also possible to compile the plot without rendering it to access the lower-level representation.

Methods[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#methods "Permalink to this heading")

---------------------------------------------------------------------------------------------------------------

Specification methods

|     |     |
| --- | --- |
| [`add`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.add.html#seaborn.objects.Plot.add "seaborn.objects.Plot.add") | Specify a layer of the visualization in terms of mark and data transform(s). |
| [`scale`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.scale.html#seaborn.objects.Plot.scale "seaborn.objects.Plot.scale") | Specify mappings from data units to visual properties. |

Subplot methods

|     |     |
| --- | --- |
| [`facet`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.facet.html#seaborn.objects.Plot.facet "seaborn.objects.Plot.facet") | Produce subplots with conditional subsets of the data. |
| [`pair`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.pair.html#seaborn.objects.Plot.pair "seaborn.objects.Plot.pair") | Produce subplots by pairing multiple `x` and/or `y` variables. |

Customization methods

|     |     |
| --- | --- |
| [`layout`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.layout.html#seaborn.objects.Plot.layout "seaborn.objects.Plot.layout") | Control the figure size and layout. |
| [`label`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.label.html#seaborn.objects.Plot.label "seaborn.objects.Plot.label") | Control the labels and titles for axes, legends, and subplots. |
| [`limit`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.limit.html#seaborn.objects.Plot.limit "seaborn.objects.Plot.limit") | Control the range of visible data. |
| [`share`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.share.html#seaborn.objects.Plot.share "seaborn.objects.Plot.share") | Control sharing of axis limits and ticks across subplots. |
| [`theme`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.theme.html#seaborn.objects.Plot.theme "seaborn.objects.Plot.theme") | Control the appearance of elements in the plot. |

Integration methods

|     |     |
| --- | --- |
| [`on`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.on.html#seaborn.objects.Plot.on "seaborn.objects.Plot.on") | Provide existing Matplotlib figure or axes for drawing the plot. |

Output methods

|     |     |
| --- | --- |
| [`plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.plot.html#seaborn.objects.Plot.plot "seaborn.objects.Plot.plot") | Compile the plot spec and return the Plotter object. |
| [`save`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.save.html#seaborn.objects.Plot.save "seaborn.objects.Plot.save") | Compile the plot and write it to a buffer or file on disk. |
| [`show`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.show.html#seaborn.objects.Plot.show "seaborn.objects.Plot.show") | Compile the plot and display it by hooking into pyplot. |

Configuration[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#configuration "Permalink to this heading")

---------------------------------------------------------------------------------------------------------------------------

The [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot")
 object’s default behavior can be configured through its `Plot.config` attribute. Notice that this is a property of the class, not a method on an instance.

### Theme configuration[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#theme-configuration "Permalink to this heading")

Theme changes made through the the `Plot.config` interface will apply to all subsequent [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot")
 instances. Use the [`Plot.theme()`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.theme.html#seaborn.objects.Plot.theme "seaborn.objects.Plot.theme")
 method to modify the theme on a plot-by-plot basis.

The theme is a dictionary of matplotlib [rc parameters](https://matplotlib.org/stable/tutorials/introductory/customizing.html)
. You can set individual parameters directly:

so.Plot.config.theme\["axes.facecolor"\] \= "white"

Copy to clipboard

To change the overall style of the plot, update the theme with a dictionary of parameters, perhaps from one of seaborn’s theming functions:

from seaborn import axes\_style
so.Plot.config.theme.update(axes\_style("whitegrid"))

Copy to clipboard

To sync [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot")
 with matplotlib’s global state, pass the `rcParams` dictionary:

import matplotlib as mpl
so.Plot.config.theme.update(mpl.rcParams)

Copy to clipboard

The theme can also be reset back to seaborn defaults:

so.Plot.config.theme.reset()

Copy to clipboard

### Display configuration[#](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#display-configuration "Permalink to this heading")

When returned from the last statement in a notebook cell, a [`Plot`](https://seaborn.pydata.org/generated/seaborn.objects.Plot.html#seaborn.objects.Plot "seaborn.objects.Plot")
 will be compiled and embedded in the notebook as an image. By default, the image is rendered as HiDPI PNG. Alternatively, it is possible to display the plots in SVG format:

so.Plot.config.display\["format"\] \= "svg"

Copy to clipboard

SVG images use vector graphics with “infinite” resolution, so they will appear crisp at any amount of zoom. The downside is that each plot element is drawn separately, so the image data can get very heavy for certain kinds of plots (e.g., for dense scatterplots).

The HiDPI scaling of the default PNG images will also inflate the size of the notebook they are stored in. (Unlike with SVG, PNG size will scale with the dimensions of the plot but not its complexity). When not useful, it can be disabled:

so.Plot.config.display\["hidpi"\] \= False

Copy to clipboard

The embedded images are scaled down slightly — independently from the figure size or DPI — so that more information can be presented on the screen. The precise scaling factor is also configurable:

so.Plot.config.display\["scaling"\] \= 0.7

Copy to clipboard