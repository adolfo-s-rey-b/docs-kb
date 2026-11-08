[Skip to main content](https://scikit-learn.org/stable/auto_examples/applications/plot_stock_market.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/applications/plot_stock_market.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/applications/plot_stock_market.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/applications/plot_stock_market.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/applications/plot_stock_market.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/applications/plot_stock_market.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/applications/plot_stock_market.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/applications/plot_stock_market.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/applications/plot_stock_market.html#sphx-glr-download-auto-examples-applications-plot-stock-market-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Visualizing the stock market structure[#](https://scikit-learn.org/stable/auto_examples/applications/plot_stock_market.html#visualizing-the-stock-market-structure "Link to this heading")

===========================================================================================================================================================================================

This example employs several unsupervised learning techniques to extract the stock market structure from variations in historical quotes.

The quantity that we use is the daily variation in quote price: quotes that are linked tend to fluctuate in relation to each other during a day.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Retrieve the data from Internet[#](https://scikit-learn.org/stable/auto_examples/applications/plot_stock_market.html#retrieve-the-data-from-internet "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The data is from 2003 - 2008. This is reasonably calm: not too long ago so that we get high-tech firms, and before the 2008 crash. This kind of historical data can be obtained from APIs like the [data.nasdaq.com](https://data.nasdaq.com/)
 and [alphavantage.co](https://www.alphavantage.co/)
.

import sys

import numpy as np
import pandas as pd

symbol\_dict \= {
    "TOT": "Total",
    "XOM": "Exxon",
    "CVX": "Chevron",
    "COP": "ConocoPhillips",
    "VLO": "Valero Energy",
    "MSFT": "Microsoft",
    "IBM": "IBM",
    "TWX": "Time Warner",
    "CMCSA": "Comcast",
    "CVC": "Cablevision",
    "YHOO": "Yahoo",
    "DELL": "Dell",
    "HPQ": "HP",
    "AMZN": "Amazon",
    "TM": "Toyota",
    "CAJ": "Canon",
    "SNE": "Sony",
    "F": "Ford",
    "HMC": "Honda",
    "NAV": "Navistar",
    "NOC": "Northrop Grumman",
    "BA": "Boeing",
    "KO": "Coca Cola",
    "MMM": "3M",
    "MCD": "McDonald's",
    "PEP": "Pepsi",
    "K": "Kellogg",
    "UN": "Unilever",
    "MAR": "Marriott",
    "PG": "Procter Gamble",
    "CL": "Colgate-Palmolive",
    "GE": "General Electrics",
    "WFC": "Wells Fargo",
    "JPM": "JPMorgan Chase",
    "AIG": "AIG",
    "AXP": "American express",
    "BAC": "Bank of America",
    "GS": "Goldman Sachs",
    "AAPL": "Apple",
    "SAP": "SAP",
    "CSCO": "Cisco",
    "TXN": "Texas Instruments",
    "XRX": "Xerox",
    "WMT": "Wal-Mart",
    "HD": "Home Depot",
    "GSK": "GlaxoSmithKline",
    "PFE": "Pfizer",
    "SNY": "Sanofi-Aventis",
    "NVS": "Novartis",
    "KMB": "Kimberly-Clark",
    "R": "Ryder",
    "GD": "General Dynamics",
    "RTN": "Raytheon",
    "CVS": "CVS",
    "CAT": "Caterpillar",
    "DD": "DuPont de Nemours",
}

symbols, names \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(sorted(symbol\_dict.items())).T

quotes \= \[\]

for symbol in symbols:
    print("Fetching quote history for %r" % symbol, file\=[sys.stderr](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")
)
    url \= (
        "https://raw.githubusercontent.com/scikit-learn/examples-data/"
        "master/financial-data/{}.csv"
    )
    quotes.append([pd.read\_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")
(url.format(symbol)))

close\_prices \= [np.vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
(\[q\["close"\] for q in quotes\])
open\_prices \= [np.vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
(\[q\["open"\] for q in quotes\])

\# The daily variations of the quotes are what carry the most information
variation \= close\_prices \- open\_prices

Copy to clipboard

Fetching quote history for np.str\_('AAPL')
Fetching quote history for np.str\_('AIG')
Fetching quote history for np.str\_('AMZN')
Fetching quote history for np.str\_('AXP')
Fetching quote history for np.str\_('BA')
Fetching quote history for np.str\_('BAC')
Fetching quote history for np.str\_('CAJ')
Fetching quote history for np.str\_('CAT')
Fetching quote history for np.str\_('CL')
Fetching quote history for np.str\_('CMCSA')
Fetching quote history for np.str\_('COP')
Fetching quote history for np.str\_('CSCO')
Fetching quote history for np.str\_('CVC')
Fetching quote history for np.str\_('CVS')
Fetching quote history for np.str\_('CVX')
Fetching quote history for np.str\_('DD')
Fetching quote history for np.str\_('DELL')
Fetching quote history for np.str\_('F')
Fetching quote history for np.str\_('GD')
Fetching quote history for np.str\_('GE')
Fetching quote history for np.str\_('GS')
Fetching quote history for np.str\_('GSK')
Fetching quote history for np.str\_('HD')
Fetching quote history for np.str\_('HMC')
Fetching quote history for np.str\_('HPQ')
Fetching quote history for np.str\_('IBM')
Fetching quote history for np.str\_('JPM')
Fetching quote history for np.str\_('K')
Fetching quote history for np.str\_('KMB')
Fetching quote history for np.str\_('KO')
Fetching quote history for np.str\_('MAR')
Fetching quote history for np.str\_('MCD')
Fetching quote history for np.str\_('MMM')
Fetching quote history for np.str\_('MSFT')
Fetching quote history for np.str\_('NAV')
Fetching quote history for np.str\_('NOC')
Fetching quote history for np.str\_('NVS')
Fetching quote history for np.str\_('PEP')
Fetching quote history for np.str\_('PFE')
Fetching quote history for np.str\_('PG')
Fetching quote history for np.str\_('R')
Fetching quote history for np.str\_('RTN')
Fetching quote history for np.str\_('SAP')
Fetching quote history for np.str\_('SNE')
Fetching quote history for np.str\_('SNY')
Fetching quote history for np.str\_('TM')
Fetching quote history for np.str\_('TOT')
Fetching quote history for np.str\_('TWX')
Fetching quote history for np.str\_('TXN')
Fetching quote history for np.str\_('UN')
Fetching quote history for np.str\_('VLO')
Fetching quote history for np.str\_('WFC')
Fetching quote history for np.str\_('WMT')
Fetching quote history for np.str\_('XOM')
Fetching quote history for np.str\_('XRX')
Fetching quote history for np.str\_('YHOO')

Copy to clipboard

Learning a graph structure[#](https://scikit-learn.org/stable/auto_examples/applications/plot_stock_market.html#learning-a-graph-structure "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

We use sparse inverse covariance estimation to find which quotes are correlated conditionally on the others. Specifically, sparse inverse covariance gives us a graph, that is a list of connections. For each symbol, the symbols that it is connected to are those useful to explain its fluctuations.

from sklearn import covariance

alphas \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-1.5, 1, num\=10)
edge\_model \= [covariance.GraphicalLassoCV](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV "sklearn.covariance.GraphicalLassoCV")
(alphas\=alphas)

\# standardize the time series: using correlations rather than covariance
\# former is more efficient for structure recovery
X \= variation.copy().T
X /= X.std(axis\=0)
edge\_model.fit(X)

Copy to clipboard

GraphicalLassoCV(alphas=array(\[ 0.03162278,  0.05994843,  0.11364637,  0.21544347,  0.40842387,\
        0.77426368,  1.46779927,  2.7825594 ,  5.27499706, 10.        \]))

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

GraphicalLassoCV

[?Documentation for GraphicalLassoCV](https://scikit-learn.org/1.9/modules/generated/sklearn.covariance.GraphicalLassoCV.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [alphas alphas: int or array-like of shape (n\_alphas,), dtype=float, default=4  <br>  <br>If an integer is given, it fixes the number of points on the  <br>grids of alpha to be used. If a list is given, it gives the  <br>grid to be used. See the notes in the class docstring for  <br>more details. Range is \[1, inf) for an integer.  <br>Range is (0, inf\] for an array-like of floats.](https://scikit-learn.org/1.9/modules/generated/sklearn.covariance.GraphicalLassoCV.html#:~:text=alphas,-int%20or%20array-like%20of%20shape%20%28n_alphas%2C%29%2C%20dtype%3Dfloat%2C%20default%3D4) | array(\[ 0.031... 10. \]) |
|     | [n\_refinements n\_refinements: int, default=4  <br>  <br>The number of times the grid is refined. Not used if explicit  <br>values of alphas are passed. Range is \[1, inf).](https://scikit-learn.org/1.9/modules/generated/sklearn.covariance.GraphicalLassoCV.html#:~:text=n_refinements,-int%2C%20default%3D4) | 4   |\
|     | [cv cv: int, cross-validation generator or iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the default 5-fold cross-validation,  <br>\- integer, to specify the number of folds,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs :class:\`~sklearn.model\_selection.KFold\` is used.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.  <br>  <br>.. versionchanged:: 0.20  <br>\`\`cv\`\` default value if None changed from 3-fold to 5-fold.](https://scikit-learn.org/1.9/modules/generated/sklearn.covariance.GraphicalLassoCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20iterable%2C%20default%3DNone) | None |\
|     | [tol tol: float, default=1e-4  <br>  <br>The tolerance to declare convergence: if the dual gap goes below  <br>this value, iterations are stopped. Range is (0, inf\].](https://scikit-learn.org/1.9/modules/generated/sklearn.covariance.GraphicalLassoCV.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001 |
|     | [enet\_tol enet\_tol: float, default=1e-4  <br>  <br>The tolerance for the elastic net solver used to calculate the descent  <br>direction. This parameter controls the accuracy of the search direction  <br>for a given column update, not of the overall parameter estimate. Only  <br>used for mode='cd'. Range is (0, inf\].](https://scikit-learn.org/1.9/modules/generated/sklearn.covariance.GraphicalLassoCV.html#:~:text=enet_tol,-float%2C%20default%3D1e-4) | 0.0001 |
|     | [max\_iter max\_iter: int, default=100  <br>  <br>Maximum number of iterations.](https://scikit-learn.org/1.9/modules/generated/sklearn.covariance.GraphicalLassoCV.html#:~:text=max_iter,-int%2C%20default%3D100) | 100 |
|     | [mode mode: {'cd', 'lars'}, default='cd'  <br>  <br>The Lasso solver to use: coordinate descent or LARS. Use LARS for  <br>very sparse underlying graphs, where number of features is greater  <br>than number of samples. Elsewhere prefer cd which is more numerically  <br>stable.](https://scikit-learn.org/1.9/modules/generated/sklearn.covariance.GraphicalLassoCV.html#:~:text=mode,-%7B%27cd%27%2C%20%27lars%27%7D%2C%20default%3D%27cd%27) | 'cd' |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.  <br>  <br>.. versionchanged:: v0.20  <br>\`n\_jobs\` default changed from 1 to None](https://scikit-learn.org/1.9/modules/generated/sklearn.covariance.GraphicalLassoCV.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If verbose is True, the objective function and duality gap are  <br>printed at each iteration.](https://scikit-learn.org/1.9/modules/generated/sklearn.covariance.GraphicalLassoCV.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |
|     | [eps eps: float, default=eps  <br>  <br>The machine-precision regularization in the computation of the  <br>Cholesky diagonal factors. Increase this for very ill-conditioned  <br>systems. Default is \`np.finfo(np.float64).eps\`.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.covariance.GraphicalLassoCV.html#:~:text=eps,-float%2C%20default%3Deps) | np.float64(2....049250313e-16) |
|     | [assume\_centered assume\_centered: bool, default=False  <br>  <br>If True, data are not centered before computation.  <br>Useful when working with data whose mean is almost, but not exactly  <br>zero.  <br>If False, data are centered before computation.](https://scikit-learn.org/1.9/modules/generated/sklearn.covariance.GraphicalLassoCV.html#:~:text=assume_centered,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [alpha\_ alpha\_: float  <br>  <br>Penalization parameter selected.](https://scikit-learn.org/1.9/modules/generated/sklearn.covariance.GraphicalLassoCV.html#:~:text=alpha_,-float) | float64 | 0.05995 |
| [costs\_ costs\_: list of (objective, dual\_gap) pairs  <br>  <br>The list of values of the objective function and the dual gap at  <br>each iteration. Returned only if return\_costs is True.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.covariance.GraphicalLassoCV.html#:~:text=costs_,-list%20of%20%28objective%2C%20dual_gap%29%20pairs) | list | \[(np.float64(inf), np.float64(-2...5374945193858)), (np.float64(242.72241991721066), np.float64(0....7211362260404)), (np.float64(242.72169173955422), np.float64(0....5270814104613)), (np.float64(242.72171542675326), np.float64(0....4492626584087)), ...\] |
| [covariance\_ covariance\_: ndarray of shape (n\_features, n\_features)  <br>  <br>Estimated covariance matrix.](https://scikit-learn.org/1.9/modules/generated/sklearn.covariance.GraphicalLassoCV.html#:~:text=covariance_,-ndarray%20of%20shape%20%28n_features%2C%20n_features%29) | ndarray\[float64\](56, 56) | \[\[1. ,0.22,0.29,...,0.25,0.17,0.22\], \[0.22,1. ,0.23,...,0.27,0.24,0.24\], \[0.29,0.23,1. ,...,0.21,0.21,0.43\], ..., \[0.25,0.27,0.21,...,1. ,0.2 ,0.21\], \[0.17,0.24,0.21,...,0.2 ,1. ,0.23\], \[0.22,0.24,0.43,...,0.21,0.23,1. \]\] |
| [cv\_results\_ cv\_results\_: dict of ndarrays  <br>  <br>A dict with keys:  <br>  <br>alphas : ndarray of shape (n\_alphas,)  <br>All penalization parameters explored.  <br>  <br>split(k)\_test\_score : ndarray of shape (n\_alphas,)  <br>Log-likelihood score on left-out data across (k)th fold.  <br>  <br>.. versionadded:: 1.0  <br>  <br>mean\_test\_score : ndarray of shape (n\_alphas,)  <br>Mean of scores over the folds.  <br>  <br>.. versionadded:: 1.0  <br>  <br>std\_test\_score : ndarray of shape (n\_alphas,)  <br>Standard deviation of scores over the folds.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.covariance.GraphicalLassoCV.html#:~:text=cv_results_,-dict%20of%20ndarrays) | dict | {'alphas': array(\[10. ... 0. \]), 'me...re': array(\[-81.87...-72.17963604\]), 'sp...re': array(\[-85.25...-73.71542769\]), 'sp...re': array(\[-76.71...-67.03463241\]), ...} |
| [location\_ location\_: ndarray of shape (n\_features,)  <br>  <br>Estimated location, i.e. the estimated mean.](https://scikit-learn.org/1.9/modules/generated/sklearn.covariance.GraphicalLassoCV.html#:~:text=location_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](56,) | \[-0.02,-0.02, 0.07,..., 0.04, 0.09,-0. \] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.covariance.GraphicalLassoCV.html#:~:text=n_features_in_,-int) | int | 56  |
| [n\_iter\_ n\_iter\_: int  <br>  <br>Number of iterations run for the optimal alpha.](https://scikit-learn.org/1.9/modules/generated/sklearn.covariance.GraphicalLassoCV.html#:~:text=n_iter_,-int) | int | 12  |
| [precision\_ precision\_: ndarray of shape (n\_features, n\_features)  <br>  <br>Estimated precision matrix (inverse covariance).](https://scikit-learn.org/1.9/modules/generated/sklearn.covariance.GraphicalLassoCV.html#:~:text=precision_,-ndarray%20of%20shape%20%28n_features%2C%20n_features%29) | ndarray\[float64\](56, 56) | \[\[ 1.28,-0. ,-0.17,...,-0.09,-0. ,-0. \], \[-0. , 1.58,-0. ,...,-0. ,-0.02,-0. \], \[-0.17,-0. , 1.38,...,-0. ,-0.04,-0.38\], ..., \[-0.09,-0. ,-0. ,..., 2.44,-0. , 0. \], \[-0. ,-0.02,-0.04,...,-0. , 1.22,-0.06\], \[-0. ,-0. ,-0.38,..., 0. ,-0.06, 1.42\]\] |

  
  

Clustering using affinity propagation[#](https://scikit-learn.org/stable/auto_examples/applications/plot_stock_market.html#clustering-using-affinity-propagation "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We use clustering to group together quotes that behave similarly. Here, amongst the [various clustering techniques](https://scikit-learn.org/stable/modules/clustering.html#clustering)
 available in the scikit-learn, we use [Affinity Propagation](https://scikit-learn.org/stable/modules/clustering.html#affinity-propagation)
 as it does not enforce equal-size clusters, and it can choose automatically the number of clusters from the data.

Note that this gives us a different indication than the graph, as the graph reflects conditional relations between variables, while the clustering reflects marginal properties: variables clustered together can be considered as having a similar impact at the level of the full stock market.

from sklearn import cluster

\_, labels \= [cluster.affinity\_propagation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.affinity_propagation.html#sklearn.cluster.affinity_propagation "sklearn.cluster.affinity_propagation")
(edge\_model.covariance\_, random\_state\=0)
n\_labels \= labels.max()

for i in range(n\_labels + 1):
    print(f"Cluster {i + 1}: {', '.join(names\[labels \== i\])}")

Copy to clipboard

Cluster 1: Apple, Amazon, Yahoo
Cluster 2: Comcast, Cablevision, Time Warner
Cluster 3: ConocoPhillips, Chevron, Total, Valero Energy, Exxon
Cluster 4: Cisco, Dell, HP, IBM, Microsoft, SAP, Texas Instruments
Cluster 5: Boeing, General Dynamics, Northrop Grumman, Raytheon
Cluster 6: AIG, American express, Bank of America, Caterpillar, CVS, DuPont de Nemours, Ford, General Electrics, Goldman Sachs, Home Depot, JPMorgan Chase, Marriott, McDonald's, 3M, Ryder, Wells Fargo, Wal-Mart
Cluster 7: GlaxoSmithKline, Novartis, Pfizer, Sanofi-Aventis, Unilever
Cluster 8: Kellogg, Coca Cola, Pepsi
Cluster 9: Colgate-Palmolive, Kimberly-Clark, Procter Gamble
Cluster 10: Canon, Honda, Navistar, Sony, Toyota, Xerox

Copy to clipboard

Embedding in 2D space[#](https://scikit-learn.org/stable/auto_examples/applications/plot_stock_market.html#embedding-in-2d-space "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

For visualization purposes, we need to lay out the different symbols on a 2D canvas. For this, we use [Manifold learning](https://scikit-learn.org/stable/modules/manifold.html#manifold)
 techniques to retrieve 2D embedding. We use a dense `eigen_solver` to achieve reproducibility (arpack is initiated with the random vectors that we do not control). In addition, we use a large number of neighbors to capture the large-scale structure.

\# Finding a low-dimension embedding for visualization: find the best position of
\# the nodes (the stocks) on a 2D plane

from sklearn import manifold

node\_position\_model \= [manifold.LocallyLinearEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")
(
    n\_components\=2, eigen\_solver\="dense", n\_neighbors\=6
)

embedding \= node\_position\_model.fit\_transform(X.T).T

Copy to clipboard

Visualization[#](https://scikit-learn.org/stable/auto_examples/applications/plot_stock_market.html#visualization "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

The output of the 3 models are combined in a 2D graph where nodes represent the stocks and edges the connections (partial correlations):

*   cluster labels are used to define the color of the nodes
    
*   the sparse covariance model is used to display the strength of the edges
    
*   the 2D embedding is used to position the nodes in the plan
    

This example has a fair amount of visualization-related code, as visualization is crucial here to display the graph. One of the challenges is to position the labels minimizing overlap. For this, we use an heuristic based on the direction of the nearest neighbor along each axis.

import matplotlib.pyplot as plt
from matplotlib.collections import [LineCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(1, facecolor\="w", figsize\=(10, 8))
[plt.clf](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clf.html#matplotlib.pyplot.clf "matplotlib.pyplot.clf")
()
ax \= [plt.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")
(\[0.0, 0.0, 1.0, 1.0\])
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("off")

\# Plot the graph of partial correlations
partial\_correlations \= edge\_model.precision\_.copy()
d \= 1 / [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
([np.diag](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag "numpy.diag")
(partial\_correlations))
partial\_correlations \*= d
partial\_correlations \*= d\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]
non\_zero \= np.abs([np.triu](https://numpy.org/doc/stable/reference/generated/numpy.triu.html#numpy.triu "numpy.triu")
(partial\_correlations, k\=1)) \> 0.02

\# Plot the nodes using the coordinates of our embedding
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    embedding\[0\], embedding\[1\], s\=100 \* d\*\*2, c\=labels, cmap\=plt.cm.nipy\_spectral
)

\# Plot the edges
start\_idx, end\_idx \= non\_zero.nonzero()
\# a sequence of (\*line0\*, \*line1\*, \*line2\*), where::
\#            linen = (x0, y0), (x1, y1), ... (xm, ym)
segments \= \[\
    \[embedding\[:, start\], embedding\[:, stop\]\] for start, stop in zip(start\_idx, end\_idx)\
\]
values \= np.abs(partial\_correlations\[non\_zero\])
lc \= [LineCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
(
    segments, zorder\=0, cmap\=plt.cm.hot\_r, norm\=plt.Normalize(0, 0.7 \* values.max())
)
lc.set\_array(values)
lc.set\_linewidths(15 \* values)
ax.add\_collection(lc)

\# Add a label to each node. The challenge here is that we want to
\# position the labels to avoid overlap with other labels
for index, (name, label, (x, y)) in enumerate(zip(names, labels, embedding.T)):
    dx \= x \- embedding\[0\]
    dx\[index\] \= 1
    dy \= y \- embedding\[1\]
    dy\[index\] \= 1
    this\_dx \= dx\[[np.argmin](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin "numpy.argmin")\
(np.abs(dy))\]
    this\_dy \= dy\[[np.argmin](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin "numpy.argmin")\
(np.abs(dx))\]
    if this\_dx \> 0:
        horizontalalignment \= "left"
        x \= x + 0.002
    else:
        horizontalalignment \= "right"
        x \= x \- 0.002
    if this\_dy \> 0:
        verticalalignment \= "bottom"
        y \= y + 0.002
    else:
        verticalalignment \= "top"
        y \= y \- 0.002
    [plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
(
        x,
        y,
        name,
        size\=10,
        horizontalalignment\=horizontalalignment,
        verticalalignment\=verticalalignment,
        bbox\=dict(
            facecolor\="w",
            edgecolor\=plt.cm.nipy\_spectral(label / float(n\_labels)),
            alpha\=0.6,
        ),
    )

[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(
    embedding\[0\].min() \- 0.15 \* [np.ptp](https://numpy.org/doc/stable/reference/generated/numpy.ptp.html#numpy.ptp "numpy.ptp")
(embedding\[0\]),
    embedding\[0\].max() + 0.10 \* [np.ptp](https://numpy.org/doc/stable/reference/generated/numpy.ptp.html#numpy.ptp "numpy.ptp")
(embedding\[0\]),
)
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(
    embedding\[1\].min() \- 0.03 \* [np.ptp](https://numpy.org/doc/stable/reference/generated/numpy.ptp.html#numpy.ptp "numpy.ptp")
(embedding\[1\]),
    embedding\[1\].max() + 0.03 \* [np.ptp](https://numpy.org/doc/stable/reference/generated/numpy.ptp.html#numpy.ptp "numpy.ptp")
(embedding\[1\]),
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![plot stock market](https://scikit-learn.org/stable/_images/sphx_glr_plot_stock_market_001.png)

**Total running time of the script:** (0 minutes 2.966 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_stock_market.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_stock_market.ipynb)

[`Download Jupyter notebook: plot_stock_market.ipynb`](https://scikit-learn.org/stable/_downloads/2840d928d4f93cd381486b35c2031752/plot_stock_market.ipynb)

[`Download Python source code: plot_stock_market.py`](https://scikit-learn.org/stable/_downloads/70af03f765a8f15d7c1d63e836e68590/plot_stock_market.py)

[`Download zipped: plot_stock_market.zip`](https://scikit-learn.org/stable/_downloads/df96f413a13b9b7958a4a343650cd091/plot_stock_market.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_thumb.png)

[Manifold learning on handwritten digits: Locally Linear Embedding, Isomap…](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html)

Manifold learning on handwritten digits: Locally Linear Embedding, Isomap...

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_methods_thumb.png)

[Comparison of Manifold Learning methods](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html)

Comparison of Manifold Learning methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_linkage_thumb.png)

[Various Agglomerative Clustering on a 2D embedding of digits](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_linkage.html)

Various Agglomerative Clustering on a 2D embedding of digits

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_segmentation_thumb.png)

[Segmenting the picture of greek coins in regions](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_segmentation.html)

Segmenting the picture of greek coins in regions

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/70af03f765a8f15d7c1d63e836e68590/plot_stock_market.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/2840d928d4f93cd381486b35c2031752/plot_stock_market.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/df96f413a13b9b7958a4a343650cd091/plot_stock_market.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_stock_market.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_stock_market.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)