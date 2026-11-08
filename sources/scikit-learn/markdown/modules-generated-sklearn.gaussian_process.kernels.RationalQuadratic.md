[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html)

Collapse Sidebar Expand Sidebar

RationalQuadratic[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#rationalquadratic "Link to this heading")

=========================================================================================================================================================================

class sklearn.gaussian\_process.kernels.RationalQuadratic(_length\_scale\=1.0_, _alpha\=1.0_, _length\_scale\_bounds\=(1e-05, 100000.0)_, _alpha\_bounds\=(1e-05, 100000.0)_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L1801)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#sklearn.gaussian_process.kernels.RationalQuadratic "Link to this definition")

Rational Quadratic kernel.

The RationalQuadratic kernel can be seen as a scale mixture (an infinite sum) of RBF kernels with different characteristic length scales. It is parameterized by a length scale parameter l\>0 and a scale mixture parameter α\>0. Only the isotropic variant where length\_scale l is a scalar is supported at the moment. The kernel is given by:

k(xi,xj)\=(1+d(xi,xj)22αl2)−α

where α is the scale mixture parameter, l is the length scale of the kernel and d(⋅,⋅) is the Euclidean distance. For advice on how to set the parameters, see e.g. [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#rc7764613bdcf-1)
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/gaussian_process.html#gp-kernels)
.

Added in version 0.18.

Parameters:

**length\_scale**float > 0, default=1.0

The length scale of the kernel.

**alpha**float > 0, default=1.0

Scale mixture parameter

**length\_scale\_bounds**pair of floats >= 0 or “fixed”, default=(1e-5, 1e5)

The lower and upper bound on ‘length\_scale’. If set to “fixed”, ‘length\_scale’ cannot be changed during hyperparameter tuning.

**alpha\_bounds**pair of floats >= 0 or “fixed”, default=(1e-5, 1e5)

The lower and upper bound on ‘alpha’. If set to “fixed”, ‘alpha’ cannot be changed during hyperparameter tuning.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#id1)\
\]

[David Duvenaud (2014). “The Kernel Cookbook: Advice on Covariance functions”.](https://www.cs.toronto.edu/~duvenaud/cookbook/)

Examples

\>>> from sklearn.datasets import load\_iris
\>>> from sklearn.gaussian\_process import GaussianProcessClassifier
\>>> from sklearn.gaussian\_process.kernels import RationalQuadratic
\>>> X, y \= load\_iris(return\_X\_y\=True)
\>>> kernel \= RationalQuadratic(length\_scale\=1.0, alpha\=1.5)
\>>> gpc \= GaussianProcessClassifier(kernel\=kernel,
...         random\_state\=0).fit(X, y)
\>>> gpc.score(X, y)
0.9733
\>>> gpc.predict\_proba(X\[:2,:\])
array(\[\[0.8881, 0.0566, 0.05518\],\
        \[0.8678, 0.0707 , 0.0614\]\])

Copy to clipboard

\_\_call\_\_(_X_, _Y\=None_, _eval\_gradient\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L1884)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#sklearn.gaussian_process.kernels.RationalQuadratic.__call__ "Link to this definition")

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

**K\_gradient**ndarray of shape (n\_samples\_X, n\_samples\_X, n\_dims)

The gradient of the kernel k(X, X) with respect to the log of the hyperparameter of the kernel. Only returned when eval\_gradient is True.

property bounds[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#sklearn.gaussian_process.kernels.RationalQuadratic.bounds "Link to this definition")

Returns the log-transformed bounds on the theta.

Returns:

**bounds**ndarray of shape (n\_dims, 2)

The log-transformed bounds on the kernel’s hyperparameters theta

clone\_with\_theta(_theta_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L263)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#sklearn.gaussian_process.kernels.RationalQuadratic.clone_with_theta "Link to this definition")

Returns a clone of self with given hyperparameters theta.

Parameters:

**theta**ndarray of shape (n\_dims,)

The hyperparameters

diag(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L473)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#sklearn.gaussian_process.kernels.RationalQuadratic.diag "Link to this definition")

Returns the diagonal of the kernel k(X, X).

The result of this method is identical to np.diag(self(X)); however, it can be evaluated more efficiently since only the diagonal is evaluated.

Parameters:

**X**ndarray of shape (n\_samples\_X, n\_features)

Left argument of the returned kernel k(X, Y)

Returns:

**K\_diag**ndarray of shape (n\_samples\_X,)

Diagonal of kernel k(X, X)

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L184)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#sklearn.gaussian_process.kernels.RationalQuadratic.get_params "Link to this definition")

Get parameters of this kernel.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

property hyperparameters[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#sklearn.gaussian_process.kernels.RationalQuadratic.hyperparameters "Link to this definition")

Returns a list of all hyperparameter specifications.

is\_stationary()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L499)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#sklearn.gaussian_process.kernels.RationalQuadratic.is_stationary "Link to this definition")

Returns whether the kernel is stationary.

property n\_dims[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#sklearn.gaussian_process.kernels.RationalQuadratic.n_dims "Link to this definition")

Returns the number of non-fixed hyperparameters of the kernel.

property requires\_vector\_input[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#sklearn.gaussian_process.kernels.RationalQuadratic.requires_vector_input "Link to this definition")

Returns whether the kernel is defined on fixed-length feature vectors or generic objects. Defaults to True for backward compatibility.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L223)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#sklearn.gaussian_process.kernels.RationalQuadratic.set_params "Link to this definition")

Set the parameters of this kernel.

The method works on simple kernels as well as on nested kernels. The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Returns:

self

property theta[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#sklearn.gaussian_process.kernels.RationalQuadratic.theta "Link to this definition")

Returns the (flattened, log-transformed) non-fixed hyperparameters.

Note that theta are typically the log-transformed values of the kernel’s hyperparameters as this representation of the search space is more amenable for hyperparameter search, as hyperparameters like length-scales naturally live on a log-scale.

Returns:

**theta**ndarray of shape (n\_dims,)

The non-fixed, log-transformed hyperparameters of the kernel

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_co2_thumb.png)

[Forecasting of CO2 level on Mona Loa dataset using Gaussian process regression (GPR)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_co2.html)

Forecasting of CO2 level on Mona Loa dataset using Gaussian process regression (GPR)

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