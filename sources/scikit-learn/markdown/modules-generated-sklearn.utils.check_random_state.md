[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.check_random_state.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.check_random_state.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.check_random_state.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.check_random_state.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.check_random_state.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.check_random_state.html)

Collapse Sidebar Expand Sidebar

check\_random\_state[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html#check-random-state "Link to this heading")

===========================================================================================================================================================

sklearn.utils.check\_random\_state(_seed_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/validation.py#L1455)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html#sklearn.utils.check_random_state "Link to this definition")

Turn seed into an np.random.RandomState instance.

Parameters:

**seed**None, int or instance of RandomState

If seed is None, return the RandomState singleton used by np.random. If seed is an int, return a new RandomState instance seeded with seed. If seed is already a RandomState instance, return it. Otherwise raise ValueError.

Returns:

[`numpy.random.RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "(in NumPy v2.5)")

The random state object based on `seed` parameter.

Examples

\>>> from sklearn.utils.validation import check\_random\_state
\>>> check\_random\_state(42)
RandomState(MT19937) at 0x...

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_callback_support_thumb.png)

[Supporting callbacks in third party estimators](https://scikit-learn.org/stable/auto_examples/callbacks/plot_callback_support.html)

Supporting callbacks in third party estimators

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_stability_low_dim_dense_thumb.png)

[Empirical evaluation of the impact of k-means initialization](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.html)

Empirical evaluation of the impact of k-means initialization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_logistic_regression_mnist_thumb.png)

[MNIST classification using multinomial logistic + L1](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_mnist.html)

MNIST classification using multinomial logistic + L1

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_manifold_sphere_thumb.png)

[Manifold Learning methods on a severed sphere](https://scikit-learn.org/stable/auto_examples/manifold/plot_manifold_sphere.html)

Manifold Learning methods on a severed sphere

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_isotonic_regression_thumb.png)

[Isotonic Regression](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_isotonic_regression.html)

Isotonic Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multioutput_face_completion_thumb.png)

[Face completion with a multi-output estimators](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multioutput_face_completion.html)

Face completion with a multi-output estimators

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)