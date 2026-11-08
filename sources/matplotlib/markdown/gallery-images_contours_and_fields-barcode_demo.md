[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/barcode_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/barcode_demo.html#sphx-glr-download-gallery-images-contours-and-fields-barcode-demo-py)
 to download the full example code.

Barcode[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/barcode_demo.html#barcode "Link to this heading")

==============================================================================================================================

This demo shows how to produce a bar code.

The figure size is calculated so that the width in pixels is a multiple of the number of data points to prevent interpolation artifacts. Additionally, the `Axes` is defined to span the whole figure and all `Axis` are turned off.

The data itself is rendered with [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 using

*   `code.reshape(1, -1)` to turn the data into a 2D array with one row.
    
*   `imshow(..., aspect='auto')` to allow for non-square pixels.
    
*   `imshow(..., interpolation='nearest')` to prevent blurred edges. This should not happen anyway because we fine-tuned the figure width in pixels, but just to be safe.
    

import matplotlib.pyplot as plt
import numpy as np

[code](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\
    1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1,\
    0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0,\
    1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1,\
    1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1\])

[pixel\_per\_bar](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 4
[dpi](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 100

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(len([code](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* [pixel\_per\_bar](https://docs.python.org/3/library/functions.html#int "builtins.int")
 / [dpi](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 2), [dpi](https://docs.python.org/3/library/functions.html#int "builtins.int")
\=[dpi](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0, 0, 1, 1))  \# span the whole figure
[ax.set\_axis\_off](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_off.html#matplotlib.axes.Axes.set_axis_off "matplotlib.axes.Axes.set_axis_off")
()
[ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([code](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.reshape(1, \-1), cmap\='binary', aspect\='auto',
          interpolation\='nearest')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![barcode demo](https://matplotlib.org/stable/_images/sphx_glr_barcode_demo_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
     / [`matplotlib.pyplot.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
    
*   [`matplotlib.figure.Figure.add_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
    

Tags: [component: axes](https://matplotlib.org/stable/_tags/component-axes.html)
 [plot-type: imshow](https://matplotlib.org/stable/_tags/plot-type-imshow.html)
 [purpose: fun](https://matplotlib.org/stable/_tags/purpose-fun.html)

[`Download Jupyter notebook: barcode_demo.ipynb`](https://matplotlib.org/stable/_downloads/629441a6e97357694a3ec20ea8a6711f/barcode_demo.ipynb)

[`Download Python source code: barcode_demo.py`](https://matplotlib.org/stable/_downloads/7773e82aca62130e700b147505be37d4/barcode_demo.py)

[`Download zipped: barcode_demo.zip`](https://matplotlib.org/stable/_downloads/40935b0d9445938592149d16a81c21d5/barcode_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)