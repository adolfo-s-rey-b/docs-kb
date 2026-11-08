Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/autograd.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/autograd.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/autograd.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/autograd.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/autograd.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/autograd.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/autograd.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/autograd.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/autograd.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/autograd.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/autograd.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/autograd.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/autograd.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/autograd.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/autograd.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/autograd.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/autograd.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/autograd.html)
[v1.13](https://docs.pytorch.org/docs/1.13/autograd.html)
[v1.12](https://docs.pytorch.org/docs/1.12/autograd.html)
[v1.11](https://docs.pytorch.org/docs/1.11/autograd.html)
[v1.10](https://docs.pytorch.org/docs/1.10/autograd.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/autograd.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/autograd.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/autograd.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/autograd.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/autograd.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/autograd.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/autograd.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/autograd.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/autograd.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/autograd.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/autograd.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/autograd.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/autograd.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/autograd.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/autograd.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/autograd.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/autograd.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/autograd.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/autograd.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/autograd.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/autograd.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/autograd.html)

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

Automatic differentiation package - torch.autograd[#](https://docs.pytorch.org/docs/2.15/autograd.html#module-torch.autograd "Link to this heading")

=====================================================================================================================================================

Created On: Dec 23, 2016 | Last Updated On: Sep 16, 2026

`torch.autograd` provides classes and functions implementing automatic differentiation of arbitrary scalar valued functions.

It requires minimal changes to the existing code - you only need to declare `Tensor` s for which gradients should be computed with the `requires_grad=True` keyword. As of now, we only support autograd for floating point `Tensor` types ( half, float, double and bfloat16) and complex `Tensor` types (cfloat, cdouble).

|     |     |
| --- | --- |
| [`backward`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.backward.html#torch.autograd.backward "torch.autograd.backward") | Compute the sum of gradients of given tensors with respect to graph leaves. |
| [`grad`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.grad.html#torch.autograd.grad "torch.autograd.grad") | Compute and return the sum of gradients of outputs with respect to the inputs. |

Forward-mode Automatic Differentiation[#](https://docs.pytorch.org/docs/2.15/autograd.html#forward-mode-automatic-differentiation "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

Warning

This API is in beta. Even though the function signatures are very unlikely to change, improved operator coverage is planned before we consider this stable.

Please see the [forward-mode AD tutorial](https://pytorch.org/tutorials/intermediate/forward_ad_usage.html)
 for detailed steps on how to use this API.

|     |     |
| --- | --- |
| [`forward_ad.dual_level`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.forward_ad.dual_level.html#torch.autograd.forward_ad.dual_level "torch.autograd.forward_ad.dual_level") | Context-manager for forward AD, where all forward AD computation must occur within the `dual_level` context. |
| [`forward_ad.make_dual`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.forward_ad.make_dual.html#torch.autograd.forward_ad.make_dual "torch.autograd.forward_ad.make_dual") | Associate a tensor value with its tangent to create a "dual tensor" for forward AD gradient computation. |
| [`forward_ad.unpack_dual`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.forward_ad.unpack_dual.html#torch.autograd.forward_ad.unpack_dual "torch.autograd.forward_ad.unpack_dual") | Unpack a "dual tensor" to get both its Tensor value and its forward AD gradient. |
| [`forward_ad.enter_dual_level`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.forward_ad.enter_dual_level.html#torch.autograd.forward_ad.enter_dual_level "torch.autograd.forward_ad.enter_dual_level") | Enter a new forward grad level. |
| [`forward_ad.exit_dual_level`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.forward_ad.exit_dual_level.html#torch.autograd.forward_ad.exit_dual_level "torch.autograd.forward_ad.exit_dual_level") | Exit a forward grad level. |
| [`forward_ad.UnpackedDualTensor`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.forward_ad.UnpackedDualTensor.html#torch.autograd.forward_ad.UnpackedDualTensor "torch.autograd.forward_ad.UnpackedDualTensor") | Namedtuple returned by `unpack_dual()` containing the primal and tangent components of the dual tensor. |

Functional higher level API[#](https://docs.pytorch.org/docs/2.15/autograd.html#functional-higher-level-api "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

Warning

This API is in beta. Even though the function signatures are very unlikely to change, major improvements to performances are planned before we consider this stable.

This section contains the higher level API for the autograd that builds on the basic API above and allows you to compute jacobians, hessians, etc.

This API works with user-provided functions that take only Tensors as input and return only Tensors. If your function takes other arguments that are not Tensors or Tensors that don’t have requires\_grad set, you can use a lambda to capture them. For example, for a function `f` that takes three inputs, a Tensor for which we want the jacobian, another tensor that should be considered constant and a boolean flag as `f(input, constant, flag=flag)` you can use it as `functional.jacobian(lambda x: f(x, constant, flag=flag), input)`.

|     |     |
| --- | --- |
| [`functional.jacobian`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.functional.jacobian.html#torch.autograd.functional.jacobian "torch.autograd.functional.jacobian") | Compute the Jacobian of a given function. |
| [`functional.hessian`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.functional.hessian.html#torch.autograd.functional.hessian "torch.autograd.functional.hessian") | Compute the Hessian of a given scalar function. |
| [`functional.vjp`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.functional.vjp.html#torch.autograd.functional.vjp "torch.autograd.functional.vjp") | Compute the dot product between a vector `v` and the Jacobian of the given function at the point given by the inputs. |
| [`functional.jvp`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.functional.jvp.html#torch.autograd.functional.jvp "torch.autograd.functional.jvp") | Compute the dot product between the Jacobian of the given function at the point given by the inputs and a vector `v`. |
| [`functional.vhp`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.functional.vhp.html#torch.autograd.functional.vhp "torch.autograd.functional.vhp") | Compute the dot product between vector `v` and Hessian of a given scalar function at a specified point. |
| [`functional.hvp`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.functional.hvp.html#torch.autograd.functional.hvp "torch.autograd.functional.hvp") | Compute the dot product between the scalar function's Hessian and a vector `v` at a specified point. |

Locally disabling gradient computation[#](https://docs.pytorch.org/docs/2.15/autograd.html#locally-disabling-gradient-computation "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

See [Locally disabling gradient computation](https://docs.pytorch.org/docs/2.15/notes/autograd.html#locally-disable-grad-doc)
 for more information on the differences between no-grad and inference mode as well as other related mechanisms that may be confused with the two. Also see [Locally disabling gradient computation](https://docs.pytorch.org/docs/2.15/torch.html#torch-rst-local-disable-grad)
 for a list of functions that can be used to locally disable gradients.

Default gradient layouts[#](https://docs.pytorch.org/docs/2.15/autograd.html#default-gradient-layouts "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

When a non-sparse `param` receives a non-sparse gradient during [`torch.autograd.backward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.backward.html#torch.autograd.backward "torch.autograd.backward")
 or [`torch.Tensor.backward()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.backward.html#torch.Tensor.backward "torch.Tensor.backward")
 `param.grad` is accumulated as follows.

If `param.grad` is initially `None`:

1.  If `param`’s memory is non-overlapping and dense, `.grad` is created with strides matching `param` (thus matching `param`’s layout).
    
2.  Otherwise, `.grad` is created with rowmajor-contiguous strides.
    

If `param` already has a non-sparse `.grad` attribute:

3.  If `create_graph=False`, `backward()` accumulates into `.grad` in-place, which preserves its strides.
    
4.  If `create_graph=True`, `backward()` replaces `.grad` with a new tensor `.grad + new grad`, which attempts (but does not guarantee) matching the preexisting `.grad`’s strides.
    

The default behavior (letting `.grad`s be `None` before the first `backward()`, such that their layout is created according to 1 or 2, and retained over time according to 3 or 4) is recommended for best performance. Calls to `model.zero_grad()` or `optimizer.zero_grad()` will not affect `.grad` layouts.

In fact, resetting all `.grad`s to `None` before each accumulation phase, e.g.:

for iterations...
    ...
    for param in model.parameters():
        param.grad \= None
    loss.backward()

Copy to clipboard

such that they’re recreated according to 1 or 2 every time, is a valid alternative to `model.zero_grad()` or `optimizer.zero_grad()` that may improve performance for some networks.

### Manual gradient layouts[#](https://docs.pytorch.org/docs/2.15/autograd.html#manual-gradient-layouts "Link to this heading")

If you need manual control over `.grad`’s strides, assign `param.grad =` a zeroed tensor with desired strides before the first `backward()`, and never reset it to `None`. 3 guarantees your layout is preserved as long as `create_graph=False`. 4 indicates your layout is _likely_ preserved even if `create_graph=True`.

In-place operations on Tensors[#](https://docs.pytorch.org/docs/2.15/autograd.html#in-place-operations-on-tensors "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

Supporting in-place operations in autograd is a hard matter, and we discourage their use in most cases. Autograd’s aggressive buffer freeing and reuse makes it very efficient and there are very few occasions when in-place operations actually lower memory usage by any significant amount. Unless you’re operating under heavy memory pressure, you might never need to use them.

### In-place correctness checks[#](https://docs.pytorch.org/docs/2.15/autograd.html#in-place-correctness-checks "Link to this heading")

All `Tensor` s keep track of in-place operations applied to them, and if the implementation detects that a tensor was saved for backward in one of the functions, but it was modified in-place afterwards, an error will be raised once backward pass is started. This ensures that if you’re using in-place functions and not seeing any errors, you can be sure that the computed gradients are correct.

Variable (deprecated)[#](https://docs.pytorch.org/docs/2.15/autograd.html#variable-deprecated "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

Warning

The Variable API has been deprecated: Variables are no longer necessary to use autograd with tensors. Autograd automatically supports Tensors with `requires_grad` set to `True`. Below please find a quick guide on what has changed:

*   `Variable(tensor)` and `Variable(tensor, requires_grad)` still work as expected, but they return Tensors instead of Variables.
    
*   `var.data` is the same thing as `tensor.data`.
    
*   Methods such as `var.backward(), var.detach(), var.register_hook()` now work on tensors with the same method names.
    

In addition, one can now create tensors with `requires_grad=True` using factory methods such as [`torch.randn()`](https://docs.pytorch.org/docs/2.15/generated/torch.randn.html#torch.randn "torch.randn")
, [`torch.zeros()`](https://docs.pytorch.org/docs/2.15/generated/torch.zeros.html#torch.zeros "torch.zeros")
, [`torch.ones()`](https://docs.pytorch.org/docs/2.15/generated/torch.ones.html#torch.ones "torch.ones")
, and others like the following:

`autograd_tensor = torch.randn((2, 3, 4), requires_grad=True)`

Tensor autograd functions[#](https://docs.pytorch.org/docs/2.15/autograd.html#tensor-autograd-functions "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| `torch.Tensor.grad` | This attribute is `None` by default and becomes a Tensor the first time a call to [`backward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.backward.html#torch.autograd.backward "torch.autograd.backward")<br> computes gradients for `self`. |
| `torch.Tensor.requires_grad` | Is `True` if gradients need to be computed for this Tensor, `False` otherwise. |
| `torch.Tensor.is_leaf` | All Tensors that have `requires_grad` which is `False` will be leaf Tensors by convention. |
| `torch.Tensor.backward`(\[gradient, ...\]) | Computes the gradient of current tensor wrt graph leaves. |
| `torch.Tensor.detach` | Returns a new Tensor, detached from the current graph. |
| `torch.Tensor.detach_` | Detaches the Tensor from the graph that created it, making it a leaf. |
| `torch.Tensor.register_hook`(hook) | Registers a backward hook. |
| `torch.Tensor.register_post_accumulate_grad_hook`(hook) | Registers a backward hook that runs after grad accumulation. |
| `torch.Tensor.retain_grad`() | Enables this Tensor to have their [`grad`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.grad.html#torch.autograd.grad "torch.autograd.grad")<br> populated during [`backward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.backward.html#torch.autograd.backward "torch.autograd.backward")<br>. |

Function[#](https://docs.pytorch.org/docs/2.15/autograd.html#function "Link to this heading")

----------------------------------------------------------------------------------------------

_class_ torch.autograd.Function(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/function.py#L646)
[#](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "Link to this definition")

Base class to create custom autograd.Function.

To create a custom autograd.Function, subclass this class and implement the [`forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.forward.html#torch.autograd.Function.forward "torch.autograd.Function.forward")
 and [`backward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.backward.html#torch.autograd.backward "torch.autograd.backward")
 static methods. Then, to use your custom op in the forward pass, call the class method `apply`. Do not call [`forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.forward.html#torch.autograd.Function.forward "torch.autograd.Function.forward")
 directly.

To ensure correctness and best performance, make sure you are calling the correct methods on `ctx` and validating your backward function using [`torch.autograd.gradcheck()`](https://docs.pytorch.org/docs/2.15/autograd.html#module-torch.autograd.gradcheck "torch.autograd.gradcheck")
.

See [Extending torch.autograd](https://docs.pytorch.org/docs/2.15/notes/extending.html#extending-autograd)
 for more details on how to use this class.

Examples:

\>>> class Exp(Function):
\>>>     @staticmethod
\>>>     def forward(ctx, i):
\>>>         result \= i.exp()
\>>>         ctx.save\_for\_backward(result)
\>>>         return result
\>>>
\>>>     @staticmethod
\>>>     def backward(ctx, grad\_output):
\>>>         result, \= ctx.saved\_tensors
\>>>         return grad\_output \* result
\>>>
\>>> \# Use it by calling the apply method:
\>>> output \= Exp.apply(input)

Copy to clipboard

|     |     |
| --- | --- |
| [`Function.forward`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.forward.html#torch.autograd.Function.forward "torch.autograd.Function.forward") | Define the forward of the custom autograd Function. |
| [`Function.backward`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.backward.html#torch.autograd.Function.backward "torch.autograd.Function.backward") | Define a formula for differentiating the operation with backward mode automatic differentiation. |
| [`Function.jvp`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.jvp.html#torch.autograd.Function.jvp "torch.autograd.Function.jvp") | Define a formula for differentiating the operation with forward mode automatic differentiation. |
| [`Function.vmap`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.vmap.html#torch.autograd.Function.vmap "torch.autograd.Function.vmap") | Define the behavior for this autograd.Function underneath [`torch.vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")<br>. |

Context method mixins[#](https://docs.pytorch.org/docs/2.15/autograd.html#context-method-mixins "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

When creating a new [`Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
, the following members are available to `ctx`.

_class_ torch.autograd.function.FunctionCtx[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/function.py#L38)
[#](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.function.FunctionCtx "Link to this definition")

_class_ torch.autograd.function.FunctionMeta(_name_, _bases_, _attrs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/function.py#L473)
[#](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.function.FunctionMeta "Link to this definition")

Function metaclass.

This metaclass sets up the following properties:

\_backward\_cls: The Function class corresponding to the differentiated

version of this function (which is generated on the fly by this metaclass).

|     |     |
| --- | --- |
| [`function.FunctionCtx.input_grad_buffers`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.function.FunctionCtx.input_grad_buffers.html#torch.autograd.function.FunctionCtx.input_grad_buffers "torch.autograd.function.FunctionCtx.input_grad_buffers") | Return existing buffers for accumulating gradients of this Function's inputs. |
| [`function.FunctionCtx.mark_dirty`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.function.FunctionCtx.mark_dirty.html#torch.autograd.function.FunctionCtx.mark_dirty "torch.autograd.function.FunctionCtx.mark_dirty") | Mark given tensors as modified in an in-place operation. |
| [`function.FunctionCtx.mark_non_differentiable`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.function.FunctionCtx.mark_non_differentiable.html#torch.autograd.function.FunctionCtx.mark_non_differentiable "torch.autograd.function.FunctionCtx.mark_non_differentiable") | Mark outputs as non-differentiable. |
| [`function.FunctionCtx.save_for_backward`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.function.FunctionCtx.save_for_backward.html#torch.autograd.function.FunctionCtx.save_for_backward "torch.autograd.function.FunctionCtx.save_for_backward") | Save given tensors for a future call to [`backward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.backward.html#torch.autograd.Function.backward "torch.autograd.Function.backward")<br>. |
| [`function.FunctionCtx.set_materialize_grads`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.function.FunctionCtx.set_materialize_grads.html#torch.autograd.function.FunctionCtx.set_materialize_grads "torch.autograd.function.FunctionCtx.set_materialize_grads") | Set whether to materialize grad tensors. |

Custom Function utilities[#](https://docs.pytorch.org/docs/2.15/autograd.html#custom-function-utilities "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

Decorator for backward method.

|     |     |
| --- | --- |
| [`function.once_differentiable`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.function.once_differentiable.html#torch.autograd.function.once_differentiable "torch.autograd.function.once_differentiable") |     |

Base custom [`Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
 used to build PyTorch utilities

|     |     |
| --- | --- |
| [`function.BackwardCFunction`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.function.BackwardCFunction.html#torch.autograd.function.BackwardCFunction "torch.autograd.function.BackwardCFunction") | This class is used for internal autograd work. |
| [`function.InplaceFunction`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.function.InplaceFunction.html#torch.autograd.function.InplaceFunction "torch.autograd.function.InplaceFunction") | This class is here only for backward compatibility reasons. |
| [`function.NestedIOFunction`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.function.NestedIOFunction.html#torch.autograd.function.NestedIOFunction "torch.autograd.function.NestedIOFunction") | This class is here only for backward compatibility reasons. |

Numerical gradient checking[#](https://docs.pytorch.org/docs/2.15/autograd.html#module-torch.autograd.gradcheck "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`gradcheck`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.gradcheck.gradcheck.html#torch.autograd.gradcheck.gradcheck "torch.autograd.gradcheck.gradcheck") | Check gradients computed via small finite differences against analytical gradients wrt tensors in `inputs` that are of floating point or complex type and with `requires_grad=True`. |
| [`gradgradcheck`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.gradcheck.gradgradcheck.html#torch.autograd.gradcheck.gradgradcheck "torch.autograd.gradcheck.gradgradcheck") | Check gradients of gradients computed via small finite differences against analytical gradients wrt tensors in `inputs` and `grad_outputs` that are of floating point or complex type and with `requires_grad=True`. |
| [`GradcheckError`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.gradcheck.GradcheckError.html#torch.autograd.gradcheck.GradcheckError "torch.autograd.gradcheck.GradcheckError") | Error raised by [`gradcheck()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.gradcheck.gradcheck.html#torch.autograd.gradcheck.gradcheck "torch.autograd.gradcheck.gradcheck")<br> and [`gradgradcheck()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.gradcheck.gradgradcheck.html#torch.autograd.gradcheck.gradgradcheck "torch.autograd.gradcheck.gradgradcheck")<br>. |
| [`get_analytical_jacobian`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.gradcheck.get_analytical_jacobian.html#torch.autograd.gradcheck.get_analytical_jacobian "torch.autograd.gradcheck.get_analytical_jacobian") |     |
| [`get_numerical_jacobian`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.gradcheck.get_numerical_jacobian.html#torch.autograd.gradcheck.get_numerical_jacobian "torch.autograd.gradcheck.get_numerical_jacobian") | Compute the numerical Jacobian for a given fn and its inputs. |
| [`get_numerical_jacobian_wrt_specific_input`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.gradcheck.get_numerical_jacobian_wrt_specific_input.html#torch.autograd.gradcheck.get_numerical_jacobian_wrt_specific_input "torch.autograd.gradcheck.get_numerical_jacobian_wrt_specific_input") |     |

Profiler[#](https://docs.pytorch.org/docs/2.15/autograd.html#profiler "Link to this heading")

----------------------------------------------------------------------------------------------

Autograd includes a profiler that lets you inspect the cost of different operators inside your model - both on the CPU and GPU. There are three modes implemented at the moment - CPU-only using [`profile`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.profiler.profile "torch.autograd.profiler.profile")
. nvprof based (registers both CPU and GPU activity) using [`emit_nvtx`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.profiler.emit_nvtx "torch.autograd.profiler.emit_nvtx")
. and vtune profiler based using [`emit_itt`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.profiler.emit_itt "torch.autograd.profiler.emit_itt")
.

_class_ torch.autograd.profiler.profile(_enabled\=True_, _\*_, _use\_device\=None_, _record\_shapes\=False_, _with\_flops\=False_, _profile\_memory\=False_, _with\_stack\=False_, _with\_modules\=False_, _use\_kineto\=False_, _use\_cpu\=True_, _experimental\_config\=None_, _acc\_events\=False_, _custom\_trace\_id\_callback\=None_, _post\_processing\_timeout\_s\=None_, _activity\_filters\=None_, _\_profiler\_extensions\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/profiler.py#L114)
[#](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.profiler.profile "Link to this definition")

Context manager that manages autograd profiler state and holds a summary of results.

Note

This is the backend, most people should use [`torch.profiler`](https://docs.pytorch.org/docs/2.15/profiler.html#module-torch.profiler "torch.profiler")
 instead.

Under the hood it just records events of functions being executed in C++ and exposes those events to Python. You can wrap any code into it and it will only report runtime of PyTorch functions. Note: profiler is thread local and is automatically propagated into the async tasks

Parameters:

*   **enabled** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Setting this to False makes this context manager a no-op.
    
*   **use\_device** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – Enables timing of device events. Adds approximately 4us of overhead to each tensor operation when use cuda. The valid devices options are ‘cuda’, ‘xpu’, ‘mtia’ and ‘privateuseone’.
    
*   **record\_shapes** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If shapes recording is set, information about input dimensions will be collected. This allows one to see which dimensions have been used under the hood and further group by them using prof.key\_averages(group\_by\_input\_shape=True). Please note that shape recording might skew your profiling data. It is recommended to use separate runs with and without shape recording to validate the timing. Most likely the skew will be negligible for bottom most events (in a case of nested function calls). But for higher level functions the total self cpu time might be artificially increased because of the shape collection.
    
*   **with\_flops** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If with\_flops is set, the profiler will estimate the FLOPs (floating point operations) value using the operator’s input shape. This allows one to estimate the hardware performance. Currently, this option only works for the matrix multiplication and 2D convolution operators.
    
*   **profile\_memory** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – track tensor memory allocation/deallocation.
    
*   **with\_stack** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – record source information (file and line number) for the ops.
    
*   **with\_modules** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) –
    
    record module hierarchy (including function names) corresponding to the callstack of the op. e.g. If module A’s forward call’s module B’s forward which contains an aten::add op, then aten::add’s module hierarchy is A.B
    
    Deprecated since version \`\`with\_modules\`\`: is deprecated and will be removed in a future version. It only collects data for TorchScript models, which are themselves deprecated, and does nothing in eager mode. Use `with_stack=True`, which records `nn.Module` events for eager models.
    
*   **use\_kineto** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – experimental, enable profiling with Kineto profiler.
    
*   **use\_cpu** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – profile CPU events; setting to `False` requires `use_kineto=True` and can be used to lower the overhead for GPU-only profiling.
    
*   **experimental\_config** (_\_ExperimentalConfig_) – A set of experimental options used by profiler libraries like Kineto. Note, backward compatibility is not guaranteed.
    
*   **acc\_events** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Enable the accumulation of FunctionEvents across multiple profiling cycles
    
*   **post\_processing\_timeout\_s** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – Optional timeout in seconds for post-processing profiler results. In this context, post-processing happens after the profiling itself has finished. If specified, event parsing will stop after this duration and return partial results. Useful for handling large traces that may take too long to process.
    

Warning

Enabling memory profiling or source attribution incurs additional profiler overhead

Warning

This context managers should not be called recursively, i.e. no nested instances are allowed

Warning

Due to some CUDA multiprocessing limitations (see [CUDA in multiprocessing](https://docs.pytorch.org/docs/2.15/notes/multiprocessing.html#multiprocessing-cuda-note)
), one cannot use the profiler with `use_device = 'cuda'` to benchmark DataLoaders with `num_workers > 0`. If you wish to benchmark data loading, please use `use_device = None` or `num_workers = 0`.

Example

\>>> x \= torch.randn((1, 1), requires\_grad\=True)
\>>> with torch.autograd.profiler.profile() as prof:
\>>>     for \_ in range(100):  \# any normal python code, really!
\>>>         y \= x \*\* 2
\>>>         y.backward()
\>>> \# NOTE: some columns were removed for brevity
\>>> print(prof.key\_averages().table(sort\_by\="self\_cpu\_time\_total"))
\-----------------------------------  ---------------  ---------------  ---------------
Name                                 Self CPU total   CPU time avg     Number of Calls
\-----------------------------------  ---------------  ---------------  ---------------
mul                                  32.048ms         32.048ms         200
pow                                  27.041ms         27.041ms         200
PowBackward0                         9.727ms          55.483ms         100
torch::autograd::AccumulateGrad      9.148ms          9.148ms          100
torch::autograd::GraphRoot           691.816us        691.816us        100
\-----------------------------------  ---------------  ---------------  ---------------

Copy to clipboard

|     |     |
| --- | --- |
| [`profiler.profile.export_chrome_trace`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.profiler.profile.export_chrome_trace.html#torch.autograd.profiler.profile.export_chrome_trace "torch.autograd.profiler.profile.export_chrome_trace") | Export an EventList as a Chrome tracing tools file. |
| [`profiler.profile.key_averages`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.profiler.profile.key_averages.html#torch.autograd.profiler.profile.key_averages "torch.autograd.profiler.profile.key_averages") | Averages all function events over their keys. |
| [`profiler.profile.self_cpu_time_total`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.profiler.profile.self_cpu_time_total.html#torch.autograd.profiler.profile.self_cpu_time_total "torch.autograd.profiler.profile.self_cpu_time_total") | Returns total time spent on CPU. |
| [`profiler.profile.total_average`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.profiler.profile.total_average.html#torch.autograd.profiler.profile.total_average "torch.autograd.profiler.profile.total_average") | Compute aggregate statistics across all events. |
| [`profiler.parse_nvprof_trace`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.profiler.parse_nvprof_trace.html#torch.autograd.profiler.parse_nvprof_trace "torch.autograd.profiler.parse_nvprof_trace") | Parse autograd annotations from an nvprof trace file. |
| [`profiler.EnforceUnique`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.profiler.EnforceUnique.html#torch.autograd.profiler.EnforceUnique "torch.autograd.profiler.EnforceUnique") | Raises an error if a key is seen more than once. |
| [`profiler.KinetoStepTracker`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.profiler.KinetoStepTracker.html#torch.autograd.profiler.KinetoStepTracker "torch.autograd.profiler.KinetoStepTracker") | Provides an abstraction for incrementing the step count globally. |
| [`profiler.record_function`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.profiler.record_function.html#torch.autograd.profiler.record_function "torch.autograd.profiler.record_function") | Context manager/function decorator that adds a label to a code block/function when running autograd profiler. |
| [`profiler_util.EventList`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.profiler_util.EventList.html#torch.autograd.profiler_util.EventList "torch.autograd.profiler_util.EventList") | A list of profiling events with helper methods for analysis and visualization. |
| [`profiler_util.FormattedTimesMixin`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.profiler_util.FormattedTimesMixin.html#torch.autograd.profiler_util.FormattedTimesMixin "torch.autograd.profiler_util.FormattedTimesMixin") | Helpers for FunctionEvent and FunctionEventAvg. |
| [`profiler_util.FunctionEvent`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.profiler_util.FunctionEvent.html#torch.autograd.profiler_util.FunctionEvent "torch.autograd.profiler_util.FunctionEvent") | Profiling information about a single function. |
| [`profiler_util.FunctionEventAvg`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.profiler_util.FunctionEventAvg.html#torch.autograd.profiler_util.FunctionEventAvg "torch.autograd.profiler_util.FunctionEventAvg") | Averaged profiling statistics over multiple FunctionEvent objects. |
| [`profiler_util.Interval`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.profiler_util.Interval.html#torch.autograd.profiler_util.Interval "torch.autograd.profiler_util.Interval") |     |
| [`profiler_util.Kernel`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.profiler_util.Kernel.html#torch.autograd.profiler_util.Kernel "torch.autograd.profiler_util.Kernel") |     |
| [`profiler_util.MemRecordsAcc`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.profiler_util.MemRecordsAcc.html#torch.autograd.profiler_util.MemRecordsAcc "torch.autograd.profiler_util.MemRecordsAcc") | Acceleration structure for accessing mem\_records in interval. |
| [`profiler_util.StringTable`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.profiler_util.StringTable.html#torch.autograd.profiler_util.StringTable "torch.autograd.profiler_util.StringTable") |     |

_class_ torch.autograd.profiler.emit\_nvtx(_enabled\=True_, _record\_shapes\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/profiler.py#L1095)
[#](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.profiler.emit_nvtx "Link to this definition")

Context manager that makes every autograd operation emit an NVTX range.

It is useful when running the program under nvprof:

nvprof \--profile\-from\-start off \-o trace\_name.prof \-- <regular command here\>

Copy to clipboard

Unfortunately, there’s no way to force nvprof to flush the data it collected to disk, so for CUDA profiling one has to use this context manager to annotate nvprof traces and wait for the process to exit before inspecting them. Then, either NVIDIA Visual Profiler (nvvp) can be used to visualize the timeline, or [`torch.autograd.profiler.load_nvprof()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.profiler.load_nvprof.html#torch.autograd.profiler.load_nvprof "torch.autograd.profiler.load_nvprof")
 can load the results for inspection e.g. in Python REPL.

Parameters:

*   **enabled** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Setting `enabled=False` makes this context manager a no-op. Default: `True`.
    
*   **record\_shapes** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `record_shapes=True`, the nvtx range wrapping each autograd op will append information about the sizes of Tensor arguments received by that op, in the following format: `[[arg0.size(0), arg0.size(1), ...], [arg1.size(0), arg1.size(1), ...], ...]` Non-tensor arguments will be represented by `[]`. Arguments will be listed in the order they are received by the backend op. Please note that this order may not match the order in which those arguments were passed on the Python side. Also note that shape recording may increase the overhead of nvtx range creation. Default: `False`
    

Example

\>>> with torch.cuda.profiler.profile():
...     model(x)  \# Warmup CUDA memory allocator and profiler
...     with torch.autograd.profiler.emit\_nvtx():
...         model(x)

Copy to clipboard

**Forward-backward correlation**

When viewing a profile created using [`emit_nvtx`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.profiler.emit_nvtx "torch.autograd.profiler.emit_nvtx")
 in the Nvidia Visual Profiler, correlating each backward-pass op with the corresponding forward-pass op can be difficult. To ease this task, [`emit_nvtx`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.profiler.emit_nvtx "torch.autograd.profiler.emit_nvtx")
 appends sequence number information to the ranges it generates.

During the forward pass, each function range is decorated with `seq=<N>`. `seq` is a running counter, incremented each time a new backward Function object is created and stashed for backward. Thus, the `seq=<N>` annotation associated with each forward function range tells you that if a backward Function object is created by this forward function, the backward object will receive sequence number N. During the backward pass, the top-level range wrapping each C++ backward Function’s `apply()` call is decorated with `stashed seq=<M>`. `M` is the sequence number that the backward object was created with. By comparing `stashed seq` numbers in backward with `seq` numbers in forward, you can track down which forward op created each backward Function.

Any functions executed during the backward pass are also decorated with `seq=<N>`. During default backward (with `create_graph=False`) this information is irrelevant, and in fact, `N` may simply be 0 for all such functions. Only the top-level ranges associated with backward Function objects’ `apply()` methods are useful, as a way to correlate these Function objects with the earlier forward pass.

**Double-backward**

If, on the other hand, a backward pass with `create_graph=True` is underway (in other words, if you are setting up for a double-backward), each function’s execution during backward is given a nonzero, useful `seq=<N>`. Those functions may themselves create Function objects to be executed later during double-backward, just as the original functions in the forward pass did. The relationship between backward and double-backward is conceptually the same as the relationship between forward and backward: The functions still emit current-sequence-number-tagged ranges, the Function objects they create still stash those sequence numbers, and during the eventual double-backward, the Function objects’ `apply()` ranges are still tagged with `stashed seq` numbers, which can be compared to seq numbers from the backward pass.

_class_ torch.autograd.profiler.emit\_itt(_enabled\=True_, _record\_shapes\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/profiler.py#L1024)
[#](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.profiler.emit_itt "Link to this definition")

Context manager that makes every autograd operation emit an ITT range.

It is useful when running the program under Intel(R) VTune Profiler:

vtune <--vtune\-flags\> <regular command here\>

Copy to clipboard

The Instrumentation and Tracing Technology (ITT) API enables your application to generate and control the collection of trace data during its execution across different Intel tools. This context manager is to annotate Intel(R) VTune Profiling trace. With help of this context manager, you will be able to see labeled ranges in Intel(R) VTune Profiler GUI.

Parameters:

*   **enabled** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Setting `enabled=False` makes this context manager a no-op. Default: `True`.
    
*   **record\_shapes** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `record_shapes=True`, the itt range wrapping each autograd op will append information about the sizes of Tensor arguments received by that op, in the following format: `[[arg0.size(0), arg0.size(1), ...], [arg1.size(0), arg1.size(1), ...], ...]` Non-tensor arguments will be represented by `[]`. Arguments will be listed in the order they are received by the backend op. Please note that this order may not match the order in which those arguments were passed on the Python side. Also note that shape recording may increase the overhead of itt range creation. Default: `False`
    

Example

\>>> with torch.autograd.profiler.emit\_itt():
...     model(x)

Copy to clipboard

|     |     |
| --- | --- |
| [`profiler.load_nvprof`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.profiler.load_nvprof.html#torch.autograd.profiler.load_nvprof "torch.autograd.profiler.load_nvprof") | Open an nvprof trace file and parse autograd annotations. |

Debugging and anomaly detection[#](https://docs.pytorch.org/docs/2.15/autograd.html#debugging-and-anomaly-detection "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

_class_ torch.autograd.detect\_anomaly(_check\_nan\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/anomaly_mode.py#L12)
[#](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.detect_anomaly "Link to this definition")

Context-manager that enables anomaly detection for the autograd engine.

This does two things:

*   Running the forward pass with detection enabled will allow the backward pass to print the traceback of the forward operation that created the failing backward function.
    
*   If `check_nan` is `True`, any backward computation that generates “nan” value will raise an error. Default `True`.
    

Warning

This mode should be enabled only for debugging as the different tests will slow down your program execution.

Example

\>>> import torch
\>>> from torch import autograd
\>>> class MyFunc(autograd.Function):
...     @staticmethod
...     def forward(ctx, inp):
...         return inp.clone()
...
...     @staticmethod
...     def backward(ctx, gO):
...         \# Error during the backward pass
...         raise RuntimeError("Some error in backward")
...         return gO.clone()
\>>> def run\_fn(a):
...     out \= MyFunc.apply(a)
...     return out.sum()
\>>> inp \= torch.rand(10, 10, requires\_grad\=True)
\>>> out \= run\_fn(inp)
\>>> out.backward()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/your/pytorch/install/torch/\_tensor.py", line 93, in backward
        torch.autograd.backward(self, gradient, retain\_graph, create\_graph)
      File "/your/pytorch/install/torch/autograd/\_\_init\_\_.py", line 90, in backward
        allow\_unreachable=True)  # allow\_unreachable flag
      File "/your/pytorch/install/torch/autograd/function.py", line 76, in apply
        return self.\_forward\_cls.backward(self, \*args)
      File "<stdin>", line 8, in backward
    RuntimeError: Some error in backward
\>>> with autograd.detect\_anomaly():
...     inp \= torch.rand(10, 10, requires\_grad\=True)
...     out \= run\_fn(inp)
...     out.backward()
    Traceback of forward call that caused the error:
      File "tmp.py", line 53, in <module>
        out = run\_fn(inp)
      File "tmp.py", line 44, in run\_fn
        out = MyFunc.apply(a)
    Traceback (most recent call last):
      File "<stdin>", line 4, in <module>
      File "/your/pytorch/install/torch/\_tensor.py", line 93, in backward
        torch.autograd.backward(self, gradient, retain\_graph, create\_graph)
      File "/your/pytorch/install/torch/autograd/\_\_init\_\_.py", line 90, in backward
        allow\_unreachable=True)  # allow\_unreachable flag
      File "/your/pytorch/install/torch/autograd/function.py", line 76, in apply
        return self.\_forward\_cls.backward(self, \*args)
      File "<stdin>", line 8, in backward
    RuntimeError: Some error in backward

Copy to clipboard

_class_ torch.autograd.set\_detect\_anomaly(_mode_, _check\_nan\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/anomaly_mode.py#L97)
[#](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.set_detect_anomaly "Link to this definition")

Context-manager that sets the anomaly detection for the autograd engine on or off.

`set_detect_anomaly` will enable or disable the autograd anomaly detection based on its argument `mode`. It can be used as a context-manager or as a function.

See `detect_anomaly` above for details of the anomaly detection behaviour.

Parameters:

*   **mode** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Flag whether to enable anomaly detection (`True`), or disable (`False`).
    
*   **check\_nan** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Flag whether to raise an error when the backward generate “nan”
    

|     |     |
| --- | --- |
| [`grad_mode.set_multithreading_enabled`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.grad_mode.set_multithreading_enabled.html#torch.autograd.grad_mode.set_multithreading_enabled "torch.autograd.grad_mode.set_multithreading_enabled") | Context-manager that enables or disables multithreaded backward. |
| [`grad_mode.enforce_grad_layout_policy`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.grad_mode.enforce_grad_layout_policy.html#torch.autograd.grad_mode.enforce_grad_layout_policy "torch.autograd.grad_mode.enforce_grad_layout_policy") | Context-manager that controls the gradient layout policy enforcement. |

Autograd graph[#](https://docs.pytorch.org/docs/2.15/autograd.html#autograd-graph "Link to this heading")

----------------------------------------------------------------------------------------------------------

Autograd exposes methods that allow one to inspect the graph and interpose behavior during the backward pass.

The `grad_fn` attribute of a [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
 holds a `torch.autograd.graph.Node` if the tensor is the output of a operation that was recorded by autograd (i.e., grad\_mode is enabled and at least one of the inputs required gradients), or `None` otherwise.

|     |     |
| --- | --- |
| [`graph.Node.name`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.graph.Node.name.html#torch.autograd.graph.Node.name "torch.autograd.graph.Node.name") | Return the name. |
| [`graph.Node.metadata`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.graph.Node.metadata.html#torch.autograd.graph.Node.metadata "torch.autograd.graph.Node.metadata") | Return the metadata. |
| [`graph.Node.next_functions`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.graph.Node.next_functions.html#torch.autograd.graph.Node.next_functions "torch.autograd.graph.Node.next_functions") | Return the edges from this node to its input functions. |
| [`graph.Node.register_hook`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.graph.Node.register_hook.html#torch.autograd.graph.Node.register_hook "torch.autograd.graph.Node.register_hook") | Register a backward hook. |
| [`graph.Node.register_prehook`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.graph.Node.register_prehook.html#torch.autograd.graph.Node.register_prehook "torch.autograd.graph.Node.register_prehook") | Register a backward pre-hook. |
| [`graph.increment_version`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.graph.increment_version.html#torch.autograd.graph.increment_version "torch.autograd.graph.increment_version") | Update autograd metadata tracking whether the given Tensor was modified in place. |

Some operations need intermediary results to be saved during the forward pass in order to execute the backward pass. These intermediary results are saved as attributes on the `grad_fn` and can be accessed. For example:

\>>> a \= torch.tensor(\[0., 0., 0.\], requires\_grad\=True)
\>>> b \= a.exp()
\>>> print(isinstance(b.grad\_fn, torch.autograd.graph.Node))
True
\>>> print(dir(b.grad\_fn))
\['\_\_call\_\_', '\_\_class\_\_', '\_\_delattr\_\_', '\_\_dir\_\_', '\_\_doc\_\_', '\_\_eq\_\_', '\_\_format\_\_', '\_\_ge\_\_', '\_\_getattribute\_\_', '\_\_gt\_\_', '\_\_hash\_\_', '\_\_init\_\_', '\_\_init\_subclass\_\_', '\_\_le\_\_', '\_\_lt\_\_', '\_\_ne\_\_', '\_\_new\_\_', '\_\_reduce\_\_', '\_\_reduce\_ex\_\_', '\_\_repr\_\_', '\_\_setattr\_\_', '\_\_sizeof\_\_', '\_\_str\_\_', '\_\_subclasshook\_\_', '\_raw\_saved\_result', '\_register\_hook\_dict', '\_saved\_result', 'metadata', 'name', 'next\_functions', 'register\_hook', 'register\_prehook', 'requires\_grad'\]
\>>> print(torch.allclose(b.grad\_fn.\_saved\_result, b))
True

Copy to clipboard

You can also define how these saved tensors should be packed / unpacked using hooks. A common application is to trade compute for memory by saving those intermediary results to disk or to CPU instead of leaving them on the GPU. This is especially useful if you notice your model fits on GPU during evaluation, but not training. When writing a `pack_hook` that keeps its input tensor, call `.detach()` on it first to avoid a reference cycle when the saved tensor is a graph output; see [Hooks for saved tensors](https://docs.pytorch.org/docs/2.15/notes/autograd.html#saved-tensors-hooks-doc)
 for details.

_class_ torch.autograd.graph.saved\_tensors\_hooks(_pack\_hook_, _unpack\_hook_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/graph.py#L297)
[#](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.graph.saved_tensors_hooks "Link to this definition")

Context-manager that sets a pair of pack / unpack hooks for saved tensors.

Use this context-manager to define how intermediary results of an operation should be packed before saving, and unpacked on retrieval.

In that context, the `pack_hook` function will be called every time an operation saves a tensor for backward (this includes intermediary results saved using `save_for_backward()` but also those recorded by a PyTorch-defined operation). The output of `pack_hook` is then stored in the computation graph instead of the original tensor.

The `unpack_hook` is called when the saved tensor needs to be accessed, namely when executing [`torch.Tensor.backward()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.backward.html#torch.Tensor.backward "torch.Tensor.backward")
 or [`torch.autograd.grad()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.grad.html#torch.autograd.grad "torch.autograd.grad")
. It takes as argument the _packed_ object returned by `pack_hook` and should return a tensor which has the same content as the original tensor (passed as input to the corresponding `pack_hook`).

The hooks should have the following signatures:

> pack\_hook(tensor: Tensor) -> Any
> 
> unpack\_hook(Any) -> Tensor

where the return value of `pack_hook` is a valid input to `unpack_hook`.

In general, you want `unpack_hook(pack_hook(t))` to be equal to `t` in terms of value, size, dtype and device.

Example:

\>>> def pack\_hook(x):
...     print("Packing", x)
...     return x.detach()
\>>>
\>>> def unpack\_hook(x):
...     print("Unpacking", x)
...     return x
\>>>
\>>> a \= torch.ones(5, requires\_grad\=True)
\>>> b \= torch.ones(5, requires\_grad\=True) \* 2
\>>> with torch.autograd.graph.saved\_tensors\_hooks(pack\_hook, unpack\_hook):
...     y \= a \* b
Packing tensor(\[1., 1., 1., 1., 1.\], requires\_grad=True)
Packing tensor(\[2., 2., 2., 2., 2.\], grad\_fn=<MulBackward0>)
\>>> y.sum().backward()
Unpacking tensor(\[1., 1., 1., 1., 1.\], requires\_grad=True)
Unpacking tensor(\[2., 2., 2., 2., 2.\], grad\_fn=<MulBackward0>)

Copy to clipboard

Warning

Performing an inplace operation on the input to either hooks may lead to undefined behavior.

Warning

Only one pair of hooks is allowed at a time. When recursively nesting this context-manager, only the inner-most pair of hooks will be applied.

Warning

To avoid reference cycle, the return value of `pack_hook` cannot hold a reference to the input tensor. For example, use lambda x: x.detach() instead of lambda x: x as the pack hook.

Note

The order in which `unpack_hook` calls are made during the backward pass is not specified. It follows the autograd engine’s execution order, which is not, in general, the reverse of the order in which `pack_hook` was called during the forward pass, and it can differ between graphs, workloads, and releases. Hooks that reconstruct tensors from shared state must therefore not rely on being invoked in reverse packing order.

_class_ torch.autograd.graph.save\_on\_cpu(_pin\_memory\=False_, _device\_type\='cuda'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/graph.py#L390)
[#](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.graph.save_on_cpu "Link to this definition")

Context manager under which tensors saved by the forward pass will be stored on cpu, then retrieved for backward.

When performing operations within this context manager, intermediary results saved in the graph during the forward pass will be moved to CPU, then copied back to the original device when needed for the backward pass. If the graph was already on CPU, no tensor copy is performed.

Use this context-manager to trade compute for GPU memory usage (e.g. when your model doesn’t fit in GPU memory during training).

Warning

When `pin_memory=True`, the GPU to CPU copy during packing is asynchronous. Accessing saved tensors on CPU (e.g. via `grad_fn._saved_self`) before the CUDA stream has finished may yield incorrect data. Call [`torch.cuda.synchronize()`](https://docs.pytorch.org/docs/2.15/generated/torch.cuda.synchronize.html#torch.cuda.synchronize "torch.cuda.synchronize")
 first if you need to read them.

Parameters:

**pin\_memory** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
) – If `True` tensors will be saved to CPU pinned memory during packing and copied to GPU asynchronously during both packing and unpacking. Defaults to `False`. Also see [Use pinned memory buffers](https://docs.pytorch.org/docs/2.15/notes/cuda.html#cuda-memory-pinning)
.

Example:

\>>> a \= torch.randn(5, requires\_grad\=True, device\="cuda")
\>>> b \= torch.randn(5, requires\_grad\=True, device\="cuda")
\>>> c \= torch.randn(5, requires\_grad\=True, device\="cuda")
\>>>
\>>> def f(a, b, c):
...     prod\_1 \= a \* b           \# a and b are saved on GPU
...     with torch.autograd.graph.save\_on\_cpu():
...         prod\_2 \= prod\_1 \* c  \# prod\_1 and c are saved on CPU
...     y \= prod\_2 \* a           \# prod\_2 and a are saved on GPU
...     return y
\>>>
\>>> y \= f(a, b, c)
\>>> del a, b, c  \# for illustration only
\>>> \# the content of a, b, and prod\_2 are still alive on GPU
\>>> \# the content of prod\_1 and c only live on CPU
\>>> y.sum().backward()  \# all CPU tensors are moved back to GPU, for backward
\>>> \# all intermediary tensors are released (deleted) after the call to backward

Copy to clipboard

_class_ torch.autograd.graph.disable\_saved\_tensors\_hooks(_error\_message_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/graph.py#L463)
[#](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.graph.disable_saved_tensors_hooks "Link to this definition")

Context-manager that disables the saved tensors default hooks feature.

Useful for if you are creating a feature that does not work with saved tensors default hooks.

Parameters:

**error\_message** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – When saved tensors default hooks are used when they have been disabled, a RuntimeError with this error message gets raised.

Return type:

[_Generator_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "(in Python v3.15)")
\[None, None, None\]

Example:

\>>> message \= "saved tensors default hooks are disabled"
\>>> with torch.autograd.graph.disable\_saved\_tensors\_hooks(message):
...     \# Raises RuntimeError: saved tensors default hooks are disabled
...     with torch.autograd.graph.save\_on\_cpu():
...         pass

Copy to clipboard

_class_ torch.autograd.graph.register\_multi\_grad\_hook(_tensors_, _fn_, _\*_, _mode\='all'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/graph.py#L712)
[#](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.graph.register_multi_grad_hook "Link to this definition")

Register a multi-grad backward hook.

There are two supported modes: `"all"` and `"any"`.

Under the `"all"` mode, the hook will be called after gradients with respect to every tensor in `tensors` have been computed. If a tensor is in `tensors` but is not part of the graph, or if a tensor is not needed to compute the gradients for any `inputs` specified for the current `.backward()` or `.grad()` call, this tensor will be ignored and the hook will not wait for its gradient to be computed.

After every non-ignored tensor’s gradient has been computed, `fn` will be called with those gradients. `None` will be passed for tensors that did not have their gradients computed.

Under the `"any"` mode, the hook will be called after the first gradient with respect to a tensor in `tensors` has been computed. The hook will be called with that gradient as its argument.

The hook should not modify its arguments.

This function returns a handle with a method `handle.remove()` that removes the hook.

Note

See [Backward Hooks execution](https://docs.pytorch.org/docs/2.15/notes/autograd.html#backward-hooks-execution)
 for more information on how when this hook is executed, and how its execution is ordered relative to other hooks.

Example:

\>>> import torch
\>>>
\>>> a \= torch.rand(2, 3, requires\_grad\=True)
\>>> b \= torch.rand(2, 3, requires\_grad\=True)
\>>> c \= a \* b
\>>> d \= a \* b
\>>>
\>>> def fn(grads):
...     print(\[g is not None for g in grads\])
...
\>>> torch.autograd.graph.register\_multi\_grad\_hook((a, b, c, d), fn)
\>>>
\>>> c.sum().backward(retain\_graph\=True)
\[True, True, True, False\]
\>>> c.sum().backward(inputs\=(a,), retain\_graph\=True)
\[True, False, True, False\]
\>>>

Copy to clipboard

Return type:

_RemovableHandle_

_class_ torch.autograd.graph.node\_creation\_hook(_hook_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/graph.py#L499)
[#](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.graph.node_creation_hook "Link to this definition")

Context-manager that registers a hook called on each autograd Node created within it.

In that context, `hook` is called once for every autograd graph node created by operations on tensors that require grad, with the freshly created `torch.autograd.graph.Node` as its only argument. The intended use is to record the node, stash entries in `node.metadata`, or register backward hooks on it via [`register_hook()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.graph.Node.register_hook.html#torch.autograd.graph.Node.register_hook "torch.autograd.graph.Node.register_hook")
 and [`register_prehook()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.graph.Node.register_prehook.html#torch.autograd.graph.Node.register_prehook "torch.autograd.graph.Node.register_prehook")
.

The node is passed to the hook only once it is fully populated: its `next_functions` are wired, all outputs’ metadata are bound, and the tensors saved for backward (`_saved_*`) have been stored, so a hook that inspects the node sees its complete state.

The hook should have the following signature:

hook(node: torch.autograd.graph.Node) \-> None

Copy to clipboard

The registration is thread-local and propagates like other autograd thread-local state: it is active on autograd engine worker threads, so nodes created during backward (e.g. with `create_graph=True` or inside checkpoint recomputation) also fire the hook.

When nesting this context-manager, every active hook is called for each node, in registration order (outermost context-manager first). Creating a new autograd node from inside a hook raises an error; hooks must only observe the node they are given.

One motivating use case is attributing work done during backward to the forward region that created the graph, by capturing state at node creation time and restoring it around the node’s backward execution:

\>>> def creation\_hook(node):
...     \# \`\`current\_region()\`\`/\`\`enter\_region()\`\` are user-defined and
...     \# stand in for whatever thread-local state you want to restore
...     \# while this node runs in backward.
...     region \= current\_region()
...     node.register\_prehook(lambda gO: enter\_region(region))
...     node.register\_hook(lambda gI, gO: enter\_region(None))
\>>>
\>>> with torch.autograd.graph.node\_creation\_hook(creation\_hook):
...     loss \= model(inputs)

Copy to clipboard

Example:

\>>> a \= torch.ones(5, requires\_grad\=True)
\>>> with torch.autograd.graph.node\_creation\_hook(lambda node: print(node)):
...     b \= a \* 2
<AccumulateGrad object at ...>
<MulBackward0 object at ...>

Copy to clipboard

Note

An `AccumulateGrad` node fires this hook when it is created, but not when a previously created one is reused. The node is created on demand the first time a leaf tensor is wired into a graph and is then cached (via a weak reference) on the leaf, so it fires again only after the old node has been freed. Since freeing the autograd graph drops that node, code that frees the graph each iteration (the common case) fires the hook consistently on each leaf’s first use within the context.

_class_ torch.autograd.graph.allow\_mutation\_on\_saved\_tensors[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/graph.py#L1002)
[#](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.graph.allow_mutation_on_saved_tensors "Link to this definition")

Context manager under which mutating tensors saved for backward is allowed.

Under this context manager, tensors saved for backward are cloned on mutation, so the original version can still be used during backward. Normally, mutating a tensor saved for backward will result in an error raised when it’s used during backward.

To ensure the correct behavior, both the forward and backward should be run under the same context manager.

Returns:

An \_AllowMutationOnSavedContext object storing the state managed by this context manager. This object can be useful for debugging purposes. The state managed by the context manager is automatically cleared upon exiting.

Return type:

[_Generator_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "(in Python v3.15)")
\[_\_AllowMutationOnSavedContext_, None, None\]

Example:

\>>> import torch
\>>> with torch.autograd.graph.allow\_mutation\_on\_saved\_tensors():
...     \# forward
...     a \= torch.ones(2, 3, requires\_grad\=True)
...     b \= a.clone()
...     out \= (b\*\*2).sum()
...     b.sin\_()
...     \# backward
...     out.sum().backward()
...
tensor(\[\[0.8415, 0.8415, 0.8415\],\
        \[0.8415, 0.8415, 0.8415\]\], grad\_fn=<SinBackward0>)

Copy to clipboard

_class_ torch.autograd.graph.GradientEdge(_node_, _output\_nr_, _ownership\_token\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/graph.py#L211)
[#](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.graph.GradientEdge "Link to this definition")

Object representing a given gradient edge within the autograd graph.

To get the gradient edge where a given Tensor gradient will be computed, you can do `edge = autograd.graph.get_gradient_edge(tensor)`.

torch.autograd.graph.get\_gradient\_edge(_tensor_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/graph.py#L225)
[#](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.graph.get_gradient_edge "Link to this definition")

Get the gradient edge for computing the gradient of the given Tensor.

In particular, it is equivalent to call `g = autograd.grad(loss, input)` and `g = autograd.grad(loss, get_gradient_edge(input))`.

Return type:

[_GradientEdge_](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.graph.GradientEdge "torch.autograd.graph.GradientEdge")

torch.autograd.graph.queue\_callback(_callback_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/graph.py#L274)
[#](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.graph.queue_callback "Link to this definition")

Queue a callback to run after the current backward pass completes.

Must be called during a backward pass, for example from a [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
 backward or a backward hook. The callback runs once the backward pass currently executing on this thread completes successfully; it is not run if the backward pass raises an error. Callbacks queued multiple times run multiple times, in queueing order.

Example:

\>>> t \= torch.rand(3, requires\_grad\=True)
\>>>
\>>> def hook(unused\_grad):
...     torch.autograd.graph.queue\_callback(lambda: print("backward done"))
\>>>
\>>> \_ \= t.register\_hook(hook)
\>>> t.sum().backward()
backward done

Copy to clipboard

torch.autograd.graph.region\_activation\_memory\_budget(_budget_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/graph.py#L574)
[#](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.graph.region_activation_memory_budget "Link to this definition")

Set the activation memory budget for the region of a compiled forward traced under this context manager.

Warning

This is a prototype feature and is subject to change.

Using this API with regions that remain as opaque higher-order operators, such as `torch.compiler.nested_compile_region`, is not recommended. An opaque higher-order operator and its enclosing graph may be partitioned independently, which can cause unexpected interactions such as duplicated recomputation. This behavior is subject to change.

Under [`torch.compile()`](https://docs.pytorch.org/docs/2.15/generated/torch.compile.html#torch.compile "torch.compile")
, the min-cut partitioner chooses which activations to save versus recompute in the backward pass to stay under a memory budget. `budget` is a ratio in `[0, 1]`: `0.0` corresponds to the activation memory from applying activation checkpointing to the full region, and `1.0` corresponds to the activation memory from the default runtime-optimized strategy. So `0.4` would result in a strategy that saves 40% of the activations compared to the default strategy. It solves a 0-1 knapsack to find the minimum recompute necessary to stay below the budget. This overrides the global `torch._functorch.config.activation_memory_budget` for the annotated region.

Note

Today the partitioner only supports a single budget per compiled graph, so all budget contexts within a graph must agree. By default, the context must cover every forward operation in that graph. Set `torch._functorch.config.activation_memory_budget_require_full_coverage` to `False` while compiling to permit unannotated operations; the budget then applies to the whole graph containing the context. To use different budgets for different parts of a model, separate them with a graph break (e.g. `torch._dynamo.graph_break()`). The context remains active across graph breaks, but a graph with no annotated operations uses the global `torch._functorch.config.activation_memory_budget`.

This only has an effect under [`torch.compile()`](https://docs.pytorch.org/docs/2.15/generated/torch.compile.html#torch.compile "torch.compile")
; using it outside of a compiled region raises a `RuntimeError`.

Parameters:

**budget** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
) – Activation memory budget ratio in `[0, 1]`.

Return type:

[_AbstractContextManager_](https://docs.python.org/3/library/contextlib.html#contextlib.AbstractContextManager "(in Python v3.15)")
\[None\]

Example:

\>>> with torch.autograd.graph.region\_activation\_memory\_budget(0.0):
...     x \= layer(x)  \# recompute this region's activations in backward

Copy to clipboard

torch.autograd.graph.set\_warn\_on\_accumulate\_grad\_stream\_mismatch(_enabled_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/graph.py#L647)
[#](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.graph.set_warn_on_accumulate_grad_stream_mismatch "Link to this definition")

Whether to warn when the AccumulateGrad node’s stream does not match the stream of the node that produced the incoming gradient.

torch.autograd.graph.set\_override\_stale\_capture\_stream(_enabled_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/autograd/graph.py#L654)
[#](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.graph.set_override_stale_capture_stream "Link to this definition")

Control behavior when autograd detects a stale non-capturing stream during CUDA graph capture.

During CUDA graph capture, autograd nodes may reference a stale stream that is not part of the capture. With the flag disabled (the process-initial state), autograd raises a `RuntimeError` when the stale stream is the default stream (stream 0), because this case always invalidates the capture: `cudaStreamWaitEvent` on the default stream pulls a non-capturing stream into the graph. For non-default stale streams the stream reference is left unchanged; the capture will succeed if the user has joined the stream into the capture (e.g. via `capture_stream.wait_stream(stale_stream)`) and will otherwise fail with a CUDA runtime error.

When `enabled=True`, any stale non-capturing stream (default or non-default) is automatically overridden with the producer’s capturing stream, allowing the capture to proceed. This is a process-global setting and is not thread-local.

The flag also governs the end-of-backward sync between each leaf’s stream and the caller’s current stream. A leaf whose incoming gradients are all undefined (e.g. patterns that compute certain gradients out of band and return `None` from autograd) cannot be reconciled by the override, so when exactly one of the two streams is capturing, that sync would cross the capture boundary: with the flag enabled the sync is skipped (work on a non-capturing stream is not part of the capture, so the ordering has no effect on it); with the flag disabled a `RuntimeError` is raised.

Parameters:

**enabled** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
) – If `True`, override stale non-capturing streams with the producer’s capturing stream during CUDA graph capture, and skip end-of-backward leaf syncs that would cross the capture boundary. If `False` (the process-initial state), raise an error when the stale stream is the default stream (stream 0) or when a leaf sync would cross the capture boundary; other stale streams are left unchanged.

|     |     |
| --- | --- |
| [`Variable`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.variable.Variable.html#torch.autograd.variable.Variable "torch.autograd.variable.Variable") |     |
| [`VariableMeta`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.variable.VariableMeta.html#torch.autograd.variable.VariableMeta "torch.autograd.variable.VariableMeta") |     |

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/autograd.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/autograd.md.txt)

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