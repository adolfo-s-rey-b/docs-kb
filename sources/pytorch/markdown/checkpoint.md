Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/checkpoint.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/checkpoint.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/checkpoint.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/checkpoint.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/checkpoint.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/checkpoint.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/checkpoint.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/checkpoint.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/checkpoint.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/checkpoint.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/checkpoint.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/checkpoint.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/checkpoint.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/checkpoint.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/checkpoint.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/checkpoint.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/checkpoint.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/checkpoint.html)
[v1.13](https://docs.pytorch.org/docs/1.13/checkpoint.html)
[v1.12](https://docs.pytorch.org/docs/1.12/checkpoint.html)
[v1.11](https://docs.pytorch.org/docs/1.11/checkpoint.html)
[v1.10](https://docs.pytorch.org/docs/1.10/checkpoint.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/checkpoint.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/checkpoint.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/checkpoint.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/checkpoint.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/checkpoint.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/checkpoint.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/checkpoint.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/checkpoint.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/checkpoint.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/checkpoint.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/checkpoint.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/checkpoint.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/checkpoint.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/checkpoint.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/checkpoint.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/checkpoint.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/checkpoint.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/checkpoint.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/checkpoint.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/checkpoint.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/checkpoint.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/checkpoint.html)

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

torch.utils.checkpoint[#](https://docs.pytorch.org/docs/2.15/checkpoint.html#torch-utils-checkpoint "Link to this heading")

============================================================================================================================

Created On: Jun 16, 2025 | Last Updated On: Jul 27, 2026

Note

Checkpointing is implemented by rerunning a forward-pass segment for each checkpointed segment during backward propagation. This can cause persistent states like the RNG state to be more advanced than they would without checkpointing. By default, checkpointing includes logic to juggle the RNG state such that checkpointed passes making use of RNG (through dropout for example) have deterministic output as compared to non-checkpointed passes. The logic to stash and restore RNG states can incur a moderate performance hit depending on the runtime of checkpointed operations. If deterministic output compared to non-checkpointed passes is not required, supply `preserve_rng_state=False` to `checkpoint` or `checkpoint_sequential` to omit stashing and restoring the RNG state during each checkpoint.

The stashing logic saves and restores the RNG state for CPU and another device type (infer the device type from Tensor arguments excluding CPU tensors by `_infer_device_type`) to the `run_fn`. If there are multiple devices, device state will only be saved for devices of a single device type, and the remaining devices will be ignored. Consequently, if any checkpointed functions involve randomness, this may result in incorrect gradients. (Note that if CUDA devices are among the devices detected, it will be prioritized; otherwise, the first device encountered will be selected.) If there are no CPU-tensors, the default device type state (default value is `cuda`, and it could be set to other device by `DefaultDeviceType`) will be saved and restored. However, the logic has no way to anticipate if the user will move Tensors to a new device within the `run_fn` itself. Therefore, if you move Tensors to a new device (“new” meaning not belonging to the set of \[current device + devices of Tensor arguments\]) within `run_fn`, deterministic output compared to non-checkpointed passes is never guaranteed.

`checkpoint` may also be called without a function to produce a decorator. This keeps checkpoint configuration separate from the keyword arguments passed to the checkpointed function:

checkpointed\_fn \= checkpoint(use\_reentrant\=False, preserve\_rng\_state\=False)(fn)
out \= checkpointed\_fn(\*args, \*\*kwargs)

Copy to clipboard

torch.utils.checkpoint.checkpoint(_function: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[...\], \_T\]_, _\*args: Any_, _use\_reentrant: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _preserve\_rng\_state: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= True_, _context\_fn: Callable\[\[\], Tuple\[ContextManager, ContextManager\]\] \= noop\_context\_fn_, _determinism\_check: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 \= \_DEFAULT\_DETERMINISM\_MODE_, _debug: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= False_, _early\_stop: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= True_, _respect\_saved\_tensors\_hooks: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _\*\*kwargs: Any_) → \_T[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/checkpoint.py#L422)
[#](https://docs.pytorch.org/docs/2.15/checkpoint.html#torch.utils.checkpoint.checkpoint "Link to this definition")

torch.utils.checkpoint.checkpoint(_function: [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _\*_, _use\_reentrant: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _preserve\_rng\_state: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= True_, _context\_fn: Callable\[\[\], Tuple\[ContextManager, ContextManager\]\] \= noop\_context\_fn_, _determinism\_check: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 \= \_DEFAULT\_DETERMINISM\_MODE_, _debug: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= False_, _early\_stop: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= True_, _respect\_saved\_tensors\_hooks: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_) → [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")\
\[\[\_P\], \_T\]\], [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")\
\[\[\_P\], \_T\]\]

Checkpoint a model or part of the model.

Activation checkpointing is a technique that trades compute for memory. By default, tensors computed during the forward pass are kept alive until they are used in gradient computations in the backward pass. To reduce this memory usage, tensors produced in the passed `function` are not kept alive until the backward pass. Instead, any passed tensors in `args` are kept alive, and the unsaved tensors are recomputed by re-invoking `function` in the backward pass as needed for gradient computation. Activation checkpointing can be applied to any part of a model – this is sometimes described as “checkpointing” that part of the model.

There are currently two checkpointing implementations available, determined by the `use_reentrant` parameter. It is recommended that you use `use_reentrant=False`. Please refer the note below for a discussion of their differences.

Warning

If the `function` invocation during the backward pass differs from the forward pass, e.g., due to a global variable, the checkpointed version may not be equivalent, potentially causing an error being raised or leading to silently incorrect gradients.

Warning

The `use_reentrant` parameter should be passed explicitly. In a future release, we will raise an exception if `use_reentrant` is not passed. If you are using the `use_reentrant=True` variant, please refer to the note below for important considerations and potential limitations.

Note

The reentrant variant of checkpoint (`use_reentrant=True`) and the non-reentrant variant of checkpoint (`use_reentrant=False`) differ in the following ways:

*   Non-reentrant checkpoint stops recomputation as soon as all needed intermediate activations have been recomputed. This feature is enabled by default, but can be disabled with [`set_checkpoint_early_stop()`](https://docs.pytorch.org/docs/2.15/checkpoint.html#torch.utils.checkpoint.set_checkpoint_early_stop "torch.utils.checkpoint.set_checkpoint_early_stop")
    . Reentrant checkpoint always recomputes `function` in its entirety during the backward pass.
    
*   The reentrant variant does not record the autograd graph during the forward pass, as it runs with the forward pass under [`torch.no_grad()`](https://docs.pytorch.org/docs/2.15/generated/torch.no_grad.html#torch.no_grad "torch.no_grad")
    . The non-reentrant version does record the autograd graph, allowing one to perform backward on the graph within checkpointed regions.
    
*   The reentrant checkpoint only supports the [`torch.autograd.backward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.backward.html#torch.autograd.backward "torch.autograd.backward")
     API for the backward pass without its inputs argument, while the non-reentrant version supports all ways of performing the backward pass.
    
*   At least one input and output must have `requires_grad=True` for the reentrant variant. If this condition is unmet, the checkpointed part of the model will not have gradients. The non-reentrant version does not have this requirement.
    
*   The reentrant version does not consider tensors in nested structures (e.g., custom objects, lists, dicts, etc) as participating in autograd, while the non-reentrant version does.
    
*   The reentrant checkpoint does not support checkpointed regions with detached tensors from the computational graph, whereas the non-reentrant version does. For the reentrant variant, if the checkpointed segment contains tensors detached using `detach()` or with [`torch.no_grad()`](https://docs.pytorch.org/docs/2.15/generated/torch.no_grad.html#torch.no_grad "torch.no_grad")
    , the backward pass will raise an error. This is because `checkpoint` makes all the outputs require gradients and this causes issues when a tensor is defined to have no gradient in the model. To avoid this, detach the tensors outside of the `checkpoint` function.
    

Parameters:

*   **function** – describes what to run in the forward pass of the model or part of the model. It should also know how to handle the inputs passed as the tuple. For example, in LSTM, if user passes `(activation, hidden)`, `function` should correctly use the first input as `activation` and the second input as `hidden`. If omitted, `checkpoint` returns a decorator that can be used to wrap a function before passing user arguments.
    
*   **args** – tuple containing inputs to the `function`
    

Keyword Arguments:

*   **preserve\_rng\_state** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Omit stashing and restoring the RNG state during each checkpoint. Note that under torch.compile, this flag doesn’t take effect and we always preserve RNG state. Default: `True`
    
*   **use\_reentrant** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – specify whether to use the activation checkpoint variant that requires reentrant autograd. This parameter should be passed explicitly. In a future release, we will raise an exception if `use_reentrant` is not passed. If `use_reentrant=False`, `checkpoint` will use an implementation that does not require reentrant autograd. This allows `checkpoint` to support additional functionality, such as working as expected with `torch.autograd.grad` and support for keyword arguments input into the checkpointed function.
    
*   **context\_fn** (_Callable__,_ _optional_) – A callable returning a tuple of two context managers. The function and its recomputation will be run under the first and second context managers respectively. This argument is only supported if `use_reentrant=False`.
    
*   **determinism\_check** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – A string specifying the determinism check to perform. By default it is set to `"default"` which compares the shapes, dtypes, and devices of the recomputed tensors against those the saved tensors. To turn off this check, specify `"none"`. Currently these are the only two supported values. Please open an issue if you would like to see more determinism checks. This argument is only supported if `use_reentrant=False`, if `use_reentrant=True`, the determinism check is always disabled.
    
*   **debug** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True`, error messages will also include a trace of the operators ran during the original forward computation as well as the recomputation. This argument is only supported if `use_reentrant=False`.
    
*   **early\_stop** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True`, non-reentrant checkpoint stops recomputation as soon as it has computed all needed Tensors. This argument is ignored if `use_reentrant=True`. Can be overridden globally using [`set_checkpoint_early_stop()`](https://docs.pytorch.org/docs/2.15/checkpoint.html#torch.utils.checkpoint.set_checkpoint_early_stop "torch.utils.checkpoint.set_checkpoint_early_stop")
     context manager. Default: `True`.
    
*   **respect\_saved\_tensors\_hooks** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Whether tensors that selective activation checkpointing (SAC) saves are routed through the surrounding user [`torch.autograd.graph.saved_tensors_hooks()`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.graph.saved_tensors_hooks "torch.autograd.graph.saved_tensors_hooks")
     (e.g. [`torch.autograd.graph.save_on_cpu()`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.graph.save_on_cpu "torch.autograd.graph.save_on_cpu")
    ). Such tensors are held outside the autograd graph, so historically these hooks did not see them; a future release will make checkpoint honor the hooks by default. Until then the default (`None`) keeps the legacy behavior and emits a `FutureWarning` when a user hook is in scope; pass `True` to opt in or `False` to keep the legacy behavior without the warning. Has no effect without SAC (plain checkpoint recomputes rather than saves) or when `use_reentrant=True`. This argument is only supported if `use_reentrant=False`.
    

Returns:

Output of running `function` on `*args`, or a decorator when `function` is omitted.

Example

\>>> \# Direct call: checkpoint the function immediately.
\>>> out \= torch.utils.checkpoint.checkpoint(
...     fn, \*args, use\_reentrant\=False, \*\*kwargs
... )
\>>> \# Decorator/curried form: configure once, then call.
\>>> checkpointed\_fn \= torch.utils.checkpoint.checkpoint(
...     use\_reentrant\=False,
...     preserve\_rng\_state\=False,
... )(fn)
\>>> out \= checkpointed\_fn(\*args, \*\*kwargs)
\>>> \# The same decorator can be applied directly to a function or method.
\>>> @torch.utils.checkpoint.checkpoint(use\_reentrant\=False)
... def fn(\*args, \*\*kwargs):
...     ...
\>>> out \= fn(\*args, \*\*kwargs)

Copy to clipboard

torch.utils.checkpoint.checkpoint\_sequential(_functions_, _segments_, _input_, _use\_reentrant\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/checkpoint.py#L701)
[#](https://docs.pytorch.org/docs/2.15/checkpoint.html#torch.utils.checkpoint.checkpoint_sequential "Link to this definition")

Checkpoint a sequential model to save memory.

Sequential models execute a list of modules/functions in order (sequentially). Therefore, we can divide such a model in various segments and checkpoint each segment. All segments except the last will not store the intermediate activations. The inputs of each checkpointed segment will be saved for re-running the segment in the backward pass.

Warning

The `use_reentrant` parameter should be passed explicitly. In a future release, we will raise an exception if `use_reentrant` is not passed. If you are using the ```use_reentrant=True` variant, please see :func:`~torch.utils.checkpoint.checkpoint` for the important considerations and limitations of this variant. It is recommended that you use ``use_reentrant=False```.

Parameters:

*   **functions** – A [`torch.nn.Sequential`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Sequential.html#torch.nn.Sequential "torch.nn.Sequential")
     or the list of modules or functions (comprising the model) to run sequentially.
    
*   **segments** – Number of chunks to create in the model
    
*   **input** – A Tensor that is input to `functions`
    
*   **preserve\_rng\_state** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – Omit stashing and restoring the RNG state during each checkpoint. Default: `True`
    
*   **use\_reentrant** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – specify whether to use the activation checkpoint variant that requires reentrant autograd. This parameter should be passed explicitly. In version 2.5 we will raise an exception if `use_reentrant` is not passed. If `use_reentrant=False`, `checkpoint` will use an implementation that does not require reentrant autograd. This allows `checkpoint` to support additional functionality, such as working as expected with `torch.autograd.grad` and support for keyword arguments input into the checkpointed function.
    

Returns:

Output of running `functions` sequentially on `*inputs`

Example

\>>> model \= nn.Sequential(...)
\>>> input\_var \= checkpoint\_sequential(model, chunks, input\_var)

Copy to clipboard

torch.utils.checkpoint.set\_checkpoint\_debug\_enabled(_enabled_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/checkpoint.py#L53)
[#](https://docs.pytorch.org/docs/2.15/checkpoint.html#torch.utils.checkpoint.set_checkpoint_debug_enabled "Link to this definition")

Context manager that sets whether checkpoint should print additional debug information when running. See the `debug` flag for [`checkpoint()`](https://docs.pytorch.org/docs/2.15/checkpoint.html#torch.utils.checkpoint.checkpoint "torch.utils.checkpoint.checkpoint")
 for more information. Note that when set, this context manager overrides the value of `debug` passed to checkpoint. To defer to the local setting, pass `None` to this context.

Parameters:

**enabled** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
) – Whether checkpoint should print debug information. Default is ‘None’.

_class_ torch.utils.checkpoint.CheckpointPolicy(_value_, _names\=None_, _\*_, _module\=None_, _qualname\=None_, _type\=None_, _start\=1_, _boundary\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/checkpoint.py#L1480)
[#](https://docs.pytorch.org/docs/2.15/checkpoint.html#torch.utils.checkpoint.CheckpointPolicy "Link to this definition")

Enum for specifying the policy for checkpointing during backpropagation.

The following policies are supported:

*   `{MUST,PREFER}_SAVE`: The operation’s output will be saved during the forward pass and will not be recomputed during the backward pass
    
*   `{MUST,PREFER}_RECOMPUTE`: The operation’s output will not be saved during the forward pass and will be recomputed during the backward pass
    
*   `{MUST,PREFER}_CPU_OFFLOAD`: The operation’s output will be saved during the forward pass, offloaded to CPU, and reloaded to GPU during the backward pass
    

Use `MUST_*` over `PREFER_*` to indicate that the policy should not be overridden by other subsystems like torch.compile.

Note

A policy function that always returns `PREFER_RECOMPUTE` is equivalent to vanilla checkpointing.

A policy function that returns `PREFER_SAVE` every op is NOT equivalent to not using checkpointing. Using such a policy would save additional tensors not limited to ones that are actually needed for gradient computation.

For example, eager selective checkpointing overrides `PREFER_RECOMPUTE` to save the outputs of non-aliasing operators with an ordered effect. An operator may be explicitly registered with an ordered effect through `torch.library` or inferred to have one from non-whitelisted TorchBind arguments. This override does not apply to `MUST_RECOMPUTE` or operators in the `c10d` namespace.

_class_ torch.utils.checkpoint.SelectiveCheckpointContext(_\*_, _is\_recompute_, _op\_output\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/checkpoint.py#L1450)
[#](https://docs.pytorch.org/docs/2.15/checkpoint.html#torch.utils.checkpoint.SelectiveCheckpointContext "Link to this definition")

Context passed to policy function during selective checkpointing.

This class is used to pass relevant metadata to the policy function during selective checkpointing.

The policy function is only called during the forward pass. During recomputation, cached values are retrieved by index, so `is_recompute` is deprecated and always `False`.

Example

\>>>
\>>> def policy\_fn(ctx, op, \*args, \*\*kwargs):
\>>>    print(ctx.op\_output)
\>>>
\>>> context\_fn \= functools.partial(create\_selective\_checkpoint\_contexts, policy\_fn)
\>>>
\>>> out \= torch.utils.checkpoint.checkpoint(
\>>>     fn, x, y,
\>>>     use\_reentrant\=False,
\>>>     context\_fn\=context\_fn,
\>>> )

Copy to clipboard

torch.utils.checkpoint.create\_selective\_checkpoint\_contexts(_policy\_fn\_or\_list_, _allow\_cache\_entry\_mutation\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/checkpoint.py#L1737)
[#](https://docs.pytorch.org/docs/2.15/checkpoint.html#torch.utils.checkpoint.create_selective_checkpoint_contexts "Link to this definition")

Helper to avoid recomputing certain ops during activation checkpointing.

Use this with torch.utils.checkpoint.checkpoint to control which operations are recomputed during the backward pass.

Note

This API expresses selective activation checkpointing policies at the level of individual ATen operators. If you would rather define save/recompute decisions over regions of source code, we recommend trying the separate [torch\_remat](https://github.com/meta-pytorch/remat)
 package. Its region-based API lets you:

*   assign different policies to different uses of the same operator;
    
*   apply policies to arbitrary multi-operation code, including custom [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
     implementations, without wrapping the region in a custom operator;
    
*   in eager mode, retain only tensors needed for backward or subsequent recomputation instead of caching every output of a selected operator; and
    
*   avoid the eager-mode `TorchDispatchMode` overhead of per-operator policies.
    

`torch_remat` also provides eager-mode tracing and memory diagnostics for named regions, while its core save/recompute policy works with [`torch.compile()`](https://docs.pytorch.org/docs/2.15/generated/torch.compile.html#torch.compile "torch.compile")
.

Parameters:

*   **policy\_fn\_or\_list** (_Callable_ _or_ _List_) –
    
    *   If a policy function is provided, it should accept a [`SelectiveCheckpointContext`](https://docs.pytorch.org/docs/2.15/checkpoint.html#torch.utils.checkpoint.SelectiveCheckpointContext "torch.utils.checkpoint.SelectiveCheckpointContext")
        , the `OpOverload`, args and kwargs to the op, and return a [`CheckpointPolicy`](https://docs.pytorch.org/docs/2.15/checkpoint.html#torch.utils.checkpoint.CheckpointPolicy "torch.utils.checkpoint.CheckpointPolicy")
         enum value indicating whether the execution of the op should be recomputed or not.
        
    *   If a list of operations is provided, it is equivalent to a policy returning CheckpointPolicy.MUST\_SAVE for the specified operations and CheckpointPolicy.PREFER\_RECOMPUTE for all other operations.
        
    
*   **allow\_cache\_entry\_mutation** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – By default, an error is raised if any tensors cached by selective activation checkpoint are mutated in order to ensure correctness. If set to True, this check is disabled.
    

Returns:

A tuple of two context managers.

Example

\>>> import functools
\>>>
\>>> x \= torch.rand(10, 10, requires\_grad\=True)
\>>> y \= torch.rand(10, 10, requires\_grad\=True)
\>>>
\>>> ops\_to\_save \= \[\
\>>>    torch.ops.aten.mm.default,\
\>>> \]
\>>>
\>>> def policy\_fn(ctx, op, \*args, \*\*kwargs):
\>>>    if op in ops\_to\_save:
\>>>        return CheckpointPolicy.MUST\_SAVE
\>>>    else:
\>>>        return CheckpointPolicy.PREFER\_RECOMPUTE
\>>>
\>>> context\_fn \= functools.partial(create\_selective\_checkpoint\_contexts, policy\_fn)
\>>>
\>>> \# or equivalently
\>>> context\_fn \= functools.partial(create\_selective\_checkpoint\_contexts, ops\_to\_save)
\>>>
\>>> def fn(x, y):
\>>>     return torch.sigmoid(torch.matmul(torch.matmul(x, y), y)) \* y
\>>>
\>>> out \= torch.utils.checkpoint.checkpoint(
\>>>     fn, x, y,
\>>>     use\_reentrant\=False,
\>>>     context\_fn\=context\_fn,
\>>> )

Copy to clipboard

_class_ torch.utils.checkpoint.GraphExecGroup[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/checkpoint.py#L2072)
[#](https://docs.pytorch.org/docs/2.15/checkpoint.html#torch.utils.checkpoint.GraphExecGroup "Link to this definition")

Any checkpointed regions encountered by backward under the same instance of this context manager will trigger recompute at most once, even if there are multiple calls to backward.

Backward calls under the same instance of this context manager must execute over non-overlapping regions of the backward graph even if retain\_graph=True. In particular, any two backward call cannot use the same saved activation for gradient computation.

Note

This context manager only affects checkpoint with use\_reentrant=False, and is a no-op otherwise.

torch.utils.checkpoint.set\_checkpoint\_early\_stop(_enable_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/checkpoint.py#L935)
[#](https://docs.pytorch.org/docs/2.15/checkpoint.html#torch.utils.checkpoint.set_checkpoint_early_stop "Link to this definition")

Controls whether checkpoint should stop recomputation early.

By default, non-reentrant checkpoint stops recomputation as soon as it has computed all needed Tensors. This context manager can be used to disable that feature if it is problematic for your specific application.

This context manager only needs to be active when forward is run. It does not need to be active during backward.

Example:

\>>> message \= "saved tensors default hooks are disabled"
\>>> with set\_checkpoint\_early\_stop(False):
...     \# Any checkpoint under this context manager will respect this
...     \# context manager, even if its backward is performed outside.
...     out \= checkpoint(fn, inputs)
...
\>>> out.backward()

Copy to clipboard

torch.utils.checkpoint.set\_device\_states(_devices_, _states_, _\*_, _device\_type\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/checkpoint.py#L199)
[#](https://docs.pytorch.org/docs/2.15/checkpoint.html#torch.utils.checkpoint.set_device_states "Link to this definition")

Sets random number generator states for the specified devices.

Parameters:

*   **devices** – Device ids to set states for.
    
*   **states** – States to set.
    
*   **device\_type** – `device_type` of the devices to set states for. Default is the device returned by a call to `DefaultDeviceType.get_device_type()`, which is `cuda` if not changed by calling `DefaultDeviceType::set_device_type()`.
    

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/checkpoint.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/checkpoint.md.txt)

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