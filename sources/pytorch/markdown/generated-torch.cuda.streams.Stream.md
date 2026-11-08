Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Stream.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.cuda.streams.Stream.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Stream.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.cuda.streams.Stream.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.cuda.streams.Stream.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.cuda.streams.Stream.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.cuda.streams.Stream.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.cuda.streams.Stream.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.cuda.streams.Stream.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.cuda.streams.Stream.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.cuda.streams.Stream.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.cuda.streams.Stream.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.cuda.streams.Stream.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.cuda.streams.Stream.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.cuda.streams.Stream.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.cuda.streams.Stream.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.cuda.streams.Stream.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.cuda.streams.Stream.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.cuda.streams.Stream.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.cuda.streams.Stream.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.cuda.streams.Stream.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.cuda.streams.Stream.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.cuda.streams.Stream.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.cuda.streams.Stream.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.cuda.streams.Stream.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.cuda.streams.Stream.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.cuda.streams.Stream.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.cuda.streams.Stream.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.cuda.streams.Stream.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.cuda.streams.Stream.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.cuda.streams.Stream.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.cuda.streams.Stream.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.cuda.streams.Stream.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.cuda.streams.Stream.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.cuda.streams.Stream.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.cuda.streams.Stream.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.cuda.streams.Stream.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.cuda.streams.Stream.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.cuda.streams.Stream.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.cuda.streams.Stream.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.cuda.streams.Stream.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.cuda.streams.Stream.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.cuda.streams.Stream.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.cuda.streams.Stream.html)

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

Stream[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Stream.html#stream "Link to this heading")

=====================================================================================================================

_class_ torch.cuda.streams.Stream(_device\=None_, _priority\=0_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/streams.py#L17)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Stream.html#torch.cuda.streams.Stream "Link to this definition")

Wrapper around a CUDA stream.

A CUDA stream is a linear sequence of execution that belongs to a specific device, independent from other streams. It supports with statement as a context manager to ensure the operators within the with block are running on the corresponding stream. See [CUDA semantics](https://docs.pytorch.org/docs/2.15/notes/cuda.html#cuda-semantics)
 for details.

Parameters:

*   **device** ([_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
     _or_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – a device on which to allocate the stream. If `device` is `None` (default) or a negative integer, this will use the current device.
    
*   **priority** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – priority of the stream, which can be positive, 0, or negative. A lower number indicates a higher priority. By default, the priority is set to 0. If the value falls outside of the allowed priority range, it will automatically be mapped to the nearest valid priority (lowest for large positive numbers or highest for large negative numbers).
    

query()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/streams.py#L94)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Stream.html#torch.cuda.streams.Stream.query "Link to this definition")

Check if all the work submitted has been completed.

Returns:

A boolean indicating if all kernels in this stream are completed.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

record\_event(_event\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/streams.py#L79)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Stream.html#torch.cuda.streams.Stream.record_event "Link to this definition")

Record an event.

Parameters:

**event** ([_Event_](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Event.html#torch.cuda.streams.Event "torch.cuda.streams.Event")
_,_ [_torch.Event_](https://docs.pytorch.org/docs/2.15/generated/torch.Event.html#torch.Event "torch.Event")
_,_ _optional_) – event to record. If not given, a new one will be allocated.

Returns:

Recorded event.

synchronize()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/streams.py#L102)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Stream.html#torch.cuda.streams.Stream.synchronize "Link to this definition")

Wait for all the kernels in this stream to complete.

Note

This is a wrapper around `cudaStreamSynchronize()`: see [CUDA Stream documentation](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__STREAM.html)
 for more info.

wait\_event(_event_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/streams.py#L48)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Stream.html#torch.cuda.streams.Stream.wait_event "Link to this definition")

Make all future work submitted to the stream wait for an event.

Parameters:

**event** ([_Event_](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Event.html#torch.cuda.streams.Event "torch.cuda.streams.Event")
_,_ [_torch.Event_](https://docs.pytorch.org/docs/2.15/generated/torch.Event.html#torch.Event "torch.Event")
) – an event to wait for.

Note

This is a wrapper around `cudaStreamWaitEvent()`: see [CUDA Stream documentation](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__STREAM.html)
 for more info.

This function returns without waiting for `event`: only future operations are affected.

wait\_stream(_stream_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/streams.py#L65)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Stream.html#torch.cuda.streams.Stream.wait_stream "Link to this definition")

Synchronize with another stream.

All future work submitted to this stream will wait until all kernels submitted to a given stream at the time of call complete.

Parameters:

**stream** ([_Stream_](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.streams.Stream.html#torch.cuda.streams.Stream "torch.cuda.streams.Stream")
_,_ [_torch.Stream_](https://docs.pytorch.org/docs/2.15/generated/torch.Stream.html#torch.Stream "torch.Stream")
) – a stream to synchronize.

Note

This function returns without waiting for currently enqueued kernels in `stream`: only future operations are affected.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.cuda.streams.Stream.rst.txt)

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