Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/distributed.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/distributed.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/distributed.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/distributed.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/distributed.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/distributed.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/distributed.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/distributed.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/distributed.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/distributed.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/distributed.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/distributed.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/distributed.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/distributed.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/distributed.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/distributed.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/distributed.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/distributed.html)
[v1.13](https://docs.pytorch.org/docs/1.13/distributed.html)
[v1.12](https://docs.pytorch.org/docs/1.12/distributed.html)
[v1.11](https://docs.pytorch.org/docs/1.11/distributed.html)
[v1.10](https://docs.pytorch.org/docs/1.10/distributed.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/distributed.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/distributed.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/distributed.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/distributed.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/distributed.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/distributed.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/distributed.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/distributed.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/distributed.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/distributed.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/distributed.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/distributed.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/distributed.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/distributed.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/distributed.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/distributed.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/distributed.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/distributed.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/distributed.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/distributed.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/distributed.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/distributed.html)

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

Distributed communication package - torch.distributed[#](https://docs.pytorch.org/docs/2.15/distributed.html#distributed-communication-package-torch-distributed "Link to this heading")

=========================================================================================================================================================================================

Created On: Jul 12, 2017 | Last Updated On: Oct 01, 2026

Note

Please refer to [PyTorch Distributed Overview](https://pytorch.org/tutorials/beginner/dist_overview.html)
 for a brief introduction to all features related to distributed training.

torch.distributed.elastic.utils.api.get\_env\_variable\_or\_raise(_env\_name_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/utils/api.py#L15)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.elastic.utils.api.get_env_variable_or_raise "Link to this definition")

Tries to retrieve environment variable. Raises `ValueError` if no environment variable found.

Parameters:

**env\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – Name of the env variable

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

torch.distributed.elastic.utils.distributed.get\_free\_port()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/utils/distributed.py#L124)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.elastic.utils.distributed.get_free_port "Link to this definition")

Returns a port that is unused on all local addresses.

This function finds an unused port by binding a socket to the wildcard address and then closing it.

Returns:

a port that is unused on all local addresses

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

Example

\>>> get\_free\_port()
63976

Copy to clipboard

Note

The port returned by [`get_free_port()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.elastic.utils.distributed.get_free_port "torch.distributed.elastic.utils.distributed.get_free_port")
 is not reserved and may be taken by another process after this function returns.

torch.distributed.elastic.utils.log\_level.get\_log\_level()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/utils/log_level.py#L10)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.elastic.utils.log_level.get_log_level "Link to this definition")

Return default log level for pytorch.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

torch.distributed.elastic.utils.logging.get\_logger(_name\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/utils/logging.py#L17)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.elastic.utils.logging.get_logger "Link to this definition")

Util function to set up a simple logger that writes into stderr. The loglevel is fetched from the LOGLEVEL env. variable or WARNING as default. The function will use the module name of the caller if no name is provided.

Parameters:

**name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 _|_ _None_) – Name of the logger. If no name provided, the name will be derived from the call stack.

Return type:

[_Logger_](https://docs.python.org/3/library/logging.html#logging.Logger "(in Python v3.15)")

torch.distributed.rendezvous.register\_rendezvous\_handler(_scheme_, _handler_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/rendezvous.py#L25)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.rendezvous.register_rendezvous_handler "Link to this definition")

Register a new rendezvous handler.

Before we can run collective algorithms, participating processes need to find each other and exchange information to be able to communicate. We call this process rendezvous.

The outcome of the rendezvous process is a triplet containing a shared key/value store, the rank of the process, and the total number of participating processes.

If none of the bundled rendezvous methods apply to your execution environment you can opt to register your own rendezvous handler. Pick a unique name and use the URL scheme to identify it when calling the rendezvous() function.

Parameters:

*   **scheme** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – URL scheme to identify your rendezvous handler.
    
*   **handler** (_function_) – Handler that is invoked when the rendezvous() function is called with a URL that uses the corresponding scheme. It must be a generator function that yields the triplet.
    

torch.distributed.algorithms.model\_averaging.utils.average\_parameters(_params_, _process\_group_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/model_averaging/utils.py#L21)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.algorithms.model_averaging.utils.average_parameters "Link to this definition")

Averages all the given parameters.

For allreduce efficiency, all the parameters are flattened into a contiguous buffer. Thus, it requires extra memory of the same size as the given parameters.

torch.distributed.algorithms.model\_averaging.utils.average\_parameters\_or\_parameter\_groups(_params_, _process\_group_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/model_averaging/utils.py#L81)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.algorithms.model_averaging.utils.average_parameters_or_parameter_groups "Link to this definition")

Averages parameters of a model or parameter groups of an optimizer.

torch.distributed.algorithms.model\_averaging.utils.get\_params\_to\_average(_params_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/algorithms/model_averaging/utils.py#L52)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.algorithms.model_averaging.utils.get_params_to_average "Link to this definition")

Return a list of parameters that need to average.

This filters out the parameters that do not contain any gradients. :param params: The parameters of a model or parameter groups of an optimizer.

Backends[#](https://docs.pytorch.org/docs/2.15/distributed.html#backends "Link to this heading")

-------------------------------------------------------------------------------------------------

`torch.distributed` supports four built-in backends, each with different capabilities. The table below shows which functions are available for use with a CPU or GPU for each backend. For NCCL, GPU refers to CUDA GPU while for XCCL to XPU GPU.

MPI supports CUDA only if the implementation used to build PyTorch supports it.

| Backend | `gloo` |     | `mpi` |     | `nccl` |     | `xccl` |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Device | CPU | GPU | CPU | GPU | CPU | GPU | CPU | GPU |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| send | ✓   | ✘   | ✓   | ?   | ✘   | ✓   | ✘   | ✓   |
| recv | ✓   | ✘   | ✓   | ?   | ✘   | ✓   | ✘   | ✓   |
| broadcast | ✓   | ✓   | ✓   | ?   | ✘   | ✓   | ✘   | ✓   |
| all\_reduce | ✓   | ✓   | ✓   | ?   | ✘   | ✓   | ✘   | ✓   |
| reduce | ✓   | ✓   | ✓   | ?   | ✘   | ✓   | ✘   | ✓   |
| all\_gather | ✓   | ✓   | ✓   | ?   | ✘   | ✓   | ✘   | ✓   |
| gather | ✓   | ✓   | ✓   | ?   | ✘   | ✓   | ✘   | ✓   |
| scatter | ✓   | ✓   | ✓   | ?   | ✘   | ✓   | ✘   | ✓   |
| reduce\_scatter | ✓   | ✓   | ✘   | ✘   | ✘   | ✓   | ✘   | ✓   |
| all\_to\_all | ✘   | ✘   | ✓   | ?   | ✘   | ✓   | ✘   | ✓   |
| barrier | ✓   | ✘   | ✓   | ?   | ✘   | ✓   | ✘   | ✓   |

### Backends that come with PyTorch[#](https://docs.pytorch.org/docs/2.15/distributed.html#backends-that-come-with-pytorch "Link to this heading")

PyTorch distributed package supports Linux (stable), macOS (stable), and Windows (prototype). By default for Linux, the Gloo and NCCL backends are built and included in PyTorch distributed (NCCL only when building with CUDA). MPI is an optional backend that can only be included if you build PyTorch from source. (e.g. building PyTorch on a host that has MPI installed.)

Note

As of PyTorch v1.8, Windows supports all collective communications backends but NCCL, If the `init_method` argument of [`init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")
 points to a file it must adhere to the following schema:

*   Local file system, `init_method="file:///d:/tmp/some_file"`
    
*   Shared file system, `init_method="file://////{machine_name}/{share_folder_name}/some_file"`
    

Same as on Linux platform, you can enable TcpStore by setting environment variables, MASTER\_ADDR and MASTER\_PORT.

### Which backend to use?[#](https://docs.pytorch.org/docs/2.15/distributed.html#which-backend-to-use "Link to this heading")

In the past, we were often asked: “which backend should I use?”.

*   Rule of thumb
    
    *   Use the NCCL backend for distributed training with CUDA **GPU**.
        
    *   Use the XCCL backend for distributed training with XPU **GPU**.
        
    *   Use the Gloo backend for distributed training with **CPU**.
        
*   GPU hosts with InfiniBand interconnect
    
    *   Use NCCL, since it’s the only backend that currently supports InfiniBand and GPUDirect.
        
*   GPU hosts with Ethernet interconnect
    
    *   Use NCCL, since it currently provides the best distributed GPU training performance, especially for multiprocess single-node or multi-node distributed training. If you encounter any problem with NCCL, use Gloo as the fallback option. (Note that Gloo currently runs slower than NCCL for GPUs.)
        
*   CPU hosts with InfiniBand interconnect
    
    *   If your InfiniBand has enabled IP over IB, use Gloo, otherwise, use MPI instead. We are planning on adding InfiniBand support for Gloo in the upcoming releases.
        
*   CPU hosts with Ethernet interconnect
    
    *   Use Gloo, unless you have specific reasons to use MPI.
        

### Common environment variables[#](https://docs.pytorch.org/docs/2.15/distributed.html#common-environment-variables "Link to this heading")

#### Choosing the network interface to use[#](https://docs.pytorch.org/docs/2.15/distributed.html#choosing-the-network-interface-to-use "Link to this heading")

By default, both the NCCL and Gloo backends will try to find the right network interface to use. If the automatically detected interface is not correct, you can override it using the following environment variables (applicable to the respective backend):

*   **NCCL\_SOCKET\_IFNAME**, for example `export NCCL_SOCKET_IFNAME=eth0`
    
*   **GLOO\_SOCKET\_IFNAME**, for example `export GLOO_SOCKET_IFNAME=eth0`
    

If you’re using the Gloo backend, you can specify multiple interfaces by separating them by a comma, like this: `export GLOO_SOCKET_IFNAME=eth0,eth1,eth2,eth3`. The backend will dispatch operations in a round-robin fashion across these interfaces. It is imperative that all processes specify the same number of interfaces in this variable.

#### Other NCCL environment variables[#](https://docs.pytorch.org/docs/2.15/distributed.html#other-nccl-environment-variables "Link to this heading")

**Debugging** - in case of NCCL failure, you can set `NCCL_DEBUG=INFO` to print an explicit warning message as well as basic NCCL initialization information.

You may also use `NCCL_DEBUG_SUBSYS` to get more details about a specific aspect of NCCL. For example, `NCCL_DEBUG_SUBSYS=COLL` would print logs of collective calls, which may be helpful when debugging hangs, especially those caused by collective type or message size mismatch. In case of topology detection failure, it would be helpful to set `NCCL_DEBUG_SUBSYS=GRAPH` to inspect the detailed detection result and save as reference if further help from NCCL team is needed.

**Performance tuning** - NCCL performs automatic tuning based on its topology detection to save users’ tuning effort. On some socket-based systems, users may still try tuning `NCCL_SOCKET_NTHREADS` and `NCCL_NSOCKS_PERTHREAD` to increase socket network bandwidth. These two environment variables have been pre-tuned by NCCL for some cloud providers, such as AWS or GCP.

For a full list of NCCL environment variables, please refer to [NVIDIA NCCL’s official documentation](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html)

You can tune NCCL communicators even further using `torch.distributed.ProcessGroupNCCL.NCCLConfig` and `torch.distributed.ProcessGroupNCCL.Options`. Learn more about them using `help` (e.g. `help(torch.distributed.ProcessGroupNCCL.NCCLConfig)`) in the interpreter.

Basics[#](https://docs.pytorch.org/docs/2.15/distributed.html#basics "Link to this heading")

---------------------------------------------------------------------------------------------

The `torch.distributed` package provides PyTorch support and communication primitives for multiprocess parallelism across several computation nodes running on one or more machines. The class [`torch.nn.parallel.DistributedDataParallel()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")
 builds on this functionality to provide synchronous distributed training as a wrapper around any PyTorch model. This differs from the kinds of parallelism provided by [Multiprocessing package - torch.multiprocessing](https://docs.pytorch.org/docs/2.15/multiprocessing.html)
 and [`torch.nn.DataParallel()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.DataParallel.html#torch.nn.DataParallel "torch.nn.DataParallel")
 in that it supports multiple network-connected machines and in that the user must explicitly launch a separate copy of the main training script for each process.

In the single-machine synchronous case, `torch.distributed` or the [`torch.nn.parallel.DistributedDataParallel()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")
 wrapper may still have advantages over other approaches to data-parallelism, including [`torch.nn.DataParallel()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.DataParallel.html#torch.nn.DataParallel "torch.nn.DataParallel")
:

*   Each process maintains its own optimizer and performs a complete optimization step with each iteration. While this may appear redundant, since the gradients have already been gathered together and averaged across processes and are thus the same for every process, this means that no parameter broadcast step is needed, reducing time spent transferring tensors between nodes.
    
*   Each process contains an independent Python interpreter, eliminating the extra interpreter overhead and “GIL-thrashing” that comes from driving several execution threads, model replicas, or GPUs from a single Python process. This is especially important for models that make heavy use of the Python runtime, including models with recurrent layers or many small components.
    

Initialization[#](https://docs.pytorch.org/docs/2.15/distributed.html#initialization "Link to this heading")

-------------------------------------------------------------------------------------------------------------

The package needs to be initialized using the [`torch.distributed.init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")
 or [`torch.distributed.device_mesh.init_device_mesh()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.device_mesh.init_device_mesh "torch.distributed.device_mesh.init_device_mesh")
 function before calling any other methods. Both block until all processes have joined.

Warning

Initialization is not thread-safe. Process group creation should be performed from a single thread, to prevent inconsistent ‘UUID’ assignment across ranks, and to prevent races during initialization that can lead to hangs.

torch.distributed.is\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/__init__.py#L18)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.is_available "Link to this definition")

Return `True` if the distributed package is available.

Otherwise, `torch.distributed` does not expose any other APIs. Currently, `torch.distributed` is available on Linux, MacOS and Windows. Set `USE_DISTRIBUTED=1` to enable it when building PyTorch from source. Currently, the default value is `USE_DISTRIBUTED=1` for Linux and Windows, `USE_DISTRIBUTED=0` for MacOS.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.distributed.init\_process\_group(_backend\=None_, _init\_method\=None_, _timeout\=None_, _world\_size\=\-1_, _rank\=\-1_, _store\=None_, _group\_name\=''_, _pg\_options\=None_, _device\_id\=None_, _\_ranks\=None_, _enable\_reconfigure\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L2453)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "Link to this definition")

Initialize the default distributed process group.

This will also initialize the distributed package.

There are 2 main ways to initialize a process group:

1.  Specify `store`, `rank`, and `world_size` explicitly.
    
2.  Specify `init_method` (a URL string) which indicates where/how to discover peers. Optionally specify `rank` and `world_size`, or encode all required parameters in the URL and omit them.
    

If neither is specified, `init_method` is assumed to be “env://”.

Parameters:

*   **backend** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _or_ [_Backend_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Backend "torch.distributed.Backend")
    _,_ _optional_) – The backend to use. Depending on build-time configurations, valid values include `mpi`, `gloo`, `nccl`, `ucc`, `xccl` or one that is registered by a third-party plugin. Since 2.6, if `backend` is not provided, c10d will use a backend registered for the device type indicated by the device\_id kwarg (if provided). The known default registrations today are: `nccl` for `cuda`, `gloo` for `cpu`, `xccl` for `xpu`. If neither `backend` nor `device_id` is provided, c10d will detect the accelerator on the run-time machine and use a backend registered for that detected accelerator (or `cpu`). This field can be given as a lowercase string (e.g., `"gloo"`), which can also be accessed via [`Backend`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Backend "torch.distributed.Backend")
     attributes (e.g., `Backend.GLOO`). If using multiple processes per machine with `nccl` backend, each process must have exclusive access to every GPU it uses, as sharing GPUs between processes can result in deadlock or NCCL invalid usage. `ucc` backend is experimental. Default backend for the device can be queried with [`get_default_backend_for_device()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.get_default_backend_for_device "torch.distributed.get_default_backend_for_device")
    .
    
*   **init\_method** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – URL specifying how to initialize the process group. Default is “env://” if no `init_method` or `store` is specified. Mutually exclusive with `store`.
    
*   **world\_size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – Number of processes participating in the job. Required if `store` is specified.
    
*   **rank** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – Rank of the current process (it should be a number between 0 and `world_size`\-1). Required if `store` is specified.
    
*   **store** ([_Store_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store "torch.distributed.Store")
    _,_ _optional_) – Key/value store accessible to all workers, used to exchange connection/address information. Mutually exclusive with `init_method`.
    
*   **timeout** (_timedelta__,_ _optional_) – Timeout for operations executed against the process group. Default value is 10 minutes for NCCL and 30 minutes for other backends. This is the duration after which collectives will be aborted asynchronously and the process will crash. This is done since CUDA execution is async and it is no longer safe to continue executing user code since failed async NCCL operations might result in subsequent CUDA operations running on corrupted data. When TORCH\_NCCL\_BLOCKING\_WAIT is set, the process will block and wait for this timeout.
    
*   **group\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional__,_ _deprecated_) – Group name. This argument is ignored
    
*   **pg\_options** (`Backend.Options`, optional) – process group options specifying what additional options need to be passed in during the construction of specific process groups. As of now, the only options we support is `ProcessGroupNCCL.Options` for the `nccl` backend, `is_high_priority_stream` can be specified so that the nccl backend can pick up high priority cuda streams when there’re compute kernels waiting. For other available options to config nccl, See [https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/api/types.html#ncclconfig-t](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/api/types.html#ncclconfig-t)
    
*   **device\_id** ([_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
     _|_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – a single, specific device this process will work on, allowing for backend-specific optimizations. Both accelerator devices (e.g. `cuda:0`) and CPU devices (e.g. `cpu:0`) are accepted; on CPU, this currently only validates and records the device, without any of the NCCL-specific optimizations described below. Currently this has two effects, only under NCCL: the communicator is immediately formed (calling `ncclCommInit*` immediately rather than the normal lazy call) and sub-groups will use `ncclCommSplit` when possible to avoid unnecessary overhead of group creation. If you want to know NCCL initialization error early, you can also use this field. If an int is provided, the API assumes that the accelerator type at compile time will be used.
    
*   **\_ranks** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_ _|_ _None_) – The ranks in the process group. If provided, the process group name will be the hash of all the ranks in the group.
    
*   **enable\_reconfigure** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True`, create the backend in the reconfigure (fault tolerance) regime. The communicator is not initialized until `ProcessGroup.reconfigure()` is called. Backends that do not support reconfigure ignore this flag. Default is `False`.
    

Note

To enable `backend == Backend.MPI`, PyTorch needs to be built from source on a system that supports MPI.

Note

Support for multiple backends is experimental. Currently when no backend is specified, both `gloo` and `nccl` backends will be created. The `gloo` backend will be used for collectives with CPU tensors and the `nccl` backend will be used for collectives with CUDA tensors. A custom backend can be specified by passing in a string with format “<device\_type>:<backend\_name>,<device\_type>:<backend\_name>”, e.g. “cpu:gloo,cuda:custom\_backend”.

torch.distributed.device\_mesh.init\_device\_mesh(_device\_type_, _mesh\_shape_, _\*_, _mesh\_dim\_names\=None_, _backend\_override\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/device_mesh.py#L1640)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.device_mesh.init_device_mesh "Link to this definition")

Initializes a DeviceMesh based on device\_type, mesh\_shape, and mesh\_dim\_names parameters.

This creates a DeviceMesh with an n-dimensional array layout, where n is the length of mesh\_shape. If mesh\_dim\_names is provided, each dimension is labeled as mesh\_dim\_names\[i\].

Note

init\_device\_mesh follows SPMD programming model, meaning the same PyTorch Python program runs on all processes/ranks in the cluster. Ensure mesh\_shape (the dimensions of the nD array describing device layout) is identical across all ranks. Inconsistent mesh\_shape may lead to hanging.

Note

If no process group is found, init\_device\_mesh will initialize distributed process group/groups required for distributed communications behind the scene.

Parameters:

*   **device\_type** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The device type of the mesh. Currently supports: “cpu”, “cuda/cuda-like”, “xpu”. Passing in a device type with a GPU index, such as “cuda:0”, is not allowed.
    
*   **mesh\_shape** (_Tuple__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – A tuple defining the dimensions of the multi-dimensional array describing the layout of devices.
    
*   **mesh\_dim\_names** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _...__\]__,_ _optional_) – A tuple of mesh dimension names to assign to each dimension of the multi-dimensional array describing the layout of devices. Its length must match the length of mesh\_shape. Each string in mesh\_dim\_names must be unique.
    
*   **backend\_override** (_Dict__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
     _|_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _Options__\]_ _|_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
     _|_ _Options__\]__,_ _optional_) – Overrides for some or all of the ProcessGroups that will be created for each mesh dimension. Each key can be either the index of a dimension or its name (if mesh\_dim\_names is provided). Each value can be a tuple containing the name of the backend and its options, or just one of these two components (in which case the other will be set to its default value).
    

Returns:

A [`DeviceMesh`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.device_mesh.DeviceMesh "torch.distributed.device_mesh.DeviceMesh")
 object representing the device layout.

Return type:

[DeviceMesh](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.device_mesh.DeviceMesh "torch.distributed.device_mesh.DeviceMesh")

Example:

\>>> from torch.distributed.device\_mesh import init\_device\_mesh
\>>>
\>>> mesh\_1d \= init\_device\_mesh("cuda", mesh\_shape\=(8,))
\>>> mesh\_2d \= init\_device\_mesh("cuda", mesh\_shape\=(2, 8), mesh\_dim\_names\=("dp", "tp"))

Copy to clipboard

torch.distributed.is\_initialized()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L2117)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.is_initialized "Link to this definition")

Check if the default process group has been initialized.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.distributed.is\_mpi\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L2054)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.is_mpi_available "Link to this definition")

Check if the MPI backend is available.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.distributed.is\_nccl\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L2059)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.is_nccl_available "Link to this definition")

Check if the NCCL backend is available.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.distributed.is\_gloo\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L2064)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.is_gloo_available "Link to this definition")

Check if the Gloo backend is available.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.distributed.distributed\_c10d.is\_xccl\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L2074)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.distributed_c10d.is_xccl_available "Link to this definition")

Check if the XCCL backend is available.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.distributed.distributed\_c10d.batch\_isend\_irecv(_p2p\_op\_list_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L3892)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.distributed_c10d.batch_isend_irecv "Link to this definition")

Send or Receive a batch of tensors asynchronously and return a list of requests.

Process each of the operations in `p2p_op_list` and return the corresponding requests. NCCL, Gloo, and UCC backend are currently supported.

Parameters:

**p2p\_op\_list** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
_\[_[_P2POp_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.P2POp "torch.distributed.distributed_c10d.P2POp")\
_\]_) –

A list of point-to-point operations(type of each operator is `torch.distributed.P2POp`). All operations in the list are treated as a single batch – the relative ordering of sends vs. receives in the list does not matter and will not cause deadlocks. For example, `[recv_from_1, send_to_1]` is equivalent to `[send_to_1, recv_from_1]`.

The ordering **does** matter for multiple operations between the same pair of ranks in the same direction: if rank 0 calls `[send_to_1(A), send_to_1(B)]`, rank 1 must call `[recv_from_0(A), recv_from_0(B)]` in the same order to ensure the correct tensors are matched.

Returns:

A list of distributed request objects returned by calling the corresponding op in the op\_list.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[_Work_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.distributed_c10d.Work")\
\]

Examples

\>>> send\_tensor \= torch.arange(2, dtype\=torch.float32) + 2 \* rank
\>>> recv\_tensor \= torch.randn(2, dtype\=torch.float32)
\>>> send\_op \= dist.P2POp(dist.isend, send\_tensor, (rank + 1) % world\_size)
\>>> recv\_op \= dist.P2POp(
...     dist.irecv, recv\_tensor, (rank \- 1 + world\_size) % world\_size
... )
\>>> reqs \= batch\_isend\_irecv(\[send\_op, recv\_op\])
\>>> for req in reqs:
\>>>     req.wait()
\>>> recv\_tensor
tensor(\[2, 3\])     # Rank 0
tensor(\[0, 1\])     # Rank 1

Copy to clipboard

Note

Note that when this API is used with the NCCL PG backend, users must set the current GPU device with torch.cuda.set\_device, otherwise it will lead to unexpected hang issues.

In addition, if this API is the first collective call in the `group` passed to `dist.P2POp`, all ranks of the `group` must participate in this API call; otherwise, the behavior is undefined. If this API call is not the first collective call in the `group`, batched P2P operations involving only a subset of ranks of the `group` are allowed.

torch.distributed.distributed\_c10d.destroy\_process\_group(_group\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L3232)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.distributed_c10d.destroy_process_group "Link to this definition")

Destroy a given process group, and deinitialize the distributed package.

Parameters:

**group** (_ProcessGroup__,_ _optional_) – The process group to be destroyed, if group.WORLD is given, all process groups including the default one will be destroyed.

torch.distributed.distributed\_c10d.is\_backend\_available(_backend_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L2092)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.distributed_c10d.is_backend_available "Link to this definition")

Check backend availability.

Checks if the given backend is available and supports the built-in backends or third-party backends through function `Backend.register_backend`.

Parameters:

**backend** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – Backend name.

Returns:

Returns true if the backend is available otherwise false.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.distributed.distributed\_c10d.irecv(_tensor_, _src\=None_, _group\=None_, _tag\=0_, _group\_src\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L3553)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.distributed_c10d.irecv "Link to this definition")

Receives a tensor asynchronously.

Warning

`tag` is not supported with the NCCL backend.

Unlike recv, which is blocking, irecv allows src == dst rank, i.e. recv from self.

Parameters:

*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Tensor to fill with received data.
    
*   **src** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – Source rank on global process group (regardless of `group` argument). Will receive from any process if unspecified.
    
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.
    
*   **tag** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – Tag to match recv with remote send
    
*   **group\_src** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – Source rank on `group`. Invalid to specify both `src` and `group_src`.
    

Returns:

A distributed request object. None, if not part of the group

Return type:

[_Work_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.distributed_c10d.Work")
 | None

torch.distributed.distributed\_c10d.is\_gloo\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L2064)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.distributed_c10d.is_gloo_available "Link to this definition")

Check if the Gloo backend is available.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.distributed.distributed\_c10d.is\_initialized()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L2117)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.distributed_c10d.is_initialized "Link to this definition")

Check if the default process group has been initialized.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.distributed.distributed\_c10d.is\_mpi\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L2054)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.distributed_c10d.is_mpi_available "Link to this definition")

Check if the MPI backend is available.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.distributed.distributed\_c10d.is\_nccl\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L2059)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.distributed_c10d.is_nccl_available "Link to this definition")

Check if the NCCL backend is available.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.distributed.distributed\_c10d.is\_torchelastic\_launched()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L2122)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.distributed_c10d.is_torchelastic_launched "Link to this definition")

Check whether this process was launched with `torch.distributed.elastic` (aka torchelastic).

The existence of `TORCHELASTIC_RUN_ID` environment variable is used as a proxy to determine whether the current process was launched with torchelastic. This is a reasonable proxy since `TORCHELASTIC_RUN_ID` maps to the rendezvous id which is always a non-null value indicating the job id for peer discovery purposes..

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.distributed.distributed\_c10d.is\_ucc\_available()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L2069)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.distributed_c10d.is_ucc_available "Link to this definition")

Check if the UCC backend is available.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.distributed.is\_torchelastic\_launched()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L2122)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.is_torchelastic_launched "Link to this definition")

Check whether this process was launched with `torch.distributed.elastic` (aka torchelastic).

The existence of `TORCHELASTIC_RUN_ID` environment variable is used as a proxy to determine whether the current process was launched with torchelastic. This is a reasonable proxy since `TORCHELASTIC_RUN_ID` maps to the rendezvous id which is always a non-null value indicating the job id for peer discovery purposes..

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.distributed.get\_default\_backend\_for\_device(_device_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L2278)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.get_default_backend_for_device "Link to this definition")

Return the default backend for the given device.

Parameters:

