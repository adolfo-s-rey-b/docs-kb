[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.haversine_distances.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.pairwise.haversine_distances.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.haversine_distances.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.pairwise.haversine_distances.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.pairwise.haversine_distances.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.pairwise.haversine_distances.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.pairwise.haversine_distances.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.pairwise.haversine_distances.html)

Collapse Sidebar Expand Sidebar

haversine\_distances[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.haversine_distances.html#haversine-distances "Link to this heading")

========================================================================================================================================================================

sklearn.metrics.pairwise.haversine\_distances(_X_, _Y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/pairwise.py#L990)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.haversine_distances.html#sklearn.metrics.pairwise.haversine_distances "Link to this definition")

Compute the Haversine distance between samples in X and Y.

The Haversine (or great circle) distance is the angular distance between two points on the surface of a sphere. The first coordinate of each point is assumed to be the latitude, the second is the longitude, given in radians. The dimension of the data must be 2.

D(x,y)\=2arcsin⁡\[sin2⁡((xlat−ylat)/2)+cos⁡(xlat)cos⁡(ylat) sin2((xlon−ylon)/2)\]

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples\_X, 2)

A feature array.

**Y**{array-like, sparse matrix} of shape (n\_samples\_Y, 2), default=None

An optional second feature array. If `None`, uses `Y=X`.

Returns:

**distances**ndarray of shape (n\_samples\_X, n\_samples\_Y)

The distance matrix.

Notes

As the Earth is nearly spherical, the haversine formula provides a good approximation of the distance between two points of the Earth surface, with a less than 1% error on average.

Examples

We want to calculate the distance between the Ezeiza Airport (Buenos Aires, Argentina) and the Charles de Gaulle Airport (Paris, France).

\>>> from sklearn.metrics.pairwise import haversine\_distances
\>>> from math import radians
\>>> bsas \= \[\-34.83333, \-58.5166646\]
\>>> paris \= \[49.0083899664, 2.53844117956\]
\>>> bsas\_in\_radians \= \[radians(\_) for \_ in bsas\]
\>>> paris\_in\_radians \= \[radians(\_) for \_ in paris\]
\>>> result \= haversine\_distances(\[bsas\_in\_radians, paris\_in\_radians\])
\>>> result \* 6371000/1000  \# multiply by Earth radius to get kilometers
array(\[\[    0.        , 11099.54035582\],\
       \[11099.54035582,     0.        \]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)