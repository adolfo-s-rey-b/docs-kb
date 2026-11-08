[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_face_compress.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_face_compress.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_face_compress.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_face_compress.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_face_compress.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_face_compress.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_face_compress.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_face_compress.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_face_compress.html#sphx-glr-download-auto-examples-cluster-plot-face-compress-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Vector Quantization Example[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_face_compress.html#vector-quantization-example "Link to this heading")

=================================================================================================================================================================

This example shows how one can use [`KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
 to perform vector quantization on a set of toy image, the raccoon face.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Original image[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_face_compress.html#original-image "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

We start by loading the raccoon face image from SciPy. We will additionally check a couple of information regarding the image, such as the shape and data type used to store the image.

from scipy.datasets import [face](https://docs.scipy.org/doc/scipy/reference/generated/scipy.datasets.face.html#scipy.datasets.face "scipy.datasets.face")

raccoon\_face \= [face](https://docs.scipy.org/doc/scipy/reference/generated/scipy.datasets.face.html#scipy.datasets.face "scipy.datasets.face")
(gray\=True)

print(f"The dimension of the image is {raccoon\_face.shape}")
print(f"The data used to encode the image is of type {raccoon\_face.dtype}")
print(f"The number of bytes taken in RAM is {raccoon\_face.nbytes}")

Copy to clipboard

The dimension of the image is (768, 1024)
The data used to encode the image is of type uint8
The number of bytes taken in RAM is 786432

Copy to clipboard

Thus the image is a 2D array of 768 pixels in height and 1024 pixels in width. Each value is an 8-bit unsigned integer, which means that the image is encoded using 8 bits per pixel. The total memory usage of the image is 786 kilobytes (1 byte equals 8 bits).

Using 8-bit unsigned integer means that the image is encoded using 256 different shades of gray, at most. We can check the distribution of these values.

import matplotlib.pyplot as plt

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, figsize\=(12, 4))

ax\[0\].imshow(raccoon\_face, cmap\=plt.cm.gray)
ax\[0\].axis("off")
ax\[0\].set\_title("Rendering of the image")
ax\[1\].hist(raccoon\_face.ravel(), bins\=256)
ax\[1\].set\_xlabel("Pixel value")
ax\[1\].set\_ylabel("Count of pixels")
ax\[1\].set\_title("Distribution of the pixel values")
\_ \= fig.suptitle("Original image of a raccoon face")

Copy to clipboard

![Original image of a raccoon face, Rendering of the image, Distribution of the pixel values](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_compress_001.png)

Compression via vector quantization[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_face_compress.html#compression-via-vector-quantization "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The idea behind compression via vector quantization is to reduce the number of gray levels to represent an image. For instance, we can use 8 values instead of 256 values. Therefore, it means that we could efficiently use 3 bits instead of 8 bits to encode a single pixel and therefore reduce the memory usage by a factor of approximately 2.5. We will later discuss about this memory usage.

### Encoding strategy[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_face_compress.html#encoding-strategy "Link to this heading")

The compression can be done using a [`KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
. We need to choose a strategy to define the 8 gray values to sub-sample. The simplest strategy is to define them equally spaced, which correspond to setting `strategy="uniform"`. From the previous histogram, we know that this strategy is certainly not optimal.

from sklearn.preprocessing import [KBinsDiscretizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")

n\_bins \= 8
encoder \= [KBinsDiscretizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
(
    n\_bins\=n\_bins,
    encode\="ordinal",
    strategy\="uniform",
    random\_state\=0,
)
compressed\_raccoon\_uniform \= encoder.fit\_transform(raccoon\_face.reshape(\-1, 1)).reshape(
    raccoon\_face.shape
)

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, figsize\=(12, 4))
ax\[0\].imshow(compressed\_raccoon\_uniform, cmap\=plt.cm.gray)
ax\[0\].axis("off")
ax\[0\].set\_title("Rendering of the image")
ax\[1\].hist(compressed\_raccoon\_uniform.ravel(), bins\=256)
ax\[1\].set\_xlabel("Pixel value")
ax\[1\].set\_ylabel("Count of pixels")
ax\[1\].set\_title("Sub-sampled distribution of the pixel values")
\_ \= fig.suptitle("Raccoon face compressed using 3 bits and a uniform strategy")

Copy to clipboard

![Raccoon face compressed using 3 bits and a uniform strategy, Rendering of the image, Sub-sampled distribution of the pixel values](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_compress_002.png)

Qualitatively, we can spot some small regions where we see the effect of the compression (e.g. leaves on the bottom right corner). But after all, the resulting image is still looking good.

We observe that the distribution of pixels values have been mapped to 8 different values. We can check the correspondence between such values and the original pixel values.

bin\_edges \= encoder.bin\_edges\_\[0\]
bin\_center \= bin\_edges\[:\-1\] + (bin\_edges\[1:\] \- bin\_edges\[:\-1\]) / 2
bin\_center

Copy to clipboard

array(\[ 15.5625,  46.6875,  77.8125, 108.9375, 140.0625, 171.1875,\
       202.3125, 233.4375\])

Copy to clipboard

\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
ax.hist(raccoon\_face.ravel(), bins\=256)
color \= "tab:orange"
for center in bin\_center:
    ax.axvline(center, color\=color)
    ax.text(center \- 10, ax.get\_ybound()\[1\] + 100, f"{center:.1f}", color\=color)

Copy to clipboard

![plot face compress](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_compress_003.png)

As previously stated, the uniform sampling strategy is not optimal. Notice for instance that the pixels mapped to the value 7 will encode a rather small amount of information, whereas the mapped value 3 will represent a large amount of counts. We can instead use a clustering strategy such as k-means to find a more optimal mapping.

encoder \= [KBinsDiscretizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
(
    n\_bins\=n\_bins,
    encode\="ordinal",
    strategy\="kmeans",
    random\_state\=0,
)
compressed\_raccoon\_kmeans \= encoder.fit\_transform(raccoon\_face.reshape(\-1, 1)).reshape(
    raccoon\_face.shape
)

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, figsize\=(12, 4))
ax\[0\].imshow(compressed\_raccoon\_kmeans, cmap\=plt.cm.gray)
ax\[0\].axis("off")
ax\[0\].set\_title("Rendering of the image")
ax\[1\].hist(compressed\_raccoon\_kmeans.ravel(), bins\=256)
ax\[1\].set\_xlabel("Pixel value")
ax\[1\].set\_ylabel("Number of pixels")
ax\[1\].set\_title("Distribution of the pixel values")
\_ \= fig.suptitle("Raccoon face compressed using 3 bits and a K-means strategy")

Copy to clipboard

![Raccoon face compressed using 3 bits and a K-means strategy, Rendering of the image, Distribution of the pixel values](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_compress_004.png)

bin\_edges \= encoder.bin\_edges\_\[0\]
bin\_center \= bin\_edges\[:\-1\] + (bin\_edges\[1:\] \- bin\_edges\[:\-1\]) / 2
bin\_center

Copy to clipboard

array(\[ 18.90934343,  53.33478066,  82.59678424, 109.22385188,\
       134.67876527, 159.67877978, 184.72384803, 223.17132867\])

Copy to clipboard

\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
ax.hist(raccoon\_face.ravel(), bins\=256)
color \= "tab:orange"
for center in bin\_center:
    ax.axvline(center, color\=color)
    ax.text(center \- 10, ax.get\_ybound()\[1\] + 100, f"{center:.1f}", color\=color)

Copy to clipboard

![plot face compress](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_compress_005.png)

The counts in the bins are now more balanced and their centers are no longer equally spaced. Note that we could enforce the same number of pixels per bin by using the `strategy="quantile"` instead of `strategy="kmeans"`.

### Memory footprint[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_face_compress.html#memory-footprint "Link to this heading")

We previously stated that we should save 8 times less memory. Let’s verify it.

print(f"The number of bytes taken in RAM is {compressed\_raccoon\_kmeans.nbytes}")
print(f"Compression ratio: {compressed\_raccoon\_kmeans.nbytes / raccoon\_face.nbytes}")

Copy to clipboard

The number of bytes taken in RAM is 6291456
Compression ratio: 8.0

Copy to clipboard

It is quite surprising to see that our compressed image is taking x8 more memory than the original image. This is indeed the opposite of what we expected. The reason is mainly due to the type of data used to encode the image.

print(f"Type of the compressed image: {compressed\_raccoon\_kmeans.dtype}")

Copy to clipboard

Type of the compressed image: float64

Copy to clipboard

Indeed, the output of the [`KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
 is an array of 64-bit float. It means that it takes x8 more memory. However, we use this 64-bit float representation to encode 8 values. Indeed, we will save memory only if we cast the compressed image into an array of 3-bits integers. We could use the method `numpy.ndarray.astype`. However, a 3-bits integer representation does not exist and to encode the 8 values, we would need to use the 8-bit unsigned integer representation as well.

In practice, observing a memory gain would require the original image to be in a 64-bit float representation.

**Total running time of the script:** (0 minutes 1.944 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_face_compress.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_face_compress.ipynb)

[`Download Jupyter notebook: plot_face_compress.ipynb`](https://scikit-learn.org/stable/_downloads/f52666c44d104a3e37802015751177fe/plot_face_compress.ipynb)

[`Download Python source code: plot_face_compress.py`](https://scikit-learn.org/stable/_downloads/5bb71b0b2052531cacf3736b4d2b3a92/plot_face_compress.py)

[`Download zipped: plot_face_compress.zip`](https://scikit-learn.org/stable/_downloads/07f60cdd0b8c83dd80140be675140b02/plot_face_compress.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_image_denoising_thumb.png)

[Image denoising using dictionary learning](https://scikit-learn.org/stable/auto_examples/decomposition/plot_image_denoising.html)

Image denoising using dictionary learning

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_classification_thumb.png)

[Recognizing hand-written digits](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html)

Recognizing hand-written digits

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_ward_segmentation_thumb.png)

[A demo of structured Ward hierarchical clustering on an image of coins](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_ward_segmentation.html)

A demo of structured Ward hierarchical clustering on an image of coins

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_segmentation_thumb.png)

[Segmenting the picture of greek coins in regions](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_segmentation.html)

Segmenting the picture of greek coins in regions

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/5bb71b0b2052531cacf3736b4d2b3a92/plot_face_compress.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/f52666c44d104a3e37802015751177fe/plot_face_compress.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/07f60cdd0b8c83dd80140be675140b02/plot_face_compress.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_face_compress.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_face_compress.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)