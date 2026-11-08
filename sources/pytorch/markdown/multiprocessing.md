Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/multiprocessing.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/multiprocessing.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/multiprocessing.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/multiprocessing.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/multiprocessing.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/multiprocessing.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/multiprocessing.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/multiprocessing.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/multiprocessing.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/multiprocessing.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/multiprocessing.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/multiprocessing.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/multiprocessing.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/multiprocessing.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/multiprocessing.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/multiprocessing.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/multiprocessing.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/multiprocessing.html)
[v1.13](https://docs.pytorch.org/docs/1.13/multiprocessing.html)
[v1.12](https://docs.pytorch.org/docs/1.12/multiprocessing.html)
[v1.11](https://docs.pytorch.org/docs/1.11/multiprocessing.html)
[v1.10](https://docs.pytorch.org/docs/1.10/multiprocessing.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/multiprocessing.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/multiprocessing.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/multiprocessing.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/multiprocessing.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/multiprocessing.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/multiprocessing.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/multiprocessing.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/multiprocessing.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/multiprocessing.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/multiprocessing.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/multiprocessing.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/multiprocessing.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/multiprocessing.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/multiprocessing.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/multiprocessing.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/multiprocessing.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/multiprocessing.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/multiprocessing.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/multiprocessing.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/multiprocessing.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/multiprocessing.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/multiprocessing.html)

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

Multiprocessing package - torch.multiprocessing[#](https://docs.pytorch.org/docs/2.15/multiprocessing.html#module-torch.multiprocessing "Link to this heading")

================================================================================================================================================================

Created On: Dec 23, 2016 | Last Updated On: Apr 13, 2026

torch.multiprocessing is a wrapper around the native [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "(in Python v3.15)")
 module.

It registers custom reducers, that use shared memory to provide shared views on the same data in different processes. Once the tensor/storage is moved to shared\_memory (see [`share_memory_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.share_memory_.html#torch.Tensor.share_memory_ "torch.Tensor.share_memory_")
), it will be possible to send it to other processes without making any copies.

The API is 100% compatible with the original module - it’s enough to change `import multiprocessing` to `import torch.multiprocessing` to have all the tensors sent through the queues or shared via other mechanisms, moved to shared memory.

Because of the similarity of APIs we do not document most of this package contents, and we recommend referring to very good docs of the original module.

Warning

If the main process exits abruptly (e.g. because of an incoming signal), Python’s `multiprocessing` sometimes fails to clean up its children. It’s a known caveat, so if you’re seeing any resource leaks after interrupting the interpreter, it probably means that this has just happened to you.

Strategy management[#](https://docs.pytorch.org/docs/2.15/multiprocessing.html#strategy-management "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

torch.multiprocessing.get\_all\_sharing\_strategies()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/multiprocessing/__init__.py#L82)
[#](https://docs.pytorch.org/docs/2.15/multiprocessing.html#torch.multiprocessing.get_all_sharing_strategies "Link to this definition")

Return a set of sharing strategies supported on a current system.

torch.multiprocessing.get\_sharing\_strategy()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/multiprocessing/__init__.py#L77)
[#](https://docs.pytorch.org/docs/2.15/multiprocessing.html#torch.multiprocessing.get_sharing_strategy "Link to this definition")

Return the current strategy for sharing CPU tensors.

torch.multiprocessing.set\_sharing\_strategy(_new\_strategy_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/multiprocessing/__init__.py#L61)
[#](https://docs.pytorch.org/docs/2.15/multiprocessing.html#torch.multiprocessing.set_sharing_strategy "Link to this definition")

Set the strategy for sharing CPU tensors.

Parameters:

**new\_strategy** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – Name of the selected strategy. Should be one of the values returned by [`get_all_sharing_strategies()`](https://docs.pytorch.org/docs/2.15/multiprocessing.html#torch.multiprocessing.get_all_sharing_strategies "torch.multiprocessing.get_all_sharing_strategies")
.

Sharing CUDA tensors[#](https://docs.pytorch.org/docs/2.15/multiprocessing.html#sharing-cuda-tensors "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

Sharing CUDA tensors between processes is supported only in Python 3, using a `spawn` or `forkserver` start methods.

Unlike CPU tensors, the sending process is required to keep the original tensor as long as the receiving process retains a copy of the tensor. The refcounting is implemented under the hood but requires users to follow the next best practices.

Warning

If the consumer process dies abnormally to a fatal signal, the shared tensor could be forever kept in memory as long as the sending process is running.

1.  Release memory ASAP in the consumer.
    

\## Good
x \= queue.get()
\# do somethings with x
del x

Copy to clipboard

\## Bad
x \= queue.get()
\# do somethings with x
\# do everything else (producer have to keep x in memory)

Copy to clipboard

2.  Keep producer process running until all consumers exits. This will prevent the situation when the producer process releasing memory which is still in use by the consumer.
    

\## producer
\# send tensors, do something
event.wait()

Copy to clipboard

\## consumer
\# receive tensors and use them
event.set()

Copy to clipboard

3.  Don’t pass received tensors.
    

\# not going to work
x \= queue.get()
queue\_2.put(x)

Copy to clipboard

\# you need to create a process-local copy
x \= queue.get()
x\_clone \= x.clone()
queue\_2.put(x\_clone)

Copy to clipboard

\# putting and getting from the same queue in the same process will likely end up with segfault
queue.put(tensor)
x \= queue.get()

Copy to clipboard

Sharing strategies[#](https://docs.pytorch.org/docs/2.15/multiprocessing.html#sharing-strategies "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

This section provides a brief overview into how different sharing strategies work. Note that it applies only to CPU tensor - CUDA tensors will always use the CUDA API, as that’s the only way they can be shared.

### File descriptor - `file_descriptor`[#](https://docs.pytorch.org/docs/2.15/multiprocessing.html#file-descriptor-file-descriptor "Link to this heading")

Note

This is the default strategy (except for macOS and OS X where it’s not supported).

This strategy will use file descriptors as shared memory handles. Whenever a storage is moved to shared memory, a file descriptor obtained from `shm_open` is cached with the object, and when it’s going to be sent to other processes, the file descriptor will be transferred (e.g. via UNIX sockets) to it. The receiver will also cache the file descriptor and `mmap` it, to obtain a shared view onto the storage data.

Note that if there will be a lot of tensors shared, this strategy will keep a large number of file descriptors open most of the time. If your system has low limits for the number of open file descriptors, and you can’t raise them, you should use the `file_system` strategy.

### File system - `file_system`[#](https://docs.pytorch.org/docs/2.15/multiprocessing.html#file-system-file-system "Link to this heading")

This strategy will use file names given to `shm_open` to identify the shared memory regions. This has a benefit of not requiring the implementation to cache the file descriptors obtained from it, but at the same time is prone to shared memory leaks. The file can’t be deleted right after its creation, because other processes need to access it to open their views. If the processes fatally crash, or are killed, and don’t call the storage destructors, the files will remain in the system. This is very serious, because they keep using up the memory until the system is restarted, or they’re freed manually.

To counter the problem of shared memory file leaks, [`torch.multiprocessing`](https://docs.pytorch.org/docs/2.15/multiprocessing.html#module-torch.multiprocessing "torch.multiprocessing")
 will spawn a daemon named `torch_shm_manager` that will isolate itself from the current process group, and will keep track of all shared memory allocations. Once all processes connected to it exit, it will wait a moment to ensure there will be no new connections, and will iterate over all shared memory files allocated by the group. If it finds that any of them still exist, they will be deallocated. We’ve tested this method and it proved to be robust to various failures. Still, if your system has high enough limits, and `file_descriptor` is a supported strategy, we do not recommend switching to this one.

Spawning subprocesses[#](https://docs.pytorch.org/docs/2.15/multiprocessing.html#spawning-subprocesses "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

Note

Available for Python >= 3.4.

This depends on the `spawn` start method in Python’s `multiprocessing` package.

Spawning a number of subprocesses to perform some function can be done by creating `Process` instances and calling `join` to wait for their completion. This approach works fine when dealing with a single subprocess but presents potential issues when dealing with multiple processes.

Namely, joining processes sequentially implies they will terminate sequentially. If they don’t, and the first process does not terminate, the process termination will go unnoticed. Also, there are no native facilities for error propagation.

The `spawn` function below addresses these concerns and takes care of error propagation, out of order termination, and will actively terminate processes upon detecting an error in one of them.

torch.multiprocessing.spawn.spawn(_fn_, _args\=()_, _nprocs\=1_, _join\=True_, _daemon\=False_, _start\_method\='spawn'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/multiprocessing/spawn.py#L309)
[#](https://docs.pytorch.org/docs/2.15/multiprocessing.html#torch.multiprocessing.spawn.spawn "Link to this definition")

Spawns `nprocs` processes that run `fn` with `args`.

If one of the processes exits with a non-zero exit status, the remaining processes are killed and an exception is raised with the cause of termination. In the case an exception was caught in the child process, it is forwarded and its traceback is included in the exception raised in the parent process.

Parameters:

*   **fn** (_function_) –
    
    Function is called as the entrypoint of the spawned process. This function must be defined at the top level of a module so it can be pickled and spawned. This is a requirement imposed by multiprocessing.
    
    The function is called as `fn(i, *args)`, where `i` is the process index and `args` is the passed through tuple of arguments.
    
*   **args** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    ) – Arguments passed to `fn`.
    
*   **nprocs** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Number of processes to spawn.
    
*   **join** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Perform a blocking join on all processes.
    
*   **daemon** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – The spawned processes’ daemon flag. If set to True, daemonic processes will be created.
    
*   **start\_method** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – (deprecated) this method will always use `spawn` as the start method. To use a different start method use `start_processes()`.
    

Returns:

None if `join` is `True`, `ProcessContext` if `join` is `False`

_class_ torch.multiprocessing.SpawnContext[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/multiprocessing/spawn.py#L223)
[#](https://docs.pytorch.org/docs/2.15/multiprocessing.html#torch.multiprocessing.SpawnContext "Link to this definition")

Returned by [`spawn()`](https://docs.pytorch.org/docs/2.15/multiprocessing.html#module-torch.multiprocessing.spawn "torch.multiprocessing.spawn")
 when called with `join=False`.

join(_timeout\=None_, _grace\_period\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/multiprocessing/spawn.py#L127)
[#](https://docs.pytorch.org/docs/2.15/multiprocessing.html#torch.multiprocessing.SpawnContext.join "Link to this definition")

Join one or more processes within spawn context.

Attempt to join one or more processes in this spawn context. If one of them exited with a non-zero exit status, this function kills the remaining processes (optionally with a grace period) and raises an exception with the cause of the first process exiting.

Returns `True` if all processes have been joined successfully, `False` if there are more processes that need to be joined.

Parameters:

*   **timeout** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – Wait this long (in seconds) before giving up on waiting.
    
*   **grace\_period** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – When any processes fail, wait this long (in seconds) for others to shutdown gracefully before terminating them. If they still don’t exit, wait another grace period before killing them.
    

torch.multiprocessing.pool[#](https://docs.pytorch.org/docs/2.15/multiprocessing.html#module-torch.multiprocessing.pool "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/multiprocessing.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/multiprocessing.md.txt)

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