Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.MaxPool2d.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.MaxPool2d.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.MaxPool2d.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.MaxPool2d.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.MaxPool2d.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.MaxPool2d.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.MaxPool2d.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.MaxPool2d.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.MaxPool2d.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.MaxPool2d.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.MaxPool2d.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.MaxPool2d.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.MaxPool2d.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.MaxPool2d.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.MaxPool2d.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.MaxPool2d.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.MaxPool2d.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.MaxPool2d.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.MaxPool2d.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.MaxPool2d.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.MaxPool2d.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.MaxPool2d.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.MaxPool2d.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.MaxPool2d.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.MaxPool2d.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.MaxPool2d.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.MaxPool2d.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.MaxPool2d.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.MaxPool2d.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.MaxPool2d.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.MaxPool2d.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.MaxPool2d.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.MaxPool2d.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.MaxPool2d.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.MaxPool2d.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.MaxPool2d.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.MaxPool2d.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.MaxPool2d.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.MaxPool2d.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.MaxPool2d.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.MaxPool2d.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.MaxPool2d.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.MaxPool2d.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.MaxPool2d.html)

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

MaxPool2d[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.MaxPool2d.html#maxpool2d "Link to this heading")

====================================================================================================================

_class_ torch.nn.MaxPool2d(_kernel\_size_, _stride\=None_, _padding\=0_, _dilation\=1_, _return\_indices\=False_, _ceil\_mode\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/pooling.py#L155)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.MaxPool2d.html#torch.nn.MaxPool2d "Link to this definition")

Applies a 2D max pooling over an input signal composed of several input planes.

In the simplest case, the output value of the layer with input size (N,C,H,W)(N, C, H, W)(N,C,H,W), output (N,C,Hout,Wout)(N, C, H\_{out}, W\_{out})(N,C,Hout​,Wout​) and `kernel_size` (kH,kW)(kH, kW)(kH,kW) can be precisely described as:

out(Ni,Cj,h,w)\=max⁡m\=0,…,kH−1max⁡n\=0,…,kW−1input(Ni,Cj,stride\[0\]×h+m,stride\[1\]×w+n)\\begin{aligned} out(N\_i, C\_j, h, w) ={} & \\max\_{m=0, \\ldots, kH-1} \\max\_{n=0, \\ldots, kW-1} \\\\ & \\text{input}(N\_i, C\_j, \\text{stride\[0\]} \\times h + m, \\text{stride\[1\]} \\times w + n) \\end{aligned} out(Ni​,Cj​,h,w)\=​m\=0,…,kH−1max​n\=0,…,kW−1max​input(Ni​,Cj​,stride\[0\]×h+m,stride\[1\]×w+n)​

If `padding` is non-zero, then the input is implicitly padded with negative infinity on both sides for `padding` number of points. `dilation` controls the spacing between the kernel points. It is harder to describe, but this [link](https://github.com/vdumoulin/conv_arithmetic/blob/master/README.md)
 has a nice visualization of what `dilation` does.

Note

When ceil\_mode=True, sliding windows are allowed to go off-bounds if they start within the left padding or the input. Sliding windows that would start in the right padded region are ignored.

The parameters `kernel_size`, `stride`, `padding`, `dilation` can either be:

> *   a single `int` – in which case the same value is used for the height and width dimension
>     
> *   a `tuple` of two ints – in which case, the first int is used for the height dimension, and the second int for the width dimension
>     

Parameters:

*   **kernel\_size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – the size of the window to take a max over
    
*   **stride** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – the stride of the window. Default value is `kernel_size`
    
*   **padding** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – Implicit negative infinity padding to be added on both sides
    
*   **dilation** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – a parameter that controls the stride of elements in the window
    
*   **return\_indices** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – if `True`, will return the max indices along with the outputs. Useful for [`torch.nn.MaxUnpool2d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.MaxUnpool2d.html#torch.nn.MaxUnpool2d "torch.nn.MaxUnpool2d")
     later
    
*   **ceil\_mode** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – when True, will use ceil instead of floor to compute the output shape
    

Shape:

*   Input: (N,C,Hin,Win)(N, C, H\_{in}, W\_{in})(N,C,Hin​,Win​) or (C,Hin,Win)(C, H\_{in}, W\_{in})(C,Hin​,Win​)
    
*   Output: (N,C,Hout,Wout)(N, C, H\_{out}, W\_{out})(N,C,Hout​,Wout​) or (C,Hout,Wout)(C, H\_{out}, W\_{out})(C,Hout​,Wout​), where
    
    Hout\=⌊Hin+2∗padding\[0\]−dilation\[0\]×(kernel\_size\[0\]−1)−1stride\[0\]+1⌋H\_{out} = \\left\\lfloor\\frac{H\_{in} + 2 \* \\text{padding\[0\]} - \\text{dilation\[0\]} \\times (\\text{kernel\\\_size\[0\]} - 1) - 1}{\\text{stride\[0\]}} + 1\\right\\rfloor Hout​\=⌊stride\[0\]Hin​+2∗padding\[0\]−dilation\[0\]×(kernel\_size\[0\]−1)−1​+1⌋
    
    Wout\=⌊Win+2∗padding\[1\]−dilation\[1\]×(kernel\_size\[1\]−1)−1stride\[1\]+1⌋W\_{out} = \\left\\lfloor\\frac{W\_{in} + 2 \* \\text{padding\[1\]} - \\text{dilation\[1\]} \\times (\\text{kernel\\\_size\[1\]} - 1) - 1}{\\text{stride\[1\]}} + 1\\right\\rfloor Wout​\=⌊stride\[1\]Win​+2∗padding\[1\]−dilation\[1\]×(kernel\_size\[1\]−1)−1​+1⌋
    

Examples:

\>>> \# pool of square window of size=3, stride=2
\>>> m \= nn.MaxPool2d(3, stride\=2)
\>>> \# pool of non-square window
\>>> m \= nn.MaxPool2d((3, 2), stride\=(2, 1))
\>>> input \= torch.randn(20, 16, 50, 32)
\>>> output \= m(input)

Copy to clipboard

forward(_input_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/pooling.py#L222)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.MaxPool2d.html#torch.nn.MaxPool2d.forward "Link to this definition")

Runs the forward pass.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.MaxPool2d.rst.txt)

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