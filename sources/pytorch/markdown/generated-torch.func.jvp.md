Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.func.jvp.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.func.jvp.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.func.jvp.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.func.jvp.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.func.jvp.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.func.jvp.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.func.jvp.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.func.jvp.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.func.jvp.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.func.jvp.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.func.jvp.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.func.jvp.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.func.jvp.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.func.jvp.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.func.jvp.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.func.jvp.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.func.jvp.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.func.jvp.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.func.jvp.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.func.jvp.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.func.jvp.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.func.jvp.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.func.jvp.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.func.jvp.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.func.jvp.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.func.jvp.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.func.jvp.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.func.jvp.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.func.jvp.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.func.jvp.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.func.jvp.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.func.jvp.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.func.jvp.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.func.jvp.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.func.jvp.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.func.jvp.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.func.jvp.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.func.jvp.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.func.jvp.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.func.jvp.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.func.jvp.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.func.jvp.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.func.jvp.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.func.jvp.html)

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

torch.func.jvp[#](https://docs.pytorch.org/docs/2.15/generated/torch.func.jvp.html#torch-func-jvp "Link to this heading")

==========================================================================================================================

torch.func.jvp(_func_, _primals_, _tangents_, _\*_, _strict\=False_, _has\_aux\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_functorch/eager_transforms.py#L1093)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.func.jvp.html#torch.func.jvp "Link to this definition")

Standing for the Jacobian-vector product, returns a tuple containing the output of func(\*primals) and the “Jacobian of `func` evaluated at `primals`” times `tangents`. This is also known as forward-mode autodiff.

Parameters:

*   **func** (_function_) – A Python function that takes one or more arguments, one of which must be a Tensor, and returns one or more Tensors
    
*   **primals** (_Tensors_) – Positional arguments to `func` that must all be Tensors. The returned function will also be computing the derivative with respect to these arguments
    
*   **tangents** (_Tensors_) – The “vector” for which Jacobian-vector-product is computed. Must be the same structure and sizes as the inputs to `func`.
    
*   **has\_aux** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Flag indicating that `func` returns a `(output, aux)` tuple where the first element is the output of the function to be differentiated and the second element is other auxiliary objects that will not be differentiated. Default: False.
    

Returns:

Returns a `(output, jvp_out)` tuple containing the output of `func` evaluated at `primals` and the Jacobian-vector product. If `has_aux is True`, then instead returns a `(output, jvp_out, aux)` tuple.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[Any, Any\] | [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[Any, Any, Any\]

Note

You may see this API error out with “forward-mode AD not implemented for operator X”. If so, please file a bug report and we will prioritize it.

jvp is useful when you wish to compute gradients of a function R^1 -> R^N

\>>> from torch.func import jvp
\>>> x \= torch.randn(\[\])
\>>> f \= lambda x: x \* torch.tensor(\[1.0, 2.0, 3\])
\>>> warnings.filterwarnings(
...     "ignore", message\=".\*torch.jit.script"
... )  \# docs: hide
\>>> value, grad \= jvp(f, (x,), (torch.tensor(1.0),))
\>>> assert torch.allclose(value, f(x))
\>>> assert torch.allclose(grad, torch.tensor(\[1.0, 2, 3\]))

Copy to clipboard

[`jvp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jvp.html#torch.func.jvp "torch.func.jvp")
 can support functions with multiple inputs by passing in the tangents for each of the inputs

\>>> from torch.func import jvp
\>>> x \= torch.randn(5)
\>>> y \= torch.randn(5)
\>>> f \= lambda x, y: (x \* y)
\>>> \_, output \= jvp(f, (x, y), (torch.ones(5), torch.ones(5)))
\>>> assert torch.allclose(output, x + y)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.func.jvp.rst.txt)

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