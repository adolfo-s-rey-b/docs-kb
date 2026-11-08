[Skip to main content](https://numpy.org/doc/stable/user/basics.interoperability.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/user/basics.interoperability.html)
[2.5 (stable)](https://numpy.org/doc/stable/user/basics.interoperability.html)
[2.4](https://numpy.org/doc/2.4/user/basics.interoperability.html)
[2.3](https://numpy.org/doc/2.3/user/basics.interoperability.html)
[2.2](https://numpy.org/doc/2.2/user/basics.interoperability.html)
[2.1](https://numpy.org/doc/2.1/user/basics.interoperability.html)
[2.0](https://numpy.org/doc/2.0/user/basics.interoperability.html)
[1.26](https://numpy.org/doc/1.26/user/basics.interoperability.html)
[1.25](https://numpy.org/doc/1.25/user/basics.interoperability.html)
[1.24](https://numpy.org/doc/1.24/user/basics.interoperability.html)
[1.23](https://numpy.org/doc/1.23/user/basics.interoperability.html)
[1.22](https://numpy.org/doc/1.22/user/basics.interoperability.html)
[1.21](https://numpy.org/doc/1.21/user/basics.interoperability.html)
[1.20](https://numpy.org/doc/1.20/user/basics.interoperability.html)
[1.19](https://numpy.org/doc/1.19/user/basics.interoperability.html)
[1.18](https://numpy.org/doc/1.18/user/basics.interoperability.html)
[1.17](https://numpy.org/doc/1.17/user/basics.interoperability.html)
[1.16](https://numpy.org/doc/1.16/user/basics.interoperability.html)
[1.15](https://numpy.org/doc/1.15/user/basics.interoperability.html)
[1.14](https://numpy.org/doc/1.14/user/basics.interoperability.html)
[1.13](https://numpy.org/doc/1.13/user/basics.interoperability.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Interoperability with NumPy[#](https://numpy.org/doc/stable/user/basics.interoperability.html#interoperability-with-numpy "Link to this heading")

==================================================================================================================================================

NumPy’s ndarray objects provide both a high-level API for operations on array-structured data and a concrete implementation of the API based on [strided in-RAM storage](https://numpy.org/doc/stable/reference/arrays.html#arrays)
. While this API is powerful and fairly general, its concrete implementation has limitations. As datasets grow and NumPy becomes used in a variety of new environments and architectures, there are cases where the strided in-RAM storage strategy is inappropriate, which has caused different libraries to reimplement this API for their own uses. This includes GPU arrays ([CuPy](https://cupy.dev/)
), Sparse arrays ([`scipy.sparse`](https://docs.scipy.org/doc/scipy/reference/sparse.html#module-scipy.sparse "(in SciPy v1.18.0)")
, [PyData/Sparse](https://sparse.pydata.org/)
) and parallel arrays ([Dask](https://docs.dask.org/)
 arrays) as well as various NumPy-like implementations in deep learning frameworks, like [TensorFlow](https://www.tensorflow.org/)
 and [PyTorch](https://pytorch.org/)
. Similarly, there are many projects that build on top of the NumPy API for labeled and indexed arrays ([XArray](https://xarray.dev/)
), automatic differentiation ([JAX](https://jax.readthedocs.io/)
), masked arrays ([`numpy.ma`](https://numpy.org/doc/stable/reference/maskedarray.generic.html#module-numpy.ma "numpy.ma")
), physical units ([astropy.units](https://docs.astropy.org/en/stable/units/)
, [pint](https://pint.readthedocs.io/)
, [unyt](https://unyt.readthedocs.io/)
), among others that add additional functionality on top of the NumPy API.

Yet, users still want to work with these arrays using the familiar NumPy API and reuse existing code with minimal (ideally zero) porting overhead. With this goal in mind, various protocols are defined for implementations of multi-dimensional arrays with high-level APIs matching NumPy.

Broadly speaking, there are three groups of features used for interoperability with NumPy:

1.  Methods of turning a foreign object into an ndarray;
    
2.  Methods of deferring execution from a NumPy function to another array library;
    
3.  Methods that use NumPy functions and return an instance of a foreign object.
    

We describe these features below.

1\. Using arbitrary objects in NumPy[#](https://numpy.org/doc/stable/user/basics.interoperability.html#using-arbitrary-objects-in-numpy "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

The first set of interoperability features from the NumPy API allows foreign objects to be treated as NumPy arrays whenever possible. When NumPy functions encounter a foreign object, they will try (in order):

1.  The buffer protocol, described [in the Python C-API documentation](https://docs.python.org/3/c-api/buffer.html "(in Python v3.14)")
    .
    
2.  The `__array_interface__` protocol, described [in this page](https://numpy.org/doc/stable/reference/arrays.interface.html#arrays-interface)
    . A precursor to Python’s buffer protocol, it defines a way to access the contents of a NumPy array from other C extensions.
    
3.  The `__array__()` method, which asks an arbitrary object to convert itself into an array.
    

For both the buffer and the `__array_interface__` protocols, the object describes its memory layout and NumPy does everything else (zero-copy if possible). If that’s not possible, the object itself is responsible for returning a `ndarray` from `__array__()`.

[DLPack](https://dmlc.github.io/dlpack/latest/index.html "(in DLPack)")
 is yet another protocol to convert foreign objects to NumPy arrays in a language and device agnostic manner. NumPy doesn’t implicitly convert objects to ndarrays using DLPack. It provides the function [`numpy.from_dlpack`](https://numpy.org/doc/stable/reference/generated/numpy.from_dlpack.html#numpy.from_dlpack "numpy.from_dlpack")
 that accepts any object implementing the `__dlpack__` method and outputs a NumPy ndarray (which is generally a view of the input object’s data buffer). The [Python Specification for DLPack](https://dmlc.github.io/dlpack/latest/python_spec.html#python-spec "(in DLPack)")
 page explains the `__dlpack__` protocol in detail.

### `dtype` interoperability[#](https://numpy.org/doc/stable/user/basics.interoperability.html#dtype-interoperability "Link to this heading")

Similar to `__array__()` for array objects, defining `__numpy_dtype__` allows a custom dtype object to be interoperable with NumPy. The `__numpy_dtype__` must return a NumPy dtype instance (note that `np.float64` is not a dtype instance, `np.dtype(np.float64)` is).

New in version 2.4: Before NumPy 2.4 a `.dtype` attribute was treated similarly. As of NumPy 2.4 both is accepted and implementing `__numpy_dtype__` prevents `.dtype` from being checked.

### The array interface protocol[#](https://numpy.org/doc/stable/user/basics.interoperability.html#the-array-interface-protocol "Link to this heading")

The [array interface protocol](https://numpy.org/doc/stable/reference/arrays.interface.html#arrays-interface)
 defines a way for array-like objects to reuse each other’s data buffers. Its implementation relies on the existence of the following attributes or methods:

*   `__array_interface__`: a Python dictionary containing the shape, the element type, and optionally, the data buffer address and the strides of an array-like object;
    
*   `__array__()`: a method returning the NumPy ndarray copy or a view of an array-like object;
    

The `__array_interface__` attribute can be inspected directly:

\>>> import numpy as np
\>>> x \= np.array(\[1, 2, 5.0, 8\])
\>>> x.\_\_array\_interface\_\_
{'data': (94708397920832, False), 'strides': None, 'descr': \[('', '<f8')\], 'typestr': '<f8', 'shape': (4,), 'version': 3}

Copy to clipboard

The `__array_interface__` attribute can also be used to manipulate the object data in place:

\>>> class wrapper():
...     pass
...
\>>> arr \= np.array(\[1, 2, 3, 4\])
\>>> buf \= arr.\_\_array\_interface\_\_
\>>> buf
{'data': (140497590272032, False), 'strides': None, 'descr': \[('', '<i8')\], 'typestr': '<i8', 'shape': (4,), 'version': 3}
\>>> buf\['shape'\] \= (2, 2)
\>>> w \= wrapper()
\>>> w.\_\_array\_interface\_\_ \= buf
\>>> new\_arr \= np.array(w, copy\=False)
\>>> new\_arr
array(\[\[1, 2\],\
       \[3, 4\]\])

Copy to clipboard

We can check that `arr` and `new_arr` share the same data buffer:

\>>> new\_arr\[0, 0\] \= 1000
\>>> new\_arr
array(\[\[1000,    2\],\
       \[   3,    4\]\])
\>>> arr
array(\[1000, 2, 3, 4\])

Copy to clipboard

### The `__array__()` method[#](https://numpy.org/doc/stable/user/basics.interoperability.html#the-array-method "Link to this heading")

The [\_\_array\_\_()](https://numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array__)
 method ensures that any NumPy-like object (an array, any object exposing the array interface, an object whose `__array__()` method returns an array or any nested sequence) that implements it can be used as a NumPy array. If possible, this will mean using `__array__()` to create a NumPy ndarray view of the array-like object. Otherwise, this copies the data into a new ndarray object. This is not optimal, as coercing arrays into ndarrays may cause performance problems or create the need for copies and loss of metadata, as the original object and any attributes/behavior it may have had, is lost.

The signature of the method should be `__array__(self, dtype=None, copy=None)`. If a passed `dtype` isn’t `None` and different than the object’s data type, a casting should happen to a specified type. If `copy` is `None`, a copy should be made only if `dtype` argument enforces it. For `copy=True`, a copy should always be made, where `copy=False` should raise an exception if a copy is needed.

If a class implements the old signature `__array__(self)`, for `np.array(a)` a warning will be raised saying that `dtype` and `copy` arguments are missing.

### The DLPack Protocol[#](https://numpy.org/doc/stable/user/basics.interoperability.html#the-dlpack-protocol "Link to this heading")

The [DLPack](https://dmlc.github.io/dlpack/latest/index.html "(in DLPack)")
 protocol defines a memory-layout of strided n-dimensional array objects. It offers the following syntax for data exchange:

1.  A [`numpy.from_dlpack`](https://numpy.org/doc/stable/reference/generated/numpy.from_dlpack.html#numpy.from_dlpack "numpy.from_dlpack")
     function, which accepts (array) objects with a `__dlpack__` method and uses that method to construct a new array containing the data from `x`.
    
2.  `__dlpack__(self, stream=None)` and `__dlpack_device__` methods on the array object, which will be called from within `from_dlpack`, to query what device the array is on (may be needed to pass in the correct stream, e.g. in the case of multiple GPUs) and to access the data.
    

Unlike the buffer protocol, DLPack allows exchanging arrays containing data on devices other than the CPU (e.g. Vulkan or GPU). Since NumPy only supports CPU, it can only convert objects whose data exists on the CPU. But other libraries, like [PyTorch](https://pytorch.org/)
 and [CuPy](https://cupy.dev/)
, may exchange data on GPU using this protocol.

2\. Operating on foreign objects without converting[#](https://numpy.org/doc/stable/user/basics.interoperability.html#operating-on-foreign-objects-without-converting "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A second set of methods defined by the NumPy API allows us to defer the execution from a NumPy function to another array library.

Consider the following function.

\>>> import numpy as np
\>>> def f(x):
...     return np.mean(np.exp(x))

Copy to clipboard

Note that [`np.exp`](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
 is a [ufunc](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-basics)
, which means that it operates on ndarrays in an element-by-element fashion. On the other hand, [`np.mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
 operates along one of the array’s axes.

We can apply `f` to a NumPy ndarray object directly:

\>>> x \= np.array(\[1, 2, 3, 4\])
\>>> f(x)
21.1977562209304

Copy to clipboard

We would like this function to work equally well with any NumPy-like array object.

NumPy allows a class to indicate that it would like to handle computations in a custom-defined way through the following interfaces:

*   `__array_ufunc__`: allows third-party objects to support and override [ufuncs](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-basics)
    .
    
*   `__array_function__`: a catch-all for NumPy functionality that is not covered by the `__array_ufunc__` protocol for universal functions.
    

As long as foreign objects implement the `__array_ufunc__` or `__array_function__` protocols, it is possible to operate on them without the need for explicit conversion.

### The `__array_ufunc__` protocol[#](https://numpy.org/doc/stable/user/basics.interoperability.html#the-array-ufunc-protocol "Link to this heading")

A [universal function (or ufunc for short)](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-basics)
 is a “vectorized” wrapper for a function that takes a fixed number of specific inputs and produces a fixed number of specific outputs. The output of the ufunc (and its methods) is not necessarily an ndarray, if not all input arguments are ndarrays. Indeed, if any input defines an `__array_ufunc__` method, control will be passed completely to that function, i.e., the ufunc is overridden. The `__array_ufunc__` method defined on that (non-ndarray) object has access to the NumPy ufunc. Because ufuncs have a well-defined structure, the foreign `__array_ufunc__` method may rely on ufunc attributes like `.at()`, `.reduce()`, and others.

A subclass can override what happens when executing NumPy ufuncs on it by overriding the default `ndarray.__array_ufunc__` method. This method is executed instead of the ufunc and should return either the result of the operation, or `NotImplemented` if the operation requested is not implemented.

### The `__array_function__` protocol[#](https://numpy.org/doc/stable/user/basics.interoperability.html#the-array-function-protocol "Link to this heading")

To achieve enough coverage of the NumPy API to support downstream projects, there is a need to go beyond `__array_ufunc__` and implement a protocol that allows arguments of a NumPy function to take control and divert execution to another function (for example, a GPU or parallel implementation) in a way that is safe and consistent across projects.

The semantics of `__array_function__` are very similar to `__array_ufunc__`, except the operation is specified by an arbitrary callable object rather than a ufunc instance and method. For more details, see [NEP 18 — A dispatch mechanism for NumPy’s high level array functions](https://numpy.org/neps/nep-0018-array-function-protocol.html#nep18 "(in NumPy Enhancement Proposals)")
.

3\. Returning foreign objects[#](https://numpy.org/doc/stable/user/basics.interoperability.html#returning-foreign-objects "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

A third type of feature set is meant to use the NumPy function implementation and then convert the return value back into an instance of the foreign object. The `__array_finalize__` and `__array_wrap__` methods act behind the scenes to ensure that the return type of a NumPy function can be specified as needed.

The `__array_finalize__` method is the mechanism that NumPy provides to allow subclasses to handle the various ways that new instances get created. This method is called whenever the system internally allocates a new array from an object which is a subclass (subtype) of the ndarray. It can be used to change attributes after construction, or to update meta-information from the “parent.”

The `__array_wrap__` method “wraps up the action” in the sense of allowing any object (such as user-defined functions) to set the type of its return value and update attributes and metadata. This can be seen as the opposite of the `__array__` method. At the end of every object that implements `__array_wrap__`, this method is called on the input object with the highest _array priority_, or the output object if one was specified. The `__array_priority__` attribute is used to determine what type of object to return in situations where there is more than one possibility for the Python type of the returned object. For example, subclasses may opt to use this method to transform the output array into an instance of the subclass and update metadata before returning the array to the user.

For more information on these methods, see [Subclassing ndarray](https://numpy.org/doc/stable/user/basics.subclassing.html#basics-subclassing)
 and [Specific features of ndarray sub-typing](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#specific-array-subtyping)
.

Interoperability examples[#](https://numpy.org/doc/stable/user/basics.interoperability.html#interoperability-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

### Example: Pandas `Series` objects[#](https://numpy.org/doc/stable/user/basics.interoperability.html#example-pandas-series-objects "Link to this heading")

Consider the following:

\>>> import pandas as pd
\>>> ser \= pd.Series(\[1, 2, 3, 4\])
\>>> type(ser)
pandas.core.series.Series

Copy to clipboard

Now, `ser` is **not** an ndarray, but because it [implements the \_\_array\_ufunc\_\_ protocol](https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe-interoperability-with-numpy-functions)
, we can apply ufuncs to it as if it were an ndarray:

\>>> np.exp(ser)
   0     2.718282
   1     7.389056
   2    20.085537
   3    54.598150
   dtype: float64
\>>> np.sin(ser)
   0    0.841471
   1    0.909297
   2    0.141120
   3   -0.756802
   dtype: float64

Copy to clipboard

We can even do operations with other ndarrays:

\>>> np.add(ser, np.array(\[5, 6, 7, 8\]))
   0     6
   1     8
   2    10
   3    12
   dtype: int64
\>>> f(ser)
21.1977562209304
\>>> result \= ser.\_\_array\_\_()
\>>> type(result)
numpy.ndarray

Copy to clipboard

### Example: PyTorch tensors[#](https://numpy.org/doc/stable/user/basics.interoperability.html#example-pytorch-tensors "Link to this heading")

[PyTorch](https://pytorch.org/)
 is an optimized tensor library for deep learning using GPUs and CPUs. PyTorch arrays are commonly called _tensors_. Tensors are similar to NumPy’s ndarrays, except that tensors can run on GPUs or other hardware accelerators. In fact, tensors and NumPy arrays can often share the same underlying memory, eliminating the need to copy data.

\>>> import torch
\>>> data \= \[\[1, 2\],\[3, 4\]\]
\>>> x\_np \= np.array(data)
\>>> x\_tensor \= torch.tensor(data)

Copy to clipboard

Note that `x_np` and `x_tensor` are different kinds of objects:

\>>> x\_np
array(\[\[1, 2\],\
       \[3, 4\]\])
\>>> x\_tensor
tensor(\[\[1, 2\],\
        \[3, 4\]\])

Copy to clipboard

However, we can treat PyTorch tensors as NumPy arrays without the need for explicit conversion:

\>>> np.exp(x\_tensor)
tensor(\[\[ 2.7183,  7.3891\],\
        \[20.0855, 54.5982\]\], dtype=torch.float64)

Copy to clipboard

Also, note that the return type of this function is compatible with the initial data type.

Warning

While this mixing of ndarrays and tensors may be convenient, it is not recommended. It will not work for non-CPU tensors, and will have unexpected behavior in corner cases. Users should prefer explicitly converting the ndarray to a tensor.

Note

PyTorch does not implement `__array_function__` or `__array_ufunc__`. Under the hood, the `Tensor.__array__()` method returns a NumPy ndarray as a view of the tensor data buffer. See [this issue](https://github.com/pytorch/pytorch/issues/24015)
 and the [\_\_torch\_function\_\_ implementation](https://github.com/pytorch/pytorch/blob/master/torch/overrides.py)
 for details.

Note also that we can see `__array_wrap__` in action here, even though `torch.Tensor` is not a subclass of ndarray:

\>>> import torch
\>>> t \= torch.arange(4)
\>>> np.abs(t)
tensor(\[0, 1, 2, 3\])

Copy to clipboard

PyTorch implements `__array_wrap__` to be able to get tensors back from NumPy functions, and we can modify it directly to control which type of objects are returned from these functions.

### Example: CuPy arrays[#](https://numpy.org/doc/stable/user/basics.interoperability.html#example-cupy-arrays "Link to this heading")

CuPy is a NumPy/SciPy-compatible array library for GPU-accelerated computing with Python. CuPy implements a subset of the NumPy interface by implementing `cupy.ndarray`, [a counterpart to NumPy ndarrays](https://docs.cupy.dev/en/stable/reference/ndarray.html)
.

\>>> import cupy as cp
\>>> x\_gpu \= cp.array(\[1, 2, 3, 4\])

Copy to clipboard

The `cupy.ndarray` object implements the `__array_ufunc__` interface. This enables NumPy ufuncs to be applied to CuPy arrays (this will defer operation to the matching CuPy CUDA/ROCm implementation of the ufunc):

\>>> np.mean(np.exp(x\_gpu))
array(21.19775622)

Copy to clipboard

Note that the return type of these operations is still consistent with the initial type:

\>>> arr \= cp.random.randn(1, 2, 3, 4).astype(cp.float32)
\>>> result \= np.sum(arr)
\>>> print(type(result))
<class 'cupy.\_core.core.ndarray'>

Copy to clipboard

See [this page in the CuPy documentation for details](https://docs.cupy.dev/en/stable/reference/ufunc.html)
.

`cupy.ndarray` also implements the `__array_function__` interface, meaning it is possible to do operations such as

\>>> a \= np.random.randn(100, 100)
\>>> a\_gpu \= cp.asarray(a)
\>>> qr\_gpu \= np.linalg.qr(a\_gpu)

Copy to clipboard

CuPy implements many NumPy functions on `cupy.ndarray` objects, but not all. See [the CuPy documentation](https://docs.cupy.dev/en/stable/user_guide/difference.html)
 for details.

### Example: Dask arrays[#](https://numpy.org/doc/stable/user/basics.interoperability.html#example-dask-arrays "Link to this heading")

Dask is a flexible library for parallel computing in Python. Dask Array implements a subset of the NumPy ndarray interface using blocked algorithms, cutting up the large array into many small arrays. This allows computations on larger-than-memory arrays using multiple cores.

Dask supports `__array__()` and `__array_ufunc__`.

\>>> import dask.array as da
\>>> x \= da.random.normal(1, 0.1, size\=(20, 20), chunks\=(10, 10))
\>>> np.mean(np.exp(x))
dask.array<mean\_agg-aggregate, shape=(), dtype=float64, chunksize=(), chunktype=numpy.ndarray>
\>>> np.mean(np.exp(x)).compute()
5.090097550553843

Copy to clipboard

Note

Dask is lazily evaluated, and the result from a computation isn’t computed until you ask for it by invoking `compute()`.

See [the Dask array documentation](https://docs.dask.org/en/stable/array.html)
 and the [scope of Dask arrays interoperability with NumPy arrays](https://docs.dask.org/en/stable/array.html#scope)
 for details.

### Example: DLPack[#](https://numpy.org/doc/stable/user/basics.interoperability.html#example-dlpack "Link to this heading")

Several Python data science libraries implement the `__dlpack__` protocol. Among them are [PyTorch](https://pytorch.org/)
 and [CuPy](https://cupy.dev/)
. A full list of libraries that implement this protocol can be found on [this page of DLPack documentation](https://dmlc.github.io/dlpack/latest/index.html "(in DLPack)")
.

Convert a PyTorch CPU tensor to NumPy array:

\>>> import torch
\>>> x\_torch \= torch.arange(5)
\>>> x\_torch
tensor(\[0, 1, 2, 3, 4\])
\>>> x\_np \= np.from\_dlpack(x\_torch)
\>>> x\_np
array(\[0, 1, 2, 3, 4\])
\>>> \# note that x\_np is a view of x\_torch
\>>> x\_torch\[1\] \= 100
\>>> x\_torch
tensor(\[  0, 100,   2,   3,   4\])
\>>> x\_np
array(\[  0, 100,   2,   3,   4\])

Copy to clipboard

The imported arrays are read-only so writing or operating in-place will fail:

\>>> x\_np.flags.writeable
False
\>>> x\_np\[1\] \= 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: assignment destination is read-only

Copy to clipboard

A copy must be created in order to operate on the imported arrays in-place, but will mean duplicating the memory. Do not do this for very large arrays:

\>>> x\_np\_copy \= x\_np.copy()
\>>> x\_np\_copy.sort()  \# works

Copy to clipboard

Note

GPU tensors cannot be directly zero-copy converted to NumPy arrays since NumPy does not support GPU devices. However, since DLPack v1, cross-device copy is supported via the `device` parameter:

\>>> x\_torch \= torch.arange(5, device\='cuda')
\>>> np.from\_dlpack(x\_torch)  \# fails: implicit device=None means same device
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: Unsupported device in DLTensor.
\>>> np.from\_dlpack(x\_torch, device\='cpu')  \# works: explicit copy to CPU
array(\[0, 1, 2, 3, 4\])

Copy to clipboard

If both libraries support the device the data buffer is on, it is possible to use the `__dlpack__` protocol (e.g. [PyTorch](https://pytorch.org/)
 and [CuPy](https://cupy.dev/)
):

\>>> x\_torch \= torch.arange(5, device\='cuda')
\>>> x\_cupy \= cupy.from\_dlpack(x\_torch)

Copy to clipboard

Similarly, a NumPy array can be converted to a PyTorch tensor:

\>>> x\_np \= np.arange(5)
\>>> x\_torch \= torch.from\_dlpack(x\_np)

Copy to clipboard

Read-only arrays cannot be exported:

\>>> x\_np \= np.arange(5)
\>>> x\_np.flags.writeable \= False
\>>> torch.from\_dlpack(x\_np)  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File ".../site-packages/torch/utils/dlpack.py", line 63, in from\_dlpack
    dlpack \= ext\_tensor.\_\_dlpack\_\_()
TypeError: NumPy currently only supports dlpack for writeable arrays

Copy to clipboard

Further reading[#](https://numpy.org/doc/stable/user/basics.interoperability.html#further-reading "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

*   [The array interface protocol](https://numpy.org/doc/stable/reference/arrays.interface.html#arrays-interface)
    
*   [Writing custom array containers](https://numpy.org/doc/stable/user/basics.dispatch.html#basics-dispatch)
    
*   [Special attributes and methods](https://numpy.org/doc/stable/reference/arrays.classes.html#special-attributes-and-methods)
     (details on the `__array_ufunc__` and `__array_function__` protocols)
    
*   [Subclassing ndarray](https://numpy.org/doc/stable/user/basics.subclassing.html#basics-subclassing)
     (details on the `__array_wrap__` and `__array_finalize__` methods)
    
*   [Specific features of ndarray sub-typing](https://numpy.org/doc/stable/user/c-info.beyond-basics.html#specific-array-subtyping)
     (more details on the implementation of `__array_finalize__`, `__array_wrap__` and `__array_priority__`)
    
*   [NumPy roadmap: interoperability](https://numpy.org/neps/roadmap.html "(in NumPy Enhancement Proposals)")
    
*   [PyTorch documentation on the Bridge with NumPy](https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#bridge-to-np-label)
    

On this page