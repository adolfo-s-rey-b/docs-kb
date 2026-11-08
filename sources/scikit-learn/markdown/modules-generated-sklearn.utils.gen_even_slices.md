[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.gen_even_slices.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.gen_even_slices.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.gen_even_slices.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.gen_even_slices.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.gen_even_slices.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.gen_even_slices.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.gen_even_slices.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.gen_even_slices.html)

Collapse Sidebar Expand Sidebar

gen\_even\_slices[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.gen_even_slices.html#gen-even-slices "Link to this heading")

==================================================================================================================================================

sklearn.utils.gen\_even\_slices(_n_, _n\_packs_, _\*_, _n\_samples\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_chunking.py#L81)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.gen_even_slices.html#sklearn.utils.gen_even_slices "Link to this definition")

Generator to create `n_packs` evenly spaced slices going up to `n`.

If `n_packs` does not divide `n`, except for the first `n % n_packs` slices, remaining slices may contain fewer elements.

Parameters:

**n**int

Size of the sequence.

**n\_packs**int

Number of slices to generate.

**n\_samples**int, default=None

Number of samples. Pass `n_samples` when the slices are to be used for sparse matrix indexing; slicing off-the-end raises an exception, while it works for NumPy arrays.

Yields:

`slice` representing a set of indices from 0 to n.

See also

[`gen_batches`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.gen_batches.html#sklearn.utils.gen_batches "sklearn.utils.gen_batches")

Generator to create slices containing batch\_size elements from 0 to n.

Examples

\>>> from sklearn.utils import gen\_even\_slices
\>>> list(gen\_even\_slices(10, 1))
\[slice(0, 10, None)\]
\>>> list(gen\_even\_slices(10, 10))
\[slice(0, 1, None), slice(1, 2, None), ..., slice(9, 10, None)\]
\>>> list(gen\_even\_slices(10, 5))
\[slice(0, 2, None), slice(2, 4, None), ..., slice(8, 10, None)\]
\>>> list(gen\_even\_slices(10, 3))
\[slice(0, 4, None), slice(4, 7, None), slice(7, 10, None)\]

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.gen_even_slices.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_poisson_regression_non_normal_loss_thumb.png)

[Poisson regression and non-normal loss](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html)

Poisson regression and non-normal loss

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)