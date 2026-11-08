Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.bilinear.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.bilinear.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.bilinear.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.bilinear.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.bilinear.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.bilinear.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.bilinear.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.bilinear.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.bilinear.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.bilinear.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.bilinear.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.bilinear.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.bilinear.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.bilinear.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.bilinear.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.bilinear.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.bilinear.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.bilinear.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.bilinear.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.bilinear.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.bilinear.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.bilinear.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.bilinear.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.bilinear.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.bilinear.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.bilinear.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.bilinear.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.bilinear.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.bilinear.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.bilinear.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.bilinear.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.bilinear.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.bilinear.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.bilinear.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.bilinear.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.bilinear.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.bilinear.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.bilinear.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.bilinear.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.bilinear.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.bilinear.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.bilinear.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.bilinear.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.bilinear.html)

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

torch.bilinear[#](https://docs.pytorch.org/docs/2.15/generated/torch.bilinear.html#torch-bilinear "Link to this heading")

==========================================================================================================================

torch.bilinear(_input1_, _input2_, _weight_, _bias\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.bilinear.html#torch.bilinear "Link to this definition")

Applies a bilinear transformation to the incoming data: y\=x1TAx2+by = x\_1^T A x\_2 + by\=x1T​Ax2​+b

Shape:

> *   input1: (N,∗,Hin1)(N, \*, H\_{in1})(N,∗,Hin1​) where Hin1\=in1\_featuresH\_{in1}=\\text{in1\\\_features}Hin1​\=in1\_features and ∗\*∗ means any number of additional dimensions. All but the last dimension of the inputs should be the same.
>     
> *   input2: (N,∗,Hin2)(N, \*, H\_{in2})(N,∗,Hin2​) where Hin2\=in2\_featuresH\_{in2}=\\text{in2\\\_features}Hin2​\=in2\_features
>     
> *   weight: (out\_features,in1\_features,in2\_features)(\\text{out\\\_features}, \\text{in1\\\_features}, \\text{in2\\\_features})(out\_features,in1\_features,in2\_features)
>     
> *   bias: (out\_features)(\\text{out\\\_features})(out\_features)
>     
> *   output: (N,∗,Hout)(N, \*, H\_{out})(N,∗,Hout​) where Hout\=out\_featuresH\_{out}=\\text{out\\\_features}Hout​\=out\_features and all but the last dimension are the same shape as the input.
>     

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.bilinear.rst.txt)

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