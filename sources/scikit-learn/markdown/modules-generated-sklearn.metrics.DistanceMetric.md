[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.DistanceMetric.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.DistanceMetric.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.DistanceMetric.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.DistanceMetric.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.DistanceMetric.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.DistanceMetric.html)

Collapse Sidebar Expand Sidebar

DistanceMetric[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html#distancemetric "Link to this heading")

===============================================================================================================================================

class sklearn.metrics.DistanceMetric[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html#sklearn.metrics.DistanceMetric "Link to this definition")

Uniform interface for fast distance metric functions.

The `DistanceMetric` class provides a convenient way to compute pairwise distances between samples. It supports various distance metrics, such as Euclidean distance, Manhattan distance, and more.

The `pairwise` method can be used to compute pairwise distances between samples in the input arrays. It returns a distance matrix representing the distances between all pairs of samples.

The [`get_metric`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html#sklearn.metrics.DistanceMetric.get_metric "sklearn.metrics.DistanceMetric.get_metric")
 method allows you to retrieve a specific metric using its string identifier.

Examples

\>>> from sklearn.metrics import DistanceMetric
\>>> dist \= DistanceMetric.get\_metric('euclidean')
\>>> X \= \[\[1, 2\], \[3, 4\], \[5, 6\]\]
\>>> Y \= \[\[7, 8\], \[9, 10\]\]
\>>> dist.pairwise(X,Y)
array(\[\[7.81..., 10.63...\]\
       \[5.65...,  8.48...\]\
       \[1.41...,  4.24...\]\])

Copy to clipboard

Available Metrics

The following lists the string metric identifiers and the associated distance metric classes:

**Metrics intended for real-valued vector spaces:**

|     |     |     |     |
| --- | --- | --- | --- |
| identifier | class name | args | distance function |
| “euclidean” | EuclideanDistance |     | `sqrt(sum((x - y)^2))` |
| “manhattan” | ManhattanDistance |     | `sum(\|x - y\|)` |
| “chebyshev” | ChebyshevDistance |     | `max(\|x - y\|)` |
| “minkowski” | MinkowskiDistance | p, w | `sum(w * \|x - y\|^p)^(1/p)` |
| “seuclidean” | SEuclideanDistance | V   | `sqrt(sum((x - y)^2 / V))` |
| “mahalanobis” | MahalanobisDistance | V or VI | `sqrt((x - y)' V^-1 (x - y))` |

**Metrics intended for two-dimensional vector spaces:** Note that the haversine distance metric requires data in the form of \[latitude, longitude\] and both inputs and outputs are in units of radians.

|     |     |     |
| --- | --- | --- |
| identifier | class name | distance function |
| “haversine” | HaversineDistance | `2 arcsin(sqrt(sin^2(0.5*dx) + cos(x1)cos(x2)sin^2(0.5*dy)))` |

**Metrics intended for integer-valued vector spaces:** Though intended for integer-valued vectors, these are also valid metrics in the case of real-valued vectors.

|     |     |     |
| --- | --- | --- |
| identifier | class name | distance function |
| “hamming” | HammingDistance | `N_unequal(x, y) / N_tot` |
| “canberra” | CanberraDistance | `sum(\|x - y\| / (\|x\| + \|y\|))` |
| “braycurtis” | BrayCurtisDistance | `sum(\|x - y\|) / (sum(\|x\|) + sum(\|y\|))` |

**Metrics intended for boolean-valued vector spaces:** Any nonzero entry is evaluated to “True”. In the listings below, the following abbreviations are used:

*   N: number of dimensions
    
*   NTT: number of dims in which both values are True
    
*   NTF: number of dims in which the first value is True, second is False
    
*   NFT: number of dims in which the first value is False, second is True
    
*   NFF: number of dims in which both values are False
    
*   NNEQ: number of non-equal dimensions, NNEQ = NTF + NFT
    
*   NNZ: number of nonzero dimensions, NNZ = NTF + NFT + NTT
    

|     |     |     |
| --- | --- | --- |
| identifier | class name | distance function |
| “jaccard” | JaccardDistance | NNEQ / NNZ |
| “matching” | MatchingDistance | NNEQ / N |
| “dice” | DiceDistance | NNEQ / (NTT + NNZ) |
| “kulsinski” | KulsinskiDistance | (NNEQ + N - NTT) / (NNEQ + N) |
| “rogerstanimoto” | RogersTanimotoDistance | 2 \* NNEQ / (N + NNEQ) |
| “russellrao” | RussellRaoDistance | (N - NTT) / N |
| “sokalmichener” | SokalMichenerDistance | 2 \* NNEQ / (N + NNEQ) |
| “sokalsneath” | SokalSneathDistance | NNEQ / (NNEQ + 0.5 \* NTT) |

**User-defined distance:**

|     |     |     |
| --- | --- | --- |
| identifier | class name | args |
| “pyfunc” | PyFuncDistance | func |

Here `func` is a function which takes two one-dimensional numpy arrays, and returns a distance. Note that in order to be used within the BallTree, the distance must be a true metric: i.e. it must satisfy the following properties

1.  Non-negativity: d(x, y) >= 0
    
2.  Identity: d(x, y) = 0 if and only if x == y
    
3.  Symmetry: d(x, y) = d(y, x)
    
4.  Triangle Inequality: d(x, y) + d(y, z) >= d(x, z)
    

Because of the Python object overhead involved in calling the python function, this will be fairly slow, but it will have the same scaling as other distances.

classmethod get\_metric(_metric_, _dtype\=<class 'numpy.float64'>_, _\*\*kwargs_)[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html#sklearn.metrics.DistanceMetric.get_metric "Link to this definition")

Get the given distance metric from the string identifier.

See the docstring of DistanceMetric for a list of available metrics.

Parameters:

**metric**str or class name

The string identifier or class name of the desired distance metric. See the documentation of the `DistanceMetric` class for a list of available metrics.

**dtype**{np.float32, np.float64}, default=np.float64

The data type of the input on which the metric will be applied. This affects the precision of the computed distances. By default, it is set to `np.float64`.

**\*\*kwargs**

Additional keyword arguments that will be passed to the requested metric. These arguments can be used to customize the behavior of the specific metric.

Returns:

**metric\_obj**instance of the requested metric

An instance of the requested distance metric class.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)