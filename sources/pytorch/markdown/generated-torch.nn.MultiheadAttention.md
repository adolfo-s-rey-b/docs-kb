Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.MultiheadAttention.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.MultiheadAttention.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.MultiheadAttention.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.MultiheadAttention.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.MultiheadAttention.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.MultiheadAttention.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.MultiheadAttention.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.MultiheadAttention.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.MultiheadAttention.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.MultiheadAttention.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.MultiheadAttention.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.MultiheadAttention.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.MultiheadAttention.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.MultiheadAttention.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.MultiheadAttention.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.MultiheadAttention.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.MultiheadAttention.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.MultiheadAttention.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.MultiheadAttention.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.MultiheadAttention.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.MultiheadAttention.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.MultiheadAttention.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.MultiheadAttention.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.MultiheadAttention.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.MultiheadAttention.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.MultiheadAttention.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.MultiheadAttention.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.MultiheadAttention.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.MultiheadAttention.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.MultiheadAttention.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.MultiheadAttention.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.MultiheadAttention.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.MultiheadAttention.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.MultiheadAttention.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.MultiheadAttention.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.MultiheadAttention.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.MultiheadAttention.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.MultiheadAttention.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.MultiheadAttention.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.MultiheadAttention.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.MultiheadAttention.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.MultiheadAttention.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.MultiheadAttention.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.MultiheadAttention.html)

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

