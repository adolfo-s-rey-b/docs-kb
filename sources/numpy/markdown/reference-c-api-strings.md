[Skip to main content](https://numpy.org/doc/stable/reference/c-api/strings.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/c-api/strings.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/c-api/strings.html)
[2.4](https://numpy.org/doc/2.4/reference/c-api/strings.html)
[2.3](https://numpy.org/doc/2.3/reference/c-api/strings.html)
[2.2](https://numpy.org/doc/2.2/reference/c-api/strings.html)
[2.1](https://numpy.org/doc/2.1/reference/c-api/strings.html)
[2.0](https://numpy.org/doc/2.0/reference/c-api/strings.html)
[1.26](https://numpy.org/doc/1.26/reference/c-api/strings.html)
[1.25](https://numpy.org/doc/1.25/reference/c-api/strings.html)
[1.24](https://numpy.org/doc/1.24/reference/c-api/strings.html)
[1.23](https://numpy.org/doc/1.23/reference/c-api/strings.html)
[1.22](https://numpy.org/doc/1.22/reference/c-api/strings.html)
[1.21](https://numpy.org/doc/1.21/reference/c-api/strings.html)
[1.20](https://numpy.org/doc/1.20/reference/c-api/strings.html)
[1.19](https://numpy.org/doc/1.19/reference/c-api/strings.html)
[1.18](https://numpy.org/doc/1.18/reference/c-api/strings.html)
[1.17](https://numpy.org/doc/1.17/reference/c-api/strings.html)
[1.16](https://numpy.org/doc/1.16/reference/c-api/strings.html)
[1.15](https://numpy.org/doc/1.15/reference/c-api/strings.html)
[1.14](https://numpy.org/doc/1.14/reference/c-api/strings.html)
[1.13](https://numpy.org/doc/1.13/reference/c-api/strings.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

NpyString API[#](https://numpy.org/doc/stable/reference/c-api/strings.html#npystring-api "Link to this heading")

=================================================================================================================

New in version 2.0.

This API allows access to the UTF-8 string data stored in NumPy StringDType arrays. See [NEP-55](https://numpy.org/neps/nep-0055-string_dtype.html#nep55 "(in NumPy Enhancement Proposals)")
 for more in-depth details into the design of StringDType.

Examples[#](https://numpy.org/doc/stable/reference/c-api/strings.html#examples "Link to this heading")

-------------------------------------------------------------------------------------------------------

### Loading a String[#](https://numpy.org/doc/stable/reference/c-api/strings.html#loading-a-string "Link to this heading")

Say we are writing a ufunc implementation for `StringDType`. If we are given `const char *buf` pointer to the beginning of a `StringDType` array entry, and a `PyArray_Descr *` pointer to the array descriptor, one can access the underlying string data like so:

npy\_string\_allocator \*allocator \= NpyString\_acquire\_allocator(
        (PyArray\_StringDTypeObject \*)descr);

npy\_static\_string sdata \= {0, NULL};
npy\_packed\_static\_string \*packed\_string \= (npy\_packed\_static\_string \*)buf;
int is\_null \= 0;

is\_null \= NpyString\_load(allocator, packed\_string, &sdata);

if (is\_null \== \-1) {
    // failed to load string, set error
    return \-1;
}
else if (is\_null) {
    // handle missing string
    // sdata->buf is NULL
    // sdata->size is 0
}
else {
    // sdata->buf is a pointer to the beginning of a string
    // sdata->size is the size of the string
}
NpyString\_release\_allocator(allocator);

Copy to clipboard

### Packing a String[#](https://numpy.org/doc/stable/reference/c-api/strings.html#packing-a-string "Link to this heading")

This example shows how to pack a new string entry into an array:

char \*str \= "Hello world";
size\_t size \= 11;
npy\_packed\_static\_string \*packed\_string \= (npy\_packed\_static\_string \*)buf;

npy\_string\_allocator \*allocator \= NpyString\_acquire\_allocator(
        (PyArray\_StringDTypeObject \*)descr);

// copy contents of str into packed\_string
if (NpyString\_pack(allocator, packed\_string, str, size) \== \-1) {
    // string packing failed, set error
    return \-1;
}

// packed\_string contains a copy of "Hello world"

NpyString\_release\_allocator(allocator);

Copy to clipboard

Types[#](https://numpy.org/doc/stable/reference/c-api/strings.html#types "Link to this heading")

-------------------------------------------------------------------------------------------------

type npy\_packed\_static\_string[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.npy_packed_static_string "Link to this definition")
  

An opaque struct that represents “packed” encoded strings. Individual entries in array buffers are instances of this struct. Direct access to the data in the struct is undefined and future version of the library may change the packed representation of strings.

type npy\_static\_string[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.npy_static_string "Link to this definition")
  

An unpacked string allowing access to the UTF-8 string data.

typedef struct npy\_unpacked\_static\_string {
    size\_t size;
    const char \*buf;
} npy\_static\_string;

Copy to clipboard

size\_t size[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.npy_static_string.size "Link to this definition")
  

The size of the string, in bytes.

const char \*buf[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.npy_static_string.buf "Link to this definition")
  

The string buffer. Holds UTF-8-encoded bytes. Does not currently end in a null string but we may decide to add null termination in the future, so do not rely on the presence or absence of null-termination.

Note that this is a `const` buffer. If you want to alter an entry in an array, you should create a new string and pack it into the array entry.

type npy\_string\_allocator[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.npy_string_allocator "Link to this definition")
  

An opaque pointer to an object that handles string allocation. Before using the allocator, you must acquire the allocator lock and release the lock after you are done interacting with strings managed by the allocator.

type PyArray\_StringDTypeObject[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.PyArray_StringDTypeObject "Link to this definition")
  

The C struct backing instances of StringDType in Python. Attributes store the settings the object was created with, an instance of `npy_string_allocator` that manages string allocations for arrays associated with the DType instance, and several attributes caching information about the missing string object that is commonly needed in cast and ufunc loop implementations.

typedef struct {
    PyArray\_Descr base;
    PyObject \*na\_object;
    char coerce;
    char has\_nan\_na;
    char has\_string\_na;
    char array\_owned;
    npy\_static\_string default\_string;
    npy\_static\_string na\_name;
    npy\_string\_allocator \*allocator;
} PyArray\_StringDTypeObject;

Copy to clipboard

[PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 base[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.PyArray_StringDTypeObject.base "Link to this definition")
  

The base object. Use this member to access fields common to all descriptor objects.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*na\_object[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.PyArray_StringDTypeObject.na_object "Link to this definition")
  

A reference to the object representing the null value. If there is no null value (the default) this will be NULL.

char coerce[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.PyArray_StringDTypeObject.coerce "Link to this definition")
  

1 if string coercion is enabled, 0 otherwise.

char has\_nan\_na[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.PyArray_StringDTypeObject.has_nan_na "Link to this definition")
  

1 if the missing string object (if any) is NaN-like, 0 otherwise.

char has\_string\_na[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.PyArray_StringDTypeObject.has_string_na "Link to this definition")
  

1 if the missing string object (if any) is a string, 0 otherwise.

char array\_owned[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.PyArray_StringDTypeObject.array_owned "Link to this definition")
  

1 if an array owns the StringDType instance, 0 otherwise.

[npy\_static\_string](https://numpy.org/doc/stable/reference/c-api/strings.html#c.npy_static_string "npy_static_string")
 default\_string[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.PyArray_StringDTypeObject.default_string "Link to this definition")
  

The default string to use in operations. If the missing string object is a string, this will contain the string data for the missing string.

[npy\_static\_string](https://numpy.org/doc/stable/reference/c-api/strings.html#c.npy_static_string "npy_static_string")
 na\_name[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.PyArray_StringDTypeObject.na_name "Link to this definition")
  

The name of the missing string object, if any. An empty string otherwise.

[npy\_string\_allocator](https://numpy.org/doc/stable/reference/c-api/strings.html#c.npy_string_allocator "npy_string_allocator")
 allocator[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.PyArray_StringDTypeObject.allocator "Link to this definition")
  

The allocator instance associated with the array that owns this descriptor instance. The allocator should only be directly accessed after acquiring the allocator\_lock and the lock should be released immediately after the allocator is no longer needed

Functions[#](https://numpy.org/doc/stable/reference/c-api/strings.html#functions "Link to this heading")

---------------------------------------------------------------------------------------------------------

[npy\_string\_allocator](https://numpy.org/doc/stable/reference/c-api/strings.html#c.npy_string_allocator "npy_string_allocator")
 \*NpyString\_acquire\_allocator(const [PyArray\_StringDTypeObject](https://numpy.org/doc/stable/reference/c-api/strings.html#c.PyArray_StringDTypeObject "PyArray_StringDTypeObject")
 \*descr)[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.NpyString_acquire_allocator "Link to this definition")
  

Acquire the mutex locking the allocator attached to `descr`. `NpyString_release_allocator` must be called on the allocator returned by this function exactly once. Note that functions requiring the GIL should not be called while the allocator mutex is held, as doing so may cause deadlocks.

void NpyString\_acquire\_allocators(size\_t n\_descriptors, [PyArray\_Descr](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")
 \*const descrs\[\], [npy\_string\_allocator](https://numpy.org/doc/stable/reference/c-api/strings.html#c.npy_string_allocator "npy_string_allocator")
 \*allocators\[\])[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.NpyString_acquire_allocators "Link to this definition")
  

Simultaneously acquire the mutexes locking the allocators attached to multiple descriptors. Writes a pointer to the associated allocator in the allocators array for each StringDType descriptor in the array. If any of the descriptors are not StringDType instances, write NULL to the allocators array for that entry.

`n_descriptors` is the number of descriptors in the descrs array that should be examined. Any descriptor after `n_descriptors` elements is ignored. A buffer overflow will happen if the `descrs` array does not contain n\_descriptors elements.

If pointers to the same descriptor are passed multiple times, only acquires the allocator mutex once but sets identical allocator pointers appropriately. The allocator mutexes must be released after this function returns, see `NpyString_release_allocators`.

Note that functions requiring the GIL should not be called while the allocator mutex is held, as doing so may cause deadlocks.

void NpyString\_release\_allocator([npy\_string\_allocator](https://numpy.org/doc/stable/reference/c-api/strings.html#c.npy_string_allocator "npy_string_allocator")
 \*allocator)[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.NpyString_release_allocator "Link to this definition")
  

Release the mutex locking an allocator. This must be called exactly once after acquiring the allocator mutex and all operations requiring the allocator are done.

If you need to release multiple allocators, see NpyString\_release\_allocators, which can correctly handle releasing the allocator once when given several references to the same allocator.

void NpyString\_release\_allocators(size\_t length, [npy\_string\_allocator](https://numpy.org/doc/stable/reference/c-api/strings.html#c.npy_string_allocator "npy_string_allocator")
 \*allocators\[\])[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.NpyString_release_allocators "Link to this definition")
  

Release the mutexes locking N allocators. `length` is the length of the allocators array. NULL entries are ignored.

If pointers to the same allocator are passed multiple times, only releases the allocator mutex once.

int NpyString\_load([npy\_string\_allocator](https://numpy.org/doc/stable/reference/c-api/strings.html#c.npy_string_allocator "npy_string_allocator")
 \*allocator, const [npy\_packed\_static\_string](https://numpy.org/doc/stable/reference/c-api/strings.html#c.npy_packed_static_string "npy_packed_static_string")
 \*packed\_string, [npy\_static\_string](https://numpy.org/doc/stable/reference/c-api/strings.html#c.npy_static_string "npy_static_string")
 \*unpacked\_string)[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.NpyString_load "Link to this definition")
  

Extract the packed contents of `packed_string` into `unpacked_string`.

The `unpacked_string` is a read-only view onto the `packed_string` data and should not be used to modify the string data. If `packed_string` is the null string, sets `unpacked_string.buf` to the NULL pointer. Returns -1 if unpacking the string fails, returns 1 if `packed_string` is the null string, and returns 0 otherwise.

A useful pattern is to define a stack-allocated npy\_static\_string instance initialized to `{0, NULL}` and pass a pointer to the stack-allocated unpacked string to this function. This function can be used to simultaneously unpack a string and determine if it is a null string.

int NpyString\_pack\_null([npy\_string\_allocator](https://numpy.org/doc/stable/reference/c-api/strings.html#c.npy_string_allocator "npy_string_allocator")
 \*allocator, [npy\_packed\_static\_string](https://numpy.org/doc/stable/reference/c-api/strings.html#c.npy_packed_static_string "npy_packed_static_string")
 \*packed\_string)[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.NpyString_pack_null "Link to this definition")
  

Pack the null string into `packed_string`. Returns 0 on success and -1 on failure.

int NpyString\_pack([npy\_string\_allocator](https://numpy.org/doc/stable/reference/c-api/strings.html#c.npy_string_allocator "npy_string_allocator")
 \*allocator, [npy\_packed\_static\_string](https://numpy.org/doc/stable/reference/c-api/strings.html#c.npy_packed_static_string "npy_packed_static_string")
 \*packed\_string, const char \*buf, size\_t size)[#](https://numpy.org/doc/stable/reference/c-api/strings.html#c.NpyString_pack "Link to this definition")
  

Copy and pack the first `size` entries of the buffer pointed to by `buf` into the `packed_string`. Returns 0 on success and -1 on failure.

On this page