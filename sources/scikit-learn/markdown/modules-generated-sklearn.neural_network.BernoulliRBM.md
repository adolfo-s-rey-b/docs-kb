[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.neural_network.BernoulliRBM.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.neural_network.BernoulliRBM.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.neural_network.BernoulliRBM.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.neural_network.BernoulliRBM.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.neural_network.BernoulliRBM.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.neural_network.BernoulliRBM.html)

Collapse Sidebar Expand Sidebar

BernoulliRBM[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#bernoullirbm "Link to this heading")

================================================================================================================================================

class sklearn.neural\_network.BernoulliRBM(_n\_components\=256_, _\*_, _learning\_rate\=0.1_, _batch\_size\=10_, _n\_iter\=10_, _verbose\=0_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neural_network/_rbm.py#L25)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM "Link to this definition")

Bernoulli Restricted Boltzmann Machine (RBM).

A Restricted Boltzmann Machine with binary visible units and binary hidden units. Parameters are estimated using Stochastic Maximum Likelihood (SML), also known as Persistent Contrastive Divergence (PCD) \[2\].

The time complexity of this implementation is `O(d ** 2)` assuming d ~ n\_features ~ n\_components.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/neural_networks_unsupervised.html#rbm)
.

Parameters:

**n\_components**int, default=256

Number of binary hidden units.

**learning\_rate**float, default=0.1

The learning rate for weight updates. It is _highly_ recommended to tune this hyper-parameter. Reasonable values are in the 10\*\*\[0., -3.\] range.

**batch\_size**int, default=10

Number of examples per minibatch.

**n\_iter**int, default=10

Number of iterations/sweeps over the training dataset to perform during training.

**verbose**int, default=0

The verbosity level. The default, zero, means silent mode. Range of values is \[0, inf\].

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for:

*   Gibbs sampling from visible and hidden layers.
    
*   Initializing components, sampling from layers during fit.
    
*   Corrupting the data when scoring samples.
    

Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Attributes:

**intercept\_hidden\_**array-like of shape (n\_components,)

Biases of the hidden units.

**intercept\_visible\_**array-like of shape (n\_features,)

Biases of the visible units.

**components\_**array-like of shape (n\_components, n\_features)

Weight matrix, where `n_features` is the number of visible units and `n_components` is the number of hidden units.

**h\_samples\_**array-like of shape (batch\_size, n\_components)

Hidden Activation sampled from the model distribution, where `batch_size` is the number of examples per minibatch and `n_components` is the number of hidden units.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`sklearn.neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")

Multi-layer Perceptron regressor.

[`sklearn.neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")

Multi-layer Perceptron classifier.

[`sklearn.decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")

An unsupervised linear dimensionality reduction model.

References

\[1\] Hinton, G. E., Osindero, S. and Teh, Y. A fast learning algorithm for

deep belief nets. Neural Computation 18, pp 1527-1554. [https://www.cs.toronto.edu/~hinton/absps/fastnc.pdf](https://www.cs.toronto.edu/~hinton/absps/fastnc.pdf)

\[2\] Tieleman, T. Training Restricted Boltzmann Machines using

Approximations to the Likelihood Gradient. International Conference on Machine Learning (ICML) 2008

Examples

\>>> import numpy as np
\>>> from sklearn.neural\_network import BernoulliRBM
\>>> X \= np.array(\[\[0, 0, 0\], \[0, 1, 1\], \[1, 0, 1\], \[1, 1, 1\]\])
\>>> model \= BernoulliRBM(n\_components\=2)
\>>> model.fit(X)
BernoulliRBM(n\_components=2)

Copy to clipboard

For a more detailed example usage, see [Restricted Boltzmann Machine features for digit classification](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_rbm_logistic_classification.html#sphx-glr-auto-examples-neural-networks-plot-rbm-logistic-classification-py)
.

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neural_network/_rbm.py#L385)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM.fit "Link to this definition")

Fit the model to the data X.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training data.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs), default=None

Target values (None for unsupervised transformations).

Returns:

**self**BernoulliRBM

The fitted model.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM.fit_transform "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

The feature names out will prefixed by the lowercased class name. For example, if the transformer outputs 3 features, then the feature names out are: `["class_name0", "class_name1", "class_name2"]`.

Parameters:

**input\_features**array-like of str or None, default=None

Only used to validate feature names with the names seen in `fit`.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

gibbs(_v_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neural_network/_rbm.py#L251)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM.gibbs "Link to this definition")

Perform one Gibbs sampling step.

Parameters:

**v**ndarray of shape (n\_samples, n\_features)

Values of the visible layer to start from.

Returns:

**v\_new**ndarray of shape (n\_samples, n\_features)

Values of the visible layer after one Gibbs step.

partial\_fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neural_network/_rbm.py#L272)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM.partial_fit "Link to this definition")

Fit the model to the partial segment of the data X.

Parameters:

**X**ndarray of shape (n\_samples, n\_features)

Training data.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs), default=None

Target values (None for unsupervised transformations).

Returns:

**self**BernoulliRBM

The fitted model.

score\_samples(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neural_network/_rbm.py#L344)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM.score_samples "Link to this definition")

Compute the pseudo-likelihood of X.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Values of the visible layer. Must be all-boolean (not checked).

Returns:

**pseudo\_likelihood**ndarray of shape (n\_samples,)

Value of the pseudo-likelihood (proxy for likelihood).

Notes

This method is not deterministic: it computes a quantity called the free energy on X, then on a randomly corrupted version of X, and returns the log of the logistic function of the difference.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM.set_output "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neural_network/_rbm.py#L157)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM.transform "Link to this definition")

Compute the hidden layer activation probabilities, P(h=1|v=X).

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data to be transformed.

Returns:

**h**ndarray of shape (n\_samples, n\_components)

Latent representations of the data.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbm_logistic_classification_thumb.png)

[Restricted Boltzmann Machine features for digit classification](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_rbm_logistic_classification.html)

Restricted Boltzmann Machine features for digit classification

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)