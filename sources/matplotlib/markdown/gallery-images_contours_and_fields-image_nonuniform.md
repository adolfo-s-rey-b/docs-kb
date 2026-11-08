[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_nonuniform.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_nonuniform.html#sphx-glr-download-gallery-images-contours-and-fields-image-nonuniform-py)
 to download the full example code.

Image nonuniform[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_nonuniform.html#image-nonuniform "Link to this heading")

====================================================================================================================================================

[`NonUniformImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage "matplotlib.image.NonUniformImage")
 is a generalized image with pixels on a rectilinear grid, i.e. it allows rows and columns with individual heights / widths.

There is no high-level plotting method on [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 or [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 to create a NonUniformImage. Instead, you have to instantiate the image explicitly add it to the Axes using [`Axes.add_image`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_image.html#matplotlib.axes.Axes.add_image "matplotlib.axes.Axes.add_image")
.

![NonUniformImage class, nearest, nearest, bilinear, bilinear](https://matplotlib.org/stable/_images/sphx_glr_image_nonuniform_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.image import [NonUniformImage](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage "matplotlib.image.NonUniformImage")

[interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= 'nearest'

\# Linear x array for cell centers:
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-4, 4, 9)

\# Highly nonlinear x array:
[x2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*3

[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-4, 4, 9)

[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
, :\]\*\*2 + [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]\*\*2)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, ncols\=2, layout\='constrained')
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('NonUniformImage class', fontsize\='large')
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\]
[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage "matplotlib.image.NonUniformImage")
 \= [NonUniformImage](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage "matplotlib.image.NonUniformImage")
([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, interpolation\=[interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, extent\=(\-4, 4, \-4, 4),
                     cmap\="Purples")
[im.set\_data](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage.set_data "matplotlib.image.NonUniformImage.set_data")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.add\_image](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_image.html#matplotlib.axes.Axes.add_image "matplotlib.axes.Axes.add_image")
([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage "matplotlib.image.NonUniformImage")
)
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(\-4, 4)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\-4, 4)
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
([interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\]
[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage "matplotlib.image.NonUniformImage")
 \= [NonUniformImage](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage "matplotlib.image.NonUniformImage")
([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, interpolation\=[interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, extent\=(\-64, 64, \-4, 4),
                     cmap\="Purples")
[im.set\_data](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage.set_data "matplotlib.image.NonUniformImage.set_data")
([x2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.add\_image](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_image.html#matplotlib.axes.Axes.add_image "matplotlib.axes.Axes.add_image")
([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage "matplotlib.image.NonUniformImage")
)
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(\-64, 64)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\-4, 4)
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
([interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

[interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= 'bilinear'

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\]
[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage "matplotlib.image.NonUniformImage")
 \= [NonUniformImage](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage "matplotlib.image.NonUniformImage")
([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, interpolation\=[interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, extent\=(\-4, 4, \-4, 4),
                     cmap\="Purples")
[im.set\_data](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage.set_data "matplotlib.image.NonUniformImage.set_data")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.add\_image](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_image.html#matplotlib.axes.Axes.add_image "matplotlib.axes.Axes.add_image")
([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage "matplotlib.image.NonUniformImage")
)
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(\-4, 4)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\-4, 4)
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
([interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\]
[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage "matplotlib.image.NonUniformImage")
 \= [NonUniformImage](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage "matplotlib.image.NonUniformImage")
([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, interpolation\=[interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, extent\=(\-64, 64, \-4, 4),
                     cmap\="Purples")
[im.set\_data](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage.set_data "matplotlib.image.NonUniformImage.set_data")
([x2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.add\_image](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_image.html#matplotlib.axes.Axes.add_image "matplotlib.axes.Axes.add_image")
([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage "matplotlib.image.NonUniformImage")
)
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(\-64, 64)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\-4, 4)
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
([interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 1.911 seconds)

[`Download Jupyter notebook: image_nonuniform.ipynb`](https://matplotlib.org/stable/_downloads/c2aacf36b8871ca0f2235e2803662802/image_nonuniform.ipynb)

[`Download Python source code: image_nonuniform.py`](https://matplotlib.org/stable/_downloads/cfc16c13f4a562ee23bf206246c5da51/image_nonuniform.py)

[`Download zipped: image_nonuniform.zip`](https://matplotlib.org/stable/_downloads/9f19a96c5fe85f8e4d515bb3dd031b53/image_nonuniform.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)