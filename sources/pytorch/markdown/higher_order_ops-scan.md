Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/higher_order_ops/scan.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/higher_order_ops/scan.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/higher_order_ops/scan.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/higher_order_ops/scan.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/higher_order_ops/scan.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/higher_order_ops/scan.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/higher_order_ops/scan.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/higher_order_ops/scan.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/higher_order_ops/scan.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/higher_order_ops/scan.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/higher_order_ops/scan.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/higher_order_ops/scan.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/higher_order_ops/scan.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/higher_order_ops/scan.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/higher_order_ops/scan.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/higher_order_ops/scan.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/higher_order_ops/scan.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/higher_order_ops/scan.html)
[v1.13](https://docs.pytorch.org/docs/1.13/higher_order_ops/scan.html)
[v1.12](https://docs.pytorch.org/docs/1.12/higher_order_ops/scan.html)
[v1.11](https://docs.pytorch.org/docs/1.11/higher_order_ops/scan.html)
[v1.10](https://docs.pytorch.org/docs/1.10/higher_order_ops/scan.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/higher_order_ops/scan.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/higher_order_ops/scan.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/higher_order_ops/scan.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/higher_order_ops/scan.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/higher_order_ops/scan.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/higher_order_ops/scan.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/higher_order_ops/scan.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/higher_order_ops/scan.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/higher_order_ops/scan.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/higher_order_ops/scan.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/higher_order_ops/scan.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/higher_order_ops/scan.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/higher_order_ops/scan.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/higher_order_ops/scan.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/higher_order_ops/scan.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/higher_order_ops/scan.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/higher_order_ops/scan.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/higher_order_ops/scan.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/higher_order_ops/scan.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/higher_order_ops/scan.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/higher_order_ops/scan.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/higher_order_ops/scan.html)

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

Control Flow - Scan[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/scan.html#control-flow-scan "Link to this heading")

===============================================================================================================================

Created On: Feb 14, 2026 | Last Updated On: Feb 14, 2026

`torch.scan` is a structured control flow operator that performs an inclusive scan with a combine function. It is commonly used for cumulative operations like cumsum, cumprod, or more general recurrences. It can logically be seen as implemented as follows:

def scan(
    combine\_fn: Callable\[\[PyTree, PyTree\], tuple\[PyTree, PyTree\]\],
    init: PyTree,
    xs: PyTree,
    \*,
    dim: int \= 0,
    reverse: bool \= False,
) \-> tuple\[PyTree, PyTree\]:
    carry \= init
    ys \= \[\]
    for i in range(xs.size(dim)):
        x\_slice \= xs.select(dim, i)
        carry, y \= combine\_fn(carry, x\_slice)
        ys.append(y)
    return carry, torch.stack(ys)

Copy to clipboard

Warning

`torch.scan` is a prototype feature in PyTorch. You may run into miscompiles. Read more about feature classification at: https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype

Examples[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/scan.html#examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------

Below is an example that uses scan to compute a cumulative sum:

import torch
from torch.\_higher\_order\_ops import scan

def add(carry: torch.Tensor, x: torch.Tensor):
    next\_carry = carry + x
    y = next\_carry.clone()  # clone to avoid output-output aliasing
    return next\_carry, y

init = torch.zeros(1)
xs = torch.arange(5, dtype=torch.float32)

final\_carry, cumsum = scan(add, init=init, xs=xs)
print(final\_carry)
print(cumsum)

Copy to clipboard

We can export the model with scan for further transformations and deployment. This example uses dynamic shapes to allow variable sequence length:

class ScanModule(torch.nn.Module):
    def forward(self, xs: torch.Tensor) -> tuple\[torch.Tensor, torch.Tensor\]:
        def combine\_fn(carry, x):
            next\_carry = carry + x
            return next\_carry, next\_carry.clone()

        init = torch.zeros\_like(xs\[0\])
        return scan(combine\_fn, init=init, xs=xs)

mod = ScanModule()
inp = torch.randn(5, 3)
ep = torch.export.export(mod, (inp,), dynamic\_shapes={"xs": {0: torch.export.Dim.DYNAMIC}})
print(ep)

Copy to clipboard

Notice that the combine function becomes a sub-graph attribute of the top-level graph module.

Restrictions[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/scan.html#restrictions "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

*   `combine_fn` must return tensors with the same metadata (shape, dtype) for `next_carry` as `init`.
    
*   `combine_fn` must not in-place mutate its inputs. A clone before mutation is required.
    
*   `combine_fn` must not mutate Python variables (e.g., list/dict) created outside the function.
    
*   `combine_fn`’s output cannot alias any of the inputs. A clone is required.
    

API Reference[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/scan.html#api-reference "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

torch.\_higher\_order\_ops.scan.scan(_combine\_fn_, _init_, _xs_, _\*_, _dim\=0_, _reverse\=False_, _length\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_higher_order_ops/scan.py#L112)
[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/scan.html#torch._higher_order_ops.scan.scan "Link to this definition")

Performs an inclusive scan with a combine function.

Warning

`torch.scan` is a prototype feature in PyTorch. You may run into miscompiles. Read more about feature classification at: [https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype](https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype)

Parameters:

*   **combine\_fn** (_Callable_) – A binary callable with type `(Tensor, Tensor) -> (Tensor, Tensor)`, or if xs is a pytree `(pytree, pytree) -> (pytree, pytree)`. The first input to `combine_fn` is the previous or initial scan carry and the second input element to `combine_fn` is a slice of the input along dim. The first output element of `combine_fn` is the next scan carry and the second output of `combine_fn` represents a slice of the output. This function must be pure, i.e., no lifted arguments are supported at the moment and may not have any side effects.
    
*   **init** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _or_ _pytree with tensor leaves_) – The initial scan carry, a tensor, or nested pytree of tensors. The `init` is expected to have the same pytree structure as the first output element (i.e. carry) of `combine_fn`.
    
*   **xs** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _or_ _pytree with tensor leaves_ _or_ _None_) – The input tensor, or nested pytree of tensors. May be `None` when `length` is provided, in which case `combine_fn` receives `None` as `x` each step (counter-loop mode).
    

Keyword Arguments:

*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the dimension to scan over, default 0.
    
*   **reverse** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – A boolean stating if the scan should be reversed with respect to `dim`, default `False`.
    
*   **length** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ [_None_](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
    ) – Optional number of scan iterations, default `None`. When `xs` has tensor leaves, `length` is optional; if given it must equal `xs.shape[dim]` and serves only as a consistency check (no constraint when `length` is `None`). When `xs` has no leaves (`None` or empty pytree), `length` drives the number of iterations and `combine_fn` receives `x=None` each step. `length=0` with no xs tensors is supported in eager mode only; it is not supported under `torch.compile`.
    

Returns:

final\_carry (torch.Tensor or pytree with tensor leaves),

the final carry of the scan operation with same pytree structure as init.

out (torch.Tensor or pytree with tensor leaves),

each tensor leaf is a stacked output along first dim, where each slice is the output of a scan iteration. If the scan dimension has size 0, `final_carry` equals `init` unchanged and each output leaf has size 0 along `dim`. The gradient of `final_carry` with respect to `init` is the identity (not zero), since the body is never called and the carry passes through untouched.

Return type:

[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
\[[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
, [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\]

Restrictions:

*   The combine\_fn shouldn’t have any aliasing between input-input, input-output, and output-output. E.g. return a view
    
    or the same tensor as input is not supported. As a workaround, can clone the output to avoid aliasing.
    
*   The combine\_fn shouldn’t mutate any inputs. We’ll remove the mutation restriction for inference soon. Please file an issue
    
    if you input mutation support for training is needed.
    
*   The combine\_fn’s init carry should match the next\_carry in pytree structure and in tensor metadata.
    

Example:

def add(x: torch.Tensor, y: torch.Tensor):
    next\_carry \= y \= x + y
    \# clone the output to avoid output-output aliasing
    return next\_carry, y.clone()

i0 \= torch.zeros(1)
xs \= torch.arange(5)
\# returns torch.tensor(\[10.\]), torch.tensor(\[\[0\], \[1.\], \[3.\], \[6.\], \[10.\]\])
last\_carry, cumsum \= scan(add, init\=i0, xs\=xs)

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/higher_order_ops/scan.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/higher_order_ops/scan.md.txt)

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