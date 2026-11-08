Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.func.hessian.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.func.hessian.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.func.hessian.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.func.hessian.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.func.hessian.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.func.hessian.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.func.hessian.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.func.hessian.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.func.hessian.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.func.hessian.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.func.hessian.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.func.hessian.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.func.hessian.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.func.hessian.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.func.hessian.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.func.hessian.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.func.hessian.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.func.hessian.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.func.hessian.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.func.hessian.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.func.hessian.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.func.hessian.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.func.hessian.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.func.hessian.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.func.hessian.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.func.hessian.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.func.hessian.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.func.hessian.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.func.hessian.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.func.hessian.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.func.hessian.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.func.hessian.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.func.hessian.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.func.hessian.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.func.hessian.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.func.hessian.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.func.hessian.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.func.hessian.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.func.hessian.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.func.hessian.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.func.hessian.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.func.hessian.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.func.hessian.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.func.hessian.html)

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

torch.func.hessian[#](https://docs.pytorch.org/docs/2.15/generated/torch.func.hessian.html#torch-func-hessian "Link to this heading")

======================================================================================================================================

torch.func.hessian(_func_, _argnums\=0_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_functorch/eager_transforms.py#L1432)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.func.hessian.html#torch.func.hessian "Link to this definition")

Computes the Hessian of `func` with respect to the arg(s) at index `argnum` via a forward-over-reverse strategy.

The forward-over-reverse strategy (composing `jacfwd(jacrev(func))`) is a good default for good performance. It is possible to compute Hessians through other compositions of [`jacfwd()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacfwd.html#torch.func.jacfwd "torch.func.jacfwd")
 and [`jacrev()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacrev.html#torch.func.jacrev "torch.func.jacrev")
 like `jacfwd(jacfwd(func))` or `jacrev(jacrev(func))`.

Parameters:

*   **func** (_function_) – A Python function that takes one or more arguments, one of which must be a Tensor, and returns one or more Tensors
    
*   **argnums** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _...__\]_) – Optional, integer or tuple of integers, saying which arguments to get the Hessian with respect to. Default: 0.
    

Returns:

Returns a function that takes in the same inputs as `func` and returns the Hessian of `func` with respect to the arg(s) at `argnums`.

Return type:

Callable\[…, Any\]

Note

You may see this API error out with “forward-mode AD not implemented for operator X”. If so, please file a bug report and we will prioritize it. An alternative is to use `jacrev(jacrev(func))`, which has better operator coverage.

A basic usage with a R^N -> R^1 function gives a N x N Hessian:

\>>> from torch.func import hessian
\>>> def f(x):
\>>>   return x.sin().sum()
\>>>
\>>> x \= torch.randn(5)
\>>> hess \= hessian(f)(x)  \# equivalent to jacfwd(jacrev(f))(x)
\>>> assert torch.allclose(hess, torch.diag(\-x.sin()))

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.func.hessian.rst.txt)

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