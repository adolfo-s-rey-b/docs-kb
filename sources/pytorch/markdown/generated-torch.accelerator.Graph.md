Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.Graph.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.accelerator.Graph.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.Graph.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.accelerator.Graph.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.accelerator.Graph.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.accelerator.Graph.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.accelerator.Graph.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.accelerator.Graph.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.accelerator.Graph.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.accelerator.Graph.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.accelerator.Graph.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.accelerator.Graph.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.accelerator.Graph.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.accelerator.Graph.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.accelerator.Graph.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.accelerator.Graph.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.accelerator.Graph.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.accelerator.Graph.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.accelerator.Graph.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.accelerator.Graph.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.accelerator.Graph.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.accelerator.Graph.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.accelerator.Graph.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.accelerator.Graph.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.accelerator.Graph.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.accelerator.Graph.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.accelerator.Graph.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.accelerator.Graph.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.accelerator.Graph.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.accelerator.Graph.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.accelerator.Graph.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.accelerator.Graph.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.accelerator.Graph.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.accelerator.Graph.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.accelerator.Graph.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.accelerator.Graph.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.accelerator.Graph.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.accelerator.Graph.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.accelerator.Graph.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.accelerator.Graph.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.accelerator.Graph.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.accelerator.Graph.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.accelerator.Graph.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.accelerator.Graph.html)

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

Graph[#](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.Graph.html#graph "Link to this heading")

=================================================================================================================

_class_ torch.accelerator.Graph(_keep\_graph\=False_, _\*_, _pool\=None_, _capture\_error\_mode\='default'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/accelerator/graphs.py#L9)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.Graph.html#torch.accelerator.Graph "Link to this definition")

Wrapper around an [accelerator](https://docs.pytorch.org/docs/2.15/torch.html#accelerators)
 graph that supports capture and replay.

A graph captures a sequence of operations and their dependencies, allowing them to be replayed efficiently with reduced overhead. This class can be used as a context manager to automatically capture operations on the current stream.

Parameters:

*   **keep\_graph** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `False`, the underlying graph is destroyed and the executable graph is instantiated on the GPU at the end of `capture_end`. If `True`, the underlying graph is preserved after `capture_end`. In this case, the executable graph is not instantiated automatically; it must be explicitly created by calling `instantiate`, or it will be instantiated on the first call to `replay`. Defaults to `False`.
    
*   **pool** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]__,_ _optional_) – Memory pool identifier for this graph. Multiple graphs can share the same pool by passing the same identifier, which can reduce memory overhead. Defaults to `None`.
    
*   **capture\_error\_mode** (_Literal__\[__"default"__,_ _"global"__,_ _"thread\_local"__,_ _"relaxed"__\]__,_ _optional_) – Specifies the behavior of graph capture. The exact semantics are backend-specific. `"default"`: backend-defined default capture behavior. `"global"`: potentially unsafe API calls are prohibited. Errors may occur if capture in the current thread affects other threads. `"thread_local"`: potentially unsafe API calls are prohibited. Errors occur only if capture in the current thread affects itself. `"relaxed"`: the current thread is allowed to make potentially unsafe API calls, except for calls that inherently conflict with stream capture. Default: `"default"`.
    

Return type:

[_Self_](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.15)")

Example:

\>>> x \= torch.zeros(\[2000\], device\=0)

\>>> stream \= torch.Stream()
\>>> graph \= torch.accelerator.Graph()
\>>> with stream, graph:
...     x += 1

\>>> graph.replay()

Copy to clipboard

capture\_begin()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/accelerator/graphs.py#L76)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.Graph.html#torch.accelerator.Graph.capture_begin "Link to this definition")

Begin graph capture on the current stream.

All operations on the current stream after this call will be recorded into the graph until `capture_end` is called, using the memory pool and capture error mode provided at construction time.

capture\_end()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/accelerator/graphs.py#L87)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.Graph.html#torch.accelerator.Graph.capture_end "Link to this definition")

End graph capture on the current stream of the current device.

After this call, the graph can be replayed via `replay`.

debug\_dump(_path_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/accelerator/graphs.py#L140)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.Graph.html#torch.accelerator.Graph.debug_dump "Link to this definition")

Dump the captured graph to a file for debugging purposes if the debugging is enabled via `enable_debug_mode`.

Parameters:

**path** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – Path to dump the graph to.

Example::

\>>> s \= torch.Stream()
\>>> g \= torch.accelerator.Graph()
\>>> g.enable\_debug\_mode()

Copy to clipboard

\>>> with s, g:
\>>> \# ... operations ...

Copy to clipboard

\>>> \# Dump captured graph to a file "graph\_dump.dot"
\>>> g.debug\_dump("graph\_dump.dot")

Copy to clipboard

enable\_debug\_mode()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/accelerator/graphs.py#L136)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.Graph.html#torch.accelerator.Graph.enable_debug_mode "Link to this definition")

Enable debugging mode for `debug_dump`.

instantiate()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/accelerator/graphs.py#L95)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.Graph.html#torch.accelerator.Graph.instantiate "Link to this definition")

Instantiate the underlying graph. Will be called by `capture_end` if `keep_graph=False`, or by `replay` if `keep_graph=True` and `instantiate` has not already been explicitly called.

pool()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/accelerator/graphs.py#L116)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.Graph.html#torch.accelerator.Graph.pool "Link to this definition")

Return an opaque token representing the id of this graph’s memory pool.

This id can optionally be passed to another graph’s `capture_begin`, which hints the other graph may share the same memory pool.

Example::

\>>> g1 \= torch.accelerator.Graph()
\>>> g1.capture\_begin()
\>>> \# ... operations ...
\>>> g1.capture\_end()

Copy to clipboard

\>>> \# Share g1's memory pool with a new graph
\>>> pool\_id \= g1.pool()
\>>> g2 \= torch.accelerator.Graph(pool\=pool\_id)

Copy to clipboard

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
\]

replay()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/accelerator/graphs.py#L103)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.Graph.html#torch.accelerator.Graph.replay "Link to this definition")

Replay the work captured by this graph.

reset()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/accelerator/graphs.py#L107)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.accelerator.Graph.html#torch.accelerator.Graph.reset "Link to this definition")

Delete the graph currently held by this instance.

After this call, the graph can be recaptured. Set `graph_pool` or `capture_error_mode` beforehand to use different settings on the next capture.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.accelerator.Graph.rst.txt)

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