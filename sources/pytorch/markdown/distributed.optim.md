Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/distributed.optim.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/distributed.optim.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/distributed.optim.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/distributed.optim.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/distributed.optim.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/distributed.optim.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/distributed.optim.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/distributed.optim.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/distributed.optim.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/distributed.optim.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/distributed.optim.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/distributed.optim.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/distributed.optim.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/distributed.optim.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/distributed.optim.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/distributed.optim.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/distributed.optim.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/distributed.optim.html)
[v1.13](https://docs.pytorch.org/docs/1.13/distributed.optim.html)
[v1.12](https://docs.pytorch.org/docs/1.12/distributed.optim.html)
[v1.11](https://docs.pytorch.org/docs/1.11/distributed.optim.html)
[v1.10](https://docs.pytorch.org/docs/1.10/distributed.optim.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/distributed.optim.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/distributed.optim.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/distributed.optim.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/distributed.optim.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/distributed.optim.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/distributed.optim.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/distributed.optim.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/distributed.optim.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/distributed.optim.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/distributed.optim.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/distributed.optim.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/distributed.optim.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/distributed.optim.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/distributed.optim.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/distributed.optim.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/distributed.optim.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/distributed.optim.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/distributed.optim.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/distributed.optim.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/distributed.optim.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/distributed.optim.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/distributed.optim.html)

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

Distributed Optimizers[#](https://docs.pytorch.org/docs/2.15/distributed.optim.html#distributed-optimizers "Link to this heading")

===================================================================================================================================

Created On: Mar 01, 2021 | Last Updated On: May 11, 2026

Warning

Distributed optimizer is not currently supported when using CUDA tensors

[`torch.distributed.optim`](https://docs.pytorch.org/docs/2.15/distributed.optim.html#module-torch.distributed.optim "torch.distributed.optim")
 exposes DistributedOptimizer, which takes a list of remote parameters (`RRef`) and runs the optimizer locally on the workers where the parameters live. The distributed optimizer can use any of the local optimizer [Base class](https://docs.pytorch.org/docs/2.15/optim.html#optimizer-algorithms)
 to apply the gradients on each worker.

_class_ torch.distributed.optim.DistributedOptimizer(_optimizer\_class_, _params\_rref_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/optim/optimizer.py#L98)
[#](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.DistributedOptimizer "Link to this definition")

DistributedOptimizer takes remote references to parameters scattered across workers and applies the given optimizer locally for each parameter.

This class uses [`get_gradients()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.autograd.get_gradients "torch.distributed.autograd.get_gradients")
 in order to retrieve the gradients for specific parameters.

Concurrent calls to [`step()`](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.DistributedOptimizer.step "torch.distributed.optim.DistributedOptimizer.step")
, either from the same or different clients, will be serialized on each worker – as each worker’s optimizer can only work on one set of gradients at a time. However, there is no guarantee that the full forward-backward-optimizer sequence will execute for one client at a time. This means that the gradients being applied may not correspond to the latest forward pass executed on a given worker. Also, there is no guaranteed ordering across workers.

DistributedOptimizer uses a functional optimizer internally when one is available for the given `optimizer_class`, so that optimizer updates are not blocked by the Python Global Interpreter Lock (GIL) in the case of multithreaded training (e.g. Distributed Model Parallel). This feature is currently enabled for most optimizers.

Parameters:

*   **optimizer\_class** ([_optim.Optimizer_](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.Optimizer")
    ) – the class of optimizer to instantiate on each worker.
    
*   **params\_rref** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[__RRef__\]_) – list of RRefs to local or remote parameters to optimize.
    
*   **args** – arguments to pass to the optimizer constructor on each worker.
    
*   **kwargs** – arguments to pass to the optimizer constructor on each worker.
    

Example::

\>>> import torch.distributed.autograd as dist\_autograd
\>>> import torch.distributed.rpc as rpc
\>>> from torch import optim
\>>> from torch.distributed.optim import DistributedOptimizer
\>>>
\>>> with dist\_autograd.context() as context\_id:
\>>>   \# Forward pass.
\>>>   rref1 \= rpc.remote("worker1", torch.add, args\=(torch.ones(2), 3))
\>>>   rref2 \= rpc.remote("worker1", torch.add, args\=(torch.ones(2), 1))
\>>>   loss \= rref1.to\_here() + rref2.to\_here()
\>>>
\>>>   \# Backward pass.
\>>>   dist\_autograd.backward(context\_id, \[loss.sum()\])
\>>>
\>>>   \# Optimizer.
\>>>   dist\_optim \= DistributedOptimizer(
\>>>      optim.SGD,
\>>>      \[rref1, rref2\],
\>>>      lr\=0.05,
\>>>   )
\>>>   dist\_optim.step(context\_id)

Copy to clipboard

step(_context\_id_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/optim/optimizer.py#L192)
[#](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.DistributedOptimizer.step "Link to this definition")

Performs a single optimization step.

This will call [`torch.optim.Optimizer.step()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Optimizer.step.html#torch.optim.Optimizer.step "torch.optim.Optimizer.step")
 on each worker containing parameters to be optimized, and will block until all workers return. The provided `context_id` will be used to retrieve the corresponding [`context`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.autograd.context "torch.distributed.autograd.context")
 that contains the gradients that should be applied to the parameters.

Parameters:

**context\_id** – the autograd context id for which we should run the optimizer step.

_class_ torch.distributed.optim.PostLocalSGDOptimizer(_optim_, _averager_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/optim/post_localSGD_optimizer.py#L8)
[#](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.PostLocalSGDOptimizer "Link to this definition")

Wraps an arbitrary [`torch.optim.Optimizer`](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.Optimizer")
 and runs [post-local SGD](https://arxiv.org/abs/1808.07217)
, This optimizer runs local optimizer at every step. After the warm-up stage, it averages parameters periodically after the local optimizer is applied.

Parameters:

*   **optim** ([_Optimizer_](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.optimizer.Optimizer")
    ) – The local optimizer.
    
*   **averager** (_ModelAverager_) – A model averager instance to run post-localSGD algorithm.
    

Example:

\>>> import torch
\>>> import torch.distributed as dist
\>>> import torch.distributed.algorithms.model\_averaging.averagers as averagers
\>>> import torch.nn as nn
\>>> from torch.distributed.optim import PostLocalSGDOptimizer
\>>> from torch.distributed.algorithms.ddp\_comm\_hooks.post\_localSGD\_hook import (
\>>>   PostLocalSGDState,
\>>>   post\_localSGD\_hook,
\>>> )
\>>>
\>>> model \= nn.parallel.DistributedDataParallel(
\>>>    module, device\_ids\=\[rank\], output\_device\=rank
\>>> )
\>>>
\>>> \# Register a post-localSGD communication hook.
\>>> state \= PostLocalSGDState(process\_group\=None, subgroup\=None, start\_localSGD\_iter\=100)
\>>> model.register\_comm\_hook(state, post\_localSGD\_hook)
\>>>
\>>> \# Create a post-localSGD optimizer that wraps a local optimizer.
\>>> \# Note that \`\`warmup\_steps\`\` used in \`\`PostLocalSGDOptimizer\`\` must be the same as
\>>> \# \`\`start\_localSGD\_iter\`\` used in \`\`PostLocalSGDState\`\`.
\>>> local\_optim \= torch.optim.SGD(params\=model.parameters(), lr\=0.01)
\>>> opt \= PostLocalSGDOptimizer(
\>>>     optim\=local\_optim,
\>>>     averager\=averagers.PeriodicModelAverager(period\=4, warmup\_steps\=100)
\>>> )
\>>>
\>>> \# In the first 100 steps, DDP runs global gradient averaging at every step.
\>>> \# After 100 steps, DDP runs gradient averaging within each subgroup (intra-node by default),
\>>> \# and post-localSGD optimizer runs global model averaging every 4 steps after applying the local optimizer.
\>>> for step in range(0, 200):
\>>>    opt.zero\_grad()
\>>>    loss \= loss\_fn(output, labels)
\>>>    loss.backward()
\>>>    opt.step()

Copy to clipboard

load\_state\_dict(_state\_dict_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/optim/post_localSGD_optimizer.py#L80)
[#](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.PostLocalSGDOptimizer.load_state_dict "Link to this definition")

This is the same as [`torch.optim.Optimizer`](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.Optimizer")
 [`load_state_dict()`](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.PostLocalSGDOptimizer.load_state_dict "torch.distributed.optim.PostLocalSGDOptimizer.load_state_dict")
, but also restores model averager’s step value to the one saved in the provided `state_dict`.

If there is no `"step"` entry in `state_dict`, it will raise a warning and initialize the model averager’s step to 0.

state\_dict()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/optim/post_localSGD_optimizer.py#L70)
[#](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.PostLocalSGDOptimizer.state_dict "Link to this definition")

This is the same as [`torch.optim.Optimizer`](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.Optimizer")
 [`state_dict()`](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.PostLocalSGDOptimizer.state_dict "torch.distributed.optim.PostLocalSGDOptimizer.state_dict")
, but adds an extra entry to record model averager’s step to the checkpoint to ensure reload does not cause unnecessary warm up again.

step()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/optim/post_localSGD_optimizer.py#L100)
[#](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.PostLocalSGDOptimizer.step "Link to this definition")

Performs a single optimization step (parameter update).

_class_ torch.distributed.optim.ZeroRedundancyOptimizer(_params_, _optimizer\_class_, _process\_group\=None_, _parameters\_as\_bucket\_view\=False_, _overlap\_with\_ddp\=False_, _\*\*defaults_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/optim/zero_redundancy_optimizer.py#L290)
[#](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.ZeroRedundancyOptimizer "Link to this definition")

Wrap an arbitrary [`optim.Optimizer`](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.Optimizer")
 and shard its states across ranks in the group.

The sharing is done as described by [ZeRO](https://arxiv.org/abs/1910.02054)
.

The local optimizer instance in each rank is only responsible for updating approximately `1 / world_size` parameters and hence only needs to keep `1 / world_size` optimizer states. After parameters are updated locally, each rank will broadcast its parameters to all other peers to keep all model replicas in the same state. `ZeroRedundancyOptimizer` can be used in conjunction with [`torch.nn.parallel.DistributedDataParallel`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")
 to reduce per-rank peak memory consumption.

`ZeroRedundancyOptimizer` uses a sorted-greedy algorithm to pack a number of parameters at each rank. Each parameter belongs to a single rank and is not divided among ranks. The partition is arbitrary and might not match the parameter registration or usage order.

Parameters:

**params** (`Iterable`) – an `Iterable` of [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 s or [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
 s giving all parameters, which will be sharded across ranks.

Keyword Arguments:

*   **optimizer\_class** (`torch.nn.Optimizer`) – the class of the local optimizer.
    
*   **process\_group** (`ProcessGroup`, optional) – `torch.distributed` `ProcessGroup` (default: `dist.group.WORLD` initialized by [`torch.distributed.init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")
    ).
    
*   **parameters\_as\_bucket\_view** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – if `True`, parameters are packed into buckets to speed up communication, and `param.data` fields point to bucket views at different offsets; if `False`, each individual parameter is communicated separately, and each `params.data` stays intact (default: `False`).
    
*   **overlap\_with\_ddp** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – if `True`, [`step()`](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.ZeroRedundancyOptimizer.step "torch.distributed.optim.ZeroRedundancyOptimizer.step")
     is overlapped with `DistributedDataParallel` ‘s gradient synchronization; this requires (1) either a functional optimizer for the `optimizer_class` argument or one with a functional equivalent and (2) registering a DDP communication hook constructed from one of the functions in `ddp_zero_hook.py`; parameters are packed into buckets matching those in `DistributedDataParallel`, meaning that the `parameters_as_bucket_view` argument is ignored. If `False`, [`step()`](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.ZeroRedundancyOptimizer.step "torch.distributed.optim.ZeroRedundancyOptimizer.step")
     runs disjointly after the backward pass (per normal). (default: `False`)
    
*   **\*\*defaults** – any trailing arguments, which are forwarded to the local optimizer.
    

Example:

\>>> import torch.nn as nn
\>>> from torch.distributed.optim import ZeroRedundancyOptimizer
\>>> from torch.nn.parallel import DistributedDataParallel as DDP
\>>> model \= nn.Sequential(\*\[nn.Linear(2000, 2000).to(rank) for \_ in range(20)\])
\>>> ddp \= DDP(model, device\_ids\=\[rank\])
\>>> opt \= ZeroRedundancyOptimizer(
\>>>     ddp.parameters(),
\>>>     optimizer\_class\=torch.optim.Adam,
\>>>     lr\=0.01
\>>> )
\>>> ddp(inputs).sum().backward()
\>>> opt.step()

Copy to clipboard

Warning

Currently, `ZeroRedundancyOptimizer` requires that all of the passed-in parameters are the same dense type.

Warning

If you pass `overlap_with_ddp=True`, be wary of the following: Given the way that overlapping `DistributedDataParallel` with [`ZeroRedundancyOptimizer`](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.ZeroRedundancyOptimizer "torch.distributed.optim.ZeroRedundancyOptimizer")
 is currently implemented, the first two or three training iterations do not perform parameter updates in the optimizer step, depending on if `static_graph=False` or `static_graph=True`, respectively. This is because it needs information about the gradient bucketing strategy used by `DistributedDataParallel`, which is not finalized until the second forward pass if `static_graph=False` or until the third forward pass if `static_graph=True`. To adjust for this, one option is to prepend dummy inputs.

Warning

ZeroRedundancyOptimizer is experimental and subject to change.

add\_param\_group(_param\_group_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/optim/zero_redundancy_optimizer.py#L467)
[#](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.ZeroRedundancyOptimizer.add_param_group "Link to this definition")

Add a parameter group to the `Optimizer` ‘s `param_groups`.

This can be useful when fine tuning a pre-trained network, as frozen layers can be made trainable and added to the `Optimizer` as training progresses.

Parameters:

**param\_group** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
) – specifies the parameters to be optimized and group-specific optimization options.

Warning

This method handles updating the shards on all partitions but needs to be called on all ranks. Calling this on a subset of the ranks will cause the training to hang because communication primitives are called depending on the managed parameters and expect all the ranks to participate on the same set of parameters.

consolidate\_state\_dict(_to\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/optim/zero_redundancy_optimizer.py#L513)
[#](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.ZeroRedundancyOptimizer.consolidate_state_dict "Link to this definition")

Consolidate a list of `state_dict` s (one per rank) on the target rank.

Parameters:

**to** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
) – the rank that receives the optimizer states (default: 0).

Raises:

[**RuntimeError**](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "(in Python v3.15)")
 – if `overlap_with_ddp=True` and this method is called before this [`ZeroRedundancyOptimizer`](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.ZeroRedundancyOptimizer "torch.distributed.optim.ZeroRedundancyOptimizer")
 instance has been fully initialized, which happens once `DistributedDataParallel` gradient buckets have been rebuilt.

Warning

This needs to be called on all ranks.

_property_ join\_device_: [device](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
_[#](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.ZeroRedundancyOptimizer.join_device "Link to this definition")

Return default device.

join\_hook(_\*\*\_kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/optim/zero_redundancy_optimizer.py#L1155)
[#](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.ZeroRedundancyOptimizer.join_hook "Link to this definition")

Return the ZeRO join hook.

It enables training on uneven inputs by shadowing the collective communications in the optimizer step.

Gradients must be properly set before this hook is called.

Parameters:

**kwargs** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
) – a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
 containing any keyword arguments to modify the behavior of the join hook at run time; all `Joinable` instances sharing the same join context manager are forwarded the same value for `kwargs`.

Return type:

[_JoinHook_](https://docs.pytorch.org/docs/2.15/distributed.algorithms.join.html#torch.distributed.algorithms.JoinHook "torch.distributed.algorithms.join.JoinHook")

This hook does not support any keyword arguments; i.e. `kwargs` is unused.

_property_ join\_process\_group_: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.ZeroRedundancyOptimizer.join_process_group "Link to this definition")

Return process group.

load\_state\_dict(_state\_dict_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/optim/zero_redundancy_optimizer.py#L1185)
[#](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.ZeroRedundancyOptimizer.load_state_dict "Link to this definition")

Load the state pertaining to the given rank from the input `state_dict`, updating the local optimizer as needed.

Parameters:

**state\_dict** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
) – optimizer state; should be an object returned from a call to [`state_dict()`](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.ZeroRedundancyOptimizer.state_dict "torch.distributed.optim.ZeroRedundancyOptimizer.state_dict")
.

Raises:

[**RuntimeError**](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "(in Python v3.15)")
 – if `overlap_with_ddp=True` and this method is called before this [`ZeroRedundancyOptimizer`](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.ZeroRedundancyOptimizer "torch.distributed.optim.ZeroRedundancyOptimizer")
 instance has been fully initialized, which happens once `DistributedDataParallel` gradient buckets have been rebuilt.

state\_dict()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/optim/zero_redundancy_optimizer.py#L1223)
[#](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.ZeroRedundancyOptimizer.state_dict "Link to this definition")

Return the last global optimizer state known to this rank.

Raises:

[**RuntimeError**](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "(in Python v3.15)")
 – if `overlap_with_ddp=True` and this method is called before this [`ZeroRedundancyOptimizer`](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.ZeroRedundancyOptimizer "torch.distributed.optim.ZeroRedundancyOptimizer")
 instance has been fully initialized, which happens once `DistributedDataParallel` gradient buckets have been rebuilt; or if this method is called without a preceding call to [`consolidate_state_dict()`](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.ZeroRedundancyOptimizer.consolidate_state_dict "torch.distributed.optim.ZeroRedundancyOptimizer.consolidate_state_dict")
.

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\]

step(_closure\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/optim/zero_redundancy_optimizer.py#L1124)
[#](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.ZeroRedundancyOptimizer.step "Link to this definition")

Perform a single optimizer step and sync parameters across all ranks.

Parameters:

**closure** (_Callable_) – a closure that re-evaluates the model and returns the loss; optional for most optimizers.

Returns:

Optional loss depending on the underlying local optimizer.

Return type:

[float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
 | None

Note

Any extra parameters are passed to the base optimizer as-is.

torch.distributed.optim.utils.register\_functional\_optim(_key_, _optim_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/optim/utils.py#L31)
[#](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.utils.register_functional_optim "Link to this definition")

Interface to insert a new functional optimizer to functional\_optim\_map. `fn_optim_key` and `fn_optimizer` are user defined. The optimizer and key need not be of [`torch.optim.Optimizer`](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.Optimizer")
 (e.g. for custom optimizers).

Example:

\>>> \# import the new functional optimizer
\>>> from xyz import fn\_optimizer
\>>> from torch.distributed.optim.utils import register\_functional\_optim
\>>> fn\_optim\_key \= "XYZ\_optim"
\>>> register\_functional\_optim(fn\_optim\_key, fn\_optimizer)

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/distributed.optim.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/distributed.optim.md.txt)

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