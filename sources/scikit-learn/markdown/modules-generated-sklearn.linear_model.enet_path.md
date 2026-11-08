[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.enet_path.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.enet_path.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.enet_path.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.enet_path.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.enet_path.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.enet_path.html)

Collapse Sidebar Expand Sidebar

enet\_path[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#enet-path "Link to this heading")

======================================================================================================================================

sklearn.linear\_model.enet\_path(_X_, _y_, _\*_, _l1\_ratio\=0.5_, _eps\=0.001_, _n\_alphas\='deprecated'_, _alphas\='warn'_, _precompute\='auto'_, _Xy\=None_, _copy\_X\=True_, _coef\_init\=None_, _verbose\=False_, _return\_n\_iter\=False_, _positive\=False_, _check\_input\=True_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_coordinate_descent.py#L449)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "Link to this definition")

Compute elastic net path with coordinate descent.

The elastic net optimization function varies for mono and multi-outputs.

For mono-output tasks it is:

1 / (2 \* n\_samples) \* ||y \- Xw||^2\_2
+ alpha \* l1\_ratio \* ||w||\_1
+ 0.5 \* alpha \* (1 \- l1\_ratio) \* ||w||^2\_2

Copy to clipboard

For multi-output tasks it is:

1 / (2 \* n\_samples) \* ||Y \- XW||\_Fro^2
+ alpha \* l1\_ratio \* ||W||\_21
+ 0.5 \* alpha \* (1 \- l1\_ratio) \* ||W||\_Fro^2

Copy to clipboard

Where:

||W||\_21 \= \\sum\_i \\sqrt{\\sum\_j w\_{ij}^2}

Copy to clipboard

i.e. the sum of L2-norm of each row (task) (i=feature, j=task)

Read more in the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#elastic-net)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training data. Pass directly as Fortran-contiguous data to avoid unnecessary memory duplication. If `y` is mono-output then `X` can be sparse.

**y**{array-like, sparse matrix} of shape (n\_samples,) or (n\_samples, n\_targets)

Target values.

**l1\_ratio**float, default=0.5

Number between 0 and 1 passed to elastic net (scaling between l1 and l2 penalties). `l1_ratio=1` corresponds to the Lasso.

**eps**float, default=1e-3

Length of the path. `eps=1e-3` means that `alpha_min / alpha_max = 1e-3`.

**n\_alphas**int, default=100

Number of alphas along the regularization path.

**alphas**array-like, default=None

List of alphas where to compute the models. If None alphas are set automatically.

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

**check\_input**bool, default=True

If set to False, the input validation checks are skipped (including the Gram matrix when provided). It is assumed that they are handled by the caller.

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

The number of iterations taken by the coordinate descent optimizer to reach the specified tolerance for each alpha. (Is returned when `return_n_iter` is set to True).

See also

[`MultiTaskElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNet.html#sklearn.linear_model.MultiTaskElasticNet "sklearn.linear_model.MultiTaskElasticNet")

Multi-task ElasticNet model trained with L1/L2 mixed-norm as regularizer.

[`MultiTaskElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNetCV.html#sklearn.linear_model.MultiTaskElasticNetCV "sklearn.linear_model.MultiTaskElasticNetCV")

Multi-task L1/L2 ElasticNet with built-in cross-validation.

[`ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")

Linear regression with combined L1 and L2 priors as regularizer.

[`ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")

Elastic Net model with iterative fitting along a regularization path.

Notes

For an example, see [examples/linear\_model/plot\_lasso\_lasso\_lars\_elasticnet\_path.py](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html#sphx-glr-auto-examples-linear-model-plot-lasso-lasso-lars-elasticnet-path-py)
.

The underlying coordinate descent solver uses gap safe screening rules to speedup fitting time, see [User Guide on coordinate descent](https://scikit-learn.org/stable/modules/linear_model.html#coordinate-descent)
.

Examples

\>>> from sklearn.linear\_model import enet\_path
\>>> from sklearn.datasets import make\_regression
\>>> X, y, true\_coef \= make\_regression(
...    n\_samples\=100, n\_features\=5, n\_informative\=2, coef\=True, random\_state\=0
... )
\>>> true\_coef
array(\[ 0.        ,  0.        ,  0.        , 97.9, 45.7\])
\>>> alphas, estimated\_coef, \_ \= enet\_path(X, y, alphas\=3)
\>>> alphas.shape
(3,)
\>>> estimated\_coef
 array(\[\[ 0.,  0.787,  0.568\],\
        \[ 0.,  1.120,  0.620\],\
        \[-0., -2.129, -1.128\],\
        \[ 0., 23.046, 88.939\],\
        \[ 0., 10.637, 41.566\]\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

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