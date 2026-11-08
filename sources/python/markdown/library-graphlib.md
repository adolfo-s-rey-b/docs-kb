### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/numeric.html "Numeric and Mathematical Modules")
     |
*   [previous](https://docs.python.org/3/library/enum.html "enum — Support for enumerations")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Data Types](https://docs.python.org/3/library/datatypes.html)
     »
*   [`graphlib` — Functionality to operate with graph-like structures](https://docs.python.org/3/library/graphlib.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`graphlib` — Functionality to operate with graph-like structures[¶](https://docs.python.org/3/library/graphlib.html#module-graphlib "Link to this heading")

============================================================================================================================================================

**Source code:** [Lib/graphlib.py](https://github.com/python/cpython/tree/3.15/Lib/graphlib.py)

* * *

class graphlib.TopologicalSorter(_graph\=None_)[¶](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter "Link to this definition")

Provides functionality to topologically sort a graph of [hashable](https://docs.python.org/3/glossary.html#term-hashable)
 nodes.

A topological order is a linear ordering of the vertices in a graph such that for every directed edge u -> v from vertex u to vertex v, vertex u comes before vertex v in the ordering. For instance, the vertices of the graph may represent tasks to be performed, and the edges may represent constraints that one task must be performed before another; in this example, a topological ordering is just a valid sequence for the tasks. A complete topological ordering is possible if and only if the graph has no directed cycles, that is, if it is a directed acyclic graph.

If the optional _graph_ argument is provided it must be a dictionary representing a directed acyclic graph where the keys are nodes and the values are iterables of all predecessors of that node in the graph (the nodes that have edges that point to the value in the key). Additional nodes can be added to the graph using the [`add()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.add "graphlib.TopologicalSorter.add")
 method.

In the general case, the steps required to perform the sorting of a given graph are as follows:

*   Create an instance of the `TopologicalSorter` with an optional initial graph.
    
*   Add additional nodes to the graph.
    
*   Call [`prepare()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.prepare "graphlib.TopologicalSorter.prepare")
     on the graph.
    
*   While [`is_active()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.is_active "graphlib.TopologicalSorter.is_active")
     is `True`, iterate over the nodes returned by [`get_ready()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.get_ready "graphlib.TopologicalSorter.get_ready")
     and process them. Call [`done()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.done "graphlib.TopologicalSorter.done")
     on each node as it finishes processing.
    

In case just an immediate sorting of the nodes in the graph is required and no parallelism is involved, the convenience method [`TopologicalSorter.static_order()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.static_order "graphlib.TopologicalSorter.static_order")
 can be used directly:

Copy

\>>> graph \= {"D": {"B", "C"}, "C": {"A"}, "B": {"A"}}
\>>> ts \= TopologicalSorter(graph)
\>>> tuple(ts.static\_order())
('A', 'C', 'B', 'D')

The class is designed to easily support parallel processing of the nodes as they become ready. For instance:

Copy

topological\_sorter \= TopologicalSorter()

\# Add nodes to 'topological\_sorter'...

topological\_sorter.prepare()
while topological\_sorter.is\_active():
    for node in topological\_sorter.get\_ready():
        \# Worker threads or processes take nodes to work on off the
        \# 'task\_queue' queue.
        task\_queue.put(node)

    \# When the work for a node is done, workers put the node in
    \# 'finalized\_tasks\_queue' so we can get more nodes to work on.
    \# The definition of 'is\_active()' guarantees that, at this point, at
    \# least one node has been placed on 'task\_queue' that hasn't yet
    \# been passed to 'done()', so this blocking 'get()' must (eventually)
    \# succeed.  After calling 'done()', we loop back to call 'get\_ready()'
    \# again, so put newly freed nodes on 'task\_queue' as soon as
    \# logically possible.
    node \= finalized\_tasks\_queue.get()
    topological\_sorter.done(node)

add(_node_, _\*predecessors_)[¶](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.add "Link to this definition")

Add a new node and its predecessors to the graph. Both the _node_ and all elements in _predecessors_ must be [hashable](https://docs.python.org/3/glossary.html#term-hashable)
.

If called multiple times with the same node argument, the set of dependencies will be the union of all dependencies passed in.

It is possible to add a node with no dependencies (_predecessors_ is not provided) or to provide a dependency twice. If a node that has not been provided before is included among _predecessors_ it will be automatically added to the graph with no predecessors of its own.

Raises [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 if called after [`prepare()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.prepare "graphlib.TopologicalSorter.prepare")
.

prepare()[¶](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.prepare "Link to this definition")

Mark the graph as finished and check for cycles in the graph. If any cycle is detected, [`CycleError`](https://docs.python.org/3/library/graphlib.html#graphlib.CycleError "graphlib.CycleError")
 will be raised, but [`get_ready()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.get_ready "graphlib.TopologicalSorter.get_ready")
 can still be used to obtain as many nodes as possible until cycles block more progress. After a call to this function, the graph cannot be modified, and therefore no more nodes can be added using [`add()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.add "graphlib.TopologicalSorter.add")
.

A [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 will be raised if the sort has been started by [`static_order()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.static_order "graphlib.TopologicalSorter.static_order")
 or [`get_ready()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.get_ready "graphlib.TopologicalSorter.get_ready")
.

Changed in version 3.14: `prepare()` can now be called more than once as long as the sort has not started. Previously this raised [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
.

is\_active()[¶](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.is_active "Link to this definition")

Returns `True` if more progress can be made and `False` otherwise. Progress can be made if cycles do not block the resolution and either there are still nodes ready that haven’t yet been returned by [`TopologicalSorter.get_ready()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.get_ready "graphlib.TopologicalSorter.get_ready")
 or the number of nodes marked [`TopologicalSorter.done()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.done "graphlib.TopologicalSorter.done")
 is less than the number that have been returned by `TopologicalSorter.get_ready()`.

The [`__bool__()`](https://docs.python.org/3/reference/datamodel.html#object.__bool__ "object.__bool__")
 method of this class defers to this function, so instead of:

Copy

if ts.is\_active():
    ...

it is possible to simply do:

Copy

if ts:
    ...

Raises [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 if called without calling [`prepare()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.prepare "graphlib.TopologicalSorter.prepare")
 previously.

done(_\*nodes_)[¶](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.done "Link to this definition")

Marks a set of nodes returned by [`TopologicalSorter.get_ready()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.get_ready "graphlib.TopologicalSorter.get_ready")
 as processed, unblocking any successor of each node in _nodes_ for being returned in the future by a call to `TopologicalSorter.get_ready()`.

Raises [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 if any node in _nodes_ has already been marked as processed by a previous call to this method or if a node was not added to the graph by using [`TopologicalSorter.add()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.add "graphlib.TopologicalSorter.add")
, if called without calling [`prepare()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.prepare "graphlib.TopologicalSorter.prepare")
 or if node has not yet been returned by [`get_ready()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.get_ready "graphlib.TopologicalSorter.get_ready")
.

get\_ready()[¶](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.get_ready "Link to this definition")

Returns a `tuple` with all the nodes that are ready. Initially it returns all nodes with no predecessors, and once those are marked as processed by calling [`TopologicalSorter.done()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.done "graphlib.TopologicalSorter.done")
, further calls will return all new nodes that have all their predecessors already processed. Once no more progress can be made, empty tuples are returned.

Raises [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 if called without calling [`prepare()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.prepare "graphlib.TopologicalSorter.prepare")
 previously.

static\_order()[¶](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.static_order "Link to this definition")

Returns an iterator object which will iterate over nodes in a topological order. When using this method, [`prepare()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.prepare "graphlib.TopologicalSorter.prepare")
 and [`done()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.done "graphlib.TopologicalSorter.done")
 should not be called. This method is equivalent to:

Copy

def static\_order(self):
    self.prepare()
    while self.is\_active():
        node\_group \= self.get\_ready()
        yield from node\_group
        self.done(\*node\_group)

The particular order that is returned may depend on the specific order in which the items were inserted in the graph. For example:

Copy

\>>> ts \= TopologicalSorter()
\>>> ts.add(3, 2, 1)
\>>> ts.add(1, 0)
\>>> print(\[\*ts.static\_order()\])
\[2, 0, 1, 3\]

\>>> ts2 \= TopologicalSorter()
\>>> ts2.add(1, 0)
\>>> ts2.add(3, 2, 1)
\>>> print(\[\*ts2.static\_order()\])
\[0, 2, 1, 3\]

This is due to the fact that “0” and “2” are in the same level in the graph (they would have been returned in the same call to [`get_ready()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.get_ready "graphlib.TopologicalSorter.get_ready")
) and the order between them is determined by the order of insertion.

If any cycle is detected, [`CycleError`](https://docs.python.org/3/library/graphlib.html#graphlib.CycleError "graphlib.CycleError")
 will be raised.

Added in version 3.9.

Exceptions[¶](https://docs.python.org/3/library/graphlib.html#exceptions "Link to this heading")

-------------------------------------------------------------------------------------------------

The `graphlib` module defines the following exception classes:

exception graphlib.CycleError[¶](https://docs.python.org/3/library/graphlib.html#graphlib.CycleError "Link to this definition")

Subclass of [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 raised by [`TopologicalSorter.prepare()`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter.prepare "graphlib.TopologicalSorter.prepare")
 if cycles exist in the working graph. If multiple cycles exist, only one undefined choice among them will be reported and included in the exception.

The detected cycle can be accessed via the second element in the [`args`](https://docs.python.org/3/builtins/exceptions.html#BaseException.args "BaseException.args")
 attribute of the exception instance and consists in a list of nodes, such that each node is, in the graph, an immediate predecessor of the next node in the list. In the reported list, the first and the last node will be the same, to make it clear that it is cyclic.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`graphlib` — Functionality to operate with graph-like structures](https://docs.python.org/3/library/graphlib.html#)
    *   [Exceptions](https://docs.python.org/3/library/graphlib.html#exceptions)
        

#### Previous topic

[`enum` — Support for enumerations](https://docs.python.org/3/library/enum.html "previous chapter")

#### Next topic

[Numeric and Mathematical Modules](https://docs.python.org/3/library/numeric.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=graphlib+%E2%80%94+Functionality+to+operate+with+graph-like+structures&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fgraphlib.html&pagesource=library%2Fgraphlib.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/graphlib.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/numeric.html "Numeric and Mathematical Modules")
     |
*   [previous](https://docs.python.org/3/library/enum.html "enum — Support for enumerations")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Data Types](https://docs.python.org/3/library/datatypes.html)
     »
*   [`graphlib` — Functionality to operate with graph-like structures](https://docs.python.org/3/library/graphlib.html)
    
*    
    
    |
*   Theme Auto Light Dark |