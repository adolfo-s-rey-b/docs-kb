Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.Event.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.Event.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.Event.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.Event.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.Event.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.Event.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.Event.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.Event.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.Event.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.Event.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.Event.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.Event.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.Event.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.Event.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.Event.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.Event.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.Event.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.Event.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.Event.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.Event.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.Event.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.Event.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.Event.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.Event.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.Event.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.Event.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.Event.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.Event.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.Event.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.Event.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.Event.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.Event.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.Event.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.Event.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.Event.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.Event.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.Event.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.Event.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.Event.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.Event.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.Event.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.Event.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.Event.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.Event.html)

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

Event[#](https://docs.pytorch.org/docs/2.15/generated/torch.Event.html#event "Link to this heading")

=====================================================================================================

_class_ torch.Event(_device\=None_, _\*_, _enable\_timing\=False_, _blocking\=False_, _interprocess\=False_)[#](https://docs.pytorch.org/docs/2.15/generated/torch.Event.html#torch.Event "Link to this definition")

Query and record Stream status to identify or control dependencies across Stream and measure timing.

Parameters:

*   **device** ([`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    , optional) – the desired device for the Event. If not given, the current [accelerator](https://docs.pytorch.org/docs/2.15/torch.html#accelerators)
     type will be used.
    
*   **enable\_timing** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – indicates if the event should measure time (default: `False`)
    
*   **blocking** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – if `True`, [`wait()`](https://docs.pytorch.org/docs/2.15/generated/torch.wait.html#torch.wait "torch.wait")
     will be blocking (default: `False`)
    
*   **interprocess** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – if `True`, the event can be shared between processes (default: `False`)
    

Warning

Both blocking and interprocess are not supported right now and are noops.

Returns:

An torch.Event object.

Return type:

[Event](https://docs.pytorch.org/docs/2.15/generated/torch.Event.html#torch.Event "torch.Event")

Example:

\>>> event \= torch.Event()
\>>> e\_cuda \= torch.Event(device\='cuda')

Copy to clipboard

elapsed\_time(_end\_event_) → [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Event.html#torch.Event.elapsed_time "Link to this definition")

Returns the elapsed time in milliseconds between when this event and the `end_event` are each recorded via [`torch.Stream.record_event()`](https://docs.pytorch.org/docs/2.15/generated/torch.Stream.html#torch.Stream.record_event "torch.Stream.record_event")
.

Parameters:

**end\_event** ([`torch.Event`](https://docs.pytorch.org/docs/2.15/generated/torch.Event.html#torch.Event "torch.Event")
) – The ending event has been recorded.

Returns:

Time between starting and ending event in milliseconds.

Return type:

[float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")

Example:

\>>> s\_cuda \= torch.Stream(device\='cuda')
\>>> e1\_cuda \= s\_cuda.record\_event()
\>>> e2\_cuda \= s\_cuda.record\_event()
\>>> ms \= e1\_cuda.elapsed\_time(e2\_cuda)

Copy to clipboard

query() → [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Event.html#torch.Event.query "Link to this definition")

Check if the stream where this event was recorded already moved past the point where the event was recorded. Always returns `True` if the Event was not recorded.

Returns:

A boolean indicating if all work currently captured by event has completed.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

Example:

\>>> s\_cuda \= torch.Stream(device\='cuda')
\>>> e\_cuda \= s\_cuda.record\_event()
\>>> e\_cuda.query()
True

Copy to clipboard

record(_stream\=None_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Event.html#torch.Event.record "Link to this definition")

Record the event in a given stream. The stream’s device must match the event’s device. This function is equivalent to `stream.record_event(self)`.

Parameters:

**stream** ([`torch.Stream`](https://docs.pytorch.org/docs/2.15/generated/torch.Stream.html#torch.Stream "torch.Stream")
, optional) – A stream to be recorded. If not given, the current stream will be used.

Example:

\>>> e\_cuda \= torch.Event(device\='cuda')
\>>> e\_cuda.record()

Copy to clipboard

synchronize() → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Event.html#torch.Event.synchronize "Link to this definition")

Wait for the event to complete. This prevents the CPU thread from proceeding until the event completes.

Example:

\>>> s\_cuda \= torch.Stream(device\='cuda')
\>>> e\_cuda \= s\_cuda.record\_event()
\>>> e\_cuda.synchronize()

Copy to clipboard

wait(_stream\=None_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.Event.html#torch.Event.wait "Link to this definition")

Make all future work submitted to the given stream wait for this event.

Parameters:

**stream** ([`torch.Stream`](https://docs.pytorch.org/docs/2.15/generated/torch.Stream.html#torch.Stream "torch.Stream")
, optional) – A stream to synchronize. If not given, the current stream will be used.

Example:

\>>> s1\_cuda \= torch.Stream(device\='cuda')
\>>> s2\_cuda \= torch.Stream(device\='cuda')
\>>> e\_cuda \= s1\_cuda.record()
\>>> e\_cuda.wait(s2)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.Event.rst.txt)

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