**device** (_Union__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_,_ [_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")\
_\]_) – The device to get the default backend for.

Returns:

The default backend for the given device as a lower case string.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

* * *

Currently three initialization methods are supported:

### TCP initialization[#](https://docs.pytorch.org/docs/2.15/distributed.html#tcp-initialization "Link to this heading")

There are two ways to initialize using TCP, both requiring a network address reachable from all processes and a desired `world_size`. The first way requires specifying an address that belongs to the rank 0 process. This initialization method requires that all processes have manually specified ranks.

Note that multicast address is not supported anymore in the latest distributed package. `group_name` is deprecated as well.

import torch.distributed as dist

\# Use address of one of the machines
dist.init\_process\_group(backend, init\_method\='tcp://10.1.1.20:23456',
                        rank\=args.rank, world\_size\=4)

Copy to clipboard

### Shared file-system initialization[#](https://docs.pytorch.org/docs/2.15/distributed.html#shared-file-system-initialization "Link to this heading")

Another initialization method makes use of a file system that is shared and visible from all machines in a group, along with a desired `world_size`. The URL should start with `file://` and contain a path to a non-existent file (in an existing directory) on a shared file system. File-system initialization will automatically create that file if it doesn’t exist, but will not delete the file. Therefore, it is your responsibility to make sure that the file is cleaned up before the next [`init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")
 call on the same file path/name.

Note that automatic rank assignment is not supported anymore in the latest distributed package and `group_name` is deprecated as well.

Warning

This method assumes that the file system supports locking using `fcntl` - most local systems and NFS support it.

Warning

This method will always create the file and try its best to clean up and remove the file at the end of the program. In other words, each initialization with the file init method will need a brand new empty file in order for the initialization to succeed. If the same file used by the previous initialization (which happens not to get cleaned up) is used again, this is unexpected behavior and can often cause deadlocks and failures. Therefore, even though this method will try its best to clean up the file, if the auto-delete happens to be unsuccessful, it is your responsibility to ensure that the file is removed at the end of the training to prevent the same file to be reused again during the next time. This is especially important if you plan to call [`init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")
 multiple times on the same file name. In other words, if the file is not removed/cleaned up and you call [`init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")
 again on that file, failures are expected. The rule of thumb here is that, make sure that the file is non-existent or empty every time [`init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")
 is called.

import torch.distributed as dist

\# rank should always be specified
dist.init\_process\_group(backend, init\_method\='file:///mnt/nfs/sharedfile',
                        world\_size\=4, rank\=args.rank)

Copy to clipboard

### Environment variable initialization[#](https://docs.pytorch.org/docs/2.15/distributed.html#environment-variable-initialization "Link to this heading")

This method will read the configuration from environment variables, allowing one to fully customize how the information is obtained. The variables to be set are:

*   `MASTER_PORT` - required; has to be a free port on machine with rank 0
    
*   `MASTER_ADDR` - required (except for rank 0); address of rank 0 node
    
*   `WORLD_SIZE` - required; can be set either here, or in a call to init function
    
*   `RANK` - required; can be set either here, or in a call to init function
    

The machine with rank 0 will be used to set up all connections.

This is the default method, meaning that `init_method` does not have to be specified (or can be `env://`).

### Improving initialization time[#](https://docs.pytorch.org/docs/2.15/distributed.html#improving-initialization-time "Link to this heading")

*   `TORCH_GLOO_LAZY_INIT` - establishes connections on demand rather than using a full mesh which can greatly improve initialization time for non all2all operations.
    

Post-Initialization[#](https://docs.pytorch.org/docs/2.15/distributed.html#post-initialization "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

Once [`torch.distributed.init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")
 was run, the following functions can be used. To check whether the process group has already been initialized use [`torch.distributed.is_initialized()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.is_initialized "torch.distributed.is_initialized")
.

_class_ torch.distributed.Backend(_name_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L558)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Backend "Link to this definition")

An enum-like class for backends.

Available backends: GLOO, NCCL, UCC, MPI, XCCL, FAKE, and other registered backends.

The values of this class are lowercase strings, e.g., `"gloo"`. They can be accessed as attributes, e.g., `Backend.NCCL`.

This class can be directly called to parse the string, e.g., `Backend(backend_str)` will check if `backend_str` is valid, and return the parsed lowercase string if so. It also accepts uppercase strings, e.g., `Backend("GLOO")` returns `"gloo"`.

Note

The entry `Backend.UNDEFINED` is present but only used as initial value of some fields. Users should neither use it directly nor assume its existence.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

_classmethod_ register\_backend(_name_, _func_, _extended\_api\=False_, _devices\=None_, _\*_, _\_backend\_type\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L664)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Backend.register_backend "Link to this definition")

Register a new backend with the given name and instantiating function.

This class method is used by 3rd party `ProcessGroup` extension to register new backends.

Parameters:

*   **name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Backend name of the `ProcessGroup` extension. It should match the one in `init_process_group()`.
    
*   **func** (_function_) – Function handler that instantiates the backend. The function should be implemented in the backend extension and takes four arguments, including `store`, `rank`, `world_size`, and `timeout`.
    
*   **extended\_api** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Whether the backend supports extended argument structure. Default: `False`. If set to `True`, the backend will get an instance of `c10d::DistributedBackendOptions`, and a process group options object as defined by the backend implementation.
    
*   **devices** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _or_ [_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
     _of_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – device type this backend supports, e.g. “cpu”, “cuda”, etc. If None, assumes CPU and the current accelerator.
    

Note

This support of 3rd party backend is experimental and subject to change.

torch.distributed.get\_backend(_group\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L2194)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.get_backend "Link to this definition")

Return the backend of the given process group.

Parameters:

**group** (_ProcessGroup__,_ _optional_) – The process group to work on. The default is the general main process group. If another specific group is specified, the calling process must be part of `group`.

Returns:

The backend of the given process group as a lower case string.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

torch.distributed.get\_backend\_impl(_group\=None_, _device\=None_) → torch.\_C.\_distributed\_c10d.Backend[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L2220)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.get_backend_impl "Link to this definition")

Return the underlying backend implementation of the given process group.

This allows custom backends to expose backend-specific methods for experimentation purposes.

Warning

This API bypasses `torch.compile` tracing and other hooks. Backend methods are experimental and subject to breakage without warning.

Parameters:

*   **group** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _or_ _ProcessGroup__,_ _optional_) – The process group or process group name to work on. The default is the general main process group. If another specific group is specified, the calling process must be part of `group`.
    
*   **device** ([`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    , optional) – The device used to select a backend implementation. If `None`, this returns the bound device backend or the single backend shared by the registered devices. Default: `None`.
    

Returns:

The backend implementation for the given process group and device.

Return type:

torch.\_C.\_distributed\_c10d.Backend

torch.distributed.get\_backend\_config(_group\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L2174)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.get_backend_config "Link to this definition")

Return the backend configuration of the given process group.

Parameters:

**group** (_ProcessGroup__,_ _optional_) – The process group to work on. The default is the general main process group. If another specific group is specified, the calling process must be part of `group`.

Returns:

The backend configuration of the given process group as a lower case string.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

torch.distributed.get\_rank(_group\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L3450)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.get_rank "Link to this definition")

Return the rank of the current process in the provided `group`, default otherwise.

Rank is a unique identifier assigned to each process within a distributed process group. They are always consecutive integers ranging from 0 to `world_size`.

Parameters:

**group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.

Returns:

The rank of the process group -1, if not part of the group

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

torch.distributed.get\_world\_size(_group\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L3477)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.get_world_size "Link to this definition")

Return the number of processes in the current process group.

Parameters:

**group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.

Returns:

The world size of the process group -1, if not part of the group

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

torch.distributed.get\_debug\_level() → torch.\_C.\_distributed\_c10d.DebugLevel[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.get_debug_level "Link to this definition")

Gets the debug level of the torch.distributed package.

torch.distributed.get\_node\_local\_rank(_fallback\_rank\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L2346)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.get_node_local_rank "Link to this definition")

Return the local rank of the current process relative to the node.

Semantically, this is a useful concept for mapping processes to devices. For example, on a node with 8 accelerator you could use the node local rank to decide which accelerator device to bind the process to.

In practice, the actual assignment of node local ranks is handled by the process launcher outside of pytorch, and communicated via the LOCAL\_RANK environment variable.

Torchrun will automatically populate LOCAL\_RANK, but other launchers may not. If LOCAL\_RANK is unspecified, this API will fall back to the provided kwarg ‘fallback\_rank’ if specified, otherwise it will raise an error. The intent is to allow writing an application that runs either in single or multi device contexts without error.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

torch.distributed.get\_pg\_count()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L2338)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.get_pg_count "Link to this definition")

Return the number of process groups.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

torch.distributed.set\_timeout(_timeout_, _group\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L2396)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.set_timeout "Link to this definition")

Set the default timeout for all future operations on a process group.

This overrides the timeout configured when the group was created (via [`init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")
 or [`new_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.new_group "torch.distributed.new_group")
). The new timeout is forwarded to every backend registered with `group` – for example both the Gloo and NCCL backends of a group spanning CPU and CUDA devices. Backends that do not support changing their timeout (such as MPI and UCC) emit a warning and leave their timeout unchanged.

Parameters:

*   **timeout** (_timedelta_) – Timeout to set for operations executed against the process group. The default configured at initialization time is 10 minutes for NCCL and 30 minutes for other backends. For NCCL this is the duration after which collectives are aborted asynchronously and the process crashes; this is necessary because CUDA execution is async, so it is not safe to keep running user code once an async NCCL operation has failed (subsequent CUDA operations might run on corrupted data). When `TORCH_NCCL_BLOCKING_WAIT` is set, the process blocks and waits for this timeout instead.
    
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. The default is the general main process group. If another specific group is specified, the calling process must be part of `group`.
    

Raises:

[**ValueError**](https://docs.python.org/3/builtins/exceptions.html#ValueError "(in Python v3.15)")
 – If the calling process is not part of `group`.

Returns:

None

Return type:

None

Example::

\>>> import torch.distributed as dist
\>>> from datetime import timedelta
\>>> \# Shorten the timeout of the default process group to 30 seconds.
\>>> dist.set\_timeout(timedelta(seconds\=30))

Copy to clipboard

### Experimental collective time estimation[#](https://docs.pytorch.org/docs/2.15/distributed.html#experimental-collective-time-estimation "Link to this heading")

The context manager and the backend’s `_supports_time_estimate` capability probe are experimental and may change without notice.

torch.distributed.distributed\_c10d.\_time\_estimator(_group\=None_, _device\=None_) → Iterator\[\_TimeEstimator\][\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L3842)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.distributed_c10d._time_estimator "Link to this definition")

Estimate the execution time of collectives without running them.

A supported backend simulates collectives issued inside the context. After the context exits, `estimated_time` contains their total duration in microseconds.

Warning

This API is experimental and subject to change. It currently supports only NCCL-based backends. The NCCL communicator must be initialized before entering the context so the estimate reflects its actual topology. Pass `device_id` to `init_process_group()` or issue a collective first.

Parameters:

*   **group** (_ProcessGroup__,_ _optional_) – Process group whose backend should simulate the collectives. Default: `None` uses the default process group.
    
*   **device** ([_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    _,_ _optional_) – Device whose backend should perform the estimation. Default: `None` uses the process group’s default device.
    

Yields:

_\_TimeEstimator_ –

Context object whose `estimated_time` attribute is populated

when the context exits.

Return type:

[_Iterator_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.15)")
\[_\_TimeEstimator_\]

Examples:

\>>> tensor \= torch.ones(1024, device\="cuda")
\>>> dist.all\_reduce(tensor)  \# Initialize the communicator.
\>>> with dist.\_time\_estimator() as estimate:
...     dist.all\_reduce(tensor)
\>>> estimate.estimated\_time  \# Total simulated duration in microseconds.

Copy to clipboard

### Fault-tolerant reconfiguration[#](https://docs.pytorch.org/docs/2.15/distributed.html#fault-tolerant-reconfiguration "Link to this heading")

torch.distributed.distributed\_c10d.\_supports\_reconfigure(_group\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L8179)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.distributed_c10d._supports_reconfigure "Link to this definition")

Return whether `group` supports the reconfigure-based fault tolerance API.

Warning

This API is experimental and subject to change or removal.

Parameters:

**group** (_ProcessGroup__,_ _optional_) – The process group to query. If `None`, the default process group is used.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.distributed.distributed\_c10d.\_get\_reconfigure\_handle(_group\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L8194)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.distributed_c10d._get_reconfigure_handle "Link to this definition")

Return an opaque reconfigure handle for `group`.

The handle encodes the information peers exchange out-of-band to (re)initialize the communicator via [`_reconfigure()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.distributed_c10d._reconfigure "torch.distributed.distributed_c10d._reconfigure")
.

Warning

This API is experimental and subject to change or removal.

Parameters:

**group** (_ProcessGroup__,_ _optional_) – The process group to query. If `None`, the default process group is used.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

torch.distributed.distributed\_c10d.\_reconfigure(_uuid_, _handles_, _group\=None_, _timeout\=None_, _hints\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L8212)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.distributed_c10d._reconfigure "Link to this definition")

Reconfigure `group` with a new set of peers for fault tolerance.

Warning

This API is experimental and subject to change or removal.

Parameters:

*   **uuid** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Uniquely identifies this instance of the communicator. Pass a fresh value on every (re)initialization.
    
*   **handles** ([_set_](https://docs.python.org/3/builtins/stdtypes.html#set "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\] or_ [_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_) – One reconfigure handle per peer, as returned by [`_get_reconfigure_handle()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.distributed_c10d._get_reconfigure_handle "torch.distributed.distributed_c10d._get_reconfigure_handle")
    . A list assigns ranks by position; a set lets the backend choose the rank assignment.
    
*   **group** (_ProcessGroup__,_ _optional_) – The process group to reconfigure. If `None`, the default process group is used.
    
*   **timeout** (_timedelta__,_ _optional_) – How long to allow reconfiguration before failing. `None` uses the backend’s default timeout.
    
*   **hints** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]__,_ _optional_) – Backend-specific configuration.
    

Returns:

An async work handle for the reconfigure operation.

Return type:

[Work](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.distributed_c10d.Work")

Example::

\>>> dist.init\_process\_group("gloo", enable\_reconfigure\=True)
\>>> \# Every peer receives the same fresh UUID and rank-ordered handles.
\>>> uuid, handles \= rendezvous\_reconfigure(dist.\_get\_reconfigure\_handle())
\>>> dist.\_reconfigure(uuid\=uuid, handles\=handles).wait()

Copy to clipboard

Shutdown[#](https://docs.pytorch.org/docs/2.15/distributed.html#shutdown "Link to this heading")

-------------------------------------------------------------------------------------------------

It is important to clean up resources on exit by calling `destroy_process_group()`.

The simplest pattern to follow is to destroy every process group and backend by calling `destroy_process_group()` with the default value of None for the `group` argument, at a point in the training script where communications are no longer needed, usually near the end of main(). The call should be made once per trainer-process, not at the outer process-launcher level.

if `destroy_process_group()` is not called by all ranks in a pg within the timeout duration, especially when there are multiple process-groups in the application e.g. for N-D parallelism, hangs on exit are possible. This is because the destructor for ProcessGroupNCCL calls ncclCommAbort, which must be called collectively, but the order of calling ProcessGroupNCCL’s destructor if called by python’s GC is not deterministic. Calling `destroy_process_group()` helps by ensuring ncclCommAbort is called in a consistent order across ranks, and avoids calling ncclCommAbort during ProcessGroupNCCL’s destructor.

### Reinitialization[#](https://docs.pytorch.org/docs/2.15/distributed.html#reinitialization "Link to this heading")

`destroy_process_group` can also be used to destroy individual process groups. One use case could be fault tolerant training, where a process group may be destroyed and then a new one initialized during runtime. In this case, it’s critical to synchronize the trainer processes using some means other than torch.distributed primitives \_after\_ calling destroy and before subsequently initializing. This behavior is currently unsupported/untested, due to the difficulty of achieving this synchronization, and is considered a known issue. Please file a github issue or RFC if this is a use case that’s blocking you.

* * *

Groups[#](https://docs.pytorch.org/docs/2.15/distributed.html#groups "Link to this heading")

---------------------------------------------------------------------------------------------

By default collectives operate on the default group (also called the world) and require all processes to enter the distributed function call. However, some workloads can benefit from more fine-grained communication. This is where distributed groups come into play. [`new_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.new_group "torch.distributed.new_group")
 function can be used to create new groups, with arbitrary subsets of all processes. It returns an opaque group handle that can be given as a `group` argument to all collectives (collectives are distributed functions to exchange information in certain well-known programming patterns).

torch.distributed.new\_group(_ranks\=None_, _timeout\=None_, _backend\=None_, _pg\_options\=None_, _use\_local\_synchronization\=False_, _group\_desc\=None_, _device\_id\=None_, _sort\_ranks\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L7045)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.new_group "Link to this definition")

Create a new distributed group.

This function requires that all processes in the main group (i.e. all processes that are part of the distributed job) enter this function, even if they are not going to be members of the group. Additionally, groups should be created in the same order in all processes.

Warning

Safe concurrent usage: When using multiple process groups with the `NCCL` backend, the user must ensure a globally consistent execution order of collectives across ranks.

If multiple threads within a process issue collectives, explicit synchronization is necessary to ensure consistent ordering.

When using async variants of torch.distributed communication APIs, a work object is returned and the communication kernel is enqueued on a separate CUDA stream, allowing overlap of communication and computation. Once one or more async ops have been issued on one process group, they must be synchronized with other cuda streams by calling work.wait() before using another process group.

See Using multiple NCCL communicators concurrently <https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/communicators.html#using-multiple-nccl-communicators-concurrently> for more details.

Parameters:

*   **ranks** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – List of ranks of group members. If `None`, will be set to all ranks. Default is `None`.
    
*   **timeout** (_timedelta__,_ _optional_) – see init\_process\_group for details and default value.
    
*   **backend** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _or_ [_Backend_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Backend "torch.distributed.Backend")
    _,_ _optional_) – The backend to use. Depending on build-time configurations, valid values are `gloo` and `nccl`. By default uses the same backend as the global group. This field should be given as a lowercase string (e.g., `"gloo"`), which can also be accessed via [`Backend`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Backend "torch.distributed.Backend")
     attributes (e.g., `Backend.GLOO`). If `None` is passed in, the backend corresponding to the default process group will be used. Default is `None`.
    
*   **pg\_options** (`Backend.Options`, optional) – process group options specifying what additional options need to be passed in during the construction of specific process groups. i.e. for the `nccl` backend, `is_high_priority_stream` can be specified so that process group can pick up high priority cuda streams. For other available options to config nccl, See [https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/api/types.html#ncclconfig-tuse\_local\_synchronization](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/api/types.html#ncclconfig-tuse_local_synchronization)
     (bool, optional): perform a group-local barrier at the end of the process group creation. This is different in that non-member ranks don’t need to call into API and don’t join the barrier.
    
*   **group\_desc** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – a string to describe the process group.
    
*   **device\_id** ([_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    _,_ _optional_) – a single, specific device to “bind” this process to, The new\_group call will try to initialize a communication backend immediately for the device if this field is given.
    
*   **sort\_ranks** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True` (the default), sort the `ranks` list before creating the group. If `False`, preserve the caller-provided rank order so that position in the `ranks` list determines group rank. All processes must pass the identical `ranks` list. Default is `True`.
    

Returns:

A handle of distributed group that can be given to collective calls or GroupMember.NON\_GROUP\_MEMBER if the rank is not part of `ranks`.

Return type:

_ProcessGroup_ | [_Literal_](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.15)")
\[-100\]

N.B. use\_local\_synchronization doesn’t work with MPI.

N.B. While use\_local\_synchronization=True can be significantly faster with larger clusters and small process groups, care must be taken since it changes cluster behavior as non-member ranks don’t join the group barrier().

N.B. use\_local\_synchronization=True can lead to deadlocks when each rank creates multiple overlapping process groups. To avoid that, make sure all ranks follow the same global creation order.

N.B. When TorchComms is enabled (`torch.distributed.config.use_torchcomms` / `TORCH_DISTRIBUTED_USE_TORCHCOMMS=1`), subgroups are created directly via TorchComms’ `new_comm` (the normal `_new_group_with_tag` path), not by splitting the parent communicator. Pass `backend="nccl-lazy"` to build a per-peer, lazily-initialized group (a dedicated comm + stream per send/recv peer, like `ProcessGroupNCCL`) so concurrent P2P to different peers can overlap; pass the default / `"nccl"` backend for an eager group.

torch.distributed.distributed\_c10d.shrink\_group(_ranks\_to\_exclude_, _group\=None_, _shrink\_flags\=0_, _pg\_options\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L7615)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.distributed_c10d.shrink_group "Link to this definition")

Shrinks a process group by excluding specified ranks.

Creates and returns a new, smaller process group comprising only the ranks from the original group that were not in the `ranks_to_exclude` list.

Parameters:

*   **ranks\_to\_exclude** (_List__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – A list of ranks from the original `group` to exclude from the new group.
    
*   **group** (_ProcessGroup__,_ _optional_) – The process group to shrink. If `None`, the default process group is used. Defaults to `None`.
    
*   **shrink\_flags** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – Flags to control the shrinking behavior. Can be `SHRINK_DEFAULT` (default) or `SHRINK_ABORT`. `SHRINK_ABORT` will attempt to terminate ongoing operations in the parent communicator before shrinking. Defaults to `SHRINK_DEFAULT`.
    
*   **pg\_options** (`Backend.Options`, optional) – Backend-specific options to apply to the shrunken process group. If provided, the backend will use these options when creating the new group. If omitted, the new group inherits defaults from the parent.
    

Returns:

a new group comprised of the remaining ranks. If the default group was shrunk, the returned group becomes the new default group.

Return type:

ProcessGroup

Raises:

*   [**TypeError**](https://docs.python.org/3/builtins/exceptions.html#TypeError "(in Python v3.15)")
     – if the group’s backend does not support shrinking.
    
*   [**ValueError**](https://docs.python.org/3/builtins/exceptions.html#ValueError "(in Python v3.15)")
     – if `ranks_to_exclude` is invalid (empty, out of bounds,
    
*   **duplicates****, or** **excludes all ranks****)****.** –
    
*   [**RuntimeError**](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "(in Python v3.15)")
     – if an excluded rank calls this function or the backend
    
*   **fails the operation.** –
    

Notes

*   Only non-excluded ranks should call this function; excluded ranks must not participate in the shrink operation.
    
*   Shrinking the default group destroys all other process groups since rank reassignment makes them inconsistent.
    

torch.distributed.get\_group\_rank(_group_, _global\_rank_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L1829)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.get_group_rank "Link to this definition")

Translate a global rank into a group rank.

`global_rank` must be part of `group` otherwise this raises RuntimeError.

Parameters:

*   **group** (_ProcessGroup_) – ProcessGroup to find the relative rank.
    
*   **global\_rank** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Global rank to query.
    

Returns:

Group rank of `global_rank` relative to `group`

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

N.B. calling this function on the default process group returns identity

torch.distributed.get\_global\_rank(_group_, _group\_rank_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L1857)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.get_global_rank "Link to this definition")

Translate a group rank into a global rank.

`group_rank` must be part of group otherwise this raises RuntimeError.

Parameters:

*   **group** (_ProcessGroup_) – ProcessGroup to find the global rank from.
    
*   **group\_rank** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Group rank to query.
    

Returns:

Global rank of `group_rank` relative to `group`

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

N.B. calling this function on the default process group returns identity

torch.distributed.get\_process\_group\_ranks(_group_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L1895)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.get_process_group_ranks "Link to this definition")

Get all ranks associated with `group`.

Parameters:

**group** (_Optional__\[__ProcessGroup__\]_) – ProcessGroup to get all ranks from. If None, the default process group will be used.

Returns:

List of global ranks ordered by group rank.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
\]

torch.distributed.split\_group(_parent\_pg\=None_, _split\_ranks\=None_, _timeout\=None_, _pg\_options\=None_, _group\_desc\=None_, _backend\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L6782)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.split_group "Link to this definition")

Create a new process group split from the given parent process group.

Warning

This is an experimental API. The selected parent backend must implement process-group splitting. Built-in support includes `NCCL`, `XCCL`, and `Gloo`. Custom backends are responsible for cloning the prefixed child Store if they require an independent connection or mutate connection-global state such as the Store timeout.

Users of this API must guarantee that all ranks in the parent group enter this API call, and the split of the sub groups is the same across all ranks in the parent group.

Parameters:

*   **parent\_pg** (_ProcessGroup__,_ _optional_) – The parent process group. If None, the default process group will be used. Users need to guarantee that the parent group is fully initialized (e.g, communicators are initialized)
    
*   **split\_ranks** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]__\]_) – the split ranks, which is a list of list of ranks. Users need to make sure the validity of the split ranks such that one split (represented by one inner list of ints) does not overlap with any other split. Note that the ranks in each split is the group rank (instead of global rank) in the parent pg. For example, if the parent group has 4 ranks, and split\_ranks can be \[\[0, 1\], \[2, 3\]\]. Note \[\[0,1\]\] is also a valid split, in which case ranks 2, 3 would return a non-group member. The order of ranks within each split is preserved: position in the list determines the group rank in the new group. All ranks must pass the same ordering.
    
*   **timeout** (_timedelta__,_ _optional_) – see init\_process\_group for details and default value.
    
*   **pg\_options** (`Backend.Options`, optional) – Additional options need to be passed in during the construction of specific process groups. i.e.\`\`is\_high\_priority\_stream\`\` can be specified so that process group can pick up high priority cuda streams.
    
*   **group\_desc** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – a string to describe the process group.
    
*   **backend** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _or_ [_Backend_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Backend "torch.distributed.Backend")
    _,_ _optional_) – selects a subset of the parent process group’s per-device backends to retain in the child group. The string follows the same format as `init_process_group` (e.g. `"nccl"` or `"cpu:gloo,cuda:nccl"`). Each device type in the requested backend must be present in the parent group, and the backend name for that device type must exactly match the parent’s. The child’s default backend’s device type must be in the requested set. If `None` (default), the child inherits the full backend configuration of the parent.
    

Returns:

ProcessGroup if the current rank is within one split/subgroup given by split\_ranks, or GroupMember.NON\_GROUP\_MEMBER if the current rank is not part of any split in `split_ranks`.

Return type:

_ProcessGroup_ | [_Literal_](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.15)")
\[-100\]

torch.distributed.distributed\_c10d.GroupName _\= torch.distributed.distributed\_c10d.GroupName_[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.distributed_c10d.GroupName "Link to this definition")

NewType creates simple unique types with almost zero runtime overhead.

NewType(name, tp) is considered a subtype of tp by static type checkers. At runtime, NewType(name, tp) returns a dummy callable that simply returns its argument.

Usage:

UserId \= NewType('UserId', int)

def name\_by\_id(user\_id: UserId) \-> str:
    ...

UserId('user')          \# Fails type check

name\_by\_id(42)          \# Fails type check
name\_by\_id(UserId(42))  \# OK

num \= UserId(5) + 1     \# type: int

Copy to clipboard

DeviceMesh[#](https://docs.pytorch.org/docs/2.15/distributed.html#devicemesh "Link to this heading")

-----------------------------------------------------------------------------------------------------

DeviceMesh is a higher level abstraction that manages process groups (or NCCL communicators). It allows user to easily create inter node and intra node process groups without worrying about how to set up the ranks correctly for different sub process groups, and it helps manage those distributed process group easily. [`init_device_mesh()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.device_mesh.init_device_mesh "torch.distributed.device_mesh.init_device_mesh")
 function can be used to create new DeviceMesh, with a mesh shape describing the device topology.

_class_ torch.distributed.device\_mesh.DeviceMesh(_device\_type_, _mesh\=None_, _\*_, _mesh\_dim\_names\=None_, _backend\_override\=None_, _preserve\_rank\_order\=False_, _\_init\_backend\=True_, _\_rank\=None_, _\_layout\=None_, _\_rank\_map\=None_, _\_root\_mesh\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/device_mesh.py#L188)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.device_mesh.DeviceMesh "Link to this definition")

DeviceMesh represents a mesh of devices, where layout of devices could be represented as a n-d dimension array, and each value of the n-d dimensional array is the global id of the default process group ranks.

DeviceMesh could be used to setup the N dimensional device connections across the cluster, and manage the ProcessGroups for N dimensional parallelisms. Communications could happen on each dimension of the DeviceMesh separately. DeviceMesh respects the device that user selects already (i.e. if user call torch.cuda.set\_device before the DeviceMesh initialization), and will select/set the device for the current process if user does not set the device beforehand. Note that manual device selection should happen BEFORE the DeviceMesh initialization.

DeviceMesh can also be used as a context manager when using together with DTensor APIs.

Note

DeviceMesh follows SPMD programming model, which means the same PyTorch Python program is running on all processes/ranks in the cluster. Therefore, users need to make sure the mesh array (which describes the layout of devices) should be identical across all ranks. Inconsistent mesh will lead to silent hang.

Parameters:

*   **device\_type** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The device type of the mesh. Currently supports: “cpu”, “cuda/cuda-like”.
    
*   **mesh** (_ndarray_) – A multi-dimensional array or an integer tensor describing the layout of devices, where the IDs are global IDs of the default process group.
    
*   **preserve\_rank\_order** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If True, subgroup rank order is preserved instead of being sorted in ascending order, and a mesh dim spanning the full world whose ranks are a permutation of \[0..N) gets a dedicated process group honoring that order instead of silently reusing default\_group. This provides flexibility for custom or topology-aware rank ordering. Defaults to False for backward compatibility with existing code that relies on sorted ranks and default\_group reuse.\
    \
*   **\_rank** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – (experimental/internal) The global rank of the current process. If not provided, it will be inferred from the default process group.\
    \
\
Returns:\
\
A [`DeviceMesh`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.device_mesh.DeviceMesh "torch.distributed.device_mesh.DeviceMesh")\
 object representing the device layout.\
\
Return type:\
\
[DeviceMesh](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.device_mesh.DeviceMesh "torch.distributed.device_mesh.DeviceMesh")\
\
The following program runs on each process/rank in an SPMD manner. In this example, we have 2 hosts with 4 GPUs each. A reduction over the first dimension of mesh will reduce across columns (0, 4), .. and (3, 7), a reduction over the second dimension of mesh reduces across rows (0, 1, 2, 3) and (4, 5, 6, 7).\
\
Example:\
\
\>>> from torch.distributed.device\_mesh import DeviceMesh\
\>>>\
\>>> \# Initialize device mesh as (2, 4) to represent the topology\
\>>> \# of cross-host(dim 0), and within-host (dim 1).\
\>>> mesh \= DeviceMesh(device\_type\="cuda", mesh\=\[\[0, 1, 2, 3\],\[4, 5, 6, 7\]\])\
\
Copy to clipboard\
\
abort()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/device_mesh.py#L910)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.device_mesh.DeviceMesh.abort "Link to this definition")\
\
Abort all process groups associated with this DeviceMesh.\
\
When a rank in a DeviceMesh exits prematurely, other ranks can call this method to abort the mesh’s process groups instead of hanging.\
\
This method must be called on a root mesh. Calling it on a submesh raises `RuntimeError` because the scope of a submesh abort is ambiguous.\
\
Note\
\
This API is experimental. For NCCL backends, aborts are performed concurrently using group semantics to avoid deadlocks. For other backends, `abort()` is called serially on each process group.\
\
_property_ device\_type_: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.device_mesh.DeviceMesh.device_type "Link to this definition")\
\
Returns the device type of the mesh.\
\
_static_ from\_group(_group_, _device\_type_, _mesh\=None_, _\*_, _mesh\_dim\_names\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/device_mesh.py#L1191)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.device_mesh.DeviceMesh.from_group "Link to this definition")\
\
Constructs a [`DeviceMesh`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.device_mesh.DeviceMesh "torch.distributed.device_mesh.DeviceMesh")\
 with `device_type` from an existing `ProcessGroup` or a list of existing `ProcessGroup`.\
\
The constructed device mesh has number of dimensions equal to the number of groups passed. For example, if a single process group is passed in, the resulted DeviceMesh is a 1D mesh. If a list of 2 process groups is passed in, the resulted DeviceMesh is a 2D mesh.\
\
If more than one group is passed, then the `mesh` and `mesh_dim_names` arguments are required. The order of the process groups passed in determines the topology of the mesh. For example, the first process group will be the 0th dimension of the DeviceMesh. The mesh tensor passed in must have the same number of dimensions as the number of process groups passed in, and the order of the dimensions in the mesh tensor must match the order in the process groups passed in.\
\
Parameters:\
\
*   **group** (_ProcessGroup_ _or_ [_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
    _\[__ProcessGroup__\]_) – the existing ProcessGroup or a list of existing ProcessGroups.\
    \
*   **device\_type** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – The device type of the mesh. Currently supports: “cpu”, “cuda/cuda-like”. Passing in a device type with a GPU index, such as “cuda:0”, is not allowed.\
    \
*   **mesh** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
     _or_ _ArrayLike__,_ _optional_) – A multi-dimensional array or an integer tensor describing the layout of devices, where the IDs are global IDs of the default process group. Default is None.\
    \
*   **mesh\_dim\_names** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _...__\]__,_ _optional_) – A tuple of mesh dimension names to assign to each dimension of the multi-dimensional array describing the layout of devices. Its length must match the length of mesh\_shape. Each string in mesh\_dim\_names must be unique. Default is None.\
    \
