[Skip to main content](https://numpy.org/doc/stable/reference/arrays.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Array objects[#](https://numpy.org/doc/stable/reference/arrays.html#array-objects "Link to this heading")

==========================================================================================================

NumPy provides an N-dimensional array type, the [ndarray](https://numpy.org/doc/stable/reference/arrays.ndarray.html#arrays-ndarray)
, which describes a collection of “items” of the same type. The items can be [indexed](https://numpy.org/doc/stable/reference/routines.indexing.html#arrays-indexing)
 using for example N integers.

All ndarrays are [homogeneous](https://numpy.org/doc/stable/glossary.html#term-homogeneous)
: every item takes up the same size block of memory, and all blocks are interpreted in exactly the same way. How each item in the array is to be interpreted is specified by a separate [data-type object](https://numpy.org/doc/stable/reference/arrays.dtypes.html#arrays-dtypes)
, one of which is associated with every array. In addition to basic types (integers, floats, _etc._), the data type objects can also represent data structures.

An item extracted from an array, _e.g._, by indexing, is represented by a Python object whose type is one of the [array scalar types](https://numpy.org/doc/stable/reference/arrays.scalars.html#arrays-scalars)
 built in NumPy. The array scalars allow easy manipulation of also more complicated arrangements of data.

![../_images/threefundamental.png](https://numpy.org/doc/stable/_images/threefundamental.png)

**Figure** Conceptual diagram showing the relationship between the three fundamental objects used to describe the data in an array: 1) the ndarray itself, 2) the data-type object that describes the layout of a single fixed-size element of the array, 3) the array-scalar Python object that is returned when a single element of the array is accessed.[#](https://numpy.org/doc/stable/reference/arrays.html#id1 "Link to this image")

*   [The N-dimensional array (`ndarray`)](https://numpy.org/doc/stable/reference/arrays.ndarray.html)
    *   [Constructing arrays](https://numpy.org/doc/stable/reference/arrays.ndarray.html#constructing-arrays)
        
    *   [Indexing arrays](https://numpy.org/doc/stable/reference/arrays.ndarray.html#indexing-arrays)
        
    *   [Internal memory layout of an ndarray](https://numpy.org/doc/stable/reference/arrays.ndarray.html#internal-memory-layout-of-an-ndarray)
        
    *   [Array attributes](https://numpy.org/doc/stable/reference/arrays.ndarray.html#array-attributes)
        
    *   [Array methods](https://numpy.org/doc/stable/reference/arrays.ndarray.html#array-methods)
        
    *   [Arithmetic, matrix multiplication, and comparison operations](https://numpy.org/doc/stable/reference/arrays.ndarray.html#arithmetic-matrix-multiplication-and-comparison-operations)
        
    *   [Special methods](https://numpy.org/doc/stable/reference/arrays.ndarray.html#special-methods)
        
    *   [Structural pattern matching](https://numpy.org/doc/stable/reference/arrays.ndarray.html#structural-pattern-matching)
        
*   [Scalars](https://numpy.org/doc/stable/reference/arrays.scalars.html)
    *   [Built-in scalar types](https://numpy.org/doc/stable/reference/arrays.scalars.html#built-in-scalar-types)
        
    *   [Attributes](https://numpy.org/doc/stable/reference/arrays.scalars.html#attributes)
        
    *   [Indexing](https://numpy.org/doc/stable/reference/arrays.scalars.html#indexing)
        
    *   [Methods](https://numpy.org/doc/stable/reference/arrays.scalars.html#methods)
        
    *   [Defining new types](https://numpy.org/doc/stable/reference/arrays.scalars.html#defining-new-types)
        
*   [Data type objects (`dtype`)](https://numpy.org/doc/stable/reference/arrays.dtypes.html)
    *   [Specifying and constructing data types](https://numpy.org/doc/stable/reference/arrays.dtypes.html#specifying-and-constructing-data-types)
        
    *   [Checking the data type](https://numpy.org/doc/stable/reference/arrays.dtypes.html#checking-the-data-type)
        
    *   [`dtype`](https://numpy.org/doc/stable/reference/arrays.dtypes.html#dtype)
        
*   [Data type promotion in NumPy](https://numpy.org/doc/stable/reference/arrays.promotion.html)
    *   [Detailed behavior of Python scalars](https://numpy.org/doc/stable/reference/arrays.promotion.html#detailed-behavior-of-python-scalars)
        
    *   [Numerical promotion](https://numpy.org/doc/stable/reference/arrays.promotion.html#numerical-promotion)
        
    *   [Exceptions to the general promotion rules](https://numpy.org/doc/stable/reference/arrays.promotion.html#exceptions-to-the-general-promotion-rules)
        
    *   [Promotion of non-numerical datatypes](https://numpy.org/doc/stable/reference/arrays.promotion.html#promotion-of-non-numerical-datatypes)
        
    *   [Details of promoted `dtype` instances](https://numpy.org/doc/stable/reference/arrays.promotion.html#details-of-promoted-dtype-instances)
        
*   [Iterating over arrays](https://numpy.org/doc/stable/reference/arrays.nditer.html)
    *   [Single array iteration](https://numpy.org/doc/stable/reference/arrays.nditer.html#single-array-iteration)
        
    *   [Broadcasting array iteration](https://numpy.org/doc/stable/reference/arrays.nditer.html#broadcasting-array-iteration)
        
    *   [Putting the inner loop in Cython](https://numpy.org/doc/stable/reference/arrays.nditer.html#putting-the-inner-loop-in-cython)
        
*   [Standard array subclasses](https://numpy.org/doc/stable/reference/arrays.classes.html)
    *   [Special attributes and methods](https://numpy.org/doc/stable/reference/arrays.classes.html#special-attributes-and-methods)
        
    *   [Matrix objects](https://numpy.org/doc/stable/reference/arrays.classes.html#matrix-objects)
        
    *   [Memory-mapped file arrays](https://numpy.org/doc/stable/reference/arrays.classes.html#memory-mapped-file-arrays)
        
    *   [Character arrays (`numpy.char`)](https://numpy.org/doc/stable/reference/arrays.classes.html#character-arrays-numpy-char)
        
    *   [Record arrays](https://numpy.org/doc/stable/reference/arrays.classes.html#record-arrays)
        
    *   [Masked arrays (`numpy.ma`)](https://numpy.org/doc/stable/reference/arrays.classes.html#masked-arrays-numpy-ma)
        
    *   [Standard container class](https://numpy.org/doc/stable/reference/arrays.classes.html#standard-container-class)
        
    *   [Array iterators](https://numpy.org/doc/stable/reference/arrays.classes.html#array-iterators)
        
*   [Masked arrays](https://numpy.org/doc/stable/reference/maskedarray.html)
    *   [The `numpy.ma` module](https://numpy.org/doc/stable/reference/maskedarray.generic.html)
        
    *   [Using numpy.ma](https://numpy.org/doc/stable/reference/maskedarray.generic.html#using-numpy-ma)
        
    *   [Examples](https://numpy.org/doc/stable/reference/maskedarray.generic.html#examples)
        
    *   [Constants of the `numpy.ma` module](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html)
        
    *   [The `MaskedArray` class](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#the-maskedarray-class)
        
    *   [`MaskedArray` methods](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#maskedarray-methods)
        
    *   [Masked array operations](https://numpy.org/doc/stable/reference/routines.ma.html)
        
*   [The array interface protocol](https://numpy.org/doc/stable/reference/arrays.interface.html)
    *   [Python side](https://numpy.org/doc/stable/reference/arrays.interface.html#python-side)
        
    *   [C-struct access](https://numpy.org/doc/stable/reference/arrays.interface.html#c-struct-access)
        
    *   [Type description examples](https://numpy.org/doc/stable/reference/arrays.interface.html#type-description-examples)
        
    *   [Differences with array interface (version 2)](https://numpy.org/doc/stable/reference/arrays.interface.html#differences-with-array-interface-version-2)
        
*   [Datetimes and timedeltas](https://numpy.org/doc/stable/reference/arrays.datetime.html)
    *   [Datetime64 conventions and assumptions](https://numpy.org/doc/stable/reference/arrays.datetime.html#datetime64-conventions-and-assumptions)
        
    *   [Basic datetimes](https://numpy.org/doc/stable/reference/arrays.datetime.html#basic-datetimes)
        
    *   [Datetime and timedelta arithmetic](https://numpy.org/doc/stable/reference/arrays.datetime.html#datetime-and-timedelta-arithmetic)
        
    *   [Datetime units](https://numpy.org/doc/stable/reference/arrays.datetime.html#datetime-units)
        
    *   [Converting datetime and timedelta to Python Object](https://numpy.org/doc/stable/reference/arrays.datetime.html#converting-datetime-and-timedelta-to-python-object)
        
    *   [Business day functionality](https://numpy.org/doc/stable/reference/arrays.datetime.html#business-day-functionality)
        
    *   [Datetime64 shortcomings](https://numpy.org/doc/stable/reference/arrays.datetime.html#datetime64-shortcomings)
        
    *   [Migration guide for deprecation of generic units](https://numpy.org/doc/stable/reference/arrays.datetime.html#migration-guide-for-deprecation-of-generic-units)