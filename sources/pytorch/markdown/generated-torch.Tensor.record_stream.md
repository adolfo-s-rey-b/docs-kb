Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.record_stream.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.Tensor.record_stream.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.record_stream.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.Tensor.record_stream.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.Tensor.record_stream.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.Tensor.record_stream.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.Tensor.record_stream.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.Tensor.record_stream.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.Tensor.record_stream.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.Tensor.record_stream.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.Tensor.record_stream.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.Tensor.record_stream.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.Tensor.record_stream.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.Tensor.record_stream.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.Tensor.record_stream.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.Tensor.record_stream.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.Tensor.record_stream.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.Tensor.record_stream.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.Tensor.record_stream.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.Tensor.record_stream.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.Tensor.record_stream.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.Tensor.record_stream.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.Tensor.record_stream.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.Tensor.record_stream.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.Tensor.record_stream.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.Tensor.record_stream.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.Tensor.record_stream.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.Tensor.record_stream.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.Tensor.record_stream.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.Tensor.record_stream.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.Tensor.record_stream.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.Tensor.record_stream.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.Tensor.record_stream.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.Tensor.record_stream.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.Tensor.record_stream.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.Tensor.record_stream.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.Tensor.record_stream.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.Tensor.record_stream.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.Tensor.record_stream.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.Tensor.record_stream.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.Tensor.record_stream.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.Tensor.record_stream.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.Tensor.record_stream.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.Tensor.record_stream.html)

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

torch.Tensor.record\_stream[#](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.record_stream.html#torch-tensor-record-stream "Link to this heading")

===============================================================================================================================================================

Tensor.record\_stream(_stream_)[#](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.record_stream.html#torch.Tensor.record_stream "Link to this definition")

Marks the tensor as having been used by this stream. When the tensor is deallocated, ensure the tensor memory is not reused for another tensor until all work queued on `stream` at the time of deallocation is complete.

Note

The caching allocator is aware of only the stream where a tensor was allocated. Due to the awareness, it already correctly manages the life cycle of tensors on only one stream. But if a tensor is used on a stream different from the stream of origin, the allocator might reuse the memory unexpectedly. Calling this method lets the allocator know which streams have used the tensor.

Warning

This method is most suitable for use cases where you are providing a function that created a tensor on a side stream, and want users to be able to make use of the tensor without having to think carefully about stream safety when making use of them. These safety guarantees come at some performance and predictability cost (analogous to the tradeoff between GC and manual memory management), so if you are in a situation where you manage the full lifetime of your tensors, you may consider instead manually managing CUDA events so that calling this method is not necessary. In particular, when you call this method, on later allocations the allocator will poll the recorded stream to see if all operations have completed yet; you can potentially race with side stream computation and non-deterministically reuse or fail to reuse memory for an allocation.

You can safely use tensors allocated on side streams without [`record_stream()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.record_stream.html#torch.Tensor.record_stream "torch.Tensor.record_stream")
; you must manually ensure that any non-creation stream uses of a tensor are synced back to the creation stream before you deallocate the tensor. As the CUDA caching allocator guarantees that the memory will only be reused with the same creation stream, this is sufficient to ensure that writes to future reallocations of the memory will be delayed until non-creation stream uses are done. (Counterintuitively, you may observe that on the CPU side we have already reallocated the tensor, even though CUDA kernels on the old tensor are still in progress. This is fine, because CUDA operations on the new tensor will appropriately wait for the old operations to complete, as they are all on the same stream.)

Concretely, this looks like this:

with torch.cuda.stream(s0):
    x \= torch.zeros(N)

s1.wait\_stream(s0)
with torch.cuda.stream(s1):
    y \= some\_comm\_op(x)

... some compute on s0 ...

\# synchronize creation stream s0 to side stream s1
\# before deallocating x
s0.wait\_stream(s1)
del x

Copy to clipboard

Note that some discretion is required when deciding when to perform `s0.wait_stream(s1)`. In particular, if we were to wait immediately after `some_comm_op`, there wouldn’t be any point in having the side stream; it would be equivalent to have run `some_comm_op` on `s0`. Instead, the synchronization must be placed at some appropriate, later point in time where you expect the side stream `s1` to have finished work. This location is typically identified via profiling, e.g., using Chrome traces produced [`torch.autograd.profiler.profile.export_chrome_trace()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.profiler.profile.export_chrome_trace.html#torch.autograd.profiler.profile.export_chrome_trace "torch.autograd.profiler.profile.export_chrome_trace")
. If you place the wait too early, work on s0 will block until `s1` has finished, preventing further overlapping of communication and computation. If you place the wait too late, you will use more memory than is strictly necessary (as you are keeping `x` live for longer.) For a concrete example of how this guidance can be applied in practice, see this post: [FSDP and CUDACachingAllocator](https://dev-discuss.pytorch.org/t/fsdp-cudacachingallocator-an-outsider-newb-perspective/1486)
.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.Tensor.record_stream.rst.txt)

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