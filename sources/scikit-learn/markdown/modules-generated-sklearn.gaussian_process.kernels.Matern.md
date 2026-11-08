[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.gaussian_process.kernels.Matern.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.gaussian_process.kernels.Matern.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.gaussian_process.kernels.Matern.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.gaussian_process.kernels.Matern.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.gaussian_process.kernels.Matern.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.gaussian_process.kernels.Matern.html)

Collapse Sidebar Expand Sidebar

Matern[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#matern "Link to this heading")

========================================================================================================================================

class sklearn.gaussian\_process.kernels.Matern(_length\_scale\=1.0_, _length\_scale\_bounds\=(1e-05, 100000.0)_, _nu\=1.5_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L1601)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#sklearn.gaussian_process.kernels.Matern "Link to this definition")

Matern kernel.

The class of Matern kernels is a generalization of the [`RBF`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
. It has an additional parameter ν which controls the smoothness of the resulting function. The smaller ν, the less smooth the approximated function is. As ν→∞, the kernel becomes equivalent to the [`RBF`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
 kernel. When ν\=1/2, the Matérn kernel becomes identical to the absolute exponential kernel. Important intermediate values are ν\=1.5 (once differentiable functions) and ν\=2.5 (twice differentiable functions).

The kernel is given by:

k(xi,xj)\=1Γ(ν)2ν−1(2νld(xi,xj))νKν(2νld(xi,xj))

where d(⋅,⋅) is the Euclidean distance, Kν(⋅) is a modified Bessel function and Γ(⋅) is the gamma function. See [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#rc15b4675c755-1)
, Chapter 4, Section 4.2, for details regarding the different variants of the Matern kernel.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/gaussian_process.html#gp-kernels)
.

Added in version 0.18.

Parameters:

**length\_scale**float or ndarray of shape (n\_features,), default=1.0

The length scale of the kernel. If a float, an isotropic kernel is used. If an array, an anisotropic kernel is used where each dimension of l defines the length-scale of the respective feature dimension.

**length\_scale\_bounds**pair of floats >= 0 or “fixed”, default=(1e-5, 1e5)

The lower and upper bound on ‘length\_scale’. If set to “fixed”, ‘length\_scale’ cannot be changed during hyperparameter tuning.

**nu**float, default=1.5

The parameter nu controlling the smoothness of the learned function. The smaller nu, the less smooth the approximated function is. For nu=inf, the kernel becomes equivalent to the RBF kernel and for nu=0.5 to the absolute exponential kernel. Important intermediate values are nu=1.5 (once differentiable functions) and nu=2.5 (twice differentiable functions). Note that values of nu not in \[0.5, 1.5, 2.5, inf\] incur a considerably higher computational cost (appr. 10 times higher) since they require to evaluate the modified Bessel function. Furthermore, in contrast to l, nu is kept fixed to its initial value and not optimized.

References

\[[1](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#id1)\
\]

[Carl Edward Rasmussen, Christopher K. I. Williams (2006). “Gaussian Processes for Machine Learning”. The MIT Press.](http://www.gaussianprocess.org/gpml/)

Examples

\>>> from sklearn.datasets import load\_iris
\>>> from sklearn.gaussian\_process import GaussianProcessClassifier
\>>> from sklearn.gaussian\_process.kernels import Matern
\>>> X, y \= load\_iris(return\_X\_y\=True)
\>>> kernel \= 1.0 \* Matern(length\_scale\=1.0, nu\=1.5)
\>>> gpc \= GaussianProcessClassifier(kernel\=kernel,
...         random\_state\=0).fit(X, y)
\>>> gpc.score(X, y)
0.9866
\>>> gpc.predict\_proba(X\[:2,:\])
array(\[\[0.8513, 0.0368, 0.1117\],\
        \[0.8086, 0.0693, 0.1220\]\])

Copy to clipboard

\_\_call\_\_(_X_, _Y\=None_, _eval\_gradient\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L1685)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#sklearn.gaussian_process.kernels.Matern.__call__ "Link to this definition")

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

property bounds[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#sklearn.gaussian_process.kernels.Matern.bounds "Link to this definition")

Returns the log-transformed bounds on the theta.

Returns:

**bounds**ndarray of shape (n\_dims, 2)

The log-transformed bounds on the kernel’s hyperparameters theta

clone\_with\_theta(_theta_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L263)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#sklearn.gaussian_process.kernels.Matern.clone_with_theta "Link to this definition")

Returns a clone of self with given hyperparameters theta.

Parameters:

**theta**ndarray of shape (n\_dims,)

The hyperparameters

diag(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L473)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#sklearn.gaussian_process.kernels.Matern.diag "Link to this definition")

Returns the diagonal of the kernel k(X, X).

The result of this method is identical to np.diag(self(X)); however, it can be evaluated more efficiently since only the diagonal is evaluated.

Parameters:

**X**ndarray of shape (n\_samples\_X, n\_features)

Left argument of the returned kernel k(X, Y)

Returns:

**K\_diag**ndarray of shape (n\_samples\_X,)

Diagonal of kernel k(X, X)

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L184)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#sklearn.gaussian_process.kernels.Matern.get_params "Link to this definition")

Get parameters of this kernel.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

property hyperparameters[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#sklearn.gaussian_process.kernels.Matern.hyperparameters "Link to this definition")

Returns a list of all hyperparameter specifications.

is\_stationary()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L499)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#sklearn.gaussian_process.kernels.Matern.is_stationary "Link to this definition")

Returns whether the kernel is stationary.

property n\_dims[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#sklearn.gaussian_process.kernels.Matern.n_dims "Link to this definition")

Returns the number of non-fixed hyperparameters of the kernel.

property requires\_vector\_input[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#sklearn.gaussian_process.kernels.Matern.requires_vector_input "Link to this definition")

Returns whether the kernel is defined on fixed-length feature vectors or generic objects. Defaults to True for backward compatibility.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/gaussian_process/kernels.py#L223)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#sklearn.gaussian_process.kernels.Matern.set_params "Link to this definition")

Set the parameters of this kernel.

The method works on simple kernels as well as on nested kernels. The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Returns:

self

property theta[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#sklearn.gaussian_process.kernels.Matern.theta "Link to this definition")

Returns the (flattened, log-transformed) non-fixed hyperparameters.

Note that theta are typically the log-transformed values of the kernel’s hyperparameters as this representation of the search space is more amenable for hyperparameter search, as hyperparameters like length-scales naturally live on a log-scale.

Returns:

**theta**ndarray of shape (n\_dims,)

The non-fixed, log-transformed hyperparameters of the kernel

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

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