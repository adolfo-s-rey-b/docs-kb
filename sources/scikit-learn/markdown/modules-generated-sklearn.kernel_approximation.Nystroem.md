[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.kernel_approximation.Nystroem.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.kernel_approximation.Nystroem.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.kernel_approximation.Nystroem.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.kernel_approximation.Nystroem.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.kernel_approximation.Nystroem.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.kernel_approximation.Nystroem.html)

Collapse Sidebar Expand Sidebar

Nystroem[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#nystroem "Link to this heading")

==========================================================================================================================================

class sklearn.kernel\_approximation.Nystroem(_kernel\='rbf'_, _\*_, _gamma\=None_, _coef0\=None_, _degree\=None_, _kernel\_params\=None_, _n\_components\=100_, _random\_state\=None_, _n\_jobs\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/kernel_approximation.py#L859)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "Link to this definition")

Approximate a kernel map using a subset of the training data.

Constructs an approximate feature map for an arbitrary kernel using a subset of the data as basis.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/kernel_approximation.html#nystroem-kernel-approx)
.

Added in version 0.13.

Parameters:

**kernel**str or callable, default=’rbf’

Kernel map to be approximated. A callable should accept two arguments and the keyword arguments passed to this object as `kernel_params`, and should return a floating point number.

**gamma**float, default=None

Gamma parameter for the RBF, laplacian, polynomial, exponential chi2 and sigmoid kernels. Interpretation of the default value is left to the kernel; see the documentation for sklearn.metrics.pairwise. Ignored by other kernels.

**coef0**float, default=None

Zero coefficient for polynomial and sigmoid kernels. Ignored by other kernels.

**degree**float, default=None

Degree of the polynomial kernel. Ignored by other kernels.

**kernel\_params**dict, default=None

Additional parameters (keyword arguments) for kernel function passed as callable object.

**n\_components**int, default=100

Number of features to construct. How many data points will be used to construct the mapping.

**random\_state**int, RandomState instance or None, default=None

Pseudo-random number generator to control the uniform sampling without replacement of `n_components` of the training data to construct the basis kernel. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**n\_jobs**int, default=None

The number of jobs to use for the computation. This works by breaking down the kernel matrix into `n_jobs` even slices and computing them in parallel.

`None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Added in version 0.24.

Attributes:

**components\_**ndarray of shape (n\_components, n\_features)

Subset of training points used to construct the feature map.

**component\_indices\_**ndarray of shape (n\_components)

Indices of `components_` in the training set.

**normalization\_**ndarray of shape (n\_components, n\_components)

Normalization matrix needed for embedding. Square root of the kernel matrix on `components_`.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`AdditiveChi2Sampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.AdditiveChi2Sampler.html#sklearn.kernel_approximation.AdditiveChi2Sampler "sklearn.kernel_approximation.AdditiveChi2Sampler")

Approximate feature map for additive chi2 kernel.

[`PolynomialCountSketch`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#sklearn.kernel_approximation.PolynomialCountSketch "sklearn.kernel_approximation.PolynomialCountSketch")

Polynomial kernel approximation via Tensor Sketch.

[`RBFSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler "sklearn.kernel_approximation.RBFSampler")

Approximate an RBF kernel feature map using random Fourier features.

[`SkewedChi2Sampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.SkewedChi2Sampler.html#sklearn.kernel_approximation.SkewedChi2Sampler "sklearn.kernel_approximation.SkewedChi2Sampler")

Approximate feature map for “skewed chi-squared” kernel.

[`sklearn.metrics.pairwise.kernel_metrics`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.kernel_metrics.html#sklearn.metrics.pairwise.kernel_metrics "sklearn.metrics.pairwise.kernel_metrics")

List of built-in kernels.

References

*   Williams, C.K.I. and Seeger, M. “Using the Nystroem method to speed up kernel machines”, Advances in neural information processing systems 2001
    
*   T. Yang, Y. Li, M. Mahdavi, R. Jin and Z. Zhou “Nystroem Method vs Random Fourier Features: A Theoretical and Empirical Comparison”, Advances in Neural Information Processing Systems 2012
    

Examples

\>>> from sklearn import datasets, svm
\>>> from sklearn.kernel\_approximation import Nystroem
\>>> X, y \= datasets.load\_digits(n\_class\=9, return\_X\_y\=True)
\>>> data \= X / 16.
\>>> clf \= svm.LinearSVC()
\>>> feature\_map\_nystroem \= Nystroem(gamma\=.2,
...                                 random\_state\=1,
...                                 n\_components\=300)
\>>> data\_transformed \= feature\_map\_nystroem.fit\_transform(data)
\>>> clf.fit(data\_transformed, y)
LinearSVC()
\>>> clf.score(data\_transformed, y)
0.9987...

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/kernel_approximation.py#L1010)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem.fit "Link to this definition")

Fit estimator to data.

Samples a subset of training points, computes kernel on these and computes normalization matrix.

Parameters:

**X**array-like, shape (n\_samples, n\_features)

Training data, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like, shape (n\_samples,) or (n\_samples, n\_outputs), default=None

Target values (None for unsupervised transformations).

Returns:

**self**object

Returns the instance itself.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem.fit_transform "Link to this definition")

Fit to data, then transform it.

Fits transformer to `X` and `y` with optional parameters `fit_params` and returns a transformed version of `X`.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Input samples.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs), default=None

Target values (None for unsupervised transformations).

**\*\*fit\_params**dict

Additional fit parameters. Pass only if the estimator accepts additional params in its `fit` method.

Returns:

**X\_new**ndarray array of shape (n\_samples, n\_features\_new)

Transformed array.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1046)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem.set_output "Link to this definition")

Set output container.

Refer to the [user guide](https://scikit-learn.org/stable/modules/df_output_transform.html#df-output-transform)
 for more details and [Introducing the set\_output API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html#sphx-glr-auto-examples-miscellaneous-plot-set-output-py)
 for an example on how to use the API.

Parameters:

**transform**{“default”, “pandas”, “polars”}, default=None

Configure output of `transform` and `fit_transform`.

*   `"default"`: Default output format of a transformer
    
*   `"pandas"`: DataFrame output
    
*   `"polars"`: Polars output
    
*   `None`: Transform configuration is unchanged
    

Added in version 1.4: `"polars"` option was added.

Returns:

**self**estimator instance

Estimator instance.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/kernel_approximation.py#L1076)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem.transform "Link to this definition")

Apply feature map to X.

Computes an approximate feature map using the kernel between some training points and X.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Data to transform.

Returns:

**X\_transformed**ndarray of shape (n\_samples, n\_components)

Transformed data.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_thumb.png)

[Time-related feature engineering](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html)

Time-related feature engineering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_recognition_thumb.png)

[Faces recognition example using eigenfaces and kernel approximation](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html)

Faces recognition example using eigenfaces and kernel approximation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_probability_thumb.png)

[Plot classification probability](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html)

Plot classification probability

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_voting_decision_regions_thumb.png)

[Visualizing the probabilistic predictions of a VotingClassifier](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_decision_regions.html)

Visualizing the probabilistic predictions of a VotingClassifier

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iterative_imputer_variants_comparison_thumb.png)

[Imputing missing values with variants of IterativeImputer](https://scikit-learn.org/stable/auto_examples/impute/plot_iterative_imputer_variants_comparison.html)

Imputing missing values with variants of IterativeImputer

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgdocsvm_vs_ocsvm_thumb.png)

[One-Class SVM versus One-Class SVM using Stochastic Gradient Descent](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgdocsvm_vs_ocsvm.html)

One-Class SVM versus One-Class SVM using Stochastic Gradient Descent

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_anomaly_comparison_thumb.png)

[Comparing anomaly detection algorithms for outlier detection on toy datasets](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html)

Comparing anomaly detection algorithms for outlier detection on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_approximation_thumb.png)

[Explicit feature map approximation for RBF kernels](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_approximation.html)

Explicit feature map approximation for RBF kernels

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)