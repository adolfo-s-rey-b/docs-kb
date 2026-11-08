Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/storage.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/storage.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/storage.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/storage.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/storage.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/storage.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/storage.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/storage.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/storage.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/storage.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/storage.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/storage.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/storage.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/storage.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/storage.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/storage.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/storage.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/storage.html)
[v1.13](https://docs.pytorch.org/docs/1.13/storage.html)
[v1.12](https://docs.pytorch.org/docs/1.12/storage.html)
[v1.11](https://docs.pytorch.org/docs/1.11/storage.html)
[v1.10](https://docs.pytorch.org/docs/1.10/storage.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/storage.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/storage.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/storage.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/storage.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/storage.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/storage.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/storage.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/storage.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/storage.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/storage.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/storage.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/storage.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/storage.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/storage.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/storage.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/storage.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/storage.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/storage.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/storage.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/storage.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/storage.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/storage.html)

[Go to pytorch.org](https://pytorch.org/)

 Ctrl+K

|     |     |
| --- | --- |
|     | [×](javascript:void(0) "Clear search box") |

search

Custom Search

|     |     |
| --- | --- |
|     | Sort by<br><br>Relevance<br><br>Date |

*   [X](https://x.com/PyTorch)
    
*   [GitHub](https://github.com/pytorch/pytorch)
    
*   [PyTorch Forum](https://discuss.pytorch.org/)
    
*   [PyPi](https://pypi.org/project/torch/)
    

Rate this Page

★ ★ ★ ★ ★

torch.Storage[#](https://docs.pytorch.org/docs/2.15/storage.html#torch-storage "Link to this heading")

=======================================================================================================

Created On: Dec 30, 2016 | Last Updated On: May 06, 2026

In PyTorch, a regular tensor is a multi-dimensional array that is defined by the following components:

*   Storage: The actual data of the tensor, stored as a contiguous, one-dimensional array of bytes.
    
*   `dtype`: The data type of the elements in the tensor, such as torch.float32 or torch.int64.
    
*   `shape`: A tuple indicating the size of the tensor in each dimension.
    
*   Stride: The step size needed to move from one element to the next in each dimension.
    
*   Offset: The starting point in the storage from which the tensor data begins. This will usually be 0 for newly created tensors.
    

These components together define the structure and data of a tensor, with the storage holding the actual data and the rest serving as metadata.

Untyped Storage API[#](https://docs.pytorch.org/docs/2.15/storage.html#untyped-storage-api "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

A [`torch.UntypedStorage`](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage "torch.UntypedStorage")
 is a contiguous, one-dimensional array of elements. Its length is equal to the number of bytes of the tensor. The storage serves as the underlying data container for tensors. In general, a tensor created in PyTorch using regular constructors such as [`zeros()`](https://docs.pytorch.org/docs/2.15/generated/torch.zeros.html#torch.zeros "torch.zeros")
, [`zeros_like()`](https://docs.pytorch.org/docs/2.15/generated/torch.zeros_like.html#torch.zeros_like "torch.zeros_like")
 or [`new_zeros()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.new_zeros.html#torch.Tensor.new_zeros "torch.Tensor.new_zeros")
 will produce tensors where there is a one-to-one correspondence between the tensor storage and the tensor itself.

However, a storage is allowed to be shared by multiple tensors. For instance, any view of a tensor (obtained through [`view()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.view.html#torch.Tensor.view "torch.Tensor.view")
 or some, but not all, kinds of indexing like integers and slices) will point to the same underlying storage as the original tensor. When serializing and deserializing tensors that share a common storage, the relationship is preserved, and the tensors continue to point to the same storage. Interestingly, deserializing multiple tensors that point to a single storage can be faster than deserializing multiple independent tensors.

A tensor storage can be accessed through the [`untyped_storage()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.untyped_storage.html#torch.Tensor.untyped_storage "torch.Tensor.untyped_storage")
 method. This will return an object of type [`torch.UntypedStorage`](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage "torch.UntypedStorage")
. Fortunately, storages have a unique identifier accessed through the [`torch.UntypedStorage.data_ptr()`](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.data_ptr "torch.UntypedStorage.data_ptr")
 method. In regular settings, two tensors with the same data storage will have the same storage `data_ptr`. However, tensors themselves can point to two separate storages, one for its data attribute and another for its grad attribute. Each will require a `data_ptr()` of its own. In general, there is no guarantee that a [`torch.Tensor.data_ptr()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.data_ptr.html#torch.Tensor.data_ptr "torch.Tensor.data_ptr")
 and [`torch.UntypedStorage.data_ptr()`](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.data_ptr "torch.UntypedStorage.data_ptr")
 match and this should not be assumed to be true.

Untyped storages are somewhat independent of the tensors that are built on them. Practically, this means that tensors with different dtypes or shape can point to the same storage. It also implies that a tensor storage can be changed, as the following example shows:

\>>> t \= torch.ones(3)
\>>> s0 \= t.untyped\_storage()
\>>> s0
 0
 0
 128
 63
 0
 0
 128
 63
 0
 0
 128
 63
\[torch.storage.UntypedStorage(device=cpu) of size 12\]
\>>> s1 \= s0.clone()
\>>> s1.fill\_(0)
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
 0
\[torch.storage.UntypedStorage(device=cpu) of size 12\]
\>>> \# Fill the tensor with a zeroed storage
\>>> t.set\_(s1, storage\_offset\=t.storage\_offset(), stride\=t.stride(), size\=t.size())
tensor(\[0., 0., 0.\])

Copy to clipboard

Warning

Please note that directly modifying a tensor’s storage as shown in this example is not a recommended practice. This low-level manipulation is illustrated solely for educational purposes, to demonstrate the relationship between tensors and their underlying storages. In general, it’s more efficient and safer to use standard `torch.Tensor` methods, such as [`clone()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.clone.html#torch.Tensor.clone "torch.Tensor.clone")
 and [`fill_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.fill_.html#torch.Tensor.fill_ "torch.Tensor.fill_")
, to achieve the same results.

Other than `data_ptr`, untyped storage also have other attributes such as [`filename`](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.filename "torch.UntypedStorage.filename")
 (in case the storage points to a file on disk), [`device`](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.device "torch.UntypedStorage.device")
 or [`is_cuda`](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.is_cuda "torch.UntypedStorage.is_cuda")
 for device checks. A storage can also be manipulated in-place or out-of-place with methods like [`copy_`](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.copy_ "torch.UntypedStorage.copy_")
, [`fill_`](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.fill_ "torch.UntypedStorage.fill_")
 or [`pin_memory`](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.pin_memory "torch.UntypedStorage.pin_memory")
. For more information, check the API reference below. Keep in mind that modifying storages is a low-level API and comes with risks! Most of these APIs also exist on the tensor level: if present, they should be prioritized over their storage counterparts.

Special cases[#](https://docs.pytorch.org/docs/2.15/storage.html#special-cases "Link to this heading")

-------------------------------------------------------------------------------------------------------

We mentioned that a tensor that has a non-None `grad` attribute has actually two pieces of data within it. In this case, [`untyped_storage()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.untyped_storage.html#torch.Tensor.untyped_storage "torch.Tensor.untyped_storage")
 will return the storage of the `data` attribute, whereas the storage of the gradient can be obtained through `tensor.grad.untyped_storage()`.

\>>> t \= torch.zeros(3, requires\_grad\=True)
\>>> t.sum().backward()
\>>> assert list(t.untyped\_storage()) \== \[0\] \* 12  \# the storage of the tensor is just 0s
\>>> assert list(t.grad.untyped\_storage()) != \[0\] \* 12  \# the storage of the gradient isn't

Copy to clipboard

There are also special cases where tensors do not have a typical storage, or no storage at all:

*   Tensors on `"meta"` device: Tensors on the `"meta"` device are used for shape inference and do not hold actual data.
    
*   Fake Tensors: Another internal tool used by PyTorch’s compiler is [FakeTensor](https://pytorch.org/docs/stable/torch.compiler_fake_tensor.html)
     which is based on a similar idea.
    

Tensor subclasses or tensor-like objects can also display unusual behaviours. In general, we do not expect many use cases to require operating at the Storage level!

_class_ torch.UntypedStorage(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L476)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage "Link to this definition")

bfloat16()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L336)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.bfloat16 "Link to this definition")

Casts this storage to bfloat16 type.

bool()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L332)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.bool "Link to this definition")

Casts this storage to bool type.

byte()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L328)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.byte "Link to this definition")

Casts this storage to byte type.

byteswap(_dtype_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L428)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.byteswap "Link to this definition")

Swap bytes in underlying data.

char()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L324)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.char "Link to this definition")

Casts this storage to char type.

clone()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L262)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.clone "Link to this definition")

Return a copy of this storage.

complex\_double()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L340)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.complex_double "Link to this definition")

Casts this storage to complex double type.

complex\_float()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L344)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.complex_float "Link to this definition")

Casts this storage to complex float type.

copy\_()[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.copy_ "Link to this definition")

cpu()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L270)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.cpu "Link to this definition")

Return a CPU copy of this storage if it’s not already on the CPU.

cuda(_device\=None_, _non\_blocking\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L91)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.cuda "Link to this definition")

Returns a copy of this object in CUDA memory.

If this object is already in CUDA memory and on the correct device, then no copy is performed and the original object is returned.

Parameters:

*   **device** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The destination GPU id. Defaults to the current device.
    
*   **non\_blocking** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True` and the source is in pinned memory, the copy will be asynchronous with respect to the host. Otherwise, the argument has no effect.
    

Return type:

_\_StorageBase_ | [_TypedStorage_](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage "torch.storage.TypedStorage")

data\_ptr()[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.data_ptr "Link to this definition")

device_: [device](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.device "Link to this definition")

double()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L300)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.double "Link to this definition")

Casts this storage to double type.

element\_size()[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.element_size "Link to this definition")

_property_ filename_: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.filename "Link to this definition")

Returns the file name associated with this storage.

The file name will be a string if the storage is on CPU and was created via [`from_file()`](https://docs.pytorch.org/docs/2.15/generated/torch.from_file.html#torch.from_file "torch.from_file")
 with `shared` as `True`. This attribute is `None` otherwise.

fill\_()[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.fill_ "Link to this definition")

float()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L304)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.float "Link to this definition")

Casts this storage to float type.

float8\_e4m3fn()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L352)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.float8_e4m3fn "Link to this definition")

Casts this storage to float8\_e4m3fn type

float8\_e4m3fnuz()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L360)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.float8_e4m3fnuz "Link to this definition")

Casts this storage to float8\_e4m3fnuz type

float8\_e5m2()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L348)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.float8_e5m2 "Link to this definition")

Casts this storage to float8\_e5m2 type

float8\_e5m2fnuz()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L356)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.float8_e5m2fnuz "Link to this definition")

Casts this storage to float8\_e5m2fnuz type

_static_ from\_buffer()[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.from_buffer "Link to this definition")

_static_ from\_file(_filename_, _shared\=False_, _nbytes\=0_) → Storage[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.from_file "Link to this definition")

Creates a CPU storage backed by a memory-mapped file.

If `shared` is `True`, then memory is shared between all processes. All changes are written to the file. If `shared` is `False`, then the changes on the storage do not affect the file.

`nbytes` is the number of bytes of storage. If `shared` is `False`, then the file must contain at least `nbytes` bytes. If `shared` is `True` the file will be created if needed. (Note that for `UntypedStorage` this argument differs from that of `TypedStorage.from_file`)

Parameters:

*   **filename** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – file name to map
    
*   **shared** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – whether to share memory (whether `MAP_SHARED` or `MAP_PRIVATE` is passed to the underlying [mmap(2) call](https://man7.org/linux/man-pages/man2/mmap.2.html)
    )
    
*   **nbytes** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – number of bytes of storage
    

get\_device()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L124)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.get_device "Link to this definition")

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

half()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L308)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.half "Link to this definition")

Casts this storage to half type.

hpu(_device\=None_, _non\_blocking\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L106)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.hpu "Link to this definition")

Returns a copy of this object in HPU memory.

If this object is already in HPU memory and on the correct device, then no copy is performed and the original object is returned.

Parameters:

*   **device** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The destination HPU id. Defaults to the current device.
    
*   **non\_blocking** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True` and the source is in pinned memory, the copy will be asynchronous with respect to the host. Otherwise, the argument has no effect.
    

Return type:

_\_StorageBase_ | [_TypedStorage_](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage "torch.storage.TypedStorage")

int()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L316)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.int "Link to this definition")

Casts this storage to int type.

_property_ is\_cuda[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.is_cuda "Link to this definition")

_property_ is\_hpu[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.is_hpu "Link to this definition")

is\_pinned(_device\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L364)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.is_pinned "Link to this definition")

Determine whether the CPU storage is already pinned on device.

Parameters:

**device** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 _or_ [_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
) – The device to pin memory on (default: `None`). This argument is discouraged and subject to deprecated.

Returns:

A boolean variable.

is\_shared()[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.is_shared "Link to this definition")

is\_sparse_: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
_ _\= False_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.is_sparse "Link to this definition")

is\_sparse\_csr_: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
_ _\= False_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.is_sparse_csr "Link to this definition")

long()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L312)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.long "Link to this definition")

Casts this storage to long type.

mps()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L276)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.mps "Link to this definition")

Return a MPS copy of this storage if it’s not already on the MPS.

nbytes()[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.nbytes "Link to this definition")

new()[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.new "Link to this definition")

pin\_memory(_device\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L380)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.pin_memory "Link to this definition")

Copy the CPU storage to pinned memory, if it’s not already pinned.

Parameters:

**device** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 _or_ [_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
) – The device to pin memory on (default: `None`). This argument is discouraged and subject to deprecated.

Returns:

A pinned CPU storage.

resizable()[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.resizable "Link to this definition")

resize\_()[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.resize_ "Link to this definition")

share\_memory\_(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L499)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.share_memory_ "Link to this definition")

Moves the storage to shared memory.

This is a no-op for storages already in shared memory and for CUDA storages, which do not need to be moved for sharing across processes. Storages in shared memory cannot be resized.

Note that to mitigate issues like [this](https://github.com/pytorch/pytorch/issues/95606)
 it is thread safe to call this function from multiple threads on the same object. It is NOT thread safe though to call any other function on self without proper synchronization. Please see [Multiprocessing best practices](https://docs.pytorch.org/docs/2.15/notes/multiprocessing.html)
 for more details.

Note

When all references to a storage in shared memory are deleted, the associated shared memory object will also be deleted. PyTorch has a special cleanup process to ensure that this happens even if the current process exits unexpectedly.

It is worth noting the difference between [`share_memory_()`](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.share_memory_ "torch.UntypedStorage.share_memory_")
 and [`from_file()`](https://docs.pytorch.org/docs/2.15/generated/torch.from_file.html#torch.from_file "torch.from_file")
 with `shared = True`

1.  `share_memory_` uses [shm\_open(3)](https://man7.org/linux/man-pages/man3/shm_open.3.html)
     to create a POSIX shared memory object while [`from_file()`](https://docs.pytorch.org/docs/2.15/generated/torch.from_file.html#torch.from_file "torch.from_file")
     uses [open(2)](https://man7.org/linux/man-pages/man2/open.2.html)
     to open the filename passed by the user.
    
2.  Both use an [mmap(2) call](https://man7.org/linux/man-pages/man2/mmap.2.html)
     with `MAP_SHARED` to map the file/object into the current virtual address space
    
3.  `share_memory_` will call `shm_unlink(3)` on the object after mapping it to make sure the shared memory object is freed when no process has the object open. `torch.from_file(shared=True)` does not unlink the file. This file is persistent and will remain until it is deleted by the user.
    

Returns:

`self`

short()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L320)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.short "Link to this definition")

Casts this storage to short type.

size()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L83)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.size "Link to this definition")

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

to(_\*_, _device_, _non\_blocking\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L295)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.to "Link to this definition")

tolist()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L266)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.tolist "Link to this definition")

Return a list containing the elements of this storage.

type(_dtype\=None_, _non\_blocking\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L86)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.type "Link to this definition")

Return type:

_\_StorageBase_ | [_TypedStorage_](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage "torch.storage.TypedStorage")

untyped()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L425)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.untyped "Link to this definition")

Legacy Typed Storage[#](https://docs.pytorch.org/docs/2.15/storage.html#legacy-typed-storage "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

Warning

For historical context, PyTorch previously used typed storage classes, which are now deprecated and should be avoided. The following details this API in case you should encounter it, although its usage is highly discouraged. All storage classes except for [`torch.UntypedStorage`](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage "torch.UntypedStorage")
 will be removed in the future, and [`torch.UntypedStorage`](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage "torch.UntypedStorage")
 will be used in all cases.

`torch.Storage` is an alias for the storage class that corresponds with the default data type ([`torch.get_default_dtype()`](https://docs.pytorch.org/docs/2.15/generated/torch.get_default_dtype.html#torch.get_default_dtype "torch.get_default_dtype")
). For example, if the default data type is `torch.float`, `torch.Storage` resolves to [`torch.FloatStorage`](https://docs.pytorch.org/docs/2.15/storage.html#torch.FloatStorage "torch.FloatStorage")
.

The `torch.<type>Storage` and `torch.cuda.<type>Storage` classes, like [`torch.FloatStorage`](https://docs.pytorch.org/docs/2.15/storage.html#torch.FloatStorage "torch.FloatStorage")
, [`torch.IntStorage`](https://docs.pytorch.org/docs/2.15/storage.html#torch.IntStorage "torch.IntStorage")
, etc., are not actually ever instantiated. Calling their constructors creates a [`torch.TypedStorage`](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage "torch.TypedStorage")
 with the appropriate [`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
 and [`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
. `torch.<type>Storage` classes have all of the same class methods that [`torch.TypedStorage`](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage "torch.TypedStorage")
 has.

A [`torch.TypedStorage`](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage "torch.TypedStorage")
 is a contiguous, one-dimensional array of elements of a particular [`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
. It can be given any [`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
, and the internal data will be interpreted appropriately. [`torch.TypedStorage`](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage "torch.TypedStorage")
 contains a [`torch.UntypedStorage`](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage "torch.UntypedStorage")
 which holds the data as an untyped array of bytes.

Every strided [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 contains a [`torch.TypedStorage`](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage "torch.TypedStorage")
, which stores all of the data that the [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 views.

_class_ torch.TypedStorage(_\*args_, _wrap\_storage\=None_, _dtype\=None_, _device\=None_, _\_internal\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L685)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage "Link to this definition")

bfloat16()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1384)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.bfloat16 "Link to this definition")

Casts this storage to bfloat16 type.

bool()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1379)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.bool "Link to this definition")

Casts this storage to bool type.

byte()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1374)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.byte "Link to this definition")

Casts this storage to byte type.

char()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1369)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.char "Link to this definition")

Casts this storage to char type.

clone()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1162)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.clone "Link to this definition")

Return a copy of this storage.

complex\_double()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1389)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.complex_double "Link to this definition")

Casts this storage to complex double type.

complex\_float()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1394)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.complex_float "Link to this definition")

Casts this storage to complex float type.

copy\_(_source_, _non\_blocking\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1038)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.copy_ "Link to this definition")

cpu()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1172)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.cpu "Link to this definition")

Return a CPU copy of this storage if it’s not already on the CPU.

cuda(_device\=None_, _non\_blocking\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1071)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.cuda "Link to this definition")

Returns a copy of this object in CUDA memory.

If this object is already in CUDA memory and on the correct device, then no copy is performed and the original object is returned.

Parameters:

*   **device** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The destination GPU id. Defaults to the current device.
    
*   **non\_blocking** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True` and the source is in pinned memory, the copy will be asynchronous with respect to the host. Otherwise, the argument has no effect.
    

Return type:

[_Self_](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.15)")

data\_ptr()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1262)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.data_ptr "Link to this definition")

_property_ device[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.device "Link to this definition")

double()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1339)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.double "Link to this definition")

