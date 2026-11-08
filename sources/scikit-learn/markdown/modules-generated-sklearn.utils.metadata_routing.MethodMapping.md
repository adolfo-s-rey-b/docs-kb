[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html)

Collapse Sidebar Expand Sidebar

MethodMapping[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html#methodmapping "Link to this heading")

===========================================================================================================================================================

class sklearn.utils.metadata\_routing.MethodMapping[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L793)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html#sklearn.utils.metadata_routing.MethodMapping "Link to this definition")

Stores the mapping between `caller` and `callee` methods for a [router](https://scikit-learn.org/stable/glossary.html#term-router)
.

This class is primarily used in a `get_metadata_routing()` of a router object when defining the mapping between the router’s methods and a sub-object (a sub-estimator or a scorer).

Iterating through an instance of this class yields `MethodPair(caller, callee)` instances.

Read more on developing custom estimators that can route metadata in the [Metadata Routing Developing Guide](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html#sphx-glr-auto-examples-miscellaneous-plot-metadata-routing-py)
.

Added in version 1.3.

Examples

\>>> from sklearn.utils.metadata\_routing import MethodMapping
\>>> MethodMapping().add(caller\="fit", callee\="split")
\[{'caller': 'fit', 'callee': 'split'}\]

Copy to clipboard

add(_\*_, _caller_, _callee_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L822)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html#sklearn.utils.metadata_routing.MethodMapping.add "Link to this definition")

Add a method mapping.

Parameters:

**caller**str

Parent estimator’s method name in which the `callee` is called.

**callee**str

Child object’s method name. This method is called in `caller`.

Returns:

**self**MethodMapping

Returns self.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

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