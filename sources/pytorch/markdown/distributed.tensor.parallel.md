Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/distributed.tensor.parallel.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/distributed.tensor.parallel.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/distributed.tensor.parallel.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/distributed.tensor.parallel.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/distributed.tensor.parallel.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/distributed.tensor.parallel.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/distributed.tensor.parallel.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/distributed.tensor.parallel.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/distributed.tensor.parallel.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/distributed.tensor.parallel.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/distributed.tensor.parallel.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/distributed.tensor.parallel.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/distributed.tensor.parallel.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/distributed.tensor.parallel.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/distributed.tensor.parallel.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/distributed.tensor.parallel.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/distributed.tensor.parallel.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/distributed.tensor.parallel.html)
[v1.13](https://docs.pytorch.org/docs/1.13/distributed.tensor.parallel.html)
[v1.12](https://docs.pytorch.org/docs/1.12/distributed.tensor.parallel.html)
[v1.11](https://docs.pytorch.org/docs/1.11/distributed.tensor.parallel.html)
[v1.10](https://docs.pytorch.org/docs/1.10/distributed.tensor.parallel.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/distributed.tensor.parallel.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/distributed.tensor.parallel.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/distributed.tensor.parallel.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/distributed.tensor.parallel.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/distributed.tensor.parallel.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/distributed.tensor.parallel.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/distributed.tensor.parallel.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/distributed.tensor.parallel.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/distributed.tensor.parallel.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/distributed.tensor.parallel.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/distributed.tensor.parallel.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/distributed.tensor.parallel.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/distributed.tensor.parallel.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/distributed.tensor.parallel.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/distributed.tensor.parallel.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/distributed.tensor.parallel.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/distributed.tensor.parallel.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/distributed.tensor.parallel.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/distributed.tensor.parallel.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/distributed.tensor.parallel.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/distributed.tensor.parallel.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/distributed.tensor.parallel.html)

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

Tensor Parallelism - torch.distributed.tensor.parallel[#](https://docs.pytorch.org/docs/2.15/distributed.tensor.parallel.html#tensor-parallelism-torch-distributed-tensor-parallel "Link to this heading")

===========================================================================================================================================================================================================

Created On: Jun 13, 2025 | Last Updated On: May 12, 2026

Tensor Parallelism(TP) is built on top of the PyTorch DistributedTensor ([DTensor](https://github.com/pytorch/pytorch/blob/main/torch/distributed/tensor/README.md)
) and provides different parallelism styles: Colwise, Rowwise, and Sequence Parallelism.

Warning

Tensor Parallelism APIs are experimental and subject to change.

The entrypoint to parallelize your `nn.Module` using Tensor Parallelism is:

torch.distributed.tensor.parallel.parallelize\_module(_module_, _device\_mesh\=None_, _parallelize\_plan\=None_, _\*_, _src\_data\_rank\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/tensor/parallel/api.py#L14)
[#](https://docs.pytorch.org/docs/2.15/distributed.tensor.parallel.html#torch.distributed.tensor.parallel.parallelize_module "Link to this definition")

Apply Tensor Parallelism in PyTorch by parallelizing modules or sub-modules based on a user-specified plan.

We parallelize module or sub\_modules based on a parallelize\_plan. The parallelize\_plan contains `ParallelStyle`, which indicates how user wants the module or sub\_module to be parallelized.

User can also specify different parallel style per module fully qualified name (FQN).

Note that `parallelize_module` only accepts a 1-D `DeviceMesh`, if you have a 2-D or N-D `DeviceMesh`, slice the DeviceMesh to a 1-D sub DeviceMesh first then pass to this API(i.e. `device_mesh["tp"]`)

Parameters:

*   **module** (`nn.Module`) – Module to be parallelized.
    
*   **device\_mesh** (`DeviceMesh`, optional) – Object which describes the mesh topology of devices for the DTensor. If not specified, the call must be under a DeviceMesh context.
    
*   **parallelize\_plan** (Union\[`ParallelStyle`, Dict\[str, `ParallelStyle`\]\], optional) – The plan used to parallelize the module. It can be either a `ParallelStyle` object which contains how we prepare input/output for Tensor Parallelism or it can be a dict of module FQN and its corresponding `ParallelStyle` object. If not specified, the call will do nothing at the moment.
    

Keyword Arguments:

**src\_data\_rank** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_,_ _optional_) – the rank of the source data for the logical/global tensor, it is used by `distribute_tensor()` to scatter/broadcast the shards/replicas to other ranks. By default, we use `group_rank=0` on each DeviceMesh dimension as the source data to preserve the single-device semantic. If passing `None` explicitly, [`parallelize_module()`](https://docs.pytorch.org/docs/2.15/distributed.tensor.parallel.html#torch.distributed.tensor.parallel.parallelize_module "torch.distributed.tensor.parallel.parallelize_module")
 simply uses its local data instead of trying to preserve the single-device semantic via scatter/broadcast. Default: 0

Returns:

A `nn.Module` object parallelized.

Return type:

[_Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.modules.module.Module")

Example::

\>>> from torch.distributed.tensor.parallel import parallelize\_module, ColwiseParallel
\>>> from torch.distributed.device\_mesh import init\_device\_mesh
\>>>
\>>> \# Define the module.
\>>> m \= Model(...)
\>>> tp\_mesh \= init\_device\_mesh("cuda", (8,))
\>>> m \= parallelize\_module(m, tp\_mesh, {"w1": ColwiseParallel(), "w2": RowwiseParallel()})
\>>>

Copy to clipboard

Note

For complex module architecture like Attention, MLP layers, we recommend composing different ParallelStyles together (i.e. `ColwiseParallel` and `RowwiseParallel`) and pass as a parallelize\_plan, to achieve the desired sharding computation.

torch.distributed.tensor.parallel.api.parallelize\_module(_module_, _device\_mesh\=None_, _parallelize\_plan\=None_, _\*_, _src\_data\_rank\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/tensor/parallel/api.py#L14)
[#](https://docs.pytorch.org/docs/2.15/distributed.tensor.parallel.html#torch.distributed.tensor.parallel.api.parallelize_module "Link to this definition")

Apply Tensor Parallelism in PyTorch by parallelizing modules or sub-modules based on a user-specified plan.

We parallelize module or sub\_modules based on a parallelize\_plan. The parallelize\_plan contains `ParallelStyle`, which indicates how user wants the module or sub\_module to be parallelized.

User can also specify different parallel style per module fully qualified name (FQN).

Note that `parallelize_module` only accepts a 1-D `DeviceMesh`, if you have a 2-D or N-D `DeviceMesh`, slice the DeviceMesh to a 1-D sub DeviceMesh first then pass to this API(i.e. `device_mesh["tp"]`)

Parameters:

*   **module** (`nn.Module`) – Module to be parallelized.
    
*   **device\_mesh** (`DeviceMesh`, optional) – Object which describes the mesh topology of devices for the DTensor. If not specified, the call must be under a DeviceMesh context.
    
*   **parallelize\_plan** (Union\[`ParallelStyle`, Dict\[str, `ParallelStyle`\]\], optional) – The plan used to parallelize the module. It can be either a `ParallelStyle` object which contains how we prepare input/output for Tensor Parallelism or it can be a dict of module FQN and its corresponding `ParallelStyle` object. If not specified, the call will do nothing at the moment.
    

Keyword Arguments:

**src\_data\_rank** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_,_ _optional_) – the rank of the source data for the logical/global tensor, it is used by `distribute_tensor()` to scatter/broadcast the shards/replicas to other ranks. By default, we use `group_rank=0` on each DeviceMesh dimension as the source data to preserve the single-device semantic. If passing `None` explicitly, [`parallelize_module()`](https://docs.pytorch.org/docs/2.15/distributed.tensor.parallel.html#torch.distributed.tensor.parallel.api.parallelize_module "torch.distributed.tensor.parallel.api.parallelize_module")
 simply uses its local data instead of trying to preserve the single-device semantic via scatter/broadcast. Default: 0

Returns:

A `nn.Module` object parallelized.

Return type:

[_Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.modules.module.Module")

Example::

\>>> from torch.distributed.tensor.parallel import parallelize\_module, ColwiseParallel
\>>> from torch.distributed.device\_mesh import init\_device\_mesh
\>>>
\>>> \# Define the module.
\>>> m \= Model(...)
\>>> tp\_mesh \= init\_device\_mesh("cuda", (8,))
\>>> m \= parallelize\_module(m, tp\_mesh, {"w1": ColwiseParallel(), "w2": RowwiseParallel()})
\>>>

Copy to clipboard

Note

For complex module architecture like Attention, MLP layers, we recommend composing different ParallelStyles together (i.e. `ColwiseParallel` and `RowwiseParallel`) and pass as a parallelize\_plan, to achieve the desired sharding computation.

Tensor Parallelism supports the following parallel styles:

_class_ torch.distributed.tensor.parallel.ColwiseParallel(_\*_, _input\_layouts\=None_, _output\_layouts\=None_, _use\_local\_output\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/tensor/parallel/style.py#L45)
[#](https://docs.pytorch.org/docs/2.15/distributed.tensor.parallel.html#torch.distributed.tensor.parallel.ColwiseParallel "Link to this definition")

Partition a compatible nn.Module in a column-wise fashion. Currently supports nn.Linear and nn.Embedding. Users can compose it together with RowwiseParallel to achieve the sharding of more complicated modules. (i.e. MLP, Attention)

Keyword Arguments:

*   **input\_layouts** ([_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")
    _,_ _optional_) – The DTensor layout of input tensor for the nn.Module, this is used to annotate the input tensor to become a DTensor. If not specified, we assume the input tensor to be replicated.
    
*   **output\_layouts** ([_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")
    _,_ _optional_) – The DTensor layout of the output for the nn.Module, this is used to ensure the output of the nn.Module with the user desired layout. If not specified, the output tensor is sharded on the last dimension.
    
*   **use\_local\_output** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Whether to use local [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     instead of `DTensor` for the module output, default: True.
    

Returns:

A `ParallelStyle` object that represents Colwise sharding of the nn.Module.

Example::

\>>> from torch.distributed.tensor.parallel import parallelize\_module, ColwiseParallel
\>>> from torch.distributed.device\_mesh import init\_device\_mesh
\>>> ...
\>>> m \= Model(...)  \# m is a nn.Module that contains a "w1" nn.Linear submodule
\>>> tp\_mesh \= init\_device\_mesh("cuda", (8,))
\>>>
\>>> \# By default, the input of the "w1" Linear will be converted to Replicated DTensor
\>>> \# and the output of "w1" will return :class:\`torch.Tensor\` that shards on the last dim.
\>>>
\>>> sharded\_mod \= parallelize\_module(m, tp\_mesh, {"w1": ColwiseParallel()})
\>>> ...

Copy to clipboard

Note

By default `ColwiseParallel` output is sharded on the last dimension if the `output_layouts` not specified, if there’re operators that require specific tensor shape (i.e. before the paired `RowwiseParallel`), keep in mind that if the output is sharded the operator might need to be adjusted to the sharded size.

_class_ torch.distributed.tensor.parallel.RowwiseParallel(_\*_, _input\_layouts\=None_, _output\_layouts\=None_, _use\_local\_output\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/tensor/parallel/style.py#L186)
[#](https://docs.pytorch.org/docs/2.15/distributed.tensor.parallel.html#torch.distributed.tensor.parallel.RowwiseParallel "Link to this definition")

Partition a compatible nn.Module in a row-wise fashion. Currently supports nn.Linear and nn.Embedding. Users can compose it with ColwiseParallel to achieve the sharding of more complicated modules. (i.e. MLP, Attention)

Keyword Arguments:

*   **input\_layouts** ([_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")
    _,_ _optional_) – The DTensor layout of input tensor for the nn.Module, this is used to annotate the input tensor to become a DTensor. If not specified, we assume the input tensor to be sharded on the last dimension.
    
*   **output\_layouts** ([_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")
    _,_ _optional_) – The DTensor layout of the output for the nn.Module, this is used to ensure the output of the nn.Module with the user desired layout. If not specified, the output tensor is replicated.
    
*   **use\_local\_output** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Whether to use local [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     instead of `DTensor` for the module output, default: True.
    

Returns:

A `ParallelStyle` object that represents Rowwise sharding of the nn.Module.

Example::

\>>> from torch.distributed.tensor.parallel import parallelize\_module, RowwiseParallel
\>>> from torch.distributed.device\_mesh import init\_device\_mesh
\>>> ...
\>>> m \= Model(...)  \# m is a nn.Module that contains a "w2" nn.Linear submodule
\>>> tp\_mesh \= init\_device\_mesh("cuda", (8,))
\>>>
\>>> \# By default, the input of the "w2" Linear will be converted to DTensor that shards on the last dim
\>>> \# and the output of "w2" will return a replicated :class:\`torch.Tensor\`.
\>>>
\>>> sharded\_mod \= parallelize\_module(m, tp\_mesh, {"w2": RowwiseParallel()}),
\>>> ...

Copy to clipboard

_class_ torch.distributed.tensor.parallel.SequenceParallel(_\*_, _sequence\_dim\=1_, _use\_local\_output\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/tensor/parallel/style.py#L339)
[#](https://docs.pytorch.org/docs/2.15/distributed.tensor.parallel.html#torch.distributed.tensor.parallel.SequenceParallel "Link to this definition")

SequenceParallel replicates a compatible `nn.Module` parameters and runs the sharded computation with input sharded on the sequence dimension. This currently supports `nn.LayerNorm`, `nn.Dropout`, and the [RMSNorm python implementation](https://github.com/facebookresearch/llama/blob/main/llama/model.py#L34)

This style implements the operation that is described in the paper [Reducing Activation Recomputation in Large Transformer Models](https://arxiv.org/abs/2205.05198)

If the input passed in to this `nn.Module` is a [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
, it assumes that the input is already sharded on the sequence dimension and converts the input to a `DTensor` sharded on the sequence dimension. If the input passed in to this `nn.Module` is already a `DTensor` but is not sharded on the sequence dimension, it would redistribute the input to be sharded on the sequence dimension.

The output of the `nn.Module` will be sharded on the sequence dimension.

Keyword Arguments:

*   **sequence\_dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – The sequence dimension of the input tensor for the `nn.Module`, this is used to annotate the input tensor to become a DTensor that is sharded on the sequence dimension, default: 1.
    
*   **use\_local\_output** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Whether to use local [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     instead of `DTensor` for the module output, default: False.
    

Returns:

A `ParallelStyle` object that represents Sequence Parallel of the `nn.Module`.

Example::

\>>> from torch.distributed.tensor.parallel import parallelize\_module, SequenceParallel
\>>> from torch.distributed.device\_mesh import init\_device\_mesh
\>>> ...
\>>> m \= Model(...)  \# m is a nn.Module that contains a "norm" nn.LayerNorm submodule
\>>> tp\_mesh \= init\_device\_mesh("cuda", (8,))
\>>>
\>>> \# By default, the input of the "norm" will be converted to DTensor that shards on the sequence dim
\>>> \# and the output of "norm" will return a sharded on sequence dimension :class:\`DTensor\`.
\>>>
\>>> sharded\_mod \= parallelize\_module(m, tp\_mesh, {"norm": SequenceParallel()}),
\>>> ...

Copy to clipboard

Note

SequenceParallel style assumes ones initialization if there are weights in the nn.Module (i.e. `nn.LayerNorm` or `RMSNorm`, and they by default have ones initialization). If you have custom inits for the weights on those modules, you need to broadcast the weights before/after parallelizing to ensure that they are replicated.

To simply configure the nn.Module’s inputs and outputs with DTensor layouts and perform necessary layout redistributions, without distribute the module parameters to DTensors, the following `ParallelStyle` s can be used in the `parallelize_plan` when calling `parallelize_module`:

_class_ torch.distributed.tensor.parallel.PrepareModuleInput(_\*_, _input\_layouts\=None_, _desired\_input\_layouts\=None_, _input\_kwarg\_layouts\=None_, _desired\_input\_kwarg\_layouts\=None_, _use\_local\_output\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/tensor/parallel/style.py#L442)
[#](https://docs.pytorch.org/docs/2.15/distributed.tensor.parallel.html#torch.distributed.tensor.parallel.PrepareModuleInput "Link to this definition")

Configure the nn.Module’s inputs to convert the input tensors of the nn.Module to DTensors at runtime according to `input_layouts`, and perform layout redistribution according to the `desired_input_layouts`.

Keyword Arguments:

*   **input\_layouts** (_Union__\[_[_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")\
    _,_ _Tuple__\[__Optional__\[_[_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")\
    _\]__\]__\]_) – The DTensor layouts of input tensors for the nn.Module, this is used to convert the input tensors to DTensors. If some inputs are not torch.Tensor or no need to convert to DTensors, `None` need to be specified as a placeholder. default: None.
    
*   **desired\_input\_layouts** (_Union__\[_[_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")\
    _,_ _Tuple__\[__Optional__\[_[_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")\
    _\]__\]__\]_) – The desired DTensor layout of input tensors for the nn.Module, this is used to ensure the inputs of the nn.Module have the desired DTensor layouts. This argument needs to have the same length with `input_layouts`. default: None.
    
*   **input\_kwarg\_layouts** (_Dict__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")\
    _\]_) – The DTensor layouts of input kwargs for the nn.Module, this is used to convert the input kwarg tensors to DTensors. default: None
    
*   **desired\_input\_kwarg\_layouts** – (Dict\[str, Placement\]): The desired DTensor layout of input kwargs for the nn.Module, this is used to ensure the inputs of the nn.Module have the desired DTensor layouts. default: None.
    
*   **use\_local\_output** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Whether to use local [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     instead of `DTensor` for the module inputs, default: False.
    

Returns:

A `ParallelStyle` object that prepares the sharding layouts of the nn.Module’s inputs.

Example::

\>>> from torch.distributed.tensor.parallel import parallelize\_module, PrepareModuleInput
\>>> from torch.distributed.device\_mesh import init\_device\_mesh
\>>> ...
\>>> block \= TransformerBlock(...)  \# block is a nn.Module that contains an "attn" Attention submodule
\>>> tp\_mesh \= init\_device\_mesh("cuda", (8,))
\>>>
\>>> \# According to the style specified below, the first input of attn will be annotated to Sharded DTensor
\>>> \# and then redistributed to Replicated DTensor.
\>>> parallelize\_module(
\>>>     block, \# this can be a submodule or module
\>>>     tp\_mesh,
\>>>     parallelize\_plan\={
\>>>         "attn": PrepareModuleInput(
\>>>             input\_layouts\=(Shard(0), None, None, ...),
\>>>             desired\_input\_layouts\=(Replicate(), None, None, ...)
\>>>         ),
\>>>     }
\>>> )

Copy to clipboard

_class_ torch.distributed.tensor.parallel.PrepareModuleOutput(_\*_, _output\_layouts_, _desired\_output\_layouts_, _use\_local\_output\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/tensor/parallel/style.py#L607)
[#](https://docs.pytorch.org/docs/2.15/distributed.tensor.parallel.html#torch.distributed.tensor.parallel.PrepareModuleOutput "Link to this definition")

Configure the nn.Module’s outputs to convert the output tensors of the nn.Module to DTensors at runtime according to `output_layouts`, and perform layout redistribution according to the `desired_output_layouts`.

Keyword Arguments:

*   **output\_layouts** (_Union__\[_[_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")\
    _,_ _Tuple__\[_[_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")\
    _\]__\]_) – The DTensor layouts of output tensors for the nn.Module, this is used to convert the output tensors to DTensors if they are [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    . If some outputs are not torch.Tensor or no need to convert to DTensors, `None` need to be specified as a placeholder.
    
*   **desired\_output\_layouts** (_Union__\[_[_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")\
    _,_ _Tuple__\[_[_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")\
    _\]__\]_) – The desired DTensor layouts of output tensors for the nn.Module, this is used to ensure the outputs of the nn.Module have the desired DTensor layouts.
    
*   **use\_local\_output** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Whether to use local [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     instead of `DTensor` for the module outputs, default: True.
    

Returns:

A ParallelStyle object that prepares the sharding layouts of the nn.Module’s outputs.

Example::

\>>> from torch.distributed.tensor.parallel import parallelize\_module, PrepareModuleOutput
\>>> from torch.distributed.device\_mesh import init\_device\_mesh
\>>> ...
\>>> block \= TransformerBlock(...)  \# block is a nn.Module that contains an "attn" Attention submodule
\>>> tp\_mesh \= init\_device\_mesh("cuda", (8,))
\>>>
\>>> \# According to the style specified below, the output of the TransformerBlock will be converted to Replicated DTensor
\>>> \# and then redistributed to Sharded DTensor.
\>>> parallelize\_module(
\>>>     block, \# this can be a submodule or module
\>>>     tp\_mesh,
\>>>     parallelize\_plan \= PrepareModuleOutput(
\>>>         output\_layouts\=Replicate(),
\>>>         desired\_output\_layouts\=Shard(0)
\>>>     )
\>>> )

Copy to clipboard

_class_ torch.distributed.tensor.parallel.PrepareModuleInputOutput(_\*_, _input\_layouts\=None_, _desired\_input\_layouts\=None_, _input\_kwarg\_layouts\=None_, _desired\_input\_kwarg\_layouts\=None_, _use\_local\_input\=False_, _output\_layouts_, _desired\_output\_layouts_, _use\_local\_output\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/tensor/parallel/style.py#L717)
[#](https://docs.pytorch.org/docs/2.15/distributed.tensor.parallel.html#torch.distributed.tensor.parallel.PrepareModuleInputOutput "Link to this definition")

Configure the nn.Module’s inputs (and outputs) to convert the input tensors (and output tensors, respectively) of the nn.Module to DTensors at runtime according to `input_layouts` (and output\_layouts, respectively), and perform layout redistribution according to the `desired_input_layouts` (and `desired_output_layouts`, respectively). This is a combination of [`PrepareModuleInput`](https://docs.pytorch.org/docs/2.15/distributed.tensor.parallel.html#torch.distributed.tensor.parallel.PrepareModuleInput "torch.distributed.tensor.parallel.PrepareModuleInput")
 and [`PrepareModuleOutput`](https://docs.pytorch.org/docs/2.15/distributed.tensor.parallel.html#torch.distributed.tensor.parallel.PrepareModuleOutput "torch.distributed.tensor.parallel.PrepareModuleOutput")
.

Keyword Arguments:

*   **input\_layouts** (_Union__\[_[_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")\
    _,_ _Tuple__\[__Optional__\[_[_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")\
    _\]__\]__\]_) – The DTensor layouts of input tensors for the nn.Module, this is used to convert the input tensors to DTensors. If some inputs are not torch.Tensor or no need to convert to DTensors, `None` need to be specified as a placeholder. default: None.
    
*   **desired\_input\_layouts** (_Union__\[_[_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")\
    _,_ _Tuple__\[__Optional__\[_[_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")\
    _\]__\]__\]_) – The desired DTensor layout of input tensors for the nn.Module, this is used to ensure the inputs of the nn.Module have the desired DTensor layouts. This argument needs to have the same length with `input_layouts`. default: None.
    
*   **input\_kwarg\_layouts** (_Dict__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")\
    _\]_) – The DTensor layouts of input kwargs for the nn.Module, this is used to convert the input kwarg tensors to DTensors. default: None
    
*   **desired\_input\_kwarg\_layouts** – (Dict\[str, Placement\]): The desired DTensor layout of input kwargs for the nn.Module, this is used to ensure the inputs of the nn.Module have the desired DTensor layouts. default: None.
    
*   **use\_local\_input** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Whether to use local [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     instead of `DTensor` for the module inputs, default: False.
    
*   **output\_layouts** (_Union__\[_[_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")\
    _,_ _Tuple__\[_[_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")\
    _\]__\]_) – The DTensor layouts of output tensors for the nn.Module, this is used to convert the output tensors to DTensors if they are [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    . If some outputs are not torch.Tensor or no need to convert to DTensors, `None` need to be specified as a placeholder.
    
*   **desired\_output\_layouts** (_Union__\[_[_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")\
    _,_ _Tuple__\[_[_Placement_](https://docs.pytorch.org/docs/2.15/distributed.tensor.html#torch.distributed.tensor.placement_types.Placement "torch.distributed.tensor.placement_types.Placement")\
    _\]__\]_) – The desired DTensor layouts of output tensors for the nn.Module, this is used to ensure the outputs of the nn.Module have the desired DTensor layouts.
    
*   **use\_local\_output** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Whether to use local [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     instead of `DTensor` for the module outputs, default: True.
    

Returns:

A `ParallelStyle` object that prepares the sharding layouts of the nn.Module’s inputs and outputs.

Example::

\>>> from torch.distributed.tensor.parallel import parallelize\_module, PrepareModuleInputOutput
\>>> from torch.distributed.device\_mesh import init\_device\_mesh
\>>> ...
\>>> block \= TransformerBlock(...)  \# block is a nn.Module that contains an "attn" Attention submodule
\>>> tp\_mesh \= init\_device\_mesh("cuda", (8,))
\>>>
\>>> \# According to the style specified below, the first input of attn will be annotated as Sharded DTensor
\>>> \# and then redistributed to Replicated DTensor, and the output of the TransformerBlock will be annotated
\>>> \# as Replicated DTensor and then redistributed to Sharded DTensor.
\>>> parallelize\_module(
\>>>     block, \# this can be a submodule or module
\>>>     tp\_mesh,
\>>>     parallelize\_plan\={
\>>>         "attn": PrepareModuleInputOutput(
\>>>             input\_layouts\=(Shard(0), None, None, ...),
\>>>             desired\_input\_layouts\=(Replicate(), None, None, ...),
\>>>             output\_layouts\=Replicate(),
\>>>             desired\_output\_layouts\=Shard(0),
\>>>         ),
\>>>     }
\>>> )

Copy to clipboard

Note

when using the `Shard(dim)` as the input/output layouts for the above `ParallelStyle` s, we assume the input/output activation tensors are evenly sharded on the tensor dimension `dim` on the `DeviceMesh` that TP operates on. For instance, since `RowwiseParallel` accepts input that is sharded on the last dimension, it assumes the input tensor has already been evenly sharded on the last dimension. For the case of uneven sharded activation tensors, one could pass in DTensor directly to the partitioned modules, and use `use_local_output=False` to return DTensor after each `ParallelStyle`, where DTensor could track the uneven sharding information.

For models like Transformer, we recommend users to use `ColwiseParallel` and `RowwiseParallel` together in the parallelize\_plan for achieve the desired sharding for the entire model (i.e. Attention and MLP).

Parallelized cross-entropy loss computation (loss parallelism), is supported via the following context manager:

torch.distributed.tensor.parallel.loss\_parallel()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/tensor/parallel/loss.py#L30)
[#](https://docs.pytorch.org/docs/2.15/distributed.tensor.parallel.html#torch.distributed.tensor.parallel.loss_parallel "Link to this definition")

A context manager that enables loss parallelism, where efficient parallelized loss computation can be performed when the input is sharded on the class dimension. Currently only the cross-entropy loss is supported.

Within this context manager, one can use [`cross_entropy()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.cross_entropy.html#torch.nn.functional.cross_entropy "torch.nn.functional.cross_entropy")
 or [`CrossEntropyLoss`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.CrossEntropyLoss.html#torch.nn.CrossEntropyLoss "torch.nn.CrossEntropyLoss")
 as usual, with the following assumptions on the input parameters. The corresponding `backward()` call, if any, also needs to happen under this context manager.

Both one-dimensional and multi-dimensional `DeviceMesh` are supported. On a multi-dimensional mesh, exactly one mesh dim must shard the class dimension — that dim is treated as the “TP” dim and can be in any position (not necessarily last). The remaining mesh dims may be `Shard` (e.g. batch-sharded for DP/CP) or `Replicate`.

Parameters:

*   **input** (`DTensor`) – Input logits. Assumed to be sharded on the class dimension on exactly one mesh dim.
    
*   **target** (Union\[[`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    , `DTensor`\]) –
    
    Must be ground truth class indices (class probabilities currently not supported). Its placements are derived from `input`’s placements by (1) replacing the TP dim’s `Shard(class_dim)` with `Replicate` and (2) shifting any other `Shard(d)` with `d > class_dim` down by one (since the class tensor dim is removed from the output):
    
    input tensor shape       input placements             target shape      target placements
    \----------------------   \--------------------------   \---------------   \------------------------
    (batch, class)           (Shard(0), Shard(1))         (batch,)          (Shard(0), Replicate())
    (batch, class)           (Replicate(), Shard(1))      (batch,)          (Replicate(), Replicate())
    (batch, class, seq)      (Shard(2), Shard(1))         (batch, seq)      (Shard(1), Replicate())
    (batch, class, seq)      (Shard(0), Shard(1))         (batch, seq)      (Shard(0), Replicate())
    
    Copy to clipboard
    
    A plain [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     is only accepted when the derived target placements are all `Replicate` (e.g. on a one-dimensional mesh); otherwise a `DTensor` must be passed explicitly so that the intended sharding is unambiguous.
    
*   **weight** (Union\[[`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    , `DTensor`\], optional) – If given, assumed to be replicated across the `DeviceMesh`.
    
*   **label\_smoothing** – Currently not supported.
    

Returns:

*   `reduction="none"` — per-sample loss; inherits the `target` placements (`Shard` on batch-parallel dims, `Replicate` on TP).
    
*   `reduction="sum"` — scalar; `Replicate` on the TP dim (the custom all-reduce makes each rank’s local value globally correct over TP), `Partial("sum")` on every other `Shard` mesh dim so that the cross-rank reduction happens lazily on materialization/redistribution, and `Replicate` on `Replicate` mesh dims.
    
*   `reduction="mean"` — only supported on a one-dimensional mesh; returns a fully replicated `DTensor`.
    

On a one-dimensional mesh all three cases simplify to a fully replicated `DTensor` (the original behavior).

Return type:

A `DTensor` whose placements depend on `reduction`

Note

`reduction="mean"` is only supported on a one-dimensional `DeviceMesh`. On a multi-dimensional mesh the per-rank division by `total_weight` uses a local count, so aggregating across non-TP dims does not yield the correct global mean; use `reduction="sum"` or `"none"` instead and divide by the global count yourself if needed.

Example

A sharded DTensor is manually created here to showcase the usage. In practice, it is usually the output of a TP module.

\>>> from torch.distributed.tensor.parallel import loss\_parallel
\>>> from torch.distributed.device\_mesh import init\_device\_mesh
\>>> ...
\>>> device\_mesh \= init\_device\_mesh("cuda", (8,))
\>>> input \= torch.randn(4, 16, device\="cuda", requires\_grad\=True)
\>>> dist\_input \= distribute\_tensor(input, device\_mesh, placements\=\[Shard(1)\])
\>>> target \= torch.randint(16, (4,), device\="cuda")
\>>> with loss\_parallel():
\>>>     loss \= F.cross\_entropy(dist\_input, target, reduction\="mean")
\>>>     loss.backward()
\>>> ...

Copy to clipboard

Warning

The loss\_parallel API is experimental and subject to change.

Copy to clipboard

torch.distributed.tensor.parallel.loss.loss\_parallel()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/tensor/parallel/loss.py#L30)
[#](https://docs.pytorch.org/docs/2.15/distributed.tensor.parallel.html#torch.distributed.tensor.parallel.loss.loss_parallel "Link to this definition")

A context manager that enables loss parallelism, where efficient parallelized loss computation can be performed when the input is sharded on the class dimension. Currently only the cross-entropy loss is supported.

Within this context manager, one can use [`cross_entropy()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.cross_entropy.html#torch.nn.functional.cross_entropy "torch.nn.functional.cross_entropy")
 or [`CrossEntropyLoss`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.CrossEntropyLoss.html#torch.nn.CrossEntropyLoss "torch.nn.CrossEntropyLoss")
 as usual, with the following assumptions on the input parameters. The corresponding `backward()` call, if any, also needs to happen under this context manager.

Both one-dimensional and multi-dimensional `DeviceMesh` are supported. On a multi-dimensional mesh, exactly one mesh dim must shard the class dimension — that dim is treated as the “TP” dim and can be in any position (not necessarily last). The remaining mesh dims may be `Shard` (e.g. batch-sharded for DP/CP) or `Replicate`.

Parameters:

*   **input** (`DTensor`) – Input logits. Assumed to be sharded on the class dimension on exactly one mesh dim.
    
*   **target** (Union\[[`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    , `DTensor`\]) –
    
    Must be ground truth class indices (class probabilities currently not supported). Its placements are derived from `input`’s placements by (1) replacing the TP dim’s `Shard(class_dim)` with `Replicate` and (2) shifting any other `Shard(d)` with `d > class_dim` down by one (since the class tensor dim is removed from the output):
    
    input tensor shape       input placements             target shape      target placements
    \----------------------   \--------------------------   \---------------   \------------------------
    (batch, class)           (Shard(0), Shard(1))         (batch,)          (Shard(0), Replicate())
    (batch, class)           (Replicate(), Shard(1))      (batch,)          (Replicate(), Replicate())
    (batch, class, seq)      (Shard(2), Shard(1))         (batch, seq)      (Shard(1), Replicate())
    (batch, class, seq)      (Shard(0), Shard(1))         (batch, seq)      (Shard(0), Replicate())
    
    Copy to clipboard
    
    A plain [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     is only accepted when the derived target placements are all `Replicate` (e.g. on a one-dimensional mesh); otherwise a `DTensor` must be passed explicitly so that the intended sharding is unambiguous.
    
*   **weight** (Union\[[`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    , `DTensor`\], optional) – If given, assumed to be replicated across the `DeviceMesh`.
    
*   **label\_smoothing** – Currently not supported.
    

Returns:

*   `reduction="none"` — per-sample loss; inherits the `target` placements (`Shard` on batch-parallel dims, `Replicate` on TP).
    
*   `reduction="sum"` — scalar; `Replicate` on the TP dim (the custom all-reduce makes each rank’s local value globally correct over TP), `Partial("sum")` on every other `Shard` mesh dim so that the cross-rank reduction happens lazily on materialization/redistribution, and `Replicate` on `Replicate` mesh dims.
    
*   `reduction="mean"` — only supported on a one-dimensional mesh; returns a fully replicated `DTensor`.
    

On a one-dimensional mesh all three cases simplify to a fully replicated `DTensor` (the original behavior).

Return type:

A `DTensor` whose placements depend on `reduction`

Note

`reduction="mean"` is only supported on a one-dimensional `DeviceMesh`. On a multi-dimensional mesh the per-rank division by `total_weight` uses a local count, so aggregating across non-TP dims does not yield the correct global mean; use `reduction="sum"` or `"none"` instead and divide by the global count yourself if needed.

Example

A sharded DTensor is manually created here to showcase the usage. In practice, it is usually the output of a TP module.

\>>> from torch.distributed.tensor.parallel import loss\_parallel
\>>> from torch.distributed.device\_mesh import init\_device\_mesh
\>>> ...
\>>> device\_mesh \= init\_device\_mesh("cuda", (8,))
\>>> input \= torch.randn(4, 16, device\="cuda", requires\_grad\=True)
\>>> dist\_input \= distribute\_tensor(input, device\_mesh, placements\=\[Shard(1)\])
\>>> target \= torch.randint(16, (4,), device\="cuda")
\>>> with loss\_parallel():
\>>>     loss \= F.cross\_entropy(dist\_input, target, reduction\="mean")
\>>>     loss.backward()
\>>> ...

Copy to clipboard

torch.distributed.tensor.parallel.input\_reshard.input\_reshard(_module_, _tp\_device\_mesh_, _input\_reshard\_dim\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/tensor/parallel/input_reshard.py#L15)
[#](https://docs.pytorch.org/docs/2.15/distributed.tensor.parallel.html#torch.distributed.tensor.parallel.input_reshard.input_reshard "Link to this definition")

Register hooks to an nn.Module for input resharding, enabling sharding and restoration during backward computation.

Register hooks to an nn.Module with input resharding so that we can shard per the given tp\_device\_mesh and input\_reshard\_dim and restore the input back when recomputing the activations in the backward. The reason why we can do this is that for Tensor Parallel(TP), the input are same across all TP ranks.

Parameters:

*   **module** (`nn.Module`) – Module to be registered with input resharding.
    
*   **tp\_device\_mesh** (`DeviceMesh`) – Object which describes the mesh topology of devices for Tensor Parallel.
    
*   **input\_reshard\_dim** (_Optional__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – The dimension of where we perform the sharding of input. If set None, there is no sharding of input. Default: None
    

Returns:

A `nn.Module` object registered with TP input resharding.

Return type:

[_Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.modules.module.Module")

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/distributed.tensor.parallel.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/distributed.tensor.parallel.md.txt)

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