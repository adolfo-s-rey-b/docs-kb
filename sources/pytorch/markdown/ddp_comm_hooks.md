Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/ddp_comm_hooks.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/ddp_comm_hooks.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/ddp_comm_hooks.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/ddp_comm_hooks.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/ddp_comm_hooks.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/ddp_comm_hooks.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/ddp_comm_hooks.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/ddp_comm_hooks.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/ddp_comm_hooks.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/ddp_comm_hooks.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/ddp_comm_hooks.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/ddp_comm_hooks.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/ddp_comm_hooks.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/ddp_comm_hooks.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/ddp_comm_hooks.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/ddp_comm_hooks.html)
[v1.13](https://docs.pytorch.org/docs/1.13/ddp_comm_hooks.html)
[v1.12](https://docs.pytorch.org/docs/1.12/ddp_comm_hooks.html)
[v1.11](https://docs.pytorch.org/docs/1.11/ddp_comm_hooks.html)
[v1.10](https://docs.pytorch.org/docs/1.10/ddp_comm_hooks.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/ddp_comm_hooks.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/ddp_comm_hooks.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/ddp_comm_hooks.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/ddp_comm_hooks.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/ddp_comm_hooks.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/ddp_comm_hooks.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/ddp_comm_hooks.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/ddp_comm_hooks.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/ddp_comm_hooks.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/ddp_comm_hooks.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/ddp_comm_hooks.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/ddp_comm_hooks.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/ddp_comm_hooks.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/ddp_comm_hooks.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/ddp_comm_hooks.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/ddp_comm_hooks.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/ddp_comm_hooks.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/ddp_comm_hooks.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/ddp_comm_hooks.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/ddp_comm_hooks.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/ddp_comm_hooks.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/ddp_comm_hooks.html)

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

DDP Communication Hooks[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#ddp-communication-hooks "Link to this heading")

==================================================================================================================================

Created On: Jun 06, 2025 | Last Updated On: May 12, 2026

DDP communication hook is a generic interface to control how to communicate gradients across workers by overriding the vanilla allreduce in [DistributedDataParallel](https://pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel.)
. A few built-in communication hooks are provided, and users can easily apply any of these hooks to optimize communication. Besides, the hook interface can also support user-defined communication strategies for more advanced use cases.

How to Use a Communication Hook?[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#how-to-use-a-communication-hook "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

To use a communication hook, the user just needs to let the DDP model register the hook before the training loop as below.

[`torch.nn.parallel.DistributedDataParallel.register_comm_hook()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel.register_comm_hook "torch.nn.parallel.DistributedDataParallel.register_comm_hook")

What Does a Communication Hook Operate On?[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#what-does-a-communication-hook-operate-on "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

A communication hook provides a flexible way to allreduce gradients. Therefore, it mainly operates on the gradients on each replica before allreduce, which are bucketized to increase the overlap between communication and computation. Particularly, [`torch.distributed.GradBucket`](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.GradBucket "torch.distributed.GradBucket")
 represents a bucket of gradient tensors to be allreduced.

_class_ torch.distributed.GradBucket[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.GradBucket "Link to this definition")

This class mainly passes a flattened gradient tensor (returned by [`buffer()`](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.GradBucket.buffer "torch.distributed.GradBucket.buffer")
) to DDP communication hook. This tensor can be further decomposed into a list of per-parameter tensors within this bucket (returned by `get_per_parameter_tensors()`) to apply layer-wise operations.

torch.distributed.GradBucket.index(_self: [torch.\_C.\_distributed\_c10d.GradBucket](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.GradBucket "torch._C._distributed_c10d.GradBucket")
_) → [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.GradBucket.index "Link to this definition")

Warning

Since the buckets are rebuilt after the first iteration, should not rely on the indices at the beginning of training.

Returns:

The index of a bucket that stores gradients of a few contiguous layers. All the gradients are bucketized.

torch.distributed.GradBucket.buffer(_self: [torch.\_C.\_distributed\_c10d.GradBucket](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.GradBucket "torch._C._distributed_c10d.GradBucket")
_) → [torch.Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.GradBucket.buffer "Link to this definition")

Returns:

A flattened 1D `torch.Tensor` buffer, which can be further decomposed into a list of per-parameter tensors within this bucket.

torch.distributed.GradBucket.gradients(_self: [torch.\_C.\_distributed\_c10d.GradBucket](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.GradBucket "torch._C._distributed_c10d.GradBucket")
_) → [list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[torch.Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\][#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.GradBucket.gradients "Link to this definition")

Returns:

A list of `torch.Tensor`. Each tensor in the list corresponds to a gradient.

torch.distributed.GradBucket.is\_last(_self: [torch.\_C.\_distributed\_c10d.GradBucket](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.GradBucket "torch._C._distributed_c10d.GradBucket")
_) → [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.GradBucket.is_last "Link to this definition")

Returns:

Whether this bucket is the last bucket to allreduce in an iteration. This also means that this bucket corresponds to the first few layers in the forward pass.

torch.distributed.GradBucket.set\_buffer(_self: [torch.\_C.\_distributed\_c10d.GradBucket](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.GradBucket "torch._C._distributed_c10d.GradBucket")
_, _buffer: [torch.Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.GradBucket.set_buffer "Link to this definition")

Replaces the tensor in the bucket with the input tensor buffer.

torch.distributed.GradBucket.parameters(_self: [torch.\_C.\_distributed\_c10d.GradBucket](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.GradBucket "torch._C._distributed_c10d.GradBucket")
_) → [list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[torch.Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\][#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.GradBucket.parameters "Link to this definition")

Returns:

A list of `torch.Tensor`. Each tensor in the list corresponds to a model parameter.

Register Communication Hook[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#register-communication-hook "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

torch.distributed.algorithms.ddp\_comm\_hooks.register\_ddp\_comm\_hook(_comm\_hook\_type_, _model_, _state\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/ddp_comm_hooks/__init__.py#L127)
[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.register_ddp_comm_hook "Link to this definition")

Register `ddp_comm_hooks` to DDP model.

Registers the hooks of `torch.distributed.algorithms.ddp_comm_hooks` to the DDP model. User can specify the type of hook as an enum `DDPCommHookType` type using `comm_hook_type` input. State input will be passed to the model. Uses Python comm hook implementations.

Example::

\>>> register\_ddp\_comm\_hook(DDPCommHookType.FP16\_COMPRESS, model, state)

Copy to clipboard

torch.distributed.algorithms.ddp\_comm\_hooks.post\_localSGD\_hook.post\_localSGD\_hook(_state_, _bucket_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/ddp_comm_hooks/post_localSGD_hook.py#L69)
[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.post_localSGD_hook.post_localSGD_hook "Link to this definition")

Run post-localSGD algorithm.

This DDP communication hook is used for running post-localSGD algorithm, by combining with a model averaging component (e.g., `PeriodicModelAverager`) that runs after the optimizer step.

Parameters:

*   **state** (_PostLocalSGDState_) – State information to run post-localSGD. Users mainly need to tune `start_localSGD_iter` to determine when to start local SGD.
    
*   **bucket** (_dist.GradBucket_) – Bucket that stores a 1D flattened gradient tensor that batches multiple per-variable tensors. Note that since DDP comm hook only supports single process single device mode, only exactly one tensor is stored in this bucket.
    

Returns:

Future handler of the communication, which updates the gradients in place.

Return type:

[_Future_](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.jit.Future")
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]

Example::

\>>> state \= PostLocalSGDState(process\_group\=process\_group, subgroup\=subgroup,
                          start\_localSGD\_iter=10)
\>>> ddp\_model.register\_comm\_hook(state, post\_localSGD\_hook)
\>>> \# Also need to establish a model averaging module and run model averaging after \`\`optimizer.step()\`\`.
\>>> \# Please refer to the examples in \`\`torch.distributed.algorithms.model\_averaging.averagers\`\` module.

Copy to clipboard

torch.distributed.algorithms.ddp\_comm\_hooks.ddp\_zero\_hook.hook\_with\_zero\_step(_hook_, _ddp_, _zero_, _shard\_buckets\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/ddp_comm_hooks/ddp_zero_hook.py#L183)
[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.ddp_zero_hook.hook_with_zero_step "Link to this definition")

Modify `hook` to overlap `ZeroRedundancyOptimizer` optimizer step with `DistributedDataParallel` backward pass.

This approach overlaps the optimizer computation and communication with the backward communication. In particular, the backward computation proceeds contiguously, and the optimizer computation follows, overlapping with outstanding backward communication (i.e. all-reduces) and possibly other optimizer communication (i.e. broadcasts). The optimizer step computation begins after the last gradient bucket computation has finished.

This approach may be preferred over [`hook_with_zero_step_interleaved()`](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.ddp_zero_hook.hook_with_zero_step_interleaved "torch.distributed.algorithms.ddp_comm_hooks.ddp_zero_hook.hook_with_zero_step_interleaved")
 if communication is relatively slow compared to computation.

Parameters:

*   **hook** (_Callable__\[__\[__Any__,_ _dist.GradBucket__\]__,_ [_torch.futures.Future_](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")\
    _\]_) – the hook to modify.
    
*   **ddp** ([_DistributedDataParallel_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")
    ) – the `DistributedDataParallel` instance to use.
    
*   **zero** ([_ZeroRedundancyOptimizer_](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.ZeroRedundancyOptimizer "torch.distributed.optim.ZeroRedundancyOptimizer")
    ) – the `ZeroRedundancyOptimizer` instance to use.
    
*   **shard\_buckets** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – if `True`, then the assignment of each `DistributedDataParallel` bucket is partitioned across possibly multiple `ZeroRedundancyOptimizer` instances (i.e. across possibly multiple ranks) to approximate uniformity; if `False`, then each bucket is wholly assigned to a single `ZeroRedundancyOptimizer` instance (i.e. to a single rank).
    

Returns:

The modified hook.

Raises:

*   [**ValueError**](https://docs.python.org/3/builtins/exceptions.html#ValueError "(in Python v3.15)")
     – if `zero` was constructed with `overlap_with_ddp=False`.
    
*   [**RuntimeError**](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "(in Python v3.15)")
     – if using any backend other than NCCL/HCCL since currently Gloo may hang.
    

Return type:

[_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
, [_GradBucket_](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.GradBucket "torch._C._distributed_c10d.GradBucket")\
\], [_Future_](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.jit.Future")\
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]\]

Warning

Given the way that overlapping `DistributedDataParallel` with `ZeroRedundancyOptimizer` is currently implemented, the first two or three training iterations do not perform parameter updates in the optimizer step, depending on if `static_graph=False` or `static_graph=True`, respectively. This is because it needs information about the gradient bucketing strategy used by `DistributedDataParallel`, which is not finalized until the second forward pass if `static_graph=False` or until the third forward pass if `static_graph=True`.

torch.distributed.algorithms.ddp\_comm\_hooks.ddp\_zero\_hook.hook\_with\_zero\_step\_interleaved(_hook_, _ddp_, _zero_, _shard\_buckets\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/ddp_comm_hooks/ddp_zero_hook.py#L344)
[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.ddp_zero_hook.hook_with_zero_step_interleaved "Link to this definition")

Modify `hook` to overlap `ZeroRedundancyOptimizer` optimizer step with `DistributedDataParallel` backward pass

This approach overlaps the optimizer computation and communication with the backward computation and communication. In particular, once a bucket’s gradients have been computed, the optimizer computation using those gradients is launched (though the actual computation must wait for the bucket’s all-reduce to complete). This yields an interleaving of all- reduces and broadcasts in the communication stream.

This approach may be preferred over [`hook_with_zero_step()`](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.ddp_zero_hook.hook_with_zero_step "torch.distributed.algorithms.ddp_comm_hooks.ddp_zero_hook.hook_with_zero_step")
 if communication is relatively fast compared to computation.

Parameters:

*   **hook** (_Any \* dist.GradBucket -> torch.futures.Future_) – the hook to modify.
    
*   **ddp** ([_DistributedDataParallel_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")
    ) – the `DistributedDataParallel` instance to use.
    
*   **zero** ([_ZeroRedundancyOptimizer_](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.ZeroRedundancyOptimizer "torch.distributed.optim.ZeroRedundancyOptimizer")
    ) – the `ZeroRedundancyOptimizer` instance to use.
    
*   **shard\_buckets** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – if `True`, then the assignment of each `DistributedDataParallel` bucket is partitioned across possibly multiple `ZeroRedundancyOptimizer` instances (i.e. across possibly multiple ranks) to approximate uniformity; if `False`, then each bucket is wholly assigned to a single `ZeroRedundancyOptimizer` instance (i.e. to a single rank).
    

Returns:

The modified hook.

Raises:

*   [**ValueError**](https://docs.python.org/3/builtins/exceptions.html#ValueError "(in Python v3.15)")
     – if `zero` was constructed with `overlap_with_ddp=False`.
    
*   [**RuntimeError**](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "(in Python v3.15)")
     – if using any backend other than NCCL since currently Gloo may hang.
    

Return type:

[_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
, [_GradBucket_](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.GradBucket "torch._C._distributed_c10d.GradBucket")\
\], [_Future_](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.jit.Future")\
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]\]

Warning

Given the way that overlapping `DistributedDataParallel` with `ZeroRedundancyOptimizer` is currently implemented, the first two or three training iterations do not perform parameter updates in the optimizer step, depending on if `static_graph=False` or `static_graph=True`, respectively. This is because it needs information about the gradient bucketing strategy used by `DistributedDataParallel`, which is not finalized until the second forward pass if `static_graph=False` or until the third forward pass if `static_graph=True`.

torch.distributed.algorithms.ddp\_comm\_hooks.quantization\_hooks.quantization\_perchannel\_hook(_process\_group_, _bucket_, _bucket\_size\=512_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/ddp_comm_hooks/quantization_hooks.py#L125)
[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.quantization_hooks.quantization_perchannel_hook "Link to this definition")

Apply\`\`torch.quantize\_per\_channel\`\` logic to DDP using `allgather` protocol.

Compared to per-tensor, the main motivation of per-channel is for considerably large tensors such as a tensor that contains 6 million elements quantizing per a bucket size of 512 (or 128) elements may significantly increase the resolution.

It first splits `GradBucket` tensor into multiple chunks (channels) of `bucket_size` elements. Then, workers allgather the scales and zero points of their own `GradBucket` prior to the quantization. After all workers have that information, the first `then` callback called `quantize_and_allgather` quantizes worker’s own gradient tensor, and uses `allgather` to communicate these across all workers. The final `then` callback called `dequantize_and_aggregate`, dequantizes, flattens, and aggregates each quantized gradient tensor locally and returns the mean.

Warning

This is experimental, and uses `allgather` protocol which is considerably slower than `allreduce` protocol. It works only with flattened grads.

Example::

\>>> ddp\_model.register\_comm\_hook(process\_group, quantization\_perchannel\_hook)

Copy to clipboard

Return type:

[_Future_](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.jit.Future")
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]

torch.distributed.algorithms.ddp\_comm\_hooks.quantization\_hooks.quantization\_pertensor\_hook(_process\_group_, _bucket_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/ddp_comm_hooks/quantization_hooks.py#L46)
[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.quantization_hooks.quantization_pertensor_hook "Link to this definition")

Apply `torch.quantize_per_tensor` logic to DDP using `allgather` protocol.

Workers first allgather the scale and zero point of their own `GradBucket` prior to the quantization. After all workers have that information, the first `then` callback called `quantize_and_allgather` quantizes worker’s own gradient tensor, and uses `allgather` to communicate these across all workers. The final `then` callback called `dequantize_and_aggregate`, dequantizes and aggregates each quantized gradient tensor locally and returns the mean.

Warning

This is experimental, and uses `allgather` protocol which is considerably slower than `allreduce` protocol. It works only with flattened grads.

Example::

\>>> ddp\_model.register\_comm\_hook(process\_group, quantization\_pertensor\_hook)

Copy to clipboard

Return type:

[_Future_](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.jit.Future")
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]

Default Communication Hooks[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#default-communication-hooks "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

Default communication hooks are simple **stateless** hooks, so the input state in `register_comm_hook` is either a process group or `None`. The input `bucket` is a [`torch.distributed.GradBucket`](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.GradBucket "torch.distributed.GradBucket")
 object.

torch.distributed.algorithms.ddp\_comm\_hooks.default\_hooks.allreduce\_hook(_process\_group_, _bucket_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/ddp_comm_hooks/default_hooks.py#L35)
[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.default_hooks.allreduce_hook "Link to this definition")

Call `allreduce` using `GradBucket` tensors.

Once gradient tensors are aggregated across all workers, its `then` callback takes the mean and returns the result.

If user registers this DDP communication hook, DDP results is expected to be same as the case where no hook was registered. Hence, this won’t change behavior of DDP and user can use this as a reference or modify this hook to log useful information or any other purposes while unaffecting DDP behavior.

Example::

\>>> ddp\_model.register\_comm\_hook(process\_group, allreduce\_hook)

Copy to clipboard

Return type:

[_Future_](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.jit.Future")
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]

torch.distributed.algorithms.ddp\_comm\_hooks.default\_hooks.fp16\_compress\_hook(_process\_group_, _bucket_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/ddp_comm_hooks/default_hooks.py#L96)
[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.default_hooks.fp16_compress_hook "Link to this definition")

Compress by casting `GradBucket` to `torch.float16` divided by process group size.

This DDP communication hook implements a simple gradient compression approach that casts `GradBucket` tensor to half-precision floating-point format (`torch.float16`) and then divides it by the process group size. It allreduces those `float16` gradient tensors. Once compressed gradient tensors are allreduced, the chained callback `decompress` casts it back to the input data type (such as `float32`).

Example::

\>>> ddp\_model.register\_comm\_hook(process\_group, fp16\_compress\_hook)

Copy to clipboard

Return type:

[_Future_](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.jit.Future")
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]

torch.distributed.algorithms.ddp\_comm\_hooks.default\_hooks.bf16\_compress\_hook(_process\_group_, _bucket_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/ddp_comm_hooks/default_hooks.py#L116)
[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.default_hooks.bf16_compress_hook "Link to this definition")

Warning: This API is experimental, and it requires NCCL version later than 2.9.6.

This DDP communication hook implements a simple gradient compression approach that casts `GradBucket` tensor to half-precision [Brain floating point format](https://en.wikipedia.org/wiki/Bfloat16_floating-point_format)
 (`torch.bfloat16`) and then divides it by the process group size. It allreduces those `bfloat16` gradient tensors. Once compressed gradient tensors are allreduced, the chained callback `decompress` casts it back to the input data type (such as `float32`).

Example::

\>>> ddp\_model.register\_comm\_hook(process\_group, bf16\_compress\_hook)

Copy to clipboard

Return type:

[_Future_](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.jit.Future")
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]

Additionally, a communication hook wrapper is provided to support [`fp16_compress_hook()`](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.default_hooks.fp16_compress_hook "torch.distributed.algorithms.ddp_comm_hooks.default_hooks.fp16_compress_hook")
 or [`bf16_compress_hook()`](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.default_hooks.bf16_compress_hook "torch.distributed.algorithms.ddp_comm_hooks.default_hooks.bf16_compress_hook")
 as a wrapper, which can be combined with other communication hooks.

torch.distributed.algorithms.ddp\_comm\_hooks.default\_hooks.fp16\_compress\_wrapper(_hook_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/ddp_comm_hooks/default_hooks.py#L137)
[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.default_hooks.fp16_compress_wrapper "Link to this definition")

Cast input tensor to `torch.float16`, cast result of hook back to input dtype.

This wrapper casts the input gradient tensor of a given DDP communication hook to half-precision floating point format (`torch.float16`), and casts the resulting tensor of the given hook back to the input data type, such as `float32`. Therefore, `fp16_compress_hook` is equivalent to `fp16_compress_wrapper(allreduce_hook)`.

Example::

\>>> state \= PowerSGDState(process\_group\=process\_group, matrix\_approximation\_rank\=1, start\_powerSGD\_iter\=10)
\>>> ddp\_model.register\_comm\_hook(state, fp16\_compress\_wrapper(powerSGD\_hook))

Copy to clipboard

Return type:

[_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
, [_GradBucket_](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.GradBucket "torch._C._distributed_c10d.GradBucket")\
\], [_Future_](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.jit.Future")\
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]\]

torch.distributed.algorithms.ddp\_comm\_hooks.default\_hooks.bf16\_compress\_wrapper(_hook_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/ddp_comm_hooks/default_hooks.py#L175)
[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.default_hooks.bf16_compress_wrapper "Link to this definition")

Warning: This API is experimental, and it requires NCCL version later than 2.9.6.

This wrapper casts the input gradient tensor of a given DDP communication hook to half-precision [Brain floating point format](https://en.wikipedia.org/wiki/Bfloat16_floating-point_format)
 (`torch.bfloat16`), and casts the resulting tensor of the given hook back to the input data type, such as `float32`.

Therefore, `bf16_compress_hook` is equivalent to `bf16_compress_wrapper(allreduce_hook)`.

Example::

\>>> state \= PowerSGDState(process\_group\=process\_group, matrix\_approximation\_rank\=1, start\_powerSGD\_iter\=10)
\>>> ddp\_model.register\_comm\_hook(state, bf16\_compress\_wrapper(powerSGD\_hook))

Copy to clipboard

Return type:

[_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
, [_GradBucket_](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.GradBucket "torch._C._distributed_c10d.GradBucket")\
\], [_Future_](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.jit.Future")\
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]\]

PowerSGD Communication Hook[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#powersgd-communication-hook "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

PowerSGD ([Vogels et al., NeurIPS 2019](https://arxiv.org/abs/1905.13727)
) is a gradient compression algorithm, which can provide very high compression rates and accelerate bandwidth-bound distributed training. This algorithm needs to maintain both some hyperparameters and the internal state. Therefore, PowerSGD communication hook is a **stateful** hook, and the user needs to provide a state object defined as below.

### PowerSGD State[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#powersgd-state "Link to this heading")

_class_ torch.distributed.algorithms.ddp\_comm\_hooks.powerSGD\_hook.PowerSGDState(_process\_group_, _matrix\_approximation\_rank\=1_, _start\_powerSGD\_iter\=1000_, _min\_compression\_rate\=2_, _use\_error\_feedback\=True_, _warm\_start\=True_, _orthogonalization\_epsilon\=0_, _random\_seed\=0_, _compression\_stats\_logging\_frequency\=10000_, _batch\_tensors\_with\_same\_shape\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/ddp_comm_hooks/powerSGD_hook.py#L122)
[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.powerSGD_hook.PowerSGDState "Link to this definition")

Store both the algorithm’s hyperparameters and internal state for all gradients during training.

Particularly, `matrix_approximation_rank` and `start_powerSGD_iter` are the main hyperparameters that should be tuned by the user. For performance, we suggest to keep binary hyperparameters `use_error_feedback` and `warm_start` on.

1.  `matrix_approximation_rank` controls the size of compressed low-rank tensors, which determines the compression rate. The lower the rank, the stronger the compression.
    
    > 1.1. If `matrix_approximation_rank` is too low, the full model quality will need more training steps to reach or will never reach and yield loss in accuracy.
    > 
    > 1.2. The increase of `matrix_approximation_rank` can substantially increase the computation costs of the compression, and the accuracy may not be further improved beyond a certain `matrix_approximation_rank` threshold.
    

To tune `matrix_approximation_rank`, we suggest to start from 1 and increase by factors of 2 (like an exponential grid search, 1, 2, 4, …), until a satisfactory accuracy is reached. Typically only a small value 1-4 is used. For some NLP tasks (as shown in Appendix D of the original paper), this value has been increased to 32.

2.  `start_powerSGD_iter` defers PowerSGD compression until step `start_powerSGD_iter`, and vanilla allreduce runs prior to step `start_powerSGD_iter`. This hybrid scheme of **vanilla allreduce + PowerSGD** can effectively improve the accuracy, even a relatively small `matrix_approximation_rank` is used. This is because that, the beginning of training phase is usually very sensitive to inaccurate gradients, and compressing gradients too early may make the training quickly take a suboptimal trajectory, which can result in an irrecoverable impact on the accuracy.
    

To tune `start_powerSGD_iter`, we suggest to start with 10% of total training steps, and increase it until a satisfactory accuracy is reached. If there is a warm-up stage in the training, `start_powerSGD_iter` typically should be no less than the number of warm-up steps.

3.  `min_compression_rate` is the minimum compression rate required when a layer is compressed. Due to the computation overheads incurred by the compression, a tensor is worth compressing only if there can be sufficient saving in bandwidth, where `(num_rows + num_cols) * matrix_approximation_rank * min_compression_rate < num_rows * num_cols`. If the specified compression rate threshold cannot be satisfied, the tensor will be directly allreduced without compression.
    

Compression statistics are logged every `compression_stats_logging_frequency` iterations once PowerSGD compression starts.

4.  `orthogonalization_epsilon` can be a very small value (e.g., 1e-8) added to every normalized matrix column in orthogonalization step, to prevent div-by-zero error if any column has all 0s. If this can already be prevented (e.g., by batch normalization), an epsilon of 0 is recommended for accuracy.
    
5.  `batch_tensors_with_same_shape` controls whether to compress and decompress tensors with same shape in a batched operation to achieve higher parallelism. Note that you should also increase the bucket size (i.e., `bucket_cap_mb` arg in DDP constructor) to make more same-shaped tensors appear in the same bucket, however this may reduce the overlap between computation and communication, and increase the memory footprint due to stacking the tensors of the same shape. Set to `True` if the compression / decompression computation is a bottleneck.
    

Warning

If error feedback or warm-up is enabled, the minimum value of `start_powerSGD_iter` allowed in DDP is 2. This is because there is another internal optimization that rebuilds buckets at iteration 1 in DDP, and this can conflict with any tensor memorized before the rebuild process.

### PowerSGD Hooks[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#powersgd-hooks "Link to this heading")

Warning

PowerSGD typically requires extra memory of the same size as the model’s gradients to enable error feedback, which can compensate for biased compressed communication and improve accuracy.

Warning

PowerSGD hooks may conflict with [Apex automatic mixed precision package](https://github.com/NVIDIA/apex)
. Please use PyTorch [native automatic mixed precision package](https://pytorch.org/docs/stable/amp.html)
 instead.

torch.distributed.algorithms.ddp\_comm\_hooks.powerSGD\_hook.powerSGD\_hook(_state_, _bucket_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/ddp_comm_hooks/powerSGD_hook.py#L340)
[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.powerSGD_hook.powerSGD_hook "Link to this definition")

Implement PowerSGD algorithm.

This DDP communication hook implements PowerSGD gradient compression algorithm described in the [paper](https://arxiv.org/abs/1905.13727)
. Once gradient tensors are aggregated across all workers, this hook applies compression as follows:

1.  Views the input flattened 1D gradient tensor as a list of per-parameter tensors, and divides all the tensors into two groups:
    
    > 1.1 The tensors that should be compressed before allreduce, because the compression can give enough saving in bandwidth.
    > 
    > 1.2 Rest of the tensors will be directly allreduced without compression, including all the vector tensors (for biases).
    
2.  Handles uncompressed tensors:
    
    > 2.1. Allocate contiguous memory for those uncompressed tensors, and allreduces all the uncompressed tensors as a batch, without compression;
    > 
    > 2.2. Copies the individual uncompressed tensors from the contiguous memory back to the input tensor.
    
3.  Handles the tensors that should be compressed by PowerSGD compression:
    
    > 3.1. For each tensor M, creates two low-rank tensors P and Q for decomposing M, such that M = PQ^T, where Q is initialized from a standard normal distribution and orthogonalized;
    > 
    > 3.2. Computes each P in Ps, which is equal to MQ;
    > 
    > 3.3. Allreduces Ps as a batch;
    > 
    > 3.4. Orthogonalizes each P in Ps;
    > 
    > 3.5. Computes each Q in Qs, which is approximately equal to M^TP;
    > 
    > 3.6. Allreduces Qs as a batch;
    > 
    > 3.7. Computes each M among all the compressed tensors, which is approximately equal to PQ^T.
    

Note that this communication hook enforces vanilla allreduce for the first `state.start_powerSGD_iter` iterations. This not only gives the user more control over the tradeoff between speedup and accuracy, but also helps abstract away some complexity of the internal optimization of DDP for future communication hook developers.

Parameters:

*   **state** ([_PowerSGDState_](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.powerSGD_hook.PowerSGDState "torch.distributed.algorithms.ddp_comm_hooks.powerSGD_hook.PowerSGDState")
    ) – State information to configure the compression rate and support error feedback, warm start, etc. To tune the compression configs, mainly need to tune `matrix_approximation_rank`, `start_powerSGD_iter` and `min_compression_rate`.
    
*   **bucket** (_dist.GradBucket_) – Bucket that stores a 1D flattened gradient tensor that batches multiple per-variable tensors. Note that since DDP comm hook only supports single process single device mode, only exactly one tensor is stored in this bucket.
    

Returns:

Future handler of the communication, which updates the gradients in place.

Return type:

[_Future_](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.jit.Future")
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]

Example::

\>>> state \= PowerSGDState(process\_group\=process\_group, matrix\_approximation\_rank\=1,
                          start\_powerSGD\_iter=10, min\_compression\_rate=0.5)
\>>> ddp\_model.register\_comm\_hook(state, powerSGD\_hook)

Copy to clipboard

torch.distributed.algorithms.ddp\_comm\_hooks.powerSGD\_hook.batched\_powerSGD\_hook(_state_, _bucket_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/ddp_comm_hooks/powerSGD_hook.py#L655)
[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.powerSGD_hook.batched_powerSGD_hook "Link to this definition")

Implement simplified PowerSGD algorithm.

This DDP communication hook implements a simplified PowerSGD gradient compression algorithm described in the [paper](https://arxiv.org/abs/1905.13727)
. This variant does not compress the gradients layer by layer, but instead compresses the flattened input tensor that batches all the gradients. Therefore, it is **faster** than [`powerSGD_hook()`](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.powerSGD_hook.powerSGD_hook "torch.distributed.algorithms.ddp_comm_hooks.powerSGD_hook.powerSGD_hook")
, but usually results in a **much lower accuracy**, unless `matrix_approximation_rank` is 1.

Warning

Increasing `matrix_approximation_rank` here may not necessarily increase the accuracy, because batching per-parameter tensors without column/row alignment can destroy low-rank structure. Therefore, the user should always consider [`powerSGD_hook()`](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.powerSGD_hook.powerSGD_hook "torch.distributed.algorithms.ddp_comm_hooks.powerSGD_hook.powerSGD_hook")
 first, and only consider this variant when a satisfactory accuracy can be achieved when `matrix_approximation_rank` is 1.

Once gradient tensors are aggregated across all workers, this hook applies compression as follows:

1.  Views the input flattened 1D gradient tensor as a square-shaped tensor M with 0 paddings;
    
2.  Creates two low-rank tensors P and Q for decomposing M, such that M = PQ^T, where Q is initialized from a standard normal distribution and orthogonalized;
    
3.  Computes P, which is equal to MQ;
    
4.  Allreduces P;
    
5.  Orthogonalizes P;
    
6.  Computes Q, which is approximately equal to M^TP;
    
7.  Allreduces Q;
    
8.  Computes M, which is approximately equal to PQ^T.
    
9.  Truncates the input tensor to the original length.
    

Note that this communication hook enforces vanilla allreduce for the first `state.start_powerSGD_iter` iterations. This not only gives the user more control over the tradeoff between speedup and accuracy, but also helps abstract away some complexity of the internal optimization of DDP for future communication hook developers.

Parameters:

*   **state** ([_PowerSGDState_](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.powerSGD_hook.PowerSGDState "torch.distributed.algorithms.ddp_comm_hooks.powerSGD_hook.PowerSGDState")
    ) – State information to configure the compression rate and support error feedback, warm start, etc. To tune the compression configs, mainly need to tune `matrix_approximation_rank` and `start_powerSGD_iter`.
    
*   **bucket** (_dist.GradBucket_) – Bucket that stores a 1D flattened gradient tensor that batches multiple per-variable tensors. Note that since DDP comm hook only supports single process single device mode, only exactly one tensor is stored in this bucket.
    

Returns:

Future handler of the communication, which updates the gradients in place.

Return type:

[_Future_](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.jit.Future")
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]

Example::

\>>> state \= PowerSGDState(process\_group\=process\_group, matrix\_approximation\_rank\=1)
\>>> ddp\_model.register\_comm\_hook(state, batched\_powerSGD\_hook)

Copy to clipboard

Debugging Communication Hooks[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#debugging-communication-hooks "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

As the name implies, debugging communication hooks are **only** used for debugging and performance optimization purpose.

Warning

Debugging communication hooks do not necessarily output the correct results.

torch.distributed.algorithms.ddp\_comm\_hooks.debugging\_hooks.noop\_hook(_\__, _bucket_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/ddp_comm_hooks/debugging_hooks.py#L10)
[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.debugging_hooks.noop_hook "Link to this definition")

Return a future that wraps the input, so it is a no-op that does not incur any communication overheads.

This hook should **only** be used for headroom analysis of allreduce optimization, instead of the normal gradient synchronization. For example, if only less than 10% speedup of training time can be observed after this hook is registered, it usually implies that allreduce is not a performance bottleneck for this case. Such instrumentation can be particularly useful if GPU traces cannot be easily retrieved or the trace analysis is complicated by some factors such as the overlap between allreduce and computation or the desynchronization across ranks.

Example::

\>>> ddp\_model.register\_comm\_hook(None, noop\_hook)

Copy to clipboard

Return type:

[_Future_](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.jit.Future")
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]

Checkpointing of Communication Hooks[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#checkpointing-of-communication-hooks "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

A stateful communication hook can be saved as a part of model checkpointing to enable trainer restarts. To make a hook serializable, `__setstate__` and `__getstate__` should be defined.

Warning

`__getstate__` should exclude non-serializable attributes from a returned dictionary.

Warning

`__setstate__` should properly initialize non-serializable attributes, excluded from a provided `state`.

[`PowerSGDState`](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.powerSGD_hook.PowerSGDState "torch.distributed.algorithms.ddp_comm_hooks.powerSGD_hook.PowerSGDState")
 has `__setstate__` and `__getstate__` implemented and can be used as a reference.

_class_ torch.distributed.algorithms.ddp\_comm\_hooks.powerSGD\_hook.PowerSGDState[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/ddp_comm_hooks/powerSGD_hook.py#L122)

\_\_getstate\_\_()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/ddp_comm_hooks/powerSGD_hook.py#L276)
[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.powerSGD_hook.PowerSGDState.__getstate__ "Link to this definition")

Return a `Dict[str, Any]` which will be pickled and saved.

`process_group` is not serializable and excluded from a returned state.

\_\_setstate\_\_(_state_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/ddp_comm_hooks/powerSGD_hook.py#L292)
[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#torch.distributed.algorithms.ddp_comm_hooks.powerSGD_hook.PowerSGDState.__setstate__ "Link to this definition")

Take a provided `state` and set to this `PowerSGDState` instance.

`process_group` is set to default.

Here is a simple, end-to-end example of saving and reloading PowerSGD state and hook.

import os
import sys
import tempfile
import torch
import torch.distributed as dist
import torch.nn as nn
import torch.optim as optim
import torch.multiprocessing as mp

from torch.nn.parallel import DistributedDataParallel
from torch.distributed.algorithms.ddp\_comm\_hooks import powerSGD\_hook as powerSGD

class SimpleModel(nn.Module):
    def \_\_init\_\_(self):
        super().\_\_init\_\_()
        self.fc1 \= nn.Linear(24,24)
        self.relu \= nn.ReLU()
        self.fc2 \= nn.Linear(24,12)

    def forward(self, x):
        return self.fc2(self.relu(self.fc1(x)))

def setup(rank, world\_size):
    os.environ\['MASTER\_ADDR'\] \= 'localhost'
    os.environ\['MASTER\_PORT'\] \= '12355'

    \# initialize the process group
    dist.init\_process\_group("nccl", rank\=rank, world\_size\=world\_size)

def cleanup():
    dist.destroy\_process\_group()

def run\_demo(demo\_fn, world\_size):
    mp.spawn(
        demo\_fn,
        args\=(world\_size,),
        nprocs\=world\_size,
        join\=True)

def demo\_serialization(rank, world\_size):
    setup(rank, world\_size)

    CHECKPOINT \= tempfile.gettempdir() + "/checkpoint.pt"

    model \= SimpleModel().to(rank)
    ddp\_model \= DistributedDataParallel(model, device\_ids\=\[rank\])

    powersgd\_hook \= powerSGD.powerSGD\_hook
    powersgd\_state \= powerSGD.PowerSGDState(process\_group\=None)

    optimizer \= optim.SGD(ddp\_model.parameters(), lr\=0.001)
    ddp\_model.register\_comm\_hook(powersgd\_state, powersgd\_hook)

    state \= {
        'state\_dict': ddp\_model.state\_dict(),
        'comm\_hook': powersgd\_hook,
        'comm\_hook\_state': powersgd\_state}

    if rank \== 0:
        torch.save(state, CHECKPOINT)

    dist.barrier()
    map\_location \= {'cuda:%d' % 0: 'cuda:%d' % rank}
    checkpoint \= torch.load(CHECKPOINT, map\_location\=map\_location)

    new\_ddp\_model \= DistributedDataParallel(SimpleModel().to(rank), device\_ids\=\[rank\])
    new\_ddp\_model.load\_state\_dict(checkpoint\['state\_dict'\])
    powersgd\_hook \= checkpoint\['comm\_hook'\]
    powersgd\_state \= checkpoint\['comm\_hook\_state'\]

    new\_ddp\_model.register\_comm\_hook(powersgd\_state, powersgd\_hook)

    if rank \== 0:
        os.remove(CHECKPOINT)

    cleanup()

if \_\_name\_\_ \== "\_\_main\_\_":
    n\_gpus \= torch.cuda.device\_count()
    assert n\_gpus \>= 2, f"Requires at least 2 GPUs to run, but got {n\_gpus}"
    world\_size \= n\_gpus
    run\_demo(demo\_serialization, world\_size)

Copy to clipboard

Acknowledgements[#](https://docs.pytorch.org/docs/2.15/ddp_comm_hooks.html#acknowledgements "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

Many thanks to PowerSGD paper author **Thijs Vogels** for the code review on PowerSGD communication hook, as well as the [comparison experiments](https://observablehq.com/@tvogels/powersgd-benchmark)
, which show that the performance of PowerSGD communication hook is on par with the implementation in the original [paper](https://arxiv.org/abs/1905.13727)
.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/ddp_comm_hooks.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/ddp_comm_hooks.md.txt)

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