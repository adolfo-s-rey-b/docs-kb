[Skip to main content](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multioutput_face_completion.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/miscellaneous/plot_multioutput_face_completion.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multioutput_face_completion.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/miscellaneous/plot_multioutput_face_completion.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/miscellaneous/plot_multioutput_face_completion.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/miscellaneous/plot_multioutput_face_completion.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/miscellaneous/plot_multioutput_face_completion.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/miscellaneous/plot_multioutput_face_completion.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multioutput_face_completion.html#sphx-glr-download-auto-examples-miscellaneous-plot-multioutput-face-completion-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Face completion with a multi-output estimators[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multioutput_face_completion.html#face-completion-with-a-multi-output-estimators "Link to this heading")

===========================================================================================================================================================================================================================

This example shows the use of multi-output estimator to complete images. The goal is to predict the lower half of a face given its upper half.

The first column of images shows true faces. The next columns illustrate how extremely randomized trees, k nearest neighbors, linear regression and ridge regression complete the lower half of those faces.

![Face completion with multi-output estimators, true faces, Extra trees, K-nn, Linear regression, Ridge](https://scikit-learn.org/stable/_images/sphx_glr_plot_multioutput_face_completion_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [fetch\_olivetti\_faces](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html#sklearn.datasets.fetch_olivetti_faces "sklearn.datasets.fetch_olivetti_faces")
from sklearn.ensemble import [ExtraTreesRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
from sklearn.linear\_model import [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
, [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
from sklearn.neighbors import [KNeighborsRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")
from sklearn.utils.validation import [check\_random\_state](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html#sklearn.utils.check_random_state "sklearn.utils.check_random_state")

\# Load the faces datasets
data, targets \= [fetch\_olivetti\_faces](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html#sklearn.datasets.fetch_olivetti_faces "sklearn.datasets.fetch_olivetti_faces")
(return\_X\_y\=True)

train \= data\[targets < 30\]
test \= data\[targets \>= 30\]  \# Test on independent people

\# Test on a subset of people
n\_faces \= 5
rng \= [check\_random\_state](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html#sklearn.utils.check_random_state "sklearn.utils.check_random_state")
(4)
face\_ids \= rng.randint(test.shape\[0\], size\=(n\_faces,))
test \= test\[face\_ids, :\]

n\_pixels \= data.shape\[1\]
\# Upper half of the faces
X\_train \= train\[:, : (n\_pixels + 1) // 2\]
\# Lower half of the faces
y\_train \= train\[:, n\_pixels // 2 :\]
X\_test \= test\[:, : (n\_pixels + 1) // 2\]
y\_test \= test\[:, n\_pixels // 2 :\]

\# Fit estimators
ESTIMATORS \= {
    "Extra trees": [ExtraTreesRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
(
        n\_estimators\=10, max\_features\=32, random\_state\=0
    ),
    "K-nn": [KNeighborsRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")
(),
    "Linear regression": [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
(),
    "Ridge": [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
(),
}

y\_test\_predict \= dict()
for name, estimator in ESTIMATORS.items():
    estimator.fit(X\_train, y\_train)
    y\_test\_predict\[name\] \= estimator.predict(X\_test)

\# Plot the completed faces
image\_shape \= (64, 64)

n\_cols \= 1 + len(ESTIMATORS)
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(2.0 \* n\_cols, 2.26 \* n\_faces))
[plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
("Face completion with multi-output estimators", size\=16)

for i in range(n\_faces):
    true\_face \= [np.hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")
((X\_test\[i\], y\_test\[i\]))

    if i:
        sub \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(n\_faces, n\_cols, i \* n\_cols + 1)
    else:
        sub \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(n\_faces, n\_cols, i \* n\_cols + 1, title\="true faces")

    sub.axis("off")
    sub.imshow(
        true\_face.reshape(image\_shape), cmap\=plt.cm.gray, interpolation\="nearest"
    )

    for j, est in enumerate(sorted(ESTIMATORS)):
        completed\_face \= [np.hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")
((X\_test\[i\], y\_test\_predict\[est\]\[i\]))

        if i:
            sub \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(n\_faces, n\_cols, i \* n\_cols + 2 + j)

        else:
            sub \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(n\_faces, n\_cols, i \* n\_cols + 2 + j, title\=est)

        sub.axis("off")
        sub.imshow(
            completed\_face.reshape(image\_shape),
            cmap\=plt.cm.gray,
            interpolation\="nearest",
        )

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 1.645 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_multioutput_face_completion.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_multioutput_face_completion.ipynb)

[`Download Jupyter notebook: plot_multioutput_face_completion.ipynb`](https://scikit-learn.org/stable/_downloads/59c5e476396afdc4788c35a49f6289b9/plot_multioutput_face_completion.ipynb)

[`Download Python source code: plot_multioutput_face_completion.py`](https://scikit-learn.org/stable/_downloads/ea40aa6b32c0c42d58220adef4c4e0b8/plot_multioutput_face_completion.py)

[`Download zipped: plot_multioutput_face_completion.zip`](https://scikit-learn.org/stable/_downloads/98a587e4b782bdfca89898083ebe7b05/plot_multioutput_face_completion.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_dict_face_patches_thumb.png)

[Online learning of a dictionary of parts of faces](https://scikit-learn.org/stable/auto_examples/cluster/plot_dict_face_patches.html)

Online learning of a dictionary of parts of faces

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_agglomeration_thumb.png)

[Feature agglomeration](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_agglomeration.html)

Feature agglomeration

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_thumb.png)

[Faces dataset decompositions](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html)

Faces dataset decompositions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stack_predictors_thumb.png)

[Combine predictors using stacking](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html)

Combine predictors using stacking

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/ea40aa6b32c0c42d58220adef4c4e0b8/plot_multioutput_face_completion.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/59c5e476396afdc4788c35a49f6289b9/plot_multioutput_face_completion.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/98a587e4b782bdfca89898083ebe7b05/plot_multioutput_face_completion.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_multioutput_face_completion.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_multioutput_face_completion.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)