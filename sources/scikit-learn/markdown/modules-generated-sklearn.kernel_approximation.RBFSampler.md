[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.kernel_approximation.RBFSampler.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.kernel_approximation.RBFSampler.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.kernel_approximation.RBFSampler.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.kernel_approximation.RBFSampler.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.kernel_approximation.RBFSampler.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.kernel_approximation.RBFSampler.html)

Collapse Sidebar Expand Sidebar

RBFSampler[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#rbfsampler "Link to this heading")

================================================================================================================================================

class sklearn.kernel\_approximation.RBFSampler(_\*_, _gamma\=1.0_, _n\_components\=100_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/kernel_approximation.py#L253)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler "Link to this definition")

Approximate an RBF kernel feature map using random Fourier features.

It implements a variant of Random Kitchen Sinks.\[1\]

Read more in the [User Guide](https://scikit-learn.org/stable/modules/kernel_approximation.html#rbf-kernel-approx)
.

Parameters:

**gamma**‘scale’ or float, default=1.0

Parameter of RBF kernel: exp(-gamma \* x^2). If `gamma='scale'` is passed then it uses 1 / (n\_features \* X.var()) as value of gamma.

Added in version 1.2: The option `"scale"` was added in 1.2.

**n\_components**int, default=100

Number of Monte Carlo samples per original feature. Equals the dimensionality of the computed feature space.

**random\_state**int, RandomState instance or None, default=None

Pseudo-random number generator to control the generation of the random weights and random offset when fitting the training data. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Attributes:

**random\_offset\_**ndarray of shape (n\_components,), dtype={np.float64, np.float32}

Random offset used to compute the projection in the `n_components` dimensions of the feature space.

**random\_weights\_**ndarray of shape (n\_features, n\_components), dtype={np.float64, np.float32}

Random projection directions drawn from the Fourier transform of the RBF kernel.

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

[`Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")

Approximate a kernel map using a subset of the training data.

[`PolynomialCountSketch`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#sklearn.kernel_approximation.PolynomialCountSketch "sklearn.kernel_approximation.PolynomialCountSketch")

Polynomial kernel approximation via Tensor Sketch.

[`SkewedChi2Sampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.SkewedChi2Sampler.html#sklearn.kernel_approximation.SkewedChi2Sampler "sklearn.kernel_approximation.SkewedChi2Sampler")

Approximate feature map for “skewed chi-squared” kernel.

[`sklearn.metrics.pairwise.kernel_metrics`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.kernel_metrics.html#sklearn.metrics.pairwise.kernel_metrics "sklearn.metrics.pairwise.kernel_metrics")

List of built-in kernels.

Notes

See “Random Features for Large-Scale Kernel Machines” by A. Rahimi and Benjamin Recht.

\[1\] “Weighted Sums of Random Kitchen Sinks: Replacing minimization with randomization in learning” by A. Rahimi and Benjamin Recht. ([https://people.eecs.berkeley.edu/~brecht/papers/08.rah.rec.nips.pdf](https://people.eecs.berkeley.edu/~brecht/papers/08.rah.rec.nips.pdf)
)

Examples

\>>> from sklearn.kernel\_approximation import RBFSampler
\>>> from sklearn.linear\_model import SGDClassifier
\>>> X \= \[\[0, 0\], \[1, 1\], \[1, 0\], \[0, 1\]\]
\>>> y \= \[0, 0, 1, 1\]
\>>> rbf\_feature \= RBFSampler(gamma\=1, random\_state\=1)
\>>> X\_features \= rbf\_feature.fit\_transform(X)
\>>> clf \= SGDClassifier(max\_iter\=5, tol\=1e-3)
\>>> clf.fit(X\_features, y)
SGDClassifier(max\_iter=5)
\>>> clf.score(X\_features, y)
1.0

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/kernel_approximation.py#L350)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler.fit "Link to this definition")

Fit the model with X.

Samples random projection according to n\_features.

Parameters:

**X**{array-like, sparse matrix}, shape (n\_samples, n\_features)

Training data, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like, shape (n\_samples,) or (n\_samples, n\_outputs), default=None

Target values (None for unsupervised transformations).

Returns:

**self**object

Returns the instance itself.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler.fit_transform "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/kernel_approximation.py#L395)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler.transform "Link to this definition")

Apply the approximate feature map to X.

Parameters:

**X**{array-like, sparse matrix}, shape (n\_samples, n\_features)

New data, where `n_samples` is the number of samples and `n_features` is the number of features.

Returns:

**X\_new**array-like, shape (n\_samples, n\_components)

Returns the instance itself.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

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