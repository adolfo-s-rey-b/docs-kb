[Skip to main content](https://numpy.org/doc/stable/reference/c-api/index.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/c-api/index.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/c-api/index.html)
[2.4](https://numpy.org/doc/2.4/reference/c-api/index.html)
[2.3](https://numpy.org/doc/2.3/reference/c-api/index.html)
[2.2](https://numpy.org/doc/2.2/reference/c-api/index.html)
[2.1](https://numpy.org/doc/2.1/reference/c-api/index.html)
[2.0](https://numpy.org/doc/2.0/reference/c-api/index.html)
[1.26](https://numpy.org/doc/1.26/reference/c-api/index.html)
[1.25](https://numpy.org/doc/1.25/reference/c-api/index.html)
[1.24](https://numpy.org/doc/1.24/reference/c-api/index.html)
[1.23](https://numpy.org/doc/1.23/reference/c-api/index.html)
[1.22](https://numpy.org/doc/1.22/reference/c-api/index.html)
[1.21](https://numpy.org/doc/1.21/reference/c-api/index.html)
[1.20](https://numpy.org/doc/1.20/reference/c-api/index.html)
[1.19](https://numpy.org/doc/1.19/reference/c-api/index.html)
[1.18](https://numpy.org/doc/1.18/reference/c-api/index.html)
[1.17](https://numpy.org/doc/1.17/reference/c-api/index.html)
[1.16](https://numpy.org/doc/1.16/reference/c-api/index.html)
[1.15](https://numpy.org/doc/1.15/reference/c-api/index.html)
[1.14](https://numpy.org/doc/1.14/reference/c-api/index.html)
[1.13](https://numpy.org/doc/1.13/reference/c-api/index.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

NumPy C-API[#](https://numpy.org/doc/stable/reference/c-api/index.html#numpy-c-api "Link to this heading")

===========================================================================================================

Beware of the man who won’t be bothered with details.

— _William Feather, Sr._

The truth is out there.

— _Chris Carter, The X Files_

NumPy provides a C-API to enable users to extend the system and get access to the array object for use in other routines. The best way to truly understand the C-API is to read the source code. If you are unfamiliar with (C) source code, however, this can be a daunting experience at first. Be assured that the task becomes easier with practice, and you may be surprised at how simple the C-code can be to understand. Even if you don’t think you can write C-code from scratch, it is much easier to understand and modify already-written source code than create it _de novo_.

Python extensions are especially straightforward to understand because they all have a very similar structure. Admittedly, NumPy is not a trivial extension to Python, and may take a little more snooping to grasp. This is especially true because of the code-generation techniques, which simplify maintenance of very similar code, but can make the code a little less readable to beginners. Still, with a little persistence, the code can be opened to your understanding. It is my hope, that this guide to the C-API can assist in the process of becoming familiar with the compiled-level work that can be done with NumPy in order to squeeze that last bit of necessary speed out of your code.

*   [Python types and C-structures](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html)
    *   [New Python types defined](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#new-python-types-defined)
        
    *   [Other C-structures](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#other-c-structures)
        
    *   [NumPy C-API and C complex](https://numpy.org/doc/stable/reference/c-api/types-and-structures.html#numpy-c-api-and-c-complex)
        
*   [System configuration](https://numpy.org/doc/stable/reference/c-api/config.html)
    *   [Data type sizes](https://numpy.org/doc/stable/reference/c-api/config.html#data-type-sizes)
        
    *   [Platform information](https://numpy.org/doc/stable/reference/c-api/config.html#platform-information)
        
    *   [Compiler directives](https://numpy.org/doc/stable/reference/c-api/config.html#compiler-directives)
        
*   [Data type API](https://numpy.org/doc/stable/reference/c-api/dtype.html)
    *   [Enumerated types](https://numpy.org/doc/stable/reference/c-api/dtype.html#enumerated-types)
        
    *   [Defines](https://numpy.org/doc/stable/reference/c-api/dtype.html#defines)
        
    *   [C-type names](https://numpy.org/doc/stable/reference/c-api/dtype.html#c-type-names)
        
    *   [Printf formatting](https://numpy.org/doc/stable/reference/c-api/dtype.html#printf-formatting)
        
*   [Array API](https://numpy.org/doc/stable/reference/c-api/array.html)
    *   [Array structure and data access](https://numpy.org/doc/stable/reference/c-api/array.html#array-structure-and-data-access)
        
    *   [Creating arrays](https://numpy.org/doc/stable/reference/c-api/array.html#creating-arrays)
        
    *   [Dealing with types](https://numpy.org/doc/stable/reference/c-api/array.html#dealing-with-types)
        
    *   [Array flags](https://numpy.org/doc/stable/reference/c-api/array.html#array-flags)
        
    *   [ArrayMethod API](https://numpy.org/doc/stable/reference/c-api/array.html#arraymethod-api)
        
    *   [API for calling array methods](https://numpy.org/doc/stable/reference/c-api/array.html#api-for-calling-array-methods)
        
    *   [Functions](https://numpy.org/doc/stable/reference/c-api/array.html#functions)
        
    *   [Auxiliary data with object semantics](https://numpy.org/doc/stable/reference/c-api/array.html#auxiliary-data-with-object-semantics)
        
    *   [Array iterators](https://numpy.org/doc/stable/reference/c-api/array.html#array-iterators)
        
    *   [Broadcasting (multi-iterators)](https://numpy.org/doc/stable/reference/c-api/array.html#broadcasting-multi-iterators)
        
    *   [Neighborhood iterator](https://numpy.org/doc/stable/reference/c-api/array.html#neighborhood-iterator)
        
    *   [Array scalars](https://numpy.org/doc/stable/reference/c-api/array.html#array-scalars)
        
    *   [Data-type descriptors](https://numpy.org/doc/stable/reference/c-api/array.html#data-type-descriptors)
        
    *   [Data Type Promotion and Inspection](https://numpy.org/doc/stable/reference/c-api/array.html#data-type-promotion-and-inspection)
        
    *   [Custom Data Types](https://numpy.org/doc/stable/reference/c-api/array.html#custom-data-types)
        
    *   [Conversion utilities](https://numpy.org/doc/stable/reference/c-api/array.html#conversion-utilities)
        
    *   [Including and importing the C API](https://numpy.org/doc/stable/reference/c-api/array.html#including-and-importing-the-c-api)
        
*   [Array iterator API](https://numpy.org/doc/stable/reference/c-api/iterator.html)
    *   [Array iterator](https://numpy.org/doc/stable/reference/c-api/iterator.html#array-iterator)
        
    *   [Iteration example](https://numpy.org/doc/stable/reference/c-api/iterator.html#iteration-example)
        
    *   [Multi-iteration example](https://numpy.org/doc/stable/reference/c-api/iterator.html#multi-iteration-example)
        
    *   [Multi index tracking example](https://numpy.org/doc/stable/reference/c-api/iterator.html#multi-index-tracking-example)
        
    *   [Iterator data types](https://numpy.org/doc/stable/reference/c-api/iterator.html#iterator-data-types)
        
    *   [Construction and destruction](https://numpy.org/doc/stable/reference/c-api/iterator.html#construction-and-destruction)
        
    *   [Functions for iteration](https://numpy.org/doc/stable/reference/c-api/iterator.html#functions-for-iteration)
        
    *   [Converting from previous NumPy iterators](https://numpy.org/doc/stable/reference/c-api/iterator.html#converting-from-previous-numpy-iterators)
        
*   [ufunc API](https://numpy.org/doc/stable/reference/c-api/ufunc.html)
    *   [Constants](https://numpy.org/doc/stable/reference/c-api/ufunc.html#constants)
        
    *   [Macros](https://numpy.org/doc/stable/reference/c-api/ufunc.html#macros)
        
    *   [Types](https://numpy.org/doc/stable/reference/c-api/ufunc.html#types)
        
    *   [Functions](https://numpy.org/doc/stable/reference/c-api/ufunc.html#functions)
        
    *   [Generic functions](https://numpy.org/doc/stable/reference/c-api/ufunc.html#generic-functions)
        
    *   [Importing the API](https://numpy.org/doc/stable/reference/c-api/ufunc.html#importing-the-api)
        
*   [Generalized universal function API](https://numpy.org/doc/stable/reference/c-api/generalized-ufuncs.html)
    *   [Definitions](https://numpy.org/doc/stable/reference/c-api/generalized-ufuncs.html#definitions)
        
    *   [Details of signature](https://numpy.org/doc/stable/reference/c-api/generalized-ufuncs.html#details-of-signature)
        
    *   [C-API for implementing elementary functions](https://numpy.org/doc/stable/reference/c-api/generalized-ufuncs.html#c-api-for-implementing-elementary-functions)
        
    *   [Customizing core dimension size processing](https://numpy.org/doc/stable/reference/c-api/generalized-ufuncs.html#customizing-core-dimension-size-processing)
        
*   [NpyString API](https://numpy.org/doc/stable/reference/c-api/strings.html)
    *   [Examples](https://numpy.org/doc/stable/reference/c-api/strings.html#examples)
        
    *   [Types](https://numpy.org/doc/stable/reference/c-api/strings.html#types)
        
    *   [Functions](https://numpy.org/doc/stable/reference/c-api/strings.html#functions)
        
*   [NumPy core math library](https://numpy.org/doc/stable/reference/c-api/coremath.html)
    *   [Floating point classification](https://numpy.org/doc/stable/reference/c-api/coremath.html#floating-point-classification)
        
    *   [Useful math constants](https://numpy.org/doc/stable/reference/c-api/coremath.html#useful-math-constants)
        
    *   [Low-level floating point manipulation](https://numpy.org/doc/stable/reference/c-api/coremath.html#low-level-floating-point-manipulation)
        
    *   [Support for complex numbers](https://numpy.org/doc/stable/reference/c-api/coremath.html#support-for-complex-numbers)
        
    *   [Linking against the core math library in an extension](https://numpy.org/doc/stable/reference/c-api/coremath.html#linking-against-the-core-math-library-in-an-extension)
        
    *   [Half-precision functions](https://numpy.org/doc/stable/reference/c-api/coremath.html#half-precision-functions)
        
*   [Datetime API](https://numpy.org/doc/stable/reference/c-api/datetimes.html)
    *   [Data types](https://numpy.org/doc/stable/reference/c-api/datetimes.html#data-types)
        
    *   [Conversion functions](https://numpy.org/doc/stable/reference/c-api/datetimes.html#conversion-functions)
        
*   [C API deprecations](https://numpy.org/doc/stable/reference/c-api/deprecations.html)
    *   [Background](https://numpy.org/doc/stable/reference/c-api/deprecations.html#background)
        
    *   [Deprecation mechanism NPY\_NO\_DEPRECATED\_API](https://numpy.org/doc/stable/reference/c-api/deprecations.html#deprecation-mechanism-npy-no-deprecated-api)
        
*   [Memory management in NumPy](https://numpy.org/doc/stable/reference/c-api/data_memory.html)
    *   [Historical overview](https://numpy.org/doc/stable/reference/c-api/data_memory.html#historical-overview)
        
    *   [Configurable memory routines in NumPy (NEP 49)](https://numpy.org/doc/stable/reference/c-api/data_memory.html#configurable-memory-routines-in-numpy-nep-49)
        
    *   [What happens when deallocating if there is no policy set](https://numpy.org/doc/stable/reference/c-api/data_memory.html#what-happens-when-deallocating-if-there-is-no-policy-set)
        
    *   [Example of memory tracing with `np.lib.tracemalloc_domain`](https://numpy.org/doc/stable/reference/c-api/data_memory.html#example-of-memory-tracing-with-np-lib-tracemalloc-domain)