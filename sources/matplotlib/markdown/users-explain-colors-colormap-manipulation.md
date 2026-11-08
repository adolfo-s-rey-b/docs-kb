[Skip to main content](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html#sphx-glr-download-users-explain-colors-colormap-manipulation-py)
 to download the full example code.

Creating Colormaps in Matplotlib[#](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html#creating-colormaps-in-matplotlib "Link to this heading")

===========================================================================================================================================================================

Matplotlib has a number of built-in colormaps accessible via [`matplotlib.colormaps`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.colormaps "matplotlib.colormaps")
. There are also external libraries like [palettable](https://jiffyclub.github.io/palettable/)
 that have many extra colormaps.

However, we may also want to create or manipulate our own colormaps. This can be done using the class [`ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 or [`LinearSegmentedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
. Both colormap classes map values between 0 and 1 to colors. There are however differences, as explained below.

Before manually creating or manipulating colormaps, let us first see how we can obtain colormaps and their colors from existing colormap classes.

Getting colormaps and accessing their values[#](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html#getting-colormaps-and-accessing-their-values "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

First, getting a named colormap, most of which are listed in [Choosing Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html#colormaps)
, may be done using [`matplotlib.colormaps`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.colormaps "matplotlib.colormaps")
, which returns a colormap object. The length of the list of colors used internally to define the colormap can be adjusted via [`Colormap.resampled`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.resampled "matplotlib.colors.Colormap.resampled")
. Below we use a modest value of 8 so there are not a lot of values to look at.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
from matplotlib.colors import [LinearSegmentedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
, [ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")

[viridis](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 \= [mpl.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\['viridis'\].resampled(8)

The object `viridis` is a callable, that when passed a float between 0 and 1 returns an RGBA value from the colormap:

print([viridis](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
(0.56))

(np.float64(0.122312), np.float64(0.633153), np.float64(0.530398), np.float64(1.0))

### ListedColormap[#](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html#listedcolormap "Link to this heading")

[`ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
s store their color values in a `.colors` attribute. The list of colors that comprise the colormap can be directly accessed using the `colors` property, or it can be accessed indirectly by calling `viridis` with an array of values matching the length of the colormap. Note that the returned list is in the form of an RGBA (N, 4) array, where N is the length of the colormap.

print('viridis.colors', [viridis.colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
print('viridis(range(8))', [viridis](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
(range(8)))
print('viridis(np.linspace(0, 1, 8))', [viridis](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, 8)))

viridis.colors \[\[0.267004 0.004874 0.329415 1.      \]\
 \[0.275191 0.194905 0.496005 1.      \]\
 \[0.212395 0.359683 0.55171  1.      \]\
 \[0.153364 0.497    0.557724 1.      \]\
 \[0.122312 0.633153 0.530398 1.      \]\
 \[0.288921 0.758394 0.428426 1.      \]\
 \[0.626579 0.854645 0.223353 1.      \]\
 \[0.993248 0.906157 0.143936 1.      \]\]
viridis(range(8)) \[\[0.267004 0.004874 0.329415 1.      \]\
 \[0.275191 0.194905 0.496005 1.      \]\
 \[0.212395 0.359683 0.55171  1.      \]\
 \[0.153364 0.497    0.557724 1.      \]\
 \[0.122312 0.633153 0.530398 1.      \]\
 \[0.288921 0.758394 0.428426 1.      \]\
 \[0.626579 0.854645 0.223353 1.      \]\
 \[0.993248 0.906157 0.143936 1.      \]\]
viridis(np.linspace(0, 1, 8)) \[\[0.267004 0.004874 0.329415 1.      \]\
 \[0.275191 0.194905 0.496005 1.      \]\
 \[0.212395 0.359683 0.55171  1.      \]\
 \[0.153364 0.497    0.557724 1.      \]\
 \[0.122312 0.633153 0.530398 1.      \]\
 \[0.288921 0.758394 0.428426 1.      \]\
 \[0.626579 0.854645 0.223353 1.      \]\
 \[0.993248 0.906157 0.143936 1.      \]\]

The colormap is a lookup table, so "oversampling" the colormap returns nearest-neighbor interpolation (note the repeated colors in the list below)

print('viridis(np.linspace(0, 1, 12))', [viridis](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, 12)))

viridis(np.linspace(0, 1, 12)) \[\[0.267004 0.004874 0.329415 1.      \]\
 \[0.267004 0.004874 0.329415 1.      \]\
 \[0.275191 0.194905 0.496005 1.      \]\
 \[0.212395 0.359683 0.55171  1.      \]\
 \[0.212395 0.359683 0.55171  1.      \]\
 \[0.153364 0.497    0.557724 1.      \]\
 \[0.122312 0.633153 0.530398 1.      \]\
 \[0.288921 0.758394 0.428426 1.      \]\
 \[0.288921 0.758394 0.428426 1.      \]\
 \[0.626579 0.854645 0.223353 1.      \]\
 \[0.993248 0.906157 0.143936 1.      \]\
 \[0.993248 0.906157 0.143936 1.      \]\]

### LinearSegmentedColormap[#](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html#linearsegmentedcolormap "Link to this heading")

[`LinearSegmentedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
s do not have a `.colors` attribute. However, one may still call the colormap with an integer array, or with a float array between 0 and 1.

[copper](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
 \= [mpl.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\['copper'\].resampled(8)

print('copper(range(8))', [copper](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
(range(8)))
print('copper(np.linspace(0, 1, 8))', [copper](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, 8)))

copper(range(8)) \[\[0.         0.         0.         1.        \]\
 \[0.17647055 0.1116     0.07107143 1.        \]\
 \[0.35294109 0.2232     0.14214286 1.        \]\
 \[0.52941164 0.3348     0.21321429 1.        \]\
 \[0.70588219 0.4464     0.28428571 1.        \]\
 \[0.88235273 0.558      0.35535714 1.        \]\
 \[1.         0.6696     0.42642857 1.        \]\
 \[1.         0.7812     0.4975     1.        \]\]
copper(np.linspace(0, 1, 8)) \[\[0.         0.         0.         1.        \]\
 \[0.17647055 0.1116     0.07107143 1.        \]\
 \[0.35294109 0.2232     0.14214286 1.        \]\
 \[0.52941164 0.3348     0.21321429 1.        \]\
 \[0.70588219 0.4464     0.28428571 1.        \]\
 \[0.88235273 0.558      0.35535714 1.        \]\
 \[1.         0.6696     0.42642857 1.        \]\
 \[1.         0.7812     0.4975     1.        \]\]

Creating listed colormaps[#](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html#creating-listed-colormaps "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

Creating a colormap is essentially the inverse operation of the above where we supply a list or array of color specifications to [`ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 to make a new colormap.

Before continuing with the tutorial, let us define a helper function that takes one of more colormaps as input, creates some random data and applies the colormap(s) to an image plot of that dataset.

def plot\_examples(colormaps):
    """
    Helper function to plot data with associated colormap.
    """
    [np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)
    [data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(30, 30)
    n \= len(colormaps)
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, n, figsize\=(n \* 2 + 2, 3),
                            layout\='constrained', squeeze\=False)
    for \[ax, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")\
\] in zip(axs.flat, colormaps):
        psm \= ax.pcolormesh([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
\=[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
, rasterized\=True, vmin\=-4, vmax\=4)
        [fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
(psm, ax\=ax)
    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

In the simplest case we might type in a list of color names to create a colormap from those.

[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 \= [ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
(\["darkorange", "gold", "lawngreen", "lightseagreen"\])
plot\_examples(\[[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")\
\])

![colormap manipulation](https://matplotlib.org/stable/_images/sphx_glr_colormap-manipulation_001_2_00x.png)

In fact, that list may contain any valid [Matplotlib color specification](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
. Particularly useful for creating custom colormaps are (N, 4)-shaped arrays. Because with the variety of numpy operations that we can do on a such an array, carpentry of new colormaps from existing colormaps become quite straight forward.

For example, suppose we want to make the first 25 entries of a 256-length "viridis" colormap pink for some reason:

[viridis](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 \= [mpl.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\['viridis'\].resampled(256)
[newcolors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [viridis](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, 256))
[pink](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[248/256, 24/256, 148/256, 1\])
[newcolors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:25, :\] \= [pink](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
[newcmp](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 \= [ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
([newcolors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

plot\_examples(\[[viridis](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")\
, [newcmp](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")\
\])

![colormap manipulation](https://matplotlib.org/stable/_images/sphx_glr_colormap-manipulation_002_2_00x.png)

We can reduce the dynamic range of a colormap; here we choose the middle half of the colormap. Note, however, that because viridis is a listed colormap, we will end up with 128 discrete values instead of the 256 values that were in the original colormap. This method does not interpolate in color-space to add new colors.

[viridis\_big](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 \= [mpl.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\['viridis'\]
[newcmp](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 \= [ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
([viridis\_big](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.25, 0.75, 128)))
plot\_examples(\[[viridis](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")\
, [newcmp](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")\
\])

![colormap manipulation](https://matplotlib.org/stable/_images/sphx_glr_colormap-manipulation_003_2_00x.png)

and we can easily concatenate two colormaps:

[top](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
 \= [mpl.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\['Oranges\_r'\].resampled(128)
[bottom](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
 \= [mpl.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\['Blues'\].resampled(128)

[newcolors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
(([top](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, 128)),
                       [bottom](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, 128))))
[newcmp](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 \= [ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
([newcolors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, name\='OrangeBlue')
plot\_examples(\[[viridis](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")\
, [newcmp](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")\
\])

![colormap manipulation](https://matplotlib.org/stable/_images/sphx_glr_colormap-manipulation_004_2_00x.png)

Of course we need not start from a named colormap, we just need to create the (N, 4) array to pass to [`ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
. Here we create a colormap that goes from brown (RGB: 90, 40, 40) to white (RGB: 255, 255, 255).

[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 256
[vals](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
(([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 4))
[vals](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 0\] \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(90/256, 1, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[vals](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 1\] \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(40/256, 1, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[vals](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 2\] \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(40/256, 1, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[newcmp](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 \= [ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
([vals](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
plot\_examples(\[[viridis](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")\
, [newcmp](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")\
\])

![colormap manipulation](https://matplotlib.org/stable/_images/sphx_glr_colormap-manipulation_005_2_00x.png)

Creating linear segmented colormaps[#](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html#creating-linear-segmented-colormaps "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [`LinearSegmentedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
 class specifies colormaps using anchor points between which RGB(A) values are interpolated.

The format to specify these colormaps allows discontinuities at the anchor points. Each anchor point is specified as a row in a matrix of the form `[x[i] yleft[i] yright[i]]`, where `x[i]` is the anchor, and `yleft[i]` and `yright[i]` are the values of the color on either side of the anchor point.

If there are no discontinuities, then `yleft[i] == yright[i]`:

[cdict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {'red':   \[\[0.0,  0.0, 0.0\],\
                   \[0.5,  1.0, 1.0\],\
                   \[1.0,  1.0, 1.0\]\],
         'green': \[\[0.0,  0.0, 0.0\],\
                   \[0.25, 0.0, 0.0\],\
                   \[0.75, 1.0, 1.0\],\
                   \[1.0,  1.0, 1.0\]\],
         'blue':  \[\[0.0,  0.0, 0.0\],\
                   \[0.5,  0.0, 0.0\],\
                   \[1.0,  1.0, 1.0\]\]}

def plot\_linearmap([cdict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
):
    [newcmp](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 \= [LinearSegmentedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
('testCmap', segmentdata\=[cdict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
\=256)
    rgba \= [newcmp](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, 256))
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(4, 3), layout\='constrained')
    col \= \['r', 'g', 'b'\]
    for xx in \[0.25, 0.5, 0.75\]:
        ax.axvline(xx, color\='0.7', linestyle\='--')
    for i in range(3):
        ax.plot([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(256)/256, rgba\[:, i\], color\=col\[i\])
    ax.set\_xlabel('index')
    ax.set\_ylabel('RGB')
    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

plot\_linearmap([cdict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![colormap manipulation](https://matplotlib.org/stable/_images/sphx_glr_colormap-manipulation_006_2_00x.png)

In order to make a discontinuity at an anchor point, the third column is different than the second. The matrix for each of "red", "green", "blue", and optionally "alpha" is set up as:

[cdict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['red'\] \= \[...\
                \[x\[i\]      yleft\[i\]     yright\[i\]\],\
                \[x\[i+1\]    yleft\[i+1\]   yright\[i+1\]\],\
               ...\]

and for values passed to the colormap between `x[i]` and `x[i+1]`, the interpolation is between `yright[i]` and `yleft[i+1]`.

In the example below there is a discontinuity in red at 0.5. The interpolation between 0 and 0.5 goes from 0.3 to 1, and between 0.5 and 1 it goes from 0.9 to 1. Note that `red[0, 1]`, and `red[2, 2]` are both superfluous to the interpolation because `red[0, 1]` (i.e., `yleft[0]`) is the value to the left of 0, and `red[2, 2]` (i.e., `yright[2]`) is the value to the right of 1, which are outside the color mapping domain.

[cdict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['red'\] \= \[\[0.0,  0.0, 0.3\],\
                \[0.5,  1.0, 0.9\],\
                \[1.0,  1.0, 1.0\]\]
plot\_linearmap([cdict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![colormap manipulation](https://matplotlib.org/stable/_images/sphx_glr_colormap-manipulation_007_2_00x.png)

### Directly creating a segmented colormap from a list[#](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html#directly-creating-a-segmented-colormap-from-a-list "Link to this heading")

The approach described above is very versatile, but admittedly a bit cumbersome to implement. For some basic cases, the use of [`LinearSegmentedColormap.from_list`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap.from_list "matplotlib.colors.LinearSegmentedColormap.from_list")
 may be easier. This creates a segmented colormap with equal spacings from a supplied list of colors.

[colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \["darkorange", "gold", "lawngreen", "lightseagreen"\]
[cmap1](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
 \= [LinearSegmentedColormap.from\_list](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap.from_list "matplotlib.colors.LinearSegmentedColormap.from_list")
("mycmap", [colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

If desired, the nodes of the colormap can be given as numbers between 0 and 1. For example, one could have the reddish part take more space in the colormap.

[nodes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[0.0, 0.4, 0.8, 1.0\]
[cmap2](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
 \= [LinearSegmentedColormap.from\_list](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap.from_list "matplotlib.colors.LinearSegmentedColormap.from_list")
("mycmap", list(zip([nodes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)))

plot\_examples(\[[cmap1](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")\
, [cmap2](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")\
\])

![colormap manipulation](https://matplotlib.org/stable/_images/sphx_glr_colormap-manipulation_008_2_00x.png)

Reversing a colormap[#](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html#reversing-a-colormap "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

[`Colormap.reversed`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.reversed "matplotlib.colors.Colormap.reversed")
 creates a new colormap that is a reversed version of the original colormap.

[colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \["#ffffcc", "#a1dab4", "#41b6c4", "#2c7fb8", "#253494"\]
[my\_cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 \= [ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
([colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, name\="my\_cmap")

[my\_cmap\_r](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 \= [my\_cmap.reversed](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap.reversed "matplotlib.colors.ListedColormap.reversed")
()

plot\_examples(\[[my\_cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")\
, [my\_cmap\_r](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")\
\])

![colormap manipulation](https://matplotlib.org/stable/_images/sphx_glr_colormap-manipulation_009_2_00x.png)

If no name is passed in, `.reversed` also names the copy by [appending '\_r'](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html#registering-colormap)
 to the original colormap's name.

Registering a colormap[#](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html#registering-a-colormap "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

Colormaps can be added to the [`matplotlib.colormaps`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.colormaps "matplotlib.colormaps")
 list of named colormaps. This allows the colormaps to be accessed by name in plotting functions:

\# my\_cmap, my\_cmap\_r from reversing a colormap
[mpl.colormaps.register](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.register "matplotlib.cm.ColormapRegistry.register")
([cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
\=[my\_cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
)
[mpl.colormaps.register](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.register "matplotlib.cm.ColormapRegistry.register")
([cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
\=[my\_cmap\_r](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
)

[data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\[1, 2, 3, 4, 5\]\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2)

[ax1.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
\='my\_cmap')
[ax2.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
\='my\_cmap\_r')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![colormap manipulation](https://matplotlib.org/stable/_images/sphx_glr_colormap-manipulation_010_2_00x.png)

Colormaps added to the registry can also be deregistered:

[mpl.colormaps.unregister](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.unregister "matplotlib.cm.ColormapRegistry.unregister")
([my\_cmap.name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
    
*   [`matplotlib.figure.Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
    
*   [`matplotlib.colors`](https://matplotlib.org/stable/api/colors_api.html#module-matplotlib.colors "matplotlib.colors")
    
*   [`matplotlib.colors.LinearSegmentedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
    
*   [`matplotlib.colors.ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
    
*   [`matplotlib.cm`](https://matplotlib.org/stable/api/cm_api.html#module-matplotlib.cm "matplotlib.cm")
    
*   [`matplotlib.colormaps`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.colormaps "matplotlib.colormaps")
    

**Total running time of the script:** (0 minutes 8.355 seconds)

[`Download Jupyter notebook: colormap-manipulation.ipynb`](https://matplotlib.org/stable/_downloads/ed45f2a3380f33f4b7a2dbf4b6b31be0/colormap-manipulation.ipynb)

[`Download Python source code: colormap-manipulation.py`](https://matplotlib.org/stable/_downloads/389295c6d59aec11c1aadaccf12ff422/colormap-manipulation.py)

[`Download zipped: colormap-manipulation.zip`](https://matplotlib.org/stable/_downloads/c01dd5cad04166d697c28e40ccae2cef/colormap-manipulation.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page