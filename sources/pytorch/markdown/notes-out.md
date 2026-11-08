Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/notes/out.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/notes/out.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/notes/out.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/notes/out.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/notes/out.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/notes/out.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/notes/out.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/notes/out.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/notes/out.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/notes/out.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/notes/out.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/notes/out.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/notes/out.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/notes/out.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/notes/out.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/notes/out.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/notes/out.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/notes/out.html)
[v1.13](https://docs.pytorch.org/docs/1.13/notes/out.html)
[v1.12](https://docs.pytorch.org/docs/1.12/notes/out.html)
[v1.11](https://docs.pytorch.org/docs/1.11/notes/out.html)
[v1.10](https://docs.pytorch.org/docs/1.10/notes/out.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/notes/out.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/notes/out.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/notes/out.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/notes/out.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/notes/out.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/notes/out.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/notes/out.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/notes/out.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/notes/out.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/notes/out.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/notes/out.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/notes/out.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/notes/out.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/notes/out.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/notes/out.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/notes/out.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/notes/out.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/notes/out.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/notes/out.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/notes/out.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/notes/out.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/notes/out.html)

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

Out Notes[#](https://docs.pytorch.org/docs/2.15/notes/out.html#out-notes "Link to this heading")

=================================================================================================

Created On: Apr 24, 2025 | Last Updated On: May 07, 2026

When a user passes one or more tensors to out= the contract is as follows:

*   if an out tensor has no elements it will be resized to the shape, stride, and memory format of the output of the computation.
    
*   if an out tensor has a different shape than the result of the computation an error is thrown OR the out tensor is resized to the same shape, stride, and memory format of the output computation, just like a tensor with no elements. (This resizing behavior is deprecated and PyTorch is updating its operators to consistently throw an error.)
    
*   passing out= tensors with the correct shape is numerically equivalent to performing the operation and “safe copying” its results to the (possibly resized) out tensor. In this case strides and memory format are preserved.
    
*   passing out= tensors with grad needed is not supported.
    
*   if multiple tensors are passed to out= then the above behavior applies to each independently.
    

A “safe copy” is different from PyTorch’s regular copy. For operations that do not participate in type promotion the device and dtype of the source and destination tensors must match. For operations that do participate in type promotion the copy can be to a different dtype, but the destination of the copy cannot be a lower “type kind” than the source. PyTorch has four type kinds: boolean, integer, float, and complex, in that order. So, for example, an operation like add (which participates in type promotion) will throw a runtime error if given float inputs but an integer out= tensor.

Note that while the numerics of out= for correctly shaped tensors are that the operation is performed and then its results are “safe copied,” behind the scenes operations may reuse the storage of out= tensors and fuse the copy for efficiency. Many operations, like add, perform these optimizations. Also, while PyTorch’s “out= contract” is specified above, many operations in PyTorch do not correctly implement the contract and need to be updated.

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/notes/out.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/notes/out.md.txt)

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