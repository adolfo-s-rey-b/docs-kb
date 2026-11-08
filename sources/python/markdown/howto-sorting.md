### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/howto/unicode.html "Unicode HOWTO")
     |
*   [previous](https://docs.python.org/3/howto/sockets.html "Socket Programming HOWTO")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python HOWTOs](https://docs.python.org/3/howto/index.html)
     »
*   [Sorting Techniques](https://docs.python.org/3/howto/sorting.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Sorting Techniques[¶](https://docs.python.org/3/howto/sorting.html#sorting-techniques "Link to this heading")

==============================================================================================================

Python lists have a built-in [`list.sort()`](https://docs.python.org/3/builtins/stdtypes.html#list.sort "list.sort")
 method that modifies the list in-place. There is also a [`sorted()`](https://docs.python.org/3/builtins/functions.html#sorted "sorted")
 built-in function that builds a new sorted list from an iterable.

In this document, we explore the various techniques for sorting data using Python.

Sorting Basics[¶](https://docs.python.org/3/howto/sorting.html#sorting-basics "Link to this heading")

------------------------------------------------------------------------------------------------------

A simple ascending sort is very easy: just call the [`sorted()`](https://docs.python.org/3/builtins/functions.html#sorted "sorted")
 function. It returns a new sorted list:

Copy

\>>> sorted(\[5, 2, 3, 1, 4\])
\[1, 2, 3, 4, 5\]

You can also use the [`list.sort()`](https://docs.python.org/3/builtins/stdtypes.html#list.sort "list.sort")
 method. It modifies the list in-place (and returns `None` to avoid confusion). Usually it’s less convenient than [`sorted()`](https://docs.python.org/3/builtins/functions.html#sorted "sorted")
 - but if you don’t need the original list, it’s slightly more efficient.

Copy

\>>> a \= \[5, 2, 3, 1, 4\]
\>>> a.sort()
\>>> a
\[1, 2, 3, 4, 5\]

Another difference is that the [`list.sort()`](https://docs.python.org/3/builtins/stdtypes.html#list.sort "list.sort")
 method is only defined for lists. In contrast, the [`sorted()`](https://docs.python.org/3/builtins/functions.html#sorted "sorted")
 function accepts any iterable.

Copy

\>>> sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
\[1, 2, 3, 4, 5\]

Key Functions[¶](https://docs.python.org/3/howto/sorting.html#key-functions "Link to this heading")

----------------------------------------------------------------------------------------------------

The [`list.sort()`](https://docs.python.org/3/builtins/stdtypes.html#list.sort "list.sort")
 method and the functions [`sorted()`](https://docs.python.org/3/builtins/functions.html#sorted "sorted")
, [`min()`](https://docs.python.org/3/builtins/functions.html#min "min")
, [`max()`](https://docs.python.org/3/builtins/functions.html#max "max")
, [`heapq.nsmallest()`](https://docs.python.org/3/library/heapq.html#heapq.nsmallest "heapq.nsmallest")
, and [`heapq.nlargest()`](https://docs.python.org/3/library/heapq.html#heapq.nlargest "heapq.nlargest")
 have a _key_ parameter to specify a function (or other callable) to be called on each list element prior to making comparisons.

For example, here’s a case-insensitive string comparison using [`str.casefold()`](https://docs.python.org/3/builtins/stdtypes.html#str.casefold "str.casefold")
:

Copy

\>>> sorted("This is a test string from Andrew".split(), key\=str.casefold)
\['a', 'Andrew', 'from', 'is', 'string', 'test', 'This'\]

The value of the _key_ parameter should be a function (or other callable) that takes a single argument and returns a key to use for sorting purposes. This technique is fast because the key function is called exactly once for each input record.

A common pattern is to sort complex objects using some of the object’s indices as keys. For example:

Copy

\>>> student\_tuples \= \[\
...     ('john', 'A', 15),\
...     ('jane', 'B', 12),\
...     ('dave', 'B', 10),\
... \]
\>>> sorted(student\_tuples, key\=lambda student: student\[2\])   \# sort by age
\[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)\]

The same technique works for objects with named attributes. For example:

Copy

\>>> class Student:
...     def \_\_init\_\_(self, name, grade, age):
...         self.name \= name
...         self.grade \= grade
...         self.age \= age
...     def \_\_repr\_\_(self):
...         return repr((self.name, self.grade, self.age))

\>>> student\_objects \= \[\
...     Student('john', 'A', 15),\
...     Student('jane', 'B', 12),\
...     Student('dave', 'B', 10),\
... \]
\>>> sorted(student\_objects, key\=lambda student: student.age)   \# sort by age
\[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)\]

Objects with named attributes can be made by a regular class as shown above, or they can be instances of [`dataclass`](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass "dataclasses.dataclass")
 or a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)
.

Operator Module Functions and Partial Function Evaluation[¶](https://docs.python.org/3/howto/sorting.html#operator-module-functions-and-partial-function-evaluation "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [key function](https://docs.python.org/3/glossary.html#term-key-function)
 patterns shown above are very common, so Python provides convenience functions to make accessor functions easier and faster. The [`operator`](https://docs.python.org/3/library/operator.html#module-operator "operator: Functions corresponding to the standard operators.")
 module has [`itemgetter()`](https://docs.python.org/3/library/operator.html#operator.itemgetter "operator.itemgetter")
, [`attrgetter()`](https://docs.python.org/3/library/operator.html#operator.attrgetter "operator.attrgetter")
, and a [`methodcaller()`](https://docs.python.org/3/library/operator.html#operator.methodcaller "operator.methodcaller")
 function.

Using those functions, the above examples become simpler and faster:

Copy

\>>> from operator import itemgetter, attrgetter

\>>> sorted(student\_tuples, key\=itemgetter(2))
\[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)\]

\>>> sorted(student\_objects, key\=attrgetter('age'))
\[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)\]

The operator module functions allow multiple levels of sorting. For example, to sort by _grade_ then by _age_:

Copy

\>>> sorted(student\_tuples, key\=itemgetter(1,2))
\[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)\]

\>>> sorted(student\_objects, key\=attrgetter('grade', 'age'))
\[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)\]

The [`functools`](https://docs.python.org/3/library/functools.html#module-functools "functools: Higher-order functions and operations on callable objects.")
 module provides another helpful tool for making key-functions. The [`partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
 function can reduce the [arity](https://en.wikipedia.org/wiki/Arity)
 of a multi-argument function making it suitable for use as a key-function.

Copy

\>>> from functools import partial
\>>> from unicodedata import normalize

\>>> names \= 'Zoë Åbjørn Núñez Élana Zeke Abe Nubia Eloise'.split()

\>>> sorted(names, key\=partial(normalize, 'NFD'))
\['Abe', 'Åbjørn', 'Eloise', 'Élana', 'Nubia', 'Núñez', 'Zeke', 'Zoë'\]

\>>> sorted(names, key\=partial(normalize, 'NFC'))
\['Abe', 'Eloise', 'Nubia', 'Núñez', 'Zeke', 'Zoë', 'Åbjørn', 'Élana'\]

Ascending and Descending[¶](https://docs.python.org/3/howto/sorting.html#ascending-and-descending "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

Both [`list.sort()`](https://docs.python.org/3/builtins/stdtypes.html#list.sort "list.sort")
 and [`sorted()`](https://docs.python.org/3/builtins/functions.html#sorted "sorted")
 accept a _reverse_ parameter with a boolean value. This is used to flag descending sorts. For example, to get the student data in reverse _age_ order:

Copy

\>>> sorted(student\_tuples, key\=itemgetter(2), reverse\=True)
\[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)\]

\>>> sorted(student\_objects, key\=attrgetter('age'), reverse\=True)
\[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)\]

Sort Stability and Complex Sorts[¶](https://docs.python.org/3/howto/sorting.html#sort-stability-and-complex-sorts "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

Sorts are guaranteed to be [stable](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability)
. That means that when multiple records have the same key, their original order is preserved.

Copy

\>>> data \= \[('red', 1), ('blue', 1), ('red', 2), ('blue', 2)\]
\>>> sorted(data, key\=itemgetter(0))
\[('blue', 1), ('blue', 2), ('red', 1), ('red', 2)\]

Notice how the two records for _blue_ retain their original order so that `('blue', 1)` is guaranteed to precede `('blue', 2)`.

This wonderful property lets you build complex sorts in a series of sorting steps. For example, to sort the student data by descending _grade_ and then ascending _age_, do the _age_ sort first and then sort again using _grade_:

Copy

\>>> s \= sorted(student\_objects, key\=attrgetter('age'))     \# sort on secondary key
\>>> sorted(s, key\=attrgetter('grade'), reverse\=True)       \# now sort on primary key, descending
\[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)\]

This can be abstracted out into a wrapper function that can take a list and tuples of field and order to sort them on multiple passes.

Copy

\>>> def multisort(xs, specs):
...     for key, reverse in reversed(specs):
...         xs.sort(key\=attrgetter(key), reverse\=reverse)
...     return xs

\>>> multisort(list(student\_objects), (('grade', True), ('age', False)))
\[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)\]

The [Timsort](https://en.wikipedia.org/wiki/Timsort)
 algorithm used in Python does multiple sorts efficiently because it can take advantage of any ordering already present in a dataset.

Decorate-Sort-Undecorate[¶](https://docs.python.org/3/howto/sorting.html#decorate-sort-undecorate "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

This idiom is called Decorate-Sort-Undecorate after its three steps:

*   First, the initial list is decorated with new values that control the sort order.
    
*   Second, the decorated list is sorted.
    
*   Finally, the decorations are removed, creating a list that contains only the initial values in the new order.
    

For example, to sort the student data by _grade_ using the DSU approach:

Copy

\>>> decorated \= \[(student.grade, i, student) for i, student in enumerate(student\_objects)\]
\>>> decorated.sort()
\>>> \[student for grade, i, student in decorated\]               \# undecorate
\[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)\]

This idiom works because tuples are compared lexicographically; the first items are compared; if they are the same then the second items are compared, and so on.

It is not strictly necessary in all cases to include the index _i_ in the decorated list, but including it gives two benefits:

*   The sort is stable – if two items have the same key, their order will be preserved in the sorted list.
    
*   The original items do not have to be comparable because the ordering of the decorated tuples will be determined by at most the first two items. So for example the original list could contain complex numbers which cannot be sorted directly.
    

Another name for this idiom is [Schwartzian transform](https://en.wikipedia.org/wiki/Schwartzian_transform)
, after Randal L. Schwartz, who popularized it among Perl programmers.

Now that Python sorting provides key-functions, this technique is not often needed.

Comparison Functions[¶](https://docs.python.org/3/howto/sorting.html#comparison-functions "Link to this heading")

------------------------------------------------------------------------------------------------------------------

Unlike key functions that return an absolute value for sorting, a comparison function computes the relative ordering for two inputs.

For example, a [balance scale](https://upload.wikimedia.org/wikipedia/commons/1/17/Balance_%C3%A0_tabac_1850.JPG)
 compares two samples giving a relative ordering: lighter, equal, or heavier. Likewise, a comparison function such as `cmp(a, b)` will return a negative value for less-than, zero if the inputs are equal, or a positive value for greater-than.

It is common to encounter comparison functions when translating algorithms from other languages. Also, some libraries provide comparison functions as part of their API. For example, [`locale.strcoll()`](https://docs.python.org/3/library/locale.html#locale.strcoll "locale.strcoll")
 is a comparison function.

To accommodate those situations, Python provides [`functools.cmp_to_key`](https://docs.python.org/3/library/functools.html#functools.cmp_to_key "functools.cmp_to_key")
 to wrap the comparison function to make it usable as a key function:

Copy

sorted(words, key\=cmp\_to\_key(strcoll))  \# locale-aware sort order

Strategies For Unorderable Types and Values[¶](https://docs.python.org/3/howto/sorting.html#strategies-for-unorderable-types-and-values "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

A number of type and value issues can arise when sorting. Here are some strategies that can help:

*   Convert non-comparable input types to strings prior to sorting:
    

Copy

\>>> data \= \['twelve', '11', 10\]
\>>> sorted(map(str, data))
\['10', '11', 'twelve'\]

This is needed because most cross-type comparisons raise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
.

*   Remove special values prior to sorting:
    

Copy

\>>> from math import isnan
\>>> from itertools import filterfalse
\>>> data \= \[3.3, float('nan'), 1.1, 2.2\]
\>>> sorted(filterfalse(isnan, data))
\[1.1, 2.2, 3.3\]

This is needed because the [IEEE-754 standard](https://en.wikipedia.org/wiki/IEEE_754)
 specifies that, “Every NaN shall compare unordered with everything, including itself.”

Likewise, `None` can be stripped from datasets as well:

Copy

\>>> data \= \[3.3, None, 1.1, 2.2\]
\>>> sorted(x for x in data if x is not None)
\[1.1, 2.2, 3.3\]

This is needed because `None` is not comparable to other types.

*   Convert mapping types into sorted item lists before sorting:
    

Copy

\>>> data \= \[{'a': 1}, {'b': 2}\]
\>>> sorted(data, key\=lambda d: sorted(d.items()))
\[{'a': 1}, {'b': 2}\]

This is needed because dict-to-dict comparisons raise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
.

*   Convert set types into sorted lists before sorting:
    

Copy

\>>> data \= \[{'a', 'b', 'c'}, {'b', 'c', 'd'}\]
\>>> sorted(map(sorted, data))
\[\['a', 'b', 'c'\], \['b', 'c', 'd'\]\]

This is needed because the elements contained in set types do not have a deterministic order. For example, `list({'a', 'b'})` may produce either `['a', 'b']` or `['b', 'a']`.

Odds and Ends[¶](https://docs.python.org/3/howto/sorting.html#odds-and-ends "Link to this heading")

----------------------------------------------------------------------------------------------------

*   For locale aware sorting, use [`locale.strxfrm()`](https://docs.python.org/3/library/locale.html#locale.strxfrm "locale.strxfrm")
     for a key function or [`locale.strcoll()`](https://docs.python.org/3/library/locale.html#locale.strcoll "locale.strcoll")
     for a comparison function. This is necessary because “alphabetical” sort orderings can vary across cultures even if the underlying alphabet is the same.
    
*   The _reverse_ parameter still maintains sort stability (so that records with equal keys retain the original order). Interestingly, that effect can be simulated without the parameter by using the builtin [`reversed()`](https://docs.python.org/3/builtins/functions.html#reversed "reversed")
     function twice:
    
    Copy
    
    \>>> data \= \[('red', 1), ('blue', 1), ('red', 2), ('blue', 2)\]
    \>>> standard\_way \= sorted(data, key\=itemgetter(0), reverse\=True)
    \>>> double\_reversed \= list(reversed(sorted(reversed(data), key\=itemgetter(0))))
    \>>> assert standard\_way \== double\_reversed
    \>>> standard\_way
    \[('red', 1), ('red', 2), ('blue', 1), ('blue', 2)\]
    
*   The sort routines use `<` when making comparisons between two objects. So, it is easy to add a standard sort order to a class by defining an [`__lt__()`](https://docs.python.org/3/reference/datamodel.html#object.__lt__ "object.__lt__")
     method:
    
    Copy
    
    \>>> Student.\_\_lt\_\_ \= lambda self, other: self.age < other.age
    \>>> sorted(student\_objects)
    \[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)\]
    
    However, note that `<` can fall back to using [`__gt__()`](https://docs.python.org/3/reference/datamodel.html#object.__gt__ "object.__gt__")
     if [`__lt__()`](https://docs.python.org/3/reference/datamodel.html#object.__lt__ "object.__lt__")
     is not implemented (see [`object.__lt__()`](https://docs.python.org/3/reference/datamodel.html#object.__lt__ "object.__lt__")
     for details on the mechanics). To avoid surprises, [**PEP 8**](https://peps.python.org/pep-0008/)
     recommends that all six comparison methods be implemented. The [`@total_ordering`](https://docs.python.org/3/library/functools.html#functools.total_ordering "functools.total_ordering")
     decorator is provided to make that task easier.
    
*   Key functions need not depend directly on the objects being sorted. A key function can also access external resources. For instance, if the student grades are stored in a dictionary, they can be used to sort a separate list of student names:
    
    Copy
    
    \>>> students \= \['dave', 'john', 'jane'\]
    \>>> newgrades \= {'john': 'F', 'jane':'A', 'dave': 'C'}
    \>>> sorted(students, key\=newgrades.\_\_getitem\_\_)
    \['jane', 'dave', 'john'\]
    

Partial Sorts[¶](https://docs.python.org/3/howto/sorting.html#partial-sorts "Link to this heading")

----------------------------------------------------------------------------------------------------

Some applications require only some of the data to be ordered. The standard library provides several tools that do less work than a full sort:

*   [`min()`](https://docs.python.org/3/builtins/functions.html#min "min")
     and [`max()`](https://docs.python.org/3/builtins/functions.html#max "max")
     return the smallest and largest values, respectively. These functions make a single pass over the input data and require almost no auxiliary memory.
    
*   [`heapq.nsmallest()`](https://docs.python.org/3/library/heapq.html#heapq.nsmallest "heapq.nsmallest")
     and [`heapq.nlargest()`](https://docs.python.org/3/library/heapq.html#heapq.nlargest "heapq.nlargest")
     return the _n_ smallest and largest values, respectively. These functions make a single pass over the data keeping only _n_ elements in memory at a time. For values of _n_ that are small relative to the number of inputs, these functions make far fewer comparisons than a full sort.
    
*   [`heapq.heappush()`](https://docs.python.org/3/library/heapq.html#heapq.heappush "heapq.heappush")
     and [`heapq.heappop()`](https://docs.python.org/3/library/heapq.html#heapq.heappop "heapq.heappop")
     create and maintain a partially sorted arrangement of data that keeps the smallest element at position `0`. These functions are suitable for implementing priority queues which are commonly used for task scheduling.
    

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Sorting Techniques](https://docs.python.org/3/howto/sorting.html#)
    *   [Sorting Basics](https://docs.python.org/3/howto/sorting.html#sorting-basics)
        
    *   [Key Functions](https://docs.python.org/3/howto/sorting.html#key-functions)
        
    *   [Operator Module Functions and Partial Function Evaluation](https://docs.python.org/3/howto/sorting.html#operator-module-functions-and-partial-function-evaluation)
        
    *   [Ascending and Descending](https://docs.python.org/3/howto/sorting.html#ascending-and-descending)
        
    *   [Sort Stability and Complex Sorts](https://docs.python.org/3/howto/sorting.html#sort-stability-and-complex-sorts)
        
    *   [Decorate-Sort-Undecorate](https://docs.python.org/3/howto/sorting.html#decorate-sort-undecorate)
        
    *   [Comparison Functions](https://docs.python.org/3/howto/sorting.html#comparison-functions)
        
    *   [Strategies For Unorderable Types and Values](https://docs.python.org/3/howto/sorting.html#strategies-for-unorderable-types-and-values)
        
    *   [Odds and Ends](https://docs.python.org/3/howto/sorting.html#odds-and-ends)
        
    *   [Partial Sorts](https://docs.python.org/3/howto/sorting.html#partial-sorts)
        

#### Previous topic

[Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html "previous chapter")

#### Next topic

[Unicode HOWTO](https://docs.python.org/3/howto/unicode.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Sorting+Techniques&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fhowto%2Fsorting.html&pagesource=howto%2Fsorting.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/howto/sorting.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/howto/unicode.html "Unicode HOWTO")
     |
*   [previous](https://docs.python.org/3/howto/sockets.html "Socket Programming HOWTO")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python HOWTOs](https://docs.python.org/3/howto/index.html)
     »
*   [Sorting Techniques](https://docs.python.org/3/howto/sorting.html)
    
*    
    
    |
*   Theme Auto Light Dark |