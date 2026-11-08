Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Conv1d.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.Conv1d.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Conv1d.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.Conv1d.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.Conv1d.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.Conv1d.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.Conv1d.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.Conv1d.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.Conv1d.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.Conv1d.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.Conv1d.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.Conv1d.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.Conv1d.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.Conv1d.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.Conv1d.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.Conv1d.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.Conv1d.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.Conv1d.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.Conv1d.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.Conv1d.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.Conv1d.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.Conv1d.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.Conv1d.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.Conv1d.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.Conv1d.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.Conv1d.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.Conv1d.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.Conv1d.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.Conv1d.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.Conv1d.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.Conv1d.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.Conv1d.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.Conv1d.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.Conv1d.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.Conv1d.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.Conv1d.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.Conv1d.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.Conv1d.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.Conv1d.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.Conv1d.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.Conv1d.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.Conv1d.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.Conv1d.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.Conv1d.html)

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

Conv1d[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Conv1d.html#conv1d "Link to this heading")

===========================================================================================================

_class_ torch.nn.Conv1d(_in\_channels_, _out\_channels_, _kernel\_size_, _stride\=1_, _padding\=0_, _dilation\=1_, _groups\=1_, _bias\=True_, _padding\_mode\='zeros'_, _device\=None_, _dtype\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/conv.py#L225)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Conv1d.html#torch.nn.Conv1d "Link to this definition")

Applies a 1D convolution over an input signal composed of several input planes.

In the simplest case, the output value of the layer with input size (N,Cin,L)(N, C\_{\\text{in}}, L)(N,Cin​,L) and output (N,Cout,Lout)(N, C\_{\\text{out}}, L\_{\\text{out}})(N,Cout​,Lout​) can be precisely described as:

out(Ni,Coutj)\=bias(Coutj)+∑k\=0Cin−1weight(Coutj,k)⋆input(Ni,k)\\text{out}(N\_i, C\_{\\text{out}\_j}) = \\text{bias}(C\_{\\text{out}\_j}) + \\sum\_{k = 0}^{C\_{in} - 1} \\text{weight}(C\_{\\text{out}\_j}, k) \\star \\text{input}(N\_i, k) out(Ni​,Coutj​​)\=bias(Coutj​​)+k\=0∑Cin​−1​weight(Coutj​​,k)⋆input(Ni​,k)

where ⋆\\star⋆ is the valid [cross-correlation](https://en.wikipedia.org/wiki/Cross-correlation)
 operator, NNN is a batch size, CCC denotes a number of channels, LLL is a length of signal sequence.

This module supports [TensorFloat32](https://docs.pytorch.org/docs/2.15/notes/cuda.html#tf32-on-ampere)
.

On certain ROCm devices, when using float16 inputs this module will use [different precision](https://docs.pytorch.org/docs/2.15/notes/numerical_accuracy.html#fp16-on-mi200)
 for backward.

*   `stride` controls the stride for the cross-correlation, a single number or a one-element tuple.
    
*   `padding` controls the amount of padding applied to the input. It can be either a string {‘valid’, ‘same’} or a tuple of ints giving the amount of implicit padding applied on both sides.
    
*   `dilation` controls the spacing between the kernel points; also known as the à trous algorithm. It is harder to describe, but this [link](https://github.com/vdumoulin/conv_arithmetic/blob/master/README.md)
     has a nice visualization of what `dilation` does.
    
*   `groups` controls the connections between inputs and outputs. `in_channels` and `out_channels` must both be divisible by `groups`. For example,
    
    > *   At groups=1, all inputs are convolved to all outputs.
    >     
    > *   At groups=2, the operation becomes equivalent to having two conv layers side by side, each seeing half the input channels and producing half the output channels, and both subsequently concatenated.
    >     
    > *   At groups= `in_channels`, each input channel is convolved with its own set of filters (of size out\_channelsin\_channels\\frac{\\text{out\\\_channels}}{\\text{in\\\_channels}}in\_channelsout\_channels​).
    >     
    

Note

When groups == in\_channels and out\_channels == K \* in\_channels, where K is a positive integer, this operation is also known as a “depthwise convolution”.

In other words, for an input of size (N,Cin,Lin)(N, C\_{in}, L\_{in})(N,Cin​,Lin​), a depthwise convolution with a depthwise multiplier K can be performed with the arguments (Cin\=Cin,Cout\=Cin×K,...,groups\=Cin)(C\_\\text{in}=C\_\\text{in}, C\_\\text{out}=C\_\\text{in} \\times \\text{K}, ..., \\text{groups}=C\_\\text{in})(Cin​\=Cin​,Cout​\=Cin​×K,...,groups\=Cin​).

Note

In some circumstances when given tensors on a CUDA device and using CuDNN, this operator may select a nondeterministic algorithm to increase performance. If this is undesirable, you can try to make the operation deterministic (potentially at a performance cost) by setting `torch.backends.cudnn.deterministic = True`. See [Reproducibility](https://docs.pytorch.org/docs/2.15/notes/randomness.html)
 for more information.

Note

`padding='valid'` is the same as no padding. `padding='same'` pads the input so the output has the shape as the input. However, this mode doesn’t support any stride values other than 1.

Note

This module supports complex data types i.e. `complex32, complex64, complex128`.

Parameters:

*   **in\_channels** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Number of channels in the input image
    
*   **out\_channels** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Number of channels produced by the convolution
    
*   **kernel\_size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    ) – Size of the convolving kernel
    
*   **stride** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _,_ _optional_) – Stride of the convolution. Default: 1
    
*   **padding** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
     _or_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – Padding added to both sides of the input. Default: 0
    
*   **dilation** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _,_ _optional_) – Spacing between kernel elements. Default: 1
    
*   **groups** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – Number of blocked connections from input channels to output channels. Default: 1
    
*   **bias** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True`, adds a learnable bias to the output. Default: `True`
    
*   **padding\_mode** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – `'zeros'`, `'reflect'`, `'replicate'` or `'circular'`. Default: `'zeros'`
    

Shape:

*   Input: (N,Cin,Lin)(N, C\_{in}, L\_{in})(N,Cin​,Lin​) or (Cin,Lin)(C\_{in}, L\_{in})(Cin​,Lin​)
    
*   Output: (N,Cout,Lout)(N, C\_{out}, L\_{out})(N,Cout​,Lout​) or (Cout,Lout)(C\_{out}, L\_{out})(Cout​,Lout​), where
    
    Lout\=⌊Lin+2×padding−dilation×(kernel\_size−1)−1stride+1⌋L\_{out} = \\left\\lfloor\\frac{L\_{in} + 2 \\times \\text{padding} - \\text{dilation} \\times (\\text{kernel\\\_size} - 1) - 1}{\\text{stride}} + 1\\right\\rfloor Lout​\=⌊strideLin​+2×padding−dilation×(kernel\_size−1)−1​+1⌋
    

Variables:

*   **weight** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the learnable weights of the module of shape (out\_channels,in\_channelsgroups,kernel\_size)(\\text{out\\\_channels}, \\frac{\\text{in\\\_channels}}{\\text{groups}}, \\text{kernel\\\_size})(out\_channels,groupsin\_channels​,kernel\_size). The values of these weights are sampled from U(−k,k)\\mathcal{U}(-\\sqrt{k}, \\sqrt{k})U(−k​,k​) where k\=groupsCin∗kernel\_sizek = \\frac{groups}{C\_\\text{in} \* \\text{kernel\\\_size}}k\=Cin​∗kernel\_sizegroups​
    
*   **bias** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the learnable bias of the module of shape (out\_channels). If `bias` is `True`, then the values of these weights are sampled from U(−k,k)\\mathcal{U}(-\\sqrt{k}, \\sqrt{k})U(−k​,k​) where k\=groupsCin∗kernel\_sizek = \\frac{groups}{C\_\\text{in} \* \\text{kernel\\\_size}}k\=Cin​∗kernel\_sizegroups​
    

Examples:

\>>> m \= nn.Conv1d(16, 33, 3, stride\=2)
\>>> input \= torch.randn(20, 16, 50)
\>>> output \= m(input)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.Conv1d.rst.txt)

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