Casts this storage to double type.

dtype_: [dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.dtype "Link to this definition")

element\_size()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1114)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.element_size "Link to this definition")

_property_ filename_: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.filename "Link to this definition")

Returns the file name associated with this storage if the storage was memory mapped from a file. or `None` if the storage was not created by memory mapping a file.

fill\_(_value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L702)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.fill_ "Link to this definition")

float()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1344)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.float "Link to this definition")

Casts this storage to float type.

float8\_e4m3fn()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1404)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.float8_e4m3fn "Link to this definition")

Casts this storage to float8\_e4m3fn type

float8\_e4m3fnuz()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1414)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.float8_e4m3fnuz "Link to this definition")

Casts this storage to float8\_e4m3fnuz type

float8\_e5m2()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1399)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.float8_e5m2 "Link to this definition")

Casts this storage to float8\_e5m2 type

float8\_e5m2fnuz()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1409)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.float8_e5m2fnuz "Link to this definition")

Casts this storage to float8\_e5m2fnuz type

_classmethod_ from\_buffer(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1289)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.from_buffer "Link to this definition")

_classmethod_ from\_file(_filename_, _shared\=False_, _size\=0_) → Storage[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1419)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.from_file "Link to this definition")

Creates a CPU storage backed by a memory-mapped file.

