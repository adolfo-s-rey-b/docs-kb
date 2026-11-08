Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/random.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/random.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/random.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/random.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/random.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/random.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/random.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/random.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/random.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/random.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/random.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/random.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/random.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/random.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/random.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/random.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/random.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/random.html)
[v1.13](https://docs.pytorch.org/docs/1.13/random.html)
[v1.12](https://docs.pytorch.org/docs/1.12/random.html)
[v1.11](https://docs.pytorch.org/docs/1.11/random.html)
[v1.10](https://docs.pytorch.org/docs/1.10/random.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/random.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/random.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/random.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/random.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/random.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/random.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/random.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/random.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/random.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/random.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/random.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/random.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/random.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/random.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/random.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/random.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/random.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/random.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/random.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/random.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/random.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/random.html)

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

torch.random[#](https://docs.pytorch.org/docs/2.15/random.html#module-torch.random "Link to this heading")

===========================================================================================================

Created On: Aug 07, 2019 | Last Updated On: Jun 18, 2025

torch.random.fork\_rng(_devices\=None_, _enabled\=True_, _\_caller\='fork\_rng'_, _\_devices\_kw\='devices'_, _device\_type\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/random.py#L156)
[#](https://docs.pytorch.org/docs/2.15/random.html#torch.random.fork_rng "Link to this definition")

Forks the RNG, so that when you return, the RNG is reset to the state that it was previously in.

Parameters:

*   **devices** (_iterable_ _of_ _Device IDs_) – devices for which to fork the RNG. CPU RNG state is always forked. By default, [`fork_rng()`](https://docs.pytorch.org/docs/2.15/random.html#torch.random.fork_rng "torch.random.fork_rng")
     operates on all devices, but will emit a warning if your machine has a lot of devices, since this function will run very slowly in that case. If you explicitly specify devices, this warning will be suppressed
    
*   **enabled** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – if `False`, the RNG is not forked. This is a convenience argument for easily disabling the context manager without having to delete it and unindent your Python code under it.
    
*   **device\_type** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – device type str, default is `None`, in which case the type is taken from [`torch.accelerator.current_accelerator()`](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.current_accelerator.html#torch.accelerator.current_accelerator "torch.accelerator.current_accelerator")
    , falling back to `"cuda"` when the type cannot be determined. As for supported devices, see details in [accelerator](https://docs.pytorch.org/docs/2.15/torch.html#accelerators)
    

Return type:

[_Generator_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "(in Python v3.15)")

torch.random.get\_rng\_state()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/random.py#L39)
[#](https://docs.pytorch.org/docs/2.15/random.html#torch.random.get_rng_state "Link to this definition")

Returns the random number generator state as a torch.ByteTensor.

Note

The returned state is for the default generator on CPU only.

See also: [`torch.random.fork_rng()`](https://docs.pytorch.org/docs/2.15/random.html#torch.random.fork_rng "torch.random.fork_rng")
.

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

torch.random.initial\_seed()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/random.py#L144)
[#](https://docs.pytorch.org/docs/2.15/random.html#torch.random.initial_seed "Link to this definition")

Returns the initial seed for generating random numbers as a Python long.

Note

The returned seed is for the default generator on CPU only.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

torch.random.manual\_seed(_seed_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/random.py#L49)
[#](https://docs.pytorch.org/docs/2.15/random.html#torch.random.manual_seed "Link to this definition")

Sets the seed for generating random numbers on all devices. Returns a torch.Generator object.

Parameters:

**seed** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
) – The desired seed. Value must be within the inclusive range \[-0x8000\_0000\_0000\_0000, 0xffff\_ffff\_ffff\_ffff\]. Otherwise, a RuntimeError is raised. Negative inputs are remapped to positive values with the formula 0xffff\_ffff\_ffff\_ffff + seed.

Return type:

[_Generator_](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch._C.Generator")

torch.random.seed()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/random.py#L89)
[#](https://docs.pytorch.org/docs/2.15/random.html#torch.random.seed "Link to this definition")

Sets the seed for generating random numbers to a non-deterministic random number on all devices. Returns a 64 bit number used to seed the RNG.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

torch.random.set\_rng\_state(_new\_state_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/random.py#L27)
[#](https://docs.pytorch.org/docs/2.15/random.html#torch.random.set_rng_state "Link to this definition")

Sets the random number generator state.

Note

This function only works for CPU. For CUDA, please use [`torch.manual_seed()`](https://docs.pytorch.org/docs/2.15/generated/torch.manual_seed.html#torch.manual_seed "torch.manual_seed")
, which works for both CPU and CUDA.

Parameters:

**new\_state** (_torch.ByteTensor_) – The desired state

torch.random.thread\_safe\_generator()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/random.py#L242)
[#](https://docs.pytorch.org/docs/2.15/random.html#torch.random.thread_safe_generator "Link to this definition")

Returns a thread-safe random number generator for use in DataLoader workers. This function provides a convenient way for transforms and user code to use thread-safe random number generation without manually checking worker context. When called in a DataLoader thread worker, returns the worker’s thread-local [`torch.Generator`](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch.Generator")
. When called in the main process or process workers, returns `None` (which causes PyTorch functions to use the default global RNG). :returns: Thread-local generator in thread workers, None otherwise. :rtype: Optional\[torch.Generator\]

Example::

\>>> from torch.random import thread\_safe\_generator
\>>> generator \= thread\_safe\_generator()
\>>> torch.randint(0, 10, (5,), generator\=generator)

Copy to clipboard

Example with transforms::

\>>> from torch.random import thread\_safe\_generator
\>>> class MyRandomTransform:
...     def \_\_call\_\_(self, img):
...         generator \= thread\_safe\_generator()
...         offset \= torch.randint(0, 10, (2,), generator\=generator)
...         return img\[..., offset\[0\]:, offset\[1\]:\]

Copy to clipboard

Return type:

[_Generator_](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch._C.Generator")
 | None

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/random.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/random.md.txt)

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