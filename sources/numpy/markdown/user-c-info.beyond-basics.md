[Skip to main content](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/user/c-info.beyond-basics.html)
[2.5 (stable)](https://numpy.org/doc/stable/user/c-info.beyond-basics.html)
[2.4](https://numpy.org/doc/2.4/user/c-info.beyond-basics.html)
[2.3](https://numpy.org/doc/2.3/user/c-info.beyond-basics.html)
[2.2](https://numpy.org/doc/2.2/user/c-info.beyond-basics.html)
[2.1](https://numpy.org/doc/2.1/user/c-info.beyond-basics.html)
[2.0](https://numpy.org/doc/2.0/user/c-info.beyond-basics.html)
[1.26](https://numpy.org/doc/1.26/user/c-info.beyond-basics.html)
[1.25](https://numpy.org/doc/1.25/user/c-info.beyond-basics.html)
[1.24](https://numpy.org/doc/1.24/user/c-info.beyond-basics.html)
[1.23](https://numpy.org/doc/1.23/user/c-info.beyond-basics.html)
[1.22](https://numpy.org/doc/1.22/user/c-info.beyond-basics.html)
[1.21](https://numpy.org/doc/1.21/user/c-info.beyond-basics.html)
[1.20](https://numpy.org/doc/1.20/user/c-info.beyond-basics.html)
[1.19](https://numpy.org/doc/1.19/user/c-info.beyond-basics.html)
[1.18](https://numpy.org/doc/1.18/user/c-info.beyond-basics.html)
[1.17](https://numpy.org/doc/1.17/user/c-info.beyond-basics.html)
[1.16](https://numpy.org/doc/1.16/user/c-info.beyond-basics.html)
[1.15](https://numpy.org/doc/1.15/user/c-info.beyond-basics.html)
[1.14](https://numpy.org/doc/1.14/user/c-info.beyond-basics.html)
[1.13](https://numpy.org/doc/1.13/user/c-info.beyond-basics.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Beyond the basics[#](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#beyond-the-basics "Link to this heading")

===========================================================================================================================

The voyage of discovery is not in seeking new landscapes but in having

new eyes.

— _Marcel Proust_

Discovery is seeing what everyone else has seen and thinking what no

one else has thought.

— _Albert Szent-Gyorgi_

Iterating over elements in the array[#](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#iterating-over-elements-in-the-array "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

### Basic iteration[#](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#basic-iteration "Link to this heading")

One common algorithmic requirement is to be able to walk over all elements in a multidimensional array. The array iterator object makes this easy to do in a generic way that works for arrays of any dimension. Naturally, if you know the number of dimensions you will be using, then you can always write nested for loops to accomplish the iteration. If, however, you want to write code that works with any number of dimensions, then you can make use of the array iterator. An array iterator object is returned when accessing the .flat attribute of an array.

Basic usage is to call [`PyArray_IterNew`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_IterNew "PyArray_IterNew")
 ( `array` ) where array is an ndarray object (or one of its sub-classes). The returned object is an array-iterator object (the same object returned by the .flat attribute of the ndarray). This object is usually cast to PyArrayIterObject\* so that its members can be accessed. The only members that are needed are `iter->size` which contains the total size of the array, `iter->index`, which contains the current 1-d index into the array, and `iter->dataptr` which is a pointer to the data for the current element of the array. Sometimes it is also useful to access `iter->ao` which is a pointer to the underlying ndarray object.

After processing data at the current element of the array, the next element of the array can be obtained using the macro [`PyArray_ITER_NEXT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ITER_NEXT "PyArray_ITER_NEXT")
 ( `iter` ). The iteration always proceeds in a C-style contiguous fashion (last index varying the fastest). The [`PyArray_ITER_GOTO`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ITER_GOTO "PyArray_ITER_GOTO")
 ( `iter`, `destination` ) can be used to jump to a particular point in the array, where `destination` is an array of npy\_intp data-type with space to handle at least the number of dimensions in the underlying array. Occasionally it is useful to use [`PyArray_ITER_GOTO1D`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ITER_GOTO1D "PyArray_ITER_GOTO1D")
 ( `iter`, `index` ) which will jump to the 1-d index given by the value of `index`. The most common usage, however, is given in the following example.

PyObject \*obj; /\* assumed to be some ndarray object \*/
PyArrayIterObject \*iter;
...
iter \= (PyArrayIterObject \*)PyArray\_IterNew(obj);
if (iter \== NULL) goto fail;   /\* Assume fail has clean-up code \*/
while (iter\->index < iter\->size) {
    /\* do something with the data at it->dataptr \*/
    PyArray\_ITER\_NEXT(it);
}
...

Copy to clipboard

You can also use [`PyArrayIter_Check`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArrayIter_Check "PyArrayIter_Check")
 ( `obj` ) to ensure you have an iterator object and [`PyArray_ITER_RESET`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ITER_RESET "PyArray_ITER_RESET")
 ( `iter` ) to reset an iterator object back to the beginning of the array.

It should be emphasized at this point that you may not need the array iterator if your array is already contiguous (using an array iterator will work but will be slower than the fastest code you could write). The major purpose of array iterators is to encapsulate iteration over N-dimensional arrays with arbitrary strides. They are used in many, many places in the NumPy source code itself. If you already know your array is contiguous (Fortran or C), then simply adding the element- size to a running pointer variable will step you through the array very efficiently. In other words, code like this will probably be faster for you in the contiguous case (assuming doubles).

npy\_intp size;
double \*dptr;  /\* could make this any variable type \*/
size \= PyArray\_SIZE(obj);
dptr \= PyArray\_DATA(obj);
while(size\--) {
   /\* do something with the data at dptr \*/
   dptr++;
}

Copy to clipboard

### Iterating over all but one axis[#](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#iterating-over-all-but-one-axis "Link to this heading")

A common algorithm is to loop over all elements of an array and perform some function with each element by issuing a function call. As function calls can be time consuming, one way to speed up this kind of algorithm is to write the function so it takes a vector of data and then write the iteration so the function call is performed for an entire dimension of data at a time. This increases the amount of work done per function call, thereby reducing the function-call over-head to a small(er) fraction of the total time. Even if the interior of the loop is performed without a function call it can be advantageous to perform the inner loop over the dimension with the highest number of elements to take advantage of speed enhancements available on micro- processors that use pipelining to enhance fundamental operations.

The [`PyArray_IterAllButAxis`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_IterAllButAxis "PyArray_IterAllButAxis")
 ( `array`, `&dim` ) constructs an iterator object that is modified so that it will not iterate over the dimension indicated by dim. The only restriction on this iterator object, is that the [`PyArray_ITER_GOTO1D`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_ITER_GOTO1D "PyArray_ITER_GOTO1D")
 ( `it`, `ind` ) macro cannot be used (thus flat indexing won’t work either if you pass this object back to Python — so you shouldn’t do this). Note that the returned object from this routine is still usually cast to PyArrayIterObject \*. All that’s been done is to modify the strides and dimensions of the returned iterator to simulate iterating over array\[…,0,…\] where 0 is placed on the \\(\\textrm{dim}^{\\textrm{th}}\\) dimension. If dim is negative, then the dimension with the largest axis is found and used.

### Iterating over multiple arrays[#](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#iterating-over-multiple-arrays "Link to this heading")

Very often, it is desirable to iterate over several arrays at the same time. The universal functions are an example of this kind of behavior. If all you want to do is iterate over arrays with the same shape, then simply creating several iterator objects is the standard procedure. For example, the following code iterates over two arrays assumed to be the same shape and size (actually obj1 just has to have at least as many total elements as does obj2):

/\* It is already assumed that obj1 and obj2
   are ndarrays of the same shape and size.
\*/
iter1 \= (PyArrayIterObject \*)PyArray\_IterNew(obj1);
if (iter1 \== NULL) goto fail;
iter2 \= (PyArrayIterObject \*)PyArray\_IterNew(obj2);
if (iter2 \== NULL) goto fail;  /\* assume iter1 is DECREF'd at fail \*/
while (iter2\->index < iter2\->size)  {
    /\* process with iter1->dataptr and iter2->dataptr \*/
    PyArray\_ITER\_NEXT(iter1);
    PyArray\_ITER\_NEXT(iter2);
}

Copy to clipboard

### Broadcasting over multiple arrays[#](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#broadcasting-over-multiple-arrays "Link to this heading")

When multiple arrays are involved in an operation, you may want to use the same broadcasting rules that the math operations (_i.e._ the ufuncs) use. This can be done easily using the [`PyArrayMultiIterObject`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMultiIterObject "PyArrayMultiIterObject")
. This is the object returned from the Python command numpy.broadcast and it is almost as easy to use from C. The function [`PyArray_MultiIterNew`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MultiIterNew "PyArray_MultiIterNew")
 ( `n`, `...` ) is used (with `n` input objects in place of `...` ). The input objects can be arrays or anything that can be converted into an array. A pointer to a PyArrayMultiIterObject is returned. Broadcasting has already been accomplished which adjusts the iterators so that all that needs to be done to advance to the next element in each array is for PyArray\_ITER\_NEXT to be called for each of the inputs. This incrementing is automatically performed by [`PyArray_MultiIter_NEXT`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MultiIter_NEXT "PyArray_MultiIter_NEXT")
 ( `obj` ) macro (which can handle a multiterator `obj` as either a [PyArrayMultiIterObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayMultiIterObject "PyArrayMultiIterObject")
\* or a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
\*). The data from input number `i` is available using [`PyArray_MultiIter_DATA`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_MultiIter_DATA "PyArray_MultiIter_DATA")
 ( `obj`, `i` ). An example of using this feature follows.

mobj \= PyArray\_MultiIterNew(2, obj1, obj2);
size \= mobj\->size;
while(size\--) {
    ptr1 \= PyArray\_MultiIter\_DATA(mobj, 0);
    ptr2 \= PyArray\_MultiIter\_DATA(mobj, 1);
    /\* code using contents of ptr1 and ptr2 \*/
    PyArray\_MultiIter\_NEXT(mobj);
}

Copy to clipboard

The function [`PyArray_RemoveSmallest`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_RemoveSmallest "PyArray_RemoveSmallest")
 ( `multi` ) can be used to take a multi-iterator object and adjust all the iterators so that iteration does not take place over the largest dimension (it makes that dimension of size 1). The code being looped over that makes use of the pointers will very-likely also need the strides data for each of the iterators. This information is stored in multi->iters\[i\]->strides.

There are several examples of using the multi-iterator in the NumPy source code as it makes N-dimensional broadcasting-code very simple to write. Browse the source for more examples.

User-defined data-types[#](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#user-defined-data-types "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

NumPy comes with 24 builtin data-types. While this covers a large majority of possible use cases, it is conceivable that a user may have a need for an additional data-type. There is some support for adding an additional data-type into the NumPy system. This additional data- type will behave much like a regular data-type except ufuncs must have 1-d loops registered to handle it separately. Also checking for whether or not other data-types can be cast “safely” to and from this new type or not will always return “can cast” unless you also register which types your new data-type can be cast to and from.

The NumPy source code includes an example of a custom data-type as part of its test suite. The file `_rational_tests.c.src` in the source code directory `numpy/_core/src/umath/` contains an implementation of a data-type that represents a rational number as the ratio of two 32 bit integers.

### Adding the new data-type[#](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#adding-the-new-data-type "Link to this heading")

To begin to make use of the new data-type, you need to first define a new Python type to hold the scalars of your new data-type. It should be acceptable to inherit from one of the array scalars if your new type has a binary compatible layout. This will allow your new data type to have the methods and attributes of array scalars. New data- types must have a fixed memory size (if you want to define a data-type that needs a flexible representation, like a variable-precision number, then use a pointer to the object as the data-type). The memory layout of the object structure for the new Python type must be PyObject\_HEAD followed by the fixed-size memory needed for the data- type. For example, a suitable structure for the new Python type is:

typedef struct {
   PyObject\_HEAD;
   some\_data\_type obval;
   /\* the name can be whatever you want \*/
} PySomeDataTypeObject;

Copy to clipboard

After you have defined a new Python type object, you must then define a new [`PyArray_Descr`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 structure whose typeobject member will contain a pointer to the data-type you’ve just defined. In addition, the required functions in the “.f” member must be defined: nonzero, copyswap, copyswapn, setitem, getitem, and cast. The more functions in the “.f” member you define, however, the more useful the new data-type will be. It is very important to initialize unused functions to NULL. This can be achieved using [`PyArray_InitArrFuncs`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_InitArrFuncs "PyArray_InitArrFuncs")
 (f).

Once a new [`PyArray_Descr`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 structure is created and filled with the needed information and useful functions you call [`PyArray_RegisterDataType`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_RegisterDataType "PyArray_RegisterDataType")
 (new\_descr). The return value from this call is an integer providing you with a unique type\_number that specifies your data-type. This type number should be stored and made available by your module so that other modules can use it to recognize your data-type.

Note that this API is inherently thread-unsafe. See [Thread Safety](https://numpy.org/doc/stable/reference/thread_safety.html#thread-safety)
 for more details about thread safety in NumPy.

### Registering a casting function[#](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#registering-a-casting-function "Link to this heading")

You may want to allow builtin (and other user-defined) data-types to be cast automatically to your data-type. In order to make this possible, you must register a casting function with the data-type you want to be able to cast from. This requires writing low-level casting functions for each conversion you want to support and then registering these functions with the data-type descriptor. A low-level casting function has the signature.

void castfunc(void \*from, void \*to, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 n, void \*fromarr, void \*toarr)[#](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#c.castfunc "Link to this definition")
  

Cast `n` elements `from` one type `to` another. The data to cast from is in a contiguous, correctly-swapped and aligned chunk of memory pointed to by from. The buffer to cast to is also contiguous, correctly-swapped and aligned. The fromarr and toarr arguments should only be used for flexible-element-sized arrays (string, unicode, void).

An example castfunc is:

static void
double\_to\_float(double \*from, float\* to, npy\_intp n,
                void\* ignore1, void\* ignore2) {
    while (n\--) {
          (\*to++) \= (double) \*(from++);
    }
}

Copy to clipboard

This could then be registered to convert doubles to floats using the code:

doub \= PyArray\_DescrFromType(NPY\_DOUBLE);
PyArray\_RegisterCastFunc(doub, NPY\_FLOAT,
     (PyArray\_VectorUnaryFunc \*)double\_to\_float);
Py\_DECREF(doub);

Copy to clipboard

### Registering coercion rules[#](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#registering-coercion-rules "Link to this heading")

By default, all user-defined data-types are not presumed to be safely castable to any builtin data-types. In addition builtin data-types are not presumed to be safely castable to user-defined data-types. This situation limits the ability of user-defined data-types to participate in the coercion system used by ufuncs and other times when automatic coercion takes place in NumPy. This can be changed by registering data-types as safely castable from a particular data-type object. The function [`PyArray_RegisterCanCast`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_RegisterCanCast "PyArray_RegisterCanCast")
 (from\_descr, totype\_number, scalarkind) should be used to specify that the data-type object from\_descr can be cast to the data-type with type number totype\_number. If you are not trying to alter scalar coercion rules, then use [`NPY_NOSCALAR`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SCALARKIND.NPY_NOSCALAR "NPY_NOSCALAR")
 for the scalarkind argument.

If you want to allow your new data-type to also be able to share in the scalar coercion rules, then you need to specify the scalarkind function in the data-type object’s “.f” member to return the kind of scalar the new data-type should be seen as (the value of the scalar is available to that function). Then, you can register data-types that can be cast to separately for each scalar kind that may be returned from your user-defined data-type. If you don’t register scalar coercion handling, then all of your user-defined data-types will be seen as [`NPY_NOSCALAR`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_SCALARKIND.NPY_NOSCALAR "NPY_NOSCALAR")
.

### Registering a ufunc loop[#](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#registering-a-ufunc-loop "Link to this heading")

You may also want to register low-level ufunc loops for your data-type so that an ndarray of your data-type can have math applied to it seamlessly. Registering a new loop with exactly the same arg\_types signature, silently replaces any previously registered loops for that data-type.

Before you can register a 1-d loop for a ufunc, the ufunc must be previously created. Then you call [`PyUFunc_RegisterLoopForType`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_RegisterLoopForType "PyUFunc_RegisterLoopForType")
 (…) with the information needed for the loop. The return value of this function is `0` if the process was successful and `-1` with an error condition set if it was not successful.

Subtyping the ndarray in C[#](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#subtyping-the-ndarray-in-c "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

One of the lesser-used features that has been lurking in Python since 2.2 is the ability to sub-class types in C. This facility is one of the important reasons for basing NumPy off of the Numeric code-base which was already in C. A sub-type in C allows much more flexibility with regards to memory management. Sub-typing in C is not difficult even if you have only a rudimentary understanding of how to create new types for Python. While it is easiest to sub-type from a single parent type, sub-typing from multiple parent types is also possible. Multiple inheritance in C is generally less useful than it is in Python because a restriction on Python sub-types is that they have a binary compatible memory layout. Perhaps for this reason, it is somewhat easier to sub-type from a single parent type.

All C-structures corresponding to Python objects must begin with [`PyObject_HEAD`](https://docs.python.org/3/c-api/structures.html#c.PyObject_HEAD "(in Python v3.14)")
 (or [`PyObject_VAR_HEAD`](https://docs.python.org/3/c-api/structures.html#c.PyObject_VAR_HEAD "(in Python v3.14)")
). In the same way, any sub-type must have a C-structure that begins with exactly the same memory layout as the parent type (or all of the parent types in the case of multiple-inheritance). The reason for this is that Python may attempt to access a member of the sub-type structure as if it had the parent structure ( _i.e._ it will cast a given pointer to a pointer to the parent structure and then dereference one of it’s members). If the memory layouts are not compatible, then this attempt will cause unpredictable behavior (eventually leading to a memory violation and program crash).

One of the elements in [`PyObject_HEAD`](https://docs.python.org/3/c-api/structures.html#c.PyObject_HEAD "(in Python v3.14)")
 is a pointer to a type-object structure. A new Python type is created by creating a new type-object structure and populating it with functions and pointers to describe the desired behavior of the type. Typically, a new C-structure is also created to contain the instance-specific information needed for each object of the type as well. For example, [`&PyArray_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Type "PyArray_Type")
 is a pointer to the type-object table for the ndarray while a [PyArrayObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")
\* variable is a pointer to a particular instance of an ndarray (one of the members of the ndarray structure is, in turn, a pointer to the type- object table [`&PyArray_Type`](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Type "PyArray_Type")
). Finally [`PyType_Ready`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "(in Python v3.14)")
 (<pointer\_to\_type\_object>) must be called for every new Python type.

### Creating sub-types[#](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#creating-sub-types "Link to this heading")

To create a sub-type, a similar procedure must be followed except only behaviors that are different require new entries in the type- object structure. All other entries can be NULL and will be filled in by [`PyType_Ready`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "(in Python v3.14)")
 with appropriate functions from the parent type(s). In particular, to create a sub-type in C follow these steps:

1.  If needed create a new C-structure to handle each instance of your type. A typical C-structure would be:
    
    typedef \_new\_struct {
        PyArrayObject base;
        /\* new things here \*/
    } NewArrayObject;
    
    Copy to clipboard
    
    Notice that the full PyArrayObject is used as the first entry in order to ensure that the binary layout of instances of the new type is identical to the PyArrayObject.
    
2.  Fill in a new Python type-object structure with pointers to new functions that will over-ride the default behavior while leaving any function that should remain the same unfilled (or NULL). The tp\_name element should be different.
    
3.  Fill in the tp\_base member of the new type-object structure with a pointer to the (main) parent type object. For multiple-inheritance, also fill in the tp\_bases member with a tuple containing all of the parent objects in the order they should be used to define inheritance. Remember, all parent-types must have the same C-structure for multiple inheritance to work properly.
    
4.  Call [`PyType_Ready`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "(in Python v3.14)")
     (<pointer\_to\_new\_type>). If this function returns a negative number, a failure occurred and the type is not initialized. Otherwise, the type is ready to be used. It is generally important to place a reference to the new type into the module dictionary so it can be accessed from Python.
    

More information on creating sub-types in C can be learned by reading PEP 253 (available at [https://www.python.org/dev/peps/pep-0253](https://www.python.org/dev/peps/pep-0253)
).

### Specific features of ndarray sub-typing[#](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#specific-features-of-ndarray-sub-typing "Link to this heading")

Some special methods and attributes are used by arrays in order to facilitate the interoperation of sub-types with the base ndarray type.

#### The \_\_array\_finalize\_\_ method[#](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#the-array-finalize-method "Link to this heading")

ndarray.\_\_array\_finalize\_\_[#](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#ndarray.__array_finalize__ "Link to this definition")

Several array-creation functions of the ndarray allow specification of a particular sub-type to be created. This allows sub-types to be handled seamlessly in many routines. When a sub-type is created in such a fashion, however, neither the \_\_new\_\_ method nor the \_\_init\_\_ method gets called. Instead, the sub-type is allocated and the appropriate instance-structure members are filled in. Finally, the [`__array_finalize__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_finalize__ "numpy.class.__array_finalize__")
 attribute is looked-up in the object dictionary. If it is present and not None, then it can be either a [`PyCapsule`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule "(in Python v3.14)")
 containing a pointer to a [`PyArray_FinalizeFunc`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_FinalizeFunc "PyArray_FinalizeFunc")
 or it can be a method taking a single argument (which could be None)

If the [`__array_finalize__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_finalize__ "numpy.class.__array_finalize__")
 attribute is a [`PyCapsule`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule "(in Python v3.14)")
, then the pointer must be a pointer to a function with the signature:

(int) (PyArrayObject \*, PyObject \*)

Copy to clipboard

The first argument is the newly created sub-type. The second argument (if not NULL) is the “parent” array (if the array was created using slicing or some other operation where a clearly-distinguishable parent is present). This routine can do anything it wants to. It should return a -1 on error and 0 otherwise.

If the [`__array_finalize__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_finalize__ "numpy.class.__array_finalize__")
 attribute is not None nor a [`PyCapsule`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule "(in Python v3.14)")
, then it must be a Python method that takes the parent array as an argument (which could be None if there is no parent), and returns nothing. Errors in this method will be caught and handled.

#### The \_\_array\_priority\_\_ attribute[#](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#the-array-priority-attribute "Link to this heading")

ndarray.\_\_array\_priority\_\_[#](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#ndarray.__array_priority__ "Link to this definition")

This attribute allows simple but flexible determination of which sub- type should be considered “primary” when an operation involving two or more sub-types arises. In operations where different sub-types are being used, the sub-type with the largest [`__array_priority__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_priority__ "numpy.class.__array_priority__")
 attribute will determine the sub-type of the output(s). If two sub- types have the same [`__array_priority__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_priority__ "numpy.class.__array_priority__")
 then the sub-type of the first argument determines the output. The default [`__array_priority__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_priority__ "numpy.class.__array_priority__")
 attribute returns a value of 0.0 for the base ndarray type and 1.0 for a sub-type. This attribute can also be defined by objects that are not sub-types of the ndarray and can be used to determine which [`__array_wrap__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_wrap__ "numpy.class.__array_wrap__")
 method should be called for the return output.

#### The \_\_array\_wrap\_\_ method[#](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#the-array-wrap-method "Link to this heading")

ndarray.\_\_array\_wrap\_\_[#](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#ndarray.__array_wrap__ "Link to this definition")

Any class or type can define this method which should take an ndarray argument and return an instance of the type. It can be seen as the opposite of the [`__array__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array__ "numpy.class.__array__")
 method. This method is used by the ufuncs (and other NumPy functions) to allow other objects to pass through. For Python >2.4, it can also be used to write a decorator that converts a function that works only with ndarrays to one that works with any type with [`__array__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array__ "numpy.class.__array__")
 and [`__array_wrap__`](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_wrap__ "numpy.class.__array_wrap__")
 methods.

On this page