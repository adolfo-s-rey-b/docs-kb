Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.func.grad.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.func.grad.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.func.grad.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.func.grad.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.func.grad.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.func.grad.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.func.grad.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.func.grad.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.func.grad.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.func.grad.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.func.grad.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.func.grad.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.func.grad.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.func.grad.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.func.grad.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.func.grad.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.func.grad.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.func.grad.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.func.grad.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.func.grad.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.func.grad.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.func.grad.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.func.grad.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.func.grad.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.func.grad.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.func.grad.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.func.grad.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.func.grad.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.func.grad.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.func.grad.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.func.grad.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.func.grad.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.func.grad.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.func.grad.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.func.grad.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.func.grad.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.func.grad.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.func.grad.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.func.grad.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.func.grad.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.func.grad.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.func.grad.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.func.grad.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.func.grad.html)

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

torch.func.grad[#](https://docs.pytorch.org/docs/2.15/generated/torch.func.grad.html#torch-func-grad "Link to this heading")

=============================================================================================================================

torch.func.grad(_func_, _argnums\=0_, _has\_aux\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_functorch/apis.py#L355)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.func.grad.html#torch.func.grad "Link to this definition")

`grad` operator helps computing gradients of `func` with respect to the input(s) specified by `argnums`. This operator can be nested to compute higher-order gradients.

Parameters:

*   **func** (_Callable_) – A Python function that takes one or more arguments. Must return a single-element Tensor. If specified `has_aux` equals `True`, function can return a tuple of single-element Tensor and other auxiliary objects: `(output, aux)`.
    
*   **argnums** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ _Tuple__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – Specifies arguments to compute gradients with respect to. `argnums` can be single integer or tuple of integers. Default: 0.
    
*   **has\_aux** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Flag indicating that `func` returns a tensor and other auxiliary objects: `(output, aux)`. Default: False.
    

Returns:

Function to compute gradients with respect to its inputs. By default, the output of the function is the gradient tensor(s) with respect to the first argument. If specified `has_aux` equals `True`, tuple of gradients and output auxiliary objects is returned. If `argnums` is a tuple of integers, a tuple of output gradients with respect to each `argnums` value is returned.

Return type:

[_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[~\_P\], [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\]

Example of using `grad`:

\>>> from torch.func import grad
\>>> x \= torch.randn(\[\])
\>>> cos\_x \= grad(lambda x: torch.sin(x))(x)
\>>> assert torch.allclose(cos\_x, x.cos())
\>>>
\>>> \# Second-order gradients
\>>> neg\_sin\_x \= grad(grad(lambda x: torch.sin(x)))(x)
\>>> assert torch.allclose(neg\_sin\_x, \-x.sin())

Copy to clipboard

When composed with `vmap`, `grad` can be used to compute per-sample-gradients:

\>>> from torch.func import grad, vmap
\>>> batch\_size, feature\_size \= 3, 5
\>>>
\>>> def model(weights, feature\_vec):
\>>> \# Very simple linear model with activation
\>>>     assert feature\_vec.dim() \== 1
\>>>     return feature\_vec.dot(weights).relu()
\>>>
\>>> def compute\_loss(weights, example, target):
\>>>     y \= model(weights, example)
\>>>     return ((y \- target) \*\* 2).mean()  \# MSELoss
\>>>
\>>> weights \= torch.randn(feature\_size, requires\_grad\=True)
\>>> examples \= torch.randn(batch\_size, feature\_size)
\>>> targets \= torch.randn(batch\_size)
\>>> inputs \= (weights, examples, targets)
\>>> grad\_weight\_per\_example \= vmap(grad(compute\_loss), in\_dims\=(None, 0, 0))(
...     \*inputs
... )

Copy to clipboard

Example of using `grad` with `has_aux` and `argnums`:

\>>> from torch.func import grad
\>>> def my\_loss\_func(y, y\_pred):
\>>>    loss\_per\_sample \= (0.5 \* y\_pred \- y) \*\* 2
\>>>    loss \= loss\_per\_sample.mean()
\>>>    return loss, (y\_pred, loss\_per\_sample)
\>>>
\>>> fn \= grad(my\_loss\_func, argnums\=(0, 1), has\_aux\=True)
\>>> y\_true \= torch.rand(4)
\>>> y\_preds \= torch.rand(4, requires\_grad\=True)
\>>> out \= fn(y\_true, y\_preds)
\>>> \# > output is ((grads w.r.t y\_true, grads w.r.t y\_preds), (y\_pred, loss\_per\_sample))

Copy to clipboard

Note

Using PyTorch `torch.no_grad` together with `grad`.

Case 1: Using `torch.no_grad` inside a function:

\>>> def f(x):
\>>>     with torch.no\_grad():
\>>>         c \= x \*\* 2
\>>>     return x \- c

Copy to clipboard

In this case, `grad(f)(x)` will respect the inner `torch.no_grad`.

Case 2: Using `grad` inside `torch.no_grad` context manager:

\>>> with torch.no\_grad():
\>>>     grad(f)(x)

Copy to clipboard

In this case, `grad` will respect the inner `torch.no_grad`, but not the outer one. This is because `grad` is a “function transform”: its result should not depend on the result of a context manager outside of `f`.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.func.grad.rst.txt)

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