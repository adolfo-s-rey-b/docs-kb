[Skip to main content](https://numpy.org/doc/stable/reference/typing.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/typing.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/typing.html)
[2.4](https://numpy.org/doc/2.4/reference/typing.html)
[2.3](https://numpy.org/doc/2.3/reference/typing.html)
[2.2](https://numpy.org/doc/2.2/reference/typing.html)
[2.1](https://numpy.org/doc/2.1/reference/typing.html)
[2.0](https://numpy.org/doc/2.0/reference/typing.html)
[1.26](https://numpy.org/doc/1.26/reference/typing.html)
[1.25](https://numpy.org/doc/1.25/reference/typing.html)
[1.24](https://numpy.org/doc/1.24/reference/typing.html)
[1.23](https://numpy.org/doc/1.23/reference/typing.html)
[1.22](https://numpy.org/doc/1.22/reference/typing.html)
[1.21](https://numpy.org/doc/1.21/reference/typing.html)
[1.20](https://numpy.org/doc/1.20/reference/typing.html)
[1.19](https://numpy.org/doc/1.19/reference/typing.html)
[1.18](https://numpy.org/doc/1.18/reference/typing.html)
[1.17](https://numpy.org/doc/1.17/reference/typing.html)
[1.16](https://numpy.org/doc/1.16/reference/typing.html)
[1.15](https://numpy.org/doc/1.15/reference/typing.html)
[1.14](https://numpy.org/doc/1.14/reference/typing.html)
[1.13](https://numpy.org/doc/1.13/reference/typing.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Typing ([`numpy.typing`](https://numpy.org/doc/stable/reference/typing.html#module-numpy.typing "numpy.typing")
)[#](https://numpy.org/doc/stable/reference/typing.html#typing-numpy-typing "Link to this heading")

====================================================================================================================================================================================================================

New in version 1.20.

Large parts of the NumPy API have [**PEP 484**](https://peps.python.org/pep-0484/)
\-style type annotations. In addition a number of type aliases are available to users, most prominently the two below:

*   [`ArrayLike`](https://numpy.org/doc/stable/reference/typing.html#numpy.typing.ArrayLike "numpy.typing.ArrayLike")
    : objects that can be converted to arrays
    
*   [`DTypeLike`](https://numpy.org/doc/stable/reference/typing.html#numpy.typing.DTypeLike "numpy.typing.DTypeLike")
    : objects that can be converted to dtypes
    

Mypy plugin[#](https://numpy.org/doc/stable/reference/typing.html#mypy-plugin "Link to this heading")

------------------------------------------------------------------------------------------------------

New in version 1.21.

A [mypy](https://mypy-lang.org/)
 plugin for managing a number of platform-specific annotations. Its functionality can be split into three distinct parts:

*   Assigning the (platform-dependent) precisions of certain [`number`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.number "numpy.number")
     subclasses, including the likes of [`int_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int_ "numpy.int_")
    , [`intp`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.intp "numpy.intp")
     and [`longlong`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.longlong "numpy.longlong")
    . See the documentation on [scalar types](https://numpy.org/doc/stable/reference/arrays.scalars.html#arrays-scalars-built-in)
     for a comprehensive overview of the affected classes. Without the plugin the precision of all relevant classes will be inferred as [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")
    .
    
*   Removing all extended-precision [`number`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.number "numpy.number")
     subclasses that are unavailable for the platform in question. Most notably this includes the likes of [`float128`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float128 "numpy.float128")
     and [`complex256`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.complex256 "numpy.complex256")
    . Without the plugin _all_ extended-precision types will, as far as mypy is concerned, be available to all platforms.
    
*   Assigning the (platform-dependent) precision of [`c_intp`](https://numpy.org/doc/stable/reference/routines.ctypeslib.html#numpy.ctypeslib.c_intp "numpy.ctypeslib.c_intp")
    . Without the plugin the type will default to [`ctypes.c_int64`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int64 "(in Python v3.14)")
    .
    
    New in version 1.22.
    

Deprecated since version 2.3: The [`numpy.typing.mypy_plugin`](https://numpy.org/doc/stable/reference/typing.html#module-numpy.typing.mypy_plugin "numpy.typing.mypy_plugin")
 entry-point is deprecated in favor of platform-agnostic static type inference. Remove `numpy.typing.mypy_plugin` from the `plugins` section of your mypy configuration; if that surfaces new errors, please open an issue with a minimal reproducer.

### Examples[#](https://numpy.org/doc/stable/reference/typing.html#examples "Link to this heading")

To enable the plugin, one must add it to their mypy [configuration file](https://mypy.readthedocs.io/en/stable/config_file.html)
:

\[mypy\]
plugins \= numpy.typing.mypy\_plugin

Copy to clipboard

Differences from the runtime NumPy API[#](https://numpy.org/doc/stable/reference/typing.html#differences-from-the-runtime-numpy-api "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

NumPy is very flexible. Trying to describe the full range of possibilities statically would result in types that are not very helpful. For that reason, the typed NumPy API is often stricter than the runtime NumPy API. This section describes some notable differences.

### ArrayLike[#](https://numpy.org/doc/stable/reference/typing.html#arraylike "Link to this heading")

The [`ArrayLike`](https://numpy.org/doc/stable/reference/typing.html#numpy.typing.ArrayLike "numpy.typing.ArrayLike")
 type tries to avoid creating object arrays. For example,

\>>> np.array(x\*\*2 for x in range(10))
array(<generator object <genexpr> at ...>, dtype=object)

Copy to clipboard

is valid NumPy code which will create a 0-dimensional object array. Type checkers will complain about the above example when using the NumPy types however. If you really intended to do the above, then you can either use a `# type: ignore` comment:

\>>> np.array(x\*\*2 for x in range(10))  \# type: ignore

Copy to clipboard

or explicitly type the array like object as [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")
:

\>>> from typing import Any
\>>> array\_like: Any \= (x\*\*2 for x in range(10))
\>>> np.array(array\_like)
array(<generator object <genexpr> at ...>, dtype=object)

Copy to clipboard

### DTypeLike[#](https://numpy.org/doc/stable/reference/typing.html#dtypelike "Link to this heading")

The [`DTypeLike`](https://numpy.org/doc/stable/reference/typing.html#numpy.typing.DTypeLike "numpy.typing.DTypeLike")
 type tries to avoid creation of dtype objects using dictionary of fields like below:

\>>> x \= np.dtype({"field1": (float, 1), "field2": (int, 3)})

Copy to clipboard

Although this is valid NumPy code, the type checker will complain about it, since its usage is discouraged. Please see : [Data type objects](https://numpy.org/doc/stable/reference/arrays.dtypes.html#arrays-dtypes)

### Number precision[#](https://numpy.org/doc/stable/reference/typing.html#number-precision "Link to this heading")

The precision of [`numpy.number`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.number "numpy.number")
 subclasses is treated as an invariant generic parameter (see [`NBitBase`](https://numpy.org/doc/stable/reference/typing.html#numpy.typing.NBitBase "numpy.typing.NBitBase")
), simplifying the annotating of processes involving precision-based casting.

\>>> from typing import TypeVar
\>>> import numpy as np
\>>> import numpy.typing as npt

\>>> T \= TypeVar("T", bound\=npt.NBitBase)
\>>> def func(a: np.floating\[T\], b: np.floating\[T\]) \-> np.floating\[T\]:
...     ...

Copy to clipboard

Consequently, the likes of [`float16`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float16 "numpy.float16")
, [`float32`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32 "numpy.float32")
 and [`float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 are still sub-types of [`floating`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.floating "numpy.floating")
, but, contrary to runtime, they’re not necessarily considered as sub-classes.

Deprecated since version 2.3: The [`NBitBase`](https://numpy.org/doc/stable/reference/typing.html#numpy.typing.NBitBase "numpy.typing.NBitBase")
 helper is deprecated and will be removed in a future release. Prefer expressing precision relationships via `typing.overload` or `TypeVar` definitions bounded by concrete scalar classes. For example:

> from typing import TypeVar
> import numpy as np
> 
> S \= TypeVar("S", bound\=np.floating)
> 
> def func(a: S, b: S) \-> S:
>     ...
> 
> Copy to clipboard
> 
> or in the case of different input types mapping to different output types:

from typing import overload
import numpy as np

@overload
def phase(x: np.complex64) \-> np.float32: ...
@overload
def phase(x: np.complex128) \-> np.float64: ...
@overload
def phase(x: np.clongdouble) \-> np.longdouble: ...
def phase(x: np.complexfloating) \-> np.floating:
    ...

Copy to clipboard

### Timedelta64[#](https://numpy.org/doc/stable/reference/typing.html#timedelta64 "Link to this heading")

The [`timedelta64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "numpy.timedelta64")
 class is not considered a subclass of [`signedinteger`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.signedinteger "numpy.signedinteger")
, the former only inheriting from [`generic`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.generic "numpy.generic")
 while static type checking.

### Record array dtypes[#](https://numpy.org/doc/stable/reference/typing.html#record-array-dtypes "Link to this heading")

The dtype of [`numpy.recarray`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.html#numpy.recarray "numpy.recarray")
, and the [Creating record arrays](https://numpy.org/doc/stable/reference/routines.array-creation.html#routines-array-creation-rec)
 functions in general, can be specified in one of two ways:

*   Directly via the `dtype` argument.
    
*   With up to five helper arguments that operate via [`numpy.rec.format_parser`](https://numpy.org/doc/stable/reference/generated/numpy.rec.format_parser.html#numpy.rec.format_parser "numpy.rec.format_parser")
    : `formats`, `names`, `titles`, `aligned` and `byteorder`.
    

These two approaches are currently typed as being mutually exclusive, _i.e._ if `dtype` is specified than one may not specify `formats`. While this mutual exclusivity is not (strictly) enforced during runtime, combining both dtype specifiers can lead to unexpected or even downright buggy behavior.

API[#](https://numpy.org/doc/stable/reference/typing.html#api "Link to this heading")

--------------------------------------------------------------------------------------

ndarray

The [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 class is a [generic type](https://typing.python.org/en/latest/spec/generics.html)
 that accepts two type arguments:

1.  The type of [`numpy.ndarray.shape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html#numpy.ndarray.shape "numpy.ndarray.shape")
    , which must be a _tuple_ of _int_, e.g. `tuple[int, int]` (2-D shape) or `tuple[()]` (0-D shape). The default shape is `tuple[Any, ...]`, which represents an unknown shape with _any_ number of dimensions. Currently, `Literal` ints or other more specific types are not supported.
    
2.  The type of [`numpy.ndarray.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.dtype.html#numpy.ndarray.dtype "numpy.ndarray.dtype")
    , which must be a subtype of [`numpy.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
     such as `numpy.dtype[numpy.float64]`. If omitted, it will default to `numpy.dtype[Any]`.
    

\>>> import numpy as np

\>>> type ImageRGB \= np.ndarray\[tuple\[int, int, int\], np.dtype\[np.uint8\]\]
\>>> type Vector\[S: np.generic\] \= np.ndarray\[tuple\[int\], np.dtype\[S\]\]

Copy to clipboard

numpy.typing.ArrayLike _\= typing.Union\[...\]_[#](https://numpy.org/doc/stable/reference/typing.html#numpy.typing.ArrayLike "Link to this definition")

A [`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.14)")
 representing objects that can be coerced into an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.

Among others this includes the likes of:

*   Scalars.
    
*   (Nested) sequences.
    
*   Objects implementing the _\_\_array\_\__ protocol.
    

New in version 1.20.

See Also

[array\_like](https://numpy.org/doc/stable/glossary.html#term-array_like)
:

Any scalar or sequence that can be interpreted as an ndarray.

Examples

Try it in your browser!

> \>>> import numpy as np
> \>>> import numpy.typing as npt
> 
> \>>> def as\_array(a: npt.ArrayLike) \-> np.ndarray:
> ...     return np.array(a)
> 
> Copy to clipboard

numpy.typing.DTypeLike _\= typing.Union\[...\]_[#](https://numpy.org/doc/stable/reference/typing.html#numpy.typing.DTypeLike "Link to this definition")

A [`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.14)")
 representing objects that can be coerced into a [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
.

Among others this includes the likes of:

*   [`type`](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")
     objects.
    
*   Character codes or the names of [`type`](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")
     objects.
    
*   Objects with the `.dtype` attribute.
    

New in version 1.20.

See Also

[Specifying and constructing data types](https://numpy.org/doc/stable/reference/arrays.dtypes.html#arrays-dtypes-constructing)

A comprehensive overview of all objects that can be coerced into data types.

Examples

\>>> import numpy as np
\>>> import numpy.typing as npt

\>>> def as\_dtype(d: npt.DTypeLike) \-> np.dtype:
...     return np.dtype(d)

Copy to clipboard

numpy.typing.NDArray _\= NDArray_[#](https://numpy.org/doc/stable/reference/typing.html#numpy.typing.NDArray "Link to this definition")

A [`np.ndarray[tuple[Any, ...], np.dtype[ScalarT]]`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 type alias [generic](https://docs.python.org/3/glossary.html#term-generic-type "(in Python v3.14)")
 w.r.t. its [`dtype.type`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.type.html#numpy.dtype.type "numpy.dtype.type")
.

Can be used during runtime for typing arrays with a given dtype and unspecified shape.

New in version 1.21.

Examples

\>>> import numpy as np
\>>> import numpy.typing as npt

\>>> print(npt.NDArray)
NDArray

\>>> print(npt.NDArray\[np.float64\])
NDArray\[numpy.float64\]

\>>> NDArrayInt \= npt.NDArray\[np.int\_\]
\>>> a: NDArrayInt \= np.arange(10)

\>>> def func(a: npt.ArrayLike) \-> npt.NDArray\[Any\]:
...     return np.array(a)

Copy to clipboard

_class_ numpy.typing.NBitBase[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_typing/_nbit_base.py#L7-L62)
[#](https://numpy.org/doc/stable/reference/typing.html#numpy.typing.NBitBase "Link to this definition")

A type representing [`numpy.number`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.number "numpy.number")
 precision during static type checking.

Used exclusively for the purpose of static type checking, [`NBitBase`](https://numpy.org/doc/stable/reference/typing.html#numpy.typing.NBitBase "numpy.typing.NBitBase")
 represents the base of a hierarchical set of subclasses. Each subsequent subclass is herein used for representing a lower level of precision, _e.g._ `64Bit > 32Bit > 16Bit`.

New in version 1.20.

Deprecated since version 2.3: Use `@typing.overload` or a `TypeVar` with a scalar-type as upper bound, instead.

Examples

Try it in your browser!

Below is a typical usage example: [`NBitBase`](https://numpy.org/doc/stable/reference/typing.html#numpy.typing.NBitBase "numpy.typing.NBitBase")
 is herein used for annotating a function that takes a float and integer of arbitrary precision as arguments and returns a new float of whichever precision is largest (_e.g._ `np.float16 + np.int64 -> np.float64`).

\>>> from typing import TYPE\_CHECKING
\>>> import numpy as np
\>>> import numpy.typing as npt

\>>> def add\[S: npt.NBitBase, T: npt.NBitBase\](
...     a: np.floating\[S\], b: np.integer\[T\]
... ) \-> np.floating\[S | T\]:
...     return a + b

\>>> a \= np.float16()
\>>> b \= np.int64()
\>>> out \= add(a, b)

\>>> if TYPE\_CHECKING:
...     reveal\_locals()
...     \# note: Revealed local types are:
...     \# note:     a: numpy.floating\[numpy.typing.\_16Bit\*\]
...     \# note:     b: numpy.signedinteger\[numpy.typing.\_64Bit\*\]
...     \# note:     out: numpy.floating\[numpy.typing.\_64Bit\*\]

Copy to clipboard

Go BackOpen In Tab

Go BackOpen In Tab

On this page