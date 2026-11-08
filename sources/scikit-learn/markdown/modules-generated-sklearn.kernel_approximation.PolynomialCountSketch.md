[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html)

Collapse Sidebar Expand Sidebar

PolynomialCountSketch[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#polynomialcountsketch "Link to this heading")

=================================================================================================================================================================================

class sklearn.kernel\_approximation.PolynomialCountSketch(_\*_, _gamma\=1.0_, _degree\=2_, _coef0\=0.0_, _n\_components\=100_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/kernel_approximation.py#L40)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#sklearn.kernel_approximation.PolynomialCountSketch "Link to this definition")

Polynomial kernel approximation via Tensor Sketch.

Implements Tensor Sketch, which approximates the feature map of the polynomial kernel:

K(X, Y) \= (gamma \* <X, Y\> + coef0)^degree

Copy to clipboard

by efficiently computing a Count Sketch of the outer product of a vector with itself using Fast Fourier Transforms (FFT). Read more in the [User Guide](https://scikit-learn.org/stable/modules/kernel_approximation.html#polynomial-kernel-approx)
.

Added in version 0.24.

Parameters:

**gamma**float, default=1.0

Parameter of the polynomial kernel whose feature map will be approximated.

**degree**int, default=2

Degree of the polynomial kernel whose feature map will be approximated.

**coef0**float, default=0.0

Constant term of the polynomial kernel whose feature map will be approximated.

**n\_components**int, default=100

Dimensionality of the output feature space. Usually, `n_components` should be greater than the number of features in input samples in order to achieve good performance. The optimal score / run time balance is typically achieved around `n_components` = 10 \* `n_features`, but this depends on the specific dataset being used.

**random\_state**int, RandomState instance, default=None

Determines random number generation for indexHash and bitHash initialization. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Attributes:

**indexHash\_**ndarray of shape (degree, n\_features), dtype=int64

Array of indexes in range \[0, n\_components) used to represent the 2-wise independent hash functions for Count Sketch computation.\
\
**bitHash\_**ndarray of shape (degree, n\_features), dtype=float32\
\
Array with random entries in {+1, -1}, used to represent the 2-wise independent hash functions for Count Sketch computation.\
\
**n\_features\_in\_**int\
\
Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)\
.\
\
Added in version 0.24.\
\
**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)\
\
Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)\
. Defined only when `X` has feature names that are all strings.\
\
Added in version 1.0.\
\
See also\
\
[`AdditiveChi2Sampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.AdditiveChi2Sampler.html#sklearn.kernel_approximation.AdditiveChi2Sampler "sklearn.kernel_approximation.AdditiveChi2Sampler")\
\
Approximate feature map for additive chi2 kernel.\
\
[`Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")\
\
Approximate a kernel map using a subset of the training data.\
\
[`RBFSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler "sklearn.kernel_approximation.RBFSampler")\
\
Approximate an RBF kernel feature map using random Fourier features.\
\
[`SkewedChi2Sampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.SkewedChi2Sampler.html#sklearn.kernel_approximation.SkewedChi2Sampler "sklearn.kernel_approximation.SkewedChi2Sampler")\
\
Approximate feature map for “skewed chi-squared” kernel.\
\
[`sklearn.metrics.pairwise.kernel_metrics`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.kernel_metrics.html#sklearn.metrics.pairwise.kernel_metrics "sklearn.metrics.pairwise.kernel_metrics")\
\
List of built-in kernels.\
\
Examples\
\
\>>> from sklearn.kernel\_approximation import PolynomialCountSketch\
\>>> from sklearn.linear\_model import SGDClassifier\
\>>> X \= \[\[0, 0\], \[1, 1\], \[1, 0\], \[0, 1\]\]\
\>>> y \= \[0, 0, 1, 1\]\
\>>> ps \= PolynomialCountSketch(degree\=3, random\_state\=1)\
\>>> X\_features \= ps.fit\_transform(X)\
\>>> clf \= SGDClassifier(max\_iter\=10, tol\=1e-3)\
\>>> clf.fit(X\_features, y)\
SGDClassifier(max\_iter=10)\
\>>> clf.score(X\_features, y)\
1.0\
\
Copy to clipboard\
\
For a more detailed example of usage, see [Scalable learning with polynomial kernel approximation](https://scikit-learn.org/stable/auto_examples/kernel_approximation/plot_scalable_poly_kernels.html#sphx-glr-auto-examples-kernel-approximation-plot-scalable-poly-kernels-py)\
\
fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/kernel_approximation.py#L147)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#sklearn.kernel_approximation.PolynomialCountSketch.fit "Link to this definition")\
\
Fit the model with X.\
\
Initializes the internal variables. The method needs no information about the distribution of data, so we only care about n\_features in X.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
Training data, where `n_samples` is the number of samples and `n_features` is the number of features.\
\
**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs), default=None\
\
Target values (None for unsupervised transformations).\
\
Returns:\
\
**self**object\
\
Returns the instance itself.\
\
fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#sklearn.kernel_approximation.PolynomialCountSketch.fit_transform "Link to this definition")\
\
Fit to data, then transform it.\
\
Fits transformer to `X` and `y` with optional parameters `fit_params` and returns a transformed version of `X`.\
\
Parameters:\
\
**X**array-like of shape (n\_samples, n\_features)\
\
Input samples.\
\
**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs), default=None\
\
Target values (None for unsupervised transformations).\
\
**\*\*fit\_params**dict\
\
Additional fit parameters. Pass only if the estimator accepts additional params in its `fit` method.\
\
Returns:\
\
**X\_new**ndarray array of shape (n\_samples, n\_features\_new)\
\
Transformed array.\
\
get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1046)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#sklearn.kernel_approximation.PolynomialCountSketch.get_feature_names_out "Link to this definition")\
\
Get output feature names for transformation.\
\
The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.\
\
Parameters:\
\
**input\_features**array-like of str or None, default=None\
\
Only used to validate feature names with the names seen in `fit`.\
\
Returns:\
\
**feature\_names\_out**ndarray of str objects\
\
Transformed feature names.\
\
get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#sklearn.kernel_approximation.PolynomialCountSketch.get_metadata_routing "Link to this definition")\
\
Get metadata routing of this object.\
\
Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)\
 on how the routing mechanism works.\
