[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html)

Collapse Sidebar Expand Sidebar

PairwiseKernel[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html#pairwisekernel "Link to this heading")

================================================================================================================================================================

class sklearn.gaussian\_process.kernels.PairwiseKernel(_gamma\=1.0_, _gamma\_bounds\=(1e-05, 100000.0)_, _metric\='linear'_, _pairwise\_kernels\_kwargs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L2253)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html#sklearn.gaussian_process.kernels.PairwiseKernel "Link to this definition")

Wrapper for kernels in sklearn.metrics.pairwise.

A thin wrapper around the functionality of the kernels in sklearn.metrics.pairwise.

Note: Evaluation of eval\_gradient is not analytic but numeric and all

kernels support only isotropic distances. The parameter gamma is considered to be a hyperparameter and may be optimized. The other kernel parameters are set directly at initialization and are kept fixed.

Added in version 0.18.

Parameters:

**gamma**float, default=1.0

Parameter gamma of the pairwise kernel specified by metric. It should be positive.

**gamma\_bounds**pair of floats >= 0 or “fixed”, default=(1e-5, 1e5)

The lower and upper bound on ‘gamma’. If set to “fixed”, ‘gamma’ cannot be changed during hyperparameter tuning.

**metric**{“linear”, “additive\_chi2”, “chi2”, “poly”, “polynomial”, “rbf”, “laplacian”, “sigmoid”, “cosine”} or callable, default=”linear”

The metric to use when calculating kernel between instances in a feature array. If metric is a string, it must be one of the metrics in pairwise.PAIRWISE\_KERNEL\_FUNCTIONS. If metric is “precomputed”, X is assumed to be a kernel matrix. Alternatively, if metric is a callable function, it is called on each pair of instances (rows) and the resulting value recorded. The callable should take two arrays from X as input and return a value indicating the distance between them.

**pairwise\_kernels\_kwargs**dict, default=None

All entries of this dict (if any) are passed as keyword arguments to the pairwise kernel function.

Examples

\>>> from sklearn.datasets import load\_iris
\>>> from sklearn.gaussian\_process import GaussianProcessClassifier
\>>> from sklearn.gaussian\_process.kernels import PairwiseKernel
\>>> X, y \= load\_iris(return\_X\_y\=True)
\>>> kernel \= PairwiseKernel(metric\='rbf')
\>>> gpc \= GaussianProcessClassifier(kernel\=kernel,
...         random\_state\=0).fit(X, y)
\>>> gpc.score(X, y)
0.9733
\>>> gpc.predict\_proba(X\[:2,:\])
array(\[\[0.8880, 0.05663, 0.05532\],\
       \[0.8676, 0.07073, 0.06165\]\])

Copy to clipboard

\_\_call\_\_(_X_, _Y\=None_, _eval\_gradient\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L2326)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html#sklearn.gaussian_process.kernels.PairwiseKernel.__call__ "Link to this definition")

Return the kernel k(X, Y) and optionally its gradient.

Parameters:

**X**ndarray of shape (n\_samples\_X, n\_features)

Left argument of the returned kernel k(X, Y)

**Y**ndarray of shape (n\_samples\_Y, n\_features), default=None

Right argument of the returned kernel k(X, Y). If None, k(X, X) if evaluated instead.

**eval\_gradient**bool, default=False

Determines whether the gradient with respect to the log of the kernel hyperparameter is computed. Only supported when Y is None.

Returns:

**K**ndarray of shape (n\_samples\_X, n\_samples\_Y)

Kernel k(X, Y)

**K\_gradient**ndarray of shape (n\_samples\_X, n\_samples\_X, n\_dims), optional

The gradient of the kernel k(X, X) with respect to the log of the hyperparameter of the kernel. Only returned when `eval_gradient` is True.

property bounds[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html#sklearn.gaussian_process.kernels.PairwiseKernel.bounds "Link to this definition")

Returns the log-transformed bounds on the theta.

Returns:

**bounds**ndarray of shape (n\_dims, 2)

The log-transformed bounds on the kernel’s hyperparameters theta

clone\_with\_theta(_theta_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L263)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html#sklearn.gaussian_process.kernels.PairwiseKernel.clone_with_theta "Link to this definition")

Returns a clone of self with given hyperparameters theta.

Parameters:

**theta**ndarray of shape (n\_dims,)

The hyperparameters

diag(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L2386)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html#sklearn.gaussian_process.kernels.PairwiseKernel.diag "Link to this definition")

Returns the diagonal of the kernel k(X, X).

The result of this method is identical to np.diag(self(X)); however, it can be evaluated more efficiently since only the diagonal is evaluated.

Parameters:

**X**ndarray of shape (n\_samples\_X, n\_features)

Left argument of the returned kernel k(X, Y)

Returns:

**K\_diag**ndarray of shape (n\_samples\_X,)

Diagonal of kernel k(X, X)

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L184)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html#sklearn.gaussian_process.kernels.PairwiseKernel.get_params "Link to this definition")

Get parameters of this kernel.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

property hyperparameters[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html#sklearn.gaussian_process.kernels.PairwiseKernel.hyperparameters "Link to this definition")

Returns a list of all hyperparameter specifications.

is\_stationary()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L2406)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html#sklearn.gaussian_process.kernels.PairwiseKernel.is_stationary "Link to this definition")

Returns whether the kernel is stationary.

property n\_dims[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html#sklearn.gaussian_process.kernels.PairwiseKernel.n_dims "Link to this definition")

Returns the number of non-fixed hyperparameters of the kernel.

property requires\_vector\_input[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html#sklearn.gaussian_process.kernels.PairwiseKernel.requires_vector_input "Link to this definition")

Returns whether the kernel is defined on fixed-length feature vectors or generic objects. Defaults to True for backward compatibility.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L223)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html#sklearn.gaussian_process.kernels.PairwiseKernel.set_params "Link to this definition")

Set the parameters of this kernel.

The method works on simple kernels as well as on nested kernels. The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Returns:

self

property theta[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html#sklearn.gaussian_process.kernels.PairwiseKernel.theta "Link to this definition")

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