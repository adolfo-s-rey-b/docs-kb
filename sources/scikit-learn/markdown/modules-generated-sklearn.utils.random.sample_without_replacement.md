[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.random.sample_without_replacement.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.random.sample_without_replacement.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.random.sample_without_replacement.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.random.sample_without_replacement.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.random.sample_without_replacement.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.random.sample_without_replacement.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.random.sample_without_replacement.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.random.sample_without_replacement.html)

Collapse Sidebar Expand Sidebar

sample\_without\_replacement[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.random.sample_without_replacement.html#sample-without-replacement "Link to this heading")

==========================================================================================================================================================================================

sklearn.utils.random.sample\_without\_replacement(_n\_population_, _n\_samples_, _method\='auto'_, _random\_state\=None_)[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.random.sample_without_replacement.html#sklearn.utils.random.sample_without_replacement "Link to this definition")

Sample integers without replacement.

Select n\_samples integers from the set \[0, n\_population) without replacement.\
\
Parameters:\
\
**n\_population**int\
\
The size of the set to sample from.\
\
**n\_samples**int\
\
The number of integer to sample.\
\
**random\_state**int, RandomState instance or None, default=None\
\
If int, random\_state is the seed used by the random number generator; If RandomState instance, random\_state is the random number generator; If None, the random number generator is the RandomState instance used by `np.random`.\
\
**method**{“auto”, “tracking\_selection”, “reservoir\_sampling”, “pool”}, default=’auto’\
\
If method == “auto”, the ratio of n\_samples / n\_population is used to determine which algorithm to use: If ratio is between 0 and 0.01, tracking selection is used. If ratio is between 0.01 and 0.99, numpy.random.permutation is used. If ratio is greater than 0.99, reservoir sampling is used. The order of the selected integers is undefined. If a random order is desired, the selected subset should be shuffled.\
\
If method ==”tracking\_selection”, a set based implementation is used which is suitable for `n_samples` <<< `n_population`.\
\
If method == “reservoir\_sampling”, a reservoir sampling algorithm is used which is suitable for high memory constraint or when O(`n_samples`) ~ O(`n_population`). The order of the selected integers is undefined. If a random order is desired, the selected subset should be shuffled.\
\
If method == “pool”, a pool based algorithm is particularly fast, even faster than the tracking selection method. However, a vector containing the entire population has to be initialized. If n\_samples ~ n\_population, the reservoir sampling method is faster.\
\
Returns:\
\
**out**ndarray of shape (n\_samples,)\
\
The sampled subsets of integer. The subset of selected integer might not be randomized, see the method argument.\
\
Examples\
\
\>>> from sklearn.utils.random import sample\_without\_replacement\
\>>> sample\_without\_replacement(10, 5, random\_state\=42)\
array(\[8, 1, 5, 0, 7\])\
\
Copy to clipboard\
\
On this page\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)