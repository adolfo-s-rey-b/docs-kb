Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.cuda.graph.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.cuda.graph.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.cuda.graph.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.cuda.graph.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.cuda.graph.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.cuda.graph.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.cuda.graph.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.cuda.graph.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.cuda.graph.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.cuda.graph.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.cuda.graph.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.cuda.graph.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.cuda.graph.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.cuda.graph.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.cuda.graph.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.cuda.graph.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.cuda.graph.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.cuda.graph.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.cuda.graph.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.cuda.graph.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.cuda.graph.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.cuda.graph.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.cuda.graph.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.cuda.graph.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.cuda.graph.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.cuda.graph.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.cuda.graph.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.cuda.graph.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.cuda.graph.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.cuda.graph.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.cuda.graph.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.cuda.graph.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.cuda.graph.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.cuda.graph.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.cuda.graph.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.cuda.graph.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.cuda.graph.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.cuda.graph.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.cuda.graph.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.cuda.graph.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.cuda.graph.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.cuda.graph.html)

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

graph[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph.html#graph "Link to this heading")

==========================================================================================================

_class_ torch.cuda.graph(_cuda\_graph_, _pool\=None_, _stream\=None_, _capture\_error\_mode\='global'_, _enable\_annotations\=False_, _annotation\_config\=None_, _check\_input\_liveness\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/graphs.py#L1199)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph.html#torch.cuda.graph "Link to this definition")

Context-manager that captures CUDA work into a [`torch.cuda.CUDAGraph`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph "torch.cuda.CUDAGraph")
 object for later replay.

See [CUDA Graphs](https://docs.pytorch.org/docs/2.15/notes/cuda.html#cuda-graph-semantics)
 for a general introduction, detailed use, and constraints.

Parameters:

*   **cuda\_graph** ([_torch.cuda.CUDAGraph_](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph "torch.cuda.CUDAGraph")
    ) – Graph object used for capture.
    
*   **pool** (_optional_) – Opaque token (returned by a call to [`graph_pool_handle()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph_pool_handle.html#torch.cuda.graph_pool_handle "torch.cuda.graph_pool_handle")
     or [`other_Graph_instance.pool()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.CUDAGraph.html#torch.cuda.CUDAGraph.pool "torch.cuda.CUDAGraph.pool")
    ) or `MemPool` hinting this graph’s capture may share memory from the specified pool. See [Graph memory management](https://docs.pytorch.org/docs/2.15/notes/cuda.html#graph-memory-management)
    .
    
*   **stream** ([_torch.cuda.Stream_](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.Stream_class.html#torch.cuda.Stream "torch.cuda.Stream")
    _,_ _optional_) – If supplied, will be set as the current stream in the context. If not supplied, `graph` sets its own internal side stream as the current stream in the context.
    
*   **capture\_error\_mode** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – specifies the cudaStreamCaptureMode for the graph capture stream. Can be “global”, “thread\_local” or “relaxed”. During cuda graph capture, some actions, such as cudaMalloc, may be unsafe. “global” will error on actions in other threads, “thread\_local” will only error for actions in the current thread, and “relaxed” will not error on actions. Do NOT change this setting unless you’re familiar with [cudaStreamCaptureMode](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__STREAM.html#group__CUDART__STREAM_1g9d0535d93a214cbf126835257b16ba85)
    
*   **enable\_annotations** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True`, enables kernel annotation recording on entry and automatically calls `resolve_pending_annotations()` before the capture ends. Annotations are **not** cleared on exit so that multiple graphs in the same workload can accumulate annotations. Requires `cuda.bindings` package and cuda-compat >= 13.1 or CUDA driver >= 13.1. Requires single-threaded autograd; wrap the capture in `torch.autograd.grad_mode.set_multithreading_enabled(False)`.
    
*   **annotation\_config** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _,_ _optional_) – Options for annotation recording, used when `enable_annotations=True`. An unrecognized key or value raises. Currently supports `"backend"`, which selects how `mark_kernels` scopes discover their nodes: `"auto"` (default) uses CUPTI node-creation callbacks when Cuspy already holds a subscription and otherwise walks the capture graph’s dependent edges; `"cupti"` requires the CUPTI path, bringing Cuspy up if needed – which prevents kineto from initializing, so a later [`torch.profiler.profile`](https://docs.pytorch.org/docs/2.15/profiler.html#torch.profiler.profile "torch.profiler.profile")
     records no GPU activity; `"edge_walk"` forces the walk, which cannot see nodes created while the current stream was not yet capturing. Also supports `"key_by"`, which selects the graph the annotations stay keyed to: `"exec"` (default) rekeys them to the executable graph at each `instantiate()`, matching the graph node id CUPTI reports for replayed work; `"source"` leaves them on the capture graph, for a consumer that reads CUPTI’s `sourceGraphNodeId` instead (needs CUPTI >= 13.4 and a CUDA driver >= 13.4, else the capture raises); `"auto"` is `"source"` where the stack supports it and `"exec"` where it does not, so it never raises. `"exec"` remains the default because kineto reports only the exec node id, so a trace exported through it cannot resolve capture-keyed annotations. `"record_py_stacks"` (bool, default `False`) records user Python launch frames for kernel, memcpy, memset, batch-memory, event, and host nodes. It requires CUPTI and single-threaded autograd: `backend="auto"` acquires a CUPTI subscription as with `"cupti"`, and `"edge_walk"` is rejected. By default, framework and generated Inductor frames are omitted. Conditional and child-graph bodies require `key_by="source"`. Use `"exec"` keys for exported traces or `"source"` keys for CUPTI’s `sourceGraphNodeId`. Save stacks separately with [`dump_kernel_py_stacks()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph_annotations.dump_kernel_py_stacks.html#torch.cuda.graph_annotations.dump_kernel_py_stacks "torch.cuda.graph_annotations.dump_kernel_py_stacks")
     or read them with [`get_kernel_py_stacks()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.graph_annotations.get_kernel_py_stacks.html#torch.cuda.graph_annotations.get_kernel_py_stacks "torch.cuda.graph_annotations.get_kernel_py_stacks")
    . `"py_stack_filter_paths"` (list or tuple of str, default `None`) replaces the default stack filters with directories whose frames should be omitted. Paths are matched on directory boundaries; relative paths are resolved when capture begins. `None` uses the defaults; an empty list disables filtering. Used only with `record_py_stacks=True`.
    
*   **check\_input\_liveness** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) –
    
    If `True`, tracks external tensor inputs during graph capture and raises an error if any are deallocated before replay. This helps debug “use after free” errors where input tensors are garbage collected between capture and replay. Default: `False`.
    
    Note
    
    Custom CUDA kernels added outside PyTorch (e.g., via cuLaunchKernel or DLPack) are not tracked by this mechanism.
    

Note

For effective memory sharing, if you pass a `pool` used by a previous capture and the previous capture used an explicit `stream` argument, you should pass the same `stream` argument to this capture.

Warning

This API is in beta and may change in future releases.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.cuda.graph.rst.txt)

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