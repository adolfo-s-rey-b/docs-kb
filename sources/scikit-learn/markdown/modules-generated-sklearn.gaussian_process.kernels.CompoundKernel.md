[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html)

Collapse Sidebar Expand Sidebar

CompoundKernel[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html#compoundkernel "Link to this heading")

================================================================================================================================================================

class sklearn.gaussian\_process.kernels.CompoundKernel(_kernels_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L517)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html#sklearn.gaussian_process.kernels.CompoundKernel "Link to this definition")

Kernel which is composed of a set of other kernels.

Added in version 0.18.

Parameters:

**kernels**list of Kernels

The other kernels

Examples

\>>> from sklearn.gaussian\_process.kernels import WhiteKernel
\>>> from sklearn.gaussian\_process.kernels import RBF
\>>> from sklearn.gaussian\_process.kernels import CompoundKernel
\>>> kernel \= CompoundKernel(
...     \[WhiteKernel(noise\_level\=3.0), RBF(length\_scale\=2.0)\])
\>>> print(kernel.bounds)
\[\[-11.51292546  11.51292546\]\
 \[-11.51292546  11.51292546\]\]
\>>> print(kernel.n\_dims)
2
\>>> print(kernel.theta)
\[1.09861229 0.69314718\]

Copy to clipboard

\_\_call\_\_(_X_, _Y\=None_, _eval\_gradient\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L602)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html#sklearn.gaussian_process.kernels.CompoundKernel.__call__ "Link to this definition")

Return the kernel k(X, Y) and optionally its gradient.

Note that this compound kernel returns the results of all simple kernel stacked along an additional axis.

Parameters:

**X**array-like of shape (n\_samples\_X, n\_features) or list of object, default=None

Left argument of the returned kernel k(X, Y)

**Y**array-like of shape (n\_samples\_X, n\_features) or list of object, default=None

Right argument of the returned kernel k(X, Y). If None, k(X, X) is evaluated instead.

**eval\_gradient**bool, default=False

Determines whether the gradient with respect to the log of the kernel hyperparameter is computed.

Returns:

**K**ndarray of shape (n\_samples\_X, n\_samples\_Y, n\_kernels)

Kernel k(X, Y)

**K\_gradient**ndarray of shape (n\_samples\_X, n\_samples\_X, n\_dims, n\_kernels), optional

The gradient of the kernel k(X, X) with respect to the log of the hyperparameter of the kernel. Only returned when `eval_gradient` is True.

property bounds[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html#sklearn.gaussian_process.kernels.CompoundKernel.bounds "Link to this definition")

Returns the log-transformed bounds on the theta.

Returns:

**bounds**array of shape (n\_dims, 2)

The log-transformed bounds on the kernel’s hyperparameters theta

clone\_with\_theta(_theta_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L263)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html#sklearn.gaussian_process.kernels.CompoundKernel.clone_with_theta "Link to this definition")

Returns a clone of self with given hyperparameters theta.

Parameters:

**theta**ndarray of shape (n\_dims,)

The hyperparameters

diag(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L661)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html#sklearn.gaussian_process.kernels.CompoundKernel.diag "Link to this definition")

Returns the diagonal of the kernel k(X, X).

The result of this method is identical to `np.diag(self(X))`; however, it can be evaluated more efficiently since only the diagonal is evaluated.

Parameters:

**X**array-like of shape (n\_samples\_X, n\_features) or list of object

Argument to the kernel.

Returns:

**K\_diag**ndarray of shape (n\_samples\_X, n\_kernels)

Diagonal of kernel k(X, X)

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L546)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html#sklearn.gaussian_process.kernels.CompoundKernel.get_params "Link to this definition")

Get parameters of this kernel.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

property hyperparameters[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html#sklearn.gaussian_process.kernels.CompoundKernel.hyperparameters "Link to this definition")

Returns a list of all hyperparameter specifications.

is\_stationary()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L652)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html#sklearn.gaussian_process.kernels.CompoundKernel.is_stationary "Link to this definition")

Returns whether the kernel is stationary.

property n\_dims[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html#sklearn.gaussian_process.kernels.CompoundKernel.n_dims "Link to this definition")

Returns the number of non-fixed hyperparameters of the kernel.

property requires\_vector\_input[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html#sklearn.gaussian_process.kernels.CompoundKernel.requires_vector_input "Link to this definition")

Returns whether the kernel is defined on discrete structures.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L223)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html#sklearn.gaussian_process.kernels.CompoundKernel.set_params "Link to this definition")

Set the parameters of this kernel.

The method works on simple kernels as well as on nested kernels. The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Returns:

self

property theta[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html#sklearn.gaussian_process.kernels.CompoundKernel.theta "Link to this definition")

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