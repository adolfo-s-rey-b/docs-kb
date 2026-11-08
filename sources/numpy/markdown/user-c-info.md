[Skip to main content](https://numpy.org/doc/stable/user/c-info.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/user/c-info.html)
[2.5 (stable)](https://numpy.org/doc/stable/user/c-info.html)
[2.4](https://numpy.org/doc/2.4/user/c-info.html)
[2.3](https://numpy.org/doc/2.3/user/c-info.html)
[2.2](https://numpy.org/doc/2.2/user/c-info.html)
[2.1](https://numpy.org/doc/2.1/user/c-info.html)
[2.0](https://numpy.org/doc/2.0/user/c-info.html)
[1.26](https://numpy.org/doc/1.26/user/c-info.html)
[1.25](https://numpy.org/doc/1.25/user/c-info.html)
[1.24](https://numpy.org/doc/1.24/user/c-info.html)
[1.23](https://numpy.org/doc/1.23/user/c-info.html)
[1.22](https://numpy.org/doc/1.22/user/c-info.html)
[1.21](https://numpy.org/doc/1.21/user/c-info.html)
[1.20](https://numpy.org/doc/1.20/user/c-info.html)
[1.19](https://numpy.org/doc/1.19/user/c-info.html)
[1.18](https://numpy.org/doc/1.18/user/c-info.html)
[1.17](https://numpy.org/doc/1.17/user/c-info.html)
[1.16](https://numpy.org/doc/1.16/user/c-info.html)
[1.15](https://numpy.org/doc/1.15/user/c-info.html)
[1.14](https://numpy.org/doc/1.14/user/c-info.html)
[1.13](https://numpy.org/doc/1.13/user/c-info.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Using NumPy C-API[#](https://numpy.org/doc/stable/user/c-info.html#using-numpy-c-api "Link to this heading")

=============================================================================================================

*   [How to extend NumPy](https://numpy.org/doc/stable/user/c-info.how-to-extend.html)
    *   [Writing an extension module](https://numpy.org/doc/stable/user/c-info.how-to-extend.html#writing-an-extension-module)
        
    *   [Required subroutine](https://numpy.org/doc/stable/user/c-info.how-to-extend.html#required-subroutine)
        
    *   [Defining functions](https://numpy.org/doc/stable/user/c-info.how-to-extend.html#defining-functions)
        *   [Functions without keyword arguments](https://numpy.org/doc/stable/user/c-info.how-to-extend.html#functions-without-keyword-arguments)
            
        *   [Functions with keyword arguments](https://numpy.org/doc/stable/user/c-info.how-to-extend.html#functions-with-keyword-arguments)
            
        *   [Reference counting](https://numpy.org/doc/stable/user/c-info.how-to-extend.html#reference-counting)
            
    *   [Dealing with array objects](https://numpy.org/doc/stable/user/c-info.how-to-extend.html#dealing-with-array-objects)
        *   [Converting an arbitrary sequence object](https://numpy.org/doc/stable/user/c-info.how-to-extend.html#converting-an-arbitrary-sequence-object)
            
        *   [Creating a brand-new ndarray](https://numpy.org/doc/stable/user/c-info.how-to-extend.html#creating-a-brand-new-ndarray)
            
        *   [Getting at ndarray memory and accessing elements of the ndarray](https://numpy.org/doc/stable/user/c-info.how-to-extend.html#getting-at-ndarray-memory-and-accessing-elements-of-the-ndarray)
            
    *   [Example](https://numpy.org/doc/stable/user/c-info.how-to-extend.html#example)
        
*   [Using Python as glue](https://numpy.org/doc/stable/user/c-info.python-as-glue.html)
    *   [Calling other compiled libraries from Python](https://numpy.org/doc/stable/user/c-info.python-as-glue.html#calling-other-compiled-libraries-from-python)
        
    *   [Hand-generated wrappers](https://numpy.org/doc/stable/user/c-info.python-as-glue.html#hand-generated-wrappers)
        
    *   [F2PY](https://numpy.org/doc/stable/user/c-info.python-as-glue.html#f2py)
        
    *   [Cython](https://numpy.org/doc/stable/user/c-info.python-as-glue.html#cython)
        *   [Complex addition in Cython](https://numpy.org/doc/stable/user/c-info.python-as-glue.html#complex-addition-in-cython)
            
        *   [Image filter in Cython](https://numpy.org/doc/stable/user/c-info.python-as-glue.html#image-filter-in-cython)
            
        *   [Conclusion](https://numpy.org/doc/stable/user/c-info.python-as-glue.html#conclusion)
            
    *   [ctypes](https://numpy.org/doc/stable/user/c-info.python-as-glue.html#index-2)
        *   [Having a shared library](https://numpy.org/doc/stable/user/c-info.python-as-glue.html#having-a-shared-library)
            
        *   [Loading the shared library](https://numpy.org/doc/stable/user/c-info.python-as-glue.html#loading-the-shared-library)
            
        *   [Converting arguments](https://numpy.org/doc/stable/user/c-info.python-as-glue.html#converting-arguments)
            
        *   [Calling the function](https://numpy.org/doc/stable/user/c-info.python-as-glue.html#calling-the-function)
            *   [`ndpointer`](https://numpy.org/doc/stable/user/c-info.python-as-glue.html#ndpointer)
                
        *   [Complete example](https://numpy.org/doc/stable/user/c-info.python-as-glue.html#complete-example)
            
        *   [Conclusion](https://numpy.org/doc/stable/user/c-info.python-as-glue.html#id4)
            
    *   [Additional tools you may find useful](https://numpy.org/doc/stable/user/c-info.python-as-glue.html#additional-tools-you-may-find-useful)
        *   [SWIG](https://numpy.org/doc/stable/user/c-info.python-as-glue.html#swig)
            
        *   [SIP](https://numpy.org/doc/stable/user/c-info.python-as-glue.html#sip)
            
        *   [Boost Python](https://numpy.org/doc/stable/user/c-info.python-as-glue.html#boost-python)
            
        *   [Pyfort](https://numpy.org/doc/stable/user/c-info.python-as-glue.html#pyfort)
            
*   [Writing your own ufunc](https://numpy.org/doc/stable/user/c-info.ufunc-tutorial.html)
    *   [Creating a new universal function](https://numpy.org/doc/stable/user/c-info.ufunc-tutorial.html#creating-a-new-universal-function)
        
    *   [Example non-ufunc extension](https://numpy.org/doc/stable/user/c-info.ufunc-tutorial.html#example-non-ufunc-extension)
        
    *   [Example NumPy ufunc for one dtype](https://numpy.org/doc/stable/user/c-info.ufunc-tutorial.html#example-numpy-ufunc-for-one-dtype)
        
    *   [Example NumPy ufunc with multiple dtypes](https://numpy.org/doc/stable/user/c-info.ufunc-tutorial.html#example-numpy-ufunc-with-multiple-dtypes)
        
    *   [Example NumPy ufunc with multiple arguments/return values](https://numpy.org/doc/stable/user/c-info.ufunc-tutorial.html#example-numpy-ufunc-with-multiple-arguments-return-values)
        
    *   [Example NumPy ufunc with structured array dtype arguments](https://numpy.org/doc/stable/user/c-info.ufunc-tutorial.html#example-numpy-ufunc-with-structured-array-dtype-arguments)
        
*   [Beyond the basics](https://numpy.org/doc/stable/user/c-info.beyond-basics.html)
    *   [Iterating over elements in the array](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#iterating-over-elements-in-the-array)
        *   [Basic iteration](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#basic-iteration)
            
        *   [Iterating over all but one axis](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#iterating-over-all-but-one-axis)
            
        *   [Iterating over multiple arrays](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#iterating-over-multiple-arrays)
            
        *   [Broadcasting over multiple arrays](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#broadcasting-over-multiple-arrays)
            
    *   [User-defined data-types](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#user-defined-data-types)
        *   [Adding the new data-type](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#adding-the-new-data-type)
            
        *   [Registering a casting function](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#registering-a-casting-function)
            
        *   [Registering coercion rules](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#registering-coercion-rules)
            
        *   [Registering a ufunc loop](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#registering-a-ufunc-loop)
            
    *   [Subtyping the ndarray in C](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#subtyping-the-ndarray-in-c)
        *   [Creating sub-types](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#creating-sub-types)
            
        *   [Specific features of ndarray sub-typing](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#specific-features-of-ndarray-sub-typing)
            *   [The \_\_array\_finalize\_\_ method](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#the-array-finalize-method)
                *   [`ndarray.__array_finalize__`](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#ndarray.__array_finalize__)
                    
            *   [The \_\_array\_priority\_\_ attribute](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#the-array-priority-attribute)
                *   [`ndarray.__array_priority__`](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#ndarray.__array_priority__)
                    
            *   [The \_\_array\_wrap\_\_ method](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#the-array-wrap-method)
                *   [`ndarray.__array_wrap__`](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#ndarray.__array_wrap__)