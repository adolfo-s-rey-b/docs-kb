[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html#sphx-glr-download-gallery-images-contours-and-fields-image-annotated-heatmap-py)
 to download the full example code.

Annotated heatmap[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html#annotated-heatmap "Link to this heading")

=============================================================================================================================================================

It is often desirable to show data which depends on two independent variables as a color coded image plot. This is often referred to as a heatmap. If the data is categorical, this would be called a categorical heatmap.

Matplotlib's [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 function makes production of such plots particularly easy.

The following examples show how to create a heatmap with annotations. We will start with an easy example and expand it to be usable as a universal function.

A simple categorical heatmap[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html#a-simple-categorical-heatmap "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We may start by defining some data. What we need is a 2D list or array which defines the data to color code. We then also need two lists or arrays of categories; of course the number of elements in those lists need to match the data along the respective axes. The heatmap itself is an [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 plot with the labels set to the categories we have. Note that it is important to set both, the tick locations ([`set_xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
) as well as the tick labels ([`set_xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels")
), otherwise they would become out of sync. The locations are just the ascending integer numbers, while the ticklabels are the labels to show. Finally, we can label the data itself by creating a [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 within each cell showing the value of that cell.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib
import matplotlib as mpl

[vegetables](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \["cucumber", "tomato", "lettuce", "asparagus",\
              "potato", "wheat", "barley"\]
[farmers](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \["Farmer Joe", "Upland Bros.", "Smith Gardening",\
           "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."\]

[harvest](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0\],\
                    \[2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0\],\
                    \[1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0\],\
                    \[0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0\],\
                    \[0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0\],\
                    \[1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1\],\
                    \[0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3\]\])

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([harvest](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# Show all ticks and label them with the respective list entries
[ax.set\_xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
(range(len([farmers](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)), labels\=[farmers](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
,
              rotation\=45, rotation\_mode\="xtick")
[ax.set\_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
(range(len([vegetables](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)), labels\=[vegetables](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

\# Loop over data dimensions and create text annotations.
for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(len([vegetables](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)):
    for [j](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(len([farmers](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)):
        [text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 \= [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
([j](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [harvest](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [j](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\],
                       ha\="center", va\="center", color\="w")

[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Harvest of local farmers (in tons/year)")
[fig.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Harvest of local farmers (in tons/year)](https://matplotlib.org/stable/_images/sphx_glr_image_annotated_heatmap_001_2_00x.png)

Using the helper function code style[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html#using-the-helper-function-code-style "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As discussed in the [Coding styles](https://matplotlib.org/stable/users/explain/quick_start.html#coding-styles)
 one might want to reuse such code to create some kind of heatmap for different input data and/or on different axes. We create a function that takes the data and the row and column labels as input, and allows arguments that are used to customize the plot

Here, in addition to the above we also want to create a colorbar and position the labels above of the heatmap instead of below it. The annotations shall get different colors depending on a threshold for better contrast against the pixel color. Finally, we turn the surrounding axes spines off and create a grid of white lines to separate the cells.

def heatmap([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, row\_labels, col\_labels, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=None,
            cbar\_kw\=None, cbarlabel\="", \*\*kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (M, N).
    row\_labels
        A list or array of length M with the labels for the rows.
    col\_labels
        A list or array of length N with the labels for the columns.
    ax
        A \`matplotlib.axes.Axes\` instance to which the heatmap is plotted.  If
        not provided, use current Axes or create a new one.  Optional.
    cbar\_kw
        A dictionary with arguments to \`matplotlib.Figure.colorbar\`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    \*\*kwargs
        All other arguments are forwarded to \`imshow\`.
    """

    if [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 is None:
        [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
()

    if cbar\_kw is None:
        cbar\_kw \= {}

    \# Plot the heatmap
    [im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \*\*kwargs)

    \# Create colorbar
    [cbar](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 \= [ax.figure.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure")
([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, \*\*cbar\_kw)
    [cbar.ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
(cbarlabel, rotation\=-90, va\="bottom")

    \# Show all ticks and label them with the respective list entries.
    [ax.set\_xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
(range([data.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[1\]), labels\=col\_labels,
                  rotation\=-30, rotation\_mode\="xtick")
    [ax.set\_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
(range([data.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[0\]), labels\=row\_labels)

    \# Let the horizontal axes labeling appear on top.
    [ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(top\=True, bottom\=False,
                   labeltop\=True, labelbottom\=False)

    \# Turn spines off and create white grid.
    [ax.spines](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
\[:\].set\_visible(False)

    [ax.set\_xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([data.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[1\]+1)\-.5, minor\=True)
    [ax.set\_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([data.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[0\]+1)\-.5, minor\=True)
    [ax.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
(which\="minor", color\="w", linestyle\='-', linewidth\=3)
    [ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(which\="minor", bottom\=False, left\=False)

    return [im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [cbar](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")

def annotate\_heatmap([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=None, valfmt\="{x:.2f}",
                     textcolors\=("black", "white"),
                     threshold\=None, \*\*textkw):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        \`matplotlib.ticker.Formatter\`.  Optional.
    textcolors
        A pair of colors.  The first is used for values below a threshold,
        the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    \*\*kwargs
        All other arguments are forwarded to each call to \`text\` used to create
        the text labels.
    """

    if not isinstance([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, (list, [np.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)):
        [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [im.get\_array](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ScalarMappable.get_array "matplotlib.colorizer._ScalarMappable.get_array")
()

    \# Normalize the threshold to the images color range.
    if threshold is not None:
        threshold \= [im.norm](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.norm "matplotlib.colorizer._ColorizerInterface.norm")
(threshold)
    else:
        threshold \= [im.norm](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.norm "matplotlib.colorizer._ColorizerInterface.norm")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.max())/2.

    \# Set default alignment to center, but allow it to be
    \# overwritten by textkw.
    kw \= dict(horizontalalignment\="center",
              verticalalignment\="center")
    kw.update(textkw)

    \# Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt \= [matplotlib.ticker.StrMethodFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.StrMethodFormatter "matplotlib.ticker.StrMethodFormatter")
(valfmt)

    \# Loop over the data and create a \`Text\` for each "pixel".
    \# Change the text's color depending on the data.
    [texts](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\]
    for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range([data.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[0\]):
        for [j](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range([data.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[1\]):
            kw.update(color\=textcolors\[int([im.norm](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.norm "matplotlib.colorizer._ColorizerInterface.norm")\
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [j](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]) \> threshold)\])
            [text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 \= [im.axes.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.axes.html#matplotlib.artist.Artist.axes "matplotlib.artist.Artist.axes")
([j](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, valfmt([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [j](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], None), \*\*kw)
            [texts](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.append([text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
)

    return [texts](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")

The above now allows us to keep the actual plot creation pretty compact.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [cbar](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 \= heatmap([harvest](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [vegetables](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [farmers](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
,
                   cmap\="YlGn", cbarlabel\="harvest \[t/year\]")
[texts](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= annotate\_heatmap([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, valfmt\="{x:.1f} t")

[fig.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![image annotated heatmap](https://matplotlib.org/stable/_images/sphx_glr_image_annotated_heatmap_002_2_00x.png)

Some more complex heatmap examples[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html#some-more-complex-heatmap-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In the following we show the versatility of the previously created functions by applying it in different cases and using different arguments.

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, (([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
), ([ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax4](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, figsize\=(8, 6))

\# Replicate the above example with a different font size and colormap.

[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [\_](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 \= heatmap([harvest](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [vegetables](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [farmers](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
,
                cmap\="Wistia", cbarlabel\="harvest \[t/year\]")
annotate\_heatmap([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, valfmt\="{x:.1f}", size\=7)

\# Create some new data, give further arguments to imshow (vmin),
\# use an integer format on the annotations and provide some colors.

[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randint](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint "numpy.random.randint")
(2, 100, size\=(7, 7))
[y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[f"Book {[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
}" for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 in range(1, 8)\]
[x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[f"Store {[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
}" for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 in list("ABCDEFG")\]
[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [\_](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 \= heatmap([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, vmin\=0,
                cmap\="magma\_r", cbarlabel\="weekly sold copies")
annotate\_heatmap([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, valfmt\="{x:d}", size\=7, threshold\=20,
                 textcolors\=("red", "white"))

\# Sometimes even the data itself is categorical. Here we use a
\# \`matplotlib.colors.BoundaryNorm\` to get the data into classes
\# and use this to colorize the plot, but also to obtain the class
\# labels from an array of classes.

[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(6, 6)
[y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[f"Prod. {[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
}" for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 in range(10, 70, 10)\]
[x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[f"Cycle {[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
}" for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 in range(1, 7)\]

[qrates](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= list("ABCDEFG")
[norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
 \= [matplotlib.colors.BoundaryNorm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-3.5, 3.5, 8), 7)
[fmt](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter")
 \= [matplotlib.ticker.FuncFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter")
(lambda [x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, pos: [qrates](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[::\-1\]\[[norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")\
([x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
)\])

[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [\_](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 \= heatmap([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
,
                cmap\=[mpl.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["PiYG"\].resampled(7), [norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
\=[norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
,
                cbar\_kw\=dict(ticks\=[np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-3, 4), format\=[fmt](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter")
),
                cbarlabel\="Quality Rating")

annotate\_heatmap([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, valfmt\=[fmt](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter")
, size\=9, fontweight\="bold", threshold\=-1,
                 textcolors\=("red", "black"))

\# We can nicely plot a correlation matrix. Since this is bound by -1 and 1,
\# we use those as vmin and vmax. We may also remove leading zeros and hide
\# the diagonal elements (which are all 1) by using a
\# \`matplotlib.ticker.FuncFormatter\`.

[corr\_matrix](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.corrcoef](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef "numpy.corrcoef")
([harvest](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [\_](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 \= heatmap([corr\_matrix](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [vegetables](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [vegetables](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax4](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
,
                cmap\="PuOr", vmin\=-1, vmax\=1,
                cbarlabel\="correlation coeff.")

def func([x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, pos):
    return f"{[x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
:.2f}".replace("0.", ".").replace("1.00", "")

annotate\_heatmap([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, valfmt\=[matplotlib.ticker.FuncFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter")
(func), size\=7)

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![image annotated heatmap](https://matplotlib.org/stable/_images/sphx_glr_image_annotated_heatmap_003_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
     / [`matplotlib.pyplot.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
    
*   [`matplotlib.figure.Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
     / [`matplotlib.pyplot.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
    

**Total running time of the script:** (0 minutes 5.711 seconds)

[`Download Jupyter notebook: image_annotated_heatmap.ipynb`](https://matplotlib.org/stable/_downloads/e1a9efcd0a9e889499abacec5670fae2/image_annotated_heatmap.ipynb)

[`Download Python source code: image_annotated_heatmap.py`](https://matplotlib.org/stable/_downloads/9d9e065de89f1666f743d014a09fc0b4/image_annotated_heatmap.py)

[`Download zipped: image_annotated_heatmap.zip`](https://matplotlib.org/stable/_downloads/a55f12e7d94747eda261a6ed3e82b9b0/image_annotated_heatmap.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page