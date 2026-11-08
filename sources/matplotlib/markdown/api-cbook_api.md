[Skip to main content](https://matplotlib.org/stable/api/cbook_api.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

`matplotlib.cbook`[#](https://matplotlib.org/stable/api/cbook_api.html#module-matplotlib.cbook "Link to this heading")

=======================================================================================================================

A collection of utility functions and classes. Originally, many (but not all) were from the Python Cookbook -- hence the name cbook.

class matplotlib.cbook.CallbackRegistry(_exception\_handler\=<function \_exception\_printer>_, _\*_, _signals\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L202-L422)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Handle registering, processing, blocking, and disconnecting for a set of signals and callbacks:

\>>> def oneat(x):
...     print('eat', x)
\>>> def ondrink(x):
...     print('drink', x)

\>>> from matplotlib.cbook import CallbackRegistry
\>>> callbacks \= CallbackRegistry()

\>>> id\_eat \= callbacks.connect('eat', oneat)
\>>> id\_drink \= callbacks.connect('drink', ondrink)

\>>> callbacks.process('drink', 123)
drink 123
\>>> callbacks.process('eat', 456)
eat 456
\>>> callbacks.process('be merry', 456)   \# nothing will be called

\>>> callbacks.disconnect(id\_eat)
\>>> callbacks.process('eat', 456)        \# nothing will be called

\>>> with callbacks.blocked(signal\='drink'):
...     callbacks.process('drink', 123)  \# nothing will be called
\>>> callbacks.process('drink', 123)
drink 123

\>>> callbacks.disconnect(ondrink, signal\='drink')  \# disconnect by func
\>>> callbacks.process('drink', 123)      \# nothing will be called

In practice, one should always disconnect all callbacks when they are no longer needed to avoid dangling references (and thus memory leaks). However, real code in Matplotlib rarely does so, and due to its design, it is rather difficult to place this kind of code. To get around this, and prevent this class of memory leaks, we instead store weak references to bound methods only, so when the destination object needs to die, the CallbackRegistry won't keep it alive.

Parameters:

**exception\_handler**callable, optional

If not None, _exception\_handler_ must be a function that takes an [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)")
 as single parameter. It gets called with any [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)")
 raised by the callbacks during [`CallbackRegistry.process`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry.process "matplotlib.cbook.CallbackRegistry.process")
, and may either re-raise the exception or handle it in another manner.

The default handler prints the exception (with [`traceback.print_exc`](https://docs.python.org/3/library/traceback.html#traceback.print_exc "(in Python v3.14)")
) if an interactive event loop is running; it re-raises the exception if no interactive event loop is running.

**signals**list, optional

If not None, _signals_ is a list of signals that this registry handles: attempting to [`process`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry.process "matplotlib.cbook.CallbackRegistry.process")
 or to [`connect`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry.connect "matplotlib.cbook.CallbackRegistry.connect")
 to a signal not in the list throws a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")
. The default, None, does not restrict the handled signals.

blocked(_\*_, _signal\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L399-L422)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry.blocked "Link to this definition")

Block callback signals from being processed.

A context manager to temporarily block/disable callback signals from being processed by the registered listeners.

Parameters:

**signal**str, optional

The callback signal to block. The default is to block all signals.

connect(_signal_, _func_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L300-L310)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry.connect "Link to this definition")

Register _func_ to be called when signal _signal_ is generated.

disconnect(_cid\_or\_func_, _\*_, _signal\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L337-L375)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry.disconnect "Link to this definition")

Disconnect a callback.

Parameters:

**cid\_or\_func**int or callable

If an int, disconnect the callback with that connection id. If a callable, disconnect that function from signals.

**signal**optional

Only used when _cid\_or\_func_ is a callable. If given, disconnect the function only from that specific signal. If not given, disconnect from all signals the function is connected to.

Notes

No error is raised if such a callback does not exist.

process(_s_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L377-L397)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry.process "Link to this definition")

Process signal _s_.

All of the functions registered to receive callbacks on _s_ will be called with `*args` and `**kwargs`.

class matplotlib.cbook.Grouper(_init\=()_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L809-L924)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.Grouper "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A disjoint-set data structure.

Objects can be joined using [`join()`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.Grouper.join "matplotlib.cbook.Grouper.join")
, tested for connectedness using [`joined()`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.Grouper.joined "matplotlib.cbook.Grouper.joined")
, and all disjoint sets can be retrieved by using the object as an iterator.

The objects being joined must be hashable and weak-referenceable.

Examples

