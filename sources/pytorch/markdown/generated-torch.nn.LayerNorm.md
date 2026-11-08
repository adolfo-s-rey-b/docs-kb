Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.LayerNorm.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.LayerNorm.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.LayerNorm.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.LayerNorm.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.LayerNorm.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.LayerNorm.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.LayerNorm.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.LayerNorm.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.LayerNorm.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.LayerNorm.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.LayerNorm.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.LayerNorm.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.LayerNorm.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.LayerNorm.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.LayerNorm.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.LayerNorm.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.LayerNorm.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.LayerNorm.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.LayerNorm.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.LayerNorm.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.LayerNorm.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.LayerNorm.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.LayerNorm.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.LayerNorm.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.LayerNorm.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.LayerNorm.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.LayerNorm.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.LayerNorm.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.LayerNorm.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.LayerNorm.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.LayerNorm.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.LayerNorm.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.LayerNorm.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.LayerNorm.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.LayerNorm.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.LayerNorm.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.LayerNorm.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.LayerNorm.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.LayerNorm.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.LayerNorm.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.LayerNorm.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.LayerNorm.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.LayerNorm.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.LayerNorm.html)

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

LayerNorm[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.LayerNorm.html#layernorm "Link to this heading")

====================================================================================================================

_class_ torch.nn.LayerNorm(_normalized\_shape_, _eps\=1e-05_, _elementwise\_affine\=True_, _bias\=True_, _device\=None_, _dtype\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/normalization.py#L105)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.LayerNorm.html#torch.nn.LayerNorm "Link to this definition")

Applies Layer Normalization over a mini-batch of inputs.

This layer implements the operation as described in the paper [Layer Normalization](https://arxiv.org/abs/1607.06450)

y\=x−E\[x\]Var\[x\]+ϵ∗γ+βy = \\frac{x - \\mathrm{E}\[x\]}{ \\sqrt{\\mathrm{Var}\[x\] + \\epsilon}} \* \\gamma + \\beta y\=Var\[x\]+ϵ​x−E\[x\]​∗γ+β

The mean and standard-deviation are calculated over the last D dimensions, where D is the dimension of `normalized_shape`. For example, if `normalized_shape` is `(3, 5)` (a 2-dimensional shape), the mean and standard-deviation are computed over the last 2 dimensions of the input (i.e. `input.mean((-2, -1))`). γ\\gammaγ and β\\betaβ are learnable affine transform parameters of `normalized_shape` if `elementwise_affine` is `True`. The variance is calculated via the biased estimator, equivalent to torch.var(input, correction=0).

Note

Unlike Batch Normalization and Instance Normalization, which applies scalar scale and bias for each entire channel/plane with the `affine` option, Layer Normalization applies per-element scale and bias with `elementwise_affine`.

This layer uses statistics computed from input data in both training and evaluation modes.

Parameters:

*   **normalized\_shape** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
     _or_ [_torch.Size_](https://docs.pytorch.org/docs/2.15/size.html#torch.Size "torch.Size")
    ) –
    
    input shape from an expected input of size
    
    \[∗×normalized\_shape\[0\]×normalized\_shape\[1\]×…×normalized\_shape\[−1\]\]\[\* \\times \\text{normalized\\\_shape}\[0\] \\times \\text{normalized\\\_shape}\[1\] \\times \\ldots \\times \\text{normalized\\\_shape}\[-1\]\] \[∗×normalized\_shape\[0\]×normalized\_shape\[1\]×…×normalized\_shape\[−1\]\]
    
    If a single integer is used, it is treated as a singleton list, and this module will normalize over the last dimension which is expected to be of that specific size.
    
*   **eps** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – a value added to the denominator for numerical stability. Default: 1e-5
    
*   **elementwise\_affine** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – a boolean value that when set to `True`, this module has learnable per-element affine parameters initialized to ones (for weights) and zeros (for biases). Default: `True`
    
*   **bias** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If set to `False`, the layer will not learn an additive bias (only relevant if `elementwise_affine` is `True`). Default: `True`
    

Variables:

*   **weight** – the learnable weights of the module of shape normalized\_shape\\text{normalized\\\_shape}normalized\_shape when `elementwise_affine` is set to `True`. The values are initialized to 1.
    
*   **bias** – the learnable bias of the module of shape normalized\_shape\\text{normalized\\\_shape}normalized\_shape when `elementwise_affine` is set to `True`. The values are initialized to 0.
    

Shape:

*   Input: (N,∗)(N, \*)(N,∗)
    
*   Output: (N,∗)(N, \*)(N,∗) (same shape as input)
    

Examples:

\>>> \# NLP Example
\>>> batch, sentence\_length, embedding\_dim \= 20, 5, 10
\>>> embedding \= torch.randn(batch, sentence\_length, embedding\_dim)
\>>> layer\_norm \= nn.LayerNorm(embedding\_dim)
\>>> \# Activate module
\>>> layer\_norm(embedding)
\>>>
\>>> \# Image Example
\>>> N, C, H, W \= 20, 5, 10, 10
\>>> input \= torch.randn(N, C, H, W)
\>>> \# Normalize over the last three dimensions (i.e. the channel and spatial dimensions)
\>>> \# as shown in the image below
\>>> layer\_norm \= nn.LayerNorm(\[C, H, W\])
\>>> output \= layer\_norm(input)

Copy to clipboard

[![../_images/layer_norm.jpg](https://docs.pytorch.org/docs/2.15/_images/layer_norm.jpg)](https://docs.pytorch.org/docs/2.15/_images/layer_norm.jpg)

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.LayerNorm.rst.txt)

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