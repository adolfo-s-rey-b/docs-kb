Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Event.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.cuda.streams.Event.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Event.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.cuda.streams.Event.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.cuda.streams.Event.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.cuda.streams.Event.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.cuda.streams.Event.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.cuda.streams.Event.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.cuda.streams.Event.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.cuda.streams.Event.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.cuda.streams.Event.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.cuda.streams.Event.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.cuda.streams.Event.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.cuda.streams.Event.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.cuda.streams.Event.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.cuda.streams.Event.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.cuda.streams.Event.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.cuda.streams.Event.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.cuda.streams.Event.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.cuda.streams.Event.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.cuda.streams.Event.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.cuda.streams.Event.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.cuda.streams.Event.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.cuda.streams.Event.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.cuda.streams.Event.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.cuda.streams.Event.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.cuda.streams.Event.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.cuda.streams.Event.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.cuda.streams.Event.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.cuda.streams.Event.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.cuda.streams.Event.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.cuda.streams.Event.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.cuda.streams.Event.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.cuda.streams.Event.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.cuda.streams.Event.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.cuda.streams.Event.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.cuda.streams.Event.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.cuda.streams.Event.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.cuda.streams.Event.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.cuda.streams.Event.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.cuda.streams.Event.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.cuda.streams.Event.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.cuda.streams.Event.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.cuda.streams.Event.html)

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

Event[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Event.html#event "Link to this heading")

==================================================================================================================

_class_ torch.cuda.streams.Event(_enable\_timing\=False_, _blocking\=False_, _interprocess\=False_, _external\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/streams.py#L159)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Event.html#torch.cuda.streams.Event "Link to this definition")

Wrapper around a CUDA event.

CUDA events are synchronization markers that can be used to monitor the device’s progress, to accurately measure timing, and to synchronize CUDA streams.

The underlying CUDA events are lazily initialized when the event is first recorded or exported to another process. After creation, only streams on the same device may record the event. However, streams on any device can wait on the event.

Parameters:

*   **enable\_timing** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – indicates if the event should measure time (default: `False`)
    
*   **blocking** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – if `True`, [`wait()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Event.html#torch.cuda.streams.Event.wait "torch.cuda.streams.Event.wait")
     will be blocking (default: `False`)
    
*   **interprocess** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – if `True`, the event can be shared between processes (default: `False`)
    
*   **external** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – indicates whether this event should create event record and event wait nodes, or create an internal cross-stream dependency, when captured in a cuda graph. See [cross-stream dependencies](https://docs.nvidia.com/cuda/archive/12.9.0/cuda-c-programming-guide/index.html#cross-stream-dependencies-and-events)
    , [cudaEventRecordExternal](https://docs.nvidia.com/cuda/archive/12.9.0/cuda-runtime-api/group__CUDART__TYPES.html#group__CUDART__TYPES_1g3457b81d1d32c6a00f6132fbc2693d47)
    , and [cudaEventWaitExternal](https://docs.nvidia.com/cuda/archive/12.9.0/cuda-runtime-api/group__CUDART__TYPES.html#group__CUDART__TYPES_1g0c23426b7252eaa9cef695859991304e)
     for more information about internal vs. external events. (default: `False`)
    

elapsed\_time(_end\_event_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/streams.py#L234)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Event.html#torch.cuda.streams.Event.elapsed_time "Link to this definition")

Return the time elapsed.

Time reported in milliseconds after the event was recorded and before the end\_event was recorded.

Parameters:

**end\_event** ([_Event_](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Event.html#torch.cuda.streams.Event "torch.cuda.streams.Event")
) – the end event.

_classmethod_ from\_ipc\_handle(_device_, _handle_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/streams.py#L194)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Event.html#torch.cuda.streams.Event.from_ipc_handle "Link to this definition")

Reconstruct an event from an IPC handle on the given device.

ipc\_handle()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/streams.py#L256)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Event.html#torch.cuda.streams.Event.ipc_handle "Link to this definition")

Return an IPC handle of this event.

If not recorded yet, the event will use the current device.

query()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/streams.py#L225)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Event.html#torch.cuda.streams.Event.query "Link to this definition")

Check if all work currently captured by event has completed.

Returns:

A boolean indicating if all work currently captured by event has completed.

record(_stream\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/streams.py#L199)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Event.html#torch.cuda.streams.Event.record "Link to this definition")

Record the event in a given stream.

Parameters:

**stream** ([_Stream_](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Stream.html#torch.cuda.streams.Stream "torch.cuda.streams.Stream")
_,_ [_torch.Stream_](https://docs.pytorch.org/docs/2.15/generated/torch.Stream.html#torch.Stream "torch.Stream")
_,_ _optional_) – Uses `torch.cuda.current_stream()` if no stream is specified. The stream’s device must match the event’s device.

synchronize()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/streams.py#L245)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Event.html#torch.cuda.streams.Event.synchronize "Link to this definition")

Wait for the event to complete.

Waits until the completion of all work currently captured in this event. This prevents the CPU thread from proceeding until the event completes.

> Note
> 
> This is a wrapper around `cudaEventSynchronize()`: see [CUDA Event documentation](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__EVENT.html)
>  for more info.

wait(_stream\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/streams.py#L211)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Event.html#torch.cuda.streams.Event.wait "Link to this definition")

Make all future work submitted to the given stream wait for this event.

Parameters:

**stream** ([_Stream_](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Stream.html#torch.cuda.streams.Stream "torch.cuda.streams.Stream")
_,_ [_torch.Stream_](https://docs.pytorch.org/docs/2.15/generated/torch.Stream.html#torch.Stream "torch.Stream")
_,_ _optional_) – Uses `torch.cuda.current_stream()` if no stream is specified.

Note

This is a wrapper around `cudaStreamWaitEvent()`: see [CUDA Event documentation](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__EVENT.html)
 for more info.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.cuda.streams.Event.rst.txt)

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