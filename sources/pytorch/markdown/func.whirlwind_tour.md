Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/func.whirlwind_tour.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/func.whirlwind_tour.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/func.whirlwind_tour.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/func.whirlwind_tour.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/func.whirlwind_tour.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/func.whirlwind_tour.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/func.whirlwind_tour.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/func.whirlwind_tour.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/func.whirlwind_tour.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/func.whirlwind_tour.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/func.whirlwind_tour.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/func.whirlwind_tour.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/func.whirlwind_tour.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/func.whirlwind_tour.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/func.whirlwind_tour.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/func.whirlwind_tour.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/func.whirlwind_tour.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/func.whirlwind_tour.html)
[v1.13](https://docs.pytorch.org/docs/1.13/func.whirlwind_tour.html)
[v1.12](https://docs.pytorch.org/docs/1.12/func.whirlwind_tour.html)
[v1.11](https://docs.pytorch.org/docs/1.11/func.whirlwind_tour.html)
[v1.10](https://docs.pytorch.org/docs/1.10/func.whirlwind_tour.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/func.whirlwind_tour.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/func.whirlwind_tour.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/func.whirlwind_tour.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/func.whirlwind_tour.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/func.whirlwind_tour.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/func.whirlwind_tour.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/func.whirlwind_tour.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/func.whirlwind_tour.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/func.whirlwind_tour.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/func.whirlwind_tour.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/func.whirlwind_tour.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/func.whirlwind_tour.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/func.whirlwind_tour.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/func.whirlwind_tour.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/func.whirlwind_tour.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/func.whirlwind_tour.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/func.whirlwind_tour.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/func.whirlwind_tour.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/func.whirlwind_tour.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/func.whirlwind_tour.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/func.whirlwind_tour.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/func.whirlwind_tour.html)

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

torch.func Whirlwind Tour[#](https://docs.pytorch.org/docs/2.15/func.whirlwind_tour.html#torch-func-whirlwind-tour "Link to this heading")

===========================================================================================================================================

Created On: Jun 12, 2025 | Last Updated On: Jun 12, 2025

What is torch.func?[#](https://docs.pytorch.org/docs/2.15/func.whirlwind_tour.html#what-is-torch-func "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

torch.func, previously known as functorch, is a library for [JAX](https://github.com/google/jax)
\-like composable function transforms in PyTorch.

*   A “function transform” is a higher-order function that accepts a numerical function and returns a new function that computes a different quantity.
    
*   torch.func has auto-differentiation transforms (`grad(f)` returns a function that computes the gradient of `f`), a vectorization/batching transform (`vmap(f)` returns a function that computes `f` over batches of inputs), and others.
    
*   These function transforms can compose with each other arbitrarily. For example, composing `vmap(grad(f))` computes a quantity called per-sample-gradients that stock PyTorch cannot efficiently compute today.
    

Why composable function transforms?[#](https://docs.pytorch.org/docs/2.15/func.whirlwind_tour.html#why-composable-function-transforms "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

There are a number of use cases that are tricky to do in PyTorch today:

*   computing per-sample-gradients (or other per-sample quantities)
    
*   running ensembles of models on a single machine
    
*   efficiently batching together tasks in the inner-loop of MAML
    
*   efficiently computing Jacobians and Hessians
    
*   efficiently computing batched Jacobians and Hessians
    

Composing [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vmap.html#torch.func.vmap "torch.func.vmap")
, [`grad()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.grad.html#torch.func.grad "torch.func.grad")
, [`vjp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vjp.html#torch.func.vjp "torch.func.vjp")
, and [`jvp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jvp.html#torch.func.jvp "torch.func.jvp")
 transforms allows us to express the above without designing a separate subsystem for each.

What are the transforms?[#](https://docs.pytorch.org/docs/2.15/func.whirlwind_tour.html#what-are-the-transforms "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

### [`grad()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.grad.html#torch.func.grad "torch.func.grad")
 (gradient computation)[#](https://docs.pytorch.org/docs/2.15/func.whirlwind_tour.html#grad-gradient-computation "Link to this heading")

`grad(func)` is our gradient computation transform. It returns a new function that computes the gradients of `func`. It assumes `func` returns a single-element Tensor and by default it computes the gradients of the output of `func` w.r.t. to the first input.

import torch
from torch.func import grad
x \= torch.randn(\[\])
cos\_x \= grad(lambda x: torch.sin(x))(x)
assert torch.allclose(cos\_x, x.cos())

\# Second-order gradients
neg\_sin\_x \= grad(grad(lambda x: torch.sin(x)))(x)
assert torch.allclose(neg\_sin\_x, \-x.sin())

Copy to clipboard

### [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vmap.html#torch.func.vmap "torch.func.vmap")
 (auto-vectorization)[#](https://docs.pytorch.org/docs/2.15/func.whirlwind_tour.html#vmap-auto-vectorization "Link to this heading")

Note: [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vmap.html#torch.func.vmap "torch.func.vmap")
 imposes restrictions on the code that it can be used on. For more details, please see [UX Limitations](https://docs.pytorch.org/docs/2.15/func.ux_limitations.html#ux-limitations)
.

`vmap(func)(*inputs)` is a transform that adds a dimension to all Tensor operations in `func`. `vmap(func)` returns a new function that maps `func` over some dimension (default: 0) of each Tensor in inputs.

vmap is useful for hiding batch dimensions: one can write a function func that runs on examples and then lift it to a function that can take batches of examples with `vmap(func)`, leading to a simpler modeling experience:

import torch
from torch.func import vmap
batch\_size, feature\_size \= 3, 5
weights \= torch.randn(feature\_size, requires\_grad\=True)

def model(feature\_vec):
    \# Very simple linear model with activation
    assert feature\_vec.dim() \== 1
    return feature\_vec.dot(weights).relu()

examples \= torch.randn(batch\_size, feature\_size)
result \= vmap(model)(examples)

Copy to clipboard

When composed with [`grad()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.grad.html#torch.func.grad "torch.func.grad")
, [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vmap.html#torch.func.vmap "torch.func.vmap")
 can be used to compute per-sample-gradients:

from torch.func import vmap
batch\_size, feature\_size \= 3, 5

def model(weights,feature\_vec):
    \# Very simple linear model with activation
    assert feature\_vec.dim() \== 1
    return feature\_vec.dot(weights).relu()

def compute\_loss(weights, example, target):
    y \= model(weights, example)
    return ((y \- target) \*\* 2).mean()  \# MSELoss

weights \= torch.randn(feature\_size, requires\_grad\=True)
examples \= torch.randn(batch\_size, feature\_size)
targets \= torch.randn(batch\_size)
inputs \= (weights,examples, targets)
grad\_weight\_per\_example \= vmap(grad(compute\_loss), in\_dims\=(None, 0, 0))(\*inputs)

Copy to clipboard

### [`vjp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vjp.html#torch.func.vjp "torch.func.vjp")
 (vector-Jacobian product)[#](https://docs.pytorch.org/docs/2.15/func.whirlwind_tour.html#vjp-vector-jacobian-product "Link to this heading")

The [`vjp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vjp.html#torch.func.vjp "torch.func.vjp")
 transform applies `func` to `inputs` and returns a new function that computes the vector-Jacobian product (vjp) given some `cotangents` Tensors.

from torch.func import vjp

inputs \= torch.randn(3)
func \= torch.sin
cotangents \= (torch.randn(3),)

outputs, vjp\_fn \= vjp(func, inputs); vjps \= vjp\_fn(\*cotangents)

Copy to clipboard

### [`jvp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jvp.html#torch.func.jvp "torch.func.jvp")
 (Jacobian-vector product)[#](https://docs.pytorch.org/docs/2.15/func.whirlwind_tour.html#jvp-jacobian-vector-product "Link to this heading")

The [`jvp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jvp.html#torch.func.jvp "torch.func.jvp")
 transforms computes Jacobian-vector-products and is also known as “forward-mode AD”. It is not a higher-order function unlike most other transforms, but it returns the outputs of `func(inputs)` as well as the jvps.

from torch.func import jvp
x \= torch.randn(5)
y \= torch.randn(5)
f \= lambda x, y: (x \* y)
\_, out\_tangent \= jvp(f, (x, y), (torch.ones(5), torch.ones(5)))
assert torch.allclose(out\_tangent, x + y)

Copy to clipboard

### [`jacrev()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacrev.html#torch.func.jacrev "torch.func.jacrev")
, [`jacfwd()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacfwd.html#torch.func.jacfwd "torch.func.jacfwd")
, and [`hessian()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.hessian.html#torch.func.hessian "torch.func.hessian")
[#](https://docs.pytorch.org/docs/2.15/func.whirlwind_tour.html#jacrev-jacfwd-and-hessian "Link to this heading")

The [`jacrev()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacrev.html#torch.func.jacrev "torch.func.jacrev")
 transform returns a new function that takes in `x` and returns the Jacobian of the function with respect to `x` using reverse-mode AD.

from torch.func import jacrev
x \= torch.randn(5)
jacobian \= jacrev(torch.sin)(x)
expected \= torch.diag(torch.cos(x))
assert torch.allclose(jacobian, expected)

Copy to clipboard

[`jacrev()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacrev.html#torch.func.jacrev "torch.func.jacrev")
 can be composed with [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vmap.html#torch.func.vmap "torch.func.vmap")
 to produce batched jacobians:

x \= torch.randn(64, 5)
jacobian \= vmap(jacrev(torch.sin))(x)
assert jacobian.shape \== (64, 5, 5)

Copy to clipboard

[`jacfwd()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacfwd.html#torch.func.jacfwd "torch.func.jacfwd")
 is a drop-in replacement for jacrev that computes Jacobians using forward-mode AD:

from torch.func import jacfwd
x \= torch.randn(5)
jacobian \= jacfwd(torch.sin)(x)
expected \= torch.diag(torch.cos(x))
assert torch.allclose(jacobian, expected)

Copy to clipboard

Composing [`jacrev()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacrev.html#torch.func.jacrev "torch.func.jacrev")
 with itself or [`jacfwd()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacfwd.html#torch.func.jacfwd "torch.func.jacfwd")
 can produce hessians:

def f(x):
    return x.sin().sum()

x \= torch.randn(5)
hessian0 \= jacrev(jacrev(f))(x)
hessian1 \= jacfwd(jacrev(f))(x)

Copy to clipboard

[`hessian()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.hessian.html#torch.func.hessian "torch.func.hessian")
 is a convenience function that combines jacfwd and jacrev:

from torch.func import hessian

def f(x):
    return x.sin().sum()

x \= torch.randn(5)
hess \= hessian(f)(x)

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/func.whirlwind_tour.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/func.whirlwind_tour.md.txt)

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