Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/func.migrating.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/func.migrating.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/func.migrating.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/func.migrating.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/func.migrating.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/func.migrating.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/func.migrating.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/func.migrating.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/func.migrating.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/func.migrating.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/func.migrating.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/func.migrating.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/func.migrating.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/func.migrating.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/func.migrating.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/func.migrating.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/func.migrating.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/func.migrating.html)
[v1.13](https://docs.pytorch.org/docs/1.13/func.migrating.html)
[v1.12](https://docs.pytorch.org/docs/1.12/func.migrating.html)
[v1.11](https://docs.pytorch.org/docs/1.11/func.migrating.html)
[v1.10](https://docs.pytorch.org/docs/1.10/func.migrating.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/func.migrating.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/func.migrating.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/func.migrating.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/func.migrating.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/func.migrating.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/func.migrating.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/func.migrating.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/func.migrating.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/func.migrating.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/func.migrating.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/func.migrating.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/func.migrating.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/func.migrating.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/func.migrating.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/func.migrating.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/func.migrating.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/func.migrating.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/func.migrating.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/func.migrating.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/func.migrating.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/func.migrating.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/func.migrating.html)

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

Migrating from functorch to torch.func[#](https://docs.pytorch.org/docs/2.15/func.migrating.html#migrating-from-functorch-to-torch-func "Link to this heading")

================================================================================================================================================================

Created On: Jun 11, 2025 | Last Updated On: Jun 11, 2025

torch.func, previously known as “functorch”, is [JAX-like](https://github.com/google/jax)
 composable function transforms for PyTorch.

functorch started as an out-of-tree library over at the [pytorch/functorch](https://github.com/pytorch/functorch)
 repository. Our goal has always been to upstream functorch directly into PyTorch and provide it as a core PyTorch library.

As the final step of the upstream, we’ve decided to migrate from being a top level package (`functorch`) to being a part of PyTorch to reflect how the function transforms are integrated directly into PyTorch core. As of PyTorch 2.0, we are deprecating `import functorch` and ask that users migrate to the newest APIs, which we will maintain going forward. `import functorch` will be kept around to maintain backwards compatibility for a couple of releases.

function transforms[#](https://docs.pytorch.org/docs/2.15/func.migrating.html#function-transforms "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

The following APIs are a drop-in replacement for the following [functorch APIs](https://pytorch.org/functorch/1.13/functorch.html)
. They are fully backwards compatible.

| functorch API | PyTorch API (as of PyTorch 2.0) |
| --- | --- |
| functorch.vmap | [`torch.vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")<br> or [`torch.func.vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vmap.html#torch.func.vmap "torch.func.vmap") |
| functorch.grad | [`torch.func.grad()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.grad.html#torch.func.grad "torch.func.grad") |
| functorch.vjp | [`torch.func.vjp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vjp.html#torch.func.vjp "torch.func.vjp") |
| functorch.jvp | [`torch.func.jvp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jvp.html#torch.func.jvp "torch.func.jvp") |
| functorch.jacrev | [`torch.func.jacrev()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacrev.html#torch.func.jacrev "torch.func.jacrev") |
| functorch.jacfwd | [`torch.func.jacfwd()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacfwd.html#torch.func.jacfwd "torch.func.jacfwd") |
| functorch.hessian | [`torch.func.hessian()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.hessian.html#torch.func.hessian "torch.func.hessian") |
| functorch.functionalize | [`torch.func.functionalize()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.functionalize.html#torch.func.functionalize "torch.func.functionalize") |

Furthermore, if you are using torch.autograd.functional APIs, please try out the [`torch.func`](https://docs.pytorch.org/docs/2.15/func.api.html#module-torch.func "torch.func")
 equivalents instead. [`torch.func`](https://docs.pytorch.org/docs/2.15/func.api.html#module-torch.func "torch.func")
 function transforms are more composable and more performant in many cases.

| torch.autograd.functional API | torch.func API (as of PyTorch 2.0) |
| --- | --- |
| [`torch.autograd.functional.vjp()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.functional.vjp.html#torch.autograd.functional.vjp "torch.autograd.functional.vjp") | [`torch.func.grad()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.grad.html#torch.func.grad "torch.func.grad")<br> or [`torch.func.vjp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vjp.html#torch.func.vjp "torch.func.vjp") |
| [`torch.autograd.functional.jvp()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.functional.jvp.html#torch.autograd.functional.jvp "torch.autograd.functional.jvp") | [`torch.func.jvp()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jvp.html#torch.func.jvp "torch.func.jvp") |
| [`torch.autograd.functional.jacobian()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.functional.jacobian.html#torch.autograd.functional.jacobian "torch.autograd.functional.jacobian") | [`torch.func.jacrev()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacrev.html#torch.func.jacrev "torch.func.jacrev")<br> or [`torch.func.jacfwd()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.jacfwd.html#torch.func.jacfwd "torch.func.jacfwd") |
| [`torch.autograd.functional.hessian()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.functional.hessian.html#torch.autograd.functional.hessian "torch.autograd.functional.hessian") | [`torch.func.hessian()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.hessian.html#torch.func.hessian "torch.func.hessian") |

NN module utilities[#](https://docs.pytorch.org/docs/2.15/func.migrating.html#nn-module-utilities "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

We’ve changed the APIs to apply function transforms over NN modules to make them fit better into the PyTorch design philosophy. The new API is different, so please read this section carefully.

### functorch.make\_functional[#](https://docs.pytorch.org/docs/2.15/func.migrating.html#functorch-make-functional "Link to this heading")

[`torch.func.functional_call()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.functional_call.html#torch.func.functional_call "torch.func.functional_call")
 is the replacement for [functorch.make\_functional](https://pytorch.org/functorch/1.13/generated/functorch.make_functional.html#functorch.make_functional)
 and [functorch.make\_functional\_with\_buffers](https://pytorch.org/functorch/1.13/generated/functorch.make_functional_with_buffers.html#functorch.make_functional_with_buffers)
. However, it is not a drop-in replacement.

If you’re in a hurry, you can use [helper functions in this gist](https://gist.github.com/zou3519/7769506acc899d83ef1464e28f22e6cf)
 that emulate the behavior of functorch.make\_functional and functorch.make\_functional\_with\_buffers. We recommend using [`torch.func.functional_call()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.functional_call.html#torch.func.functional_call "torch.func.functional_call")
 directly because it is a more explicit and flexible API.

Concretely, functorch.make\_functional returns a functional module and parameters. The functional module accepts parameters and inputs to the model as arguments. [`torch.func.functional_call()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.functional_call.html#torch.func.functional_call "torch.func.functional_call")
 allows one to call the forward pass of an existing module using new parameters and buffers and inputs.

Here’s an example of how to compute gradients of parameters of a model using functorch vs [`torch.func`](https://docs.pytorch.org/docs/2.15/func.api.html#module-torch.func "torch.func")
:

\# ---------------
\# using functorch
\# ---------------
import torch
import functorch
inputs \= torch.randn(64, 3)
targets \= torch.randn(64, 3)
model \= torch.nn.Linear(3, 3)

fmodel, params \= functorch.make\_functional(model)

def compute\_loss(params, inputs, targets):
    prediction \= fmodel(params, inputs)
    return torch.nn.functional.mse\_loss(prediction, targets)

grads \= functorch.grad(compute\_loss)(params, inputs, targets)

\# ------------------------------------
\# using torch.func (as of PyTorch 2.0)
\# ------------------------------------
import torch
inputs \= torch.randn(64, 3)
targets \= torch.randn(64, 3)
model \= torch.nn.Linear(3, 3)

params \= dict(model.named\_parameters())

def compute\_loss(params, inputs, targets):
    prediction \= torch.func.functional\_call(model, params, (inputs,))
    return torch.nn.functional.mse\_loss(prediction, targets)

grads \= torch.func.grad(compute\_loss)(params, inputs, targets)

Copy to clipboard

And here’s an example of how to compute jacobians of model parameters:

\# ---------------
\# using functorch
\# ---------------
import torch
import functorch
inputs \= torch.randn(64, 3)
model \= torch.nn.Linear(3, 3)

fmodel, params \= functorch.make\_functional(model)
jacobians \= functorch.jacrev(fmodel)(params, inputs)

\# ------------------------------------
\# using torch.func (as of PyTorch 2.0)
\# ------------------------------------
import torch
from torch.func import jacrev, functional\_call
inputs \= torch.randn(64, 3)
model \= torch.nn.Linear(3, 3)

params \= dict(model.named\_parameters())
\# jacrev computes jacobians of argnums=0 by default.
\# We set it to 1 to compute jacobians of params
jacobians \= jacrev(functional\_call, argnums\=1)(model, params, (inputs,))

Copy to clipboard

Note that it is important for memory consumption that you should only carry around a single copy of your parameters. `model.named_parameters()` does not copy the parameters. If in your model training you update the parameters of the model in-place, then the `nn.Module` that is your model has the single copy of the parameters and everything is OK.

However, if you want to carry your parameters around in a dictionary and update them out-of-place, then there are two copies of parameters: the one in the dictionary and the one in the `model`. In this case, you should change `model` to not hold memory by converting it to the meta device via `model.to('meta')`.

### functorch.combine\_state\_for\_ensemble[#](https://docs.pytorch.org/docs/2.15/func.migrating.html#functorch-combine-state-for-ensemble "Link to this heading")

Please use [`torch.func.stack_module_state()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.stack_module_state.html#torch.func.stack_module_state "torch.func.stack_module_state")
 instead of [functorch.combine\_state\_for\_ensemble](https://pytorch.org/functorch/1.13/generated/functorch.combine_state_for_ensemble.html)
 [`torch.func.stack_module_state()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.stack_module_state.html#torch.func.stack_module_state "torch.func.stack_module_state")
 returns two dictionaries, one of stacked parameters, and one of stacked buffers, that can then be used with [`torch.vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
 and [`torch.func.functional_call()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.functional_call.html#torch.func.functional_call "torch.func.functional_call")
 for ensembling.

For example, here is an example of how to ensemble over a very simple model:

import torch
num\_models \= 5
batch\_size \= 64
in\_features, out\_features \= 3, 3
models \= \[torch.nn.Linear(in\_features, out\_features) for i in range(num\_models)\]
data \= torch.randn(batch\_size, 3)

\# ---------------
\# using functorch
\# ---------------
import functorch
fmodel, params, buffers \= functorch.combine\_state\_for\_ensemble(models)
output \= functorch.vmap(fmodel, (0, 0, None))(params, buffers, data)
assert output.shape \== (num\_models, batch\_size, out\_features)

\# ------------------------------------
\# using torch.func (as of PyTorch 2.0)
\# ------------------------------------
import copy

\# Construct a version of the model with no memory by putting the Tensors on
\# the meta device.
base\_model \= copy.deepcopy(models\[0\])
base\_model.to('meta')

params, buffers \= torch.func.stack\_module\_state(models)

\# It is possible to vmap directly over torch.func.functional\_call,
\# but wrapping it in a function makes it clearer what is going on.
def call\_single\_model(params, buffers, data):
    return torch.func.functional\_call(base\_model, (params, buffers), (data,))

output \= torch.vmap(call\_single\_model, (0, 0, None))(params, buffers, data)
assert output.shape \== (num\_models, batch\_size, out\_features)

Copy to clipboard

functorch.compile[#](https://docs.pytorch.org/docs/2.15/func.migrating.html#functorch-compile "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

We are no longer supporting functorch.compile (also known as AOTAutograd) as a frontend for compilation in PyTorch; we have integrated AOTAutograd into PyTorch’s compilation story. If you are a user, please use [`torch.compile()`](https://docs.pytorch.org/docs/2.15/generated/torch.compile.html#torch.compile "torch.compile")
 instead.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/func.migrating.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/func.migrating.md.txt)

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