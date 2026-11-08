[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html)

Collapse Sidebar Expand Sidebar

LatentDirichletAllocation[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#latentdirichletallocation "Link to this heading")

======================================================================================================================================================================================

class sklearn.decomposition.LatentDirichletAllocation(_n\_components\=10_, _\*_, _doc\_topic\_prior\=None_, _topic\_word\_prior\=None_, _learning\_method\='batch'_, _learning\_decay\=0.7_, _learning\_offset\=10.0_, _max\_iter\=10_, _batch\_size\=128_, _evaluate\_every\=\-1_, _total\_samples\=1000000.0_, _perp\_tol\=0.1_, _mean\_change\_tol\=0.001_, _max\_doc\_update\_iter\=100_, _n\_jobs\=None_, _verbose\=0_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_lda.py#L160)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation "Link to this definition")

Latent Dirichlet Allocation with online variational Bayes algorithm.

The implementation is based on [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#re25e5648fc37-1)
 and [\[2\]](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#re25e5648fc37-2)
.

Added in version 0.17.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/decomposition.html#latentdirichletallocation)
.

Parameters:

**n\_components**int, default=10

Number of topics.

Changed in version 0.19: `n_topics` was renamed to `n_components`

**doc\_topic\_prior**float, default=None

Prior of document topic distribution `theta`. If the value is None, defaults to `1 / n_components`. In [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#re25e5648fc37-1)
, this is called `alpha`.

**topic\_word\_prior**float, default=None

Prior of topic word distribution `beta`. If the value is None, defaults to `1 / n_components`. In [\[1\]](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#re25e5648fc37-1)
, this is called `eta`.

**learning\_method**{‘batch’, ‘online’}, default=’batch’

Method used to update `_component`. Only used in [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation.fit "sklearn.decomposition.LatentDirichletAllocation.fit")
 method. In general, if the data size is large, the online update will be much faster than the batch update.

Valid options:

*   ‘batch’: Batch variational Bayes method. Use all training data in each EM update. Old `components_` will be overwritten in each iteration.
    
*   ‘online’: Online variational Bayes method. In each EM update, use mini-batch of training data to update the `components_` variable incrementally. The learning rate is controlled by the `learning_decay` and the `learning_offset` parameters.
    

Changed in version 0.20: The default learning method is now `"batch"`.

**learning\_decay**float, default=0.7

It is a parameter that control learning rate in the online learning method. The value should be set between (0.5, 1.0\] to guarantee asymptotic convergence. When the value is 0.0 and batch\_size is `n_samples`, the update method is same as batch learning. In the literature, this is called kappa.

**learning\_offset**float, default=10.0

A (positive) parameter that downweights early iterations in online learning. It should be greater than 1.0. In the literature, this is called tau\_0.

**max\_iter**int, default=10

The maximum number of passes over the training data (aka epochs). It only impacts the behavior in the [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation.fit "sklearn.decomposition.LatentDirichletAllocation.fit")
 method, and not the [`partial_fit`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation.partial_fit "sklearn.decomposition.LatentDirichletAllocation.partial_fit")
 method.

**batch\_size**int, default=128

Number of documents to use in each EM iteration. Only used in online learning.

**evaluate\_every**int, default=-1

How often to evaluate perplexity. Only used in `fit` method. set it to 0 or negative number to not evaluate perplexity in training at all. Evaluating perplexity can help you check convergence in training process, but it will also increase total training time. Evaluating perplexity in every iteration might increase training time up to two-fold.

**total\_samples**int, default=1e6

Total number of documents. Only used in the [`partial_fit`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation.partial_fit "sklearn.decomposition.LatentDirichletAllocation.partial_fit")
 method.

**perp\_tol**float, default=1e-1

Perplexity tolerance. Only used when `evaluate_every` is greater than 0.

**mean\_change\_tol**float, default=1e-3

Stopping tolerance for updating document topic distribution in E-step.

**max\_doc\_update\_iter**int, default=100

Max number of iterations for updating document topic distribution in the E-step.

**n\_jobs**int, default=None

The number of jobs to use in the E-step. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**verbose**int, default=0

Verbosity level.

**random\_state**int, RandomState instance or None, default=None

Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Attributes:

**components\_**ndarray of shape (n\_components, n\_features)

Variational parameters for topic word distribution. Since the complete conditional for topic word distribution is a Dirichlet, `components_[i, j]` can be viewed as pseudocount that represents the number of times word `j` was assigned to topic `i`. It can also be viewed as distribution over the words for each topic after normalization: `model.components_ / model.components_.sum(axis=1)[:, np.newaxis]`.

**exp\_dirichlet\_component\_**ndarray of shape (n\_components, n\_features)

Exponential value of expectation of log topic word distribution. In the literature, this is `exp(E[log(beta)])`.

**n\_batch\_iter\_**int

Number of iterations of the EM step.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

**n\_iter\_**int

Number of passes over the dataset.

**bound\_**float

Final perplexity score on training set.

**doc\_topic\_prior\_**float

Prior of document topic distribution `theta`. If the value is None, it is `1 / n_components`.

**random\_state\_**RandomState instance

RandomState instance that is generated either from a seed, the random number generator or by `np.random`.

**topic\_word\_prior\_**float

Prior of topic word distribution `beta`. If the value is None, it is `1 / n_components`.

See also

[`sklearn.discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")

A classifier with a linear decision boundary, generated by fitting class conditional densities to the data and using Bayes’ rule.

References

\[1\] ([1](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#id1)
,[2](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#id3)
,[3](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#id4)
)

“Online Learning for Latent Dirichlet Allocation”, Matthew D. Hoffman, David M. Blei, Francis Bach, 2010. [blei-lab/onlineldavb](https://github.com/blei-lab/onlineldavb)

\[[2](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#id2)\
\]

“Stochastic Variational Inference”, Matthew D. Hoffman, David M. Blei, Chong Wang, John Paisley, 2013. [https://jmlr.org/papers/volume14/hoffman13a/hoffman13a.pdf](https://jmlr.org/papers/volume14/hoffman13a/hoffman13a.pdf)

Examples

\>>> from sklearn.decomposition import LatentDirichletAllocation
\>>> from sklearn.datasets import make\_multilabel\_classification
\>>> \# This produces a feature matrix of token counts, similar to what
\>>> \# CountVectorizer would produce on text.
\>>> X, \_ \= make\_multilabel\_classification(random\_state\=0)
\>>> lda \= LatentDirichletAllocation(n\_components\=5,
...     random\_state\=0)
\>>> lda.fit(X)
LatentDirichletAllocation(...)
\>>> \# get topics for some given samples:
\>>> lda.transform(X\[\-2:\])
array(\[\[0.00360392, 0.25499205, 0.0036211 , 0.64236448, 0.09541846\],\
       \[0.15297572, 0.00362644, 0.44412786, 0.39568399, 0.003586  \]\])

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_lda.py#L624)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation.fit "Link to this definition")

Learn model for the data X with variational Bayes method.

When `learning_method` is ‘online’, use mini-batch update. Otherwise, use batch update.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Document word matrix.

**y**Ignored

Not used, present here for API consistency by convention.

Returns:

self

Fitted estimator.

fit\_transform(_X_, _y\=None_, _\*_, _normalize\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_lda.py#L752)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation.fit_transform "Link to this definition")

Fit to data, then transform it.

Fits transformer to `X` and `y` and returns a transformed version of `X`.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Input samples.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs), default=None

Target values (None for unsupervised transformations).

**normalize**bool, default=True

Whether to normalize the document topic distribution in `transform`.

Returns:

**X\_new**ndarray array of shape (n\_samples, n\_components)

Transformed array.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L1046)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

partial\_fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_lda.py#L576)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation.partial_fit "Link to this definition")

Online VB with Mini-Batch update.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Document word matrix.

**y**Ignored

Not used, present here for API consistency by convention.

Returns:

self

Partially fitted estimator.

perplexity(_X_, _sub\_sampling\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_lda.py#L925)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation.perplexity "Link to this definition")

Calculate approximate perplexity for data X.

Perplexity is defined as exp(-1. \* log-likelihood per word)

Changed in version 0.19: _doc\_topic\_distr_ argument has been deprecated and is ignored because user no longer has access to unnormalized distribution

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Document word matrix.

**sub\_sampling**bool

Do sub-sampling or not.

Returns:

**score**float

Perplexity score.

score(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_lda.py#L856)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation.score "Link to this definition")

Calculate approximate log-likelihood as score.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Document word matrix.

**y**Ignored

Not used, present here for API consistency by convention.

Returns:

**score**float

Use approximate bound as score.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

set\_transform\_request(_\*_, _normalize: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [LatentDirichletAllocation](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation "sklearn.decomposition._lda.LatentDirichletAllocation")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation.set_transform_request "Link to this definition")

Configure whether metadata should be requested to be passed to the `transform` method.

Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

The options for each parameter are:

*   `True`: metadata is requested, and passed to `transform` if provided. The request is ignored if metadata is not provided.
    
*   `False`: metadata is not requested and the meta-estimator will not pass it to `transform`.
    
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
    
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.
    

The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.

Added in version 1.3.

Parameters:

**normalize**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `normalize` parameter in `transform`.

Returns:

**self**object

The updated object.

transform(_X_, _\*_, _normalize\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_lda.py#L724)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation.transform "Link to this definition")

Transform data X according to the fitted model.

Changed in version 0.18: `doc_topic_distr` is now normalized.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Document word matrix.

**normalize**bool, default=True

Whether to normalize the document topic distribution.

Returns:

**doc\_topic\_distr**ndarray of shape (n\_samples, n\_components)

Document topic distribution for X.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_topics_extraction_with_nmf_lda_thumb.png)

[Topic extraction with Non-negative Matrix Factorization and Latent Dirichlet Allocation](https://scikit-learn.org/stable/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html)

Topic extraction with Non-negative Matrix Factorization and Latent Dirichlet Allocation

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)