\
Returns:\
\
**routing**MetadataRequest\
\
A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")\
 encapsulating routing information.\
\
get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#sklearn.kernel_approximation.PolynomialCountSketch.get_params "Link to this definition")\
\
Get parameters for this estimator.\
\
Parameters:\
\
**deep**bool, default=True\
\
If True, will return the parameters for this estimator and contained subobjects that are estimators.\
\
Returns:\
\
**params**dict\
\
Parameter names mapped to their values.\
\
set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#sklearn.kernel_approximation.PolynomialCountSketch.set_output "Link to this definition")\
\
Set output container.\
\
Refer to the [user guide](https://scikit-learn.org/stable/modules/df_output_transform.html#df-output-transform)\
 for more details and [Introducing the set\_output API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html#sphx-glr-auto-examples-miscellaneous-plot-set-output-py)\
 for an example on how to use the API.\
\
Parameters:\
\
**transform**{“default”, “pandas”, “polars”}, default=None\
\
Configure output of `transform` and `fit_transform`.\
\
*   `"default"`: Default output format of a transformer\
    \
*   `"pandas"`: DataFrame output\
    \
*   `"polars"`: Polars output\
    \
*   `None`: Transform configuration is unchanged\
    \
\
Added in version 1.4: `"polars"` option was added.\
\
Returns:\
\
**self**estimator instance\
\
Estimator instance.\
\
set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#sklearn.kernel_approximation.PolynomialCountSketch.set_params "Link to this definition")\
\
Set the parameters of this estimator.\
\
The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.\
\
Parameters:\
\
**\*\*params**dict\
\
Estimator parameters.\
\
Returns:\
\
**self**estimator instance\
\
Estimator instance.\
\
transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/kernel_approximation.py#L184)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#sklearn.kernel_approximation.PolynomialCountSketch.transform "Link to this definition")\
\
Generate the feature map approximation for X.\
\
Parameters:\
\
**X**{array-like}, shape (n\_samples, n\_features)\
\
New data, where `n_samples` is the number of samples and `n_features` is the number of features.\
\
Returns:\
\
**X\_new**array-like, shape (n\_samples, n\_components)\
\
Returns the instance itself.\
\
Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#gallery-examples "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scalable_poly_kernels_thumb.png)\
\
[Scalable learning with polynomial kernel approximation](https://scikit-learn.org/stable/auto_examples/kernel_approximation/plot_scalable_poly_kernels.html)\
\
Scalable learning with polynomial kernel approximation\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_thumb.png)\
\
[Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)\
\
Release Highlights for scikit-learn 0.24\
\
On this page\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)