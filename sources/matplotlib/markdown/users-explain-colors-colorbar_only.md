[Skip to main content](https://matplotlib.org/stable/users/explain/colors/colorbar_only.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/users/explain/colors/colorbar_only.html#sphx-glr-download-users-explain-colors-colorbar-only-py)
 to download the full example code.

Customized Colorbars Tutorial[#](https://matplotlib.org/stable/users/explain/colors/colorbar_only.html#customized-colorbars-tutorial "Link to this heading")

=============================================================================================================================================================

This tutorial shows how to build and customize standalone colorbars, i.e. without an attached plot.

A [`colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
 requires a [`matplotlib.colorizer.ColorizingArtist`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist "matplotlib.colorizer.ColorizingArtist")
 which contains a [`matplotlib.colorizer.Colorizer`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
 that holds the data-to-color pipeline (norm and colormap). To create a colorbar without an attached plot one can directly instantiate the base class [`ColorizingArtist`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist "matplotlib.colorizer.ColorizingArtist")
, which has no associated data.

import matplotlib.pyplot as plt

import matplotlib as mpl

Basic continuous colorbar[#](https://matplotlib.org/stable/users/explain/colors/colorbar_only.html#basic-continuous-colorbar "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

Here, we create a basic continuous colorbar with ticks and labels.

The arguments to the [`colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
 call are a [`ColorizingArtist`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist "matplotlib.colorizer.ColorizingArtist")
, the axes where the colorbar should be drawn, and the colorbar's orientation. To crate a [`ColorizingArtist`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist "matplotlib.colorizer.ColorizingArtist")
 one must first make [`Colorizer`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
 that holds the desired _norm_ and _cmap_.

For more information see the [`colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#module-matplotlib.colorbar "matplotlib.colorbar")
 API.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 1), layout\='constrained')

[norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
 \= [mpl.colors.Normalize](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
(vmin\=5, vmax\=10)

[colorizer](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
 \= [mpl.colorizer.Colorizer](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
([norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
\=[norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
\="cool")

[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([mpl.colorizer.ColorizingArtist](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist "matplotlib.colorizer.ColorizingArtist")
([colorizer](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
),
             cax\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, orientation\='horizontal', label\='Some Units')

![colorbar only](https://matplotlib.org/stable/_images/sphx_glr_colorbar_only_001_2_00x.png)

Colorbar attached next to a pre-existing axes[#](https://matplotlib.org/stable/users/explain/colors/colorbar_only.html#colorbar-attached-next-to-a-pre-existing-axes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

All examples in this tutorial (except this one) show a standalone colorbar on its own figure, but it is possible to display the colorbar _next_ to a pre-existing Axes _ax_ by passing `ax=ax` to the colorbar() call (meaning "draw the colorbar next to _ax_") rather than `cax=ax` (meaning "draw the colorbar on _ax_").

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(layout\='constrained')

[colorizer](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
 \= [mpl.colorizer.Colorizer](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
([norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
\=[mpl.colors.Normalize](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
(0, 1), [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
\='magma')

[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([mpl.colorizer.ColorizingArtist](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist "matplotlib.colorizer.ColorizingArtist")
([colorizer](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
),
             [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, orientation\='vertical', label\='a colorbar label')

![colorbar only](https://matplotlib.org/stable/_images/sphx_glr_colorbar_only_002_2_00x.png)

Discrete and extended colorbar with continuous colorscale[#](https://matplotlib.org/stable/users/explain/colors/colorbar_only.html#discrete-and-extended-colorbar-with-continuous-colorscale "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following example shows how to make a discrete colorbar based on a continuous cmap. We use [`matplotlib.colors.BoundaryNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
 to describe the interval boundaries (which must be in increasing order), and further pass the _extend_ argument to it to further display "over" and "under" colors (which are used for data outside of the norm range).

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 1), layout\='constrained')

[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 \= [mpl.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["viridis"\]
[bounds](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\-1, 2, 5, 7, 12, 15\]
[norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
 \= [mpl.colors.BoundaryNorm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
([bounds](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [cmap.N](https://docs.python.org/3/library/functions.html#int "builtins.int")
, extend\='both')

[colorizer](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
 \= [mpl.colorizer.Colorizer](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
([norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
\=[norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
\='viridis')

[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([mpl.colorizer.ColorizingArtist](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist "matplotlib.colorizer.ColorizingArtist")
([colorizer](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
),
             cax\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, orientation\='horizontal',
             label\="Discrete intervals with extend='both' keyword")

![colorbar only](https://matplotlib.org/stable/_images/sphx_glr_colorbar_only_003_2_00x.png)

Colorbar with arbitrary colors[#](https://matplotlib.org/stable/users/explain/colors/colorbar_only.html#colorbar-with-arbitrary-colors "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------

The following example still uses a [`BoundaryNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
 to describe discrete interval boundaries, but now uses a [`matplotlib.colors.ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 to associate each interval with an arbitrary color (there must be as many intervals than there are colors).

We also pass additional arguments to [`colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
:

*   To display the out-of-range values on the colorbar, we use the _extend_ argument in the colorbar() call. (This is equivalent to passing the _extend_ argument in the [`BoundaryNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
     constructor as done in the previous example.)
    
*   To make the length of each colorbar segment proportional to its corresponding interval, we use the _spacing_ argument in the colorbar() call.
    

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 1), layout\='constrained')

[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 \= [mpl.colors.ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
(
    \['red', 'green', 'blue', 'cyan'\], under\='yellow', over\='magenta')
[bounds](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[1, 2, 4, 7, 8\]
[norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
 \= [mpl.colors.BoundaryNorm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
([bounds](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [cmap.N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[colorizer](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
 \= [mpl.colorizer.Colorizer](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
([norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
\=[norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
\=[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
)

[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
(
    [mpl.colorizer.ColorizingArtist](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist "matplotlib.colorizer.ColorizingArtist")
([colorizer](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
),
    cax\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, orientation\='horizontal',
    extend\='both',
    spacing\='proportional',
    label\='Discrete intervals, some other units',
)

![colorbar only](https://matplotlib.org/stable/_images/sphx_glr_colorbar_only_004_2_00x.png)

Colorbar with custom extension lengths[#](https://matplotlib.org/stable/users/explain/colors/colorbar_only.html#colorbar-with-custom-extension-lengths "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We can customize the length colorbar extensions, on a colorbar with discrete intervals. To make the length of each extension the same as the length of the interior colors, use `extendfrac='auto'`.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 1), layout\='constrained')

[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 \= [mpl.colors.ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
(
    \['royalblue', 'cyan', 'yellow', 'orange'\], over\='red', under\='blue')
[bounds](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\-1.0, \-0.5, 0.0, 0.5, 1.0\]
[norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
 \= [mpl.colors.BoundaryNorm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
([bounds](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [cmap.N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[colorizer](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
 \= [mpl.colorizer.Colorizer](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
([norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
\=[norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
\=[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
)

[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
(
    [mpl.colorizer.ColorizingArtist](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist "matplotlib.colorizer.ColorizingArtist")
([colorizer](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
),
    cax\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, orientation\='horizontal',
    extend\='both', extendfrac\='auto',
    spacing\='uniform',
    label\='Custom extension lengths, some other units',
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![colorbar only](https://matplotlib.org/stable/_images/sphx_glr_colorbar_only_005_2_00x.png)

**Total running time of the script:** (0 minutes 1.721 seconds)

[`Download Jupyter notebook: colorbar_only.ipynb`](https://matplotlib.org/stable/_downloads/b963041f451cde8f99a405ec0ea0f25d/colorbar_only.ipynb)

[`Download Python source code: colorbar_only.py`](https://matplotlib.org/stable/_downloads/5a60123144cbaa16c29cb481926340cb/colorbar_only.py)

[`Download zipped: colorbar_only.zip`](https://matplotlib.org/stable/_downloads/2b8f8b11f03eb7a55ee900209c225d7a/colorbar_only.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page