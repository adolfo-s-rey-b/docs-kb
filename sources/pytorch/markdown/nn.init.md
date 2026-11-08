Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/nn.init.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/nn.init.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/nn.init.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/nn.init.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/nn.init.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/nn.init.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/nn.init.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/nn.init.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/nn.init.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/nn.init.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/nn.init.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/nn.init.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/nn.init.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/nn.init.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/nn.init.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/nn.init.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/nn.init.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/nn.init.html)
[v1.13](https://docs.pytorch.org/docs/1.13/nn.init.html)
[v1.12](https://docs.pytorch.org/docs/1.12/nn.init.html)
[v1.11](https://docs.pytorch.org/docs/1.11/nn.init.html)
[v1.10](https://docs.pytorch.org/docs/1.10/nn.init.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/nn.init.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/nn.init.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/nn.init.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/nn.init.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/nn.init.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/nn.init.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/nn.init.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/nn.init.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/nn.init.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/nn.init.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/nn.init.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/nn.init.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/nn.init.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/nn.init.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/nn.init.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/nn.init.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/nn.init.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/nn.init.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/nn.init.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/nn.init.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/nn.init.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/nn.init.html)

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

torch.nn.init[#](https://docs.pytorch.org/docs/2.15/nn.init.html#torch-nn-init "Link to this heading")

=======================================================================================================

Created On: Jun 11, 2019 | Last Updated On: May 12, 2026

Warning

All the functions in this module are intended to be used to initialize neural network parameters, so they all run in [`torch.no_grad()`](https://docs.pytorch.org/docs/2.15/generated/torch.no_grad.html#torch.no_grad "torch.no_grad")
 mode and will not be taken into account by autograd.

torch.nn.init.calculate\_gain(_nonlinearity_, _param\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/init.py#L173)
[#](https://docs.pytorch.org/docs/2.15/nn.init.html#torch.nn.init.calculate_gain "Link to this definition")

Return the recommended gain value for the given nonlinearity function.

The values are as follows:

| nonlinearity | gain |
| --- | --- |
| Linear / Identity | 111 |
| Conv{1,2,3}D | 111 |
| Sigmoid | 111 |
| Tanh | 53\\frac{5}{3}35​ |
| ReLU | 2\\sqrt{2}2​ |
| Leaky Relu | 21+negative\_slope2\\sqrt{\\frac{2}{1 + \\text{negative\\\_slope}^2}}1+negative\_slope22​​ |
| SELU | 34\\frac{3}{4}43​ |

Warning

In order to implement [Self-Normalizing Neural Networks](https://papers.nips.cc/paper/2017/hash/5d44ee6f2c3f71b73125876103c8f6c4-Abstract.html)
, you should use `nonlinearity='linear'` instead of `nonlinearity='selu'`. This gives the initial weights a variance of `1 / N`, which is necessary to induce a stable fixed point in the forward pass. In contrast, the default gain for `SELU` sacrifices the normalization effect for more stable gradient flow in rectangular layers.

Parameters:

*   **nonlinearity** ([_Literal_](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.15)")
    _\[__'linear'__,_ _'conv1d'__,_ _'conv2d'__,_ _'conv3d'__,_ _'conv\_transpose1d'__,_ _'conv\_transpose2d'__,_ _'conv\_transpose3d'__,_ _'sigmoid'__,_ _'tanh'__,_ _'relu'__,_ _'leaky\_relu'__,_ _'selu'__\]_) – the non-linear function (nn.functional name)
    
*   **param** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ [_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
     _|_ _None_) – optional parameter for the non-linear function
    

Return type:

[float](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")

Examples

\>>> gain \= nn.init.calculate\_gain(
...     "leaky\_relu", 0.2
... )  \# leaky\_relu with negative\_slope=0.2

Copy to clipboard

torch.nn.init.uniform\_(_tensor_, _a\=0.0_, _b\=1.0_, _generator\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/init.py#L247)
[#](https://docs.pytorch.org/docs/2.15/nn.init.html#torch.nn.init.uniform_ "Link to this definition")

Fill the input Tensor with values drawn from the uniform distribution.

U(a,b)\\mathcal{U}(a, b)U(a,b).

Parameters:

*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – an n-dimensional torch.Tensor
    
*   **a** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – the lower bound of the uniform distribution
    
*   **b** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – the upper bound of the uniform distribution
    
*   **generator** ([_Generator_](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch._C.Generator")
     _|_ _None_) – the torch Generator to sample from (default: None)
    

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Examples

\>>> w \= torch.empty(3, 5)
\>>> nn.init.uniform\_(w)

Copy to clipboard

torch.nn.init.normal\_(_tensor_, _mean\=0.0_, _std\=1.0_, _generator\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/init.py#L274)
[#](https://docs.pytorch.org/docs/2.15/nn.init.html#torch.nn.init.normal_ "Link to this definition")

Fill the input Tensor with values drawn from the normal distribution.

N(mean,std2)\\mathcal{N}(\\text{mean}, \\text{std}^2)N(mean,std2).

Parameters:

*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – an n-dimensional torch.Tensor
    
*   **mean** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – the mean of the normal distribution
    
*   **std** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – the standard deviation of the normal distribution
    
*   **generator** ([_Generator_](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch._C.Generator")
     _|_ _None_) – the torch Generator to sample from (default: None)
    

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Examples

\>>> w \= torch.empty(3, 5)
\>>> nn.init.normal\_(w)

Copy to clipboard

torch.nn.init.constant\_(_tensor_, _val_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/init.py#L337)
[#](https://docs.pytorch.org/docs/2.15/nn.init.html#torch.nn.init.constant_ "Link to this definition")

Fill the input Tensor with the value val\\text{val}val.

Parameters:

*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – an n-dimensional torch.Tensor
    
*   **val** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – the value to fill the tensor with
    

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Examples

\>>> w \= torch.empty(3, 5)
\>>> nn.init.constant\_(w, 0.3)

Copy to clipboard

torch.nn.init.ones\_(_tensor_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/init.py#L355)
[#](https://docs.pytorch.org/docs/2.15/nn.init.html#torch.nn.init.ones_ "Link to this definition")

Fill the input Tensor with the scalar value 1.

Parameters:

**tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – an n-dimensional torch.Tensor

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Examples

\>>> w \= torch.empty(3, 5)
\>>> nn.init.ones\_(w)

Copy to clipboard

torch.nn.init.zeros\_(_tensor_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/init.py#L368)
[#](https://docs.pytorch.org/docs/2.15/nn.init.html#torch.nn.init.zeros_ "Link to this definition")

Fill the input Tensor with the scalar value 0.

Parameters:

**tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – an n-dimensional torch.Tensor

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Examples

\>>> w \= torch.empty(3, 5)
\>>> nn.init.zeros\_(w)

Copy to clipboard

torch.nn.init.eye\_(_tensor_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/init.py#L381)
[#](https://docs.pytorch.org/docs/2.15/nn.init.html#torch.nn.init.eye_ "Link to this definition")

Fill the 2-dimensional input Tensor with the identity matrix.

Preserves the identity of the inputs in Linear layers, where as many inputs are preserved as possible.

Parameters:

**tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – a 2-dimensional torch.Tensor

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Examples

\>>> w \= torch.empty(3, 5)
\>>> nn.init.eye\_(w)

Copy to clipboard

torch.nn.init.dirac\_(_tensor_, _groups\=1_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/init.py#L402)
[#](https://docs.pytorch.org/docs/2.15/nn.init.html#torch.nn.init.dirac_ "Link to this definition")

Fill the {3, 4, 5}-dimensional input Tensor with the Dirac delta function.

Preserves the identity of the inputs in Convolutional layers, where as many input channels are preserved as possible. In case of groups>1, each group of channels preserves identity

Parameters:

*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – a {3, 4, 5}-dimensional torch.Tensor
    
*   **groups** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – number of groups in the conv layer (default: 1)
    

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Examples

\>>> w \= torch.empty(3, 16, 5, 5)
\>>> nn.init.dirac\_(w)
\>>> w \= torch.empty(3, 24, 5, 5)
\>>> nn.init.dirac\_(w, 3)

Copy to clipboard

torch.nn.init.xavier\_uniform\_(_tensor_, _gain\=1.0_, _generator\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/init.py#L479)
[#](https://docs.pytorch.org/docs/2.15/nn.init.html#torch.nn.init.xavier_uniform_ "Link to this definition")

Fill the input Tensor with values using a Xavier uniform distribution.

The method is described in Understanding the difficulty of training deep feedforward neural networks - Glorot, X. & Bengio, Y. (2010). The resulting tensor will have values sampled from U(−a,a)\\mathcal{U}(-a, a)U(−a,a) where

a\=gain×6fan\_in+fan\_outa = \\text{gain} \\times \\sqrt{\\frac{6}{\\text{fan\\\_in} + \\text{fan\\\_out}}} a\=gain×fan\_in+fan\_out6​​

Also known as Glorot initialization.

Parameters:

*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – an n-dimensional torch.Tensor
    
*   **gain** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – an optional scaling factor
    
*   **generator** ([_Generator_](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch._C.Generator")
     _|_ _None_) – the torch Generator to sample from (default: None)
    

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Examples

\>>> w \= torch.empty(3, 5)
\>>> nn.init.xavier\_uniform\_(w, gain\=nn.init.calculate\_gain("relu"))

Copy to clipboard

torch.nn.init.xavier\_normal\_(_tensor_, _gain\=1.0_, _generator\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/init.py#L512)
[#](https://docs.pytorch.org/docs/2.15/nn.init.html#torch.nn.init.xavier_normal_ "Link to this definition")

Fill the input Tensor with values using a Xavier normal distribution.

The method is described in Understanding the difficulty of training deep feedforward neural networks - Glorot, X. & Bengio, Y. (2010). The resulting tensor will have values sampled from N(0,std2)\\mathcal{N}(0, \\text{std}^2)N(0,std2) where

std\=gain×2fan\_in+fan\_out\\text{std} = \\text{gain} \\times \\sqrt{\\frac{2}{\\text{fan\\\_in} + \\text{fan\\\_out}}} std\=gain×fan\_in+fan\_out2​​

Also known as Glorot initialization.

Parameters:

*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – an n-dimensional torch.Tensor
    
*   **gain** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – an optional scaling factor
    
*   **generator** ([_Generator_](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch._C.Generator")
     _|_ _None_) – the torch Generator to sample from (default: None)
    

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Examples

\>>> w \= torch.empty(3, 5)
\>>> nn.init.xavier\_normal\_(w)

Copy to clipboard

torch.nn.init.kaiming\_uniform\_(_tensor_, _a\=0_, _mode\='fan\_in'_, _nonlinearity\='leaky\_relu'_, _generator\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/init.py#L554)
[#](https://docs.pytorch.org/docs/2.15/nn.init.html#torch.nn.init.kaiming_uniform_ "Link to this definition")

Fill the input Tensor with values using a Kaiming uniform distribution.

The method is described in Delving deep into rectifiers: Surpassing human-level performance on ImageNet classification - He, K. et al. (2015). The resulting tensor will have values sampled from U(−bound,bound)\\mathcal{U}(-\\text{bound}, \\text{bound})U(−bound,bound) where

bound\=gain×3fan\_mode\\text{bound} = \\text{gain} \\times \\sqrt{\\frac{3}{\\text{fan\\\_mode}}} bound\=gain×fan\_mode3​​

Also known as He initialization.

Parameters:

*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – an n-dimensional torch.Tensor
    
*   **a** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – the negative slope of the rectifier used after this layer (only used with `'leaky_relu'`)
    
*   **mode** ([_Literal_](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.15)")
    _\[__'fan\_in'__,_ _'fan\_out'__\]_) – either `'fan_in'` (default) or `'fan_out'`. Choosing `'fan_in'` preserves the magnitude of the variance of the weights in the forward pass. Choosing `'fan_out'` preserves the magnitudes in the backwards pass.
    
*   **nonlinearity** ([_Literal_](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.15)")
    _\[__'linear'__,_ _'conv1d'__,_ _'conv2d'__,_ _'conv3d'__,_ _'conv\_transpose1d'__,_ _'conv\_transpose2d'__,_ _'conv\_transpose3d'__,_ _'sigmoid'__,_ _'tanh'__,_ _'relu'__,_ _'leaky\_relu'__,_ _'selu'__\]_) – the non-linear function (nn.functional name), recommended to use only with `'relu'` or `'leaky_relu'` (default).
    
*   **generator** ([_Generator_](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch._C.Generator")
     _|_ _None_) – the torch Generator to sample from (default: None)
    

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Examples

\>>> w \= torch.empty(3, 5)
\>>> nn.init.kaiming\_uniform\_(w, mode\="fan\_in", nonlinearity\="relu")

Copy to clipboard

Note

Be aware that `fan_in` and `fan_out` are calculated assuming that the weight matrix is used in a transposed manner, (i.e., `x @ w.T` in `Linear` layers, where `w.shape = [fan_out, fan_in]`). This is important for correct initialization. If you plan to use `x @ w`, where `w.shape = [fan_in, fan_out]`, pass in a transposed weight matrix, i.e. `nn.init.kaiming_uniform_(w.T, ...)`.

torch.nn.init.kaiming\_normal\_(_tensor_, _a\=0_, _mode\='fan\_in'_, _nonlinearity\='leaky\_relu'_, _generator\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/init.py#L619)
[#](https://docs.pytorch.org/docs/2.15/nn.init.html#torch.nn.init.kaiming_normal_ "Link to this definition")

Fill the input Tensor with values using a Kaiming normal distribution.

The method is described in Delving deep into rectifiers: Surpassing human-level performance on ImageNet classification - He, K. et al. (2015). The resulting tensor will have values sampled from N(0,std2)\\mathcal{N}(0, \\text{std}^2)N(0,std2) where

std\=gainfan\_mode\\text{std} = \\frac{\\text{gain}}{\\sqrt{\\text{fan\\\_mode}}} std\=fan\_mode​gain​

Also known as He initialization.

Parameters:

*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – an n-dimensional torch.Tensor
    
*   **a** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – the negative slope of the rectifier used after this layer (only used with `'leaky_relu'`)
    
*   **mode** ([_Literal_](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.15)")
    _\[__'fan\_in'__,_ _'fan\_out'__\]_) – either `'fan_in'` (default) or `'fan_out'`. Choosing `'fan_in'` preserves the magnitude of the variance of the weights in the forward pass. Choosing `'fan_out'` preserves the magnitudes in the backwards pass.
    
*   **nonlinearity** ([_Literal_](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.15)")
    _\[__'linear'__,_ _'conv1d'__,_ _'conv2d'__,_ _'conv3d'__,_ _'conv\_transpose1d'__,_ _'conv\_transpose2d'__,_ _'conv\_transpose3d'__,_ _'sigmoid'__,_ _'tanh'__,_ _'relu'__,_ _'leaky\_relu'__,_ _'selu'__\]_) – the non-linear function (nn.functional name), recommended to use only with `'relu'` or `'leaky_relu'` (default).
    
*   **generator** ([_Generator_](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch._C.Generator")
     _|_ _None_) – the torch Generator to sample from (default: None)
    

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Examples

\>>> w \= torch.empty(3, 5)
\>>> nn.init.kaiming\_normal\_(w, mode\="fan\_out", nonlinearity\="relu")

Copy to clipboard

Note

Be aware that `fan_in` and `fan_out` are calculated assuming that the weight matrix is used in a transposed manner, (i.e., `x @ w.T` in `Linear` layers, where `w.shape = [fan_out, fan_in]`). This is important for correct initialization. If you plan to use `x @ w`, where `w.shape = [fan_in, fan_out]`, pass in a transposed weight matrix, i.e. `nn.init.kaiming_normal_(w.T, ...)`.

torch.nn.init.trunc\_normal\_(_tensor_, _mean\=0.0_, _std\=1.0_, _a\=\-2.0_, _b\=2.0_, _generator\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/init.py#L301)
[#](https://docs.pytorch.org/docs/2.15/nn.init.html#torch.nn.init.trunc_normal_ "Link to this definition")

Fill the input Tensor with values drawn from a truncated normal distribution.

The values are effectively drawn from the normal distribution N(mean,std2)\\mathcal{N}(\\text{mean}, \\text{std}^2)N(mean,std2) with values outside \[a,b\]\[a, b\]\[a,b\] redrawn until they are within the bounds. The method used for generating the random values works best when a≤mean≤ba \\leq \\text{mean} \\leq ba≤mean≤b.

For reduced-precision types (`torch.float16` and `torch.bfloat16`), sampling quality depends on the underlying `normal_()` and `uniform_()` implementations which operate at higher internal precision to avoid quantization artifacts.

Parameters:

*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – an n-dimensional torch.Tensor
    
*   **mean** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – the mean of the normal distribution
    
*   **std** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – the standard deviation of the normal distribution
    
*   **a** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – the minimum cutoff value
    
*   **b** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – the maximum cutoff value
    
*   **generator** ([_Generator_](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch._C.Generator")
     _|_ _None_) – the torch Generator to sample from (default: None)
    

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Examples

\>>> w \= torch.empty(3, 5)
\>>> nn.init.trunc\_normal\_(w)

Copy to clipboard

torch.nn.init.orthogonal\_(_tensor_, _gain\=1_, _generator\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/init.py#L672)
[#](https://docs.pytorch.org/docs/2.15/nn.init.html#torch.nn.init.orthogonal_ "Link to this definition")

Fill the input Tensor with a (semi) orthogonal matrix.

Described in Exact solutions to the nonlinear dynamics of learning in deep linear neural networks - Saxe, A. et al. (2013). The input tensor must have at least 2 dimensions, and for tensors with more than 2 dimensions the trailing dimensions are flattened.

Parameters:

*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – an n-dimensional torch.Tensor, where n≥2n \\geq 2n≥2
    
*   **gain** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – optional scaling factor
    
*   **generator** ([_Generator_](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch._C.Generator")
     _|_ _None_) – the torch Generator to sample from (default: None)
    

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Examples

\>>> w \= torch.empty(3, 5)
\>>> nn.init.orthogonal\_(w)

Copy to clipboard

torch.nn.init.sparse\_(_tensor_, _sparsity_, _std\=0.01_, _generator\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/init.py#L723)
[#](https://docs.pytorch.org/docs/2.15/nn.init.html#torch.nn.init.sparse_ "Link to this definition")

Fill the 2D input Tensor as a sparse matrix.

The non-zero elements will be drawn from the normal distribution N(0,0.01)\\mathcal{N}(0, 0.01)N(0,0.01), as described in Deep learning via Hessian-free optimization - Martens, J. (2010).

Parameters:

*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – an n-dimensional torch.Tensor
    
*   **sparsity** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – The fraction of elements in each column to be set to zero
    
*   **std** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – the standard deviation of the normal distribution used to generate the non-zero values
    
*   **generator** ([_Generator_](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch._C.Generator")
     _|_ _None_) – the torch Generator to sample from (default: None)
    

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Examples

\>>> w \= torch.empty(3, 5)
\>>> nn.init.sparse\_(w, sparsity\=0.1)

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/nn.init.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/nn.init.md.txt)

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