\
Returns:\
\
A [`DeviceMesh`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.device_mesh.DeviceMesh "torch.distributed.device_mesh.DeviceMesh")\
 object representing the device layout.\
\
Return type:\
\
[DeviceMesh](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.device_mesh.DeviceMesh "torch.distributed.device_mesh.DeviceMesh")\
\
get\_all\_groups()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/device_mesh.py#L901)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.device_mesh.DeviceMesh.get_all_groups "Link to this definition")\
\
Returns a list of ProcessGroups for all mesh dimensions.\
\
Returns:\
\
A list of `ProcessGroup` object.\
\
Return type:\
\
[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[_ProcessGroup_\]\
\
get\_coordinate()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/device_mesh.py#L1371)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.device_mesh.DeviceMesh.get_coordinate "Link to this definition")\
\
Return the relative indices of this rank relative to all dimensions of the mesh. If this rank is not part of the mesh, return None.\
\
Return type:\
\
[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, …\] | None\
\
get\_group(_mesh\_dim\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/device_mesh.py#L846)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.device_mesh.DeviceMesh.get_group "Link to this definition")\
\
Returns the single ProcessGroup specified by mesh\_dim, or, if mesh\_dim is not specified and the DeviceMesh is 1-dimensional, returns the only ProcessGroup in the mesh.\
\
Parameters:\
\
*   **mesh\_dim** (_str/python:int__,_ _optional_) – it can be the name of the mesh dimension or the index\
    \
*   **None.** (_of the mesh dimension. Default is_) –\
    \
\
Returns:\
\
A `ProcessGroup` object.\
\
Return type:\
\
_ProcessGroup_\
\
get\_local\_rank(_mesh\_dim\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/device_mesh.py#L1308)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.device_mesh.DeviceMesh.get_local_rank "Link to this definition")\
\
Returns the local rank of the given mesh\_dim of the DeviceMesh.\
\
Parameters:\
\
*   **mesh\_dim** (_str/python:int__,_ _optional_) – it can be the name of the mesh dimension or the index\
    \
*   **None.** (_of the mesh dimension. Default is_) –\
    \
\
Returns:\
\
An integer denotes the local rank.\
\
Return type:\
\
[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
\
The following program runs on each process/rank in an SPMD manner. In this example, we have 2 hosts with 4 GPUs each. Calling mesh\_2d.get\_local\_rank(mesh\_dim=0) on rank 0, 1, 2, 3 would return 0. Calling mesh\_2d.get\_local\_rank(mesh\_dim=0) on rank 4, 5, 6, 7 would return 1. Calling mesh\_2d.get\_local\_rank(mesh\_dim=1) on rank 0, 4 would return 0. Calling mesh\_2d.get\_local\_rank(mesh\_dim=1) on rank 1, 5 would return 1. Calling mesh\_2d.get\_local\_rank(mesh\_dim=1) on rank 2, 6 would return 2. Calling mesh\_2d.get\_local\_rank(mesh\_dim=1) on rank 3, 7 would return 3.\
\
Example:\
\
\>>> from torch.distributed.device\_mesh import DeviceMesh\
\>>>\
\>>> \# Initialize device mesh as (2, 4) to represent the topology\
\>>> \# of cross-host(dim 0), and within-host (dim 1).\
\>>> mesh \= DeviceMesh(device\_type\="cuda", mesh\=\[\[0, 1, 2, 3\],\[4, 5, 6, 7\]\])\
\
Copy to clipboard\
\
get\_rank()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/device_mesh.py#L1302)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.device_mesh.DeviceMesh.get_rank "Link to this definition")\
\
Returns the current global rank.\
\
Return type:\
\
[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
\
_property_ mesh_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.device_mesh.DeviceMesh.mesh "Link to this definition")\
\
Returns the tensor representing the layout of devices.\
\
_property_ mesh\_dim\_names_: [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, ...\] | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
_[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.device_mesh.DeviceMesh.mesh_dim_names "Link to this definition")\
\
Returns the names of mesh dimensions.\
\
Point-to-point communication[#](https://docs.pytorch.org/docs/2.15/distributed.html#point-to-point-communication "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------------------------\
\
torch.distributed.send(_tensor_, _dst\=None_, _group\=None_, _tag\=0_, _group\_dst\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L3610)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.send "Link to this definition")\
\
Send a tensor synchronously.\
\
Warning\
\
`tag` is not supported with the NCCL backend.\
\
Parameters:\
\
*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Tensor to send.\
    \
*   **dst** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – Destination rank on global process group (regardless of `group` argument). Destination rank should not be the same as the rank of the current process.\
    \
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.\
    \
*   **tag** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Tag to match send with remote recv\
    \
*   **group\_dst** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Destination rank on `group`. Invalid to specify both `dst` and `group_dst`.\
    \
\
torch.distributed.recv(_tensor_, _src\=None_, _group\=None_, _tag\=0_, _group\_src\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L3654)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.recv "Link to this definition")\
\
Receives a tensor synchronously.\
\
Warning\
\
`tag` is not supported with the NCCL backend.\
\
Parameters:\
\
*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Tensor to fill with received data.\
    \
*   **src** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Source rank on global process group (regardless of `group` argument). Will receive from any process if unspecified.\
    \
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.\
    \
*   **tag** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Tag to match recv with remote send\
    \
*   **group\_src** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Destination rank on `group`. Invalid to specify both `src` and `group_src`.\
    \
\
Returns:\
\
Sender rank -1, if not part of the group\
\
Return type:\
\
[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
\
[`isend()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.isend "torch.distributed.isend")\
 and [`irecv()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.irecv "torch.distributed.irecv")\
 return distributed request objects when used. In general, the type of this object is unspecified as they should never be created manually, but they are guaranteed to support two methods:\
\
*   `is_completed()` - returns True if the operation has finished\
    \
*   `wait()` - will block the process until the operation is finished. `is_completed()` is guaranteed to return True once it returns.\
    \
\
torch.distributed.isend(_tensor_, _dst\=None_, _group\=None_, _tag\=0_, _group\_dst\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L3496)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.isend "Link to this definition")\
\
Send a tensor asynchronously.\
\
Warning\
\
Modifying `tensor` before the request completes causes undefined behavior.\
\
Warning\
\
`tag` is not supported with the NCCL backend.\
\
Unlike send, which is blocking, isend allows src == dst rank, i.e. send to self.\
\
Parameters:\
\
*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Tensor to send.\
    \
*   **dst** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – Destination rank on global process group (regardless of `group` argument)\
    \
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.\
    \
*   **tag** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Tag to match send with remote recv\
    \
*   **group\_dst** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Destination rank on `group`. Invalid to specify both `dst` and `group_dst`\
    \
\
Returns:\
\
A distributed request object. None, if not part of the group\
\
Return type:\
\
[_Work_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.distributed_c10d.Work")\
 | None\
\
torch.distributed.irecv(_tensor_, _src\=None_, _group\=None_, _tag\=0_, _group\_src\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L3553)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.irecv "Link to this definition")\
\
Receives a tensor asynchronously.\
\
Warning\
\
`tag` is not supported with the NCCL backend.\
\
Unlike recv, which is blocking, irecv allows src == dst rank, i.e. recv from self.\
\
Parameters:\
\
*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Tensor to fill with received data.\
    \
*   **src** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Source rank on global process group (regardless of `group` argument). Will receive from any process if unspecified.\
    \
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.\
    \
*   **tag** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Tag to match recv with remote send\
    \
*   **group\_src** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Source rank on `group`. Invalid to specify both `src` and `group_src`.\
    \
\
Returns:\
\
A distributed request object. None, if not part of the group\
\
Return type:\
\
[_Work_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.distributed_c10d.Work")\
 | None\
\
torch.distributed.send\_object\_list(_object\_list_, _dst\=None_, _group\=None_, _device\=None_, _group\_dst\=None_, _use\_batch\=False_, _weights\_only\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L4631)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.send_object_list "Link to this definition")\
\
Sends picklable objects in `object_list` synchronously.\
\
Similar to [`send()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.send "torch.distributed.send")\
, but Python objects can be passed in. Note that all objects in `object_list` must be picklable in order to be sent.\
\
Parameters:\
\
*   **object\_list** (_List__\[__Any__\]_) – List of input objects to sent. Each object must be picklable. Receiver must provide lists of equal sizes.\
    \
*   **dst** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – Destination rank to send `object_list` to. Destination rank is based on global process group (regardless of `group` argument)\
    \
*   **group** (_ProcessGroup_ _|_ _None_) – (ProcessGroup, optional): The process group to work on. If None, the default process group will be used. Default is `None`.\
    \
*   **device** (`torch.device`, optional) – If not None, the objects are serialized and converted to tensors which are moved to the `device` before sending. Default is `None`.\
    \
*   **group\_dst** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Destination rank on `group`. Must specify one of `dst` and `group_dst` but not both\
    \
*   **use\_batch** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – If True, use batch p2p operations instead of regular send operations. This avoids initializing 2-rank communicators and uses existing entire group communicators. See batch\_isend\_irecv for usage and assumptions. Default is `False`.\
    \
*   **weights\_only** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – If `True`, objects are serialized with `torch.save`, which the receiver can deserialize with `torch.load(weights_only=True)`. If `False`, `pickle` is used, which is insecure with untrusted data. Must match the value passed to [`recv_object_list()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.recv_object_list "torch.distributed.recv_object_list")\
     on the receiver. Default is `False`.\
    \
\
Returns:\
\
`None`.\
\
Return type:\
\
None\
\
Note\
\
For NCCL-based process groups, internal tensor representations of objects must be moved to the GPU device before communication takes place. In this case, the device used is given by `torch.cuda.current_device()` and it is the user’s responsibility to ensure that this is set so that each rank has an individual GPU, via `torch.cuda.set_device()`.\
\
Warning\
\
Object collectives have a number of serious performance and scalability limitations. See [Object collectives](https://docs.pytorch.org/docs/2.15/distributed.html#object-collectives)\
 for details.\
\
Warning\
\
[`send_object_list()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.send_object_list "torch.distributed.send_object_list")\
 with `weights_only=False` uses `pickle` module implicitly, which is known to be insecure. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling. Only call this function with data you trust.\
\
Warning\
\
Calling [`send_object_list()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.send_object_list "torch.distributed.send_object_list")\
 with GPU tensors is not well supported and inefficient as it incurs GPU -> CPU transfer since tensors would be pickled. Please consider using [`send()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.send "torch.distributed.send")\
 instead.\
\
Example::\
\
\>>> \# Note: Process group initialization omitted on each rank.\
\>>> import torch.distributed as dist\
\>>> \# Assumes backend is not NCCL\
\>>> device \= torch.device("cpu")\
\>>> if dist.get\_rank() \== 0:\
\>>>     \# Assumes world\_size of 2.\
\>>>     objects \= \["foo", 12, {1: 2}\] \# any picklable object\
\>>>     dist.send\_object\_list(objects, dst\=1, device\=device)\
\>>> else:\
\>>>     objects \= \[None, None, None\]\
\>>>     dist.recv\_object\_list(objects, src\=0, device\=device)\
\>>> objects\
\['foo', 12, {1: 2}\]\
\
Copy to clipboard\
\
torch.distributed.recv\_object\_list(_object\_list_, _src\=None_, _group\=None_, _device\=None_, _group\_src\=None_, _use\_batch\=False_, _weights\_only\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L4758)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.recv_object_list "Link to this definition")\
\
Receives picklable objects in `object_list` synchronously.\
\
Similar to [`recv()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.recv "torch.distributed.recv")\
, but can receive Python objects.\
\
Parameters:\
\
*   **object\_list** (_List__\[__Any__\]_) – List of objects to receive into. Must provide a list of sizes equal to the size of the list being sent.\
    \
*   **src** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Source rank from which to recv `object_list`. Source rank is based on global process group (regardless of `group` argument) Will receive from any rank if set to None. Default is `None`.\
    \
*   **group** (_ProcessGroup_ _|_ _None_) – (ProcessGroup, optional): The process group to work on. If None, the default process group will be used. Default is `None`.\
    \
*   **device** (`torch.device`, optional) – If not None, receives on this device. Default is `None`.\
    \
*   **group\_src** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Destination rank on `group`. Invalid to specify both `src` and `group_src`.\
    \
*   **use\_batch** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – If True, use batch p2p operations instead of regular send operations. This avoids initializing 2-rank communicators and uses existing entire group communicators. See batch\_isend\_irecv for usage and assumptions. Default is `False`.\
    \
*   **weights\_only** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – If `True`, objects are deserialized with `torch.load(weights_only=True)`, which restricts deserialization to safe types. If `False`, `pickle` is used, which is insecure with untrusted data. Must match the value passed to [`send_object_list()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.send_object_list "torch.distributed.send_object_list")\
     on the sender. Default is `False`.\
    \
\
Returns:\
\
Sender rank. -1 if rank is not part of the group. If rank is part of the group, `object_list` will contain the sent objects from `src` rank.\
\
Return type:\
\
[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
\
Note\
\
For NCCL-based process groups, internal tensor representations of objects must be moved to the GPU device before communication takes place. In this case, the device used is given by `torch.cuda.current_device()` and it is the user’s responsibility to ensure that this is set so that each rank has an individual GPU, via `torch.cuda.set_device()`.\
\
Warning\
\
Object collectives have a number of serious performance and scalability limitations. See [Object collectives](https://docs.pytorch.org/docs/2.15/distributed.html#object-collectives)\
 for details.\
\
Warning\
\
[`recv_object_list()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.recv_object_list "torch.distributed.recv_object_list")\
 with `weights_only=False` uses `pickle` module implicitly, which is known to be insecure. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling. Only call this function with data you trust.\
\
Warning\
\
Calling [`recv_object_list()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.recv_object_list "torch.distributed.recv_object_list")\
 with GPU tensors is not well supported and inefficient as it incurs GPU -> CPU transfer since tensors would be pickled. Please consider using [`recv()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.recv "torch.distributed.recv")\
 instead.\
\
Example::\
\
\>>> \# Note: Process group initialization omitted on each rank.\
\>>> import torch.distributed as dist\
\>>> \# Assumes backend is not NCCL\
\>>> device \= torch.device("cpu")\
\>>> if dist.get\_rank() \== 0:\
\>>>     \# Assumes world\_size of 2.\
\>>>     objects \= \["foo", 12, {1: 2}\] \# any picklable object\
\>>>     dist.send\_object\_list(objects, dst\=1, device\=device)\
\>>> else:\
\>>>     objects \= \[None, None, None\]\
\>>>     dist.recv\_object\_list(objects, src\=0, device\=device)\
\>>> objects\
\['foo', 12, {1: 2}\]\
\
Copy to clipboard\
\
torch.distributed.batch\_isend\_irecv(_p2p\_op\_list_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L3892)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.batch_isend_irecv "Link to this definition")\
\
Send or Receive a batch of tensors asynchronously and return a list of requests.\
\
Process each of the operations in `p2p_op_list` and return the corresponding requests. NCCL, Gloo, and UCC backend are currently supported.\
\
Parameters:\
\
**p2p\_op\_list** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
_\[_[_P2POp_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.P2POp "torch.distributed.distributed_c10d.P2POp")\
_\]_) –\
\
A list of point-to-point operations(type of each operator is `torch.distributed.P2POp`). All operations in the list are treated as a single batch – the relative ordering of sends vs. receives in the list does not matter and will not cause deadlocks. For example, `[recv_from_1, send_to_1]` is equivalent to `[send_to_1, recv_from_1]`.\
\
The ordering **does** matter for multiple operations between the same pair of ranks in the same direction: if rank 0 calls `[send_to_1(A), send_to_1(B)]`, rank 1 must call `[recv_from_0(A), recv_from_0(B)]` in the same order to ensure the correct tensors are matched.\
\
Returns:\
\
A list of distributed request objects returned by calling the corresponding op in the op\_list.\
\
Return type:\
\
[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[_Work_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.distributed_c10d.Work")\
\]\
\
Examples\
\
\>>> send\_tensor \= torch.arange(2, dtype\=torch.float32) + 2 \* rank\
\>>> recv\_tensor \= torch.randn(2, dtype\=torch.float32)\
\>>> send\_op \= dist.P2POp(dist.isend, send\_tensor, (rank + 1) % world\_size)\
\>>> recv\_op \= dist.P2POp(\
...     dist.irecv, recv\_tensor, (rank \- 1 + world\_size) % world\_size\
... )\
\>>> reqs \= batch\_isend\_irecv(\[send\_op, recv\_op\])\
\>>> for req in reqs:\
\>>>     req.wait()\
\>>> recv\_tensor\
tensor(\[2, 3\])     # Rank 0\
tensor(\[0, 1\])     # Rank 1\
\
Copy to clipboard\
\
Note\
\
Note that when this API is used with the NCCL PG backend, users must set the current GPU device with torch.cuda.set\_device, otherwise it will lead to unexpected hang issues.\
\
In addition, if this API is the first collective call in the `group` passed to `dist.P2POp`, all ranks of the `group` must participate in this API call; otherwise, the behavior is undefined. If this API call is not the first collective call in the `group`, batched P2P operations involving only a subset of ranks of the `group` are allowed.\
\
_class_ torch.distributed.P2POp(_op_, _tensor_, _peer\=None_, _group\=None_, _tag\=0_, _group\_peer\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L1265)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.P2POp "Link to this definition")\
\
A class to build point-to-point operations for `batch_isend_irecv`.\
\
This class builds the type of P2P operation, communication buffer, peer rank, Process Group, and tag. Instances of this class will be passed to `batch_isend_irecv` for point-to-point communications.\
\
Parameters:\
\
*   **op** (_Callable_) – A function to send data to or receive data from a peer process. The type of `op` is either `torch.distributed.isend` or `torch.distributed.irecv`.\
    \
*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Tensor to send or receive.\
    \
*   **peer** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Destination or source rank.\
    \
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.\
    \
*   **tag** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Tag to match send with recv.\
    \
*   **group\_peer** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Destination or source rank.\
    \
\
Return type:\
\
[P2POp](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.P2POp "torch.distributed.P2POp")\
\
Synchronous and asynchronous collective operations[#](https://docs.pytorch.org/docs/2.15/distributed.html#synchronous-and-asynchronous-collective-operations "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
Every collective operation function supports the following two kinds of operations, depending on the setting of the `async_op` flag passed into the collective:\
\
**Synchronous operation** - the default mode, when `async_op` is set to `False`. When the function returns, it is guaranteed that the collective operation is performed. In the case of CUDA operations, it is not guaranteed that the CUDA operation is completed, since CUDA operations are asynchronous. For CPU collectives, any further function calls utilizing the output of the collective call will behave as expected. For CUDA collectives, function calls utilizing the output on the same CUDA stream will behave as expected. Users must take care of synchronization under the scenario of running under different streams. For details on CUDA semantics such as stream synchronization, see [CUDA Semantics](https://pytorch.org/docs/stable/notes/cuda.html)\
. See the below script to see examples of differences in these semantics for CPU and CUDA operations.\
\
**Asynchronous operation** - when `async_op` is set to True. The collective operation function returns a distributed request object. In general, you don’t need to create it manually and it is guaranteed to support two methods:\
\
*   `is_completed()` - in the case of CPU collectives, returns `True` if completed. In the case of CUDA operations, returns `True` if the operation has been successfully enqueued onto a CUDA stream and the output can be utilized on the default stream without further synchronization.\
    \
*   `wait()` - in the case of CPU collectives, will block the process until the operation is completed. In the case of CUDA collectives, will block the currently active CUDA stream until the operation is completed (but will not block the CPU).\
    \
*   `get_future()` - returns `torch._C.Future` object. Supported for NCCL, also supported for most operations on GLOO and MPI, except for peer to peer operations. Note: as we continue adopting Futures and merging APIs, `get_future()` call might become redundant.\
    \
\
**Example**\
\
The following code can serve as a reference regarding semantics for CUDA operations when using distributed collectives. It shows the explicit need to synchronize when using collective outputs on different CUDA streams:\
\
\# Code runs on each rank.\
dist.init\_process\_group("nccl", rank\=rank, world\_size\=2)\
output \= torch.tensor(\[rank\]).cuda(rank)\
s \= torch.cuda.Stream()\
handle \= dist.all\_reduce(output, async\_op\=True)\
\# Wait ensures the operation is enqueued, but not necessarily complete.\
handle.wait()\
\# Using result on non-default stream.\
with torch.cuda.stream(s):\
    s.wait\_stream(torch.cuda.default\_stream())\
    output.add\_(100)\
if rank \== 0:\
    \# if the explicit call to wait\_stream was omitted, the output below will be\
    \# non-deterministically 1 or 101, depending on whether the allreduce overwrote\
    \# the value after the add completed.\
    print(output)\
\
Copy to clipboard\
\
Collective functions[#](https://docs.pytorch.org/docs/2.15/distributed.html#collective-functions "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------\
\
torch.distributed.broadcast(_tensor_, _src\=None_, _group\=None_, _async\_op\=False_, _group\_src\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L3989)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.broadcast "Link to this definition")\
\
Broadcasts the tensor to the whole group.\
\
`tensor` must have the same number of elements in all processes participating in the collective.\
\
Parameters:\
\
*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Data to be sent if `src` is the rank of current process, and tensor to be used to save received data otherwise.\
    \
*   **src** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – Source rank on global process group (regardless of `group` argument).\
    \
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.\
    \
*   **async\_op** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – Whether this op should be an async op\
    \
*   **group\_src** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – Source rank on `group`. Must specify one of `group_src` and `src` but not both.\
    \
\
Returns:\
\
Async work handle, if async\_op is set to True. None, if not async\_op or if not part of the group\
\
Return type:\
\
[_Work_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.distributed_c10d.Work")\
 | None\
\
torch.distributed.broadcast\_object\_list(_object\_list_, _src\=None_, _group\=None_, _device\=None_, _group\_src\=None_, _weights\_only\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L4908)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.broadcast_object_list "Link to this definition")\
\
Broadcasts picklable objects in `object_list` to the whole group.\
\
Similar to [`broadcast()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.broadcast "torch.distributed.broadcast")\
, but Python objects can be passed in. Note that all objects in `object_list` must be picklable in order to be broadcasted.\
\
Parameters:\
\
*   **object\_list** (_List__\[__Any__\]_) – List of input objects to broadcast. Each object must be picklable. Only objects on the `src` rank will be broadcast, but each rank must provide lists of equal sizes.\
    \
*   **src** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – Source rank from which to broadcast `object_list`. Source rank is based on global process group (regardless of `group` argument)\
    \
*   **group** (_ProcessGroup_ _|_ _None_) – (ProcessGroup, optional): The process group to work on. If None, the default process group will be used. Default is `None`.\
    \
*   **device** (`torch.device`, optional) – If not None, the objects are serialized and converted to tensors which are moved to the `device` before broadcasting. Default is `None`.\
    \
*   **group\_src** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – Source rank on `group`. Must not specify one of `group_src` and `src` but not both.\
    \
*   **weights\_only** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – If `True`, objects are serialized with `torch.save` and deserialized with `torch.load(weights_only=True)`, which restricts deserialization to safe types. If `False`, `pickle` is used, which is insecure with untrusted data. All ranks must pass the same value. Default is `False`.\
    \
\
Returns:\
\
`None`. If rank is part of the group, `object_list` will contain the broadcasted objects from `src` rank.\
\
Return type:\
\
None\
\
Note\
\
For NCCL-based process groups, internal tensor representations of objects must be moved to the GPU device before communication takes place. In this case, the device used is given by `torch.cuda.current_device()` and it is the user’s responsibility to ensure that this is set so that each rank has an individual GPU, via `torch.cuda.set_device()`.\
\
Note\
\
Note that this API differs slightly from the [`broadcast()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.broadcast "torch.distributed.broadcast")\
 collective since it does not provide an `async_op` handle and thus will be a blocking call.\
\
Warning\
\
Object collectives have a number of serious performance and scalability limitations. See [Object collectives](https://docs.pytorch.org/docs/2.15/distributed.html#object-collectives)\
 for details.\
\
Warning\
\
[`broadcast_object_list()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.broadcast_object_list "torch.distributed.broadcast_object_list")\
 with `weights_only=False` uses `pickle` module implicitly, which is known to be insecure. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling. Only call this function with data you trust.\
\
Warning\
\
Calling [`broadcast_object_list()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.broadcast_object_list "torch.distributed.broadcast_object_list")\
 with GPU tensors is not well supported and inefficient as it incurs GPU -> CPU transfer since tensors would be pickled. Please consider using [`broadcast()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.broadcast "torch.distributed.broadcast")\
 instead.\
\
Example::\
\
\>>> \# Note: Process group initialization omitted on each rank.\
\>>> import torch.distributed as dist\
\>>> if dist.get\_rank() \== 0:\
\>>>     \# Assumes world\_size of 3.\
\>>>     objects \= \["foo", 12, {1: 2}\] \# any picklable object\
\>>> else:\
\>>>     objects \= \[None, None, None\]\
\>>> \# Assumes backend is not NCCL\
\>>> device \= torch.device("cpu")\
\>>> dist.broadcast\_object\_list(objects, src\=0, device\=device)\
\>>> objects\
\['foo', 12, {1: 2}\]\
\
Copy to clipboard\
\
torch.distributed.all\_reduce(_tensor: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_, _op: \_ReduceOp \= ReduceOp.SUM_, _group: ProcessGroup | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
 \= None_, _\*_, _async\_op: Literal\[True\]_) → [Work](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.Work")\
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L4079)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.all_reduce "Link to this definition")\
\
torch.distributed.all\_reduce(_tensor: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_, _op: \_ReduceOp \= ReduceOp.SUM_, _group: ProcessGroup | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
 \= None_, _async\_op: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 \= False_) → [Work](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.Work")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
\
Reduces the tensor data across all machines in a way that all get the final result.\
\
After the call `tensor` is going to be bitwise identical in all processes.\
\
Complex tensors are supported.\
\
Parameters:\
\
*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Input and output of the collective. The function operates in-place.\
    \
*   **op** (_optional_) – One of the values from `torch.distributed.ReduceOp` enum. Specifies an operation used for element-wise reductions.\
    \
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.\
    \
*   **async\_op** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – Whether this op should be an async op\
    \
\
Returns:\
\
Async work handle, if async\_op is set to True. None, if not async\_op or if not part of the group\
\
Examples\
\
\>>> \# All tensors below are of torch.int64 type.\
\>>> \# We have 2 process groups, 2 ranks.\
\>>> device \= torch.device(f"cuda:{rank}")\
\>>> tensor \= torch.arange(2, dtype\=torch.int64, device\=device) + 1 + 2 \* rank\
\>>> tensor\
tensor(\[1, 2\], device='cuda:0') # Rank 0\
tensor(\[3, 4\], device='cuda:1') # Rank 1\
\>>> dist.all\_reduce(tensor, op\=ReduceOp.SUM)\
\>>> tensor\
tensor(\[4, 6\], device='cuda:0') # Rank 0\
tensor(\[4, 6\], device='cuda:1') # Rank 1\
\
Copy to clipboard\
\
\>>> \# All tensors below are of torch.cfloat type.\
\>>> \# We have 2 process groups, 2 ranks.\
\>>> tensor \= torch.tensor(\
...     \[1 + 1j, 2 + 2j\], dtype\=torch.cfloat, device\=device\
... ) + 2 \* rank \* (1 + 1j)\
\>>> tensor\
tensor(\[1.+1.j, 2.+2.j\], device='cuda:0') # Rank 0\
tensor(\[3.+3.j, 4.+4.j\], device='cuda:1') # Rank 1\
\>>> dist.all\_reduce(tensor, op\=ReduceOp.SUM)\
\>>> tensor\
tensor(\[4.+4.j, 6.+6.j\], device='cuda:0') # Rank 0\
tensor(\[4.+4.j, 6.+6.j\], device='cuda:1') # Rank 1\
\
Copy to clipboard\
\
torch.distributed.all\_reduce\_coalesced(_tensors_, _op=<RedOpType.SUM: 0>_, _group=None_, _async\_op=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L4186)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.all_reduce_coalesced "Link to this definition")\
\
WARNING: at this time individual shape checking is not implemented across nodes.\
\
For example, if the rank 0 node passes \[torch.rand(4), torch.rand(2)\] and the rank 1 node passes \[torch.rand(2), torch.rand(2), torch.rand(2)\], the allreduce operation will proceed without complaint and return erroneous outputs. This lack of shape checking results in significant performance improvements but users of this function should take extra care to ensure that each node passes in tensors whose shapes match across nodes.\
\
Reduces each tensor in tensors (residing on the same device) across all machines in such a way that all get the final result.\
\
After the call each tensor in tensors is going to bitwise identical in all processes.\
\
Complex tensors are supported.\
\
Parameters:\
\
*   **tensors** (_Union__\[__List__\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]__,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]_) – Input and output of the collective. The function operates in-place.\
    \
*   **op** (_Optional__\[_[_ReduceOp_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.ReduceOp "torch.distributed.ReduceOp")\
    _\]_) – One of the values from `torch.distributed.ReduceOp` enum. Specifies an operation used for element-wise reductions.\
    \
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.\
    \
*   **async\_op** (_Optional__\[_[_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _\]_) – Whether this op should be an async op.\
    \
\
Returns:\
\
Async work handle, if async\_op is set to True. None, if not async\_op or if not part of the group.\
\
Return type:\
\
_Future_ | None\
\
torch.distributed.reduce(_tensor_, _dst=None_, _op=<RedOpType.SUM: 0>_, _group=None_, _async\_op=False_, _group\_dst=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L4271)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.reduce "Link to this definition")\
\
Reduces the tensor data across all machines.\
\
Only the process with rank `dst` is going to receive the final result.\
\
Parameters:\
\
*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Input and output of the collective. The function operates in-place.\
    \
*   **dst** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – Destination rank on global process group (regardless of `group` argument)\
    \
*   **op** (_optional_) – One of the values from `torch.distributed.ReduceOp` enum. Specifies an operation used for element-wise reductions.\
    \
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.\
    \
*   **async\_op** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – Whether this op should be an async op\
    \
*   **group\_dst** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – Destination rank on `group`. Must specify one of `group_dst` and `dst` but not both.\
    \
\
Returns:\
\
Async work handle, if async\_op is set to True. None, if not async\_op or if not part of the group\
\
Return type:\
\
[_Work_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.distributed_c10d.Work")\
 | None\
\
torch.distributed.all\_gather(_tensor\_list: [list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]_, _tensor: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_, _group: ProcessGroup | C10DBackend | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
 \= None_, _\*_, _async\_op: Literal\[True\]_) → [Work](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.Work")\
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L5212)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.all_gather "Link to this definition")\
\
torch.distributed.all\_gather(_tensor\_list: [list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]_, _tensor: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_, _group: ProcessGroup | C10DBackend | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
 \= None_, _async\_op: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 \= False_) → [Work](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.Work")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
\
Gathers tensors from the whole group in a list.\
\
Complex and uneven sized tensors are supported.\
\
Parameters:\
\
*   **tensor\_list** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
    _\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]_) – Output list. It should contain correctly-sized tensors to be used for output of the collective. Uneven sized tensors are supported.\
    \
*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Tensor to be broadcast from current process.\
    \
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.\
    \
*   **async\_op** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – Whether this op should be an async op\
    \
\
Returns:\
\
Async work handle, if async\_op is set to True. None, if not async\_op or if not part of the group\
\
Examples\
\
\>>> \# All tensors below are of torch.int64 dtype.\
\>>> \# We have 2 process groups, 2 ranks.\
\>>> device \= torch.device(f"cuda:{rank}")\
\>>> tensor\_list \= \[\
...     torch.zeros(2, dtype\=torch.int64, device\=device) for \_ in range(2)\
... \]\
\>>> tensor\_list\
\[tensor(\[0, 0\], device='cuda:0'), tensor(\[0, 0\], device='cuda:0')\] # Rank 0\
\[tensor(\[0, 0\], device='cuda:1'), tensor(\[0, 0\], device='cuda:1')\] # Rank 1\
\>>> tensor \= torch.arange(2, dtype\=torch.int64, device\=device) + 1 + 2 \* rank\
\>>> tensor\
tensor(\[1, 2\], device='cuda:0') # Rank 0\
tensor(\[3, 4\], device='cuda:1') # Rank 1\
\>>> dist.all\_gather(tensor\_list, tensor)\
\>>> tensor\_list\
\[tensor(\[1, 2\], device='cuda:0'), tensor(\[3, 4\], device='cuda:0')\] # Rank 0\
\[tensor(\[1, 2\], device='cuda:1'), tensor(\[3, 4\], device='cuda:1')\] # Rank 1\
\
Copy to clipboard\
\
\>>> \# All tensors below are of torch.cfloat dtype.\
\>>> \# We have 2 process groups, 2 ranks.\
\>>> tensor\_list \= \[\
...     torch.zeros(2, dtype\=torch.cfloat, device\=device) for \_ in range(2)\
... \]\
\>>> tensor\_list\
\[tensor(\[0.+0.j, 0.+0.j\], device='cuda:0'), tensor(\[0.+0.j, 0.+0.j\], device='cuda:0')\] # Rank 0\
\[tensor(\[0.+0.j, 0.+0.j\], device='cuda:1'), tensor(\[0.+0.j, 0.+0.j\], device='cuda:1')\] # Rank 1\
\>>> tensor \= torch.tensor(\
...     \[1 + 1j, 2 + 2j\], dtype\=torch.cfloat, device\=device\
... ) + 2 \* rank \* (1 + 1j)\
\>>> tensor\
tensor(\[1.+1.j, 2.+2.j\], device='cuda:0') # Rank 0\
tensor(\[3.+3.j, 4.+4.j\], device='cuda:1') # Rank 1\
\>>> dist.all\_gather(tensor\_list, tensor)\
\>>> tensor\_list\
\[tensor(\[1.+1.j, 2.+2.j\], device='cuda:0'), tensor(\[3.+3.j, 4.+4.j\], device='cuda:0')\] # Rank 0\
\[tensor(\[1.+1.j, 2.+2.j\], device='cuda:1'), tensor(\[3.+3.j, 4.+4.j\], device='cuda:1')\] # Rank 1\
\
Copy to clipboard\
\
torch.distributed.all\_gather\_single(_output\_tensor_, _input\_tensor_, _group\=None_, _async\_op\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L5320)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.all_gather_single "Link to this definition")\
\
Gather tensors from all ranks and put them in a single output tensor.\
\
This function requires all tensors to be the same size on each process.\
\
Parameters:\
\
*   **output\_tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Output tensor to accommodate tensor elements from all ranks. It must be correctly sized to have one of the following forms: (i) a concatenation of all the input tensors along the primary dimension; for definition of “concatenation”, see `torch.cat()`; (ii) a stack of all the input tensors along the primary dimension; for definition of “stack”, see `torch.stack()`. Examples below may better explain the supported output forms.\
    \
*   **input\_tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Tensor to be gathered from current rank. Different from the `all_gather` API, the input tensors in this API must have the same size across all ranks.\
    \
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.\
    \
*   **async\_op** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – Whether this op should be an async op\
    \
\
Returns:\
\
Async work handle, if async\_op is set to True. None, if not async\_op or if not part of the group\
\
Return type:\
\
[_Work_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.distributed_c10d.Work")\
 | None\
\
Examples\
\
\>>> \# All tensors below are of torch.int64 dtype and on CUDA devices.\
\>>> \# We have two ranks.\
\>>> device \= torch.device(f"cuda:{rank}")\
\>>> tensor\_in \= torch.arange(2, dtype\=torch.int64, device\=device) + 1 + 2 \* rank\
\>>> tensor\_in\
tensor(\[1, 2\], device='cuda:0') # Rank 0\
tensor(\[3, 4\], device='cuda:1') # Rank 1\
\>>> \# Output in concatenation form\
\>>> tensor\_out \= torch.zeros(world\_size \* 2, dtype\=torch.int64, device\=device)\
\>>> dist.all\_gather\_single(tensor\_out, tensor\_in)\
\>>> tensor\_out\
tensor(\[1, 2, 3, 4\], device='cuda:0') # Rank 0\
tensor(\[1, 2, 3, 4\], device='cuda:1') # Rank 1\
\>>> \# Output in stack form\
\>>> tensor\_out2 \= torch.zeros(world\_size, 2, dtype\=torch.int64, device\=device)\
\>>> dist.all\_gather\_single(tensor\_out2, tensor\_in)\
\>>> tensor\_out2\
tensor(\[\[1, 2\],\
        \[3, 4\]\], device='cuda:0') # Rank 0\
tensor(\[\[1, 2\],\
        \[3, 4\]\], device='cuda:1') # Rank 1\
\
Copy to clipboard\
\
torch.distributed.all\_gather\_object(_object\_list_, _obj_, _group\=None_, _weights\_only\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L4389)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.all_gather_object "Link to this definition")\
\
Gathers picklable objects from the whole group into a list.\
\
Similar to [`all_gather()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.all_gather "torch.distributed.all_gather")\
, but Python objects can be passed in. Note that the object must be picklable in order to be gathered.\
\
Parameters:\
\
*   **object\_list** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
    _\[__Any__\]_) – Output list. It should be correctly sized as the size of the group for this collective and will contain the output.\
    \
*   **obj** (_Any_) – Pickable Python object to be broadcast from current process.\
    \
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used. Default is `None`.\
    \
*   **weights\_only** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – If `True`, objects are serialized with `torch.save` and deserialized with `torch.load(weights_only=True)`, which restricts deserialization to safe types. If `False`, `pickle` is used, which is insecure with untrusted data. All ranks must pass the same value. Default is `False`.\
    \
\
Returns:\
\
None. If the calling rank is part of this group, the output of the collective will be populated into the input `object_list`. If the calling rank is not part of the group, the passed in `object_list` will be unmodified.\
\
Return type:\
\
None\
\
Note\
\
Note that this API differs slightly from the [`all_gather()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.all_gather "torch.distributed.all_gather")\
 collective since it does not provide an `async_op` handle and thus will be a blocking call.\
\
Note\
\
For NCCL-based processed groups, internal tensor representations of objects must be moved to the GPU device before communication takes place. In this case, the device used is given by `torch.cuda.current_device()` and it is the user’s responsibility to ensure that this is set so that each rank has an individual GPU, via `torch.cuda.set_device()`.\
\
Warning\
\
Object collectives have a number of serious performance and scalability limitations. See [Object collectives](https://docs.pytorch.org/docs/2.15/distributed.html#object-collectives)\
 for details.\
\
Warning\
\
[`all_gather_object()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.all_gather_object "torch.distributed.all_gather_object")\
 with `weights_only=False` uses `pickle` module implicitly, which is known to be insecure. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling. Only call this function with data you trust.\
\
Warning\
\
Calling [`all_gather_object()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.all_gather_object "torch.distributed.all_gather_object")\
 with GPU tensors is not well supported and inefficient as it incurs GPU -> CPU transfer since tensors would be pickled. Please consider using [`all_gather()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.all_gather "torch.distributed.all_gather")\
 instead.\
\
Example::\
\
\>>> \# Note: Process group initialization omitted on each rank.\
\>>> import torch.distributed as dist\
\>>> \# Assumes world\_size of 3.\
\>>> gather\_objects \= \["foo", 12, {1: 2}\] \# any picklable object\
\>>> output \= \[None for \_ in gather\_objects\]\
\>>> dist.all\_gather\_object(output, gather\_objects\[dist.get\_rank()\])\
\>>> output\
\['foo', 12, {1: 2}\]\
\
Copy to clipboard\
\
torch.distributed.all\_gather\_coalesced(_output\_tensor\_lists_, _input\_tensor\_list_, _group\=None_, _async\_op\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L5487)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.all_gather_coalesced "Link to this definition")\
\
Gathers input tensors from the whole group in a list in a coalesced manner.\
\
Complex tensors are supported.\
\
Parameters:\
\
*   **output\_tensor\_lists** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
    _\[_[_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
    _\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]__\]_) – Output list. It should contain correctly-sized tensors to be used for output of the collective.\
    \
