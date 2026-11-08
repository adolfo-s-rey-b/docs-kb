[Skip to main content](https://numpy.org/doc/stable/reference/maskedarray.generic.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/maskedarray.generic.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/maskedarray.generic.html)
[2.4](https://numpy.org/doc/2.4/reference/maskedarray.generic.html)
[2.3](https://numpy.org/doc/2.3/reference/maskedarray.generic.html)
[2.2](https://numpy.org/doc/2.2/reference/maskedarray.generic.html)
[2.1](https://numpy.org/doc/2.1/reference/maskedarray.generic.html)
[2.0](https://numpy.org/doc/2.0/reference/maskedarray.generic.html)
[1.26](https://numpy.org/doc/1.26/reference/maskedarray.generic.html)
[1.25](https://numpy.org/doc/1.25/reference/maskedarray.generic.html)
[1.24](https://numpy.org/doc/1.24/reference/maskedarray.generic.html)
[1.23](https://numpy.org/doc/1.23/reference/maskedarray.generic.html)
[1.22](https://numpy.org/doc/1.22/reference/maskedarray.generic.html)
[1.21](https://numpy.org/doc/1.21/reference/maskedarray.generic.html)
[1.20](https://numpy.org/doc/1.20/reference/maskedarray.generic.html)
[1.19](https://numpy.org/doc/1.19/reference/maskedarray.generic.html)
[1.18](https://numpy.org/doc/1.18/reference/maskedarray.generic.html)
[1.17](https://numpy.org/doc/1.17/reference/maskedarray.generic.html)
[1.16](https://numpy.org/doc/1.16/reference/maskedarray.generic.html)
[1.15](https://numpy.org/doc/1.15/reference/maskedarray.generic.html)
[1.14](https://numpy.org/doc/1.14/reference/maskedarray.generic.html)
[1.13](https://numpy.org/doc/1.13/reference/maskedarray.generic.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

The [`numpy.ma`](https://numpy.org/doc/stable/reference/maskedarray.generic.html#module-numpy.ma "numpy.ma")
 module[#](https://numpy.org/doc/stable/reference/maskedarray.generic.html#the-numpy-ma-module "Link to this heading")

====================================================================================================================================================================================================================================

Rationale[#](https://numpy.org/doc/stable/reference/maskedarray.generic.html#rationale "Link to this heading")

---------------------------------------------------------------------------------------------------------------

Masked arrays are arrays that may have missing or invalid entries. The [`numpy.ma`](https://numpy.org/doc/stable/reference/maskedarray.generic.html#module-numpy.ma "numpy.ma")
 module provides a nearly work-alike replacement for numpy that supports data arrays with masks.

What is a masked array?[#](https://numpy.org/doc/stable/reference/maskedarray.generic.html#what-is-a-masked-array "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

In many circumstances, datasets can be incomplete or tainted by the presence of invalid data. For example, a sensor may have failed to record a data point, or recorded an invalid value. The [`numpy.ma`](https://numpy.org/doc/stable/reference/maskedarray.generic.html#module-numpy.ma "numpy.ma")
 module provides a convenient way to address this issue, by introducing masked arrays.

A masked array is the combination of a standard [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 and a mask. A mask is either [`nomask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.nomask "numpy.ma.nomask")
, indicating that no value of the associated array is invalid, or an array of booleans that determines for each element of the associated array whether the value is valid or not. When an element of the mask is `False`, the corresponding element of the associated array is valid and is said to be unmasked. When an element of the mask is `True`, the corresponding element of the associated array is said to be masked (invalid).

The package ensures that masked entries are not used in computations.

Try it in your browser!

As an illustration, let’s consider the following dataset:

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> x \= np.array(\[1, 2, 3, \-1, 5\])

Copy to clipboard

We wish to mark the fourth entry as invalid. The easiest is to create a masked array:

\>>> mx \= ma.masked\_array(x, mask\=\[0, 0, 0, 1, 0\])

Copy to clipboard

We can now compute the mean of the dataset, without taking the invalid data into account:

\>>> mx.mean()
2.75

Copy to clipboard

Go BackOpen In Tab

The [`numpy.ma`](https://numpy.org/doc/stable/reference/maskedarray.generic.html#module-numpy.ma "numpy.ma")
 module[#](https://numpy.org/doc/stable/reference/maskedarray.generic.html#id1 "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The main feature of the [`numpy.ma`](https://numpy.org/doc/stable/reference/maskedarray.generic.html#module-numpy.ma "numpy.ma")
 module is the [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 class, which is a subclass of [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
. The class, its attributes and methods are described in more details in the [MaskedArray class](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#maskedarray-baseclass)
 section.

Try it in your browser!

The [`numpy.ma`](https://numpy.org/doc/stable/reference/maskedarray.generic.html#module-numpy.ma "numpy.ma")
 module can be used as an addition to [`numpy`](https://numpy.org/doc/stable/reference/index.html#module-numpy "numpy")
:

\>>> import numpy as np
\>>> import numpy.ma as ma

Copy to clipboard

To create an array with the second element invalid, we would do:

\>>> y \= ma.array(\[1, 2, 3\], mask \= \[0, 1, 0\])

Copy to clipboard

To create a masked array where all values close to 1.e20 are invalid, we would do:

\>>> z \= ma.masked\_values(\[1.0, 1.e20, 3.0, 4.0\], 1.e20)

Copy to clipboard

Go BackOpen In Tab

For a complete discussion of creation methods for masked arrays please see section [Constructing masked arrays](https://numpy.org/doc/stable/reference/maskedarray.generic.html#maskedarray-generic-constructing)
.

Using numpy.ma[#](https://numpy.org/doc/stable/reference/maskedarray.generic.html#using-numpy-ma "Link to this heading")

=========================================================================================================================

Constructing masked arrays[#](https://numpy.org/doc/stable/reference/maskedarray.generic.html#constructing-masked-arrays "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

There are several ways to construct a masked array.

*   A first possibility is to directly invoke the [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
     class.
    
*   A second possibility is to use the two masked array constructors, [`array`](https://numpy.org/doc/stable/reference/generated/numpy.ma.array.html#numpy.ma.array "numpy.ma.array")
     and [`masked_array`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.html#numpy.ma.masked_array "numpy.ma.masked_array")
    .
    
    |     |     |
    | --- | --- |
    | [`array`](https://numpy.org/doc/stable/reference/generated/numpy.ma.array.html#numpy.ma.array "numpy.ma.array")<br>(data\[, dtype, copy, order, mask, ...\]) | An array class with possibly masked values. |
    | [`masked_array`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.html#numpy.ma.masked_array "numpy.ma.masked_array") | alias of [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray") |
    
*   A third option is to take the view of an existing array. In that case, the mask of the view is set to [`nomask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.nomask "numpy.ma.nomask")
     if the array has no named fields, or an array of boolean with the same structure as the array otherwise.
    

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[1, 2, 3\])
\>>> x.view(ma.MaskedArray)
masked\_array(data=\[1, 2, 3\],
            mask=False,
      fill\_value=999999)
\>>> x \= np.array(\[(1, 1.), (2, 2.)\], dtype\=\[('a',int), ('b', float)\])
\>>> x.view(ma.MaskedArray)
masked\_array(data=\[(1, 1.0), (2, 2.0)\],
            mask=\[(False, False), (False, False)\],
      fill\_value=(999999, 1e+20),
            dtype=\[('a', '<i8'), ('b', '<f8')\])

Copy to clipboard

Go BackOpen In Tab

*   Yet another possibility is to use any of the following functions:
    
    |     |     |
    | --- | --- |
    | [`asarray`](https://numpy.org/doc/stable/reference/generated/numpy.ma.asarray.html#numpy.ma.asarray "numpy.ma.asarray")<br>(a\[, dtype, order\]) | Convert the input to a masked array of the given data-type. |
    | [`asanyarray`](https://numpy.org/doc/stable/reference/generated/numpy.ma.asanyarray.html#numpy.ma.asanyarray "numpy.ma.asanyarray")<br>(a\[, dtype, order\]) | Convert the input to a masked array, conserving subclasses. |
    | [`fix_invalid`](https://numpy.org/doc/stable/reference/generated/numpy.ma.fix_invalid.html#numpy.ma.fix_invalid "numpy.ma.fix_invalid")<br>(a\[, mask, copy, fill\_value\]) | Return input with invalid data masked and replaced by a fill value. |
    | [`masked_equal`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_equal.html#numpy.ma.masked_equal "numpy.ma.masked_equal")<br>(x, value\[, copy\]) | Mask an array where equal to a given value. |
    | [`masked_greater`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_greater.html#numpy.ma.masked_greater "numpy.ma.masked_greater")<br>(x, value\[, copy\]) | Mask an array where greater than a given value. |
    | [`masked_greater_equal`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_greater_equal.html#numpy.ma.masked_greater_equal "numpy.ma.masked_greater_equal")<br>(x, value\[, copy\]) | Mask an array where greater than or equal to a given value. |
    | [`masked_inside`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_inside.html#numpy.ma.masked_inside "numpy.ma.masked_inside")<br>(x, v1, v2\[, copy\]) | Mask an array inside a given interval. |
    | [`masked_invalid`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_invalid.html#numpy.ma.masked_invalid "numpy.ma.masked_invalid")<br>(a\[, copy\]) | Mask an array where invalid values occur (NaNs or infs). |
    | [`masked_less`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_less.html#numpy.ma.masked_less "numpy.ma.masked_less")<br>(x, value\[, copy\]) | Mask an array where less than a given value. |
    | [`masked_less_equal`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_less_equal.html#numpy.ma.masked_less_equal "numpy.ma.masked_less_equal")<br>(x, value\[, copy\]) | Mask an array where less than or equal to a given value. |
    | [`masked_not_equal`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_not_equal.html#numpy.ma.masked_not_equal "numpy.ma.masked_not_equal")<br>(x, value\[, copy\]) | Mask an array where _not_ equal to a given value. |
    | [`masked_object`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_object.html#numpy.ma.masked_object "numpy.ma.masked_object")<br>(x, value\[, copy, shrink\]) | Mask the array _x_ where the data are exactly equal to value. |
    | [`masked_outside`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_outside.html#numpy.ma.masked_outside "numpy.ma.masked_outside")<br>(x, v1, v2\[, copy\]) | Mask an array outside a given interval. |
    | [`masked_values`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_values.html#numpy.ma.masked_values "numpy.ma.masked_values")<br>(x, value\[, rtol, atol, copy, ...\]) | Mask using floating point equality. |
    | [`masked_where`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_where.html#numpy.ma.masked_where "numpy.ma.masked_where")<br>(condition, a\[, copy\]) | Mask an array where a condition is met. |
    

Accessing the data[#](https://numpy.org/doc/stable/reference/maskedarray.generic.html#accessing-the-data "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

The underlying data of a masked array can be accessed in several ways:

*   through the [`data`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.data "numpy.ma.MaskedArray.data")
     attribute. The output is a view of the array as a [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
     or one of its subclasses, depending on the type of the underlying data at the masked array creation.
    
*   through the [`__array__`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__array__.html#numpy.ma.MaskedArray.__array__ "numpy.ma.MaskedArray.__array__")
     method. The output is then a [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
    .
    
*   by directly taking a view of the masked array as a [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
     or one of its subclass (which is actually what using the [`data`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.data "numpy.ma.MaskedArray.data")
     attribute does).
    
*   by using the [`getdata`](https://numpy.org/doc/stable/reference/generated/numpy.ma.getdata.html#numpy.ma.getdata "numpy.ma.getdata")
     function.
    

None of these methods is completely satisfactory if some entries have been marked as invalid. As a general rule, where a representation of the array is required without any masked entries, it is recommended to fill the array with the [`filled`](https://numpy.org/doc/stable/reference/generated/numpy.ma.filled.html#numpy.ma.filled "numpy.ma.filled")
 method.

Accessing the mask[#](https://numpy.org/doc/stable/reference/maskedarray.generic.html#accessing-the-mask "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

The mask of a masked array is accessible through its [`mask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.mask "numpy.ma.MaskedArray.mask")
 attribute. We must keep in mind that a `True` entry in the mask indicates an _invalid_ data.

Another possibility is to use the [`getmask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.getmask.html#numpy.ma.getmask "numpy.ma.getmask")
 and [`getmaskarray`](https://numpy.org/doc/stable/reference/generated/numpy.ma.getmaskarray.html#numpy.ma.getmaskarray "numpy.ma.getmaskarray")
 functions. `getmask(x)` outputs the mask of `x` if `x` is a masked array, and the special value [`nomask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.nomask "numpy.ma.nomask")
 otherwise. `getmaskarray(x)` outputs the mask of `x` if `x` is a masked array. If `x` has no invalid entry or is not a masked array, the function outputs a boolean array of `False` with as many elements as `x`.

Accessing only the valid entries[#](https://numpy.org/doc/stable/reference/maskedarray.generic.html#accessing-only-the-valid-entries "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

To retrieve only the valid entries, we can use the inverse of the mask as an index. The inverse of the mask can be calculated with the [`numpy.logical_not`](https://numpy.org/doc/stable/reference/generated/numpy.logical_not.html#numpy.logical_not "numpy.logical_not")
 function or simply with the `~` operator:

Try it in your browser!

\>>> import numpy as np
\>>> x \= ma.array(\[\[1, 2\], \[3, 4\]\], mask\=\[\[0, 1\], \[1, 0\]\])
\>>> x\[~x.mask\]
masked\_array(data=\[1, 4\],
               mask=\[False, False\],
         fill\_value=999999)

Copy to clipboard

Another way to retrieve the valid data is to use the [`compressed`](https://numpy.org/doc/stable/reference/generated/numpy.ma.compressed.html#numpy.ma.compressed "numpy.ma.compressed")
 method, which returns a one-dimensional [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 (or one of its subclasses, depending on the value of the [`baseclass`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.baseclass "numpy.ma.MaskedArray.baseclass")
 attribute):

\>>> x.compressed()
array(\[1, 4\])

Copy to clipboard

Note that the output of [`compressed`](https://numpy.org/doc/stable/reference/generated/numpy.ma.compressed.html#numpy.ma.compressed "numpy.ma.compressed")
 is always 1D.

Go BackOpen In Tab

Modifying the mask[#](https://numpy.org/doc/stable/reference/maskedarray.generic.html#modifying-the-mask "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

### Masking an entry[#](https://numpy.org/doc/stable/reference/maskedarray.generic.html#masking-an-entry "Link to this heading")

The recommended way to mark one or several specific entries of a masked array as invalid is to assign the special value [`masked`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.masked "numpy.ma.masked")
 to them:

Try it in your browser!

\>>> x \= ma.array(\[1, 2, 3\])
\>>> x\[0\] \= ma.masked
\>>> x
masked\_array(data=\[--, 2, 3\],
             mask=\[ True, False, False\],
       fill\_value=999999)
\>>> y \= ma.array(\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\]\])
\>>> y\[(0, 1, 2), (1, 2, 0)\] \= ma.masked
\>>> y
masked\_array(
  data=\[\[1, --, 3\],\
        \[4, 5, --\],\
        \[--, 8, 9\]\],
  mask=\[\[False,  True, False\],\
        \[False, False,  True\],\
        \[ True, False, False\]\],
  fill\_value=999999)
\>>> z \= ma.array(\[1, 2, 3, 4\])
\>>> z\[:\-2\] \= ma.masked
\>>> z
masked\_array(data=\[--, --, 3, 4\],
             mask=\[ True,  True, False, False\],
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

A second possibility is to modify the [`mask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.mask "numpy.ma.MaskedArray.mask")
 directly, but this usage is discouraged.

Note

When creating a new masked array with a simple, non-structured datatype, the mask is initially set to the special value [`nomask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.nomask "numpy.ma.nomask")
, that corresponds roughly to the boolean `False`. Trying to set an element of [`nomask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.nomask "numpy.ma.nomask")
 will fail with a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
 exception, as a boolean does not support item assignment.

All the entries of an array can be masked at once by assigning `True` to the mask:

Try it in your browser!

\>>> import numpy.ma as ma
\>>> x \= ma.array(\[1, 2, 3\], mask\=\[0, 0, 1\])
\>>> x.mask \= True
\>>> x
masked\_array(data=\[--, --, --\],
             mask=\[ True,  True,  True\],
       fill\_value=999999,
            dtype=int64)

Copy to clipboard

Finally, specific entries can be masked and/or unmasked by assigning to the mask a sequence of booleans:

\>>> x \= ma.array(\[1, 2, 3\])
\>>> x.mask \= \[0, 1, 0\]
\>>> x
masked\_array(data=\[1, --, 3\],
             mask=\[False,  True, False\],
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

### Unmasking an entry[#](https://numpy.org/doc/stable/reference/maskedarray.generic.html#unmasking-an-entry "Link to this heading")

To unmask one or several specific entries, we can just assign one or several new valid values to them:

Try it in your browser!

\>>> import numpy.ma as ma
\>>> x \= ma.array(\[1, 2, 3\], mask\=\[0, 0, 1\])
\>>> x
masked\_array(data=\[1, 2, --\],
             mask=\[False, False,  True\],
       fill\_value=999999)
\>>> x\[\-1\] \= 5
\>>> x
masked\_array(data=\[1, 2, 5\],
             mask=\[False, False, False\],
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

Note

Unmasking an entry by direct assignment will silently fail if the masked array has a _hard_ mask, as shown by the [`hardmask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.hardmask "numpy.ma.MaskedArray.hardmask")
 attribute. This feature was introduced to prevent overwriting the mask. To force the unmasking of an entry where the array has a hard mask, the mask must first to be softened using the [`soften_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.soften_mask.html#numpy.ma.soften_mask "numpy.ma.soften_mask")
 method before the allocation. It can be re-hardened with [`harden_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.harden_mask.html#numpy.ma.harden_mask "numpy.ma.harden_mask")
 as follows:

Try it in your browser!

\>>> import numpy.ma as ma
\>>> x \= ma.array(\[1, 2, 3\], mask\=\[0, 0, 1\], hard\_mask\=True)
\>>> x
masked\_array(data=\[1, 2, --\],
               mask=\[False, False,  True\],
         fill\_value=999999)
\>>> x\[\-1\] \= 5
\>>> x
masked\_array(data=\[1, 2, --\],
               mask=\[False, False,  True\],
         fill\_value=999999)
\>>> x.soften\_mask()
masked\_array(data=\[1, 2, --\],
               mask=\[False, False,  True\],
         fill\_value=999999)
\>>> x\[\-1\] \= 5
\>>> x
masked\_array(data=\[1, 2, 5\],
               mask=\[False, False, False\],
         fill\_value=999999)
\>>> x.harden\_mask()
masked\_array(data=\[1, 2, 5\],
               mask=\[False, False, False\],
         fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

To unmask all masked entries of a masked array (provided the mask isn’t a hard mask), the simplest solution is to assign the constant [`nomask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.nomask "numpy.ma.nomask")
 to the mask:

Try it in your browser!

\>>> import numpy.ma as ma
\>>> x \= ma.array(\[1, 2, 3\], mask\=\[0, 0, 1\])
\>>> x
masked\_array(data=\[1, 2, --\],
             mask=\[False, False,  True\],
       fill\_value=999999)
\>>> x.mask \= ma.nomask
\>>> x
masked\_array(data=\[1, 2, 3\],
             mask=\[False, False, False\],
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

Indexing and slicing[#](https://numpy.org/doc/stable/reference/maskedarray.generic.html#indexing-and-slicing "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

As a [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 is a subclass of [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, it inherits its mechanisms for indexing and slicing.

When accessing a single entry of a masked array with no named fields, the output is either a scalar (if the corresponding entry of the mask is `False`) or the special value [`masked`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.masked "numpy.ma.masked")
 (if the corresponding entry of the mask is `True`):

Try it in your browser!

\>>> import numpy.ma as ma
\>>> x \= ma.array(\[1, 2, 3\], mask\=\[0, 0, 1\])
\>>> x\[0\]
1
\>>> x\[\-1\]
masked
\>>> x\[\-1\] is ma.masked
True

Copy to clipboard

Go BackOpen In Tab

If the masked array has named fields, accessing a single entry returns a [`numpy.void`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.void "numpy.void")
 object if none of the fields are masked, or a 0d masked array with the same dtype as the initial array if at least one of the fields is masked.

Try it in your browser!

\>>> import numpy.ma as ma
\>>> y \= ma.masked\_array(\[(1,2), (3, 4)\],
...                mask\=\[(0, 0), (0, 1)\],
...               dtype\=\[('a', int), ('b', int)\])
\>>> y\[0\]
(1, 2)
\>>> y\[\-1\]
(3, --)

Copy to clipboard

Go BackOpen In Tab

When accessing a slice, the output is a masked array whose [`data`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.data "numpy.ma.MaskedArray.data")
 attribute is a view of the original data, and whose mask is either [`nomask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.nomask "numpy.ma.nomask")
 (if there was no invalid entries in the original array) or a view of the corresponding slice of the original mask. The view is required to ensure propagation of any modification of the mask to the original.

Try it in your browser!

\>>> import numpy.ma as ma
\>>> x \= ma.array(\[1, 2, 3, 4, 5\], mask\=\[0, 1, 0, 0, 1\])
\>>> mx \= x\[:3\]
\>>> mx
masked\_array(data=\[1, --, 3\],
             mask=\[False,  True, False\],
       fill\_value=999999)
\>>> mx\[1\] \= \-1
\>>> mx
masked\_array(data=\[1, -1, 3\],
             mask=\[False, False, False\],
       fill\_value=999999)
\>>> x.mask
array(\[False, False, False, False,  True\])
\>>> x.data
array(\[ 1, -1,  3,  4,  5\])

Copy to clipboard

Go BackOpen In Tab

Accessing a field of a masked array with structured datatype returns a [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
.

Operations on masked arrays[#](https://numpy.org/doc/stable/reference/maskedarray.generic.html#operations-on-masked-arrays "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

Arithmetic and comparison operations are supported by masked arrays. As much as possible, invalid entries of a masked array are not processed, meaning that the corresponding [`data`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.data "numpy.ma.MaskedArray.data")
 entries _should_ be the same before and after the operation.

Warning

We need to stress that this behavior may not be systematic, that masked data may be affected by the operation in some cases and therefore users should not rely on this data remaining unchanged.

The [`numpy.ma`](https://numpy.org/doc/stable/reference/maskedarray.generic.html#module-numpy.ma "numpy.ma")
 module comes with a specific implementation of most ufuncs. Unary and binary functions that have a validity domain (such as [`log`](https://numpy.org/doc/stable/reference/generated/numpy.log.html#numpy.log "numpy.log")
 or [`divide`](https://numpy.org/doc/stable/reference/generated/numpy.divide.html#numpy.divide "numpy.divide")
) return the [`masked`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.masked "numpy.ma.masked")
 constant whenever the input is masked or falls outside the validity domain:

Try it in your browser!

\>>> import numpy.ma as ma
\>>> ma.log(\[\-1, 0, 1, 2\])
masked\_array(data=\[--, --, 0.0, 0.6931471805599453\],
             mask=\[ True,  True, False, False\],
       fill\_value=1e+20)

Copy to clipboard

Go BackOpen In Tab

Masked arrays also support standard numpy ufuncs. The output is then a masked array. The result of a unary ufunc is masked wherever the input is masked. The result of a binary ufunc is masked wherever any of the input is masked. If the ufunc also returns the optional context output (a 3-element tuple containing the name of the ufunc, its arguments and its domain), the context is processed and entries of the output masked array are masked wherever the corresponding input fall outside the validity domain:

Try it in your browser!

\>>> import numpy.ma as ma
\>>> x \= ma.array(\[\-1, 1, 0, 2, 3\], mask\=\[0, 0, 0, 0, 1\])
\>>> np.log(x)
masked\_array(data=\[--, 0.0, --, 0.6931471805599453, --\],
             mask=\[ True, False,  True, False,  True\],
       fill\_value=1e+20)

Copy to clipboard

Go BackOpen In Tab

Examples[#](https://numpy.org/doc/stable/reference/maskedarray.generic.html#examples "Link to this heading")

=============================================================================================================

Data with a given value representing missing data[#](https://numpy.org/doc/stable/reference/maskedarray.generic.html#data-with-a-given-value-representing-missing-data "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let’s consider a list of elements, `x`, where values of -9999. represent missing data. We wish to compute the average value of the data and the vector of anomalies (deviations from the average):

Try it in your browser!

\>>> import numpy.ma as ma
\>>> x \= \[0.,1.,\-9999.,3.,4.\]
\>>> mx \= ma.masked\_values (x, \-9999.)
\>>> print(mx.mean())
2.0
\>>> print(mx \- mx.mean())
\[-2.0 -1.0 -- 1.0 2.0\]
\>>> print(mx.anom())
\[-2.0 -1.0 -- 1.0 2.0\]

Copy to clipboard

Go BackOpen In Tab

Filling in the missing data[#](https://numpy.org/doc/stable/reference/maskedarray.generic.html#filling-in-the-missing-data "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

Suppose now that we wish to print that same data, but with the missing values replaced by the average value.

Try it in your browser!

\>>> import numpy.ma as ma
\>>> mx \= ma.masked\_values (x, \-9999.)
\>>> print(mx.filled(mx.mean()))
\[0.  1.  2.  3.  4.\]

Copy to clipboard

Go BackOpen In Tab

Numerical operations[#](https://numpy.org/doc/stable/reference/maskedarray.generic.html#numerical-operations "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

Numerical operations can be easily performed without worrying about missing values, dividing by zero, square roots of negative numbers, etc.:

Try it in your browser!

\>>> import numpy.ma as ma
\>>> x \= ma.array(\[1., \-1., 3., 4., 5., 6.\], mask\=\[0,0,0,0,1,0\])
\>>> y \= ma.array(\[1., 2., 0., 4., 5., 6.\], mask\=\[0,0,0,0,0,1\])
\>>> print(ma.sqrt(x/y))
\[1.0 -- -- 1.0 -- --\]

Copy to clipboard

Go BackOpen In Tab

Four values of the output are invalid: the first one comes from taking the square root of a negative number, the second from the division by zero, and the last two where the inputs were masked.

Ignoring extreme values[#](https://numpy.org/doc/stable/reference/maskedarray.generic.html#ignoring-extreme-values "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

Let’s consider an array `d` of floats between 0 and 1. We wish to compute the average of the values of `d` while ignoring any data outside the range `[0.2, 0.9]`:

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> d \= np.linspace(0, 1, 20)
\>>> print(d.mean() \- ma.masked\_outside(d, 0.2, 0.9).mean())
\-0.05263157894736836

Copy to clipboard

Go BackOpen In Tab

On this page