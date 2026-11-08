Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.histc.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.histc.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.histc.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.histc.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.histc.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.histc.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.histc.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.histc.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.histc.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.histc.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.histc.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.histc.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.histc.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.histc.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.histc.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.histc.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.histc.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.histc.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.histc.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.histc.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.histc.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.histc.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.histc.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.histc.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.histc.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.histc.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.histc.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.histc.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.histc.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.histc.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.histc.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.histc.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.histc.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.histc.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.histc.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.histc.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.histc.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.histc.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.histc.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.histc.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.histc.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.histc.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.histc.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.histc.html)

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

torch.histc[#](https://docs.pytorch.org/docs/2.15/generated/torch.histc.html#torch-histc "Link to this heading")

=================================================================================================================

torch.histc(_input_, _bins\=100_, _min\=0_, _max\=0_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.histc.html#torch.histc "Link to this definition")

Computes the histogram of a tensor.

The elements are sorted into equal width bins between [`min`](https://docs.pytorch.org/docs/2.15/generated/torch.min.html#torch.min "torch.min")
 and [`max`](https://docs.pytorch.org/docs/2.15/generated/torch.max.html#torch.max "torch.max")
. If [`min`](https://docs.pytorch.org/docs/2.15/generated/torch.min.html#torch.min "torch.min")
 and [`max`](https://docs.pytorch.org/docs/2.15/generated/torch.max.html#torch.max "torch.max")
 are both zero, the minimum and maximum values of the data are used.

Elements lower than min and higher than max and `NaN` elements are ignored.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor.
    
*   **bins** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – number of histogram bins
    
*   **min** (_Scalar_) – lower end of the range (inclusive)
    
*   **max** (_Scalar_) – upper end of the range (inclusive)
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Returns:

Histogram represented as a tensor

Return type:

[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Example:

\>>> torch.histc(torch.tensor(\[1., 2, 1\]), bins\=4, min\=0, max\=3)
tensor(\[ 0.,  2.,  1.,  0.\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.histc.rst.txt)

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