Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.functional.jacobian.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.autograd.functional.jacobian.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.functional.jacobian.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.autograd.functional.jacobian.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.autograd.functional.jacobian.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.autograd.functional.jacobian.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.autograd.functional.jacobian.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.autograd.functional.jacobian.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.autograd.functional.jacobian.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.autograd.functional.jacobian.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.autograd.functional.jacobian.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.autograd.functional.jacobian.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.autograd.functional.jacobian.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.autograd.functional.jacobian.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.autograd.functional.jacobian.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.autograd.functional.jacobian.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.autograd.functional.jacobian.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.autograd.functional.jacobian.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.autograd.functional.jacobian.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.autograd.functional.jacobian.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.autograd.functional.jacobian.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.autograd.functional.jacobian.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.autograd.functional.jacobian.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.autograd.functional.jacobian.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.autograd.functional.jacobian.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.autograd.functional.jacobian.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.autograd.functional.jacobian.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.autograd.functional.jacobian.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.autograd.functional.jacobian.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.autograd.functional.jacobian.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.autograd.functional.jacobian.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.autograd.functional.jacobian.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.autograd.functional.jacobian.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.autograd.functional.jacobian.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.autograd.functional.jacobian.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.autograd.functional.jacobian.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.autograd.functional.jacobian.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.autograd.functional.jacobian.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.autograd.functional.jacobian.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.autograd.functional.jacobian.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.autograd.functional.jacobian.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.autograd.functional.jacobian.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.autograd.functional.jacobian.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.autograd.functional.jacobian.html)

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

torch.autograd.functional.jacobian[#](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.functional.jacobian.html#torch-autograd-functional-jacobian "Link to this heading")

======================================================================================================================================================================================

torch.autograd.functional.jacobian(_func_, _inputs_, _create\_graph\=False_, _strict\=False_, _vectorize\=False_, _strategy\='reverse-mode'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/functional.py#L587)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.functional.jacobian.html#torch.autograd.functional.jacobian "Link to this definition")

Compute the Jacobian of a given function.

Parameters:

*   **func** (_function_) – a Python function that takes Tensor inputs and returns a tuple of Tensors or a Tensor.
    
*   **inputs** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
     _of_ _Tensors_ _or_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – inputs to the function `func`.
    
*   **create\_graph** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True`, the Jacobian will be computed in a differentiable manner. Note that when `strict` is `False`, the result can not require gradients or be disconnected from the inputs. Defaults to `False`.
    
*   **strict** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True`, an error will be raised when we detect that there exists an input such that all the outputs are independent of it. If `False`, we return a Tensor of zeros as the jacobian for said inputs, which is the expected mathematical value. Defaults to `False`.
    
*   **vectorize** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – This feature is experimental. Please consider using [`torch.func.jacrev()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacrev.html#torch.func.jacrev "torch.func.jacrev")
     or [`torch.func.jacfwd()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacfwd.html#torch.func.jacfwd "torch.func.jacfwd")
     instead if you are looking for something less experimental and more performant. When computing the jacobian, usually we invoke `autograd.grad` once per row of the jacobian. If this flag is `True`, we perform only a single `autograd.grad` call with `batched_grad=True` which uses the vmap prototype feature. Though this should lead to performance improvements in many cases, because this feature is still experimental, there may be performance cliffs. See [`torch.autograd.grad()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.grad.html#torch.autograd.grad "torch.autograd.grad")
    ’s `batched_grad` parameter for more information.
    
*   **strategy** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – Set to `"forward-mode"` or `"reverse-mode"` to determine whether the Jacobian will be computed with forward or reverse mode AD. Currently, `"forward-mode"` requires `vectorized=True`. Defaults to `"reverse-mode"`. If `func` has more outputs than inputs, `"forward-mode"` tends to be more performant. Otherwise, prefer to use `"reverse-mode"`.
    

Returns:

if there is a single input and output, this will be a single Tensor containing the Jacobian for the linearized inputs and output. If one of the two is a tuple, then the Jacobian will be a tuple of Tensors. If both of them are tuples, then the Jacobian will be a tuple of tuple of Tensors where `Jacobian[i][j]` will contain the Jacobian of the `i`th output and `j`th input and will have as size the concatenation of the sizes of the corresponding output and the corresponding input and will have same dtype and device as the corresponding input. If strategy is `forward-mode`, the dtype will be that of the output; otherwise, the input.

Return type:

Jacobian ([Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 or nested tuple of Tensors)

Example

\>>> def exp\_reducer(x):
...     return x.exp().sum(dim\=1)
\>>> inputs \= torch.rand(2, 2)
\>>> jacobian(exp\_reducer, inputs)
tensor(\[\[\[1.4917, 2.4352\],\
         \[0.0000, 0.0000\]\],\
        \[\[0.0000, 0.0000\],\
         \[2.4369, 2.3799\]\]\])

Copy to clipboard

\>>> jacobian(exp\_reducer, inputs, create\_graph\=True)
tensor(\[\[\[1.4917, 2.4352\],\
         \[0.0000, 0.0000\]\],\
        \[\[0.0000, 0.0000\],\
         \[2.4369, 2.3799\]\]\], grad\_fn=<ViewBackward>)

Copy to clipboard

\>>> def exp\_adder(x, y):
...     return 2 \* x.exp() + 3 \* y
\>>> inputs \= (torch.rand(2), torch.rand(2))
\>>> jacobian(exp\_adder, inputs)
(tensor(\[\[2.8052, 0.0000\],\
        \[0.0000, 3.3963\]\]),
 tensor(\[\[3., 0.\],\
         \[0., 3.\]\]))

Copy to clipboard

\>>> def linear\_model(x):
...     W \= torch.tensor(\[\[2.0, \-1.0\], \[0.0, 1.0\]\])
...     b \= torch.tensor(\[1.0, 0.5\])
...     return x @ W.T + b

Copy to clipboard

\>>> x \= torch.randn(4, 2, requires\_grad\=True)
\>>> jac \= jacobian(linear\_model, x, vectorize\=True)
\>>> jac.shape
torch.Size(\[4, 2, 4, 2\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.autograd.functional.jacobian.rst.txt)

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