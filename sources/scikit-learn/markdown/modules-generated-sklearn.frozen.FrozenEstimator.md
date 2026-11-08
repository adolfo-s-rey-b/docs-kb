[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.frozen.FrozenEstimator.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.frozen.FrozenEstimator.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.frozen.FrozenEstimator.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.frozen.FrozenEstimator.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.frozen.FrozenEstimator.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.frozen.FrozenEstimator.html)

Collapse Sidebar Expand Sidebar

FrozenEstimator[#](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#frozenestimator "Link to this heading")

=================================================================================================================================================

class sklearn.frozen.FrozenEstimator(_estimator_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/frozen/_frozen.py#L27)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator "Link to this definition")

Estimator that wraps a fitted estimator to prevent re-fitting.

This meta-estimator takes an estimator and freezes it, in the sense that calling `fit` on it has no effect. `fit_predict` and `fit_transform` are also disabled. All other methods are delegated to the original estimator and original estimator’s attributes are accessible as well.

This is particularly useful when you have a fitted or a pre-trained model as a transformer in a pipeline, and you’d like `pipeline.fit` to have no effect on this step.

Parameters:

**estimator**estimator

The estimator which is to be kept frozen.

See also

[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")

No similar entry in the scikit-learn documentation.

Examples

\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.frozen import FrozenEstimator
\>>> from sklearn.linear\_model import LogisticRegression
\>>> X, y \= make\_classification(random\_state\=0)
\>>> clf \= LogisticRegression(random\_state\=0).fit(X, y)
\>>> frozen\_clf \= FrozenEstimator(clf)
\>>> frozen\_clf.fit(X, y)  \# No-op
FrozenEstimator(estimator=LogisticRegression(random\_state=0))
\>>> frozen\_clf.predict(X)  \# Predictions from \`clf.predict\`
array(...)

Copy to clipboard

fit(_X_, _y_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/frozen/_frozen.py#L89)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator.fit "Link to this definition")

No-op.

As a frozen estimator, calling `fit` has no effect.

Parameters:

**X**object

Ignored.

**y**object

Ignored.

**\*args**tuple

Additional positional arguments. Ignored, but present for API compatibility with `self.estimator`.

**\*\*kwargs**dict

Additional keyword arguments. Ignored, but present for API compatibility with `self.estimator`.

Returns:

**self**object

Returns the instance itself.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/frozen/_frozen.py#L145)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator.get_params "Link to this definition")

Get parameters for this estimator.

Returns a `{"estimator": estimator}` dict. The parameters of the inner estimator are not included.

Parameters:

**deep**bool, default=True

Ignored.

Returns:

**params**dict

Parameter names mapped to their values.

set\_params(_\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/frozen/_frozen.py#L118)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator.set_params "Link to this definition")

Set the parameters of this estimator.

The only valid key here is `estimator`. You cannot set the parameters of the inner estimator.

Parameters:

**\*\*kwargs**dict

Estimator parameters.

Returns:

**self**FrozenEstimator

This estimator.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_multiclass_thumb.png)

[Probability Calibration for 3-class classification](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_multiclass.html)

Probability Calibration for 3-class classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_frozen_examples_thumb.png)

[Examples of Using FrozenEstimator](https://scikit-learn.org/stable/auto_examples/frozen/plot_frozen_examples.html)

Examples of Using FrozenEstimator

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_sensitive_learning_thumb.png)

[Post-tuning the decision threshold for cost-sensitive learning](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html)

Post-tuning the decision threshold for cost-sensitive learning

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_6_0_thumb.png)

[Release Highlights for scikit-learn 1.6](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html)

Release Highlights for scikit-learn 1.6

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)