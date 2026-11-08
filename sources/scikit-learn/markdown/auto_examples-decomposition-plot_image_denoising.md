[Skip to main content](https://scikit-learn.org/stable/auto_examples/decomposition/plot_image_denoising.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/decomposition/plot_image_denoising.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/decomposition/plot_image_denoising.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/decomposition/plot_image_denoising.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/decomposition/plot_image_denoising.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/decomposition/plot_image_denoising.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/decomposition/plot_image_denoising.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/decomposition/plot_image_denoising.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/decomposition/plot_image_denoising.html#sphx-glr-download-auto-examples-decomposition-plot-image-denoising-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Image denoising using dictionary learning[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_image_denoising.html#image-denoising-using-dictionary-learning "Link to this heading")

=====================================================================================================================================================================================================

An example comparing the effect of reconstructing noisy fragments of a raccoon face image using firstly online [Dictionary Learning](https://scikit-learn.org/stable/modules/decomposition.html#dictionarylearning)
 and various transform methods.

The dictionary is fitted on the distorted left half of the image, and subsequently used to reconstruct the right half. Note that even better performance could be achieved by fitting to an undistorted (i.e. noiseless) image, but here we start from the assumption that it is not available.

A common practice for evaluating the results of image denoising is by looking at the difference between the reconstruction and the original image. If the reconstruction is perfect this will look like Gaussian noise.

It can be seen from the plots that the results of [Orthogonal Matching Pursuit (OMP)](https://scikit-learn.org/stable/modules/linear_model.html#omp)
 with two non-zero coefficients is a bit less biased than when keeping only one (the edges look less prominent). It is in addition closer from the ground truth in Frobenius norm.

The result of [Least Angle Regression](https://scikit-learn.org/stable/modules/linear_model.html#least-angle-regression)
 is much more strongly biased: the difference is reminiscent of the local intensity value of the original image.

Thresholding is clearly not useful for denoising, but it is here to show that it can produce a suggestive output with very high speed, and thus be useful for other tasks such as object classification, where performance is not necessarily related to visualisation.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate distorted image[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_image_denoising.html#generate-distorted-image "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np
from scipy.datasets import [face](https://docs.scipy.org/doc/scipy/reference/generated/scipy.datasets.face.html#scipy.datasets.face "scipy.datasets.face")

raccoon\_face \= [face](https://docs.scipy.org/doc/scipy/reference/generated/scipy.datasets.face.html#scipy.datasets.face "scipy.datasets.face")
(gray\=True)

\# Convert from uint8 representation with values between 0 and 255 to
\# a floating point representation with values between 0 and 1.
raccoon\_face \= raccoon\_face / 255.0

\# downsample for higher speed
raccoon\_face \= (
    raccoon\_face\[::4, ::4\]
    + raccoon\_face\[1::4, ::4\]
    + raccoon\_face\[::4, 1::4\]
    + raccoon\_face\[1::4, 1::4\]
)
raccoon\_face /= 4.0
height, width \= raccoon\_face.shape

\# Distort the right half of the image
print("Distorting image...")
distorted \= raccoon\_face.copy()
distorted\[:, width // 2 :\] += 0.075 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(height, width // 2)

Copy to clipboard

Distorting image...

Copy to clipboard

Display the distorted image[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_image_denoising.html#display-the-distorted-image "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

def show\_with\_diff(image, reference, title):
    """Helper function to display denoising"""
    [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(5, 3.3))
    [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(1, 2, 1)
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Image")
    [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(image, vmin\=0, vmax\=1, cmap\=plt.cm.gray, interpolation\="nearest")
    [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
    [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())
    [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(1, 2, 2)
    difference \= image \- reference

    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Difference (norm: %.2f)" % [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
([np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
(difference\*\*2)))
    [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(
        difference, vmin\=-0.5, vmax\=0.5, cmap\=plt.cm.PuOr, interpolation\="nearest"
    )
    [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
    [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())
    [plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
(title, size\=16)
    [plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(0.02, 0.02, 0.98, 0.79, 0.02, 0.2)

show\_with\_diff(distorted, raccoon\_face, "Distorted image")

Copy to clipboard

![Distorted image, Image, Difference (norm: 11.71)](https://scikit-learn.org/stable/_images/sphx_glr_plot_image_denoising_001.png)

Extract reference patches[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_image_denoising.html#extract-reference-patches "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

from sklearn.feature\_extraction.image import [extract\_patches\_2d](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html#sklearn.feature_extraction.image.extract_patches_2d "sklearn.feature_extraction.image.extract_patches_2d")

\# Extract all reference patches from the left half of the image
print("Extracting reference patches...")
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
patch\_size \= (7, 7)
data \= [extract\_patches\_2d](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html#sklearn.feature_extraction.image.extract_patches_2d "sklearn.feature_extraction.image.extract_patches_2d")
(distorted\[:, : width // 2\], patch\_size)
data \= data.reshape(data.shape\[0\], \-1)
data \-= [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(data, axis\=0)
data /= [np.std](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std")
(data, axis\=0)
print(f"{data.shape\[0\]} patches extracted in %.2fs." % ([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0))

Copy to clipboard

Extracting reference patches...
22692 patches extracted in 0.01s.

Copy to clipboard

Learn the dictionary from reference patches[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_image_denoising.html#learn-the-dictionary-from-reference-patches "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from sklearn.decomposition import [MiniBatchDictionaryLearning](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")

print("Learning the dictionary...")
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
dico \= [MiniBatchDictionaryLearning](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
(
    \# increase to 300 for higher quality results at the cost of slower
    \# training times.
    n\_components\=50,
    batch\_size\=200,
    alpha\=1.0,
    max\_iter\=10,
)
V \= dico.fit(data).components\_
dt \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0
print(f"{dico.n\_iter\_} iterations / {dico.n\_steps\_} steps in {dt:.2f}.")

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(4.2, 4))
for i, comp in enumerate(V\[:100\]):
    [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(10, 10, i + 1)
    [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(comp.reshape(patch\_size), cmap\=plt.cm.gray\_r, interpolation\="nearest")
    [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
    [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())
[plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
(
    "Dictionary learned from face patches\\n"
    + "Train time %.1fs on %d patches" % (dt, len(data)),
    fontsize\=16,
)
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(0.08, 0.02, 0.92, 0.85, 0.08, 0.23)

Copy to clipboard

![Dictionary learned from face patches Train time 15.8s on 22692 patches](https://scikit-learn.org/stable/_images/sphx_glr_plot_image_denoising_002.png)

Learning the dictionary...
1.0 iterations / 105 steps in 15.81.

Copy to clipboard

Extract noisy patches and reconstruct them using the dictionary[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_image_denoising.html#extract-noisy-patches-and-reconstruct-them-using-the-dictionary "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from sklearn.feature\_extraction.image import [reconstruct\_from\_patches\_2d](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.reconstruct_from_patches_2d.html#sklearn.feature_extraction.image.reconstruct_from_patches_2d "sklearn.feature_extraction.image.reconstruct_from_patches_2d")

print("Extracting noisy patches... ")
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
data \= [extract\_patches\_2d](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html#sklearn.feature_extraction.image.extract_patches_2d "sklearn.feature_extraction.image.extract_patches_2d")
(distorted\[:, width // 2 :\], patch\_size)
data \= data.reshape(data.shape\[0\], \-1)
intercept \= [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(data, axis\=0)
data \-= intercept
print("done in %.2fs." % ([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0))

transform\_algorithms \= \[\
    ("Orthogonal Matching Pursuit\\n1 atom", "omp", {"transform\_n\_nonzero\_coefs": 1}),\
    ("Orthogonal Matching Pursuit\\n2 atoms", "omp", {"transform\_n\_nonzero\_coefs": 2}),\
    ("Least-angle regression\\n4 atoms", "lars", {"transform\_n\_nonzero\_coefs": 4}),\
    ("Thresholding\\n alpha=0.1", "threshold", {"transform\_alpha": 0.1}),\
\]

reconstructions \= {}
for title, transform\_algorithm, kwargs in transform\_algorithms:
    print(title + "...")
    reconstructions\[title\] \= raccoon\_face.copy()
    t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    dico.set\_params(transform\_algorithm\=transform\_algorithm, \*\*kwargs)
    code \= dico.transform(data)
    patches \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(code, V)

    patches += intercept
    patches \= patches.reshape(len(data), \*patch\_size)
    if transform\_algorithm \== "threshold":
        patches \-= patches.min()
        patches /= patches.max()
    reconstructions\[title\]\[:, width // 2 :\] \= [reconstruct\_from\_patches\_2d](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.reconstruct_from_patches_2d.html#sklearn.feature_extraction.image.reconstruct_from_patches_2d "sklearn.feature_extraction.image.reconstruct_from_patches_2d")
(
        patches, (height, width // 2)
    )
    dt \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0
    print("done in %.2fs." % dt)
    show\_with\_diff(reconstructions\[title\], raccoon\_face, title + " (time: %.1fs)" % dt)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

*   ![Orthogonal Matching Pursuit 1 atom (time: 0.5s), Image, Difference (norm: 10.69)](https://scikit-learn.org/stable/_images/sphx_glr_plot_image_denoising_003.png)
*   ![Orthogonal Matching Pursuit 2 atoms (time: 1.4s), Image, Difference (norm: 9.29)](https://scikit-learn.org/stable/_images/sphx_glr_plot_image_denoising_004.png)
*   ![Least-angle regression 4 atoms (time: 9.8s), Image, Difference (norm: 13.34)](https://scikit-learn.org/stable/_images/sphx_glr_plot_image_denoising_005.png)
*   ![Thresholding  alpha=0.1 (time: 0.1s), Image, Difference (norm: 14.23)](https://scikit-learn.org/stable/_images/sphx_glr_plot_image_denoising_006.png)

Extracting noisy patches...
done in 0.00s.
Orthogonal Matching Pursuit
1 atom...
done in 0.52s.
Orthogonal Matching Pursuit
2 atoms...
done in 1.41s.
Least-angle regression
4 atoms...
done in 9.77s.
Thresholding
 alpha=0.1...
done in 0.09s.

Copy to clipboard

**Total running time of the script:** (0 minutes 28.461 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_image_denoising.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_image_denoising.ipynb)

[`Download Jupyter notebook: plot_image_denoising.ipynb`](https://scikit-learn.org/stable/_downloads/f726f6c50f1cc13e1afb7561fa005d16/plot_image_denoising.ipynb)

[`Download Python source code: plot_image_denoising.py`](https://scikit-learn.org/stable/_downloads/149ff4a0ff65a845f675cc7a0fcb86ea/plot_image_denoising.py)

[`Download zipped: plot_image_denoising.zip`](https://scikit-learn.org/stable/_downloads/5b58ff41853cd5fd1f2f388574fbf6db/plot_image_denoising.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_compress_thumb.png)

[Vector Quantization Example](https://scikit-learn.org/stable/auto_examples/cluster/plot_face_compress.html)

Vector Quantization Example

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_dict_face_patches_thumb.png)

[Online learning of a dictionary of parts of faces](https://scikit-learn.org/stable/auto_examples/cluster/plot_dict_face_patches.html)

Online learning of a dictionary of parts of faces

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_segmentation_thumb.png)

[Segmenting the picture of greek coins in regions](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_segmentation.html)

Segmenting the picture of greek coins in regions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_classification_thumb.png)

[Recognizing hand-written digits](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html)

Recognizing hand-written digits

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/149ff4a0ff65a845f675cc7a0fcb86ea/plot_image_denoising.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/f726f6c50f1cc13e1afb7561fa005d16/plot_image_denoising.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/5b58ff41853cd5fd1f2f388574fbf6db/plot_image_denoising.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_image_denoising.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_image_denoising.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)