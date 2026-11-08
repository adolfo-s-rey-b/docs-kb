[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_transparency_blend.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_transparency_blend.html#sphx-glr-download-gallery-images-contours-and-fields-image-transparency-blend-py)
 to download the full example code.

Blend transparency with color in 2D images[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_transparency_blend.html#blend-transparency-with-color-in-2d-images "Link to this heading")

================================================================================================================================================================================================================

Blend transparency with color to highlight parts of data with imshow.

A common use for [`matplotlib.pyplot.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
 is to plot a 2D statistical map. The function makes it easy to visualize a 2D matrix as an image and add transparency to the output. For example, one can plot a statistic (such as a t-statistic) and color the transparency of each pixel according to its p-value. This example demonstrates how you can achieve this effect.

First we will generate some data, in this case, we'll create two 2D "blobs" in a 2D grid. One blob will be positive, and the other negative.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import [Normalize](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")

def normal\_pdf(x, mean, [var](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    return [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-(x \- mean)\*\*2 / (2\*[var](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
))

\# Generate the space in which the blobs will live
[xmin](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [xmax](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ymin](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ymax](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= (0, 100, 0, 100)
[n\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 100
[xx](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
([xmin](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [xmax](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [n\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[yy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
([ymin](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ymax](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [n\_bins](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

\# Generate the blobs. The range of the values is roughly -.0002 to .0002
[means\_high](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[20, 50\]
[means\_low](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[50, 60\]
[var](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[150, 200\]

[gauss\_x\_high](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= normal\_pdf([xx](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [means\_high](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\], [var](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\])
[gauss\_y\_high](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= normal\_pdf([yy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [means\_high](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[1\], [var](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\])

[gauss\_x\_low](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= normal\_pdf([xx](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [means\_low](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\], [var](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[1\])
[gauss\_y\_low](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= normal\_pdf([yy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [means\_low](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[1\], [var](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[1\])

[weights](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= ([np.outer](https://numpy.org/doc/stable/reference/generated/numpy.outer.html#numpy.outer "numpy.outer")
([gauss\_y\_high](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [gauss\_x\_high](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
           \- [np.outer](https://numpy.org/doc/stable/reference/generated/numpy.outer.html#numpy.outer "numpy.outer")
([gauss\_y\_low](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [gauss\_x\_low](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))

\# We'll also create a grey background into which the pixels will fade
[greys](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.full](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")
((\*[weights.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, 3), 70, dtype\=[np.uint8](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")
)

\# First we'll plot these blobs using \`\`imshow\`\` without transparency.
[vmax](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [np.abs](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([weights](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
).max()
[imshow\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {
    'vmax': [vmax](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
,
    'vmin': \-[vmax](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
,
    'cmap': 'RdYlBu',
    'extent': ([xmin](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [xmax](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ymin](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ymax](https://docs.python.org/3/library/functions.html#int "builtins.int")
),
}

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([greys](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([weights](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \*\*[imshow\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[ax.set\_axis\_off](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_off.html#matplotlib.axes.Axes.set_axis_off "matplotlib.axes.Axes.set_axis_off")
()

![image transparency blend](https://matplotlib.org/stable/_images/sphx_glr_image_transparency_blend_001_2_00x.png)

Blending in transparency[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_transparency_blend.html#blending-in-transparency "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The simplest way to include transparency when plotting data with [`matplotlib.pyplot.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
 is to pass an array matching the shape of the data to the `alpha` argument. For example, we'll create a gradient moving from left to right below.

\# Create an alpha channel of linearly increasing values moving to the right.
[alphas](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 \= [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
([weights.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)
[alphas](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
\[:, 30:\] \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(1, 0, 70)

\# Create the figure and image
\# Note that the absolute values may be slightly different
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([greys](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([weights](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, alpha\=[alphas](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, \*\*[imshow\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[ax.set\_axis\_off](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_off.html#matplotlib.axes.Axes.set_axis_off "matplotlib.axes.Axes.set_axis_off")
()

![image transparency blend](https://matplotlib.org/stable/_images/sphx_glr_image_transparency_blend_002_2_00x.png)

Using transparency to highlight values with high amplitude[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_transparency_blend.html#using-transparency-to-highlight-values-with-high-amplitude "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Finally, we'll recreate the same plot, but this time we'll use transparency to highlight the extreme values in the data. This is often used to highlight data points with smaller p-values. We'll also add in contour lines to highlight the image values.

\# Create an alpha channel based on weight values
\# Any value whose absolute value is > .0001 will have zero transparency
[alphas](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 \= [Normalize](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
(0, .3, clip\=True)([np.abs](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([weights](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))
[alphas](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 \= [np.clip](https://numpy.org/doc/stable/reference/generated/numpy.clip.html#numpy.clip "numpy.clip")
([alphas](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, .4, 1)  \# alpha value clipped at the bottom at .4

\# Create the figure and image
\# Note that the absolute values may be slightly different
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([greys](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([weights](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, alpha\=[alphas](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, \*\*[imshow\_kwargs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

\# Add contour lines to further highlight different levels.
[ax.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
([weights](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[::\-1\], levels\=\[\-.1, .1\], colors\='k', linestyles\='-')
[ax.set\_axis\_off](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_off.html#matplotlib.axes.Axes.set_axis_off "matplotlib.axes.Axes.set_axis_off")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[ax.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
([weights](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[::\-1\], levels\=\[\-.0001, .0001\], colors\='k', linestyles\='-')
[ax.set\_axis\_off](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_off.html#matplotlib.axes.Axes.set_axis_off "matplotlib.axes.Axes.set_axis_off")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![image transparency blend](https://matplotlib.org/stable/_images/sphx_glr_image_transparency_blend_003_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
     / [`matplotlib.pyplot.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
    
*   [`matplotlib.axes.Axes.contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
     / [`matplotlib.pyplot.contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
    
*   [`matplotlib.colors.Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
    
*   [`matplotlib.axes.Axes.set_axis_off`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_off.html#matplotlib.axes.Axes.set_axis_off "matplotlib.axes.Axes.set_axis_off")
    

[`Download Jupyter notebook: image_transparency_blend.ipynb`](https://matplotlib.org/stable/_downloads/d79f0b2ef4fc0669703e8de6a3edc5b9/image_transparency_blend.ipynb)

[`Download Python source code: image_transparency_blend.py`](https://matplotlib.org/stable/_downloads/f916babc2a191fb56bf15aadecb3bae1/image_transparency_blend.py)

[`Download zipped: image_transparency_blend.zip`](https://matplotlib.org/stable/_downloads/14b7dee82206b088ff3767916333845d/image_transparency_blend.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page