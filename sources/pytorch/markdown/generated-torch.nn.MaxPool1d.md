Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.MaxPool1d.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.MaxPool1d.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.MaxPool1d.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.MaxPool1d.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.MaxPool1d.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.MaxPool1d.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.MaxPool1d.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.MaxPool1d.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.MaxPool1d.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.MaxPool1d.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.MaxPool1d.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.MaxPool1d.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.MaxPool1d.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.MaxPool1d.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.MaxPool1d.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.MaxPool1d.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.MaxPool1d.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.MaxPool1d.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.MaxPool1d.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.MaxPool1d.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.MaxPool1d.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.MaxPool1d.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.MaxPool1d.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.MaxPool1d.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.MaxPool1d.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.MaxPool1d.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.MaxPool1d.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.MaxPool1d.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.MaxPool1d.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.MaxPool1d.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.MaxPool1d.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.MaxPool1d.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.MaxPool1d.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.MaxPool1d.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.MaxPool1d.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.MaxPool1d.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.MaxPool1d.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.MaxPool1d.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.MaxPool1d.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.MaxPool1d.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.MaxPool1d.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.MaxPool1d.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.MaxPool1d.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.MaxPool1d.html)

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

MaxPool1d[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.MaxPool1d.html#maxpool1d "Link to this heading")

====================================================================================================================

_class_ torch.nn.MaxPool1d(_kernel\_size_, _stride\=None_, _padding\=0_, _dilation\=1_, _return\_indices\=False_, _ceil\_mode\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/pooling.py#L79)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.MaxPool1d.html#torch.nn.MaxPool1d "Link to this definition")

Applies a 1D max pooling over an input signal composed of several input planes.

In the simplest case, the output value of the layer with input size (N,C,L)(N, C, L)(N,C,L) and output (N,C,Lout)(N, C, L\_{out})(N,C,Lout​) can be precisely described as:

out(Ni,Cj,k)\=max⁡m\=0,…,kernel\_size−1input(Ni,Cj,stride×k+m)out(N\_i, C\_j, k) = \\max\_{m=0, \\ldots, \\text{kernel\\\_size} - 1} input(N\_i, C\_j, stride \\times k + m) out(Ni​,Cj​,k)\=m\=0,…,kernel\_size−1max​input(Ni​,Cj​,stride×k+m)

If `padding` is non-zero, then the input is implicitly padded with negative infinity on both sides for `padding` number of points. `dilation` is the stride between the elements within the sliding window. This [link](https://github.com/vdumoulin/conv_arithmetic/blob/master/README.md)
 has a nice visualization of the pooling parameters.

Note

When ceil\_mode=True, sliding windows are allowed to go off-bounds if they start within the left padding or the input. Sliding windows that would start in the right padded region are ignored.

Parameters:

*   **kernel\_size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – The size of the sliding window, must be > 0.
    
*   **stride** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – The stride of the sliding window, must be > 0. Default value is `kernel_size`.
    
*   **padding** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – Implicit negative infinity padding to be added on both sides, must be >= 0 and <= kernel\_size / 2.
    
*   **dilation** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – The stride between elements within a sliding window, must be > 0.
    
*   **return\_indices** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True`, will return the argmax along with the max values. Useful for [`torch.nn.MaxUnpool1d`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.MaxUnpool1d.html#torch.nn.MaxUnpool1d "torch.nn.MaxUnpool1d")
     later
    
*   **ceil\_mode** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True`, will use ceil instead of floor to compute the output shape. This ensures that every element in the input tensor is covered by a sliding window.
    

Shape:

*   Input: (N,C,Lin)(N, C, L\_{in})(N,C,Lin​) or (C,Lin)(C, L\_{in})(C,Lin​).
    
*   Output: (N,C,Lout)(N, C, L\_{out})(N,C,Lout​) or (C,Lout)(C, L\_{out})(C,Lout​),
    
    where `ceil_mode = False`
    
    Lout\=⌊Lin+2×padding−dilation×(kernel\_size−1)−1stride⌋+1L\_{out} = \\left\\lfloor \\frac{L\_{in} + 2 \\times \\text{padding} - \\text{dilation} \\times (\\text{kernel\\\_size} - 1) - 1}{\\text{stride}}\\right\\rfloor + 1 Lout​\=⌊strideLin​+2×padding−dilation×(kernel\_size−1)−1​⌋+1
    
    where `ceil_mode = True`
    
    Lout\=⌊Lin+2×padding−dilation×(kernel\_size−1)−1+(stride−1)stride⌋+1L\_{out} = \\left\\lfloor \\frac{L\_{in} + 2 \\times \\text{padding} - \\text{dilation} \\times (\\text{kernel\\\_size} - 1) - 1 + (\\text{stride} - 1)}{\\text{stride}}\\right\\rfloor + 1 Lout​\=⌊strideLin​+2×padding−dilation×(kernel\_size−1)−1+(stride−1)​⌋+1
    
*   Ensure that the last pooling starts inside the image, make Lout\=Lout−1L\_{out} = L\_{out} - 1Lout​\=Lout​−1 when (Lout−1)∗stride\>\=Lin+padding(L\_{out} - 1) \* \\text{stride} >= L\_{in} + \\text{padding}(Lout​−1)∗stride\>=Lin​+padding.
    

Examples:

\>>> \# pool of size=3, stride=2
\>>> m \= nn.MaxPool1d(3, stride\=2)
\>>> input \= torch.randn(20, 16, 50)
\>>> output \= m(input)

Copy to clipboard

forward(_input_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/pooling.py#L142)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.MaxPool1d.html#torch.nn.MaxPool1d.forward "Link to this definition")

Runs the forward pass.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.MaxPool1d.rst.txt)

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