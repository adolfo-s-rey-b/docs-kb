[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_dict_face_patches.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_dict_face_patches.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_dict_face_patches.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_dict_face_patches.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_dict_face_patches.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_dict_face_patches.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_dict_face_patches.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_dict_face_patches.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_dict_face_patches.html#sphx-glr-download-auto-examples-cluster-plot-dict-face-patches-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Online learning of a dictionary of parts of faces[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_dict_face_patches.html#online-learning-of-a-dictionary-of-parts-of-faces "Link to this heading")

=================================================================================================================================================================================================================

This example uses a large dataset of faces to learn a set of 20 x 20 images patches that constitute faces.

From the programming standpoint, it is interesting because it shows how to use the online API of the scikit-learn to process a very large dataset by chunks. The way we proceed is that we load an image at a time and extract randomly 50 patches from this image. Once we have accumulated 500 of these patches (using 10 images), we run the [`partial_fit`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans.partial_fit "sklearn.cluster.MiniBatchKMeans.partial_fit")
 method of the online KMeans object, MiniBatchKMeans.

The verbose setting on the MiniBatchKMeans enables us to see that some clusters are reassigned during the successive calls to partial-fit. This is because the number of patches that they represent has become too low, and it is better to choose a random new cluster.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Load the data[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_dict_face_patches.html#load-the-data "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

from sklearn import datasets

faces \= [datasets.fetch\_olivetti\_faces](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html#sklearn.datasets.fetch_olivetti_faces "sklearn.datasets.fetch_olivetti_faces")
()

Copy to clipboard

Learn the dictionary of images[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_dict_face_patches.html#learn-the-dictionary-of-images "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import time

import numpy as np

from sklearn.cluster import [MiniBatchKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
from sklearn.feature\_extraction.image import [extract\_patches\_2d](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html#sklearn.feature_extraction.image.extract_patches_2d "sklearn.feature_extraction.image.extract_patches_2d")

print("Learning the dictionary... ")
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
kmeans \= [MiniBatchKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
(n\_clusters\=81, random\_state\=rng, verbose\=True, n\_init\=3)
patch\_size \= (20, 20)

buffer \= \[\]
t0 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()

\# The online learning part: cycle over the whole dataset 6 times
index \= 0
for \_ in range(6):
    for img in faces.images:
        data \= [extract\_patches\_2d](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html#sklearn.feature_extraction.image.extract_patches_2d "sklearn.feature_extraction.image.extract_patches_2d")
(img, patch\_size, max\_patches\=50, random\_state\=rng)
        data \= [np.reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")
(data, (len(data), \-1))
        buffer.append(data)
        index += 1
        if index % 10 \== 0:
            data \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(buffer, axis\=0)
            data \-= [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(data, axis\=0)
            data /= [np.std](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std")
(data, axis\=0)
            kmeans.partial\_fit(data)
            buffer \= \[\]
        if index % 100 \== 0:
            print("Partial fit of %4i out of %i" % (index, 6 \* len(faces.images)))

dt \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0
print("done in %.2fs." % dt)

Copy to clipboard

Learning the dictionary...
\[MiniBatchKMeans\] Reassigning 8 cluster centers.
\[MiniBatchKMeans\] Reassigning 5 cluster centers.
Partial fit of  100 out of 2400
\[MiniBatchKMeans\] Reassigning 3 cluster centers.
Partial fit of  200 out of 2400
\[MiniBatchKMeans\] Reassigning 1 cluster centers.
Partial fit of  300 out of 2400
\[MiniBatchKMeans\] Reassigning 3 cluster centers.
Partial fit of  400 out of 2400
Partial fit of  500 out of 2400
Partial fit of  600 out of 2400
Partial fit of  700 out of 2400
Partial fit of  800 out of 2400
Partial fit of  900 out of 2400
Partial fit of 1000 out of 2400
Partial fit of 1100 out of 2400
Partial fit of 1200 out of 2400
Partial fit of 1300 out of 2400
Partial fit of 1400 out of 2400
Partial fit of 1500 out of 2400
Partial fit of 1600 out of 2400
Partial fit of 1700 out of 2400
Partial fit of 1800 out of 2400
Partial fit of 1900 out of 2400
Partial fit of 2000 out of 2400
Partial fit of 2100 out of 2400
Partial fit of 2200 out of 2400
Partial fit of 2300 out of 2400
Partial fit of 2400 out of 2400
done in 1.22s.

Copy to clipboard

Plot the results[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_dict_face_patches.html#plot-the-results "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(4.2, 4))
for i, patch in enumerate(kmeans.cluster\_centers\_):
    [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(9, 9, i + 1)
    [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(patch.reshape(patch\_size), cmap\=plt.cm.gray, interpolation\="nearest")
    [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
    [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())

[plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
(
    "Patches of faces\\nTrain time %.1fs on %d patches" % (dt, 8 \* len(faces.images)),
    fontsize\=16,
)
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(0.08, 0.02, 0.92, 0.85, 0.08, 0.23)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Patches of faces Train time 1.2s on 3200 patches](https://scikit-learn.org/stable/_images/sphx_glr_plot_dict_face_patches_001.png)

**Total running time of the script:** (0 minutes 1.851 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_dict_face_patches.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_dict_face_patches.ipynb)

[`Download Jupyter notebook: plot_dict_face_patches.ipynb`](https://scikit-learn.org/stable/_downloads/0af0092c704518874f82d38d725bb97f/plot_dict_face_patches.ipynb)

[`Download Python source code: plot_dict_face_patches.py`](https://scikit-learn.org/stable/_downloads/7f205ae026a8c21fcab1e6a86cfadb7d/plot_dict_face_patches.py)

[`Download zipped: plot_dict_face_patches.zip`](https://scikit-learn.org/stable/_downloads/cb3f1818f509a9fcaea18d325eeb2e71/plot_dict_face_patches.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_image_denoising_thumb.png)

[Image denoising using dictionary learning](https://scikit-learn.org/stable/auto_examples/decomposition/plot_image_denoising.html)

Image denoising using dictionary learning

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_thumb.png)

[Faces dataset decompositions](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html)

Faces dataset decompositions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_agglomeration_thumb.png)

[Feature agglomeration](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_agglomeration.html)

Feature agglomeration

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mini_batch_kmeans_thumb.png)

[Comparison of the K-Means and MiniBatchKMeans clustering algorithms](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html)

Comparison of the K-Means and MiniBatchKMeans clustering algorithms

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/7f205ae026a8c21fcab1e6a86cfadb7d/plot_dict_face_patches.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/0af0092c704518874f82d38d725bb97f/plot_dict_face_patches.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/cb3f1818f509a9fcaea18d325eeb2e71/plot_dict_face_patches.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_dict_face_patches.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_dict_face_patches.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)