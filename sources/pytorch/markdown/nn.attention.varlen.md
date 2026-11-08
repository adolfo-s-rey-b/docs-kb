Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/nn.attention.varlen.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/nn.attention.varlen.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/nn.attention.varlen.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/nn.attention.varlen.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/nn.attention.varlen.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/nn.attention.varlen.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/nn.attention.varlen.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/nn.attention.varlen.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/nn.attention.varlen.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/nn.attention.varlen.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/nn.attention.varlen.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/nn.attention.varlen.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/nn.attention.varlen.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/nn.attention.varlen.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/nn.attention.varlen.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/nn.attention.varlen.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/nn.attention.varlen.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/nn.attention.varlen.html)
[v1.13](https://docs.pytorch.org/docs/1.13/nn.attention.varlen.html)
[v1.12](https://docs.pytorch.org/docs/1.12/nn.attention.varlen.html)
[v1.11](https://docs.pytorch.org/docs/1.11/nn.attention.varlen.html)
[v1.10](https://docs.pytorch.org/docs/1.10/nn.attention.varlen.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/nn.attention.varlen.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/nn.attention.varlen.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/nn.attention.varlen.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/nn.attention.varlen.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/nn.attention.varlen.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/nn.attention.varlen.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/nn.attention.varlen.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/nn.attention.varlen.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/nn.attention.varlen.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/nn.attention.varlen.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/nn.attention.varlen.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/nn.attention.varlen.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/nn.attention.varlen.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/nn.attention.varlen.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/nn.attention.varlen.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/nn.attention.varlen.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/nn.attention.varlen.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/nn.attention.varlen.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/nn.attention.varlen.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/nn.attention.varlen.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/nn.attention.varlen.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/nn.attention.varlen.html)

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

torch.nn.attention.varlen[#](https://docs.pytorch.org/docs/2.15/nn.attention.varlen.html#module-torch.nn.attention.varlen "Link to this heading")

==================================================================================================================================================

Created On: Oct 14, 2025 | Last Updated On: Mar 10, 2026

Variable-length attention implementation using Flash Attention.

This module provides a high-level Python interface for variable-length attention that calls into the optimized Flash Attention kernels.

torch.nn.attention.varlen.varlen\_attn(_query_, _key_, _value_, _cu\_seq\_q_, _cu\_seq\_k_, _max\_q_, _max\_k_, _\*_, _return\_aux\=None_, _scale\=None_, _window\_size\=(-1, \-1)_, _enable\_gqa\=False_, _seqused\_k\=None_, _block\_table\=None_, _num\_splits\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/attention/varlen.py#L348)
[#](https://docs.pytorch.org/docs/2.15/nn.attention.varlen.html#torch.nn.attention.varlen.varlen_attn "Link to this definition")

Compute variable-length attention using Flash Attention.

This function is similar to scaled\_dot\_product\_attention but optimized for variable-length sequences using cumulative sequence position tensors. Backend enablement follows [`torch.nn.attention.sdpa_kernel()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.attention.sdpa_kernel.html#torch.nn.attention.sdpa_kernel "torch.nn.attention.sdpa_kernel")
. By default, eligible cuDNN is preferred over Flash; `set_priority=True` overrides this order.

Parameters:

*   **query** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Query tensor; shape (Tq,Hq,D)(T\_q, H\_q, D)(Tq​,Hq​,D)
    
*   **key** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Key tensor; shape (Tk,Hkv,D)(T\_k, H\_{kv}, D)(Tk​,Hkv​,D), or (total\_pages,page\_size,Hkv,D)(\\text{total\\\_pages}, \\text{page\\\_size}, H\_{kv}, D)(total\_pages,page\_size,Hkv​,D) when `block_table` is provided.
    
*   **value** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Value tensor; shape (Tk,Hkv,D)(T\_k, H\_{kv}, D)(Tk​,Hkv​,D), or (total\_pages,page\_size,Hkv,D)(\\text{total\\\_pages}, \\text{page\\\_size}, H\_{kv}, D)(total\_pages,page\_size,Hkv​,D) when `block_table` is provided.
    
*   **cu\_seq\_q** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Cumulative sequence positions for queries; shape (N+1,)(N+1,)(N+1,)
    
*   **cu\_seq\_k** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Cumulative sequence positions for keys/values; shape (N+1,)(N+1,)(N+1,)
    
*   **max\_q** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Maximum query sequence length in the batch.
    
*   **max\_k** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Maximum key/value sequence length in the batch.
    
*   **return\_aux** (_Optional__\[_[_AuxRequest_](https://docs.pytorch.org/docs/2.15/nn.attention.varlen.html#torch.nn.attention.varlen.AuxRequest "torch.nn.attention.varlen.AuxRequest")\
    _\]_) – If not None and `return_aux.lse` is True, also returns the logsumexp tensor.
    
*   **scale** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    _,_ _optional_) – Positive scaling factor for attention scores.
    
*   **window\_size** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]__,_ _optional_) – Window size for sliding window attention as (left, right). Use (-1, -1) for full attention (default), (-1, 0) for causal attention, or (W, 0) for causal attention with sliding window of size W.
    
*   **enable\_gqa** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If set to True, enables Grouped Query Attention (GQA) and allows key/value to have fewer heads than query. Each KV head is shared by a group of Hq/HkvH\_q / H\_{kv}Hq​/Hkv​ query heads, so HqH\_qHq​ must be divisible by HkvH\_{kv}Hkv​. Default is False.
    
*   **seqused\_k** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – Number of valid KV tokens per batch element; shape (N,)(N,)(N,). When set, only the first `seqused_k[i]` tokens in the key/value sequence for batch element _i_ participate in attention. Useful for KV-cache decoding where the cache slot is larger than the actual sequence. Inference-only (not supported in backward).
    
*   **block\_table** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) –
    
    Block table for paged KV cache; shape (N,max\_pages\_per\_seq)(N, \\text{max\\\_pages\\\_per\\\_seq})(N,max\_pages\_per\_seq), dtype `int32`. Requires `seqused_k`. Inference-only (not supported in backward).
    
    When `block_table` is provided, `key` and `value` are a “pool” of pages of tokens of KV data and the pages belong to any sequence/order. The `block_table` is what maps each sequence’s logical chunks back to physical pages in this pool.
    
    `seqused_k[i]` tells the kernel how many tokens in sequence _i_ are actually valid, since the last page is typically only partially filled.
    
*   **num\_splits** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – Number of splits for split-KV. Set to `1` to disable split-KV which enables batch invariance. Split-KV parallelizes the key/value sequence dimension across multiple thread blocks and combines partial results. The split decision depends on `max_k` (the longest sequence in the batch), so different batch compositions can change the reduction order and produce different floating-point results for the same sequence. When this is disabled, bitwise identical outputs are guaranteed for a given sequence regardless of what other sequences are in the batch, at the cost of lower GPU utilization when there are few queries. When `None` (default), the kernel chooses automatically.
    

Returns:

Output tensor from attention computation; shape (Tq,Hq,D)(T\_q, H\_q, D)(Tq​,Hq​,D).

If `return_aux` is not None and `return_aux.lse` is True:

lse (Tensor): Log-sum-exp of attention scores; shape (Hq,Tq)(H\_q, T\_q)(Hq​,Tq​).

Return type:

output ([Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
)

Shape legend:

*   NNN: Batch size
    
*   TqT\_qTq​: Total number of query tokens in the batch (sum of all query sequence lengths)
    
*   TkT\_kTk​: Total number of key/value tokens in the batch (sum of all key/value sequence lengths)
    
*   HqH\_qHq​: Number of query attention heads
    
*   HkvH\_{kv}Hkv​: Number of key/value attention heads (equal to HqH\_qHq​ unless GQA is enabled)
    
*   DDD: Head dimension
    

Example:

\>>> batch\_size, max\_seq\_len, embed\_dim, num\_heads \= 2, 512, 1024, 16
\>>> head\_dim \= embed\_dim // num\_heads
\>>> seq\_lengths \= \[\]
\>>> for \_ in range(batch\_size):
...     length \= torch.randint(1, max\_seq\_len // 64 + 1, (1,)).item() \* 64
...     seq\_lengths.append(min(length, max\_seq\_len))
\>>> seq\_lengths \= torch.tensor(seq\_lengths, device\="cuda")
\>>> total\_tokens \= seq\_lengths.sum().item()
\>>>
\>>> \# Create packed query, key, value tensors
\>>> query \= torch.randn(
...     total\_tokens, num\_heads, head\_dim, dtype\=torch.float16, device\="cuda"
... )
\>>> key \= torch.randn(
...     total\_tokens, num\_heads, head\_dim, dtype\=torch.float16, device\="cuda"
... )
\>>> value \= torch.randn(
...     total\_tokens, num\_heads, head\_dim, dtype\=torch.float16, device\="cuda"
... )
\>>>
\>>> \# Build cumulative sequence tensor
\>>> cu\_seq \= torch.zeros(batch\_size + 1, device\="cuda", dtype\=torch.int32)
\>>> cu\_seq\[1:\] \= seq\_lengths.cumsum(0)
\>>> max\_len \= seq\_lengths.max().item()
\>>>
\>>> \# Call varlen\_attn
\>>> output \= varlen\_attn(
...     query, key, value, cu\_seq, cu\_seq, max\_len, max\_len
... )

Copy to clipboard

torch.nn.attention.varlen.varlen\_attn\_out(_out_, _query_, _key_, _value_, _cu\_seq\_q_, _cu\_seq\_k_, _max\_q_, _max\_k_, _\*_, _return\_aux\=None_, _scale\=None_, _window\_size\=(-1, \-1)_, _enable\_gqa\=False_, _seqused\_k\=None_, _block\_table\=None_, _num\_splits\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/attention/varlen.py#L614)
[#](https://docs.pytorch.org/docs/2.15/nn.attention.varlen.html#torch.nn.attention.varlen.varlen_attn_out "Link to this definition")

Compute variable-length attention with a pre-allocated output tensor.

Same as [`varlen_attn()`](https://docs.pytorch.org/docs/2.15/nn.attention.varlen.html#torch.nn.attention.varlen.varlen_attn "torch.nn.attention.varlen.varlen_attn")
 but writes the attention output into the provided `out` tensor instead of allocating a new one. Backend selection follows [`varlen_attn()`](https://docs.pytorch.org/docs/2.15/nn.attention.varlen.html#torch.nn.attention.varlen.varlen_attn "torch.nn.attention.varlen.varlen_attn")
; the cuDNN backend requires `out` to be 16-byte aligned with a contiguous last dimension.

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 | [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]

_class_ torch.nn.attention.varlen.AuxRequest(_lse\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/attention/varlen.py#L222)
[#](https://docs.pytorch.org/docs/2.15/nn.attention.varlen.html#torch.nn.attention.varlen.AuxRequest "Link to this definition")

Request which auxiliary outputs to compute from varlen\_attn.

Each field is a boolean indicating whether that auxiliary output should be computed.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/nn.attention.varlen.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/nn.attention.varlen.md.txt)

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