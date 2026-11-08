[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.lasso_path.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.lasso_path.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.lasso_path.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.lasso_path.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.lasso_path.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.lasso_path.html)

Collapse Sidebar Expand Sidebar

lasso\_path[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#lasso-path "Link to this heading")

=========================================================================================================================================

sklearn.linear\_model.lasso\_path(_X_, _y_, _\*_, _eps\=0.001_, _n\_alphas\='deprecated'_, _alphas\='warn'_, _precompute\='auto'_, _Xy\=None_, _copy\_X\=True_, _coef\_init\=None_, _verbose\=False_, _return\_n\_iter\=False_, _positive\=False_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_coordinate_descent.py#L213)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#sklearn.linear_model.lasso_path "Link to this definition")

Compute Lasso path with coordinate descent.

The Lasso optimization function varies for mono and multi-outputs.

For mono-output tasks it is:

(1 / (2 \* n\_samples)) \* ||y \- Xw||^2\_2 + alpha \* ||w||\_1

Copy to clipboard

For multi-output tasks it is:

(1 / (2 \* n\_samples)) \* ||Y \- XW||^2\_Fro + alpha \* ||W||\_21

Copy to clipboard

Where:

||W||\_21 \= \\sum\_i \\sqrt{\\sum\_j w\_{ij}^2}

Copy to clipboard

i.e. the sum of norm of each row.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#lasso)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training data. Pass directly as Fortran-contiguous data to avoid unnecessary memory duplication. If `y` is mono-output then `X` can be sparse.

**y**{array-like, sparse matrix} of shape (n\_samples,) or (n\_samples, n\_targets)

Target values.

**eps**float, default=1e-3

Length of the path. `eps=1e-3` means that `alpha_min / alpha_max = 1e-3`.

**n\_alphas**int, default=100

Number of alphas along the regularization path.

**alphas**array-like, default=None

List of alphas where to compute the models. If `None` alphas are set automatically.

**precompute**‘auto’, bool or array-like of shape (n\_features, n\_features), default=’auto’

Whether to use a precomputed Gram matrix to speed up calculations. If set to `'auto'` let us decide. The Gram matrix can also be passed as argument.

**Xy**array-like of shape (n\_features,) or (n\_features, n\_targets), default=None

Xy = np.dot(X.T, y) that can be precomputed. It is useful only when the Gram matrix is precomputed.

**copy\_X**bool, default=True

If `True`, X will be copied; else, it may be overwritten.

**coef\_init**array-like of shape (n\_features, ), default=None

The initial values of the coefficients.

**verbose**bool or int, default=False

Amount of verbosity.

**return\_n\_iter**bool, default=False

Whether to return the number of iterations or not.

**positive**bool, default=False

If set to True, forces coefficients to be positive. (Only allowed when `y.ndim == 1`).

**\*\*params**kwargs

Keyword arguments passed to the coordinate descent solver.

Returns:

**alphas**ndarray of shape (n\_alphas,)

The alphas along the path where models are computed.

**coefs**ndarray of shape (n\_features, n\_alphas) or (n\_targets, n\_features, n\_alphas)

Coefficients along the path.

**dual\_gaps**ndarray of shape (n\_alphas,)

The dual gaps at the end of the optimization for each alpha.

**n\_iters**list of int

The number of iterations taken by the coordinate descent optimizer to reach the specified tolerance for each alpha.

See also

[`lars_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")

Compute Least Angle Regression or Lasso path using LARS algorithm.

[`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")

The Lasso is a linear model that estimates sparse coefficients.

[`LassoLars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html#sklearn.linear_model.LassoLars "sklearn.linear_model.LassoLars")

Lasso model fit with Least Angle Regression a.k.a. Lars.

[`LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")

Lasso linear model with iterative fitting along a regularization path.

[`LassoLarsCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsCV.html#sklearn.linear_model.LassoLarsCV "sklearn.linear_model.LassoLarsCV")

Cross-validated Lasso using the LARS algorithm.

[`sklearn.decomposition.sparse_encode`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html#sklearn.decomposition.sparse_encode "sklearn.decomposition.sparse_encode")

Estimator that can be used to transform signals into sparse linear combination of atoms from a fixed.

Notes

For an example, see [examples/linear\_model/plot\_lasso\_lasso\_lars\_elasticnet\_path.py](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html#sphx-glr-auto-examples-linear-model-plot-lasso-lasso-lars-elasticnet-path-py)
.

To avoid unnecessary memory duplication the X argument of the fit method should be directly passed as a Fortran-contiguous numpy array.

Note that in certain cases, the Lars solver may be significantly faster to implement this functionality. In particular, linear interpolation can be used to retrieve model coefficients between the values output by lars\_path.

The underlying coordinate descent solver uses gap safe screening rules to speedup fitting time, see [User Guide on coordinate descent](https://scikit-learn.org/stable/modules/linear_model.html#coordinate-descent)
.

Examples

Comparing lasso\_path and lars\_path with interpolation:

\>>> import numpy as np
\>>> from sklearn.linear\_model import lasso\_path
\>>> X \= np.array(\[\[1, 2, 3.1\], \[2.3, 5.4, 4.3\]\]).T
\>>> y \= np.array(\[1, 2, 3.1\])
\>>> \# Use lasso\_path to compute a coefficient path
\>>> \_, coef\_path, \_ \= lasso\_path(X, y, alphas\=\[5., 1., .5\])
\>>> print(coef\_path)
\[\[0.         0.         0.46874778\]\
 \[0.2159048  0.4425765  0.23689075\]\]

Copy to clipboard

\>>> \# Now use lars\_path and 1D linear interpolation to compute the
\>>> \# same path
\>>> from sklearn.linear\_model import lars\_path
\>>> alphas, active, coef\_path\_lars \= lars\_path(X, y, method\='lasso')
\>>> from scipy import interpolate
\>>> coef\_path\_continuous \= interpolate.interp1d(alphas\[::\-1\],
...                                             coef\_path\_lars\[:, ::\-1\])
\>>> print(coef\_path\_continuous(\[5., 1., .5\]))
\[\[0.         0.         0.46915237\]\
 \[0.2159048  0.4425765  0.23668876\]\]

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_lasso_lars_elasticnet_path_thumb.png)

[Lasso, Lasso-LARS, and Elastic Net paths](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html)

Lasso, Lasso-LARS, and Elastic Net paths

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)