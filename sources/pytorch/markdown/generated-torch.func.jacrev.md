Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacrev.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.func.jacrev.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacrev.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.func.jacrev.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.func.jacrev.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.func.jacrev.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.func.jacrev.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.func.jacrev.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.func.jacrev.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.func.jacrev.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.func.jacrev.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.func.jacrev.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.func.jacrev.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.func.jacrev.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.func.jacrev.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.func.jacrev.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.func.jacrev.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.func.jacrev.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.func.jacrev.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.func.jacrev.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.func.jacrev.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.func.jacrev.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.func.jacrev.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.func.jacrev.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.func.jacrev.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.func.jacrev.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.func.jacrev.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.func.jacrev.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.func.jacrev.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.func.jacrev.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.func.jacrev.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.func.jacrev.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.func.jacrev.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.func.jacrev.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.func.jacrev.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.func.jacrev.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.func.jacrev.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.func.jacrev.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.func.jacrev.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.func.jacrev.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.func.jacrev.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.func.jacrev.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.func.jacrev.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.func.jacrev.html)

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

torch.func.jacrev[#](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacrev.html#torch-func-jacrev "Link to this heading")

===================================================================================================================================

torch.func.jacrev(_func_, _argnums\=0_, _\*_, _has\_aux\=False_, _chunk\_size\=None_, _\_preallocate\_and\_copy\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_functorch/eager_transforms.py#L505)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacrev.html#torch.func.jacrev "Link to this definition")

Computes the Jacobian of `func` with respect to the arg(s) at index `argnum` using reverse mode autodiff

Note

Using `chunk_size=1` is equivalent to computing the jacobian row-by-row with a for-loop i.e. the constraints of [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vmap.html#torch.func.vmap "torch.func.vmap")
 are not applicable.

Parameters:

*   **func** (_function_) – A Python function that takes one or more arguments, one of which must be a Tensor, and returns one or more Tensors
    
*   **argnums** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ _...__\]_) – Optional, integer or tuple of integers, saying which arguments to get the Jacobian with respect to. Default: 0.
    
*   **has\_aux** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Flag indicating that `func` returns a `(output, aux)` tuple where the first element is the output of the function to be differentiated and the second element is auxiliary objects that will not be differentiated. Default: False.
    
*   **chunk\_size** (_None_ _or_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – If None (default), use the maximum chunk size (equivalent to doing a single vmap over vjp to compute the jacobian). If 1, then compute the jacobian row-by-row with a for-loop. If not None, then compute the jacobian `chunk_size` rows at a time (equivalent to doing multiple vmap over vjp). If you run into memory issues computing the jacobian, please try to specify a non-None chunk\_size.
    

Returns:

Returns a function that takes in the same inputs as `func` and returns the Jacobian of `func` with respect to the arg(s) at `argnums`. If `has_aux is True`, then the returned function instead returns a `(jacobian, aux)` tuple where `jacobian` is the Jacobian and `aux` is auxiliary objects returned by `func`.

Return type:

Callable\[…, Any\]

A basic usage with a pointwise, unary operation will give a diagonal array as the Jacobian

\>>> from torch.func import jacrev
\>>> x \= torch.randn(5)
\>>> jacobian \= jacrev(torch.sin)(x)
\>>> expected \= torch.diag(torch.cos(x))
\>>> assert torch.allclose(jacobian, expected)

Copy to clipboard

If you would like to compute the output of the function as well as the jacobian of the function, use the `has_aux` flag to return the output as an auxiliary object:

\>>> from torch.func import jacrev
\>>> x \= torch.randn(5)
\>>>
\>>> def f(x):
\>>>   return x.sin()
\>>>
\>>> def g(x):
\>>>   result \= f(x)
\>>>   return result, result
\>>>
\>>> jacobian\_f, f\_x \= jacrev(g, has\_aux\=True)(x)
\>>> assert torch.allclose(f\_x, f(x))

Copy to clipboard

[`jacrev()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacrev.html#torch.func.jacrev "torch.func.jacrev")
 can be composed with vmap to produce batched Jacobians:

\>>> from torch.func import jacrev, vmap
\>>> x \= torch.randn(64, 5)
\>>> jacobian \= vmap(jacrev(torch.sin))(x)
\>>> assert jacobian.shape \== (64, 5, 5)

Copy to clipboard

Additionally, [`jacrev()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacrev.html#torch.func.jacrev "torch.func.jacrev")
 can be composed with itself to produce Hessians

\>>> from torch.func import jacrev
\>>> def f(x):
\>>>   return x.sin().sum()
\>>>
\>>> x \= torch.randn(5)
\>>> hessian \= jacrev(jacrev(f))(x)
\>>> assert torch.allclose(hessian, torch.diag(\-x.sin()))

Copy to clipboard

By default, [`jacrev()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacrev.html#torch.func.jacrev "torch.func.jacrev")
 computes the Jacobian with respect to the first input. However, it can compute the Jacobian with respect to a different argument by using `argnums`:

\>>> from torch.func import jacrev
\>>> def f(x, y):
\>>>   return x + y \*\* 2
\>>>
\>>> x, y \= torch.randn(5), torch.randn(5)
\>>> jacobian \= jacrev(f, argnums\=1)(x, y)
\>>> expected \= torch.diag(2 \* y)
\>>> assert torch.allclose(jacobian, expected)

Copy to clipboard

Additionally, passing a tuple to `argnums` will compute the Jacobian with respect to multiple arguments

\>>> from torch.func import jacrev
\>>> def f(x, y):
\>>>   return x + y \*\* 2
\>>>
\>>> x, y \= torch.randn(5), torch.randn(5)
\>>> jacobian \= jacrev(f, argnums\=(0, 1))(x, y)
\>>> expectedX \= torch.diag(torch.ones\_like(x))
\>>> expectedY \= torch.diag(2 \* y)
\>>> assert torch.allclose(jacobian\[0\], expectedX)
\>>> assert torch.allclose(jacobian\[1\], expectedY)

Copy to clipboard

Note

Using PyTorch `torch.no_grad` together with `jacrev`. Case 1: Using `torch.no_grad` inside a function:

\>>> def f(x):
\>>>     with torch.no\_grad():
\>>>         c \= x \*\* 2
\>>>     return x \- c

Copy to clipboard

In this case, `jacrev(f)(x)` will respect the inner `torch.no_grad`.

Case 2: Using `jacrev` inside `torch.no_grad` context manager:

\>>> with torch.no\_grad():
\>>>     jacrev(f)(x)

Copy to clipboard

In this case, `jacrev` will respect the inner `torch.no_grad`, but not the outer one. This is because `jacrev` is a “function transform”: its result should not depend on the result of a context manager outside of `f`.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.func.jacrev.rst.txt)

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