MultiheadAttention[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.MultiheadAttention.html#multiheadattention "Link to this heading")

===============================================================================================================================================

_class_ torch.nn.MultiheadAttention(_embed\_dim_, _num\_heads_, _dropout\=0.0_, _bias\=True_, _add\_bias\_kv\=False_, _add\_zero\_attn\=False_, _kdim\=None_, _vdim\=None_, _batch\_first\=False_, _device\=None_, _dtype\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/activation.py#L1090)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.MultiheadAttention.html#torch.nn.MultiheadAttention "Link to this definition")

Allows the model to jointly attend to information from different representation subspaces.

This MultiheadAttention layer implements the original architecture described in the [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
 paper. The intent of this layer is as a reference implementation for foundational understanding and thus it contains only limited features relative to newer architectures. Given the fast pace of innovation in transformer-like architectures, we recommend exploring this [tutorial](https://pytorch.org/tutorials/intermediate/transformer_building_blocks.html)
 to build efficient layers from building blocks in core or using higher level libraries from the [PyTorch Ecosystem](https://landscape.pytorch.org/)
.

Multi-Head Attention is defined as:

MultiHead(Q,K,V)\=Concat(head1,…,headh)WO\\text{MultiHead}(Q, K, V) = \\text{Concat}(\\text{head}\_1,\\dots,\\text{head}\_h)W^O MultiHead(Q,K,V)\=Concat(head1​,…,headh​)WO

where headi\=Attention(QWiQ,KWiK,VWiV)\\text{head}\_i = \\text{Attention}(QW\_i^Q, KW\_i^K, VW\_i^V)headi​\=Attention(QWiQ​,KWiK​,VWiV​).

`nn.MultiheadAttention` will use the optimized implementations of `scaled_dot_product_attention()` when possible.

In addition to support for the new `scaled_dot_product_attention()` function, for speeding up Inference, MHA will use fastpath inference with support for Nested Tensors, iff:

*   self attention is being computed (i.e., `query`, `key`, and `value` are the same tensor).
    
*   inputs are batched (3D) with `batch_first==True`
    
*   Either autograd is disabled (using `torch.inference_mode` or `torch.no_grad`) or no tensor argument `requires_grad`
    
*   training is disabled (using `.eval()`)
    
*   `add_bias_kv` is `False`
    
*   `add_zero_attn` is `False`
    
*   `kdim` and `vdim` are equal to `embed_dim`
    
*   if a [NestedTensor](https://pytorch.org/docs/stable/nested.html)
     is passed, neither `key_padding_mask` nor `attn_mask` is passed
    
*   autocast is disabled
    

If the optimized inference fastpath implementation is in use, a [NestedTensor](https://pytorch.org/docs/stable/nested.html)
 can be passed for `query`/`key`/`value` to represent padding more efficiently than using a padding mask. In this case, a [NestedTensor](https://pytorch.org/docs/stable/nested.html)
 will be returned, and an additional speedup proportional to the fraction of the input that is padding can be expected.

Parameters:

*   **embed\_dim** – Total dimension of the model.
    
*   **num\_heads** – Number of parallel attention heads. Note that `embed_dim` will be split across `num_heads` (i.e. each head will have dimension `embed_dim // num_heads`).
    
*   **dropout** – Dropout probability on `attn_output_weights`. Default: `0.0` (no dropout).
    
*   **bias** – If specified, adds bias to input / output projection layers. Default: `True`.
    
*   **add\_bias\_kv** – If specified, adds bias to the key and value sequences at dim=0. Default: `False`.
    
*   **add\_zero\_attn** – If specified, adds a new batch of zeros to the key and value sequences at dim=1. Default: `False`.
    
*   **kdim** – Total number of features for keys. Default: `None` (uses `kdim=embed_dim`).
    
*   **vdim** – Total number of features for values. Default: `None` (uses `vdim=embed_dim`).
    
*   **batch\_first** – If `True`, then the input and output tensors are provided as (batch, seq, feature). Default: `False` (seq, batch, feature).
    

Examples:

\>>> multihead\_attn \= nn.MultiheadAttention(embed\_dim, num\_heads)
\>>> attn\_output, attn\_output\_weights \= multihead\_attn(query, key, value)

Copy to clipboard

forward(_query_, _key_, _value_, _key\_padding\_mask\=None_, _need\_weights\=True_, _attn\_mask\=None_, _average\_attn\_weights\=True_, _is\_causal\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/activation.py#L1256)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.MultiheadAttention.html#torch.nn.MultiheadAttention.forward "Link to this definition")

Compute attention outputs using query, key, and value embeddings.

> Supports optional parameters for padding, masks and attention weights.

Parameters:

*   **query** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Query embeddings of shape (L,Eq)(L, E\_q)(L,Eq​) for unbatched input, (L,N,Eq)(L, N, E\_q)(L,N,Eq​) when `batch_first=False` or (N,L,Eq)(N, L, E\_q)(N,L,Eq​) when `batch_first=True`, where LLL is the target sequence length, NNN is the batch size, and EqE\_qEq​ is the query embedding dimension `embed_dim`. Queries are compared against key-value pairs to produce the output. See “Attention Is All You Need” for more details.
    
*   **key** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Key embeddings of shape (S,Ek)(S, E\_k)(S,Ek​) for unbatched input, (S,N,Ek)(S, N, E\_k)(S,N,Ek​) when `batch_first=False` or (N,S,Ek)(N, S, E\_k)(N,S,Ek​) when `batch_first=True`, where SSS is the source sequence length, NNN is the batch size, and EkE\_kEk​ is the key embedding dimension `kdim`. See “Attention Is All You Need” for more details.
    
*   **value** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Value embeddings of shape (S,Ev)(S, E\_v)(S,Ev​) for unbatched input, (S,N,Ev)(S, N, E\_v)(S,N,Ev​) when `batch_first=False` or (N,S,Ev)(N, S, E\_v)(N,S,Ev​) when `batch_first=True`, where SSS is the source sequence length, NNN is the batch size, and EvE\_vEv​ is the value embedding dimension `vdim`. See “Attention Is All You Need” for more details.
    
*   **key\_padding\_mask** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _|_ _None_) – If specified, a mask of shape (N,S)(N, S)(N,S) indicating which elements within `key` to ignore for the purpose of attention (i.e. treat as “padding”). For unbatched query, shape should be (S)(S)(S). Binary and float masks are supported. For a binary mask, a `True` value indicates that the corresponding `key` value will be ignored for the purpose of attention. For a float mask, it will be directly added to the corresponding `key` value.
    
*   **need\_weights** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If specified, returns `attn_output_weights` in addition to `attn_outputs`. Set `need_weights=False` to use the optimized `scaled_dot_product_attention` and achieve the best performance for MHA. Default: `True`.
    
*   **attn\_mask** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _|_ _None_) – If specified, a 2D or 3D mask preventing attention to certain positions. Must be of shape (L,S)(L, S)(L,S) or (N⋅num\_heads,L,S)(N\\cdot\\text{num\\\_heads}, L, S)(N⋅num\_heads,L,S), where NNN is the batch size, LLL is the target sequence length, and SSS is the source sequence length. A 2D mask will be broadcasted across the batch while a 3D mask allows for a different mask for each entry in the batch. Binary and float masks are supported. For a binary mask, a `True` value indicates that the corresponding position is not allowed to attend. For a float mask, the mask values will be added to the attention weight. If both attn\_mask and key\_padding\_mask are supplied, their types should match.
    
*   **average\_attn\_weights** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If true, indicates that the returned `attn_weights` should be averaged across heads. Otherwise, `attn_weights` are provided separately per head. Note that this flag only has an effect when `need_weights=True`. Default: `True` (i.e. average weights across heads)
    
*   **is\_causal** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If specified, applies a causal mask as attention mask. Default: `False`. Warning: `is_causal` provides a hint that `attn_mask` is the causal mask. Providing incorrect hints can result in incorrect execution, including forward and backward compatibility.
    

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | None\]

Outputs:

*   **attn\_output** - Attention outputs of shape (L,E)(L, E)(L,E) when input is unbatched, (L,N,E)(L, N, E)(L,N,E) when `batch_first=False` or (N,L,E)(N, L, E)(N,L,E) when `batch_first=True`, where LLL is the target sequence length, NNN is the batch size, and EEE is the embedding dimension `embed_dim`.
    
*   **attn\_output\_weights** - Only returned when `need_weights=True`. If `average_attn_weights=True`, returns attention weights averaged across heads of shape (L,S)(L, S)(L,S) when input is unbatched or (N,L,S)(N, L, S)(N,L,S), where NNN is the batch size, LLL is the target sequence length, and SSS is the source sequence length. If `average_attn_weights=False`, returns attention weights per head of shape (num\_heads,L,S)(\\text{num\\\_heads}, L, S)(num\_heads,L,S) when input is unbatched or (N,num\_heads,L,S)(N, \\text{num\\\_heads}, L, S)(N,num\_heads,L,S).
    

Note

batch\_first argument is ignored for unbatched inputs.

merge\_masks(_attn\_mask_, _key\_padding\_mask_, _query_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/activation.py#L1525)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.MultiheadAttention.html#torch.nn.MultiheadAttention.merge_masks "Link to this definition")

Determine mask type and combine masks if necessary.

If only one mask is provided, that mask and the corresponding mask type will be returned. If both masks are provided, they will be both expanded to shape `(batch_size, num_heads, seq_len, seq_len)`, combined with logical `or` and mask type 2 will be returned :param attn\_mask: attention mask of shape `(seq_len, seq_len)`, mask type 0 :param key\_padding\_mask: padding mask of shape `(batch_size, seq_len)`, mask type 1 :param query: query embeddings of shape `(batch_size, seq_len, embed_dim)`

Returns:

merged mask mask\_type: merged mask type (0, 1, or 2)

Return type:

merged\_mask

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.MultiheadAttention.rst.txt)

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