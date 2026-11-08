Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/rpc.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/rpc.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/rpc.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/rpc.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/rpc.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/rpc.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/rpc.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/rpc.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/rpc.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/rpc.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/rpc.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/rpc.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/rpc.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/rpc.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/rpc.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/rpc.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/rpc.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/rpc.html)
[v1.13](https://docs.pytorch.org/docs/1.13/rpc.html)
[v1.12](https://docs.pytorch.org/docs/1.12/rpc.html)
[v1.11](https://docs.pytorch.org/docs/1.11/rpc.html)
[v1.10](https://docs.pytorch.org/docs/1.10/rpc.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/rpc.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/rpc.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/rpc.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/rpc.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/rpc.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/rpc.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/rpc.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/rpc.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/rpc.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/rpc.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/rpc.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/rpc.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/rpc.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/rpc.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/rpc.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/rpc.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/rpc.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/rpc.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/rpc.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/rpc.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/rpc.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/rpc.html)

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

Distributed RPC Framework[#](https://docs.pytorch.org/docs/2.15/rpc.html#distributed-rpc-framework "Link to this heading")

===========================================================================================================================

Created On: Nov 14, 2019 | Last Updated On: May 14, 2026

The distributed RPC framework provides mechanisms for multi-machine model training through a set of primitives to allow for remote communication, and a higher-level API to automatically differentiate models split across several machines.

Warning

APIs in the RPC package are stable and in maintenance mode.

Warning

CUDA support is a **beta** feature. Not all features of the RPC package are yet compatible with CUDA support and thus their use is discouraged. These unsupported features include: RRefs, JIT compatibility, dist autograd and dist optimizer, and profiling.

Note

Please refer to `PyTorch Distributed Overview <https://pytorch.org/tutorials/beginner/dist_overview.html>`\_\_ for a brief introduction to all features related to distributed training.

Basics[#](https://docs.pytorch.org/docs/2.15/rpc.html#basics "Link to this heading")

-------------------------------------------------------------------------------------

The distributed RPC framework makes it easy to run functions remotely, supports referencing remote objects without copying the real data around, and provides autograd and optimizer APIs to transparently run backward and update parameters across RPC boundaries. These features can be categorized into four sets of APIs.

1.  **Remote Procedure Call (RPC)** supports running a function on the specified destination worker with the given arguments and getting the return value back or creating a reference to the return value. There are three main RPC APIs: [`rpc_sync()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.rpc_sync "torch.distributed.rpc.rpc_sync")
     (synchronous), [`rpc_async()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.rpc_async "torch.distributed.rpc.rpc_async")
     (asynchronous), and [`remote()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.remote "torch.distributed.rpc.remote")
     (asynchronous and returns a reference to the remote return value). Use the synchronous API if the user code cannot proceed without the return value. Otherwise, use the asynchronous API to get a future, and wait on the future when the return value is needed on the caller. The [`remote()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.remote "torch.distributed.rpc.remote")
     API is useful when the requirement is to create something remotely but never need to fetch it to the caller. Imagine the case that a driver process is setting up a parameter server and a trainer. The driver can create an embedding table on the parameter server and then share the reference to the embedding table with the trainer, but itself will never use the embedding table locally. In this case, [`rpc_sync()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.rpc_sync "torch.distributed.rpc.rpc_sync")
     and [`rpc_async()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.rpc_async "torch.distributed.rpc.rpc_async")
     are no longer appropriate, as they always imply that the return value will be returned to the caller immediately or in the future.
    
2.  **Remote Reference (RRef)** serves as a distributed shared pointer to a local or remote object. It can be shared with other workers and reference counting will be handled transparently. Each RRef only has one owner and the object only lives on that owner. Non-owner workers holding RRefs can get copies of the object from the owner by explicitly requesting it. This is useful when a worker needs to access some data object, but itself is neither the creator (the caller of [`remote()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.remote "torch.distributed.rpc.remote")
    ) or the owner of the object. The distributed optimizer, as we will discuss below, is one example of such use cases.
    
3.  **Distributed Autograd** stitches together local autograd engines on all the workers involved in the forward pass, and automatically reach out to them during the backward pass to compute gradients. This is especially helpful if the forward pass needs to span multiple machines when conducting, e.g., distributed model parallel training, parameter-server training, etc. With this feature, user code no longer needs to worry about how to send gradients across RPC boundaries and in which order should the local autograd engines be launched, which can become quite complicated where there are nested and inter-dependent RPC calls in the forward pass.
    
4.  **Distributed Optimizer**’s constructor takes a [`Optimizer()`](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.Optimizer")
     (e.g., [`SGD()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.SGD.html#torch.optim.SGD "torch.optim.SGD")
    , [`Adagrad()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Adagrad.html#torch.optim.Adagrad "torch.optim.Adagrad")
    , etc.) and a list of parameter RRefs, creates an [`Optimizer()`](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.Optimizer")
     instance on each distinct RRef owner, and updates parameters accordingly when running `step()`. When you have distributed forward and backward passes, parameters and gradients will be scattered across multiple workers, and hence it requires an optimizer on each of the involved workers. Distributed Optimizer wraps all those local optimizers into one, and provides a concise constructor and `step()` API.
    

RPC[#](https://docs.pytorch.org/docs/2.15/rpc.html#rpc "Link to this heading")

-------------------------------------------------------------------------------

Before using RPC and distributed autograd primitives, initialization must take place. To initialize the RPC framework we need to use [`init_rpc()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.init_rpc "torch.distributed.rpc.init_rpc")
 which would initialize the RPC framework, RRef framework and distributed autograd.

torch.distributed.rpc.init\_rpc(_name_, _backend\=None_, _rank\=\-1_, _world\_size\=None_, _rpc\_backend\_options\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/rpc/__init__.py#L93)
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.init_rpc "Link to this definition")

Initializes RPC primitives such as the local RPC agent and distributed autograd, which immediately makes the current process ready to send and receive RPCs.

Parameters:

*   **name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – a globally unique name of this node. (e.g., `Trainer3`, `ParameterServer2`, `Master`, `Worker1`) Name can only contain number, alphabet, underscore, colon, and/or dash, and must be shorter than 128 characters.
    
*   **backend** ([_BackendType_](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.BackendType "torch.distributed.rpc.BackendType")
    _,_ _optional_) – The type of RPC backend implementation. Supported values is `BackendType.TENSORPIPE` (the default). See [Backends](https://docs.pytorch.org/docs/2.15/rpc.html#rpc-backends)
     for more information.
    
*   **rank** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – a globally unique id/rank of this node.
    
*   **world\_size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The number of workers in the group.
    
*   **rpc\_backend\_options** ([_RpcBackendOptions_](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.RpcBackendOptions "torch.distributed.rpc.RpcBackendOptions")
    _,_ _optional_) – The options passed to the RpcAgent constructor. It must be an agent-specific subclass of [`RpcBackendOptions`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.RpcBackendOptions "torch.distributed.rpc.RpcBackendOptions")
     and contains agent-specific initialization configurations. By default, for all agents, it sets the default timeout to 60 seconds and performs the rendezvous with an underlying process group initialized using `init_method = "env://"`, meaning that environment variables `MASTER_ADDR` and `MASTER_PORT` need to be set properly. See [Backends](https://docs.pytorch.org/docs/2.15/rpc.html#rpc-backends)
     for more information and find which options are available.
    

torch.distributed.rpc.is\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/rpc/__init__.py#L24)
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.is_available "Link to this definition")

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

The following APIs allow users to remotely execute functions as well as create references (RRefs) to remote data objects. In these APIs, when passing a `Tensor` as an argument or a return value, the destination worker will try to create a `Tensor` with the same meta (i.e., shape, stride, etc.). We intentionally disallow transmitting CUDA tensors because it might crash if the device lists on source and destination workers do not match. In such cases, applications can always explicitly move the input tensors to CPU on the caller and move it to the desired devices on the callee if necessary.

torch.distributed.rpc.rpc\_sync(_to_, _func_, _args\=None_, _kwargs\=None_, _timeout\=\-1.0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/rpc/api.py#L771)
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.rpc_sync "Link to this definition")

Make a blocking RPC call to run function `func` on worker `to`. RPC messages are sent and received in parallel to execution of Python code. This method is thread-safe.

Parameters:

*   **to** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _or_ [_WorkerInfo_](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.WorkerInfo "torch.distributed.rpc.WorkerInfo")
     _or_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – name/rank/`WorkerInfo` of the destination worker.
    
*   **func** (_Callable_) – a callable function, such as Python callables, builtin operators (e.g. [`add()`](https://docs.pytorch.org/docs/2.15/generated/torch.add.html#torch.add "torch.add")
    ) and annotated TorchScript functions.
    
*   **args** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    ) – the argument tuple for the `func` invocation.
    
*   **kwargs** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    ) – is a dictionary of keyword arguments for the `func` invocation.
    
*   **timeout** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    _,_ _optional_) – timeout in seconds to use for this RPC. If the RPC does not complete in this amount of time, an exception indicating it has timed out will be raised. A value of 0 indicates an infinite timeout, i.e. a timeout error will never be raised. If not provided, the default value set during initialization or with `_set_rpc_timeout` is used.
    

Returns:

Returns the result of running `func` with `args` and `kwargs`.

Example::

Make sure that `MASTER_ADDR` and `MASTER_PORT` are set properly on both workers. Refer to [`init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")
 API for more details. For example,

export MASTER\_ADDR=localhost export MASTER\_PORT=5678

Then run the following code in two different processes:

\>>> \# On worker 0:
\>>> import torch
\>>> import torch.distributed.rpc as rpc
\>>> rpc.init\_rpc("worker0", rank\=0, world\_size\=2)
\>>> ret \= rpc.rpc\_sync("worker1", torch.add, args\=(torch.ones(2), 3))
\>>> rpc.shutdown()

Copy to clipboard

\>>> \# On worker 1:
\>>> import torch.distributed.rpc as rpc
\>>> rpc.init\_rpc("worker1", rank\=1, world\_size\=2)
\>>> rpc.shutdown()

Copy to clipboard

Below is an example of running a TorchScript function using RPC.

\>>> \# On both workers:
\>>> @torch.jit.script
\>>> def my\_script\_add(tensor: torch.Tensor, scalar: int):
\>>>    return torch.add(tensor, scalar)

Copy to clipboard

\>>> \# On worker 0:
\>>> import torch.distributed.rpc as rpc
\>>> rpc.init\_rpc("worker0", rank\=0, world\_size\=2)
\>>> ret \= rpc.rpc\_sync("worker1", my\_script\_add, args\=(torch.ones(2), 3))
\>>> rpc.shutdown()

Copy to clipboard

\>>> \# On worker 1:
\>>> import torch.distributed.rpc as rpc
\>>> rpc.init\_rpc("worker1", rank\=1, world\_size\=2)
\>>> rpc.shutdown()

Copy to clipboard

torch.distributed.rpc.rpc\_async(_to_, _func_, _args\=None_, _kwargs\=None_, _timeout\=\-1.0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/rpc/api.py#L845)
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.rpc_async "Link to this definition")

Make a non-blocking RPC call to run function `func` on worker `to`. RPC messages are sent and received in parallel to execution of Python code. This method is thread-safe. This method will immediately return a [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 that can be awaited on.

Parameters:

*   **to** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _or_ [_WorkerInfo_](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.WorkerInfo "torch.distributed.rpc.WorkerInfo")
     _or_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – name/rank/`WorkerInfo` of the destination worker.
    
*   **func** (_Callable_) – a callable function, such as Python callables, builtin operators (e.g. [`add()`](https://docs.pytorch.org/docs/2.15/generated/torch.add.html#torch.add "torch.add")
    ) and annotated TorchScript functions.
    
*   **args** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    ) – the argument tuple for the `func` invocation.
    
*   **kwargs** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    ) – is a dictionary of keyword arguments for the `func` invocation.
    
*   **timeout** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    _,_ _optional_) – timeout in seconds to use for this RPC. If the RPC does not complete in this amount of time, an exception indicating it has timed out will be raised. A value of 0 indicates an infinite timeout, i.e. a timeout error will never be raised. If not provided, the default value set during initialization or with `_set_rpc_timeout` is used.
    

Returns:

Returns a [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 object that can be waited on. When completed, the return value of `func` on `args` and `kwargs` can be retrieved from the [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 object.

Warning

Using GPU tensors as arguments or return values of `func` is not supported since we don’t support sending GPU tensors over the wire. You need to explicitly copy GPU tensors to CPU before using them as arguments or return values of `func`.

Warning

The `rpc_async` API does not copy storages of argument tensors until sending them over the wire, which could be done by a different thread depending on the RPC backend type. The caller should make sure that the contents of those tensors stay intact until the returned [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 completes.

Example::

Make sure that `MASTER_ADDR` and `MASTER_PORT` are set properly on both workers. Refer to [`init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")
 API for more details. For example,

export MASTER\_ADDR=localhost export MASTER\_PORT=5678

Then run the following code in two different processes:

\>>> \# On worker 0:
\>>> import torch
\>>> import torch.distributed.rpc as rpc
\>>> rpc.init\_rpc("worker0", rank\=0, world\_size\=2)
\>>> fut1 \= rpc.rpc\_async("worker1", torch.add, args\=(torch.ones(2), 3))
\>>> fut2 \= rpc.rpc\_async("worker1", min, args\=(1, 2))
\>>> result \= fut1.wait() + fut2.wait()
\>>> rpc.shutdown()

Copy to clipboard

\>>> \# On worker 1:
\>>> import torch.distributed.rpc as rpc
\>>> rpc.init\_rpc("worker1", rank\=1, world\_size\=2)
\>>> rpc.shutdown()

Copy to clipboard

Below is an example of running a TorchScript function using RPC.

\>>> \# On both workers:
\>>> @torch.jit.script
\>>> def my\_script\_add(tensor: torch.Tensor, scalar: int):
\>>>    return torch.add(tensor, scalar)

Copy to clipboard

\>>> \# On worker 0:
\>>> import torch.distributed.rpc as rpc
\>>> rpc.init\_rpc("worker0", rank\=0, world\_size\=2)
\>>> fut \= rpc.rpc\_async("worker1", my\_script\_add, args\=(torch.ones(2), 3))
\>>> ret \= fut.wait()
\>>> rpc.shutdown()

Copy to clipboard

\>>> \# On worker 1:
\>>> import torch.distributed.rpc as rpc
\>>> rpc.init\_rpc("worker1", rank\=1, world\_size\=2)
\>>> rpc.shutdown()

Copy to clipboard

torch.distributed.rpc.remote(_to_, _func_, _args\=None_, _kwargs\=None_, _timeout\=\-1.0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/rpc/api.py#L554)
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.remote "Link to this definition")

Make a remote call to run `func` on worker `to` and return an `RRef` to the result value immediately. Worker `to` will be the owner of the returned `RRef`, and the worker calling `remote` is a user. The owner manages the global reference count of its `RRef`, and the owner `RRef` is only destructed when globally there are no living references to it.

Parameters:

*   **to** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _or_ [_WorkerInfo_](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.WorkerInfo "torch.distributed.rpc.WorkerInfo")
     _or_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – name/rank/`WorkerInfo` of the destination worker.
    
*   **func** (_Callable_) – a callable function, such as Python callables, builtin operators (e.g. [`add()`](https://docs.pytorch.org/docs/2.15/generated/torch.add.html#torch.add "torch.add")
    ) and annotated TorchScript functions.
    
*   **args** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    ) – the argument tuple for the `func` invocation.
    
*   **kwargs** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    ) – is a dictionary of keyword arguments for the `func` invocation.
    
*   **timeout** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    _,_ _optional_) – timeout in seconds for this remote call. If the creation of this `RRef` on worker `to` is not successfully processed on this worker within this timeout, then the next time there is an attempt to use the RRef (such as `to_here()`), a timeout will be raised indicating this failure. A value of 0 indicates an infinite timeout, i.e. a timeout error will never be raised. If not provided, the default value set during initialization or with `_set_rpc_timeout` is used.
    

Returns:

A user `RRef` instance to the result value. Use the blocking API `torch.distributed.rpc.RRef.to_here()` to retrieve the result value locally.

Warning

The `remote` API does not copy storages of argument tensors until sending them over the wire, which could be done by a different thread depending on the RPC backend type. The caller should make sure that the contents of those tensors stay intact until the returned RRef is confirmed by the owner, which can be checked using the `torch.distributed.rpc.RRef.confirmed_by_owner()` API.

Warning

Errors such as timeouts for the `remote` API are handled on a best-effort basis. This means that when remote calls initiated by `remote` fail, such as with a timeout error, we take a best-effort approach to error handling. This means that errors are handled and set on the resulting RRef on an asynchronous basis. If the RRef has not been used by the application before this handling (such as `to_here` or fork call), then future uses of the `RRef` will appropriately raise errors. However, it is possible that the user application will use the `RRef` before the errors are handled. In this case, errors may not be raised as they have not yet been handled.

Example:

Make sure that \`\`MASTER\_ADDR\`\` and \`\`MASTER\_PORT\`\` are set properly
on both workers. Refer to :meth:\`~torch.distributed.init\_process\_group\`
API for more details. For example,

export MASTER\_ADDR=localhost
export MASTER\_PORT=5678

Then run the following code in two different processes:

>>> # On worker 0:
>>> import torch
>>> import torch.distributed.rpc as rpc
>>> rpc.init\_rpc("worker0", rank=0, world\_size=2)
>>> rref1 = rpc.remote("worker1", torch.add, args=(torch.ones(2), 3))
>>> rref2 = rpc.remote("worker1", torch.add, args=(torch.ones(2), 1))
>>> x = rref1.to\_here() + rref2.to\_here()
>>> rpc.shutdown()

>>> # On worker 1:
>>> import torch.distributed.rpc as rpc
>>> rpc.init\_rpc("worker1", rank=1, world\_size=2)
>>> rpc.shutdown()

Below is an example of running a TorchScript function using RPC.

>>> # On both workers:
>>> @torch.jit.script
>>> def my\_script\_add(tensor: torch.Tensor, scalar: int):
>>>    return torch.add(tensor, scalar)

>>> # On worker 0:
>>> import torch.distributed.rpc as rpc
>>> rpc.init\_rpc("worker0", rank=0, world\_size=2)
>>> rref = rpc.remote("worker1", my\_script\_add, args=(torch.ones(2), 3))
>>> rref.to\_here()
>>> rpc.shutdown()

>>> # On worker 1:
>>> import torch.distributed.rpc as rpc
>>> rpc.init\_rpc("worker1", rank=1, world\_size=2)
>>> rpc.shutdown()

Copy to clipboard

torch.distributed.rpc.get\_worker\_info(_worker\_name\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/rpc/api.py#L427)
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.get_worker_info "Link to this definition")

Get [`WorkerInfo`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.WorkerInfo "torch.distributed.rpc.WorkerInfo")
 of a given worker name. Use this [`WorkerInfo`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.WorkerInfo "torch.distributed.rpc.WorkerInfo")
 to avoid passing an expensive string on every invocation.

Parameters:

**worker\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – the string name of a worker. If `None`, return the id of the current worker. (default `None`)

Returns:

[`WorkerInfo`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.WorkerInfo "torch.distributed.rpc.WorkerInfo")
 instance for the given `worker_name` or [`WorkerInfo`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.WorkerInfo "torch.distributed.rpc.WorkerInfo")
 of the current worker if `worker_name` is `None`.

torch.distributed.rpc.shutdown(_graceful\=True_, _timeout\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/rpc/api.py#L326)
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.shutdown "Link to this definition")

Perform a shutdown of the RPC agent, and then destroy the RPC agent. This stops the local agent from accepting outstanding requests, and shuts down the RPC framework by terminating all RPC threads. If `graceful=True`, this will block until all local and remote RPC processes reach this method and wait for all outstanding work to complete. Otherwise, if `graceful=False`, this is a local shutdown, and it does not wait for other RPC processes to reach this method.

Warning

For [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 objects returned by [`rpc_async()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.rpc_async "torch.distributed.rpc.rpc_async")
, `future.wait()` should not be called after `shutdown()`.

Parameters:

**graceful** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
) – Whether to do a graceful shutdown or not. If True, this will 1) wait until there is no pending system messages for `UserRRefs` and delete them; 2) block until all local and remote RPC processes have reached this method and wait for all outstanding work to complete.

Example::

Make sure that `MASTER_ADDR` and `MASTER_PORT` are set properly on both workers. Refer to [`init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")
 API for more details. For example,

export MASTER\_ADDR=localhost export MASTER\_PORT=5678

Then run the following code in two different processes:

\>>> \# On worker 0:
\>>> import torch
\>>> import torch.distributed.rpc as rpc
\>>> rpc.init\_rpc("worker0", rank\=0, world\_size\=2)
\>>> \# do some work
\>>> result \= rpc.rpc\_sync("worker1", torch.add, args\=(torch.ones(1), 1))
\>>> \# ready to shutdown
\>>> rpc.shutdown()

Copy to clipboard

\>>> \# On worker 1:
\>>> import torch.distributed.rpc as rpc
\>>> rpc.init\_rpc("worker1", rank\=1, world\_size\=2)
\>>> \# wait for worker 0 to finish work, and then shutdown.
\>>> rpc.shutdown()

Copy to clipboard

_class_ torch.distributed.rpc.WorkerInfo[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.WorkerInfo "Link to this definition")

A structure that encapsulates information of a worker in the system. Contains the name and ID of the worker. This class is not meant to be constructed directly, rather, an instance can be retrieved through [`get_worker_info()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.get_worker_info "torch.distributed.rpc.get_worker_info")
 and the result can be passed in to functions such as [`rpc_sync()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.rpc_sync "torch.distributed.rpc.rpc_sync")
, [`rpc_async()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.rpc_async "torch.distributed.rpc.rpc_async")
, [`remote()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.remote "torch.distributed.rpc.remote")
 to avoid copying a string on every invocation.

_property_ id[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.WorkerInfo.id "Link to this definition")

Globally unique id to identify the worker.

_property_ name[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.WorkerInfo.name "Link to this definition")

The name of the worker.

The RPC package also provides decorators which allow applications to specify how a given function should be treated on the callee side.

torch.distributed.rpc.functions.async\_execution(_fn_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/rpc/functions.py#L5)
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.functions.async_execution "Link to this definition")

A decorator for a function indicating that the return value of the function is guaranteed to be a [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 object and this function can run asynchronously on the RPC callee. More specifically, the callee extracts the [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 returned by the wrapped function and installs subsequent processing steps as a callback to that [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
. The installed callback will read the value from the [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 when completed and send the value back as the RPC response. That also means the returned [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 only exists on the callee side and is never sent through RPC. This decorator is useful when the wrapped function’s (`fn`) execution needs to pause and resume due to, e.g., containing [`rpc_async()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.rpc_async "torch.distributed.rpc.rpc_async")
 or waiting for other signals.

Note

To enable asynchronous execution, applications must pass the function object returned by this decorator to RPC APIs. If RPC detected attributes installed by this decorator, it knows that this function returns a `Future` object and will handle that accordingly. However, this does not mean this decorator has to be outmost one when defining a function. For example, when combined with `@staticmethod` or `@classmethod`, `@rpc.functions.async_execution` needs to be the inner decorator to allow the target function to be recognized as a static or class function. This target function can still execute asynchronously because, when accessed, the static or class method preserves attributes installed by `@rpc.functions.async_execution`.

Example::

The returned [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 object can come from [`rpc_async()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.rpc_async "torch.distributed.rpc.rpc_async")
, [`then()`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future.then "torch.futures.Future.then")
, or [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 constructor. The example below shows directly using the [`Future`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future "torch.futures.Future")
 returned by [`then()`](https://docs.pytorch.org/docs/2.15/futures.html#torch.futures.Future.then "torch.futures.Future.then")
.

\>>> from torch.distributed import rpc
\>>>
\>>> \# omitting setup and shutdown RPC
\>>>
\>>> \# On all workers
\>>> @rpc.functions.async\_execution
\>>> def async\_add\_chained(to, x, y, z):
\>>>     \# This function runs on "worker1" and returns immediately when
\>>>     \# the callback is installed through the \`then(cb)\` API. In the
\>>>     \# mean time, the \`rpc\_async\` to "worker2" can run concurrently.
\>>>     \# When the return value of that \`rpc\_async\` arrives at
\>>>     \# "worker1", "worker1" will run the lambda function accordingly
\>>>     \# and set the value for the previously returned \`Future\`, which
\>>>     \# will then trigger RPC to send the result back to "worker0".
\>>>     return rpc.rpc\_async(to, torch.add, args\=(x, y)).then(
\>>>         lambda fut: fut.wait() + z
\>>>     )
\>>>
\>>> \# On worker0
\>>> ret \= rpc.rpc\_sync(
\>>>     "worker1",
\>>>     async\_add\_chained,
\>>>     args\=("worker2", torch.ones(2), 1, 1)
\>>> )
\>>> print(ret)  \# prints tensor(\[3., 3.\])

Copy to clipboard

When combined with TorchScript decorators, this decorator must be the outmost one.

\>>> from torch import Tensor
\>>> from torch.futures import Future
\>>> from torch.distributed import rpc
\>>>
\>>> \# omitting setup and shutdown RPC
\>>>
\>>> \# On all workers
\>>> @torch.jit.script
\>>> def script\_add(x: Tensor, y: Tensor) \-> Tensor:
\>>>     return x + y
\>>>
\>>> @rpc.functions.async\_execution
\>>> @torch.jit.script
\>>> def async\_add(to: str, x: Tensor, y: Tensor) \-> Future\[Tensor\]:
\>>>     return rpc.rpc\_async(to, script\_add, (x, y))
\>>>
\>>> \# On worker0
\>>> ret \= rpc.rpc\_sync(
\>>>     "worker1",
\>>>     async\_add,
\>>>     args\=("worker2", torch.ones(2), 1)
\>>> )
\>>> print(ret)  \# prints tensor(\[2., 2.\])

Copy to clipboard

When combined with static or class method, this decorator must be the inner one.

\>>> from torch.distributed import rpc
\>>>
\>>> \# omitting setup and shutdown RPC
\>>>
\>>> \# On all workers
\>>> class AsyncExecutionClass:
\>>>
\>>>     @staticmethod
\>>>     @rpc.functions.async\_execution
\>>>     def static\_async\_add(to, x, y, z):
\>>>         return rpc.rpc\_async(to, torch.add, args\=(x, y)).then(
\>>>             lambda fut: fut.wait() + z
\>>>         )
\>>>
\>>>     @classmethod
\>>>     @rpc.functions.async\_execution
\>>>     def class\_async\_add(cls, to, x, y, z):
\>>>         ret\_fut \= torch.futures.Future()
\>>>         rpc.rpc\_async(to, torch.add, args\=(x, y)).then(
\>>>             lambda fut: ret\_fut.set\_result(fut.wait() + z)
\>>>         )
\>>>         return ret\_fut
\>>>
\>>>     @rpc.functions.async\_execution
\>>>     def bound\_async\_add(self, to, x, y, z):
\>>>         return rpc.rpc\_async(to, torch.add, args\=(x, y)).then(
\>>>             lambda fut: fut.wait() + z
\>>>         )
\>>>
\>>> \# On worker0
\>>> ret \= rpc.rpc\_sync(
\>>>     "worker1",
\>>>     AsyncExecutionClass.static\_async\_add,
\>>>     args\=("worker2", torch.ones(2), 1, 2)
\>>> )
\>>> print(ret)  \# prints tensor(\[4., 4.\])
\>>>
\>>> ret \= rpc.rpc\_sync(
\>>>     "worker1",
\>>>     AsyncExecutionClass.class\_async\_add,
\>>>     args\=("worker2", torch.ones(2), 1, 2)
\>>> )
\>>> print(ret)  \# prints tensor(\[4., 4.\])

Copy to clipboard

This decorator also works with RRef helpers, i.e., . `torch.distributed.rpc.RRef.rpc_sync()`, `torch.distributed.rpc.RRef.rpc_async()`, and `torch.distributed.rpc.RRef.remote()`.

\>>> from torch.distributed import rpc
\>>>
\>>> \# reuse the AsyncExecutionClass class above
\>>> rref \= rpc.remote("worker1", AsyncExecutionClass)
\>>> ret \= rref.rpc\_sync().static\_async\_add("worker2", torch.ones(2), 1, 2)
\>>> print(ret)  \# prints tensor(\[4., 4.\])
\>>>
\>>> rref \= rpc.remote("worker1", AsyncExecutionClass)
\>>> ret \= rref.rpc\_async().static\_async\_add("worker2", torch.ones(2), 1, 2).wait()
\>>> print(ret)  \# prints tensor(\[4., 4.\])
\>>>
\>>> rref \= rpc.remote("worker1", AsyncExecutionClass)
\>>> ret \= rref.remote().static\_async\_add("worker2", torch.ones(2), 1, 2).to\_here()
\>>> print(ret)  \# prints tensor(\[4., 4.\])

Copy to clipboard

torch.distributed.rpc.backend\_registry.backend\_registered(_backend\_name_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/rpc/backend_registry.py#L51)
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.backend_registry.backend_registered "Link to this definition")

Checks if backend\_name is registered as an RPC backend.

Parameters:

**backend\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – string to identify the RPC backend.

Returns:

True if the backend has been registered with `register_backend`, else False.

torch.distributed.rpc.backend\_registry.register\_backend(_backend\_name_, _construct\_rpc\_backend\_options\_handler_, _init\_backend\_handler_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/rpc/backend_registry.py#L64)
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.backend_registry.register_backend "Link to this definition")

Registers a new RPC backend.

Parameters:

*   **backend\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – backend string to identify the handler.
    
*   **construct\_rpc\_backend\_options\_handler** (_function_) – Handler that is invoked when `rpc_backend.construct_rpc_backend_options(**dict)` is called.
    
*   **init\_backend\_handler** (_function_) – Handler that is invoked when the \_init\_rpc\_backend() function is called with a backend. This returns the agent.
    

### Backends[#](https://docs.pytorch.org/docs/2.15/rpc.html#backends "Link to this heading")

The RPC module can leverage different backends to perform the communication between the nodes. The backend to be used can be specified in the [`init_rpc()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.init_rpc "torch.distributed.rpc.init_rpc")
 function, by passing a certain value of the [`BackendType`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.BackendType "torch.distributed.rpc.BackendType")
 enum. Regardless of what backend is used, the rest of the RPC API won’t change. Each backend also defines its own subclass of the [`RpcBackendOptions`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.RpcBackendOptions "torch.distributed.rpc.RpcBackendOptions")
 class, an instance of which can also be passed to [`init_rpc()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.init_rpc "torch.distributed.rpc.init_rpc")
 to configure the backend’s behavior.

_class_ torch.distributed.rpc.BackendType(_value_, _names\=None_, _\*_, _module\=None_, _qualname\=None_, _type\=None_, _start\=1_, _boundary\=None_)[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.BackendType "Link to this definition")

_class_ torch.distributed.rpc.RpcBackendOptions[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.RpcBackendOptions "Link to this definition")

An abstract structure encapsulating the options passed into the RPC backend. An instance of this class can be passed in to [`init_rpc()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.init_rpc "torch.distributed.rpc.init_rpc")
 in order to initialize RPC with specific configurations, such as the RPC timeout and `init_method` to be used.

_property_ init\_method[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.RpcBackendOptions.init_method "Link to this definition")

URL specifying how to initialize the process group. Default is `env://`

_property_ rpc\_timeout[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.RpcBackendOptions.rpc_timeout "Link to this definition")

A float indicating the timeout to use for all RPCs. If an RPC does not complete in this timeframe, it will complete with an exception indicating that it has timed out.

#### TensorPipe Backend[#](https://docs.pytorch.org/docs/2.15/rpc.html#tensorpipe-backend "Link to this heading")

The TensorPipe agent, which is the default, leverages [the TensorPipe library](https://github.com/pytorch/tensorpipe)
, which provides a natively point-to-point communication primitive specifically suited for machine learning that fundamentally addresses some of the limitations of Gloo. Compared to Gloo, it has the advantage of being asynchronous, which allows a large number of transfers to occur simultaneously, each at their own speed, without blocking each other. It will only open pipes between pairs of nodes when needed, on demand, and when one node fails only its incident pipes will be closed, while all other ones will keep working as normal. In addition, it is able to support multiple different transports (TCP, of course, but also shared memory, NVLink, InfiniBand, …) and can automatically detect their availability and negotiate the best transport to use for each pipe.

The TensorPipe backend comes with a TCP-based transport, just like Gloo. It is also able to automatically chunk and multiplex large tensors over multiple sockets and threads in order to achieve very high bandwidths. The agent will be able to pick the best transport on its own, with no intervention required.

Example:

import os
from torch.distributed import rpc
os.environ\['MASTER\_ADDR'\] \= 'localhost'
os.environ\['MASTER\_PORT'\] \= '29500'

rpc.init\_rpc(
    "worker1",
    rank\=0,
    world\_size\=2,
    rpc\_backend\_options\=rpc.TensorPipeRpcBackendOptions(
        num\_worker\_threads\=8,
        rpc\_timeout\=20 \# 20 second timeout
    )
)

\# omitting init\_rpc invocation on worker2

Copy to clipboard

_class_ torch.distributed.rpc.TensorPipeRpcBackendOptions(_\*_, _num\_worker\_threads\=16_, _rpc\_timeout\=60.0_, _init\_method\='env://'_, _device\_maps\=None_, _devices\=None_, _\_transports\=None_, _\_channels\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/rpc/options.py#L50)
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.TensorPipeRpcBackendOptions "Link to this definition")

The backend options for `TensorPipeAgent`, derived from [`RpcBackendOptions`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.RpcBackendOptions "torch.distributed.rpc.RpcBackendOptions")
.

Parameters:

*   **num\_worker\_threads** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – The number of threads in the thread-pool used by `TensorPipeAgent` to execute requests (default: 16).
    
*   **rpc\_timeout** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    _,_ _optional_) – The default timeout, in seconds, for RPC requests (default: 60 seconds). If the RPC has not completed in this timeframe, an exception indicating so will be raised. Callers can override this timeout for individual RPCs in [`rpc_sync()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.rpc_sync "torch.distributed.rpc.rpc_sync")
     and [`rpc_async()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.rpc_async "torch.distributed.rpc.rpc_async")
     if necessary.
    
*   **init\_method** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – The URL to initialize the distributed store used for rendezvous. It takes any value accepted for the same argument of [`init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")
     (default: `env://`).
    
*   **device\_maps** (_Dict__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _Dict__\]__,_ _optional_) – Device placement mappings from this worker to the callee. Key is the callee worker name and value the dictionary (`Dict` of `int`, `str`, or `torch.device`) that maps this worker’s devices to the callee worker’s devices. (default: `None`)
    
*   **devices** (List\[int, str, or `torch.device`\], optional) – all local CUDA devices used by RPC agent. By Default, it will be initialized to all local devices from its own `device_maps` and corresponding devices from its peers’ `device_maps`. When processing CUDA RPC requests, the agent will properly synchronize CUDA streams for all devices in this `List`.
    

_property_ device\_maps[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.TensorPipeRpcBackendOptions.device_maps "Link to this definition")

The device map locations.

_property_ devices[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.TensorPipeRpcBackendOptions.devices "Link to this definition")

All devices used by the local agent.

_property_ init\_method[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.TensorPipeRpcBackendOptions.init_method "Link to this definition")

URL specifying how to initialize the process group. Default is `env://`

_property_ num\_worker\_threads[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.TensorPipeRpcBackendOptions.num_worker_threads "Link to this definition")

The number of threads in the thread-pool used by `TensorPipeAgent` to execute requests.

_property_ rpc\_timeout[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.TensorPipeRpcBackendOptions.rpc_timeout "Link to this definition")

A float indicating the timeout to use for all RPCs. If an RPC does not complete in this timeframe, it will complete with an exception indicating that it has timed out.

set\_device\_map(_to_, _device\_map_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/rpc/options.py#L111)
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.TensorPipeRpcBackendOptions.set_device_map "Link to this definition")

Set device mapping between each RPC caller and callee pair. This function can be called multiple times to incrementally add device placement configurations.

Parameters:

*   **to** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Callee name.
    
*   **device\_map** (_Dict_ _of_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _, or_ [_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    ) – Device placement mappings from this worker to the callee. This map must be invertible.
    

Example

\>>> \# both workers
\>>> def add(x, y):
\>>>     print(x)  \# tensor(\[1., 1.\], device='cuda:1')
\>>>     return x + y, (x + y).to(2)
\>>>
\>>> \# on worker 0
\>>> options \= TensorPipeRpcBackendOptions(
\>>>     num\_worker\_threads\=8,
\>>>     device\_maps\={"worker1": {0: 1}}
\>>> \# maps worker0's cuda:0 to worker1's cuda:1
\>>> )
\>>> options.set\_device\_map("worker1", {1: 2})
\>>> \# maps worker0's cuda:1 to worker1's cuda:2
\>>>
\>>> rpc.init\_rpc(
\>>>     "worker0",
\>>>     rank\=0,
\>>>     world\_size\=2,
\>>>     backend\=rpc.BackendType.TENSORPIPE,
\>>>     rpc\_backend\_options\=options
\>>> )
\>>>
\>>> x \= torch.ones(2)
\>>> rets \= rpc.rpc\_sync("worker1", add, args\=(x.to(0), 1))
\>>> \# The first argument will be moved to cuda:1 on worker1. When
\>>> \# sending the return value back, it will follow the invert of
\>>> \# the device map, and hence will be moved back to cuda:0 and
\>>> \# cuda:1 on worker0
\>>> print(rets\[0\])  \# tensor(\[2., 2.\], device='cuda:0')
\>>> print(rets\[1\])  \# tensor(\[2., 2.\], device='cuda:1')

Copy to clipboard

set\_devices(_devices_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/rpc/options.py#L169)
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.TensorPipeRpcBackendOptions.set_devices "Link to this definition")

Set local devices used by the TensorPipe RPC agent. When processing CUDA RPC requests, the TensorPipe RPC agent will properly synchronize CUDA streams for all devices in this `List`.

Parameters:

**devices** (_List_ _of_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_,_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_, or_ [_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
) – local devices used by the TensorPipe RPC agent.

Note

The RPC framework does not automatically retry any [`rpc_sync()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.rpc_sync "torch.distributed.rpc.rpc_sync")
, [`rpc_async()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.rpc_async "torch.distributed.rpc.rpc_async")
 and [`remote()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.remote "torch.distributed.rpc.remote")
 calls. The reason being that there is no way the RPC framework can determine whether an operation is idempotent or not and whether it is safe to retry. As a result, it is the application’s responsibility to deal with failures and retry if necessary. RPC communication is based on TCP and as a result failures could happen due to network failures or intermittent network connectivity issues. In such scenarios, the application needs to retry appropriately with reasonable backoffs to ensure the network isn’t overwhelmed by aggressive retries.

RRef[#](https://docs.pytorch.org/docs/2.15/rpc.html#rref "Link to this heading")

---------------------------------------------------------------------------------

Warning

RRefs are not currently supported when using CUDA tensors

An `RRef` (Remote REFerence) is a reference to a value of some type `T` (e.g. `Tensor`) on a remote worker. This handle keeps the referenced remote value alive on the owner, but there is no implication that the value will be transferred to the local worker in the future. RRefs can be used in multi-machine training by holding references to [nn.Modules](https://pytorch.org/docs/stable/nn.html#torch.nn.Module)
 that exist on other workers, and calling the appropriate functions to retrieve or modify their parameters during training. See [Remote Reference Protocol](https://docs.pytorch.org/docs/2.15/rpc/rref.html#remote-reference-protocol)
 for more details.

_class_ torch.distributed.rpc.PyRRef(_RRef_)[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.PyRRef "Link to this definition")

A class encapsulating a reference to a value of some type on a remote worker. This handle will keep the referenced remote value alive on the worker. A `UserRRef` will be deleted when 1) no references to it in both the application code and in the local RRef context, or 2) the application has called a graceful shutdown. Invoking methods on a deleted RRef leads to undefined behaviors. RRef implementation only offers best-effort error detection, and applications should not use `UserRRefs` after `rpc.shutdown()`.

Warning

RRefs can only be serialized and deserialized by the RPC module. Serializing and deserializing RRefs without RPC (e.g., Python pickle, torch [`save()`](https://docs.pytorch.org/docs/2.15/generated/torch.save.html#torch.save "torch.save")
 / [`load()`](https://docs.pytorch.org/docs/2.15/generated/torch.load.html#torch.load "torch.load")
, JIT `save()` / `load()`, etc.) will lead to errors.

Parameters:

*   **value** ([_object_](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")
    ) – The value to be wrapped by this RRef.
    
*   **type\_hint** (_Type__,_ _optional_) – Python type that should be passed to `TorchScript` compiler as type hint for `value`.
    

Example::

Following examples skip RPC initialization and shutdown code for simplicity. Refer to RPC docs for those details.

1.  Create an RRef using rpc.remote
    

\>>> import torch
\>>> import torch.distributed.rpc as rpc
\>>> rref \= rpc.remote("worker1", torch.add, args\=(torch.ones(2), 3))
\>>> \# get a copy of value from the RRef
\>>> x \= rref.to\_here()

Copy to clipboard

2.  Create an RRef from a local object
    

\>>> import torch
\>>> from torch.distributed.rpc import RRef
\>>> x \= torch.zeros(2, 2)
\>>> rref \= RRef(x)

Copy to clipboard

3.  Share an RRef with other workers
    

\>>> \# On both worker0 and worker1:
\>>> def f(rref):
\>>>   return rref.to\_here() + 1

Copy to clipboard

\>>> \# On worker0:
\>>> import torch
\>>> import torch.distributed.rpc as rpc
\>>> from torch.distributed.rpc import RRef
\>>> rref \= RRef(torch.zeros(2, 2))
\>>> \# the following RPC shares the rref with worker1, reference
\>>> \# count is automatically updated.
\>>> rpc.rpc\_sync("worker1", f, args\=(rref,))

Copy to clipboard

backward(_self: [torch.\_C.\_distributed\_rpc.PyRRef](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.PyRRef "torch._C._distributed_rpc.PyRRef")
_, _dist\_autograd\_ctx\_id: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.15)")
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.15)")
 \= \-1_, _retain\_graph: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= False_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.PyRRef.backward "Link to this definition")

> Runs the backward pass using the RRef as the root of the backward pass. If `dist_autograd_ctx_id` is provided, we perform a distributed backward pass using the provided ctx\_id starting from the owner of the RRef. In this case, [`get_gradients()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.autograd.get_gradients "torch.distributed.autograd.get_gradients")
>  should be used to retrieve the gradients. If `dist_autograd_ctx_id` is `None`, it is assumed that this is a local autograd graph and we only perform a local backward pass. In the local case, the node calling this API has to be the owner of the RRef. The value of the RRef is expected to be a scalar Tensor.

Parameters:

*   **dist\_autograd\_ctx\_id** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – The distributed autograd context id for which we should retrieve the gradients (default: -1).
    
*   **retain\_graph** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `False`, the graph used to compute the grad will be freed. Note that in nearly all cases setting this option to `True` is not needed and often can be worked around in a much more efficient way. Usually, you need to set this to `True` to run backward multiple times (default: False).
    

Example::

\>>> import torch.distributed.autograd as dist\_autograd
\>>> with dist\_autograd.context() as context\_id:
\>>>     rref.backward(context\_id)

Copy to clipboard

confirmed\_by\_owner(_self: [torch.\_C.\_distributed\_rpc.PyRRef](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.PyRRef "torch._C._distributed_rpc.PyRRef")
_) → [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.PyRRef.confirmed_by_owner "Link to this definition")

Returns whether this `RRef` has been confirmed by the owner. `OwnerRRef` always returns true, while `UserRRef` only returns true when the owner knows about this `UserRRef`.

is\_owner(_self: [torch.\_C.\_distributed\_rpc.PyRRef](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.PyRRef "torch._C._distributed_rpc.PyRRef")
_) → [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.PyRRef.is_owner "Link to this definition")

Returns whether or not the current node is the owner of this `RRef`.

local\_value(_self: [torch.\_C.\_distributed\_rpc.PyRRef](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.PyRRef "torch._C._distributed_rpc.PyRRef")
_) → [object](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.PyRRef.local_value "Link to this definition")

If the current node is the owner, returns a reference to the local value. Otherwise, throws an exception.

owner(_self: [torch.\_C.\_distributed\_rpc.PyRRef](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.PyRRef "torch._C._distributed_rpc.PyRRef")
_) → [torch.\_C.\_distributed\_rpc.WorkerInfo](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.WorkerInfo "torch._C._distributed_rpc.WorkerInfo")
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.PyRRef.owner "Link to this definition")

Returns worker information of the node that owns this `RRef`.

owner\_name(_self: [torch.\_C.\_distributed\_rpc.PyRRef](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.PyRRef "torch._C._distributed_rpc.PyRRef")
_) → [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.PyRRef.owner_name "Link to this definition")

Returns worker name of the node that owns this `RRef`.

remote(_self: [torch.\_C.\_distributed\_rpc.PyRRef](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.PyRRef "torch._C._distributed_rpc.PyRRef")
_, _timeout: [SupportsFloat](https://docs.python.org/3/library/typing.html#typing.SupportsFloat "(in Python v3.15)")
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.15)")
 \= \-1.0_) → [object](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.PyRRef.remote "Link to this definition")

Create a helper proxy to easily launch a `remote` using the owner of the RRef as the destination to run functions on the object referenced by this RRef. More specifically, `rref.remote().func_name(*args, **kwargs)` is the same as the following:

\>>> def run(rref, func\_name, args, kwargs):
\>>>   return getattr(rref.local\_value(), func\_name)(\*args, \*\*kwargs)
\>>>
\>>> rpc.remote(rref.owner(), run, args\=(rref, func\_name, args, kwargs))

Copy to clipboard

Parameters:

**timeout** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
_,_ _optional_) – Timeout for `rref.remote()`. If the creation of this `RRef` is not successfully completed within the timeout, then the next time there is an attempt to use the RRef (such as `to_here`), a timeout will be raised. If not provided, the default RPC timeout will be used. Please see `rpc.remote()` for specific timeout semantics for `RRef`.

Example::

\>>> from torch.distributed import rpc
\>>> rref \= rpc.remote("worker1", torch.add, args\=(torch.zeros(2, 2), 1))
\>>> rref.remote().size().to\_here()  \# returns torch.Size(\[2, 2\])
\>>> rref.remote().view(1, 4).to\_here()  \# returns tensor(\[\[1., 1., 1., 1.\]\])

Copy to clipboard

rpc\_async(_self: [torch.\_C.\_distributed\_rpc.PyRRef](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.PyRRef "torch._C._distributed_rpc.PyRRef")
_, _timeout: [SupportsFloat](https://docs.python.org/3/library/typing.html#typing.SupportsFloat "(in Python v3.15)")
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.15)")
 \= \-1.0_) → [object](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.PyRRef.rpc_async "Link to this definition")

Create a helper proxy to easily launch an `rpc_async` using the owner of the RRef as the destination to run functions on the object referenced by this RRef. More specifically, `rref.rpc_async().func_name(*args, **kwargs)` is the same as the following:

\>>> def run(rref, func\_name, args, kwargs):
\>>>   return getattr(rref.local\_value(), func\_name)(\*args, \*\*kwargs)
\>>>
\>>> rpc.rpc\_async(rref.owner(), run, args\=(rref, func\_name, args, kwargs))

Copy to clipboard

Parameters:

**timeout** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
_,_ _optional_) – Timeout for `rref.rpc_async()`. If the call does not complete within this timeframe, an exception indicating so will be raised. If this argument is not provided, the default RPC timeout will be used.

Example::

\>>> from torch.distributed import rpc
\>>> rref \= rpc.remote("worker1", torch.add, args\=(torch.zeros(2, 2), 1))
\>>> rref.rpc\_async().size().wait()  \# returns torch.Size(\[2, 2\])
\>>> rref.rpc\_async().view(1, 4).wait()  \# returns tensor(\[\[1., 1., 1., 1.\]\])

Copy to clipboard

rpc\_sync(_self: [torch.\_C.\_distributed\_rpc.PyRRef](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.PyRRef "torch._C._distributed_rpc.PyRRef")
_, _timeout: [SupportsFloat](https://docs.python.org/3/library/typing.html#typing.SupportsFloat "(in Python v3.15)")
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.15)")
 \= \-1.0_) → [object](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.PyRRef.rpc_sync "Link to this definition")

Create a helper proxy to easily launch an `rpc_sync` using the owner of the RRef as the destination to run functions on the object referenced by this RRef. More specifically, `rref.rpc_sync().func_name(*args, **kwargs)` is the same as the following:

\>>> def run(rref, func\_name, args, kwargs):
\>>>   return getattr(rref.local\_value(), func\_name)(\*args, \*\*kwargs)
\>>>
\>>> rpc.rpc\_sync(rref.owner(), run, args\=(rref, func\_name, args, kwargs))

Copy to clipboard

Parameters:

**timeout** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
_,_ _optional_) – Timeout for `rref.rpc_sync()`. If the call does not complete within this timeframe, an exception indicating so will be raised. If this argument is not provided, the default RPC timeout will be used.

Example::

\>>> from torch.distributed import rpc
\>>> rref \= rpc.remote("worker1", torch.add, args\=(torch.zeros(2, 2), 1))
\>>> rref.rpc\_sync().size()  \# returns torch.Size(\[2, 2\])
\>>> rref.rpc\_sync().view(1, 4)  \# returns tensor(\[\[1., 1., 1., 1.\]\])

Copy to clipboard

to\_here(_self: [torch.\_C.\_distributed\_rpc.PyRRef](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.PyRRef "torch._C._distributed_rpc.PyRRef")
_, _timeout: [SupportsFloat](https://docs.python.org/3/library/typing.html#typing.SupportsFloat "(in Python v3.15)")
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.15)")
 \= \-1.0_) → [object](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.rpc.PyRRef.to_here "Link to this definition")

Blocking call that copies the value of the RRef from the owner to the local node and returns it. If the current node is the owner, returns a reference to the local value.

Parameters:

**timeout** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
_,_ _optional_) – Timeout for `to_here`. If the call does not complete within this timeframe, an exception indicating so will be raised. If this argument is not provided, the default RPC timeout (60s) will be used.

