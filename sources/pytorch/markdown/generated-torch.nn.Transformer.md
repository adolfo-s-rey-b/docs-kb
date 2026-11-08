Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Transformer.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.Transformer.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Transformer.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.Transformer.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.Transformer.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.Transformer.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.Transformer.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.Transformer.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.Transformer.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.Transformer.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.Transformer.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.Transformer.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.Transformer.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.Transformer.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.Transformer.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.Transformer.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.Transformer.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.Transformer.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.Transformer.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.Transformer.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.Transformer.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.Transformer.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.Transformer.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.Transformer.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.Transformer.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.Transformer.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.Transformer.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.Transformer.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.Transformer.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.Transformer.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.Transformer.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.Transformer.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.Transformer.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.Transformer.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.Transformer.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.Transformer.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.Transformer.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.Transformer.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.Transformer.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.Transformer.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.Transformer.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.Transformer.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.Transformer.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.Transformer.html)

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

Transformer[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Transformer.html#transformer "Link to this heading")

==========================================================================================================================

_class_ torch.nn.Transformer(_d\_model=512_, _nhead=8_, _num\_encoder\_layers=6_, _num\_decoder\_layers=6_, _dim\_feedforward=2048_, _dropout=0.1_, _activation=<function relu>_, _custom\_encoder=None_, _custom\_decoder=None_, _layer\_norm\_eps=1e-05_, _batch\_first=False_, _norm\_first=False_, _bias=True_, _device=None_, _dtype=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/transformer.py#L58)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Transformer.html#torch.nn.Transformer "Link to this definition")

A basic transformer layer.

This Transformer layer implements the original Transformer architecture described in the [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
 paper. The intent of this layer is as a reference implementation for foundational understanding and thus it contains only limited features relative to newer Transformer architectures. Given the fast pace of innovation in transformer-like architectures, we recommend exploring this [tutorial](https://pytorch.org/tutorials/intermediate/transformer_building_blocks.html)
 to build an efficient transformer layer from building blocks in core or using higher level libraries from the [PyTorch Ecosystem](https://landscape.pytorch.org/)
.

Parameters:

*   **d\_model** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the number of expected features in the encoder/decoder inputs (default=512).
    
*   **nhead** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the number of heads in the multiheadattention models (default=8).
    
*   **num\_encoder\_layers** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the number of sub-encoder-layers in the encoder (default=6).
    
*   **num\_decoder\_layers** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the number of sub-decoder-layers in the decoder (default=6).
    
*   **dim\_feedforward** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the dimension of the feedforward network model (default=2048).
    
*   **dropout** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – the dropout value (default=0.1).
    
*   **activation** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ [_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
    _\[__\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]__,_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]_) – the activation function of encoder/decoder intermediate layer, can be a string (“relu” or “gelu”) or a unary callable. Default: relu
    
*   **custom\_encoder** ([_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")
     _|_ _None_) – custom encoder (default=None).
    
*   **custom\_decoder** ([_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")
     _|_ _None_) – custom decoder (default=None).
    
*   **layer\_norm\_eps** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – the eps value in layer normalization components (default=1e-5).
    
*   **batch\_first** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True`, then the input and output tensors are provided as (batch, seq, feature). Default: `False` (seq, batch, feature).
    
*   **norm\_first** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – if `True`, encoder and decoder layers will perform LayerNorms before other attention and feedforward operations, otherwise after. Default: `False` (after).
    
*   **bias** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If set to `False`, `Linear` and `LayerNorm` layers will not learn an additive bias. Default: `True`.
    

Examples

\>>> transformer\_model \= nn.Transformer(
...     nhead\=16, num\_encoder\_layers\=12, batch\_first\=True
... )
\>>> src \= torch.rand((32, 10, 512))
\>>> tgt \= torch.rand((32, 20, 512))
\>>> out \= transformer\_model(src, tgt)

Copy to clipboard

Note: A full example to apply nn.Transformer module for the word language model is available in [pytorch/examples](https://github.com/pytorch/examples/tree/master/word_language_model)

forward(_src_, _tgt_, _src\_mask\=None_, _tgt\_mask\=None_, _memory\_mask\=None_, _src\_key\_padding\_mask\=None_, _tgt\_key\_padding\_mask\=None_, _memory\_key\_padding\_mask\=None_, _src\_is\_causal\=None_, _tgt\_is\_causal\=None_, _memory\_is\_causal\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/transformer.py#L181)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Transformer.html#torch.nn.Transformer.forward "Link to this definition")

Take in and process masked source/target sequences.

Note

If a boolean tensor is provided for any of the \[src/tgt/memory\]\_mask arguments, positions with a `True` value are not allowed to participate in the attention, which is the opposite of the definition for `attn_mask` in [`torch.nn.functional.scaled_dot_product_attention()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.scaled_dot_product_attention.html#torch.nn.functional.scaled_dot_product_attention "torch.nn.functional.scaled_dot_product_attention")
.

Parameters:

*   **src** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the sequence to the encoder (required).
    
*   **tgt** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the sequence to the decoder (required).
    
*   **src\_mask** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _|_ _None_) – the additive mask for the src sequence (optional).
    
*   **tgt\_mask** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _|_ _None_) – the additive mask for the tgt sequence (optional).
    
*   **memory\_mask** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _|_ _None_) – the additive mask for the encoder output (optional).
    
*   **src\_key\_padding\_mask** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _|_ _None_) – the Tensor mask for src keys per batch (optional).
    
*   **tgt\_key\_padding\_mask** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _|_ _None_) – the Tensor mask for tgt keys per batch (optional).
    
*   **memory\_key\_padding\_mask** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _|_ _None_) – the Tensor mask for memory keys per batch (optional).
    
