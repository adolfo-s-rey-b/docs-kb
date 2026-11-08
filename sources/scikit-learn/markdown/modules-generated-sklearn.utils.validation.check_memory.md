[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_memory.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.validation.check_memory.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_memory.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.validation.check_memory.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.validation.check_memory.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.validation.check_memory.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.validation.check_memory.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.validation.check_memory.html)

Collapse Sidebar Expand Sidebar

check\_memory[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_memory.html#check-memory "Link to this heading")

===================================================================================================================================================

sklearn.utils.validation.check\_memory(_memory_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/validation.py#L399)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_memory.html#sklearn.utils.validation.check_memory "Link to this definition")

Check that `memory` is joblib.Memory-like.

joblib.Memory-like means that `memory` can be converted into a joblib.Memory instance (typically a str denoting the `location`) or has the same interface (has a `cache` method).

Parameters:

**memory**None, str or object with the joblib.Memory interface

*   If string, the location where to create the `joblib.Memory` interface.
    
*   If None, no caching is done and the Memory object is completely transparent.
    

Returns:

**memory**object with the joblib.Memory interface

A correct joblib.Memory object.

Raises:

ValueError

If `memory` is not joblib.Memory-like.

Examples

\>>> from sklearn.utils.validation import check\_memory
\>>> check\_memory("caching\_dir")
Memory(location=caching\_dir/joblib)

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)