\>>> from matplotlib.cbook import Grouper
\>>> class Foo:
...     def \_\_init\_\_(self, s):
...         self.s \= s
...     def \_\_repr\_\_(self):
...         return self.s
...
\>>> a, b, c, d, e, f \= \[Foo(x) for x in 'abcdef'\]
\>>> grp \= Grouper()
\>>> grp.join(a, b)
\>>> grp.join(b, c)
\>>> grp.join(d, e)
\>>> list(grp)
\[\[a, b, c\], \[d, e\]\]
\>>> grp.joined(a, b)
True
\>>> grp.joined(a, c)
True
\>>> grp.joined(a, d)
False

get\_siblings(_a_, _\*_, _include\_self\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L914-L924)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.Grouper.get_siblings "Link to this definition")

Return all the items joined with _a_.

_a_ is included in the list if _include\_self_ is True.

join(_a_, _\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L870-L893)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.Grouper.join "Link to this definition")

Join given arguments into the same set. Accepts one or more arguments.

joined(_a_, _b_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L895-L897)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.Grouper.joined "Link to this definition")

Return whether _a_ and _b_ are members of the same set.

remove(_a_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L899-L902)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.Grouper.remove "Link to this definition")

Remove _a_ from the grouper, doing nothing if it is not there.

class matplotlib.cbook.GrouperView(_grouper_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L927-L946)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.GrouperView "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Immutable view over a [`Grouper`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.Grouper "matplotlib.cbook.Grouper")
.

get\_siblings(_a_, _\*_, _include\_self\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L940-L946)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.GrouperView.get_siblings "Link to this definition")

Return all the items joined with _a_.

_a_ is included in the list if _include\_self_ is True.

joined(_a_, _b_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L934-L938)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.GrouperView.joined "Link to this definition")

Return whether _a_ and _b_ are members of the same set.

matplotlib.cbook.boxplot\_stats(_X_, _whis\=1.5_, _bootstrap\=None_, _labels\=None_, _autorange\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L1153-L1352)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.boxplot_stats "Link to this definition")

