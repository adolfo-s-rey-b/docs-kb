[Skip to main content](https://numpy.org/doc/stable/reference/c-api/ufunc.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/c-api/ufunc.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/c-api/ufunc.html)
[2.4](https://numpy.org/doc/2.4/reference/c-api/ufunc.html)
[2.3](https://numpy.org/doc/2.3/reference/c-api/ufunc.html)
[2.2](https://numpy.org/doc/2.2/reference/c-api/ufunc.html)
[2.1](https://numpy.org/doc/2.1/reference/c-api/ufunc.html)
[2.0](https://numpy.org/doc/2.0/reference/c-api/ufunc.html)
[1.26](https://numpy.org/doc/1.26/reference/c-api/ufunc.html)
[1.25](https://numpy.org/doc/1.25/reference/c-api/ufunc.html)
[1.24](https://numpy.org/doc/1.24/reference/c-api/ufunc.html)
[1.23](https://numpy.org/doc/1.23/reference/c-api/ufunc.html)
[1.22](https://numpy.org/doc/1.22/reference/c-api/ufunc.html)
[1.21](https://numpy.org/doc/1.21/reference/c-api/ufunc.html)
[1.20](https://numpy.org/doc/1.20/reference/c-api/ufunc.html)
[1.19](https://numpy.org/doc/1.19/reference/c-api/ufunc.html)
[1.18](https://numpy.org/doc/1.18/reference/c-api/ufunc.html)
[1.17](https://numpy.org/doc/1.17/reference/c-api/ufunc.html)
[1.16](https://numpy.org/doc/1.16/reference/c-api/ufunc.html)
[1.15](https://numpy.org/doc/1.15/reference/c-api/ufunc.html)
[1.14](https://numpy.org/doc/1.14/reference/c-api/ufunc.html)
[1.13](https://numpy.org/doc/1.13/reference/c-api/ufunc.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

ufunc API[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#ufunc-api "Link to this heading")

=======================================================================================================

Constants[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#constants "Link to this heading")

-------------------------------------------------------------------------------------------------------

`UFUNC_{THING}_{ERR}`

> Deprecated, use `NPY_{THING}_{ERR}` instead
> 
> UFUNC\_FPE\_DIVIDEBYZERO[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.UFUNC_FPE_DIVIDEBYZERO "Link to this definition")
>   
> 
> UFUNC\_FPE\_OVERFLOW[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.UFUNC_FPE_OVERFLOW "Link to this definition")
>   
> 
> UFUNC\_FPE\_UNDERFLOW[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.UFUNC_FPE_UNDERFLOW "Link to this definition")
>   
> 
> UFUNC\_FPE\_INVALID[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.UFUNC_FPE_INVALID "Link to this definition")
>   

`PyUFunc_{VALUE}`

PyUFunc\_One[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_One "Link to this definition")
  

PyUFunc\_Zero[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_Zero "Link to this definition")
  

PyUFunc\_MinusOne[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_MinusOne "Link to this definition")
  

PyUFunc\_ReorderableNone[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_ReorderableNone "Link to this definition")
  

PyUFunc\_None[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_None "Link to this definition")
  

PyUFunc\_IdentityValue[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_IdentityValue "Link to this definition")
  

Macros[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#macros "Link to this heading")

-------------------------------------------------------------------------------------------------

NPY\_LOOP\_BEGIN\_THREADS[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.NPY_LOOP_BEGIN_THREADS "Link to this definition")
  

Used in universal function code to only release the Python GIL if loop->obj is not true (_i.e._ this is not an OBJECT array loop). Requires use of [`NPY_BEGIN_THREADS_DEF`](https://numpy.org/doc/stable/reference/c-api/array.html#c.NPY_BEGIN_THREADS_DEF "NPY_BEGIN_THREADS_DEF")
 in variable declaration area.

NPY\_LOOP\_END\_THREADS[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.NPY_LOOP_END_THREADS "Link to this definition")
  

Used in universal function code to re-acquire the Python GIL if it was released (because loop->obj was not true).

Types[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#types "Link to this heading")

-----------------------------------------------------------------------------------------------

type PyUFuncGenericFunction[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFuncGenericFunction "Link to this definition")
  

Pointers to functions that actually implement the underlying (element-by-element) function \\(N\\) times with the following signature:

void loopfunc(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*data)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFuncGenericFunction.loopfunc "Link to this definition")
  

Parameters:

*   **args** – An array of pointers to the actual data for the input and output arrays. The input arguments are given first followed by the output arguments.
    
*   **dimensions** – A pointer to the size of the dimension over which this function is looping.
    
*   **steps** – A pointer to the number of bytes to jump to get to the next element in this dimension for each of the input and output arguments.
    
*   **data** –
    
    Arbitrary data (extra arguments, function names, _etc._ ) that can be stored with the ufunc and will be passed in when it is called. May be `NULL`.
    
    Changed in version 1.23.0: Accepts `NULL` _data_ in addition to array of `NULL` values.
    

This is an example of a func specialized for addition of doubles returning doubles.

static void
double\_add(char \*\*args,
           npy\_intp const \*dimensions,
           npy\_intp const \*steps,
           void \*extra)
{
    npy\_intp i;
    npy\_intp is1 \= steps\[0\], is2 \= steps\[1\];
    npy\_intp os \= steps\[2\], n \= dimensions\[0\];
    char \*i1 \= args\[0\], \*i2 \= args\[1\], \*op \= args\[2\];
    for (i \= 0; i < n; i++) {
        \*((double \*)op) \= \*((double \*)i1) +
                          \*((double \*)i2);
        i1 += is1;
        i2 += is2;
        op += os;
     }
}

Copy to clipboard

Functions[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#functions "Link to this heading")

-------------------------------------------------------------------------------------------------------

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyUFunc\_FromFuncAndData([PyUFuncGenericFunction](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFuncGenericFunction "PyUFuncGenericFunction")
 \*func, void \*const \*data, const char \*types, int ntypes, int nin, int nout, int identity, const char \*name, const char \*doc, int unused)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_FromFuncAndData "Link to this definition")
  

Create a new broadcasting universal function from required variables. Each ufunc builds around the notion of an element-by-element operation. Each ufunc object contains pointers to 1-d loops implementing the basic functionality for each supported type.

Note

The _func_, _data_, _types_, _name_, and _doc_ arguments are not copied by [`PyUFunc_FromFuncAndData`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_FromFuncAndData "PyUFunc_FromFuncAndData")
. The caller must ensure that the memory used by these arrays is not freed as long as the ufunc object is alive.

Parameters:

*   **func** – Must point to an array containing _ntypes_ [`PyUFuncGenericFunction`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFuncGenericFunction "PyUFuncGenericFunction")
     elements.
    
*   **data** – Should be `NULL` or a pointer to an array of size _ntypes_. This array may contain arbitrary extra-data to be passed to the corresponding loop function in the func array, including `NULL`.
    
*   **types** –
    
    Length `(nin + nout) * ntypes` array of `char` encoding the [`numpy.dtype.num`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.num.html#numpy.dtype.num "numpy.dtype.num")
     (built-in only) that the corresponding function in the `func` array accepts. For instance, for a comparison ufunc with three `ntypes`, two `nin` and one `nout`, where the first function accepts [`numpy.int32`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int32 "numpy.int32")
     and the second [`numpy.int64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
    , with both returning [`numpy.bool_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool_ "numpy.bool_")
    , `types` would be `(char[]) {5, 5, 0, 7, 7, 0}` since `NPY_INT32` is 5, `NPY_INT64` is 7, and `NPY_BOOL` is 0.
    
    The bit-width names can also be used (e.g. [`NPY_INT32`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_INT32 "NPY_INT32")
    , [`NPY_COMPLEX128`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_COMPLEX128 "NPY_COMPLEX128")
     ) if desired.
    
    [Type casting rules](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-casting)
     will be used at runtime to find the first `func` callable by the input/output provided.
    
*   **ntypes** – How many different data-type-specific functions the ufunc has implemented.
    
*   **nin** – The number of inputs to this operation.
    
*   **nout** – The number of outputs
    
*   **identity** – Either [`PyUFunc_One`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_One "PyUFunc_One")
    , [`PyUFunc_Zero`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_Zero "PyUFunc_Zero")
    , [`PyUFunc_MinusOne`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_MinusOne "PyUFunc_MinusOne")
    , or [`PyUFunc_None`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_None "PyUFunc_None")
    . This specifies what should be returned when an empty array is passed to the reduce method of the ufunc. The special value [`PyUFunc_IdentityValue`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_IdentityValue "PyUFunc_IdentityValue")
     may only be used with the [`PyUFunc_FromFuncAndDataAndSignatureAndIdentity`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_FromFuncAndDataAndSignatureAndIdentity "PyUFunc_FromFuncAndDataAndSignatureAndIdentity")
     method, to allow an arbitrary python object to be used as the identity.
    
*   **name** – The name for the ufunc as a `NULL` terminated string. Specifying a name of ‘add’ or ‘multiply’ enables a special behavior for integer-typed reductions when no dtype is given. If the input type is an integer (or boolean) data type smaller than the size of the [`numpy.int_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int_ "numpy.int_")
     data type, it will be internally upcast to the [`numpy.int_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int_ "numpy.int_")
     (or [`numpy.uint`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint "numpy.uint")
    ) data type.
    
*   **doc** – Allows passing in a documentation string to be stored with the ufunc. The documentation string should not contain the name of the function or the calling signature as that will be dynamically determined from the object and available when accessing the **\_\_doc\_\_** attribute of the ufunc.
    
*   **unused** – Unused and present for backwards compatibility of the C-API.
    

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyUFunc\_FromFuncAndDataAndSignature([PyUFuncGenericFunction](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFuncGenericFunction "PyUFuncGenericFunction")
 \*func, void \*const \*data, const char \*types, int ntypes, int nin, int nout, int identity, const char \*name, const char \*doc, int unused, const char \*signature)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_FromFuncAndDataAndSignature "Link to this definition")
  

This function is very similar to PyUFunc\_FromFuncAndData above, but has an extra _signature_ argument, to define a [generalized universal functions](https://numpy.org/doc/stable/reference/c-api/generalized-ufuncs.html#c-api-generalized-ufuncs)
. Similarly to how ufuncs are built around an element-by-element operation, gufuncs are around subarray-by-subarray operations, the [signature](https://numpy.org/doc/stable/reference/c-api/generalized-ufuncs.html#details-of-signature)
 defining the subarrays to operate on.

Parameters:

*   **signature** – The signature for the new gufunc. Setting it to NULL is equivalent to calling PyUFunc\_FromFuncAndData. A copy of the string is made, so the passed in buffer can be freed.
    

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyUFunc\_FromFuncAndDataAndSignatureAndIdentity([PyUFuncGenericFunction](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFuncGenericFunction "PyUFuncGenericFunction")
 \*func, void \*\*data, char \*types, int ntypes, int nin, int nout, int identity, char \*name, char \*doc, int unused, char \*signature, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*identity\_value)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_FromFuncAndDataAndSignatureAndIdentity "Link to this definition")
  

This function is very similar to [`PyUFunc_FromFuncAndDataAndSignature`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_FromFuncAndDataAndSignature "PyUFunc_FromFuncAndDataAndSignature")
 above, but has an extra _identity\_value_ argument, to define an arbitrary identity for the ufunc when `identity` is passed as `PyUFunc_IdentityValue`.

Parameters:

*   **identity\_value** – The identity for the new gufunc. Must be passed as `NULL` unless the `identity` argument is `PyUFunc_IdentityValue`. Setting it to NULL is equivalent to calling PyUFunc\_FromFuncAndDataAndSignature.
    

int PyUFunc\_RegisterLoopForType([PyUFuncObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject "PyUFuncObject")
 \*ufunc, int usertype, [PyUFuncGenericFunction](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFuncGenericFunction "PyUFuncGenericFunction")
 function, int \*arg\_types, void \*data)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_RegisterLoopForType "Link to this definition")
  

This function allows the user to register a 1-d loop with an already- created ufunc to be used whenever the ufunc is called with any of its input arguments as the user-defined data-type. This is needed in order to make ufuncs work with built-in data-types. The data-type must have been previously registered with the numpy system. The loop is passed in as _function_. This loop can take arbitrary data which should be passed in as _data_. The data-types the loop requires are passed in as _arg\_types_ which must be a pointer to memory at least as large as ufunc->nargs.

int PyUFunc\_RegisterLoopForDescr([PyUFuncObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject "PyUFuncObject")
 \*ufunc, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*userdtype, [PyUFuncGenericFunction](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFuncGenericFunction "PyUFuncGenericFunction")
 function, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*\*arg\_dtypes, void \*data)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_RegisterLoopForDescr "Link to this definition")
  

This function behaves like PyUFunc\_RegisterLoopForType above, except that it allows the user to register a 1-d loop using PyArray\_Descr objects instead of dtype type num values. This allows a 1-d loop to be registered for structured array data-dtypes and custom data-types instead of scalar data-types.

int PyUFunc\_ReplaceLoopBySignature([PyUFuncObject](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyUFuncObject "PyUFuncObject")
 \*ufunc, [PyUFuncGenericFunction](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFuncGenericFunction "PyUFuncGenericFunction")
 newfunc, int \*signature, [PyUFuncGenericFunction](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFuncGenericFunction "PyUFuncGenericFunction")
 \*oldfunc)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_ReplaceLoopBySignature "Link to this definition")
  

Replace a 1-d loop matching the given _signature_ in the already-created _ufunc_ with the new 1-d loop newfunc. Return the old 1-d loop function in _oldfunc_. Return 0 on success and -1 on failure. This function works only with built-in types (use [`PyUFunc_RegisterLoopForType`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_RegisterLoopForType "PyUFunc_RegisterLoopForType")
 for user-defined types). A signature is an array of data-type numbers indicating the inputs followed by the outputs assumed by the 1-d loop.

void PyUFunc\_clearfperr()[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_clearfperr "Link to this definition")
  

Clear the IEEE error flags.

Generic functions[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#generic-functions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

At the core of every ufunc is a collection of type-specific functions that defines the basic functionality for each of the supported types. These functions must evaluate the underlying function \\(N\\geq1\\) times. Extra-data may be passed in that may be used during the calculation. This feature allows some general functions to be used as these basic looping functions. The general function has all the code needed to point variables to the right place and set up a function call. The general function assumes that the actual function to call is passed in as the extra data and calls it with the correct values. All of these functions are suitable for placing directly in the array of functions stored in the functions member of the PyUFuncObject structure.

void PyUFunc\_f\_f\_As\_d\_d(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_f_f_As_d_d "Link to this definition")
  

void PyUFunc\_d\_d(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_d_d "Link to this definition")
  

void PyUFunc\_f\_f(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_f_f "Link to this definition")
  

void PyUFunc\_g\_g(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_g_g "Link to this definition")
  

void PyUFunc\_F\_F\_As\_D\_D(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_F_F_As_D_D "Link to this definition")
  

void PyUFunc\_F\_F(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_F_F "Link to this definition")
  

void PyUFunc\_D\_D(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_D_D "Link to this definition")
  

void PyUFunc\_G\_G(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_G_G "Link to this definition")
  

void PyUFunc\_e\_e(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_e_e "Link to this definition")
  

void PyUFunc\_e\_e\_As\_f\_f(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_e_e_As_f_f "Link to this definition")
  

void PyUFunc\_e\_e\_As\_d\_d(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_e_e_As_d_d "Link to this definition")
  

Type specific, core 1-d functions for ufuncs where each calculation is obtained by calling a function taking one input argument and returning one output. This function is passed in `func`. The letters correspond to dtypechar’s of the supported data types ( `e` - half, `f` - float, `d` - double, `g` - long double, `F` - cfloat, `D` - cdouble, `G` - clongdouble). The argument _func_ must support the same signature. The \_As\_X\_X variants assume ndarray’s of one data type but cast the values to use an underlying function that takes a different data type. Thus, [`PyUFunc_f_f_As_d_d`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_f_f_As_d_d "PyUFunc_f_f_As_d_d")
 uses ndarrays of data type [`NPY_FLOAT`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_FLOAT "NPY_FLOAT")
 but calls out to a C-function that takes double and returns double.

void PyUFunc\_ff\_f\_As\_dd\_d(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_ff_f_As_dd_d "Link to this definition")
  

void PyUFunc\_ff\_f(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_ff_f "Link to this definition")
  

void PyUFunc\_dd\_d(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_dd_d "Link to this definition")
  

void PyUFunc\_gg\_g(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_gg_g "Link to this definition")
  

void PyUFunc\_FF\_F\_As\_DD\_D(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_FF_F_As_DD_D "Link to this definition")
  

void PyUFunc\_DD\_D(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_DD_D "Link to this definition")
  

void PyUFunc\_FF\_F(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_FF_F "Link to this definition")
  

void PyUFunc\_GG\_G(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_GG_G "Link to this definition")
  

void PyUFunc\_ee\_e(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_ee_e "Link to this definition")
  

void PyUFunc\_ee\_e\_As\_ff\_f(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_ee_e_As_ff_f "Link to this definition")
  

void PyUFunc\_ee\_e\_As\_dd\_d(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_ee_e_As_dd_d "Link to this definition")
  

Type specific, core 1-d functions for ufuncs where each calculation is obtained by calling a function taking two input arguments and returning one output. The underlying function to call is passed in as _func_. The letters correspond to dtypechar’s of the specific data type supported by the general-purpose function. The argument `func` must support the corresponding signature. The `_As_XX_X` variants assume ndarrays of one data type but cast the values at each iteration of the loop to use the underlying function that takes a different data type.

void PyUFunc\_O\_O(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_O_O "Link to this definition")
  

void PyUFunc\_OO\_O(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_OO_O "Link to this definition")
  

One-input, one-output, and two-input, one-output core 1-d functions for the [`NPY_OBJECT`](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.NPY_TYPES.NPY_OBJECT "NPY_OBJECT")
 data type. These functions handle reference count issues and return early on error. The actual function to call is _func_ and it must accept calls with the signature `(PyObject*) (PyObject*)` for [`PyUFunc_O_O`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_O_O "PyUFunc_O_O")
 or `(PyObject*)(PyObject *, PyObject *)` for [`PyUFunc_OO_O`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_OO_O "PyUFunc_OO_O")
.

void PyUFunc\_O\_O\_method(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_O_O_method "Link to this definition")
  

This general purpose 1-d core function assumes that _func_ is a string representing a method of the input object. For each iteration of the loop, the Python object is extracted from the array and its _func_ method is called returning the result to the output array.

void PyUFunc\_OO\_O\_method(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_OO_O_method "Link to this definition")
  

This general purpose 1-d core function assumes that _func_ is a string representing a method of the input object that takes one argument. The first argument in _args_ is the method whose function is called, the second argument in _args_ is the argument passed to the function. The output of the function is stored in the third entry of _args_.

void PyUFunc\_On\_Om(char \*\*args, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*dimensions, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 const \*steps, void \*func)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_On_Om "Link to this definition")
  

This is the 1-d core function used by the dynamic ufuncs created by umath.frompyfunc(function, nin, nout). In this case _func_ is a pointer to a [`PyUFunc_PyFuncData`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_On_Om.PyUFunc_PyFuncData "PyUFunc_PyFuncData")
 structure which has definition

type PyUFunc\_PyFuncData[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_On_Om.PyUFunc_PyFuncData "Link to this definition")
  

typedef struct {
    int nin;
    int nout;
    PyObject \*callable;
} PyUFunc\_PyFuncData;

Copy to clipboard

At each iteration of the loop, the _nin_ input objects are extracted from their object arrays and placed into an argument tuple, the Python _callable_ is called with the input arguments, and the nout outputs are placed into their object arrays.

Importing the API[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#importing-the-api "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

PY\_UFUNC\_UNIQUE\_SYMBOL[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PY_UFUNC_UNIQUE_SYMBOL "Link to this definition")
  

NO\_IMPORT\_UFUNC[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.NO_IMPORT_UFUNC "Link to this definition")
  

int PyUFunc\_ImportUFuncAPI(void)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_ImportUFuncAPI "Link to this definition")
  

Ensures that the UFunc C-API is imported and usable. It returns `0` on success and `-1` with an error set if NumPy couldn’t be imported. While preferable to call it once at module initialization, this function is very light-weight if called multiple times.

New in version 2.0: This function mainly checks for `PyUFunc_API == NULL` so it can be manually backported if desired.

import\_ufunc(void)[#](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.import_ufunc "Link to this definition")
  

These are the constants and functions for accessing the ufunc C-API from extension modules in precisely the same way as the array C-API can be accessed. The `import_ufunc` () function must always be called (in the initialization subroutine of the extension module). If your extension module is in one file then that is all that is required. The other two constants are useful if your extension module makes use of multiple files. In that case, define [`PY_UFUNC_UNIQUE_SYMBOL`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PY_UFUNC_UNIQUE_SYMBOL "PY_UFUNC_UNIQUE_SYMBOL")
 to something unique to your code and then in source files that do not contain the module initialization function but still need access to the UFUNC API, define [`PY_UFUNC_UNIQUE_SYMBOL`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PY_UFUNC_UNIQUE_SYMBOL "PY_UFUNC_UNIQUE_SYMBOL")
 to the same name used previously and also define [`NO_IMPORT_UFUNC`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.NO_IMPORT_UFUNC "NO_IMPORT_UFUNC")
.

The C-API is actually an array of function pointers. This array is created (and pointed to by a global variable) by import\_ufunc. The global variable is either statically defined or allowed to be seen by other files depending on the state of [`PY_UFUNC_UNIQUE_SYMBOL`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PY_UFUNC_UNIQUE_SYMBOL "PY_UFUNC_UNIQUE_SYMBOL")
 and [`NO_IMPORT_UFUNC`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.NO_IMPORT_UFUNC "NO_IMPORT_UFUNC")
.

On this page