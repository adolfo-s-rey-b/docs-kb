Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.DataParallel.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.DataParallel.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.DataParallel.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.DataParallel.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.DataParallel.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.DataParallel.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.DataParallel.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.DataParallel.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.DataParallel.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.DataParallel.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.DataParallel.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.DataParallel.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.DataParallel.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.DataParallel.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.DataParallel.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.DataParallel.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.DataParallel.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.DataParallel.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.DataParallel.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.DataParallel.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.DataParallel.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.DataParallel.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.DataParallel.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.DataParallel.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.DataParallel.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.DataParallel.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.DataParallel.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.DataParallel.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.DataParallel.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.DataParallel.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.DataParallel.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.DataParallel.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.DataParallel.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.DataParallel.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.DataParallel.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.DataParallel.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.DataParallel.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.DataParallel.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.DataParallel.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.DataParallel.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.DataParallel.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.DataParallel.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.DataParallel.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.DataParallel.html)

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

DataParallel[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.DataParallel.html#dataparallel "Link to this heading")

=============================================================================================================================

_class_ torch.nn.DataParallel(_module_, _device\_ids\=None_, _output\_device\=None_, _dim\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/parallel/data_parallel.py#L54)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.DataParallel.html#torch.nn.DataParallel "Link to this definition")

Implements data parallelism at the module level.

This container parallelizes the application of the given `module` by splitting the input across the specified devices by chunking in the batch dimension (other objects will be copied once per device). In the forward pass, the module is replicated on each device, and each replica handles a portion of the input. During the backwards pass, gradients from each replica are summed into the original module.

The batch size should be larger than the number of GPUs used.

Warning

It is recommended to use [`DistributedDataParallel`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")
, instead of this class, to do multi-GPU training, even if there is only a single node. See: [Use nn.parallel.DistributedDataParallel instead of multiprocessing or nn.DataParallel](https://docs.pytorch.org/docs/2.15/notes/cuda.html#cuda-nn-ddp-instead)
 and [Distributed Data Parallel](https://docs.pytorch.org/docs/2.15/notes/ddp.html#ddp)
.

Arbitrary positional and keyword inputs are allowed to be passed into DataParallel but some types are specially handled. tensors will be **scattered** on dim specified (default 0). tuple, list and dict types will be shallow copied. The other types will be shared among different threads and can be corrupted if written to in the model’s forward pass.

The parallelized `module` must have its parameters and buffers on `device_ids[0]` before running this [`DataParallel`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.DataParallel.html#torch.nn.DataParallel "torch.nn.DataParallel")
 module.

Warning

In each forward, `module` is **replicated** on each device, so any updates to the running module in `forward` will be lost. For example, if `module` has a counter attribute that is incremented in each `forward`, it will always stay at the initial value because the update is done on the replicas which are destroyed after `forward`. However, [`DataParallel`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.DataParallel.html#torch.nn.DataParallel "torch.nn.DataParallel")
 guarantees that the replica on `device[0]` will have its parameters and buffers sharing storage with the base parallelized `module`. So **in-place** updates to the parameters or buffers on `device[0]` will be recorded. E.g., [`BatchNorm2d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.BatchNorm2d.html#torch.nn.BatchNorm2d "torch.nn.BatchNorm2d")
 and [`spectral_norm()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.utils.spectral_norm.html#torch.nn.utils.spectral_norm "torch.nn.utils.spectral_norm")
 rely on this behavior to update the buffers.

Warning

Forward and backward hooks defined on `module` and its submodules will be invoked `len(device_ids)` times, each with inputs located on a particular device. Particularly, the hooks are only guaranteed to be executed in correct order with respect to operations on corresponding devices. For example, it is not guaranteed that hooks set via [`register_forward_pre_hook()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.register_forward_pre_hook "torch.nn.Module.register_forward_pre_hook")
 be executed before all `len(device_ids)` [`forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.forward "torch.nn.Module.forward")
 calls, but that each such hook be executed before the corresponding [`forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.forward "torch.nn.Module.forward")
 call of that device.

Warning

When `module` returns a scalar (i.e., 0-dimensional tensor) in `forward()`, this wrapper will return a vector of length equal to number of devices used in data parallelism, containing the result from each device.

Note

There is a subtlety in using the `pack sequence -> recurrent network -> unpack sequence` pattern in a [`Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
 wrapped in [`DataParallel`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.DataParallel.html#torch.nn.DataParallel "torch.nn.DataParallel")
. See [My recurrent network doesn’t work with data parallelism](https://docs.pytorch.org/docs/2.15/notes/faq.html#pack-rnn-unpack-with-data-parallelism)
 section in FAQ for details.

Parameters:

*   **module** ([_Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
    ) – module to be parallelized
    
*   **device\_ids** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
     _of_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    ) – CUDA devices (default: all devices)
    
*   **output\_device** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    ) – device location of output (default: device\_ids\[0\])
    

Variables:

**module** ([_Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
) – the module to be parallelized

Example:

\>>> net \= torch.nn.DataParallel(model, device\_ids\=\[0, 1, 2\])
\>>> output \= net(input\_var)  \# input\_var can be on any device, including CPU

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.DataParallel.rst.txt)

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