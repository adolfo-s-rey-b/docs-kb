Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/nn.attention.flex_attention.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/nn.attention.flex_attention.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/nn.attention.flex_attention.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/nn.attention.flex_attention.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/nn.attention.flex_attention.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/nn.attention.flex_attention.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/nn.attention.flex_attention.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/nn.attention.flex_attention.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/nn.attention.flex_attention.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/nn.attention.flex_attention.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/nn.attention.flex_attention.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/nn.attention.flex_attention.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/nn.attention.flex_attention.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/nn.attention.flex_attention.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/nn.attention.flex_attention.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/nn.attention.flex_attention.html)
[v1.13](https://docs.pytorch.org/docs/1.13/nn.attention.flex_attention.html)
[v1.12](https://docs.pytorch.org/docs/1.12/nn.attention.flex_attention.html)
[v1.11](https://docs.pytorch.org/docs/1.11/nn.attention.flex_attention.html)
[v1.10](https://docs.pytorch.org/docs/1.10/nn.attention.flex_attention.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/nn.attention.flex_attention.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/nn.attention.flex_attention.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/nn.attention.flex_attention.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/nn.attention.flex_attention.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/nn.attention.flex_attention.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/nn.attention.flex_attention.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/nn.attention.flex_attention.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/nn.attention.flex_attention.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/nn.attention.flex_attention.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/nn.attention.flex_attention.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/nn.attention.flex_attention.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/nn.attention.flex_attention.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/nn.attention.flex_attention.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/nn.attention.flex_attention.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/nn.attention.flex_attention.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/nn.attention.flex_attention.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/nn.attention.flex_attention.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/nn.attention.flex_attention.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/nn.attention.flex_attention.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/nn.attention.flex_attention.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/nn.attention.flex_attention.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/nn.attention.flex_attention.html)

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

torch.nn.attention.flex\_attention[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#module-torch.nn.attention.flex_attention "Link to this heading")

===========================================================================================================================================================================

Created On: Jul 16, 2024 | Last Updated On: Aug 07, 2026

torch.nn.attention.flex\_attention.flex\_attention(_query: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _key: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _value: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _score\_mod: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\], [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\] | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _block\_mask: [BlockMask](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask "torch.nn.attention.flex_attention.BlockMask")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _scale: [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _enable\_gqa: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= False_, _return\_lse: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.15)")
\[False\] \= False_, _kernel\_options: [FlexKernelOptions](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions "torch.nn.attention.flex_attention.FlexKernelOptions")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _\*_, _return\_aux: [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/attention/flex_attention.py#L2390)
[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.flex_attention "Link to this definition")

torch.nn.attention.flex\_attention.flex\_attention(_query: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _key: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _value: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _score\_mod: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\], [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\] | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _block\_mask: [BlockMask](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask "torch.nn.attention.flex_attention.BlockMask")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _scale: [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _enable\_gqa: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= False_, _return\_lse: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.15)")
\[True\] \= False_, _kernel\_options: [FlexKernelOptions](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions "torch.nn.attention.flex_attention.FlexKernelOptions")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _\*_, _return\_aux: [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_) → [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]

torch.nn.attention.flex\_attention.flex\_attention(_query: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _key: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _value: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _score\_mod: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\], [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\] | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _block\_mask: [BlockMask](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask "torch.nn.attention.flex_attention.BlockMask")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _scale: [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _enable\_gqa: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= False_, _return\_lse: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= False_, _kernel\_options: [FlexKernelOptions](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions "torch.nn.attention.flex_attention.FlexKernelOptions")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _\*_, _return\_aux: [AuxRequest](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.AuxRequest "torch.nn.attention.flex_attention.AuxRequest")
_) → [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [AuxOutput](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.AuxOutput "torch.nn.attention.flex_attention.AuxOutput")\
\]

torch.nn.attention.flex\_attention.flex\_attention(_query: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _key: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _value: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _score\_mod: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\], [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\] | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _block\_mask: [BlockMask](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask "torch.nn.attention.flex_attention.BlockMask")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _scale: [float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _enable\_gqa: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= False_, _return\_lse: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.15)")
\[True\] \= False_, _kernel\_options: [FlexKernelOptions](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions "torch.nn.attention.flex_attention.FlexKernelOptions")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _\*_, _return\_aux: [AuxRequest](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.AuxRequest "torch.nn.attention.flex_attention.AuxRequest")
_) → [Never](https://docs.python.org/3/library/typing.html#typing.Never "(in Python v3.15)")

This function implements scaled dot product attention with an arbitrary attention score modification function described in the [Flex Attention](https://arxiv.org/abs/2412.05496)
 paper. See also the [blog post](https://pytorch.org/blog/flexattention/)
.

This function computes the scaled dot product attention between query, key, and value tensors with a user-defined attention score modification function. The attention score modification function will be applied after the attention scores have been calculated between the query and key tensors. The attention scores are calculated as follows:

The `score_mod` function should have the following signature:

def score\_mod(
    score: Tensor,
    batch: Tensor,
    head: Tensor,
    q\_idx: Tensor,
    k\_idx: Tensor
) \-> Tensor:

Copy to clipboard

Where:

*   `score`: A scalar tensor representing the attention score, with the same data type and device as the query, key, and value tensors.
    
*   `batch`, `head`, `q_idx`, `k_idx`: Scalar tensors indicating the batch index, query head index, query index, and key/value index, respectively. These should have the `torch.int` data type and be located on the same device as the score tensor.
    

Parameters:

*   **query** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Query tensor; shape (B,Hq,L,E)(B, Hq, L, E)(B,Hq,L,E). For FP8 dtypes, should be in row-major memory layout for optimal performance.
    
*   **key** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Key tensor; shape (B,Hkv,S,E)(B, Hkv, S, E)(B,Hkv,S,E). For FP8 dtypes, should be in row-major memory layout for optimal performance.
    
*   **value** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Value tensor; shape (B,Hkv,S,Ev)(B, Hkv, S, Ev)(B,Hkv,S,Ev). For FP8 dtypes, should be in column-major memory layout for optimal performance.
    
*   **score\_mod** (_Optional__\[__Callable__\]_) – Function to modify attention scores. By default no score\_mod is applied.
    
*   **block\_mask** (_Optional__\[_[_BlockMask_](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask "torch.nn.attention.flex_attention.BlockMask")\
    _\]_) – BlockMask object that controls the blocksparsity pattern of the attention.
    
*   **scale** (_Optional__\[_[_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
    _\]_) – Scaling factor applied prior to softmax. If none, the default value is set to 1E\\frac{1}{\\sqrt{E}}E​1​.
    
*   **enable\_gqa** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If set to True, enables Grouped Query Attention (GQA) and broadcasts key/value heads to query heads.
    
*   **return\_lse** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether to return the logsumexp of the attention scores. Default is False. **Deprecated**: Use `return_aux=AuxRequest(lse=True)` instead.
    
*   **kernel\_options** (_Optional__\[_[_FlexKernelOptions_](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions "torch.nn.attention.flex_attention.FlexKernelOptions")\
    _\]_) – Options to control the behavior of the underlying Triton kernels. See [`FlexKernelOptions`](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions "torch.nn.attention.flex_attention.FlexKernelOptions")
     for available options and usage examples.
    
*   **return\_aux** (_Optional__\[_[_AuxRequest_](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.AuxRequest "torch.nn.attention.flex_attention.AuxRequest")\
    _\]_) – Specifies which auxiliary outputs to compute and return. If None, only the attention output is returned. Use `AuxRequest(lse=True, max_scores=True)` to request both auxiliary outputs.
    

Returns:

Attention output; shape (B,Hq,L,Ev)(B, Hq, L, Ev)(B,Hq,L,Ev).

When `return_aux` is not None:

aux (AuxOutput): Auxiliary outputs with requested fields populated.

When `return_aux` is None (deprecated paths):

lse (Tensor): Log-sum-exp of attention scores; shape (B,Hq,L)(B, Hq, L)(B,Hq,L). Only returned if `return_lse=True`.

Return type:

output ([Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
)

Shape legend:

*   N:Batch size...:Any number of other batch dimensions (optional)N: \\text{Batch size} ... : \\text{Any number of other batch dimensions (optional)}N:Batch size...:Any number of other batch dimensions (optional)
    
*   S:Source sequence lengthS: \\text{Source sequence length}S:Source sequence length
    
*   L:Target sequence lengthL: \\text{Target sequence length}L:Target sequence length
    
*   E:Embedding dimension of the query and keyE: \\text{Embedding dimension of the query and key}E:Embedding dimension of the query and key
    
*   Ev:Embedding dimension of the valueEv: \\text{Embedding dimension of the value}Ev:Embedding dimension of the value
    

Warning

torch.nn.attention.flex\_attention is a prototype feature in PyTorch. Please look forward to a more stable implementation in a future version of PyTorch. Read more about feature classification at: [https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype](https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype)

_class_ torch.nn.attention.flex\_attention.AuxOutput(_lse\=None_, _max\_scores\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/attention/flex_attention.py#L318)
[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.AuxOutput "Link to this definition")

Auxiliary outputs from flex\_attention operation.

Fields will be None if not requested, or contain the tensor if requested.

_class_ torch.nn.attention.flex\_attention.AuxRequest(_lse\=False_, _max\_scores\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/attention/flex_attention.py#L308)
[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.AuxRequest "Link to this definition")

Request which auxiliary outputs to compute from flex\_attention.

Each field is a boolean indicating whether that auxiliary output should be computed.

BlockMask Utilities[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#blockmask-utilities "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

torch.nn.attention.flex\_attention.create\_block\_mask(_mask\_mod_, _B_, _H_, _Q\_LEN_, _KV\_LEN_, _device\=None_, _BLOCK\_SIZE\=128_, _\_compile\=False_, _separate\_full\_blocks\=True_, _compute\_dq\_write\_order\=False_, _dq\_kv\_order\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/attention/flex_attention.py#L1992)
[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.create_block_mask "Link to this definition")

This function creates a block mask tuple from a mask\_mod function.

Parameters:

*   **mask\_mod** (_Callable_) – mask\_mod function. This is a callable that defines the masking pattern for the attention mechanism. It takes four arguments: b (batch size), h (number of heads), q\_idx (query index), and kv\_idx (key/value index). It should return a boolean tensor indicating which attention connections are allowed (True) or masked out (False).
    
*   **B** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Batch size.
    
*   **H** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Number of query heads.
    
*   **Q\_LEN** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Sequence length of query.
    
*   **KV\_LEN** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Sequence length of key/value.
    
*   **device** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Device to run the mask creation on.
    
*   **BLOCK\_SIZE** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – Block size for the block mask. If a single int is provided it is used for both query and key/value.
    
*   **separate\_full\_blocks** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If True, fully unmasked blocks are stored separately so kernels can skip mask\_mod on those blocks. If False, all non-empty blocks are stored as partial blocks and mask\_mod is applied to every block.
    
*   **compute\_dq\_write\_order** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If True, precompute dQ write-order metadata needed by deterministic block-sparse FLASH backward.
    
*   **dq\_kv\_order** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – KV-column scheduler order used for deterministic dQ accumulation when compute\_dq\_write\_order is True. False means ascending n-block order and True means descending/SPT order. Explicit tensor schedules are not supported by create\_block\_mask yet; they are supported by BlockMask.from\_kv\_blocks for callers that provide precomputed write-order metadata directly.
    

Returns:

A BlockMask object that contains the block mask information.

Return type:

[BlockMask](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask "torch.nn.attention.flex_attention.BlockMask")

Example Usage:

def causal\_mask(b, h, q\_idx, kv\_idx):
    return q\_idx \>= kv\_idx

block\_mask \= create\_block\_mask(causal\_mask, 1, 1, 8192, 8192, device\="cuda")
query \= torch.randn(1, 1, 8192, 64, device\="cuda", dtype\=torch.float16)
key \= torch.randn(1, 1, 8192, 64, device\="cuda", dtype\=torch.float16)
value \= torch.randn(1, 1, 8192, 64, device\="cuda", dtype\=torch.float16)
output \= flex\_attention(query, key, value, block\_mask\=block\_mask)

Copy to clipboard

torch.nn.attention.flex\_attention.create\_mask(_mod\_fn_, _B_, _H_, _Q\_LEN_, _KV\_LEN_, _device\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/attention/flex_attention.py#L1853)
[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.create_mask "Link to this definition")

This function creates a mask tensor from a mod\_fn function.

Parameters:

*   **mod\_fn** (_Union__\[__\_score\_mod\_signature__,_ _\_mask\_mod\_signature__\]_) – Function to modify attention scores.
    
*   **B** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Batch size.
    
*   **H** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Number of query heads.
    
*   **Q\_LEN** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Sequence length of query.
    
*   **KV\_LEN** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Sequence length of key/value.
    
*   **device** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Device to run the mask creation on.
    

Returns:

A mask tensor with shape (B, H, M, N).

Return type:

mask ([Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
)

torch.nn.attention.flex\_attention.and\_masks(_\*mask\_mods_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/attention/flex_attention.py#L1798)
[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.and_masks "Link to this definition")

Returns a mask\_mod that’s the intersection of provided mask\_mods

Return type:

[_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\], [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]

torch.nn.attention.flex\_attention.or\_masks(_\*mask\_mods_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/attention/flex_attention.py#L1784)
[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.or_masks "Link to this definition")

Returns a mask\_mod that’s the union of provided mask\_mods

Return type:

[_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\], [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]

torch.nn.attention.flex\_attention.noop\_mask(_batch_, _head_, _token\_q_, _token\_kv_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/attention/flex_attention.py#L432)
[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.noop_mask "Link to this definition")

Returns a noop mask\_mod

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

FlexKernelOptions[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#flexkerneloptions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

_class_ torch.nn.attention.flex\_attention.FlexKernelOptions[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/attention/flex_attention.py#L144)
[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions "Link to this definition")

Options for controlling the behavior of FlexAttention kernels.

These options are passed to the underlying Triton kernels to control performance and numerical behavior. Most users will not need to specify these options as the default autotuning provides good performance.

The options can be prefixed with `fwd_` or `bwd_` to apply only to forward or backward pass respectively. For example: `fwd_BLOCK_M` and `bwd_BLOCK_M1`.

Note

We currently do not provide any backward compatibility guarantees for these options. That being said most of these have remained pretty stable since their introduction. But We do not consider this part of the public API just yet. We think that some documentation Is better than secret hidden flags, but we may change these options in the future.

Example Usage:

\# Using dictionary (backward compatible)
kernel\_opts \= {"BLOCK\_M": 64, "BLOCK\_N": 64, "PRESCALE\_QK": True}
output \= flex\_attention(q, k, v, kernel\_options\=kernel\_opts)

\# Using TypedDict (recommended for type safety)
from torch.nn.attention.flex\_attention import FlexKernelOptions

kernel\_opts: FlexKernelOptions \= {
    "BLOCK\_M": 64,
    "BLOCK\_N": 64,
    "PRESCALE\_QK": True,
}
output \= flex\_attention(q, k, v, kernel\_options\=kernel\_opts)

\# Forward/backward specific options
kernel\_opts: FlexKernelOptions \= {
    "fwd\_BLOCK\_M": 64,
    "bwd\_BLOCK\_M1": 32,
    "PRESCALE\_QK": False,
}
output \= flex\_attention(q, k, v, kernel\_options\=kernel\_opts)

Copy to clipboard

BACKEND_: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.15)")
\['AUTO', 'TRITON', 'FLASH', 'TRITON\_DECODE'\]_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions.BACKEND "Link to this definition")

Selects a specific kernel backend.

Options:

*   “AUTO”: Use current heuristics (typically Triton-based kernels with automatic selection between flex\_attention and flex\_decoding)
    
*   “TRITON”: Standard Triton flex\_attention kernel
    
*   “TRITON\_DECODE”: Triton flex\_decoding kernel, only available for short sequence lengths with specific configurations
    
*   “FLASH”: Experimental: Flash Attention kernel (cute-dsl), user needs to have flash installed
    

This option cannot be combined with legacy knobs such as `FORCE_USE_FLEX_ATTENTION`. Raises an error if the requested backend cannot be used. Default: “AUTO”

BLOCKS\_ARE\_CONTIGUOUS_: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions.BLOCKS_ARE_CONTIGUOUS "Link to this definition")

If True, guarantees that all blocks in the mask are contiguous. Allows optimizing block traversal. For example, causal masks would satisfy this, but prefix\_lm + sliding window would not. Default: False.

BLOCK\_M_: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions.BLOCK_M "Link to this definition")

Thread block size for the sequence length dimension of Q in forward pass. Must be a power of 2. Common values: 16, 32, 64, 128. Default is determined by autotuning.

BLOCK\_M1_: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions.BLOCK_M1 "Link to this definition")

Thread block size for Q dimension in backward pass. Use as ‘bwd\_BLOCK\_M1’. Default is determined by autotuning.

BLOCK\_M2_: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions.BLOCK_M2 "Link to this definition")

Thread block size for second Q dimension in backward pass. Use as ‘bwd\_BLOCK\_M2’. Default is determined by autotuning.

BLOCK\_N_: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions.BLOCK_N "Link to this definition")

Thread block size for the sequence length dimension of K/V in forward pass. Must be a power of 2. Common values: 16, 32, 64, 128. Default is determined by autotuning.

BLOCK\_N1_: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions.BLOCK_N1 "Link to this definition")

Thread block size for K/V dimension in backward pass. Use as ‘bwd\_BLOCK\_N1’. Default is determined by autotuning.

BLOCK\_N2_: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions.BLOCK_N2 "Link to this definition")

Thread block size for second K/V dimension in backward pass. Use as ‘bwd\_BLOCK\_N2’. Default is determined by autotuning.

FORCE\_USE\_FLEX\_ATTENTION_: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions.FORCE_USE_FLEX_ATTENTION "Link to this definition")

If True, forces the use of the flex attention kernel instead of potentially using the more optimized flex-decoding kernel for short sequences. This can be a helpful option for debugging. Default: False.

PRESCALE\_QK_: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions.PRESCALE_QK "Link to this definition")

Whether to pre-scale QK by 1/sqrt(d) and change of base. This is slightly faster but may have more numerical error. Default: False.

ROWS\_GUARANTEED\_SAFE_: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions.ROWS_GUARANTEED_SAFE "Link to this definition")

If True, skips the guard that sanitizes the softmax row maximum.

The condition this requires is stronger than “every row attends to at least one key”. The kernel carries a running row maximum across the KV blocks the block mask schedules, starting from `-inf`, and this option removes the only thing keeping it finite. Each row must therefore have an unmasked key in the _first_ block scheduled for it: if a row’s keys all fall in later blocks, the running maximum is still `-inf` when the rescaling runs, and `exp2` overflows to NaN. Block metadata can mark a block live because _other_ rows in the query block need it, so a mask can look valid at block granularity while individual rows are empty in their first block.

Causal attention satisfies this. Local or windowed masks often do not, since the earliest key a late row attends to can sit beyond the first scheduled block. Eager execution materializes the full row and is unaffected, so the NaN appears only under `torch.compile`.

Only set this if you are certain your mask satisfies the stronger condition; see the `ROWS_GUARANTEED_SAFE` demo in attention-gym for a worked example of a mask that looks safe and is not. Default: False.

USE\_TMA_: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions.USE_TMA "Link to this definition")

Whether to use hardware tensor descriptors for the attention operands. This is experimental and may not work on all hardware. It is supported on NVIDIA Hopper+ (TMA), Intel GPUs, and AMD gfx1250 (TDM); the AMD path covers the forward and decode kernels only, not the backward pass. The default is backend-dependent: Intel GPUs and eligible AMD gfx1250 inputs select descriptors automatically, and everything else defaults to False. Setting False forces the pointer path. Setting True requests descriptors but remains subject to the dtype and layout checks, falling back to the pointer path when the operands are ineligible. On AMD gfx1250, setting `torch._inductor.config.triton.enable_flex_tdm = False` at compile time disables the forward and decode descriptors even for `USE_TMA=True`; it is the control for callers that cannot reach this option, and it does not affect NVIDIA or Intel selection.

WRITE\_DQ_: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions.WRITE_DQ "Link to this definition")

Controls whether gradient scatters are done in the DQ iteration loop of the backward pass. Setting this to False will force this to happen in the DK loop which depending on your specific score\_mod and mask\_mod might be faster. Default: True.

kpack_: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions.kpack "Link to this definition")

ROCm-specific kernel packing parameter.

matrix\_instr\_nonkdim_: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions.matrix_instr_nonkdim "Link to this definition")

ROCm-specific matrix instruction non-K dimension.

num\_stages_: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions.num_stages "Link to this definition")

Number of pipeline stages in the CUDA kernel. Higher values may improve performance but increase shared memory usage. Default is determined by autotuning.

num\_warps_: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions.num_warps "Link to this definition")

Number of warps to use in the CUDA kernel. Higher values may improve performance but increase register pressure. Default is determined by autotuning.

waves\_per\_eu_: [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.FlexKernelOptions.waves_per_eu "Link to this definition")

ROCm-specific waves per execution unit.

BlockMask[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#blockmask "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

_class_ torch.nn.attention.flex\_attention.BlockMask(_seq\_lengths_, _kv\_num\_blocks_, _kv\_indices_, _full\_kv\_num\_blocks_, _full\_kv\_indices_, _q\_num\_blocks_, _q\_indices_, _full\_q\_num\_blocks_, _full\_q\_indices_, _BLOCK\_SIZE=(128_, _128)_, _mask\_mod=<function noop\_mask>_, _\*_, _dq\_write\_order=None_, _dq\_write\_order\_full=None_, _dq\_kv\_order=None_, _dq\_kv\_order\_spt=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/attention/flex_attention.py#L880)
[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask "Link to this definition")

BlockMask is our format for representing a block-sparse attention mask. It is somewhat of a cross in-between BCSR and a non-sparse format.

**Basics**

A block-sparse mask means that instead of representing the sparsity of individual elements in the mask, a KV\_BLOCK\_SIZE x Q\_BLOCK\_SIZE block is considered sparse only if every element within that block is sparse. This aligns well with hardware, which generally expects to perform contiguous loads and computation.

This format is primarily optimized for 1. simplicity, and 2. kernel efficiency. Notably, it is _not_ optimized for size, as this mask is always reduced by a factor of KV\_BLOCK\_SIZE \* Q\_BLOCK\_SIZE. If the size is a concern, the tensors can be reduced in size by increasing the block size.

The essentials of our format are:

num\_blocks\_in\_row: Tensor\[ROWS\]: Describes the number of blocks present in each row.

col\_indices: Tensor\[ROWS, MAX\_BLOCKS\_IN\_COL\]: col\_indices\[i\] is the sequence of block positions for row i. The values of this row after col\_indices\[i\]\[num\_blocks\_in\_row\[i\]\] are undefined.

For example, to reconstruct the original tensor from this format:

dense\_mask \= torch.zeros(ROWS, COLS)
for row in range(ROWS):
    for block\_idx in range(num\_blocks\_in\_row\[row\]):
        dense\_mask\[row, col\_indices\[row, block\_idx\]\] \= 1

Copy to clipboard

Notably, this format makes it easier to implement a reduction along the _rows_ of the mask.

**Details**

The basics of our format require only kv\_num\_blocks and kv\_indices. The primary block-sparse layout is represented by up to 4 tensor pairs:

1\. (kv\_num\_blocks, kv\_indices): Used for the forwards pass of attention, as we reduce along the KV dimension.

2\. \[OPTIONAL\] (full\_kv\_num\_blocks, full\_kv\_indices): This is optional and purely an optimization. As it turns out, applying masking to every block is quite expensive! If we specifically know which blocks are “full” and don’t require masking at all, then we can skip applying mask\_mod to these blocks. This requires the user to split out a separate mask\_mod from the score\_mod. For causal masks, this is about a 15% speedup.

3\. \[GENERATED\] (q\_num\_blocks, q\_indices): Required for the backwards pass, as computing dKV requires iterating along the mask along the Q dimension. These are autogenerated from 1.

4\. \[GENERATED\] (full\_q\_num\_blocks, full\_q\_indices): Same as above, but for the backwards pass. These are autogenerated from 2.

Additional optional tensors may carry deterministic dQ metadata for block-sparse FLASH backward:

5\. \[OPTIONAL\] dq\_write\_order: Write-order metadata for partial blocks. This is produced by create\_block\_mask when compute\_dq\_write\_order=True, or passed directly to BlockMask.from\_kv\_blocks by callers that precompute it.

6\. \[OPTIONAL\] dq\_write\_order\_full: Write-order metadata for full blocks, produced or passed the same way as dq\_write\_order.

7\. \[OPTIONAL\] dq\_kv\_order: Explicit KV scheduler order used to produce the write-order metadata. create\_block\_mask currently accepts a boolean dq\_kv\_order; BlockMask.from\_kv\_blocks also accepts a tensor for callers that provide precomputed write-order metadata directly.

BLOCK\_SIZE_: [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
\]_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.BLOCK_SIZE "Link to this definition")

dq\_kv\_order_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.dq_kv_order "Link to this definition")

dq\_kv\_order\_spt_: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.dq_kv_order_spt "Link to this definition")

dq\_write\_order_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.dq_write_order "Link to this definition")

dq\_write\_order\_full_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.dq_write_order_full "Link to this definition")

