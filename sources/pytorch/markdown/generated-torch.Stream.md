Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.Stream.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.Stream.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.Stream.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.Stream.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.Stream.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.Stream.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.Stream.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.Stream.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.Stream.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.Stream.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.Stream.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.Stream.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.Stream.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.Stream.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.Stream.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.Stream.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.Stream.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.Stream.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.Stream.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.Stream.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.Stream.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.Stream.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.Stream.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.Stream.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.Stream.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.Stream.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.Stream.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.Stream.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.Stream.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.Stream.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.Stream.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.Stream.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.Stream.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.Stream.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.Stream.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.Stream.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.Stream.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.Stream.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.Stream.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.Stream.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.Stream.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.Stream.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.Stream.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.Stream.html)

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

Stream[#](https://docs.pytorch.org/docs/2.15/generated/torch.Stream.html#stream "Link to this heading")

========================================================================================================

_class_ torch.Stream(_device_, _\*_, _priority_)[#](https://docs.pytorch.org/docs/2.15/generated/torch.Stream.html#torch.Stream "Link to this definition")

An in-order queue of executing the respective tasks asynchronously in first in first out (FIFO) order. It can control or synchronize the execution of other Stream or block the current host thread to ensure the correct task sequencing. It supports with statement as a context manager to ensure the operators within the with block are running on the corresponding stream.

See in-depth description of the CUDA behavior at [CUDA semantics](https://docs.pytorch.org/docs/2.15/notes/cuda.html#cuda-semantics)
 for details on the exact semantic that applies to all devices.

Parameters:

*   **device** ([`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    , optional) – the desired device for the Stream. If not given, the current [accelerator](https://docs.pytorch.org/docs/2.15/torch.html#accelerators)
     type will be used.
    
*   **priority** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – priority of the stream, should be 0 or negative, where negative numbers indicate higher priority. By default, streams have priority 0.
    

Returns:

An torch.Stream object.

Return type:

[Stream](https://docs.pytorch.org/docs/2.15/generated/torch.Stream.html#torch.Stream "torch.Stream")

Example:

\>>> with torch.Stream(device\='cuda') as s\_cuda:
\>>>     a \= torch.randn(10, 5, device\='cuda')
\>>>     b \= torch.randn(5, 10, device\='cuda')
\>>>     c \= torch.mm(a, b)

Copy to clipboard

is\_capturing() → [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Stream.html#torch.Stream.is_capturing "Link to this definition")

Return true if this stream is currently recording work for graph capture.

Returns:

A boolean indicating if the stream is capturing.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

Example:

\>>> s\_cuda \= torch.Stream(device\='cuda')
\>>> s\_cuda.is\_capturing()

Copy to clipboard

query() → [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Stream.html#torch.Stream.query "Link to this definition")

Check if all the work submitted has been completed.

Returns:

A boolean indicating if all kernels in this stream are completed.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

Example:

\>>> s\_cuda \= torch.Stream(device\='cuda')
\>>> s\_cuda.query()
True

Copy to clipboard

record\_event(_event_) → [Event](https://docs.pytorch.org/docs/2.15/generated/torch.Event.html#torch.Event "torch.Event")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Stream.html#torch.Stream.record_event "Link to this definition")

Record an event. En-queuing it into the Stream to allow further synchronization from the current point in the FIFO queue.

Parameters:

**event** ([`torch.Event`](https://docs.pytorch.org/docs/2.15/generated/torch.Event.html#torch.Event "torch.Event")
, optional) – event to record. If not given, a new one will be allocated.

Returns:

Recorded event.

Return type:

[Event](https://docs.pytorch.org/docs/2.15/generated/torch.Event.html#torch.Event "torch.Event")

Example:

\>>> s\_cuda \= torch.Stream(device\='cuda')
\>>> e\_cuda \= s\_cuda.record\_event()

Copy to clipboard

synchronize() → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Stream.html#torch.Stream.synchronize "Link to this definition")

Wait for all the kernels in this stream to complete.

Example:

\>>> s\_cuda \= torch.Stream(device\='cuda')
\>>> s\_cuda.synchronize()

Copy to clipboard

wait\_event(_event_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Stream.html#torch.Stream.wait_event "Link to this definition")

Make all future work submitted to the stream wait for an event.

Parameters:

**event** ([`torch.Event`](https://docs.pytorch.org/docs/2.15/generated/torch.Event.html#torch.Event "torch.Event")
) – an event to wait for.

Example:

\>>> s1\_cuda \= torch.Stream(device\='cuda')
\>>> s2\_cuda \= torch.Stream(device\='cuda')
\>>> e\_cuda \= s1\_cuda.record\_event()
\>>> s2\_cuda.wait\_event(e\_cuda)

Copy to clipboard

wait\_stream(_stream_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Stream.html#torch.Stream.wait_stream "Link to this definition")

Synchronize with another stream. All future work submitted to this stream will wait until all kernels already submitted to the given stream are completed.

Parameters:

**stream** ([`torch.Stream`](https://docs.pytorch.org/docs/2.15/generated/torch.Stream.html#torch.Stream "torch.Stream")
) – a stream to synchronize.

Example:

\>>> s1\_cuda \= torch.Stream(device\='cuda')
\>>> s2\_cuda \= torch.Stream(device\='cuda')
\>>> s2\_cuda.wait\_stream(s1\_cuda)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.Stream.rst.txt)

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