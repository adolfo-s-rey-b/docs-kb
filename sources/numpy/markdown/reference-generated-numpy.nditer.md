[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.nditer.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.nditer.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.nditer.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.nditer.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.nditer.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.nditer.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.nditer.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.nditer.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.nditer.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.nditer.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.nditer.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.nditer.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.nditer.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.nditer.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.nditer.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.nditer.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.nditer.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.nditer.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.nditer.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.nditer.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.nditer.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.nditer.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.nditer[#](https://numpy.org/doc/stable/reference/generated/numpy.nditer.html#numpy-nditer "Link to this heading")

========================================================================================================================

_class_ numpy.nditer(_op_, _flags\=None_, _op\_flags\=None_, _op\_dtypes\=None_, _order\='K'_, _casting\='safe'_, _op\_axes\=None_, _itershape\=None_, _buffersize\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/__init__.py)
[#](https://numpy.org/doc/stable/reference/generated/numpy.nditer.html#numpy.nditer "Link to this definition")

Efficient multi-dimensional iterator object to iterate over arrays. To get started using this object, see the [introductory guide to array iteration](https://numpy.org/doc/stable/reference/arrays.nditer.html#arrays-nditer)
.

Parameters:

**op**ndarray or sequence of array\_like

The array(s) to iterate over.

**flags**sequence of str, optional

Flags to control the behavior of the iterator.

*   `buffered` enables buffering when required.
    
*   `c_index` causes a C-order index to be tracked.
    
*   `f_index` causes a Fortran-order index to be tracked.
    
*   `multi_index` causes a multi-index, or a tuple of indices with one per iteration dimension, to be tracked.
    
*   `common_dtype` causes all the operands to be converted to a common data type, with copying or buffering as necessary.
    
*   `copy_if_overlap` causes the iterator to determine if read operands have overlap with write operands, and make temporary copies as necessary to avoid overlap. False positives (needless copying) are possible in some cases.
    
*   `delay_bufalloc` delays allocation of the buffers until a reset() call is made. Allows `allocate` operands to be initialized before their values are copied into the buffers.
    
*   `external_loop` causes the `values` given to be one-dimensional arrays with multiple values instead of zero-dimensional arrays.
    
*   `grow_inner` allows the `value` array sizes to be made larger than the buffer size when both `buffered` and `external_loop` is used.
    
*   `ranged` allows the iterator to be restricted to a sub-range of the iterindex values.
    
*   `refs_ok` enables iteration of reference types, such as object arrays.
    
*   `reduce_ok` enables iteration of `readwrite` operands which are broadcasted, also known as reduction operands.
    
*   `zerosize_ok` allows [`itersize`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.itersize.html#numpy.nditer.itersize "numpy.nditer.itersize")
     to be zero.
    

**op\_flags**list of list of str, optional

This is a list of flags for each operand. At minimum, one of `readonly`, `readwrite`, or `writeonly` must be specified.

*   `readonly` indicates the operand will only be read from.
    
*   `readwrite` indicates the operand will be read from and written to.
    
*   `writeonly` indicates the operand will only be written to.
    
*   `no_broadcast` prevents the operand from being broadcasted.
    
*   `contig` forces the operand data to be contiguous.
    
*   `aligned` forces the operand data to be aligned.
    
*   `nbo` forces the operand data to be in native byte order.
    
*   `copy` allows a temporary read-only copy if required.
    
*   `updateifcopy` allows a temporary read-write copy if required.
    
*   `allocate` causes the array to be allocated if it is None in the `op` parameter.
    
*   `no_subtype` prevents an `allocate` operand from using a subtype.
    
*   `arraymask` indicates that this operand is the mask to use for selecting elements when writing to operands with the ‘writemasked’ flag set. The iterator does not enforce this, but when writing from a buffer back to the array, it only copies those elements indicated by this mask.
    
*   `writemasked` indicates that only elements where the chosen `arraymask` operand is True will be written to.
    
*   `overlap_assume_elementwise` can be used to mark operands that are accessed only in the iterator order, to allow less conservative copying when `copy_if_overlap` is present.
    

**op\_dtypes**dtype or tuple of dtype(s), optional

The required data type(s) of the operands. If copying or buffering is enabled, the data will be converted to/from their original types.

**order**{‘C’, ‘F’, ‘A’, ‘K’}, optional

Controls the iteration order. ‘C’ means C order, ‘F’ means Fortran order, ‘A’ means ‘F’ order if all the arrays are Fortran contiguous, ‘C’ order otherwise, and ‘K’ means as close to the order the array elements appear in memory as possible. This also affects the element memory order of `allocate` operands, as they are allocated to be compatible with iteration order. Default is ‘K’.

**casting**{‘no’, ‘equiv’, ‘safe’, ‘same\_kind’, ‘unsafe’}, optional

Controls what kind of data casting may occur when making a copy or buffering. Setting this to ‘unsafe’ is not recommended, as it can adversely affect accumulations.

*   ‘no’ means the data types should not be cast at all.
    
*   ‘equiv’ means only byte-order changes are allowed.
    
*   ‘safe’ means only casts which can preserve values are allowed.
    
*   ‘same\_kind’ means only safe casts or casts within a kind, like float64 to float32, are allowed.
    
*   ‘unsafe’ means any data conversions may be done.
    

**op\_axes**list of list of ints, optional

If provided, is a list of ints or None for each operands. The list of axes for an operand is a mapping from the dimensions of the iterator to the dimensions of the operand. A value of -1 can be placed for entries, causing that dimension to be treated as [`newaxis`](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")
.

**itershape**tuple of ints, optional

The desired shape of the iterator. This allows `allocate` operands with a dimension mapped by op\_axes not corresponding to a dimension of a different operand to get a value not equal to 1 for that dimension.

**buffersize**int, optional

When buffering is enabled, controls the size of the temporary buffers. Set to 0 for the default value.

Attributes:

**dtypes**tuple of dtype(s)

The data types of the values provided in [`value`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.value.html#numpy.nditer.value "numpy.nditer.value")
. This may be different from the operand data types if buffering is enabled. Valid only before the iterator is closed.

**finished**bool

Whether the iteration over the operands is finished or not.

**has\_delayed\_bufalloc**bool

If True, the iterator was created with the `delay_bufalloc` flag, and no reset() function was called on it yet.

**has\_index**bool

If True, the iterator was created with either the `c_index` or the `f_index` flag, and the property [`index`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.index.html#numpy.nditer.index "numpy.nditer.index")
 can be used to retrieve it.

**has\_multi\_index**bool

If True, the iterator was created with the `multi_index` flag, and the property [`multi_index`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.multi_index.html#numpy.nditer.multi_index "numpy.nditer.multi_index")
 can be used to retrieve it.

**index**

When the `c_index` or `f_index` flag was used, this property provides access to the index. Raises a ValueError if accessed and `has_index` is False.

**iterationneedsapi**bool

Whether iteration requires access to the Python API, for example if one of the operands is an object array.

**iterindex**int

An index which matches the order of iteration.

**itersize**int

Size of the iterator.

**itviews**

Structured view(s) of [`operands`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.operands.html#numpy.nditer.operands "numpy.nditer.operands")
 in memory, matching the reordered and optimized iterator access pattern. Valid only before the iterator is closed.

**multi\_index**

When the `multi_index` flag was used, this property provides access to the index. Raises a ValueError if accessed accessed and `has_multi_index` is False.

**ndim**int

The dimensions of the iterator.

**nop**int

The number of iterator operands.

[`operands`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.operands.html#numpy.nditer.operands "numpy.nditer.operands")
tuple of operand(s)

operands\[_Slice_\]

**shape**tuple of ints

Shape tuple, the shape of the iterator.

**value**

Value of `operands` at current iteration. Normally, this is a tuple of array scalars, but if the flag `external_loop` is used, it is a tuple of one dimensional arrays.

Methods

|     |     |
| --- | --- |
| [`close`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.close.html#numpy.nditer.close "numpy.nditer.close")<br>() | Resolve all writeback semantics in writeable operands. |
| [`copy`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.copy.html#numpy.nditer.copy "numpy.nditer.copy")<br>() | Get a copy of the iterator in its current state. |
| [`debug_print`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.debug_print.html#numpy.nditer.debug_print "numpy.nditer.debug_print")<br>() | Print the current state of the [`nditer`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.html#numpy.nditer "numpy.nditer")<br> instance and debug info to stdout. |
| [`enable_external_loop`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.enable_external_loop.html#numpy.nditer.enable_external_loop "numpy.nditer.enable_external_loop")<br>() | When the "external\_loop" was not used during construction, but is desired, this modifies the iterator to behave as if the flag was specified. |
| [`iternext`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.iternext.html#numpy.nditer.iternext "numpy.nditer.iternext")<br>() | Check whether iterations are left, and perform a single internal iteration without returning the result. |
| [`remove_axis`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.remove_axis.html#numpy.nditer.remove_axis "numpy.nditer.remove_axis")<br>(i, /) | Removes axis _i_ from the iterator. |
| [`remove_multi_index`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.remove_multi_index.html#numpy.nditer.remove_multi_index "numpy.nditer.remove_multi_index")<br>() | When the "multi\_index" flag was specified, this removes it, allowing the internal iteration structure to be optimized further. |
| [`reset`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.reset.html#numpy.nditer.reset "numpy.nditer.reset")<br>() | Reset the iterator to its initial state. |

Notes

[`nditer`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.html#numpy.nditer "numpy.nditer")
 supersedes [`flatiter`](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
. The iterator implementation behind [`nditer`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.html#numpy.nditer "numpy.nditer")
 is also exposed by the NumPy C API.

The Python exposure supplies two iteration interfaces, one which follows the Python iterator protocol, and another which mirrors the C-style do-while pattern. The native Python approach is better in most cases, but if you need the coordinates or index of an iterator, use the C-style pattern.

Examples

Try it in your browser!

Here is how we might write an `iter_add` function, using the Python iterator protocol:

\>>> import numpy as np

Copy to clipboard

\>>> def iter\_add\_py(x, y, out\=None):
...     addop \= np.add
...     it \= np.nditer(\[x, y, out\], \[\],
...                 \[\['readonly'\], \['readonly'\], \['writeonly','allocate'\]\])
...     with it:
...         for (a, b, c) in it:
...             addop(a, b, out\=c)
...         return it.operands\[2\]

Copy to clipboard

Here is the same function, but following the C-style pattern:

\>>> def iter\_add(x, y, out\=None):
...    addop \= np.add
...    it \= np.nditer(\[x, y, out\], \[\],
...                \[\['readonly'\], \['readonly'\], \['writeonly','allocate'\]\])
...    with it:
...        while not it.finished:
...            addop(it\[0\], it\[1\], out\=it\[2\])
...            it.iternext()
...        return it.operands\[2\]

Copy to clipboard

Here is an example outer product function:

\>>> def outer\_it(x, y, out\=None):
...     mulop \= np.multiply
...     it \= np.nditer(\[x, y, out\], \['external\_loop'\],
...             \[\['readonly'\], \['readonly'\], \['writeonly', 'allocate'\]\],
...             op\_axes\=\[list(range(x.ndim)) + \[\-1\] \* y.ndim,\
...                      \[\-1\] \* x.ndim + list(range(y.ndim)),\
...                      None\])
...     with it:
...         for (a, b, c) in it:
...             mulop(a, b, out\=c)
...         return it.operands\[2\]

Copy to clipboard

\>>> a \= np.arange(2)+1
\>>> b \= np.arange(3)+1
\>>> outer\_it(a,b)
array(\[\[1, 2, 3\],\
       \[2, 4, 6\]\])

Copy to clipboard

Here is an example function which operates like a “lambda” ufunc:

\>>> def luf(lamdaexpr, \*args, \*\*kwargs):
... '''luf(lambdaexpr, op1, ..., opn, out=None, order='K', casting='safe', buffersize=0)'''
...    nargs \= len(args)
...    op \= (kwargs.get('out',None),) + args
...    it \= np.nditer(op, \['buffered','external\_loop'\],
...            \[\['writeonly','allocate','no\_broadcast'\]\] +
...                            \[\['readonly','nbo','aligned'\]\]\*nargs,
...            order\=kwargs.get('order','K'),
...            casting\=kwargs.get('casting','safe'),
...            buffersize\=kwargs.get('buffersize',0))
...    while not it.finished:
...        it\[0\] \= lamdaexpr(\*it\[1:\])
...        it.iternext()
...    return it.operands\[0\]

Copy to clipboard

\>>> a \= np.arange(5)
\>>> b \= np.ones(5)
\>>> luf(lambda i,j:i\*i + j/2, a, b)
array(\[  0.5,   1.5,   4.5,   9.5,  16.5\])

Copy to clipboard

If operand flags `"writeonly"` or `"readwrite"` are used the operands may be views into the original data with the _WRITEBACKIFCOPY_ flag. In this case [`nditer`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.html#numpy.nditer "numpy.nditer")
 must be used as a context manager or the [`nditer.close`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.close.html#numpy.nditer.close "numpy.nditer.close")
 method must be called before using the result. The temporary data will be written back to the original data when the [`__exit__`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "(in Python v3.14)")
 function is called but not before:

\>>> a \= np.arange(6, dtype\=np.int32)\[::\-2\]
\>>> with np.nditer(a, \[\],
...        \[\['writeonly', 'updateifcopy'\]\],
...        casting\='unsafe',
...        op\_dtypes\=\[np.dtype(np.float32)\]) as i:
...    x \= i.operands\[0\]
...    x\[:\] \= \[\-1, \-2, \-3\]
...    \# a still unchanged here
\>>> a, x
(array(\[-1, -2, -3\], dtype=int32), array(\[-1., -2., -3.\], dtype=float32))

Copy to clipboard

It is important to note that once the iterator is exited, dangling references (like _x_ in the example) may or may not share data with the original data _a_. If writeback semantics were active, i.e. if _x.base.flags.writebackifcopy_ is _True_, then exiting the iterator will sever the connection between _x_ and _a_, writing to _x_ will no longer write to _a_. If writeback semantics are not active, then _x.data_ will still point at some part of _a.data_, and writing to one will affect the other.

Context management and the [`close`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.close.html#numpy.nditer.close "numpy.nditer.close")
 method appeared in version 1.15.0.

Go BackOpen In Tab

On this page