Return a list of dictionaries of statistics used to draw a series of box and whisker plots using [`bxp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html#matplotlib.axes.Axes.bxp "matplotlib.axes.Axes.bxp")
.

Parameters:

**X**array-like

Data that will be represented in the boxplots. Should have 2 or fewer dimensions.

**whis**float or (float, float), default: 1.5

The position of the whiskers.

If a float, the lower whisker is at the lowest datum above `Q1 - whis*(Q3-Q1)`, and the upper whisker at the highest datum below `Q3 + whis*(Q3-Q1)`, where Q1 and Q3 are the first and third quartiles. The default value of `whis = 1.5` corresponds to Tukey's original definition of boxplots.

If a pair of floats, they indicate the percentiles at which to draw the whiskers (e.g., (5, 95)). In particular, setting this to (0, 100) results in whiskers covering the whole range of the data.

In the edge case where `Q1 == Q3`, _whis_ is automatically set to (0, 100) (cover the whole range of the data) if _autorange_ is True.

Beyond the whiskers, data are considered outliers and are plotted as individual points.

**bootstrap**int, optional

Number of times the confidence intervals around the median should be bootstrapped (percentile method).

**labels**list of str, optional

Labels for each dataset. Length must be compatible with dimensions of _X_.

**autorange**bool, optional (False)

When [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
 and the data are distributed such that the 25th and 75th percentiles are equal, `whis` is set to (0, 100) such that the whisker ends are at the minimum and maximum of the data.

Returns:

list of dict

A list of dictionaries containing the results for each column of data. Keys of each dictionary are the following:

| Key | Value Description |
| --- | --- |
| label | tick label for the boxplot |
| mean | arithmetic mean value |
| med | 50th percentile |
| q1  | first quartile (25th percentile) |
| q3  | third quartile (75th percentile) |
| iqr | interquartile range |
| cilo | lower notch around the median |
| cihi | upper notch around the median |
| whislo | end of the lower whisker |
| whishi | end of the upper whisker |
| fliers | outliers |

Notes

Non-bootstrapping approach to confidence interval uses Gaussian-based asymptotic approximation:

\\\[\\mathrm{med} \\pm 1.57 \\times \\frac{\\mathrm{iqr}}{\\sqrt{N}}\\\]

General approach from: McGill, R., Tukey, J.W., and Larsen, W.A. (1978) "Variations of Boxplots", The American Statistician, 32:12-16.

matplotlib.cbook.contiguous\_regions(_mask_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L1361-L1384)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.contiguous_regions "Link to this definition")

Return a list of (ind0, ind1) such that `mask[ind0:ind1].all()` is True and we cover all such regions.

matplotlib.cbook.delete\_masked\_points(_\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L973-L1047)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.delete_masked_points "Link to this definition")

Find all masked and/or non-finite points in a set of arguments, and return the arguments with only the unmasked points remaining.

Arguments can be in any of 5 categories:

1.  1-D masked arrays
    
2.  1-D ndarrays
    
3.  ndarrays with more than one dimension
    
4.  other non-string iterables
    
5.  anything else
    

The first argument must be in one of the first four categories; any argument with a length differing from that of the first argument (and hence anything in category 5) then will be passed through unchanged.

Masks are obtained from all arguments of the correct length in categories 1, 2, and 4; a point is bad if masked in a masked array or if it is a nan or inf. No attempt is made to extract a mask from categories 2, 3, and 4 if [`numpy.isfinite`](https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html#numpy.isfinite "(in NumPy v2.5)")
 does not yield a Boolean array.

All input arguments that are not passed unchanged are returned as ndarrays after removing the points or rows corresponding to masks in any of the arguments.

A vastly simpler version of this function was originally written as a helper for Axes.scatter().

matplotlib.cbook.file\_requires\_unicode(_x_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L522-L532)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.file_requires_unicode "Link to this definition")

Return whether the given writable file-like object requires Unicode to be written to it.

matplotlib.cbook.flatten(_seq_, _scalarp\=<function is\_scalar\_or\_string>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L635-L654)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.flatten "Link to this definition")

Return a generator of flattened nested containers.

For example:

\>>> from matplotlib.cbook import flatten
\>>> l \= (('John', \['Hunter'\]), (1, 23), \[\[(\[42, (5, 23)\], )\]\])
\>>> print(list(flatten(l)))
\['John', 'Hunter', 1, 23, 42, 5, 23\]

By: Composite of Holger Krekel and Luther Blissett From: [https://code.activestate.com/recipes/121294-simple-generator-for-flattening-nested-containers/](https://code.activestate.com/recipes/121294-simple-generator-for-flattening-nested-containers/)
 and Recipe 1.12 in cookbook

matplotlib.cbook.get\_sample\_data(_fname_, _asfileobj\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L598-L623)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "Link to this definition")

Return a sample data file. _fname_ is a path relative to the `mpl-data/sample_data` directory. If _asfileobj_ is [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
 return a file object, otherwise just a file path.

Sample data files are stored in the 'mpl-data/sample\_data' directory within the Matplotlib package.

If the filename ends in .gz, the file is implicitly ungzipped. If the filename ends with .npy or .npz, and _asfileobj_ is [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
, the file is loaded with [`numpy.load`](https://numpy.org/doc/stable/reference/generated/numpy.load.html#numpy.load "(in NumPy v2.5)")
.

matplotlib.cbook.index\_of(_y_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L1742-L1774)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.index_of "Link to this definition")

A helper function to create reasonable x values for the given _y_.

This is used for plotting (x, y) if x values are not explicitly given.

First try `y.index` (assuming _y_ is a [`pandas.Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "(in pandas v3.0.5)")
), if that fails, use `range(len(y))`.

This will be extended in the future to deal with more types of labeled data.

Parameters:

**y**float or array-like

Returns:

**x, y**ndarray

The x and y values to plot.

matplotlib.cbook.is\_math\_text(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L1387-L1397)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.is_math_text "Link to this definition")

Return whether the string _s_ contains math expressions.

This is done by checking whether _s_ contains an even number of non-escaped dollar signs.

matplotlib.cbook.is\_scalar\_or\_string(_val_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L593-L595)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.is_scalar_or_string "Link to this definition")

Return whether the given object is a scalar or string like.

matplotlib.cbook.is\_writable\_file\_like(_obj_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L517-L519)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.is_writable_file_like "Link to this definition")

Return whether _obj_ looks like a file object with a _write_ method.

matplotlib.cbook.ls\_mapper \= {'-': 'solid', '--': 'dashed', '-.': 'dashdot', ':': 'dotted'}[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.ls_mapper "Link to this definition")

Maps short codes for line style to their full name used by backends.

matplotlib.cbook.ls\_mapper\_r \= {'dashdot': '-.', 'dashed': '--', 'dotted': ':', 'solid': '-'}[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.ls_mapper_r "Link to this definition")

Maps full names for line styles used by backends to their short codes.

matplotlib.cbook.normalize\_kwargs(_kw_, _alias\_mapping\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L1864-L1921)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.normalize_kwargs "Link to this definition")

Helper function to normalize kwarg inputs.

Parameters:

**kw**dict or None

A dict of keyword arguments. None is explicitly supported and treated as an empty dict, to support functions with an optional parameter of the form `props=None`.

