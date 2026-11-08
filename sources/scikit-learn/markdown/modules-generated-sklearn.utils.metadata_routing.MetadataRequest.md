[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html)

Collapse Sidebar Expand Sidebar

MetadataRequest[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#metadatarequest "Link to this heading")

=================================================================================================================================================================

class sklearn.utils.metadata\_routing.MetadataRequest(_owner_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L570)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "Link to this definition")

Container for storing metadata request info and an associated consumer (`owner`).

Instances of `MethodMetadataRequest` are used in this class for each available method under `MetadataRequest(owner=obj).{method}`.

Every [consumer](https://scikit-learn.org/stable/glossary.html#term-consumer)
 in scikit-learn has a `_metadata_request` attribute that is a `MetadataRequest`.

Read more on developing custom estimators that can route metadata in the [Metadata Routing Developing Guide](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html#sphx-glr-auto-examples-miscellaneous-plot-metadata-routing-py)
.

Added in version 1.3.

Parameters:

**owner**object

The object to which these requests belong.

Examples

\>>> from sklearn import set\_config
\>>> set\_config(enable\_metadata\_routing\=True)
\>>> from pprint import pprint
\>>> from sklearn.utils.metadata\_routing import MetadataRequest
\>>> r \= MetadataRequest(owner\="any\_object")
\>>> r.fit.add\_request(param\="sample\_weight", alias\=True)
{'sample\_weight': True}
\>>> r.score.add\_request(param\="sample\_weight", alias\=False)
{'sample\_weight': False}
\>>> pprint(r)
{'fit': {'sample\_weight': True}, 'score': {'sample\_weight': False}}
\>>> set\_config(enable\_metadata\_routing\=False)

Copy to clipboard

consumes(_method_, _params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L628)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest.consumes "Link to this definition")

Return params consumed as metadata in a [consumer](https://scikit-learn.org/stable/glossary.html#term-consumer)
.

This method returns the subset of given `params` that are consumed by the given `method`. It can be used to check if parameters are used as metadata in the specified method of the [consumer](https://scikit-learn.org/stable/glossary.html#term-consumer)
 that owns this `MetadataRequest` instance.

Added in version 1.4.

Parameters:

**method**str

The name of the method for which to determine consumed parameters.

**params**iterable of str

An iterable of parameter names to test for consumption.

Returns:

**consumed\_params**set of str

A subset of parameters from `params` which are consumed by the given method.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)