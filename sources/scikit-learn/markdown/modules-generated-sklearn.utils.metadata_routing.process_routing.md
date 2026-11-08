[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.process_routing.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.metadata_routing.process_routing.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.process_routing.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.metadata_routing.process_routing.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.metadata_routing.process_routing.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.metadata_routing.process_routing.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.metadata_routing.process_routing.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.metadata_routing.process_routing.html)

Collapse Sidebar Expand Sidebar

process\_routing[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.process_routing.html#process-routing "Link to this heading")

==================================================================================================================================================================

sklearn.utils.metadata\_routing.process\_routing(_\_obj_, _\_method_, _/_, _\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1768)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.process_routing.html#sklearn.utils.metadata_routing.process_routing "Link to this definition")

Validate and route metadata.

This function is used inside a [router](https://scikit-learn.org/stable/glossary.html#term-router)
’s method, e.g. [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
, to validate the metadata and handle the routing.

Assuming this signature of a router’s fit method: `fit(self, X, y, sample_weight=None, **fit_params)`, a call to this function would be: `process_routing(self, "fit", sample_weight=sample_weight, **fit_params)`.

Internally, the function uses the router’s `MetadataRouter` object (as returned by a call to its `get_metadata_routing` method) to validate per method that the routed metadata had been requested by the underlying estimator, and extracts a mapping of the given metadata to the requested metadata based on the routing information defined by the `MetadataRouter`.

Note that if routing is not enabled and `kwargs` is empty, then it returns an empty routing where `process_routing(...).ANYTHING.ANY_METHOD` is always an empty dictionary.

The output of this function is a [`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")
 that has a key for each consuming object and those hold keys for their consuming methods, which then contain keys for the metadata which should be routed to them. Consumers should use item access (`routed_params[child][method]`) rather than attribute access, so that the structure remains usable after crossing process boundaries (e.g. [`joblib.Parallel`](https://joblib.readthedocs.io/en/latest/generated/joblib.Parallel.html#joblib.Parallel "(in joblib v1.7)")
 with the dask backend), where serializers may downgrade [`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")
 to plain [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")
.

Read more on developing custom estimators that can route metadata in the [Metadata Routing Developing Guide](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html#sphx-glr-auto-examples-miscellaneous-plot-metadata-routing-py)
.

Added in version 1.3.

Parameters:

**\_obj**object

An object implementing `get_metadata_routing`. Typically a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
.

**\_method**str

The name of the router’s method in which this function is called.

**\*\*kwargs**dict

Metadata to be routed.

Returns:

**routed\_params**Bunch

A [`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")
 of the form `{"object_name": {"method_name": {metadata: value}}}` which can be used to pass the required metadata to corresponding methods or corresponding child objects. The object names are those defined in `obj.get_metadata_routing()`.

Examples

\>>> import numpy as np
\>>> from sklearn import set\_config
\>>> from sklearn.utils.metadata\_routing import process\_routing
\>>> from sklearn.linear\_model import Ridge
\>>> from sklearn.feature\_selection import SelectFromModel
\>>> set\_config(enable\_metadata\_routing\=True)
\>>> process\_routing(
...     SelectFromModel(Ridge().set\_fit\_request(sample\_weight\=True)),
...     "fit",
...     sample\_weight\=np.array(\[1, 1, 2\]),
... )
{'estimator': {'fit': {'sample\_weight': array(\[1, 1, 2\])}}}
\>>> set\_config(enable\_metadata\_routing\=False)

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.process_routing.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

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