**alias\_mapping**Artist subclass or Artist instance

A mapping between a canonical name to a list of aliases, in order of precedence from lowest to highest.

If the canonical value is not in the list it is assumed to have the highest priority.

If an Artist subclass or instance is passed, use its properties alias mapping.

Raises:

TypeError

To match what Python raises if invalid arguments/keyword arguments are passed to a callable.

matplotlib.cbook.open\_file\_cm(_path\_or\_file_, _mode\='r'_, _encoding\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L587-L590)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.open_file_cm "Link to this definition")

Pass through file objects and context-manage path-likes.

matplotlib.cbook.print\_cycles(_objects_, _outstream\=<\_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>_, _show\_progress\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L740-L806)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.print_cycles "Link to this definition")

Print loops of cyclic references in the given _objects_.

It is often useful to pass in `gc.garbage` to find the cycles that are preventing some objects from being garbage collected.

Parameters:

**objects**

A list of objects to find cycles in.

**outstream**

The stream for output.

**show\_progress**bool

If True, print the number of objects reached as they are found.

matplotlib.cbook.pts\_to\_midstep(_x_, _\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L1697-L1732)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.pts_to_midstep "Link to this definition")

Convert continuous line to mid-steps.

Given a set of `N` points convert to `2N` points which when connected linearly give a step function which changes values at the middle of the intervals.

Parameters:

**x**array

The x location of the steps. May be empty.

**y1, ..., yp**array

y arrays to be turned into steps; all must be the same length as `x`.

Returns:

array

The x and y values converted to steps in the same order as the input; can be unpacked as `x_out, y1_out, ..., yp_out`. If the input is length `N`, each of these arrays will be length `2N`.

Examples

\>>> x\_s, y1\_s, y2\_s \= pts\_to\_midstep(x, y1, y2)

matplotlib.cbook.pts\_to\_poststep(_x_, _\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L1661-L1694)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.pts_to_poststep "Link to this definition")

Convert continuous line to post-steps.

Given a set of `N` points convert to `2N + 1` points, which when connected linearly give a step function which changes values at the end of the intervals.

Parameters:

**x**array

The x location of the steps. May be empty.

**y1, ..., yp**array

y arrays to be turned into steps; all must be the same length as `x`.

Returns:

array

The x and y values converted to steps in the same order as the input; can be unpacked as `x_out, y1_out, ..., yp_out`. If the input is length `N`, each of these arrays will be length `2N + 1`. For `N=0`, the length will be 0.

Examples

\>>> x\_s, y1\_s, y2\_s \= pts\_to\_poststep(x, y1, y2)

matplotlib.cbook.pts\_to\_prestep(_x_, _\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L1623-L1658)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.pts_to_prestep "Link to this definition")

Convert continuous line to pre-steps.

Given a set of `N` points, convert to `2N - 1` points, which when connected linearly give a step function which changes values at the beginning of the intervals.

Parameters:

**x**array

The x location of the steps. May be empty.

**y1, ..., yp**array

y arrays to be turned into steps; all must be the same length as `x`.

Returns:

array

The x and y values converted to steps in the same order as the input; can be unpacked as `x_out, y1_out, ..., yp_out`. If the input is length `N`, each of these arrays will be length `2N + 1`. For `N=0`, the length will be 0.

Examples

\>>> x\_s, y1\_s, y2\_s \= pts\_to\_prestep(x, y1, y2)

matplotlib.cbook.safe\_first\_element(_obj_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L1777-L1794)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.safe_first_element "Link to this definition")

Return the first element in _obj_.

This is a type-independent way of obtaining the first element, supporting both index access and the iterator protocol.

matplotlib.cbook.safe\_masked\_invalid(_x_, _copy\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L712-L737)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.safe_masked_invalid "Link to this definition")

matplotlib.cbook.sanitize\_sequence(_data_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L1836-L1841)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.sanitize_sequence "Link to this definition")

Convert dictview objects to list. Other inputs are returned unchanged.

class matplotlib.cbook.silent\_list(_type_, _seq\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L425-L456)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.silent_list "Link to this definition")

Bases: [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")

A list with a short `repr()`.

This is meant to be used for a homogeneous list of artists, so that they don't cause long, meaningless output.

Instead of

\[<matplotlib.lines.Line2D object at 0x7f5749fed3c8\>,\
 <matplotlib.lines.Line2D object at 0x7f5749fed4e0\>,\
 <matplotlib.lines.Line2D object at 0x7f5758016550\>\]

one will get

<a list of 3 Line2D objects\>

If `self.type` is None, the type name is obtained from the first item in the list (if any).

matplotlib.cbook.simple\_linear\_interpolation(_a_, _steps_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L949-L970)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.simple_linear_interpolation "Link to this definition")