*   **input\_tensor\_list** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
    _\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]_) – Tensors to be broadcast from current process. At least one tensor has to be non empty.\
    \
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.\
    \
*   **async\_op** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – Whether this op should be an async op.\
    \
\
Returns:\
\
Async work handle, if async\_op is set to True. None, if not async\_op or if not part of the group\
\
Return type:\
\
_Future_ | None\
\
Example:\
\
\# we have 2 process groups, 2 ranks.\
\# rank 0 passes:\
input\_tensor\_list \= \[\[\[1, 1\], \[1, 1\]\], \[2\], \[3, 3\]\]\
output\_tensor\_lists \= \[\
    \[\[\[\-1, \-1\], \[\-1, \-1\]\], \[\-1\], \[\-1, \-1\]\],\
    \[\[\[\-1, \-1\], \[\-1, \-1\]\], \[\-1\], \[\-1, \-1\]\],\
\]\
\# rank 1 passes:\
input\_tensor\_list \= \[\[\[3, 3\], \[3, 3\]\], \[5\], \[1, 1\]\]\
output\_tensor\_lists \= \[\
    \[\[\[\-1, \-1\], \[\-1, \-1\]\], \[\-1\], \[\-1, \-1\]\],\
    \[\[\[\-1, \-1\], \[\-1, \-1\]\], \[\-1\], \[\-1, \-1\]\],\
\]\
\# both rank 0 and 1 get:\
output\_tensor\_lists \= \[\
    \[\[\[1, 1\], \[1, 1\]\], \[2\], \[3, 3\]\],\
    \[\[\[3, 3\], \[3, 3\]\], \[5\], \[1, 1\]\],\
\]\
\
Copy to clipboard\
\
WARNING: at this time individual shape checking is not implemented across nodes. For example, if the rank 0 node passes \[torch.rand(4), torch.rand(2)\] and the rank 1 node passes \[torch.rand(2), torch.rand(2), torch.rand(2)\], the all\_gather\_coalesced operation will proceed without complaint and return erroneous outputs. This lack of shape checking results in significant performance improvements but users of this function should take extra care to ensure that each node passes in tensors whose shapes match across nodes.\
\
torch.distributed.gather(_tensor_, _gather\_list\=None_, _dst\=None_, _group\=None_, _async\_op\=False_, _group\_dst\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L5613)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.gather "Link to this definition")\
\
Gathers a list of tensors in a single process.\
\
This function requires all tensors to be the same size on each process.\
\
Parameters:\
\
*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Input tensor.\
    \
*   **gather\_list** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
    _\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]__,_ _optional_) – List of appropriately, same-sized tensors to use for gathered data (default is None, must be specified on the destination rank)\
    \
*   **dst** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Destination rank on global process group (regardless of `group` argument). (If both `dst` and `group_dst` are None, default is global rank 0)\
    \
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.\
    \
*   **async\_op** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – Whether this op should be an async op\
    \
*   **group\_dst** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Destination rank on `group`. Invalid to specify both `dst` and `group_dst`\
    \
\
Returns:\
\
Async work handle, if async\_op is set to True. None, if not async\_op or if not part of the group\
\
Return type:\
\
[_Work_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.distributed_c10d.Work")\
 | None\
\
Note\
\
Note that all Tensors in gather\_list must have the same size.\
\
Example::\
\
\>>> \# We have 2 process groups, 2 ranks.\
\>>> tensor\_size \= 2\
\>>> device \= torch.device(f'cuda:{rank}')\
\>>> tensor \= torch.ones(tensor\_size, device\=device) + rank\
\>>> if dist.get\_rank() \== 0:\
\>>>     gather\_list \= \[torch.zeros\_like(tensor, device\=device) for i in range(2)\]\
\>>> else:\
\>>>     gather\_list \= None\
\>>> dist.gather(tensor, gather\_list, dst\=0)\
\>>> \# Rank 0 gets gathered data.\
\>>> gather\_list\
\[tensor(\[1., 1.\], device='cuda:0'), tensor(\[2., 2.\], device='cuda:0')\] # Rank 0\
None                                                                   # Rank 1\
\
Copy to clipboard\
\
torch.distributed.gather\_single(_tensor_, _gather\_tensor\=None_, _dst\=None_, _group\=None_, _async\_op\=False_, _group\_dst\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L5718)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.gather_single "Link to this definition")\
\
Gather the input tensor from all ranks into a single output tensor on `dst`.\
\
This is the single-output-tensor analog of [`gather()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.gather "torch.distributed.gather")\
: instead of filling a Python list of per-rank tensors on the destination rank, each rank’s contribution is written directly into a single, correctly-sized `gather_tensor`. Backends that support a native gather-into-tensor path (e.g. NCCL >= 2.28.3 via `ncclGather`) avoid the extra per-rank copy that [`gather()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.gather "torch.distributed.gather")\
 incurs.\
\
This function requires `tensor` to be the same size on each process.\
\
Parameters:\
\
*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Input tensor to be gathered from the current rank.\
    \
*   **gather\_tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _,_ _optional_) – Output tensor to accommodate the gathered contributions from all ranks. It must be contiguous and sized to hold `world_size` copies of `tensor`; only its total number of elements is validated, so either a flat concatenation (`world_size * tensor.numel()`) or a stack (`[world_size, *tensor.shape]`) works, as both share the same contiguous layout. A non-contiguous output (e.g. a strided stacked view) raises a contiguity error rather than a shape error. Only required (and only used) on the destination rank.\
    \
*   **dst** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Destination rank on global process group (regardless of `group` argument). (If both `dst` and `group_dst` are None, default is global rank 0)\
    \
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.\
    \
*   **async\_op** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – Whether this op should be an async op\
    \
*   **group\_dst** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Destination rank on `group`. Invalid to specify both `dst` and `group_dst`\
    \
\
Returns:\
\
Async work handle, if async\_op is set to True. None, if not async\_op or if not part of the group\
\
Example::\
\
\>>> \# We have 2 process groups, 2 ranks.\
\>>> device \= torch.device(f"cuda:{rank}")\
\>>> tensor \= torch.arange(2, dtype\=torch.int64, device\=device) + 1 + 2 \* rank\
\>>> if dist.get\_rank() \== 0:\
\>>>     gather\_tensor \= torch.zeros(2 \* 2, dtype\=torch.int64, device\=device)\
\>>> else:\
\>>>     gather\_tensor \= None\
\>>> dist.gather\_single(tensor, gather\_tensor, dst\=0)\
\>>> gather\_tensor\
tensor(\[1, 2, 3, 4\], device='cuda:0')  # Rank 0\
None                                    # Rank 1\
\
Copy to clipboard\
\
torch.distributed.gather\_object(_obj_, _object\_gather\_list\=None_, _dst\=None_, _group\=None_, _group\_dst\=None_, _weights\_only\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L4490)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.gather_object "Link to this definition")\
\
Gathers picklable objects from the whole group in a single process.\
\
Similar to [`gather()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.gather "torch.distributed.gather")\
, but Python objects can be passed in. Note that the object must be picklable in order to be gathered.\
\
Parameters:\
\
*   **obj** (_Any_) – Input object. Must be picklable.\
    \
*   **object\_gather\_list** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
    _\[__Any__\]_) – Output list. On the `dst` rank, it should be correctly sized as the size of the group for this collective and will contain the output. Must be `None` on non-dst ranks. (default is `None`)\
    \
*   **dst** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Destination rank on global process group (regardless of `group` argument). (If both `dst` and `group_dst` are None, default is global rank 0)\
    \
*   **group** (_ProcessGroup_ _|_ _None_) – (ProcessGroup, optional): The process group to work on. If None, the default process group will be used. Default is `None`.\
    \
*   **group\_dst** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Destination rank on `group`. Invalid to specify both `dst` and `group_dst`\
    \
*   **weights\_only** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – If `True`, objects are serialized with `torch.save` and deserialized with `torch.load(weights_only=True)`, which restricts deserialization to safe types. If `False`, `pickle` is used, which is insecure with untrusted data. All ranks must pass the same value. Default is `False`.\
    \
