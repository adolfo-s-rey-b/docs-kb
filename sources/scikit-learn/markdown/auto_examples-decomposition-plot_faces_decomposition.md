[Skip to main content](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/decomposition/plot_faces_decomposition.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/decomposition/plot_faces_decomposition.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/decomposition/plot_faces_decomposition.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/decomposition/plot_faces_decomposition.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/decomposition/plot_faces_decomposition.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/decomposition/plot_faces_decomposition.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html#sphx-glr-download-auto-examples-decomposition-plot-faces-decomposition-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Faces dataset decompositions[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html#faces-dataset-decompositions "Link to this heading")

===============================================================================================================================================================================

This example applies to [The Olivetti faces dataset](https://scikit-learn.org/stable/datasets/real_world.html#olivetti-faces-dataset)
 different unsupervised matrix decomposition (dimension reduction) methods from the module [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
 (see the documentation chapter [Decomposing signals in components (matrix factorization problems)](https://scikit-learn.org/stable/modules/decomposition.html#decompositions)
).

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Dataset preparation[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html#dataset-preparation "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

Loading and preprocessing the Olivetti faces dataset.

import logging

import matplotlib.pyplot as plt
from numpy.random import [RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")

from sklearn import cluster, decomposition
from sklearn.datasets import [fetch\_olivetti\_faces](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html#sklearn.datasets.fetch_olivetti_faces "sklearn.datasets.fetch_olivetti_faces")

rng \= [RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)

\# Display progress logs on stdout
[logging.basicConfig](https://docs.python.org/3/library/logging.html#logging.basicConfig "logging.basicConfig")
(level\=[logging.INFO](https://docs.python.org/3/library/logging.html#logging.INFO "logging.INFO")
, format\="%(asctime)s %(levelname)s %(message)s")

faces, \_ \= [fetch\_olivetti\_faces](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html#sklearn.datasets.fetch_olivetti_faces "sklearn.datasets.fetch_olivetti_faces")
(return\_X\_y\=True, shuffle\=True, random\_state\=rng)
n\_samples, n\_features \= faces.shape

\# Global centering (focus on one feature, centering all samples)
faces\_centered \= faces \- faces.mean(axis\=0)

\# Local centering (focus on one sample, centering all features)
faces\_centered \-= faces\_centered.mean(axis\=1).reshape(n\_samples, \-1)

print("Dataset consists of %d faces" % n\_samples)

Copy to clipboard

Dataset consists of 400 faces

Copy to clipboard

Define a base function to plot the gallery of faces.

n\_row, n\_col \= 2, 3
n\_components \= n\_row \* n\_col
image\_shape \= (64, 64)

def plot\_gallery(title, images, n\_col\=n\_col, n\_row\=n\_row, cmap\=plt.cm.gray):
    fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(
        nrows\=n\_row,
        ncols\=n\_col,
        figsize\=(2.0 \* n\_col, 2.3 \* n\_row),
        facecolor\="white",
        constrained\_layout\=True,
    )
    fig.get\_layout\_engine().set(w\_pad\=0.01, h\_pad\=0.02, hspace\=0, wspace\=0)
    fig.set\_edgecolor("black")
    fig.suptitle(title, size\=16)
    for ax, vec in zip(axs.flat, images):
        vmax \= max(vec.max(), \-vec.min())
        im \= ax.imshow(
            vec.reshape(image\_shape),
            cmap\=cmap,
            interpolation\="nearest",
            vmin\=-vmax,
            vmax\=vmax,
        )
        ax.axis("off")

    fig.colorbar(im, ax\=axs, orientation\="horizontal", shrink\=0.99, aspect\=40, pad\=0.01)
    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

Let’s take a look at our data. Gray color indicates negative values, white indicates positive values.

plot\_gallery("Faces from dataset", faces\_centered\[:n\_components\])

Copy to clipboard

![Faces from dataset](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_001.png)

Decomposition[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html#decomposition "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

Initialise different estimators for decomposition and fit each of them on all images and plot some results. Each estimator extracts 6 components as vectors h∈R4096. We just displayed these vectors in human-friendly visualisation as 64x64 pixel images.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/decomposition.html#decompositions)
.

### Eigenfaces - PCA using randomized SVD[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html#eigenfaces-pca-using-randomized-svd "Link to this heading")

Linear dimensionality reduction using Singular Value Decomposition (SVD) of the data to project it to a lower dimensional space.

Note

The Eigenfaces estimator, via the [`sklearn.decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
, also provides a scalar `noise_variance_` (the mean of pixelwise variance) that cannot be displayed as an image.

pca\_estimator \= [decomposition.PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(
    n\_components\=n\_components, svd\_solver\="randomized", whiten\=True
)
pca\_estimator.fit(faces\_centered)
plot\_gallery(
    "Eigenfaces - PCA using randomized SVD", pca\_estimator.components\_\[:n\_components\]
)

Copy to clipboard

![Eigenfaces - PCA using randomized SVD](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_002.png)

### Non-negative components - NMF[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html#non-negative-components-nmf "Link to this heading")

Estimate non-negative original data as production of two non-negative matrices.

nmf\_estimator \= [decomposition.NMF](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
(n\_components\=n\_components, tol\=5e-3)
nmf\_estimator.fit(faces)  \# original non- negative dataset
plot\_gallery("Non-negative components - NMF", nmf\_estimator.components\_\[:n\_components\])

Copy to clipboard

![Non-negative components - NMF](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_003.png)

### Independent components - FastICA[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html#independent-components-fastica "Link to this heading")

Independent component analysis separates a multivariate vectors into additive subcomponents that are maximally independent.

ica\_estimator \= [decomposition.FastICA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA "sklearn.decomposition.FastICA")
(
    n\_components\=n\_components, max\_iter\=400, whiten\="arbitrary-variance", tol\=15e-5
)
ica\_estimator.fit(faces\_centered)
plot\_gallery(
    "Independent components - FastICA", ica\_estimator.components\_\[:n\_components\]
)

Copy to clipboard

![Independent components - FastICA](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_004.png)

### Sparse components - MiniBatchSparsePCA[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html#sparse-components-minibatchsparsepca "Link to this heading")

Mini-batch sparse PCA ([`MiniBatchSparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "sklearn.decomposition.MiniBatchSparsePCA")
) extracts the set of sparse components that best reconstruct the data. This variant is faster but less accurate than the similar [`SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")
.

batch\_pca\_estimator \= [decomposition.MiniBatchSparsePCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "sklearn.decomposition.MiniBatchSparsePCA")
(
    n\_components\=n\_components, alpha\=0.1, max\_iter\=100, batch\_size\=3, random\_state\=rng
)
batch\_pca\_estimator.fit(faces\_centered)
plot\_gallery(
    "Sparse components - MiniBatchSparsePCA",
    batch\_pca\_estimator.components\_\[:n\_components\],
)

Copy to clipboard

![Sparse components - MiniBatchSparsePCA](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_005.png)

### Dictionary learning[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html#dictionary-learning "Link to this heading")

By default, [`MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
 divides the data into mini-batches and optimizes in an online manner by cycling over the mini-batches for the specified number of iterations.

batch\_dict\_estimator \= [decomposition.MiniBatchDictionaryLearning](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
(
    n\_components\=n\_components, alpha\=0.1, max\_iter\=50, batch\_size\=3, random\_state\=rng
)
batch\_dict\_estimator.fit(faces\_centered)
plot\_gallery("Dictionary learning", batch\_dict\_estimator.components\_\[:n\_components\])

Copy to clipboard

![Dictionary learning](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_006.png)

### Cluster centers - MiniBatchKMeans[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html#cluster-centers-minibatchkmeans "Link to this heading")

[`sklearn.cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
 is computationally efficient and implements on-line learning with a [`partial_fit`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans.partial_fit "sklearn.cluster.MiniBatchKMeans.partial_fit")
 method. That is why it could be beneficial to enhance some time-consuming algorithms with [`MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
.

kmeans\_estimator \= [cluster.MiniBatchKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
(
    n\_clusters\=n\_components,
    tol\=1e-3,
    batch\_size\=20,
    max\_iter\=50,
    random\_state\=rng,
)
kmeans\_estimator.fit(faces\_centered)
plot\_gallery(
    "Cluster centers - MiniBatchKMeans",
    kmeans\_estimator.cluster\_centers\_\[:n\_components\],
)

Copy to clipboard

![Cluster centers - MiniBatchKMeans](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_007.png)

### Factor Analysis components - FA[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html#factor-analysis-components-fa "Link to this heading")

[`FactorAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis "sklearn.decomposition.FactorAnalysis")
 is similar to [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
 but has the advantage of modelling the variance in every direction of the input space independently (heteroscedastic noise). Read more in the [User Guide](https://scikit-learn.org/stable/modules/decomposition.html#fa)
.

fa\_estimator \= [decomposition.FactorAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis "sklearn.decomposition.FactorAnalysis")
(n\_components\=n\_components, max\_iter\=20)
fa\_estimator.fit(faces\_centered)
plot\_gallery("Factor Analysis (FA)", fa\_estimator.components\_\[:n\_components\])

\# --- Pixelwise variance
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(3.2, 3.6), facecolor\="white", tight\_layout\=True)
vec \= fa\_estimator.noise\_variance\_
vmax \= max(vec.max(), \-vec.min())
[plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(
    vec.reshape(image\_shape),
    cmap\=plt.cm.gray,
    interpolation\="nearest",
    vmin\=-vmax,
    vmax\=vmax,
)
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("off")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Pixelwise variance from \\n Factor Analysis (FA)", size\=16, wrap\=True)
[plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
(orientation\="horizontal", shrink\=0.8, pad\=0.03)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

*   ![Factor Analysis (FA)](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_008.png)
*   ![Pixelwise variance from   Factor Analysis (FA)](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_009.png)

Decomposition: Dictionary learning[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html#decomposition-dictionary-learning "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In the further section, let’s consider [Dictionary Learning](https://scikit-learn.org/stable/modules/decomposition.html#dictionarylearning)
 more precisely. Dictionary learning is a problem that amounts to finding a sparse representation of the input data as a combination of simple elements. These simple elements form a dictionary. It is possible to constrain the dictionary and/or coding coefficients to be positive to match constraints that may be present in the data.

[`MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
 implements a faster, but less accurate version of the dictionary learning algorithm that is better suited for large datasets. Read more in the [User Guide](https://scikit-learn.org/stable/modules/decomposition.html#minibatchdictionarylearning)
.

Plot the same samples from our dataset but with another colormap. Red indicates negative values, blue indicates positive values, and white represents zeros.

plot\_gallery("Faces from dataset", faces\_centered\[:n\_components\], cmap\=plt.cm.RdBu)

Copy to clipboard

![Faces from dataset](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_010.png)

Similar to the previous examples, we change parameters and train [`MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
 estimator on all images. Generally, the dictionary learning and sparse encoding decompose input data into the dictionary and the coding coefficients matrices. X≈UV, where X\=\[x1,...,xn\], X∈Rm×n, dictionary U∈Rm×k, coding coefficients V∈Rk×n.

Also below are the results when the dictionary and coding coefficients are positively constrained.

### Dictionary learning - positive dictionary[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html#dictionary-learning-positive-dictionary "Link to this heading")

In the following section we enforce positivity when finding the dictionary.

dict\_pos\_dict\_estimator \= [decomposition.MiniBatchDictionaryLearning](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
(
    n\_components\=n\_components,
    alpha\=0.1,
    max\_iter\=50,
    batch\_size\=3,
    random\_state\=rng,
    positive\_dict\=True,
)
dict\_pos\_dict\_estimator.fit(faces\_centered)
plot\_gallery(
    "Dictionary learning - positive dictionary",
    dict\_pos\_dict\_estimator.components\_\[:n\_components\],
    cmap\=plt.cm.RdBu,
)

Copy to clipboard

![Dictionary learning - positive dictionary](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_011.png)

### Dictionary learning - positive code[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html#dictionary-learning-positive-code "Link to this heading")

Below we constrain the coding coefficients as a positive matrix.

dict\_pos\_code\_estimator \= [decomposition.MiniBatchDictionaryLearning](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
(
    n\_components\=n\_components,
    alpha\=0.1,
    max\_iter\=50,
    batch\_size\=3,
    fit\_algorithm\="cd",
    random\_state\=rng,
    positive\_code\=True,
)
dict\_pos\_code\_estimator.fit(faces\_centered)
plot\_gallery(
    "Dictionary learning - positive code",
    dict\_pos\_code\_estimator.components\_\[:n\_components\],
    cmap\=plt.cm.RdBu,
)

Copy to clipboard

![Dictionary learning - positive code](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_012.png)

/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.737e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 8.344e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.841e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.383e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 6.946e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.218e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.449e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 9.834e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 1.114e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.722046e-06, tolerance: 6.049e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 8.649e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.722046e-06, tolerance: 5.296e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 7.128e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.722046e-06, tolerance: 6.210e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.079e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 8.788e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.651e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 1.224e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 7.611e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 2.944e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.817e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 2.379e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 8.545e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.859e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 2.861023e-06, tolerance: 2.167e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 9.119e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 2.861023e-06, tolerance: 3.944e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 1.035e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.136e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 7.029e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 7.156e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 8.168e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 6.879e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 1.198e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 3.552e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 1.527e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.144409e-05, tolerance: 1.163e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 8.746e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 9.130e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 3.573e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 4.261e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.300e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.513e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 8.678e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 4.199e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.722046e-06, tolerance: 8.734e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 6.932e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.722046e-06, tolerance: 8.329e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 7.010e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 6.543e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.202e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 5.837e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 4.355e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 1.092e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 1.014e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 9.927e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 5.925e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.557e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 7.025e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 3.762e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.538e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 6.054e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 4.195e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.550e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 6.657e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.572e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 5.554e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 8.905e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-06, tolerance: 1.078e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 6.612e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 7.665e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 4.052e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 3.306e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 4.625e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 3.298e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 4.763e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 2.861023e-06, tolerance: 4.891e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 5.547e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 7.358e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 1.003e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 3.633e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 8.583069e-06, tolerance: 6.241e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 4.918e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.753e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 4.778e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 9.415e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.848e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 4.301e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 6.627e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 8.608e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.722046e-06, tolerance: 6.940e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 2.861023e-06, tolerance: 3.477e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 4.595e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 7.043e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 7.102e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 2.994e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-06, tolerance: 7.140e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 5.747e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.144409e-05, tolerance: 6.874e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.716614e-05, tolerance: 5.098e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 9.072e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.727e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 3.102e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 2.367e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.144409e-05, tolerance: 6.277e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.107e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 2.861023e-06, tolerance: 6.114e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.477e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-06, tolerance: 9.802e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.408e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 8.004e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 5.641e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 8.267e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 7.240e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 8.803e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 8.233e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 1.334e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 8.758e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 2.774e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 7.025e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 9.176e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 7.162e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 4.768372e-06, tolerance: 1.654e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 5.890e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 6.287e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 5.303e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 2.861023e-06, tolerance: 2.489e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.717e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 6.309e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 9.135e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 2.861023e-06, tolerance: 4.033e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 2.753e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.819e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.638e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.722046e-06, tolerance: 6.345e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 7.785e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.722046e-06, tolerance: 7.396e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.722046e-06, tolerance: 8.913e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 7.874e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-06, tolerance: 1.514e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.284e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 5.125e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 5.121e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 7.662e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 4.417e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 7.624e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 4.249e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.144409e-05, tolerance: 9.182e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.028e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-06, tolerance: 5.378e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 7.663e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 4.183e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.049042e-05, tolerance: 6.518e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 2.634e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 3.450e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 3.795e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.722046e-06, tolerance: 6.064e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-06, tolerance: 7.027e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-06, tolerance: 1.593e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.844e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-06, tolerance: 5.881e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 2.861023e-06, tolerance: 3.354e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.722046e-06, tolerance: 6.841e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.722046e-06, tolerance: 7.313e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.049042e-05, tolerance: 5.981e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-06, tolerance: 7.690e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 4.164e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.722046e-06, tolerance: 6.907e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.178e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 6.342e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.882e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 4.768372e-07, tolerance: 1.841e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.144409e-05, tolerance: 5.226e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 4.926e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 5.621e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.722046e-06, tolerance: 5.269e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 3.489e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 2.830e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 4.066e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 8.025e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 4.566e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.239777e-05, tolerance: 5.862e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 8.615e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 2.384186e-05, tolerance: 9.957e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 2.861023e-06, tolerance: 3.901e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 8.923e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 5.538e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 2.861023e-06, tolerance: 6.393e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.051758e-05, tolerance: 8.307e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 4.099e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.722046e-06, tolerance: 8.355e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 6.286e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 2.806e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 7.320e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 2.067e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 1.115e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 2.428e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.144409e-05, tolerance: 6.520e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.369e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.228e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(

Copy to clipboard

### Dictionary learning - positive dictionary & code[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html#dictionary-learning-positive-dictionary-code "Link to this heading")

Also below are the results if the dictionary values and coding coefficients are positively constrained.

dict\_pos\_estimator \= [decomposition.MiniBatchDictionaryLearning](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
(
    n\_components\=n\_components,
    alpha\=0.1,
    max\_iter\=50,
    batch\_size\=3,
    fit\_algorithm\="cd",
    random\_state\=rng,
    positive\_dict\=True,
    positive\_code\=True,
)
dict\_pos\_estimator.fit(faces\_centered)
plot\_gallery(
    "Dictionary learning - positive dictionary & code",
    dict\_pos\_estimator.components\_\[:n\_components\],
    cmap\=plt.cm.RdBu,
)

Copy to clipboard

![Dictionary learning - positive dictionary & code](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_013.png)

/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.226e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 4.417e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.318e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 6.114e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 1.115e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.365e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.621e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 6.049e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 1.163e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 9.421e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 2.861023e-06, tolerance: 3.033e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 7.008e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 2.634e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.795e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 8.355e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 7.358e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 7.755e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 7.474e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.722046e-06, tolerance: 5.948e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 6.408e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.981e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 6.836e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 4.566e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.722046e-06, tolerance: 6.943e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 6.538e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 1.514e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.547e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 9.119e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.358e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.047e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 4.681e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 2.732e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 8.267e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 7.611e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 7.240e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 4.510e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 8.743e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 8.788e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.725e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 4.625e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.071e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.732e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 9.390e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 9.415e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.572e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 1.035e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.739e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 9.130e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.543e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 1.486e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 8.734e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 8.678e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 7.264e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 5.340e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 9.176e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.747e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 2.861e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 8.026e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 6.477e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.575e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.722046e-06, tolerance: 7.094e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 4.340e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.550e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 4.869e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 7.206e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 4.195e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 4.386e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 4.061e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.144409e-05, tolerance: 1.092e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 2.367e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.996e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.346e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.557e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.881e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.477e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 7.690e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 2.830e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.144409e-05, tolerance: 8.168e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 7.156e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.287e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.510e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.722046e-06, tolerance: 6.309e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.722046e-06, tolerance: 4.595e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 7.107e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.354e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 4.301e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.560e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 8.233e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.891e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 5.658e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 3.017e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 7.624e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 7.102e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 9.258e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.098e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 3.595e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 1.298e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 7.025e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 6.277e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 4.249e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-06, tolerance: 9.957e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.727e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 4.068e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 3.203e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 8.329e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.079e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.629395e-06, tolerance: 1.014e-06
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 9.536743e-07, tolerance: 3.226e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.393e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 7.015e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 9.802e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.722046e-06, tolerance: 5.641e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 2.379e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.538e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.944e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 4.177e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 3.733e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.055e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.814697e-06, tolerance: 6.284e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.303e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(
/home/circleci/project/sklearn/linear\_model/\_coordinate\_descent.py:827: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.907349e-06, tolerance: 5.043e-07
  model = cd\_fast.enet\_coordinate\_descent\_gram(

Copy to clipboard

**Total running time of the script:** (0 minutes 7.383 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_faces_decomposition.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_faces_decomposition.ipynb)

[`Download Jupyter notebook: plot_faces_decomposition.ipynb`](https://scikit-learn.org/stable/_downloads/fcae36814d8e700024ca855a1eb87ca9/plot_faces_decomposition.ipynb)

[`Download Python source code: plot_faces_decomposition.py`](https://scikit-learn.org/stable/_downloads/4825fc8223d1af0f3b61080c3dea3a62/plot_faces_decomposition.py)

[`Download zipped: plot_faces_decomposition.zip`](https://scikit-learn.org/stable/_downloads/3d6c2c74b5e16738ba82279166b9bf46/plot_faces_decomposition.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_dict_face_patches_thumb.png)

[Online learning of a dictionary of parts of faces](https://scikit-learn.org/stable/auto_examples/cluster/plot_dict_face_patches.html)

Online learning of a dictionary of parts of faces

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_varimax_fa_thumb.png)

[Factor Analysis (with rotation) to visualize patterns](https://scikit-learn.org/stable/auto_examples/decomposition/plot_varimax_fa.html)

Factor Analysis (with rotation) to visualize patterns

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_coding_thumb.png)

[Sparse coding with a precomputed dictionary](https://scikit-learn.org/stable/auto_examples/decomposition/plot_sparse_coding.html)

Sparse coding with a precomputed dictionary

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_recognition_thumb.png)

[Faces recognition example using eigenfaces and kernel approximation](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html)

Faces recognition example using eigenfaces and kernel approximation

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/4825fc8223d1af0f3b61080c3dea3a62/plot_faces_decomposition.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/fcae36814d8e700024ca855a1eb87ca9/plot_faces_decomposition.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/3d6c2c74b5e16738ba82279166b9bf46/plot_faces_decomposition.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_faces_decomposition.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_faces_decomposition.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)