If `shared` is `True`, then memory is shared between all processes. All changes are written to the file. If `shared` is `False`, then the changes on the storage do not affect the file.

`size` is the number of elements in the storage. If `shared` is `False`, then the file must contain at least `size * sizeof(Type)` bytes (`Type` is the type of storage). If `shared` is `True` the file will be created if needed.

Parameters:

*   **filename** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – file name to map
    
*   **shared** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – whether to share memory (whether `MAP_SHARED` or `MAP_PRIVATE` is passed to the underlying [mmap(2) call](https://man7.org/linux/man-pages/man2/mmap.2.html)
    )
    
*   **size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – number of elements in the storage
    

get\_device()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1122)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.get_device "Link to this definition")

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

half()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1349)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.half "Link to this definition")

Casts this storage to half type.

hpu(_device\=None_, _non\_blocking\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1084)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.hpu "Link to this definition")

Returns a copy of this object in HPU memory.

If this object is already in HPU memory and on the correct device, then no copy is performed and the original object is returned.

Parameters:

*   **device** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The destination HPU id. Defaults to the current device.
    
*   **non\_blocking** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True` and the source is in pinned memory, the copy will be asynchronous with respect to the host. Otherwise, the argument has no effect.
    

Return type:

[_Self_](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.15)")

int()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1359)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.int "Link to this definition")

Casts this storage to int type.

_property_ is\_cuda[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.is_cuda "Link to this definition")

_property_ is\_hpu[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.is_hpu "Link to this definition")

is\_pinned(_device\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1177)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.is_pinned "Link to this definition")

Determine whether the CPU TypedStorage is already pinned on device.

Parameters:

**device** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 _or_ [_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
) – The device to pin memory on (default: `None`). This argument is discouraged and subject to deprecated.

Returns:

A boolean variable.

is\_shared()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1464)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.is_shared "Link to this definition")

is\_sparse_: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
_ _\= False_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.is_sparse "Link to this definition")

long()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1354)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.long "Link to this definition")

Casts this storage to long type.

nbytes()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1046)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.nbytes "Link to this definition")

pickle\_storage\_type()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1246)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.pickle_storage_type "Link to this definition")

pin\_memory(_device\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1190)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.pin_memory "Link to this definition")

Copy the CPU TypedStorage to pinned memory, if it’s not already pinned.

Parameters:

**device** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 _or_ [_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
) – The device to pin memory on (default: `None`). This argument is discouraged and subject to deprecated.

Returns:

A pinned CPU storage.

resizable()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1270)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.resizable "Link to this definition")

resize\_(_size_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1274)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.resize_ "Link to this definition")

share\_memory\_()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1205)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.share_memory_ "Link to this definition")

See [`torch.UntypedStorage.share_memory_()`](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage.share_memory_ "torch.UntypedStorage.share_memory_")

short()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1364)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.short "Link to this definition")

Casts this storage to short type.

size()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1236)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.size "Link to this definition")

to(_\*_, _device_, _non\_blocking\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1097)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.to "Link to this definition")

Returns a copy of this object in device memory.

If this object is already on the correct device, then no copy is performed and the original object is returned.

Parameters:

*   **device** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The destination device.
    
*   **non\_blocking** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True` and the source is in pinned memory, the copy will be asynchronous with respect to the host. Otherwise, the argument has no effect.
    

