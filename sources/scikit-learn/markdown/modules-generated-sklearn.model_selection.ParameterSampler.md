[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterSampler.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.ParameterSampler.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterSampler.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.ParameterSampler.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.ParameterSampler.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.ParameterSampler.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.ParameterSampler.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.ParameterSampler.html)

Collapse Sidebar Expand Sidebar

ParameterSampler[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterSampler.html#parametersampler "Link to this heading")

=============================================================================================================================================================

class sklearn.model\_selection.ParameterSampler(_param\_distributions_, _n\_iter_, _\*_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_search.py#L223)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterSampler.html#sklearn.model_selection.ParameterSampler "Link to this definition")

Generator on parameters sampled from given distributions.

Non-deterministic iterable over random candidate combinations for hyper- parameter search. If all parameters are presented as a list, sampling without replacement is performed. If at least one parameter is given as a distribution, sampling with replacement is used. It is highly recommended to use continuous distributions for continuous parameters.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/grid_search.html#grid-search)
.

Parameters:

**param\_distributions**dict

Dictionary with parameter names (`str`) as keys and distributions or lists of parameters to try. Distributions must provide a `rvs` method for sampling (such as those from scipy.stats.distributions). If a list is given, it is sampled uniformly. If a list of dicts is given, first a dict is sampled uniformly, and then a parameter is sampled using that dict as above.

**n\_iter**int

Number of parameter settings that are produced.

**random\_state**int, RandomState instance or None, default=None

Pseudo random number generator state used for random uniform sampling from lists of possible values instead of scipy.stats distributions. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Returns:

**params**dict of str to any

**Yields** dictionaries mapping each estimator parameter to as sampled value.

Examples

\>>> from sklearn.model\_selection import ParameterSampler
\>>> from scipy.stats.distributions import expon
\>>> import numpy as np
\>>> rng \= np.random.RandomState(0)
\>>> param\_grid \= {'a':\[1, 2\], 'b': expon()}
\>>> param\_list \= list(ParameterSampler(param\_grid, n\_iter\=4,
...                                    random\_state\=rng))
\>>> rounded\_list \= \[dict((k, round(v, 6)) for (k, v) in d.items())\
...                 for d in param\_list\]
\>>> rounded\_list \== \[{'b': 0.89856, 'a': 1},\
...                  {'b': 0.923223, 'a': 1},\
...                  {'b': 1.878964, 'a': 2},\
...                  {'b': 1.038159, 'a': 2}\]
True

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)