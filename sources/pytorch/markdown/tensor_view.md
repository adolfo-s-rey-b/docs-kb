Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/tensor_view.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/tensor_view.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/tensor_view.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/tensor_view.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/tensor_view.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/tensor_view.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/tensor_view.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/tensor_view.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/tensor_view.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/tensor_view.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/tensor_view.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/tensor_view.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/tensor_view.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/tensor_view.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/tensor_view.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/tensor_view.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/tensor_view.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/tensor_view.html)
[v1.13](https://docs.pytorch.org/docs/1.13/tensor_view.html)
[v1.12](https://docs.pytorch.org/docs/1.12/tensor_view.html)
[v1.11](https://docs.pytorch.org/docs/1.11/tensor_view.html)
[v1.10](https://docs.pytorch.org/docs/1.10/tensor_view.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/tensor_view.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/tensor_view.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/tensor_view.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/tensor_view.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/tensor_view.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/tensor_view.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/tensor_view.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/tensor_view.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/tensor_view.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/tensor_view.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/tensor_view.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/tensor_view.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/tensor_view.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/tensor_view.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/tensor_view.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/tensor_view.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/tensor_view.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/tensor_view.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/tensor_view.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/tensor_view.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/tensor_view.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/tensor_view.html)

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

Tensor Views[#](https://docs.pytorch.org/docs/2.15/tensor_view.html#tensor-views "Link to this heading")

=========================================================================================================

Created On: May 07, 2026 | Last Updated On: May 07, 2026

PyTorch allows a tensor to be a `View` of an existing tensor. View tensor shares the same underlying data with its base tensor. Supporting `View` avoids explicit data copy, thus allows us to do fast and memory efficient reshaping, slicing and element-wise operations.

For example, to get a view of an existing tensor `t`, you can call `t.view(...)`.

\>>> t \= torch.rand(4, 4)
\>>> b \= t.view(2, 8)
\>>> t.storage().data\_ptr() \== b.storage().data\_ptr()  \# \`t\` and \`b\` share the same underlying data.
True
\# Modifying view tensor changes base tensor as well.
\>>> b\[0\]\[0\] \= 3.14
\>>> t\[0\]\[0\]
tensor(3.14)

Copy to clipboard

Since views share underlying data with its base tensor, if you edit the data in the view, it will be reflected in the base tensor as well.

Typically a PyTorch op returns a new tensor as output, e.g. [`add()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.add.html#torch.Tensor.add "torch.Tensor.add")
. But in case of view ops, outputs are views of input tensors to avoid unnecessary data copy. No data movement occurs when creating a view, view tensor just changes the way it interprets the same data. Taking a view of contiguous tensor could potentially produce a non-contiguous tensor. Users should pay additional attention as contiguity might have implicit performance impact. [`transpose()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.transpose.html#torch.Tensor.transpose "torch.Tensor.transpose")
 is a common example.

\>>> base \= torch.tensor(\[\[0, 1\],\[2, 3\]\])
\>>> base.is\_contiguous()
True
\>>> t \= base.transpose(0, 1)  \# \`t\` is a view of \`base\`. No data movement happened here.
\# View tensors might be non-contiguous.
\>>> t.is\_contiguous()
False
\# To get a contiguous tensor, call \`.contiguous()\` to enforce
\# copying data when \`t\` is not contiguous.
\>>> c \= t.contiguous()

Copy to clipboard

For reference, here’s a full list of view ops in PyTorch:

*   Basic slicing and indexing op, e.g. `tensor[0, 2:, 1:7:2]` returns a view of base `tensor`, see note below.
    
*   [`adjoint()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.adjoint.html#torch.Tensor.adjoint "torch.Tensor.adjoint")
    
*   [`as_strided()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.as_strided.html#torch.Tensor.as_strided "torch.Tensor.as_strided")
    
*   [`detach()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.detach.html#torch.Tensor.detach "torch.Tensor.detach")
    
*   [`diagonal()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.diagonal.html#torch.Tensor.diagonal "torch.Tensor.diagonal")
    
*   [`expand()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.expand.html#torch.Tensor.expand "torch.Tensor.expand")
    
*   [`expand_as()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.expand_as.html#torch.Tensor.expand_as "torch.Tensor.expand_as")
    
*   [`movedim()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.movedim.html#torch.Tensor.movedim "torch.Tensor.movedim")
    
*   [`narrow()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.narrow.html#torch.Tensor.narrow "torch.Tensor.narrow")
    
*   [`permute()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.permute.html#torch.Tensor.permute "torch.Tensor.permute")
    
*   [`select()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.select.html#torch.Tensor.select "torch.Tensor.select")
    
*   [`squeeze()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.squeeze.html#torch.Tensor.squeeze "torch.Tensor.squeeze")
    
*   [`transpose()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.transpose.html#torch.Tensor.transpose "torch.Tensor.transpose")
    
*   [`t()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.t.html#torch.Tensor.t "torch.Tensor.t")
    
*   [`T`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor.T "torch.Tensor.T")
    
*   [`H`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor.H "torch.Tensor.H")
    
*   [`mT`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor.mT "torch.Tensor.mT")
    
*   [`mH`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor.mH "torch.Tensor.mH")
    
*   [`real`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.real.html#torch.Tensor.real "torch.Tensor.real")
    
*   [`imag`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.imag.html#torch.Tensor.imag "torch.Tensor.imag")
    
*   `view_as_real()`
    
*   [`unflatten()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.unflatten.html#torch.Tensor.unflatten "torch.Tensor.unflatten")
    
*   [`unfold()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.unfold.html#torch.Tensor.unfold "torch.Tensor.unfold")
    
*   [`unsqueeze()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.unsqueeze.html#torch.Tensor.unsqueeze "torch.Tensor.unsqueeze")
    
*   [`view()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.view.html#torch.Tensor.view "torch.Tensor.view")
    
*   [`view_as()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.view_as.html#torch.Tensor.view_as "torch.Tensor.view_as")
    
*   [`unbind()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.unbind.html#torch.Tensor.unbind "torch.Tensor.unbind")
    
*   [`split()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.split.html#torch.Tensor.split "torch.Tensor.split")
    
*   [`hsplit()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.hsplit.html#torch.Tensor.hsplit "torch.Tensor.hsplit")
    
*   [`vsplit()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.vsplit.html#torch.Tensor.vsplit "torch.Tensor.vsplit")
    
*   [`tensor_split()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.tensor_split.html#torch.Tensor.tensor_split "torch.Tensor.tensor_split")
    
*   `split_with_sizes()`
    
*   [`swapaxes()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.swapaxes.html#torch.Tensor.swapaxes "torch.Tensor.swapaxes")
    
*   [`swapdims()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.swapdims.html#torch.Tensor.swapdims "torch.Tensor.swapdims")
    
*   [`chunk()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.chunk.html#torch.Tensor.chunk "torch.Tensor.chunk")
    
*   [`indices()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.indices.html#torch.Tensor.indices "torch.Tensor.indices")
     (sparse tensor only)
    
*   [`values()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.values.html#torch.Tensor.values "torch.Tensor.values")
     (sparse tensor only)
    

Note

When accessing the contents of a tensor via indexing, PyTorch follows Numpy behaviors that basic indexing returns views, while advanced indexing returns a copy. Assignment via either basic or advanced indexing is in-place. See more examples in [Numpy indexing documentation](https://numpy.org/doc/stable/user/basics.indexing.html)
.

It’s also worth mentioning a few ops with special behaviors:

*   [`reshape()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.reshape.html#torch.Tensor.reshape "torch.Tensor.reshape")
    , [`reshape_as()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.reshape_as.html#torch.Tensor.reshape_as "torch.Tensor.reshape_as")
     and [`flatten()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.flatten.html#torch.Tensor.flatten "torch.Tensor.flatten")
     can return either a view or new tensor, user code shouldn’t rely on whether it’s view or not.
    
*   [`contiguous()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.contiguous.html#torch.Tensor.contiguous "torch.Tensor.contiguous")
     returns **itself** if input tensor is already contiguous, otherwise it returns a new contiguous tensor by copying data.
    

For a more detailed walk-through of PyTorch internal implementation, please refer to [ezyang’s blogpost about PyTorch Internals](http://blog.ezyang.com/2019/05/pytorch-internals/)
.

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/tensor_view.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/tensor_view.md.txt)

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