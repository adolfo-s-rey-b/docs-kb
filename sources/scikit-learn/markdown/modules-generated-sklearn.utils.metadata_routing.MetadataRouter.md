[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html)

Collapse Sidebar Expand Sidebar

MetadataRouter[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#metadatarouter "Link to this heading")

==============================================================================================================================================================

class sklearn.utils.metadata\_routing.MetadataRouter(_owner_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L872)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "Link to this definition")

Coordinates metadata routing for a [router](https://scikit-learn.org/stable/glossary.html#term-router)
 object.

This class is used by [meta-estimators](https://scikit-learn.org/stable/glossary.html#term-meta-estimators)
 or functions that can route metadata, to handle their metadata routing. Routing information is stored in a dictionary-like structure of the form `{"object_name": RouterMappingPair(mapping, router)}`, where `mapping` is an instance of [`MethodMapping`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html#sklearn.utils.metadata_routing.MethodMapping "sklearn.utils.metadata_routing.MethodMapping")
 and `router` is either a [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 or another [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 instance.

Read more on developing custom estimators that can route metadata in the [Metadata Routing Developing Guide](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html#sphx-glr-auto-examples-miscellaneous-plot-metadata-routing-py)
.

Added in version 1.3.

Parameters:

**owner**object

The object to which these requests belong.

Examples

\>>> from pprint import pprint
\>>> from sklearn import set\_config
\>>> from sklearn.feature\_selection import SelectFromModel
\>>> from sklearn.linear\_model import LinearRegression
\>>> from sklearn.utils.metadata\_routing import MetadataRouter, MethodMapping
\>>> set\_config(enable\_metadata\_routing\=True)
\>>> meta\_estimator \= SelectFromModel(
...     estimator\=LinearRegression().set\_fit\_request(sample\_weight\=True)
... )
\>>> router \= MetadataRouter(owner\=meta\_estimator).add(
...     estimator\=meta\_estimator.estimator,
...     method\_mapping\=MethodMapping()
...     .add(caller\="partial\_fit", callee\="partial\_fit")
...     .add(caller\="fit", callee\="fit"),
... )
\>>> pprint(router)
{'estimator': {'mapping': \[{'caller': 'partial\_fit', 'callee': 'partial\_fit'},\
                       {'caller': 'fit', 'callee': 'fit'}\],
           'router': {'fit': {'sample\_weight': True},
                      'score': {'sample\_weight': None}}}}
\>>> set\_config(enable\_metadata\_routing\=False)

Copy to clipboard

add(_\*_, _method\_mapping_, _\*\*objs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L988)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter.add "Link to this definition")

Add [consumers](https://scikit-learn.org/stable/glossary.html#term-consumer)
 to the `MetadataRouter`.

The estimators that consume metadata are passed as named objects along with a method mapping, that defines how their methods relate to those of the [router](https://scikit-learn.org/stable/glossary.html#term-router)
.

Parameters:

**method\_mapping**MethodMapping

The mapping between the child ([consumer](https://scikit-learn.org/stable/glossary.html#term-consumer)
) and the parent’s ([router](https://scikit-learn.org/stable/glossary.html#term-router)
’s) methods.

**\*\*objs**dict

A dictionary of objects, whose requests are extracted by calling [`get_routing_for_object`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.get_routing_for_object.html#sklearn.utils.metadata_routing.get_routing_for_object "sklearn.utils.metadata_routing.get_routing_for_object")
 on them.

Returns:

**self**MetadataRouter

Returns `self`.

add\_self\_request(_obj_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L952)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter.add_self_request "Link to this definition")

Add `self` (as a [consumer](https://scikit-learn.org/stable/glossary.html#term-consumer)
) to the `MetadataRouter`.

This method is used if the [router](https://scikit-learn.org/stable/glossary.html#term-router)
 is also a [consumer](https://scikit-learn.org/stable/glossary.html#term-consumer)
, and hence the router itself needs to be included in the routing. The passed object can be an estimator or a [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
.

A router should add itself using this method instead of `add` since it should be treated differently than the other consumer objects to which metadata is routed by the router.

Parameters:

**obj**object

This is typically the router instance, i.e. `self` in a `get_metadata_routing()` implementation. It can also be a `MetadataRequest` instance.

Returns:

**self**MetadataRouter

Returns `self`.

consumes(_method_, _params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1018)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter.consumes "Link to this definition")

Return params consumed as metadata in a [router](https://scikit-learn.org/stable/glossary.html#term-router)
 or its sub-estimators.

This method returns the subset of `params` that are consumed by the `method`. A `param` is considered consumed if it is used in the specified method of the [router](https://scikit-learn.org/stable/glossary.html#term-router)
 itself or any of its sub-estimators (or their sub-estimators).

Added in version 1.4.

Parameters:

**method**str

The name of the method for which to determine consumed parameters.

**params**iterable of str

An iterable of parameter names to test for consumption.

Returns:

**consumed\_params**set of str

A subset of parameters from `params` which are consumed by this method.

route\_params(_\*_, _caller_, _params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1167)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter.route_params "Link to this definition")

Get the values of metadata requested by [consumers](https://scikit-learn.org/stable/glossary.html#term-consumer)
.

Returns a [`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")
 containing the metadata that this [router](https://scikit-learn.org/stable/glossary.html#term-router)
’s `caller` method needs to route, organized by each [consumer](https://scikit-learn.org/stable/glossary.html#term-consumer)
 and their corresponding methods.

This can be used to pass the required metadata to corresponding methods in consumers.

Parameters:

**caller**str

The name of the [router](https://scikit-learn.org/stable/glossary.html#term-router)
’s method through which the metadata is routed. For example, if called inside the [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 method of a router, this would be `"fit"`.

**params**dict

A dictionary of provided metadata.

Returns:

**params**Bunch

A [`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")
 of the form `{"object_name": {"method_name": {metadata: value}}}`.

validate\_metadata(_\*_, _method_, _params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1211)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter.validate_metadata "Link to this definition")

Validate given metadata for a method.

This raises a `TypeError` if some of the passed metadata are not understood by child objects.

Parameters:

**method**str

The name of the [router](https://scikit-learn.org/stable/glossary.html#term-router)
’s method through which the metadata is routed. For example, if called inside the [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 method of a router, this would be `"fit"`.

**params**dict

A dictionary of provided metadata.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_metadata_routing_thumb.png)

[Developing Estimators Compliant with Metadata Routing](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html)

Developing Estimators Compliant with Metadata Routing

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)