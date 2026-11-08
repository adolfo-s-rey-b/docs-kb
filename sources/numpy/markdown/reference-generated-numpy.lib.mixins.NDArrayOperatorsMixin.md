[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.mixins.NDArrayOperatorsMixin[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html#numpy-lib-mixins-ndarrayoperatorsmixin "Link to this heading")

======================================================================================================================================================================================================

_class_ numpy.lib.mixins.NDArrayOperatorsMixin[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/mixins.py#L60-L180)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html#numpy.lib.mixins.NDArrayOperatorsMixin "Link to this definition")

Mixin defining all operator special methods using \_\_array\_ufunc\_\_.

This class implements the special methods for almost all of Python’s builtin operators defined in the [`operator`](https://docs.python.org/3/library/operator.html#module-operator "(in Python v3.14)")
 module, including comparisons (`==`, `>`, etc.) and arithmetic (`+`, `*`, `-`, etc.), by deferring to the `__array_ufunc__` method, which subclasses must implement.

It is useful for writing classes that do not inherit from [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, but that should support arithmetic and numpy universal functions like arrays as described in [NEP 13 — A mechanism for overriding Ufuncs](https://numpy.org/neps/nep-0013-ufunc-overrides.html "(in NumPy Enhancement Proposals)")
.

As a trivial example, consider this implementation of an `ArrayLike` class that simply wraps a NumPy array and ensures that the result of any arithmetic operation is also an `ArrayLike` object:

\>>> import numbers
\>>> class ArrayLike(np.lib.mixins.NDArrayOperatorsMixin):
...     def \_\_init\_\_(self, value):
...         self.value \= np.asarray(value)
...
...     \# One might also consider adding the built-in list type to this
...     \# list, to support operations like np.add(array\_like, list)
...     \_HANDLED\_TYPES \= (np.ndarray, numbers.Number)
...
...     def \_\_array\_ufunc\_\_(self, ufunc, method, \*inputs, \*\*kwargs):
...         out \= kwargs.get('out', ())
...         for x in inputs + out:
...             \# Only support operations with instances of
...             \# \_HANDLED\_TYPES. Use ArrayLike instead of type(self)
...             \# for isinstance to allow subclasses that don't
...             \# override \_\_array\_ufunc\_\_ to handle ArrayLike objects.
...             if not isinstance(
...                 x, self.\_HANDLED\_TYPES + (ArrayLike,)
...             ):
...                 return NotImplemented
...
...         \# Defer to the implementation of the ufunc
...         \# on unwrapped values.
...         inputs \= tuple(x.value if isinstance(x, ArrayLike) else x
...                     for x in inputs)
...         if out:
...             kwargs\['out'\] \= tuple(
...                 x.value if isinstance(x, ArrayLike) else x
...                 for x in out)
...         result \= getattr(ufunc, method)(\*inputs, \*\*kwargs)
...
...         if type(result) is tuple:
...             \# multiple return values
...             return tuple(type(self)(x) for x in result)
...         elif method \== 'at':
...             \# no return value
...             return None
...         else:
...             \# one return value
...             return type(self)(result)
...
...     def \_\_repr\_\_(self):
...         return '%s(%r)' % (type(self).\_\_name\_\_, self.value)

Copy to clipboard

In interactions between `ArrayLike` objects and numbers or numpy arrays, the result is always another `ArrayLike`:

\>>> x \= ArrayLike(\[1, 2, 3\])
\>>> x \- 1
ArrayLike(array(\[0, 1, 2\]))
\>>> 1 \- x
ArrayLike(array(\[ 0, -1, -2\]))
\>>> np.arange(3) \- x
ArrayLike(array(\[-1, -1, -1\]))
\>>> x \- np.arange(3)
ArrayLike(array(\[1, 1, 1\]))

Copy to clipboard

Note that unlike `numpy.ndarray`, `ArrayLike` does not allow operations with arbitrary, unrecognized types. This ensures that interactions with ArrayLike preserve a well-defined casting hierarchy.

On this page