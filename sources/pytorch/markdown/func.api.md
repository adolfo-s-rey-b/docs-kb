Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/func.api.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/func.api.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/func.api.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/func.api.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/func.api.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/func.api.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/func.api.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/func.api.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/func.api.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/func.api.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/func.api.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/func.api.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/func.api.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/func.api.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/func.api.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/func.api.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/func.api.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/func.api.html)
[v1.13](https://docs.pytorch.org/docs/1.13/func.api.html)
[v1.12](https://docs.pytorch.org/docs/1.12/func.api.html)
[v1.11](https://docs.pytorch.org/docs/1.11/func.api.html)
[v1.10](https://docs.pytorch.org/docs/1.10/func.api.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/func.api.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/func.api.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/func.api.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/func.api.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/func.api.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/func.api.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/func.api.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/func.api.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/func.api.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/func.api.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/func.api.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/func.api.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/func.api.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/func.api.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/func.api.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/func.api.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/func.api.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/func.api.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/func.api.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/func.api.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/func.api.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/func.api.html)

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

torch.func API Reference[#](https://docs.pytorch.org/docs/2.15/func.api.html#module-torch.func "Link to this heading")

=======================================================================================================================

Created On: Jun 11, 2025 | Last Updated On: May 04, 2026

Function Transforms[#](https://docs.pytorch.org/docs/2.15/func.api.html#function-transforms "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`vmap`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vmap.html#torch.func.vmap "torch.func.vmap") | vmap is the vectorizing map; `vmap(func)` returns a new function that maps `func` over some dimension of the inputs. |
| [`grad`](https://docs.pytorch.org/docs/2.15/generated/torch.func.grad.html#torch.func.grad "torch.func.grad") | `grad` operator helps computing gradients of `func` with respect to the input(s) specified by `argnums`. |
| [`grad_and_value`](https://docs.pytorch.org/docs/2.15/generated/torch.func.grad_and_value.html#torch.func.grad_and_value "torch.func.grad_and_value") | Returns a function to compute a tuple of the gradient and primal, or forward, computation. |
| [`vjp`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vjp.html#torch.func.vjp "torch.func.vjp") | Standing for the vector-Jacobian product, returns a tuple containing the results of `func` applied to `primals` and a function that, when given `cotangents`, computes the reverse-mode Jacobian of `func` with respect to `primals` times `cotangents`. |
| [`jvp`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jvp.html#torch.func.jvp "torch.func.jvp") | Standing for the Jacobian-vector product, returns a tuple containing the output of func(\*primals) and the "Jacobian of `func` evaluated at `primals`" times `tangents`. |
| [`linearize`](https://docs.pytorch.org/docs/2.15/generated/torch.func.linearize.html#torch.func.linearize "torch.func.linearize") | Returns the value of `func` at `primals` and linear approximation at `primals`. |
| [`jacrev`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacrev.html#torch.func.jacrev "torch.func.jacrev") | Computes the Jacobian of `func` with respect to the arg(s) at index `argnum` using reverse mode autodiff |
| [`jacfwd`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacfwd.html#torch.func.jacfwd "torch.func.jacfwd") | Computes the Jacobian of `func` with respect to the arg(s) at index `argnum` using forward-mode autodiff |
| [`hessian`](https://docs.pytorch.org/docs/2.15/generated/torch.func.hessian.html#torch.func.hessian "torch.func.hessian") | Computes the Hessian of `func` with respect to the arg(s) at index `argnum` via a forward-over-reverse strategy. |
| [`functionalize`](https://docs.pytorch.org/docs/2.15/generated/torch.func.functionalize.html#torch.func.functionalize "torch.func.functionalize") | functionalize is a transform that can be used to remove (intermediate) mutations and aliasing from a function, while preserving the function's semantics. |
| [`rearrange`](https://docs.pytorch.org/docs/2.15/generated/torch.func.rearrange.html#torch.func.rearrange "torch.func.rearrange") | A native implementation of einops.rearrange, a reader-friendly smart element reordering for multidimensional tensors. |

Utilities for working with torch.nn.Modules[#](https://docs.pytorch.org/docs/2.15/func.api.html#utilities-for-working-with-torch-nn-modules "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

In general, you can transform over a function that calls a `torch.nn.Module`. For example, the following is an example of computing a jacobian of a function that takes three values and returns three values:

model \= torch.nn.Linear(3, 3)

def f(x):
    return model(x)

x \= torch.randn(3)
jacobian \= jacrev(f)(x)
assert jacobian.shape \== (3, 3)

Copy to clipboard

However, if you want to do something like compute a jacobian over the parameters of the model, then there needs to be a way to construct a function where the parameters are the inputs to the function. That’s what [`functional_call()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.functional_call.html#torch.func.functional_call "torch.func.functional_call")
 is for: it accepts an nn.Module, the transformed `parameters`, and the inputs to the Module’s forward pass. It returns the value of running the Module’s forward pass with the replaced parameters.

Here’s how we would compute the Jacobian over the parameters

model \= torch.nn.Linear(3, 3)

def f(params, x):
    return torch.func.functional\_call(model, params, x)

x \= torch.randn(3)
jacobian \= jacrev(f)(dict(model.named\_parameters()), x)

Copy to clipboard

|     |     |
| --- | --- |
| [`functional_call`](https://docs.pytorch.org/docs/2.15/generated/torch.func.functional_call.html#torch.func.functional_call "torch.func.functional_call") | Performs a functional call on the module by replacing the module parameters and buffers with the provided ones. |
| [`stack_module_state`](https://docs.pytorch.org/docs/2.15/generated/torch.func.stack_module_state.html#torch.func.stack_module_state "torch.func.stack_module_state") | Prepares a list of torch.nn.Modules for ensembling with [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vmap.html#torch.func.vmap "torch.func.vmap")<br>. |
| [`replace_all_batch_norm_modules_`](https://docs.pytorch.org/docs/2.15/generated/torch.func.replace_all_batch_norm_modules_.html#torch.func.replace_all_batch_norm_modules_ "torch.func.replace_all_batch_norm_modules_") | In place updates `root` by setting the `running_mean` and `running_var` to be None and setting track\_running\_stats to be False for any nn.BatchNorm module in `root` |

If you’re looking for information on fixing Batch Norm modules, please follow the guidance here

*   [Patching Batch Norm](https://docs.pytorch.org/docs/2.15/func.batch_norm.html)
    

Debug utilities[#](https://docs.pytorch.org/docs/2.15/func.api.html#debug-utilities "Link to this heading")

------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`debug_unwrap`](https://docs.pytorch.org/docs/2.15/generated/torch.func.debug_unwrap.html#torch.func.debug_unwrap "torch.func.debug_unwrap") | Unwraps a functorch tensor (e.g. BatchedTensor, GradTrackingTensor) to its underlying tensor. |

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/func.api.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/func.api.md.txt)

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