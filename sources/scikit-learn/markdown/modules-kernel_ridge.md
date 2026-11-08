[Skip to main content](https://scikit-learn.org/stable/modules/kernel_ridge.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/kernel_ridge.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/kernel_ridge.html)
[1.8.0](https://scikit-learn.org/1.8/modules/kernel_ridge.html)
[1.7.2](https://scikit-learn.org/1.7/modules/kernel_ridge.html)
[1.6.1](https://scikit-learn.org/1.6/modules/kernel_ridge.html)
[1.5.2](https://scikit-learn.org/1.5/modules/kernel_ridge.html)
[1.4.2](https://scikit-learn.org/1.4/modules/kernel_ridge.html)

Collapse Sidebar Expand Sidebar

1.3. Kernel ridge regression[#](https://scikit-learn.org/stable/modules/kernel_ridge.html#kernel-ridge-regression "Link to this heading")

==========================================================================================================================================

Kernel ridge regression (KRR) [\[M2012\]](https://scikit-learn.org/stable/modules/kernel_ridge.html#m2012)
 combines [Ridge regression and classification](https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression)
 (linear least squares with L2\-norm regularization) with the [kernel trick](https://en.wikipedia.org/wiki/Kernel_method)
. It thus learns a linear function in the space induced by the respective kernel and the data. For non-linear kernels, this corresponds to a non-linear function in the original space.

The form of the model learned by [`KernelRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge")
 is identical to support vector regression ([`SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
). However, different loss functions are used: KRR uses squared error loss while support vector regression uses ϵ\-insensitive loss, both combined with L2 regularization. In contrast to [`SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
, fitting [`KernelRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge")
 can be done in closed-form and is typically faster for medium-sized datasets. On the other hand, the learned model is non-sparse and thus slower than [`SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
, which learns a sparse model for ϵ\>0, at prediction-time.

The following figure compares [`KernelRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge")
 and [`SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
 on an artificial dataset, which consists of a sinusoidal target function and strong noise added to every fifth datapoint. The learned model of [`KernelRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge")
 and [`SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
 is plotted, where both complexity/regularization and bandwidth of the RBF kernel have been optimized using grid-search. The learned functions are very similar; however, fitting [`KernelRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge")
 is approximately seven times faster than fitting [`SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
 (both with grid-search). However, prediction of 100,000 target values is more than three times faster with [`SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
 since it has learned a sparse model using only approximately 1/3 of the 100 training datapoints as support vectors.

[![../_images/sphx_glr_plot_kernel_ridge_regression_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_ridge_regression_001.png)](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_ridge_regression.html)

The next figure compares the time for fitting and prediction of [`KernelRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge")
 and [`SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
 for different sizes of the training set. Fitting [`KernelRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge")
 is faster than [`SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
 for medium-sized training sets (less than 1000 samples); however, for larger training sets [`SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
 scales better. With regard to prediction time, [`SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
 is faster than [`KernelRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge")
 for all sizes of the training set because of the learned sparse solution. Note that the degree of sparsity and thus the prediction time depends on the parameters ϵ and C of the [`SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
; ϵ\=0 would correspond to a dense model.

[![../_images/sphx_glr_plot_kernel_ridge_regression_002.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_ridge_regression_002.png)](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_ridge_regression.html)

Examples

*   [Comparison of kernel ridge regression and SVR](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_ridge_regression.html#sphx-glr-auto-examples-miscellaneous-plot-kernel-ridge-regression-py)
    

References

\[[M2012](https://scikit-learn.org/stable/modules/kernel_ridge.html#id1)\
\]

“Machine Learning: A Probabilistic Perspective” Murphy, K. P. - chapter 14.4.3, pp. 492-493, The MIT Press, 2012

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)