*   **src\_is\_causal** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
     _|_ _None_) – If specified, applies a causal mask as `src_mask`. Default: `None`; try to detect a causal mask. Warning: `src_is_causal` provides a hint that `src_mask` is the causal mask. Providing incorrect hints can result in incorrect execution, including forward and backward compatibility.
    
*   **tgt\_is\_causal** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
     _|_ _None_) – If specified, applies a causal mask as `tgt_mask`. Default: `None`; try to detect a causal mask. Warning: `tgt_is_causal` provides a hint that `tgt_mask` is the causal mask. Providing incorrect hints can result in incorrect execution, including forward and backward compatibility.
    
*   **memory\_is\_causal** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If specified, applies a causal mask as `memory_mask`. Default: `False`. Warning: `memory_is_causal` provides a hint that `memory_mask` is the causal mask. Providing incorrect hints can result in incorrect execution, including forward and backward compatibility.
    

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Shape:

*   src: (S,E)(S, E)(S,E) for unbatched input, (S,N,E)(S, N, E)(S,N,E) if batch\_first=False or (N, S, E) if batch\_first=True.
    
*   tgt: (T,E)(T, E)(T,E) for unbatched input, (T,N,E)(T, N, E)(T,N,E) if batch\_first=False or (N, T, E) if batch\_first=True.
    
*   src\_mask: (S,S)(S, S)(S,S) or (N⋅num\_heads,S,S)(N\\cdot\\text{num\\\_heads}, S, S)(N⋅num\_heads,S,S).
    
*   tgt\_mask: (T,T)(T, T)(T,T) or (N⋅num\_heads,T,T)(N\\cdot\\text{num\\\_heads}, T, T)(N⋅num\_heads,T,T).
    
*   memory\_mask: (T,S)(T, S)(T,S).
    
*   src\_key\_padding\_mask: (S)(S)(S) for unbatched input otherwise (N,S)(N, S)(N,S).
    
*   tgt\_key\_padding\_mask: (T)(T)(T) for unbatched input otherwise (N,T)(N, T)(N,T).
    
*   memory\_key\_padding\_mask: (S)(S)(S) for unbatched input otherwise (N,S)(N, S)(N,S).
    

Note: \[src/tgt/memory\]\_mask ensures that position iii is allowed to attend the unmasked positions. If a BoolTensor is provided, positions with `True` are not allowed to attend while `False` values will be unchanged. If a FloatTensor is provided, it will be added to the attention weight. \[src/tgt/memory\]\_key\_padding\_mask provides specified elements in the key to be ignored by the attention. If a BoolTensor is provided, the positions with the value of `True` will be ignored while the position with the value of `False` will be unchanged.

*   output: (T,E)(T, E)(T,E) for unbatched input, (T,N,E)(T, N, E)(T,N,E) if batch\_first=False or (N, T, E) if batch\_first=True.
    

Note: Due to the multi-head attention architecture in the transformer model, the output sequence length of a transformer is same as the input sequence (i.e. target) length of the decoder.

where SSS is the source sequence length, TTT is the target sequence length, NNN is the batch size, EEE is the feature number

Examples

\>>> output \= transformer\_model(
...     src, tgt, src\_mask\=src\_mask, tgt\_mask\=tgt\_mask
... )

Copy to clipboard

_static_ generate\_square\_subsequent\_mask(_sz_, _device\=None_, _dtype\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/transformer.py#L301)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Transformer.html#torch.nn.Transformer.generate_square_subsequent_mask "Link to this definition")

Generate a square causal mask for the sequence.

The masked positions are filled with float(‘-inf’). Unmasked positions are filled with float(0.0).

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.Transformer.rst.txt)

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