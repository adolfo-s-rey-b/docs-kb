[Skip to main content](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#sphx-glr-download-users-explain-axes-legend-guide-py)
 to download the full example code.

Legend guide[#](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-guide "Link to this heading")

========================================================================================================================

This legend guide extends the [`legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
 docstring - please read it before proceeding with this guide.

This guide makes use of some common terms, which are documented here for clarity:

legend entry[#](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#term-legend-entry "Link to this term")

A legend is made up of one or more legend entries. An entry is made up of exactly one key and one label.

legend key[#](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#term-legend-key "Link to this term")

The colored/patterned marker to the left of each legend label.

legend label[#](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#term-legend-label "Link to this term")

The text which describes the handle represented by the key.

legend handle[#](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#term-legend-handle "Link to this term")

The original object which is used to generate an appropriate entry in the legend.

Controlling the legend entries[#](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#controlling-the-legend-entries "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

Calling [`legend()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
 with no arguments automatically fetches the legend handles and their associated labels. This functionality is equivalent to:

handles, labels \= [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.get\_legend\_handles\_labels()
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(handles, labels)

The [`get_legend_handles_labels()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_legend_handles_labels.html#matplotlib.axes.Axes.get_legend_handles_labels "matplotlib.axes.Axes.get_legend_handles_labels")
 function returns a list of handles/artists which exist on the Axes which can be used to generate entries for the resulting legend - it is worth noting however that not all artists can be added to a legend, at which point a "proxy" will have to be created (see [Creating artists specifically for adding to the legend (aka. Proxy artists)](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#proxy-legend-handles)
 for further details).

Note

Artists with an empty string as label or with a label starting with an underscore, "\_", will be ignored.

For full control of what is being added to the legend, it is common to pass the appropriate handles directly to [`legend()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
line\_up, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[1, 2, 3\], label\='Line 2')
line\_down, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[3, 2, 1\], label\='Line 1')
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(handles\=\[line\_up, line\_down\])

### Renaming legend entries[#](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#renaming-legend-entries "Link to this heading")

When the labels cannot directly be set on the handles, they can be directly passed to [`Axes.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
line\_up, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[1, 2, 3\], label\='Line 2')
line\_down, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[3, 2, 1\], label\='Line 1')
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(\[line\_up, line\_down\], \['Line Up', 'Line Down'\])

If the handles are not directly accessible, for example when using some [Third-party packages](https://matplotlib.org/mpl-third-party/)
, they can be accessed via [`Axes.get_legend_handles_labels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_legend_handles_labels.html#matplotlib.axes.Axes.get_legend_handles_labels "matplotlib.axes.Axes.get_legend_handles_labels")
. Here we use a dictionary to rename existing labels:

my\_map \= {'Line Up':'Up', 'Line Down':'Down'}

handles, labels \= [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.get\_legend\_handles\_labels()
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(handles, \[my\_map\[[l](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")\
\] for [l](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")\
 in labels\])

Creating artists specifically for adding to the legend (aka. Proxy artists)[#](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#creating-artists-specifically-for-adding-to-the-legend-aka-proxy-artists "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Not all handles can be turned into legend entries automatically, so it is often necessary to create an artist which _can_. Legend handles don't have to exist on the Figure or Axes in order to be used.

Suppose we wanted to create a legend which has an entry for some data which is represented by a red color:

import matplotlib.pyplot as plt

import matplotlib.patches as mpatches

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[red\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
 \= [mpatches.Patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
(color\='red', label\='The red data')
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(handles\=\[[red\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")\
\])

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![legend guide](https://matplotlib.org/stable/_images/sphx_glr_legend_guide_001_2_00x.png)

There are many supported legend handles. Instead of creating a patch of color we could have created a line with a marker:

import matplotlib.lines as mlines

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[blue\_line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 \= [mlines.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
(\[\], \[\], color\='blue', marker\='\*',
                          markersize\=15, label\='Blue stars')
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(handles\=\[[blue\_line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
\])

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![legend guide](https://matplotlib.org/stable/_images/sphx_glr_legend_guide_002_2_00x.png)

Legend location[#](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-location "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

The location of the legend can be specified by the keyword argument _loc_. Please see the documentation at [`legend()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
 for more details.

The `bbox_to_anchor` keyword gives a great degree of control for manual legend placement. For example, if you want your Axes legend located at the figure's top right-hand corner instead of the Axes' corner, simply specify the corner's location and the coordinate system of that location:

[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(bbox\_to\_anchor\=(1, 1),
          bbox\_transform\=[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
.transFigure)

More examples of custom legend placement:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(\[\['top', 'top'\], \['bottom', 'BLANK'\]\],
                                  empty\_sentinel\="BLANK")
[ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['top'\].plot(\[1, 2, 3\], label\="test1")
[ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['top'\].plot(\[3, 2, 1\], label\="test2")
\# Place a legend above this subplot, expanding itself to
\# fully use the given bounding box.
[ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['top'\].legend(bbox\_to\_anchor\=(0., 1.02, 1., .102), [loc](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='lower left',
                      ncols\=2, mode\="expand", borderaxespad\=0.)

[ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['bottom'\].plot(\[1, 2, 3\], label\="test1")
[ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['bottom'\].plot(\[3, 2, 1\], label\="test2")
\# Place a legend to the right of this smaller subplot.
[ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['bottom'\].legend(bbox\_to\_anchor\=(1.05, 1),
                         [loc](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='upper left', borderaxespad\=0.)

![legend guide](https://matplotlib.org/stable/_images/sphx_glr_legend_guide_003_2_00x.png)

### Figure legends[#](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#figure-legends "Link to this heading")

Sometimes it makes more sense to place a legend relative to the (sub)figure rather than individual Axes. By using _constrained layout_ and specifying "outside" at the beginning of the _loc_ keyword argument, the legend is drawn outside the Axes on the (sub)figure.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(\[\['left', 'right'\]\], layout\='constrained')

[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['left'\].plot(\[1, 2, 3\], label\="test1")
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['left'\].plot(\[3, 2, 1\], label\="test2")

[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['right'\].plot(\[1, 2, 3\], 'C2', label\="test3")
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['right'\].plot(\[3, 2, 1\], 'C3', label\="test4")
\# Place a legend to the right of this smaller subplot.
[fig.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html#matplotlib.figure.Figure.legend "matplotlib.figure.Figure.legend")
([loc](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='outside upper right')

![legend guide](https://matplotlib.org/stable/_images/sphx_glr_legend_guide_004_2_00x.png)

This accepts a slightly different grammar than the normal _loc_ keyword, where "outside right upper" is different from "outside upper right".

[ucl](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['upper', 'center', 'lower'\]
[lcr](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['left', 'center', 'right'\]
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 4), layout\='constrained', facecolor\='0.95')

[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[1, 2\], \[1, 2\], label\='TEST')
\# Place a legend to the right of this smaller subplot.
for [loc](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in \[\
        'outside upper left',\
        'outside upper center',\
        'outside upper right',\
        'outside lower left',\
        'outside lower center',\
        'outside lower right'\]:
    [fig.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html#matplotlib.figure.Figure.legend "matplotlib.figure.Figure.legend")
([loc](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=[loc](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, title\=[loc](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 4), layout\='constrained', facecolor\='0.95')
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[1, 2\], \[1, 2\], label\='test')

for [loc](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in \[\
        'outside left upper',\
        'outside right upper',\
        'outside left center',\
        'outside right center',\
        'outside left lower',\
        'outside right lower'\]:
    [fig.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html#matplotlib.figure.Figure.legend "matplotlib.figure.Figure.legend")
([loc](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=[loc](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, title\=[loc](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

*   ![legend guide](https://matplotlib.org/stable/_images/sphx_glr_legend_guide_005_2_00x.png)
*   ![legend guide](https://matplotlib.org/stable/_images/sphx_glr_legend_guide_006_2_00x.png)

Multiple legends on the same Axes[#](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#multiple-legends-on-the-same-axes "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes it is more clear to split legend entries across multiple legends. Whilst the instinctive approach to doing this might be to call the [`legend()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
 function multiple times, you will find that only one legend ever exists on the Axes. This has been done so that it is possible to call [`legend()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
 repeatedly to update the legend to the latest handles on the Axes. To keep old legend instances, we must add them manually to the Axes:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[line1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[1, 2, 3\], label\="Line 1", linestyle\='--')
[line2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[3, 2, 1\], label\="Line 2", linewidth\=4)

\# Create a legend for the first line.
[first\_legend](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 \= [ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(handles\=\[[line1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
\], [loc](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='upper right')

\# Add the legend manually to the Axes.
[ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([first\_legend](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
)

\# Create another legend for the second line.
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(handles\=\[[line2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
\], [loc](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='lower right')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![legend guide](https://matplotlib.org/stable/_images/sphx_glr_legend_guide_007_2_00x.png)

Legend handlers[#](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-handlers "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

In order to create legend entries, handles are given as an argument to an appropriate [`HandlerBase`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerBase "matplotlib.legend_handler.HandlerBase")
 subclass. The choice of handler subclass is determined by the following rules:

1.  Update [`get_legend_handler_map()`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.get_legend_handler_map "matplotlib.legend.Legend.get_legend_handler_map")
     with the value in the `handler_map` keyword.
    
2.  Check if the `handle` is in the newly created `handler_map`.
    
3.  Check if the type of `handle` is in the newly created `handler_map`.
    
4.  Check if any of the types in the `handle`'s mro is in the newly created `handler_map`.
    

For completeness, this logic is mostly implemented in [`get_legend_handler()`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.get_legend_handler "matplotlib.legend.Legend.get_legend_handler")
.

All of this flexibility means that we have the necessary hooks to implement custom handlers for our own type of legend key.

The simplest example of using custom handlers is to instantiate one of the existing [`legend_handler.HandlerBase`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerBase "matplotlib.legend_handler.HandlerBase")
 subclasses. For the sake of simplicity, let's choose [`legend_handler.HandlerLine2D`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerLine2D "matplotlib.legend_handler.HandlerLine2D")
 which accepts a _numpoints_ argument (numpoints is also a keyword on the [`legend()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
 function for convenience). We can then pass the mapping of instance to Handler as a keyword to legend.

from matplotlib.legend\_handler import [HandlerLine2D](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerLine2D "matplotlib.legend_handler.HandlerLine2D")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[line1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[3, 2, 1\], marker\='o', label\='Line 1')
[line2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[1, 2, 3\], marker\='o', label\='Line 2')

[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(handler\_map\={[line1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
: [HandlerLine2D](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerLine2D "matplotlib.legend_handler.HandlerLine2D")
(numpoints\=4)}, handlelength\=4)

![legend guide](https://matplotlib.org/stable/_images/sphx_glr_legend_guide_008_2_00x.png)

As you can see, "Line 1" now has 4 marker points, where "Line 2" has 2 (the default). We have also increased the length of the handles with the `handlelength` keyword to fit the larger legend entry. Try the above code, only change the map's key from `line1` to `type(line1)`. Notice how now both [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 instances get 4 markers.

Along with handlers for complex plot types such as errorbars, stem plots and histograms, the default `handler_map` has a special `tuple` handler ([`legend_handler.HandlerTuple`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerTuple "matplotlib.legend_handler.HandlerTuple")
) which simply plots the handles on top of one another for each item in the given tuple. The following example demonstrates combining two legend keys on top of one another:

from numpy.random import [randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")

[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(10)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[red\_dot](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, "ro", markersize\=15)
\# Put a white cross over some of the data.
[white\_cross](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:5\], "w+", markeredgewidth\=3, markersize\=15)

[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(\[[red\_dot](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
, ([red\_dot](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
, [white\_cross](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
)\], \["Attr A", "Attr A+B"\])

![legend guide](https://matplotlib.org/stable/_images/sphx_glr_legend_guide_009_2_00x.png)

The [`legend_handler.HandlerTuple`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerTuple "matplotlib.legend_handler.HandlerTuple")
 class can also be used to assign several legend keys to the same entry:

from matplotlib.legend\_handler import [HandlerLine2D](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerLine2D "matplotlib.legend_handler.HandlerLine2D")
, [HandlerTuple](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerTuple "matplotlib.legend_handler.HandlerTuple")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[p1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[1, 2.5, 3\], 'r-d')
[p2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[3, 2, 1\], 'k-o')

[l](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 \= [ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(\[([p1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
, [p2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
)\], \['Two keys'\], numpoints\=1,
              handler\_map\={tuple: [HandlerTuple](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerTuple "matplotlib.legend_handler.HandlerTuple")
(ndivide\=None)})

![legend guide](https://matplotlib.org/stable/_images/sphx_glr_legend_guide_010_2_00x.png)

### Implementing a custom legend handler[#](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#implementing-a-custom-legend-handler "Link to this heading")

A custom handler can be implemented to turn any handle into a legend key (handles don't necessarily need to be matplotlib artists). The handler must implement a `legend_artist` method which returns a single artist for the legend to use. The required signature for `legend_artist` is documented at [`legend_artist`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerBase.legend_artist "matplotlib.legend_handler.HandlerBase.legend_artist")
.

import matplotlib.patches as mpatches

class AnyObject:
    pass

class AnyObjectHandler:
    def legend\_artist(self, legend, orig\_handle, fontsize, handlebox):
        x0, y0 \= handlebox.xdescent, handlebox.ydescent
        width, height \= handlebox.width, handlebox.height
        patch \= [mpatches.Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
(\[x0, y0\], width, height, facecolor\='red',
                                   edgecolor\='black', hatch\='xx', lw\=3,
                                   transform\=handlebox.get\_transform())
        handlebox.add\_artist(patch)
        return patch

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(\[AnyObject()\], \['My first handler'\],
          handler\_map\={AnyObject: AnyObjectHandler()})

![legend guide](https://matplotlib.org/stable/_images/sphx_glr_legend_guide_011_2_00x.png)

Alternatively, had we wanted to globally accept `AnyObject` instances without needing to manually set the _handler\_map_ keyword all the time, we could have registered the new handler with:

from matplotlib.legend import Legend
Legend.update\_default\_handler\_map({AnyObject: AnyObjectHandler()})

Whilst the power here is clear, remember that there are already many handlers implemented and what you want to achieve may already be easily possible with existing classes. For example, to produce elliptical legend keys, rather than rectangular ones:

from matplotlib.legend\_handler import [HandlerPatch](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerPatch "matplotlib.legend_handler.HandlerPatch")

class HandlerEllipse([HandlerPatch](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerPatch "matplotlib.legend_handler.HandlerPatch")
):
    def create\_artists(self, legend, orig\_handle,
                       xdescent, ydescent, width, height, fontsize, trans):
        center \= 0.5 \* width \- 0.5 \* xdescent, 0.5 \* height \- 0.5 \* ydescent
        p \= [mpatches.Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
(xy\=center, width\=width + xdescent,
                             height\=height + ydescent)
        self.update\_prop(p, orig\_handle, legend)
        p.set\_transform(trans)
        return \[p\]

[c](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
 \= [mpatches.Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
((0.5, 0.5), 0.25, facecolor\="green",
                    edgecolor\="red", linewidth\=3)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([c](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
)
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(\[[c](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")\
\], \["An ellipse, not a rectangle"\],
          handler\_map\={[mpatches.Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
: [HandlerEllipse](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerPatch "matplotlib.legend_handler.HandlerPatch")
()})

![legend guide](https://matplotlib.org/stable/_images/sphx_glr_legend_guide_012_2_00x.png)

**Total running time of the script:** (0 minutes 7.014 seconds)

[`Download Jupyter notebook: legend_guide.ipynb`](https://matplotlib.org/stable/_downloads/9771ec3f070b014893afe3648c2fe085/legend_guide.ipynb)

[`Download Python source code: legend_guide.py`](https://matplotlib.org/stable/_downloads/e6d00111e0bce42dab04f6f9ce6374b7/legend_guide.py)

[`Download zipped: legend_guide.zip`](https://matplotlib.org/stable/_downloads/9bde6bb3ee9bbe0cc744310687d0dd3f/legend_guide.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page