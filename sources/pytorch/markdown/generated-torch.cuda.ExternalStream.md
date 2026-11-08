Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.ExternalStream.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.cuda.ExternalStream.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.ExternalStream.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.cuda.ExternalStream.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.cuda.ExternalStream.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.cuda.ExternalStream.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.cuda.ExternalStream.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.cuda.ExternalStream.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.cuda.ExternalStream.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.cuda.ExternalStream.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.cuda.ExternalStream.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.cuda.ExternalStream.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.cuda.ExternalStream.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.cuda.ExternalStream.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.cuda.ExternalStream.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.cuda.ExternalStream.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.cuda.ExternalStream.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.cuda.ExternalStream.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.cuda.ExternalStream.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.cuda.ExternalStream.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.cuda.ExternalStream.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.cuda.ExternalStream.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.cuda.ExternalStream.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.cuda.ExternalStream.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.cuda.ExternalStream.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.cuda.ExternalStream.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.cuda.ExternalStream.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.cuda.ExternalStream.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.cuda.ExternalStream.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.cuda.ExternalStream.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.cuda.ExternalStream.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.cuda.ExternalStream.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.cuda.ExternalStream.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.cuda.ExternalStream.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.cuda.ExternalStream.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.cuda.ExternalStream.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.cuda.ExternalStream.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.cuda.ExternalStream.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.cuda.ExternalStream.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.cuda.ExternalStream.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.cuda.ExternalStream.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.cuda.ExternalStream.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.cuda.ExternalStream.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.cuda.ExternalStream.html)

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

ExternalStream[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.ExternalStream.html#externalstream "Link to this heading")

=====================================================================================================================================

_class_ torch.cuda.ExternalStream(_stream\_ptr_, _device\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/streams.py#L136)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.ExternalStream.html#torch.cuda.ExternalStream "Link to this definition")

Wrapper around an externally allocated CUDA stream.

This class is used to wrap streams allocated in other libraries in order to facilitate data exchange and multi-library interactions.

Note

This class doesn’t manage the stream life-cycle, it is the user responsibility to keep the referenced stream alive while this class is being used.

Parameters:

*   **stream\_ptr** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Integer representation of the cudaStream\_t value. allocated externally.
    
*   **device** ([_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
     _or_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – the device where the stream was originally allocated. If device is specified incorrectly, subsequent launches using this stream may fail.
    

query()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/streams.py#L94)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.ExternalStream.html#torch.cuda.ExternalStream.query "Link to this definition")

Check if all the work submitted has been completed.

Returns:

A boolean indicating if all kernels in this stream are completed.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

record\_event(_event\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/streams.py#L79)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.ExternalStream.html#torch.cuda.ExternalStream.record_event "Link to this definition")

Record an event.

Parameters:

**event** ([_Event_](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.Event.html#torch.cuda.Event "torch.cuda.Event")
_,_ [_torch.Event_](https://docs.pytorch.org/docs/2.15/generated/torch.Event.html#torch.Event "torch.Event")
_,_ _optional_) – event to record. If not given, a new one will be allocated.

Returns:

Recorded event.

synchronize()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/streams.py#L102)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.ExternalStream.html#torch.cuda.ExternalStream.synchronize "Link to this definition")

Wait for all the kernels in this stream to complete.

Note

This is a wrapper around `cudaStreamSynchronize()`: see [CUDA Stream documentation](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__STREAM.html)
 for more info.

wait\_event(_event_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/streams.py#L48)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.ExternalStream.html#torch.cuda.ExternalStream.wait_event "Link to this definition")

Make all future work submitted to the stream wait for an event.

Parameters:

**event** ([_Event_](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.Event.html#torch.cuda.Event "torch.cuda.Event")
_,_ [_torch.Event_](https://docs.pytorch.org/docs/2.15/generated/torch.Event.html#torch.Event "torch.Event")
) – an event to wait for.

Note

This is a wrapper around `cudaStreamWaitEvent()`: see [CUDA Stream documentation](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__STREAM.html)
 for more info.

This function returns without waiting for `event`: only future operations are affected.

wait\_stream(_stream_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/streams.py#L65)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.ExternalStream.html#torch.cuda.ExternalStream.wait_stream "Link to this definition")

Synchronize with another stream.

All future work submitted to this stream will wait until all kernels submitted to a given stream at the time of call complete.

Parameters:

**stream** ([_Stream_](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.Stream_class.html#torch.cuda.Stream "torch.cuda.Stream")
_,_ [_torch.Stream_](https://docs.pytorch.org/docs/2.15/generated/torch.Stream.html#torch.Stream "torch.Stream")
) – a stream to synchronize.

Note

This function returns without waiting for currently enqueued kernels in [`stream`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.stream_function.html#torch.cuda.stream "torch.cuda.stream")
: only future operations are affected.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.cuda.ExternalStream.rst.txt)

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