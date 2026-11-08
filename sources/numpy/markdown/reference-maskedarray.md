[Skip to main content](https://numpy.org/doc/stable/reference/maskedarray.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/maskedarray.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/maskedarray.html)
[2.4](https://numpy.org/doc/2.4/reference/maskedarray.html)
[2.3](https://numpy.org/doc/2.3/reference/maskedarray.html)
[2.2](https://numpy.org/doc/2.2/reference/maskedarray.html)
[2.1](https://numpy.org/doc/2.1/reference/maskedarray.html)
[2.0](https://numpy.org/doc/2.0/reference/maskedarray.html)
[1.26](https://numpy.org/doc/1.26/reference/maskedarray.html)
[1.25](https://numpy.org/doc/1.25/reference/maskedarray.html)
[1.24](https://numpy.org/doc/1.24/reference/maskedarray.html)
[1.23](https://numpy.org/doc/1.23/reference/maskedarray.html)
[1.22](https://numpy.org/doc/1.22/reference/maskedarray.html)
[1.21](https://numpy.org/doc/1.21/reference/maskedarray.html)
[1.20](https://numpy.org/doc/1.20/reference/maskedarray.html)
[1.19](https://numpy.org/doc/1.19/reference/maskedarray.html)
[1.18](https://numpy.org/doc/1.18/reference/maskedarray.html)
[1.17](https://numpy.org/doc/1.17/reference/maskedarray.html)
[1.16](https://numpy.org/doc/1.16/reference/maskedarray.html)
[1.15](https://numpy.org/doc/1.15/reference/maskedarray.html)
[1.14](https://numpy.org/doc/1.14/reference/maskedarray.html)
[1.13](https://numpy.org/doc/1.13/reference/maskedarray.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Masked arrays[#](https://numpy.org/doc/stable/reference/maskedarray.html#masked-arrays "Link to this heading")

===============================================================================================================

Masked arrays are arrays that may have missing or invalid entries. The [`numpy.ma`](https://numpy.org/doc/stable/reference/maskedarray.generic.html#module-numpy.ma "numpy.ma")
 module provides a nearly work-alike replacement for numpy that supports data arrays with masks.

*   [The `numpy.ma` module](https://numpy.org/doc/stable/reference/maskedarray.generic.html)
    *   [Rationale](https://numpy.org/doc/stable/reference/maskedarray.generic.html#rationale)
        
    *   [What is a masked array?](https://numpy.org/doc/stable/reference/maskedarray.generic.html#what-is-a-masked-array)
        
    *   [The `numpy.ma` module](https://numpy.org/doc/stable/reference/maskedarray.generic.html#id1)
        
*   [Using numpy.ma](https://numpy.org/doc/stable/reference/maskedarray.generic.html#using-numpy-ma)
    *   [Constructing masked arrays](https://numpy.org/doc/stable/reference/maskedarray.generic.html#constructing-masked-arrays)
        
    *   [Accessing the data](https://numpy.org/doc/stable/reference/maskedarray.generic.html#accessing-the-data)
        
    *   [Accessing the mask](https://numpy.org/doc/stable/reference/maskedarray.generic.html#accessing-the-mask)
        
    *   [Accessing only the valid entries](https://numpy.org/doc/stable/reference/maskedarray.generic.html#accessing-only-the-valid-entries)
        
    *   [Modifying the mask](https://numpy.org/doc/stable/reference/maskedarray.generic.html#modifying-the-mask)
        
    *   [Indexing and slicing](https://numpy.org/doc/stable/reference/maskedarray.generic.html#indexing-and-slicing)
        
    *   [Operations on masked arrays](https://numpy.org/doc/stable/reference/maskedarray.generic.html#operations-on-masked-arrays)
        
*   [Examples](https://numpy.org/doc/stable/reference/maskedarray.generic.html#examples)
    *   [Data with a given value representing missing data](https://numpy.org/doc/stable/reference/maskedarray.generic.html#data-with-a-given-value-representing-missing-data)
        
    *   [Filling in the missing data](https://numpy.org/doc/stable/reference/maskedarray.generic.html#filling-in-the-missing-data)
        
    *   [Numerical operations](https://numpy.org/doc/stable/reference/maskedarray.generic.html#numerical-operations)
        
    *   [Ignoring extreme values](https://numpy.org/doc/stable/reference/maskedarray.generic.html#ignoring-extreme-values)
        
*   [Constants of the `numpy.ma` module](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html)
    *   [`masked`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.masked)
        
    *   [`nomask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.nomask)
        
    *   [`masked_print_option`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.masked_print_option)
        
*   [The `MaskedArray` class](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#the-maskedarray-class)
    *   [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray)
        
    *   [Attributes and properties of masked arrays](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#attributes-and-properties-of-masked-arrays)
        
*   [`MaskedArray` methods](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#maskedarray-methods)
    *   [Conversion](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#conversion)
        
    *   [Shape manipulation](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#shape-manipulation)
        
    *   [Item selection and manipulation](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#item-selection-and-manipulation)
        
    *   [Pickling and copy](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#pickling-and-copy)
        
    *   [Calculations](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#calculations)
        
    *   [Arithmetic and comparison operations](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#arithmetic-and-comparison-operations)
        
    *   [Representation](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#representation)
        
    *   [Special methods](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#special-methods)
        
    *   [Specific methods](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#specific-methods)
        
*   [Masked array operations](https://numpy.org/doc/stable/reference/routines.ma.html)
    *   [Constants](https://numpy.org/doc/stable/reference/routines.ma.html#constants)
        
    *   [Creation](https://numpy.org/doc/stable/reference/routines.ma.html#creation)
        
    *   [Inspecting the array](https://numpy.org/doc/stable/reference/routines.ma.html#inspecting-the-array)
        
    *   [Manipulating a MaskedArray](https://numpy.org/doc/stable/reference/routines.ma.html#manipulating-a-maskedarray)
        
    *   [Operations on masks](https://numpy.org/doc/stable/reference/routines.ma.html#operations-on-masks)
        
    *   [Conversion operations](https://numpy.org/doc/stable/reference/routines.ma.html#conversion-operations)
        
    *   [Masked arrays arithmetic](https://numpy.org/doc/stable/reference/routines.ma.html#masked-arrays-arithmetic)