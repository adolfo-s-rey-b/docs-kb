Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/mtia.mtia_graph.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/mtia.mtia_graph.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/mtia.mtia_graph.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/mtia.mtia_graph.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/mtia.mtia_graph.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/mtia.mtia_graph.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/mtia.mtia_graph.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/mtia.mtia_graph.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/mtia.mtia_graph.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/mtia.mtia_graph.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/mtia.mtia_graph.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/mtia.mtia_graph.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/mtia.mtia_graph.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/mtia.mtia_graph.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/mtia.mtia_graph.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/mtia.mtia_graph.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/mtia.mtia_graph.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/mtia.mtia_graph.html)
[v1.13](https://docs.pytorch.org/docs/1.13/mtia.mtia_graph.html)
[v1.12](https://docs.pytorch.org/docs/1.12/mtia.mtia_graph.html)
[v1.11](https://docs.pytorch.org/docs/1.11/mtia.mtia_graph.html)
[v1.10](https://docs.pytorch.org/docs/1.10/mtia.mtia_graph.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/mtia.mtia_graph.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/mtia.mtia_graph.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/mtia.mtia_graph.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/mtia.mtia_graph.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/mtia.mtia_graph.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/mtia.mtia_graph.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/mtia.mtia_graph.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/mtia.mtia_graph.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/mtia.mtia_graph.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/mtia.mtia_graph.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/mtia.mtia_graph.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/mtia.mtia_graph.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/mtia.mtia_graph.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/mtia.mtia_graph.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/mtia.mtia_graph.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/mtia.mtia_graph.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/mtia.mtia_graph.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/mtia.mtia_graph.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/mtia.mtia_graph.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/mtia.mtia_graph.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/mtia.mtia_graph.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/mtia.mtia_graph.html)

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

torch.mtia.mtia\_graph[#](https://docs.pytorch.org/docs/2.15/mtia.mtia_graph.html#torch-mtia-mtia-graph "Link to this heading")

================================================================================================================================

Created On: Nov 10, 2025 | Last Updated On: Sep 09, 2026

The MTIA backend is implemented out of the tree, only interfaces are defined here.

torch.mtia.mtia\_graph.is\_current\_stream\_capturing()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/mtia/mtia_graph.py#L12)
[#](https://docs.pytorch.org/docs/2.15/mtia.mtia_graph.html#torch.mtia.mtia_graph.is_current_stream_capturing "Link to this definition")

Return whether MTIA graph capture is underway on the current stream.

If an MTIA context does not exist on the current device, return `False` without initializing the context.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.mtia.mtia\_graph.graph\_pool\_handle()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/mtia/mtia_graph.py#L21)
[#](https://docs.pytorch.org/docs/2.15/mtia.mtia_graph.html#torch.mtia.mtia_graph.graph_pool_handle "Link to this definition")

Return an opaque token representing the id of a graph memory pool.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
\]

_class_ torch.mtia.mtia\_graph.MTIAGraph(_keep\_graph\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/mtia/mtia_graph.py#L29)
[#](https://docs.pytorch.org/docs/2.15/mtia.mtia_graph.html#torch.mtia.mtia_graph.MTIAGraph "Link to this definition")

Wrapper around a MTIA graph.

Return type:

Self

capture\_begin(_pool_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/mtia/mtia_graph.py#L37)
[#](https://docs.pytorch.org/docs/2.15/mtia.mtia_graph.html#torch.mtia.mtia_graph.MTIAGraph.capture_begin "Link to this definition")

Begin capturing a MTIA graph.

capture\_end()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/mtia/mtia_graph.py#L43)
[#](https://docs.pytorch.org/docs/2.15/mtia.mtia_graph.html#torch.mtia.mtia_graph.MTIAGraph.capture_end "Link to this definition")

End the capture of a MTIA graph.

instantiate()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/mtia/mtia_graph.py#L49)
[#](https://docs.pytorch.org/docs/2.15/mtia.mtia_graph.html#torch.mtia.mtia_graph.MTIAGraph.instantiate "Link to this definition")

Instantiate the captured MTIA graph.

pool()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/mtia/mtia_graph.py#L67)
[#](https://docs.pytorch.org/docs/2.15/mtia.mtia_graph.html#torch.mtia.mtia_graph.MTIAGraph.pool "Link to this definition")

Return an opaque token representing the id of this graph’s memory pool

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
\]

replay()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/mtia/mtia_graph.py#L55)
[#](https://docs.pytorch.org/docs/2.15/mtia.mtia_graph.html#torch.mtia.mtia_graph.MTIAGraph.replay "Link to this definition")

Replay the captured MTIA graph.

reset()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/mtia/mtia_graph.py#L61)
[#](https://docs.pytorch.org/docs/2.15/mtia.mtia_graph.html#torch.mtia.mtia_graph.MTIAGraph.reset "Link to this definition")

Destroy the captured graph and reset the states.

_class_ torch.mtia.mtia\_graph.graph(_mtia\_graph_, _pool\=None_, _stream\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/mtia/mtia_graph.py#L74)
[#](https://docs.pytorch.org/docs/2.15/mtia.mtia_graph.html#torch.mtia.mtia_graph.graph "Link to this definition")

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/mtia.mtia_graph.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/mtia.mtia_graph.md.txt)

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