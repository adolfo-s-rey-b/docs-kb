[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/multi_image.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/multi_image.html#sphx-glr-download-gallery-images-contours-and-fields-multi-image-py)
 to download the full example code.

Multiple images with one colorbar[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/multi_image.html#multiple-images-with-one-colorbar "Link to this heading")

=================================================================================================================================================================================

Use a single colorbar for multiple images.

Currently, a colorbar can only be connected to one image. The connection guarantees that the data coloring is consistent with the colormap scale (i.e. the color of value _x_ in the colormap is used for coloring a data value _x_ in the image).

If we want one colorbar to be representative for multiple images, we have to explicitly ensure consistent data coloring by using the same data-to-color pipeline for all the images. We ensure this by explicitly creating a [`matplotlib.colorizer.Colorizer`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
 object that we pass to all the image plotting methods.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.colorizer as mcolorizer
import matplotlib.colors as mcolors

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[datasets](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\
    (i+1)/10 \* [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")\
(10, 20)\
    for i in range(4)\
\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2)
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Multiple images')

\# create a colorizer with a predefined norm to be shared across all images
[norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
 \= [mcolors.Normalize](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
(vmin\=[np.min](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "numpy.min")
([datasets](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
), vmax\=[np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
([datasets](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
))
[colorizer](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
 \= [mcolorizer.Colorizer](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
([norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
\=[norm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
)

[images](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\]
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 in zip([axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
, [datasets](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [images](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.append([ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [colorizer](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
\=[colorizer](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
))

[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([images](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\], [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, orientation\='horizontal', fraction\=.1)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Multiple images](https://matplotlib.org/stable/_images/sphx_glr_multi_image_001_2_00x.png)

The colors are now kept consistent across all images when changing the scaling, e.g. through zooming in the colorbar or via the "edit axis, curves and images parameters" GUI of the Qt backend. Additionally, if the colormap of the colorizer is changed, (e.g. through the "edit axis, curves and images parameters" GUI of the Qt backend) this change propagates to the other plots and the colorbar.

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
     / [`matplotlib.pyplot.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
    
*   [`matplotlib.figure.Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
     / [`matplotlib.pyplot.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
    
*   [`matplotlib.colorizer.Colorizer`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
    
*   [`matplotlib.colors.Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
    

[`Download Jupyter notebook: multi_image.ipynb`](https://matplotlib.org/stable/_downloads/958ba75a83e53893ae8c26ee5d0ebeb2/multi_image.ipynb)

[`Download Python source code: multi_image.py`](https://matplotlib.org/stable/_downloads/3d9ed4bd74fec2fd15978e0cd1497919/multi_image.py)

[`Download zipped: multi_image.zip`](https://matplotlib.org/stable/_downloads/4d70005190751ba7774b6f67e1e5b335/multi_image.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)