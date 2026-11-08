Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/func.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/func.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/func.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/func.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/func.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/func.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/func.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/func.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/func.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/func.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/func.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/func.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/func.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/func.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/func.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/func.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/func.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/func.html)
[v1.13](https://docs.pytorch.org/docs/1.13/func.html)
[v1.12](https://docs.pytorch.org/docs/1.12/func.html)
[v1.11](https://docs.pytorch.org/docs/1.11/func.html)
[v1.10](https://docs.pytorch.org/docs/1.10/func.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/func.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/func.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/func.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/func.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/func.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/func.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/func.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/func.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/func.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/func.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/func.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/func.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/func.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/func.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/func.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/func.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/func.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/func.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/func.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/func.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/func.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/func.html)

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

torch.func[#](https://docs.pytorch.org/docs/2.15/func.html#torch-func "Link to this heading")

==============================================================================================

Created On: Jun 11, 2025 | Last Updated On: Jun 11, 2025

torch.func, previously known as “functorch”, is [JAX-like](https://github.com/google/jax)
 composable function transforms for PyTorch.

Note

This library is currently in [beta](https://pytorch.org/blog/pytorch-feature-classification-changes/#beta)
. What this means is that the features generally work (unless otherwise documented) and we (the PyTorch team) are committed to bringing this library forward. However, the APIs may change under user feedback and we don’t have full coverage over PyTorch operations.

If you have suggestions on the API or use-cases you’d like to be covered, please open a GitHub issue or reach out. We’d love to hear about how you’re using the library.

What are composable function transforms?[#](https://docs.pytorch.org/docs/2.15/func.html#what-are-composable-function-transforms "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

*   A “function transform” is a higher-order function that accepts a numerical function and returns a new function that computes a different quantity.
    
*   [`torch.func`](https://docs.pytorch.org/docs/2.15/func.api.html#module-torch.func "torch.func")
     has auto-differentiation transforms (`grad(f)` returns a function that computes the gradient of `f`), a vectorization/batching transform (`vmap(f)` returns a function that computes `f` over batches of inputs), and others.
    
*   These function transforms can compose with each other arbitrarily. For example, composing `vmap(grad(f))` computes a quantity called per-sample-gradients that stock PyTorch cannot efficiently compute today.
    

Why composable function transforms?[#](https://docs.pytorch.org/docs/2.15/func.html#why-composable-function-transforms "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

There are a number of use cases that are tricky to do in PyTorch today:

*   computing per-sample-gradients (or other per-sample quantities)
    
*   running ensembles of models on a single machine
    
*   efficiently batching together tasks in the inner-loop of MAML
    
*   efficiently computing Jacobians and Hessians
    
*   efficiently computing batched Jacobians and Hessians
    

Composing [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vmap.html#torch.func.vmap "torch.func.vmap")
, [`grad()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.grad.html#torch.func.grad "torch.func.grad")
, and [`vjp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vjp.html#torch.func.vjp "torch.func.vjp")
 transforms allows us to express the above without designing a separate subsystem for each. This idea of composable function transforms comes from the [JAX framework](https://github.com/google/jax)
.

Read More[#](https://docs.pytorch.org/docs/2.15/func.html#read-more "Link to this heading")

--------------------------------------------------------------------------------------------

*   [torch.func Whirlwind Tour](https://docs.pytorch.org/docs/2.15/func.whirlwind_tour.html)
    *   [What is torch.func?](https://docs.pytorch.org/docs/2.15/func.whirlwind_tour.html#what-is-torch-func)
        
    *   [Why composable function transforms?](https://docs.pytorch.org/docs/2.15/func.whirlwind_tour.html#why-composable-function-transforms)
        
    *   [What are the transforms?](https://docs.pytorch.org/docs/2.15/func.whirlwind_tour.html#what-are-the-transforms)
        
*   [torch.func API Reference](https://docs.pytorch.org/docs/2.15/func.api.html)
    *   [Function Transforms](https://docs.pytorch.org/docs/2.15/func.api.html#function-transforms)
        
    *   [Utilities for working with torch.nn.Modules](https://docs.pytorch.org/docs/2.15/func.api.html#utilities-for-working-with-torch-nn-modules)
        
    *   [Debug utilities](https://docs.pytorch.org/docs/2.15/func.api.html#debug-utilities)
        
*   [UX Limitations](https://docs.pytorch.org/docs/2.15/func.ux_limitations.html)
    *   [General limitations](https://docs.pytorch.org/docs/2.15/func.ux_limitations.html#general-limitations)
        
    *   [torch.autograd APIs](https://docs.pytorch.org/docs/2.15/func.ux_limitations.html#torch-autograd-apis)
        
    *   [vmap limitations](https://docs.pytorch.org/docs/2.15/func.ux_limitations.html#vmap-limitations)
        
    *   [Randomness](https://docs.pytorch.org/docs/2.15/func.ux_limitations.html#randomness)
        
*   [Migrating from functorch to torch.func](https://docs.pytorch.org/docs/2.15/func.migrating.html)
    *   [function transforms](https://docs.pytorch.org/docs/2.15/func.migrating.html#function-transforms)
        
    *   [NN module utilities](https://docs.pytorch.org/docs/2.15/func.migrating.html#nn-module-utilities)
        
    *   [functorch.compile](https://docs.pytorch.org/docs/2.15/func.migrating.html#functorch-compile)
        

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/func.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/func.md.txt)

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