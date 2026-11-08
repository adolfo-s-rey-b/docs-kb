Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/func.ux_limitations.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/func.ux_limitations.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/func.ux_limitations.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/func.ux_limitations.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/func.ux_limitations.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/func.ux_limitations.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/func.ux_limitations.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/func.ux_limitations.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/func.ux_limitations.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/func.ux_limitations.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/func.ux_limitations.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/func.ux_limitations.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/func.ux_limitations.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/func.ux_limitations.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/func.ux_limitations.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/func.ux_limitations.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/func.ux_limitations.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/func.ux_limitations.html)
[v1.13](https://docs.pytorch.org/docs/1.13/func.ux_limitations.html)
[v1.12](https://docs.pytorch.org/docs/1.12/func.ux_limitations.html)
[v1.11](https://docs.pytorch.org/docs/1.11/func.ux_limitations.html)
[v1.10](https://docs.pytorch.org/docs/1.10/func.ux_limitations.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/func.ux_limitations.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/func.ux_limitations.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/func.ux_limitations.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/func.ux_limitations.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/func.ux_limitations.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/func.ux_limitations.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/func.ux_limitations.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/func.ux_limitations.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/func.ux_limitations.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/func.ux_limitations.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/func.ux_limitations.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/func.ux_limitations.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/func.ux_limitations.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/func.ux_limitations.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/func.ux_limitations.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/func.ux_limitations.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/func.ux_limitations.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/func.ux_limitations.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/func.ux_limitations.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/func.ux_limitations.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/func.ux_limitations.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/func.ux_limitations.html)

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

UX Limitations[#](https://docs.pytorch.org/docs/2.15/func.ux_limitations.html#ux-limitations "Link to this heading")

=====================================================================================================================

Created On: Jun 12, 2025 | Last Updated On: Jun 12, 2025

torch.func, like [JAX](https://github.com/google/jax)
, has restrictions around what can be transformed. In general, JAX’s limitations are that transforms only work with pure functions: that is, functions where the output is completely determined by the input and that do not involve side effects (like mutation).

We have a similar guarantee: our transforms work well with pure functions. However, we do support certain in-place operations. On one hand, writing code compatible with function transforms may involve changing how you write PyTorch code, on the other hand, you may find that our transforms let you express things that were previously difficult to express in PyTorch.

General limitations[#](https://docs.pytorch.org/docs/2.15/func.ux_limitations.html#general-limitations "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

All torch.func transforms share a limitation in that a function should not assign to global variables. Instead, all outputs to a function must be returned from the function. This restriction comes from how torch.func is implemented: each transform wraps Tensor inputs in special torch.func Tensor subclasses that facilitate the transform.

So, instead of the following:

import torch
from torch.func import grad

\# Don't do this
intermediate \= None

def f(x):
  global intermediate
  intermediate \= x.sin()
  z \= intermediate.sin()
  return z

x \= torch.randn(\[\])
grad\_x \= grad(f)(x)

Copy to clipboard

Please rewrite `f` to return `intermediate`:

def f(x):
  intermediate \= x.sin()
  z \= intermediate.sin()
  return z, intermediate

grad\_x, intermediate \= grad(f, has\_aux\=True)(x)

Copy to clipboard

torch.autograd APIs[#](https://docs.pytorch.org/docs/2.15/func.ux_limitations.html#torch-autograd-apis "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

If you are trying to use a `torch.autograd` API like `torch.autograd.grad` or `torch.autograd.backward` inside of a function being transformed by [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vmap.html#torch.func.vmap "torch.func.vmap")
 or one of torch.func’s AD transforms ([`vjp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vjp.html#torch.func.vjp "torch.func.vjp")
, [`jvp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jvp.html#torch.func.jvp "torch.func.jvp")
, [`jacrev()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacrev.html#torch.func.jacrev "torch.func.jacrev")
, [`jacfwd()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacfwd.html#torch.func.jacfwd "torch.func.jacfwd")
), the transform may not be able to transform over it. If it is unable to do so, you’ll receive an error message.

This is a fundamental design limitation in how PyTorch’s AD support is implemented and the reason why we designed the torch.func library. Please instead use the torch.func equivalents of the `torch.autograd` APIs:

*   `torch.autograd.grad`, `Tensor.backward` -> `torch.func.vjp` or `torch.func.grad`
    
*   `torch.autograd.functional.jvp` -> `torch.func.jvp`
    
*   `torch.autograd.functional.jacobian` -> `torch.func.jacrev` or `torch.func.jacfwd`
    
*   `torch.autograd.functional.hessian` -> `torch.func.hessian`
    

vmap limitations[#](https://docs.pytorch.org/docs/2.15/func.ux_limitations.html#vmap-limitations "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

Note

[`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vmap.html#torch.func.vmap "torch.func.vmap")
 is our most restrictive transform. The grad-related transforms ([`grad()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.grad.html#torch.func.grad "torch.func.grad")
, [`vjp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vjp.html#torch.func.vjp "torch.func.vjp")
, [`jvp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jvp.html#torch.func.jvp "torch.func.jvp")
) do not have these limitations. [`jacfwd()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacfwd.html#torch.func.jacfwd "torch.func.jacfwd")
 (and [`hessian()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.hessian.html#torch.func.hessian "torch.func.hessian")
, which is implemented with [`jacfwd()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacfwd.html#torch.func.jacfwd "torch.func.jacfwd")
) is a composition of [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vmap.html#torch.func.vmap "torch.func.vmap")
 and [`jvp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jvp.html#torch.func.jvp "torch.func.jvp")
 so it also has these limitations.

`vmap(func)` is a transform that returns a function that maps `func` over some new dimension of each input Tensor. The mental model for vmap is that it is like running a for-loop: for pure functions (i.e. in the absence of side effects), `vmap(f)(x)` is equivalent to:

torch.stack(\[f(x\_i) for x\_i in x.unbind(0)\])

Copy to clipboard

### Mutation: Arbitrary mutation of Python data structures[#](https://docs.pytorch.org/docs/2.15/func.ux_limitations.html#mutation-arbitrary-mutation-of-python-data-structures "Link to this heading")

In the presence of side effects, [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vmap.html#torch.func.vmap "torch.func.vmap")
 no longer acts like it is running a for-loop. For example, the following function:

def f(x, list):
  list.pop()
  print("hello!")
  return x.sum(0)

x \= torch.randn(3, 1)
lst \= \[0, 1, 2, 3\]

result \= vmap(f, in\_dims\=(0, None))(x, lst)

Copy to clipboard

will print “hello!” once and pop only one element from `lst`.

[`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vmap.html#torch.func.vmap "torch.func.vmap")
 executes `f` a single time, so all side effects only happen once.

This is a consequence of how vmap is implemented. torch.func has a special, internal BatchedTensor class. `vmap(f)(*inputs)` takes all Tensor inputs, turns them into BatchedTensors, and calls `f(*batched_tensor_inputs)`. BatchedTensor overrides the PyTorch API to produce batched (i.e. vectorized) behavior for each PyTorch operator.

### Mutation: in-place PyTorch Operations[#](https://docs.pytorch.org/docs/2.15/func.ux_limitations.html#mutation-in-place-pytorch-operations "Link to this heading")

You might be here due to receiving an error about vmap-incompatible in-place operations. [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vmap.html#torch.func.vmap "torch.func.vmap")
 will raise an error if it encounters an unsupported PyTorch in-place operation and it will succeed otherwise. Unsupported operations are those that would cause a Tensor with more elements to be written to a Tensor with fewer elements. Here’s an example of how this can occur:

def f(x, y):
  x.add\_(y)
  return x

x \= torch.randn(1)
y \= torch.randn(3, 1)  \# When vmapped over, looks like it has shape \[1\]

\# Raises an error because \`x\` has fewer elements than \`y\`.
vmap(f, in\_dims\=(None, 0))(x, y)

Copy to clipboard

`x` is a Tensor with one element, `y` is a Tensor with three elements. `x + y` has three elements (due to broadcasting), but attempting to write three elements back into `x`, which only has one element, raises an error due to attempting to write three elements into a Tensor with a single element.

There is no problem if the Tensor being written to is batched under [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
 (i.e. it is being vmapped over).

def f(x, y):
  x.add\_(y)
  return x

x \= torch.randn(3, 1)
y \= torch.randn(3, 1)
expected \= x + y

\# Does not raise an error because x is being vmapped over.
vmap(f, in\_dims\=(0, 0))(x, y)
assert torch.allclose(x, expected)

Copy to clipboard

One common fix for this is to replace calls to factory functions with their “new\_\*” equivalent. For example:

*   Replace [`torch.zeros()`](https://docs.pytorch.org/docs/2.15/generated/torch.zeros.html#torch.zeros "torch.zeros")
     with `Tensor.new_zeros()`
    
*   Replace [`torch.empty()`](https://docs.pytorch.org/docs/2.15/generated/torch.empty.html#torch.empty "torch.empty")
     with `Tensor.new_empty()`
    

To see why this helps, consider the following.

def diag\_embed(vec):
  assert vec.dim() \== 1
  result \= torch.zeros(vec.shape\[0\], vec.shape\[0\])
  result.diagonal().copy\_(vec)
  return result

vecs \= torch.tensor(\[\[0., 1, 2\], \[3., 4, 5\]\])

\# RuntimeError: vmap: inplace arithmetic(self, \*extra\_args) is not possible ...
vmap(diag\_embed)(vecs)

Copy to clipboard

Inside of [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
, `result` is a Tensor of shape \[3, 3\]. However, although `vec` looks like it has shape \[3\], `vec` actually has underlying shape \[2, 3\]. It is not possible to copy `vec` into `result.diagonal()`, which has shape \[3\], because it has too many elements.

def diag\_embed(vec):
  assert vec.dim() \== 1
  result \= vec.new\_zeros(vec.shape\[0\], vec.shape\[0\])
  result.diagonal().copy\_(vec)
  return result

vecs \= torch.tensor(\[\[0., 1, 2\], \[3., 4, 5\]\])
vmap(diag\_embed)(vecs)

Copy to clipboard

Replacing [`torch.zeros()`](https://docs.pytorch.org/docs/2.15/generated/torch.zeros.html#torch.zeros "torch.zeros")
 with `Tensor.new_zeros()` makes it so that `result` has an underlying Tensor of shape \[2, 3, 3\], so it is now possible to copy `vec`, which has underlying shape \[2, 3\], into `result.diagonal()`.

### Mutation: out= PyTorch Operations[#](https://docs.pytorch.org/docs/2.15/func.ux_limitations.html#mutation-out-pytorch-operations "Link to this heading")

[`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vmap.html#torch.func.vmap "torch.func.vmap")
 doesn’t support the `out=` keyword argument in PyTorch operations. It will error out gracefully if it encounters that in your code.

This is not a fundamental limitation; we could theoretically support this in the future but we have chosen not to for now.

### Data-dependent Python control flow[#](https://docs.pytorch.org/docs/2.15/func.ux_limitations.html#data-dependent-python-control-flow "Link to this heading")

We don’t yet support `vmap` over data-dependent control flow. Data-dependent control flow is when the condition of an if-statement, while-loop, or for-loop is a Tensor that is being `vmap`’ed over. For example, the following will raise an error message:

def relu(x):
  if x \> 0:
    return x
  return 0

x \= torch.randn(3)
vmap(relu)(x)

Copy to clipboard

However, any control flow that is not dependent on the values in `vmap`’ed tensors will work:

def custom\_dot(x):
  if x.dim() \== 1:
    return torch.dot(x, x)
  return (x \* x).sum()

x \= torch.randn(3)
vmap(custom\_dot)(x)

Copy to clipboard

JAX supports transforming over [data-dependent control flow](https://jax.readthedocs.io/en/latest/jax.lax.html#control-flow-operators)
 using special control flow operators (e.g. `jax.lax.cond`, `jax.lax.while_loop`). We’re investigating adding equivalents of those to PyTorch.

### Data-dependent operations (.item())[#](https://docs.pytorch.org/docs/2.15/func.ux_limitations.html#data-dependent-operations-item "Link to this heading")

We do not (and will not) support vmap over a user-defined function that calls `.item()` on a Tensor. For example, the following will raise an error message:

def f(x):
  return x.item()

x \= torch.randn(3)
vmap(f)(x)

Copy to clipboard

Please try to rewrite your code to not use `.item()` calls.

You may also encounter an error message about using `.item()` but you might not have used it. In those cases, it is possible that PyTorch internally is calling `.item()` – please file an issue on GitHub and we’ll fix PyTorch internals.

### Dynamic shape operations (nonzero and friends)[#](https://docs.pytorch.org/docs/2.15/func.ux_limitations.html#dynamic-shape-operations-nonzero-and-friends "Link to this heading")

`vmap(f)` requires that `f` applied to every “example” in your input returns a Tensor with the same shape. Operations such as `torch.nonzero`, `torch.is_nonzero` are not supported and will error as a result.

To see why, consider the following example:

xs \= torch.tensor(\[\[0, 1, 2\], \[0, 0, 3\]\])
vmap(torch.nonzero)(xs)

Copy to clipboard

`torch.nonzero(xs[0])` returns a Tensor of shape 2; but `torch.nonzero(xs[1])` returns a Tensor of shape 1. We are unable to construct a single Tensor as an output; the output would need to be a ragged Tensor (and PyTorch does not yet have the concept of a ragged Tensor).

Randomness[#](https://docs.pytorch.org/docs/2.15/func.ux_limitations.html#randomness "Link to this heading")

-------------------------------------------------------------------------------------------------------------

The user’s intention when calling a random operation can be unclear. Specifically, some users may want the random behavior to be the same across batches while others may want it to differ across batches. To address this, `vmap` takes a randomness flag.

The flag can only be passed to vmap and can take on 3 values, “error,” “different,” or “same,” defaulting to error. Under “error” mode, any call to a random function will produce an error asking the user to use one of the other two flags based on their use case.

Under “different” randomness, elements in a batch produce different random values. For instance,

def add\_noise(x):
  y \= torch.randn(())  \# y will be different across the batch
  return x + y

x \= torch.ones(3)
result \= vmap(add\_noise, randomness\="different")(x)  \# we get 3 different values

Copy to clipboard

Under “same” randomness, elements in a batch produce same random values. For instance,

def add\_noise(x):
  y \= torch.randn(())  \# y will be the same across the batch
  return x + y

x \= torch.ones(3)
result \= vmap(add\_noise, randomness\="same")(x)  \# we get the same value, repeated 3 times

Copy to clipboard

Warning

Our system only determine the randomness behavior of PyTorch operators and cannot control the behavior of other libraries, like numpy. This is similar to JAX’s limitations with their solutions

Note

Multiple vmap calls using either type of supported randomness will not produce the same results. Like with standard PyTorch, a user can get randomness reproducibility through either using `torch.manual_seed()` outside of vmap or by using generators.

Note

Finally, our randomness differs from JAX because we aren’t using a stateless PRNG, in part because PyTorch doesn’t have full support for a stateless PRNG. Instead, we’ve introduced a flag system to allow for the most common forms of randomness that we see. If your use case does not fit these forms of randomness, please file an issue.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/func.ux_limitations.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/func.ux_limitations.md.txt)

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