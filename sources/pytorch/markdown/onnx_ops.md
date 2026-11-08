Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/onnx_ops.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/onnx_ops.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/onnx_ops.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/onnx_ops.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/onnx_ops.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/onnx_ops.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/onnx_ops.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/onnx_ops.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/onnx_ops.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/onnx_ops.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/onnx_ops.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/onnx_ops.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/onnx_ops.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/onnx_ops.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/onnx_ops.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/onnx_ops.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/onnx_ops.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/onnx_ops.html)
[v1.13](https://docs.pytorch.org/docs/1.13/onnx_ops.html)
[v1.12](https://docs.pytorch.org/docs/1.12/onnx_ops.html)
[v1.11](https://docs.pytorch.org/docs/1.11/onnx_ops.html)
[v1.10](https://docs.pytorch.org/docs/1.10/onnx_ops.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/onnx_ops.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/onnx_ops.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/onnx_ops.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/onnx_ops.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/onnx_ops.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/onnx_ops.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/onnx_ops.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/onnx_ops.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/onnx_ops.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/onnx_ops.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/onnx_ops.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/onnx_ops.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/onnx_ops.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/onnx_ops.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/onnx_ops.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/onnx_ops.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/onnx_ops.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/onnx_ops.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/onnx_ops.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/onnx_ops.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/onnx_ops.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/onnx_ops.html)

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

torch.onnx.ops[#](https://docs.pytorch.org/docs/2.15/onnx_ops.html#module-torch.onnx.ops "Link to this heading")

=================================================================================================================

Created On: Jun 10, 2025 | Last Updated On: Jun 20, 2025

ONNX operators as native torch.fx operators.

This module provides a set of functions to create ONNX operators in the FX graph which are exportable to ONNX.

Symbolic Operators[#](https://docs.pytorch.org/docs/2.15/onnx_ops.html#symbolic-operators "Link to this heading")

------------------------------------------------------------------------------------------------------------------

Operators that can be used to create any ONNX ops in the FX graph symbolically. These operators do not do actual computation. It’s recommended that you used them inside an `if torch.onnx.is_in_onnx_export` block.

torch.onnx.ops.symbolic(_domain\_op_, _/_, _inputs_, _attrs\=None_, _\*_, _dtype_, _shape_, _version\=None_, _metadata\_props\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/ops/__init__.py#L73)
[#](https://docs.pytorch.org/docs/2.15/onnx_ops.html#torch.onnx.ops.symbolic "Link to this definition")

Create a symbolic FX operator to represent an arbitrary ONNX operator.

This function is used to create a symbolic operator with a single output. To create an operator with multiple outputs, use [`symbolic_multi_out()`](https://docs.pytorch.org/docs/2.15/onnx_ops.html#torch.onnx.ops.symbolic_multi_out "torch.onnx.ops.symbolic_multi_out")
.

You may use `if torch.onnx.is_in_onnx_export()` to conditionally enable the symbolic logic only during `torch.onnx.export()`.

Example:

class CustomOp(torch.nn.Module):
    def forward(self, x: torch.Tensor) \-> torch.Tensor:
        \# Normal torch operators can interleave with the symbolic ops during ONNX export
        x \= x + 1

        \# Create a symbolic ONNX operator with the name "CustomOp" in the "custom\_domain" domain.
        \# The output tensor will have the specified dtype and shape
        val \= torch.onnx.ops.symbolic(
            "custom\_domain::CustomOp",
            (x,),
            dict(attr\_key\="attr\_value"),
            dtype\=x.dtype,
            shape\=x.shape,
            version\=1,
        )

        \# The result of the symbolic op can be used in normal torch operations during ONNX export
        return torch.nn.functional.relu(val)

\# You may then export this model to ONNX using torch.onnx.export(..., dynamo=True).

Copy to clipboard

Parameters:

*   **domain\_op** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The domain and operator name, separated by “::”. For example, “custom\_domain::CustomOp”.
    
*   **inputs** (_Sequence__\[_[_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
     _|_ _None__\]_) – The input tensors to the operator.
    
*   **attrs** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
     _|_ [_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _|_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
     _|_ [_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
     _|_ _Sequence__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_ _|_ _Sequence__\[_[_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
    _\]_ _|_ _Sequence__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ _Sequence__\[_[_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _\]__\]_ _|_ _None_) – The attributes of the operator. The keys are attribute names and the values are attribute values. Valid attribute types are int, float, str, bool, and lists of int, float, str, and bool. Tensor attributes are unsupported.
    
*   **dtype** ([_torch.dtype_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
     _|_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – The data type of the output tensor.This can be either a torch.dtype or an integer representing the ONNX data type.
    
*   **shape** (_Sequence__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
     _|_ [_torch.SymInt_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymInt "torch.SymInt")\
    _\]_) – The shape of the output tensor. This can be a list of integers or SymInt values.
    
*   **version** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ _None_) – The version of the opset used for the operator.
    
*   **metadata\_props** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ _None_) – Metadata properties for the ONNX node. This is a dictionary of str-str pairs.
    

Returns:

The output tensor of the operator.

Return type:

[torch.Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

torch.onnx.ops.symbolic\_multi\_out(_domain\_op_, _/_, _inputs_, _attrs\=None_, _\*_, _dtypes_, _shapes_, _version\=None_, _metadata\_props\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/ops/__init__.py#L174)
[#](https://docs.pytorch.org/docs/2.15/onnx_ops.html#torch.onnx.ops.symbolic_multi_out "Link to this definition")

Create a symbolic FX operator to represent an arbitrary ONNX operator with multiple outputs.

You may use `if torch.onnx.is_in_onnx_export()` to conditionally enable the symbolic logic only during `torch.onnx.export()`.

Example:

class CustomOp(torch.nn.Module):
    def forward(self, x: torch.Tensor) \-> torch.Tensor:
        \# Normal torch operators can interleave with the symbolic ops during ONNX export
        x \= x + 1

        \# Create a symbolic ONNX operator with the name "CustomOp" in the "custom\_domain" domain.
        \# The output tensors will have the specified dtypes and shapes
        (out1, out2) \= torch.onnx.ops.symbolic\_multi\_out(
            "custom\_domain::CustomOp",
            (x,),
            dict(attr\_key\="attr\_value"),
            dtypes\=(x.dtype, torch.float32),
            shapes\=(x.shape, \[1, 2, 3\]),
            version\=1,
        )

        \# The result of the symbolic op can be used in normal torch operations during ONNX export
        return torch.nn.functional.relu(out1 + out2)

\# You may then export this model to ONNX using torch.onnx.export(..., dynamo=True).

Copy to clipboard

Parameters:

*   **domain\_op** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The domain and operator name, separated by “::”. For example, “custom\_domain::CustomOp”.
    
*   **inputs** (_Sequence__\[_[_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
     _|_ _None__\]_) – The input tensors to the operator.
    
*   **attrs** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
     _|_ [_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
     _|_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
     _|_ [_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
     _|_ _Sequence__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_ _|_ _Sequence__\[_[_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
    _\]_ _|_ _Sequence__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ _Sequence__\[_[_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _\]__\]_ _|_ _None_) – The attributes of the operator. The keys are attribute names and the values are attribute values. Valid attribute types are int, float, str, bool, and lists of int, float, str, and bool. Tensor attributes are unsupported.
    
*   **dtypes** (_Sequence__\[_[_torch.dtype_](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")\
     _|_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – The data types of the output tensors. This can be a list of torch.dtype or integers representing the ONNX data types. The length of this list must be the number of outputs.
    
*   **shapes** (_Sequence__\[__Sequence__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
     _|_ [_torch.SymInt_](https://docs.pytorch.org/docs/2.15/torch.html#torch.SymInt "torch.SymInt")\
    _\]__\]_) – The shapes of the output tensors. This can be a list of lists of integers or SymInt values. The length of this list must be the number of outputs.
    
*   **version** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ _None_) – The version of the opset used for the operator.
    
*   **metadata\_props** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ _None_) – Metadata properties for the ONNX node. This is a dictionary of str-str pairs.
    

Returns:

A list of output tensors of the operator.

Return type:

Sequence\[[torch.Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]

ONNX Operators[#](https://docs.pytorch.org/docs/2.15/onnx_ops.html#onnx-operators "Link to this heading")

----------------------------------------------------------------------------------------------------------

The following operators are implemented as native PyTorch ops and can be exported as ONNX operators. They can be used natively in an `nn.Module`.

For example, you can define a module:

class Model(torch.nn.Module):
    def forward(
        self, input\_data, cos\_cache\_data, sin\_cache\_data, position\_ids\_data
    ):
        return torch.onnx.ops.rotary\_embedding(
            input\_data,
            cos\_cache\_data,
            sin\_cache\_data,
            position\_ids\_data,
        )

Copy to clipboard

and export it to ONNX using:

input\_data \= torch.rand(2, 3, 4, 8)
position\_ids\_data \= torch.randint(0, 50, (2, 3)).long()
sin\_cache\_data \= torch.rand(50, 4)
cos\_cache\_data \= torch.rand(50, 4)
dynamic\_shapes \= {
    "input\_data": {0: torch.export.Dim.DYNAMIC},
    "cos\_cache\_data": None,
    "sin\_cache\_data": None,
    "position\_ids\_data": {0: torch.export.Dim.DYNAMIC},
}
onnx\_program \= torch.onnx.export(
    model,
    (input\_data, cos\_cache\_data, sin\_cache\_data, position\_ids\_data),
    dynamic\_shapes\=dynamic\_shapes,
    dynamo\=True,
    opset\_version\=23,
)

Copy to clipboard

Printing the ONNX program will show the ONNX operators used in the graph:

<...>

graph(
    name=main\_graph,
    inputs=(
        %"input\_data"<FLOAT,\[s0,3,4,8\]>,
        %"cos\_cache\_data"<FLOAT,\[50,4\]>,
        %"sin\_cache\_data"<FLOAT,\[50,4\]>,
        %"position\_ids\_data"<INT64,\[s0,3\]>
    ),
    outputs=(
        %"rotary\_embedding"<FLOAT,\[s0,3,4,8\]>
    ),
) {
    0 |  # rotary\_embedding
        %"rotary\_embedding"<FLOAT,\[s0,3,4,8\]> ⬅️ ::RotaryEmbedding(%"input\_data", %"cos\_cache\_data", %"sin\_cache\_data", %"position\_ids\_data")
    return %"rotary\_embedding"<FLOAT,\[s0,3,4,8\]>
}

Copy to clipboard

with the corresponding `ExportedProgram`:

ExportedProgram:

class GraphModule(torch.nn.Module):
    def forward(self, input\_data: "f32\[s0, 3, 4, 8\]", cos\_cache\_data: "f32\[50, 4\]", sin\_cache\_data: "f32\[50, 4\]", position\_ids\_data: "i64\[s0, 3\]"):
        rotary\_embedding: "f32\[s0, 3, 4, 8\]" \= torch.ops.onnx.RotaryEmbedding.opset23(input\_data, cos\_cache\_data, sin\_cache\_data, position\_ids\_data);  input\_data \= cos\_cache\_data \= sin\_cache\_data \= position\_ids\_data \= None
        return (rotary\_embedding,)

Copy to clipboard

torch.onnx.ops.rotary\_embedding(_X_, _cos\_cache_, _sin\_cache_, _position\_ids\=None_, _\*_, _interleaved\=False_, _num\_heads\=0_, _rotary\_embedding\_dim\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/ops/__init__.py#L282)
[#](https://docs.pytorch.org/docs/2.15/onnx_ops.html#torch.onnx.ops.rotary_embedding "Link to this definition")

RotaryEmbedding op in ONNX.

[https://onnx.ai/onnx/operators/onnx\_\_RotaryEmbedding.html](https://onnx.ai/onnx/operators/onnx__RotaryEmbedding.html)

RotaryEmbedding is the implementation of rotary positional embeddings (RoPE) based on the paper [https://arxiv.org/pdf/2104.09864](https://arxiv.org/pdf/2104.09864)
. The key advantage of RoPE is that it allows the model to understand both the absolute position of a token and the relative distances between tokens. This is achieved through a rotational mechanism where the extent of rotation is computed based on the token’s absolute position (position\_ids).

The rotational mechanism is defined by sine and cosine functions that are used to represent the rotation angles. For each token in the sequence, its positional embedding is computed by rotating its embedding vector. This is done by splitting the embedding vector either into two halves or interleaving every alternate token and applying the rotation matrix to each half of the embedding vector. The rotation matrix is parameterized by the token’s position in the sequence. The rotated halves of the embedding vector are concatenated to form the final positional embedding for each token. The rotated positional embeddings are used in the self-attention mechanism. The rotation ensures that the model captures both absolute and relative positional information.

Parameters:

*   **X** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – The input tensor representing the token embeddings. 4D tensor with shape (batch\_size, num\_heads, sequence\_length, head\_size) or 3D tensor with shape (batch\_size, sequence\_length, hidden\_size). For cases with a 4D input tensor, head\_size has to be even. For cases with a 3D input tensor, num\_heads attribute must be provided and hidden\_size must be an even multiple of num\_heads where hidden\_size = num\_heads \* head\_size
    
*   **cos\_cache** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – The cosine values for the rotation. 2D tensor with shape (max\_position\_id\_plus\_1, head\_size / 2) for full rotation or (max\_position\_id\_plus\_1, rotary\_embedding\_dim / 2) for partial rotation when position\_ids are provided. 3D tensor with shape (batch\_size, sequence\_length, head\_size / 2) for full rotation or (batch\_size, sequence\_length, rotary\_embedding\_dim / 2) for partial rotation when position\_ids are not provided. max\_position\_id\_plus\_1 is a parameter to the model.
    
*   **sin\_cache** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – The sine values for the rotation. 2D tensor with shape (max\_position\_id\_plus\_1, head\_size / 2) for full rotation or (max\_position\_id\_plus\_1, rotary\_embedding\_dim / 2) for partial rotation when position\_ids are provided. 3D tensor with shape (batch\_size, sequence\_length, head\_size / 2) for full rotation or (batch\_size, sequence\_length, rotary\_embedding\_dim / 2) for partial rotation when position\_ids are not provided. max\_position\_id\_plus\_1 is a parameter to the model.
    
*   **position\_ids** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _|_ _None_) – The position indices for the tokens. 2D tensor with shape (batch\_size, sequence\_length).
    
*   **interleaved** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Rotate using interleaved pattern. Default value is 0 (False).
    
*   **num\_heads** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Number of attention heads. Must be provided when input is a 3D tensor.
    
*   **rotary\_embedding\_dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Rotary embedding dimension used to apply partial rotary embeddings.
    

Returns:

Tensor with same shape as input.

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

torch.onnx.ops.attention(_Q_, _K_, _V_, _attn\_mask\=None_, _past\_key\=None_, _past\_value\=None_, _\*_, _is\_causal\=False_, _kv\_num\_heads\=0_, _q\_num\_heads\=0_, _qk\_matmul\_output\_mode\=0_, _scale\=None_, _softcap\=0.0_, _softmax\_precision\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/ops/__init__.py#L348)
[#](https://docs.pytorch.org/docs/2.15/onnx_ops.html#torch.onnx.ops.attention "Link to this definition")

Attention op in ONNX.

[https://onnx.ai/onnx/operators/onnx\_\_Attention.html](https://onnx.ai/onnx/operators/onnx__Attention.html)

Computes scaled dot product attention on query, key and value tensors, using an optional attention mask if passed.

This operator covers self and cross variants of the attention operation based on sequence lengths of K, Q and V.

For self attention, `kv_sequence_length` equals to `q_sequence_length`.

For cross attention, query and key might have different lengths.

This operator also covers the 3 following variants based on the number of heads:

1.  Multi-headed Attention (MHA): Described in the paper [https://arxiv.org/pdf/1706.03762](https://arxiv.org/pdf/1706.03762)
    , q\_num\_heads = kv\_num\_heads.
    
2.  Group-query Attention (GQA): Described in the paper [https://arxiv.org/pdf/2305.13245](https://arxiv.org/pdf/2305.13245)
    , q\_num\_heads > kv\_num\_heads, q\_num\_heads % kv\_num\_heads == 0.
    
3.  Multi-query Attention (MQA): Described in the paper [https://arxiv.org/pdf/1911.02150](https://arxiv.org/pdf/1911.02150)
    , q\_num\_heads > kv\_num\_heads, kv\_num\_heads=1.
    

Attention bias to be added is calculated based on `attn_mask` input and ``is_causal` `attribute``, only one of which can be provided.

1.  If `is_causal` is set to 1, the attention masking is a lower triangular matrix when the mask is a square matrix. The attention masking has the form of the upper left causal bias due to the alignment.
    
2.  attn\_mask: A boolean mask where a value of True indicates that the element should take part in attention or a float mask of the same type as query, key, value that is added to the attention score.
    

Both past and present state key/values are optional. They shall be used together, and not allowed to use only one of them. The following pattern is applied to the Q, K and V inputs after appropriate reshaping of K and V inputs based on sequence lengths and num heads provided:

The following pattern is applied by this operator:
        Q          K          V
        |          |          |
Q\*sqrt(scale) K\*sqrt(scale) |
        |          |          |
        |       Transpose     |
        |          |          |
        \---MatMul\---          |
            |               |
at\_mask\---Add              |
            |               |
    softcap (if provided)     |
            |               |
        Softmax            |
            |               |
            \-----MatMul\------
                    |
                    Y

Copy to clipboard

Parameters:

*   **Q** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Query tensor. 4D tensor with shape (batch\_size, q\_num\_heads, q\_sequence\_length, head\_size) or 3D tensor with shape (batch\_size, q\_sequence\_length, q\_hidden\_size). For cases with a 3D input tensor, q\_hidden\_size = q\_num\_heads \* head\_size
    
*   **K** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Key tensor. 4D tensor with shape (batch\_size, kv\_num\_heads, kv\_sequence\_length, head\_size) or 3D tensor with shape (batch\_size, kv\_sequence\_length, k\_hidden\_size). For cases with a 3D input tensor, k\_hidden\_size = kv\_num\_heads \* head\_size
    
*   **V** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Value tensor. 4D tensor with shape (batch\_size, kv\_num\_heads, kv\_sequence\_length, v\_head\_size) or 3D tensor with shape (batch\_size, kv\_sequence\_length, v\_hidden\_size). For cases with a 3D input tensor, v\_hidden\_size = kv\_num\_heads \* v\_head\_size
    
*   **attn\_mask** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _|_ _None_) – Attention mask. Shape must be broadcastable to 4D tensor with shape (batch\_size, q\_num\_heads, q\_sequence\_length, total\_sequence\_length) where total\_sequence\_length = past\_sequence\_length + kv\_sequence\_length. Two types of masks are supported. A boolean mask where a value of True indicates that the element should take part in attention. Also supports a float mask of the same type as query, key, value that is added to the attention score.
    
*   **past\_key** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _|_ _None_) – Past state cache for key with shape (batch\_size, kv\_num\_heads, past\_sequence\_length, head\_size)
    
*   **past\_value** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _|_ _None_) – Past state cache for value with shape (batch\_size, kv\_num\_heads, past\_sequence\_length, v\_head\_size)
    
*   **is\_causal** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If set to True, the attention masking is a lower triangular matrix when the mask is a square matrix. The attention masking has the form of the upper left causal bias due to the alignment.
    
*   **kv\_num\_heads** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Number of heads of key and value. Must be used with 3D inputs of Q, K and V.
    
*   **q\_num\_heads** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Number of heads of query. Must be used with 3D inputs of Q, K and V.
    
*   **qk\_matmul\_output\_mode** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – If set to 0, qk\_matmul\_output is the output of qk matmul. If set to 1, qk\_matmul\_output includes the addition of the attention mask to the output of qk matmul. If set to 2, qk\_matmul\_output is the output after the softcap operation. If set to 3, qk\_matmul\_output is the output after the softmax operation. Default value is 0.
    
*   **scale** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _|_ _None_) – Scaling factor applied to Q\*K^T. Default value is 1/sqrt(head\_size). To prevent numerical overflow, scale Q, K by sqrt(scale) before matmul.
    
*   **softcap** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – Softcap value for attention weights. Default value is 0.
    
*   **softmax\_precision** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ _None_) – The floating-point precision used in softmax computation. If softmax precision is not provided, the same precision as the input of softmax (Q and K) is used.
    

Returns:

*   The output tensor. 4D tensor with shape (batch\_size, q\_num\_heads, q\_sequence\_length, v\_head\_size) or 3D tensor with shape (batch\_size, q\_sequence\_length, hidden\_size). For cases with a 3D input tensor, hidden\_size = q\_num\_heads \* v\_head\_size
    
*   Updated key cache with shape (batch\_size, kv\_num\_heads, total\_sequence\_length, head\_size) where total\_sequence\_length = past\_sequence\_length + kv\_sequence\_length.
    
*   Updated value cache with shape (batch\_size, kv\_num\_heads, total\_sequence\_length, v\_head\_size) where total\_sequence\_length = past\_sequence\_length + kv\_sequence\_length.
    
*   The output of QK matmul. 4D tensor with shape (batch\_size, q\_num\_heads, q\_sequence\_length, total\_sequence\_length) where total\_sequence\_length = past\_sequence\_length + kv\_sequence\_length.
    

Return type:

A tuple containing

ONNX to ATen Decomposition Table[#](https://docs.pytorch.org/docs/2.15/onnx_ops.html#onnx-to-aten-decomposition-table "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

You can use [`torch.onnx.ops.aten_decompositions()`](https://docs.pytorch.org/docs/2.15/onnx_ops.html#torch.onnx.ops.aten_decompositions "torch.onnx.ops.aten_decompositions")
 to obtain a decomposition table to decompose ONNX operators defined above to ATen operators.

class Model(torch.nn.Module):
    def forward(
        self, input\_data, cos\_cache\_data, sin\_cache\_data, position\_ids\_data
    ):
        return torch.onnx.ops.rotary\_embedding(
            input\_data,
            cos\_cache\_data,
            sin\_cache\_data,
            position\_ids\_data,
        )

model \= Model()

ep \= torch.export.export(
    model,
    (input\_data, cos\_cache\_data, sin\_cache\_data, position\_ids\_data),
)
\# The program can be decomposed into aten ops
ep\_decomposed \= ep.run\_decompositions(torch.onnx.ops.aten\_decompositions())

Copy to clipboard

torch.onnx.ops.aten\_decompositions()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/onnx/ops/__init__.py#L57)
[#](https://docs.pytorch.org/docs/2.15/onnx_ops.html#torch.onnx.ops.aten_decompositions "Link to this definition")

Return the ONNX to ATen decomp table.

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[torch.\_ops.OpOverload, Callable\]

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/onnx_ops.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/onnx_ops.md.txt)

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