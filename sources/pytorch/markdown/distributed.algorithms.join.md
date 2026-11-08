Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/distributed.algorithms.join.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/distributed.algorithms.join.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/distributed.algorithms.join.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/distributed.algorithms.join.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/distributed.algorithms.join.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/distributed.algorithms.join.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/distributed.algorithms.join.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/distributed.algorithms.join.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/distributed.algorithms.join.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/distributed.algorithms.join.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/distributed.algorithms.join.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/distributed.algorithms.join.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/distributed.algorithms.join.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/distributed.algorithms.join.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/distributed.algorithms.join.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/distributed.algorithms.join.html)
[v1.13](https://docs.pytorch.org/docs/1.13/distributed.algorithms.join.html)
[v1.12](https://docs.pytorch.org/docs/1.12/distributed.algorithms.join.html)
[v1.11](https://docs.pytorch.org/docs/1.11/distributed.algorithms.join.html)
[v1.10](https://docs.pytorch.org/docs/1.10/distributed.algorithms.join.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/distributed.algorithms.join.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/distributed.algorithms.join.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/distributed.algorithms.join.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/distributed.algorithms.join.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/distributed.algorithms.join.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/distributed.algorithms.join.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/distributed.algorithms.join.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/distributed.algorithms.join.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/distributed.algorithms.join.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/distributed.algorithms.join.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/distributed.algorithms.join.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/distributed.algorithms.join.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/distributed.algorithms.join.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/distributed.algorithms.join.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/distributed.algorithms.join.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/distributed.algorithms.join.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/distributed.algorithms.join.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/distributed.algorithms.join.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/distributed.algorithms.join.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/distributed.algorithms.join.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/distributed.algorithms.join.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/distributed.algorithms.join.html)

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

Generic Join Context Manager[#](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#generic-join-context-manager "Link to this heading")

=========================================================================================================================================================

Created On: Jun 06, 2025 | Last Updated On: Jun 06, 2025

The generic join context manager facilitates distributed training on uneven inputs. This page outlines the API of the relevant classes: `Join`, `Joinable`, and `JoinHook`. For a tutorial, see [Distributed Training with Uneven Inputs Using the Join Context Manager](https://pytorch.org/tutorials/advanced/generic_join.html)
.

_class_ torch.distributed.algorithms.Join(_joinables_, _enable\=True_, _throw\_on\_early\_termination\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/join.py#L104)
[#](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.Join "Link to this definition")

This class defines the generic join context manager, which allows custom hooks to be called after a process joins.

These hooks should shadow the collective communications of non-joined processes to prevent hanging and erroring and to ensure algorithmic correctness. Refer to [`JoinHook`](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.JoinHook "torch.distributed.algorithms.JoinHook")
 for details about the hook definition.

Warning

The context manager requires each participating [`Joinable`](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.Joinable "torch.distributed.algorithms.Joinable")
 to call the method [`notify_join_context()`](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.Join.notify_join_context "torch.distributed.algorithms.Join.notify_join_context")
 before its own per- iteration collective communications to ensure correctness.

Warning

The context manager requires that all `process_group` attributes in the [`JoinHook`](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.JoinHook "torch.distributed.algorithms.JoinHook")
 objects are the same. If there are multiple [`JoinHook`](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.JoinHook "torch.distributed.algorithms.JoinHook")
 objects, then the `device` of the first is used. The process group and device information is used for checking for non- joined processes and for notifying processes to throw an exception if `throw_on_early_termination` is enabled, both of which using an all- reduce.

Parameters:

*   **joinables** (_List__\[_[_Joinable_](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.Joinable "torch.distributed.algorithms.Joinable")\
    _\]_) – a list of the participating [`Joinable`](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.Joinable "torch.distributed.algorithms.Joinable")
     s; their hooks are iterated over in the given order.
    
*   **enable** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – a flag enabling uneven input detection; setting to `False` disables the context manager’s functionality and should only be set when the user knows the inputs will not be uneven (default: `True`).
    
*   **throw\_on\_early\_termination** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – a flag controlling whether to throw an exception upon detecting uneven inputs (default: `False`).
    

Example:

\>>> import os
\>>> import torch
\>>> import torch.distributed as dist
\>>> import torch.multiprocessing as mp
\>>> import torch.nn.parallel.DistributedDataParallel as DDP
\>>> import torch.distributed.optim.ZeroRedundancyOptimizer as ZeRO
\>>> from torch.distributed.algorithms.join import Join
\>>>
\>>> \# On each spawned worker
\>>> def worker(rank):
\>>>     dist.init\_process\_group("nccl", rank\=rank, world\_size\=2)
\>>>     model \= DDP(torch.nn.Linear(1, 1).to(rank), device\_ids\=\[rank\])
\>>>     optim \= ZeRO(model.parameters(), torch.optim.Adam, lr\=0.01)
\>>>     \# Rank 1 gets one more input than rank 0
\>>>     inputs \= \[torch.tensor(\[1.\]).to(rank) for \_ in range(10 + rank)\]
\>>>     with Join(\[model, optim\]):
\>>>         for input in inputs:
\>>>             loss \= model(input).sum()
\>>>             loss.backward()
\>>>             optim.step()
\>>>     \# All ranks reach here without hanging/erroring

Copy to clipboard

_static_ notify\_join\_context(_joinable_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/join.py#L298)
[#](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.Join.notify_join_context "Link to this definition")

Notifies the join context manager that the calling process has not yet joined.

Then, if `throw_on_early_termination=True`, checks if uneven inputs have been detected (i.e. if one process has already joined) and throws an exception if so.

This method should be called from a [`Joinable`](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.Joinable "torch.distributed.algorithms.Joinable")
 object before its per-iteration collective communications. For example, this should be called at the beginning of the forward pass in `DistributedDataParallel`.

Only the first [`Joinable`](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.Joinable "torch.distributed.algorithms.Joinable")
 object passed into the context manager performs the collective communications in this method, and for the others, this method is vacuous.

Parameters:

**joinable** ([_Joinable_](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.Joinable "torch.distributed.algorithms.Joinable")
) – the [`Joinable`](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.Joinable "torch.distributed.algorithms.Joinable")
 object calling this method.

Returns:

An async work handle for the all-reduce meant to notify the context manager that the process has not yet joined if `joinable` is the first one passed into the context manager; `None` otherwise.

_class_ torch.distributed.algorithms.Joinable[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/join.py#L44)
[#](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.Joinable "Link to this definition")

This defines an abstract base class for joinable classes.

A joinable class (inheriting from [`Joinable`](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.Joinable "torch.distributed.algorithms.Joinable")
) should implement [`join_hook()`](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.Joinable.join_hook "torch.distributed.algorithms.Joinable.join_hook")
, which returns a [`JoinHook`](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.JoinHook "torch.distributed.algorithms.JoinHook")
 instance, in addition to [`join_device()`](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.Joinable.join_device "torch.distributed.algorithms.Joinable.join_device")
 and [`join_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.Joinable.join_process_group "torch.distributed.algorithms.Joinable.join_process_group")
 that return device and process group information, respectively.

_abstract property_ join\_device_: [device](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
_[#](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.Joinable.join_device "Link to this definition")

Return the device from which to perform collective communications needed by the join context manager.

_abstract_ join\_hook(_\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/join.py#L60)
[#](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.Joinable.join_hook "Link to this definition")

Return a [`JoinHook`](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.JoinHook "torch.distributed.algorithms.JoinHook")
 instance for the given [`Joinable`](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.Joinable "torch.distributed.algorithms.Joinable")
.

Parameters:

**kwargs** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
) – a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
 containing any keyword arguments to modify the behavior of the join hook at run time; all [`Joinable`](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.Joinable "torch.distributed.algorithms.Joinable")
 instances sharing the same join context manager are forwarded the same value for `kwargs`.

Return type:

[_JoinHook_](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.JoinHook "torch.distributed.algorithms.join.JoinHook")

_abstract property_ join\_process\_group_: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.Joinable.join_process_group "Link to this definition")

Returns the process group for the collective communications needed by the join context manager itself.

_class_ torch.distributed.algorithms.JoinHook[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/join.py#L14)
[#](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.JoinHook "Link to this definition")

This defines a join hook, which provides two entry points in the join context manager.

Entry points : a main hook, which is called repeatedly while there exists a non-joined process, and a post-hook, which is called once all processes have joined.

To implement a join hook for the generic join context manager, define a class that inherits from [`JoinHook`](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.JoinHook "torch.distributed.algorithms.JoinHook")
 and override `main_hook()` and `post_hook()` as appropriate.

main\_hook()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/join.py#L26)
[#](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.JoinHook.main_hook "Link to this definition")

Call this hook while there exists a non-joined process to shadow collective communications in a training iteration.

Training iteration i.e., in one forward pass, backward pass, and optimizer step.

post\_hook(_is\_last\_joiner_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/join.py#L32)
[#](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.JoinHook.post_hook "Link to this definition")

Call hook after all processes have joined.

It is passed an additional `bool` argument `is_last_joiner`, which indicates if the rank is one of the last to join.

Parameters:

**is\_last\_joiner** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
) – `True` if the rank is one of the last to join; `False` otherwise.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/distributed.algorithms.join.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/distributed.algorithms.join.md.txt)

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