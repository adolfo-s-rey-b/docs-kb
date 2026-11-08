Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/notes/amp_examples.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/notes/amp_examples.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/notes/amp_examples.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/notes/amp_examples.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/notes/amp_examples.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/notes/amp_examples.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/notes/amp_examples.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/notes/amp_examples.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/notes/amp_examples.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/notes/amp_examples.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/notes/amp_examples.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/notes/amp_examples.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/notes/amp_examples.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/notes/amp_examples.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/notes/amp_examples.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/notes/amp_examples.html)
[v1.13](https://docs.pytorch.org/docs/1.13/notes/amp_examples.html)
[v1.12](https://docs.pytorch.org/docs/1.12/notes/amp_examples.html)
[v1.11](https://docs.pytorch.org/docs/1.11/notes/amp_examples.html)
[v1.10](https://docs.pytorch.org/docs/1.10/notes/amp_examples.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/notes/amp_examples.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/notes/amp_examples.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/notes/amp_examples.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/notes/amp_examples.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/notes/amp_examples.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/notes/amp_examples.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/notes/amp_examples.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/notes/amp_examples.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/notes/amp_examples.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/notes/amp_examples.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/notes/amp_examples.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/notes/amp_examples.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/notes/amp_examples.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/notes/amp_examples.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/notes/amp_examples.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/notes/amp_examples.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/notes/amp_examples.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/notes/amp_examples.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/notes/amp_examples.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/notes/amp_examples.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/notes/amp_examples.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/notes/amp_examples.html)

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

Automatic Mixed Precision examples[#](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#automatic-mixed-precision-examples "Link to this heading")

============================================================================================================================================================

Created On: May 07, 2026 | Last Updated On: May 07, 2026

Ordinarily, “automatic mixed precision training” means training with [`torch.autocast`](https://docs.pytorch.org/docs/2.15/amp.html#torch.autocast "torch.autocast")
 and `torch.amp.GradScaler` together.

Instances of [`torch.autocast`](https://docs.pytorch.org/docs/2.15/amp.html#torch.autocast "torch.autocast")
 enable autocasting for chosen regions. Autocasting automatically chooses the precision for operations to improve performance while maintaining accuracy.

Instances of `torch.amp.GradScaler` help perform the steps of gradient scaling conveniently. Gradient scaling improves convergence for networks with `float16` (by default on CUDA and XPU) gradients by minimizing gradient underflow, as explained [here](https://docs.pytorch.org/docs/2.15/amp.html#gradient-scaling)
.

[`torch.autocast`](https://docs.pytorch.org/docs/2.15/amp.html#torch.autocast "torch.autocast")
 and `torch.amp.GradScaler` are modular. In the samples below, each is used as its individual documentation suggests.

(Samples here are illustrative. See the [Automatic Mixed Precision recipe](https://pytorch.org/tutorials/recipes/recipes/amp_recipe.html)
 for a runnable walkthrough.)

[Typical Mixed Precision Training](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#id2)
[#](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#typical-mixed-precision-training "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\# Creates model and optimizer in default precision
model \= Net().cuda()
optimizer \= optim.SGD(model.parameters(), ...)

\# Creates a GradScaler once at the beginning of training.
scaler \= GradScaler()

for epoch in epochs:
    for input, target in data:
        optimizer.zero\_grad()

        \# Runs the forward pass with autocasting.
        with autocast(device\_type\='cuda', dtype\=torch.float16):
            output \= model(input)
            loss \= loss\_fn(output, target)

        \# Scales loss.  Calls backward() on scaled loss to create scaled gradients.
        \# Backward passes under autocast are not recommended.
        \# Backward ops run in the same dtype autocast chose for corresponding forward ops.
        scaler.scale(loss).backward()

        \# scaler.step() first unscales the gradients of the optimizer's assigned params.
        \# If these gradients do not contain infs or NaNs, optimizer.step() is then called,
        \# otherwise, optimizer.step() is skipped.
        scaler.step(optimizer)

        \# Updates the scale for next iteration.
        scaler.update()

Copy to clipboard

[Working with Unscaled Gradients](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#id3)
[#](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#working-with-unscaled-gradients "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

All gradients produced by `scaler.scale(loss).backward()` are scaled. If you wish to modify or inspect the parameters’ `.grad` attributes between `backward()` and `scaler.step(optimizer)`, you should unscale them first. For example, gradient clipping manipulates a set of gradients such that their global norm (see [`torch.nn.utils.clip_grad_norm_()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.utils.clip_grad_norm_.html#torch.nn.utils.clip_grad_norm_ "torch.nn.utils.clip_grad_norm_")
) or maximum magnitude (see [`torch.nn.utils.clip_grad_value_()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.utils.clip_grad_value_.html#torch.nn.utils.clip_grad_value_ "torch.nn.utils.clip_grad_value_")
) is <\=<=<= some user-imposed threshold. If you attempted to clip _without_ unscaling, the gradients’ norm/maximum magnitude would also be scaled, so your requested threshold (which was meant to be the threshold for _unscaled_ gradients) would be invalid.

`scaler.unscale_(optimizer)` unscales gradients held by `optimizer`’s assigned parameters. If your model or models contain other parameters that were assigned to another optimizer (say `optimizer2`), you may call `scaler.unscale_(optimizer2)` separately to unscale those parameters’ gradients as well.

### [Gradient clipping](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#id4)
[#](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#gradient-clipping "Link to this heading")

Calling `scaler.unscale_(optimizer)` before clipping enables you to clip unscaled gradients as usual:

scaler \= GradScaler()

for epoch in epochs:
    for input, target in data:
        optimizer.zero\_grad()
        with autocast(device\_type\='cuda', dtype\=torch.float16):
            output \= model(input)
            loss \= loss\_fn(output, target)
        scaler.scale(loss).backward()

        \# Unscales the gradients of optimizer's assigned params in-place
        scaler.unscale\_(optimizer)

        \# Since the gradients of optimizer's assigned params are unscaled, clips as usual:
        torch.nn.utils.clip\_grad\_norm\_(model.parameters(), max\_norm)

        \# optimizer's gradients are already unscaled, so scaler.step does not unscale them,
        \# although it still skips optimizer.step() if the gradients contain infs or NaNs.
        scaler.step(optimizer)

        \# Updates the scale for next iteration.
        scaler.update()

Copy to clipboard

`scaler` records that `scaler.unscale_(optimizer)` was already called for this optimizer this iteration, so `scaler.step(optimizer)` knows not to redundantly unscale gradients before (internally) calling `optimizer.step()`.

Warning

`unscale_` should only be called once per optimizer per `step` call, and only after all gradients for that optimizer’s assigned parameters have been accumulated. Calling `unscale_` twice for a given optimizer between each `step` triggers a RuntimeError.

[Working with Scaled Gradients](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#id5)
[#](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#working-with-scaled-gradients "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Gradient accumulation](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#id6)
[#](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#gradient-accumulation "Link to this heading")

Gradient accumulation adds gradients over an effective batch of size `batch_per_iter * iters_to_accumulate` (`* num_procs` if distributed). The scale should be calibrated for the effective batch, which means inf/NaN checking, step skipping if inf/NaN grads are found, and scale updates should occur at effective-batch granularity. Also, grads should remain scaled, and the scale factor should remain constant, while grads for a given effective batch are accumulated. If grads are unscaled (or the scale factor changes) before accumulation is complete, the next backward pass will add scaled grads to unscaled grads (or grads scaled by a different factor) after which it’s impossible to recover the accumulated unscaled grads `step` must apply.

Therefore, if you want to `unscale_` grads (e.g., to allow clipping unscaled grads), call `unscale_` just before `step`, after all (scaled) grads for the upcoming `step` have been accumulated. Also, only call `update` at the end of iterations where you called `step` for a full effective batch:

scaler \= GradScaler()

for epoch in epochs:
    for i, (input, target) in enumerate(data):
        with autocast(device\_type\='cuda', dtype\=torch.float16):
            output \= model(input)
            loss \= loss\_fn(output, target)
            loss \= loss / iters\_to\_accumulate

        \# Accumulates scaled gradients.
        scaler.scale(loss).backward()

        if (i + 1) % iters\_to\_accumulate \== 0:
            \# may unscale\_ here if desired (e.g., to allow clipping unscaled gradients)

            scaler.step(optimizer)
            scaler.update()
            optimizer.zero\_grad()

Copy to clipboard

### [Gradient penalty](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#id7)
[#](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#gradient-penalty "Link to this heading")

A gradient penalty implementation commonly creates gradients using [`torch.autograd.grad()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.grad.html#torch.autograd.grad "torch.autograd.grad")
, combines them to create the penalty value, and adds the penalty value to the loss.

Here’s an ordinary example of an L2 penalty without gradient scaling or autocasting:

for epoch in epochs:
    for input, target in data:
        optimizer.zero\_grad()
        output \= model(input)
        loss \= loss\_fn(output, target)

        \# Creates gradients
        grad\_params \= torch.autograd.grad(outputs\=loss,
                                          inputs\=model.parameters(),
                                          create\_graph\=True)

        \# Computes the penalty term and adds it to the loss
        grad\_norm \= 0
        for grad in grad\_params:
            grad\_norm += grad.pow(2).sum()
        grad\_norm \= grad\_norm.sqrt()
        loss \= loss + grad\_norm

        loss.backward()

        \# clip gradients here, if desired

        optimizer.step()

Copy to clipboard

To implement a gradient penalty _with_ gradient scaling, the `outputs` Tensor(s) passed to [`torch.autograd.grad()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.grad.html#torch.autograd.grad "torch.autograd.grad")
 should be scaled. The resulting gradients will therefore be scaled, and should be unscaled before being combined to create the penalty value.

Also, the penalty term computation is part of the forward pass, and therefore should be inside an `autocast` context.

Here’s how that looks for the same L2 penalty:

scaler \= GradScaler()

for epoch in epochs:
    for input, target in data:
        optimizer.zero\_grad()
        with autocast(device\_type\='cuda', dtype\=torch.float16):
            output \= model(input)
            loss \= loss\_fn(output, target)

        \# Scales the loss for autograd.grad's backward pass, producing scaled\_grad\_params
        scaled\_grad\_params \= torch.autograd.grad(outputs\=scaler.scale(loss),
                                                 inputs\=model.parameters(),
                                                 create\_graph\=True)

        \# Creates unscaled grad\_params before computing the penalty. scaled\_grad\_params are
        \# not owned by any optimizer, so ordinary division is used instead of scaler.unscale\_:
        inv\_scale \= 1./scaler.get\_scale()
        grad\_params \= \[p \* inv\_scale for p in scaled\_grad\_params\]

        \# Computes the penalty term and adds it to the loss
        with autocast(device\_type\='cuda', dtype\=torch.float16):
            grad\_norm \= 0
            for grad in grad\_params:
                grad\_norm += grad.pow(2).sum()
            grad\_norm \= grad\_norm.sqrt()
            loss \= loss + grad\_norm

        \# Applies scaling to the backward call as usual.
        \# Accumulates leaf gradients that are correctly scaled.
        scaler.scale(loss).backward()

        \# may unscale\_ here if desired (e.g., to allow clipping unscaled gradients)

        \# step() and update() proceed as usual.
        scaler.step(optimizer)
        scaler.update()

Copy to clipboard

[Working with Multiple Models, Losses, and Optimizers](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#id8)
[#](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#working-with-multiple-models-losses-and-optimizers "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If your network has multiple losses, you must call `scaler.scale` on each of them individually. If your network has multiple optimizers, you may call `scaler.unscale_` on any of them individually, and you must call `scaler.step` on each of them individually.

However, `scaler.update` should only be called once, after all optimizers used this iteration have been stepped:

scaler \= torch.amp.GradScaler()

for epoch in epochs:
    for input, target in data:
        optimizer0.zero\_grad()
        optimizer1.zero\_grad()
        with autocast(device\_type\='cuda', dtype\=torch.float16):
            output0 \= model0(input)
            output1 \= model1(input)
            loss0 \= loss\_fn(2 \* output0 + 3 \* output1, target)
            loss1 \= loss\_fn(3 \* output0 \- 5 \* output1, target)

        \# (retain\_graph here is unrelated to amp, it's present because in this
        \# example, both backward() calls share some sections of graph.)
        scaler.scale(loss0).backward(retain\_graph\=True)
        scaler.scale(loss1).backward()

        \# You can choose which optimizers receive explicit unscaling, if you
        \# want to inspect or modify the gradients of the params they own.
        scaler.unscale\_(optimizer0)

        scaler.step(optimizer0)
        scaler.step(optimizer1)

        scaler.update()

Copy to clipboard

Each optimizer checks its gradients for infs/NaNs and makes an independent decision whether or not to skip the step. This may result in one optimizer skipping the step while the other one does not. Since step skipping occurs rarely (every several hundred iterations) this should not impede convergence. If you observe poor convergence after adding gradient scaling to a multiple-optimizer model, please report a bug.

[Working with Multiple GPUs](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#id9)
[#](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#working-with-multiple-gpus "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The issues described here only affect `autocast`. `GradScaler`’s usage is unchanged.

### [DataParallel in a single process](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#id10)
[#](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#dataparallel-in-a-single-process "Link to this heading")

Even if [`torch.nn.DataParallel`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.DataParallel.html#torch.nn.DataParallel "torch.nn.DataParallel")
 spawns threads to run the forward pass on each device. The autocast state is propagated in each one and the following will work:

model \= MyModel()
dp\_model \= nn.DataParallel(model)

\# Sets autocast in the main thread
with autocast(device\_type\='cuda', dtype\=torch.float16):
    \# dp\_model's internal threads will autocast.
    output \= dp\_model(input)
    \# loss\_fn also autocast
    loss \= loss\_fn(output)

Copy to clipboard

### [DistributedDataParallel, one GPU per process](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#id11)
[#](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#distributeddataparallel-one-gpu-per-process "Link to this heading")

[`torch.nn.parallel.DistributedDataParallel`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")
’s documentation recommends one GPU per process for best performance. In this case, `DistributedDataParallel` does not spawn threads internally, so usages of `autocast` and `GradScaler` are not affected.

### [DistributedDataParallel, multiple GPUs per process](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#id12)
[#](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#distributeddataparallel-multiple-gpus-per-process "Link to this heading")

Here [`torch.nn.parallel.DistributedDataParallel`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")
 may spawn a side thread to run the forward pass on each device, like [`torch.nn.DataParallel`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.DataParallel.html#torch.nn.DataParallel "torch.nn.DataParallel")
. [The fix is the same](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#amp-dataparallel)
: apply autocast as part of your model’s `forward` method to ensure it’s enabled in side threads.

[Autocast and Custom Autograd Functions](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#id13)
[#](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#autocast-and-custom-autograd-functions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If your network uses [custom autograd functions](https://docs.pytorch.org/docs/2.15/notes/extending.html#extending-autograd)
 (subclasses of [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
), changes are required for autocast compatibility if any function

*   takes multiple floating-point Tensor inputs,
    
*   wraps any autocastable op (see the [Autocast Op Reference](https://docs.pytorch.org/docs/2.15/amp.html#autocast-op-reference)
    ), or
    
*   requires a particular `dtype` (for example, if it wraps [CUDA extensions](https://pytorch.org/tutorials/advanced/cpp_extension.html)
     that were only compiled for `dtype`).
    

In all cases, if you’re importing the function and can’t alter its definition, a safe fallback is to disable autocast and force execution in `float32` ( or `dtype`) at any points of use where errors occur:

with autocast(device\_type\='cuda', dtype\=torch.float16):
    ...
    with autocast(device\_type\='cuda', dtype\=torch.float16, enabled\=False):
        output \= imported\_function(input1.float(), input2.float())

Copy to clipboard

If you’re the function’s author (or can alter its definition) a better solution is to use the [`torch.amp.custom_fwd()`](https://docs.pytorch.org/docs/2.15/amp.html#torch.amp.custom_fwd "torch.amp.custom_fwd")
 and [`torch.amp.custom_bwd()`](https://docs.pytorch.org/docs/2.15/amp.html#torch.amp.custom_bwd "torch.amp.custom_bwd")
 decorators as shown in the relevant case below.

### [Functions with multiple inputs or autocastable ops](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#id14)
[#](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#functions-with-multiple-inputs-or-autocastable-ops "Link to this heading")

Apply [`custom_fwd`](https://docs.pytorch.org/docs/2.15/amp.html#torch.amp.custom_fwd "torch.amp.custom_fwd")
 and [`custom_bwd`](https://docs.pytorch.org/docs/2.15/amp.html#torch.amp.custom_bwd "torch.amp.custom_bwd")
 (with no arguments) to `forward` and `backward` respectively. These ensure `forward` executes with the current autocast state and `backward` executes with the same autocast state as `forward` (which can prevent type mismatch errors):

class MyMM(torch.autograd.Function):
    @staticmethod
    @custom\_fwd
    def forward(ctx, a, b):
        ctx.save\_for\_backward(a, b)
        return a.mm(b)
    @staticmethod
    @custom\_bwd
    def backward(ctx, grad):
        a, b \= ctx.saved\_tensors
        return grad.mm(b.t()), a.t().mm(grad)

Copy to clipboard

Now `MyMM` can be invoked anywhere, without disabling autocast or manually casting inputs:

mymm \= MyMM.apply

with autocast(device\_type\='cuda', dtype\=torch.float16):
    output \= mymm(input1, input2)

Copy to clipboard

### [Functions that need a particular `dtype`](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#id15)
[#](https://docs.pytorch.org/docs/2.15/notes/amp_examples.html#functions-that-need-a-particular-dtype "Link to this heading")

Consider a custom function that requires `torch.float32` inputs. Apply [`custom_fwd(device_type='cuda', cast_inputs=torch.float32)`](https://docs.pytorch.org/docs/2.15/amp.html#torch.amp.custom_fwd "torch.amp.custom_fwd")
 to `forward` and [`custom_bwd(device_type='cuda')`](https://docs.pytorch.org/docs/2.15/amp.html#torch.amp.custom_bwd "torch.amp.custom_bwd")
 to `backward`. If `forward` runs in an autocast-enabled region, the decorators cast floating-point Tensor inputs to `float32` on designated device assigned by the argument [device\_type](https://docs.pytorch.org/docs/2.15/amp.html)
, `CUDA` in this example, and locally disable autocast during `forward` and `backward`:

class MyFloat32Func(torch.autograd.Function):
    @staticmethod
    @custom\_fwd(device\_type\='cuda', cast\_inputs\=torch.float32)
    def forward(ctx, input):
        ctx.save\_for\_backward(input)
        ...
        return fwd\_output
    @staticmethod
    @custom\_bwd(device\_type\='cuda')
    def backward(ctx, grad):
        ...

Copy to clipboard

Now `MyFloat32Func` can be invoked anywhere, without manually disabling autocast or casting inputs:

func \= MyFloat32Func.apply

with autocast(device\_type\='cuda', dtype\=torch.float16):
    \# func will run in float32, regardless of the surrounding autocast state
    output \= func(input)

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/notes/amp_examples.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/notes/amp_examples.md.txt)

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