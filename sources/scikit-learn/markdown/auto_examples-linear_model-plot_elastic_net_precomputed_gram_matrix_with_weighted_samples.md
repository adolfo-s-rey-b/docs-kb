[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.html#sphx-glr-download-auto-examples-linear-model-plot-elastic-net-precomputed-gram-matrix-with-weighted-samples-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Fitting an Elastic Net with a precomputed Gram Matrix and Weighted Samples[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.html#fitting-an-elastic-net-with-a-precomputed-gram-matrix-and-weighted-samples "Link to this heading")

================================================================================================================================================================================================================================================================================================================

The following example shows how to precompute the gram matrix while using weighted samples with an [`ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
.

If weighted samples are used, the design matrix must be centered and then rescaled by the square root of the weight vector before the gram matrix is computed.

Note

`sample_weight` vector is also rescaled to sum to `n_samples`, see the

documentation for the `sample_weight` parameter to [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet.fit "sklearn.linear_model.ElasticNet.fit")
.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Let’s start by loading the dataset and creating some sample weights.

import numpy as np

from sklearn.datasets import [make\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)

n\_samples \= int(1e5)
X, y \= [make\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")
(n\_samples\=n\_samples, noise\=0.5, random\_state\=rng)

sample\_weight \= rng.lognormal(size\=n\_samples)
\# normalize the sample weights
normalized\_weights \= sample\_weight \* (n\_samples / (sample\_weight.sum()))

Copy to clipboard

To fit the elastic net using the `precompute` option together with the sample weights, we must first center the design matrix, and rescale it by the normalized weights prior to computing the gram matrix.

X\_offset \= [np.average](https://numpy.org/doc/stable/reference/generated/numpy.average.html#numpy.average "numpy.average")
(X, axis\=0, weights\=normalized\_weights)
X\_centered \= X \- [np.average](https://numpy.org/doc/stable/reference/generated/numpy.average.html#numpy.average "numpy.average")
(X, axis\=0, weights\=normalized\_weights)
X\_scaled \= X\_centered \* [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(normalized\_weights)\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]
gram \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(X\_scaled.T, X\_scaled)

Copy to clipboard

We can now proceed with fitting. We must passed the centered design matrix to `fit` otherwise the elastic net estimator will detect that it is uncentered and discard the gram matrix we passed. However, if we pass the scaled design matrix, the preprocessing code will incorrectly rescale it a second time.

from sklearn.linear\_model import [ElasticNet](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")

lm \= [ElasticNet](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
(alpha\=0.01, precompute\=gram)
lm.fit(X\_centered, y, sample\_weight\=normalized\_weights)

Copy to clipboard

ElasticNet(alpha=0.01,
           precompute=array(\[\[ 9.98809919e+04, -4.48938813e+02, -1.03237920e+03, ...,\
        -2.25349312e+02, -3.53959628e+02, -1.67451144e+02\],\
       \[-4.48938813e+02,  1.00768662e+05,  1.19112072e+02, ...,\
        -1.07963978e+03,  7.47987268e+01, -5.76195467e+02\],\
       \[-1.03237920e+03,  1.19112072e+02,  1.00393284e+05, ...,\
        -3.07582983e+02,  6.66670169e+02,  2.65799352e+02\],\
       ...,\
       \[-2.25349312e+02, -1.07963978e+03, -3.07582983e+02, ...,\
         9.99891212e+04, -4.58195950e+02, -1.58667835e+02\],\
       \[-3.53959628e+02,  7.47987268e+01,  6.66670169e+02, ...,\
        -4.58195950e+02,  9.98350372e+04,  5.60836363e+02\],\
       \[-1.67451144e+02, -5.76195467e+02,  2.65799352e+02, ...,\
        -1.58667835e+02,  5.60836363e+02,  1.00911944e+05\]\],
      shape=(100, 100)))

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

ElasticNet

[?Documentation for ElasticNet](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.ElasticNet.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [alpha alpha: float, default=1.0  <br>  <br>Constant that multiplies the penalty terms. Defaults to 1.0.  <br>See the notes for the exact mathematical meaning of this  <br>parameter. \`\`alpha = 0\`\` is equivalent to an ordinary least square,  <br>solved by the :class:\`LinearRegression\` object. For numerical  <br>reasons, using \`\`alpha = 0\`\` with the \`\`Lasso\`\` object is not advised.  <br>Given this, you should use the :class:\`LinearRegression\` object.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.ElasticNet.html#:~:text=alpha,-float%2C%20default%3D1.0) | 0.01 |
|     | [precompute precompute: bool or array-like of shape (n\_features, n\_features), default=False  <br>  <br>Whether to use a precomputed Gram matrix to speed up  <br>calculations. The Gram matrix can also be passed as argument.  <br>For sparse input this option is always \`\`False\`\` to preserve sparsity.  <br>Check :ref:\`an example on how to use a precomputed Gram Matrix in ElasticNet  <br><sphx\_glr\_auto\_examples\_linear\_model\_plot\_elastic\_net\_precomputed\_gram\_matrix\_with\_weighted\_samples.py>\`  <br>for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.ElasticNet.html#:~:text=precompute,-bool%20or%20array-like%20of%20shape%20%28n_features%2C%20n_features%29%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DFalse) | array(\[\[ 9.98...pe=(100, 100)) |\
|     | [l1\_ratio l1\_ratio: float, default=0.5  <br>  <br>The ElasticNet mixing parameter, with \`\`0 <= l1\_ratio <= 1\`\`. For  <br>\`\`l1\_ratio = 0\`\` the penalty is an L2 penalty. \`\`For l1\_ratio = 1\`\` it  <br>is an L1 penalty. For \`\`0 < l1\_ratio < 1\`\`, the penalty is a  <br>combination of L1 and L2.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.ElasticNet.html#:~:text=l1_ratio,-float%2C%20default%3D0.5) | 0.5 |\
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Whether the intercept should be estimated or not. If \`\`False\`\`, the  <br>data is assumed to be already centered.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.ElasticNet.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |\
|     | [max\_iter max\_iter: int, default=1000  <br>  <br>The maximum number of iterations.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.ElasticNet.html#:~:text=max_iter,-int%2C%20default%3D1000) | 1000 |\
|     | [copy\_X copy\_X: bool, default=True  <br>  <br>If \`\`True\`\`, X will be copied; else, it may be overwritten.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.ElasticNet.html#:~:text=copy_X,-bool%2C%20default%3DTrue) | True |\
|     | [tol tol: float, default=1e-4  <br>  <br>The tolerance for the optimization: if the updates are smaller or equal to  <br>\`\`tol\`\`, the optimization code checks the dual gap for optimality and continues  <br>until it is smaller or equal to \`\`tol\`\`, see Notes below.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.ElasticNet.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001 |\
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to \`\`True\`\`, reuse the solution of the previous call to fit as  <br>initialization, otherwise, just erase the previous solution.  <br>See :term:\`the Glossary <warm\_start>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.ElasticNet.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |\
|     | [positive positive: bool, default=False  <br>  <br>When set to \`\`True\`\`, forces the coefficients to be positive.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.ElasticNet.html#:~:text=positive,-bool%2C%20default%3DFalse) | False |\
|     | [random\_state random\_state: int, RandomState instance, default=None  <br>  <br>The seed of the pseudo random number generator that selects a random  <br>feature to update. Used when \`\`selection\`\` == 'random'.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.ElasticNet.html#:~:text=random_state,-int%2C%20RandomState%20instance%2C%20default%3DNone) | None |\
|     | [selection selection: {'cyclic', 'random'}, default='cyclic'  <br>  <br>If set to 'random', a random coefficient is updated every iteration  <br>rather than looping over features sequentially by default. This  <br>(setting to 'random') often leads to significantly faster convergence  <br>especially when tol is higher than 1e-4.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.ElasticNet.html#:~:text=selection,-%7B%27cyclic%27%2C%20%27random%27%7D%2C%20default%3D%27cyclic%27) | 'cyclic' |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [coef\_ coef\_: ndarray of shape (n\_features,) or (n\_targets, n\_features)  <br>  <br>Parameter vector (w in the cost function formula).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.ElasticNet.html#:~:text=coef_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20%28n_targets%2C%20n_features%29) | ndarray\[float64\](100,) | \[-0.,-0., 0.,..., 0., 0., 0.\] |\
| [dual\_gap\_ dual\_gap\_: float or ndarray of shape (n\_targets,)  <br>  <br>Given param alpha, the dual gaps at the end of the optimization,  <br>same shape as each observation of y.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.ElasticNet.html#:~:text=dual_gap_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float64 | 0.003181 |\
| [intercept\_ intercept\_: float or ndarray of shape (n\_targets,)  <br>  <br>Independent term in decision function.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.ElasticNet.html#:~:text=intercept_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float64 | \-0.03042 |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.ElasticNet.html#:~:text=n_features_in_,-int) | int | 100 |\
| [n\_iter\_ n\_iter\_: list of int  <br>  <br>Number of iterations run by the coordinate descent solver to reach  <br>the specified tolerance.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.ElasticNet.html#:~:text=n_iter_,-list%20of%20int) | int | 4   |\
| [sparse\_coef\_ sparse\_coef\_: sparse matrix of shape (n\_features,) or (n\_targets, n\_features)  <br>  <br>Sparse representation of the \`coef\_\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.ElasticNet.html#:~:text=sparse_coef_,-sparse%20matrix%20of%20shape%20%28n_features%2C%29%20or%20%20%20%20%20%20%20%20%20%20%20%20%20%28n_targets%2C%20n_features%29) | csr\_matrix\[float64\](1, 100) | <Compressed S...hape (1, 100)> |\
\
  \
  \
\
**Total running time of the script:** (0 minutes 0.754 seconds)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.ipynb)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.ipynb)\
\
[`Download Jupyter notebook: plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.ipynb`](https://scikit-learn.org/stable/_downloads/1054d40caffbd65c52b20dac784c7c5c/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.ipynb)\
\
[`Download Python source code: plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.py`](https://scikit-learn.org/stable/_downloads/c50f4529d4a653ccd8d5117ec9300975/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.py)\
\
[`Download zipped: plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.zip`](https://scikit-learn.org/stable/_downloads/8c73025f63b2513cd701f6a378d77281/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.zip)\
\
Related examples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_weighted_samples_thumb.png)\
\
[SVM: Weighted samples](https://scikit-learn.org/stable/auto_examples/svm/plot_weighted_samples.html)\
\
SVM: Weighted samples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_metadata_routing_thumb.png)\
\
[Developing Estimators Compliant with Metadata Routing](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html)\
\
Developing Estimators Compliant with Metadata Routing\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_weighted_samples_thumb.png)\
\
[SGD: Weighted samples](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_weighted_samples.html)\
\
SGD: Weighted samples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_regression_thumb.png)\
\
[Nearest Neighbors regression](https://scikit-learn.org/stable/auto_examples/neighbors/plot_regression.html)\
\
Nearest Neighbors regression\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
[Download source code](https://scikit-learn.org/stable/_downloads/c50f4529d4a653ccd8d5117ec9300975/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.py)\
\
[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/1054d40caffbd65c52b20dac784c7c5c/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.ipynb)\
\
[Download zipped](https://scikit-learn.org/stable/_downloads/8c73025f63b2513cd701f6a378d77281/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.zip)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.ipynb)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.ipynb)\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)