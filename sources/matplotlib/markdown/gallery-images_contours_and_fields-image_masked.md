[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_masked.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_masked.html#sphx-glr-download-gallery-images-contours-and-fields-image-masked-py)
 to download the full example code.

Image with masked values[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_masked.html#image-with-masked-values "Link to this heading")

================================================================================================================================================================

imshow with masked array input and out-of-range colors.

The second subplot illustrates the use of BoundaryNorm to get a filled contour effect.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.colors as colors

\# compute some interesting data
[x0](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [x1](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= \-5, 5
[y0](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [y1](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= \-3, 3
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
([x0](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [x1](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 500)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
([y0](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [y1](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 500)
[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[Z1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2 \- [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2)
[Z2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 1)\*\*2 \- ([Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 1)\*\*2)
[Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= ([Z1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- [Z2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* 2

\# Set up a colormap:
[palette](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
 \= [plt.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["gray"\].with\_extremes(over\='r', under\='g', bad\='b')
\# Alternatively, we could use
\# palette.set\_bad(alpha = 0.0)
\# to make the bad region transparent.  This is the default.
\# If you comment out all the palette.set\* lines, you will see
\# all the defaults; under and over will be colored with the
\# first and last colors in the palette, respectively.
[Zm](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 \= [np.ma.masked\_where](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_where.html#numpy.ma.masked_where "numpy.ma.masked_where")
([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \> 1.2, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# By setting vmin and vmax in the norm, we establish the
\# range to which the regular palette color scale is applied.
\# Anything above that range is colored based on palette.set\_over, etc.

\# set up the Axes objects
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, figsize\=(6, 5.4))

\# plot using 'continuous' colormap
[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax1.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([Zm](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, interpolation\='bilinear',
                cmap\=[palette](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
,
                norm\=[colors.Normalize](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
(vmin\=-1.0, vmax\=1.0),
                aspect\='auto',
                origin\='lower',
                extent\=\[[x0](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [x1](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [y0](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [y1](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\])
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Green=low, Red=high, Blue=masked')
[cbar](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 \= [fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, extend\='both', shrink\=0.9, ax\=[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
[cbar.set\_label](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.set_label "matplotlib.colorbar.Colorbar.set_label")
('uniform')
[ax1.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(axis\='x', labelbottom\=False)

\# Plot using a small number of colors, with unevenly spaced boundaries.
[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax2.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([Zm](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, interpolation\='nearest',
                cmap\=[palette](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
,
                norm\=[colors.BoundaryNorm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
(\[\-1, \-0.5, \-0.2, 0, 0.2, 0.5, 1\],
                                         ncolors\=[palette.N](https://docs.python.org/3/library/functions.html#int "builtins.int")
),
                aspect\='auto',
                origin\='lower',
                extent\=\[[x0](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [x1](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [y0](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [y1](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\])
[ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('With BoundaryNorm')
[cbar](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 \= [fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, extend\='both', spacing\='proportional',
                    shrink\=0.9, ax\=[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
[cbar.set\_label](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.set_label "matplotlib.colorbar.Colorbar.set_label")
('proportional')

[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('imshow, with out-of-range and masked data')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![imshow, with out-of-range and masked data, Green=low, Red=high, Blue=masked, With BoundaryNorm](https://matplotlib.org/stable/_images/sphx_glr_image_masked_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
     / [`matplotlib.pyplot.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
    
*   [`matplotlib.figure.Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
     / [`matplotlib.pyplot.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
    
*   [`matplotlib.colors.BoundaryNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
    
*   [`matplotlib.colorbar.Colorbar.set_label`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.set_label "matplotlib.colorbar.Colorbar.set_label")
    

**Total running time of the script:** (0 minutes 1.238 seconds)

[`Download Jupyter notebook: image_masked.ipynb`](https://matplotlib.org/stable/_downloads/3c70239ca296fbd6f0e0258d94b81620/image_masked.ipynb)

[`Download Python source code: image_masked.py`](https://matplotlib.org/stable/_downloads/455c7369df685db431cee2fd16862fdd/image_masked.py)

[`Download zipped: image_masked.zip`](https://matplotlib.org/stable/_downloads/02364fe9e55f3dfcd38ea93f7be43beb/image_masked.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)