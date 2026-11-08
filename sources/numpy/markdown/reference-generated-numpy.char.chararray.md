[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.char.chararray.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.char.chararray.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.char.chararray.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.char.chararray.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.char.chararray.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.char.chararray.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.char.chararray.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.char.chararray.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.char.chararray.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.char.chararray.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.char.chararray.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.char.chararray.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.char.chararray.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.char.chararray.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.char.chararray.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.char.chararray.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.char.chararray.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.char.chararray.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.char.chararray.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.char.chararray.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.char.chararray[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#numpy-char-chararray "Link to this heading")

================================================================================================================================================

_class_ numpy.char.chararray(_shape_, _itemsize\=1_, _unicode\=False_, _buffer\=None_, _offset\=0_, _strides\=None_, _order\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/defchararray.py#L404-L1217)
[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#numpy.char.chararray "Link to this definition")

Provides a convenient view on arrays of string and unicode values.

Deprecated since version 2.5: `chararray` is deprecated. Use an `ndarray` with a string or bytes dtype instead.

Note

The [`chararray`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#numpy.char.chararray "numpy.char.chararray")
 class exists for backwards compatibility with Numarray, it is not recommended for new development. Starting from numpy 1.4, if one needs arrays of strings, it is recommended to use arrays of [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.dtype.html#numpy.char.chararray.dtype "numpy.char.chararray.dtype")
 [`object_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.object_ "numpy.object_")
, [`bytes_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_")
 or [`str_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.str_ "numpy.str_")
, and use the free functions in the [`numpy.char`](https://numpy.org/doc/stable/reference/routines.char.html#module-numpy.char "numpy.char")
 module for fast vectorized string operations.

Versus a NumPy array of dtype [`bytes_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_")
 or [`str_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.str_ "numpy.str_")
, this class adds the following functionality:

1.  values automatically have whitespace removed from the end when indexed
    
2.  comparison operators automatically remove whitespace from the end when comparing values
    
3.  vectorized string operations are provided as methods (e.g. [`endswith`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.endswith.html#numpy.char.chararray.endswith "numpy.char.chararray.endswith")
    ) and infix operators (e.g. `"+", "*", "%"`)
    

chararrays should be created using [`numpy.char.array`](https://numpy.org/doc/stable/reference/generated/numpy.char.array.html#numpy.char.array "numpy.char.array")
 or [`numpy.char.asarray`](https://numpy.org/doc/stable/reference/generated/numpy.char.asarray.html#numpy.char.asarray "numpy.char.asarray")
, rather than this constructor directly.

This constructor creates the array, using _buffer_ (with _offset_ and [`strides`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.strides.html#numpy.char.chararray.strides "numpy.char.chararray.strides")
) if it is not `None`. If _buffer_ is `None`, then constructs a new array with [`strides`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.strides.html#numpy.char.chararray.strides "numpy.char.chararray.strides")
 in “C order”, unless both `len(shape) >= 2` and `order='F'`, in which case [`strides`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.strides.html#numpy.char.chararray.strides "numpy.char.chararray.strides")
 is in “Fortran order”.

Parameters:

**shape**tuple

Shape of the array.

**itemsize**int, optional

Length of each array element, in number of characters. Default is 1.

**unicode**bool, optional

Are the array elements of type unicode (True) or string (False). Default is False.

**buffer**object exposing the buffer interface or str, optional

Memory address of the start of the array data. Default is None, in which case a new array is created.

**offset**int, optional

Fixed stride displacement from the beginning of an axis? Default is 0. Needs to be >=0.

**strides**array\_like of ints, optional

Strides for the array (see [`strides`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.strides.html#numpy.ndarray.strides "numpy.ndarray.strides")
 for full description). Default is None.

**order**{‘C’, ‘F’}, optional

The order in which the array data is stored in memory: ‘C’ -> “row major” order (the default), ‘F’ -> “column major” (Fortran) order.

Attributes:

[`T`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.T.html#numpy.char.chararray.T "numpy.char.chararray.T")

View of the transposed array.

[`base`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.base.html#numpy.char.chararray.base "numpy.char.chararray.base")

Base object if memory is from some other object.

[`ctypes`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.ctypes.html#numpy.char.chararray.ctypes "numpy.char.chararray.ctypes")

An object to simplify the interaction of the array with the ctypes module.

[`data`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.data.html#numpy.char.chararray.data "numpy.char.chararray.data")

Python buffer object pointing to the start of the array’s data.

**device**

[`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.dtype.html#numpy.char.chararray.dtype "numpy.char.chararray.dtype")

Data-type of the array’s elements.

[`flags`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.flags.html#numpy.char.chararray.flags "numpy.char.chararray.flags")

Information about the memory layout of the array.

[`flat`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.flat.html#numpy.char.chararray.flat "numpy.char.chararray.flat")

A 1-D iterator over the array.

[`imag`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.imag.html#numpy.char.chararray.imag "numpy.char.chararray.imag")

The imaginary part of the array.

[`itemsize`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.itemsize.html#numpy.char.chararray.itemsize "numpy.char.chararray.itemsize")

Length of one array element in bytes.

[`mT`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.mT.html#numpy.char.chararray.mT "numpy.char.chararray.mT")

View of the matrix transposed array.

[`nbytes`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.nbytes.html#numpy.char.chararray.nbytes "numpy.char.chararray.nbytes")

Total bytes consumed by the elements of the array.

[`ndim`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.ndim.html#numpy.char.chararray.ndim "numpy.char.chararray.ndim")

Number of array dimensions.

[`real`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.real.html#numpy.char.chararray.real "numpy.char.chararray.real")

The real part of the array.

[`shape`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.shape.html#numpy.char.chararray.shape "numpy.char.chararray.shape")

Tuple of array dimensions.

[`size`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.size.html#numpy.char.chararray.size "numpy.char.chararray.size")

Number of elements in the array.

[`strides`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.strides.html#numpy.char.chararray.strides "numpy.char.chararray.strides")

Tuple of bytes to step in each dimension when traversing an array.

Methods

|     |     |
| --- | --- |
| [`astype`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.astype.html#numpy.char.chararray.astype "numpy.char.chararray.astype")<br>(dtype\[, order, casting, subok, copy\]) | Copy of the array, cast to a specified type. |
| [`argsort`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.argsort.html#numpy.char.chararray.argsort "numpy.char.chararray.argsort")<br>(\[axis, kind, order, stable, descending\]) | Returns the indices that would sort this array. |
| [`copy`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.copy.html#numpy.char.chararray.copy "numpy.char.chararray.copy")<br>(\[order\]) | Return a copy of the array. |
| [`count`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.count.html#numpy.char.chararray.count "numpy.char.chararray.count")<br>(sub\[, start, end\]) | Returns an array with the number of non-overlapping occurrences of substring _sub_ in the range \[_start_, _end_\]. |
| [`decode`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.decode.html#numpy.char.chararray.decode "numpy.char.chararray.decode")<br>(\[encoding, errors\]) | Calls `bytes.decode` element-wise. |
| [`dump`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.dump.html#numpy.char.chararray.dump "numpy.char.chararray.dump")<br>(file) | Dump a pickle of the array to the specified file. |
| [`dumps`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.dumps.html#numpy.char.chararray.dumps "numpy.char.chararray.dumps")<br>() | Returns the pickle of the array as a string. |
| [`encode`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.encode.html#numpy.char.chararray.encode "numpy.char.chararray.encode")<br>(\[encoding, errors\]) | Calls [`str.encode`](https://docs.python.org/3/library/stdtypes.html#str.encode "(in Python v3.14)")<br> element-wise. |
| [`endswith`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.endswith.html#numpy.char.chararray.endswith "numpy.char.chararray.endswith")<br>(suffix\[, start, end\]) | Returns a boolean array which is _True_ where the string element in _self_ ends with _suffix_, otherwise _False_. |
| [`expandtabs`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.expandtabs.html#numpy.char.chararray.expandtabs "numpy.char.chararray.expandtabs")<br>(\[tabsize\]) | Return a copy of each string element where all tab characters are replaced by one or more spaces. |
| [`fill`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.fill.html#numpy.char.chararray.fill "numpy.char.chararray.fill")<br>(value) | Fill the array with a scalar value. |
| [`find`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.find.html#numpy.char.chararray.find "numpy.char.chararray.find")<br>(sub\[, start, end\]) | For each element, return the lowest index in the string where substring _sub_ is found. |
| [`flatten`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.flatten.html#numpy.char.chararray.flatten "numpy.char.chararray.flatten")<br>(\[order\]) | Return a copy of the array collapsed into one dimension. |
| [`getfield`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.getfield.html#numpy.char.chararray.getfield "numpy.char.chararray.getfield")<br>(dtype\[, offset\]) | Returns a field of the given array as a certain type. |
| [`index`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.index.html#numpy.char.chararray.index "numpy.char.chararray.index")<br>(sub\[, start, end\]) | Like [`find`](https://numpy.org/doc/stable/reference/generated/numpy.char.find.html#numpy.char.find "numpy.char.find")<br>, but raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")<br> when the substring is not found. |
| [`isalnum`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.isalnum.html#numpy.char.chararray.isalnum "numpy.char.chararray.isalnum")<br>() | Returns true for each element if all characters in the string are alphanumeric and there is at least one character, false otherwise. |
| [`isalpha`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.isalpha.html#numpy.char.chararray.isalpha "numpy.char.chararray.isalpha")<br>() | Returns true for each element if all characters in the string are alphabetic and there is at least one character, false otherwise. |
| [`isdecimal`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.isdecimal.html#numpy.char.chararray.isdecimal "numpy.char.chararray.isdecimal")<br>() | For each element in _self_, return True if there are only decimal characters in the element. |
| [`isdigit`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.isdigit.html#numpy.char.chararray.isdigit "numpy.char.chararray.isdigit")<br>() | Returns true for each element if all characters in the string are digits and there is at least one character, false otherwise. |
| [`islower`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.islower.html#numpy.char.chararray.islower "numpy.char.chararray.islower")<br>() | Returns true for each element if all cased characters in the string are lowercase and there is at least one cased character, false otherwise. |
| [`isnumeric`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.isnumeric.html#numpy.char.chararray.isnumeric "numpy.char.chararray.isnumeric")<br>() | For each element in _self_, return True if there are only numeric characters in the element. |
| [`isspace`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.isspace.html#numpy.char.chararray.isspace "numpy.char.chararray.isspace")<br>() | Returns true for each element if there are only whitespace characters in the string and there is at least one character, false otherwise. |
| [`istitle`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.istitle.html#numpy.char.chararray.istitle "numpy.char.chararray.istitle")<br>() | Returns true for each element if the element is a titlecased string and there is at least one character, false otherwise. |
| [`isupper`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.isupper.html#numpy.char.chararray.isupper "numpy.char.chararray.isupper")<br>() | Returns true for each element if all cased characters in the string are uppercase and there is at least one character, false otherwise. |
| [`item`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.item.html#numpy.char.chararray.item "numpy.char.chararray.item")<br>(\*args) | Copy an element of an array to a standard Python scalar and return it. |
| [`join`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.join.html#numpy.char.chararray.join "numpy.char.chararray.join")<br>(seq) | Return a string which is the concatenation of the strings in the sequence _seq_. |
| [`ljust`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.ljust.html#numpy.char.chararray.ljust "numpy.char.chararray.ljust")<br>(width\[, fillchar\]) | Return an array with the elements of _self_ left-justified in a string of length _width_. |
| [`lower`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.lower.html#numpy.char.chararray.lower "numpy.char.chararray.lower")<br>() | Return an array with the elements of _self_ converted to lowercase. |
| [`lstrip`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.lstrip.html#numpy.char.chararray.lstrip "numpy.char.chararray.lstrip")<br>(\[chars\]) | For each element in _self_, return a copy with the leading characters removed. |
| [`nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.nonzero.html#numpy.char.chararray.nonzero "numpy.char.chararray.nonzero")<br>() | Return the indices of the elements that are non-zero. |
| [`put`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.put.html#numpy.char.chararray.put "numpy.char.chararray.put")<br>(indices, values\[, mode\]) | Set `a.flat[n] = values[n]` for all `n` in indices. |
| [`ravel`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.ravel.html#numpy.char.chararray.ravel "numpy.char.chararray.ravel")<br>(\[order\]) | Return a flattened array. |
| [`repeat`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.repeat.html#numpy.char.chararray.repeat "numpy.char.chararray.repeat")<br>(repeats\[, axis\]) | Repeat elements of an array. |
| [`replace`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.replace.html#numpy.char.chararray.replace "numpy.char.chararray.replace")<br>(old, new\[, count\]) | For each element in _self_, return a copy of the string with all occurrences of substring _old_ replaced by _new_. |
| [`reshape`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.reshape.html#numpy.char.chararray.reshape "numpy.char.chararray.reshape")<br>(a.reshape) | Returns an array containing the same data with a new shape. |
| [`resize`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.resize.html#numpy.char.chararray.resize "numpy.char.chararray.resize")<br>(a.resize) | Change shape and size of array in-place. |
| [`rfind`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.rfind.html#numpy.char.chararray.rfind "numpy.char.chararray.rfind")<br>(sub\[, start, end\]) | For each element in _self_, return the highest index in the string where substring _sub_ is found, such that _sub_ is contained within \[_start_, _end_\]. |
| [`rindex`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.rindex.html#numpy.char.chararray.rindex "numpy.char.chararray.rindex")<br>(sub\[, start, end\]) | Like [`rfind`](https://numpy.org/doc/stable/reference/generated/numpy.char.rfind.html#numpy.char.rfind "numpy.char.rfind")<br>, but raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")<br> when the substring _sub_ is not found. |
| [`rjust`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.rjust.html#numpy.char.chararray.rjust "numpy.char.chararray.rjust")<br>(width\[, fillchar\]) | Return an array with the elements of _self_ right-justified in a string of length _width_. |
| [`rsplit`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.rsplit.html#numpy.char.chararray.rsplit "numpy.char.chararray.rsplit")<br>(\[sep, maxsplit\]) | For each element in _self_, return a list of the words in the string, using _sep_ as the delimiter string. |
| [`rstrip`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.rstrip.html#numpy.char.chararray.rstrip "numpy.char.chararray.rstrip")<br>(\[chars\]) | For each element in _self_, return a copy with the trailing characters removed. |
| [`searchsorted`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.searchsorted.html#numpy.char.chararray.searchsorted "numpy.char.chararray.searchsorted")<br>(v\[, side, sorter\]) | Find indices where elements of _v_ should be inserted in _a_ to maintain order. |
| [`setfield`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.setfield.html#numpy.char.chararray.setfield "numpy.char.chararray.setfield")<br>(val, dtype\[, offset\]) | Put a value into a specified place in a field defined by a data-type. |
| [`setflags`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.setflags.html#numpy.char.chararray.setflags "numpy.char.chararray.setflags")<br>(\[write, align, uic\]) | Set array flags WRITEABLE, ALIGNED, WRITEBACKIFCOPY, respectively. |
| [`sort`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.sort.html#numpy.char.chararray.sort "numpy.char.chararray.sort")<br>(\[axis, kind, order, stable, descending\]) | Sort an array in-place. |
| [`split`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.split.html#numpy.char.chararray.split "numpy.char.chararray.split")<br>(\[sep, maxsplit\]) | For each element in _self_, return a list of the words in the string, using _sep_ as the delimiter string. |
| [`splitlines`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.splitlines.html#numpy.char.chararray.splitlines "numpy.char.chararray.splitlines")<br>(\[keepends\]) | For each element in _self_, return a list of the lines in the element, breaking at line boundaries. |
| [`squeeze`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.squeeze.html#numpy.char.chararray.squeeze "numpy.char.chararray.squeeze")<br>(\[axis\]) | Remove axes of length one from _a_. |
| [`startswith`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.startswith.html#numpy.char.chararray.startswith "numpy.char.chararray.startswith")<br>(prefix\[, start, end\]) | Returns a boolean array which is _True_ where the string element in _self_ starts with _prefix_, otherwise _False_. |
| [`strip`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.strip.html#numpy.char.chararray.strip "numpy.char.chararray.strip")<br>(\[chars\]) | For each element in _self_, return a copy with the leading and trailing characters removed. |
| [`swapaxes`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.swapaxes.html#numpy.char.chararray.swapaxes "numpy.char.chararray.swapaxes")<br>(axis1, axis2, /) | Return a view of the array with _axis1_ and _axis2_ interchanged. |
| [`swapcase`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.swapcase.html#numpy.char.chararray.swapcase "numpy.char.chararray.swapcase")<br>() | For each element in _self_, return a copy of the string with uppercase characters converted to lowercase and vice versa. |
| [`take`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.take.html#numpy.char.chararray.take "numpy.char.chararray.take")<br>(indices\[, axis, out, mode\]) | Return an array formed from the elements of _a_ at the given indices. |
| [`title`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.title.html#numpy.char.chararray.title "numpy.char.chararray.title")<br>() | For each element in _self_, return a titlecased version of the string: words start with uppercase characters, all remaining cased characters are lowercase. |
| [`tofile`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.tofile.html#numpy.char.chararray.tofile "numpy.char.chararray.tofile")<br>(fid, /\[, sep, format\]) | Write array to a file as text or binary (default). |
| [`tolist`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.tolist.html#numpy.char.chararray.tolist "numpy.char.chararray.tolist")<br>() | Return the array as an `a.ndim`\-levels deep nested list of Python scalars. |
| [`translate`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.translate.html#numpy.char.chararray.translate "numpy.char.chararray.translate")<br>(table\[, deletechars\]) | For each element in _self_, return a copy of the string where all characters occurring in the optional argument _deletechars_ are removed, and the remaining characters have been mapped through the given translation table. |
| [`transpose`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.transpose.html#numpy.char.chararray.transpose "numpy.char.chararray.transpose")<br>(\*axes) | Returns a view of the array with axes transposed. |
| [`upper`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.upper.html#numpy.char.chararray.upper "numpy.char.chararray.upper")<br>() | Return an array with the elements of _self_ converted to uppercase. |
| [`view`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.view.html#numpy.char.chararray.view "numpy.char.chararray.view")<br>(\[dtype\]\[, type\]) | New view of array with the same data. |
| [`zfill`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.zfill.html#numpy.char.chararray.zfill "numpy.char.chararray.zfill")<br>(width) | Return the numeric string left-filled with zeros in a string of length _width_. |

Examples

Try it in your browser!

\>>> import numpy as np
\>>> charar \= np.char.chararray((3, 3))
\>>> charar\[:\] \= 'a'
\>>> charar
chararray(\[\[b'a', b'a', b'a'\],\
           \[b'a', b'a', b'a'\],\
           \[b'a', b'a', b'a'\]\], dtype='|S1')

Copy to clipboard

\>>> charar \= np.char.chararray(charar.shape, itemsize\=5)
\>>> charar\[:\] \= 'abc'
\>>> charar
chararray(\[\[b'abc', b'abc', b'abc'\],\
           \[b'abc', b'abc', b'abc'\],\
           \[b'abc', b'abc', b'abc'\]\], dtype='|S5')

Copy to clipboard

Go BackOpen In Tab

On this page