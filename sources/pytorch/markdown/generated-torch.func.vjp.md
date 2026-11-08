Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.func.vjp.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.func.vjp.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.func.vjp.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.func.vjp.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.func.vjp.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.func.vjp.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.func.vjp.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.func.vjp.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.func.vjp.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.func.vjp.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.func.vjp.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.func.vjp.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.func.vjp.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.func.vjp.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.func.vjp.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.func.vjp.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.func.vjp.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.func.vjp.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.func.vjp.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.func.vjp.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.func.vjp.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.func.vjp.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.func.vjp.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.func.vjp.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.func.vjp.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.func.vjp.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.func.vjp.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.func.vjp.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.func.vjp.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.func.vjp.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.func.vjp.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.func.vjp.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.func.vjp.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.func.vjp.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.func.vjp.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.func.vjp.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.func.vjp.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.func.vjp.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.func.vjp.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.func.vjp.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.func.vjp.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.func.vjp.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.func.vjp.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.func.vjp.html)

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

torch.func.vjp[#](https://docs.pytorch.org/docs/2.15/generated/torch.func.vjp.html#torch-func-vjp "Link to this heading")

==========================================================================================================================

torch.func.vjp(_func_, _\*primals_, _has\_aux\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_functorch/eager_transforms.py#L238)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.func.vjp.html#torch.func.vjp "Link to this definition")

Standing for the vector-Jacobian product, returns a tuple containing the results of `func` applied to `primals` and a function that, when given `cotangents`, computes the reverse-mode Jacobian of `func` with respect to `primals` times `cotangents`.

Parameters:

*   **func** (_Callable__\[__...__,_ _Any__\]_) – A Python function that takes one or more arguments. Must return one or more Tensors.
    
*   **primals** (_Tensors_) – Positional arguments to `func` that must all be Tensors. The returned function will also be computing the derivative with respect to these arguments
    
*   **has\_aux** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Flag indicating that `func` returns a `(output, aux)` tuple where the first element is the output of the function to be differentiated and the second element is other auxiliary objects that will not be differentiated. Default: False.
    

Returns:

Returns a `(output, vjp_fn)` tuple containing the output of `func` applied to `primals` and a function that computes the vjp of `func` with respect to all `primals` using the cotangents passed to the returned function. If `has_aux is True`, then instead returns a `(output, vjp_fn, aux)` tuple. The returned `vjp_fn` function will return a tuple of each VJP.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[Any, Callable\[…, Any\]\] | [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[Any, Callable\[…, Any\], Any\]

When used in simple cases, [`vjp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vjp.html#torch.func.vjp "torch.func.vjp")
 behaves the same as [`grad()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.grad.html#torch.func.grad "torch.func.grad")

\>>> x \= torch.randn(\[5\])
\>>> f \= lambda x: x.sin().sum()
\>>> (\_, vjpfunc) \= torch.func.vjp(f, x)
\>>> grad \= vjpfunc(torch.tensor(1.0))\[0\]
\>>> assert torch.allclose(grad, torch.func.grad(f)(x))

Copy to clipboard

However, [`vjp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vjp.html#torch.func.vjp "torch.func.vjp")
 can support functions with multiple outputs by passing in the cotangents for each of the outputs

\>>> x \= torch.randn(\[5\])
\>>> f \= lambda x: (x.sin(), x.cos())
\>>> (\_, vjpfunc) \= torch.func.vjp(f, x)
\>>> vjps \= vjpfunc((torch.ones(\[5\]), torch.ones(\[5\])))
\>>> assert torch.allclose(vjps\[0\], x.cos() + \-x.sin())

Copy to clipboard

[`vjp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vjp.html#torch.func.vjp "torch.func.vjp")
 can even support outputs being Python structs

\>>> x \= torch.randn(\[5\])
\>>> f \= lambda x: {"first": x.sin(), "second": x.cos()}
\>>> (\_, vjpfunc) \= torch.func.vjp(f, x)
\>>> cotangents \= {"first": torch.ones(\[5\]), "second": torch.ones(\[5\])}
\>>> vjps \= vjpfunc(cotangents)
\>>> assert torch.allclose(vjps\[0\], x.cos() + \-x.sin())

Copy to clipboard

The function returned by [`vjp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vjp.html#torch.func.vjp "torch.func.vjp")
 will compute the partials with respect to each of the `primals`

\>>> x, y \= torch.randn(\[5, 4\]), torch.randn(\[4, 5\])
\>>> (\_, vjpfunc) \= torch.func.vjp(torch.matmul, x, y)
\>>> cotangents \= torch.randn(\[5, 5\])
\>>> vjps \= vjpfunc(cotangents)
\>>> assert len(vjps) \== 2
\>>> assert torch.allclose(vjps\[0\], torch.matmul(cotangents, y.transpose(0, 1)))
\>>> assert torch.allclose(vjps\[1\], torch.matmul(x.transpose(0, 1), cotangents))

Copy to clipboard

`primals` are the positional arguments for `f`. All kwargs use their default value

\>>> x \= torch.randn(\[5\])
\>>> def f(x, scale\=4.):
\>>>   return x \* scale
\>>>
\>>> (\_, vjpfunc) \= torch.func.vjp(f, x)
\>>> vjps \= vjpfunc(torch.ones\_like(x))
\>>> assert torch.allclose(vjps\[0\], torch.full(x.shape, 4.0))

Copy to clipboard

Note

Using PyTorch `torch.no_grad` together with `vjp`. Case 1: Using `torch.no_grad` inside a function:

\>>> def f(x):
\>>>     with torch.no\_grad():
\>>>         c \= x \*\* 2
\>>>     return x \- c

Copy to clipboard

In this case, `vjp(f)(x)` will respect the inner `torch.no_grad`.

Case 2: Using `vjp` inside `torch.no_grad` context manager:

\>>> with torch.no\_grad():
\>>>     vjp(f)(x)

Copy to clipboard

In this case, `vjp` will respect the inner `torch.no_grad`, but not the outer one. This is because `vjp` is a “function transform”: its result should not depend on the result of a context manager outside of `f`.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.func.vjp.rst.txt)

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