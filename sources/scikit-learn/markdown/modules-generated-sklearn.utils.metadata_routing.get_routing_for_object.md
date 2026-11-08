[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.get_routing_for_object.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.metadata_routing.get_routing_for_object.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.get_routing_for_object.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.metadata_routing.get_routing_for_object.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.metadata_routing.get_routing_for_object.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.metadata_routing.get_routing_for_object.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.metadata_routing.get_routing_for_object.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.metadata_routing.get_routing_for_object.html)

Collapse Sidebar Expand Sidebar

get\_routing\_for\_object[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.get_routing_for_object.html#get-routing-for-object "Link to this heading")

=========================================================================================================================================================================================

sklearn.utils.metadata\_routing.get\_routing\_for\_object(_obj\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1280)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.get_routing_for_object.html#sklearn.utils.metadata_routing.get_routing_for_object "Link to this definition")

Get a `Metadata{Router, Request}` instance from the given object.

This function returns a [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 or a [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 from the given input.

This function always returns a copy or a new instance constructed from the input, such that changing the output of this function will not change the original object.

Added in version 1.3.

Parameters:

**obj**object

*   If the object provides a `get_metadata_routing` method, return a copy
    
    of the output of that method.
    
*   If the object is already a
    
    [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
     or a [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
    , return a copy of that.
    
*   Returns an empty [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
    
    otherwise.
    

Returns:

**obj**MetadataRequest or MetadataRouter

A `MetadataRequest` or a `MetadataRouter` taken or created from the given object.

Examples

\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.pipeline import Pipeline
\>>> from sklearn.preprocessing import StandardScaler
\>>> from sklearn.linear\_model import LogisticRegressionCV
\>>> from sklearn.utils.metadata\_routing import get\_routing\_for\_object
\>>> X, y \= make\_classification()
\>>> pipe \= Pipeline(
...       \[("scaler", StandardScaler()), ("lr\_cv", LogisticRegressionCV())\]
... )
\>>> pipe.fit(X, y)
Pipeline(steps=\[('scaler', StandardScaler()), ('lr\_cv', LogisticRegressionCV())\])
\>>> type(get\_routing\_for\_object(pipe))
<class 'sklearn.utils.\_metadata\_requests.MetadataRouter'>
\>>> type(get\_routing\_for\_object(pipe.named\_steps.scaler))
<class 'sklearn.utils.\_metadata\_requests.MetadataRequest'>
\>>> type(get\_routing\_for\_object(pipe.named\_steps.lr\_cv))
<class 'sklearn.utils.\_metadata\_requests.MetadataRouter'>

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)