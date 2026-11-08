[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.decomposition.dict_learning.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.decomposition.dict_learning.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.decomposition.dict_learning.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.decomposition.dict_learning.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.decomposition.dict_learning.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.decomposition.dict_learning.html)

Collapse Sidebar Expand Sidebar

dict\_learning[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning.html#dict-learning "Link to this heading")

===================================================================================================================================================

sklearn.decomposition.dict\_learning(_X_, _n\_components_, _\*_, _alpha_, _max\_iter\=100_, _tol\=1e-08_, _method\='lars'_, _n\_jobs\=None_, _dict\_init\=None_, _code\_init\=None_, _callback\=None_, _verbose\=False_, _random\_state\=None_, _return\_n\_iter\=False_, _positive\_dict\=False_, _positive\_code\=False_, _method\_max\_iter\=1000_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/decomposition/_dict_learning.py#L883)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning.html#sklearn.decomposition.dict_learning "Link to this definition")

Solve a dictionary learning matrix factorization problem.

Finds the best dictionary and the corresponding sparse code for approximating the data matrix X by solving:

(U^\*, V^\*) \= argmin 0.5 || X \- U V ||\_Fro^2 + alpha \* || U ||\_1,1
             (U,V)
            with || V\_k ||\_2 \= 1 for all  0 <= k < n\_components

Copy to clipboard

where V is the dictionary and U is the sparse code. ||.||\_Fro stands for the Frobenius norm and ||.||\_1,1 stands for the entry-wise matrix norm which is the sum of the absolute values of all the entries in the matrix.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/decomposition.html#dictionarylearning)
.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Data matrix.

**n\_components**int

Number of dictionary atoms to extract.

**alpha**int or float

Sparsity controlling parameter.

**max\_iter**int, default=100

Maximum number of iterations to perform.

**tol**float, default=1e-8

Tolerance for the stopping condition.

**method**{‘lars’, ‘cd’}, default=’lars’

The method used:

*   `'lars'`: uses the least angle regression method to solve the lasso
    
    problem (`linear_model.lars_path`);
    
*   `'cd'`: uses the coordinate descent method to compute the Lasso solution (`linear_model.Lasso`). Lars will be faster if the estimated components are sparse.
    

**n\_jobs**int, default=None

Number of parallel jobs to run. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**dict\_init**ndarray of shape (n\_components, n\_features), default=None

Initial value for the dictionary for warm restart scenarios. Only used if `code_init` and `dict_init` are not None.

**code\_init**ndarray of shape (n\_samples, n\_components), default=None

Initial value for the sparse code for warm restart scenarios. Only used if `code_init` and `dict_init` are not None.

**callback**callable, default=None

Callable that gets invoked every five iterations.

**verbose**bool, default=False

To control the verbosity of the procedure.

**random\_state**int, RandomState instance or None, default=None

Used for randomly initializing the dictionary. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**return\_n\_iter**bool, default=False

Whether or not to return the number of iterations.

**positive\_dict**bool, default=False

Whether to enforce positivity when finding the dictionary.

Added in version 0.20.

**positive\_code**bool, default=False

Whether to enforce positivity when finding the code.

Added in version 0.20.

**method\_max\_iter**int, default=1000

Maximum number of iterations to perform.

Added in version 0.22.

Returns:

**code**ndarray of shape (n\_samples, n\_components)

The sparse code factor in the matrix factorization.

**dictionary**ndarray of shape (n\_components, n\_features),

The dictionary factor in the matrix factorization.

**errors**array

Vector of errors at each iteration.

**n\_iter**int

Number of iterations run. Returned only if `return_n_iter` is set to True.

See also

[`dict_learning_online`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning_online.html#sklearn.decomposition.dict_learning_online "sklearn.decomposition.dict_learning_online")

Solve a dictionary learning matrix factorization problem online.

[`DictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "sklearn.decomposition.DictionaryLearning")

Find a dictionary that sparsely encodes data.

[`MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")

A faster, less accurate version of the dictionary learning algorithm.

[`SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")

Sparse Principal Components Analysis.

[`MiniBatchSparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "sklearn.decomposition.MiniBatchSparsePCA")

Mini-batch Sparse Principal Components Analysis.

Examples

\>>> import numpy as np
\>>> from sklearn.datasets import make\_sparse\_coded\_signal
\>>> from sklearn.decomposition import dict\_learning
\>>> X, \_, \_ \= make\_sparse\_coded\_signal(
...     n\_samples\=30, n\_components\=15, n\_features\=20, n\_nonzero\_coefs\=10,
...     random\_state\=42,
... )
\>>> U, V, errors \= dict\_learning(X, n\_components\=15, alpha\=0.1, random\_state\=42)

Copy to clipboard

We can check the level of sparsity of `U`:

\>>> np.mean(U \== 0)
np.float64(0.62)

Copy to clipboard

We can compare the average squared euclidean norm of the reconstruction error of the sparse coded signal relative to the squared euclidean norm of the original signal:

\>>> X\_hat \= U @ V
\>>> np.mean(np.sum((X\_hat \- X) \*\* 2, axis\=1) / np.sum(X \*\* 2, axis\=1))
np.float64(0.0192)

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)