Return type:

Self

tolist()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1167)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.tolist "Link to this definition")

Return a list containing the elements of this storage.

type(_dtype\=None_, _non\_blocking\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L1054)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.type "Link to this definition")

Returns the type if dtype is not provided, else casts this object to the specified type.

If this is already of the correct type, no copy is performed and the original object is returned.

Parameters:

*   **dtype** ([_type_](https://docs.python.org/3/builtins/functions.html#type "(in Python v3.15)")
     _or_ _string_) – The desired type
    
*   **non\_blocking** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True`, and the source is in pinned memory and destination is on the GPU or vice versa, the copy is performed asynchronously with respect to the host. Otherwise, the argument has no effect.
    
*   **\*\*kwargs** – For compatibility, may contain the key `async` in place of the `non_blocking` argument. The `async` arg is deprecated.
    

Return type:

_\_StorageBase_ | [_TypedStorage_](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage "torch.storage.TypedStorage")
 | [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

untyped()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/storage.py#L900)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.TypedStorage.untyped "Link to this definition")

Return the internal [`torch.UntypedStorage`](https://docs.pytorch.org/docs/2.15/storage.html#torch.UntypedStorage "torch.UntypedStorage")
.

_class_ torch.DoubleStorage(_\*args_, _wrap\_storage\=None_, _dtype\=None_, _device\=None_, _\_internal\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L2380)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.DoubleStorage "Link to this definition")

dtype_: [torch.dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
_ _\= torch.float64_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.DoubleStorage.dtype "Link to this definition")

_class_ torch.FloatStorage(_\*args_, _wrap\_storage\=None_, _dtype\=None_, _device\=None_, _\_internal\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L2391)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.FloatStorage "Link to this definition")

dtype_: [torch.dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
_ _\= torch.float32_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.FloatStorage.dtype "Link to this definition")

_class_ torch.HalfStorage(_\*args_, _wrap\_storage\=None_, _dtype\=None_, _device\=None_, _\_internal\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L2402)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.HalfStorage "Link to this definition")

dtype_: [torch.dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
_ _\= torch.float16_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.HalfStorage.dtype "Link to this definition")

_class_ torch.LongStorage(_\*args_, _wrap\_storage\=None_, _dtype\=None_, _device\=None_, _\_internal\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L2413)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.LongStorage "Link to this definition")

dtype_: [torch.dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
_ _\= torch.int64_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.LongStorage.dtype "Link to this definition")

_class_ torch.IntStorage(_\*args_, _wrap\_storage\=None_, _dtype\=None_, _device\=None_, _\_internal\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L2424)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.IntStorage "Link to this definition")

dtype_: [torch.dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
_ _\= torch.int32_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.IntStorage.dtype "Link to this definition")

_class_ torch.ShortStorage(_\*args_, _wrap\_storage\=None_, _dtype\=None_, _device\=None_, _\_internal\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L2435)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.ShortStorage "Link to this definition")

dtype_: [torch.dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
_ _\= torch.int16_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.ShortStorage.dtype "Link to this definition")

_class_ torch.CharStorage(_\*args_, _wrap\_storage\=None_, _dtype\=None_, _device\=None_, _\_internal\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L2446)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.CharStorage "Link to this definition")

dtype_: [torch.dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
_ _\= torch.int8_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.CharStorage.dtype "Link to this definition")

_class_ torch.ByteStorage(_\*args_, _wrap\_storage\=None_, _dtype\=None_, _device\=None_, _\_internal\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L2369)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.ByteStorage "Link to this definition")

dtype_: [torch.dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
_ _\= torch.uint8_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.ByteStorage.dtype "Link to this definition")

_class_ torch.BoolStorage(_\*args_, _wrap\_storage\=None_, _dtype\=None_, _device\=None_, _\_internal\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L2457)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.BoolStorage "Link to this definition")

dtype_: [torch.dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
_ _\= torch.bool_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.BoolStorage.dtype "Link to this definition")

_class_ torch.BFloat16Storage(_\*args_, _wrap\_storage\=None_, _dtype\=None_, _device\=None_, _\_internal\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L2468)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.BFloat16Storage "Link to this definition")

dtype_: [torch.dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
_ _\= torch.bfloat16_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.BFloat16Storage.dtype "Link to this definition")

_class_ torch.ComplexDoubleStorage(_\*args_, _wrap\_storage\=None_, _dtype\=None_, _device\=None_, _\_internal\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L2479)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.ComplexDoubleStorage "Link to this definition")

dtype_: [torch.dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
_ _\= torch.complex128_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.ComplexDoubleStorage.dtype "Link to this definition")

_class_ torch.ComplexFloatStorage(_\*args_, _wrap\_storage\=None_, _dtype\=None_, _device\=None_, _\_internal\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L2490)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.ComplexFloatStorage "Link to this definition")

dtype_: [torch.dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
_ _\= torch.complex64_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.ComplexFloatStorage.dtype "Link to this definition")

_class_ torch.QUInt8Storage(_\*args_, _wrap\_storage\=None_, _dtype\=None_, _device\=None_, _\_internal\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L2501)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.QUInt8Storage "Link to this definition")

dtype_: [torch.dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
_ _\= torch.quint8_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.QUInt8Storage.dtype "Link to this definition")

_class_ torch.QInt8Storage(_\*args_, _wrap\_storage\=None_, _dtype\=None_, _device\=None_, _\_internal\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L2512)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.QInt8Storage "Link to this definition")

dtype_: [torch.dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
_ _\= torch.qint8_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.QInt8Storage.dtype "Link to this definition")

_class_ torch.QInt32Storage(_\*args_, _wrap\_storage\=None_, _dtype\=None_, _device\=None_, _\_internal\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L2523)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.QInt32Storage "Link to this definition")

dtype_: [torch.dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
_ _\= torch.qint32_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.QInt32Storage.dtype "Link to this definition")

_class_ torch.QUInt4x2Storage(_\*args_, _wrap\_storage\=None_, _dtype\=None_, _device\=None_, _\_internal\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L2534)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.QUInt4x2Storage "Link to this definition")

dtype_: [torch.dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
_ _\= torch.quint4x2_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.QUInt4x2Storage.dtype "Link to this definition")

_class_ torch.QUInt2x4Storage(_\*args_, _wrap\_storage\=None_, _dtype\=None_, _device\=None_, _\_internal\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/__init__.py#L2545)
[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.QUInt2x4Storage "Link to this definition")

dtype_: [torch.dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
_ _\= torch.quint2x4_[#](https://docs.pytorch.org/docs/2.15/storage.html#torch.QUInt2x4Storage.dtype "Link to this definition")

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/storage.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/storage.md.txt)

PyTorch Libraries

*   [ExecuTorch](https://docs.pytorch.org/executorch)
    
*   [Helion](https://docs.pytorch.org/helion)
    
*   [torchao](https://docs.pytorch.org/ao)
    
*   [kineto](https://github.com/pytorch/kineto)
    
*   [torchtitan](https://github.com/pytorch/torchtitan)
    
*   [TorchRL](https://docs.pytorch.org/rl)
    
*   [torchvision](https://docs.pytorch.org/vision)
    
*   [torchaudio](https://docs.pytorch.org/audio)
    
*   [tensordict](https://docs.pytorch.org/tensordict)
    
*   [PyTorch on XLA Devices](https://docs.pytorch.org/xla)
    

Docs
----

Access comprehensive developer documentation for PyTorch

[View Docs](https://docs.pytorch.org/docs/stable/index.html)

Tutorials
---------

Get in-depth tutorials for beginners and advanced developers

[View Tutorials](https://docs.pytorch.org/tutorials)

Resources
---------

Find development resources and get your questions answered

[View Resources](https://pytorch.org/resources)

To analyze traffic and optimize your experience, we serve cookies on this site. By clicking or navigating, you agree to allow our usage of cookies. As the current maintainers of this site, Facebook’s Cookies Policy applies. Learn more, including about available controls: [Cookies Policy](https://opensource.fb.com/legal/cookie-policy)
.

|     |     |
| --- | --- |
|     |     |

|     |     |
| --- | --- |
|     |     |