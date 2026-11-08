Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.TransformerEncoder.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.TransformerEncoder.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.TransformerEncoder.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.TransformerEncoder.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.TransformerEncoder.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.TransformerEncoder.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.TransformerEncoder.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.TransformerEncoder.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.TransformerEncoder.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.TransformerEncoder.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.TransformerEncoder.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.TransformerEncoder.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.TransformerEncoder.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.TransformerEncoder.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.TransformerEncoder.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.TransformerEncoder.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.TransformerEncoder.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.TransformerEncoder.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.TransformerEncoder.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.TransformerEncoder.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.TransformerEncoder.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.TransformerEncoder.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.TransformerEncoder.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.TransformerEncoder.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.TransformerEncoder.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.TransformerEncoder.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.TransformerEncoder.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.TransformerEncoder.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.TransformerEncoder.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.TransformerEncoder.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.TransformerEncoder.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.TransformerEncoder.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.TransformerEncoder.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.TransformerEncoder.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.TransformerEncoder.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.TransformerEncoder.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.TransformerEncoder.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.TransformerEncoder.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.TransformerEncoder.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.TransformerEncoder.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.TransformerEncoder.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.TransformerEncoder.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.TransformerEncoder.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.TransformerEncoder.html)

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

TransformerEncoder[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.TransformerEncoder.html#transformerencoder "Link to this heading")

===============================================================================================================================================

_class_ torch.nn.TransformerEncoder(_encoder\_layer_, _num\_layers_, _norm\=None_, _enable\_nested\_tensor\=True_, _mask\_check\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/transformer.py#L320)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.TransformerEncoder.html#torch.nn.TransformerEncoder "Link to this definition")

TransformerEncoder is a stack of N encoder layers.

This TransformerEncoder layer implements the original architecture described in the [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
 paper. The intent of this layer is as a reference implementation for foundational understanding and thus it contains only limited features relative to newer Transformer architectures. Given the fast pace of innovation in transformer-like architectures, we recommend exploring this [tutorial](https://pytorch.org/tutorials/intermediate/transformer_building_blocks.html)
 to build efficient layers from building blocks in core or using higher level libraries from the [PyTorch Ecosystem](https://landscape.pytorch.org/)
.

Warning

All layers in the TransformerEncoder are initialized with the same parameters. It is recommended to manually initialize the layers after creating the TransformerEncoder instance.

Parameters:

*   **encoder\_layer** ([_TransformerEncoderLayer_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.TransformerEncoderLayer.html#torch.nn.TransformerEncoderLayer "torch.nn.TransformerEncoderLayer")
    ) – an instance of the TransformerEncoderLayer() class (required).
    
*   **num\_layers** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the number of sub-encoder-layers in the encoder (required).
    
*   **norm** ([_Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.modules.module.Module")
     _|_ _None_) – the layer normalization component (optional).
    
*   **enable\_nested\_tensor** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – if True, input will automatically convert to nested tensor (and convert back on output). This will improve the overall performance of TransformerEncoder when padding rate is high. Default: `True` (enabled).
    

Examples

\>>> encoder\_layer \= nn.TransformerEncoderLayer(
...     d\_model\=512, nhead\=8, batch\_first\=True
... )
\>>> transformer\_encoder \= nn.TransformerEncoder(encoder\_layer, num\_layers\=6)
\>>> src \= torch.rand(32, 10, 512)
\>>> out \= transformer\_encoder(src)

Copy to clipboard

forward(_src_, _mask\=None_, _src\_key\_padding\_mask\=None_, _is\_causal\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/transformer.py#L409)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.TransformerEncoder.html#torch.nn.TransformerEncoder.forward "Link to this definition")

Pass the input through the encoder layers in turn.

Parameters:

*   **src** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the sequence to the encoder (required).
    
*   **mask** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _|_ _None_) – the mask for the src sequence (optional).
    
*   **src\_key\_padding\_mask** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _|_ _None_) – the mask for the src keys per batch (optional).
    
*   **is\_causal** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
     _|_ _None_) – If specified, applies a causal mask as `mask`. Default: `None`; try to detect a causal mask. Warning: `is_causal` provides a hint that `mask` is the causal mask. Providing incorrect hints can result in incorrect execution, including forward and backward compatibility.
    

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Shape:

see the docs in [`Transformer`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Transformer.html#torch.nn.Transformer "torch.nn.Transformer")
.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.TransformerEncoder.rst.txt)

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