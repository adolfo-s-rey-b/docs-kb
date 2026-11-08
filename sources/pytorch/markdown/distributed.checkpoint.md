Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/distributed.checkpoint.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/distributed.checkpoint.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/distributed.checkpoint.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/distributed.checkpoint.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/distributed.checkpoint.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/distributed.checkpoint.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/distributed.checkpoint.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/distributed.checkpoint.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/distributed.checkpoint.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/distributed.checkpoint.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/distributed.checkpoint.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/distributed.checkpoint.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/distributed.checkpoint.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/distributed.checkpoint.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/distributed.checkpoint.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/distributed.checkpoint.html)
[v1.13](https://docs.pytorch.org/docs/1.13/distributed.checkpoint.html)
[v1.12](https://docs.pytorch.org/docs/1.12/distributed.checkpoint.html)
[v1.11](https://docs.pytorch.org/docs/1.11/distributed.checkpoint.html)
[v1.10](https://docs.pytorch.org/docs/1.10/distributed.checkpoint.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/distributed.checkpoint.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/distributed.checkpoint.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/distributed.checkpoint.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/distributed.checkpoint.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/distributed.checkpoint.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/distributed.checkpoint.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/distributed.checkpoint.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/distributed.checkpoint.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/distributed.checkpoint.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/distributed.checkpoint.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/distributed.checkpoint.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/distributed.checkpoint.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/distributed.checkpoint.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/distributed.checkpoint.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/distributed.checkpoint.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/distributed.checkpoint.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/distributed.checkpoint.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/distributed.checkpoint.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/distributed.checkpoint.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/distributed.checkpoint.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/distributed.checkpoint.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/distributed.checkpoint.html)

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

Distributed Checkpoint - torch.distributed.checkpoint[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#distributed-checkpoint-torch-distributed-checkpoint "Link to this heading")

====================================================================================================================================================================================================

Created On: Nov 16, 2022 | Last Updated On: Jul 08, 2026

Distributed Checkpoint (DCP) supports loading and saving models from multiple ranks in parallel. It handles load-time resharding which enables saving in one cluster topology and loading into another.

DCP is different than `torch.save` and `torch.load` in a few significant ways:

*   It produces multiple files per checkpoint, with at least one per rank.
    
*   It operates in place, meaning that the model should allocate its data first and DCP uses that storage instead.
    

The entrypoints to load and save a checkpoint are the following:

Additional resources:[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#additional-resources "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

*   [Getting Started with Distributed Checkpoint (DCP)](https://pytorch.org/tutorials/recipes/distributed_checkpoint_recipe.html)
    
*   [Asynchronous Saving with Distributed Checkpoint (DCP)](https://pytorch.org/tutorials/recipes/distributed_async_checkpoint_recipe.html)
    
*   [TorchTitan Checkpointing Docs](https://github.com/pytorch/torchtitan/blob/main/docs/checkpoint.md)
    
*   [TorchTitan DCP Implementation](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpoint.py)
    

torch.distributed.checkpoint.optimizer.load\_sharded\_optimizer\_state\_dict(_model\_state\_dict_, _optimizer\_key_, _storage\_reader_, _planner\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/optimizer.py#L218)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.optimizer.load_sharded_optimizer_state_dict "Link to this definition")

Load a state\_dict in conjunction with FSDP sharded optimizer state.

This is the current recommended way to checkpoint FSDP.

Examples:

\>>> import torch.distributed.checkpoint as dist\_cp
\>>> \# Save
\>>> model: torch.nn.Model
\>>> optim\_params \= model.parameters()
\>>> optim \= torch.optim.SGD(optim\_params, lr\=0.01)
\>>> \# Save
\>>> with FSDP.state\_dict\_type(model, StateDictType.SHARDED\_STATE\_DICT):
\>>>     state\_dict \= {
\>>>         "optimizer": FSDP.optim\_state\_dict(model, optim),
\>>>         "model": model.state\_dict()
\>>>     }
\>>>     dist\_cp.save\_state\_dict(
\>>>         state\_dict\=optim\_state,
\>>>         storage\_writer\=dist\_cp.FileSystemWriter("checkpoint"),
\>>>         planner\=dist\_cp.DefaultSavePlanner(),
\>>>     )
\>>>
\>>> \# Load
\>>> with FSDP.state\_dict\_type(model\_tp, StateDictType.SHARDED\_STATE\_DICT):
\>>>     model\_state\_dict \= model\_tp.state\_dict()
\>>>     checkpoint \= {
\>>>         "model": model\_state\_dict
\>>>     }
\>>>     dist\_cp.load\_state\_dict(
\>>>         state\_dict\=checkpoint,
\>>>         storage\_reader\=dist\_cp.FileSystemReader(checkpoint\_file),
\>>>         planner\=dist\_cp.DefaultLoadPlanner(),
\>>>     )
\>>>     model.load\_state\_dict(checkpoint\["model\_state"\])
\>>>
\>>>     optim\_state \= dist\_cp.load\_sharded\_optimizer\_state\_dict(
\>>>         model\_state\_dict,
\>>>         optimizer\_key\="optimizer",
\>>>         storage\_reader\=dist\_cp.FileSystemReader("checkpoint"),
\>>>     )
\>>>
\>>>     flattened\_osd \= FSDP.optim\_state\_dict\_to\_load(
\>>>        model, optim, optim\_state\["optimizer"\]
\>>>     )
\>>>
\>>>     optim.load\_state\_dict(flattened\_osd)

Copy to clipboard

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, _StatefulT_ | [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\]

torch.distributed.checkpoint.planner\_helpers.create\_read\_items\_for\_chunk\_list(_fqn_, _checkpoint\_md_, _local\_chunks_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner_helpers.py#L281)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.planner_helpers.create_read_items_for_chunk_list "Link to this definition")

Create a list of `ReadItem` based on the checkpoint and local chunks.

This applies the resharding algorithm and computes the reads needed to satisfy `local_chunks` with a checkpoint described by `checkpoint_md`.

Parameters:

*   **fqn** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The state\_dict FQN to pass to `ReadItem`.
    
*   **checkpoint\_md** ([_TensorStorageMetadata_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.metadata.TensorStorageMetadata "torch.distributed.checkpoint.metadata.TensorStorageMetadata")
    ) – metadata for a given tensor from a checkpoint.
    
*   **local\_chunks** (_List__\[__ChunkStorageMetadata__\]_) – Local chunks that needs to be loaded.
    

Returns:

A list of `ReadItem` that will satisfy all input chunks.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[_ReadItem_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.ReadItem "torch.distributed.checkpoint.planner.ReadItem")\
\]

torch.distributed.checkpoint.default\_planner.create\_default\_global\_load\_plan(_all\_plans_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/default_planner.py#L525)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.default_planner.create_default_global_load_plan "Link to this definition")

Create global load plan used by DefaultLoadPlanner.

The default load behavior involved no global coordination and this function currently doesn’t change the local plans.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[_LoadPlan_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlan "torch.distributed.checkpoint.planner.LoadPlan")\
\]

torch.distributed.checkpoint.default\_planner.create\_default\_global\_save\_plan(_all\_plans_, _rewrite\_index\_hints\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/default_planner.py#L564)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.default_planner.create_default_global_save_plan "Link to this definition")

Create the global plan and metadata used by DefaultSavePlanner.

Metadata is produced by concatenating the metadata of all `WriteItem` from the supplied plans.

The only global planning change is to update index hints in all `MetadataIndex` objects if `rewrite_index_hints` is True.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[_SavePlan_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlan "torch.distributed.checkpoint.planner.SavePlan")\
\], _Metadata_\]

torch.distributed.checkpoint.default\_planner.create\_default\_local\_save\_plan(_state\_dict_, _is\_coordinator_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/default_planner.py#L537)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.default_planner.create_default_local_save_plan "Link to this definition")

Create the `SavePlan` used by DefaultSavePlanner.

On non-coordinator ranks, this function ignores tensors and non-tensor objects, only producing writes for ShardedTensor objects.

On the coordinator rank, produce writes for all values.

Return type:

[_SavePlan_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlan "torch.distributed.checkpoint.planner.SavePlan")

_class_ torch.distributed.checkpoint.state\_dict\_saver.AsyncCheckpointerType(_value_, _names\=None_, _\*_, _module\=None_, _qualname\=None_, _type\=None_, _start\=1_, _boundary\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/state_dict_saver.py#L52)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.state_dict_saver.AsyncCheckpointerType "Link to this definition")

Enum for async checkpointer type.

_class_ torch.distributed.checkpoint.state\_dict\_saver.AsyncSaveResponse(_staging\_completion_, _upload\_completion_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/state_dict_saver.py#L206)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.state_dict_saver.AsyncSaveResponse "Link to this definition")

This class contains futures for staging and upload completion. It is returned by async\_save(). staging\_completion is a future that indicates when local copy of state\_dict is complete. upload\_completion is a future that indicates when a checkpoint completed saving.

torch.distributed.checkpoint.state\_dict\_saver.save(_state\_dict_, _\*_, _checkpoint\_id\=None_, _storage\_writer\=None_, _planner\=None_, _process\_group\=None_, _no\_dist\=False_, _use\_collectives\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/state_dict_saver.py#L87)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.state_dict_saver.save "Link to this definition")

Save a distributed model in SPMD style.

This function is different from `torch.save()` as it handles `ShardedTensor` , and `DTensor` by having each rank only save their local shards.

For each `Stateful` object (having both a `state_dict` and a `load_state_dict`), save will call `state_dict` before serialization.

Warning

There are no guarantees of Backwards Compatibility across PyTorch versions for saved state\_dicts.

Warning

If using the process\_group argument, make sure that only its ranks call save\_state\_dict and that all data in state\_dict belong to it.

Note

When saving checkpoint for FSDP’s ShardingStrategy.HYBRID\_SHARD, only one of the shard\_group should be calling save\_state\_dict and the corresponding process group needs to be passed in.

Note

If no process group is available, this function assumes the intention is to save the

state\_dict in the local process.

Parameters:

*   **state\_dict** (_Dict__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _Any__\]_) – The state\_dict to save.
    
*   **checkpoint\_id** (_Union__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_os.PathLike_](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.15)")\
    _,_ _None__\]_) – The ID of this checkpoint instance. The meaning of the checkpoint\_id depends on the storage. It can be a path to a folder or to a file. It can also be a key if the storage is a key-value store. (Default: `None`)
    
*   **storage\_writer** (_Optional__\[_[_StorageWriter_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.StorageWriter "torch.distributed.checkpoint.StorageWriter")\
    _\]_) – Instance of StorageWriter used to perform writes. If this is not specified, DCP will automatically infer the writer based on the checkpoint\_id. If checkpoint\_id is also None, an exception will be raised. (Default: `None`)
    
*   **planner** (_Optional__\[_[_SavePlanner_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlanner "torch.distributed.checkpoint.SavePlanner")\
    _\]_) – Instance of SavePlanner. If this is not specified, the default planner will be used. (Default: `None`)
    
*   **process\_group** (_Optional__\[__ProcessGroup__\]_) – ProcessGroup to be used for cross-rank synchronization. (Default: `None`)
    
*   **no\_dist** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True`, this function will assume the intent is to load a checkpoint on a single rank/process. (Default: `False`)
    
*   **use\_collectives** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `False`, this function will assume the intent is to save a checkpoint without using cross-rank synchronization. (Default: `True`) This configuration is experimental and should be used with caution. It will change the format of the saved checkpoint and may not be backward compatible.
    

Returns:

Metadata object for the saved checkpoint.

Return type:

Metadata

Example

\>>> my\_model \= MyModule()

Copy to clipboard

\>>> state\_dict \= {"model": my\_model}

Copy to clipboard

\>>> fs\_storage\_writer \= torch.distributed.checkpoint.FileSystemWriter(
...     "/checkpoint/1"
... )
\>>> torch.distributed.checkpoint.save(
\>>>     state\_dict\=state\_dict,
\>>>     storage\_writer\=fs\_storage\_writer,
\>>> )

Copy to clipboard

Note

save\_state\_dict uses collectives to coordinate writes across ranks. For NCCL-based process groups, internal tensor representations of objects must be moved to the GPU device before communication takes place. In this case, the device used is given by `torch.cuda.current_device()` and it is the user’s responsibility to ensure that this is set so that each rank has an individual GPU, via `torch.cuda.set_device()`.

torch.distributed.checkpoint.state\_dict\_saver.async\_save(_state\_dict_, _\*_, _checkpoint\_id\=None_, _storage\_writer\=None_, _planner\=None_, _process\_group\=None_, _async\_checkpointer\_type\=AsyncCheckpointerType.THREAD_, _async\_stager\=None_, _no\_dist\=False_, _use\_collectives\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/state_dict_saver.py#L220)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.state_dict_saver.async_save "Link to this definition")

Asynchronous version of `save`. This code first de-stages the state\_dict on to the staging storage (defaults to CPU memory), and then calls the save in a separate thread.

Warning

This feature is experimental and subject to change. If you provide an `async_stager`, call `close()` after the last checkpoint is saved. Internally created default stagers are closed automatically.

Parameters:

*   **state\_dict** (_Dict__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _Any__\]_) – The state\_dict to save.
    
*   **checkpoint\_id** (_Union__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_os.PathLike_](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.15)")\
    _,_ _None__\]_) – The ID of this checkpoint instance. The meaning of the checkpoint\_id depends on the storage. It can be a path to a folder or to a file. It can also be a key if the storage is a key-value store. (Default: `None`)
    
*   **storage\_writer** (_Optional__\[_[_StorageWriter_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.StorageWriter "torch.distributed.checkpoint.StorageWriter")\
    _\]_) – Instance of StorageWriter used to perform ‘stage’ and ‘save’. If this is not specified, DCP will automatically infer the writer based on the checkpoint\_id. If checkpoint\_id is also None, an exception will be raised. (Default: `None`)
    
*   **planner** (_Optional__\[_[_SavePlanner_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlanner "torch.distributed.checkpoint.SavePlanner")\
    _\]_) – Instance of SavePlanner. If this is not specified, the default planner will be used. (Default: `None`)
    
*   **process\_group** (_Optional__\[__ProcessGroup__\]_) – ProcessGroup to be used for cross-rank synchronization. (Default: `None`)
    
*   **async\_checkpointer\_type** ([_AsyncCheckpointerType_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.state_dict_saver.AsyncCheckpointerType "torch.distributed.checkpoint.state_dict_saver.AsyncCheckpointerType")
    ) – whether to do checkpoint in separate thread or process (Default: `AsyncCheckpointerType.THREAD`)
    
*   **async\_stager** ([_AsyncStager_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.staging.AsyncStager "torch.distributed.checkpoint.staging.AsyncStager")
    ) – provides staging implementation. If `storage_writer` implements `AsyncStager` and `async_stager` is not provided, `storage_writer` will be used for staging. User-provided stagers remain owned by the caller and should be closed after the last checkpoint is saved.
    
*   **no\_dist** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True`, this function will assume the intent is to save a checkpoint on a single rank/process. (Default: `False`)
    
*   **use\_collectives** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If False, Save the checkpoint without rank coordination. (Default: `True`) This configuration is experimental and should be used with caution. It will change the format of the saved checkpoint and may not be backward compatible.
    

Returns:

A future holding the resultant Metadata object from save.

Return type:

[Future](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")

Example

\>>> my\_model \= MyModule()

Copy to clipboard

\>>> state\_dict \= {"model": my\_model}

Copy to clipboard

\>>> fs\_storage\_writer \= torch.distributed.checkpoint.FileSystemWriter(
...     "/checkpoint/1"
... )
\>>> checkpoint\_future \= torch.distributed.checkpoint.async\_save(
\>>>     state\_dict\=state\_dict,
\>>>     storage\_writer\=fs\_storage\_writer,
\>>> )
\>>>
\>>> \# ... do some work ...
\>>>
\>>> checkpoint\_future.result()

Copy to clipboard

torch.distributed.checkpoint.state\_dict\_saver.save\_state\_dict(_state\_dict_, _storage\_writer_, _process\_group\=None_, _coordinator\_rank\=0_, _no\_dist\=False_, _planner\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/state_dict_saver.py#L59)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.state_dict_saver.save_state_dict "Link to this definition")

This method is deprecated. Please switch to ‘save’.

Return type:

_Metadata_

torch.distributed.checkpoint.state\_dict\_loader.load(_state\_dict_, _\*_, _checkpoint\_id\=None_, _storage\_reader\=None_, _planner\=None_, _process\_group\=None_, _no\_dist\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/state_dict_loader.py#L58)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.state_dict_loader.load "Link to this definition")

Load a checkpoint into a distributed state dict in SPMD style.

Each rank must have the same keys in their `state_dict` provided to this API. Mismatched keys may result in hangs or errors. If unsure, you can use the `utils._assert_same_keys` API to check (but may incur communication costs).

Each rank will try to read the least amount of data necessary to fulfill the requested state\_dict. When loading `ShardedTensor` or `DTensor` instances, each rank only reads data for their local shards.

For each `Stateful` object (having both a `state_dict` and a `load_state_dict`), load will first call `state_dict` before attempting deserialization, followed by `load_state_dict` once the deserialization is complete. For each non-`Stateful` object, load will deserialize the object, and then replace it in the `state_dict` with the deserialized object.

Warning

All tensors in `state_dict` must be allocated on their destination device _prior to_ calling this function.

All non-tensor data is loaded using torch.load() and modified in place on state\_dict.

Warning

Users must call load\_state\_dict on the root module to ensure load post-processing and non-tensor data properly propagates.

Parameters:

*   **state\_dict** (_Dict__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _Any__\]_) – The state\_dict to load the checkpoint into.
    
*   **checkpoint\_id** (_Union__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_os.PathLike_](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.15)")\
    _,_ _None__\]_) – The ID of this checkpoint instance. The meaning of the checkpoint\_id depends on the storage. It can be a path to a folder or to a file. It can also be a key if the storage is a key-value store. (Default: `None`)
    
*   **storage\_reader** (_Optional__\[_[_StorageReader_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.StorageReader "torch.distributed.checkpoint.StorageReader")\
    _\]_) – Instance of StorageWriter used to perform reads. If this is not specified, DCP will automatically infer the reader based on the checkpoint\_id. If checkpoint\_id is also None, an exception will be raised. (Default: `None`)
    
*   **planner** (_Optional__\[_[_LoadPlanner_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlanner "torch.distributed.checkpoint.LoadPlanner")\
    _\]_) – Instance of LoadPlanner. If this is not specified, the default planner will be used. (Default: `None`)
    
*   **process\_group** (_Optional__\[__ProcessGroup__\]_) – ProcessGroup to be used for cross-rank synchronization. (Default: `None`)
    
*   **no\_dist** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True`, this function will assume the intent is to load a checkpoint without using cross-rank synchronization. (Default: `False`)
    

Returns:

None.

Return type:

None

Examples

\>>> my\_model \= MyModule()
\>>> optimizer \= Adagrad(my\_model.parameters())
\>>> model\_state\_dict \= my\_model.state\_dict()
\>>> fs\_storage\_reader \= torch.distributed.checkpoint.FileSystemReader(
...     "/checkpoint/1"
... )

Copy to clipboard

\>>> torch.distributed.checkpoint.load\_state\_dict(
\>>>     state\_dict\=model\_state\_dict,
\>>>     storage\_reader\=fs\_storage\_reader,
\>>> )

Copy to clipboard

\>>> \# module.load\_state\_dict() function might have customized steps
\>>> \# to flush the state\_dict, must call it to
\>>> \# ensure correct behavior.
\>>> my\_model.load\_state\_dict(model\_state\_dict)

Copy to clipboard

Note

load\_state\_dict uses collectives to coordinate reads across ranks. For NCCL-based process groups, internal tensor representations of objects must be moved to the GPU device before communication takes place. In this case, the device used is given by `torch.cuda.current_device()` and it is the user’s responsibility to ensure that this is set so that each rank has an individual GPU, via `torch.cuda.set_device()`.

torch.distributed.checkpoint.state\_dict\_loader.load\_state\_dict(_state\_dict_, _storage\_reader_, _process\_group\=None_, _coordinator\_rank\=0_, _no\_dist\=False_, _planner\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/state_dict_loader.py#L31)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.state_dict_loader.load_state_dict "Link to this definition")

This method is deprecated. Please switch to ‘load’.

The following module is also useful for additional customization of the staging mechanisms used for asynchronous checkpointing (`torch.distributed.checkpoint.async_save`):

_class_ torch.distributed.checkpoint.staging.AsyncStager(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/staging.py#L39)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.staging.AsyncStager "Link to this definition")

This protocol is meant to provide customization and extensibility for dcp.async\_save, allowing users to customize how data is staged previous to executing the usual dcp.save path in parallel. The expected order of operations (concretely defined in torch.distributed.state\_dict\_saver.async\_save) is the following:

1.  AsyncStager.stage\_data(state\_dict):
    
    This call gives the AsyncStager the opportunity to ‘stage’ the state\_dict. The expectation and purpose of staging in this context is to create a “training-safe” representation of the state dict, meaning that any updates to module data after staging is complete should not be reflected in the state dict returned from this method. For example, in the default case a copy of the entire state dict is created on CPU RAM and returned here, allowing users to continue training without risking changes to data which is being serialized.
    
2.  dcp.save is called on the state\_dict returned from stage in parallel. This call is responsible
    
    for serializing the state\_dict and writing it to storage.
    
3.  If AsyncStager.should\_synchronize\_after\_execute is True, this method will be called immediately after
    
    the serialization thread starts and before returning from dcp.async\_save. If this is set to False, the assumption is the user has defined a custom synchronization point for the purpose of further optimizing save latency in the training loop (for example, by overlapping staging with the forward/backward pass), and it is the respondsibility of the user to call AsyncStager.synchronize\_staging at the appropriate time.
    

close()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/staging.py#L99)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.staging.AsyncStager.close "Link to this definition")

Clean up all resources used by the stager.

_property_ should\_synchronize\_after\_execute_: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.staging.AsyncStager.should_synchronize_after_execute "Link to this definition")

Whether to synchronize after executing the stage.

stage(_state\_dict_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/staging.py#L77)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.staging.AsyncStager.stage "Link to this definition")

Returns a “staged” copy of state\_dict. The expectation of the staged copy is that it is inoculated from any updates incurred after the stage call is complete.

Return type:

_Future_\[[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, _StatefulT_ | [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\]\] | [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, _StatefulT_ | [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\]

synchronize\_staging()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/staging.py#L88)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.staging.AsyncStager.synchronize_staging "Link to this definition")

In the case stage is async in some way, this method should be called to ensure staging is complete and it is safe to begin modifying the original state\_dict

_class_ torch.distributed.checkpoint.staging.DefaultStager(_config\=StagingOptions(use\_pinned\_memory=True, use\_shared\_memory=True, use\_async\_staging=True, use\_non\_blocking\_copy=True)_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/staging.py#L133)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.staging.DefaultStager "Link to this definition")

DefaultStager provides a full-featured staging implementation that combines multiple optimization techniques for efficient checkpoint preparation.

The staging process works as follows: 1. State dictionary is submitted for staging (sync or async) 2. Tensors are copied from GPU to optimized CPU storage 3. CUDA operations are synchronized if non-blocking copies are used 4. Staged state dictionary is returned or made available via Future

Usage Patterns:

\# Synchronous staging stager = DefaultStager(StagingOptions(use\_async\_staging=False)) staged\_dict = stager.stage(state\_dict) stager.close()

\# Asynchronous staging stager = DefaultStager(StagingOptions(use\_async\_staging=True)) future = stager.stage(state\_dict) # … do other work … staged\_dict = future.result() stager.close()

Performance Considerations:

*   Async staging provides best performance when model computation can overlap with staging operations
    
*   Pinned memory improves CPU-GPU transfer speeds but uses more memory
    
*   Shared memory allows efficient IPC to checkpoint process
    
*   Non-blocking copies reduce GPU idle time during memory transfers
    

Thread Safety:

DefaultStager is not thread-safe. Each thread should use its own instance, or external synchronization should be provided.

close()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/staging.py#L246)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.staging.DefaultStager.close "Link to this definition")

Clean up all resources used by the DefaultStager. Shuts down the ThreadPoolExecutor used for async staging operations and cleans up the underlying StateDictStager’s cached storages. Should be called when the stager is no longer needed to prevent resource leaks, especially in long-running applications. After calling close(), the stager should not be used for further staging operations.

Example Usage:

stager = DefaultStager(StagingOptions(use\_async\_staging=True)) future = stager.stage(state\_dict) result = future.result() stager.close() # Clean up all resources

stage(_state\_dict_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/staging.py#L196)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.staging.DefaultStager.stage "Link to this definition")

This function is responsible for staging the state\_dict. See class docstring for more details on staging. If use\_async\_staging is True, it will return a Future object that will be fulfilled when staging is complete. If use\_async\_staging is False, it will return the fully staged state\_dict.

Parameters:

**state\_dict** (_STATE\_DICT\_TYPE_) – The state\_dict to be staged.

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, _StatefulT_ | [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\] | _Future_\[[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, _StatefulT_ | [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\]\]

synchronize\_staging()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/staging.py#L264)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.staging.DefaultStager.synchronize_staging "Link to this definition")

When use\_async\_staging is True, this method will wait until staging is complete. If use\_async\_staging is False, this method is a no-op.

_class_ torch.distributed.checkpoint.staging.StagingOptions(_use\_pinned\_memory\=True_, _use\_shared\_memory\=True_, _use\_async\_staging\=True_, _use\_non\_blocking\_copy\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/staging.py#L105)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.staging.StagingOptions "Link to this definition")

Configuration options for checkpoint staging behavior.

Variables:

*   **use\_pinned\_memory** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Enable pinned memory allocation for faster CPU-GPU transfers. Requires CUDA to be available. Default: True
    
*   **use\_shared\_memory** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Enable shared memory for multi-process scenarios. Useful when multiple processes need access to the same staged data. Default: True
    
*   **use\_async\_staging** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Enable asynchronous staging using a background thread pool. Allows overlapping computation with staging operations. Requires CUDA. Default: True
    
*   **use\_non\_blocking\_copy** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Use non-blocking device memory copies with stream synchronization. Improves performance by allowing CPU work to continue during GPU transfers. Default: True
    

Note

CUDA-dependent features will raise exception if CUDA is not available.

_class_ torch.distributed.checkpoint.staging.BlockingAsyncStager(_cache\_staged\_state\_dict\=False_, _type\_check\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/staging.py#L273)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.staging.BlockingAsyncStager "Link to this definition")

An implementation of AsyncStager which stages the state\_dict on CPU RAM and blocks until the copy is complete. This implementation also provides an option to optimize stage latency using pinned memory.

N.B. synchronize\_staging is a no-op in this case.

stage(_state\_dict_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/staging.py#L305)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.staging.BlockingAsyncStager.stage "Link to this definition")

Returns a copy of state\_dict on the CPU.

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, _StatefulT_ | [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\]

synchronize\_staging()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/staging.py#L319)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.staging.BlockingAsyncStager.synchronize_staging "Link to this definition")

No-op function, since staging is blocking.

In addition to the above entrypoints, `Stateful` objects, as described below, provide additional customization during saving/loading

_class_ torch.distributed.checkpoint.stateful.Stateful(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/stateful.py#L8)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.stateful.Stateful "Link to this definition")

Stateful protocol for objects that can be checkpointed and restored.

load\_state\_dict(_state\_dict_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/stateful.py#L31)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.stateful.Stateful.load_state_dict "Link to this definition")

Restore the object’s state from the provided state\_dict.

Parameters:

**state\_dict** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
_\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_,_ [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
_\]_) – The state dict to restore from

state\_dict()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/stateful.py#L14)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.stateful.Stateful.state_dict "Link to this definition")

Objects should return their state\_dict representation as a dictionary. The output of this function will be checkpointed, and later restored in load\_state\_dict().

Warning

Because of the inplace nature of restoring a checkpoint, this function is also called during torch.distributed.checkpoint.load.

Returns:

The objects state dict

Return type:

Dict

This [example](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/examples/fsdp_checkpoint_example.py)
 shows how to use PyTorch Distributed Checkpoint to save a FSDP model.

The following types define the IO interface used during checkpoint:

_class_ torch.distributed.checkpoint.StorageReader[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/storage.py#L168)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.StorageReader "Link to this definition")

Interface used by `load_state_dict` to read from storage.

One StorageReader instance acts as both the coordinator and the follower in a distributed checkpoint. As part of initialization, each instance is told its role.

A subclass should expect the following sequence of calls by `load_state_dict`:

0.  (all ranks) set checkpoint\_id if users pass a valid checkpoint\_id.
    
1.  (all ranks) read\_metadata()
    
2.  (all ranks) set\_up\_storage\_reader()
    
3.  (all ranks) prepare\_local\_plan()
    
4.  (coordinator) prepare\_global\_plan()
    
5.  (all ranks) read\_data()
    

_abstract_ prepare\_global\_plan(_plans_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/storage.py#L242)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.StorageReader.prepare_global_plan "Link to this definition")

Perform centralized planning of storage loading.

This method is only called on the coordinator instance.

While this method can produce a completely different plan, the preferred way is to store storage specific data in LoadPlan::storage\_data.

Parameters:

**plans** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
_\[_[_LoadPlan_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlan "torch.distributed.checkpoint.planner.LoadPlan")\
_\]_) – A list of `LoadPlan` instances, one for each rank.

Returns:

A list of transformed `LoadPlan` after storage global planning

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[_LoadPlan_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlan "torch.distributed.checkpoint.planner.LoadPlan")\
\]

_abstract_ prepare\_local\_plan(_plan_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/storage.py#L227)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.StorageReader.prepare_local_plan "Link to this definition")

Perform storage-specific local planning.

While this method can produce a completely different plan, the recommended way is to store storage specific data in LoadPlan::storage\_data.

Parameters:

**plan** ([_LoadPlan_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlan "torch.distributed.checkpoint.LoadPlan")
) – The local plan from the `LoadPlan` in use.

Returns:

A transformed `LoadPlan` after storage local planning

Return type:

[_LoadPlan_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlan "torch.distributed.checkpoint.planner.LoadPlan")

_abstract_ read\_data(_plan_, _planner_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/storage.py#L259)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.StorageReader.read_data "Link to this definition")

Read all items from `plan` using `planner` to resolve the data.

A subclass should call `LoadPlanner::load_bytes` to deserialize a BytesIO object into the right place.

A subclass should call `LoadPlanner::resolve_tensor` to get access to the tensors that in should load data into.

It’s the StorageLayer responsibility to properly schedule any cross device copies required.

Parameters:

*   **plan** ([_LoadPlan_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlan "torch.distributed.checkpoint.LoadPlan")
    ) – The local plan to execute on
    
*   **planner** ([_LoadPlanner_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlanner "torch.distributed.checkpoint.LoadPlanner")
    ) – The planner object to use to resolve items.
    

Returns:

A future that completes once all reads are finished.

Return type:

[_Future_](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.jit.Future")
\[None\]

_abstract_ read\_metadata(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/storage.py#L204)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.StorageReader.read_metadata "Link to this definition")

Read the checkpoint metadata.

Returns:

The metadata object associated with the checkpoint being loaded.

Return type:

_Metadata_

_abstract_ reset(_checkpoint\_id\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/storage.py#L186)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.StorageReader.reset "Link to this definition")

Calls to indicates a brand new checkpoint read is going to happen. A checkpoint\_id may be present if users set the checkpoint\_id for this checkpoint read. The meaning of the checkpoint\_id is storage-dependent. It can be a path to a folder/file or a key for a key-value storage.

Parameters:

**checkpoint\_id** (_Union__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_,_ [_os.PathLike_](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.15)")\
_,_ _None__\]_) – The ID of this checkpoint instance. The meaning of the checkpoint\_id depends on the storage. It can be a path to a folder or to a file. It can also be a key if the storage is more like a key-value store. (Default: `None`)

_abstract_ set\_up\_storage\_reader(_metadata_, _is\_coordinator_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/storage.py#L214)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.StorageReader.set_up_storage_reader "Link to this definition")

Initialize this instance.

Parameters:

*   **metadata** (_Metadata_) – The metadata schema to use.
    
*   **is\_coordinator** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether this instance is responsible for coordinating the checkpoint.
    

_abstract classmethod_ validate\_checkpoint\_id(_checkpoint\_id_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/storage.py#L281)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.StorageReader.validate_checkpoint_id "Link to this definition")

Check if the given checkpoint\_id is supported by the storage. This allows us to enable automatic storage selection.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

_class_ torch.distributed.checkpoint.StorageWriter[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/storage.py#L27)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.StorageWriter "Link to this definition")

Interface used by `save_state_dict` to write to storage.

One StorageWriter instance acts as both the coordinator and the follower in a distributed checkpoint. As part of initialization, each instance is told its role.

A subclass should expect the following sequence of calls.

0.  (all ranks) set checkpoint\_id if users pass a valid checkpoint\_id.
    
1.  (all ranks) set\_up\_storage\_writer()
    
2.  (all ranks) prepare\_local\_plan()
    
3.  (coordinator) prepare\_global\_plan()
    
4.  (all ranks) write\_data()
    
5.  (coordinator) finish()
    

_abstract_ finish(_metadata_, _results_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/storage.py#L131)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.StorageWriter.finish "Link to this definition")

Write the metadata and marks the current checkpoint as successful.

The actual format/schema used for serializing metadata is an implementation detail. The only requirement is that it’s recoverable in to the same object graph.

Parameters:

*   **metadata** (_Metadata_) – metadata for the new checkpoint
    
*   **results** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
    _\[__WriteResult__\]__\]_) – A list of WriteResults from all ranks.
    

Returns:

None

Return type:

None

_abstract_ prepare\_global\_plan(_plans_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/storage.py#L90)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.StorageWriter.prepare_global_plan "Link to this definition")

Perform centralized planning of storage.

This method is only called on the coordinator instance.

While this method can produce a completely different plan, the preferred way is to store storage specific data in SavePlan::storage\_data.

Parameters:

**plans** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
_\[_[_SavePlan_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlan "torch.distributed.checkpoint.planner.SavePlan")\
_\]_) – A list of `SavePlan` instances, one for each rank.

Returns:

A list of transformed `SavePlan` after storage global planning

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[_SavePlan_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlan "torch.distributed.checkpoint.planner.SavePlan")\
\]

_abstract_ prepare\_local\_plan(_plan_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/storage.py#L75)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.StorageWriter.prepare_local_plan "Link to this definition")

Perform storage-specific local planning.

While this method can produce a completely different plan, the recommended way is to store storage specific data in SavePlan::storage\_data.

Parameters:

**plan** ([_SavePlan_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlan "torch.distributed.checkpoint.SavePlan")
) – The local plan from the `SavePlanner` in use.

Returns:

A transformed `SavePlan` after storage local planning

Return type:

[_SavePlan_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlan "torch.distributed.checkpoint.planner.SavePlan")

_abstract_ reset(_checkpoint\_id\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/storage.py#L45)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.StorageWriter.reset "Link to this definition")

Calls to indicates a brand new checkpoint write is going to happen. A checkpoint\_id may be present if users set the checkpoint\_id for this checkpoint write. The meaning of the checkpoint\_id is storage-dependent. It can be a path to a folder/file or a key for a key-value storage.

Parameters:

**checkpoint\_id** (_Union__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_,_ [_os.PathLike_](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.15)")\
_,_ _None__\]_) – The ID of this checkpoint instance. The meaning of the checkpoint\_id depends on the storage. It can be a path to a folder or to a file. It can also be a key if the storage is a key-value store. (Default: `None`)

_abstract_ set\_up\_storage\_writer(_is\_coordinator_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/storage.py#L63)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.StorageWriter.set_up_storage_writer "Link to this definition")

Initialize this instance.

Parameters:

**is\_coordinator** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
) – Whether this instance is responsible for coordinating the checkpoint.

storage\_meta()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/storage.py#L157)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.StorageWriter.storage_meta "Link to this definition")

Return the storage-specific metadata. This is used to store additional information in a checkpoint that can be useful for providing request-level observability. StorageMeta is passed to the `SavePlanner` during save calls. Returns None by default.

TODO: provide an example

Return type:

[_StorageMeta_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.metadata.StorageMeta "torch.distributed.checkpoint.metadata.StorageMeta")
 | None

_abstract classmethod_ validate\_checkpoint\_id(_checkpoint\_id_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/storage.py#L148)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.StorageWriter.validate_checkpoint_id "Link to this definition")

Check if the given checkpoint\_id is supported by the storage. This allows us to enable automatic storage selection.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

_abstract_ write\_data(_plan_, _planner_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/storage.py#L107)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.StorageWriter.write_data "Link to this definition")

Write all items from `plan` using `planner` to resolve the data.

A subclass should call `SavePlanner::resolve_data` on each item from the plan to get access to the underlying object to write.

Subclasses should lazily call resolve\_data as it can allocate memory. In case of tensors, make following assumptions:

*   They might be on any device, including not matching the one on `WriteItem::tensor_data`
    
*   They might be views or not contiguous. Only the projection needs to be saved.
    

Parameters:

*   **plan** ([_SavePlan_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlan "torch.distributed.checkpoint.SavePlan")
    ) – The save plan to execute.
    
*   **planner** ([_SavePlanner_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlanner "torch.distributed.checkpoint.SavePlanner")
    ) – Planner object to be used to resolve items to data.
    

Returns:

A future that completes to a list of WriteResult

Return type:

[_Future_](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.jit.Future")
\[[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[_WriteResult_\]\]

The following types define the metadata used during checkpoint:

_class_ torch.distributed.checkpoint.metadata.StorageMeta(_checkpoint\_id: str | os.PathLike | None \= None_, _save\_id: str | None \= None_, _load\_id: str | None \= None_, _modules: list\[str\] \= <factory>_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/metadata.py#L145)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.metadata.StorageMeta "Link to this definition")

_class_ torch.distributed.checkpoint.metadata.TensorProperties(_dtype=<factory>_, _layout=torch.strided_, _requires\_grad=False_, _memory\_format=torch.contiguous\_format_, _pin\_memory=False_, _strides=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/metadata.py#L42)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.metadata.TensorProperties "Link to this definition")

Properties used to create `Tensor`

_class_ torch.distributed.checkpoint.metadata.TensorStorageMetadata(_properties: [torch.distributed.checkpoint.metadata.TensorProperties](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.metadata.TensorProperties "torch.distributed.checkpoint.metadata.TensorProperties")
_, _size: [torch.Size](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")
_, _chunks: [list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[torch.distributed.checkpoint.metadata.ChunkStorageMetadata\]_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/metadata.py#L129)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.metadata.TensorStorageMetadata "Link to this definition")

The following types define the planner interface used during checkpoint:

_class_ torch.distributed.checkpoint.LoadPlanner[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L304)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlanner "Link to this definition")

Abstract class defining the protocol used by load\_state\_dict to plan the load process.

LoadPlanner are stateful objects that can be used to customize the whole load process.

LoadPlanner acts as an access proxy to the state\_dict, so any transformation done to it will be visible to the whole process.

A planner subclass can expect the following sequence of calls during load\_state\_dict:

1.  set\_up\_planner - called on all ranks.
    
    Signals the start of loading a checkpoint.
    
2.  create\_local\_plan - called on all ranks.
    
    Process the state\_dict and produces a LoadPlan that will be sent for global planning.
    
3.  create\_global\_plan - called on the coordinator rank only.
    
    Takes the LoadPlan from all ranks and make any global decision.
    
4.  load\_bytes - called multiple times on each rank
    
    This is called once per non-tensor value in state\_dict.
    
5.  resolve\_tensor and commit\_tensor - called multiple times on each rank
    
    They are called in pair for each Tensor value in state\_dict.
    

Users are recommended to extend DefaultLoadPlanner instead of this interface directly as most changes can be expressed by changes in a single method.

There are two usual patterns of extension:

Rewriting state\_dict. This is the simplest way to extend the load process as it doesn’t require understanding the intricacies of how LoadPlan works. We need to keep a reference to the original state\_dict as load happens in place so we need to be able to perform it in place

\>>> class RenamePlanner(DefaultLoadPlanner):
\>>>     def set\_up\_planner(
\>>>         self,
\>>>         state\_dict: STATE\_DICT\_TYPE,
\>>>         metadata: Metadata,
\>>>         is\_coordinator: bool,
\>>>     ) \-> None:
\>>>         self.original\_state\_dict \= state\_dict
\>>>         state\_dict \= {"foo\_" + k: v for k, v in state\_dict.items()}
\>>>
\>>>         if self.flatten\_sharded\_tensors:
\>>>             state\_dict \= \_flatten\_sharded\_tensors(state\_dict)
\>>>
\>>>         if self.flatten\_state\_dict:
\>>>             state\_dict, self.mappings \= flatten\_state\_dict(state\_dict)
\>>>
\>>>         self.state\_dict \= state\_dict
\>>>         self.metadata \= metadata
\>>>         self.is\_coordinator \= is\_coordinator
\>>>
\>>>     def load\_bytes(self, read\_item, value):
\>>> \# Remove the "foo\_" prefix
\>>>         self.original\_state\_dict\[read\_item.dest\_index.fqn\[4:\]\] \= torch.load(value, weights\_only\=False)

Copy to clipboard

Modifying resolve\_tensor and commit\_tensor to handle load time transformation.

\>>> class MetaModelMaterialize(DefaultSavePlanner):
\>>>     def resolve\_tensor(self, read\_item):
\>>>         tensor \= super().resolve\_tensor(read\_item)
\>>>         return torch.empty\_like(tensor, device\="cpu")
\>>>
\>>>     def commit\_tensor(self, read\_item, tensor):
\>>>         self.state\_dict\[read\_item.dest\_index.fqn\] \= tensor

Copy to clipboard

_abstract_ commit\_tensor(_read\_item_, _tensor_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L440)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlanner.commit_tensor "Link to this definition")

Call once the StorageReader finished loading data into `tensor`.

The provided tensor is the same one returned by the call to `resolve_tensor`. This method is only needed if this LoadPlanner needs to post process `tensor` prior to copying it back to the one in the state\_dict.

The contents of tensor will follow its device synchronization model.

_abstract_ create\_global\_plan(_global\_plan_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L399)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlanner.create_global_plan "Link to this definition")

Compute the global load plan and return plans for each rank.

. N.B. This is called on the coordinator rank only

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[_LoadPlan_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlan "torch.distributed.checkpoint.planner.LoadPlan")\
\]

_abstract_ create\_local\_plan()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L391)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlanner.create_local_plan "Link to this definition")

Create a LoadPlan based on state\_dict and metadata provided by set\_up\_planner.

. N.B. This is called on every rank.

Return type:

[_LoadPlan_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlan "torch.distributed.checkpoint.planner.LoadPlan")

_abstract_ finish\_plan(_central\_plan_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L407)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlanner.finish_plan "Link to this definition")

Accept the plan from coordinator and return final LoadPlan.

Return type:

[_LoadPlan_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlan "torch.distributed.checkpoint.planner.LoadPlan")

_abstract_ load\_bytes(_read\_item_, _value_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L411)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlanner.load_bytes "Link to this definition")

Load the item described by `read_item``and ``value`.

This method is expected to modify in-place the underlying state\_dict.

The contents of `value` are defined by the SavePlanner used to produce the checkpoint being loaded.

resolve\_bytes(_read\_item_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L422)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlanner.resolve_bytes "Link to this definition")

Return the BytesIO to be used by the StorageReader to load read\_item.

The BytesIO should alias with one on the underlying state\_dict as StorageReader will replace its contents.

Return type:

_BytesIO_

_abstract_ resolve\_tensor(_read\_item_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L430)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlanner.resolve_tensor "Link to this definition")

Return the tensor described by `read_item` to be used by the StorageReader to load read\_item.

The tensor should alias with one on the underlying state\_dict as StorageReader will replace its contents. If, for any reason, that’s not possible, the planner can use the `commit_tensor` method to copy the data back to the one in state\_dict.

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

_abstract_ set\_up\_planner(_state\_dict_, _metadata\=None_, _is\_coordinator\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L378)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlanner.set_up_planner "Link to this definition")

Initialize this instance to load data into `state_dict`.

. N.B. This is called on every rank.

_class_ torch.distributed.checkpoint.LoadPlan(_items: [list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[torch.distributed.checkpoint.planner.ReadItem](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.ReadItem "torch.distributed.checkpoint.planner.ReadItem")\
\]_, _storage\_data: Any \= None_, _planner\_data: Any \= None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L114)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlan "Link to this definition")

_class_ torch.distributed.checkpoint.ReadItem(_type: torch.distributed.checkpoint.planner.LoadItemType_, _dest\_index: torch.distributed.checkpoint.metadata.MetadataIndex_, _dest\_offsets: [torch.Size](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")
_, _storage\_index: torch.distributed.checkpoint.metadata.MetadataIndex_, _storage\_offsets: [torch.Size](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")
_, _lengths: [torch.Size](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")
_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L85)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.ReadItem "Link to this definition")

_class_ torch.distributed.checkpoint.SavePlanner[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L121)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlanner "Link to this definition")

Abstract class defining the protocol used by save\_state\_dict to plan the save process.

SavePlanners are stateful objects that can be used to customize the whole save process.

SavePlanner acts as an access proxy to the state\_dict, so any transformation done to it will be visible to the whole process.

A planner subclass can expect the following sequence of calls during save\_state\_dict:

1.  set\_up\_planner - called on all ranks.
    
    Signals the start of a checkpoint save.
    
2.  create\_local\_plan - called on all ranks.
    
    Process the state\_dict and produces a SavePlan that will be sent for global planning.
    
3.  create\_global\_plan - called on the coordinator rank only.
    
    Takes the SavePlan from all ranks and make any global decision.
    
4.  finish\_plan - called on all ranks.
    
    This gives each rank a chance to adjust to global planning decisions.
    
5.  resolve\_data - called multiple times on each rank
    
    Lookups a value on the state\_dict for the storage layer to write.
    

Users are recommended to extend DefaultSavePlanner instead of this interface directly as most changes can be expressed by changes in a single method.

There are 3 usual patterns of extension:

Rewriting state\_dict. This is the simplest way to extend the save process as it doesn’t require understanding the intricacies of how SavePlan works:

\>>> class RenamePlanner(DefaultSavePlanner):
\>>>     def set\_up\_planner(
\>>>         self,
\>>>         state\_dict: STATE\_DICT\_TYPE,
\>>>         storage\_meta: Optional\[StorageMeta\],
\>>>         is\_coordinator: bool,
\>>>     ) \-> None:
\>>> \# prefix all keys with \`foo\_\`\`
\>>>         super().set\_up\_planner({"foo\_" + k: v for k, v in state\_dict.items()}, storage\_meta, is\_coordinator)

Copy to clipboard

Modifying local plan and lookup in tandem. This is useful when fine control of how data is persisted

\>>> class FP16Planner(DefaultSavePlanner):
\>>>     def create\_local\_plan(self):
\>>>         plan \= super().create\_local\_plan()
\>>>         for p in plan:
\>>>             if p.tensor\_data is not None:
\>>>                 p.tensor\_data.properties.dtype \= torch.float16
\>>>         return plan
\>>>
\>>>     def resolve\_data(self, write\_item):
\>>>         item \= super().resolve\_data(write\_item)
\>>>         return item if write\_item.type \== WriteItemType.BYTE\_IO else item.to(torch.float16)

Copy to clipboard

Using the global planning step to make central decisions that can’t be made individually by each rank

\>>> from itertools import zip\_longest
\>>> from dataclasses import replace
\>>> class DDPLoadBalancingPlanner(DefaultSavePlanner):
\>>> \# This uses the default local plan behavior of having all non-sharded writes in rank 0
\>>> \# This sample doesn't handle ShardedTensors
\>>>     def create\_global\_plan(self, all\_plans):
\>>>         iters \= \[iter(all\_plans\[0\].items)\] \* len(all\_plans)
\>>>         items\_per\_rank \= \[\
\>>>             \[item for item in items if item is not None\]\
\>>>             for items in zip(\*zip\_longest(\*iters), strict\=True)\
\>>>         \]
\>>>         all\_plans \= \[\
\>>>             replace(plan, items\=items)\
\>>>             for plan, items in zip(all\_plans, items\_per\_rank, strict\=True)\
\>>>         \]
\>>>         return super().create\_global\_plan(all\_plans)

Copy to clipboard

Finally, some planners need to save additional metadata in the checkpoint, this is accomplished by having each rank contribute their data items in the local plan and the global planner aggregate them:

\>>> class SaveExtraDataPlanner(DefaultSavePlanner):
\>>>     def create\_local\_plan(self) \-> SavePlan:
\>>>         plan \= super().create\_local\_plan()
\>>>         return replace(plan, planner\_data\="per-rank-data")
\>>>
\>>>     def create\_global\_plan(self, all\_plans: List\[SavePlan\]) \-> Tuple\[List\[SavePlan\], Metadata\]:
\>>>         global\_plan, metadata \= super().create\_global\_plan(all\_plans)
\>>>         merged\_data \= \[p.planner\_data for p in global\_plan\]
\>>>         metadata \= replace(metadata, planner\_data\=merged\_data)
\>>>         return global\_plan, metadata

Copy to clipboard

_abstract_ create\_global\_plan(_all\_plans_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L265)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlanner.create_global_plan "Link to this definition")

Compute the global checkpoint plan and return the local plan of each rank.

This is called on the coordinator rank only.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[_SavePlan_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlan "torch.distributed.checkpoint.planner.SavePlan")\
\], _Metadata_\]

_abstract_ create\_local\_plan()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L254)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlanner.create_local_plan "Link to this definition")

Compute the save plan for the current rank.

This will be aggregated and passed to create\_global\_plan. Planner specific data can be passed through SavePlan::planner\_data.

This is called on all ranks.

Return type:

[_SavePlan_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlan "torch.distributed.checkpoint.planner.SavePlan")

_abstract_ finish\_plan(_new\_plan_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L275)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlanner.finish_plan "Link to this definition")

Merge the plan created by create\_local\_plan and the result of create\_global\_plan.

This is called on all ranks.

Return type:

[_SavePlan_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlan "torch.distributed.checkpoint.planner.SavePlan")

_abstract_ resolve\_data(_write\_item_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L283)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlanner.resolve_data "Link to this definition")

Transform and prepare `write_item` from `state_dict` for storage, ensuring idempotency and thread-safety.

Lookup the object associated with `write_item` in `state_dict` and apply any transformation (such as serialization) prior to the storage layer consuming it.

Called on each rank multiple times, at least once per WriteItem in the final SavePlan.

This method should be idempotent and thread-save. StorageWriter implementations are free to call it as frequently as they need.

Any transformation that allocates memory should be lazily done when his method is called in order to reduce peak memory required by checkpointing.

When returning tensors, they can be on any device or format, they can be views too. It’s the storage layer responsibility to figure out how to save them.

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 | _BytesIO_

_abstract_ set\_up\_planner(_state\_dict_, _storage\_meta\=None_, _is\_coordinator\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L239)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlanner.set_up_planner "Link to this definition")

Initialize this planner to save `state_dict`.

Implementations should save those values as they won’t be provided later in the save process.

This is called on all ranks.

_class_ torch.distributed.checkpoint.SavePlan(_items: [list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[torch.distributed.checkpoint.planner.WriteItem](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.planner.WriteItem "torch.distributed.checkpoint.planner.WriteItem")\
\]_, _storage\_data: Any \= None_, _planner\_data: Any \= None_, _usable: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L104)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlan "Link to this definition")

_class_ torch.distributed.checkpoint.planner.WriteItem(_index_, _type_, _bytes\_io\_data\=None_, _tensor\_data\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L57)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.planner.WriteItem "Link to this definition")

Dataclass which holds information about what needs to be written to storage.

tensor\_storage\_size()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L70)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.planner.WriteItem.tensor_storage_size "Link to this definition")

Calculates the storage size of the underlying tensor, or None if this is not a tensor write.

Returns:

Optional\[int\] storage size, in bytes of underlying tensor if any.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
 | None

_class_ torch.distributed.checkpoint.planner.BytesIOWriteData(_nbytes: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L45)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.planner.BytesIOWriteData "Link to this definition")

_class_ torch.distributed.checkpoint.planner.TensorWriteData(_chunk: torch.distributed.checkpoint.metadata.ChunkStorageMetadata_, _properties: [torch.distributed.checkpoint.metadata.TensorProperties](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.metadata.TensorProperties "torch.distributed.checkpoint.metadata.TensorProperties")
_, _size: [torch.Size](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")
_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/planner.py#L50)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.planner.TensorWriteData "Link to this definition")

We provide a filesystem based storage layer:

_class_ torch.distributed.checkpoint.filesystem.FileSystemBase[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/filesystem.py#L485)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.filesystem.FileSystemBase "Link to this definition")

_class_ torch.distributed.checkpoint.filesystem.FileSystem[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/filesystem.py#L517)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.filesystem.FileSystem "Link to this definition")

_class_ torch.distributed.checkpoint.filesystem.SerializationFormat(_value_, _names\=None_, _\*_, _module\=None_, _qualname\=None_, _type\=None_, _start\=1_, _boundary\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/filesystem.py#L92)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.filesystem.SerializationFormat "Link to this definition")

_class_ torch.distributed.checkpoint.FileSystemReader(_path_, _\_extension\_registry\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/filesystem.py#L845)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.FileSystemReader "Link to this definition")

_property_ checkpoint\_id_: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 | [PathLike](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.FileSystemReader.checkpoint_id "Link to this definition")

return the checkpoint\_id that will be used to load the checkpoint.

_class_ torch.distributed.checkpoint.FileSystemWriter(_path_, _single\_file\_per\_rank\=True_, _sync\_files\=True_, _thread\_count\=1_, _per\_thread\_copy\_ahead\=10000000_, _cache\_staged\_state\_dict\=False_, _overwrite\=True_, _\_extensions\=None_, _serialization\_format\=SerializationFormat.TORCH\_SAVE_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/filesystem.py#L973)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.FileSystemWriter "Link to this definition")

Basic implementation of StorageWriter using file IO.

This implementation makes the following assumptions and simplifications:

*   The checkpoint path is an empty or non-existing directory.
    
*   File creation is atomic
    

The checkpoint consist of one file per write request plus a global .metadata file with the serialized metadata if rank coordination is enabled. a rank local \_\_{rank}.metadata file with the serialized metadata if rank coordination is NOT enabled.

stage(_state\_dict_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/filesystem.py#L1033)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.FileSystemWriter.stage "Link to this definition")

Override of AsyncStager.stage

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, _StatefulT_ | [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\]

We also provide other storage layers, including ones to interact with HuggingFace safetensors:

.. autoclass:: torch.distributed.checkpoint.HuggingFaceStorageReader :members:

.. autoclass:: torch.distributed.checkpoint.HuggingFaceStorageWriter :members:

.. autoclass:: torch.distributed.checkpoint.QuantizedHuggingFaceStorageReader :members:

We provide default implementations of `LoadPlanner` and `SavePlanner` that can handle all of torch.distributed constructs such as FSDP, DDP, ShardedTensor and DistributedTensor.

_class_ torch.distributed.checkpoint.DefaultSavePlanner(_flatten\_state\_dict\=True_, _flatten\_sharded\_tensors\=True_, _dedup\_replicated\_tensors\=None_, _dedup\_save\_to\_lowest\_rank\=False_, _enable\_plan\_caching\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/default_planner.py#L71)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.DefaultSavePlanner "Link to this definition")

lookup\_object(_index_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/default_planner.py#L279)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.DefaultSavePlanner.lookup_object "Link to this definition")

Extension from the planner interface to make it easy to extend the default planner.

Return type:

[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")

transform\_object(_write\_item_, _object_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/default_planner.py#L283)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.DefaultSavePlanner.transform_object "Link to this definition")

Extension from the planner interface to make it easy to extend the default planner.

_class_ torch.distributed.checkpoint.DefaultLoadPlanner(_flatten\_state\_dict\=True_, _flatten\_sharded\_tensors\=True_, _allow\_partial\_load\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/default_planner.py#L292)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.DefaultLoadPlanner "Link to this definition")

DefaultLoadPlanner that adds multiple features on top of LoadPlanner.

In particular it adds the following:

flatten\_state\_dict: Handle state\_dict with nested dicts flatten\_sharded\_tensors: For FSDP in 2D parallel mode allow\_partial\_load: If False, will raise a runtime error if a key is present in state\_dict, but not in the checkpoint.

lookup\_tensor(_index_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/default_planner.py#L402)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.DefaultLoadPlanner.lookup_tensor "Link to this definition")

Extension from the planner interface to make it easy to extend the default planner.

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

transform\_tensor(_read\_item_, _tensor_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/default_planner.py#L406)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.DefaultLoadPlanner.transform_tensor "Link to this definition")

Extension from the planner interface to make it easy to extend the default planner.

Due to legacy design decisions, the state dictionaries of `FSDP` and `DDP` may have different keys or fully qualified names (e.g., layer1.weight) even when the original unparallelized model is identical. Moreover, `FSDP` offers various types of model state dictionaries, such as full and sharded state dictionaries. Additionally, optimizer state dictionaries employ parameter IDs instead of fully qualified names to identify parameters, potentially causing issues when parallelisms are used (e.g., pipeline parallelism).

To tackle these challenges, we offer a collection of APIs for users to easily manage state\_dicts. `get_model_state_dict()` returns a model state dictionary with keys consistent with those returned by the unparallelized model state dictionary. Similarly, `get_optimizer_state_dict()` provides the optimizer state dictionary with keys uniform across all parallelisms applied. To achieve this consistency, `get_optimizer_state_dict()` converts parameter IDs to fully qualified names identical to those found in the unparallelized model state dictionary.

Note that results returned by these APIs can be used directly with the `torch.distributed.checkpoint.save()` and `torch.distributed.checkpoint.load()` methods without requiring any additional conversions.

`set_model_state_dict()` and `set_optimizer_state_dict()` are provided to load the model and optimizer state\_dict generated by their respective getter APIs.

Note that `set_optimizer_state_dict()` can only be called before `backward()` or after `step()` is called on optimizers.

Note that this feature is experimental, and API signatures might change in the future.

torch.distributed.checkpoint.state\_dict.get\_state\_dict(_model_, _optimizers_, _\*_, _submodules\=None_, _options\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/state_dict.py#L1271)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.state_dict.get_state_dict "Link to this definition")

Return the model state\_dict and optimizers state\_dict.

`get_state_dict` can process any module that is parallelized by PyTorch FSDP/fully\_shard, DDP/replicate, tensor\_parallel/parallelize\_module, and any combination of these parallelisms. The main functions of `get_state_dict` are: 1.) returning a model and optimizer state\_dict that can be resharded with a different number of trainers and/or different parallelisms. 2.) hiding the parallelism-specific state\_dict APIs. Users don’t have to call these APIs. 3.) sanity checking the result state\_dict.

The keys of the result state dictionary are the canonical FQNs (Fully Qualified Names). A canonical FQN refers to the FQN based on a parameter’s position in an nn.Module hierarchy. More specifically, a canonical FQN to a parameter is the FQN returned by `module.named_parameters()` or `module.named_buffers()` when the module is not distributed by any parallelisms. Since the optimizer internally uses parameter IDs to represent a parameter, there will be a conversion from the parameter IDs to the canonical FQNs when calling this API.

`get_state_dict` can also process a module that is not parallelized. In such a case, `get_state_dict` only performs one function – converting the optimizer parameter IDs to the canonical FQNs.

Example

\>>> import torch
\>>> from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
\>>> from torch.nn.parallel import DistributedDataParallel as DDP
\>>> from torch.distributed.checkpoint.state\_dict import get\_state\_dict

Copy to clipboard

\>>> fsdp\_model \= FSDP(copy.deepcopy(model))
\>>> fsdp\_optim \= torch.optim.Adam(model.parameters(), lr\=1e-3)
\>>> ddp\_model \= DDP(copy.deepcopy(model))
\>>> ddp\_optim \= torch.optim.Adam(model.parameters(), lr\=1e-3)

Copy to clipboard

\>>> ddp\_state\_dict, ddp\_optim\_state\_dict \= get\_state\_dict(ddp\_model, ddp\_optim)
\>>> fsdp\_state\_dict, fsdp\_optim\_state\_dict \= get\_state\_dict(
...     fsdp\_model, fsdp\_optim
... )

Copy to clipboard

\>>> \# if we simply call ddp\_model.state\_dict() and fsdp\_model.state\_dict(),
\>>> \# the asserts will fail.
\>>> assert ddp\_state\_dict \== fsdp\_state\_dict
\>>> assert ddp\_optim\_state \== fsdp\_optim\_state\_dict

Copy to clipboard

Parameters:

*   **model** ([_nn.Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
    ) – the nn.Module to the model.
    
*   **optimizers** (_Union__\[__None__,_ [_Optimizer_](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.Optimizer")\
    _,_ _Iterable__\[_[_Optimizer_](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.Optimizer")\
    _\]__\]_) – The optimizers that are used to optimize `model`.
    
*   **submodules** (_deprecated_) – Optional\[set\[nn.Module\]\]: only return the model parameters that belong to the submodules.
    
*   **options** ([_StateDictOptions_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.state_dict.StateDictOptions "torch.distributed.checkpoint.state_dict.StateDictOptions")
    ) – the options to control how model state\_dict and optimizer state\_dict should be returned. See StateDictOptions for the details.
    

Returns:

`Tuple` that contain model state\_dict and optimizer state\_dict.

Return type:

[_Tuple_](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.15)")
\[[_Dict_](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, ValueType\], OptimizerStateType\]

torch.distributed.checkpoint.state\_dict.get\_model\_state\_dict(_model_, _\*_, _submodules\=None_, _options\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/state_dict.py#L1189)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.state_dict.get_model_state_dict "Link to this definition")

Return the model state\_dict of `model`.

See `get_state_dict` for the detail usage.

Parameters:

*   **model** ([_nn.Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
    ) – the nn.Module to the model.
    
*   **submodules** (_deprecated_) – Optional\[set\[nn.Module\]\]: only return the model parameters that belong to the submodules.
    
*   **options** ([_StateDictOptions_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.state_dict.StateDictOptions "torch.distributed.checkpoint.state_dict.StateDictOptions")
    ) – the options to control how model state\_dict and optimizer state\_dict should be returned. See StateDictOptions for the details.
    

Returns:

The state\_dict for `model`.

Return type:

[_Dict_](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, ValueType\]

torch.distributed.checkpoint.state\_dict.get\_optimizer\_state\_dict(_model_, _optimizers_, _\*_, _submodules\=None_, _options\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/state_dict.py#L1226)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.state_dict.get_optimizer_state_dict "Link to this definition")

Return the combined state\_dict for optimizers.

See `get_state_dict` for the detail usage.

Parameters:

*   **model** ([_nn.Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
    ) – the nn.Module to the model.
    
*   **optimizers** (_Union__\[__None__,_ [_Optimizer_](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.Optimizer")\
    _,_ _Iterable__\[_[_Optimizer_](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.Optimizer")\
    _\]__\]_) – The optimizers that are used to optimize `model`.
    
*   **submodules** (_deprecated_) – Optional\[set\[nn.Module\]\]: only return the model parameters that belong to the submodules.
    
*   **options** ([_StateDictOptions_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.state_dict.StateDictOptions "torch.distributed.checkpoint.state_dict.StateDictOptions")
    ) – the options to control how model state\_dict and optimizer state\_dict should be returned. See StateDictOptions for the details.
    

Returns:

The state\_dict for `optimizers`.

Return type:

OptimizerStateType

torch.distributed.checkpoint.state\_dict.set\_state\_dict(_model_, _optimizers_, _\*_, _model\_state\_dict_, _optim\_state\_dict_, _options\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/state_dict.py#L1481)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.state_dict.set_state_dict "Link to this definition")

Load the model state\_dict and optimizers state\_dict.

The counterpart of `get_state_dict` to set the state\_dict to the model and optimizers. The given `model_state_dict` and `optim_state_dict` do not have to be returned by `get_state_dict` but must meet the following requirements: 1) all FQNs are canonical FQNs as defined in `get_state_dict`, 2) if a tensor is sharded, it must be either a ShardedTensor or DTensor, 3) optimizer state\_dict cannot contain the parameter IDs; the keys should be the canonical FQNs.

WARN: `set_state_dict` can only be called before `backward()` or after `step()`

is called on the optimizers. Otherwise, the optimizer states won’t be initialized correctly.

Parameters:

*   **model** ([_nn.Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
    ) – the nn.Module to the model.
    
*   **optimizers** (_Union__\[_[_Optimizer_](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.Optimizer")\
    _,_ _Iterable__\[_[_Optimizer_](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.Optimizer")\
    _\]__\]_) – The optimizers that are used to optimize `model`.
    
*   **model\_state\_dict** ([_Dict_](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _ValueType__\]_) – (Union\[Dict\[nn.Module, Dict\[str, ValueType\]\], Dict\[str, ValueType\]\]): the model state\_dict to load. If the key of the `model_state_dict` is nn.Module, the key is a submodule of `model` and the value should be the state\_dict of the submodule. When loading the state\_dict, the prefix of the submodule will be append to the state\_dict.
    
*   **optim\_state\_dict** (_OptimizerStateType_) – OptimizerStateType: the optimizer state\_dict to load.
    
*   **options** ([_StateDictOptions_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.state_dict.StateDictOptions "torch.distributed.checkpoint.state_dict.StateDictOptions")
    ) – the options to control how model state\_dict and optimizer state\_dict should be loaded. See StateDictOptions for the details.
    

Returns:

*   **missing\_keys** is a list of str containing the missing keys of the model state\_dict.
    
*   **unexpected\_keys** is a list of str containing the unexpected keys of the model state\_dict.
    

Return type:

`NamedTuple` with `missing_keys` and `unexpected_keys` fields

torch.distributed.checkpoint.state\_dict.set\_model\_state\_dict(_model_, _model\_state\_dict_, _\*_, _options\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/state_dict.py#L1399)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.state_dict.set_model_state_dict "Link to this definition")

Load the model state\_dict.

The counterpart of `get_model_state_dict` to set the state\_dict to the model. See `set_state_dict` for the detail usage.

Parameters:

*   **model** ([_nn.Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
    ) – the nn.Module to the model.
    
*   **model\_state\_dict** ([_Dict_](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _ValueType__\]_) – (Dict\[str, ValueType\]): the model state\_dict to load. If the key of the `model_state_dict` is nn.Module, the key is a submodule of `model` and the value should be the state\_dict of the submodule. When loading the state\_dict, the prefix of the submodule will be append to the state\_dict.
    
*   **options** ([_StateDictOptions_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.state_dict.StateDictOptions "torch.distributed.checkpoint.state_dict.StateDictOptions")
    ) – the options to control how model state\_dict and optimizer state\_dict should be loaded. See StateDictOptions for the details.
    

Returns:

*   **missing\_keys** is a list of str containing the missing keys
    
*   **unexpected\_keys** is a list of str containing the unexpected keys
    

Return type:

`NamedTuple` with `missing_keys` and `unexpected_keys` fields

torch.distributed.checkpoint.state\_dict.set\_optimizer\_state\_dict(_model_, _optimizers_, _optim\_state\_dict_, _\*_, _options\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/state_dict.py#L1438)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.state_dict.set_optimizer_state_dict "Link to this definition")

Load the optimizers state\_dict.

The counterpart of `get_optimizer_state_dict` to set the state\_dict to the optimizers. See `set_state_dict` for the detail usage.

WARN: `set_optimizer_state_dict` can only be called before `backward()` or after

`step()` is called on the optimizers. Otherwise, the optimizer states won’t be initialized correctly.

Parameters:

*   **model** ([_nn.Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
    ) – the nn.Module to the model.
    
*   **optimizers** (_Union__\[_[_Optimizer_](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.Optimizer")\
    _,_ _Iterable__\[_[_Optimizer_](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.Optimizer")\
    _\]__\]_) – The optimizers that are used to optimize `model`.
    
*   **optim\_state\_dict** (_OptimizerStateType_) – OptimizerStateType: the optimizer state\_dict to load.
    
*   **options** ([_StateDictOptions_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.state_dict.StateDictOptions "torch.distributed.checkpoint.state_dict.StateDictOptions")
    ) – the options to control how model state\_dict and optimizer state\_dict should be loaded. See StateDictOptions for the details.
    

Returns:

None

Return type:

None

_class_ torch.distributed.checkpoint.state\_dict.StateDictOptions(_full\_state\_dict\=False_, _cpu\_offload\=False_, _ignore\_frozen\_params\=False_, _keep\_submodule\_prefixes\=True_, _strict\=True_, _broadcast\_from\_rank0\=False_, _flatten\_optimizer\_state\_dict\=False_, _dsd\_fqn\_modifiers\='\_fqn\_modifiers'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/state_dict.py#L93)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.state_dict.StateDictOptions "Link to this definition")

This dataclass specifies how get\_state\_dict/set\_state\_dict will work.

*   `full_state_dict`: if this is set to True, all the tensors in the returned state\_dict will be gathered. No ShardedTensor and DTensor will be in the returned state\_dict.
    
*   `cpu_offload`: offload all the tensors to cpu. To prevent CPU OOM, if `full_state_dict` is also true, then only the rank0 will get the state\_dict and all other ranks will get empty state\_dict.
    
*   `ignore_frozen_params`: if the value is True, the returned state\_dict won’t contain any frozen parameters – the `requires_grad` is False. The default value is False.
    
*   `keep_submodule_prefixes` (deprecated): when `submodules` is not None, this option indicates whether to keep the submodule prefixes from the state\_dict keys. or example, if the submodule is `module.pretrain` and the full FQN of the parameter is `pretrain.layer1.weight` of the param. When this option is True, the parameter’s key in the returned state\_dict will be `pretrain.layer1.weight`. If the options is False, the key will be `layer1.weight`. Note that if `keep_submodule_prefixes` is False, there may be conflicted FQNs, hence there should be only one submodule in `submodules`.
    
*   `strict`: the `strict` option when `set_state_dict` calls model.load\_state\_dict().
    
*   `broadcast_from_rank0`: when the option is True, rank0 should receive a
    
    full state\_dict and will broadcast the tensors in the state\_dict/ optim\_state\_dict one by one to other ranks. Other ranks will receive the tensors and shard according to the local shards in the model and optimizer. `full_state_dict` must be set to True when using this option. This option currently only supports DTensor, not the legacy ShardedTensor.
    

For users which are used to using and sharing models in the `torch.save` format, the following methods are provided which provide offline utilities for converting between formats.

torch.distributed.checkpoint.format\_utils.dcp\_to\_torch\_save(_dcp\_checkpoint\_dir_, _torch\_save\_path_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/format_utils.py#L208)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.format_utils.dcp_to_torch_save "Link to this definition")

Given a directory containing a DCP checkpoint, this function will convert it into a Torch save file.

Parameters:

*   **dcp\_checkpoint\_dir** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ [_PathLike_](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.15)")
    ) – Directory containing the DCP checkpoint.
    
*   **torch\_save\_path** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ [_PathLike_](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.15)")
    ) – Filename to store the converted Torch save file.
    

Warning

To avoid OOM, it’s recommended to only run this function on a single rank.

torch.distributed.checkpoint.format\_utils.torch\_save\_to\_dcp(_torch\_save\_path_, _dcp\_checkpoint\_dir_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/format_utils.py#L233)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.format_utils.torch_save_to_dcp "Link to this definition")

Given the location of a torch save file, converts it into a DCP checkpoint.

Parameters:

*   **torch\_save\_path** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ [_PathLike_](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.15)")
    ) – Filename of the Torch save file.
    
*   **dcp\_checkpoint\_dir** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ [_PathLike_](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.15)")
    ) – Directory to store the DCP checkpoint.
    

Warning

To avoid OOM, it’s recommended to only run this function on a single rank.

The following classes can also be utilized for online loading and resharding of models from the torch.save format.

_class_ torch.distributed.checkpoint.format\_utils.BroadcastingTorchSaveReader(_checkpoint\_id\=None_, _coordinator\_rank\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/format_utils.py#L39)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.format_utils.BroadcastingTorchSaveReader "Link to this definition")

StorageReader for reading a Torch Save file. This reader will read the entire checkpoint on the coordinator rank, and then broadcast and shard each tensor to all ranks.

. N.B. Intended to be used with DynamicMetaLoadPlanner

Warning

Current implementation only supports loading Tensors.

\>>> sd \= {"mode": model}
\>>> dcp.load(
\>>>    sd,
\>>>    storage\_reader\=BroadcastingTorchSaveReader(),
\>>>    planner\=DynamicMetaLoadPlanner(),
\>>>    checkpoint\_id\="path\_to\_model.pt"
\>>> )

Copy to clipboard

prepare\_global\_plan(_global\_plan_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/format_utils.py#L148)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.format_utils.BroadcastingTorchSaveReader.prepare_global_plan "Link to this definition")

Implementation of the StorageReader method

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[_LoadPlan_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlan "torch.distributed.checkpoint.planner.LoadPlan")\
\]

prepare\_local\_plan(_plan_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/format_utils.py#L144)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.format_utils.BroadcastingTorchSaveReader.prepare_local_plan "Link to this definition")

Implementation of the StorageReader method

Return type:

[_LoadPlan_](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlan "torch.distributed.checkpoint.planner.LoadPlan")

read\_data(_plan_, _planner_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/format_utils.py#L74)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.format_utils.BroadcastingTorchSaveReader.read_data "Link to this definition")

Reads torch save data on the coordinator rank, and broadcast afterwards this incurrs a communication cost, but avoids having to load the entire checkpoint on each rank, hopefully preventing OOM issues

Return type:

[_Future_](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.jit.Future")
\[None\]

read\_metadata()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/format_utils.py#L68)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.format_utils.BroadcastingTorchSaveReader.read_metadata "Link to this definition")

Extends the default StorageReader to support building the metadata file

Return type:

_Metadata_

reset(_checkpoint\_id\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/format_utils.py#L152)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.format_utils.BroadcastingTorchSaveReader.reset "Link to this definition")

Implementation of the StorageReader method

set\_up\_storage\_reader(_metadata_, _is\_coordinator_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/format_utils.py#L129)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.format_utils.BroadcastingTorchSaveReader.set_up_storage_reader "Link to this definition")

Implementation of the StorageReader method

_classmethod_ validate\_checkpoint\_id(_checkpoint\_id_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/format_utils.py#L156)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.format_utils.BroadcastingTorchSaveReader.validate_checkpoint_id "Link to this definition")

Implementation of the StorageReader method

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

_class_ torch.distributed.checkpoint.format\_utils.DynamicMetaLoadPlanner(_flatten\_state\_dict\=True_, _flatten\_sharded\_tensors\=True_, _allow\_partial\_load\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/format_utils.py#L162)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.format_utils.DynamicMetaLoadPlanner "Link to this definition")

Extension of DefaultLoadPlanner, which creates a new Metadata object based on the passed in state dict, avoiding the need to read metadata from disk. This is useful when reading formats which don’t have a metadata file, like Torch Save files.

. N.B. Intended to be used with BroadcastingTorchSaveReader

Warning

Current implementation only supports loading Tensors.

\>>> sd \= {"mode": model}
\>>> dcp.load(
\>>>    sd,
\>>>    storage\_reader\=BroadcastingTorchSaveReader(),
\>>>    planner\=DynamicMetaLoadPlanner(),
\>>>    checkpoint\_id\="path\_to\_model.pt"
\>>> )

Copy to clipboard

set\_up\_planner(_state\_dict_, _metadata\=None_, _is\_coordinator\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/checkpoint/format_utils.py#L183)
[#](https://docs.pytorch.org/docs/2.15/distributed.checkpoint.html#torch.distributed.checkpoint.format_utils.DynamicMetaLoadPlanner.set_up_planner "Link to this definition")

Setups of the planner, extnding default behavior by creating the Metadata object from the state dict

The following experimental interfaces are provided for improved observability in production environments:

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/distributed.checkpoint.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/distributed.checkpoint.md.txt)

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