[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_dense_vs_sparse_data.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_lasso_dense_vs_sparse_data.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_dense_vs_sparse_data.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_lasso_dense_vs_sparse_data.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_lasso_dense_vs_sparse_data.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_lasso_dense_vs_sparse_data.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_lasso_dense_vs_sparse_data.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_lasso_dense_vs_sparse_data.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_dense_vs_sparse_data.html#sphx-glr-download-auto-examples-linear-model-plot-lasso-dense-vs-sparse-data-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Lasso on dense and sparse data[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_dense_vs_sparse_data.html#lasso-on-dense-and-sparse-data "Link to this heading")

=========================================================================================================================================================================================

We show that linear\_model.Lasso provides the same results for dense and sparse data and that in the case of sparse data the speed is improved.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

from scipy import linalg, sparse

from sklearn.datasets import [make\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")
from sklearn.linear\_model import [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")

Copy to clipboard

Comparing the two Lasso implementations on Dense data[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_dense_vs_sparse_data.html#comparing-the-two-lasso-implementations-on-dense-data "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We create a linear regression problem that is suitable for the Lasso, that is to say, with more features than samples. We then store the data matrix in both dense (the usual) and sparse format, and train a Lasso on each. We compute the runtime of both and check that they learned the same model by computing the Euclidean norm of the difference between the coefficients they learned. Because the data is dense, we expect better runtime with a dense data format.

X, y \= [make\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")
(n\_samples\=200, n\_features\=5000, random\_state\=0)
\# create a copy of X in sparse format
X\_sp \= [sparse.coo\_array](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.coo_array.html#scipy.sparse.coo_array "scipy.sparse.coo_array")
(X)

alpha \= 1
sparse\_lasso \= [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
(alpha\=alpha, fit\_intercept\=False, max\_iter\=1000)
dense\_lasso \= [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
(alpha\=alpha, fit\_intercept\=False, max\_iter\=1000)

t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
sparse\_lasso.fit(X\_sp, y)
print(f"Sparse Lasso done in {([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0):.3f}s")

t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
dense\_lasso.fit(X, y)
print(f"Dense Lasso done in {([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0):.3f}s")

\# compare the regression coefficients
coeff\_diff \= [linalg.norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.norm.html#scipy.linalg.norm "scipy.linalg.norm")
(sparse\_lasso.coef\_ \- dense\_lasso.coef\_)
print(f"Distance between coefficients : {coeff\_diff:.2e}")

#

Copy to clipboard

Sparse Lasso done in 0.116s
Dense Lasso done in 0.043s
Distance between coefficients : 5.23e-14

Copy to clipboard

Comparing the two Lasso implementations on Sparse data[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_dense_vs_sparse_data.html#comparing-the-two-lasso-implementations-on-sparse-data "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We make the previous problem sparse by replacing all small values with 0 and run the same comparisons as above. Because the data is now sparse, we expect the implementation that uses the sparse data format to be faster.

\# make a copy of the previous data
Xs \= X.copy()
\# make Xs sparse by replacing the values lower than 2.5 with 0s
Xs\[Xs < 2.5\] \= 0.0
\# create a copy of Xs in sparse format
Xs\_sp \= [sparse.coo\_array](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.coo_array.html#scipy.sparse.coo_array "scipy.sparse.coo_array")
(Xs)
Xs\_sp \= Xs\_sp.tocsc()

\# compute the proportion of non-zero coefficient in the data matrix
print(f"Matrix density : {(Xs\_sp.nnz / float(X.size) \* 100):.3f}%")

alpha \= 0.1
sparse\_lasso \= [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
(alpha\=alpha, fit\_intercept\=False, max\_iter\=10000)
dense\_lasso \= [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
(alpha\=alpha, fit\_intercept\=False, max\_iter\=10000)

t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
sparse\_lasso.fit(Xs\_sp, y)
print(f"Sparse Lasso done in {([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0):.3f}s")

t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
dense\_lasso.fit(Xs, y)
print(f"Dense Lasso done in  {([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0):.3f}s")

\# compare the regression coefficients
coeff\_diff \= [linalg.norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.norm.html#scipy.linalg.norm "scipy.linalg.norm")
(sparse\_lasso.coef\_ \- dense\_lasso.coef\_)
print(f"Distance between coefficients : {coeff\_diff:.2e}")

Copy to clipboard

Matrix density : 0.626%
Sparse Lasso done in 0.148s
Dense Lasso done in  0.908s
Distance between coefficients : 3.85e-13

Copy to clipboard

**Total running time of the script:** (0 minutes 1.282 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_lasso_dense_vs_sparse_data.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_lasso_dense_vs_sparse_data.ipynb)

[`Download Jupyter notebook: plot_lasso_dense_vs_sparse_data.ipynb`](https://scikit-learn.org/stable/_downloads/0aadb4e0dc9f402704c8a56152f01083/plot_lasso_dense_vs_sparse_data.ipynb)

[`Download Python source code: plot_lasso_dense_vs_sparse_data.py`](https://scikit-learn.org/stable/_downloads/510f5becea7ec7018a8eee43d6f12b1b/plot_lasso_dense_vs_sparse_data.py)

[`Download zipped: plot_lasso_dense_vs_sparse_data.zip`](https://scikit-learn.org/stable/_downloads/2f7b3682e03ebd7066495c3252414a44/plot_lasso_dense_vs_sparse_data.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_and_elasticnet_thumb.png)

[L1-based models for Sparse Signals](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html)

L1-based models for Sparse Signals

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multi_task_lasso_support_thumb.png)

[Joint feature selection with multi-task Lasso](https://scikit-learn.org/stable/auto_examples/linear_model/plot_multi_task_lasso_support.html)

Joint feature selection with multi-task Lasso

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_lasso_lars_elasticnet_path_thumb.png)

[Lasso, Lasso-LARS, and Elastic Net paths](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html)

Lasso, Lasso-LARS, and Elastic Net paths

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_model_selection_thumb.png)

[Lasso model selection: AIC-BIC / cross-validation](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html)

Lasso model selection: AIC-BIC / cross-validation

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/510f5becea7ec7018a8eee43d6f12b1b/plot_lasso_dense_vs_sparse_data.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/0aadb4e0dc9f402704c8a56152f01083/plot_lasso_dense_vs_sparse_data.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/2f7b3682e03ebd7066495c3252414a44/plot_lasso_dense_vs_sparse_data.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_lasso_dense_vs_sparse_data.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_lasso_dense_vs_sparse_data.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)