\
Returns:\
\
None. On the `dst` rank, `object_gather_list` will contain the output of the collective.\
\
Return type:\
\
None\
\
Note\
\
Note that this API differs slightly from the gather collective since it does not provide an async\_op handle and thus will be a blocking call.\
\
Note\
\
For NCCL-based processed groups, internal tensor representations of objects must be moved to the GPU device before communication takes place. In this case, the device used is given by `torch.cuda.current_device()` and it is the user’s responsibility to ensure that this is set so that each rank has an individual GPU, via `torch.cuda.set_device()`.\
\
Warning\
\
Object collectives have a number of serious performance and scalability limitations. See [Object collectives](https://docs.pytorch.org/docs/2.15/distributed.html#object-collectives)\
 for details.\
\
Warning\
\
[`gather_object()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.gather_object "torch.distributed.gather_object")\
 with `weights_only=False` uses `pickle` module implicitly, which is known to be insecure. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling. Only call this function with data you trust.\
\
Warning\
\
Calling [`gather_object()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.gather_object "torch.distributed.gather_object")\
 with GPU tensors is not well supported and inefficient as it incurs GPU -> CPU transfer since tensors would be pickled. Please consider using [`gather()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.gather "torch.distributed.gather")\
 instead.\
\
Example::\
\
\>>> \# Note: Process group initialization omitted on each rank.\
\>>> import torch.distributed as dist\
\>>> \# Assumes world\_size of 3.\
\>>> gather\_objects \= \["foo", 12, {1: 2}\] \# any picklable object\
\>>> output \= \[None for \_ in gather\_objects\]\
\>>> dist.gather\_object(\
...     gather\_objects\[dist.get\_rank()\],\
...     output if dist.get\_rank() \== 0 else None,\
...     dst\=0\
... )\
\>>> \# On rank 0\
\>>> output\
\['foo', 12, {1: 2}\]\
\
Copy to clipboard\
\
torch.distributed.scatter(_tensor_, _scatter\_list\=None_, _src\=None_, _group\=None_, _async\_op\=False_, _group\_src\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L5845)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.scatter "Link to this definition")\
\
Scatters a list of tensors to all processes in a group.\
\
Each process will receive exactly one tensor and store its data in the `tensor` argument.\
\
Complex tensors are supported.\
\
Parameters:\
\
*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Output tensor.\
    \
*   **scatter\_list** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
    _\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]_) – List of tensors to scatter (default is None, must be specified on the source rank)\
    \
*   **src** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – Source rank on global process group (regardless of `group` argument). (If both `src` and `group_src` are None, default is global rank 0)\
    \
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.\
    \
*   **async\_op** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – Whether this op should be an async op\
    \
*   **group\_src** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Source rank on `group`. Invalid to specify both `src` and `group_src`\
    \
\
Returns:\
\
Async work handle, if async\_op is set to True. None, if not async\_op or if not part of the group\
\
Return type:\
\
[_Work_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.distributed_c10d.Work")\
 | None\
\
Note\
\
Note that all Tensors in scatter\_list must have the same size.\
\
Example::\
\
\>>> \# Note: Process group initialization omitted on each rank.\
\>>> import torch.distributed as dist\
\>>> tensor\_size \= 2\
\>>> device \= torch.device(f'cuda:{rank}')\
\>>> output\_tensor \= torch.zeros(tensor\_size, device\=device)\
\>>> if dist.get\_rank() \== 0:\
\>>>     \# Assumes world\_size of 2.\
\>>>     \# Only tensors, all of which must be the same size.\
\>>>     t\_ones \= torch.ones(tensor\_size, device\=device)\
\>>>     t\_fives \= torch.ones(tensor\_size, device\=device) \* 5\
\>>>     scatter\_list \= \[t\_ones, t\_fives\]\
\>>> else:\
\>>>     scatter\_list \= None\
\>>> dist.scatter(output\_tensor, scatter\_list, src\=0)\
\>>> \# Rank i gets scatter\_list\[i\].\
\>>> output\_tensor\
tensor(\[1., 1.\], device='cuda:0') # Rank 0\
tensor(\[5., 5.\], device='cuda:1') # Rank 1\
\
Copy to clipboard\
\
torch.distributed.scatter\_object\_list(_scatter\_object\_output\_list_, _scatter\_object\_input\_list\=None_, _src\=None_, _group\=None_, _group\_src\=None_, _weights\_only\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L5051)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.scatter_object_list "Link to this definition")\
\
Scatters picklable objects in `scatter_object_input_list` to the whole group.\
\
Similar to [`scatter()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.scatter "torch.distributed.scatter")\
, but Python objects can be passed in. On each rank, the scattered object will be stored as the first element of `scatter_object_output_list`. Note that all objects in `scatter_object_input_list` must be picklable in order to be scattered.\
\
Parameters:\
\
*   **scatter\_object\_output\_list** (_List__\[__Any__\]_) – Non-empty list whose first element will store the object scattered to this rank.\
    \
*   **scatter\_object\_input\_list** (_List__\[__Any__\]__,_ _optional_) – List of input objects to scatter. Each object must be picklable. Only objects on the `src` rank will be scattered, and the argument can be `None` for non-src ranks.\
    \
*   **src** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – Source rank from which to scatter `scatter_object_input_list`. Source rank is based on global process group (regardless of `group` argument). (If both `src` and `group_src` are None, default is global rank 0)\
    \
*   **group** (_ProcessGroup_ _|_ _None_) – (ProcessGroup, optional): The process group to work on. If None, the default process group will be used. Default is `None`.\
    \
*   **group\_src** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – Source rank on `group`. Invalid to specify both `src` and `group_src`\
    \
*   **weights\_only** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – If `True`, objects are serialized with `torch.save` and deserialized with `torch.load(weights_only=True)`, which restricts deserialization to safe types. If `False`, `pickle` is used, which is insecure with untrusted data. All ranks must pass the same value. Default is `False`.\
    \
\
Returns:\
\
`None`. If rank is part of the group, `scatter_object_output_list` will have its first element set to the scattered object for this rank.\
\
Return type:\
\
None\
\
Note\
\
Note that this API differs slightly from the scatter collective since it does not provide an `async_op` handle and thus will be a blocking call.\
\
Warning\
\
Object collectives have a number of serious performance and scalability limitations. See [Object collectives](https://docs.pytorch.org/docs/2.15/distributed.html#object-collectives)\
 for details.\
\
Warning\
\
[`scatter_object_list()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.scatter_object_list "torch.distributed.scatter_object_list")\
 with `weights_only=False` uses `pickle` module implicitly, which is known to be insecure. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling. Only call this function with data you trust.\
\
Warning\
\
Calling [`scatter_object_list()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.scatter_object_list "torch.distributed.scatter_object_list")\
 with GPU tensors is not well supported and inefficient as it incurs GPU -> CPU transfer since tensors would be pickled. Please consider using [`scatter()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.scatter "torch.distributed.scatter")\
 instead.\
\
Example::\
\
\>>> \# Note: Process group initialization omitted on each rank.\
\>>> import torch.distributed as dist\
\>>> if dist.get\_rank() \== 0:\
\>>>     \# Assumes world\_size of 3.\
\>>>     objects \= \["foo", 12, {1: 2}\] \# any picklable object\
\>>> else:\
\>>>     \# Can be any list on non-src ranks, elements are not used.\
\>>>     objects \= \[None, None, None\]\
\>>> output\_list \= \[None\]\
\>>> dist.scatter\_object\_list(output\_list, objects, src\=0)\
\>>> \# Rank i gets objects\[i\]. For example, on rank 2:\
\>>> output\_list\
\[{1: 2}\]\
\
Copy to clipboard\
\
torch.distributed.reduce\_scatter(_output: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_, _input\_list: [list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]_, _op: \_ReduceOp \= ReduceOp.SUM_, _group: ProcessGroup | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
 \= None_, _\*_, _async\_op: Literal\[True\]_) → [Work](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.Work")\
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L5985)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.reduce_scatter "Link to this definition")\
\
torch.distributed.reduce\_scatter(_output: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_, _input\_list: [list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]_, _op: \_ReduceOp \= ReduceOp.SUM_, _group: ProcessGroup | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
 \= None_, _async\_op: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 \= False_) → [Work](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.Work")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
\
Reduces, then scatters a list of tensors to all processes in a group.\
\
Parameters:\
\
*   **output** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Output tensor.\
    \
*   **input\_list** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
    _\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]_) – List of tensors to reduce and scatter.\
    \
*   **op** (_optional_) – One of the values from `torch.distributed.ReduceOp` enum. Specifies an operation used for element-wise reductions.\
    \
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.\
    \
*   **async\_op** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – Whether this op should be an async op.\
    \
\
Returns:\
\
Async work handle, if async\_op is set to True. None, if not async\_op or if not part of the group.\
\
torch.distributed.reduce\_scatter\_single(_output: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_, _input: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_, _op: \_ReduceOp \= ReduceOp.SUM_, _group: ProcessGroup | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
 \= None_, _\*_, _async\_op: Literal\[True\]_) → [Work](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.Work")\
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L6068)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.reduce_scatter_single "Link to this definition")\
\
torch.distributed.reduce\_scatter\_single(_output: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_, _input: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_, _op: \_ReduceOp \= ReduceOp.SUM_, _group: ProcessGroup | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
 \= None_, _async\_op: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 \= False_) → [Work](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.Work")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
\
Reduces, then scatters a tensor to all ranks in a group.\
\
Parameters:\
\
*   **output** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Output tensor. It should have the same size across all ranks.\
    \
*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Input tensor to be reduced and scattered. Its size should be output tensor size times the world size. The input tensor can have one of the following shapes: (i) a concatenation of the output tensors along the primary dimension, or (ii) a stack of the output tensors along the primary dimension. For definition of “concatenation”, see `torch.cat()`. For definition of “stack”, see `torch.stack()`.\
    \
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.\
    \
*   **async\_op** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – Whether this op should be an async op.\
    \
\
Returns:\
\
Async work handle, if async\_op is set to True. None, if not async\_op or if not part of the group.\
\
Examples\
\
\>>> \# All tensors below are of torch.int64 dtype and on CUDA devices.\
\>>> \# We have two ranks.\
\>>> device \= torch.device(f"cuda:{rank}")\
\>>> tensor\_out \= torch.zeros(2, dtype\=torch.int64, device\=device)\
\>>> \# Input in concatenation form\
\>>> tensor\_in \= torch.arange(world\_size \* 2, dtype\=torch.int64, device\=device)\
\>>> tensor\_in\
tensor(\[0, 1, 2, 3\], device='cuda:0') # Rank 0\
tensor(\[0, 1, 2, 3\], device='cuda:1') # Rank 1\
\>>> dist.reduce\_scatter\_single(tensor\_out, tensor\_in)\
\>>> tensor\_out\
tensor(\[0, 2\], device='cuda:0') # Rank 0\
tensor(\[4, 6\], device='cuda:1') # Rank 1\
\>>> \# Input in stack form\
\>>> tensor\_in \= torch.reshape(tensor\_in, (world\_size, 2))\
\>>> tensor\_in\
tensor(\[\[0, 1\],\
        \[2, 3\]\], device='cuda:0') # Rank 0\
tensor(\[\[0, 1\],\
        \[2, 3\]\], device='cuda:1') # Rank 1\
\>>> dist.reduce\_scatter\_single(tensor\_out, tensor\_in)\
\>>> tensor\_out\
tensor(\[0, 2\], device='cuda:0') # Rank 0\
tensor(\[4, 6\], device='cuda:1') # Rank 1\
\
Copy to clipboard\
\
torch.distributed.all\_to\_all\_single(_output_, _input_, _output\_split\_sizes\=None_, _input\_split\_sizes\=None_, _group\=None_, _async\_op\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L6229)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.all_to_all_single "Link to this definition")\
\
Split input tensor and then scatter the split list to all processes in a group.\
\
Later the received tensors are concatenated from all the processes in the group and returned as a single output tensor.\
\
Complex tensors are supported.\
\
Parameters:\
\
*   **output** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Gathered concatenated output tensor.\
    \
*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Input tensor to scatter.\
    \
*   **output\_split\_sizes** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_ _|_ _None_) – (list\[Int\], optional): Output split sizes for dim 0 if specified None or empty, dim 0 of `output` tensor must divide equally by `world_size`.\
    \
*   **input\_split\_sizes** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_ _|_ _None_) – (list\[Int\], optional): Input split sizes for dim 0 if specified None or empty, dim 0 of `input` tensor must divide equally by `world_size`.\
    \
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.\
    \
*   **async\_op** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – Whether this op should be an async op.\
    \
\
Returns:\
\
Async work handle, if async\_op is set to True. None, if not async\_op or if not part of the group.\
\
Return type:\
\
[_Work_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.distributed_c10d.Work")\
 | None\
\
Warning\
\
all\_to\_all\_single is experimental and subject to change.\
\
Examples\
\
\>>> input \= torch.arange(4) + rank \* 4\
\>>> input\
tensor(\[0, 1, 2, 3\])     # Rank 0\
tensor(\[4, 5, 6, 7\])     # Rank 1\
tensor(\[8, 9, 10, 11\])   # Rank 2\
tensor(\[12, 13, 14, 15\]) # Rank 3\
\>>> output \= torch.empty(\[4\], dtype\=torch.int64)\
\>>> dist.all\_to\_all\_single(output, input)\
\>>> output\
tensor(\[0, 4, 8, 12\])    # Rank 0\
tensor(\[1, 5, 9, 13\])    # Rank 1\
tensor(\[2, 6, 10, 14\])   # Rank 2\
tensor(\[3, 7, 11, 15\])   # Rank 3\
\
Copy to clipboard\
\
\>>> \# Essentially, it is similar to following operation:\
\>>> scatter\_list \= list(input.chunk(world\_size))\
\>>> gather\_list \= list(output.chunk(world\_size))\
\>>> for i in range(world\_size):\
\>>>     dist.scatter(gather\_list\[i\], scatter\_list if i \== rank else \[\], src \= i)\
\
Copy to clipboard\
\
\>>> \# Another example with uneven split\
\>>> input\
tensor(\[0, 1, 2, 3, 4, 5\])                                       # Rank 0\
tensor(\[10, 11, 12, 13, 14, 15, 16, 17, 18\])                     # Rank 1\
tensor(\[20, 21, 22, 23, 24\])                                     # Rank 2\
tensor(\[30, 31, 32, 33, 34, 35, 36\])                             # Rank 3\
\>>> input\_splits\
\[2, 2, 1, 1\]                                                     # Rank 0\
\[3, 2, 2, 2\]                                                     # Rank 1\
\[2, 1, 1, 1\]                                                     # Rank 2\
\[2, 2, 2, 1\]                                                     # Rank 3\
\>>> output\_splits\
\[2, 3, 2, 2\]                                                     # Rank 0\
\[2, 2, 1, 2\]                                                     # Rank 1\
\[1, 2, 1, 2\]                                                     # Rank 2\
\[1, 2, 1, 1\]                                                     # Rank 3\
\>>> output \= ...\
\>>> dist.all\_to\_all\_single(output, input, output\_splits, input\_splits)\
\>>> output\
tensor(\[ 0,  1, 10, 11, 12, 20, 21, 30, 31\])                     # Rank 0\
tensor(\[ 2,  3, 13, 14, 22, 32, 33\])                             # Rank 1\
tensor(\[ 4, 15, 16, 23, 34, 35\])                                 # Rank 2\
tensor(\[ 5, 17, 18, 24, 36\])                                     # Rank 3\
\
Copy to clipboard\
\
\>>> \# Another example with tensors of torch.cfloat type.\
\>>> input \= torch.tensor(\
...     \[1 + 1j, 2 + 2j, 3 + 3j, 4 + 4j\], dtype\=torch.cfloat\
... ) + 4 \* rank \* (1 + 1j)\
\>>> input\
tensor(\[1+1j, 2+2j, 3+3j, 4+4j\])                                # Rank 0\
tensor(\[5+5j, 6+6j, 7+7j, 8+8j\])                                # Rank 1\
tensor(\[9+9j, 10+10j, 11+11j, 12+12j\])                          # Rank 2\
tensor(\[13+13j, 14+14j, 15+15j, 16+16j\])                        # Rank 3\
\>>> output \= torch.empty(\[4\], dtype\=torch.int64)\
\>>> dist.all\_to\_all\_single(output, input)\
\>>> output\
tensor(\[1+1j, 5+5j, 9+9j, 13+13j\])                              # Rank 0\
tensor(\[2+2j, 6+6j, 10+10j, 14+14j\])                            # Rank 1\
tensor(\[3+3j, 7+7j, 11+11j, 15+15j\])                            # Rank 2\
tensor(\[4+4j, 8+8j, 12+12j, 16+16j\])                            # Rank 3\
\
Copy to clipboard\
\
torch.distributed.all\_to\_all(_output\_tensor\_list_, _input\_tensor\_list_, _group\=None_, _async\_op\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L6379)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.all_to_all "Link to this definition")\
\
Scatters list of input tensors to all processes in a group and return gathered list of tensors in output list.\
\
Complex tensors are supported.\
\
Parameters:\
\
*   **output\_tensor\_list** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
    _\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]_) – List of tensors to be gathered one per rank.\
    \
*   **input\_tensor\_list** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
    _\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]_) – List of tensors to scatter one per rank.\
    \
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.\
    \
*   **async\_op** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – Whether this op should be an async op.\
    \
\
Returns:\
\
Async work handle, if async\_op is set to True. None, if not async\_op or if not part of the group.\
\
Return type:\
\
[_Work_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.distributed_c10d.Work")\
 | None\
\
Warning\
\
all\_to\_all is experimental and subject to change.\
\
Examples\
\
\>>> input \= torch.arange(4) + rank \* 4\
\>>> input \= list(input.chunk(4))\
\>>> input\
\[tensor(\[0\]), tensor(\[1\]), tensor(\[2\]), tensor(\[3\])\]     # Rank 0\
\[tensor(\[4\]), tensor(\[5\]), tensor(\[6\]), tensor(\[7\])\]     # Rank 1\
\[tensor(\[8\]), tensor(\[9\]), tensor(\[10\]), tensor(\[11\])\]   # Rank 2\
\[tensor(\[12\]), tensor(\[13\]), tensor(\[14\]), tensor(\[15\])\] # Rank 3\
\>>> output \= list(torch.empty(\[4\], dtype\=torch.int64).chunk(4))\
\>>> dist.all\_to\_all(output, input)\
\>>> output\
\[tensor(\[0\]), tensor(\[4\]), tensor(\[8\]), tensor(\[12\])\]    # Rank 0\
\[tensor(\[1\]), tensor(\[5\]), tensor(\[9\]), tensor(\[13\])\]    # Rank 1\
\[tensor(\[2\]), tensor(\[6\]), tensor(\[10\]), tensor(\[14\])\]   # Rank 2\
\[tensor(\[3\]), tensor(\[7\]), tensor(\[11\]), tensor(\[15\])\]   # Rank 3\
\
Copy to clipboard\
\
\>>> \# Essentially, it is similar to following operation:\
\>>> scatter\_list \= input\
\>>> gather\_list \= output\
\>>> for i in range(world\_size):\
\>>>     dist.scatter(gather\_list\[i\], scatter\_list if i \== rank else \[\], src\=i)\
\
Copy to clipboard\
\
\>>> input\
tensor(\[0, 1, 2, 3, 4, 5\])                                       # Rank 0\
tensor(\[10, 11, 12, 13, 14, 15, 16, 17, 18\])                     # Rank 1\
tensor(\[20, 21, 22, 23, 24\])                                     # Rank 2\
tensor(\[30, 31, 32, 33, 34, 35, 36\])                             # Rank 3\
\>>> input\_splits\
\[2, 2, 1, 1\]                                                     # Rank 0\
\[3, 2, 2, 2\]                                                     # Rank 1\
\[2, 1, 1, 1\]                                                     # Rank 2\
\[2, 2, 2, 1\]                                                     # Rank 3\
\>>> output\_splits\
\[2, 3, 2, 2\]                                                     # Rank 0\
\[2, 2, 1, 2\]                                                     # Rank 1\
\[1, 2, 1, 2\]                                                     # Rank 2\
\[1, 2, 1, 1\]                                                     # Rank 3\
\>>> input \= list(input.split(input\_splits))\
\>>> input\
\[tensor(\[0, 1\]), tensor(\[2, 3\]), tensor(\[4\]), tensor(\[5\])\]                   # Rank 0\
\[tensor(\[10, 11, 12\]), tensor(\[13, 14\]), tensor(\[15, 16\]), tensor(\[17, 18\])\] # Rank 1\
\[tensor(\[20, 21\]), tensor(\[22\]), tensor(\[23\]), tensor(\[24\])\]                 # Rank 2\
\[tensor(\[30, 31\]), tensor(\[32, 33\]), tensor(\[34, 35\]), tensor(\[36\])\]         # Rank 3\
\>>> output \= ...\
\>>> dist.all\_to\_all(output, input)\
\>>> output\
\[tensor(\[0, 1\]), tensor(\[10, 11, 12\]), tensor(\[20, 21\]), tensor(\[30, 31\])\]   # Rank 0\
\[tensor(\[2, 3\]), tensor(\[13, 14\]), tensor(\[22\]), tensor(\[32, 33\])\]           # Rank 1\
\[tensor(\[4\]), tensor(\[15, 16\]), tensor(\[23\]), tensor(\[34, 35\])\]              # Rank 2\
\[tensor(\[5\]), tensor(\[17, 18\]), tensor(\[24\]), tensor(\[36\])\]                  # Rank 3\
\
Copy to clipboard\
\
\>>> \# Another example with tensors of torch.cfloat type.\
\>>> input \= torch.tensor(\
...     \[1 + 1j, 2 + 2j, 3 + 3j, 4 + 4j\], dtype\=torch.cfloat\
... ) + 4 \* rank \* (1 + 1j)\
\>>> input \= list(input.chunk(4))\
\>>> input\
\[tensor(\[1+1j\]), tensor(\[2+2j\]), tensor(\[3+3j\]), tensor(\[4+4j\])\]            # Rank 0\
\[tensor(\[5+5j\]), tensor(\[6+6j\]), tensor(\[7+7j\]), tensor(\[8+8j\])\]            # Rank 1\
\[tensor(\[9+9j\]), tensor(\[10+10j\]), tensor(\[11+11j\]), tensor(\[12+12j\])\]      # Rank 2\
\[tensor(\[13+13j\]), tensor(\[14+14j\]), tensor(\[15+15j\]), tensor(\[16+16j\])\]    # Rank 3\
\>>> output \= list(torch.empty(\[4\], dtype\=torch.int64).chunk(4))\
\>>> dist.all\_to\_all(output, input)\
\>>> output\
\[tensor(\[1+1j\]), tensor(\[5+5j\]), tensor(\[9+9j\]), tensor(\[13+13j\])\]          # Rank 0\
\[tensor(\[2+2j\]), tensor(\[6+6j\]), tensor(\[10+10j\]), tensor(\[14+14j\])\]        # Rank 1\
\[tensor(\[3+3j\]), tensor(\[7+7j\]), tensor(\[11+11j\]), tensor(\[15+15j\])\]        # Rank 2\
\[tensor(\[4+4j\]), tensor(\[8+8j\]), tensor(\[12+12j\]), tensor(\[16+16j\])\]        # Rank 3\
\
Copy to clipboard\
\
torch.distributed.barrier(_group: ProcessGroup | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
 \= GroupMember.WORLD_, _\*_, _async\_op: Literal\[True\]_, _device\_ids: [list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
\] | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
 \= None_, _timeout: timedelta | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
 \= None_) → [Work](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.Work")\
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L6541)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.barrier "Link to this definition")\
\
torch.distributed.barrier(_group: ProcessGroup | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
 \= GroupMember.WORLD_, _async\_op: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 \= False_, _device\_ids: [list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
\] | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
 \= None_, _timeout: timedelta | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
 \= None_) → [Work](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.Work")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
\
Synchronize all processes.\
\
This collective blocks processes until the whole group enters this function, if async\_op is False, or if async work handle is called on wait().\
\
Parameters:\
\
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If None, the default process group will be used.\
    \
*   **async\_op** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – Whether this op should be an async op\
    \
*   **device\_ids** (_\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]__,_ _optional_) – List of device/GPU ids. Only one id is expected.\
    \
*   **timeout** ([_datetime.timedelta_](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")\
    _,_ _optional_) – Timeout for barrier. If `None`, the default process group timeout will be used.\
    \
\
Returns:\
\
Async work handle, if async\_op is set to True. None, if not async\_op or if not part of the group\
\
Note\
\
ProcessGroupNCCL now blocks the cpu thread till the completion of the barrier collective.\
\
Note\
\
ProcessGroupNCCL implements barrier as an all\_reduce of a 1-element tensor. A device must be chosen for allocating this tensor. The device choice is made by checking in this order (1) the first device passed to device\_ids arg of barrier if not None, (2) the device passed to init\_process\_group if not None, (3) the device that was first used with this process group, if another collective with tensor inputs has been performed, (4) the device index indicated by the global rank mod local device count.\
\
torch.distributed.monitored\_barrier(_group\=None_, _timeout\=None_, _wait\_all\_ranks\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L6619)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.monitored_barrier "Link to this definition")\
\
Synchronize processes similar to `torch.distributed.barrier`, but consider a configurable timeout.\
\
It is able to report ranks that did not pass this barrier within the provided timeout. Specifically, for non-zero ranks, will block until a send/recv is processed from rank 0. Rank 0 will block until all send /recv from other ranks are processed, and will report failures for ranks that failed to respond in time. Note that if one rank does not reach the monitored\_barrier (for example due to a hang), all other ranks would fail in monitored\_barrier.\
\
This collective will block all processes/ranks in the group, until the whole group exits the function successfully, making it useful for debugging and synchronizing. However, it can have a performance impact and should only be used for debugging or scenarios that require full synchronization points on the host-side. For debugging purposes, this barrier can be inserted before the application’s collective calls to check if any ranks are desynchronized.\
\
Note\
\
Note that this collective is only supported with the GLOO backend.\
\
Parameters:\
\
*   **group** (_ProcessGroup__,_ _optional_) – The process group to work on. If `None`, the default process group will be used.\
    \
*   **timeout** ([_datetime.timedelta_](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")\
    _,_ _optional_) – Timeout for monitored\_barrier. If `None`, the default process group timeout will be used.\
    \
*   **wait\_all\_ranks** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – Whether to collect all failed ranks or not. By default, this is `False` and `monitored_barrier` on rank 0 will throw on the first failed rank it encounters in order to fail fast. By setting `wait_all_ranks=True` `monitored_barrier` will collect all failed ranks and throw an error containing information about all failed ranks.\
    \
\
Returns:\
\
`None`.\
\
Return type:\
\
None\
\
Example::\
\
\>>> \# Note: Process group initialization omitted on each rank.\
\>>> import torch.distributed as dist\
\>>> if dist.get\_rank() != 1:\
\>>>     dist.monitored\_barrier() \# Raises exception indicating that\
\>>> \# rank 1 did not call into monitored\_barrier.\
\>>> \# Example with wait\_all\_ranks=True\
\>>> if dist.get\_rank() \== 0:\
\>>>     dist.monitored\_barrier(wait\_all\_ranks\=True) \# Raises exception\
\>>> \# indicating that ranks 1, 2, ... world\_size - 1 did not call into\
\>>> \# monitored\_barrier.\
\
Copy to clipboard\
\
_class_ torch.distributed.Work[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "Link to this definition")\
\
A Work object represents the handle to a pending asynchronous operation in PyTorch’s distributed package. It is returned by non-blocking collective operations, such as dist.all\_reduce(tensor, async\_op=True).\
\
block\_current\_stream(_self: torch.\_C.\_distributed\_c10d.Work_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work.block_current_stream "Link to this definition")\
\
Blocks the currently active GPU stream on the operation to complete. For GPU based collectives this is equivalent to synchronize. For CPU initiated collectives such as with Gloo this will block the CUDA stream until the operation is complete.\
\
This returns immediately in all cases.\
\
To check whether an operation was successful you should check the Work object result asynchronously.\
\
boxed(_self: torch.\_C.\_distributed\_c10d.Work_) → [object](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work.boxed "Link to this definition")\
\
exception(_self: torch.\_C.\_distributed\_c10d.Work_) → [object](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work.exception "Link to this definition")\
\
get\_future(_self: torch.\_C.\_distributed\_c10d.Work_) → torch.Future[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work.get_future "Link to this definition")\
\
Returns:\
\
A `torch.futures.Future` object which is associated with the completion of the `Work`. As an example, a future object can be retrieved by `fut = process_group.allreduce(tensors).get_future()`.\
\
Example::\
\
Below is an example of a simple allreduce DDP communication hook that uses `get_future` API to retrieve a Future associated with the completion of `allreduce`.\
\
\>>> def allreduce(process\_group: dist.ProcessGroup, bucket: dist.GradBucket): \-> torch.futures.Future\
\>>>     group\_to\_use \= process\_group if process\_group is not None else torch.distributed.group.WORLD\
\>>>     tensor \= bucket.buffer().div\_(group\_to\_use.size())\
\>>>     return torch.distributed.all\_reduce(tensor, group\=group\_to\_use, async\_op\=True).get\_future()\
\>>> ddp\_model.register\_comm\_hook(state\=None, hook\=allreduce)\
\
Copy to clipboard\
\
Warning\
\
`get_future` API supports NCCL, and partially GLOO and MPI backends (no support for peer-to-peer operations like send/recv) and will return a `torch.futures.Future`.\
\
In the example above, `allreduce` work will be done on GPU using NCCL backend, `fut.wait()` will return after synchronizing the appropriate NCCL streams with PyTorch’s current device streams to ensure we can have asynchronous CUDA execution and it does not wait for the entire operation to complete on GPU. Note that `CUDAFuture` does not support `TORCH_NCCL_BLOCKING_WAIT` flag or NCCL’s `barrier()`. In addition, if a callback function was added by `fut.then()`, it will wait until `WorkNCCL`’s NCCL streams synchronize with `ProcessGroupNCCL`’s dedicated callback stream and invoke the callback inline after running the callback on the callback stream. `fut.then()` will return another `CUDAFuture` that holds the return value of the callback and a `CUDAEvent` that recorded the callback stream.\
\
> 1.  For CPU work, `fut.done()` returns true when work has been completed and value() tensors are ready.\
>     \
> 2.  For GPU work, `fut.done()` returns true only whether the operation has been enqueued.\
>     \
> 3.  For mixed CPU-GPU work (e.g. sending GPU tensors with GLOO), `fut.done()` returns true when tensors have arrived on respective nodes, but not yet necessarily synched on respective GPUs (similarly to GPU work).\
>     \
\
get\_future\_result(_self: torch.\_C.\_distributed\_c10d.Work_) → torch.Future[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work.get_future_result "Link to this definition")\
\
Returns:\
\
A `torch.futures.Future` object of int type which maps to the enum type of WorkResult As an example, a future object can be retrieved by `fut = process_group.allreduce(tensor).get_future_result()`.\
\
Example::\
\
users can use `fut.wait()` to blocking wait for the completion of the work and get the WorkResult by `fut.value()`. Also, users can use `fut.then(call_back_func)` to register a callback function to be called when the work is completed, without blocking the current thread.\
\
Warning\
\
`get_future_result` API supports NCCL\
\
is\_completed(_self: torch.\_C.\_distributed\_c10d.Work_) → [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work.is_completed "Link to this definition")\
\
is\_success(_self: torch.\_C.\_distributed\_c10d.Work_) → [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work.is_success "Link to this definition")\
\
result(_self: torch.\_C.\_distributed\_c10d.Work_) → [list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[torch.Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\][#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work.result "Link to this definition")\
\
source\_rank(_self: torch.\_C.\_distributed\_c10d.Work_) → [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work.source_rank "Link to this definition")\
\
synchronize(_self: torch.\_C.\_distributed\_c10d.Work_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work.synchronize "Link to this definition")\
\
_static_ unbox(_arg0: [object](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")\
_) → torch.\_C.\_distributed\_c10d.Work[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work.unbox "Link to this definition")\
\
wait(_self: torch.\_C.\_distributed\_c10d.Work_, _timeout: [datetime.timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")\
 \= datetime.timedelta(0)_) → [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work.wait "Link to this definition")\
\
Returns:\
\
true/false.\
\
Example::\
\
try:\
\
work.wait(timeout)\
\
except:\
\
\# some handling\
\
Warning\
\
In normal cases, users do not need to set the timeout. calling wait() is the same as calling synchronize(): Letting the current stream block on the completion of the NCCL work. However, if timeout is set, it will block the CPU thread until the NCCL work is completed or timed out. If timeout, exception will be thrown.\
\
_class_ torch.distributed.ReduceOp[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.ReduceOp "Link to this definition")\
\
An enum-like class for available reduction operations: `SUM`, `PRODUCT`, `MIN`, `MAX`, `BAND`, `BOR`, `BXOR`, and `PREMUL_SUM`.\
\
`BAND`, `BOR`, and `BXOR` reductions are not available when using the `NCCL` backend.\
\
`AVG` divides values by the world size before summing across ranks. `AVG` is only available with the `NCCL` backend, and only for NCCL versions 2.10 or later.\
\
`PREMUL_SUM` multiplies inputs by a given scalar locally before reduction. `PREMUL_SUM` is available with the `NCCL` backend (NCCL versions 2.11 or later) and the `XCCL` backend. It can be used by calling `ReduceOp.PREMUL_SUM(factor)` where factor is a float or a single-element Tensor.\
\
Additionally, `MAX`, `MIN` and `PRODUCT` are not supported for complex tensors.\
\
The values of this class can be accessed as attributes, e.g., `ReduceOp.SUM`. They are used in specifying strategies for reduction collectives, e.g., [`reduce()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.reduce "torch.distributed.reduce")\
.\
\
This class does not support `__members__` property.\
\
_class_ RedOpType[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.ReduceOp.RedOpType "Link to this definition")\
\
Members:\
\
SUM\
\
AVG\
\
PRODUCT\
\
MIN\
\
MAX\
\
BAND\
\
BOR\
\
BXOR\
\
PREMUL\_SUM\
\
_property_ name[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.ReduceOp.RedOpType.name "Link to this definition")\
\
boxed(_self: torch.\_C.\_distributed\_c10d.ReduceOp_) → [object](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.ReduceOp.boxed "Link to this definition")\
\
_property_ factor[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.ReduceOp.factor "Link to this definition")\
\
The factor of the PREMUL\_SUM ReduceOp.\
\
_static_ unbox(_arg0: [object](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")\
_) → torch.\_C.\_distributed\_c10d.ReduceOp[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.ReduceOp.unbox "Link to this definition")\
\
_class_ torch.distributed.reduce\_op[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.reduce_op "Link to this definition")\
\
Deprecated enum-like class for reduction operations: `SUM`, `PRODUCT`, `MIN`, and `MAX`.\
\
[`ReduceOp`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.ReduceOp "torch.distributed.ReduceOp")\
 is recommended to use instead.\
\
Distributed Key-Value Store[#](https://docs.pytorch.org/docs/2.15/distributed.html#distributed-key-value-store "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------\
\
The distributed package comes with a distributed key-value store, which can be used to share information between processes in the group as well as to initialize the distributed package in [`torch.distributed.init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")\
 (by explicitly creating the store as an alternative to specifying `init_method`.) There are 3 choices for Key-Value Stores: [`TCPStore`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.TCPStore "torch.distributed.TCPStore")\
, [`FileStore`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.FileStore "torch.distributed.FileStore")\
, and [`HashStore`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.HashStore "torch.distributed.HashStore")\
.\
\
_class_ torch.distributed.Store[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store "Link to this definition")\
\
Base class for all store implementations, such as the 3 provided by PyTorch distributed: ([`TCPStore`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.TCPStore "torch.distributed.TCPStore")\
, [`FileStore`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.FileStore "torch.distributed.FileStore")\
, and [`HashStore`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.HashStore "torch.distributed.HashStore")\
).\
\
\_\_init\_\_(_self: torch.\_C.\_distributed\_c10d.Store_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store.__init__ "Link to this definition")\
\
add(_self: torch.\_C.\_distributed\_c10d.Store_, _arg0: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_, _arg1: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.15)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.15)")\
_) → [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store.add "Link to this definition")\
\
The first call to add for a given `key` creates a counter associated with `key` in the store, initialized to `amount`. Subsequent calls to add with the same `key` increment the counter by the specified `amount`. Calling `add()` with a key that has already been set in the store by `set()` will result in an exception.\
\
Parameters:\
\
*   **key** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – The key in the store whose counter will be incremented.\
    \
*   **amount** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – The quantity by which the counter will be incremented.\
    \
\
Example::\
\
\>>> import torch.distributed as dist\
\>>> from datetime import timedelta\
\>>> \# Using TCPStore as an example, other store types can also be used\
\>>> store \= dist.TCPStore("127.0.0.1", 0, 1, True, timedelta(seconds\=30))\
\>>> store.add("first\_key", 1)\
\>>> store.add("first\_key", 6)\
\>>> \# Should return 7\
\>>> store.get("first\_key")\
\
Copy to clipboard\
\
append(_self: torch.\_C.\_distributed\_c10d.Store_, _arg0: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_, _arg1: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store.append "Link to this definition")\
\
Append the key-value pair into the store based on the supplied `key` and `value`. If `key` does not exist in the store, it will be created.\
\
Parameters:\
\
*   **key** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – The key to be appended to the store.\
    \
*   **value** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – The value associated with `key` to be added to the store.\
    \
\
Example::\
\
\>>> import torch.distributed as dist\
\>>> from datetime import timedelta\
\>>> store \= dist.TCPStore("127.0.0.1", 0, 1, True, timedelta(seconds\=30))\
\>>> store.append("first\_key", "po")\
\>>> store.append("first\_key", "tato")\
\>>> \# Should return "potato"\
\>>> store.get("first\_key")\
\
Copy to clipboard\
\
barrier(_self: torch.\_C.\_distributed\_c10d.Store_, _key: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_, _world\_size: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.15)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.15)")\
_, _timeout: [datetime.timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
 \= None_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store.barrier "Link to this definition")\
\
Barrier operation that blocks until `world_size` workers have called it with the same `key`. If `timeout` is not specified, the store’s default timeout is used.\
\
Parameters:\
\
*   **key** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – The unique key for this barrier instance.\
    \
*   **world\_size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – The number of workers that must call barrier before it unblocks.\
    \
*   **timeout** (_timedelta__,_ _optional_) – Time to wait before throwing an exception. Defaults to store timeout.\
    \
\
Example::\
\
\>>> import torch.distributed as dist\
\>>> from datetime import timedelta\
\>>> store \= dist.TCPStore("127.0.0.1", 0, 1, True, timedelta(seconds\=30))\
\>>> \# This will return immediately since world\_size=1\
\>>> store.barrier("my\_barrier", 1)\
\>>> store.barrier("my\_barrier2", 1, timedelta(seconds\=10))\
\
Copy to clipboard\
\
check(_self: torch.\_C.\_distributed\_c10d.Store_, _arg0: [collections.abc.Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\]_) → [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store.check "Link to this definition")\
\
The call to check whether a given list of `keys` have value stored in the store. This call immediately returns in normal cases but still suffers from some edge deadlock cases, e.g, calling check after TCPStore has been destroyed. Calling `check()` with a list of keys that one wants to check whether stored in the store or not.\
\
Parameters:\
\
**keys** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
_\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_\]_) – The keys to query whether stored in the store.\
\
Example::\
\
\>>> import torch.distributed as dist\
\>>> from datetime import timedelta\
\>>> \# Using TCPStore as an example, other store types can also be used\
\>>> store \= dist.TCPStore("127.0.0.1", 0, 1, True, timedelta(seconds\=30))\
\>>> store.add("first\_key", 1)\
\>>> \# Should return 7\
\>>> store.check(\["first\_key"\])\
\
Copy to clipboard\
\
clone(_self: torch.\_C.\_distributed\_c10d.Store_) → torch.\_C.\_distributed\_c10d.Store[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store.clone "Link to this definition")\
\
Clones the store and returns a new object that points to the same underlying store. The returned store can be used concurrently with the original object. This is intended to provide a safe way to use a store from multiple threads by cloning one store per thread.\
\
compare\_set(_self: torch.\_C.\_distributed\_c10d.Store_, _arg0: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_, _arg1: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_, _arg2: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_) → [bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store.compare_set "Link to this definition")\
\
Inserts the key-value pair into the store based on the supplied `key` and performs comparison between `expected_value` and `desired_value` before inserting. `desired_value` will only be set if `expected_value` for the `key` already exists in the store or if `expected_value` is an empty string.\
\
Parameters:\
\
*   **key** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – The key to be checked in the store.\
    \
*   **expected\_value** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – The value associated with `key` to be checked before insertion.\
    \
*   **desired\_value** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – The value associated with `key` to be added to the store.\
    \
\
Example::\
\
\>>> import torch.distributed as dist\
\>>> from datetime import timedelta\
\>>> store \= dist.TCPStore("127.0.0.1", 0, 1, True, timedelta(seconds\=30))\
\>>> store.set("key", "first\_value")\
\>>> store.compare\_set("key", "first\_value", "second\_value")\
\>>> \# Should return "second\_value"\
\>>> store.get("key")\
\
Copy to clipboard\
\
delete\_key(_self: torch.\_C.\_distributed\_c10d.Store_, _arg0: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_) → [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store.delete_key "Link to this definition")\
\
Deletes the key-value pair associated with `key` from the store. Returns true if the key was successfully deleted, and false if it was not.\
\
Warning\
\
The `delete_key` API is only supported by the [`TCPStore`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.TCPStore "torch.distributed.TCPStore")\
 and [`HashStore`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.HashStore "torch.distributed.HashStore")\
. Using this API with the [`FileStore`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.FileStore "torch.distributed.FileStore")\
 will result in an exception.\
\
Parameters:\
\
**key** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
) – The key to be deleted from the store\
\
Returns:\
\
True if `key` was deleted, otherwise False.\
\
Example::\
\
\>>> import torch.distributed as dist\
\>>> from datetime import timedelta\
\>>> \# Using TCPStore as an example, HashStore can also be used\
\>>> store \= dist.TCPStore("127.0.0.1", 0, 1, True, timedelta(seconds\=30))\
\>>> store.set("first\_key")\
\>>> \# This should return true\
\>>> store.delete\_key("first\_key")\
\>>> \# This should return false\
\>>> store.delete\_key("bad\_key")\
\
Copy to clipboard\
\
get(_self: torch.\_C.\_distributed\_c10d.Store_, _arg0: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_) → [bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store.get "Link to this definition")\
\
Retrieves the value associated with the given `key` in the store. If `key` is not present in the store, the function will wait for `timeout`, which is defined when initializing the store, before throwing an exception.\
\
Parameters:\
\
**key** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
) – The function will return the value associated with this key.\
\
Returns:\
\
Value associated with `key` if `key` is in the store.\
\
Example::\
\
\>>> import torch.distributed as dist\
\>>> from datetime import timedelta\
\>>> store \= dist.TCPStore("127.0.0.1", 0, 1, True, timedelta(seconds\=30))\
\>>> store.set("first\_key", "first\_value")\
\>>> \# Should return "first\_value"\
\>>> store.get("first\_key")\
\
Copy to clipboard\
\
has\_extended\_api(_self: torch.\_C.\_distributed\_c10d.Store_) → [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store.has_extended_api "Link to this definition")\
\
Returns true if the store supports extended operations.\
\
list\_keys(_self: torch.\_C.\_distributed\_c10d.Store_) → [list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\][#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store.list_keys "Link to this definition")\
\
Returns a list of all keys in the store.\
\
multi\_get(_self: torch.\_C.\_distributed\_c10d.Store_, _arg0: [collections.abc.Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\]_) → [list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")\
\][#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store.multi_get "Link to this definition")\
\
Retrieve all values in `keys`. If any key in `keys` is not present in the store, the function will wait for `timeout`\
\
Parameters:\
\
**keys** (_List__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_\]_) – The keys to be retrieved from the store.\
\
Example::\
\
\>>> import torch.distributed as dist\
\>>> from datetime import timedelta\
\>>> store \= dist.TCPStore("127.0.0.1", 0, 1, True, timedelta(seconds\=30))\
\>>> store.set("first\_key", "po")\
\>>> store.set("second\_key", "tato")\
\>>> \# Should return \[b"po", b"tato"\]\
\>>> store.multi\_get(\["first\_key", "second\_key"\])\
\
Copy to clipboard\
\
multi\_set(_self: torch.\_C.\_distributed\_c10d.Store_, _arg0: [collections.abc.Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\]_, _arg1: [collections.abc.Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\]_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store.multi_set "Link to this definition")\
\
Inserts a list key-value pair into the store based on the supplied `keys` and `values`\
\
Parameters:\
\
*   **keys** (_List__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_) – The keys to insert.\
    \
*   **values** (_List__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_) – The values to insert.\
    \
\
Example::\
\
\>>> import torch.distributed as dist\
\>>> from datetime import timedelta\
\>>> store \= dist.TCPStore("127.0.0.1", 0, 1, True, timedelta(seconds\=30))\
\>>> store.multi\_set(\["first\_key", "second\_key"\], \["po", "tato"\])\
\>>> \# Should return b"po"\
\>>> store.get("first\_key")\
\
Copy to clipboard\
\
num\_keys(_self: torch.\_C.\_distributed\_c10d.Store_) → [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store.num_keys "Link to this definition")\
\
Returns the number of keys set in the store. Note that this number will typically be one greater than the number of keys added by `set()` and `add()` since one key is used to coordinate all the workers using the store.\
\
Warning\
\
When used with the [`TCPStore`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.TCPStore "torch.distributed.TCPStore")\
, `num_keys` returns the number of keys written to the underlying file. If the store is destructed and another store is created with the same file, the original keys will be retained.\
\
Returns:\
\
The number of keys present in the store.\
\
Example::\
\
\>>> import torch.distributed as dist\
\>>> from datetime import timedelta\
\>>> \# Using TCPStore as an example, other store types can also be used\
\>>> store \= dist.TCPStore("127.0.0.1", 0, 1, True, timedelta(seconds\=30))\
\>>> store.set("first\_key", "first\_value")\
\>>> \# This should return 2\
\>>> store.num\_keys()\
\
Copy to clipboard\
\
queue\_len(_self: torch.\_C.\_distributed\_c10d.Store_, _arg0: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_) → [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store.queue_len "Link to this definition")\
\
Returns the length of the specified queue.\
\
If the queue doesn’t exist it returns 0.\
\
See queue\_push for more details.\
\
Parameters:\
\
**key** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
) – The key of the queue to get the length.\
\
queue\_pop(_self: torch.\_C.\_distributed\_c10d.Store_, _key: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_, _block: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 \= True_) → [bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store.queue_pop "Link to this definition")\
\
Pops a value from the specified queue or waits until timeout if the queue is empty.\
\
See queue\_push for more details.\
\
If block is False, a dist.QueueEmptyError will be raised if the queue is empty.\
\
Parameters:\
\
*   **key** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – The key of the queue to pop from.\
    \
*   **block** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    ) – Whether to block waiting for the key or immediately return.\
    \
\
queue\_push(_self: torch.\_C.\_distributed\_c10d.Store_, _arg0: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_, _arg1: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store.queue_push "Link to this definition")\
\
Pushes a value into the specified queue.\
\
Using the same key for queues and set/get operations may result in unexpected behavior.\
\
wait/check operations are supported for queues.\
\
wait with queues will only wake one waiting worker rather than all.\
\
Parameters:\
\
*   **key** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – The key of the queue to push to.\
    \
*   **value** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – The value to push into the queue.\
    \
\
set(_self: torch.\_C.\_distributed\_c10d.Store_, _arg0: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_, _arg1: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store.set "Link to this definition")\
\
Inserts the key-value pair into the store based on the supplied `key` and `value`. If `key` already exists in the store, it will overwrite the old value with the new supplied `value`.\
\
Parameters:\
\
*   **key** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – The key to be added to the store.\
    \
*   **value** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – The value associated with `key` to be added to the store.\
    \
\
Example::\
\
\>>> import torch.distributed as dist\
\>>> from datetime import timedelta\
\>>> store \= dist.TCPStore("127.0.0.1", 0, 1, True, timedelta(seconds\=30))\
\>>> store.set("first\_key", "first\_value")\
\>>> \# Should return "first\_value"\
\>>> store.get("first\_key")\
\
Copy to clipboard\
\
set\_timeout(_self: torch.\_C.\_distributed\_c10d.Store_, _arg0: [datetime.timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")\
_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store.set_timeout "Link to this definition")\
\
Sets the store’s default timeout. This timeout is used during initialization and in `wait()` and `get()`.\
\
Parameters:\
\
**timeout** (_timedelta_) – timeout to be set in the store.\
\
Example::\
\
\>>> import torch.distributed as dist\
\>>> from datetime import timedelta\
\>>> \# Using TCPStore as an example, other store types can also be used\
\>>> store \= dist.TCPStore("127.0.0.1", 0, 1, True, timedelta(seconds\=30))\
\>>> store.set\_timeout(timedelta(seconds\=10))\
\>>> \# This will throw an exception after 10 seconds\
\>>> store.wait(\["bad\_key"\])\
\
Copy to clipboard\
\
_property_ timeout[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store.timeout "Link to this definition")\
\
Gets the timeout of the store.\
\
wait(_\*args_, _\*\*kwargs_)[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Store.wait "Link to this definition")\
\
Overloaded function.\
\
1.  wait(self: torch.\_C.\_distributed\_c10d.Store, arg0: collections.abc.Sequence\[str\]) -> None\
    \
\
Waits for each key in `keys` to be added to the store. If not all keys are set before the `timeout` (set during store initialization), then `wait` will throw an exception.\
\
Parameters:\
\
**keys** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
) – List of keys on which to wait until they are set in the store.\
\
Example::\
\
\>>> import torch.distributed as dist\
\>>> from datetime import timedelta\
\>>> \# Using TCPStore as an example, other store types can also be used\
\>>> store \= dist.TCPStore("127.0.0.1", 0, 1, True, timedelta(seconds\=30))\
\>>> \# This will throw an exception after 30 seconds\
\>>> store.wait(\["bad\_key"\])\
\
Copy to clipboard\
\
2.  wait(self: torch.\_C.\_distributed\_c10d.Store, arg0: collections.abc.Sequence\[str\], arg1: datetime.timedelta) -> None\
    \
\
Waits for each key in `keys` to be added to the store, and throws an exception if the keys have not been set by the supplied `timeout`.\
\
Parameters:\
\
*   **keys** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
    ) – List of keys on which to wait until they are set in the store.\
    \
*   **timeout** (_timedelta_) – Time to wait for the keys to be added before throwing an exception.\
    \
\
Example::\
\
\>>> import torch.distributed as dist\
\>>> from datetime import timedelta\
\>>> \# Using TCPStore as an example, other store types can also be used\
\>>> store \= dist.TCPStore("127.0.0.1", 0, 1, True, timedelta(seconds\=30))\
\>>> \# This will throw an exception after 10 seconds\
\>>> store.wait(\["bad\_key"\], timedelta(seconds\=10))\
\
Copy to clipboard\
\
_class_ torch.distributed.TCPStore[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.TCPStore "Link to this definition")\
\
A TCP-based distributed key-value store implementation. The server store holds the data, while the client stores can connect to the server store over TCP and perform actions such as `set()` to insert a key-value pair, `get()` to retrieve a key-value pair, etc. There should always be one server store initialized because the client store(s) will wait for the server to establish a connection.\
\
Parameters:\
\
*   **host\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – The hostname or IP Address the server store should run on.\
    \
*   **port** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – The port on which the server store should listen for incoming requests.\
    \
*   **world\_size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – The total number of store users (number of clients + 1 for the server). Default is None (None indicates a non-fixed number of store users).\
    \
*   **is\_master** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – True when initializing the server store and False for client stores. Default is False.\
    \
*   **timeout** (_timedelta__,_ _optional_) – Timeout used by the store during initialization and for methods such as `get()` and `wait()`. Default is timedelta(seconds=300)\
    \
*   **wait\_for\_workers** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – Whether to wait for all the workers to connect with the server store. This is only applicable when world\_size is a fixed value. Default is True.\
    \
*   **multi\_tenant** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – If True, all `TCPStore` instances in the current process with the same host/port will use the same underlying `TCPServer`. Default is False.\
    \
*   **master\_listen\_fd** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – If specified, the underlying `TCPServer` will listen on this file descriptor, which must be a socket already bound to `port`. To bind an ephemeral port we recommend setting the port to 0 and reading `.port`. Default is None (meaning the server creates a new socket and attempts to bind it to `port`).\
    \
*   **use\_libuv** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _,_ _optional_) – If True, use libuv for `TCPServer` backend. Default is True.\
    \
\
Example::\
\
\>>> import torch.distributed as dist\
\>>> from datetime import timedelta\
\>>> \# Run on process 1 (server)\
\>>> server\_store \= dist.TCPStore("127.0.0.1", 1234, 2, True, timedelta(seconds\=30))\
\>>> \# Run on process 2 (client)\
\>>> client\_store \= dist.TCPStore("127.0.0.1", 1234, 2, False)\
\>>> \# Use any of the store methods from either the client or server after initialization\
\>>> server\_store.set("first\_key", "first\_value")\
\>>> client\_store.get("first\_key")\
\
Copy to clipboard\
\
\_\_init\_\_(_self: [torch.\_C.\_distributed\_c10d.TCPStore](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.TCPStore "torch._C._distributed_c10d.TCPStore")\
_, _host\_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_, _port: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.15)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.15)")\
_, _world\_size: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.15)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.15)")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
 \= None_, _is\_master: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 \= False_, _timeout: [datetime.timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")\
 \= datetime.timedelta(seconds=300)_, _wait\_for\_workers: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 \= True_, _multi\_tenant: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 \= False_, _master\_listen\_fd: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.15)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.15)")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
 \= None_, _use\_libuv: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 \= True_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.TCPStore.__init__ "Link to this definition")\
\
Creates a new TCPStore.\
\
_property_ host[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.TCPStore.host "Link to this definition")\
\
Gets the hostname on which the store listens for requests.\
\
_property_ libuvBackend[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.TCPStore.libuvBackend "Link to this definition")\
\
Returns True if it’s using the libuv backend.\
\
_property_ port[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.TCPStore.port "Link to this definition")\
\
Gets the port number on which the store listens for requests.\
\
_class_ torch.distributed.HashStore[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.HashStore "Link to this definition")\
\
A thread-safe store implementation based on an underlying hashmap. This store can be used within the same process (for example, by other threads), but cannot be used across processes.\
\
Example::\
\
\>>> import torch.distributed as dist\
\>>> store \= dist.HashStore()\
\>>> \# store can be used from other threads\
\>>> \# Use any of the store methods after initialization\
\>>> store.set("first\_key", "first\_value")\
\
Copy to clipboard\
\
\_\_init\_\_(_self: [torch.\_C.\_distributed\_c10d.HashStore](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.HashStore "torch._C._distributed_c10d.HashStore")\
_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.HashStore.__init__ "Link to this definition")\
\
Creates a new HashStore.\
\
_class_ torch.distributed.FileStore[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.FileStore "Link to this definition")\
\
A store implementation that uses a file to store the underlying key-value pairs.\
\
Parameters:\
\
*   **file\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – path of the file in which to store the key-value pairs\
    \
*   **world\_size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _optional_) – The total number of processes using the store. Default is -1 (a negative value indicates a non-fixed number of store users).\
    \
\
Example::\
\
\>>> import torch.distributed as dist\
\>>> store1 \= dist.FileStore("/tmp/filestore", 2)\
\>>> store2 \= dist.FileStore("/tmp/filestore", 2)\
\>>> \# Use any of the store methods from either the client or server after initialization\
\>>> store1.set("first\_key", "first\_value")\
\>>> store2.get("first\_key")\
\
Copy to clipboard\
\
\_\_init\_\_(_self: [torch.\_C.\_distributed\_c10d.FileStore](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.FileStore "torch._C._distributed_c10d.FileStore")\
_, _file\_name: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_, _world\_size: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "(in Python v3.15)")\
 | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex "(in Python v3.15)")\
 \= \-1_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.FileStore.__init__ "Link to this definition")\
\
Creates a new FileStore.\
\
_property_ path[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.FileStore.path "Link to this definition")\
\
Gets the path of the file used by FileStore to store key-value pairs.\
\
_class_ torch.distributed.PrefixStore[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.PrefixStore "Link to this definition")\
\
A wrapper around any of the 3 key-value stores ([`TCPStore`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.TCPStore "torch.distributed.TCPStore")\
, [`FileStore`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.FileStore "torch.distributed.FileStore")\
, and [`HashStore`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.HashStore "torch.distributed.HashStore")\
) that adds a prefix to each key inserted to the store.\
\
Parameters:\
\
*   **prefix** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    ) – The prefix string that is prepended to each key before being inserted into the store.\
    \
*   **store** (_torch.distributed.store_) – A store object that forms the underlying key-value store.\
    \
\
\_\_init\_\_(_self: torch.\_C.\_distributed\_c10d.PrefixStore_, _prefix: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
_, _store: torch.\_C.\_distributed\_c10d.Store_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.PrefixStore.__init__ "Link to this definition")\
\
Creates a new PrefixStore.\
\
_property_ underlying\_store[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.PrefixStore.underlying_store "Link to this definition")\
\
Gets the underlying store object that PrefixStore wraps around.\
\
Profiling Collective Communication[#](https://docs.pytorch.org/docs/2.15/distributed.html#profiling-collective-communication "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------------------------------------\
\
Note that you can use `torch.profiler` (recommended, only available after 1.8.1) or `torch.autograd.profiler` to profile collective communication and point-to-point communication APIs mentioned here. All out-of-the-box backends (`gloo`, `nccl`, `mpi`) are supported and collective communication usage will be rendered as expected in profiling output/traces. Profiling your code is the same as any regular torch operator:\
\
import torch\
import torch.distributed as dist\
with torch.profiler():\
    tensor \= torch.randn(20, 10)\
    dist.all\_reduce(tensor)\
\
Copy to clipboard\
\
Please refer to the [profiler documentation](https://pytorch.org/docs/main/profiler.html)\
 for a full overview of profiler features.\
\
torch.distributed.distributed\_c10d.record\_comm(_name_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/distributed_c10d.py#L8154)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.distributed_c10d.record_comm "Link to this definition")\
\
Context manager to set a custom profiling name for communication collectives.\
\
When active, all c10d collectives issued within this context will use `name` as their profiling title in the Work base class, overriding the default backend-specific name (e.g. `nccl:all_reduce`). This works across all backends without per-backend or per-collective changes.\
\
Parameters:\
\
**name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
) – The profiling name to associate with collectives.\
\
Return type:\
\
[_Iterator_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.15)")\
\[None\]\
\
Example::\
\
\>>> with dist.record\_comm("FSDP::all\_gather (layer1)"):\
...     dist.all\_gather\_into\_tensor(output, input, group\=pg)\
\
Copy to clipboard\
\
Optimization with Symmetric Memory[#](https://docs.pytorch.org/docs/2.15/distributed.html#optimization-with-symmetric-memory "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------------------------------------\
\
### NCCL Symmetric Kernels[#](https://docs.pytorch.org/docs/2.15/distributed.html#nccl-symmetric-kernels "Link to this heading")\
\
NCCL 2.27 and later ship device kernels written specifically for symmetric, window-registered buffers, using low-latency, multimem/NVLS, and TMA algorithms rather than the generic ring/tree path. `all_reduce`, `all_gather_into_tensor` and `reduce_scatter_tensor` dispatch to them automatically once their buffers are registered — the call site does not change. When the buffers are not registered, or the op/dtype combination has no symmetric implementation, NCCL silently falls back to the regular path.\
\
For how to register buffers, the supported op/dtype matrix, and how to confirm the symmetric kernels actually ran, see [NCCL Symmetric Kernels](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#nccl-symmetric-kernels)\
 in the Symmetric Memory documentation.\
\
### Copy Engine Collectives[#](https://docs.pytorch.org/docs/2.15/distributed.html#copy-engine-collectives "Link to this heading")\
\
When NCCL collective operations are performed on symmetric memory tensors with the zero-CTA policy, data movement is offloaded to the GPU’s copy engines (DMA engines) instead of using CUDA streaming multiprocessors (SMs). This frees up SMs for compute work, enabling better overlap of communication and computation.\
\
For setup instructions, requirements, and examples, see [Copy Engine Collectives](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#copy-engine-collectives)\
 in the Symmetric Memory documentation.\
\
### Higher-Precision Reduction[#](https://docs.pytorch.org/docs/2.15/distributed.html#higher-precision-reduction "Link to this heading")\
\
When NCCL collectives such as `reduce_scatter` and `all_reduce` operate on symmetric memory tensors, NCCL’s symmetric kernel implementation automatically performs internal reduction with higher precision (e.g., BF16/FP16 in → FP32 accumulate → BF16/FP16 out). This improves numerical accuracy without any code changes to the collective call.\
\
For details on scope, supported domains, and version requirements, see [Higher-Precision Reduction](https://docs.pytorch.org/docs/2.15/symmetric_memory.html#higher-precision-reduction)\
 in the Symmetric Memory documentation.\
\
Multi-GPU collective functions[#](https://docs.pytorch.org/docs/2.15/distributed.html#multi-gpu-collective-functions "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------------\
\
Warning\
\
The multi-GPU functions (which stand for multiple GPUs per CPU thread) are deprecated. As of today, PyTorch Distributed’s preferred programming model is one device per thread, as exemplified by the APIs in this document. If you are a backend developer and want to support multiple devices per thread, please contact PyTorch Distributed’s maintainers.\
\
Object collectives[#](https://docs.pytorch.org/docs/2.15/distributed.html#object-collectives "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------\
\
Warning\
\
Object collectives have a number of serious limitations. Read further to determine if they are safe to use for your use case.\
\
Object collectives are a set of collective-like operations that work on arbitrary Python objects, as long as they can be pickled. There are various collective patterns implemented (e.g. broadcast, all\_gather, …) but they each roughly follow this pattern:\
\
1.  convert the input object into a pickle (raw bytes), then shove it into a byte tensor\
    \
2.  communicate the size of this byte tensor to peers (first collective operation)\
    \
3.  allocate appropriately sized tensor to perform the real collective\
    \
4.  communicate the object data (second collective operation)\
    \
5.  convert raw data back into Python (unpickle)\
    \
\
Object collectives sometimes have surprising performance or memory characteristics that lead to long runtimes or OOMs, and thus they should be used with caution. Here are some common issues.\
\
**Asymmetric pickle/unpickle time** - Pickling objects can be slow, depending on the number, type and size of the objects. When the collective has a fan-in (e.g. gather\_object), the receiving rank(s) must unpickle N times more objects than the sending rank(s) had to pickle, which can cause other ranks to time out on their next collective.\
\
**Inefficient tensor communication** - Tensors should be sent via regular collective APIs, not object collective APIs. It is possible to send Tensors via object collective APIs, but they will be serialized and deserialized (including a CPU-sync and device-to-host copy in the case of non-CPU tensors), and in almost every case other than debugging or troubleshooting code, it would be worth the trouble to refactor the code to use non-object collectives instead.\
\
**Unexpected tensor devices** - If you still want to send tensors via object collectives, there is another aspect specific to cuda (and possibly other accelerators) tensors. If you pickle a tensor that is currently on `cuda:3`, and then unpickle it, you will get another tensor on `cuda:3` _regardless of which process you are on, or which CUDA device is the ‘default’ device for that process_. With regular tensor collective APIs, ‘output tensors’ will always be on the same, local device, which is generally what you’d expect.\
\
Unpickling a tensor will implicitly activate a CUDA context if it is the first time a GPU is used by the process, which can waste significant amounts of GPU memory. This issue can be avoided by moving tensors to CPU before passing them as inputs to an object collective.\
\
Third-party backends[#](https://docs.pytorch.org/docs/2.15/distributed.html#third-party-backends "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------\
\
Besides the builtin GLOO/MPI/NCCL backends, PyTorch distributed supports third-party backends through a run-time register mechanism. For references on how to develop a third-party backend through C++ Extension, please refer to [Tutorials - Custom C++ and CUDA Extensions](https://pytorch.org/tutorials/advanced/cpp_extension.html)\
 and `test/cpp_extensions/cpp_c10d_extension.cpp`. The capability of third-party backends are decided by their own implementations.\
\
The new backend derives from `c10d::ProcessGroup` and registers the backend name and the instantiating interface through [`torch.distributed.Backend.register_backend()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Backend.register_backend "torch.distributed.Backend.register_backend")\
 when imported.\
\
When manually importing this backend and invoking [`torch.distributed.init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")\
 with the corresponding backend name, the `torch.distributed` package runs on the new backend.\
\
Warning\
\
The support of third-party backend is experimental and subject to change.\
\
TorchComms backend[#](https://docs.pytorch.org/docs/2.15/distributed.html#torchcomms-backend "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------\
\
[TorchComms](https://github.com/meta-pytorch/torchcomms)\
 is an optional communication backend for `torch.distributed`. When enabled, it overrides the normal backend instantiation in [`init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")\
 so that all process groups are created through TorchComms instead of the built-in `ProcessGroup` implementations.\
\
Note\
\
TorchComms is experimental and must be installed separately. The `torchcomms` package must be importable for the flags below to take effect.\
\
### Enabling TorchComms[#](https://docs.pytorch.org/docs/2.15/distributed.html#enabling-torchcomms "Link to this heading")\
\
Set the `TORCH_DISTRIBUTED_USE_TORCHCOMMS` environment variable before calling [`init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")\
:\
\
export TORCH\_DISTRIBUTED\_USE\_TORCHCOMMS\=1\
\
Copy to clipboard\
\
Or set the config flag programmatically:\
\
import torch.distributed.config as dist\_config\
\
dist\_config.use\_torchcomms \= True\
\
Copy to clipboard\
\
The `backend` argument to [`init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")\
 (e.g. `"nccl"`, `"gloo"`) is still respected – it is forwarded to TorchComms, which selects the corresponding vendor plugin. No other application code changes are required; all `torch.distributed` collective APIs continue to work as before.\
\
### Behavior when enabled[#](https://docs.pytorch.org/docs/2.15/distributed.html#behavior-when-enabled "Link to this heading")\
\
When TorchComms is enabled, [`init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")\
 changes its backend instantiation path for every device/backend pair in the process group (except the `fake` backend, which is always handled natively):\
\
1.  A TorchComms communicator is created via `torchcomms.new_comm()` using the requested backend string and device.\
    \
2.  The communicator is wrapped in a `_BackendWrapper` that implements the `c10d::Backend` C++ interface, making it a drop-in replacement for the native `ProcessGroup` backends.\
    \
3.  A `FlightRecorderHook` is automatically registered on the communicator. The hook respects the `TORCH_FR_BUFFER_SIZE` and `TORCH_NCCL_TRACE_BUFFER_SIZE` environment variables for configuring the trace buffer size.\
    \
4.  `destroy_process_group()` calls `finalize()` on TorchComms communicators during cleanup.\
    \
5.  [`split_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.split_group "torch.distributed.split_group")\
     creates sub-communicators through TorchComms’ native splitting rather than constructing a new process group from scratch.\
    \
\
### Eager initialization[#](https://docs.pytorch.org/docs/2.15/distributed.html#eager-initialization "Link to this heading")\
\
TorchComms communicators are eagerly initialized during [`init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")\
 and only support a single backend device per group. The `device_id` argument must be specified at initialization time:\
\
dist.init\_process\_group(backend\="nccl", device\_id\=torch.device("cuda", local\_rank))\
\
Copy to clipboard\
\
### Point-to-point operation concurrency[#](https://docs.pytorch.org/docs/2.15/distributed.html#point-to-point-operation-concurrency "Link to this heading")\
\
Each TorchComms process group maps 1:1 to a single underlying communicator. Point-to-point operations (`send`/`recv`) issued on the same group and stream are **not guaranteed to run concurrently**. Code that relies on concurrent point-to-point operations must either:\
\
*   Use the batched P2P APIs ([`batch_isend_irecv()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.batch_isend_irecv "torch.distributed.batch_isend_irecv")\
    ), or\
    \
*   Issue the operations on separate groups or communicators.\
    \
\
Launch utility[#](https://docs.pytorch.org/docs/2.15/distributed.html#launch-utility "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------\
\
The `torch.distributed` package also provides a launch utility in `torch.distributed.launch`. This helper utility can be used to launch multiple processes per node for distributed training.\
\
Module `torch.distributed.launch`.\
\
`torch.distributed.launch` is a module that spawns up multiple distributed training processes on each of the training nodes.\
\
Warning\
\
This module is going to be deprecated in favor of [torchrun](https://docs.pytorch.org/docs/2.15/elastic/run.html#launcher-api)\
.\
\
The utility can be used for single-node distributed training, in which one or more processes per node will be spawned. The utility can be used for either CPU training or GPU training. If the utility is used for GPU training, each distributed process will be operating on a single GPU. This can achieve well-improved single-node training performance. It can also be used in multi-node distributed training, by spawning up multiple processes on each node for well-improved multi-node distributed training performance as well. This will especially be beneficial for systems with multiple Infiniband interfaces that have direct-GPU support, since all of them can be utilized for aggregated communication bandwidth.\
\
In both cases of single-node distributed training or multi-node distributed training, this utility will launch the given number of processes per node (`--nproc-per-node`). If used for GPU training, this number needs to be less or equal to the number of GPUs on the current system (`nproc_per_node`), and each process will be operating on a single GPU from _GPU 0 to GPU (nproc\_per\_node - 1)_.\
\
**How to use this module:**\
\
1.  Single-Node multi-process distributed training\
    \
\
python \-m torch.distributed.launch \--nproc\-per\-node\=NUM\_GPUS\_YOU\_HAVE\
           YOUR\_TRAINING\_SCRIPT.py (\--arg1 \--arg2 \--arg3 and all other\
           arguments of your training script)\
\
Copy to clipboard\
\
2.  Multi-Node multi-process distributed training: (e.g. two nodes)\
    \
\
Node 1: _(IP: 192.168.1.1, and has a free port: 1234)_\
\
python \-m torch.distributed.launch \--nproc\-per\-node\=NUM\_GPUS\_YOU\_HAVE\
           \--nnodes\=2 \--node\-rank\=0 \--master\-addr\="192.168.1.1"\
           \--master\-port\=1234 YOUR\_TRAINING\_SCRIPT.py (\--arg1 \--arg2 \--arg3\
           and all other arguments of your training script)\
\
Copy to clipboard\
\
Node 2:\
\
python \-m torch.distributed.launch \--nproc\-per\-node\=NUM\_GPUS\_YOU\_HAVE\
           \--nnodes\=2 \--node\-rank\=1 \--master\-addr\="192.168.1.1"\
           \--master\-port\=1234 YOUR\_TRAINING\_SCRIPT.py (\--arg1 \--arg2 \--arg3\
           and all other arguments of your training script)\
\
Copy to clipboard\
\
3.  To look up what optional arguments this module offers:\
    \
\
python \-m torch.distributed.launch \--help\
\
Copy to clipboard\
\
**Important Notices:**\
\
1\. This utility and multi-process distributed (single-node or multi-node) GPU training currently only achieves the best performance using the NCCL distributed backend. Thus NCCL backend is the recommended backend to use for GPU training.\
\
2\. In your training program, you must parse the command-line argument: `--local-rank=LOCAL_PROCESS_RANK`, which will be provided by this module. If your training program uses GPUs, you should ensure that your code only runs on the GPU device of LOCAL\_PROCESS\_RANK. This can be done by:\
\
Parsing the local\_rank argument\
\
\>>> import argparse\
\>>> parser \= argparse.ArgumentParser()\
\>>> parser.add\_argument("--local-rank", "--local\_rank", type\=int)\
\>>> args \= parser.parse\_args()\
\
Copy to clipboard\
\
Set your device to local rank using either\
\
\>>> torch.cuda.set\_device(args.local\_rank)  \# before your code runs\
\
Copy to clipboard\
\
or\
\
\>>> with torch.cuda.device(args.local\_rank):\
\>>>    \# your code to run\
\>>>    ...\
\
Copy to clipboard\
\
Changed in version 2.0.0: The launcher will pass the `--local-rank=<rank>` argument to your script. From PyTorch 2.0.0 onwards, the dashed `--local-rank` is preferred over the previously used underscored `--local_rank`.\
\
For backward compatibility, it may be necessary for users to handle both cases in their argument parsing code. This means including both `"--local-rank"` and `"--local_rank"` in the argument parser. If only `"--local_rank"` is provided, the launcher will trigger an error: “error: unrecognized arguments: –local-rank=<rank>”. For training code that only supports PyTorch 2.0.0+, including `"--local-rank"` should be sufficient.\
\
3\. In your training program, you are supposed to call the following function at the beginning to start the distributed backend. It is strongly recommended that `init_method=env://`. Other init methods (e.g. `tcp://`) may work, but `env://` is the one that is officially supported by this module.\
\
\>>> torch.distributed.init\_process\_group(backend\='YOUR BACKEND',\
\>>>                                      init\_method\='env://')\
\
Copy to clipboard\
\
4\. In your training program, you can either use regular distributed functions or use [`torch.nn.parallel.DistributedDataParallel()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")\
 module. If your training program uses GPUs for training and you would like to use [`torch.nn.parallel.DistributedDataParallel()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")\
 module, here is how to configure it.\
\
\>>> model \= torch.nn.parallel.DistributedDataParallel(model,\
\>>>                                                   device\_ids\=\[args.local\_rank\],\
\>>>                                                   output\_device\=args.local\_rank)\
\
Copy to clipboard\
\
Please ensure that `device_ids` argument is set to be the only GPU device id that your code will be operating on. This is generally the local rank of the process. In other words, the `device_ids` needs to be `[args.local_rank]`, and `output_device` needs to be `args.local_rank` in order to use this utility\
\
5\. Another way to pass `local_rank` to the subprocesses via environment variable `LOCAL_RANK`. This behavior is enabled when you launch the script with `--use-env=True`. You must adjust the subprocess example above to replace `args.local_rank` with `os.environ['LOCAL_RANK']`; the launcher will not pass `--local-rank` when you specify this flag.\
\
Warning\
\
`local_rank` is NOT globally unique: it is only unique per process on a machine. Thus, don’t use it to decide if you should, e.g., write to a networked filesystem. See [pytorch/pytorch#12042](https://github.com/pytorch/pytorch/issues/12042)\
 for an example of how things can go wrong if you don’t do this correctly.\
\
torch.distributed.launch.launch(_args_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/launch.py#L183)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.launch.launch "Link to this definition")\
\
torch.distributed.launch.main(_args\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/launch.py#L191)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.launch.main "Link to this definition")\
\
torch.distributed.launch.parse\_args(_args_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/launch.py#L168)\
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.launch.parse_args "Link to this definition")\
\
Spawn utility[#](https://docs.pytorch.org/docs/2.15/distributed.html#spawn-utility "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------\
\
The [Multiprocessing package - torch.multiprocessing](https://docs.pytorch.org/docs/2.15/multiprocessing.html#multiprocessing-doc)\
 package also provides a `spawn` function in [`torch.multiprocessing.spawn()`](https://docs.pytorch.org/docs/2.15/multiprocessing.html#module-torch.multiprocessing.spawn "torch.multiprocessing.spawn")\
. This helper function can be used to spawn multiple processes. It works by passing in the function that you want to run and spawns N processes to run it. This can be used for multiprocess distributed training as well.\
\
For references on how to use it, please refer to [PyTorch example - ImageNet implementation](https://github.com/pytorch/examples/tree/master/imagenet)\
\
Note that this function requires Python 3.4 or higher.\
\
Debugging `torch.distributed` applications[#](https://docs.pytorch.org/docs/2.15/distributed.html#debugging-torch-distributed-applications "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
Debugging distributed applications can be challenging due to hard to understand hangs, crashes, or inconsistent behavior across ranks. `torch.distributed` provides a suite of tools to help debug training applications in a self-serve fashion:\
\
### Python Breakpoint[#](https://docs.pytorch.org/docs/2.15/distributed.html#python-breakpoint "Link to this heading")\
\
It is extremely convenient to use python’s debugger in a distributed environment, but because it does not work out of the box many people do not use it at all. PyTorch offers a customized wrapper around pdb that streamlines the process.\
\
`torch.distributed.breakpoint` makes this process easy. Internally, it customizes `pdb`’s breakpoint behavior in two ways but otherwise behaves as normal `pdb`.\
\
1.  Attaches the debugger only on one rank (specified by the user).\
    \
2.  Ensures all other ranks stop, by using a `torch.distributed.barrier()` that will release once the debugged rank issues a `continue`\
    \
3.  Reroutes stdin from the child process such that it connects to your terminal.\
    \
\
To use it, simply issue `torch.distributed.breakpoint(rank)` on all ranks, using the same value for `rank` in each case.\
\
### Monitored Barrier[#](https://docs.pytorch.org/docs/2.15/distributed.html#monitored-barrier "Link to this heading")\
\
As of v1.10, [`torch.distributed.monitored_barrier()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.monitored_barrier "torch.distributed.monitored_barrier")\
 exists as an alternative to [`torch.distributed.barrier()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.barrier "torch.distributed.barrier")\
 which fails with helpful information about which rank may be faulty when crashing, i.e. not all ranks calling into [`torch.distributed.monitored_barrier()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.monitored_barrier "torch.distributed.monitored_barrier")\
 within the provided timeout. [`torch.distributed.monitored_barrier()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.monitored_barrier "torch.distributed.monitored_barrier")\
 implements a host-side barrier using `send`/`recv` communication primitives in a process similar to acknowledgements, allowing rank 0 to report which rank(s) failed to acknowledge the barrier in time. As an example, consider the following function where rank 1 fails to call into [`torch.distributed.monitored_barrier()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.monitored_barrier "torch.distributed.monitored_barrier")\
 (in practice this could be due to an application bug or hang in a previous collective):\
\
import os\
from datetime import timedelta\
\
import torch\
import torch.distributed as dist\
import torch.multiprocessing as mp\
\
def worker(rank):\
    dist.init\_process\_group("nccl", rank\=rank, world\_size\=2)\
    \# monitored barrier requires gloo process group to perform host-side sync.\
    group\_gloo \= dist.new\_group(backend\="gloo")\
    if rank not in \[1\]:\
        dist.monitored\_barrier(group\=group\_gloo, timeout\=timedelta(seconds\=2))\
\
if \_\_name\_\_ \== "\_\_main\_\_":\
    os.environ\["MASTER\_ADDR"\] \= "localhost"\
    os.environ\["MASTER\_PORT"\] \= "29501"\
    mp.spawn(worker, nprocs\=2, args\=())\
\
Copy to clipboard\
\
The following error message is produced on rank 0, allowing the user to determine which rank(s) may be faulty and investigate further:\
\
RuntimeError: Rank 1 failed to pass monitoredBarrier in 2000 ms\
 Original exception:\
\[gloo/transport/tcp/pair.cc:598\] Connection closed by peer \[2401:db00:eef0:1100:3560:0:1c05:25d\]:8594\
\
Copy to clipboard\
\
### `TORCH_DISTRIBUTED_DEBUG`[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch-distributed-debug "Link to this heading")\
\
With `TORCH_CPP_LOG_LEVEL=INFO`, the environment variable `TORCH_DISTRIBUTED_DEBUG` can be used to trigger additional useful logging and collective synchronization checks to ensure all ranks are synchronized appropriately. `TORCH_DISTRIBUTED_DEBUG` can be set to either `OFF` (default), `INFO`, or `DETAIL` depending on the debugging level required. Please note that the most verbose option, `DETAIL` may impact the application performance and thus should only be used when debugging issues.\
\
Setting `TORCH_DISTRIBUTED_DEBUG=INFO` will result in additional debug logging when models trained with [`torch.nn.parallel.DistributedDataParallel()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")\
 are initialized, and `TORCH_DISTRIBUTED_DEBUG=DETAIL` will additionally log runtime performance statistics a select number of iterations. These runtime statistics include data such as forward time, backward time, gradient communication time, etc. As an example, given the following application:\
\
import os\
\
import torch\
import torch.distributed as dist\
import torch.multiprocessing as mp\
\
class TwoLinLayerNet(torch.nn.Module):\
    def \_\_init\_\_(self):\
        super().\_\_init\_\_()\
        self.a \= torch.nn.Linear(10, 10, bias\=False)\
        self.b \= torch.nn.Linear(10, 1, bias\=False)\
\
    def forward(self, x):\
        a \= self.a(x)\
        b \= self.b(x)\
        return (a, b)\
\
def worker(rank):\
    dist.init\_process\_group("nccl", rank\=rank, world\_size\=2)\
    torch.cuda.set\_device(rank)\
    print("init model")\
    model \= TwoLinLayerNet().cuda()\
    print("init ddp")\
    ddp\_model \= torch.nn.parallel.DistributedDataParallel(model, device\_ids\=\[rank\])\
\
    inp \= torch.randn(10, 10).cuda()\
    print("train")\
\
    for \_ in range(20):\
        output \= ddp\_model(inp)\
        loss \= output\[0\] + output\[1\]\
        loss.sum().backward()\
\
if \_\_name\_\_ \== "\_\_main\_\_":\
    os.environ\["MASTER\_ADDR"\] \= "localhost"\
    os.environ\["MASTER\_PORT"\] \= "29501"\
    os.environ\["TORCH\_CPP\_LOG\_LEVEL"\]\="INFO"\
    os.environ\[\
        "TORCH\_DISTRIBUTED\_DEBUG"\
    \] \= "DETAIL"  \# set to DETAIL for runtime logging.\
    mp.spawn(worker, nprocs\=2, args\=())\
\
Copy to clipboard\
\
The following logs are rendered at initialization time:\
\
I0607 16:10:35.739390 515217 logger.cpp:173\] \[Rank 0\]: DDP Initialized with:
broadcast\_buffers: 1
bucket\_cap\_bytes: 26214400
find\_unused\_parameters: 0
gradient\_as\_bucket\_view: 0
is\_multi\_device\_module: 0
iteration: 0
num\_parameter\_tensors: 2
output\_device: 0
rank: 0
total\_parameter\_size\_bytes: 440
world\_size: 2
backend\_name: nccl
bucket\_sizes: 440
cuda\_visible\_devices: N/A
device\_ids: 0
dtypes: float
master\_addr: localhost
master\_port: 29501
module\_name: TwoLinLayerNet
nccl\_async\_error\_handling: N/A
nccl\_blocking\_wait: N/A
nccl\_debug: WARN
nccl\_ib\_timeout: N/A
nccl\_nthreads: N/A
nccl\_socket\_ifname: N/A
torch\_distributed\_debug: INFO

Copy to clipboard

The following logs are rendered during runtime (when `TORCH_DISTRIBUTED_DEBUG=DETAIL` is set):

I0607 16:18:58.085681 544067 logger.cpp:344\] \[Rank 1 / 2\] Training TwoLinLayerNet unused\_parameter\_size\=0
 Avg forward compute time: 40838608
 Avg backward compute time: 5983335
Avg backward comm. time: 4326421
 Avg backward comm/comp overlap time: 4207652
I0607 16:18:58.085693 544066 logger.cpp:344\] \[Rank 0 / 2\] Training TwoLinLayerNet unused\_parameter\_size\=0
 Avg forward compute time: 42850427
 Avg backward compute time: 3885553
Avg backward comm. time: 2357981
 Avg backward comm/comp overlap time: 2234674

Copy to clipboard

In addition, `TORCH_DISTRIBUTED_DEBUG=INFO` enhances crash logging in [`torch.nn.parallel.DistributedDataParallel()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")
 due to unused parameters in the model. Currently, `find_unused_parameters=True` must be passed into [`torch.nn.parallel.DistributedDataParallel()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")
 initialization if there are parameters that may be unused in the forward pass, and as of v1.10, all model outputs are required to be used in loss computation as [`torch.nn.parallel.DistributedDataParallel()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")
 does not support unused parameters in the backwards pass. These constraints are challenging especially for larger models, thus when crashing with an error, [`torch.nn.parallel.DistributedDataParallel()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")
 will log the fully qualified name of all parameters that went unused. For example, in the above application, if we modify `loss` to be instead computed as `loss = output[1]`, then `TwoLinLayerNet.a` does not receive a gradient in the backwards pass, and thus results in `DDP` failing. On a crash, the user is passed information about parameters which went unused, which may be challenging to manually find for large models:

RuntimeError: Expected to have finished reduction in the prior iteration before starting a new one. This error indicates that your module has parameters that were not used in producing loss. You can enable unused parameter detection by passing
 the keyword argument \`find\_unused\_parameters=True\` to \`torch.nn.parallel.DistributedDataParallel\`, and by
making sure all \`forward\` function outputs participate in calculating loss.
If you already have done the above, then the distributed data parallel module wasn't able to locate the output tensors in the return value of your module's \`forward\` function. Please include the loss function and the structure of the return va
lue of \`forward\` of your module when reporting this issue (e.g. list, dict, iterable).
Parameters which did not receive grad for rank 0: a.weight
Parameter indices which did not receive grad for rank 0: 0

Copy to clipboard

Setting `TORCH_DISTRIBUTED_DEBUG=DETAIL` will trigger additional consistency and synchronization checks on every collective call issued by the user either directly or indirectly (such as DDP `allreduce`). This is done by creating a wrapper process group that wraps all process groups returned by [`torch.distributed.init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")
 and [`torch.distributed.new_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.new_group "torch.distributed.new_group")
 APIs. As a result, these APIs will return a wrapper process group that can be used exactly like a regular process group, but performs consistency checks before dispatching the collective to an underlying process group. Currently, these checks include a [`torch.distributed.monitored_barrier()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.monitored_barrier "torch.distributed.monitored_barrier")
, which ensures all ranks complete their outstanding collective calls and reports ranks which are stuck. Next, the collective itself is checked for consistency by ensuring all collective functions match and are called with consistent tensor shapes. If this is not the case, a detailed error report is included when the application crashes, rather than a hang or uninformative error message. As an example, consider the following function which has mismatched input shapes into [`torch.distributed.all_reduce()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.all_reduce "torch.distributed.all_reduce")
:

import torch
import torch.distributed as dist
import torch.multiprocessing as mp

def worker(rank):
    dist.init\_process\_group("nccl", rank\=rank, world\_size\=2)
    torch.cuda.set\_device(rank)
    tensor \= torch.randn(10 if rank \== 0 else 20).cuda()
    dist.all\_reduce(tensor)
    torch.cuda.synchronize(device\=rank)

if \_\_name\_\_ \== "\_\_main\_\_":
    os.environ\["MASTER\_ADDR"\] \= "localhost"
    os.environ\["MASTER\_PORT"\] \= "29501"
    os.environ\["TORCH\_CPP\_LOG\_LEVEL"\]\="INFO"
    os.environ\["TORCH\_DISTRIBUTED\_DEBUG"\] \= "DETAIL"
    mp.spawn(worker, nprocs\=2, args\=())

Copy to clipboard

With the `NCCL` backend, such an application would likely result in a hang which can be challenging to root-cause in nontrivial scenarios. If the user enables `TORCH_DISTRIBUTED_DEBUG=DETAIL` and reruns the application, the following error message reveals the root cause:

work \= default\_pg.allreduce(\[tensor\], opts)
RuntimeError: Error when verifying shape tensors for collective ALLREDUCE on rank 0. This likely indicates that input shapes into the collective are mismatched across ranks. Got shapes:  10
\[ torch.LongTensor{1} \]

Copy to clipboard

Note

For fine-grained control of the debug level during runtime the functions `torch.distributed.set_debug_level()`, `torch.distributed.set_debug_level_from_env()`, and [`torch.distributed.get_debug_level()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.get_debug_level "torch.distributed.get_debug_level")
 can also be used.

In addition, `TORCH_DISTRIBUTED_DEBUG=DETAIL` can be used in conjunction with `TORCH_SHOW_CPP_STACKTRACES=1` to log the entire callstack when a collective desynchronization is detected. These collective desynchronization checks will work for all applications that use `c10d` collective calls backed by process groups created with the [`torch.distributed.init_process_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.init_process_group "torch.distributed.init_process_group")
 and [`torch.distributed.new_group()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.new_group "torch.distributed.new_group")
 APIs.

### torch.distributed.debug HTTP Server[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch-distributed-debug-http-server "Link to this heading")

The `torch.distributed.debug` module provides an HTTP server that can be used to debug distributed applications. It lets you inspect live distributed training jobs across all ranks from a single browser tab — collecting stack traces, flight-recorder events, NCCL traces, profiler captures, wait-counter metrics, and TCPStore contents without restarting or redeploying your job.

Warning

The debug server is intended for **trusted network environments only**. It is not designed to be secure and must not be exposed to the public internet.

Note

This is an experimental feature and may change at any time.

torch.distributed.debug.start\_debug\_server(_port\=25999_, _worker\_port\=0_, _start\_method\=None_, _dump\_dir\=None_, _dump\_interval\=60.0_, _enabled\_dumps\=None_, _handlers\=None_, _fetch\_timeout\=60.0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/debug/__init__.py#L27)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.debug.start_debug_server "Link to this definition")

Start the debug server stack on all workers. The frontend debug server is only started on rank0 while the per rank worker servers are started on all ranks.

This server provides an HTTP frontend that allows for debugging slow and deadlocked distributed jobs across all ranks simultaneously. This collects data such as stack traces, FlightRecorder events, and performance profiles.

This depends on dependencies which are not installed by default.

Dependencies: - Jinja2 - aiohttp

WARNING: This is intended to only be used in trusted network environments. The debug server is not designed to be secure and should not be exposed to the public internet. See SECURITY.md for more details.

WARNING: This is an experimental feature and may change at any time.

Parameters:

*   **port** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The port to start the frontend debug server on.
    
*   **worker\_port** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The port to start the worker server on. Defaults to 0, which will cause the worker server to bind to an ephemeral port.
    
*   **start\_method** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _None_) – The multiprocessing start method to use for the frontend server process. One of “fork”, “spawn”, or “forkserver”. If None, uses the default start method. Using “spawn” is recommended when using CUDA or when fork safety is a concern.
    
*   **dump\_dir** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _None_) – Directory to write periodic debug dumps to. If None, periodic dumping is disabled.
    
*   **dump\_interval** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – Seconds between periodic dumps. Defaults to 60.
    
*   **enabled\_dumps** ([_set_](https://docs.python.org/3/builtins/stdtypes.html#set "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ _None_) – Set of handler dump filenames to enable (e.g. {“stacks”, “fr\_trace”, “tcpstore”}). If None, all handlers that implement dump() are enabled.
    
*   **handlers** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[__DebugHandler__\]_ _|_ _None_) – List of debug handlers to use. If None, uses the default handlers. See torch.distributed.debug.\_handlers for the default handlers.
    
*   **fetch\_timeout** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – Timeout in seconds for fetching data from individual workers. Defaults to 60. Workers that don’t respond within this time will be reported as unavailable.
    

torch.distributed.debug.stop\_debug\_server()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/debug/__init__.py#L131)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.debug.stop_debug_server "Link to this definition")

Shutdown the debug server and stop the frontend debug server process.

#### Architecture Overview[#](https://docs.pytorch.org/docs/2.15/distributed.html#architecture-overview "Link to this heading")

The debug server has a **two-tier** architecture:

┌───────────────────────────────────┐
│     Frontend Server (rank 0)      │
│  HTTP server on a fixed port      │
│  Renders HTML dashboards          │
│  Fans out requests to all ranks   │
└──────────┬────────────────────────┘
           │  HTTP POST /handler/<endpoint>?<args>
           ▼
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ WorkerServer (0) │  │ WorkerServer (1) │  │ WorkerServer (N) │
│ Per-rank C++     │  │ Per-rank C++     │  │ Per-rank C++     │
│ HTTP server      │  │ HTTP server      │  │ HTTP server      │
│ Exposes handlers │  │ Exposes handlers │  │ Exposes handlers │
└──────────────────┘  └──────────────────┘  └──────────────────┘

Copy to clipboard

*   **WorkerServer** (`_WorkerServer`): A lightweight C++ HTTP server started on every rank. It serves _handler_ endpoints registered via `_register_handler()` (Python) or `RegisterHandler` (C++). Each handler receives a `_Request` and writes to a `_Response`.
    
*   **FrontendServer**: A Python HTTP server that starts only on **rank 0**. It aggregates data from all worker servers and renders HTML dashboards using Jinja2 templates.
    
*   **TCPStore**: Workers publish their addresses (hostname + port) to the existing `TCPStore` so the frontend knows where to find each rank.
    

#### Quick Start[#](https://docs.pytorch.org/docs/2.15/distributed.html#quick-start "Link to this heading")

**Prerequisites**

Install required dependencies (not bundled with PyTorch by default):

pip install jinja2 aiohttp tabulate

Copy to clipboard

`aiohttp` is optional — the server falls back to `requests` + thread pool if `aiohttp` is unavailable.

**Basic Usage**

Call `start_debug_server()` **after** `dist.init_process_group()` on every rank:

import torch
import torch.distributed as dist
from torch.distributed.debug import start\_debug\_server, stop\_debug\_server

dist.init\_process\_group("nccl")

\# Start the debug server on all ranks.
\# The frontend (browser UI) is served on rank 0 at port 25999.
start\_debug\_server(port\=25999)

\# ... your training loop ...

stop\_debug\_server()
dist.destroy\_process\_group()

Copy to clipboard

Then open `http://<rank0-hostname>:25999` in a browser.

**Minimal torchrun Example**

\# train.py
import torch
import torch.distributed as dist
from torch.distributed.debug import start\_debug\_server

def main():
    dist.init\_process\_group("nccl")
    start\_debug\_server()

    rank \= dist.get\_rank()
    device \= torch.device(f"cuda:{rank}")
    model \= torch.nn.Linear(10, 10).to(device)
    model \= torch.nn.parallel.DistributedDataParallel(model, device\_ids\=\[rank\])

    for \_ in range(1000):
        x \= torch.randn(32, 10, device\=device)
        loss \= model(x).sum()
        loss.backward()

    dist.destroy\_process\_group()

if \_\_name\_\_ \== "\_\_main\_\_":
    main()

Copy to clipboard

torchrun \--nproc-per-node\=2 train.py
\# Open http://localhost:25999

Copy to clipboard

For an end-to-end NCCL2 failure example, see [`verify_nccl2_flight_recorder.py`](https://docs.pytorch.org/docs/2.15/_downloads/22442dd407dcbff9b1018f1abe54a68e/verify_nccl2_flight_recorder.py)
. The example deliberately hangs an NCCL2 collective and verifies that the c10d health check causes the debug server to write a Flight Recorder dump for every rank. Run it on a host with at least two GPUs:

torchrun \--standalone \--nproc-per-node\=2 \\
  torch/distributed/examples/verify\_nccl2\_flight\_recorder.py

Copy to clipboard

#### Configuration Reference[#](https://docs.pytorch.org/docs/2.15/distributed.html#configuration-reference "Link to this heading")

`start_debug_server()` accepts the following parameters:

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `port` | `int` | `25999` | Port for the frontend HTTP server (rank 0 only). |
| `worker_port` | `int` | `0` | Port for the per-rank worker server. `0` = ephemeral. |
| `start_method` | `str \| None` | `None` | Multiprocessing start method (`"fork"`, `"spawn"`, `"forkserver"`). `"spawn"` recommended with CUDA. |
| `dump_dir` | `str \| None` | `None` | Directory for periodic debug dumps. `None` disables dumping. |
| `dump_interval` | `float` | `60.0` | Seconds between periodic dumps. |
| `enabled_dumps` | `set[str] \| None` | `None` | Handler dump filenames to enable (e.g. `{"stacks", "fr_trace"}`). `None` = default set. |
| `handlers` | `list[DebugHandler] \| None` | `None` | Custom handler list. `None` = all default handlers. |
| `fetch_timeout` | `float` | `60.0` | Timeout (seconds) when fetching data from workers. |

**Environment Variables**

The debug server reads these standard environment variables (set automatically by `torchrun` / TorchElastic):

| Variable | Description |
| --- | --- |
| `RANK` | Current process rank. |
| `WORLD_SIZE` | Total number of ranks. |
| `MASTER_ADDR` | Address of the TCPStore master. |
| `MASTER_PORT` | Port of the TCPStore master. |

#### Frontend Endpoints (Browser UI)[#](https://docs.pytorch.org/docs/2.15/distributed.html#frontend-endpoints-browser-ui "Link to this heading")

The frontend server (rank 0) exposes the following endpoints. Each one aggregates data from **all** worker ranks and renders an HTML page.

**Home** `/` The landing page with navigation links to all other endpoints.

**Python Stack Traces** `/stacks` Calls `dump_traceback` on every worker to collect Python stack traces using `faulthandler.dump_traceback()`. Useful for diagnosing hangs or deadlocks without attaching a debugger. Displays a `<pre>` block per rank showing the Python call stack of every thread.

**py-spy Stack Traces** `/pyspy_dump` Calls `pyspy_dump` on every worker. Uses `py-spy <https://github.com/benfred/py-spy>`\_ to dump both Python and optionally native (C/C++) stack traces. Accepts query parameters `native=1` (include native frames) and `subprocesses=1` (include subprocesses). `nonblocking=1` is added automatically.

Note

`py-spy` must be installed and the process must have `SYS_PTRACE` capability.

**FlightRecorder CPU** `/fr_trace` Fetches CPU-side flight recorder data from `fr_trace_json` on all workers, parses it into structured tables (Groups, Memberships, Collectives, NCCL Calls), and renders them as HTML tables.

**FlightRecorder CPU JSON** `/fr_trace_json` Same data as `/fr_trace` but rendered as raw formatted JSON per rank.

**FlightRecorder NCCL** `/fr_trace_nccl` Fetches NCCL-side flight recorder data from `dump_nccl_trace_json` (with `onlyactive=true`) on all workers and renders structured HTML tables.

**FlightRecorder NCCL JSON** `/fr_trace_nccl_json` Same data as `/fr_trace_nccl` but rendered as raw formatted JSON per rank.

**TorchComms FlightRecorder** `/torchcomms_fr_trace` Fetches TorchComms flight recorder data from `torchcomms_fr_trace_json` (with `onlyactive=true`) on all workers. Renders the same structured tables as the FlightRecorder views (Groups, Memberships, Collectives, NCCL Calls).

**TorchComms FlightRecorder JSON** `/torchcomms_fr_trace_json` Same data as `/torchcomms_fr_trace` but rendered as raw formatted JSON.

**c10d Health Check** `/c10d_health_check` Fetches the c10d health state from every rank. When any rank reports an unhealthy backend, the server requests a Flight Recorder dump for that backend from every worker.

**torch.profiler** `/profile` Triggers `torch.profiler.profile()` on every worker for a configurable duration, then returns the Chrome trace JSON. The frontend page provides a **View** button per rank that opens the trace directly in `Perfetto UI <https://ui.perfetto.dev/>`\_ (no download required). Accepts query parameter `duration` (profiling duration in seconds, default `1`, range 1–60).

**Wait Counters** `/wait_counters` Fetches `wait_counter_values` from all workers and renders the JSON data. Wait counters track time spent waiting in collective operations, useful for identifying stragglers and load imbalance.

**TCPStore Keys** `/tcpstore` Connects to the TCPStore and lists all keys with their values (truncated to 100 characters). Useful for inspecting the state of the distributed key-value store.

#### Worker-Level Endpoints (Per-Rank HTTP API)[#](https://docs.pytorch.org/docs/2.15/distributed.html#worker-level-endpoints-per-rank-http-api "Link to this heading")

Each `WorkerServer` instance exposes handler endpoints at:

POST http://<worker-host>:<worker-port>/handler/<handler\_name>?<params>

Copy to clipboard

The built-in handlers are:

**`ping`** — Simple health check. Returns `"pong"` (text/plain, 200).

curl \-X POST \\
  http://worker-host:port/handler/ping  \# @lint-ignore

Copy to clipboard

**`dump_traceback`** — Python stack traces of all threads (text/plain). Uses `faulthandler.dump_traceback()` to capture every thread’s Python stack. Requires the GIL.

curl \-X POST \\
  http://worker-host:port/handler/dump\_traceback  \# @lint-ignore

Copy to clipboard

**`pyspy_dump`** — py-spy stack dump output (text/plain). Runs `py-spy dump --pid <pid>` to capture stack traces without stopping the process. Accepts parameters `native`, `subprocesses`, and `nonblocking`.

curl \-X POST \\
  "http://worker-host:port/handler/pyspy\_dump?nonblocking=1&native=1"  \# @lint-ignore

Copy to clipboard

**`fr_trace_json`** — CPU flight-recorder trace (application/json). Returns the flight-recorder ring buffer contents as JSON, including all recorded collective operations, their metadata, and timing information.

curl \-X POST \\
  http://worker-host:port/handler/fr\_trace\_json  \# @lint-ignore

Copy to clipboard

**`fr_dump_file`** — Starts a Flight Recorder dump for one backend. The `backend` query parameter selects the backend-specific recorder.

curl \-X POST \\
  "http://worker-host:port/handler/fr\_dump\_file?backend=nccl2"  \# @lint-ignore

Copy to clipboard

**`c10d_health_check`** — Returns the process-wide c10d health state and the names of any unhealthy backends (application/json).

curl \-X POST \\
  http://worker-host:port/handler/c10d\_health\_check  \# @lint-ignore

Copy to clipboard

**`dump_nccl_trace_json`** — NCCL flight-recorder trace (application/json). Only available when built with NCCL support. Accepts parameters `includecollectives` (`true`/`false`, default `true`) and `onlyactive` (`true`/`false`, default `false`).

curl \-X POST \\
  "http://worker-host:port/handler/dump\_nccl\_trace\_json?onlyactive=true"  \# @lint-ignore

Copy to clipboard

**`dump_nccl_trace_pickle`** — NCCL trace in pickle format (application/octet-stream). Useful for programmatic analysis. Accepts parameters `includecollectives` (default `true`), `includestacktraces` (default `true`), and `onlyactive` (default `false`).

curl \-X POST \\
  \--output trace.pkl \\
  "http://worker-host:port/handler/dump\_nccl\_trace\_pickle?onlyactive=true"  \# @lint-ignore

Copy to clipboard

**`torchcomms_fr_trace_json`** — TorchComms flight-recorder trace (application/json). Similar to `dump_nccl_trace_json` but for the TorchComms communication layer. Accepts parameter `onlyactive` (`true`/`false`, default `false`).

curl \-X POST \\
  "http://worker-host:port/handler/torchcomms\_fr\_trace\_json?onlyactive=true"  \# @lint-ignore

Copy to clipboard

**`torch_profile`** — Chrome trace JSON (application/json). Runs `torch.profiler.profile()` for the specified duration and returns the Chrome trace format JSON. Requires parameter `duration` (seconds).

curl \-X POST \\
  \--output trace.json \\
  "http://worker-host:port/handler/torch\_profile?duration=5"  \# @lint-ignore
\# Open trace.json in chrome://tracing or https://ui.perfetto.dev

Copy to clipboard

**`wait_counter_values`** — Wait counter values (application/json). Returns a JSON object with wait-counter metrics tracking time spent waiting in distributed collective operations.

curl \-X POST \\
  http://worker-host:port/handler/wait\_counter\_values  \# @lint-ignore

Copy to clipboard

#### Periodic Dumping[#](https://docs.pytorch.org/docs/2.15/distributed.html#periodic-dumping "Link to this heading")

Enable periodic dumping to automatically save debug data to disk at regular intervals. This is useful for post-mortem analysis when a job hangs or crashes.

start\_debug\_server(
    dump\_dir\="/shared/nfs/debug\_dumps",
    dump\_interval\=120.0,  \# dump every 2 minutes
    enabled\_dumps\={"stacks", "fr\_trace", "pyspy\_dump", "wait\_counters", "tcpstore"},
)

Copy to clipboard

Dump files are saved as `<handler_name>_<timestamp>.txt` (e.g., `stacks_20250330_192000.txt`).

Handlers that support dumping:

| Handler | Dump filename | Content |
| --- | --- | --- |
| `StacksHandler` | `stacks` | Python stack traces for all ranks. |
| `PySpyHandler` | `pyspy_dump` | py-spy stack dumps (nonblocking) for all ranks. |
| `FlightRecorderHandler` | `fr_trace` | CPU + NCCL flight-recorder tables. |
| `TorchCommsFlightRecorderHandler` | `torchcomms_fr_trace` | TorchComms flight-recorder tables. |
| `C10dHealthCheckHandler` | `c10d_health_check` | c10d health and backend Flight Recorder dumps. |
| `WaitCountersHandler` | `wait_counters` | Wait counter JSON for all ranks. |
| `TCPStoreHandler` | `tcpstore` | All TCPStore key-value pairs. |

By default (when `enabled_dumps=None`), `"stacks"`, `"fr_trace"`, and `"c10d_health_check"` are enabled.

#### Registering Custom Handlers[#](https://docs.pytorch.org/docs/2.15/distributed.html#registering-custom-handlers "Link to this heading")

You can extend the debug server with custom frontend handlers by subclassing `DebugHandler`:

class DebugHandler(ABC):
    fetch\_timeout: float \= \_DEFAULT\_FETCH\_TIMEOUT

    @abstractmethod
    def routes(self) \-> list\[Route\]: ...

    @abstractmethod
    def nav\_links(self) \-> list\[NavLink\]: ...

    def templates(self) \-> dict\[str, str\]:
        return {}

    def dump(self) \-> str | None:
        return None

    def dump\_filename(self) \-> str:
        return type(self).\_\_name\_\_.lower()

Copy to clipboard

*   `routes()` — URL paths and their request handlers.
    
*   `nav_links()` — links shown in the navigation bar.
    
*   `templates()` — optional Jinja2 templates for HTML rendering.
    
*   `dump()` / `dump_filename()` — optional support for periodic dumping.
    

For a complete example, see `StacksHandler <https://github.com/pytorch/pytorch/blob/main/torch/distributed/debug/_debug_handlers.py>`\_ in `torch/distributed/debug/_debug_handlers.py`.

Pass custom handlers to `start_debug_server`:

from torch.distributed.debug.\_debug\_handlers import default\_handlers

handlers \= default\_handlers() + \[MyCustomHandler()\]
start\_debug\_server(handlers\=handlers)

Copy to clipboard

#### Debug Server Troubleshooting[#](https://docs.pytorch.org/docs/2.15/distributed.html#debug-server-troubleshooting "Link to this heading")

**`AssertionError: debug server already started`** `start_debug_server()` was called twice. Ensure you only call it once per process.

**Workers fail to respond (408/503 errors)**

*   Check that all ranks have started and registered their addresses in TCPStore.
    
*   Increase `fetch_timeout` for large clusters or slow networks.
    
*   Verify network connectivity between rank 0 and all worker hosts.
    

**`ImportError: No module named 'jinja2'`** Install the required dependencies: `pip install jinja2 aiohttp tabulate`

**py-spy returns errors**

*   Ensure `py-spy` is installed: `pip install py-spy`
    
*   The process may need `SYS_PTRACE` capability. In Docker use `docker run --cap-add SYS_PTRACE ...`
    
*   On Linux, you may need to set `echo 0 > /proc/sys/kernel/yama/ptrace_scope`
    

**Perfetto UI popup blocked** Allow popups for the debug server’s origin in your browser settings. The `/profile` page opens Perfetto UI in a new window using `window.open()`.

**Frontend server not reachable**

*   Ensure port `25999` (or your custom port) is not blocked by a firewall.
    
*   The frontend only starts on **rank 0**. Connect to the rank 0 host.
    
*   Check the logs for `Frontend server started on port <port>`.
    

**`spawn` start method required with CUDA** If you see CUDA re-initialization errors, use `start_debug_server(start_method="spawn")` to ensure the frontend server process does not inherit CUDA state from the parent process.

Logging[#](https://docs.pytorch.org/docs/2.15/distributed.html#logging "Link to this heading")

-----------------------------------------------------------------------------------------------

In addition to explicit debugging support via [`torch.distributed.monitored_barrier()`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.monitored_barrier "torch.distributed.monitored_barrier")
 and `TORCH_DISTRIBUTED_DEBUG`, the underlying C++ library of `torch.distributed` also outputs log messages at various levels. These messages can be helpful to understand the execution state of a distributed training job and to troubleshoot problems such as network connection failures. The following matrix shows how the log level can be adjusted via the combination of `TORCH_CPP_LOG_LEVEL` and `TORCH_DISTRIBUTED_DEBUG` environment variables.

| `TORCH_CPP_LOG_LEVEL` | `TORCH_DISTRIBUTED_DEBUG` | Effective Log Level |
| --- | --- | --- |
| `ERROR` | ignored | Error |
| `WARNING` | ignored | Warning |
| `INFO` | ignored | Info |
| `INFO` | `INFO` | Debug |
| `INFO` | `DETAIL` | Trace (a.k.a. All) |

Distributed components raise custom Exception types derived from `RuntimeError`:

*   `torch.distributed.DistError`: This is the base type of all distributed exceptions.
    
*   `torch.distributed.DistBackendError`: This exception is thrown when a backend-specific error occurs. For example, if the `NCCL` backend is used and the user attempts to use a GPU that is not available to the `NCCL` library.
    
*   `torch.distributed.DistNetworkError`: This exception is thrown when networking libraries encounter errors (ex: Connection reset by peer)
    
*   `torch.distributed.DistStoreError`: This exception is thrown when the Store encounters an error (ex: TCPStore timeout)
    

_class_ torch.distributed.DistError[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.DistError "Link to this definition")

Exception raised when an error occurs in the distributed library

_class_ torch.distributed.DistBackendError[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.DistBackendError "Link to this definition")

Exception raised when a backend error occurs in distributed

_class_ torch.distributed.DistNetworkError[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.DistNetworkError "Link to this definition")

Exception raised when a network error occurs in distributed

_class_ torch.distributed.DistStoreError[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.DistStoreError "Link to this definition")

Exception raised when an error occurs in the distributed store

If you are running single node training, it may be convenient to interactively breakpoint your script. We offer a way to conveniently breakpoint a single rank:

torch.distributed.breakpoint(_rank\=0_, _skip\=0_, _timeout\_s\=3600_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/__init__.py#L122)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.breakpoint "Link to this definition")

Set a breakpoint, but only on a single rank. All other ranks will wait for you to be done with the breakpoint before continuing.

Parameters:

*   **rank** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Which rank to break on. Default: `0`
    
*   **skip** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Skip the first `skip` calls to this breakpoint. Default: `0`.
    

Watchdog (Experimental)[#](https://docs.pytorch.org/docs/2.15/distributed.html#watchdog-experimental "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

The `torch.distributed._watchdog` module provides a pure-Python watchdog for detecting hung operations in Python-based distributed backends and related distributed primitives. It monitors both CPU-side hangs (e.g., a stuck rendezvous) and GPU-side hangs (e.g., a kernel that never completes) by running an asyncio event loop on a background daemon thread. By default, timeouts dump all thread stack traces and abort the process.

Warning

This module is experimental and subject to change.

torch.distributed.\_watchdog.shutdown()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_watchdog.py#L392)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._watchdog.shutdown "Link to this definition")

Shut down the watchdog singleton. After this, \_get\_watchdog() creates a fresh instance.

torch.distributed.\_watchdog.stream\_timeout(_timeout_, _callback\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_watchdog.py#L461)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._watchdog.stream_timeout "Link to this definition")

Record a CUDA event and fire callback if the stream hasn’t completed by deadline.

Parameters:

*   **timeout** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _|_ [_timedelta_](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")
    ) – Seconds (float) or timedelta until the callback fires.
    
*   **callback** ([_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
    _\[__\[__\]__,_ _None__\]_ _|_ _None_) – Called on timeout. Defaults to logging stack traces and aborting.
    

Return type:

_\_CancelHandle_

Example:

some\_kernel\_launch()
handle \= stream\_timeout(60.0)
\# ... when the operation completes:
handle.cancel()

Copy to clipboard

torch.distributed.\_watchdog.cpu\_timeout(_timeout_, _callback\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_watchdog.py#L480)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._watchdog.cpu_timeout "Link to this definition")

Schedule callback to fire after timeout unless cancelled.

Parameters:

*   **timeout** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _|_ [_timedelta_](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")
    ) – Seconds (float) or timedelta until the callback fires.
    
*   **callback** ([_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
    _\[__\[__\]__,_ _None__\]_ _|_ _None_) – Called on timeout. Defaults to logging stack traces and aborting.
    

Return type:

_\_CancelHandle_

Example:

handle \= cpu\_timeout(30.0)
blocking\_rendezvous\_call()
handle.cancel()

Copy to clipboard

torch.distributed.\_watchdog.op\_timeout(_timeout_, _callback\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_watchdog.py#L498)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._watchdog.op_timeout "Link to this definition")

CPU timeout guards the block; stream timeout monitors GPU work after exit.

Example:

with op\_timeout(60.0):
    foo()  \# cpu timeout fires if this hangs
torch.cuda.synchronize()  \# stream timeout fires if this hangs

Copy to clipboard

Return type:

[_Generator_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "(in Python v3.15)")
\[None, None, None\]

torch.distributed.collective\_utils.all\_gather\_object\_enforce\_type(_pg_, _object\_list_, _obj_, _type\_checker=<function <lambda>>_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/collective_utils.py#L205)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.collective_utils.all_gather_object_enforce_type "Link to this definition")

Similar to plain all\_gather\_object but with additional type checking AFTER gather is done to ensure basic consistency. If check does not pass, all ranks will fail with exception.

This is generally to prevent conditional logic leading to unexpected messages being received. This is considered fatal code error, but due to logic stacks this might happen implicitly in practice.

The default check does not check sub type (considered different) or covariance (considered same) but users can pass in custom checker if more complicated check is needed.

torch.distributed.launcher.api.launch\_agent(_config_, _entrypoint_, _args_, _health\_check\_server\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/launcher/api.py#L244)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.launcher.api.launch_agent "Link to this definition")

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\]

### One-sided tensor transports (experimental)[#](https://docs.pytorch.org/docs/2.15/distributed.html#one-sided-tensor-transports-experimental "Link to this heading")

`torch.distributed._transport` moves registered tensor byte ranges between independently managed workers. It does not require a process group, global rank assignment, or matching receives.

An endpoint connects to one peer. Exchange `bind()` bytes and remote memory descriptors through a trusted application control plane. Exchange descriptors only with authorized peers. A write copies from a local view to the remote base; a read copies from the remote base to a writable local view. Offsets and lengths are bytes; shape and dtype agreement is the application’s responsibility.

Synchronous reads/writes return zero; `async_op=True` returns [`torch.distributed.Work`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.Work")
. Successful completion means the transfer completed, not that the remote application consumed or acknowledged the data. Asyncio callers can use `read_async`, `write_async`, or `wait_all`. Registration remains valid until unregistration or close, and tensors must not be resized or have their storage replaced.

Ordinary reads and writes are not ordered on CUDA streams. The API does not provide tracing, batching, or remote slicing. Descriptor classes define explicit `serialize()`/`deserialize()` methods. The built-in backends declare their fields in a versioned JSON envelope; binary metadata is base64-encoded. Unknown fields, versions, backends, and invalid field types are rejected. Tensor contents and native handles are never serialized.

torch.distributed.\_transport.new\_transport(_backend_, _device\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_registry.py#L72)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.new_transport "Link to this definition")

Construct a one-sided transport, optionally restricting tensor devices.

Parameters:

*   **backend** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Name registered with `register_transport` or an installed `torch.distributed.transports` entry point.
    
*   **device** ([_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
     _|_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _None_) – Optional CPU/CUDA device restriction; otherwise infer each tensor’s device at registration.
    
*   **\*\*kwargs** (_Any_) – Options forwarded to the selected backend’s constructor. Backend modules are imported only when selected.
    

Return type:

[Transport](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.Transport "torch.distributed._transport.Transport")

Example:

import torch
from torch.distributed.\_transport import new\_transport

backend \= "my\_backend"  \# An installed or process-registered backend.

\# Both endpoints are shown locally. Across processes, exchange bind()
\# results and remote descriptors through your application's control plane.
with (
    new\_transport(backend, "cpu") as trainer,
    new\_transport(backend, "cpu") as replica,
):
    trainer\_url, replica\_url \= trainer.bind(), replica.bind()
    trainer.connect(replica\_url)
    replica.connect(trainer\_url)
    weights \= torch.arange(8, dtype\=torch.float32)
    received \= torch.empty\_like(weights)
    source \= trainer.register\_memory(weights)
    target \= replica.register\_memory(received)
    descriptor \= target.to\_remote\_buffer()
    \# Exchange these bytes through the application control plane.
    remote \= type(descriptor).deserialize(descriptor.serialize())
    work \= trainer.write(source.to\_view(), remote, async\_op\=True)
    work.wait()
    torch.testing.assert\_close(received, weights)
    \# Coordinate with peers before closing either endpoint.

\# Inside an asyncio application, after registration and metadata exchange:
async def push\_weights(trainer, source, remote):
    await trainer.write\_async(source.to\_view(), remote, timeout\=30.0)
    \# Coordinate with peers before cleanup; cancellation does not cancel DMA.
    await trainer.close\_async(timeout\=30.0)

Copy to clipboard

torch.distributed.\_transport.new\_transport\_rank(_backend_, _device\=None_, _\*_, _store\=None_, _peer\_rank_, _rank\=None_, _bootstrap\_timeout\=30.0_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_bootstrap.py#L22)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.new_transport_rank "Link to this definition")

Construct, bind, and connect a transport through a Store.

Parameters:

*   **backend** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Registered transport backend name.
    
*   **device** ([_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
     _|_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _None_) – Optional tensor device restriction, as in `new_transport`.
    
*   **store** (_dist.Store_ _|_ _None_) – Shared rendezvous Store, such as `torch.distributed.TCPStore`; defaults to the default process group’s Store. No collectives are performed.
    
*   **peer\_rank** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Nonnegative integer identifying the peer in this Store namespace.
    
*   **rank** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ _None_) – Local identity; defaults to `torch.distributed.get_rank()`. An explicit override requires no initialized process group. Identities need not be contiguous, but must be distinct for the two peers.
    
*   **bootstrap\_timeout** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _|_ _timedelta_) – Timeout for each of bind, the Store waits, connect, and cleanup, in seconds or as a `timedelta`. Does not change the Store’s timeout.
    
*   **\*\*kwargs** (_Any_) – Forwarded to `new_transport` and the backend constructor.
    

Return type:

[Transport](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.Transport "torch.distributed._transport.Transport")

Example:

import torch.distributed as dist
from torch.distributed.\_transport import new\_transport\_rank

dist.init\_process\_group("gloo")
\# Pair ranks 0 and 1; other ranks need not participate.
transport \= new\_transport\_rank(
    "nixl",
    "cpu",
    peer\_rank\=1 \- dist.get\_rank(),
)
\# Exchange registered-memory descriptors separately. Coordinate with
\# peers before unregistering memory or closing the transport.

Copy to clipboard

Calls are matched in order per rank pair and backend: the Nth call on each peer connects to the other’s Nth call, including failed calls. One Store can therefore connect a rank to every other rank. Bootstrap failures attempt to close the partially created transport.

_class_ torch.distributed.\_transport.Transport(_device\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_api.py#L65)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.Transport "Link to this definition")

Base class for one-sided tensor transports.

`read` and `write` return zero on synchronous success. With `async_op=True`, they return a [`torch.distributed.Work`](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.Work")
 whose `wait` blocks until completion and propagates transfer errors. `is_completed` includes failed operations. Work futures resolve to an empty list on success.

`read_async` and `write_async` are asyncio coroutines. Cancellation or timeout may leave transfers pending. `wait_all` awaits their completion futures without blocking the event loop.

Operations use byte ranges, not tensor shapes or dtypes. One endpoint has one outgoing peer; no process group, ranks, or matching receives are needed. Exchange connection bytes and remote descriptors through a trusted control plane. Registration is valid until unregistration or close, including after bind/connect.

`timeout` is a nonnegative, finite number of seconds; `None` selects the backend default. A timeout bounds the caller’s wait, not the transfer’s lifetime: it does not cancel DMA. Pending work retains its local buffers. After a timeout, wait for the Work or successfully close the transport before reusing buffers. A timed-out close rejects new operations but retains resources until close is retried successfully. Independent transfers may overlap; wait before submitting dependent or overlapping reads/writes. There is no implicit completion ordering.

Never resize, replace storage, or modify buffers while registered/exposed to a peer. The application must coordinate remote access and notify peers before unregistering memory or closing; local completion does not establish that a peer has stopped accessing this endpoint. Descriptors are invalid after unregistration or their owner closes.

`read_stream` and `write_stream` order transfers on the current CUDA stream: the transfer starts after prior work on the stream, and later work waits for it to complete. They return after enqueueing, without holding SMs while the transfer is in flight, and can be captured in CUDA graphs. Transfer failures terminate the process, since consumers may already be enqueued. Ordinary `read` and `write` do not interact with CUDA streams.

_abstract_ bind(_\*_, _timeout\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_api.py#L122)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.Transport.bind "Link to this definition")

Bind the endpoint and return its opaque connection URL.

Return type:

[bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")

_abstract_ close(_\*_, _timeout\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_api.py#L292)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.Transport.close "Link to this definition")

Drain outstanding operations and release transport resources.

_async_ close\_async(_\*_, _timeout\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_api.py#L296)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.Transport.close_async "Link to this definition")

Await cleanup when supported by the backend.

Unlike `close`, this must not block the event loop while waiting for transfers. Blocking prototype backends do not implement this method.

_abstract_ connect(_peer\_url_, _\*_, _timeout\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_api.py#L126)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.Transport.connect "Link to this definition")

Connect to a bound peer and return zero on success.

Rank-to-endpoint lookup belongs in a separate application control-plane adapter; this interface addresses peers using opaque connection bytes.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

_abstract_ connected()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_api.py#L134)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.Transport.connected "Link to this definition")

Return whether the endpoint is connected to its peer.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

_abstract_ read(_local\_buffer_, _remote\_buffer_, _\*_, _async\_op\=False_, _timeout\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_api.py#L172)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.Transport.read "Link to this definition")

Read into a local view; return Work for async\_op=True, otherwise zero.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
 | [_Work_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.distributed_c10d.Work")

_async_ read\_async(_local\_buffer_, _remote\_buffer_, _\*_, _timeout\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_api.py#L270)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.Transport.read_async "Link to this definition")

Read into a local view, yielding to asyncio until the transfer finishes.

read\_stream(_local\_buffer_, _remote\_buffer_, _\*_, _stream\=None_, _timeout\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_api.py#L204)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.Transport.read_stream "Link to this definition")

Read into a local view in order on `stream` (default: current).

_abstract_ register\_memory(_tensor_, _\*_, _timeout\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_api.py#L138)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.Transport.register_memory "Link to this definition")

Register a contiguous tensor, including after bind/connect or transfers.

Exchange its remote-buffer descriptor with the peer before remote access.

Return type:

[_Memory_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.Memory "torch.distributed._transport._api.Memory")

_abstract static_ supported()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_api.py#L117)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.Transport.supported "Link to this definition")

Return whether the transport can be used in this process.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

unregister\_memory(_memory_, _\*_, _timeout\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_api.py#L147)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.Transport.unregister_memory "Link to this definition")

Unregister memory after coordinating with peers to stop remote access.

Wait for locally submitted transfers using this registration first. Reused registrations share one lifetime: unregistering any handle invalidates all aliases, existing views, and exported descriptors. Register the tensor again and exchange fresh descriptors before reuse. Repeating unregistration on the same handle is a no-op while open. Backends without this operation raise `NotImplementedError`.

_abstract_ write(_local\_buffer_, _remote\_buffer_, _\*_, _async\_op\=False_, _timeout\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_api.py#L161)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.Transport.write "Link to this definition")

Write a local view; return Work for async\_op=True, otherwise zero.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
 | [_Work_](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed.Work "torch.distributed.distributed_c10d.Work")

_async_ write\_async(_local\_buffer_, _remote\_buffer_, _\*_, _timeout\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_api.py#L248)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.Transport.write_async "Link to this definition")

Write a local view, yielding to asyncio until the transfer finishes.

write\_stream(_local\_buffer_, _remote\_buffer_, _\*_, _stream\=None_, _timeout\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_api.py#L183)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.Transport.write_stream "Link to this definition")

Write a local view in order on `stream` (default: current).

Returns once enqueued. Backends with native stream support may override this.

_class_ torch.distributed.\_transport.Memory(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_api.py#L50)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.Memory "Link to this definition")

Memory registered with a transport.

_class_ torch.distributed.\_transport.MemoryView(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_api.py#L19)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.MemoryView "Link to this definition")

A read-only view of registered memory.

_class_ torch.distributed.\_transport.MutableMemoryView(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_api.py#L26)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.MutableMemoryView "Link to this definition")

A view explicitly permitting writes to its registered memory.

_class_ torch.distributed.\_transport.RemoteBuffer(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_api.py#L34)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.RemoteBuffer "Link to this definition")

A backend-defined wire descriptor, excluding tensor contents/native handles.

Exchange `serialize()` bytes and reconstruct them with the matching backend descriptor class’s `deserialize()`. Decoders validate their schema and version without executing code or importing classes named by the payload. Descriptors grant memory access: exchange them only with authorized peers.

_async_ torch.distributed.\_transport.wait\_all(_works_, _\*_, _timeout\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_work.py#L64)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.wait_all "Link to this definition")

Await Work futures without blocking the asyncio loop.

Timeout and cancellation stop waiting, not transfers. Retain buffers and wait again (or close the transport) before reusing them. Transfer errors and iterable errors are reported after draining submitted work, unless this wait is timed out or cancelled first. Each Work must support `get_future`. This adapter does not select CUDA streams or establish consumer-stream ordering; callers must follow their backend’s CUDA synchronization contract.

torch.distributed.\_transport.available\_transports()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_registry.py#L65)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.available_transports "Link to this definition")

Return registered and discoverable transport names.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, …\]

torch.distributed.\_transport.register\_transport(_name_, _factory_, _\*_, _replace\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/_registry.py#L20)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.register_transport "Link to this definition")

Register a transport factory for this process.

#### CUDA streams[#](https://docs.pytorch.org/docs/2.15/distributed.html#cuda-streams "Link to this heading")

`read_stream` and `write_stream` order a transfer on `stream`, or the current CUDA stream if `None`. The transfer starts after prior work on the stream; later work waits for it to complete. Calls return after enqueueing and no kernel runs while the transfer is in flight.

with torch.cuda.stream(stream):
    source.copy\_(producer)
    transport.write\_stream(source\_view, remote\_destination)
    transport.read\_stream(destination\_view, remote\_source)
    consume(destination)

Copy to clipboard

Stream transfers can be captured with `torch.cuda.graph`; each replay submits a new transfer. Register buffers and warm up transfers before capture. Captured buffers stay registered until `close`; replaying after `close` terminates the process.

graph \= torch.cuda.CUDAGraph()
with torch.cuda.graph(graph):
    source.copy\_(producer)
    transport.write\_stream(source\_view, remote\_destination)
graph.replay()

Copy to clipboard

The default implementation awaits `write_async`/`read_async` on a shared asyncio loop thread and gates the stream with a CUDA stream memory wait. It requires Linux and GPUDirect RDMA write ordering, and allows 64 outstanding transfers per stream; captured transfers hold their slot until `close`. Since consumers may already be enqueued, a failed transfer terminates the process. Backends with native stream support may override these methods.

#### NIXL backend[#](https://docs.pytorch.org/docs/2.15/distributed.html#nixl-backend "Link to this heading")

The initial backend is NIXL, installed separately with `pip install nixl`. Its default UCX plugin supports CPU and CUDA memory, subject to the installed NIXL/UCX build and hardware.

`unregister_memory(memory)` deregisters a local allocation without closing the transport. Wait for local transfers first and coordinate with peers to stop remote access; the backend cannot detect incoming DMA. All handles sharing a registration, including previously created views and exported descriptors, become invalid. Register again and exchange fresh descriptors before resuming transfers.

NIXL transfers return Work objects that retain their request handles until completion. `wait_all`, `read_async`, and `write_async` await Work futures. The NIXL adapter resolves those futures by checking native transfer status. Each live transfer owns a distinct request handle. Independent requests may overlap; explicitly wait before issuing dependent or overlapping reads/writes. Completion ordering is not implicit.

NIXL’s default wait timeout is 30 seconds. `timeout` is in seconds; `None` selects the backend default and zero polls without waiting. `Work.wait` instead takes a `datetime.timedelta`; its zero default selects the transfer’s timeout. Timeout and asyncio cancellation stop waiting, not DMA. The transport retains pending requests and buffers, even if the caller drops its Work. Wait again or successfully close before reusing buffers. Coordinate with peers before closing exposed memory; close only drains locally submitted operations.

`NIXLTransport.close_async` awaits pending transfers before native cleanup. A timed-out or cancelled close rejects new work and retains resources; retry close to finish cleanup. Registrations keep the transport alive even after its last outgoing transfer, because peers may still access exposed memory. Forgotten registrations may retain resources indefinitely: call `unregister_memory` or `close` after coordinating with peers. Checking `is_completed` also releases completed requests. For pending NIXL work, `get_future` requires a running asyncio loop; the loop must remain running to drive that future. Completed work needs no event loop.

Native metadata, registration, request submission, status checks, and cleanup calls execute synchronously on the calling thread. Their timeouts bound lock acquisition and transfer completion waits, not execution inside NIXL. Python cannot interrupt a blocked native call, even when it releases the GIL.

_class_ torch.distributed.\_transport.nixl.NIXLTransport(_device\=None_, _\*_, _plugin\='UCX'_, _agent\_name\=None_, _num\_threads\=0_, _enable\_prog\_thread\=True_, _capture\_telemetry\=False_, _backend\_options\=None_, _timeout\=30.0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/nixl/_transport.py#L41)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.nixl.NIXLTransport "Link to this definition")

One-sided tensor transport backed by a NIXL plugin.

Backend options accepted by `new_transport()` include `plugin="UCX"`, `agent_name=None`, `num_threads=0`, `enable_prog_thread=True`, `capture_telemetry=False`, `backend_options=None`, and `timeout=30.0`. `backend_options` maps plugin parameter names to strings and is forwarded to NIXL’s `create_backend`. NIXL is an optional dependency, imported only when selected. Transfers require registered views; raw tensors are rejected rather than allocated or registered implicitly.

_async_ close\_async(_\*_, _timeout\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/_transport/nixl/_transport.py#L472)
[#](https://docs.pytorch.org/docs/2.15/distributed.html#torch.distributed._transport.nixl.NIXLTransport.close_async "Link to this definition")

Await outstanding DMA before synchronous native resource cleanup.

Cancellation/timeout retains resources and rejects new submissions. Retry close after pending work completes. Native cleanup is not interruptible; peer access must already have been stopped externally.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/distributed.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/distributed.md.txt)

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