_classmethod_ from\_kv\_blocks(_kv\_num\_blocks_, _kv\_indices_, _full\_kv\_num\_blocks\=None_, _full\_kv\_indices\=None_, _BLOCK\_SIZE\=128_, _mask\_mod\=None_, _seq\_lengths\=None_, _compute\_q\_blocks\=True_, _\*_, _dq\_write\_order\=None_, _dq\_write\_order\_full\=None_, _dq\_kv\_order\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/attention/flex_attention.py#L1086)
[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.from_kv_blocks "Link to this definition")

Creates a BlockMask instance from key-value block information.

Parameters:

*   **kv\_num\_blocks** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Number of kv\_blocks in each Q\_BLOCK\_SIZE row tile.
    
*   **kv\_indices** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Indices of key-value blocks in each Q\_BLOCK\_SIZE row tile.
    
*   **full\_kv\_num\_blocks** (_Optional__\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]_) – Number of full kv\_blocks in each Q\_BLOCK\_SIZE row tile.
    
*   **full\_kv\_indices** (_Optional__\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]_) – Indices of full key-value blocks in each Q\_BLOCK\_SIZE row tile.
    
*   **BLOCK\_SIZE** (_Union__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]__\]_) – Size of KV\_BLOCK\_SIZE x Q\_BLOCK\_SIZE tiles.
    
