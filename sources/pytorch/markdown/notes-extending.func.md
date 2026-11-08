Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/notes/extending.func.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/notes/extending.func.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/notes/extending.func.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/notes/extending.func.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/notes/extending.func.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/notes/extending.func.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/notes/extending.func.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/notes/extending.func.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/notes/extending.func.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/notes/extending.func.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/notes/extending.func.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/notes/extending.func.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/notes/extending.func.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/notes/extending.func.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/notes/extending.func.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/notes/extending.func.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/notes/extending.func.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/notes/extending.func.html)
[v1.13](https://docs.pytorch.org/docs/1.13/notes/extending.func.html)
[v1.12](https://docs.pytorch.org/docs/1.12/notes/extending.func.html)
[v1.11](https://docs.pytorch.org/docs/1.11/notes/extending.func.html)
[v1.10](https://docs.pytorch.org/docs/1.10/notes/extending.func.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/notes/extending.func.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/notes/extending.func.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/notes/extending.func.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/notes/extending.func.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/notes/extending.func.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/notes/extending.func.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/notes/extending.func.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/notes/extending.func.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/notes/extending.func.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/notes/extending.func.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/notes/extending.func.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/notes/extending.func.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/notes/extending.func.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/notes/extending.func.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/notes/extending.func.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/notes/extending.func.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/notes/extending.func.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/notes/extending.func.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/notes/extending.func.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/notes/extending.func.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/notes/extending.func.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/notes/extending.func.html)

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

Extending torch.func with autograd.Function[#](https://docs.pytorch.org/docs/2.15/notes/extending.func.html#extending-torch-func-with-autograd-function "Link to this heading")

================================================================================================================================================================================

Created On: May 06, 2026 | Last Updated On: May 06, 2026

So you’d like to use [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
 with the [`torch.func`](https://docs.pytorch.org/docs/2.15/func.api.html#module-torch.func "torch.func")
 transforms like [`torch.vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
, [`torch.func.grad()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.grad.html#torch.func.grad "torch.func.grad")
, etc.

There are two main use cases:

*   you wish to call code that does not contain PyTorch operations and have it work with function transforms. That is, the [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
    ’s forward/backward/etc calls into functions from other systems like C++, CUDA, numpy.
    
*   you wish to specify custom gradient rules, like JAX’s [custom\_vjp/custom\_jvp](https://jax.readthedocs.io/en/latest/notebooks/Custom_derivative_rules_for_Python_code.html)
    

PyTorch combines both of these concepts into [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
.

Basic Usage[#](https://docs.pytorch.org/docs/2.15/notes/extending.func.html#basic-usage "Link to this heading")

----------------------------------------------------------------------------------------------------------------

This guide assumes you are familiar with [Extending torch.autograd](https://docs.pytorch.org/docs/2.15/notes/extending.html#extending-autograd)
, which explains how to use [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
.

[`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
 can either have a [`forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.forward.html#torch.autograd.Function.forward "torch.autograd.Function.forward")
 that accepts a ctx object, or it can have separate [`forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.forward.html#torch.autograd.Function.forward "torch.autograd.Function.forward")
 (that does not accept `ctx`) and a `setup_context()` staticmethod that modifies the `ctx` object.

Only the latter is supported with function transforms:

*   [`forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.forward.html#torch.autograd.Function.forward "torch.autograd.Function.forward")
     is the code that performs the operation and it should not accept a `ctx` object.
    
*   `setup_context(ctx, inputs, output)` is the code where you can call methods on `ctx`. Here is where you should save Tensors for backward (by calling `ctx.save_for_backward(*tensors)`), or save non-Tensors (by assigning them to the `ctx` object).
    

Because `setup_context()` accepts only `inputs` and `output`, the only quantities that can be saved are either objects (such as Tensors) in the inputs or outputs or quantities (like `Tensor.shape`) derived from them. If you wish to save a non-input intermediate activation from [`Function.forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.forward.html#torch.autograd.Function.forward "torch.autograd.Function.forward")
 for backward, then you’ll need to return it as an output from [`forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.forward.html#torch.autograd.Function.forward "torch.autograd.Function.forward")
 so that it gets passed to `setup_context()`.

Depending on the transform,

*   to support reverse-mode AD ([`torch.func.grad()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.grad.html#torch.func.grad "torch.func.grad")
    , [`torch.func.vjp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vjp.html#torch.func.vjp "torch.func.vjp")
    ), the [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
     needs a [`backward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.backward.html#torch.autograd.Function.backward "torch.autograd.Function.backward")
     staticmethod.
    
*   to support [`torch.vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
    , the [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
     needs a [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.vmap.html#torch.autograd.Function.vmap "torch.autograd.Function.vmap")
     staticmethod.
    
*   to support [`torch.func.jvp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jvp.html#torch.func.jvp "torch.func.jvp")
    , the [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
     needs a [`jvp()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.jvp.html#torch.autograd.Function.jvp "torch.autograd.Function.jvp")
     staticmethod.
    
*   to support compositions of transforms (like [`torch.func.jacrev()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacrev.html#torch.func.jacrev "torch.func.jacrev")
    , [`torch.func.jacfwd()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacfwd.html#torch.func.jacfwd "torch.func.jacfwd")
    , [`torch.func.hessian()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.hessian.html#torch.func.hessian "torch.func.hessian")
    ) – you may need multiple of the above.
    

In order for the [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
 to be arbitrarily composable with function transforms, we recommend that all other staticmethods other than [`forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.forward.html#torch.autograd.Function.forward "torch.autograd.Function.forward")
 and `setup_context()` must be transformable: that is, they must consist of only PyTorch operators or call other [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
 (that may call into C++/CUDA/etc).

Let’s go over some examples of common use cases.

### Example 1: autograd.Function calls into another system[#](https://docs.pytorch.org/docs/2.15/notes/extending.func.html#example-1-autograd-function-calls-into-another-system "Link to this heading")

A common case is a [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
 with both forward() and backward() calling into another system (like C++, CUDA, numpy, triton).

import torch
import numpy as np

def to\_numpy(tensor):
    return tensor.cpu().numpy()

class NumpySort(torch.autograd.Function):
    \# Note that forward does not take ctx
    @staticmethod
    def forward(x, dim):
        device \= x.device
        x \= to\_numpy(x)
        ind \= np.argsort(x, axis\=dim)
        ind\_inv \= np.argsort(ind, axis\=dim)
        result \= np.take\_along\_axis(x, ind, axis\=dim)
        \# Any intermediates to be saved in backward must be returned as
        \# outputs.
        return (
            \# The desired output
            torch.tensor(result, device\=device),
            \# intermediate to save for backward
            torch.tensor(ind, device\=device),
            \# intermediate to save for backward
            torch.tensor(ind\_inv, device\=device),
        )

    \# setup\_context is responsible for calling methods and/or assigning to
    \# the ctx object. Please do not do additional compute (e.g. add
    \# Tensors together) in setup\_context.
    @staticmethod
    def setup\_context(ctx, inputs, output):
        x, dim \= inputs
        \# Note that output is whatever you returned from forward.
        \# If you returned multiple values, then output is a Tuple of multiple values.
        \# If you returned a single Tensor, then output is a Tensor.
        \# If you returned a Tuple with a single Tensor, then output is a
        \# Tuple with a single Tensor.
        \_, ind, ind\_inv \= output
        ctx.mark\_non\_differentiable(ind, ind\_inv)
        \# Tensors must be saved via ctx.save\_for\_backward. Please do not
        \# assign them directly onto the ctx object.
        ctx.save\_for\_backward(ind, ind\_inv)
        \# Non-tensors may be saved by assigning them as attributes on the ctx object.
        ctx.dim \= dim

    @staticmethod
    def backward(ctx, grad\_output, \_0, \_1):
        \# For the autograd.Function to be arbitrarily composable with function
        \# transforms, all staticmethod other than forward and setup\_context
        \# must be implemented in a "transformable" way; that is, they must
        \# only consist of PyTorch operations or autograd.Function.
        #
        \# For example, this allows us to do double backwards and/or compute
        \# second order gradients.
        #
        \# We've written the backward pass of NumpySort in terms of another
        \# autograd.Function, NumpyTake.
        ind, ind\_inv \= ctx.saved\_tensors
        return NumpyTake.apply(grad\_output, ind\_inv, ind, ctx.dim), None

class NumpyTake(torch.autograd.Function):
    @staticmethod
    def forward(x, ind, ind\_inv, dim):
        device \= x.device
        x \= to\_numpy(x)
        ind \= to\_numpy(ind)
        return torch.tensor(np.take\_along\_axis(x, ind, dim), device\=device)

    @staticmethod
    def setup\_context(ctx, inputs, output):
        x, ind, ind\_inv, dim \= inputs
        ctx.save\_for\_backward(ind, ind\_inv)
        ctx.dim \= dim

    @staticmethod
    def backward(ctx, grad\_output):
        ind, ind\_inv \= ctx.saved\_tensors
        result \= NumpyTake.apply(grad\_output, ind\_inv, ind, ctx.dim)
        return result, None, None, None

Copy to clipboard

Now, to make it easier to use `NumpySort` (to hide away the intermediates we returned as outputs, as well as allow default args and kwargs), we create a new function that invokes it:

def numpy\_sort(x, dim\=-1):
    result, \_, \_ \= NumpySort.apply(x, dim)
    return result

Copy to clipboard

And here’s a sanity check:

x \= torch.randn(2, 3)
grad\_x \= torch.func.grad(lambda x: numpy\_sort(x).sum())(x)
assert torch.allclose(grad\_x, torch.ones\_like(x))

Copy to clipboard

### Example 2: autograd.Function specifies custom gradient rules[#](https://docs.pytorch.org/docs/2.15/notes/extending.func.html#example-2-autograd-function-specifies-custom-gradient-rules "Link to this heading")

Another common case is an [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
 that is implemented with PyTorch operations. PyTorch is able to compute gradients for PyTorch operations automatically, but perhaps we wish to customize how the gradients are computed. Some reasons why we may want a custom backward different from the one PyTorch gives us are:

*   improving numeric stability
    
*   changing the performance characteristics of the backward
    
*   changing how edge cases are handled (e.g. nans, inf)
    
*   modifying the gradient (e.g. gradient clipping)
    

Here’s an example of an [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
 for the function `y = x ** 3` where we change the performance characteristics (some computation that would normally happen during the backward pass, computing dx, happens in the forward pass).

class MyCube(torch.autograd.Function):
    @staticmethod
    def forward(x):
        result \= x \*\* 3
        \# In regular PyTorch, if we had just run y = x \*\* 3, then the backward
        \# pass computes dx = 3 \* x \*\* 2. In this autograd.Function, we've done
        \# that computation here in the forward pass instead.
        dx \= 3 \* x \*\* 2
        return result, dx

    @staticmethod
    def setup\_context(ctx, inputs, output):
        x, \= inputs
        result, dx \= output
        ctx.save\_for\_backward(x, dx)

    @staticmethod
    def backward(ctx, grad\_output, grad\_dx):
        x, dx \= ctx.saved\_tensors
        \# In order for the autograd.Function to work with higher-order
        \# gradients, we must add the gradient contribution of \`dx\`.
        result \= grad\_output \* dx + grad\_dx \* 6 \* x
        return result

Copy to clipboard

Now, to make it easier to use `NumpySort` (and hide away the intermediates we returned as outputs) we create a new function that invokes it:

def my\_cube(x):
    result, \_ \= MyCube.apply(x)
    return result

Copy to clipboard

Here’s a sanity check computing the second-order gradients:

x \= torch.randn(\[\])
ggx \= torch.func.grad(torch.func.grad(my\_cube))(x)
assert torch.allclose(ggx, 6 \* x)

Copy to clipboard

### Limitations and gotchas[#](https://docs.pytorch.org/docs/2.15/notes/extending.func.html#limitations-and-gotchas "Link to this heading")

Warning

Please read these limitations of [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
 with torch.func transforms carefully. We are not able to catch many of these situations and error out gracefully so they will lead to undefined behavior.

Please do not capture Tensors that are being transformed over, have requires\_grad=True, or are dual tensors, into the methods of the [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
. The way to be completely safe is to ensure that the only Tensors being used inside any method of the [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
 must be directly passed as inputs (or via the ctx object) rather than come from outside the [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
.

[`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
 does not handle Tensors in pytrees (arbitrary nested Python data structures that may or may not contain Tensors). For those Tensors to be tracked by autograd, they must be passed directly as an argument to [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
. This is in contrast to jax.{custom\_vjp, custom\_jvp}, which do accept pytrees.

Please only use [`save_for_backward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.function.FunctionCtx.save_for_backward.html#torch.autograd.function.FunctionCtx.save_for_backward "torch.autograd.function.FunctionCtx.save_for_backward")
 or `save_for_forward()` to save Tensors. Please do not assign Tensors or collections of Tensors directly onto the ctx object - these Tensors will not get tracked

[`torch.vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
 Support[#](https://docs.pytorch.org/docs/2.15/notes/extending.func.html#torch-vmap-support "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To use an [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
 with [`torch.vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
, you must either:

*   provide a [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.vmap.html#torch.autograd.Function.vmap "torch.autograd.Function.vmap")
     staticmethod that tells us the behavior of the [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
     under [`torch.vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
    
*   ask us to autogenerate it by setting `generate_vmap_rule=True`.
    

### Automatically generate a vmap rule[#](https://docs.pytorch.org/docs/2.15/notes/extending.func.html#automatically-generate-a-vmap-rule "Link to this heading")

If your [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
 fulfills the following additional constraints, then we are able to generate a vmap rule for it. If it doesn’t fulfill the constraints or if you want custom behavior under vmap, please manually define a vmap staticmethod (see next section).

Warning

We are not easily able to check for the following constraints and error out gracefully. Violation of the constraints may lead to undefined behavior.

*   The [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
    ’s [`forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.forward.html#torch.autograd.Function.forward "torch.autograd.Function.forward")
    , [`backward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.backward.html#torch.autograd.Function.backward "torch.autograd.Function.backward")
     (if it exists) and [`jvp()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.jvp.html#torch.autograd.Function.jvp "torch.autograd.Function.jvp")
     (if it exists) staticmethods must be transformable via [`torch.vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
    . That is, they must consist of only PyTorch operations (as opposed to e.g. NumPy or custom CUDA kernels).
    

Example:

class MyCube(torch.autograd.Function):
    \# Set generate\_vmap\_rule to True to ask PyTorch to automatically generate
    \# a vmap rule.
    generate\_vmap\_rule \= True

    @staticmethod
    def forward(x):
        result \= x \*\* 3
        dx \= 3 \* x \*\* 2
        return result, dx

    @staticmethod
    def setup\_context(ctx, inputs, output):
        x, \= inputs
        result, dx \= output
        ctx.save\_for\_backward(x, dx)

    @staticmethod
    def backward(ctx, grad\_output, grad\_dx):
        x, dx \= ctx.saved\_tensors
        result \= grad\_output \* dx + grad\_dx \* 6 \* x
        return result

def my\_cube(x):
    result, dx \= MyCube.apply(x)
    return result

x \= torch.randn(3)
result \= torch.vmap(my\_cube)(x)
assert torch.allclose(result, x \*\* 3)

Copy to clipboard

### Defining the vmap staticmethod[#](https://docs.pytorch.org/docs/2.15/notes/extending.func.html#defining-the-vmap-staticmethod "Link to this heading")

If your [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
 calls into another system (like NumPy, C++, CUDA, triton), then to get it to work with [`torch.vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
 or transforms that use it, you’ll need to manually define a [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.vmap.html#torch.autograd.Function.vmap "torch.autograd.Function.vmap")
 staticmethod.

Depending on what transforms you want to use and your use case, you may not need to add a [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.vmap.html#torch.autograd.Function.vmap "torch.autograd.Function.vmap")
 staticmethod to all of your [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
:

*   For example, [`torch.func.jacrev()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacrev.html#torch.func.jacrev "torch.func.jacrev")
     performs [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
     over the backward pass. So if you’re only interested in using [`torch.func.jacrev()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacrev.html#torch.func.jacrev "torch.func.jacrev")
    , only the [`backward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.backward.html#torch.autograd.Function.backward "torch.autograd.Function.backward")
     staticmethod needs to be vmappable.
    

We do recommend ensuring all of your [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
 have support for [`torch.vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
 though, especially if you are writing a third-party library and you want your [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
 to work with all combinations of [`torch.func()`](https://docs.pytorch.org/docs/2.15/func.api.html#module-torch.func "torch.func")
 transforms.

Conceptually, the vmap staticmethod is responsible for defining how the [`forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.forward.html#torch.autograd.Function.forward "torch.autograd.Function.forward")
 should behave under [`torch.vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
. That is, it defines how to transform the [`forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.forward.html#torch.autograd.Function.forward "torch.autograd.Function.forward")
 to run over inputs with an additional dimension (the dimension being vmapped over). This is similar to how [`torch.vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
 is implemented over PyTorch operations: for each operation, we define a vmap rule (sometimes also referred to as a “batching rule”).

Here’s how to define the [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.vmap.html#torch.autograd.Function.vmap "torch.autograd.Function.vmap")
 staticmethod:

*   the signature is `vmap(info, in_dims: Tuple[Optional[int]], *args)`, where `*args` is the same as the args to [`forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.forward.html#torch.autograd.Function.forward "torch.autograd.Function.forward")
    .
    
*   The vmap staticmethod is responsible for defining how the [`forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.forward.html#torch.autograd.Function.forward "torch.autograd.Function.forward")
     should behave under [`torch.vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
    . That is, given inputs with an additional dimension (specified by `in_dims`), how do we compute the batched version of [`forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.forward.html#torch.autograd.Function.forward "torch.autograd.Function.forward")
    ?
    
*   For each arg in `args`, `in_dims` has a corresponding `Optional[int]`. It is `None` if the arg is not a Tensor or if the arg is not being vmapped over, otherwise, it is an integer specifying what dimension of the Tensor is being vmapped over.
    
*   `info` is a collection of additional metadata that may be helpful: `info.batch_size` specifies the size of the dimension being vmapped over, while `info.randomness` is the `randomness` option that was passed to [`torch.vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
    .
    
*   The return of the vmap staticmethod is a tuple of `(output, out_dims)`. Similar to `in_dims`, `out_dims` should be of the same structure as `output` and contain one `out_dim` per output that specifies if the output has the vmapped dimension and what index it is in.
    

Example:

def to\_numpy(tensor):
    return tensor.cpu().numpy()

class NumpySort(torch.autograd.Function):
    @staticmethod
    def forward(x, dim):
        device \= x.device
        x \= to\_numpy(x)
        ind \= np.argsort(x, axis\=dim)
        ind\_inv \= np.argsort(ind, axis\=dim)
        result \= np.take\_along\_axis(x, ind, axis\=dim)
        return (
            torch.tensor(result, device\=device),
            torch.tensor(ind, device\=device),
            torch.tensor(ind\_inv, device\=device),
        )

    @staticmethod
    def setup\_context(ctx, inputs, output):
        x, dim \= inputs
        \_, ind, ind\_inv \= output
        ctx.mark\_non\_differentiable(ind, ind\_inv)
        ctx.save\_for\_backward(ind, ind\_inv)
        ctx.dim \= dim

    @staticmethod
    def backward(ctx, grad\_output, \_0, \_1):
        ind, ind\_inv \= ctx.saved\_tensors
        return NumpyTake.apply(grad\_output, ind\_inv, ind, ctx.dim), None

    \# The signature of the vmap staticmethod is:
    \# vmap(info, in\_dims: Tuple\[Optional\[int\]\], \*args)
    \# where \*args is the same as the arguments to \`forward\`.
    @staticmethod
    def vmap(info, in\_dims, x, dim):
        \# For every input (x and dim), in\_dims stores an Optional\[int\]
        \# that is:
        \# - None if the input is not being vmapped over or if the input
        \#   is not a Tensor
        \# - an integer if the input is being vmapped over that represents
        \#   the index of the dimension being vmapped over.
        x\_bdim, \_ \= in\_dims

        \# A "vmap rule" is the logic of how to perform the operation given
        \# inputs with one additional dimension. In NumpySort, x has an
        \# additional dimension (x\_bdim). The vmap rule is simply
        \# to call NumpySort again but pass it a different \`dim\`.
        x \= x.movedim(x\_bdim, 0)
        \# Handle negative dims correctly
        dim \= dim if dim \>= 0 else dim + x.dim() \- 1
        result \= NumpySort.apply(x, dim + 1)

        \# The vmap rule must return a tuple of two things
        \# 1. the output. Should be the same amount of things
        \#    as returned by the forward().
        \# 2. one Optional\[int\] for each output specifying if each output
        \# is being vmapped over, and if so, the index of the
        \# dimension being vmapped over.
        #
        \# NumpySort.forward returns a Tuple of 3 Tensors. Since we moved the
        \# dimension being vmapped over to the front of \`x\`, that appears at
        \# dimension 0 of all outputs.
        \# The return is (output, out\_dims) -- output is a tuple of 3 Tensors
        \# and out\_dims is a Tuple of 3 Optional\[int\]
        return NumpySort.apply(x, dim + 1), (0, 0, 0)

class NumpyTake(torch.autograd.Function):
    @staticmethod
    def forward(x, ind, ind\_inv, dim):
        device \= x.device
        x \= to\_numpy(x)
        ind \= to\_numpy(ind)
        return torch.tensor(np.take\_along\_axis(x, ind, dim), device\=device)

    @staticmethod
    def setup\_context(ctx, inputs, output):
        x, ind, ind\_inv, dim \= inputs
        ctx.save\_for\_backward(ind, ind\_inv)
        ctx.dim \= dim

    @staticmethod
    def backward(ctx, grad\_output):
        ind, ind\_inv \= ctx.saved\_tensors
        result \= NumpyTake.apply(grad\_output, ind\_inv, ind, ctx.dim)
        return result, None, None, None

    @staticmethod
    def vmap(info, in\_dims, x, ind, ind\_inv, dim):
        x\_bdim, ind\_bdim, ind\_inv\_bdim, \_ \= in\_dims

        \# The strategy is: expand {x, ind, ind\_inv} to all have the dimension
        \# being vmapped over.
        \# Then, call back into NumpyTake(expanded\_x, expanded\_ind, expanded\_ind\_inv, new\_dim).

        \# Handle negative dims by wrapping them to be positive
        logical\_dim \= x.dim() if x\_bdim is None else x\_bdim \- 1
        dim \= dim if dim \>= 0 else dim + logical\_dim

        def maybe\_expand\_bdim\_at\_front(x, x\_bdim):
            if x\_bdim is None:
                return x.expand(info.batch\_size, \*x.shape)
            return x.movedim(x\_bdim, 0)

        \# If the Tensor doesn't have the dimension being vmapped over,
        \# expand it out. Otherwise, move it to the front of the Tensor
        x \= maybe\_expand\_bdim\_at\_front(x, x\_bdim)
        ind \= maybe\_expand\_bdim\_at\_front(ind, ind\_bdim)
        ind\_inv \= maybe\_expand\_bdim\_at\_front(ind\_inv, ind\_inv\_bdim)

        \# The return is a tuple (output, out\_dims). Since output is a Tensor,
        \# then out\_dims is an Optional\[int\] (instead of being a Tuple).
        return NumpyTake.apply(x, ind, ind\_inv, dim + 1), 0

def numpy\_sort(x, dim\=-1):
    result, \_, \_ \= NumpySort.apply(x, dim)
    return result

x \= torch.randn(2, 3)
result \= torch.vmap(numpy\_sort)(x)
assert torch.allclose(result, numpy\_sort(result, 1))

Copy to clipboard

Note

The vmap staticmethod should aim to preserve the semantics of the entire [`Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
. That is, (pseudocode) `grad(vmap(MyFunc))` should be replaceable with a `grad(map(MyFunc))`.

If your autograd.Function has any custom behavior in the backward pass, please keep this in mind.

Note

It is a legitimate use case to write a custom vmap staticmethod for a [`Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
 that PyTorch is able to generate a vmap rule for via `generate_vmap_rule=True`. You may wish to do this if the generated vmap rule doesn’t have the semantics you’re looking for.

[`torch.func.jvp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jvp.html#torch.func.jvp "torch.func.jvp")
 Support[#](https://docs.pytorch.org/docs/2.15/notes/extending.func.html#torch-func-jvp-support "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To support forward-mode AD, a [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
 must have a [`jvp()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.jvp.html#torch.autograd.Function.jvp "torch.autograd.Function.jvp")
 staticmethod. Please see [Forward mode AD](https://docs.pytorch.org/docs/2.15/notes/extending.html#forward-ad-autograd-function)
 for details.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/notes/extending.func.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/notes/extending.func.md.txt)

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