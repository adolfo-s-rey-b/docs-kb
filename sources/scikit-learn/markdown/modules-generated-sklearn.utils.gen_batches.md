[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.gen_batches.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.gen_batches.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.gen_batches.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.gen_batches.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.gen_batches.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.gen_batches.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.gen_batches.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.gen_batches.html)

Collapse Sidebar Expand Sidebar

gen\_batches[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.gen_batches.html#gen-batches "Link to this heading")

=====================================================================================================================================

sklearn.utils.gen\_batches(_n_, _batch\_size_, _\*_, _min\_batch\_size\=0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_chunking.py#L25)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.gen_batches.html#sklearn.utils.gen_batches "Link to this definition")

Generator to create slices containing `batch_size` elements from 0 to `n`.

The last slice may contain less than `batch_size` elements, when `batch_size` does not divide `n`.

Parameters:

**n**int

Size of the sequence.

**batch\_size**int

Number of elements in each batch.

**min\_batch\_size**int, default=0

Minimum number of elements in each batch.

Yields:

slice of `batch_size` elements

See also

[`gen_even_slices`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.gen_even_slices.html#sklearn.utils.gen_even_slices "sklearn.utils.gen_even_slices")

Generator to create n\_packs slices going up to n.

Examples

\>>> from sklearn.utils import gen\_batches
\>>> list(gen\_batches(7, 3))
\[slice(0, 3, None), slice(3, 6, None), slice(6, 7, None)\]
\>>> list(gen\_batches(6, 3))
\[slice(0, 3, None), slice(3, 6, None)\]
\>>> list(gen\_batches(2, 3))
\[slice(0, 2, None)\]
\>>> list(gen\_batches(7, 3, min\_batch\_size\=0))
\[slice(0, 3, None), slice(3, 6, None), slice(6, 7, None)\]
\>>> list(gen\_batches(7, 3, min\_batch\_size\=2))
\[slice(0, 3, None), slice(3, 7, None)\]

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)