*   **mask\_mod** (_Optional__\[__Callable__\]_) – Function to modify the mask.
    
*   **dq\_write\_order** (_Optional__\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]_) – Precomputed deterministic dQ write-order metadata.
    
*   **dq\_write\_order\_full** (_Optional__\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]_) – Precomputed deterministic dQ write-order metadata for full blocks.
    
*   **dq\_kv\_order** (_Optional__\[__Union__\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _,_ [_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _\]__\]_) – KV-column scheduler order used to produce dq\_write\_order. A bool selects a built-in order; a tensor gives an explicit scheduler-rank to n-block permutation.
    

Returns:

Instance with full Q information generated via \_transposed\_ordered

Return type:

[BlockMask](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask "torch.nn.attention.flex_attention.BlockMask")

Raises:

*   [**RuntimeError**](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "(in Python v3.15)")
     – If kv\_indices has < 2 dimensions.
    
*   [**AssertionError**](https://docs.python.org/3/builtins/exceptions.html#AssertionError "(in Python v3.15)")
     – If only one of full\_kv\_\* args is provided.
    

full\_kv\_indices_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.full_kv_indices "Link to this definition")

full\_kv\_num\_blocks_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.full_kv_num_blocks "Link to this definition")

full\_q\_indices_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.full_q_indices "Link to this definition")

