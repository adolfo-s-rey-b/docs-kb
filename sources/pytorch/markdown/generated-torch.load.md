Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.load.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.load.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.load.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.load.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.load.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.load.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.load.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.load.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.load.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.load.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.load.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.load.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.load.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.load.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.load.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.load.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.load.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.load.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.load.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.load.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.load.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.load.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.load.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.load.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.load.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.load.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.load.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.load.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.load.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.load.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.load.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.load.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.load.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.load.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.load.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.load.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.load.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.load.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.load.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.load.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.load.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.load.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.load.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.load.html)

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

torch.load[#](https://docs.pytorch.org/docs/2.15/generated/torch.load.html#torch-load "Link to this heading")

==============================================================================================================

torch.load(_f_, _map\_location\=None_, _pickle\_module\=pickle_, _\*_, _weights\_only\=True_, _mmap\=None_, _\*\*pickle\_load\_args_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/serialization.py#L1316)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.load.html#torch.load "Link to this definition")

Loads an object saved with [`torch.save()`](https://docs.pytorch.org/docs/2.15/generated/torch.save.html#torch.save "torch.save")
 from a file.

Warning

[`torch.load()`](https://docs.pytorch.org/docs/2.15/generated/torch.load.html#torch.load "torch.load")
 uses an unpickler under the hood. **Never load data from an untrusted source.**

See [weights\_only security](https://docs.pytorch.org/docs/2.15/notes/serialization.html#weights-only-security)
 for more details.

[`torch.load()`](https://docs.pytorch.org/docs/2.15/generated/torch.load.html#torch.load "torch.load")
 uses Python’s unpickling facilities but treats storages, which underlie tensors, specially. They are first deserialized on the CPU and are then moved to the device they were saved from. If this fails (e.g. because the run time system doesn’t have certain devices), an exception is raised. However, storages can be dynamically remapped to an alternative set of devices using the `map_location` argument.

If `map_location` is a callable, it will be called once for each serialized storage with two arguments: storage and location. The storage argument will be the initial deserialization of the storage, residing on the CPU. Each serialized storage has a location tag associated with it which identifies the device it was saved from, and this tag is the second argument passed to `map_location`. The builtin location tags are `'cpu'` for CPU tensors and `'cuda:device_id'` (e.g. `'cuda:2'`) for CUDA tensors. `map_location` should return either `None` or a storage. If `map_location` returns a storage, it will be used as the final deserialized object, already moved to the right device. Otherwise, [`torch.load()`](https://docs.pytorch.org/docs/2.15/generated/torch.load.html#torch.load "torch.load")
 will fall back to the default behavior, as if `map_location` wasn’t specified.

If `map_location` is a [`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
 object or a string containing a device tag, it indicates the location where all tensors should be loaded.

Otherwise, if `map_location` is a dict, it will be used to remap location tags appearing in the file (keys), to ones that specify where to put the storages (values).

User extensions can register their own location tags and tagging and deserialization methods using [`torch.serialization.register_package()`](https://docs.pytorch.org/docs/2.15/notes/serialization.html#torch.serialization.register_package "torch.serialization.register_package")
.

See [Layout Control](https://docs.pytorch.org/docs/2.15/notes/serialization.html#layout-control)
 for more advanced tools to manipulate a checkpoint.

Parameters:

*   **f** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ [_PathLike_](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ [_IO_](https://docs.python.org/3/library/typing.html#typing.IO "(in Python v3.15)")
    _\[_[_bytes_](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")\
    _\]_) – a file-like object (has to implement `read()`, `readline()`, `tell()`, and `seek()`), or a string or os.PathLike object containing a file name
    
*   **map\_location** ([_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
    _\[__\[__Storage__,_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]__,_ _Storage__\]_ _|_ [_device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
     _|_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ [_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ _None_) – a function, [`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    , string or a dict specifying how to remap storage locations
    
*   **pickle\_module** ([_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")
    ) – module used for unpickling metadata and objects (has to match the `pickle_module` used to serialize file)
    
*   **weights\_only** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
     _|_ _None_) – Indicates whether unpickler should be restricted to loading only tensors, primitive types, dictionaries and any types added via [`torch.serialization.add_safe_globals()`](https://docs.pytorch.org/docs/2.15/notes/serialization.html#torch.serialization.add_safe_globals "torch.serialization.add_safe_globals")
    . See [torch.load with weights\_only=True](https://docs.pytorch.org/docs/2.15/notes/serialization.html#weights-only)
     for more details. When `weights_only=True` and the checkpoint contains sparse tensors, their invariants (e.g. index bounds) are always validated to prevent malformed indices from causing out-of-bounds reads later; this is an O(nnz) scan per sparse tensor and may be slow for large checkpoints.
    
*   **mmap** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
     _|_ _None_) – Indicates whether the file should be mapped rather than loading all the storages into memory. Typically, tensor storages in the file will first be moved from disk to CPU memory, after which they are moved to the location that they were tagged with when saving, or specified by `map_location`. This second step is a no-op if the final location is CPU. When the `mmap` flag is set, instead of copying the tensor storages from disk to CPU memory in the first step, `f` is mapped, which means tensor storages will be lazily loaded when their data is accessed.
    
*   **pickle\_load\_args** ([_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")
    ) – optional keyword arguments passed over to `pickle_module.load()` and `pickle_module.Unpickler()`, only works if `weights_only=False`, e.g., `errors=...`.
    

Return type:

[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")

Note

When you call [`torch.load()`](https://docs.pytorch.org/docs/2.15/generated/torch.load.html#torch.load "torch.load")
 on a file which contains GPU tensors, those tensors will be loaded to GPU by default. You can call `torch.load(.., map_location='cpu')` and then `load_state_dict()` to avoid GPU RAM surge when loading a model checkpoint.

Note

By default, we decode byte strings as `utf-8`. This is to avoid a common error case `UnicodeDecodeError: 'ascii' codec can't decode byte 0x...` when loading files saved by Python 2 in Python 3. If this default is incorrect, you may use an extra `encoding` keyword argument to specify how these objects should be loaded, e.g., `encoding='latin1'` decodes them to strings using `latin1` encoding, and `encoding='bytes'` keeps them as byte arrays which can be decoded later with `byte_array.decode(...)`.

Example

\>>> torch.load("tensors.pt", weights\_only\=True)
\# Load all tensors onto the CPU
\>>> torch.load(
...     "tensors.pt",
...     map\_location\=torch.device("cpu"),
...     weights\_only\=True,
... )
\# Load all tensors onto the CPU, using a function
\>>> torch.load(
...     "tensors.pt",
...     map\_location\=lambda storage, loc: storage,
...     weights\_only\=True,
... )
\# Load all tensors onto GPU 1
\>>> torch.load(
...     "tensors.pt",
...     map\_location\=lambda storage, loc: storage.cuda(1),  \# type: ignore\[attr-defined\]
...     weights\_only\=True,
... )  \# type: ignore\[attr-defined\]
\# Map tensors from GPU 1 to GPU 0
\>>> torch.load(
...     "tensors.pt",
...     map\_location\={"cuda:1": "cuda:0"},
...     weights\_only\=True,
... )
\# Load tensor from io.BytesIO object
\# Loading from a buffer setting weights\_only=False, warning this can be unsafe
\>>> with open("tensor.pt", "rb") as f:
...     buffer \= io.BytesIO(f.read())
\>>> torch.load(buffer, weights\_only\=False)
\# Load a module with 'ascii' encoding for unpickling
\# Loading from a module setting weights\_only=False, warning this can be unsafe
\>>> torch.load("module.pt", encoding\="ascii", weights\_only\=False)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.load.rst.txt)

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