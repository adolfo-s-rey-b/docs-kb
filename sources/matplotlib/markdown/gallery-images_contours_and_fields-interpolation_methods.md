[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/interpolation_methods.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/interpolation_methods.html#sphx-glr-download-gallery-images-contours-and-fields-interpolation-methods-py)
 to download the full example code.

Interpolations for imshow[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/interpolation_methods.html#interpolations-for-imshow "Link to this heading")

===========================================================================================================================================================================

This example displays the difference between interpolation methods for [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
.

If _interpolation_ is None, it defaults to the `[rcParams["image.interpolation"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.interpolation#rcparam-image-interpolation) ` (default: `'auto'`). If the interpolation is `'none'`, then no interpolation is performed for the Agg, ps and pdf backends. Other backends will default to `'auto'`.

For the Agg, ps and pdf backends, `interpolation='none'` works well when a big image is scaled down, while `interpolation='nearest'` works well when a small image is scaled up.

See [Image resampling](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_antialiasing.html)
 for a discussion on the default `interpolation='auto'` option.

import matplotlib.pyplot as plt
import numpy as np

[methods](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16',\
           'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',\
           'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos'\]

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[grid](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(4, 4)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=3, ncols\=6, figsize\=(9, 6),
                        subplot\_kw\={'xticks': \[\], 'yticks': \[\]})

for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [interp\_method](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in zip([axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
, [methods](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([grid](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, interpolation\=[interp\_method](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, cmap\='viridis')
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
(str([interp\_method](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
))

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![None, none, nearest, bilinear, bicubic, spline16, spline36, hanning, hamming, hermite, kaiser, quadric, catrom, gaussian, bessel, mitchell, sinc, lanczos](https://matplotlib.org/stable/_images/sphx_glr_interpolation_methods_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
     / [`matplotlib.pyplot.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
    

**Total running time of the script:** (0 minutes 2.323 seconds)

[`Download Jupyter notebook: interpolation_methods.ipynb`](https://matplotlib.org/stable/_downloads/0f724583c62896dfe11a7d36b7e64ea4/interpolation_methods.ipynb)

[`Download Python source code: interpolation_methods.py`](https://matplotlib.org/stable/_downloads/1b7a83577fbe998fc2f1a84e50c81939/interpolation_methods.py)

[`Download zipped: interpolation_methods.zip`](https://matplotlib.org/stable/_downloads/ba7783a302328a21e3c1e55123a8be61/interpolation_methods.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)