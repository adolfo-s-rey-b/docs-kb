[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html)

Collapse Sidebar Expand Sidebar

Exponentiation[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html#exponentiation "Link to this heading")

================================================================================================================================================================

class sklearn.gaussian\_process.kernels.Exponentiation(_kernel_, _exponent_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L996)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html#sklearn.gaussian_process.kernels.Exponentiation "Link to this definition")

The Exponentiation kernel takes one base kernel and a scalar parameter p and combines them via

kexp(X,Y)\=k(X,Y)p

Note that the `__pow__` magic method is overridden, so `Exponentiation(RBF(), 2)` is equivalent to using the \*\* operator with `RBF() ** 2`.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/gaussian_process.html#gp-kernels)
.

Added in version 0.18.

Parameters:

**kernel**Kernel

The base kernel

**exponent**float

The exponent for the base kernel

Examples

\>>> from sklearn.datasets import make\_friedman2
\>>> from sklearn.gaussian\_process import GaussianProcessRegressor
\>>> from sklearn.gaussian\_process.kernels import (RationalQuadratic,
...            Exponentiation)
\>>> X, y \= make\_friedman2(n\_samples\=500, noise\=0, random\_state\=0)
\>>> kernel \= Exponentiation(RationalQuadratic(), exponent\=2)
\>>> gpr \= GaussianProcessRegressor(kernel\=kernel, alpha\=5,
...         random\_state\=0).fit(X, y)
\>>> gpr.score(X, y)
0.419
\>>> gpr.predict(X\[:1,:\], return\_std\=True)
(array(\[635.5\]), array(\[0.559\]))

Copy to clipboard

\_\_call\_\_(_X_, _Y\=None_, _eval\_gradient\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L1119)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html#sklearn.gaussian_process.kernels.Exponentiation.__call__ "Link to this definition")

Return the kernel k(X, Y) and optionally its gradient.

Parameters:

**X**array-like of shape (n\_samples\_X, n\_features) or list of object

Left argument of the returned kernel k(X, Y)

**Y**array-like of shape (n\_samples\_Y, n\_features) or list of object, default=None

Right argument of the returned kernel k(X, Y). If None, k(X, X) is evaluated instead.

**eval\_gradient**bool, default=False

Determines whether the gradient with respect to the log of the kernel hyperparameter is computed.

Returns:

**K**ndarray of shape (n\_samples\_X, n\_samples\_Y)

Kernel k(X, Y)

**K\_gradient**ndarray of shape (n\_samples\_X, n\_samples\_X, n\_dims), optional

The gradient of the kernel k(X, X) with respect to the log of the hyperparameter of the kernel. Only returned when `eval_gradient` is True.

property bounds[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html#sklearn.gaussian_process.kernels.Exponentiation.bounds "Link to this definition")

Returns the log-transformed bounds on the theta.

Returns:

**bounds**ndarray of shape (n\_dims, 2)

The log-transformed bounds on the kernel’s hyperparameters theta

clone\_with\_theta(_theta_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L263)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html#sklearn.gaussian_process.kernels.Exponentiation.clone_with_theta "Link to this definition")

Returns a clone of self with given hyperparameters theta.

Parameters:

**theta**ndarray of shape (n\_dims,)

The hyperparameters

diag(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L1155)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html#sklearn.gaussian_process.kernels.Exponentiation.diag "Link to this definition")

Returns the diagonal of the kernel k(X, X).

The result of this method is identical to np.diag(self(X)); however, it can be evaluated more efficiently since only the diagonal is evaluated.

Parameters:

**X**array-like of shape (n\_samples\_X, n\_features) or list of object

Argument to the kernel.

Returns:

**K\_diag**ndarray of shape (n\_samples\_X,)

Diagonal of kernel k(X, X)

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L1041)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html#sklearn.gaussian_process.kernels.Exponentiation.get_params "Link to this definition")

Get parameters of this kernel.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

property hyperparameters[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html#sklearn.gaussian_process.kernels.Exponentiation.hyperparameters "Link to this definition")

Returns a list of all hyperparameter.

is\_stationary()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L1177)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html#sklearn.gaussian_process.kernels.Exponentiation.is_stationary "Link to this definition")

Returns whether the kernel is stationary.

property n\_dims[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html#sklearn.gaussian_process.kernels.Exponentiation.n_dims "Link to this definition")

Returns the number of non-fixed hyperparameters of the kernel.

property requires\_vector\_input[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html#sklearn.gaussian_process.kernels.Exponentiation.requires_vector_input "Link to this definition")

Returns whether the kernel is defined on discrete structures.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L223)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html#sklearn.gaussian_process.kernels.Exponentiation.set_params "Link to this definition")

Set the parameters of this kernel.

The method works on simple kernels as well as on nested kernels. The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Returns:

self

property theta[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html#sklearn.gaussian_process.kernels.Exponentiation.theta "Link to this definition")

Returns the (flattened, log-transformed) non-fixed hyperparameters.

Note that theta are typically the log-transformed values of the kernel’s hyperparameters as this representation of the search space is more amenable for hyperparameter search, as hyperparameters like length-scales naturally live on a log-scale.

Returns:

**theta**ndarray of shape (n\_dims,)

The non-fixed, log-transformed hyperparameters of the kernel

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)