full\_q\_num\_blocks_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.full_q_num_blocks "Link to this definition")

kv\_indices_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.kv_indices "Link to this definition")

kv\_num\_blocks_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.kv_num_blocks "Link to this definition")

mask\_mod_: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\], [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.mask_mod "Link to this definition")

numel()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/attention/flex_attention.py#L1462)
[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.numel "Link to this definition")

Returns the number of elements (not accounting for sparsity) in the mask.

Return type:

[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")

q\_indices_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.q_indices "Link to this definition")

q\_num\_blocks_: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.q_num_blocks "Link to this definition")

seq\_lengths_: [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
\]_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.seq_lengths "Link to this definition")

_property_ shape_: [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, ...\]_[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.shape "Link to this definition")

sparsity()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/attention/flex_attention.py#L1471)
[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.sparsity "Link to this definition")

Computes the percentage of blocks that are sparse (i.e. not computed)

Return type:

[float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")

to(_device_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/attention/flex_attention.py#L1565)
[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.to "Link to this definition")

Moves the BlockMask to the specified device.

Parameters:

**device** ([_torch.device_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
 _or_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – The target device to move the BlockMask to. Can be a torch.device object or a string (e.g., ‘cpu’, ‘cuda:0’).

Returns:

A new BlockMask instance with all tensor components moved to the specified device.

Return type:

[BlockMask](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask "torch.nn.attention.flex_attention.BlockMask")

Note

This method does not modify the original BlockMask in-place. Instead, it returns a new BlockMask instance where individual tensor attributes may or may not be moved to the specified device, depending on their current device placement.

to\_dense()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/attention/flex_attention.py#L1484)
[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.to_dense "Link to this definition")

Returns a dense block that is equivalent to the block mask.

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

to\_string(_grid\_size\=(20, 20)_, _limit\=4_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/attention/flex_attention.py#L1500)
[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.to_string "Link to this definition")

Returns a string representation of the block mask. Quite nifty.

If grid\_size is -1, prints out an uncompressed version. Warning, it can be quite big!

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

BlockMask.as\_tuple(_flatten: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.15)")
\[True\] \= True_) → [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")\
\[\[[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\], [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]\][\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/attention/flex_attention.py#L1225)
[#](https://docs.pytorch.org/docs/2.15/nn.attention.flex_attention.html#torch.nn.attention.flex_attention.BlockMask.as_tuple "Link to this definition")

BlockMask.as\_tuple(_flatten: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.15)")
\[False\]_) → [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
\], [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
, [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
\], [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")\
\[\[[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
, [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\], [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]\]

Returns a tuple of the attributes of the BlockMask.

Parameters:

**flatten** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
) – If True, it will flatten the tuple of (KV\_BLOCK\_SIZE, Q\_BLOCK\_SIZE)

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/nn.attention.flex_attention.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/nn.attention.flex_attention.md.txt)

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