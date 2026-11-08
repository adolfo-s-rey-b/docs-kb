[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_agglomeration.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_digits_agglomeration.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_agglomeration.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_digits_agglomeration.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_digits_agglomeration.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_digits_agglomeration.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_digits_agglomeration.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_digits_agglomeration.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_agglomeration.html#sphx-glr-download-auto-examples-cluster-plot-digits-agglomeration-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Feature agglomeration[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_agglomeration.html#feature-agglomeration "Link to this heading")

============================================================================================================================================================

These images show how similar features are merged together using feature agglomeration.

![Original data, Agglomerated data, Labels](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_agglomeration_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn import cluster, datasets
from sklearn.feature\_extraction.image import grid\_to\_graph

digits \= [datasets.load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
()
images \= digits.images
X \= [np.reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")
(images, (len(images), \-1))
connectivity \= grid\_to\_graph(\*images\[0\].shape)

agglo \= [cluster.FeatureAgglomeration](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration "sklearn.cluster.FeatureAgglomeration")
(connectivity\=connectivity, n\_clusters\=32)

agglo.fit(X)
X\_reduced \= agglo.transform(X)

X\_restored \= agglo.inverse\_transform(X\_reduced)
images\_restored \= [np.reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")
(X\_restored, images.shape)
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(1, figsize\=(4, 3.5))
[plt.clf](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clf.html#matplotlib.pyplot.clf "matplotlib.pyplot.clf")
()
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(left\=0.01, right\=0.99, bottom\=0.01, top\=0.91)
for i in range(4):
    [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(3, 4, i + 1)
    [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(images\[i\], cmap\=plt.cm.gray, vmax\=16, interpolation\="nearest")
    [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
    [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())
    if i \== 1:
        [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Original data")
    [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(3, 4, 4 + i + 1)
    [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(images\_restored\[i\], cmap\=plt.cm.gray, vmax\=16, interpolation\="nearest")
    if i \== 1:
        [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Agglomerated data")
    [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
    [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())

[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(3, 4, 10)
[plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(
    [np.reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")
(agglo.labels\_, images\[0\].shape),
    interpolation\="nearest",
    cmap\=plt.cm.nipy\_spectral,
)
[plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
[plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Labels")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.099 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_digits_agglomeration.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_digits_agglomeration.ipynb)

[`Download Jupyter notebook: plot_digits_agglomeration.ipynb`](https://scikit-learn.org/stable/_downloads/ec1f4d8025c9e2e1a227310276945765/plot_digits_agglomeration.ipynb)

[`Download Python source code: plot_digits_agglomeration.py`](https://scikit-learn.org/stable/_downloads/2be83f6fd16a57d87ecf24c2aec45229/plot_digits_agglomeration.py)

[`Download zipped: plot_digits_agglomeration.zip`](https://scikit-learn.org/stable/_downloads/0b03eb096c3d32195335ba930a0b3662/plot_digits_agglomeration.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_denoising_thumb.png)

[Image denoising using kernel PCA](https://scikit-learn.org/stable/auto_examples/applications/plot_digits_denoising.html)

Image denoising using kernel PCA

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_classification_thumb.png)

[Recognizing hand-written digits](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html)

Recognizing hand-written digits

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_dict_face_patches_thumb.png)

[Online learning of a dictionary of parts of faces](https://scikit-learn.org/stable/auto_examples/cluster/plot_dict_face_patches.html)

Online learning of a dictionary of parts of faces

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_agglomeration_vs_univariate_selection_thumb.png)

[Feature agglomeration vs. univariate selection](https://scikit-learn.org/stable/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.html)

Feature agglomeration vs. univariate selection

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/2be83f6fd16a57d87ecf24c2aec45229/plot_digits_agglomeration.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/ec1f4d8025c9e2e1a227310276945765/plot_digits_agglomeration.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/0b03eb096c3d32195335ba930a0b3662/plot_digits_agglomeration.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_digits_agglomeration.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_digits_agglomeration.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)