More Information about RRef

*   [Remote Reference Protocol](https://docs.pytorch.org/docs/2.15/rpc/rref.html)
    *   [Background](https://docs.pytorch.org/docs/2.15/rpc/rref.html#background)
        
    *   [Assumptions](https://docs.pytorch.org/docs/2.15/rpc/rref.html#assumptions)
        
    *   [RRef Lifetime](https://docs.pytorch.org/docs/2.15/rpc/rref.html#rref-lifetime)
        *   [Design Reasoning](https://docs.pytorch.org/docs/2.15/rpc/rref.html#design-reasoning)
            
        *   [Implementation](https://docs.pytorch.org/docs/2.15/rpc/rref.html#implementation)
            
    *   [Protocol Scenarios](https://docs.pytorch.org/docs/2.15/rpc/rref.html#protocol-scenarios)
        *   [User Share RRef with Owner as Return Value](https://docs.pytorch.org/docs/2.15/rpc/rref.html#user-share-rref-with-owner-as-return-value)
            
        *   [User Share RRef with Owner as Argument](https://docs.pytorch.org/docs/2.15/rpc/rref.html#user-share-rref-with-owner-as-argument)
            
        *   [Owner Share RRef with User](https://docs.pytorch.org/docs/2.15/rpc/rref.html#owner-share-rref-with-user)
            
        *   [User Share RRef with User](https://docs.pytorch.org/docs/2.15/rpc/rref.html#user-share-rref-with-user)
            

RemoteModule[#](https://docs.pytorch.org/docs/2.15/rpc.html#remotemodule "Link to this heading")

-------------------------------------------------------------------------------------------------

Warning

RemoteModule is not currently supported when using CUDA tensors

`RemoteModule` is an easy way to create an nn.Module remotely on a different process. The actual module resides on a remote host, but the local host has a handle to this module and invoke this module similar to a regular nn.Module. The invocation however incurs RPC calls to the remote end and can be performed asynchronously if needed via additional APIs supported by RemoteModule.

_class_ torch.distributed.nn.api.remote\_module.RemoteModule(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/nn/api/remote_module.py#L605)
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.nn.api.remote_module.RemoteModule "Link to this definition")

> A RemoteModule instance can only be created after RPC initialization.
> 
> It creates a user-specified module on a specified remote node. It behaves like a regular `nn.Module` except that the `forward` method is executed on the remote node. It takes care of autograd recording to ensure the backward pass propagates gradients back to the corresponding remote module.
> 
> It generates two methods `forward_async` and `forward` based on the signature of the `forward` method of `module_cls`. `forward_async` runs asynchronously and returns a Future. The arguments of `forward_async` and `forward` are the same as the `forward` method of the module returned by the `module_cls`.
> 
> For example, if `module_cls` returns an instance of `nn.Linear`, that has `forward` method signature: `def forward(input: Tensor) -> Tensor:`, the generated `RemoteModule` will have 2 methods with the signatures:
> 
> `def forward(input: Tensor) -> Tensor:`
> 
> `def forward_async(input: Tensor) -> Future[Tensor]:`

Parameters:

*   **remote\_device** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Device on the destination worker where we’d like to place this module. The format should be “<workername>/<device>”, where the device field can be parsed as torch.device type. E.g., “trainer0/cpu”, “trainer0”, “ps0/cuda:0”. In addition, the device field can be optional and the default value is “cpu”.
    
*   **module\_cls** ([_nn.Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
    ) –
    
    Class for the module to be created remotely. For example,
    
    \>>> class MyModule(nn.Module):
    \>>>     def forward(input):
    \>>>         return input + 1
    \>>>
    \>>> module\_cls \= MyModule
    
    Copy to clipboard
    
*   **args** (_Sequence__,_ _optional_) – args to be passed to `module_cls`.
    
*   **kwargs** (_Dict__,_ _optional_) – kwargs to be passed to `module_cls`.
    

Returns:

A remote module instance which wraps the `Module` created by the user-provided `module_cls`, it has a blocking `forward` method and an asynchronous `forward_async` method that returns a future of the `forward` call on the user-provided module on the remote side.

Example::

Run the following code in two different processes:

\>>> \# On worker 0:
\>>> import torch
\>>> import torch.distributed.rpc as rpc
\>>> from torch import nn, Tensor
\>>> from torch.distributed.nn.api.remote\_module import RemoteModule
\>>>
\>>> rpc.init\_rpc("worker0", rank\=0, world\_size\=2)
\>>> remote\_linear\_module \= RemoteModule(
\>>>     "worker1/cpu", nn.Linear, args\=(20, 30),
\>>> )
\>>> input \= torch.randn(128, 20)
\>>> ret\_fut \= remote\_linear\_module.forward\_async(input)
\>>> ret \= ret\_fut.wait()
\>>> rpc.shutdown()

Copy to clipboard

\>>> \# On worker 1:
\>>> import torch
\>>> import torch.distributed.rpc as rpc
\>>>
\>>> rpc.init\_rpc("worker1", rank\=1, world\_size\=2)
\>>> rpc.shutdown()

Copy to clipboard

Furthermore, a more practical example that is combined with [DistributedDataParallel](https://pytorch.org/docs/stable/nn.html#torch.nn.parallel.DistributedDataParallel)
 (DDP) can be found in this [tutorial](https://pytorch.org/tutorials/advanced/rpc_ddp_tutorial.html)
.

get\_module\_rref()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/nn/api/remote_module.py#L296)
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.nn.api.remote_module.RemoteModule.get_module_rref "Link to this definition")

Return an `RRef` (`RRef[nn.Module]`) pointing to the remote module.

Return type:

_RRef_\[[_Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.modules.module.Module")\
\]

remote\_parameters(_recurse\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/nn/api/remote_module.py#L277)
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.nn.api.remote_module.RemoteModule.remote_parameters "Link to this definition")

Return a list of `RRef` pointing to the remote module’s parameters.

This can typically be used in conjunction with [`DistributedOptimizer`](https://docs.pytorch.org/docs/2.15/distributed.optim.html#torch.distributed.optim.DistributedOptimizer "torch.distributed.optim.DistributedOptimizer")
.

Parameters:

**recurse** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
) – if True, then returns parameters of the remote module and all submodules of the remote module. Otherwise, returns only parameters that are direct members of the remote module.

Returns:

A list of `RRef` (`List[RRef[nn.Parameter]]`) to remote module’s parameters.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[_RRef_\[[_Parameter_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "torch.nn.parameter.Parameter")\
\]\]

Distributed Autograd Framework[#](https://docs.pytorch.org/docs/2.15/rpc.html#distributed-autograd-framework "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

Warning

Distributed autograd is not currently supported when using CUDA tensors

This module provides an RPC-based distributed autograd framework that can be used for applications such as model parallel training. In short, applications may send and receive gradient recording tensors over RPC. In the forward pass, we record when gradient recording tensors are sent over RPC and during the backward pass we use this information to perform a distributed backward pass using RPC. For more details see [Distributed Autograd Design](https://docs.pytorch.org/docs/2.15/rpc/distributed_autograd.html#distributed-autograd-design)
.

torch.distributed.autograd.backward(_context\_id: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_, _roots: List\[[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]_, _retain\_graph\=False_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.autograd.backward "Link to this definition")

Kicks off the distributed backward pass using the provided roots. This currently implements the [FAST mode algorithm](https://docs.pytorch.org/docs/2.15/rpc/distributed_autograd.html#fast-mode-algorithm)
 which assumes all RPC messages sent in the same distributed autograd context across workers would be part of the autograd graph during the backward pass.

We use the provided roots to discover the autograd graph and compute appropriate dependencies. This method blocks until the entire autograd computation is done.

We accumulate the gradients in the appropriate [`torch.distributed.autograd.context`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.autograd.context "torch.distributed.autograd.context")
 on each of the nodes. The autograd context to be used is looked up given the `context_id` that is passed in when [`torch.distributed.autograd.backward()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.autograd.backward "torch.distributed.autograd.backward")
 is called. If there is no valid autograd context corresponding to the given ID, we throw an error. You can retrieve the accumulated gradients using the [`get_gradients()`](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.autograd.get_gradients "torch.distributed.autograd.get_gradients")
 API.

Parameters:

*   **context\_id** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The autograd context id for which we should retrieve the gradients.
    
*   **roots** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    ) – Tensors which represent the roots of the autograd computation. All the tensors should be scalars.
    
*   **retain\_graph** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If False, the graph used to compute the grad will be freed. Note that in nearly all cases setting this option to True is not needed and often can be worked around in a much more efficient way. Usually, you need to set this to True to run backward multiple times.
    

Example::

\>>> import torch.distributed.autograd as dist\_autograd
\>>> with dist\_autograd.context() as context\_id:
\>>>     pred \= model.forward()
\>>>     loss \= loss\_func(pred, loss)
\>>>     dist\_autograd.backward(context\_id, loss)

Copy to clipboard

_class_ torch.distributed.autograd.context[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/autograd/__init__.py#L37)
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.autograd.context "Link to this definition")

Context object to wrap forward and backward passes when using distributed autograd. The `context_id` generated in the `with` statement is required to uniquely identify a distributed backward pass on all workers. Each worker stores metadata associated with this `context_id`, which is required to correctly execute a distributed autograd pass.

Example::

\>>> import torch.distributed.autograd as dist\_autograd
\>>> with dist\_autograd.context() as context\_id:
\>>>     t1 \= torch.rand((3, 3), requires\_grad\=True)
\>>>     t2 \= torch.rand((3, 3), requires\_grad\=True)
\>>>     loss \= rpc.rpc\_sync("worker1", torch.add, args\=(t1, t2)).sum()
\>>>     dist\_autograd.backward(context\_id, \[loss\])

Copy to clipboard

torch.distributed.autograd.get\_gradients(_context\_id: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_) → Dict\[[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\][#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.autograd.get_gradients "Link to this definition")

Retrieves a map from Tensor to the appropriate gradient for that Tensor accumulated in the provided context corresponding to the given `context_id` as part of the distributed autograd backward pass.

Parameters:

**context\_id** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
) – The autograd context id for which we should retrieve the gradients.

Returns:

A map where the key is the Tensor and the value is the associated gradient for that Tensor.

Example::

\>>> import torch.distributed.autograd as dist\_autograd
\>>> with dist\_autograd.context() as context\_id:
\>>>     t1 \= torch.rand((3, 3), requires\_grad\=True)
\>>>     t2 \= torch.rand((3, 3), requires\_grad\=True)
\>>>     loss \= t1 + t2
\>>>     dist\_autograd.backward(context\_id, \[loss.sum()\])
\>>>     grads \= dist\_autograd.get\_gradients(context\_id)
\>>>     print(grads\[t1\])
\>>>     print(grads\[t2\])

Copy to clipboard

torch.distributed.autograd.is\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/autograd/__init__.py#L12)
[#](https://docs.pytorch.org/docs/2.15/rpc.html#torch.distributed.autograd.is_available "Link to this definition")

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

More Information about RPC Autograd

*   [Distributed Autograd Design](https://docs.pytorch.org/docs/2.15/rpc/distributed_autograd.html)
    *   [Background](https://docs.pytorch.org/docs/2.15/rpc/distributed_autograd.html#background)
        
    *   [Autograd recording during the forward pass](https://docs.pytorch.org/docs/2.15/rpc/distributed_autograd.html#autograd-recording-during-the-forward-pass)
        
    *   [Distributed Autograd Context](https://docs.pytorch.org/docs/2.15/rpc/distributed_autograd.html#distributed-autograd-context)
        
    *   [Distributed Backward Pass](https://docs.pytorch.org/docs/2.15/rpc/distributed_autograd.html#distributed-backward-pass)
        *   [Computing dependencies](https://docs.pytorch.org/docs/2.15/rpc/distributed_autograd.html#computing-dependencies)
            
        *   [FAST mode algorithm](https://docs.pytorch.org/docs/2.15/rpc/distributed_autograd.html#fast-mode-algorithm)
            
        *   [SMART mode algorithm](https://docs.pytorch.org/docs/2.15/rpc/distributed_autograd.html#smart-mode-algorithm)
            
    *   [Distributed Optimizer](https://docs.pytorch.org/docs/2.15/rpc/distributed_autograd.html#distributed-optimizer)
        
    *   [Simple end to end example](https://docs.pytorch.org/docs/2.15/rpc/distributed_autograd.html#simple-end-to-end-example)
        

Distributed Optimizer[#](https://docs.pytorch.org/docs/2.15/rpc.html#distributed-optimizer "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

See the [torch.distributed.optim](https://pytorch.org/docs/main/distributed.optim.html)
 page for documentation on distributed optimizers.

Design Notes[#](https://docs.pytorch.org/docs/2.15/rpc.html#design-notes "Link to this heading")

-------------------------------------------------------------------------------------------------

The distributed autograd design note covers the design of the RPC-based distributed autograd framework that is useful for applications such as model parallel training.

*   [Distributed Autograd Design](https://docs.pytorch.org/docs/2.15/rpc/distributed_autograd.html#distributed-autograd-design)
    

The RRef design note covers the design of the [RRef](https://docs.pytorch.org/docs/2.15/rpc.html#rref)
 (Remote REFerence) protocol used to refer to values on remote workers by the framework.

*   [Remote Reference Protocol](https://docs.pytorch.org/docs/2.15/rpc/rref.html#remote-reference-protocol)
    

Tutorials[#](https://docs.pytorch.org/docs/2.15/rpc.html#tutorials "Link to this heading")

-------------------------------------------------------------------------------------------

The RPC tutorials introduce users to the RPC framework, provide several example applications using [torch.distributed.rpc](https://docs.pytorch.org/docs/2.15/rpc.html#distributed-rpc-framework)
 APIs, and demonstrate how to use [the profiler](https://pytorch.org/docs/stable/autograd.html#profiler)
 to profile RPC-based workloads.

*   [Getting started with Distributed RPC Framework](https://pytorch.org/tutorials/intermediate/rpc_tutorial.html)
    
*   [Implementing a Parameter Server using Distributed RPC Framework](https://pytorch.org/tutorials/intermediate/rpc_param_server_tutorial.html)
    
*   [Combining Distributed DataParallel with Distributed RPC Framework](https://pytorch.org/tutorials/advanced/rpc_ddp_tutorial.html)
     (covers **RemoteModule** as well)
    
*   [Implementing batch RPC processing](https://pytorch.org/tutorials/intermediate/rpc_async_execution.html)
    

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/rpc.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/rpc.md.txt)

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