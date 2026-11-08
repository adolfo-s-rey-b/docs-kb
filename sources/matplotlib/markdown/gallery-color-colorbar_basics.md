[Skip to main content](https://matplotlib.org/stable/gallery/color/colorbar_basics.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/color/colorbar_basics.html#sphx-glr-download-gallery-color-colorbar-basics-py)
 to download the full example code.

Colorbar[#](https://matplotlib.org/stable/gallery/color/colorbar_basics.html#colorbar "Link to this heading")

==============================================================================================================

Use [`colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
 by specifying the mappable object (here the [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 returned by [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
) and the Axes to attach the colorbar to.

import matplotlib.pyplot as plt
import numpy as np

\# setup some generic data
[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 37
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.mgrid](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")
\[:[N](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, :[N](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]
[Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= ([np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*0.2) + [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*0.3))

\# mask out the negative and positive values, respectively
[Zpos](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 \= [np.ma.masked\_less](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_less.html#numpy.ma.masked_less "numpy.ma.masked_less")
([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 0)
[Zneg](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 \= [np.ma.masked\_greater](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_greater.html#numpy.ma.masked_greater "numpy.ma.masked_greater")
([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 0)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(13, 3), ncols\=3)

\# plot just the positive data and save the
\# color "mappable" object returned by ax1.imshow
[pos](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax1.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([Zpos](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, cmap\='Blues', interpolation\='none')

\# add the colorbar using the figure's method,
\# telling which mappable we're talking about and
\# which Axes object it should be near
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([pos](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, ax\=[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

\# repeat everything above for the negative data
\# you can specify location, anchor and shrink the colorbar
[neg](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax2.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([Zneg](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, cmap\='Reds\_r', interpolation\='none')
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([neg](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, ax\=[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, location\='right', anchor\=(0, 0.3), shrink\=0.7)

\# Plot both positive and negative values between +/- 1.2
[pos\_neg\_clipped](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax3.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, cmap\='RdBu', vmin\=-1.2, vmax\=1.2,
                             interpolation\='none')
\# Add minorticks on the colorbar to make it easy to read the
\# values off the colorbar.
[cbar](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 \= [fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([pos\_neg\_clipped](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, ax\=[ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, extend\='both')
[cbar.minorticks\_on](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.minorticks_on "matplotlib.colorbar.Colorbar.minorticks_on")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![colorbar basics](https://matplotlib.org/stable/_images/sphx_glr_colorbar_basics_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
     / [`matplotlib.pyplot.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
    
*   [`matplotlib.figure.Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
     / [`matplotlib.pyplot.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
    
*   [`matplotlib.colorbar.Colorbar.minorticks_on`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.minorticks_on "matplotlib.colorbar.Colorbar.minorticks_on")
    
*   [`matplotlib.colorbar.Colorbar.minorticks_off`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.minorticks_off "matplotlib.colorbar.Colorbar.minorticks_off")
    

Tags: [component: colorbar](https://matplotlib.org/stable/_tags/component-colorbar.html)
 [styling: color](https://matplotlib.org/stable/_tags/styling-color.html)
 [plot-type: imshow](https://matplotlib.org/stable/_tags/plot-type-imshow.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

**Total running time of the script:** (0 minutes 1.211 seconds)

[`Download Jupyter notebook: colorbar_basics.ipynb`](https://matplotlib.org/stable/_downloads/424a7cb6f32b2f8b69101c20554cf1de/colorbar_basics.ipynb)

[`Download Python source code: colorbar_basics.py`](https://matplotlib.org/stable/_downloads/642498711ab58d6f80ef376a375dda14/colorbar_basics.py)

[`Download zipped: colorbar_basics.zip`](https://matplotlib.org/stable/_downloads/7dc976a64d96595665512c8845bdcf26/colorbar_basics.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)