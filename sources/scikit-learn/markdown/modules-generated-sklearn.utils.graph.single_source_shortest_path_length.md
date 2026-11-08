[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.graph.single_source_shortest_path_length.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.graph.single_source_shortest_path_length.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.graph.single_source_shortest_path_length.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.graph.single_source_shortest_path_length.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.graph.single_source_shortest_path_length.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.graph.single_source_shortest_path_length.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.graph.single_source_shortest_path_length.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.graph.single_source_shortest_path_length.html)

Collapse Sidebar Expand Sidebar

single\_source\_shortest\_path\_length[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.graph.single_source_shortest_path_length.html#single-source-shortest-path-length "Link to this heading")

===================================================================================================================================================================================================================

sklearn.utils.graph.single\_source\_shortest\_path\_length(_graph_, _source_, _\*_, _cutoff\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/graph.py#L16)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.graph.single_source_shortest_path_length.html#sklearn.utils.graph.single_source_shortest_path_length "Link to this definition")

Return the length of the shortest path from source to all reachable nodes.

Parameters:

**graph**{array-like, sparse matrix} of shape (n\_nodes, n\_nodes)

Adjacency matrix of the graph. Sparse matrix of format LIL is preferred.

**source**int

Start node for path.

**cutoff**int, default=None

Depth to stop the search - only paths of length <= cutoff are returned.

Returns:

**paths**dict

Reachable end nodes mapped to length of path from source, i.e. `{end: path_length}`.

Examples

\>>> from sklearn.utils.graph import single\_source\_shortest\_path\_length
\>>> import numpy as np
\>>> graph \= np.array(\[\[ 0, 1, 0, 0\],\
...                   \[ 1, 0, 1, 0\],\
...                   \[ 0, 1, 0, 0\],\
...                   \[ 0, 0, 0, 0\]\])
\>>> single\_source\_shortest\_path\_length(graph, 0)
{0: 0, 1: 1, 2: 2}
\>>> graph \= np.ones((6, 6))
\>>> sorted(single\_source\_shortest\_path\_length(graph, 2).items())
\[(0, 1), (1, 1), (2, 0), (3, 1), (4, 1), (5, 1)\]

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)