Resample an array with `steps - 1` points between original point pairs.

Along each column of _a_, `(steps - 1)` points are introduced between each original values; the values are linearly interpolated.

Parameters:

**a**array, shape (n, ...)

**steps**int

Returns:

array

shape `((n - 1) * steps + 1, ...)`

matplotlib.cbook.strip\_math(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L474-L494)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.strip_math "Link to this definition")

Remove latex formatting from mathtext.

Only handles fully math and fully non-math strings.

matplotlib.cbook.to\_filehandle(_fname_, _flag\='r'_, _return\_opened\=False_, _encoding\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L535-L584)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.to_filehandle "Link to this definition")

Convert a path to an open file handle or pass-through a file-like object.

Consider using [`open_file_cm`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.open_file_cm "matplotlib.cbook.open_file_cm")
 instead, as it allows one to properly close newly created file objects more easily.

Parameters:

**fname**str or path-like or file-like

If [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 or [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")
, the file is opened using the flags specified by _flag_ and _encoding_. If a file-like object, it is passed through.

**flag**str, default: 'r'

Passed as the _mode_ argument to [`open`](https://docs.python.org/3/library/functions.html#open "(in Python v3.14)")
 when _fname_ is [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 or [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")
; ignored if _fname_ is file-like.

**return\_opened**bool, default: False

If True, return both the file object and a boolean indicating whether this was a new file (that the caller needs to close). If False, return only the new file.

**encoding**str or None, default: None

Passed as the _mode_ argument to [`open`](https://docs.python.org/3/library/functions.html#open "(in Python v3.14)")
 when _fname_ is [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 or [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")
; ignored if _fname_ is file-like.

Returns:

**fh**file-like

**opened**bool

_opened_ is only returned if _return\_opened_ is True.

matplotlib.cbook.violin\_stats(_X_, _method\=('GaussianKDE', 'scott')_, _points\=100_, _quantiles\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cbook.py#L1486-L1620)
[#](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.violin_stats "Link to this definition")

Return a list of dictionaries of data which can be used to draw a series of violin plots.

See the `Returns` section below to view the required keys of the dictionary.

Users can skip this function and pass a user-defined set of dictionaries with the same keys to [`violin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violin.html#matplotlib.axes.Axes.violin "matplotlib.axes.Axes.violin")
 instead of using Matplotlib to do the calculations. See the _Returns_ section below for the keys that must be present in the dictionaries.

Parameters:

**X**1D array or sequence of 1D arrays or 2D array

Sample data that will be used to produce the gaussian kernel density estimates. Non-finite and masked values are ignored. Possible values:

*   1D array: Statistics are computed for that array.
    
*   sequence of 1D arrays: Statistics are computed for each array in the sequence.
    
*   2D array: Statistics are computed for each column in the array.
    

**method**(name, bw\_method) or callable,

The method used to calculate the kernel density estimate for each column of data. Valid values:

*   a tuple of the form `(name, bw_method)` where _name_ currently must always be `"GaussianKDE"` and _bw\_method_ is the method used to calculate the estimator bandwidth. Supported values are 'scott', 'silverman' or a float or a callable. If a float, this will be used directly as `kde.factor`. If a callable, it should take a [`matplotlib.mlab.GaussianKDE`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.GaussianKDE "matplotlib.mlab.GaussianKDE")
     instance as its only parameter and return a float.
    
*   a callable with the signature
    
    def method(data: ndarray, coords: ndarray) \-> ndarray
    
    It should return the KDE of _data_ evaluated at _coords_.
    
    Added in version 3.11: Support for `(name, bw_method)` tuple.
    

**points**int, default: 100

Defines the number of points to evaluate each of the gaussian kernel density estimates at.

**quantiles**array-like, default: None

Defines (if not None) a list of floats in interval \[0, 1\] for each column of data, which represents the quantiles that will be rendered for that column of data. Must have 2 or fewer dimensions. 1D array will be treated as a singleton list containing them.

Returns:

list of dict

A list of dictionaries containing the results for each column of data. The dictionaries contain at least the following:

*   coords: A list of scalars containing the coordinates this particular kernel density estimate was evaluated at.
    
*   vals: A list of scalars containing the values of the kernel density estimate at each of the coordinates given in _coords_.
    
*   mean: The mean value for this column of data.
    
*   median: The median value for this column of data.
    
*   min: The minimum value for this column of data.
    
*   max: The maximum value for this column of data.
    
*   quantiles: The quantile values for this column of data.
    

On this page