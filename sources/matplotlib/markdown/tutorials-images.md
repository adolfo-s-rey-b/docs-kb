[Skip to main content](https://matplotlib.org/stable/tutorials/images.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/tutorials/images.html#sphx-glr-download-tutorials-images-py)
 to download the full example code.

Image tutorial[#](https://matplotlib.org/stable/tutorials/images.html#image-tutorial "Link to this heading")

=============================================================================================================

This tutorial will use Matplotlib's implicit plotting interface, pyplot. This interface maintains global state, and is very useful for quickly and easily experimenting with various plot settings. The alternative is the explicit, which is more suitable for large application development. For an explanation of the tradeoffs between the implicit and explicit interfaces see [Matplotlib Application Interfaces (APIs)](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#api-interfaces)
 and the [Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html#quick-start)
 to start using the explicit interface. For now, let's get on with the implicit approach:

from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

Importing image data into Numpy arrays[#](https://matplotlib.org/stable/tutorials/images.html#importing-image-data-into-numpy-arrays "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

Matplotlib relies on the [Pillow](https://pillow.readthedocs.io/en/latest/)
 library to load image data.

Here's the image we're going to play with:

![../_images/stinkbug.png](https://matplotlib.org/stable/_images/stinkbug.png)

It's a 24-bit RGB PNG image (8 bits for each of R, G, B). Depending on where you get your data, the other kinds of image that you'll most likely encounter are RGBA images, which allow for transparency, or single-channel grayscale (luminosity) images. Download [stinkbug.png](https://raw.githubusercontent.com/matplotlib/matplotlib/main/doc/_static/stinkbug.png)
 to your computer for the rest of this tutorial.

We use Pillow to open an image (with [`PIL.Image.open`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open "(in Pillow (PIL Fork) v12.3.0)")
), and immediately convert the [`PIL.Image.Image`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image "(in Pillow (PIL Fork) v12.3.0)")
 object into an 8-bit (`dtype=uint8`) numpy array.

[img](https://pillow.readthedocs.io/en/stable/reference/plugins.html#PIL.PngImagePlugin.PngImageFile "PIL.PngImagePlugin.PngImageFile")
 \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
([Image.open](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open "PIL.Image.open")
('../../doc/\_static/stinkbug.png'))
print(repr([img](https://pillow.readthedocs.io/en/stable/reference/plugins.html#PIL.PngImagePlugin.PngImageFile "PIL.PngImagePlugin.PngImageFile")
))

array(\[\[\[104, 104, 104\],\
        \[104, 104, 104\],\
        \[104, 104, 104\],\
        ...,\
        \[109, 109, 109\],\
        \[109, 109, 109\],\
        \[109, 109, 109\]\],\
\
       \[\[105, 105, 105\],\
        \[105, 105, 105\],\
        \[105, 105, 105\],\
        ...,\
        \[109, 109, 109\],\
        \[109, 109, 109\],\
        \[109, 109, 109\]\],\
\
       \[\[107, 107, 107\],\
        \[106, 106, 106\],\
        \[106, 106, 106\],\
        ...,\
        \[110, 110, 110\],\
        \[110, 110, 110\],\
        \[110, 110, 110\]\],\
\
       ...,\
\
       \[\[112, 112, 112\],\
        \[111, 111, 111\],\
        \[110, 110, 110\],\
        ...,\
        \[116, 116, 116\],\
        \[115, 115, 115\],\
        \[115, 115, 115\]\],\
\
       \[\[113, 113, 113\],\
        \[113, 113, 113\],\
        \[112, 112, 112\],\
        ...,\
        \[115, 115, 115\],\
        \[114, 114, 114\],\
        \[114, 114, 114\]\],\
\
       \[\[113, 113, 113\],\
        \[115, 115, 115\],\
        \[115, 115, 115\],\
        ...,\
        \[114, 114, 114\],\
        \[114, 114, 114\],\
        \[113, 113, 113\]\]\], shape=(375, 500, 3), dtype=uint8)

Each inner list represents a pixel. Here, with an RGB image, there are 3 values. Since it's a black and white image, R, G, and B are all similar. An RGBA (where A is alpha, or transparency) has 4 values per inner list, and a simple luminance image just has one value (and is thus only a 2-D array, not a 3-D array). For RGB and RGBA images, Matplotlib supports float32 and uint8 data types. For grayscale, Matplotlib supports only float32. If your array data does not meet one of these descriptions, you need to rescale it.

Plotting numpy arrays as images[#](https://matplotlib.org/stable/tutorials/images.html#plotting-numpy-arrays-as-images "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

So, you have your data in a numpy array (either by importing it, or by generating it). Let's render it. In Matplotlib, this is performed using the [`imshow()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
 function. Here we'll grab the plot object. This object gives you an easy way to manipulate the plot from the prompt.

[imgplot](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
([img](https://pillow.readthedocs.io/en/stable/reference/plugins.html#PIL.PngImagePlugin.PngImageFile "PIL.PngImagePlugin.PngImageFile")
)

![images](https://matplotlib.org/stable/_images/sphx_glr_images_001_2_00x.png)

You can also plot any numpy array.

### Applying pseudocolor schemes to image plots[#](https://matplotlib.org/stable/tutorials/images.html#applying-pseudocolor-schemes-to-image-plots "Link to this heading")

Pseudocolor can be a useful tool for enhancing contrast and visualizing your data more easily. This is especially useful when making presentations of your data using projectors - their contrast is typically quite poor.

Pseudocolor is only relevant to single-channel, grayscale, luminosity images. We currently have an RGB image. Since R, G, and B are all similar (see for yourself above or in your data), we can just pick one channel of our data using array slicing (you can read more in the [Numpy tutorial](https://numpy.org/doc/stable/user/quickstart.html#indexing-slicing-and-iterating)
):

[lum\_img](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [img](https://pillow.readthedocs.io/en/stable/reference/plugins.html#PIL.PngImagePlugin.PngImageFile "PIL.PngImagePlugin.PngImageFile")
\[:, :, 0\]
[plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
([lum\_img](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

![images](https://matplotlib.org/stable/_images/sphx_glr_images_002_2_00x.png)

Now, with a luminosity (2D, no color) image, the default colormap (aka lookup table, LUT), is applied. The default is called viridis. There are plenty of others to choose from.

[plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
([lum\_img](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, cmap\="hot")

![images](https://matplotlib.org/stable/_images/sphx_glr_images_003_2_00x.png)

Note that you can also change colormaps on existing plot objects using the [`set_cmap()`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable.set_cmap "matplotlib.cm.ScalarMappable.set_cmap")
 method:

[imgplot](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
([lum\_img](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[imgplot.set\_cmap](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_cmap "matplotlib.colorizer._ColorizerInterface.set_cmap")
('nipy\_spectral')

![images](https://matplotlib.org/stable/_images/sphx_glr_images_004_2_00x.png)

There are many other colormap schemes available. See the [list and images of the colormaps](https://matplotlib.org/stable/users/explain/colors/colormaps.html#colormaps)
.

### Color scale reference[#](https://matplotlib.org/stable/tutorials/images.html#color-scale-reference "Link to this heading")

It's helpful to have an idea of what value a color represents. We can do that by adding a color bar to your figure:

[imgplot](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
([lum\_img](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
()

![images](https://matplotlib.org/stable/_images/sphx_glr_images_005_2_00x.png)

### Examining a specific data range[#](https://matplotlib.org/stable/tutorials/images.html#examining-a-specific-data-range "Link to this heading")

Sometimes you want to enhance the contrast in your image, or expand the contrast in a particular region while sacrificing the detail in colors that don't vary much, or don't matter. A good tool to find interesting regions is the histogram. To create a histogram of our image data, we use the [`hist()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist "matplotlib.pyplot.hist")
 function.

[plt.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist "matplotlib.pyplot.hist")
([lum\_img](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.ravel(), bins\=range(256), fc\='k', ec\='k')

![images](https://matplotlib.org/stable/_images/sphx_glr_images_006_2_00x.png)

Most often, the "interesting" part of the image is around the peak, and you can get extra contrast by clipping the regions above and/or below the peak. In our histogram, it looks like there's not much useful information in the high end (not many white things in the image). Let's adjust the upper limit, so that we effectively "zoom in on" part of the histogram. We do this by setting _clim_, the colormap limits.

This can be done by passing a _clim_ keyword argument in the call to `imshow`.

[plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
([lum\_img](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, clim\=(0, 175))

![images](https://matplotlib.org/stable/_images/sphx_glr_images_007_2_00x.png)

This can also be done by calling the [`set_clim()`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable.set_clim "matplotlib.cm.ScalarMappable.set_clim")
 method of the returned image plot object.

[imgplot](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
([lum\_img](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[imgplot.set\_clim](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_clim "matplotlib.colorizer._ColorizerInterface.set_clim")
(0, 175)

![images](https://matplotlib.org/stable/_images/sphx_glr_images_008_2_00x.png)

### Array Interpolation schemes[#](https://matplotlib.org/stable/tutorials/images.html#array-interpolation-schemes "Link to this heading")

Interpolation calculates what the color or value of a pixel "should" be, according to different mathematical schemes. One common place that this happens is when you resize an image. The number of pixels change, but you want the same information. Since pixels are discrete, there's missing space. Interpolation is how you fill that space. This is why your images sometimes come out looking pixelated when you blow them up. The effect is more pronounced when the difference between the original image and the expanded image is greater. Let's take our image and shrink it. We're effectively discarding pixels, only keeping a select few. Now when we plot it, that data gets blown up to the size on your screen. The old pixels aren't there anymore, and the computer has to draw in pixels to fill that space.

We'll use the Pillow library that we used to load the image also to resize the image.

[img](https://pillow.readthedocs.io/en/stable/reference/plugins.html#PIL.PngImagePlugin.PngImageFile "PIL.PngImagePlugin.PngImageFile")
 \= [Image.open](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open "PIL.Image.open")
('../../doc/\_static/stinkbug.png')
[img.thumbnail](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.thumbnail "PIL.Image.Image.thumbnail")
((64, 64))  \# resizes image in-place
[imgplot](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
([img](https://pillow.readthedocs.io/en/stable/reference/plugins.html#PIL.PngImagePlugin.PngImageFile "PIL.PngImagePlugin.PngImageFile")
)

![images](https://matplotlib.org/stable/_images/sphx_glr_images_009_2_00x.png)

Here we use the default interpolation ("nearest"), since we did not give [`imshow()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
 any interpolation argument.

Let's try some others. Here's "bilinear":

[imgplot](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
([img](https://pillow.readthedocs.io/en/stable/reference/plugins.html#PIL.PngImagePlugin.PngImageFile "PIL.PngImagePlugin.PngImageFile")
, interpolation\="bilinear")

![images](https://matplotlib.org/stable/_images/sphx_glr_images_010_2_00x.png)

and bicubic:

[imgplot](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
([img](https://pillow.readthedocs.io/en/stable/reference/plugins.html#PIL.PngImagePlugin.PngImageFile "PIL.PngImagePlugin.PngImageFile")
, interpolation\="bicubic")

![images](https://matplotlib.org/stable/_images/sphx_glr_images_011_2_00x.png)

Bicubic interpolation is often used when blowing up photos - people tend to prefer blurry over pixelated.

**Total running time of the script:** (0 minutes 8.791 seconds)

[`Download Jupyter notebook: images.ipynb`](https://matplotlib.org/stable/_downloads/33cdbcfd1b016e6cea1c03ad960b40ce/images.ipynb)

[`Download Python source code: images.py`](https://matplotlib.org/stable/_downloads/6da5ecb585bca3fd57ae9c5b9f7c8699/images.py)

[`Download zipped: images.zip`](https://matplotlib.org/stable/_downloads/09e23ac1295593e2867ca974c8cb5a22/images.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page