[Skip to main content](https://matplotlib.org/stable/gallery/color/custom_cmap.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/color/custom_cmap.html#sphx-glr-download-gallery-color-custom-cmap-py)
 to download the full example code.

Create a colormap from a list of colors[#](https://matplotlib.org/stable/gallery/color/custom_cmap.html#create-a-colormap-from-a-list-of-colors "Link to this heading")

========================================================================================================================================================================

For more detail on creating and manipulating colormaps see [Creating Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html#colormap-manipulation)
.

Creating a [colormap](https://matplotlib.org/stable/users/explain/colors/colormaps.html#colormaps)
 from a list of colors can be done with the [`LinearSegmentedColormap.from_list`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap.from_list "matplotlib.colors.LinearSegmentedColormap.from_list")
 method. You must pass a list of RGB tuples that define the mixture of colors from 0 to 1.

Creating custom colormaps[#](https://matplotlib.org/stable/gallery/color/custom_cmap.html#creating-custom-colormaps "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

It is also possible to create a custom mapping for a colormap. This is accomplished by creating dictionary that specifies how the RGB channels change from one end of the cmap to the other.

Example: suppose you want red to increase from 0 to 1 over the bottom half, green to do the same over the middle half, and blue over the top half. Then you would use:

cdict \= {
    'red': (
        (0.0,  0.0, 0.0),
        (0.5,  1.0, 1.0),
        (1.0,  1.0, 1.0),
    ),
    'green': (
        (0.0,  0.0, 0.0),
        (0.25, 0.0, 0.0),
        (0.75, 1.0, 1.0),
        (1.0,  1.0, 1.0),
    ),
    'blue': (
        (0.0,  0.0, 0.0),
        (0.5,  0.0, 0.0),
        (1.0,  1.0, 1.0),
    )
}

If, as in this example, there are no discontinuities in the r, g, and b components, then it is quite simple: the second and third element of each tuple, above, is the same -- call it "`y`". The first element ("`x`") defines interpolation intervals over the full range of 0 to 1, and it must span that whole range. In other words, the values of `x` divide the 0-to-1 range into a set of segments, and `y` gives the end-point color values for each segment.

Now consider the green, `cdict['green']` is saying that for:

*   0 <= `x` <= 0.25, `y` is zero; no green.
    
*   0.25 < `x` <= 0.75, `y` varies linearly from 0 to 1.
    
*   0.75 < `x` <= 1, `y` remains at 1, full green.
    

If there are discontinuities, then it is a little more complicated. Label the 3 elements in each row in the `cdict` entry for a given color as `(x, y0, y1)`. Then for values of `x` between `x[i]` and `x[i+1]` the color value is interpolated between `y1[i]` and `y0[i+1]`.

Going back to a cookbook example:

cdict \= {
    'red': (
        (0.0,  0.0, 0.0),
        (0.5,  1.0, 0.7),
        (1.0,  1.0, 1.0),
    ),
    'green': (
        (0.0,  0.0, 0.0),
        (0.5,  1.0, 0.0),
        (1.0,  1.0, 1.0),
    ),
    'blue': (
        (0.0,  0.0, 0.0),
        (0.5,  0.0, 0.0),
        (1.0,  1.0, 1.0),
    )
}

and look at `cdict['red'][1]`; because `y0 != y1`, it is saying that for `x` from 0 to 0.5, red increases from 0 to 1, but then it jumps down, so that for `x` from 0.5 to 1, red increases from 0.7 to 1. Green ramps from 0 to 1 as `x` goes from 0 to 0.5, then jumps back to 0, and ramps back to 1 as `x` goes from 0.5 to 1.

row i:   [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
  y0  y1
               /
              /
row i+1: [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
  y0  y1

Above is an attempt to show that for `x` in the range `x[i]` to `x[i+1]`, the interpolation is between `y1[i]` and `y0[i+1]`. So, `y0[0]` and `y1[-1]` are never used.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
from matplotlib.colors import [LinearSegmentedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")

\# Make some illustrative fake data:

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 0.1)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 0.1)
[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* 10

### Colormaps from a list[#](https://matplotlib.org/stable/gallery/color/custom_cmap.html#colormaps-from-a-list "Link to this heading")

[colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[(1, 0, 0), (0, 1, 0), (0, 0, 1)\]  \# R -> G -> B
[n\_bins](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[3, 6, 10, 100\]  \# Discretizes the interpolation into bins
[cmap\_name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= 'my\_list'
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, figsize\=(6, 9))
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(left\=0.02, bottom\=0.06, right\=0.95, top\=0.94, wspace\=0.05)
for [n\_bin](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in zip([n\_bins](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
):
    \# Create the colormap
    [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
 \= [LinearSegmentedColormap.from\_list](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap.from_list "matplotlib.colors.LinearSegmentedColormap.from_list")
([cmap\_name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, N\=[n\_bin](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
    \# Fewer bins will result in "coarser" colomap interpolation
    [im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, origin\='lower', [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
\=[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
)
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("N bins: %s" % [n\_bin](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
    [fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

![N bins: 3, N bins: 6, N bins: 10, N bins: 100](https://matplotlib.org/stable/_images/sphx_glr_custom_cmap_001_2_00x.png)

### Custom colormaps[#](https://matplotlib.org/stable/gallery/color/custom_cmap.html#custom-colormaps "Link to this heading")

[cdict1](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {
    'red': (
        (0.0, 0.0, 0.0),
        (0.5, 0.0, 0.1),
        (1.0, 1.0, 1.0),
    ),
    'green': (
        (0.0, 0.0, 0.0),
        (1.0, 0.0, 0.0),
    ),
    'blue': (
        (0.0, 0.0, 1.0),
        (0.5, 0.1, 0.0),
        (1.0, 0.0, 0.0),
    )
}

[cdict2](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {
    'red': (
        (0.0, 0.0, 0.0),
        (0.5, 0.0, 1.0),
        (1.0, 0.1, 1.0),
    ),
    'green': (
        (0.0, 0.0, 0.0),
        (1.0, 0.0, 0.0),
    ),
    'blue': (
        (0.0, 0.0, 0.1),
        (0.5, 1.0, 0.0),
        (1.0, 0.0, 0.0),
    )
}

[cdict3](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {
    'red': (
        (0.0, 0.0, 0.0),
        (0.25, 0.0, 0.0),
        (0.5, 0.8, 1.0),
        (0.75, 1.0, 1.0),
        (1.0, 0.4, 1.0),
    ),
    'green': (
        (0.0, 0.0, 0.0),
        (0.25, 0.0, 0.0),
        (0.5, 0.9, 0.9),
        (0.75, 0.0, 0.0),
        (1.0, 0.0, 0.0),
    ),
    'blue': (
        (0.0, 0.0, 0.4),
        (0.25, 1.0, 1.0),
        (0.5, 1.0, 0.8),
        (0.75, 0.0, 0.0),
        (1.0, 0.0, 0.0),
    )
}

\# Make a modified version of cdict3 with some transparency
\# in the middle of the range.
[cdict4](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {
    \*\*[cdict3](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
,
    'alpha': (
        (0.0, 1.0, 1.0),
        \# (0.25, 1.0, 1.0),
        (0.5, 0.3, 0.3),
        \# (0.75, 1.0, 1.0),
        (1.0, 1.0, 1.0),
    ),
}

Now we will use this example to illustrate 2 ways of handling custom colormaps. First, the most direct and explicit:

[blue\_red1](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
 \= [LinearSegmentedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
('BlueRed1', [cdict1](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

Second, create the map explicitly and register it. Like the first method, this method works with any kind of Colormap, not just a LinearSegmentedColormap:

[mpl.colormaps.register](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.register "matplotlib.cm.ColormapRegistry.register")
([LinearSegmentedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
('BlueRed2', [cdict2](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
))
[mpl.colormaps.register](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.register "matplotlib.cm.ColormapRegistry.register")
([LinearSegmentedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
('BlueRed3', [cdict3](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
))
[mpl.colormaps.register](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.register "matplotlib.cm.ColormapRegistry.register")
([LinearSegmentedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
('BlueRedAlpha', [cdict4](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
))

Make the figure, with 4 subplots:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, figsize\=(6, 9))
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(left\=0.02, bottom\=0.06, right\=0.95, top\=0.94, wspace\=0.05)

[im1](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].imshow([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
\=[blue\_red1](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
)
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([im1](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\])

[im2](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].imshow([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
\='BlueRed2')
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([im2](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\])

\# Now we will set the third cmap as the default.  One would
\# not normally do this in the middle of a script like this;
\# it is done here just to illustrate the method.

[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['image.cmap'\] \= 'BlueRed3'

[im3](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].imshow([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([im3](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\])
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].set\_title("Alpha = 1")

\# Or as yet another variation, we can replace the rcParams
\# specification \*before\* the imshow with the following \*after\*
\# imshow.
\# This sets the new default \*and\* sets the colormap of the last
\# image-like item plotted via pyplot, if any.
#

\# Draw a line with low zorder so it will be behind the image.
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].plot(\[0, 10 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")\
\], \[0, 20 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")\
\], color\='c', lw\=20, zorder\=-1)

[im4](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].imshow([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([im4](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\])

\# Here it is: changing the colormap for the current image and its
\# colorbar after they have been plotted.
[im4.set\_cmap](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_cmap "matplotlib.colorizer._ColorizerInterface.set_cmap")
('BlueRedAlpha')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].set\_title("Varying alpha")

[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Custom Blue-Red colormaps', fontsize\=16)
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(top\=0.9)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Custom Blue-Red colormaps, Alpha = 1, Varying alpha](https://matplotlib.org/stable/_images/sphx_glr_custom_cmap_002_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
     / [`matplotlib.pyplot.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
    
*   [`matplotlib.figure.Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
     / [`matplotlib.pyplot.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
    
*   [`matplotlib.colors`](https://matplotlib.org/stable/api/colors_api.html#module-matplotlib.colors "matplotlib.colors")
    
*   [`matplotlib.colors.LinearSegmentedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
    
*   [`matplotlib.colors.LinearSegmentedColormap.from_list`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap.from_list "matplotlib.colors.LinearSegmentedColormap.from_list")
    
*   [`matplotlib.cm`](https://matplotlib.org/stable/api/cm_api.html#module-matplotlib.cm "matplotlib.cm")
    
*   [`matplotlib.cm.ScalarMappable.set_cmap`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable.set_cmap "matplotlib.cm.ScalarMappable.set_cmap")
    
*   [`matplotlib.cm.ColormapRegistry.register`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.register "matplotlib.cm.ColormapRegistry.register")
    

Tags: [styling: colormap](https://matplotlib.org/stable/_tags/styling-colormap.html)
 [plot-type: imshow](https://matplotlib.org/stable/_tags/plot-type-imshow.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

**Total running time of the script:** (0 minutes 2.869 seconds)

[`Download Jupyter notebook: custom_cmap.ipynb`](https://matplotlib.org/stable/_downloads/26f5b5c2451ffd373350d617a08d2e7d/custom_cmap.ipynb)

[`Download Python source code: custom_cmap.py`](https://matplotlib.org/stable/_downloads/fba15be770735fdb1b9272eaaf80104e/custom_cmap.py)

[`Download zipped: custom_cmap.zip`](https://matplotlib.org/stable/_downloads/5362b2cabb593f911a3d98f4e4fc612f/custom_cmap.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page