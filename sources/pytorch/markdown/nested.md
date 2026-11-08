Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/nested.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/nested.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/nested.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/nested.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/nested.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/nested.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/nested.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/nested.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/nested.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/nested.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/nested.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/nested.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/nested.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/nested.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/nested.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/nested.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/nested.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/nested.html)
[v1.13](https://docs.pytorch.org/docs/1.13/nested.html)
[v1.12](https://docs.pytorch.org/docs/1.12/nested.html)
[v1.11](https://docs.pytorch.org/docs/1.11/nested.html)
[v1.10](https://docs.pytorch.org/docs/1.10/nested.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/nested.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/nested.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/nested.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/nested.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/nested.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/nested.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/nested.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/nested.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/nested.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/nested.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/nested.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/nested.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/nested.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/nested.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/nested.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/nested.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/nested.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/nested.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/nested.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/nested.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/nested.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/nested.html)

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

torch.nested[#](https://docs.pytorch.org/docs/2.15/nested.html#module-torch.nested "Link to this heading")

===========================================================================================================

Created On: Mar 02, 2022 | Last Updated On: Jan 16, 2026

Introduction[#](https://docs.pytorch.org/docs/2.15/nested.html#introduction "Link to this heading")

----------------------------------------------------------------------------------------------------

Warning

Nested tensors are not currently under active development. Use at your own risk.

Nested tensors allow for ragged-shaped data to be contained within and operated upon as a single tensor. Such data is stored underneath in an efficient packed representation, while exposing a standard PyTorch tensor interface for applying operations.

A common application of nested tensors is for expressing batches of variable-length sequential data present in various domains, such as varying sentence lengths, image sizes, and audio / video clip lengths. Traditionally, such data has been handled by padding sequences to that of the max length within a batch, performing computation on the padded form, and subsequently masking to remove padding. This is inefficient and error-prone, and nested tensors exist to address these problems.

The API for calling operations on a nested tensor is no different from that of a regular `torch.Tensor`, allowing for seamless integration with existing models, with the main difference being [construction of the inputs](https://docs.pytorch.org/docs/2.15/nested.html#construction)
.

As this is a prototype feature, the set of [operations supported](https://docs.pytorch.org/docs/2.15/nested.html#supported-operations)
 is limited, but growing. We welcome issues, feature requests, and contributions. More information on contributing can be found [in this Readme](https://github.com/pytorch/pytorch/blob/main/aten/src/ATen/native/nested/README.md)
.

Construction[#](https://docs.pytorch.org/docs/2.15/nested.html#construction "Link to this heading")

----------------------------------------------------------------------------------------------------

Note

There are two forms of nested tensors present within PyTorch, distinguished by layout as specified during construction. Layout can be one of `torch.strided` or `torch.jagged`. We recommend utilizing the `torch.jagged` layout whenever possible. While it currently only supports a single ragged dimension, it has better op coverage, receives active development, and integrates well with `torch.compile`. These docs adhere to this recommendation and refer to nested tensors with the `torch.jagged` layout as “NJTs” for brevity throughout.

Construction is straightforward and involves passing a list of tensors to the `torch.nested.nested_tensor` constructor. A nested tensor with the `torch.jagged` layout (AKA an “NJT”) supports a single ragged dimension. This constructor will copy the input tensors into a packed, contiguous block of memory according to the layout described in the `data_layout`\_ section below.

\>>> a, b \= torch.arange(3), torch.arange(5) + 3
\>>> a
tensor(\[0, 1, 2\])
\>>> b
tensor(\[3, 4, 5, 6, 7\])
\>>> nt \= torch.nested.nested\_tensor(\[a, b\], layout\=torch.jagged)
\>>> print(\[component for component in nt\])
\[tensor(\[0, 1, 2\]), tensor(\[3, 4, 5, 6, 7\])\]

Copy to clipboard

Each tensor in the list must have the same number of dimensions, but the shapes can otherwise vary along a single dimension. If the dimensionalities of the input components don’t match, the constructor throws an error.

\>>> a \= torch.randn(50, 128) \# 2D tensor
\>>> b \= torch.randn(2, 50, 128) \# 3D tensor
\>>> nt \= torch.nested.nested\_tensor(\[a, b\], layout\=torch.jagged)
...
RuntimeError: When constructing a nested tensor, all tensors in list must have the same dim

Copy to clipboard

During construction, dtype, device, and whether gradients are required can be chosen via the usual keyword arguments.

\>>> nt \= torch.nested.nested\_tensor(\[a, b\], layout\=torch.jagged, dtype\=torch.float32, device\="cuda", requires\_grad\=True)
\>>> print(\[component for component in nt\])
\[tensor(\[0., 1., 2.\], device='cuda:0',\
       grad\_fn=<UnbindBackwardAutogradNestedTensor0>), tensor(\[3., 4., 5., 6., 7.\], device='cuda:0',\
       grad\_fn=<UnbindBackwardAutogradNestedTensor0>)\]

Copy to clipboard

`torch.nested.as_nested_tensor` can be used to preserve autograd history from the tensors passed to the constructor. When this constructor is utilized, gradients will flow through the nested tensor back into the original components. Note that this constructor still copies the input components into a packed, contiguous block of memory.

\>>> a \= torch.randn(12, 512, requires\_grad\=True)
\>>> b \= torch.randn(23, 512, requires\_grad\=True)
\>>> nt \= torch.nested.as\_nested\_tensor(\[a, b\], layout\=torch.jagged, dtype\=torch.float32)
\>>> nt.sum().backward()
\>>> a.grad
tensor(\[\[1., 1., 1.,  ..., 1., 1., 1.\],\
        \[1., 1., 1.,  ..., 1., 1., 1.\],\
        \[1., 1., 1.,  ..., 1., 1., 1.\],\
        ...,\
        \[1., 1., 1.,  ..., 1., 1., 1.\],\
        \[1., 1., 1.,  ..., 1., 1., 1.\],\
        \[1., 1., 1.,  ..., 1., 1., 1.\]\])
\>>> b.grad
tensor(\[\[1., 1., 1.,  ..., 1., 1., 1.\],\
        \[1., 1., 1.,  ..., 1., 1., 1.\],\
        \[1., 1., 1.,  ..., 1., 1., 1.\],\
        ...,\
        \[1., 1., 1.,  ..., 1., 1., 1.\],\
        \[1., 1., 1.,  ..., 1., 1., 1.\],\
        \[1., 1., 1.,  ..., 1., 1., 1.\]\])

Copy to clipboard

The above functions all create contiguous NJTs, where a chunk of memory is allocated to store a packed form of the underlying components (see the `data_layout`\_ section below for more details).

It is also possible to create a non-contiguous NJT view over a pre-existing dense tensor with padding, avoiding the memory allocation and copying. `torch.nested.narrow()` is the tool for accomplishing this.

\>>> padded \= torch.randn(3, 5, 4)
\>>> seq\_lens \= torch.tensor(\[3, 2, 5\], dtype\=torch.int64)
\>>> nt \= torch.nested.narrow(padded, dim\=1, start\=0, length\=seq\_lens, layout\=torch.jagged)
\>>> nt.shape
torch.Size(\[3, j1, 4\])
\>>> nt.is\_contiguous()
False

Copy to clipboard

Note that the nested tensor acts as a view over the original padded dense tensor, referencing the same memory without copying / allocation. Operation support for non-contiguous NJTs is somewhat more limited, so if you run into support gaps, it’s always possible to convert to a contiguous NJT using `contiguous()`.

Data Layout and Shape[#](https://docs.pytorch.org/docs/2.15/nested.html#data-layout-and-shape "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

For efficiency, nested tensors generally pack their tensor components into a contiguous chunk of memory and maintain additional metadata to specify batch item boundaries. For the `torch.jagged` layout, the contiguous chunk of memory is stored in the `values` component, with the `offsets` component delineating batch item boundaries for the ragged dimension.

![image](https://docs.pytorch.org/docs/2.15/_images/njt_visual.png)

It’s possible to directly access the underlying NJT components when necessary.

\>>> a \= torch.randn(50, 128) \# text 1
\>>> b \= torch.randn(32, 128) \# text 2
\>>> nt \= torch.nested.nested\_tensor(\[a, b\], layout\=torch.jagged, dtype\=torch.float32)
\>>> nt.values().shape  \# note the "packing" of the ragged dimension; no padding needed
torch.Size(\[82, 128\])
\>>> nt.offsets()
tensor(\[ 0, 50, 82\])

Copy to clipboard

It can also be useful to construct an NJT from the jagged `values` and `offsets` constituents directly; the `torch.nested.nested_tensor_from_jagged()` constructor serves this purpose.

\>>> values \= torch.randn(82, 128)
\>>> offsets \= torch.tensor(\[0, 50, 82\], dtype\=torch.int64)
\>>> nt \= torch.nested.nested\_tensor\_from\_jagged(values\=values, offsets\=offsets)

Copy to clipboard

An NJT has a well-defined shape with dimensionality 1 greater than that of its components. The underlying structure of the ragged dimension is represented by a symbolic value (`j1` in the example below).

\>>> a \= torch.randn(50, 128)
\>>> b \= torch.randn(32, 128)
\>>> nt \= torch.nested.nested\_tensor(\[a, b\], layout\=torch.jagged, dtype\=torch.float32)
\>>> nt.dim()
3
\>>> nt.shape
torch.Size(\[2, j1, 128\])

Copy to clipboard

NJTs must have the same ragged structure to be compatible with each other. For example, to run a binary operation involving two NJTs, the ragged structures must match (i.e. they must have the same ragged shape symbol in their shapes). In the details, each symbol corresponds with an exact `offsets` tensor, so both NJTs must have the same `offsets` tensor to be compatible with each other.

\>>> a \= torch.randn(50, 128)
\>>> b \= torch.randn(32, 128)
\>>> nt1 \= torch.nested.nested\_tensor(\[a, b\], layout\=torch.jagged, dtype\=torch.float32)
\>>> nt2 \= torch.nested.nested\_tensor(\[a, b\], layout\=torch.jagged, dtype\=torch.float32)
\>>> nt1.offsets() is nt2.offsets()
False
\>>> nt3 \= nt1 + nt2
RuntimeError: cannot call binary pointwise function add.Tensor with inputs of shapes (2, j2, 128) and (2, j3, 128)

Copy to clipboard

In the above example, even though the conceptual shapes of the two NJTs are the same, they don’t share a reference to the same `offsets` tensor, so their shapes differ, and they are not compatible. We recognize that this behavior is unintuitive and are working hard to relax this restriction for the beta release of nested tensors. For a workaround, see the [Troubleshooting](https://docs.pytorch.org/docs/2.15/nested.html#ragged-structure-incompatibility)
 section of this document.

In addition to the `offsets` metadata, NJTs can also compute and cache the minimum and maximum sequence lengths for its components, which can be useful for invoking particular kernels (e.g. SDPA). There are currently no public APIs for accessing these, but this will change for the beta release.

Supported Operations[#](https://docs.pytorch.org/docs/2.15/nested.html#supported-operations "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

This section contains a list of common operations over nested tensors that you may find useful. It is not comprehensive, as there are on the order of a couple thousand ops within PyTorch. While a sizeable subset of these are supported for nested tensors today, full support is a large task. The ideal state for nested tensors is full support of all PyTorch operations that are available for non-nested tensors. To help us accomplish this, please consider:

*   Requesting particular ops needed for your use case [here](https://github.com/pytorch/pytorch/issues/118107)
     to help us prioritize.
    
*   Contributing! It’s not too hard to add nested tensor support for a given PyTorch op; see the [Contributions](https://docs.pytorch.org/docs/2.15/nested.html#contributions)
     section below for details.
    

### Viewing nested tensor constituents[#](https://docs.pytorch.org/docs/2.15/nested.html#viewing-nested-tensor-constituents "Link to this heading")

`unbind()` allows you to retrieve a view of the nested tensor’s constituents.

\>>> import torch
\>>> a \= torch.randn(2, 3)
\>>> b \= torch.randn(3, 3)
\>>> nt \= torch.nested.nested\_tensor(\[a, b\], layout\=torch.jagged)
\>>> nt.unbind()
(tensor(\[\[-0.9916, -0.3363, -0.2799\],\
        \[-2.3520, -0.5896, -0.4374\]\]), tensor(\[\[-2.0969, -1.0104,  1.4841\],\
        \[ 2.0952,  0.2973,  0.2516\],\
        \[ 0.9035,  1.3623,  0.2026\]\]))
\>>> nt.unbind()\[0\] is not a
True
\>>> nt.unbind()\[0\].mul\_(3)
tensor(\[\[ 3.6858, -3.7030, -4.4525\],\
        \[-2.3481,  2.0236,  0.1975\]\])
\>>> nt.unbind()
(tensor(\[\[-2.9747, -1.0089, -0.8396\],\
        \[-7.0561, -1.7688, -1.3122\]\]), tensor(\[\[-2.0969, -1.0104,  1.4841\],\
        \[ 2.0952,  0.2973,  0.2516\],\
        \[ 0.9035,  1.3623,  0.2026\]\]))

Copy to clipboard

Note that `nt.unbind()[0]` is not a copy, but rather a slice of the underlying memory, which represents the first entry or constituent of the nested tensor.

#### Conversions to / from padded[#](https://docs.pytorch.org/docs/2.15/nested.html#conversions-to-from-padded "Link to this heading")

`torch.nested.to_padded_tensor()` converts an NJT to a padded dense tensor with the specified padding value. The ragged dimension will be padded out to the size of the maximum sequence length.

\>>> import torch
\>>> a \= torch.randn(2, 3)
\>>> b \= torch.randn(6, 3)
\>>> nt \= torch.nested.nested\_tensor(\[a, b\], layout\=torch.jagged)
\>>> padded \= torch.nested.to\_padded\_tensor(nt, padding\=4.2)
\>>> padded
tensor(\[\[\[ 1.6107,  0.5723,  0.3913\],\
         \[ 0.0700, -0.4954,  1.8663\],\
         \[ 4.2000,  4.2000,  4.2000\],\
         \[ 4.2000,  4.2000,  4.2000\],\
         \[ 4.2000,  4.2000,  4.2000\],\
         \[ 4.2000,  4.2000,  4.2000\]\],\
        \[\[-0.0479, -0.7610, -0.3484\],\
         \[ 1.1345,  1.0556,  0.3634\],\
         \[-1.7122, -0.5921,  0.0540\],\
         \[-0.5506,  0.7608,  2.0606\],\
         \[ 1.5658, -1.1934,  0.3041\],\
         \[ 0.1483, -1.1284,  0.6957\]\]\])

Copy to clipboard

This can be useful as an escape hatch to work around NJT support gaps, but ideally such conversions should be avoided when possible for optimal memory usage and performance, as the more efficient nested tensor layout does not materialize padding.

The reverse conversion can be accomplished using `torch.nested.narrow()`, which applies ragged structure to a given dense tensor to produce an NJT. Note that by default, this operation does not copy the underlying data, and thus the output NJT is generally non-contiguous. It may be useful to explicitly call `contiguous()` here if a contiguous NJT is desired.

\>>> padded \= torch.randn(3, 5, 4)
\>>> seq\_lens \= torch.tensor(\[3, 2, 5\], dtype\=torch.int64)
\>>> nt \= torch.nested.narrow(padded, dim\=1, length\=seq\_lens, layout\=torch.jagged)
\>>> nt.shape
torch.Size(\[3, j1, 4\])
\>>> nt \= nt.contiguous()
\>>> nt.shape
torch.Size(\[3, j2, 4\])

Copy to clipboard

### Shape manipulations[#](https://docs.pytorch.org/docs/2.15/nested.html#shape-manipulations "Link to this heading")

Nested tensors support a wide array of operations for shape manipulation, including views.

\>>> a \= torch.randn(2, 6)
\>>> b \= torch.randn(4, 6)
\>>> nt \= torch.nested.nested\_tensor(\[a, b\], layout\=torch.jagged)
\>>> nt.shape
torch.Size(\[2, j1, 6\])
\>>> nt.unsqueeze(\-1).shape
torch.Size(\[2, j1, 6, 1\])
\>>> nt.unflatten(\-1, \[2, 3\]).shape
torch.Size(\[2, j1, 2, 3\])
\>>> torch.cat(\[nt, nt\], dim\=2).shape
torch.Size(\[2, j1, 12\])
\>>> torch.stack(\[nt, nt\], dim\=2).shape
torch.Size(\[2, j1, 2, 6\])
\>>> nt.transpose(\-1, \-2).shape
torch.Size(\[2, 6, j1\])

Copy to clipboard

### Attention mechanisms[#](https://docs.pytorch.org/docs/2.15/nested.html#attention-mechanisms "Link to this heading")

As variable-length sequences are common inputs to attention mechanisms, nested tensors support important attention operators [Scaled Dot Product Attention (SDPA)](https://pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html)
 and [FlexAttention](https://pytorch.org/docs/stable/nn.attention.flex_attention.html#module-torch.nn.attention.flex_attention)
. See [here](https://pytorch.org/tutorials/intermediate/transformer_building_blocks.html#multiheadattention)
 for usage examples of NJT with SDPA and [here](https://pytorch.org/tutorials/intermediate/transformer_building_blocks.html#flexattention-njt)
 for usage examples of NJT with FlexAttention.

Usage with torch.compile[#](https://docs.pytorch.org/docs/2.15/nested.html#usage-with-torch-compile "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

NJTs are designed to be used with `torch.compile()` for optimal performance, and we always recommend utilizing `torch.compile()` with NJTs when possible. NJTs work out-of-the-box and graph-break-free both when passed as inputs to a compiled function or module OR when instantiated in-line within the function.

Note

If you're not able to utilize \`\`torch.compile()\`\` for your use case, performance and memory
usage may still benefit from the use of NJTs, but it's not as clear-cut whether this will be
the case. It is important that the tensors being operated on are large enough so the
performance gains are not outweighed by the overhead of python tensor subclasses.

Copy to clipboard

\>>> import torch
\>>> a \= torch.randn(2, 3)
\>>> b \= torch.randn(4, 3)
\>>> nt \= torch.nested.nested\_tensor(\[a, b\], layout\=torch.jagged)
\>>> def f(x): return x.sin() + 1
...
\>>> compiled\_f \= torch.compile(f, fullgraph\=True)
\>>> output \= compiled\_f(nt)
\>>> output.shape
torch.Size(\[2, j1, 3\])
\>>> def g(values, offsets): return torch.nested.nested\_tensor\_from\_jagged(values, offsets) \* 2.
...
\>>> compiled\_g \= torch.compile(g, fullgraph\=True)
\>>> output2 \= compiled\_g(nt.values(), nt.offsets())
\>>> output2.shape
torch.Size(\[2, j1, 3\])

Copy to clipboard

Note that NJTs support [Dynamic Shapes](https://pytorch.org/docs/stable/torch.compiler_dynamic_shapes.html)
 to avoid unnecessary recompiles with changing ragged structure.

\>>> a \= torch.randn(2, 3)
\>>> b \= torch.randn(4, 3)
\>>> c \= torch.randn(5, 3)
\>>> d \= torch.randn(6, 3)
\>>> nt1 \= torch.nested.nested\_tensor(\[a, b\], layout\=torch.jagged)
\>>> nt2 \= torch.nested.nested\_tensor(\[c, d\], layout\=torch.jagged)
\>>> def f(x): return x.sin() + 1
...
\>>> compiled\_f \= torch.compile(f, fullgraph\=True)
\>>> output1 \= compiled\_f(nt1)
\>>> output2 \= compiled\_f(nt2)  \# NB: No recompile needed even though ragged structure differs

Copy to clipboard

If you run into problems or arcane errors when utilizing NJT + `torch.compile`, please file a PyTorch issue. Full subclass support within `torch.compile` is a long-term effort and there may be some rough edges at this time.

Troubleshooting[#](https://docs.pytorch.org/docs/2.15/nested.html#troubleshooting "Link to this heading")

----------------------------------------------------------------------------------------------------------

This section contains common errors that you may run into when utilizing nested tensors, alongside the reason for these errors and suggestions for how to address them.

### Unimplemented ops[#](https://docs.pytorch.org/docs/2.15/nested.html#unimplemented-ops "Link to this heading")

This error is becoming rarer as nested tensor op support grows, but it’s still possible to hit it today given that there are a couple thousand ops within PyTorch.

    NotImplementedError: aten.view\_as\_real.default

Copy to clipboard

The error is straightforward; we haven’t gotten around to adding op support for this particular op yet. If you’d like, you can [contribute](https://docs.pytorch.org/docs/2.15/nested.html#contributions)
 an implementation yourself OR simply [request](https://github.com/pytorch/pytorch/issues/118107)
 that we add support for this op in a future PyTorch release.

### Ragged structure incompatibility[#](https://docs.pytorch.org/docs/2.15/nested.html#ragged-structure-incompatibility "Link to this heading")

    RuntimeError: cannot call binary pointwise function add.Tensor with inputs of shapes (2, j2, 128) and (2, j3, 128)

Copy to clipboard

This error occurs when calling an op that operates over multiple NJTs with incompatible ragged structures. Currently, it is required that input NJTs have the exact same `offsets` constituent in order to have the same symbolic ragged structure symbol (e.g. `j1`).

As a workaround for this situation, it is possible to construct NJTs from the `values` and `offsets` components directly. With both NJTs referencing the same `offsets` components, they are considered to have the same ragged structure and are thus compatible.

\>>> a \= torch.randn(50, 128)
\>>> b \= torch.randn(32, 128)
\>>> nt1 \= torch.nested.nested\_tensor(\[a, b\], layout\=torch.jagged, dtype\=torch.float32)
\>>> nt2 \= torch.nested.nested\_tensor\_from\_jagged(values\=torch.randn(82, 128), offsets\=nt1.offsets())
\>>> nt3 \= nt1 + nt2
\>>> nt3.shape
torch.Size(\[2, j1, 128\])

Copy to clipboard

### Data dependent operation within torch.compile[#](https://docs.pytorch.org/docs/2.15/nested.html#data-dependent-operation-within-torch-compile "Link to this heading")

    torch.\_dynamo.exc.Unsupported: data dependent operator: aten.\_local\_scalar\_dense.default; to enable, set torch.\_dynamo.config.capture\_scalar\_outputs \= True

Copy to clipboard

This error occurs when calling an op that does data-dependent operation within torch.compile; this commonly occurs for ops that need to examine the values of the NJT’s `offsets` to determine the output shape. For example:

\>>> a \= torch.randn(50, 128)
\>>> b \= torch.randn(32, 128)
\>>> nt \= torch.nested.nested\_tensor(\[a, b\], layout\=torch.jagged, dtype\=torch.float32)
\>>> def f(nt): return nt.chunk(2, dim\=0)\[0\]
...
\>>> compiled\_f \= torch.compile(f, fullgraph\=True)
\>>> output \= compiled\_f(nt)

Copy to clipboard

In this example, calling `chunk()` on the batch dimension of the NJT requires examination of the NJT’s `offsets` data to delineate batch item boundaries within the packed ragged dimension. As a workaround, there are a couple torch.compile flags that can be set:

\>>> torch.\_dynamo.config.capture\_dynamic\_output\_shape\_ops \= True
\>>> torch.\_dynamo.config.capture\_scalar\_outputs \= True

Copy to clipboard

If, after setting these, you still see data-dependent operator errors, please file an issue with PyTorch. This area of `torch.compile()` is still in heavy development and certain aspects of NJT support may be incomplete.

Contributions[#](https://docs.pytorch.org/docs/2.15/nested.html#contributions "Link to this heading")

------------------------------------------------------------------------------------------------------

If you’d like to contribute to nested tensor development, one of the most impactful ways to do so is to add nested tensor support for a currently-unsupported PyTorch op. This process generally consists of a couple simple steps:

1.  Determine the name of the op to add; this should be something like `aten.view_as_real.default`. The signature for this op can be found in `aten/src/ATen/native/native_functions.yaml`.
    
2.  Register an op implementation in `torch/nested/_internal/ops.py`, following the pattern established there for other ops. Use the signature from `native_functions.yaml` for schema validation.
    

The most common way to implement an op is to unwrap the NJT into its constituents, redispatch the op on the underlying `values` buffer, and propagate the relevant NJT metadata (including `offsets`) to a new output NJT. If the output of the op is expected to have a different shape from the input, new `offsets`, etc. metadata must be computed.

When an op is applied over the batch or ragged dimension, these tricks can help quickly get a working implementation:

*   For _non-batchwise_ operation, an `unbind()`\-based fallback should work.
    
*   For operation on the ragged dimension, consider converting to padded dense with a properly-selected padding value that won’t negatively bias the output, running the op, and converting back to NJT. Within `torch.compile`, these conversions can be fused to avoid materializing the padded intermediate.
    

Detailed Docs for Construction and Conversion Functions[#](https://docs.pytorch.org/docs/2.15/nested.html#detailed-docs-for-construction-and-conversion-functions "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

torch.nested.nested\_tensor(_tensor\_list_, _\*_, _dtype\=None_, _layout\=None_, _device\=None_, _requires\_grad\=False_, _pin\_memory\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nested/__init__.py#L209)
[#](https://docs.pytorch.org/docs/2.15/nested.html#torch.nested.nested_tensor "Link to this definition")

Constructs a nested tensor with no autograd history (also known as a “leaf tensor”, see [Autograd mechanics](https://docs.pytorch.org/docs/2.15/notes/autograd.html#autograd-mechanics)
) from `tensor_list` a list of tensors.

Parameters:

*   **tensor\_list** (_List__\[__array\_like__\]_) – a list of tensors, or anything that can be passed to torch.tensor,
    
*   **dimensionality.** (_where each element_ _of_ _the list has the same_) –
    

Keyword Arguments:

*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    , optional) – the desired type of returned nested tensor. Default: if None, same [`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
     as leftmost tensor in the list.
    
*   **layout** ([`torch.layout`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")
    , optional) – the desired layout of returned nested tensor. Only strided and jagged layouts are supported. Default: if None, the strided layout.
    
*   **device** ([`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    , optional) – the desired device of returned nested tensor. Default: if None, same [`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
     as leftmost tensor in the list
    
*   **requires\_grad** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If autograd should record operations on the returned nested tensor. Default: `False`.
    
*   **pin\_memory** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If set, returned nested tensor would be allocated in the pinned memory. Works only for CPU tensors. Default: `False`.
    

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Example:

\>>> a \= torch.arange(3, dtype\=torch.float, requires\_grad\=True)
\>>> b \= torch.arange(5, dtype\=torch.float, requires\_grad\=True)
\>>> nt \= torch.nested.nested\_tensor(\[a, b\], layout\=torch.jagged, requires\_grad\=True)
\>>> nt.is\_leaf
True

Copy to clipboard

torch.nested.nested\_tensor\_from\_jagged(_values_, _offsets\=None_, _lengths\=None_, _jagged\_dim\=None_, _min\_seqlen\=None_, _max\_seqlen\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nested/__init__.py#L358)
[#](https://docs.pytorch.org/docs/2.15/nested.html#torch.nested.nested_tensor_from_jagged "Link to this definition")

Constructs a jagged layout nested tensor from the given jagged components. The jagged layout consists of a required values buffer with the jagged dimension packed into a single dimension. The offsets / lengths metadata determines how this dimension is split into batch elements and are expected to be allocated on the same device as the values buffer.

Expected metadata formats:

*   offsets: Indices within the packed dimension splitting it into heterogeneously-sized batch elements. Example: \[0, 2, 3, 6\] indicates that a packed jagged dim of size 6 should be conceptually split into batch elements of length \[2, 1, 3\]. Note that both the beginning and ending offsets are required for kernel convenience (i.e. shape batch\_size + 1).
    
*   lengths: Lengths of the individual batch elements; shape == batch\_size. Example: \[2, 1, 3\] indicates that a packed jagged dim of size 6 should be conceptually split into batch elements of length \[2, 1, 3\].
    

Note that it can be useful to provide both offsets and lengths. This describes a nested tensor with “holes”, where the offsets indicate the start position of each batch item and the length specifies the total number of elements (see example below).

The returned jagged layout nested tensor will be a view of the input values tensor.

Parameters:

*   **values** ([`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – The underlying buffer in the shape of (sum\_B(\*), D\_1, …, D\_N). The jagged dimension is packed into a single dimension, with the offsets / lengths metadata used to distinguish batch elements.
    
*   **offsets** (optional [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Offsets into the jagged dimension of shape B + 1.
    
*   **lengths** (optional [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Lengths of the batch elements of shape B.
    
*   **jagged\_dim** (_optional python:int_) – Indicates which dimension in values is the packed jagged dimension. Must be >= 1 as the batch dimension (dim=0) cannot be ragged. If None, this is set to dim=1 (i.e. the dimension immediately following the batch dimension). Default: None
    
*   **min\_seqlen** (_optional python:int_) – If set, uses the specified value as the cached minimum sequence length for the returned nested tensor. This can be a useful alternative to computing this value on-demand, possibly avoiding a GPU -> CPU sync. Default: None
    
*   **max\_seqlen** (_optional python:int_) – If set, uses the specified value as the cached maximum sequence length for the returned nested tensor. This can be a useful alternative to computing this value on-demand, possibly avoiding a GPU -> CPU sync. Default: None
    

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Example:

\>>> values \= torch.randn(12, 5)
\>>> offsets \= torch.tensor(\[0, 3, 5, 6, 10, 12\])
\>>> nt \= nested\_tensor\_from\_jagged(values, offsets)
\>>> \# 3D shape with the middle dimension jagged
\>>> nt.shape  \# xdoctest: +ELLIPSIS
torch.Size(\[5, j..., 5\])
\>>> \# Length of each item in the batch:
\>>> offsets.diff()
tensor(\[3, 2, 1, 4, 2\])

\>>> values \= torch.randn(6, 5)
\>>> offsets \= torch.tensor(\[0, 2, 3, 6\])
\>>> lengths \= torch.tensor(\[1, 1, 2\])
\>>> \# NT with holes
\>>> nt \= nested\_tensor\_from\_jagged(values, offsets, lengths)
\>>> a, b, c \= nt.unbind()
\>>> \# Batch item 1 consists of indices \[0, 1)\
\>>> torch.equal(a, values\[0:1, :\])\
True\
\>>> \# Batch item 2 consists of indices \[2, 3)\
\>>> torch.equal(b, values\[2:3, :\])\
True\
\>>> \# Batch item 3 consists of indices \[3, 5)\
\>>> torch.equal(c, values\[3:5, :\])\
True\
\
Copy to clipboard\
\
torch.nested.as\_nested\_tensor(_ts_, _dtype\=None_, _device\=None_, _layout\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nested/__init__.py#L21)\
[#](https://docs.pytorch.org/docs/2.15/nested.html#torch.nested.as_nested_tensor "Link to this definition")\
\
Constructs a nested tensor preserving autograd history from a tensor or a list / tuple of tensors.\
\
If a nested tensor is passed, it will be returned directly unless the device / dtype / layout differ. Note that converting device / dtype will result in a copy, while converting layout is not currently supported by this function.\
\
If a non-nested tensor is passed, it is treated as a batch of constituents of consistent size. A copy will be incurred if the passed device / dtype differ from those of the input OR if the input is non-contiguous. Otherwise, the input’s storage will be used directly.\
\
If a tensor list is provided, tensors in the list are always copied during construction of the nested tensor.\
\
Parameters:\
\
**ts** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
 _or_ _List__\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_\] or_ _Tuple__\[_[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
_\]_) – a tensor to treat as a nested tensor OR a list / tuple of tensors with the same ndim\
\
Keyword Arguments:\
\
*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")\
    , optional) – the desired type of returned nested tensor. Default: if None, same [`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")\
     as leftmost tensor in the list.\
    \
*   **device** ([`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")\
    , optional) – the desired device of returned nested tensor. Default: if None, same [`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")\
     as leftmost tensor in the list\
    \
*   **layout** ([`torch.layout`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")\
    , optional) – the desired layout of returned nested tensor. Only strided and jagged layouts are supported. Default: if None, the strided layout.\
    \
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
Example:\
\
\>>> a \= torch.arange(3, dtype\=torch.float, requires\_grad\=True)\
\>>> b \= torch.arange(5, dtype\=torch.float, requires\_grad\=True)\
\>>> nt \= torch.nested.as\_nested\_tensor(\[a, b\], layout\=torch.jagged)\
\>>> nt.is\_leaf\
False\
\>>> buffer \= torch.cat(\[torch.ones\_like(a), torch.zeros\_like(b)\])\
\>>> fake\_grad \= torch.nested.nested\_tensor\_from\_jagged(buffer, nt.offsets())\
\>>> nt.backward(fake\_grad)\
\>>> a.grad\
tensor(\[1., 1., 1.\])\
\>>> b.grad\
tensor(\[0., 0., 0., 0., 0.\])\
\>>> c \= torch.randn(3, 5, requires\_grad\=True)\
\>>> nt2 \= torch.nested.as\_nested\_tensor(c, layout\=torch.jagged)\
\
Copy to clipboard\
\
torch.nested.to\_padded\_tensor(_input_, _padding_, _output\_size\=None_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nested/__init__.py#L153)\
[#](https://docs.pytorch.org/docs/2.15/nested.html#torch.nested.to_padded_tensor "Link to this definition")\
\
Returns a new (non-nested) Tensor by padding the `input` nested tensor. The leading entries will be filled with the nested data, while the trailing entries will be padded.\
\
Warning\
\
[`to_padded_tensor()`](https://docs.pytorch.org/docs/2.15/nested.html#torch.nested.to_padded_tensor "torch.nested.to_padded_tensor")\
 always copies the underlying data, since the nested and the non-nested tensors differ in memory layout.\
\
Parameters:\
\
**padding** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
) – The padding value for the trailing entries.\
\
Keyword Arguments:\
\
*   **output\_size** (_Tuple__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – The size of the output tensor. If given, it must be large enough to contain all nested data; else, will infer by taking the max size of each nested sub-tensor along each dimension.\
    \
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _,_ _optional_) – the output tensor.\
    \
\
Example:\
\
\>>> nt \= torch.nested.nested\_tensor(\[torch.randn((2, 5)), torch.randn((3, 4))\])\
nested\_tensor(\[\
  tensor(\[\[ 1.6862, -1.1282,  1.1031,  0.0464, -1.3276\],\
          \[-1.9967, -1.0054,  1.8972,  0.9174, -1.4995\]\]),\
  tensor(\[\[-1.8546, -0.7194, -0.2918, -0.1846\],\
          \[ 0.2773,  0.8793, -0.5183, -0.6447\],\
          \[ 1.8009,  1.8468, -0.9832, -1.5272\]\])\
\])\
\>>> pt\_infer \= torch.nested.to\_padded\_tensor(nt, 0.0)\
tensor(\[\[\[ 1.6862, -1.1282,  1.1031,  0.0464, -1.3276\],\
         \[-1.9967, -1.0054,  1.8972,  0.9174, -1.4995\],\
         \[ 0.0000,  0.0000,  0.0000,  0.0000,  0.0000\]\],\
        \[\[-1.8546, -0.7194, -0.2918, -0.1846,  0.0000\],\
         \[ 0.2773,  0.8793, -0.5183, -0.6447,  0.0000\],\
         \[ 1.8009,  1.8468, -0.9832, -1.5272,  0.0000\]\]\])\
\>>> pt\_large \= torch.nested.to\_padded\_tensor(nt, 1.0, (2, 4, 6))\
tensor(\[\[\[ 1.6862, -1.1282,  1.1031,  0.0464, -1.3276,  1.0000\],\
         \[-1.9967, -1.0054,  1.8972,  0.9174, -1.4995,  1.0000\],\
         \[ 1.0000,  1.0000,  1.0000,  1.0000,  1.0000,  1.0000\],\
         \[ 1.0000,  1.0000,  1.0000,  1.0000,  1.0000,  1.0000\]\],\
        \[\[-1.8546, -0.7194, -0.2918, -0.1846,  1.0000,  1.0000\],\
         \[ 0.2773,  0.8793, -0.5183, -0.6447,  1.0000,  1.0000\],\
         \[ 1.8009,  1.8468, -0.9832, -1.5272,  1.0000,  1.0000\],\
         \[ 1.0000,  1.0000,  1.0000,  1.0000,  1.0000,  1.0000\]\]\])\
\>>> pt\_small \= torch.nested.to\_padded\_tensor(nt, 2.0, (2, 2, 2))\
RuntimeError: Value in output\_size is less than NestedTensor padded size. Truncation is not supported.\
\
Copy to clipboard\
\
torch.nested.masked\_select(_tensor_, _mask_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nested/__init__.py#L469)\
[#](https://docs.pytorch.org/docs/2.15/nested.html#torch.nested.masked_select "Link to this definition")\
\
Constructs a nested tensor given a strided tensor input and a strided mask, the resulting jagged layout nested tensor will have values retain values where the mask is equal to True. The dimensionality of the mask is preserved and is represented with the offsets, this is unlike [`masked_select()`](https://docs.pytorch.org/docs/2.15/nested.html#torch.nested.masked_select "torch.nested.masked_select")\
 where the output is collapsed to a 1D tensor.\
\
Args: tensor ([`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
): a strided tensor from which the jagged layout nested tensor is constructed from. mask ([`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
): a strided mask tensor which is applied to the tensor input\
\
Example:\
\
\>>> tensor \= torch.randn(3, 3)\
\>>> mask \= torch.tensor(\[\[False, False, True\], \[True, False, True\], \[False, False, True\]\])\
\>>> nt \= torch.nested.masked\_select(tensor, mask)\
\>>> nt.shape  \# xdoctest: +ELLIPSIS\
torch.Size(\[3, j...\])\
\>>> \# Length of each item in the batch:\
\>>> nt.offsets().diff()\
tensor(\[1, 2, 1\])\
\
\>>> tensor \= torch.randn(6, 5)\
\>>> mask \= torch.tensor(\[False\])\
\>>> nt \= torch.nested.masked\_select(tensor, mask)\
\>>> nt.shape  \# xdoctest: +ELLIPSIS\
torch.Size(\[6, j...\])\
\>>> \# Length of each item in the batch:\
\>>> nt.offsets().diff()\
tensor(\[0, 0, 0, 0, 0, 0\])\
\
Copy to clipboard\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
torch.nested.narrow(_tensor_, _dim_, _start_, _length_, _layout\=torch.strided_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nested/__init__.py#L280)\
[#](https://docs.pytorch.org/docs/2.15/nested.html#torch.nested.narrow "Link to this definition")\
\
Constructs a nested tensor (which might be a view) from `tensor`, a strided tensor. This follows similar semantics to torch.Tensor.narrow, where in the `dim`\-th dimension the new nested tensor shows only the elements in the interval \[start, start+length). As nested representations allow for a different start and length at each ‘row’ of that dimension, `start` and `length` can also be tensors of shape tensor.shape\[0\].\
\
There’s some differences depending on the layout you use for the nested tensor. If using strided layout, torch.narrow will do a copy of the narrowed data into a contiguous NT with strided layout, while jagged layout narrow() will create a non-contiguous view of your original strided tensor. This particular representation is really useful for representing kv-caches in Transformer models, as specialized SDPA kernels can deal with format easily, resulting in performance improvements.\
\
Parameters:\
\
*   **tensor** ([`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – a strided tensor, which will be used as the underlying data for the nested tensor if using the jagged layout or will be copied for the strided layout.\
    \
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – the dimension where narrow will be applied. Only dim=1 is supported for the jagged layout, while strided supports all dim\
    \
*   **start** (Union\[int, [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    \]) – starting element for the narrow operation\
    \
*   **length** (Union\[int, [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    \]) – number of elements taken during the narrow op\
    \
\
Keyword Arguments:\
\
**layout** ([`torch.layout`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.layout "torch.layout")\
, optional) – the desired layout of returned nested tensor. Only strided and jagged layouts are supported. Default: if None, the strided layout.\
\
Return type:\
\
[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\
Example:\
\
\>>> starts \= torch.tensor(\[0, 1, 2, 3, 4\], dtype\=torch.int64)\
\>>> lengths \= torch.tensor(\[3, 2, 2, 1, 5\], dtype\=torch.int64)\
\>>> narrow\_base \= torch.randn(5, 10, 20)\
\>>> nt\_narrowed \= torch.nested.narrow(narrow\_base, 1, starts, lengths, layout\=torch.jagged)\
\>>> nt\_narrowed.is\_contiguous()\
False\
\
Copy to clipboard\
\
See also\
\
[Accelerating PyTorch Transformers by replacing nn.Transformer with Nested Tensors and torch.compile](https://docs.pytorch.org/tutorials/intermediate/transformer_building_blocks.html)\
\
On this page\
\
[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/nested.md)\
\
[Show Source](https://docs.pytorch.org/docs/2.15/_sources/nested.md.txt)\
\
PyTorch Libraries\
\
*   [ExecuTorch](https://docs.pytorch.org/executorch)\
    \
*   [Helion](https://docs.pytorch.org/helion)\
    \
*   [torchao](https://docs.pytorch.org/ao)\
    \
*   [kineto](https://github.com/pytorch/kineto)\
    \
*   [torchtitan](https://github.com/pytorch/torchtitan)\
    \
*   [TorchRL](https://docs.pytorch.org/rl)\
    \
*   [torchvision](https://docs.pytorch.org/vision)\
    \
*   [torchaudio](https://docs.pytorch.org/audio)\
    \
*   [tensordict](https://docs.pytorch.org/tensordict)\
    \
*   [PyTorch on XLA Devices](https://docs.pytorch.org/xla)\
    \
\
Docs\
----\
\
Access comprehensive developer documentation for PyTorch\
\
[View Docs](https://docs.pytorch.org/docs/stable/index.html)\
\
Tutorials\
---------\
\
Get in-depth tutorials for beginners and advanced developers\
\
[View Tutorials](https://docs.pytorch.org/tutorials)\
\
Resources\
---------\
\
Find development resources and get your questions answered\
\
[View Resources](https://pytorch.org/resources)\
\
To analyze traffic and optimize your experience, we serve cookies on this site. By clicking or navigating, you agree to allow our usage of cookies. As the current maintainers of this site, Facebook’s Cookies Policy applies. Learn more, including about available controls: [Cookies Policy](https://opensource.fb.com/legal/cookie-policy)\
.\
\
|     |     |\
| --- | --- |\
|     |     |\
\
|     |     |\
| --- | --- |\
|     |     |