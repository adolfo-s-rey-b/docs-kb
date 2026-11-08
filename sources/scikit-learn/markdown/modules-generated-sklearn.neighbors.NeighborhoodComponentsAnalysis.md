[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html)

Collapse Sidebar Expand Sidebar

NeighborhoodComponentsAnalysis[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#neighborhoodcomponentsanalysis "Link to this heading")

=================================================================================================================================================================================================

class sklearn.neighbors.NeighborhoodComponentsAnalysis(_n\_components\=None_, _\*_, _init\='auto'_, _warm\_start\=False_, _max\_iter\=50_, _tol\=1e-05_, _callback\=None_, _verbose\=0_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_nca.py#L34)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis "Link to this definition")

Neighborhood Components Analysis.

Neighborhood Component Analysis (NCA) is a machine learning algorithm for metric learning. It learns a linear transformation in a supervised fashion to improve the classification accuracy of a stochastic nearest neighbors rule in the transformed space.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/neighbors.html#nca)
.

Parameters:

**n\_components**int, default=None

Preferred dimensionality of the projected space. If None it will be set to `n_features`.

**init**{‘auto’, ‘pca’, ‘lda’, ‘identity’, ‘random’} or ndarray of shape (n\_features\_a, n\_features\_b), default=’auto’

Initialization of the linear transformation. Possible options are `'auto'`, `'pca'`, `'lda'`, `'identity'`, `'random'`, and a numpy array of shape `(n_features_a, n_features_b)`.

*   `'auto'`
    
    Depending on `n_components`, the most reasonable initialization is chosen. If `n_components <= min(n_features, n_classes - 1)` we use `'lda'`, as it uses labels information. If not, but `n_components < min(n_features, n_samples)`, we use `'pca'`, as it projects data in meaningful directions (those of higher variance). Otherwise, we just use `'identity'`.
    
*   `'pca'`
    
    `n_components` principal components of the inputs passed to [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis.fit "sklearn.neighbors.NeighborhoodComponentsAnalysis.fit")
     will be used to initialize the transformation. (See [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
    )
    
*   `'lda'`
    
    `min(n_components, n_classes)` most discriminative components of the inputs passed to [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis.fit "sklearn.neighbors.NeighborhoodComponentsAnalysis.fit")
     will be used to initialize the transformation. (If `n_components > n_classes`, the rest of the components will be zero.) (See [`LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
    )
    
*   `'identity'`
    
    If `n_components` is strictly smaller than the dimensionality of the inputs passed to [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis.fit "sklearn.neighbors.NeighborhoodComponentsAnalysis.fit")
    , the identity matrix will be truncated to the first `n_components` rows.
    
*   `'random'`
    
    The initial transformation will be a random array of shape `(n_components, n_features)`. Each value is sampled from the standard normal distribution.
    
*   numpy array
    
    `n_features_b` must match the dimensionality of the inputs passed to [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis.fit "sklearn.neighbors.NeighborhoodComponentsAnalysis.fit")
     and n\_features\_a must be less than or equal to that. If `n_components` is not `None`, `n_features_a` must match it.
    

**warm\_start**bool, default=False

If `True` and [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis.fit "sklearn.neighbors.NeighborhoodComponentsAnalysis.fit")
 has been called before, the solution of the previous call to [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis.fit "sklearn.neighbors.NeighborhoodComponentsAnalysis.fit")
 is used as the initial linear transformation (`n_components` and `init` will be ignored).

**max\_iter**int, default=50

Maximum number of iterations in the optimization.

**tol**float, default=1e-5

Convergence tolerance for the optimization.

**callback**callable, default=None

If not `None`, this function is called after every iteration of the optimizer, taking as arguments the current solution (flattened transformation matrix) and the number of iterations. This might be useful in case one wants to examine or store the transformation found after each iteration.

**verbose**int, default=0

If 0, no progress messages will be printed. If 1, progress messages will be printed to stdout. If > 1, progress messages will be printed and the `disp` parameter of [`scipy.optimize.minimize`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html#scipy.optimize.minimize "(in SciPy v1.18.0)")
 will be set to `verbose - 2`.

**random\_state**int or numpy.RandomState, default=None

A pseudo random number generator object or a seed for it if int. If `init='random'`, `random_state` is used to initialize the random transformation. If `init='pca'`, `random_state` is passed as an argument to PCA when initializing the transformation. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Attributes:

**components\_**ndarray of shape (n\_components, n\_features)

The linear transformation learned during fitting.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**n\_iter\_**int

Counts the number of iterations performed by the optimizer.

**random\_state\_**numpy.RandomState

Pseudo random number generator object used during initialization.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`sklearn.discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")

Linear Discriminant Analysis.

[`sklearn.decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")

Principal component analysis (PCA).

References

\[1\]

J. Goldberger, G. Hinton, S. Roweis, R. Salakhutdinov. “Neighbourhood Components Analysis”. Advances in Neural Information Processing Systems. 17, 513-520, 2005. [https://www.cs.toronto.edu/~rsalakhu/papers/ncanips.pdf](https://www.cs.toronto.edu/~rsalakhu/papers/ncanips.pdf)

\[2\]

Wikipedia entry on Neighborhood Components Analysis [https://en.wikipedia.org/wiki/Neighbourhood\_components\_analysis](https://en.wikipedia.org/wiki/Neighbourhood_components_analysis)

Examples

\>>> from sklearn.neighbors import NeighborhoodComponentsAnalysis
\>>> from sklearn.neighbors import KNeighborsClassifier
\>>> from sklearn.datasets import load\_iris
\>>> from sklearn.model\_selection import train\_test\_split
\>>> X, y \= load\_iris(return\_X\_y\=True)
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(X, y,
... stratify\=y, test\_size\=0.7, random\_state\=42)
\>>> nca \= NeighborhoodComponentsAnalysis(random\_state\=42)
\>>> nca.fit(X\_train, y\_train)
NeighborhoodComponentsAnalysis(...)
\>>> knn \= KNeighborsClassifier(n\_neighbors\=3)
\>>> knn.fit(X\_train, y\_train)
KNeighborsClassifier(...)
\>>> print(knn.score(X\_test, y\_test))
0.933333...
\>>> knn.fit(nca.transform(X\_train), y\_train)
KNeighborsClassifier(...)
\>>> print(knn.score(nca.transform(X\_test), y\_test))
0.961904...

Copy to clipboard

fit(_X_, _y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_nca.py#L225)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis.fit "Link to this definition")

Fit the model according to the given training data.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

The training samples.

**y**array-like of shape (n\_samples,)

The corresponding training labels.

Returns:

**self**object

Fitted estimator.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis.fit_transform "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neighbors/_nca.py#L348)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis.transform "Link to this definition")

Apply the learned transformation to the given data.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Data samples.

Returns:

X\_embedded: ndarray of shape (n\_samples, n\_components)

The data samples transformed.

Raises:

NotFittedError

If [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis.fit "sklearn.neighbors.NeighborhoodComponentsAnalysis.fit")
 has not been called before.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_thumb.png)

[Manifold learning on handwritten digits: Locally Linear Embedding, Isomap…](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html)

Manifold learning on handwritten digits: Locally Linear Embedding, Isomap...

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_classification_thumb.png)

[Comparing Nearest Neighbors with and without Neighborhood Components Analysis](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_classification.html)

Comparing Nearest Neighbors with and without Neighborhood Components Analysis

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_dim_reduction_thumb.png)

[Dimensionality Reduction with Neighborhood Components Analysis](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_dim_reduction.html)

Dimensionality Reduction with Neighborhood Components Analysis

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_illustration_thumb.png)

[Neighborhood Components Analysis Illustration](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_illustration.html)

Neighborhood Components Analysis Illustration

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)