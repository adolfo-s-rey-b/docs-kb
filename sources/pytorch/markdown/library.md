Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/library.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/library.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/library.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/library.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/library.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/library.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/library.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/library.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/library.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/library.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/library.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/library.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/library.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/library.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/library.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/library.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/library.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/library.html)
[v1.13](https://docs.pytorch.org/docs/1.13/library.html)
[v1.12](https://docs.pytorch.org/docs/1.12/library.html)
[v1.11](https://docs.pytorch.org/docs/1.11/library.html)
[v1.10](https://docs.pytorch.org/docs/1.10/library.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/library.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/library.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/library.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/library.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/library.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/library.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/library.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/library.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/library.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/library.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/library.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/library.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/library.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/library.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/library.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/library.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/library.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/library.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/library.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/library.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/library.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/library.html)

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

torch.library[#](https://docs.pytorch.org/docs/2.15/library.html#module-torch.library "Link to this heading")

==============================================================================================================

Created On: Jun 13, 2022 | Last Updated On: May 19, 2026

torch.library is a collection of APIs for extending PyTorch’s core library of operators. It contains utilities for testing custom operators, creating new custom operators, and extending operators defined with PyTorch’s C++ operator registration APIs (e.g. aten operators).

For a detailed guide on effectively using these APIs, please see [PyTorch Custom Operators Landing Page](https://pytorch.org/tutorials/advanced/custom_ops_landing_page.html)
 for more details on how to effectively use these APIs.

Testing custom ops[#](https://docs.pytorch.org/docs/2.15/library.html#testing-custom-ops "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

Use [`torch.library.opcheck()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.opcheck "torch.library.opcheck")
 to test custom ops for incorrect usage of the Python torch.library and/or C++ TORCH\_LIBRARY APIs. Also, if your operator supports training, use [`torch.autograd.gradcheck()`](https://docs.pytorch.org/docs/2.15/autograd.html#module-torch.autograd.gradcheck "torch.autograd.gradcheck")
 to test that the gradients are mathematically correct.

torch.library.opcheck(_op_, _args_, _kwargs\=None_, _\*_, _test\_utils\=('test\_schema', 'test\_autograd\_registration', 'test\_faketensor', 'test\_aot\_dispatch\_dynamic')_, _raise\_exception\=True_, _atol\=None_, _rtol\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/library.py#L1798)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.opcheck "Link to this definition")

Given an operator and some sample arguments, tests if the operator is registered correctly.

That is, when you use the torch.library/TORCH\_LIBRARY APIs to create a custom op, you specified metadata (e.g. mutability info) about the custom op and these APIs require that the functions you pass them satisfy certain properties (e.g. no data pointer access in the fake/meta/abstract kernel) `opcheck` tests these metadata and properties.

Concretely, we test the following:

*   test\_schema: If the schema matches the implementation of the operator. For example: if the schema specifies a Tensor is mutated, then we check the implementation mutates the Tensor. If the schema specifies that we return a new Tensor, then we check that the implementation returns a new Tensor (instead of an existing one or a view of an existing one).
    
*   test\_autograd\_registration: If the operator supports training (autograd): we check that its autograd formula is registered via torch.library.register\_autograd or a manual registration to one or more DispatchKey::Autograd keys. Any other DispatchKey-based registrations may lead to undefined behavior.
    
*   test\_faketensor: If the operator has a FakeTensor kernel (and if it is correct). The FakeTensor kernel is necessary ( but not sufficient) for the operator to work with PyTorch compilation APIs (torch.compile/export/FX). We check that a FakeTensor kernel (also sometimes known as a meta kernel) was registered for the operator and that it is correct. This test takes the result of running the operator on real tensors and the result of running the operator on FakeTensors and checks that they have the same Tensor metadata (sizes/strides/dtype/device/etc).
    
*   test\_aot\_dispatch\_dynamic: If the operator has correct behavior with PyTorch compilation APIs (torch.compile/export/FX). This checks that the outputs (and gradients, if applicable) are the same under eager-mode PyTorch and torch.compile. This test is a superset of `test_faketensor` and is an e2e test; other things it tests are that the operator supports functionalization and that the backward pass (if it exists) also supports FakeTensor and functionalization.
    

For best results, please call `opcheck` multiple times with a representative set of inputs. If your operator supports autograd, please use `opcheck` with inputs with `requires_grad = True`; if your operator supports multiple devices (e.g. CPU and CUDA), please use `opcheck` with inputs on all supported devices.

Parameters:

*   **op** (_OpOverload_ _|_ _OpOverloadPacket_ _|_ [_CustomOpDef_](https://docs.pytorch.org/docs/2.15/library.html#torch._library.custom_ops.CustomOpDef "torch._library.custom_ops.CustomOpDef")
    ) – The operator. Must either be a function decorated with [`torch.library.custom_op()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.custom_op "torch.library.custom_op")
     or an OpOverload/OpOverloadPacket found in torch.ops.\* (e.g. torch.ops.aten.sin, torch.ops.mylib.foo)
    
*   **args** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    _\[_[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
    _,_ _...__\]_) – The args to the operator
    
*   **kwargs** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
    _\]_ _|_ _None_) – The kwargs to the operator
    
*   **test\_utils** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ [_Sequence_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_) – Tests that we should run. Default: all of them. Example: (“test\_schema”, “test\_faketensor”)
    
*   **raise\_exception** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If we should raise an exception on the first error. If False, we will return a dict with information on if each test passed or not.
    
*   **rtol** (_Optional__\[_[_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
    _\]_) – Relative tolerance for floating point comparisons. If specified `atol` must also be specified. If omitted, default values based on the `dtype` are selected (see the table in [`torch.testing.assert_close()`](https://docs.pytorch.org/docs/2.15/testing.html#torch.testing.assert_close "torch.testing.assert_close")
    ).
    
*   **atol** (_Optional__\[_[_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")\
    _\]_) – Absolute tolerance for floating point comparisons. If specified `rtol` must also be specified. If omitted, default values based on the `dtype` are selected (see the table in [`torch.testing.assert_close()`](https://docs.pytorch.org/docs/2.15/testing.html#torch.testing.assert_close "torch.testing.assert_close")
    ).
    

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\]

Warning

opcheck and [`torch.autograd.gradcheck()`](https://docs.pytorch.org/docs/2.15/autograd.html#module-torch.autograd.gradcheck "torch.autograd.gradcheck")
 test different things; opcheck tests if your usage of torch.library APIs is correct while [`torch.autograd.gradcheck()`](https://docs.pytorch.org/docs/2.15/autograd.html#module-torch.autograd.gradcheck "torch.autograd.gradcheck")
 tests if your autograd formula is mathematically correct. Use both to test custom ops that support gradient computation.

Example

\>>> @torch.library.custom\_op("mylib::numpy\_mul", mutates\_args\=())
\>>> def numpy\_mul(x: Tensor, y: float) \-> Tensor:
\>>>     x\_np \= x.numpy(force\=True)
\>>>     z\_np \= x\_np \* y
\>>>     return torch.from\_numpy(z\_np).to(x.device)
\>>>
\>>> @numpy\_mul.register\_fake
\>>> def \_(x, y):
\>>>     return torch.empty\_like(x)
\>>>
\>>> def setup\_context(ctx, inputs, output):
\>>>     y, \= inputs
\>>>     ctx.y \= y
\>>>
\>>> def backward(ctx, grad):
\>>>     return grad \* ctx.y, None
\>>>
\>>> numpy\_mul.register\_autograd(backward, setup\_context\=setup\_context)
\>>>
\>>> sample\_inputs \= \[\
\>>>     (torch.randn(3), 3.14),\
\>>>     (torch.randn(2, 3, device\='cuda'), 2.718),\
\>>>     (torch.randn(1, 10, requires\_grad\=True), 1.234),\
\>>>     (torch.randn(64, 64, device\='cuda', requires\_grad\=True), 90.18),\
\>>> \]
\>>>
\>>> for args in sample\_inputs:
\>>>     torch.library.opcheck(numpy\_mul, args)

Copy to clipboard

Creating new custom ops in Python[#](https://docs.pytorch.org/docs/2.15/library.html#creating-new-custom-ops-in-python "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

Use [`torch.library.custom_op()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.custom_op "torch.library.custom_op")
 to create new custom ops.

### Choosing the kind of custom op[#](https://docs.pytorch.org/docs/2.15/library.html#choosing-the-kind-of-custom-op "Link to this heading")

When defining a custom op, first decide what aliasing and mutation behavior the operator has. This choice determines the `mutates_args`, `tags`, return schema, and fake-kernel behavior.

Does the operator mutate any Tensor input?
  |
  +-- no --> Functional operator
  |         Use mutates\_args=().
  |         Return new Tensor objects that do not alias inputs or each other.
  |
  +-- yes --> Does it mutate the first positional Tensor argument and return it?
        |
        +-- yes --> In-place operator
        |          Use tags=torch.Tag.inplace.
        |          Use mutates\_args with exactly the first argument name.
        |          Return that same first argument.
        |
        +-- no --> Does it mutate keyword-only Tensor out= arguments and return them?
              |
              +-- yes --> out= operator
              |          Use tags=torch.Tag.out.
              |          Do not read from the out= tensors.
              |          Put mutable output tensors after \* as keyword-only args.
              |          Return all out= tensors in declaration order.
              |
              +-- no --> Mutable operator
                         Use mutates\_args for the mutated arguments.
                         Do not return mutated inputs or aliases of inputs.

Copy to clipboard

Functional operators are the simplest and should be preferred when possible. They should not mutate inputs, and their outputs should be fresh values that do not alias any input or other output.

Use `tags=torch.Tag.inplace` only for the conventional in-place shape: the first positional argument is a `Tensor`, it is the only mutated argument, and the operator returns that same `Tensor`. For example, an inferred in-place custom op has a schema shaped like:

(Tensor(a!) x, ...) -> Tensor(a!)

Copy to clipboard

Use `tags=torch.Tag.out` only for conventional `out=` variants: all mutable output tensors are keyword-only arguments, and the operator returns those outputs in declaration order. The implementation must write to `out=` tensors, but must not read from them. For example:

(Tensor x, \*, Tensor(a!) out) -> Tensor(a!)
(Tensor x, \*, Tensor(a!) out0, Tensor(b!) out1) -> (Tensor(a!), Tensor(b!))

Copy to clipboard

In-place and `out=` custom ops get an autogenerated fake kernel from their tag and schema. Registering a fake kernel for these ops is usually unnecessary, though it is still allowed if you need to override the autogenerated behavior. `out=` custom ops follow the same autograd rule as built-in `out=` operators: they do not support automatic differentiation when any argument requires grad.

Arbitrary aliasing, such as returning an alias of an input that is not one of the in-place or `out=` patterns above, is not supported by `custom_op`. PyTorch compiler transforms such as functionalization need to reason precisely about mutations and aliases, so custom op aliasing is intentionally limited to the conventional forms described here. If your operator mutates inputs but is not an in-place or `out=` operator, model it as a mutable operator and return no aliases of inputs.

The same operation can have different contracts depending on how it handles its outputs:

from torch import Tensor

@torch.library.custom\_op(
    "mylib::add\_inplace",
    mutates\_args\={"x"},
    tags\=torch.Tag.inplace,
)
def add\_inplace(x: Tensor, y: Tensor) \-> Tensor:
    x.add\_(y)
    return x

@torch.library.custom\_op(
    "mylib::add\_out",
    mutates\_args\={"out"},
    tags\=torch.Tag.out,
)
def add\_out(x: Tensor, y: Tensor, \*, out: Tensor) \-> Tensor:
    out.copy\_(x + y)
    return out

@torch.library.custom\_op("mylib::add\_mutate", mutates\_args\={"x"})
def add\_mutate(x: Tensor, y: Tensor) \-> None:
    x.add\_(y)

Copy to clipboard

More details on mutation, aliasing, and transforms

`custom_op` asks for a precise mutation and aliasing contract because PyTorch uses that contract in FakeTensor, autograd, functionalization, and `torch.compile`.

For a functional custom op, PyTorch assumes the operator does not mutate any input and that returned tensors are fresh values. This is the easiest kind of op for PyTorch transforms to reason about.

For an in-place custom op, `torch.Tag.inplace` gives PyTorch a stronger and more specific contract: the first Tensor argument is mutated and the returned Tensor is the same object. This lets PyTorch derive the fake behavior from the schema instead of requiring a separate fake kernel.

For an `out=` custom op, `torch.Tag.out` gives PyTorch the corresponding `out=`\-variant contract: keyword-only output tensors are mutated and returned in schema order. The `out=` tensors are output buffers only: the implementation must not use their current values as inputs. Like built-in `out=` operators, these custom ops do not support automatic differentiation when any argument requires grad.

For other mutable custom ops, use `mutates_args` to name the mutated arguments, but do not return mutated inputs or aliases of inputs. Arbitrary aliasing is hard for transforms because functionalization rewrites mutating programs into functional programs and must know exactly which returned tensors share storage with which inputs. `custom_op` therefore supports the conventional in-place and `out=` aliasing patterns directly, but does not model arbitrary view or alias relationships.

torch.library.custom\_op(_name_, _fn\=None_, _/_, _\*_, _mutates\_args_, _device\_types\=None_, _schema\=None_, _tags\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_library/custom_ops.py#L66)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.custom_op "Link to this definition")

Wraps a function into custom operator.

Reasons why you may want to create a custom op include: - Wrapping a third-party library or custom kernel to work with PyTorch subsystems like Autograd. - Preventing torch.compile/export/FX tracing from peeking inside your function.

This API is used as a decorator around a function (please see examples). The provided function must have type hints; these are needed to interface with PyTorch’s various subsystems.

Parameters:

*   **name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – A name for the custom op that looks like “{namespace}::{name}”, e.g. “mylib::my\_linear”. The name is used as the op’s stable identifier in PyTorch subsystems (e.g. torch.export, FX graphs). To avoid name collisions, please use your project name as the namespace; e.g. all custom ops in pytorch/fbgemm use “fbgemm” as the namespace.
    
*   **mutates\_args** (_Iterable__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\] or_ _"unknown"_) – The names of args that the function mutates. This MUST be accurate, otherwise, the behavior is undefined. If “unknown”, it pessimistically assumes that all inputs to the operator are being mutated.
    
*   **device\_types** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _None_ _|_ _Sequence__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_) – The device type(s) the function is valid for. If no device type is provided, then the function is used as the default implementation for all device types. Examples: “cpu”, “cuda”. When registering a device-specific implementation for an operator that accepts no Tensors, we require the operator to have a “device: torch.device argument”.
    
*   **schema** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _None_) – A schema string for the operator. If None (recommended) we’ll infer a schema for the operator from its type annotations. We recommend letting us infer a schema unless you have a specific reason not to. Example: “(Tensor x, int y) -> (Tensor, Tensor)”.
    
*   **tags** ([_Tag_](https://docs.pytorch.org/docs/2.15/torch.html#torch.Tag "torch.Tag")
     _|_ _Sequence__\[_[_Tag_](https://docs.pytorch.org/docs/2.15/torch.html#torch.Tag "torch.Tag")\
    _\]_ _|_ _None_) – one or more tags to apply to the operator. Use `torch.Tag.inplace` for operators that mutate their first Tensor argument and return it. Use `torch.Tag.out` for operators that mutate keyword-only output tensors and return them. Like PyTorch’s built-in `out=` operators, `torch.Tag.out` custom ops do not support autograd.
    

Return type:

[_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[[_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")\
\[\[…\], [object](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")\
\]\], [_CustomOpDef_](https://docs.pytorch.org/docs/2.15/library.html#torch._library.custom_ops.CustomOpDef "torch._library.custom_ops.CustomOpDef")\
\] | [_CustomOpDef_](https://docs.pytorch.org/docs/2.15/library.html#torch._library.custom_ops.CustomOpDef "torch._library.custom_ops.CustomOpDef")

The following types are supported for the wrapped function’s input parameters:

> *   Scalars: `int`, `float`, `bool`, `str`, `torch.types.Number`
>     
> *   Tensors: `torch.Tensor`
>     
> *   Enums/devices: `torch.dtype`, `torch.device`
>     
> *   Flat list of the same type: `list[torch.Tensor]`, `list[int]`, `list[float]`, `list[bool]`, `list[torch.types.Number]`
>     
> *   Optionals: `Optional` of any of the above scalar/tensor types
>     
> *   Types registered via `torch.library.register_custom_class()`
>     

The following types are supported for the return value:

> `torch.Tensor`, `list[torch.Tensor]`, `int`, `float`, `bool`, `torch.types.Number`.

Note

We recommend not passing in a `schema` arg and instead letting us infer it from the type annotations. It is error-prone to write your own schema. You may wish to provide your own schema if our interpretation of the type annotation is not what you want. For more info on how to write a schema string, see [here](https://github.com/pytorch/pytorch/blob/main/aten/src/ATen/native/README.md#func)

Examples::

\>>> import torch
\>>> from torch import Tensor
\>>> from torch.library import custom\_op
\>>> import numpy as np
\>>>
\>>> @custom\_op("mylib::numpy\_sin", mutates\_args\=())
\>>> def numpy\_sin(x: Tensor) \-> Tensor:
\>>>     x\_np \= x.cpu().numpy()
\>>>     y\_np \= np.sin(x\_np)
\>>>     return torch.from\_numpy(y\_np).to(device\=x.device)
\>>>
\>>> x \= torch.randn(3)
\>>> y \= numpy\_sin(x)
\>>> assert torch.allclose(y, x.sin())
\>>>
\>>> \# Example of a custom op that only works for one device type.
\>>> @custom\_op("mylib::numpy\_sin\_cpu", mutates\_args\=(), device\_types\="cpu")
\>>> def numpy\_sin\_cpu(x: Tensor) \-> Tensor:
\>>>     x\_np \= x.numpy()
\>>>     y\_np \= np.sin(x\_np)
\>>>     return torch.from\_numpy(y\_np)
\>>>
\>>> x \= torch.randn(3)
\>>> y \= numpy\_sin\_cpu(x)
\>>> assert torch.allclose(y, x.sin())
\>>>
\>>> \# Example of a custom op that mutates an input
\>>> @custom\_op("mylib::numpy\_sin\_inplace", mutates\_args\={"x"}, device\_types\="cpu")
\>>> def numpy\_sin\_inplace(x: Tensor) \-> None:
\>>>     x\_np \= x.numpy()
\>>>     np.sin(x\_np, out\=x\_np)
\>>>
\>>> x \= torch.randn(3)
\>>> expected \= x.sin()
\>>> numpy\_sin\_inplace(x)
\>>> assert torch.allclose(x, expected)
\>>>
\>>> \# Example of a custom op with inplace semantics
\>>> @custom\_op(
\>>>     "mylib::numpy\_sin\_",
\>>>     mutates\_args\={"x"},
\>>>     device\_types\="cpu",
\>>>     tags\=torch.Tag.inplace,
\>>> )
\>>> def numpy\_sin\_(x: Tensor) \-> Tensor:
\>>>     x\_np \= x.numpy()
\>>>     np.sin(x\_np, out\=x\_np)
\>>>     return x
\>>>
\>>> x \= torch.randn(3)
\>>> expected \= x.sin()
\>>> result \= numpy\_sin\_(x)
\>>> assert result is x
\>>> assert torch.allclose(x, expected)
\>>>
\>>> \# Example of a custom op with out= semantics
\>>> @custom\_op(
\>>>     "mylib::numpy\_sin\_out",
\>>>     mutates\_args\={"out"},
\>>>     device\_types\="cpu",
\>>>     tags\=torch.Tag.out,
\>>> )
\>>> def numpy\_sin\_out(x: Tensor, \*, out: Tensor) \-> Tensor:
\>>>     x\_np \= x.numpy()
\>>>     out\_np \= out.numpy()
\>>>     np.sin(x\_np, out\=out\_np)
\>>>     return out
\>>>
\>>> x \= torch.randn(3)
\>>> out \= torch.empty\_like(x)
\>>> result \= numpy\_sin\_out(x, out\=out)
\>>> assert result is out
\>>> assert torch.allclose(out, x.sin())
\>>>
\>>> \# Example of a factory function
\>>> @torch.library.custom\_op("mylib::bar", mutates\_args\={}, device\_types\="cpu")
\>>> def bar(device: torch.device) \-> Tensor:
\>>>     return torch.ones(3)
\>>>
\>>> bar("cpu")
\>>>
\>>> \# Example of a custom op with list inputs
\>>> @custom\_op("mylib::weighted\_sum", mutates\_args\=())
\>>> def weighted\_sum(
\>>>     tensors: list\[Tensor\],
\>>>     weights: list\[float\],
\>>> ) \-> Tensor:
\>>>     return sum(t \* w for t, w in zip(tensors, weights))
\>>>
\>>> x \= torch.randn(3)
\>>> y \= torch.randn(3)
\>>> out \= weighted\_sum(\[x, y\], \[0.3, 0.7\])

Copy to clipboard

torch.library.triton\_op(_name_, _fn\=None_, _/_, _\*_, _mutates\_args_, _schema\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_library/triton.py#L296)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.triton_op "Link to this definition")

Create a custom operator whose implementation is backed by 1+ triton kernels.

This is a more structured way of using triton kernels with PyTorch. Prefer using triton kernels with no `torch.library` custom operator wrappers (like [`torch.library.custom_op()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.custom_op "torch.library.custom_op")
, [`torch.library.triton_op()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.triton_op "torch.library.triton_op")
) because that is simpler; only use [`torch.library.custom_op()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.custom_op "torch.library.custom_op")
/[`torch.library.triton_op()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.triton_op "torch.library.triton_op")
 if you want to create an operator that behaves like PyTorch built-in operators. For example, you may use a `torch.library` wrapper API to define the behavior of the triton kernel when passed a tensor subclass or under a TorchDispatchMode.

Use [`torch.library.triton_op()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.triton_op "torch.library.triton_op")
 instead of [`torch.library.custom_op()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.custom_op "torch.library.custom_op")
 when the implementation consists of 1+ triton kernels. [`torch.library.custom_op()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.custom_op "torch.library.custom_op")
 treats custom operators as opaque ([`torch.compile()`](https://docs.pytorch.org/docs/2.15/generated/torch.compile.html#torch.compile "torch.compile")
 and [`torch.export.export()`](https://docs.pytorch.org/docs/2.15/user_guide/torch_compiler/export/api_reference.html#torch.export.export "torch.export.export")
 will never trace into them), but `triton_op` makes the implementation visible to these subsystems, allowing them to optimize the triton kernel(s).

Note that `fn` must only consist of calls to PyTorch-understood operators and triton kernels. Any triton kernels called inside `fn` must be wrapped in a call to [`torch.library.wrap_triton()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.wrap_triton "torch.library.wrap_triton")
.

Parameters:

*   **name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – A name for the custom op that looks like “{namespace}::{name}”, e.g. “mylib::my\_linear”. The name is used as the op’s stable identifier in PyTorch subsystems (e.g. torch.export, FX graphs). To avoid name collisions, please use your project name as the namespace; e.g. all custom ops in pytorch/fbgemm use “fbgemm” as the namespace.
    
*   **mutates\_args** (_Iterable__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\] or_ _"unknown"_) – The names of args that the function mutates. This MUST be accurate, otherwise, the behavior is undefined. If “unknown”, it pessimistically assumes that all inputs to the operator are being mutated.
    
*   **schema** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _None_) – A schema string for the operator. If None (recommended) we’ll infer a schema for the operator from its type annotations. We recommend letting us infer a schema unless you have a specific reason not to. Example: “(Tensor x, int y) -> (Tensor, Tensor)”.
    

Return type:

[_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")

Example:

\>>> import torch
\>>> from torch.library import triton\_op, wrap\_triton
\>>>
\>>> import triton
\>>> from triton import language as tl
\>>>
\>>> @triton.jit
\>>> def add\_kernel(
\>>>     in\_ptr0,
\>>>     in\_ptr1,
\>>>     out\_ptr,
\>>>     n\_elements,
\>>>     BLOCK\_SIZE: "tl.constexpr",
\>>> ):
\>>>     pid \= tl.program\_id(axis\=0)
\>>>     block\_start \= pid \* BLOCK\_SIZE
\>>>     offsets \= block\_start + tl.arange(0, BLOCK\_SIZE)
\>>>     mask \= offsets < n\_elements
\>>>     x \= tl.load(in\_ptr0 + offsets, mask\=mask)
\>>>     y \= tl.load(in\_ptr1 + offsets, mask\=mask)
\>>>     output \= x + y
\>>>     tl.store(out\_ptr + offsets, output, mask\=mask)
\>>>
\>>> @triton\_op("mylib::add", mutates\_args\={})
\>>> def add(x: torch.Tensor, y: torch.Tensor) \-> torch.Tensor:
\>>>     output \= torch.empty\_like(x)
\>>>     n\_elements \= output.numel()
\>>>
\>>>     def grid(meta):
\>>>         return (triton.cdiv(n\_elements, meta\["BLOCK\_SIZE"\]),)
\>>>
\>>>     \# NB: we need to wrap the triton kernel in a call to wrap\_triton
\>>>     wrap\_triton(add\_kernel)\[grid\](x, y, output, n\_elements, 16)
\>>>     return output
\>>>
\>>> @torch.compile
\>>> def f(x, y):
\>>>     return add(x, y)
\>>>
\>>> x \= torch.randn(3, device\="cuda")
\>>> y \= torch.randn(3, device\="cuda")
\>>>
\>>> z \= f(x, y)
\>>> assert torch.allclose(z, x + y)

Copy to clipboard

torch.library.wrap\_triton(_triton\_kernel_, _/_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_library/triton.py#L534)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.wrap_triton "Link to this definition")

Allows capture of a triton kernel into a graph via make\_fx or non-strict `torch.export`.

These technologies perform Dispatcher-based tracing (via `__torch_dispatch__`) and cannot see calls to raw triton kernels. The `wrap_triton` API wraps a triton kernel into a callable that can actually be traced into a graph.

Please use this API together with [`torch.library.triton_op()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.triton_op "torch.library.triton_op")
.

Examples

\>>> import torch
\>>> import triton
\>>> from triton import language as tl
\>>> from torch.fx.experimental.proxy\_tensor import make\_fx
\>>> from torch.library import wrap\_triton
\>>>
\>>> @triton.jit
\>>> def add\_kernel(
\>>>     in\_ptr0,
\>>>     in\_ptr1,
\>>>     out\_ptr,
\>>>     n\_elements,
\>>>     BLOCK\_SIZE: "tl.constexpr",
\>>> ):
\>>>     pid \= tl.program\_id(axis\=0)
\>>>     block\_start \= pid \* BLOCK\_SIZE
\>>>     offsets \= block\_start + tl.arange(0, BLOCK\_SIZE)
\>>>     mask \= offsets < n\_elements
\>>>     x \= tl.load(in\_ptr0 + offsets, mask\=mask)
\>>>     y \= tl.load(in\_ptr1 + offsets, mask\=mask)
\>>>     output \= x + y
\>>>     tl.store(out\_ptr + offsets, output, mask\=mask)
\>>>
\>>> def add(x, y):
\>>>     output \= torch.empty\_like(x)
\>>>     n\_elements \= output.numel()
\>>>
\>>>     def grid\_fn(meta):
\>>>         return (triton.cdiv(n\_elements, meta\["BLOCK\_SIZE"\]),)
\>>>
\>>>     wrap\_triton(add\_kernel)\[grid\_fn\](x, y, output, n\_elements, 16)
\>>>     return output
\>>>
\>>> x \= torch.randn(3, device\="cuda")
\>>> y \= torch.randn(3, device\="cuda")
\>>> gm \= make\_fx(add)(x, y)
\>>> print(gm.code)
\>>> \# def forward(self, x\_1, y\_1):
\>>> \#     empty\_like = torch.ops.aten.empty\_like.default(x\_1, pin\_memory = False)
\>>> \#     triton\_kernel\_wrapper\_mutation\_proxy = triton\_kernel\_wrapper\_mutation(
\>>> \#         kernel\_idx = 0, constant\_args\_idx = 0,
\>>> \#         grid = \[(1, 1, 1)\], kwargs = {
\>>> \#             'in\_ptr0': x\_1, 'in\_ptr1': y\_1, 'out\_ptr': empty\_like,
\>>> \#             'n\_elements': 3, 'BLOCK\_SIZE': 16
\>>> \#         })
\>>> \#     return empty\_like

Copy to clipboard

Return type:

[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")

Extending custom ops (created from Python or C++)[#](https://docs.pytorch.org/docs/2.15/library.html#extending-custom-ops-created-from-python-or-c "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use the `register.*` methods, such as [`torch.library.register_kernel()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.register_kernel "torch.library.register_kernel")
 and [`torch.library.register_fake()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.register_fake "torch.library.register_fake")
, to add implementations for any operators (they may have been created using [`torch.library.custom_op()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.custom_op "torch.library.custom_op")
 or via PyTorch’s C++ operator registration APIs).

torch.library.register\_kernel(_op_, _device\_types_, _func\=None_, _/_, _\*_, _lib\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/library.py#L1017)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.register_kernel "Link to this definition")

Register an implementation for a device type for this operator.

Some valid device\_types are: “cpu”, “cuda”, “xla”, “mps”, “ipu”, “xpu”. This API may be used as a decorator.

Parameters:

*   **op** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _OpOverload_) – The operator to register an impl to.
    
*   **device\_types** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _None_ _|_ _Sequence__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_) – The device\_types to register an impl to. If None, we will register to all device types – please only use this option if your implementation is truly device-type-agnostic.
    
*   **func** (_Callable_) – The function to register as the implementation for the given device types.
    
*   **lib** (_Optional__\[_[_Library_](https://docs.pytorch.org/docs/2.15/library.html#torch.library.Library "torch.library.Library")\
    _\]_) – If provided, the lifetime of this registration
    

Examples::

\>>> import torch
\>>> from torch import Tensor
\>>> from torch.library import custom\_op
\>>> import numpy as np
\>>>
\>>> \# Create a custom op that works on cpu
\>>> @custom\_op("mylib::numpy\_sin", mutates\_args\=(), device\_types\="cpu")
\>>> def numpy\_sin(x: Tensor) \-> Tensor:
\>>>     x\_np \= x.numpy()
\>>>     y\_np \= np.sin(x\_np)
\>>>     return torch.from\_numpy(y\_np)
\>>>
\>>> \# Add implementations for the cuda device
\>>> @torch.library.register\_kernel("mylib::numpy\_sin", "cuda")
\>>> def \_(x):
\>>>     x\_np \= x.cpu().numpy()
\>>>     y\_np \= np.sin(x\_np)
\>>>     return torch.from\_numpy(y\_np).to(device\=x.device)
\>>>
\>>> x\_cpu \= torch.randn(3)
\>>> x\_cuda \= x\_cpu.cuda()
\>>> assert torch.allclose(numpy\_sin(x\_cpu), x\_cpu.sin())
\>>> assert torch.allclose(numpy\_sin(x\_cuda), x\_cuda.sin())

Copy to clipboard

torch.library.register\_autocast(_op_, _device\_type_, _cast\_inputs_, _/_, _\*_, _lib\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/library.py#L1076)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.register_autocast "Link to this definition")

Register an autocast dispatch rule for this custom op.

Valid `device_type` values include any device type that supports autocast. See `torch.amp.is_autocast_available()` for details.

Parameters:

*   **op** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _OpOverload_) – The operator to register an autocast dispatch rule to.
    
*   **device\_type** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Device type to use. ‘cuda’, ‘cpu’, ‘xpu’, or any other device type that supports autocast. The type is the same as the type attribute of a [`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    . Thus, you may obtain the device type of a tensor using Tensor.device.type.
    
*   **cast\_inputs** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    ) – When custom op runs in an autocast-enabled region, casts incoming floating-point Tensors to the target dtype (non-floating-point Tensors are not affected), then executes custom op with autocast disabled.
    
*   **lib** (_Optional__\[_[_Library_](https://docs.pytorch.org/docs/2.15/library.html#torch.library.Library "torch.library.Library")\
    _\]_) – If provided, the lifetime of this registration
    

Examples::

\>>> import torch
\>>> from torch import Tensor
\>>> from torch.library import custom\_op
\>>>
\>>> \# Create a custom op that works on cuda
\>>> @torch.library.custom\_op("mylib::my\_sin", mutates\_args\=())
\>>> def my\_sin(x: Tensor) \-> Tensor:
\>>>     return torch.sin(x)
\>>>
\>>> \# Register autocast dispatch rule for the cuda device
\>>> torch.library.register\_autocast("mylib::my\_sin", "cuda", torch.float16)
\>>>
\>>> x \= torch.randn(3, dtype\=torch.float32, device\="cuda")
\>>> with torch.autocast("cuda", dtype\=torch.float16):
\>>>     y \= torch.ops.mylib.my\_sin(x)
\>>> assert y.dtype \== torch.float16

Copy to clipboard

torch.library.register\_autograd(_op_, _backward_, _/_, _\*_, _setup\_context\=None_, _lib\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/library.py#L1322)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.register_autograd "Link to this definition")

Register a backward formula for this custom op.

In order for an operator to work with autograd, you need to register a backward formula: 1. You must tell us how to compute gradients during the backward pass by providing us a “backward” function. 2. If you need any values from the forward to compute gradients, you can use setup\_context to save values for backward.

`backward` runs during the backward pass. It accepts `(ctx, *grads)`: - `grads` is one or more gradients. The number of gradients matches the number of outputs of the operator. The `ctx` object is [the same ctx object](https://docs.pytorch.org/docs/2.15/context_method_mixins)
 used by [`torch.autograd.Function`](https://docs.pytorch.org/docs/2.15/autograd.html#torch.autograd.Function "torch.autograd.Function")
. The semantics of `backward_fn` are the same as [`torch.autograd.Function.backward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.Function.backward.html#torch.autograd.Function.backward "torch.autograd.Function.backward")
.

Warning

The strides of the gradients passed to `backward_fn` are undefined: they may not match the strides of the corresponding forward outputs (for example, the backward of [`torch.cat()`](https://docs.pytorch.org/docs/2.15/generated/torch.cat.html#torch.cat "torch.cat")
 produces gradients that are non-contiguous views into a larger tensor). If `backward_fn` calls a kernel that assumes a particular memory layout (such as a raw Triton or CUDA kernel), it must call [`contiguous()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.contiguous.html#torch.Tensor.contiguous "torch.Tensor.contiguous")
 on the gradients or handle their strides explicitly. Backward formulas composed of PyTorch operations handle arbitrary strides automatically.

`setup_context(ctx, inputs, output)` runs during the forward pass. Please save quantities needed for backward onto the `ctx` object via either [`torch.autograd.function.FunctionCtx.save_for_backward()`](https://docs.pytorch.org/docs/2.15/generated/torch.autograd.function.FunctionCtx.save_for_backward.html#torch.autograd.function.FunctionCtx.save_for_backward "torch.autograd.function.FunctionCtx.save_for_backward")
 or assigning them as attributes of `ctx`. If your custom op has kwarg-only arguments, we expect the signature of `setup_context` to be `setup_context(ctx, inputs, keyword_only_inputs, output)`.

Both `setup_context_fn` and `backward_fn` must be traceable. That is, they may not directly access [`torch.Tensor.data_ptr()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.data_ptr.html#torch.Tensor.data_ptr "torch.Tensor.data_ptr")
 and they must not depend on or mutate global state. If you need a non-traceable backward, you can make it a separate custom\_op that you call inside `backward_fn`.

If you need different autograd behavior on different devices, then we recommend creating two different custom operators, one for each device that needs different behavior, and switching between them at runtime.

Examples

\>>> import torch
\>>> import numpy as np
\>>> from torch import Tensor
\>>>
\>>> @torch.library.custom\_op("mylib::numpy\_sin", mutates\_args\=())
\>>> def numpy\_sin(x: Tensor) \-> Tensor:
\>>>     x\_np \= x.cpu().numpy()
\>>>     y\_np \= np.sin(x\_np)
\>>>     return torch.from\_numpy(y\_np).to(device\=x.device)
\>>>
\>>> def setup\_context(ctx, inputs, output) \-> Tensor:
\>>>     x, \= inputs
\>>>     ctx.save\_for\_backward(x)
\>>>
\>>> def backward(ctx, grad):
\>>>     x, \= ctx.saved\_tensors
\>>>     return grad \* x.cos()
\>>>
\>>> torch.library.register\_autograd(
...     "mylib::numpy\_sin", backward, setup\_context\=setup\_context
... )
\>>>
\>>> x \= torch.randn(3, requires\_grad\=True)
\>>> y \= numpy\_sin(x)
\>>> (grad\_x,) \= torch.autograd.grad(y, x, torch.ones\_like(y))
\>>> assert torch.allclose(grad\_x, x.cos())
\>>>
\>>> \# Example with a keyword-only arg
\>>> @torch.library.custom\_op("mylib::numpy\_mul", mutates\_args\=())
\>>> def numpy\_mul(x: Tensor, \*, val: float) \-> Tensor:
\>>>     x\_np \= x.cpu().numpy()
\>>>     y\_np \= x\_np \* val
\>>>     return torch.from\_numpy(y\_np).to(device\=x.device)
\>>>
\>>> def setup\_context(ctx, inputs, keyword\_only\_inputs, output) \-> Tensor:
\>>>     ctx.val \= keyword\_only\_inputs\["val"\]
\>>>
\>>> def backward(ctx, grad):
\>>>     return grad \* ctx.val
\>>>
\>>> torch.library.register\_autograd(
...     "mylib::numpy\_mul", backward, setup\_context\=setup\_context
... )
\>>>
\>>> x \= torch.randn(3, requires\_grad\=True)
\>>> y \= numpy\_mul(x, val\=3.14)
\>>> (grad\_x,) \= torch.autograd.grad(y, x, torch.ones\_like(y))
\>>> assert torch.allclose(grad\_x, torch.full\_like(x, 3.14))

Copy to clipboard

torch.library.register\_fake(_op_, _func\=None_, _/_, _\*_, _lib\=None_, _\_stacklevel\=1_, _allow\_override\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/library.py#L1159)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.register_fake "Link to this definition")

Register a FakeTensor implementation (“fake impl”) for this operator.

Also sometimes known as a “meta kernel”, “abstract impl”.

An “FakeTensor implementation” specifies the behavior of this operator on Tensors that carry no data (“FakeTensor”). Given some input Tensors with certain properties (sizes/strides/storage\_offset/device), it specifies what the properties of the output Tensors are.

The FakeTensor implementation has the same signature as the operator. It is run for both FakeTensors and meta tensors. To write a FakeTensor implementation, assume that all Tensor inputs to the operator are regular CPU/CUDA/Meta tensors, but they do not have storage, and you are trying to return regular CPU/CUDA/Meta tensor(s) as output. The FakeTensor implementation must consist of only PyTorch operations (and may not directly access the storage or data of any input or intermediate Tensors).

This API may be used as a decorator (see examples).

For a detailed guide on custom ops, please see [https://pytorch.org/tutorials/advanced/custom\_ops\_landing\_page.html](https://pytorch.org/tutorials/advanced/custom_ops_landing_page.html)

Parameters:

*   **op\_name** – Operator name (along with the overload) or OpOverload object.
    
*   **func** ([_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
     _|_ _None_) – Fake tensor implementation.
    
*   **lib** (_Optional__\[_[_Library_](https://docs.pytorch.org/docs/2.15/library.html#torch.library.Library "torch.library.Library")\
    _\]_) – Library to register the fake tensor to.
    
*   **allow\_override** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Flag controlling if we want to override an existing registered fake impl. This is on by default; pass `False` to error if the operator already has a fake impl. This also only applies if the custom operator was not created via torch.library.custom\_op, as overriding an existing fake impl is already allowed.
    

Examples

\>>> import torch
\>>> import numpy as np
\>>> from torch import Tensor
\>>>
\>>> \# Example 1: an operator without data-dependent output shape
\>>> @torch.library.custom\_op("mylib::custom\_linear", mutates\_args\=())
\>>> def custom\_linear(x: Tensor, weight: Tensor, bias: Tensor) \-> Tensor:
\>>>     raise NotImplementedError("Implementation goes here")
\>>>
\>>> @torch.library.register\_fake("mylib::custom\_linear")
\>>> def \_(x, weight, bias):
\>>>     assert x.dim() \== 2
\>>>     assert weight.dim() \== 2
\>>>     assert bias.dim() \== 1
\>>>     assert x.shape\[1\] \== weight.shape\[1\]
\>>>     assert weight.shape\[0\] \== bias.shape\[0\]
\>>>     assert x.device \== weight.device
\>>>
\>>>     return (x @ weight.t()) + bias
\>>>
\>>> with torch.\_subclasses.fake\_tensor.FakeTensorMode():
\>>>     x \= torch.randn(2, 3)
\>>>     w \= torch.randn(3, 3)
\>>>     b \= torch.randn(3)
\>>>     y \= torch.ops.mylib.custom\_linear(x, w, b)
\>>>
\>>> assert y.shape \== (2, 3)
\>>>
\>>> \# Example 2: an operator with data-dependent output shape
\>>> @torch.library.custom\_op("mylib::custom\_nonzero", mutates\_args\=())
\>>> def custom\_nonzero(x: Tensor) \-> Tensor:
\>>>     x\_np \= x.numpy(force\=True)
\>>>     res \= np.stack(np.nonzero(x\_np), axis\=1)
\>>>     return torch.tensor(res, device\=x.device)
\>>>
\>>> @torch.library.register\_fake("mylib::custom\_nonzero")
\>>> def \_(x):
\>>> \# Number of nonzero-elements is data-dependent.
\>>> \# Since we cannot peek at the data in a fake impl,
\>>> \# we use the ctx object to construct a new symint that
\>>> \# represents the data-dependent size.
\>>>     ctx \= torch.library.get\_ctx()
\>>>     nnz \= ctx.new\_dynamic\_size()
\>>>     shape \= \[nnz, x.dim()\]
\>>>     result \= x.new\_empty(shape, dtype\=torch.int64)
\>>>     return result
\>>>
\>>> from torch.fx.experimental.proxy\_tensor import make\_fx
\>>>
\>>> x \= torch.tensor(\[0, 1, 2, 3, 4, 0\])
\>>> trace \= make\_fx(torch.ops.mylib.custom\_nonzero, tracing\_mode\="symbolic")(x)
\>>> trace.print\_readable()
\>>>
\>>> assert torch.allclose(trace(x), torch.ops.mylib.custom\_nonzero(x))

Copy to clipboard

torch.library.register\_vmap(_op_, _func\=None_, _/_, _\*_, _lib\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/library.py#L1525)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.register_vmap "Link to this definition")

Register a vmap implementation to support [`torch.vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
 for this custom op.

This API may be used as a decorator (see examples).

In order for an operator to work with [`torch.vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
, you may need to register a vmap implementation in the following signature:

> `vmap_func(info, in_dims: Tuple[Optional[int]], *args, **kwargs)`,

where `*args` and `**kwargs` are the arguments and kwargs for `op`. We do not support kwarg-only Tensor args.

It specifies how do we compute the batched version of `op` given inputs with an additional dimension (specified by `in_dims`).

For each arg in `args`, `in_dims` has a corresponding `Optional[int]`. It is `None` if the arg is not a Tensor or if the arg is not being vmapped over, otherwise, it is an integer specifying what dimension of the Tensor is being vmapped over.

`info` is a collection of additional metadata that may be helpful: `info.batch_size` specifies the size of the dimension being vmapped over, while `info.randomness` is the `randomness` option that was passed to [`torch.vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
.

The return of the function `func` is a tuple of `(output, out_dims)`. Similar to `in_dims`, `out_dims` should be of the same structure as `output` and contain one `out_dim` per output that specifies if the output has the vmapped dimension and what index it is in.

Examples

\>>> import torch
\>>> import numpy as np
\>>> from torch import Tensor
\>>> from typing import Tuple
\>>>
\>>> def to\_numpy(tensor):
\>>>     return tensor.cpu().numpy()
\>>>
\>>> lib \= torch.library.Library("mylib", "FRAGMENT")
\>>> @torch.library.custom\_op("mylib::numpy\_cube", mutates\_args\=())
\>>> def numpy\_cube(x: Tensor) \-> Tuple\[Tensor, Tensor\]:
\>>>     x\_np \= to\_numpy(x)
\>>>     dx \= torch.tensor(3 \* x\_np \*\* 2, device\=x.device)
\>>>     return torch.tensor(x\_np \*\* 3, device\=x.device), dx
\>>>
\>>> def numpy\_cube\_vmap(info, in\_dims, x):
\>>>     result \= numpy\_cube(x)
\>>>     return result, (in\_dims\[0\], in\_dims\[0\])
\>>>
\>>> torch.library.register\_vmap(numpy\_cube, numpy\_cube\_vmap)
\>>>
\>>> x \= torch.randn(3)
\>>> torch.vmap(numpy\_cube)(x)
\>>>
\>>> @torch.library.custom\_op("mylib::numpy\_mul", mutates\_args\=())
\>>> def numpy\_mul(x: Tensor, y: Tensor) \-> Tensor:
\>>>     return torch.tensor(to\_numpy(x) \* to\_numpy(y), device\=x.device)
\>>>
\>>> @torch.library.register\_vmap("mylib::numpy\_mul")
\>>> def numpy\_mul\_vmap(info, in\_dims, x, y):
\>>>     x\_bdim, y\_bdim \= in\_dims
\>>>     x \= x.movedim(x\_bdim, \-1) if x\_bdim is not None else x.unsqueeze(\-1)
\>>>     y \= y.movedim(y\_bdim, \-1) if y\_bdim is not None else y.unsqueeze(\-1)
\>>>     result \= x \* y
\>>>     result \= result.movedim(\-1, 0)
\>>>     return result, 0
\>>>
\>>>
\>>> x \= torch.randn(3)
\>>> y \= torch.randn(3)
\>>> torch.vmap(numpy\_mul)(x, y)

Copy to clipboard

Note

The vmap function should aim to preserve the semantics of the entire custom operator. That is, `grad(vmap(op))` should be replaceable with a `grad(map(op))`.

If your custom operator has any custom behavior in the backward pass, please keep this in mind.

torch.library.impl\_abstract(_qualname_, _func\=None_, _\*_, _lib\=None_, _\_stacklevel\=1_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/library.py#L973)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.impl_abstract "Link to this definition")

This API was renamed to [`torch.library.register_fake()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.register_fake "torch.library.register_fake")
 in PyTorch 2.4. Please use that instead.

torch.library.get\_ctx()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/library.py#L1707)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.get_ctx "Link to this definition")

get\_ctx() returns the current AbstractImplCtx object.

Calling `get_ctx()` is only valid inside of a fake impl (see [`torch.library.register_fake()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.register_fake "torch.library.register_fake")
 for more usage details.

Return type:

_FakeImplCtx_

torch.library.register\_torch\_dispatch(_op_, _torch\_dispatch\_class_, _func\=None_, _/_, _\*_, _lib\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/library.py#L1457)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.register_torch_dispatch "Link to this definition")

Registers a torch\_dispatch rule for the given operator and `torch_dispatch_class`.

This allows for open registration to specify the behavior between the operator and the `torch_dispatch_class` without needing to modify the `torch_dispatch_class` or the operator directly.

The `torch_dispatch_class` is either a Tensor subclass with `__torch_dispatch__` or a TorchDispatchMode.

If it is a Tensor subclass, we expect `func` to have the following signature: `(cls, func: OpOverload, types: Tuple[type, ...], args, kwargs) -> Any`

If it is a TorchDispatchMode, we expect `func` to have the following signature: `(mode, func: OpOverload, types: Tuple[type, ...], args, kwargs) -> Any`

`args` and `kwargs` will have been normalized the same way they are in `__torch_dispatch__` (see [\_\_torch\_dispatch\_\_ calling convention](https://docs.pytorch.org/docs/2.15/notes/extending.html#torch-dispatch-calling-convention)
).

Examples

\>>> import torch
\>>>
\>>> @torch.library.custom\_op("mylib::foo", mutates\_args\={})
\>>> def foo(x: torch.Tensor) \-> torch.Tensor:
\>>>     return x.clone()
\>>>
\>>> class MyMode(torch.utils.\_python\_dispatch.TorchDispatchMode):
\>>>     def \_\_torch\_dispatch\_\_(self, func, types, args\=(), kwargs\=None):
\>>>         return func(\*args, \*\*kwargs)
\>>>
\>>> @torch.library.register\_torch\_dispatch("mylib::foo", MyMode)
\>>> def \_(mode, func, types, args, kwargs):
\>>>     x, \= args
\>>>     return x + 1
\>>>
\>>> x \= torch.randn(3)
\>>> y \= foo(x)
\>>> assert torch.allclose(y, x)
\>>>
\>>> with MyMode():
\>>>     y \= foo(x)
\>>> assert torch.allclose(y, x + 1)

Copy to clipboard

torch.library.infer\_schema(_prototype\_function_, _/_, _\*_, _mutates\_args_, _op\_name\=None_, _tags\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_library/infer_schema.py#L23)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.infer_schema "Link to this definition")

Parses the schema of a given function with type hints. The schema is inferred from the function’s type hints, and can be used to define a new operator.

We make the following assumptions:

*   None of the outputs alias any of the inputs or each other.
    
*   String type annotations “device, dtype, Tensor, types” without library specification are
    
    assumed to be torch.\*. Similarly, string type annotations “Optional, List, Sequence, Union”
    
    without library specification are assumed to be typing.\*.
    
*   Only the args listed in `mutates_args` are being mutated. If `mutates_args` is “unknown”,
    
    it assumes that all inputs to the operator are being mutated.
    

Callers (e.g. the custom ops API) are responsible for checking these assumptions.

Parameters:

*   **prototype\_function** ([_Callable_](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.15)")
    ) – The function from which to infer a schema for from its type annotations.
    
*   **op\_name** (_Optional__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_) – The name of the operator in the schema. If `name` is None, then the name is not included in the inferred schema. Note that the input schema to `torch.library.Library.define` requires an operator name.
    
*   **mutates\_args** (_"unknown"_ _|_ _Iterable__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_) – The arguments that are mutated in the function.
    
*   **tags** ([_Tag_](https://docs.pytorch.org/docs/2.15/torch.html#torch.Tag "torch.Tag")
     _|_ _Sequence__\[_[_Tag_](https://docs.pytorch.org/docs/2.15/torch.html#torch.Tag "torch.Tag")\
    _\]_ _|_ _None_) – one or more tags to apply to the inferred schema. Use `torch.Tag.inplace` or `torch.Tag.out` to infer the conventional aliasing for those operator kinds.
    

Returns:

The inferred schema.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

Example

\>>> def foo\_impl(x: torch.Tensor) \-> torch.Tensor:
\>>>     return x.sin()
\>>>
\>>> infer\_schema(foo\_impl, op\_name\="foo", mutates\_args\={})
foo(Tensor x) -> Tensor
\>>>
\>>> infer\_schema(foo\_impl, mutates\_args\={})
(Tensor x) -> Tensor

Copy to clipboard

_class_ torch.\_library.custom\_ops.CustomOpDef(_namespace_, _name_, _schema_, _fn_, _tags\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_library/custom_ops.py#L272)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch._library.custom_ops.CustomOpDef "Link to this definition")

CustomOpDef is a wrapper around a function that turns it into a custom op.

It has various methods for registering additional behavior for this custom op.

You should not instantiate CustomOpDef directly; instead, use the [`torch.library.custom_op()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.custom_op "torch.library.custom_op")
 API.

set\_kernel\_enabled(_device\_type_, _enabled\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_library/custom_ops.py#L322)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch._library.custom_ops.CustomOpDef.set_kernel_enabled "Link to this definition")

Disable or re-enable an already registered kernel for this custom operator.

If the kernel is already disabled/enabled, this is a no-op.

Note

If a kernel is first disabled and then registered, it is disabled until enabled again.

Parameters:

*   **device\_type** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The device type to disable/enable the kernel for.
    
*   **disable** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether to disable or enable the kernel.
    

Example

\>>> inp \= torch.randn(1)
\>>>
\>>> \# define custom op \`f\`.
\>>> @custom\_op("mylib::f", mutates\_args\=())
\>>> def f(x: Tensor) \-> Tensor:
\>>>     return torch.zeros(1)
\>>>
\>>> print(f(inp))  \# tensor(\[0.\]), default kernel
\>>>
\>>> @f.register\_kernel("cpu")
\>>> def \_(x):
\>>>     return torch.ones(1)
\>>>
\>>> print(f(inp))  \# tensor(\[1.\]), CPU kernel
\>>>
\>>> \# temporarily disable the CPU kernel
\>>> with f.set\_kernel\_enabled("cpu", enabled \= False):
\>>>     print(f(inp))  \# tensor(\[0.\]) with CPU kernel disabled

Copy to clipboard

torch.library.get\_kernel(_op_, _dispatch\_key_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/library.py#L1716)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.get_kernel "Link to this definition")

Returns the computed kernel for a given operator and dispatch key.

This function retrieves the kernel that would be executed for a given operator and dispatch key combination. The returned SafeKernelFunction can be used to call the kernel in a boxed fashion. The intended use case for this function is to retrieve the original kernel for a given dispatch key and then register another kernel to the same dispatch key that calls into the original kernel for certain cases.

Parameters:

*   **op** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _OpOverload_ _|_ [_CustomOpDef_](https://docs.pytorch.org/docs/2.15/library.html#torch._library.custom_ops.CustomOpDef "torch._library.custom_ops.CustomOpDef")
    ) – Operator name (along with the overload) or OpOverload object Can be a string (e.g., “aten::add.Tensor”), an OpOverload, or a CustomOpDef.
    
*   **dispatch\_key** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _torch.DispatchKey_) – The dispatch key to get the kernel for. Can be a string (e.g., “CPU”, “CUDA”) or a DispatchKey enum value.
    

Returns:

A safe kernel function that can be used to

call the kernel.

Return type:

torch.\_C.\_SafeKernelFunction

Raises:

[**RuntimeError**](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "(in Python v3.15)")
 – If the operator does not exist.

Example

\>>> # Get the CPU kernel for torch.add
>>> kernel = torch.library.get\_kernel("aten::add.Tensor", "CPU")
>>>
>>> # You can also use DispatchKey enum
>>> kernel = torch.library.get\_kernel("aten::add.Tensor", torch.DispatchKey.CPU)
>>>
>>> # Or use an OpOverload directly
>>> kernel = torch.library.get\_kernel(torch.ops.aten.add.Tensor, "CPU")
>>>
>>> # Example: Using get\_kernel in a custom op with conditional dispatch
>>> # Get the original kernel for torch.sin
>>> original\_sin\_kernel = torch.library.get\_kernel("aten::sin", "CPU")
>>>
>>> # If input has negative values, use original sin, otherwise return zeros
>>> def conditional\_sin\_impl(dispatch\_keys, x):
>>>     if (x < 0).any():
>>>         return original\_sin\_kernel.call\_boxed(dispatch\_keys, x)
>>>     else:
>>>         return torch.zeros\_like(x)
>>>
>>> lib = torch.library.Library("aten", "IMPL")
>>> # with\_keyset=True so the first argument to the impl is the current DispatchKeySet
>>> which needs to be the first argument to \`\`kernel.call\_boxed\`\`
>>> lib.impl("sin", conditional\_sin\_impl, "CPU", with\_keyset=True)
>>>
>>> # Test the conditional behavior
>>> x\_positive = torch.tensor(\[1.0, 2.0\])
>>> x\_mixed = torch.tensor(\[-1.0, 2.0\])
>>> torch.sin(x\_positive)
tensor(\[0., 0.\])
>>> torch.sin(x\_mixed)
tensor(\[-0.8415, 0.9093\])

Copy to clipboard

Low-level APIs[#](https://docs.pytorch.org/docs/2.15/library.html#low-level-apis "Link to this heading")

---------------------------------------------------------------------------------------------------------

The following APIs are direct bindings to PyTorch’s C++ low-level operator registration APIs.

Warning

The low-level operator registration APIs and the PyTorch Dispatcher are a complicated PyTorch concept. We recommend you use the higher level APIs above (that do not require a torch.library.Library object) when possible. [This blog post](http://blog.ezyang.com/2020/09/lets-talk-about-the-pytorch-dispatcher/)
 is a good starting point to learn about the PyTorch Dispatcher.

A tutorial that walks you through some examples on how to use this API is available on [Google Colab](https://colab.research.google.com/drive/1RRhSfk7So3Cn02itzLWE9K4Fam-8U011?usp=sharing)
.

_class_ torch.library.Library(_ns_, _kind_, _dispatch\_key\=''_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/library.py#L212)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.Library "Link to this definition")

A class to create libraries that can be used to register new operators or override operators in existing libraries from Python. A user can optionally pass in a dispatch keyname if they only want to register kernels corresponding to only one specific dispatch key.

To create a library to override operators in an existing library (with name ns), set the kind to “IMPL”. To create a new library (with name ns) to register new operators, set the kind to “DEF”. To create a fragment of a possibly existing library to register operators (and bypass the limitation that there is only one library for a given namespace), set the kind to “FRAGMENT”.

Parameters:

*   **ns** – library name
    
*   **kind** – “DEF”, “IMPL”, “FRAGMENT”
    
*   **dispatch\_key** – PyTorch dispatch key (default: “”)
    

define(_schema_, _alias\_analysis\=''_, _\*_, _tags\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/library.py#L272)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.Library.define "Link to this definition")

Defines a new operator and its semantics in the ns namespace.

Parameters:

*   **schema** – function schema to define a new operator.
    
*   **alias\_analysis** (_optional_) – Indicates if the aliasing properties of the operator arguments can be inferred from the schema (default behavior) or not (“CONSERVATIVE”).
    
*   **tags** ([_Tag_](https://docs.pytorch.org/docs/2.15/torch.html#torch.Tag "torch.Tag")
     _|_ _Sequence__\[_[_Tag_](https://docs.pytorch.org/docs/2.15/torch.html#torch.Tag "torch.Tag")\
    _\]_) – one or more torch.Tag to apply to this operator. Tagging an operator changes the operator’s behavior under various PyTorch subsystems; please read the docs for the torch.Tag carefully before applying it.
    

Returns:

name of the operator as inferred from the schema.

Example:

\>>> my\_lib \= Library("mylib", "DEF")
\>>> my\_lib.define("sum(Tensor self) -> Tensor")

Copy to clipboard

fallback(_fn_, _dispatch\_key\=''_, _\*_, _with\_keyset\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/library.py#L551)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.Library.fallback "Link to this definition")

Registers the function implementation as the fallback for the given key.

This function only works for a library with global namespace (“\_”).

Parameters:

*   **fn** – function used as fallback for the given dispatch key or [`fallthrough_kernel()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.fallthrough_kernel "torch.library.fallthrough_kernel")
     to register a fallthrough.
    
*   **dispatch\_key** – dispatch key that the input function should be registered for. By default, it uses the dispatch key that the library was created with.
    
*   **with\_keyset** – flag controlling if the current dispatcher call keyset should be passed as the first argument to `fn` when calling. This should be used to create the appropriate keyset for redispatch calls.
    

Example:

\>>> my\_lib \= Library("\_", "IMPL")
\>>> def fallback\_kernel(op, \*args, \*\*kwargs):
\>>>     \# Handle all autocast ops generically
\>>>     \# ...
\>>> my\_lib.fallback(fallback\_kernel, "Autocast")

Copy to clipboard

impl(_op\_name_, _fn_, _dispatch\_key\=''_, _\*_, _with\_keyset\=False_, _allow\_override\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/library.py#L441)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.Library.impl "Link to this definition")

Registers the function implementation for an operator defined in the library.

Parameters:

*   **op\_name** – operator name (along with the overload) or OpOverload object.
    
*   **fn** – function that’s the operator implementation for the input dispatch key or [`fallthrough_kernel()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.fallthrough_kernel "torch.library.fallthrough_kernel")
     to register a fallthrough.
    
*   **dispatch\_key** – dispatch key that the input function should be registered for. By default, it uses the dispatch key that the library was created with.
    
*   **with\_keyset** – flag controlling if the current dispatcher call keyset should be passed as the first argument to `fn` when calling. This should be used to create the appropriate keyset for redispatch calls.
    
*   **allow\_override** – Flag controlling if we want to override an existing registered kernel implementation. This is on by default; pass `False` to error if a kernel is already registered for this dispatch key.
    

Example::

\>>> my\_lib \= Library("aten", "IMPL")
\>>> def div\_cpu(self, other):
\>>>     return self \* (1 / other)
\>>> my\_lib.impl("div.Tensor", div\_cpu, "CPU")

Copy to clipboard

register\_symm\_mem\_args(_op\_name_, _arg\_names_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/library.py#L518)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.Library.register_symm_mem_args "Link to this definition")

Registers which arguments require symmetric memory allocation for an operator.

This method allows operators to declaratively specify which arguments need symmetric memory treatment. When used with `torch.compile`, Inductor automatically allocates these arguments in P2P-accessible NVLink memory (`empty_strided_p2p`), enabling zero-copy inter-GPU communication.

The operator’s schema should include a `group_name` (`str`) argument. Inductor’s `FallbackKernel._maybe_realize_symm_mem_args` extracts `group_name` at compile time to allocate P2P buffers for the correct process group. Without `group_name`, the automatic realization is skipped.

Parameters:

*   **op\_name** – operator name (along with the overload) or OpOverload object.
    
*   **arg\_names** – list of argument names that require symmetric memory allocation.
    

Example::

\>>> my\_lib \= Library("symm\_mem", "FRAGMENT")
\>>> my\_lib.define("one\_shot\_all\_reduce(Tensor input, str reduce\_op, str group\_name) -> Tensor")
\>>> my\_lib.register\_symm\_mem\_args("one\_shot\_all\_reduce", \["input"\])

Copy to clipboard

torch.library.fallthrough\_kernel()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/library.py#L60)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.fallthrough_kernel "Link to this definition")

A dummy function to pass to `Library.impl` in order to register a fallthrough.

torch.library.define(_qualname_, _schema_, _\*_, _lib\=None_, _tags\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/library.py#L694)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.define "Link to this definition")

torch.library.define(_lib_, _schema_, _alias\_analysis\=''_)

Defines a new operator.

In PyTorch, defining an op (short for “operator”) is a two step-process: - we need to define the op (by providing an operator name and schema) - we need to implement behavior for how the operator interacts with various PyTorch subsystems, like CPU/CUDA Tensors, Autograd, etc.

This entrypoint defines the custom operator (the first step) you must then perform the second step by calling various `impl_*` APIs, like [`torch.library.impl()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.impl "torch.library.impl")
 or [`torch.library.register_fake()`](https://docs.pytorch.org/docs/2.15/library.html#torch.library.register_fake "torch.library.register_fake")
.

Parameters:

*   **qualname** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The qualified name for the operator. Should be a string that looks like “namespace::name”, e.g. “aten::sin”. Operators in PyTorch need a namespace to avoid name collisions; a given operator may only be created once. If you are writing a Python library, we recommend the namespace to be the name of your top-level module.
    
*   **schema** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The schema of the operator. E.g. “(Tensor x) -> Tensor” for an op that accepts one Tensor and returns one Tensor. It does not contain the operator name (that is passed in `qualname`).
    
*   **lib** (_Optional__\[_[_Library_](https://docs.pytorch.org/docs/2.15/library.html#torch.library.Library "torch.library.Library")\
    _\]_) – If provided, the lifetime of this operator will be tied to the lifetime of the Library object.
    
*   **tags** ([_Tag_](https://docs.pytorch.org/docs/2.15/torch.html#torch.Tag "torch.Tag")
     _|_ _Sequence__\[_[_Tag_](https://docs.pytorch.org/docs/2.15/torch.html#torch.Tag "torch.Tag")\
    _\]_) – one or more torch.Tag to apply to this operator. Tagging an operator changes the operator’s behavior under various PyTorch subsystems; please read the docs for the torch.Tag carefully before applying it.
    

Example::

\>>> import torch
\>>> import numpy as np
\>>>
\>>> \# Define the operator
\>>> torch.library.define("mylib::sin", "(Tensor x) -> Tensor")
\>>>
\>>> \# Add implementations for the operator
\>>> @torch.library.impl("mylib::sin", "cpu")
\>>> def f(x):
\>>>     return torch.from\_numpy(np.sin(x.numpy()))
\>>>
\>>> \# Call the new operator from torch.ops.
\>>> x \= torch.randn(3)
\>>> y \= torch.ops.mylib.sin(x)
\>>> assert torch.allclose(y, x.sin())

Copy to clipboard

torch.library.impl(_lib_, _name_, _dispatch\_key\=''_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/library.py#L804)
[#](https://docs.pytorch.org/docs/2.15/library.html#torch.library.impl "Link to this definition")

torch.library.impl(_qualname: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_, _types: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 | Sequence\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\]_, _func: [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_, _\*_, _lib: [Library](https://docs.pytorch.org/docs/2.15/library.html#torch.library.Library "torch.library.Library")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_) → Callable\[\[Callable\[..., [object](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")\
\]\], [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")\
\]

torch.library.impl(_qualname: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_, _types: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 | Sequence\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\]_, _func: Callable\[..., [object](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")\
\]_, _\*_, _lib: [Library](https://docs.pytorch.org/docs/2.15/library.html#torch.library.Library "torch.library.Library")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= None_) → [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")

torch.library.impl(_lib: [Library](https://docs.pytorch.org/docs/2.15/library.html#torch.library.Library "torch.library.Library")
_, _name: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
_, _dispatch\_key: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 \= ''_) → Callable\[\[Callable\[\_P, \_T\]\], Callable\[\_P, \_T\]\]

Register an implementation for a device type for this operator.

You may pass “default” for `types` to register this implementation as the default implementation for ALL device types. Please only use this if the implementation truly supports all device types; for example, this is true if it is a composition of built-in PyTorch operators.

This API may be used as a decorator. You can use nested decorators with this API provided they return a function and are placed inside this API (see Example 2).

Some valid types are: “cpu”, “cuda”, “xla”, “mps”, “ipu”, “xpu”.

Parameters:

*   **qualname** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Should be a string that looks like “namespace::operator\_name”.
    
*   **types** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _Sequence__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_) – The device types to register an impl to.
    
*   **lib** (_Optional__\[_[_Library_](https://docs.pytorch.org/docs/2.15/library.html#torch.library.Library "torch.library.Library")\
    _\]_) – If provided, the lifetime of this registration will be tied to the lifetime of the Library object.
    

Examples

\>>> import torch
\>>> import numpy as np
\>>> \# Example 1: Register function.
\>>> \# Define the operator
\>>> torch.library.define("mylib::mysin", "(Tensor x) -> Tensor")
\>>>
\>>> \# Add implementations for the cpu device
\>>> @torch.library.impl("mylib::mysin", "cpu")
\>>> def f(x):
\>>>     return torch.from\_numpy(np.sin(x.numpy()))
\>>>
\>>> x \= torch.randn(3)
\>>> y \= torch.ops.mylib.mysin(x)
\>>> assert torch.allclose(y, x.sin())
\>>>
\>>> \# Example 2: Register function with decorator.
\>>> def custom\_decorator(func):
\>>>     def wrapper(\*args, \*\*kwargs):
\>>>         return func(\*args, \*\*kwargs) + 1
\>>>     return wrapper
\>>>
\>>> \# Define the operator
\>>> torch.library.define("mylib::sin\_plus\_one", "(Tensor x) -> Tensor")
\>>>
\>>> \# Add implementations for the operator
\>>> @torch.library.impl("mylib::sin\_plus\_one", "cpu")
\>>> @custom\_decorator
\>>> def f(x):
\>>>     return torch.from\_numpy(np.sin(x.numpy()))
\>>>
\>>> \# Call the new operator from torch.ops.
\>>> x \= torch.randn(3)
\>>>
\>>> y1 \= torch.ops.mylib.sin\_plus\_one(x)
\>>> y2 \= torch.sin(x) + 1
\>>> assert torch.allclose(y1, y2)

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/library.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/library.md.txt)

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