[Skip to main content](https://numpy.org/doc/stable/reference/arrays.classes.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/arrays.classes.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/arrays.classes.html)
[2.4](https://numpy.org/doc/2.4/reference/arrays.classes.html)
[2.3](https://numpy.org/doc/2.3/reference/arrays.classes.html)
[2.2](https://numpy.org/doc/2.2/reference/arrays.classes.html)
[2.1](https://numpy.org/doc/2.1/reference/arrays.classes.html)
[2.0](https://numpy.org/doc/2.0/reference/arrays.classes.html)
[1.26](https://numpy.org/doc/1.26/reference/arrays.classes.html)
[1.25](https://numpy.org/doc/1.25/reference/arrays.classes.html)
[1.24](https://numpy.org/doc/1.24/reference/arrays.classes.html)
[1.23](https://numpy.org/doc/1.23/reference/arrays.classes.html)
[1.22](https://numpy.org/doc/1.22/reference/arrays.classes.html)
[1.21](https://numpy.org/doc/1.21/reference/arrays.classes.html)
[1.20](https://numpy.org/doc/1.20/reference/arrays.classes.html)
[1.19](https://numpy.org/doc/1.19/reference/arrays.classes.html)
[1.18](https://numpy.org/doc/1.18/reference/arrays.classes.html)
[1.17](https://numpy.org/doc/1.17/reference/arrays.classes.html)
[1.16](https://numpy.org/doc/1.16/reference/arrays.classes.html)
[1.15](https://numpy.org/doc/1.15/reference/arrays.classes.html)
[1.14](https://numpy.org/doc/1.14/reference/arrays.classes.html)
[1.13](https://numpy.org/doc/1.13/reference/arrays.classes.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Standard array subclasses[#](https://numpy.org/doc/stable/reference/arrays.classes.html#standard-array-subclasses "Link to this heading")

==========================================================================================================================================

Note

Subclassing a `numpy.ndarray` is possible but if your goal is to create an array with _modified_ behavior, as do dask arrays for distributed computation and cupy arrays for GPU-based computation, subclassing is discouraged. Instead, using numpy’s [dispatch mechanism](https://numpy.org/doc/stable/user/basics.dispatch.html#basics-dispatch)
 is recommended.

The [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 can be inherited from (in Python or in C) if desired. Therefore, it can form a foundation for many useful classes. Often whether to sub-class the array object or to simply use the core array component as an internal part of a new class is a difficult decision, and can be simply a matter of choice. NumPy has several tools for simplifying how your new object interacts with other array objects, and so the choice may not be significant in the end. One way to simplify the question is by asking yourself if the object you are interested in can be replaced as a single array or does it really require two or more arrays at its core.

Note that [`asarray`](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
 always returns the base-class ndarray. If you are confident that your use of the array object can handle any subclass of an ndarray, then [`asanyarray`](https://numpy.org/doc/stable/reference/generated/numpy.asanyarray.html#numpy.asanyarray "numpy.asanyarray")
 can be used to allow subclasses to propagate more cleanly through your subroutine. In principle, a subclass could redefine any aspect of the array and therefore, under strict guidelines, [`asanyarray`](https://numpy.org/doc/stable/reference/generated/numpy.asanyarray.html#numpy.asanyarray "numpy.asanyarray")
 would rarely be useful. However, most subclasses of the array object will not redefine certain aspects of the array object such as the buffer interface, or the attributes of the array. One important example, however, of why your subroutine may not be able to handle an arbitrary subclass of an array is that matrices redefine the “\*” operator to be matrix-multiplication, rather than element-by-element multiplication.

Special attributes and methods[#](https://numpy.org/doc/stable/reference/arrays.classes.html#special-attributes-and-methods "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

See also

[Subclassing ndarray](https://numpy.org/doc/stable/user/basics.subclassing.html#basics-subclassing)

NumPy provides several hooks that classes can customize:

class.\_\_array\_ufunc\_\_(_ufunc_, _method_, _\*inputs_, _\*\*kwargs_)[#](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_ufunc__ "Link to this definition")

Any class, ndarray subclass or not, can define this method or set it to None in order to override the behavior of NumPy’s ufuncs. This works quite similarly to Python’s `__mul__` and other binary operation routines.

*   _ufunc_ is the ufunc object that was called.
    
*   _method_ is a string indicating which Ufunc method was called (one of `"__call__"`, `"reduce"`, `"reduceat"`, `"accumulate"`, `"outer"`, `"inner"`).
    
*   _inputs_ is a tuple of the input arguments to the `ufunc`.
    
*   _kwargs_ is a dictionary containing the optional input arguments of the ufunc. If given, any `out` arguments, both positional and keyword, are passed as a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")
     in _kwargs_. See the discussion in [Universal functions (ufunc)](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs)
     for details.
    

The method should return either the result of the operation, or [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "(in Python v3.14)")
 if the operation requested is not implemented.

If one of the input, output, or `where` arguments has a [`__array_ufunc__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_ufunc__ "numpy.class.__array_ufunc__")
 method, it is executed _instead_ of the ufunc. If more than one of the arguments implements [`__array_ufunc__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_ufunc__ "numpy.class.__array_ufunc__")
, they are tried in the order: subclasses before superclasses, inputs before outputs, outputs before `where`, otherwise left to right. The first routine returning something other than [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "(in Python v3.14)")
 determines the result. If all of the [`__array_ufunc__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_ufunc__ "numpy.class.__array_ufunc__")
 operations return [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "(in Python v3.14)")
, a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
 is raised.

Note

We intend to re-implement numpy functions as (generalized) Ufunc, in which case it will become possible for them to be overridden by the `__array_ufunc__` method. A prime candidate is [`matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html#numpy.matmul "numpy.matmul")
, which currently is not a Ufunc, but could be relatively easily be rewritten as a (set of) generalized Ufuncs. The same may happen with functions such as [`median`](https://numpy.org/doc/stable/reference/generated/numpy.median.html#numpy.median "numpy.median")
, [`amin`](https://numpy.org/doc/stable/reference/generated/numpy.amin.html#numpy.amin "numpy.amin")
, and [`argsort`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")
.

Like with some other special methods in python, such as `__hash__` and `__iter__`, it is possible to indicate that your class does _not_ support ufuncs by setting `__array_ufunc__ = None`. Ufuncs always raise [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
 when called on an object that sets `__array_ufunc__ = None`.

The presence of [`__array_ufunc__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_ufunc__ "numpy.class.__array_ufunc__")
 also influences how [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 handles binary operations like `arr + obj` and `arr < obj` when `arr` is an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 and `obj` is an instance of a custom class. There are two possibilities. If `obj.__array_ufunc__` is present and not None, then `ndarray.__add__` and friends will delegate to the ufunc machinery, meaning that `arr + obj` becomes `np.add(arr, obj)`, and then [`add`](https://numpy.org/doc/stable/reference/generated/numpy.add.html#numpy.add "numpy.add")
 invokes `obj.__array_ufunc__`. This is useful if you want to define an object that acts like an array.

Alternatively, if `obj.__array_ufunc__` is set to None, then as a special case, special methods like `ndarray.__add__` will notice this and _unconditionally_ raise [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
. This is useful if you want to create objects that interact with arrays via binary operations, but are not themselves arrays. For example, a units handling system might have an object `m` representing the “meters” unit, and want to support the syntax `arr * m` to represent that the array has units of “meters”, but not want to otherwise interact with arrays via ufuncs or otherwise. This can be done by setting `__array_ufunc__ = None` and defining `__mul__` and `__rmul__` methods. (Note that this means that writing an `__array_ufunc__` that always returns [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "(in Python v3.14)")
 is not quite the same as setting `__array_ufunc__ = None`: in the former case, `arr + obj` will raise [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
, while in the latter case it is possible to define a `__radd__` method to prevent this.)

The above does not hold for in-place operators, for which [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 never returns [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "(in Python v3.14)")
. Hence, `arr += obj` would always lead to a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
. This is because for arrays in-place operations cannot generically be replaced by a simple reverse operation. (For instance, by default, `arr += obj` would be translated to `arr = arr + obj`, i.e., `arr` would be replaced, contrary to what is expected for in-place array operations.)

Note

If you define `__array_ufunc__`:

*   If you are not a subclass of [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
    , we recommend your class define special methods like `__add__` and `__lt__` that delegate to ufuncs just like ndarray does. An easy way to do this is to subclass from [`NDArrayOperatorsMixin`](https://numpy.org/doc/stable/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html#numpy.lib.mixins.NDArrayOperatorsMixin "numpy.lib.mixins.NDArrayOperatorsMixin")
    .
    
*   If you subclass [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
    , we recommend that you put all your override logic in `__array_ufunc__` and not also override special methods. This ensures the class hierarchy is determined in only one place rather than separately by the ufunc machinery and by the binary operation rules (which gives preference to special methods of subclasses; the alternative way to enforce a one-place only hierarchy, of setting [`__array_ufunc__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_ufunc__ "numpy.class.__array_ufunc__")
     to None, would seem very unexpected and thus confusing, as then the subclass would not work at all with ufuncs).
    
*   [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
     defines its own [`__array_ufunc__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_ufunc__ "numpy.class.__array_ufunc__")
    , which, evaluates the ufunc if no arguments have overrides, and returns [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "(in Python v3.14)")
     otherwise. This may be useful for subclasses for which [`__array_ufunc__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_ufunc__ "numpy.class.__array_ufunc__")
     converts any instances of its own class to [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
    : it can then pass these on to its superclass using `super().__array_ufunc__(*inputs, **kwargs)`, and finally return the results after possible back-conversion. The advantage of this practice is that it ensures that it is possible to have a hierarchy of subclasses that extend the behaviour. See [Subclassing ndarray](https://numpy.org/doc/stable/user/basics.subclassing.html#basics-subclassing)
     for details.
    

class.\_\_array\_function\_\_(_func_, _types_, _args_, _kwargs_)[#](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_function__ "Link to this definition")

*   `func` is an arbitrary callable exposed by NumPy’s public API, which was called in the form `func(*args, **kwargs)`.
    
*   `types` is a collection [`collections.abc.Collection`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection "(in Python v3.14)")
     of unique argument types from the original NumPy function call that implement `__array_function__`.
    
*   The tuple `args` and dict `kwargs` are directly passed on from the original call.
    

As a convenience for `__array_function__` implementers, `types` provides all argument types with an `'__array_function__'` attribute. This allows implementers to quickly identify cases where they should defer to `__array_function__` implementations on other arguments. Implementations should not rely on the iteration order of `types`.

Most implementations of `__array_function__` will start with two checks:

1.  Is the given function something that we know how to overload?
    
2.  Are all arguments of a type that we know how to handle?
    

If these conditions hold, `__array_function__` should return the result from calling its implementation for `func(*args, **kwargs)`. Otherwise, it should return the sentinel value `NotImplemented`, indicating that the function is not implemented by these types.

There are no general requirements on the return value from `__array_function__`, although most sensible implementations should probably return array(s) with the same type as one of the function’s arguments.

It may also be convenient to define a custom decorators (`implements` below) for registering `__array_function__` implementations.

HANDLED\_FUNCTIONS \= {}

class MyArray:
    def \_\_array\_function\_\_(self, func, types, args, kwargs):
        if func not in HANDLED\_FUNCTIONS:
            return NotImplemented
        \# Note: this allows subclasses that don't override
        \# \_\_array\_function\_\_ to handle MyArray objects
        if not all(issubclass(t, MyArray) for t in types):
            return NotImplemented
        return HANDLED\_FUNCTIONS\[func\](\*args, \*\*kwargs)

def implements(numpy\_function):
    """Register an \_\_array\_function\_\_ implementation for MyArray objects."""
    def decorator(func):
        HANDLED\_FUNCTIONS\[numpy\_function\] \= func
        return func
    return decorator

@implements(np.concatenate)
def concatenate(arrays, axis\=0, out\=None):
    ...  \# implementation of concatenate for MyArray objects

@implements(np.broadcast\_to)
def broadcast\_to(array, shape):
    ...  \# implementation of broadcast\_to for MyArray objects

Copy to clipboard

Note that it is not required for `__array_function__` implementations to include _all_ of the corresponding NumPy function’s optional arguments (e.g., `broadcast_to` above omits the irrelevant `subok` argument). Optional arguments are only passed in to `__array_function__` if they were explicitly used in the NumPy function call.

Just like the case for builtin special methods like `__add__`, properly written `__array_function__` methods should always return `NotImplemented` when an unknown type is encountered. Otherwise, it will be impossible to correctly override NumPy functions from another object if the operation also includes one of your objects.

For the most part, the rules for dispatch with `__array_function__` match those for `__array_ufunc__`. In particular:

*   NumPy will gather implementations of `__array_function__` from all specified inputs and call them in order: subclasses before superclasses, and otherwise left to right. Note that in some edge cases involving subclasses, this differs slightly from the [current behavior](https://bugs.python.org/issue30140)
     of Python.
    
*   Implementations of `__array_function__` indicate that they can handle the operation by returning any value other than `NotImplemented`.
    
*   If all `__array_function__` methods return `NotImplemented`, NumPy will raise `TypeError`.
    

If no `__array_function__` methods exists, NumPy will default to calling its own implementation, intended for use on NumPy arrays. This case arises, for example, when all array-like arguments are Python numbers or lists. (NumPy arrays do have a `__array_function__` method, given below, but it always returns `NotImplemented` if any argument other than a NumPy array subclass implements `__array_function__`.)

One deviation from the current behavior of `__array_ufunc__` is that NumPy will only call `__array_function__` on the _first_ argument of each unique type. This matches Python’s [rule for calling reflected methods](https://docs.python.org/3/reference/datamodel.html#object.__ror__)
, and this ensures that checking overloads has acceptable performance even when there are a large number of overloaded arguments.

class.\_\_array\_finalize\_\_(_obj_)[#](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_finalize__ "Link to this definition")

This method is called whenever the system internally allocates a new array from _obj_, where _obj_ is a subclass (subtype) of the [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
. It can be used to change attributes of _self_ after construction (so as to ensure a 2-d matrix for example), or to update meta-information from the “parent.” Subclasses inherit a default implementation of this method that does nothing.

class.\_\_array\_wrap\_\_(_array_, _context\=None_, _return\_scalar\=False_)[#](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_wrap__ "Link to this definition")

At the end of every [ufunc](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-output-type)
, this method is called on the input object with the highest array priority, or the output object if one was specified. The ufunc-computed array is passed in and whatever is returned is passed to the user. Subclasses inherit a default implementation of this method, which transforms the array into a new instance of the object’s class. Subclasses may opt to use this method to transform the output array into an instance of the subclass and update metadata before returning the array to the user.

NumPy may also call this function without a context from non-ufuncs to allow preserving subclass information.

Changed in version 2.0: `return_scalar` is now passed as either `False` (usually) or `True` indicating that NumPy would return a scalar. Subclasses may ignore the value, or return `array[()]` to behave more like NumPy.

Note

It is hoped to eventually deprecate this method in favour of [`__array_ufunc__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_ufunc__ "numpy.class.__array_ufunc__")
 for ufuncs (and [`__array_function__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_function__ "numpy.class.__array_function__")
 for a few other functions like [`numpy.squeeze`](https://numpy.org/doc/stable/reference/generated/numpy.squeeze.html#numpy.squeeze "numpy.squeeze")
).

class.\_\_array\_priority\_\_[#](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_priority__ "Link to this definition")

The value of this attribute is used to determine what type of object to return in situations where there is more than one possibility for the Python type of the returned object. Subclasses inherit a default value of 0.0 for this attribute.

Note

For ufuncs, it is hoped to eventually deprecate this method in favour of [`__array_ufunc__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_ufunc__ "numpy.class.__array_ufunc__")
.

class.\_\_array\_\_(_dtype\=None_, _copy\=None_)[#](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array__ "Link to this definition")

If defined on an object, it must return a NumPy `ndarray`. This method is called by array-coercion functions like `np.array()` if an object implementing this interface is passed to those functions.

Third-party implementations of `__array__` must take `dtype` and `copy` arguments.

Deprecated since version NumPy: 2.0 Not implementing `copy` and `dtype` is deprecated as of NumPy 2. When adding them, you must ensure correct behavior for `copy`.

*   `dtype` is the requested data type of the returned array and is passed by NumPy positionally (only if requested by the user). It is acceptable to ignore the `dtype` because NumPy will check the result and cast to `dtype` if necessary. If it is more efficient to coerce the data to the requested dtype without relying on NumPy, you should handle it in your library.
    
*   `copy` is a boolean passed by keyword. If `copy=True` you _must_ return a copy. Returning a view into existing data will lead to incorrect user code. If `copy=False` the user requested that a copy is never made and you _must_ raise an error unless no copy is made and the returned array is a view into existing data. It is valid to always raise an error for `copy=False`. The default `copy=None` (not passed) allows for the result to either be a view or a copy. However, a view return should be preferred when possible.
    

Please refer to [Interoperability with NumPy](https://numpy.org/doc/stable/user/basics.interoperability.html#basics-interoperability)
 for the protocol hierarchy, of which `__array__` is the oldest and least desirable.

Note

If a class (ndarray subclass or not) having the [`__array__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array__ "numpy.class.__array__")
 method is used as the output object of an [ufunc](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-output-type)
, results will _not_ be written to the object returned by [`__array__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array__ "numpy.class.__array__")
. This practice will return `TypeError`.

**Example**

Use `__array__` to create a diagonal array of fixed size and value:

\>>> import numpy as np
\>>> class DiagonalArray:
...     def \_\_init\_\_(self, N, value):
...         self.\_N \= N
...         self.\_i \= value
...     def \_\_repr\_\_(self):
...         return f"{self.\_\_class\_\_.\_\_name\_\_}(N={self.\_N}, value={self.\_i})"
...     def \_\_array\_\_(self, dtype\=None, copy\=None):
...         if copy is False:
...             raise ValueError(
...                 "\`copy=False\` isn't supported. A copy is always created."
...             )
...         return self.\_i \* np.eye(self.\_N, dtype\=dtype)

Copy to clipboard

Our custom array can be instantiated like:

\>>> arr \= DiagonalArray(5, 1)
\>>> arr
DiagonalArray(N=5, value=1)

Copy to clipboard

We can convert to a numpy array using [`numpy.array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
 or [`numpy.asarray`](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
, which will call its `__array__` method to obtain a standard `numpy.ndarray`.

\>>> np.asarray(arr)
array(\[\[1., 0., 0., 0., 0.\],\
       \[0., 1., 0., 0., 0.\],\
       \[0., 0., 1., 0., 0.\],\
       \[0., 0., 0., 1., 0.\],\
       \[0., 0., 0., 0., 1.\]\])

Copy to clipboard

Using `dtype` should return an appropriate ndarray or raise an error:

\>>> np.asarray(arr, dtype\=np.float32)
array(\[\[1., 0., 0., 0., 0.\],\
       \[0., 1., 0., 0., 0.\],\
       \[0., 0., 1., 0., 0.\],\
       \[0., 0., 0., 1., 0.\],\
       \[0., 0., 0., 0., 1.\]\], dtype=float32)

Copy to clipboard

If we operate on `arr` with a numpy function, numpy will again use the `__array__` interface to convert it to an array and then apply the function in the usual way.

\>>> np.multiply(arr, 2)
array(\[\[2., 0., 0., 0., 0.\],\
       \[0., 2., 0., 0., 0.\],\
       \[0., 0., 2., 0., 0.\],\
       \[0., 0., 0., 2., 0.\],\
       \[0., 0., 0., 0., 2.\]\])

Copy to clipboard

Notice that the return type is a standard `numpy.ndarray`.

\>>> type(np.multiply(arr, 2))
<class 'numpy.ndarray'>

Copy to clipboard

Matrix objects[#](https://numpy.org/doc/stable/reference/arrays.classes.html#matrix-objects "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

Note

It is strongly advised _not_ to use the matrix subclass. As described below, it makes writing functions that deal consistently with matrices and regular arrays very difficult. Currently, they are mainly used for interacting with `scipy.sparse`. We hope to provide an alternative for this use, however, and eventually remove the `matrix` subclass.

[`matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "numpy.matrix")
 objects inherit from the ndarray and therefore, they have the same attributes and methods of ndarrays. There are six important differences of matrix objects, however, that may lead to unexpected results when you use matrices but expect them to act like arrays:

1.  Matrix objects can be created using a string notation to allow Matlab-style syntax where spaces separate columns and semicolons (‘;’) separate rows.
    
2.  Matrix objects are always two-dimensional. This has far-reaching implications, in that m.ravel() is still two-dimensional (with a 1 in the first dimension) and item selection returns two-dimensional objects so that sequence behavior is fundamentally different than arrays.
    
3.  Matrix objects over-ride multiplication to be matrix-multiplication. **Make sure you understand this for functions that you may want to receive matrices. Especially in light of the fact that asanyarray(m) returns a matrix when m is a matrix.**
    
4.  Matrix objects over-ride power to be matrix raised to a power. The same warning about using power inside a function that uses asanyarray(…) to get an array object holds for this fact.
    
5.  The default \_\_array\_priority\_\_ of matrix objects is 10.0, and therefore mixed operations with ndarrays always produce matrices.
    
6.  Matrices have special attributes which make calculations easier. These are
    
    |     |     |
    | --- | --- |
    | [`matrix.T`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.T.html#numpy.matrix.T "numpy.matrix.T") | Returns the transpose of the matrix. |
    | [`matrix.H`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.H.html#numpy.matrix.H "numpy.matrix.H") | Returns the (complex) conjugate transpose of _self_. |
    | [`matrix.I`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.I.html#numpy.matrix.I "numpy.matrix.I") | Returns the (multiplicative) inverse of invertible _self_. |
    | [`matrix.A`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.A.html#numpy.matrix.A "numpy.matrix.A") | Return _self_ as an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")<br> object. |
    

Warning

Matrix objects over-ride multiplication, ‘\*’, and power, ‘\*\*’, to be matrix-multiplication and matrix power, respectively. If your subroutine can accept sub-classes and you do not convert to base- class arrays, then you must use the ufuncs multiply and power to be sure that you are performing the correct operation for all inputs.

The matrix class is a Python subclass of the ndarray and can be used as a reference for how to construct your own subclass of the ndarray. Matrices can be created from other matrices, strings, and anything else that can be converted to an `ndarray` . The name “mat “is an alias for “matrix “in NumPy.

|     |     |
| --- | --- |
| [`matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "numpy.matrix")<br>(data\[, dtype, copy\]) | Returns a matrix from an array-like object, or from a string of data. |
| [`asmatrix`](https://numpy.org/doc/stable/reference/generated/numpy.asmatrix.html#numpy.asmatrix "numpy.asmatrix")<br>(data\[, dtype\]) | Interpret the input as a matrix. |
| [`bmat`](https://numpy.org/doc/stable/reference/generated/numpy.bmat.html#numpy.bmat "numpy.bmat")<br>(obj\[, ldict, gdict\]) | Build a matrix object from a string, nested sequence, or array. |

Example 1: Matrix creation from a string

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.asmatrix('1 2 3; 4 5 3')
\>>> print((a\*a.T).I)
  \[\[ 0.29239766 -0.13450292\]\
  \[-0.13450292  0.08187135\]\]

Copy to clipboard

Go BackOpen In Tab

Example 2: Matrix creation from a nested sequence

Try it in your browser!

\>>> import numpy as np
\>>> np.asmatrix(\[\[1,5,10\],\[1.0,3,4j\]\])
matrix(\[\[  1.+0.j,   5.+0.j,  10.+0.j\],\
        \[  1.+0.j,   3.+0.j,   0.+4.j\]\])

Copy to clipboard

Go BackOpen In Tab

Example 3: Matrix creation from an array

Try it in your browser!

\>>> import numpy as np
\>>> np.asmatrix(np.random.rand(3,3)).T
matrix(\[\[4.17022005e-01, 3.02332573e-01, 1.86260211e-01\],\
        \[7.20324493e-01, 1.46755891e-01, 3.45560727e-01\],\
        \[1.14374817e-04, 9.23385948e-02, 3.96767474e-01\]\])

Copy to clipboard

Go BackOpen In Tab

Memory-mapped file arrays[#](https://numpy.org/doc/stable/reference/arrays.classes.html#memory-mapped-file-arrays "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

Memory-mapped files are useful for reading and/or modifying small segments of a large file with regular layout, without reading the entire file into memory. A simple subclass of the ndarray uses a memory-mapped file for the data buffer of the array. For small files, the over-head of reading the entire file into memory is typically not significant, however for large files using memory mapping can save considerable resources.

Memory-mapped-file arrays have one additional method (besides those they inherit from the ndarray): [`.flush()`](https://numpy.org/doc/stable/reference/generated/numpy.memmap.flush.html#numpy.memmap.flush "numpy.memmap.flush")
 which must be called manually by the user to ensure that any changes to the array actually get written to disk.

|     |     |
| --- | --- |
| [`memmap`](https://numpy.org/doc/stable/reference/generated/numpy.memmap.html#numpy.memmap "numpy.memmap")<br>(filename\[, dtype, mode, offset, ...\]) | Create a memory-map to an array stored in a _binary_ file on disk. |
| [`memmap.flush`](https://numpy.org/doc/stable/reference/generated/numpy.memmap.flush.html#numpy.memmap.flush "numpy.memmap.flush")<br>() | Write any changes in the array to the file on disk. |

Example:

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> a \= np.memmap('newfile.dat', dtype\=np.float64, mode\='w+', shape\=1000)
\>>> a\[10\] \= 10.0
\>>> a\[30\] \= 30.0
\>>> del a

Copy to clipboard

\>>> b \= np.fromfile('newfile.dat', dtype\=np.float64)
\>>> print(b\[10\], b\[30\])
10.0 30.0

Copy to clipboard

\>>> a \= np.memmap('newfile.dat', dtype\=np.float64)
\>>> print(a\[10\], a\[30\])
10.0 30.0

Copy to clipboard

Go BackOpen In Tab

Character arrays ([`numpy.char`](https://numpy.org/doc/stable/reference/routines.char.html#module-numpy.char "numpy.char")
)[#](https://numpy.org/doc/stable/reference/arrays.classes.html#character-arrays-numpy-char "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

See also

[Creating character arrays (numpy.char)](https://numpy.org/doc/stable/reference/routines.array-creation.html#routines-array-creation-char)

Note

The [`chararray`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#numpy.char.chararray "numpy.char.chararray")
 class exists for backwards compatibility with Numarray, it is not recommended for new development. Starting from numpy 1.4, if one needs arrays of strings, it is recommended to use arrays of [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 [`object_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.object_ "numpy.object_")
, [`bytes_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_")
 or [`str_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.str_ "numpy.str_")
, and use the free functions in the [`numpy.char`](https://numpy.org/doc/stable/reference/routines.char.html#module-numpy.char "numpy.char")
 module for fast vectorized string operations.

Deprecated since version 2.5: `numpy.char.chararray` is deprecated. Use an `ndarray` with a string or bytes dtype instead.

These are enhanced arrays of either [`str_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.str_ "numpy.str_")
 type or [`bytes_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_")
 type. These arrays inherit from the [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, but specially-define the operations `+`, `*`, and `%` on a (broadcasting) element-by-element basis. These operations are not available on the standard [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 of character type. In addition, the [`chararray`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#numpy.char.chararray "numpy.char.chararray")
 has all of the standard [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 (and [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")
) methods, executing them on an element-by-element basis. Perhaps the easiest way to create a chararray is to use [`self.view(chararray)`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.view.html#numpy.ndarray.view "numpy.ndarray.view")
 where _self_ is an ndarray of str or unicode data-type. However, a chararray can also be created using the [`chararray`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#numpy.char.chararray "numpy.char.chararray")
 constructor, or via the [`numpy.char.array`](https://numpy.org/doc/stable/reference/generated/numpy.char.array.html#numpy.char.array "numpy.char.array")
 function:

|     |     |
| --- | --- |
| [`char.chararray`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#numpy.char.chararray "numpy.char.chararray")<br>(shape\[, itemsize, unicode, ...\]) | Provides a convenient view on arrays of string and unicode values. |
| [`char.array`](https://numpy.org/doc/stable/reference/generated/numpy.char.array.html#numpy.char.array "numpy.char.array")<br>(obj\[, itemsize, copy, unicode, order\]) | Create a [`chararray`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.html#numpy.char.chararray "numpy.char.chararray")<br>. |

Another difference with the standard ndarray of str data-type is that the chararray inherits the feature introduced by Numarray that white-space at the end of any element in the array will be ignored on item retrieval and comparison operations.

Record arrays[#](https://numpy.org/doc/stable/reference/arrays.classes.html#record-arrays "Link to this heading")

------------------------------------------------------------------------------------------------------------------

See also

[Creating record arrays](https://numpy.org/doc/stable/reference/routines.array-creation.html#routines-array-creation-rec)
, [Data type routines](https://numpy.org/doc/stable/reference/routines.dtype.html#routines-dtype)
, [Data type objects (dtype)](https://numpy.org/doc/stable/reference/arrays.dtypes.html#arrays-dtypes)
.

NumPy provides the [`recarray`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.html#numpy.recarray "numpy.recarray")
 class which allows accessing the fields of a structured array as attributes, and a corresponding scalar data type object [`record`](https://numpy.org/doc/stable/reference/generated/numpy.record.html#numpy.record "numpy.record")
.

|     |     |
| --- | --- |
| [`recarray`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.html#numpy.recarray "numpy.recarray")<br>(shape\[, dtype, buf, offset, ...\]) | Construct an ndarray that allows field access using attributes. |
| [`record`](https://numpy.org/doc/stable/reference/generated/numpy.record.html#numpy.record "numpy.record")<br>(length\_or\_data, /\[, dtype\]) | A data-type scalar that allows field access as attribute lookup. |

Note

The pandas DataFrame is more powerful than record array. If possible, please use pandas DataFrame instead.

Masked arrays ([`numpy.ma`](https://numpy.org/doc/stable/reference/maskedarray.generic.html#module-numpy.ma "numpy.ma")
)[#](https://numpy.org/doc/stable/reference/arrays.classes.html#masked-arrays-numpy-ma "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

See also

[Masked arrays](https://numpy.org/doc/stable/reference/maskedarray.html#maskedarray)

Standard container class[#](https://numpy.org/doc/stable/reference/arrays.classes.html#standard-container-class "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

For backward compatibility and as a standard “container “class, the UserArray from Numeric has been brought over to NumPy and named [`numpy.lib.user_array.container`](https://numpy.org/doc/stable/reference/generated/numpy.lib.user_array.container.html#numpy.lib.user_array.container "numpy.lib.user_array.container")
 The container class is a Python class whose self.array attribute is an ndarray. Multiple inheritance is probably easier with numpy.lib.user\_array.container than with the ndarray itself and so it is included by default. It is not documented here beyond mentioning its existence because you are encouraged to use the ndarray class directly if you can.

|     |     |
| --- | --- |
| [`numpy.lib.user_array.container`](https://numpy.org/doc/stable/reference/generated/numpy.lib.user_array.container.html#numpy.lib.user_array.container "numpy.lib.user_array.container")<br>(data\[, ...\]) | Standard container-class for easy multiple-inheritance. |

Array iterators[#](https://numpy.org/doc/stable/reference/arrays.classes.html#array-iterators "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

Iterators are a powerful concept for array processing. Essentially, iterators implement a generalized for-loop. If _myiter_ is an iterator object, then the Python code:

for val in myiter:
    ...
    some code involving val
    ...

Copy to clipboard

calls `val = next(myiter)` repeatedly until [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration "(in Python v3.14)")
 is raised by the iterator. There are several ways to iterate over an array that may be useful: default iteration, flat iteration, and \\(N\\)\-dimensional enumeration.

### Default iteration[#](https://numpy.org/doc/stable/reference/arrays.classes.html#default-iteration "Link to this heading")

The default iterator of an ndarray object is the default Python iterator of a sequence type. Thus, when the array object itself is used as an iterator. The default behavior is equivalent to:

for i in range(arr.shape\[0\]):
    val \= arr\[i\]

Copy to clipboard

This default iterator selects a sub-array of dimension \\(N-1\\) from the array. This can be a useful construct for defining recursive algorithms. To loop over the entire array requires \\(N\\) for-loops.

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.arange(24).reshape(3,2,4) + 10
\>>> for val in a:
...     print('item:', val)
item: \[\[10 11 12 13\]\
\[14 15 16 17\]\]
item: \[\[18 19 20 21\]\
\[22 23 24 25\]\]
item: \[\[26 27 28 29\]\
\[30 31 32 33\]\]

Copy to clipboard

Go BackOpen In Tab

### Flat iteration[#](https://numpy.org/doc/stable/reference/arrays.classes.html#flat-iteration "Link to this heading")

|     |     |
| --- | --- |
| [`ndarray.flat`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flat.html#numpy.ndarray.flat "numpy.ndarray.flat") | A 1-D iterator over the array. |

As mentioned previously, the flat attribute of ndarray objects returns an iterator that will cycle over the entire array in C-style contiguous order.

Try it in your browser!

\>>> import numpy as np
\>>> for i, val in enumerate(a.flat):
...     if i%5 \== 0: print(i, val)
0 10
5 15
10 20
15 25
20 30

Copy to clipboard

Go BackOpen In Tab

Here, I’ve used the built-in enumerate iterator to return the iterator index as well as the value.

### N-dimensional enumeration[#](https://numpy.org/doc/stable/reference/arrays.classes.html#n-dimensional-enumeration "Link to this heading")

|     |     |
| --- | --- |
| [`ndenumerate`](https://numpy.org/doc/stable/reference/generated/numpy.ndenumerate.html#numpy.ndenumerate "numpy.ndenumerate")<br>(arr) | Multidimensional index iterator. |

Sometimes it may be useful to get the N-dimensional index while iterating. The ndenumerate iterator can achieve this.

Try it in your browser!

\>>> import numpy as np
\>>> for i, val in np.ndenumerate(a):
...     if sum(i)%5 \== 0:
            print(i, val)
(0, 0, 0) 10
(1, 1, 3) 25
(2, 0, 3) 29
(2, 1, 2) 32

Copy to clipboard

Go BackOpen In Tab

### Iterator for broadcasting[#](https://numpy.org/doc/stable/reference/arrays.classes.html#iterator-for-broadcasting "Link to this heading")

|     |     |
| --- | --- |
| [`broadcast`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.html#numpy.broadcast "numpy.broadcast")<br>(\*arrays) | Produce an object that mimics broadcasting. |

The general concept of broadcasting is also available from Python using the [`broadcast`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.html#numpy.broadcast "numpy.broadcast")
 iterator. This object takes \\(N\\) objects as inputs and returns an iterator that returns tuples providing each of the input sequence elements in the broadcasted result.

Try it in your browser!

\>>> import numpy as np
\>>> for val in np.broadcast(\[\[1, 0\], \[2, 3\]\], \[0, 1\]):
...     print(val)
(np.int64(1), np.int64(0))
(np.int64(0), np.int64(1))
(np.int64(2), np.int64(0))
(np.int64(3), np.int64(1))

Copy to clipboard

Go BackOpen In Tab

On this page