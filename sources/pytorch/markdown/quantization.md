Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/quantization.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/quantization.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/quantization.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/quantization.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/quantization.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/quantization.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/quantization.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/quantization.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/quantization.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/quantization.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/quantization.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/quantization.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/quantization.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/quantization.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/quantization.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/quantization.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/quantization.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/quantization.html)
[v1.13](https://docs.pytorch.org/docs/1.13/quantization.html)
[v1.12](https://docs.pytorch.org/docs/1.12/quantization.html)
[v1.11](https://docs.pytorch.org/docs/1.11/quantization.html)
[v1.10](https://docs.pytorch.org/docs/1.10/quantization.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/quantization.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/quantization.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/quantization.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/quantization.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/quantization.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/quantization.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/quantization.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/quantization.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/quantization.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/quantization.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/quantization.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/quantization.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/quantization.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/quantization.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/quantization.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/quantization.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/quantization.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/quantization.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/quantization.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/quantization.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/quantization.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/quantization.html)

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

Quantization[#](https://docs.pytorch.org/docs/2.15/quantization.html#module-torch.ao.quantization "Link to this heading")

==========================================================================================================================

Created On: Oct 09, 2019 | Last Updated On: May 11, 2026

We are centralizing all quantization related development to [torchao](https://github.com/pytorch/ao)
, please checkout our new doc page: [https://docs.pytorch.org/ao/stable/index.html](https://docs.pytorch.org/ao/stable/index.html)

Plan for the existing quantization flows:

1.  **Eager mode quantization** (`torch.ao.quantization.quantize`, `torch.ao.quantization.quantize_dynamic`): please migrate to use torchao eager mode [`quantize_`](https://docs.pytorch.org/ao/main/api_reference/generated/torchao.quantization.quantize_.html#torchao.quantization.quantize_)
     API instead.
    
2.  **FX graph mode quantization** (`torch.ao.quantization.quantize_fx.prepare_fx`, `torch.ao.quantization.quantize_fx.convert_fx`): please migrate to use torchao pt2e quantization API instead (`torchao.quantization.pt2e.quantize_pt2e.prepare_pt2e`, `torchao.quantization.pt2e.quantize_pt2e.convert_pt2e`).
    
3.  **pt2e quantization** has been migrated to torchao ([pytorch/ao](https://github.com/pytorch/ao/tree/main/torchao/quantization/pt2e)
    ); see [pytorch/ao#2259](https://github.com/pytorch/ao/issues/2259)
     for more details.
    

We plan to delete `torch.ao.quantization` in 2.10 if there are no blockers, or in the earliest PyTorch version until all the blockers are cleared.

Quantization API Reference (Kept since APIs are still public)[#](https://docs.pytorch.org/docs/2.15/quantization.html#quantization-api-reference-kept-since-apis-are-still-public "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [Quantization API Reference](https://docs.pytorch.org/docs/2.15/quantization-support.html)
 contains documentation of quantization APIs, such as quantization passes, quantized tensor operations, and supported quantized modules and functions.

torch.ao.ns.fx.utils.compute\_sqnr(_x_, _y_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/ao/ns/fx/utils.py#L441)
[#](https://docs.pytorch.org/docs/2.15/quantization.html#torch.ao.ns.fx.utils.compute_sqnr "Link to this definition")

torch.ao.ns.fx.utils.compute\_normalized\_l2\_error(_x_, _y_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/ao/ns/fx/utils.py#L441)
[#](https://docs.pytorch.org/docs/2.15/quantization.html#torch.ao.ns.fx.utils.compute_normalized_l2_error "Link to this definition")

torch.ao.ns.fx.utils.compute\_cosine\_similarity(_x_, _y_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/ao/ns/fx/utils.py#L441)
[#](https://docs.pytorch.org/docs/2.15/quantization.html#torch.ao.ns.fx.utils.compute_cosine_similarity "Link to this definition")

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/quantization.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/quantization.md.txt)

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