### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/array.html "array — Efficient arrays of numeric values")
     |
*   [previous](https://docs.python.org/3/library/heapq.html "heapq — Heap queue algorithm")
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
*   [`bisect` — Array bisection algorithm](https://docs.python.org/3/library/bisect.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`bisect` — Array bisection algorithm[¶](https://docs.python.org/3/library/bisect.html#module-bisect "Link to this heading")

============================================================================================================================

**Source code:** [Lib/bisect.py](https://github.com/python/cpython/tree/3.15/Lib/bisect.py)

* * *

This module provides support for maintaining a list in sorted order without having to sort the list after each insertion. For long lists of items with expensive comparison operations, this can be an improvement over linear searches or frequent resorting.

The module is called `bisect` because it uses a basic bisection algorithm to do its work. Unlike other bisection tools that search for a specific value, the functions in this module are designed to locate an insertion point. Accordingly, the functions never call an [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__")
 method to determine whether a value has been found. Instead, the functions only call the [`__lt__()`](https://docs.python.org/3/reference/datamodel.html#object.__lt__ "object.__lt__")
 method and will return an insertion point between values in an array.

Note

The functions in this module are not thread-safe. If multiple threads concurrently use `bisect` functions on the same sequence, this may result in undefined behaviour. Likewise, if the provided sequence is mutated by a different thread while a `bisect` function is operating on it, the result is undefined. For example, using [`insort_left()`](https://docs.python.org/3/library/bisect.html#bisect.insort_left "bisect.insort_left")
 on the same list from multiple threads may result in the list becoming unsorted.

The following functions are provided:

bisect.bisect\_left(_a_, _x_, _lo\=0_, _hi\=len(a)_, _\*_, _key\=None_)[¶](https://docs.python.org/3/library/bisect.html#bisect.bisect_left "Link to this definition")

Locate the insertion point for _x_ in _a_ to maintain sorted order. The parameters _lo_ and _hi_ may be used to specify a subset of the list which should be considered; by default the entire list is used. If _x_ is already present in _a_, the insertion point will be before (to the left of) any existing entries. The return value is suitable for use as the first parameter to `list.insert()` assuming that _a_ is already sorted.

The returned insertion point _ip_ partitions the array _a_ into two slices such that `all(elem < x for elem in a[lo : ip])` is true for the left slice and `all(elem >= x for elem in a[ip : hi])` is true for the right slice.

_key_ specifies a [key function](https://docs.python.org/3/glossary.html#term-key-function)
 of one argument that is used to extract a comparison key from each element in the array. To support searching complex records, the key function is not applied to the _x_ value.

If _key_ is `None`, the elements are compared directly and no key function is called.

Changed in version 3.10: Added the _key_ parameter.

bisect.bisect\_right(_a_, _x_, _lo\=0_, _hi\=len(a)_, _\*_, _key\=None_)[¶](https://docs.python.org/3/library/bisect.html#bisect.bisect_right "Link to this definition")

bisect.bisect(_a_, _x_, _lo\=0_, _hi\=len(a)_, _\*_, _key\=None_)[¶](https://docs.python.org/3/library/bisect.html#bisect.bisect "Link to this definition")

Similar to [`bisect_left()`](https://docs.python.org/3/library/bisect.html#bisect.bisect_left "bisect.bisect_left")
, but returns an insertion point which comes after (to the right of) any existing entries of _x_ in _a_.

The returned insertion point _ip_ partitions the array _a_ into two slices such that `all(elem <= x for elem in a[lo : ip])` is true for the left slice and `all(elem > x for elem in a[ip : hi])` is true for the right slice.

Changed in version 3.10: Added the _key_ parameter.

bisect.insort\_left(_a_, _x_, _lo\=0_, _hi\=len(a)_, _\*_, _key\=None_)[¶](https://docs.python.org/3/library/bisect.html#bisect.insort_left "Link to this definition")

Insert _x_ in _a_ in sorted order.

This function first runs [`bisect_left()`](https://docs.python.org/3/library/bisect.html#bisect.bisect_left "bisect.bisect_left")
 to locate an insertion point. Next, it runs the [`insert()`](https://docs.python.org/3/builtins/stdtypes.html#sequence.insert "sequence.insert")
 method on _a_ to insert _x_ at the appropriate position to maintain sort order.

To support inserting records in a table, the _key_ function (if any) is applied to _x_ for the search step but not for the insertion step.

Keep in mind that the _O_(log _n_) search is dominated by the slow _O_(_n_) insertion step.

Changed in version 3.10: Added the _key_ parameter.

bisect.insort\_right(_a_, _x_, _lo\=0_, _hi\=len(a)_, _\*_, _key\=None_)[¶](https://docs.python.org/3/library/bisect.html#bisect.insort_right "Link to this definition")

bisect.insort(_a_, _x_, _lo\=0_, _hi\=len(a)_, _\*_, _key\=None_)[¶](https://docs.python.org/3/library/bisect.html#bisect.insort "Link to this definition")

Similar to [`insort_left()`](https://docs.python.org/3/library/bisect.html#bisect.insort_left "bisect.insort_left")
, but inserting _x_ in _a_ after any existing entries of _x_.

This function first runs [`bisect_right()`](https://docs.python.org/3/library/bisect.html#bisect.bisect_right "bisect.bisect_right")
 to locate an insertion point. Next, it runs the [`insert()`](https://docs.python.org/3/builtins/stdtypes.html#sequence.insert "sequence.insert")
 method on _a_ to insert _x_ at the appropriate position to maintain sort order.

To support inserting records in a table, the _key_ function (if any) is applied to _x_ for the search step but not for the insertion step.

Keep in mind that the _O_(log _n_) search is dominated by the slow _O_(_n_) insertion step.

Changed in version 3.10: Added the _key_ parameter.

Performance Notes[¶](https://docs.python.org/3/library/bisect.html#performance-notes "Link to this heading")

-------------------------------------------------------------------------------------------------------------

When writing time sensitive code using _bisect()_ and _insort()_, keep these thoughts in mind:

*   Bisection is effective for searching ranges of values. For locating specific values, dictionaries are more performant.
    
*   The _insort()_ functions are _O_(_n_) because the logarithmic search step is dominated by the linear time insertion step.
    
*   The search functions are stateless and discard key function results after they are used. Consequently, if the search functions are used in a loop, the key function may be called again and again on the same array elements. If the key function isn’t fast, consider wrapping it with [`@functools.cache`](https://docs.python.org/3/library/functools.html#functools.cache "functools.cache")
     to avoid duplicate computations. Alternatively, consider searching an array of precomputed keys to locate the insertion point (as shown in the examples section below).
    

See also

*   [Sorted Collections](https://grantjenks.com/docs/sortedcollections/)
     is a high performance module that uses _bisect_ to managed sorted collections of data.
    
*   The [SortedCollection recipe](https://code.activestate.com/recipes/577197-sortedcollection/)
     uses bisect to build a full-featured collection class with straight-forward search methods and support for a key-function. The keys are precomputed to save unnecessary calls to the key function during searches.
    

Searching Sorted Lists[¶](https://docs.python.org/3/library/bisect.html#searching-sorted-lists "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

The above [bisect functions](https://docs.python.org/3/library/bisect.html#bisect-functions)
 are useful for finding insertion points but can be tricky or awkward to use for common searching tasks. The following five functions show how to transform them into the standard lookups for sorted lists:

Copy

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i \= bisect\_left(a, x)
    if i != len(a) and a\[i\] \== x:
        return i
    raise ValueError

def find\_lt(a, x):
    'Find rightmost value less than x'
    i \= bisect\_left(a, x)
    if i:
        return a\[i\-1\]
    raise ValueError

def find\_le(a, x):
    'Find rightmost value less than or equal to x'
    i \= bisect\_right(a, x)
    if i:
        return a\[i\-1\]
    raise ValueError

def find\_gt(a, x):
    'Find leftmost value greater than x'
    i \= bisect\_right(a, x)
    if i != len(a):
        return a\[i\]
    raise ValueError

def find\_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i \= bisect\_left(a, x)
    if i != len(a):
        return a\[i\]
    raise ValueError

Examples[¶](https://docs.python.org/3/library/bisect.html#examples "Link to this heading")

-------------------------------------------------------------------------------------------

The [`bisect()`](https://docs.python.org/3/library/bisect.html#bisect.bisect "bisect.bisect")
 function can be useful for numeric table lookups. This example uses `bisect()` to look up a letter grade for an exam score (say) based on a set of ordered numeric breakpoints: 90 and up is an ‘A’, 80 to 89 is a ‘B’, and so on:

Copy

\>>> def grade(score):
...     i \= bisect(\[60, 70, 80, 90\], score)
...     return "FDCBA"\[i\]
...
\>>> \[grade(score) for score in \[33, 99, 77, 70, 89, 90, 100\]\]
\['F', 'A', 'C', 'C', 'B', 'A', 'A'\]

The [`bisect()`](https://docs.python.org/3/library/bisect.html#bisect.bisect "bisect.bisect")
 and [`insort()`](https://docs.python.org/3/library/bisect.html#bisect.insort "bisect.insort")
 functions also work with lists of tuples. The _key_ argument can serve to extract the field used for ordering records in a table:

Copy

\>>> from collections import namedtuple
\>>> from operator import attrgetter
\>>> from bisect import bisect, insort
\>>> from pprint import pprint

\>>> Movie \= namedtuple('Movie', ('name', 'released', 'director'))

\>>> movies \= \[\
...     Movie('Jaws', 1975, 'Spielberg'),\
...     Movie('Titanic', 1997, 'Cameron'),\
...     Movie('The Birds', 1963, 'Hitchcock'),\
...     Movie('Aliens', 1986, 'Cameron')\
... \]

\>>> \# Find the first movie released after 1960
\>>> by\_year \= attrgetter('released')
\>>> movies.sort(key\=by\_year)
\>>> movies\[bisect(movies, 1960, key\=by\_year)\]
Movie(name='The Birds', released=1963, director='Hitchcock')

\>>> \# Insert a movie while maintaining sort order
\>>> romance \= Movie('Love Story', 1970, 'Hiller')
\>>> insort(movies, romance, key\=by\_year)
\>>> pprint(movies)
\[Movie(name='The Birds', released=1963, director='Hitchcock'),\
 Movie(name='Love Story', released=1970, director='Hiller'),\
 Movie(name='Jaws', released=1975, director='Spielberg'),\
 Movie(name='Aliens', released=1986, director='Cameron'),\
 Movie(name='Titanic', released=1997, director='Cameron')\]

If the key function is expensive, it is possible to avoid repeated function calls by searching a list of precomputed keys to find the index of a record:

Copy

\>>> data \= \[('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)\]
\>>> data.sort(key\=lambda r: r\[1\])       \# Or use operator.itemgetter(1).
\>>> keys \= \[r\[1\] for r in data\]         \# Precompute a list of keys.
\>>> data\[bisect\_left(keys, 0)\]
('black', 0)
\>>> data\[bisect\_left(keys, 1)\]
('blue', 1)
\>>> data\[bisect\_left(keys, 5)\]
('red', 5)
\>>> data\[bisect\_left(keys, 8)\]
('yellow', 8)

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`bisect` — Array bisection algorithm](https://docs.python.org/3/library/bisect.html#)
    *   [Performance Notes](https://docs.python.org/3/library/bisect.html#performance-notes)
        
    *   [Searching Sorted Lists](https://docs.python.org/3/library/bisect.html#searching-sorted-lists)
        
    *   [Examples](https://docs.python.org/3/library/bisect.html#examples)
        

#### Previous topic

[`heapq` — Heap queue algorithm](https://docs.python.org/3/library/heapq.html "previous chapter")

#### Next topic

[`array` — Efficient arrays of numeric values](https://docs.python.org/3/library/array.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=bisect+%E2%80%94+Array+bisection+algorithm&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fbisect.html&pagesource=library%2Fbisect.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/bisect.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/array.html "array — Efficient arrays of numeric values")
     |
*   [previous](https://docs.python.org/3/library/heapq.html "heapq — Heap queue algorithm")
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
*   [`bisect` — Array bisection algorithm](https://docs.python.org/3/library/bisect.html)
    
*    
    
    |
*   Theme Auto Light Dark |