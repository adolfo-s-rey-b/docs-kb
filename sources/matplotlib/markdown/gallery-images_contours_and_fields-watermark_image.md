[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/watermark_image.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/watermark_image.html#sphx-glr-download-gallery-images-contours-and-fields-watermark-image-py)
 to download the full example code.

Watermark image[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/watermark_image.html#watermark-image "Link to this heading")

=================================================================================================================================================

Overlay an image on a plot by moving it to the front (`zorder=3`) and making it semi-transparent (`alpha=0.7`).

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cbook as cbook
import matplotlib.image as image

with [cbook.get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
('logo2.png') as file:
    [im](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [image.imread](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.imread "matplotlib.image.imread")
(file)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(30)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(30)
[ax.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\='#6bbc6b')
[ax.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
()

[fig.figimage](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.figimage.html#matplotlib.figure.Figure.figimage "matplotlib.figure.Figure.figimage")
([im](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 25, 25, zorder\=3, alpha\=.7)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![watermark image](https://matplotlib.org/stable/_images/sphx_glr_watermark_image_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.image`](https://matplotlib.org/stable/api/image_api.html#module-matplotlib.image "matplotlib.image")
    
*   [`matplotlib.image.imread`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.imread "matplotlib.image.imread")
     / [`matplotlib.pyplot.imread`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html#matplotlib.pyplot.imread "matplotlib.pyplot.imread")
    
*   [`matplotlib.figure.Figure.figimage`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.figimage.html#matplotlib.figure.Figure.figimage "matplotlib.figure.Figure.figimage")
    

[`Download Jupyter notebook: watermark_image.ipynb`](https://matplotlib.org/stable/_downloads/25e8a65dc5917bca00a73bcad495cd75/watermark_image.ipynb)

[`Download Python source code: watermark_image.py`](https://matplotlib.org/stable/_downloads/5f96e9c3090dbe1028725071e100d1bc/watermark_image.py)

[`Download zipped: watermark_image.zip`](https://matplotlib.org/stable/_downloads/3a5840160b4f09930bfdb739d30766be/watermark_image.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)