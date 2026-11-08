[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metaestimators.available_if.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.metaestimators.available_if.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metaestimators.available_if.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.metaestimators.available_if.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.metaestimators.available_if.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.metaestimators.available_if.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.metaestimators.available_if.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.metaestimators.available_if.html)

Collapse Sidebar Expand Sidebar

available\_if[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metaestimators.available_if.html#available-if "Link to this heading")

=======================================================================================================================================================

sklearn.utils.metaestimators.available\_if(_check_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_available_if.py#L57)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metaestimators.available_if.html#sklearn.utils.metaestimators.available_if "Link to this definition")

An attribute that is available only if check returns a truthy value.

Parameters:

**check**callable

When passed the object with the decorated method, this should return a truthy value if the attribute is available, and either return False or raise an AttributeError if not available.

Returns:

callable

Callable makes the decorated method available if `check` returns a truthy value, otherwise the decorated method is unavailable.

Examples

\>>> from sklearn.utils.metaestimators import available\_if
\>>> class HelloIfEven:
...    def \_\_init\_\_(self, x):
...        self.x \= x
...
...    def \_x\_is\_even(self):
...        return self.x % 2 \== 0
...
...    @available\_if(\_x\_is\_even)
...    def say\_hello(self):
...        print("Hello")
...
\>>> obj \= HelloIfEven(1)
\>>> hasattr(obj, "say\_hello")
False
\>>> obj.x \= 2
\>>> hasattr(obj, "say\_hello")
True
\>>> obj.say\_hello()
Hello

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metaestimators.available_if.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_inductive_clustering_thumb.png)

[Inductive Clustering](https://scikit-learn.org/stable/auto_examples/cluster/plot_inductive_clustering.html)

Inductive Clustering

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)