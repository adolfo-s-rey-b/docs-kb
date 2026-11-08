[Skip to main content](https://scikit-learn.org/stable/auto_examples/applications/plot_wikipedia_principal_eigenvector.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/applications/plot_wikipedia_principal_eigenvector.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/applications/plot_wikipedia_principal_eigenvector.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/applications/plot_wikipedia_principal_eigenvector.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/applications/plot_wikipedia_principal_eigenvector.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/applications/plot_wikipedia_principal_eigenvector.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/applications/plot_wikipedia_principal_eigenvector.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/applications/plot_wikipedia_principal_eigenvector.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/applications/plot_wikipedia_principal_eigenvector.html#sphx-glr-download-auto-examples-applications-plot-wikipedia-principal-eigenvector-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Wikipedia principal eigenvector[#](https://scikit-learn.org/stable/auto_examples/applications/plot_wikipedia_principal_eigenvector.html#wikipedia-principal-eigenvector "Link to this heading")

================================================================================================================================================================================================

A classical way to assert the relative importance of vertices in a graph is to compute the principal eigenvector of the adjacency matrix so as to assign to each vertex the values of the components of the first eigenvector as a centrality score: [https://en.wikipedia.org/wiki/Eigenvector\_centrality](https://en.wikipedia.org/wiki/Eigenvector_centrality)
. On the graph of webpages and links those values are called the PageRank scores by Google.

The goal of this example is to analyze the graph of links inside wikipedia articles to rank articles by relative importance according to this eigenvector centrality.

The traditional way to compute the principal eigenvector is to use the [power iteration method](https://en.wikipedia.org/wiki/Power_iteration)
. Here the computation is achieved thanks to Martinsson’s Randomized SVD algorithm implemented in scikit-learn.

The graph data is fetched from the DBpedia dumps. DBpedia is an extraction of the latent structured data of the Wikipedia content.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

from bz2 import [BZ2File](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File")
from datetime import datetime
from pprint import [pprint](https://docs.python.org/3/library/pprint.html#pprint.pprint "pprint.pprint")
from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

import matplotlib.pyplot as plt
import numpy as np
from scipy import sparse

from sklearn.datasets import [fetch\_file](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_file.html#sklearn.datasets.fetch_file "sklearn.datasets.fetch_file")
from sklearn.decomposition import randomized\_svd

Copy to clipboard

Download data[#](https://scikit-learn.org/stable/auto_examples/applications/plot_wikipedia_principal_eigenvector.html#download-data "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

redirects\_url \= "https://downloads.dbpedia.org/3.5.1/en/redirects\_en.nt.bz2"
redirects\_filename \= [fetch\_file](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_file.html#sklearn.datasets.fetch_file "sklearn.datasets.fetch_file")
(redirects\_url)

page\_links\_url \= "https://downloads.dbpedia.org/3.5.1/en/page\_links\_en.nt.bz2"
page\_links\_filename \= [fetch\_file](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_file.html#sklearn.datasets.fetch_file "sklearn.datasets.fetch_file")
(page\_links\_url)

resources \= \[\
    (redirects\_url, redirects\_filename),\
    (page\_links\_url, page\_links\_filename),\
\]

Copy to clipboard

Loading the redirect files[#](https://scikit-learn.org/stable/auto_examples/applications/plot_wikipedia_principal_eigenvector.html#loading-the-redirect-files "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def index(redirects, index\_map, k):
    """Find the index of an article name after redirect resolution"""
    k \= redirects.get(k, k)
    return index\_map.setdefault(k, len(index\_map))

DBPEDIA\_RESOURCE\_PREFIX\_LEN \= len("http://dbpedia.org/resource/")
SHORTNAME\_SLICE \= slice(DBPEDIA\_RESOURCE\_PREFIX\_LEN + 1, \-1)

def short\_name(nt\_uri):
    """Remove the < and > URI markers and the common URI prefix"""
    return nt\_uri\[SHORTNAME\_SLICE\]

def get\_redirects(redirects\_filename):
    """Parse the redirections and build a transitively closed map out of it"""
    redirects \= {}
    print("Parsing the NT redirect file")
    for l, line in enumerate([BZ2File](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File")
(redirects\_filename)):
        split \= line.split()
        if len(split) != 4:
            print("ignoring malformed line: " + line)
            continue
        redirects\[short\_name(split\[0\])\] \= short\_name(split\[2\])
        if l % 1000000 \== 0:
            print("\[%s\] line: %08d" % ([datetime.now](https://docs.python.org/3/library/datetime.html#datetime.datetime.now "datetime.datetime.now")
().isoformat(), l))

    \# compute the transitive closure
    print("Computing the transitive closure of the redirect relation")
    for l, source in enumerate(redirects.keys()):
        transitive\_target \= None
        target \= redirects\[source\]
        seen \= {source}
        while True:
            transitive\_target \= target
            target \= redirects.get(target)
            if target is None or target in seen:
                break
            seen.add(target)
        redirects\[source\] \= transitive\_target
        if l % 1000000 \== 0:
            print("\[%s\] line: %08d" % ([datetime.now](https://docs.python.org/3/library/datetime.html#datetime.datetime.now "datetime.datetime.now")
().isoformat(), l))

    return redirects

Copy to clipboard

Computing the Adjacency matrix[#](https://scikit-learn.org/stable/auto_examples/applications/plot_wikipedia_principal_eigenvector.html#computing-the-adjacency-matrix "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def get\_adjacency\_matrix(redirects\_filename, page\_links\_filename, limit\=None):
    """Extract the adjacency graph as a scipy sparse matrix

    Redirects are resolved first.

    Returns X, the scipy sparse adjacency matrix, redirects as python
    dict from article names to article names and index\_map a python dict
    from article names to python int (article indexes).
    """

    print("Computing the redirect map")
    redirects \= get\_redirects(redirects\_filename)

    print("Computing the integer index map")
    index\_map \= dict()
    links \= list()
    for l, line in enumerate([BZ2File](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File")
(page\_links\_filename)):
        split \= line.split()
        if len(split) != 4:
            print("ignoring malformed line: " + line)
            continue
        i \= index(redirects, index\_map, short\_name(split\[0\]))
        j \= index(redirects, index\_map, short\_name(split\[2\]))
        links.append((i, j))
        if l % 1000000 \== 0:
            print("\[%s\] line: %08d" % ([datetime.now](https://docs.python.org/3/library/datetime.html#datetime.datetime.now "datetime.datetime.now")
().isoformat(), l))

        if limit is not None and l \>= limit \- 1:
            break

    print("Computing the adjacency matrix")
    X \= [sparse.lil\_array](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.lil_array.html#scipy.sparse.lil_array "scipy.sparse.lil_array")
((len(index\_map), len(index\_map)), dtype\=[np.float32](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32 "numpy.float32")
)
    for i, j in links:
        X\[i, j\] \= 1.0
    del links
    print("Converting to CSR representation")
    X \= X.tocsr()
    print("CSR conversion done")
    return X, redirects, index\_map

\# stop after 5M links to make it possible to work in RAM
X, redirects, index\_map \= get\_adjacency\_matrix(
    redirects\_filename, page\_links\_filename, limit\=5000000
)
names \= {i: name for name, i in index\_map.items()}

Copy to clipboard

Computing the redirect map
Parsing the NT redirect file
\[2026-09-11T13:38:09.420787\] line: 00000000
\[2026-09-11T13:38:15.513390\] line: 01000000
\[2026-09-11T13:38:22.841021\] line: 02000000
\[2026-09-11T13:38:31.037932\] line: 03000000
\[2026-09-11T13:38:37.907727\] line: 04000000
Computing the transitive closure of the redirect relation
\[2026-09-11T13:38:38.542045\] line: 00000000
\[2026-09-11T13:38:39.203074\] line: 01000000
\[2026-09-11T13:38:39.892104\] line: 02000000
\[2026-09-11T13:38:40.673841\] line: 03000000
\[2026-09-11T13:38:41.446233\] line: 04000000
Computing the integer index map
\[2026-09-11T13:38:41.519283\] line: 00000000
\[2026-09-11T13:38:48.348952\] line: 01000000
\[2026-09-11T13:38:55.746327\] line: 02000000
\[2026-09-11T13:39:03.543486\] line: 03000000
\[2026-09-11T13:39:11.092418\] line: 04000000
Computing the adjacency matrix
Converting to CSR representation
CSR conversion done

Copy to clipboard

Computing Principal Singular Vector using Randomized SVD[#](https://scikit-learn.org/stable/auto_examples/applications/plot_wikipedia_principal_eigenvector.html#computing-principal-singular-vector-using-randomized-svd "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Computing the principal singular vectors using randomized\_svd")
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
U, s, V \= randomized\_svd(X, 5, n\_iter\=3)
print("done in %0.3fs" % ([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0))

\# print the names of the wikipedia related strongest components of the
\# principal singular vector which should be similar to the highest eigenvector
print("Top wikipedia pages according to principal singular vectors")
[pprint](https://docs.python.org/3/library/pprint.html#pprint.pprint "pprint.pprint")
(\[names\[i\] for i in np.abs(U.T\[0\]).argsort()\[\-10:\]\])
[pprint](https://docs.python.org/3/library/pprint.html#pprint.pprint "pprint.pprint")
(\[names\[i\] for i in np.abs(V\[0\]).argsort()\[\-10:\]\])

Copy to clipboard

Computing the principal singular vectors using randomized\_svd
done in 4.420s
Top wikipedia pages according to principal singular vectors
\[b'1989',\
 b'1971',\
 b'1975',\
 b'1970',\
 b'2006',\
 b'1972',\
 b'1996',\
 b'1966',\
 b'1967',\
 b'2007'\]
\[b'Soviet\_Union',\
 b'Spain',\
 b'Italy',\
 b'Canada',\
 b'Japan',\
 b'Germany',\
 b'World\_War\_II',\
 b'France',\
 b'United\_Kingdom',\
 b'United\_States'\]

Copy to clipboard

Computing Centrality scores[#](https://scikit-learn.org/stable/auto_examples/applications/plot_wikipedia_principal_eigenvector.html#computing-centrality-scores "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def centrality\_scores(X, alpha\=0.85, max\_iter\=100, tol\=1e-10):
    """Power iteration computation of the principal eigenvector

    This method is also known as Google PageRank and the implementation
    is based on the one from the NetworkX project (BSD licensed too)
    with copyrights by:

      Aric Hagberg <hagberg@lanl.gov>
      Dan Schult <dschult@colgate.edu>
      Pieter Swart <swart@lanl.gov>
    """
    n \= X.shape\[0\]
    X \= X.copy()
    incoming\_counts \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
(X.sum(axis\=1)).ravel()

    print("Normalizing the graph")
    for i in incoming\_counts.nonzero()\[0\]:
        X.data\[X.indptr\[i\] : X.indptr\[i + 1\]\] \*= 1.0 / incoming\_counts\[i\]
    dangle \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
([np.where](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where "numpy.where")
([np.isclose](https://numpy.org/doc/stable/reference/generated/numpy.isclose.html#numpy.isclose "numpy.isclose")
(X.sum(axis\=1), 0), 1.0 / n, 0)).ravel()

    scores \= [np.full](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")
(n, 1.0 / n, dtype\=[np.float32](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32 "numpy.float32")
)  \# initial guess
    errors \= \[\]
    for i in range(max\_iter):
        print("power iteration #%d" % i)
        prev\_scores \= scores
        scores \= (
            alpha \* (scores @ X + dangle @ prev\_scores)
            + (1 \- alpha) \* prev\_scores.sum() / n
        )
        \# check convergence: normalized l\_inf norm
        scores\_max \= np.abs(scores).max()
        if scores\_max \== 0.0:
            scores\_max \= 1.0
        err \= np.abs(scores \- prev\_scores).max() / scores\_max
        errors.append(err)
        print("error: %0.6f" % err)
        if err < n \* tol:
            break

    return scores, [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
(errors)

print("Computing principal eigenvector score using a power iteration method")
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
scores, errors \= centrality\_scores(X, max\_iter\=100)
print("done in %0.3fs" % ([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0))
top\_abs\_score\_indices \= np.abs(scores).argsort()\[\-5:\]
[pprint](https://docs.python.org/3/library/pprint.html#pprint.pprint "pprint.pprint")
(\[names\[i\] for i in top\_abs\_score\_indices\])

Copy to clipboard

Computing principal eigenvector score using a power iteration method
Normalizing the graph
power iteration #0
error: 0.988448
power iteration #1
error: 0.495767
power iteration #2
error: 0.304177
power iteration #3
error: 0.206610
power iteration #4
error: 0.149243
power iteration #5
error: 0.112218
power iteration #6
error: 0.086735
power iteration #7
error: 0.068370
power iteration #8
error: 0.054681
power iteration #9
error: 0.044216
power iteration #10
error: 0.036059
power iteration #11
error: 0.029603
power iteration #12
error: 0.024433
power iteration #13
error: 0.020252
power iteration #14
error: 0.016845
power iteration #15
error: 0.014051
power iteration #16
error: 0.011748
power iteration #17
error: 0.009841
power iteration #18
error: 0.008257
power iteration #19
error: 0.006937
power iteration #20
error: 0.005834
power iteration #21
error: 0.004912
power iteration #22
error: 0.004138
power iteration #23
error: 0.003489
power iteration #24
error: 0.002943
power iteration #25
error: 0.002484
power iteration #26
error: 0.002097
power iteration #27
error: 0.001771
power iteration #28
error: 0.001496
power iteration #29
error: 0.001264
power iteration #30
error: 0.001068
power iteration #31
error: 0.000903
power iteration #32
error: 0.000763
power iteration #33
error: 0.000645
power iteration #34
error: 0.000546
power iteration #35
error: 0.000461
power iteration #36
error: 0.000390
power iteration #37
error: 0.000330
power iteration #38
error: 0.000279
power iteration #39
error: 0.000236
power iteration #40
error: 0.000200
power iteration #41
error: 0.000169
power iteration #42
error: 0.000143
power iteration #43
error: 0.000121
power iteration #44
error: 0.000102
done in 1.978s
\[b'Byzantine\_Empire',\
 b'New\_York\_City',\
 b'World\_War\_I',\
 b'France',\
 b'United\_States'\]

Copy to clipboard

Plot results[#](https://scikit-learn.org/stable/auto_examples/applications/plot_wikipedia_principal_eigenvector.html#plot-results "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
ax.semilogy(range(1, len(errors) + 1), errors)
ax.set\_xlabel("power iteration")
ax.set\_ylabel("convergence error (normalized $\\\\ell\_\\\\infty$)")
ax.set\_title("PageRank power-iteration convergence")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![PageRank power-iteration convergence](https://scikit-learn.org/stable/_images/sphx_glr_plot_wikipedia_principal_eigenvector_001.png)

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
ax.barh(\[names\[i\] for i in top\_abs\_score\_indices\], scores\[top\_abs\_score\_indices\])
ax.set\_xlabel("PageRank score")
ax.set\_title("Wikipedia pages with the highest eigenvector centrality")
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Wikipedia pages with the highest eigenvector centrality](https://scikit-learn.org/stable/_images/sphx_glr_plot_wikipedia_principal_eigenvector_002.png)

**Total running time of the script:** (1 minutes 31.649 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_wikipedia_principal_eigenvector.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_wikipedia_principal_eigenvector.ipynb)

[`Download Jupyter notebook: plot_wikipedia_principal_eigenvector.ipynb`](https://scikit-learn.org/stable/_downloads/fff9b030c0dbb092a4bc9f4d59ef31bb/plot_wikipedia_principal_eigenvector.ipynb)

[`Download Python source code: plot_wikipedia_principal_eigenvector.py`](https://scikit-learn.org/stable/_downloads/78fb9a4d4bbe2bed981ceb216f254cb8/plot_wikipedia_principal_eigenvector.py)

[`Download zipped: plot_wikipedia_principal_eigenvector.zip`](https://scikit-learn.org/stable/_downloads/e675dea5e1e62cf48ab62015e38bb1f5/plot_wikipedia_principal_eigenvector.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tomography_l1_reconstruction_thumb.png)

[Compressive sensing: tomography reconstruction with L1 prior (Lasso)](https://scikit-learn.org/stable/auto_examples/applications/plot_tomography_l1_reconstruction.html)

Compressive sensing: tomography reconstruction with L1 prior (Lasso)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_iris_thumb.png)

[Principal Component Analysis (PCA) on Iris Dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html)

Principal Component Analysis (PCA) on Iris Dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_segmentation_thumb.png)

[Segmenting the picture of greek coins in regions](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_segmentation.html)

Segmenting the picture of greek coins in regions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scoring_monitor_thumb.png)

[Analysis of the convergence of penalized logistic regression models](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html)

Analysis of the convergence of penalized logistic regression models

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/78fb9a4d4bbe2bed981ceb216f254cb8/plot_wikipedia_principal_eigenvector.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/fff9b030c0dbb092a4bc9f4d59ef31bb/plot_wikipedia_principal_eigenvector.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/e675dea5e1e62cf48ab62015e38bb1f5/plot_wikipedia_principal_eigenvector.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_wikipedia_principal_eigenvector.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_wikipedia_principal_eigenvector.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)