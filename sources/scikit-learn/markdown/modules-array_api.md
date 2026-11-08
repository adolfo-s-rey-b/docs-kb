[Skip to main content](https://scikit-learn.org/stable/modules/array_api.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/array_api.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/array_api.html)
[1.8.0](https://scikit-learn.org/1.8/modules/array_api.html)
[1.7.2](https://scikit-learn.org/1.7/modules/array_api.html)
[1.6.1](https://scikit-learn.org/1.6/modules/array_api.html)
[1.5.2](https://scikit-learn.org/1.5/modules/array_api.html)
[1.4.2](https://scikit-learn.org/1.4/modules/array_api.html)

Collapse Sidebar Expand Sidebar

13.2. Array API support (experimental)[#](https://scikit-learn.org/stable/modules/array_api.html#array-api-support-experimental "Link to this heading")

========================================================================================================================================================

The [array API](https://data-apis.org/array-api/latest/)
 specification defines a standard API for all array manipulation libraries with a NumPy-like API.

Some scikit-learn estimators that primarily rely on NumPy (as opposed to using Cython) to implement the algorithmic logic of their `fit`, `predict` or `transform` methods can be configured to accept any Array API compatible input data structures and automatically dispatch operations to the underlying namespace instead of relying on NumPy.

At this stage, this support is **considered experimental**, must be enabled explicitly by the `array_api_dispatch` configuration and assumes that the latest versions libraries are installed. See below for details.

The following video provides an overview of the standard’s design principles and how it facilitates interoperability between array libraries:

*   [Scikit-learn on GPUs with Array API](https://www.youtube.com/watch?v=c_s8tr1AizA)
     by [Thomas Fan](https://github.com/thomasjpfan)
     at PyData NYC 2023.
    

13.2.1. Supported array libraries[#](https://scikit-learn.org/stable/modules/array_api.html#supported-array-libraries "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

The following table lists the libraries and hardware for which we run automated compliance tests on a regular basis. Other array API conforming libraries and devices might also work out of the box.

   
| Library | Install | Supported Devices | Notes |
| --- | --- | --- | --- |
| [PyTorch](https://pytorch.org/) | [Install](https://pytorch.org/get-started/locally/) | CPU, NVIDIA GPU (CUDA), Apple GPU (MPS), Intel GPU (XPU) | See [Note on MPS device support](https://scikit-learn.org/stable/modules/array_api.html#mps-support)<br>; see [Note on Intel GPU support](https://scikit-learn.org/stable/modules/array_api.html#xpu-support)<br>; see [Note on device support for float64](https://scikit-learn.org/stable/modules/array_api.html#device-support-for-float64) |
| [CuPy](https://cupy.dev/) | [Install](https://docs.cupy.dev/en/stable/install.html) | CUDA |     |
| [dpnp](https://intelpython.github.io/dpnp/) | [Install](https://intelpython.github.io/dpnp/quick_start_guide.html) | CPU, Intel GPU (SYCL) | See install link for driver setup; see [Note on Intel GPU support](https://scikit-learn.org/stable/modules/array_api.html#xpu-support)<br>; see [Note on device support for float64](https://scikit-learn.org/stable/modules/array_api.html#device-support-for-float64) |

Coverage is expected to grow over time.

13.2.2. Enabling array API support[#](https://scikit-learn.org/stable/modules/array_api.html#enabling-array-api-support "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

The configuration parameter `array_api_dispatch` needs to be set to `True` to enable array API support. We recommend setting this configuration globally to ensure consistent behaviour and prevent accidental mixing of array namespaces. Note that in the examples below, we use a context manager ([`config_context`](https://scikit-learn.org/stable/modules/generated/sklearn.config_context.html#sklearn.config_context "sklearn.config_context")
) to avoid having to reset it to `False` at the end of every code snippet, so as to not affect the rest of the documentation.

Scikit-learn’s support for the array API standard requires the environment variable `SCIPY_ARRAY_API` to be set to `1` before importing `scipy` and `scikit-learn`:

export SCIPY\_ARRAY\_API\=1

Copy to clipboard

Please note that this environment variable is intended for temporary use. For more details, refer to SciPy’s [Array API documentation](https://docs.scipy.org/doc/scipy/dev/api-dev/array_api.html#using-array-api-standard-support)
.

The array API functionality assumes that the latest versions of scikit-learn’s dependencies are installed. Older versions might work, but we make no promises. While array API support is marked as experimental, backwards compatibility is not guaranteed. In particular, when a newer version of a dependency fixes a bug we will not introduce additional code to backport the fix or maintain compatibility with older versions.

Scikit-learn accepts [array-like](https://scikit-learn.org/stable/glossary.html#term-array-like)
 inputs for all `metrics` and some estimators. When `array_api_dispatch=False`, these inputs are converted into NumPy arrays using [`numpy.asarray`](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "(in NumPy v2.5)")
 (or [`numpy.array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "(in NumPy v2.5)")
). While this will successfully convert some array API inputs (e.g., JAX array), we generally recommend setting `array_api_dispatch=True` when using array API inputs. This is because NumPy conversion can often fail, e.g., torch tensor allocated on GPU.

13.2.3. Example usage[#](https://scikit-learn.org/stable/modules/array_api.html#example-usage "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

The example code snippet below demonstrates how to use [PyTorch](https://pytorch.org/)
 to run [`LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
 on a CUDA GPU:

\>>> from sklearn.datasets import make\_classification
\>>> from sklearn import config\_context
\>>> from sklearn.discriminant\_analysis import LinearDiscriminantAnalysis
\>>> import torch

\>>> X\_np, y\_np \= make\_classification(random\_state\=0)
\>>> X\_torch \= torch.asarray(X\_np, device\="cuda", dtype\=torch.float32)
\>>> y\_torch \= torch.asarray(y\_np, device\="cuda", dtype\=torch.float32)

\>>> with config\_context(array\_api\_dispatch\=True):
...     lda \= LinearDiscriminantAnalysis()
...     X\_trans \= lda.fit\_transform(X\_torch, y\_torch)
\>>> type(X\_trans)
<class 'torch.Tensor'>
\>>> X\_trans.device.type
'cuda'

Copy to clipboard

This pattern works identically with any supported array library. For example, replace `torch.asarray(..., device="cuda")` with `cupy.asarray(...)` for CuPy or `dpnp.asarray(...)` for dpnp. You can also target different devices within PyTorch by changing the `device=` argument (e.g., `"cpu"`, `"xpu"`, `"mps"`).

After the model is trained, fitted attributes that are arrays will also be from the same Array API namespace as the training data. For example, if PyTorch’s CUDA namespace was used for training, then fitted attributes will be on the GPU. Passing data in a different namespace or in a different device within the same namespace to `transform` or `predict` is an error:

\>>> with config\_context(array\_api\_dispatch\=True):
...     lda.transform(X\_np)
Traceback (most recent call last):
    ...
ValueError: Inputs passed to LinearDiscriminantAnalysis.transform() must use the same namespace and the same device as those passed to fit()...

Copy to clipboard

### 13.2.3.1. Moving estimators between devices[#](https://scikit-learn.org/stable/modules/array_api.html#moving-estimators-between-devices "Link to this heading")

We provide `move_estimator_to` to transfer an estimator’s array attributes to a different namespace and device:

\>>> from sklearn.utils.\_array\_api import move\_estimator\_to
\>>> import numpy as np
\>>> lda\_np \= move\_estimator\_to(lda, np, device\="cpu")
\>>> with config\_context(array\_api\_dispatch\=True):
...     X\_trans \= lda\_np.transform(X\_np)
\>>> type(X\_trans)
<class 'numpy.ndarray'>

Copy to clipboard

13.2.4. Support for array API compatible inputs[#](https://scikit-learn.org/stable/modules/array_api.html#support-for-array-api-compatible-inputs "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Estimators and other tools in scikit-learn that support array API compatible inputs.

### 13.2.4.1. Estimators[#](https://scikit-learn.org/stable/modules/array_api.html#estimators "Link to this heading")

*   [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     (with `svd_solver="full"`, `svd_solver="covariance_eigh"`, or `svd_solver="randomized"` (`svd_solver="randomized"` only if `power_iteration_normalizer="QR"`))
    
*   [`kernel_approximation.Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
    
*   [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     (with `solver="lbfgs"`)
    
*   [`linear_model.PoissonRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PoissonRegressor.html#sklearn.linear_model.PoissonRegressor "sklearn.linear_model.PoissonRegressor")
     (with `solver="lbfgs"`)
    
*   [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
     (with `solver="svd"`)
    
*   [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     (see [Note on device support for float64](https://scikit-learn.org/stable/modules/array_api.html#device-support-for-float64)
    )
    
*   [`linear_model.RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")
     (with `solver="svd"`)
    
*   [`linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")
     (see [Note on device support for float64](https://scikit-learn.org/stable/modules/array_api.html#device-support-for-float64)
    )
    
*   [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     (with `solver="svd"`)
    
*   [`naive_bayes.GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
    
*   [`preprocessing.Binarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Binarizer.html#sklearn.preprocessing.Binarizer "sklearn.preprocessing.Binarizer")
    
*   [`preprocessing.KernelCenterer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KernelCenterer.html#sklearn.preprocessing.KernelCenterer "sklearn.preprocessing.KernelCenterer")
    
*   [`preprocessing.LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")
     (with `sparse_output=False`)
    
*   [`preprocessing.LabelEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder "sklearn.preprocessing.LabelEncoder")
    
*   [`preprocessing.MaxAbsScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler "sklearn.preprocessing.MaxAbsScaler")
    
*   [`preprocessing.MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
    
*   [`preprocessing.Normalizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html#sklearn.preprocessing.Normalizer "sklearn.preprocessing.Normalizer")
    
*   [`preprocessing.PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
    
*   [`preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
     (see [Note on device support for float64](https://scikit-learn.org/stable/modules/array_api.html#device-support-for-float64)
    )
    
*   [`mixture.GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
     (with `init_params="random"` or `init_params="random_from_data"` and `warm_start=False`)
    

### 13.2.4.2. Meta-estimators[#](https://scikit-learn.org/stable/modules/array_api.html#meta-estimators "Link to this heading")

Meta-estimators that accept Array API inputs conditioned on the fact that the base estimator also does:

*   [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
     (with `method="temperature"`)
    
*   [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
    
*   [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
    
*   [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
    
*   [`model_selection.HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
    
*   [`model_selection.HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
    

### 13.2.4.3. Metrics[#](https://scikit-learn.org/stable/modules/array_api.html#metrics "Link to this heading")

*   [`sklearn.metrics.accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
    
*   [`sklearn.metrics.average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")
    
*   [`sklearn.metrics.balanced_accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html#sklearn.metrics.balanced_accuracy_score "sklearn.metrics.balanced_accuracy_score")
    
*   [`sklearn.metrics.brier_score_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")
    
*   [`sklearn.metrics.calinski_harabasz_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.calinski_harabasz_score.html#sklearn.metrics.calinski_harabasz_score "sklearn.metrics.calinski_harabasz_score")
    
*   [`sklearn.metrics.cohen_kappa_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html#sklearn.metrics.cohen_kappa_score "sklearn.metrics.cohen_kappa_score")
    
*   [`sklearn.metrics.confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")
    
*   [`sklearn.metrics.d2_absolute_error_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_absolute_error_score.html#sklearn.metrics.d2_absolute_error_score "sklearn.metrics.d2_absolute_error_score")
    
*   [`sklearn.metrics.d2_brier_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_brier_score.html#sklearn.metrics.d2_brier_score "sklearn.metrics.d2_brier_score")
    
*   [`sklearn.metrics.d2_log_loss_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_log_loss_score.html#sklearn.metrics.d2_log_loss_score "sklearn.metrics.d2_log_loss_score")
    
*   [`sklearn.metrics.d2_pinball_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_pinball_score.html#sklearn.metrics.d2_pinball_score "sklearn.metrics.d2_pinball_score")
    
*   [`sklearn.metrics.d2_tweedie_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_tweedie_score.html#sklearn.metrics.d2_tweedie_score "sklearn.metrics.d2_tweedie_score")
    
*   [`sklearn.metrics.det_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#sklearn.metrics.det_curve "sklearn.metrics.det_curve")
    
*   [`sklearn.metrics.explained_variance_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html#sklearn.metrics.explained_variance_score "sklearn.metrics.explained_variance_score")
    
*   [`sklearn.metrics.f1_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score")
    
*   [`sklearn.metrics.fbeta_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fbeta_score.html#sklearn.metrics.fbeta_score "sklearn.metrics.fbeta_score")
    
*   [`sklearn.metrics.hamming_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html#sklearn.metrics.hamming_loss "sklearn.metrics.hamming_loss")
    
*   [`sklearn.metrics.jaccard_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#sklearn.metrics.jaccard_score "sklearn.metrics.jaccard_score")
    
*   [`sklearn.metrics.log_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
    
*   [`sklearn.metrics.max_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.max_error.html#sklearn.metrics.max_error "sklearn.metrics.max_error")
    
*   [`sklearn.metrics.mean_absolute_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error "sklearn.metrics.mean_absolute_error")
    
*   [`sklearn.metrics.mean_absolute_percentage_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_percentage_error.html#sklearn.metrics.mean_absolute_percentage_error "sklearn.metrics.mean_absolute_percentage_error")
    
*   [`sklearn.metrics.mean_gamma_deviance`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_gamma_deviance.html#sklearn.metrics.mean_gamma_deviance "sklearn.metrics.mean_gamma_deviance")
    
*   [`sklearn.metrics.mean_pinball_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#sklearn.metrics.mean_pinball_loss "sklearn.metrics.mean_pinball_loss")
    
*   [`sklearn.metrics.mean_poisson_deviance`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_poisson_deviance.html#sklearn.metrics.mean_poisson_deviance "sklearn.metrics.mean_poisson_deviance")
    
*   [`sklearn.metrics.mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
    
*   [`sklearn.metrics.mean_squared_log_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_log_error.html#sklearn.metrics.mean_squared_log_error "sklearn.metrics.mean_squared_log_error")
    
*   [`sklearn.metrics.mean_tweedie_deviance`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_tweedie_deviance.html#sklearn.metrics.mean_tweedie_deviance "sklearn.metrics.mean_tweedie_deviance")
    
*   [`sklearn.metrics.median_absolute_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "sklearn.metrics.median_absolute_error")
    
*   [`sklearn.metrics.multilabel_confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.multilabel_confusion_matrix.html#sklearn.metrics.multilabel_confusion_matrix "sklearn.metrics.multilabel_confusion_matrix")
    
*   [`sklearn.metrics.pairwise.additive_chi2_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.additive_chi2_kernel.html#sklearn.metrics.pairwise.additive_chi2_kernel "sklearn.metrics.pairwise.additive_chi2_kernel")
    
*   [`sklearn.metrics.pairwise.chi2_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.chi2_kernel.html#sklearn.metrics.pairwise.chi2_kernel "sklearn.metrics.pairwise.chi2_kernel")
    
*   [`sklearn.metrics.pairwise.cosine_similarity`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html#sklearn.metrics.pairwise.cosine_similarity "sklearn.metrics.pairwise.cosine_similarity")
    
*   [`sklearn.metrics.pairwise.cosine_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_distances.html#sklearn.metrics.pairwise.cosine_distances "sklearn.metrics.pairwise.cosine_distances")
    
*   [`sklearn.metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
     (only supports “cosine”, “euclidean”, “manhattan” and “l2” metrics)
    
*   [`sklearn.metrics.pairwise_distances_argmin`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin.html#sklearn.metrics.pairwise_distances_argmin "sklearn.metrics.pairwise_distances_argmin")
    
*   [`sklearn.metrics.pairwise.euclidean_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html#sklearn.metrics.pairwise.euclidean_distances "sklearn.metrics.pairwise.euclidean_distances")
     (see [Note on device support for float64](https://scikit-learn.org/stable/modules/array_api.html#device-support-for-float64)
    )
    
*   [`sklearn.metrics.pairwise.laplacian_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.laplacian_kernel.html#sklearn.metrics.pairwise.laplacian_kernel "sklearn.metrics.pairwise.laplacian_kernel")
    
*   [`sklearn.metrics.pairwise.linear_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.linear_kernel.html#sklearn.metrics.pairwise.linear_kernel "sklearn.metrics.pairwise.linear_kernel")
    
*   [`sklearn.metrics.pairwise.manhattan_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.manhattan_distances.html#sklearn.metrics.pairwise.manhattan_distances "sklearn.metrics.pairwise.manhattan_distances")
    
*   [`sklearn.metrics.pairwise.paired_cosine_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_cosine_distances.html#sklearn.metrics.pairwise.paired_cosine_distances "sklearn.metrics.pairwise.paired_cosine_distances")
    
*   [`sklearn.metrics.pairwise.paired_euclidean_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_euclidean_distances.html#sklearn.metrics.pairwise.paired_euclidean_distances "sklearn.metrics.pairwise.paired_euclidean_distances")
    
*   [`sklearn.metrics.pairwise.paired_manhattan_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_manhattan_distances.html#sklearn.metrics.pairwise.paired_manhattan_distances "sklearn.metrics.pairwise.paired_manhattan_distances")
    
*   [`sklearn.metrics.pairwise.pairwise_kernels`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html#sklearn.metrics.pairwise.pairwise_kernels "sklearn.metrics.pairwise.pairwise_kernels")
    
*   [`sklearn.metrics.pairwise.polynomial_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.polynomial_kernel.html#sklearn.metrics.pairwise.polynomial_kernel "sklearn.metrics.pairwise.polynomial_kernel")
    
*   [`sklearn.metrics.pairwise.rbf_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.rbf_kernel.html#sklearn.metrics.pairwise.rbf_kernel "sklearn.metrics.pairwise.rbf_kernel")
     (see [Note on device support for float64](https://scikit-learn.org/stable/modules/array_api.html#device-support-for-float64)
    )
    
*   [`sklearn.metrics.pairwise.sigmoid_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.sigmoid_kernel.html#sklearn.metrics.pairwise.sigmoid_kernel "sklearn.metrics.pairwise.sigmoid_kernel")
    
*   [`sklearn.metrics.precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "sklearn.metrics.precision_score")
    
*   [`sklearn.metrics.precision_recall_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")
    
*   [`sklearn.metrics.precision_recall_fscore_support`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support "sklearn.metrics.precision_recall_fscore_support")
    
*   [`sklearn.metrics.r2_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
    
*   [`sklearn.metrics.recall_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score")
    
*   [`sklearn.metrics.roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")
    
*   [`sklearn.metrics.root_mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html#sklearn.metrics.root_mean_squared_error "sklearn.metrics.root_mean_squared_error")
    
*   [`sklearn.metrics.root_mean_squared_log_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_log_error.html#sklearn.metrics.root_mean_squared_log_error "sklearn.metrics.root_mean_squared_log_error")
    
*   [`sklearn.metrics.zero_one_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.zero_one_loss.html#sklearn.metrics.zero_one_loss "sklearn.metrics.zero_one_loss")
    

### 13.2.4.4. Tools[#](https://scikit-learn.org/stable/modules/array_api.html#tools "Link to this heading")

*   [`preprocessing.label_binarize`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.label_binarize.html#sklearn.preprocessing.label_binarize "sklearn.preprocessing.label_binarize")
     (with `sparse_output=False`)
    
*   [`model_selection.cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
    
*   [`model_selection.train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
    
*   [`utils.check_consistent_length`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_consistent_length.html#sklearn.utils.check_consistent_length "sklearn.utils.check_consistent_length")
    

13.2.5. Input and output array type handling[#](https://scikit-learn.org/stable/modules/array_api.html#input-and-output-array-type-handling "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Estimators and scoring functions are able to accept input arrays from different array libraries and/or devices. When a mixed set of input arrays is passed, scikit-learn converts arrays as needed to make them all consistent.

For estimators, the rule is **“everything follows** `X` **“** - mixed array inputs are converted so that they all match the array library and device of `X`. For scoring functions the rule is **“everything follows** `y_pred` **“** - mixed array inputs are converted so that they all match the array library and device of `y_pred`.

When a function or method has been called with array API compatible inputs, the convention is to return arrays from the same array library and on the same device as the input data.

### 13.2.5.1. Estimators[#](https://scikit-learn.org/stable/modules/array_api.html#id1 "Link to this heading")

When an estimator is fitted with an array API compatible `X`, all other array inputs, including constructor arguments, (e.g., `y`, `sample_weight`) will be converted to match the array library and device of `X`, if they do not already. This behaviour enables switching from processing on the CPU to processing on the GPU at any point within a pipeline.

This allows estimators to accept mixed input types, enabling `X` to be moved to a different device within a pipeline, without explicitly moving `y`. Note that scikit-learn pipelines do not allow transformation of `y` (to avoid [leakage](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage)
).

Take for example a pipeline where `X` and `y` both start on CPU, and go through the following three steps:

*   [`TargetEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")
    , which will transform categorial `X` but also requires `y`, meaning both `X` and `y` need to be on CPU.
    
*   [`FunctionTransformer(func=partial(torch.asarray, device="cuda"))`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
    , which moves `X` to GPU, to improve performance in the next step.
    
*   [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
    , whose performance can be improved when passed arrays on a GPU, as they can handle large matrix operations very efficiently.
    

`X` initially contains categorical string data (thus needs to be on CPU), which is target encoded to numerical values in [`TargetEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")
. `X` is then explicitly moved to GPU to improve the performance of [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
. `y` cannot be transformed by the pipeline (recall scikit-learn pipelines do not allow transformation of `y`) but as [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
 is able to accept mixed input types, this is not a problem and the pipeline is able to be run.

The fitted attributes of an estimator fitted with an array API compatible `X`, will be arrays from the same library as the input and stored on the same device. The `predict` and `transform` method subsequently expect inputs from the same array library and device as the data passed to the `fit` method.

### 13.2.5.2. Scoring functions[#](https://scikit-learn.org/stable/modules/array_api.html#scoring-functions "Link to this heading")

When an array API compatible `y_pred` is passed to a scoring function, all other array inputs (e.g., `y_true`, `sample_weight`) will be converted to match the array library and device of `y_pred`, if they do not already. This allows scoring functions to accept mixed input types, enabling them to be used within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 (or function that accepts estimators), with a pipeline that moves input arrays between devices (e.g., CPU to GPU).

For example, to be able to use the pipeline described above within e.g., [`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
 or [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
, the scoring function internally called needs to be able to accept mixed input types.

The output type of scoring functions depends on the number of output values. When a scoring function returns a scalar value, it will return a Python scalar (typically a `float` instance) instead of an array scalar value. For scoring functions that support [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 or [multioutput](https://scikit-learn.org/stable/glossary.html#term-multioutput)
, an array from the same array library and device as `y_pred` will be returned when multiple values need to be output.

13.2.6. Common estimator checks (for developers)[#](https://scikit-learn.org/stable/modules/array_api.html#common-estimator-checks-for-developers "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Add the `array_api_support` tag to an estimator’s set of tags to indicate that it supports the array API. This will enable dedicated checks as part of the common tests to verify that the estimators’ results are the same when using vanilla NumPy and array API inputs.

To run these checks you need to install [array-api-strict](https://data-apis.org/array-api-strict/)
 in your test environment. This allows you to run checks without having a GPU. To run checks on real GPU devices you also need to install [PyTorch](https://pytorch.org/)
, [CuPy](https://cupy.dev/)
, and/or [dpnp](https://intelpython.github.io/dpnp/)
, and have compatible GPU hardware. Full GPU coverage is expected to be split across machines because CUDA, MPS, and Intel GPU backends require different hardware. Checks that can not be executed or have missing dependencies will be automatically skipped. Therefore it’s important to run the tests with the `-v` flag to see which checks are skipped:

pip install array-api-strict  \# and other libraries as needed
pytest \-k "array\_api" \-v

Copy to clipboard

Running the scikit-learn tests against `array-api-strict` should help reveal most code problems related to handling multiple device inputs via the use of simulated non-CPU devices. This allows for fast iterative development and debugging of array API related code.

However, to ensure full handling of PyTorch, CuPy, or dpnp inputs allocated on actual GPU devices, it is necessary to run the tests against those libraries and hardware. This can either be achieved by using [Google Colab](https://gist.github.com/EdAbati/ff3bdc06bafeb92452b3740686cc8d7c)
 for CUDA or leveraging our CI infrastructure on pull requests. CUDA and Intel GPU tests are manually triggered by maintainers. Intel GPU testing for PyTorch XPU and dpnp is run on a dedicated self-hosted runner: [probabl-ai/scikit-learn-intel-workflow](https://github.com/probabl-ai/scikit-learn-intel-workflow)
.

13.2.7. Notes[#](https://scikit-learn.org/stable/modules/array_api.html#notes "Link to this heading")

------------------------------------------------------------------------------------------------------

### 13.2.7.1. Note on MPS device support[#](https://scikit-learn.org/stable/modules/array_api.html#note-on-mps-device-support "Link to this heading")

On macOS, PyTorch can use the Metal Performance Shaders (MPS) to access hardware accelerators (e.g. the internal GPU component of the M1 or M2 chips). However, the MPS device support for PyTorch is incomplete at the time of writing. See the following github issue for more details:

*   [pytorch/pytorch#77764](https://github.com/pytorch/pytorch/issues/77764)
    

To enable the MPS support in PyTorch, set the environment variable `PYTORCH_ENABLE_MPS_FALLBACK=1` before running the tests:

PYTORCH\_ENABLE\_MPS\_FALLBACK\=1 pytest \-k "array\_api" \-v

Copy to clipboard

At the time of writing all scikit-learn tests should pass, however, the computational speed is not necessarily better than with the CPU device.

### 13.2.7.2. Note on device support for `float64`[#](https://scikit-learn.org/stable/modules/array_api.html#note-on-device-support-for-float64 "Link to this heading")

Certain operations within scikit-learn will automatically perform operations on floating-point values with `float64` precision to prevent overflows and ensure correctness (e.g., [`metrics.pairwise.euclidean_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html#sklearn.metrics.pairwise.euclidean_distances "sklearn.metrics.pairwise.euclidean_distances")
, [`preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
). However, certain combinations of array namespaces and devices, such as PyTorch on MPS (see [Note on MPS device support](https://scikit-learn.org/stable/modules/array_api.html#mps-support)
) and some Intel GPU devices with PyTorch XPU or dpnp, do not support the `float64` data type. In these cases, scikit-learn will revert to using the `float32` data type instead. This can result in different behavior (typically numerically unstable results) compared to not using array API dispatching or using a device with `float64` support.

### 13.2.7.3. Note on Intel GPU support[#](https://scikit-learn.org/stable/modules/array_api.html#note-on-intel-gpu-support "Link to this heading")

PyTorch XPU support is only available in PyTorch >= 2.12. For detailed compatibility information and setup instructions, see the [PyTorch XPU documentation](https://docs.pytorch.org/docs/2.12/notes/get_start_xpu.html)
.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)