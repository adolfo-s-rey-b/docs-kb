[Skip to main content](https://scikit-learn.org/stable/api/sklearn.gaussian_process.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/api/sklearn.gaussian_process.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/api/sklearn.gaussian_process.html)
[1.8.0](https://scikit-learn.org/1.8/api/sklearn.gaussian_process.html)
[1.7.2](https://scikit-learn.org/1.7/api/sklearn.gaussian_process.html)
[1.6.1](https://scikit-learn.org/1.6/api/sklearn.gaussian_process.html)
[1.5.2](https://scikit-learn.org/1.5/api/sklearn.gaussian_process.html)
[1.4.2](https://scikit-learn.org/1.4/api/sklearn.gaussian_process.html)

Collapse Sidebar Expand Sidebar

sklearn.gaussian\_process[#](https://scikit-learn.org/stable/api/sklearn.gaussian_process.html#module-sklearn.gaussian_process "Link to this heading")

=======================================================================================================================================================

Gaussian process based regression and classification.

**User guide.** See the [Gaussian Processes](https://scikit-learn.org/stable/modules/gaussian_process.html#gaussian-process)
 section for further details.

|     |     |
| --- | --- |
| [`GaussianProcessClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier") | Gaussian process classification (GPC) based on Laplace approximation. |
| [`GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor") | Gaussian process regression (GPR). |

Kernels[#](https://scikit-learn.org/stable/api/sklearn.gaussian_process.html#module-sklearn.gaussian_process.kernels "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

A set of kernels that can be combined by operators and used in Gaussian processes.

|     |     |
| --- | --- |
| [`kernels.CompoundKernel`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html#sklearn.gaussian_process.kernels.CompoundKernel "sklearn.gaussian_process.kernels.CompoundKernel") | Kernel which is composed of a set of other kernels. |
| [`kernels.ConstantKernel`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.ConstantKernel.html#sklearn.gaussian_process.kernels.ConstantKernel "sklearn.gaussian_process.kernels.ConstantKernel") | Constant kernel. |
| [`kernels.DotProduct`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#sklearn.gaussian_process.kernels.DotProduct "sklearn.gaussian_process.kernels.DotProduct") | Dot-Product kernel. |
| [`kernels.ExpSineSquared`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.ExpSineSquared.html#sklearn.gaussian_process.kernels.ExpSineSquared "sklearn.gaussian_process.kernels.ExpSineSquared") | Exp-Sine-Squared kernel (aka periodic kernel). |
| [`kernels.Exponentiation`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html#sklearn.gaussian_process.kernels.Exponentiation "sklearn.gaussian_process.kernels.Exponentiation") | The Exponentiation kernel takes one base kernel and a scalar parameter p and combines them via |
| [`kernels.Hyperparameter`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Hyperparameter.html#sklearn.gaussian_process.kernels.Hyperparameter "sklearn.gaussian_process.kernels.Hyperparameter") | A kernel hyperparameter's specification in form of a namedtuple. |
| [`kernels.Kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Kernel.html#sklearn.gaussian_process.kernels.Kernel "sklearn.gaussian_process.kernels.Kernel") | Base class for all kernels. |
| [`kernels.Matern`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#sklearn.gaussian_process.kernels.Matern "sklearn.gaussian_process.kernels.Matern") | Matern kernel. |
| [`kernels.PairwiseKernel`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html#sklearn.gaussian_process.kernels.PairwiseKernel "sklearn.gaussian_process.kernels.PairwiseKernel") | Wrapper for kernels in sklearn.metrics.pairwise. |
| [`kernels.Product`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Product.html#sklearn.gaussian_process.kernels.Product "sklearn.gaussian_process.kernels.Product") | The `Product` kernel takes two kernels k1 and k2 and combines them via |
| [`kernels.RBF`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF") | Radial basis function kernel (aka squared-exponential kernel). |
| [`kernels.RationalQuadratic`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#sklearn.gaussian_process.kernels.RationalQuadratic "sklearn.gaussian_process.kernels.RationalQuadratic") | Rational Quadratic kernel. |
| [`kernels.Sum`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Sum.html#sklearn.gaussian_process.kernels.Sum "sklearn.gaussian_process.kernels.Sum") | The `Sum` kernel takes two kernels k1 and k2 and combines them via |
| [`kernels.WhiteKernel`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.WhiteKernel.html#sklearn.gaussian_process.kernels.WhiteKernel "sklearn.gaussian_process.kernels.WhiteKernel") | White kernel. |