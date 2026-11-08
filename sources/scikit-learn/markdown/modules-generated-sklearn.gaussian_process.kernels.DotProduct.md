[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html)

Collapse Sidebar Expand Sidebar

DotProduct[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#dotproduct "Link to this heading")

====================================================================================================================================================

class sklearn.gaussian\_process.kernels.DotProduct(_sigma\_0\=1.0_, _sigma\_0\_bounds\=(1e-05, 100000.0)_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L2102)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#sklearn.gaussian_process.kernels.DotProduct "Link to this definition")

Dot-Product kernel.

The DotProduct kernel is non-stationary and can be obtained from linear regression by putting N(0,1) priors on the coefficients of xd(d\=1,...,D) and a prior of N(0,σ02) on the bias. The DotProduct kernel is invariant to a rotation of the coordinates about the origin, but not translations. It is parameterized by a parameter sigma\_0 σ which controls the inhomogenity of the kernel. For σ02\=0, the kernel is called the homogeneous linear kernel, otherwise it is inhomogeneous. The kernel is given by

k(xi,xj)\=σ02+xi⋅xj

The DotProduct kernel is commonly combined with exponentiation.

See [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#r95f74c4622c1-1)
, Chapter 4, Section 4.2, for further details regarding the DotProduct kernel.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/gaussian_process.html#gp-kernels)
.

Added in version 0.18.

Parameters:

**sigma\_0**float >= 0, default=1.0

Parameter controlling the inhomogenity of the kernel. If sigma\_0=0, the kernel is homogeneous.

**sigma\_0\_bounds**pair of floats >= 0 or “fixed”, default=(1e-5, 1e5)

The lower and upper bound on ‘sigma\_0’. If set to “fixed”, ‘sigma\_0’ cannot be changed during hyperparameter tuning.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#id1)\
\]

[Carl Edward Rasmussen, Christopher K. I. Williams (2006). “Gaussian Processes for Machine Learning”. The MIT Press.](http://www.gaussianprocess.org/gpml/)

Examples

\>>> from sklearn.datasets import make\_friedman2
\>>> from sklearn.gaussian\_process import GaussianProcessRegressor
\>>> from sklearn.gaussian\_process.kernels import DotProduct, WhiteKernel
\>>> X, y \= make\_friedman2(n\_samples\=500, noise\=0, random\_state\=0)
\>>> kernel \= DotProduct() + WhiteKernel()
\>>> gpr \= GaussianProcessRegressor(kernel\=kernel,
...         random\_state\=0).fit(X, y)
\>>> gpr.score(X, y)
0.3680
\>>> gpr.predict(X\[:2,:\], return\_std\=True)
(array(\[653.0, 592.1\]), array(\[316.6, 316.6\]))

Copy to clipboard

\_\_call\_\_(_X_, _Y\=None_, _eval\_gradient\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L2167)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#sklearn.gaussian_process.kernels.DotProduct.__call__ "Link to this definition")

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

property bounds[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#sklearn.gaussian_process.kernels.DotProduct.bounds "Link to this definition")

Returns the log-transformed bounds on the theta.

Returns:

**bounds**ndarray of shape (n\_dims, 2)

The log-transformed bounds on the kernel’s hyperparameters theta

clone\_with\_theta(_theta_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L263)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#sklearn.gaussian_process.kernels.DotProduct.clone_with_theta "Link to this definition")

Returns a clone of self with given hyperparameters theta.

Parameters:

**theta**ndarray of shape (n\_dims,)

The hyperparameters

diag(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L2213)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#sklearn.gaussian_process.kernels.DotProduct.diag "Link to this definition")

Returns the diagonal of the kernel k(X, X).

The result of this method is identical to np.diag(self(X)); however, it can be evaluated more efficiently since only the diagonal is evaluated.

Parameters:

**X**ndarray of shape (n\_samples\_X, n\_features)

Left argument of the returned kernel k(X, Y).

Returns:

**K\_diag**ndarray of shape (n\_samples\_X,)

Diagonal of kernel k(X, X).

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L184)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#sklearn.gaussian_process.kernels.DotProduct.get_params "Link to this definition")

Get parameters of this kernel.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

property hyperparameters[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#sklearn.gaussian_process.kernels.DotProduct.hyperparameters "Link to this definition")

Returns a list of all hyperparameter specifications.

is\_stationary()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L2232)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#sklearn.gaussian_process.kernels.DotProduct.is_stationary "Link to this definition")

Returns whether the kernel is stationary.

property n\_dims[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#sklearn.gaussian_process.kernels.DotProduct.n_dims "Link to this definition")

Returns the number of non-fixed hyperparameters of the kernel.

property requires\_vector\_input[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#sklearn.gaussian_process.kernels.DotProduct.requires_vector_input "Link to this definition")

Returns whether the kernel is defined on fixed-length feature vectors or generic objects. Defaults to True for backward compatibility.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L223)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#sklearn.gaussian_process.kernels.DotProduct.set_params "Link to this definition")

Set the parameters of this kernel.

The method works on simple kernels as well as on nested kernels. The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Returns:

self

property theta[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#sklearn.gaussian_process.kernels.DotProduct.theta "Link to this definition")

Returns the (flattened, log-transformed) non-fixed hyperparameters.

Note that theta are typically the log-transformed values of the kernel’s hyperparameters as this representation of the search space is more amenable for hyperparameter search, as hyperparameters like length-scales naturally live on a log-scale.

Returns:

**theta**ndarray of shape (n\_dims,)

The non-fixed, log-transformed hyperparameters of the kernel

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_isoprobability_thumb.png)

[Iso-probability lines for Gaussian Processes classification (GPC)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_isoprobability.html)

Iso-probability lines for Gaussian Processes classification (GPC)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_xor_thumb.png)

[Illustration of Gaussian process classification (GPC) on the XOR dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_xor.html)

Illustration of Gaussian process classification (GPC) on the XOR dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_prior_posterior_thumb.png)

[Illustration of prior and posterior Gaussian process for different kernels](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_prior_posterior.html)

Illustration of prior and posterior Gaussian process for different kernels

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)