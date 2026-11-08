Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/higher_order_ops/associative_scan.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/higher_order_ops/associative_scan.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/higher_order_ops/associative_scan.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/higher_order_ops/associative_scan.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/higher_order_ops/associative_scan.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/higher_order_ops/associative_scan.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/higher_order_ops/associative_scan.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/higher_order_ops/associative_scan.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/higher_order_ops/associative_scan.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/higher_order_ops/associative_scan.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/higher_order_ops/associative_scan.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/higher_order_ops/associative_scan.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/higher_order_ops/associative_scan.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/higher_order_ops/associative_scan.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/higher_order_ops/associative_scan.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/higher_order_ops/associative_scan.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/higher_order_ops/associative_scan.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/higher_order_ops/associative_scan.html)
[v1.13](https://docs.pytorch.org/docs/1.13/higher_order_ops/associative_scan.html)
[v1.12](https://docs.pytorch.org/docs/1.12/higher_order_ops/associative_scan.html)
[v1.11](https://docs.pytorch.org/docs/1.11/higher_order_ops/associative_scan.html)
[v1.10](https://docs.pytorch.org/docs/1.10/higher_order_ops/associative_scan.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/higher_order_ops/associative_scan.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/higher_order_ops/associative_scan.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/higher_order_ops/associative_scan.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/higher_order_ops/associative_scan.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/higher_order_ops/associative_scan.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/higher_order_ops/associative_scan.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/higher_order_ops/associative_scan.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/higher_order_ops/associative_scan.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/higher_order_ops/associative_scan.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/higher_order_ops/associative_scan.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/higher_order_ops/associative_scan.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/higher_order_ops/associative_scan.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/higher_order_ops/associative_scan.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/higher_order_ops/associative_scan.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/higher_order_ops/associative_scan.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/higher_order_ops/associative_scan.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/higher_order_ops/associative_scan.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/higher_order_ops/associative_scan.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/higher_order_ops/associative_scan.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/higher_order_ops/associative_scan.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/higher_order_ops/associative_scan.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/higher_order_ops/associative_scan.html)

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

Control Flow - Associative Scan[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/associative_scan.html#control-flow-associative-scan "Link to this heading")

===================================================================================================================================================================

Created On: Feb 14, 2026 | Last Updated On: Feb 14, 2026

`torch.associative_scan` is a structured control flow operator that performs an inclusive scan with an associative combine function. It can logically be seen as implemented as follows:

def associative\_scan(
    combine\_fn: Callable\[\[pytree.PyTree, pytree.PyTree\], pytree.PyTree\],
    xs: pytree.PyTree,
    dim: int,
    reverse: bool \= False,
) \-> pytree.PyTree:
    result \= \[\]
    carry \= xs.select(dim, 0)
    result.append(carry)
    for i in range(1, xs.size(dim)):
        carry \= combine\_fn(carry, xs.select(dim, i))
        result.append(carry)
    return torch.stack(result, dim\=dim)

Copy to clipboard

Because `combine_fn` is required to be associative, the computation can be parallelized using a tree-reduction algorithm rather than executed sequentially. This enables efficient GPU implementations for operations like cumulative sums, products, or other associative accumulations.

Warning

`torch.associative_scan` is a prototype feature in PyTorch. You may run into miscompiles. Read more about feature classification at: https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype

Examples[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/associative_scan.html#examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

Below is an example that uses `associative_scan` to compute a cumulative sum:

import torch
from torch.\_higher\_order\_ops.associative\_scan import associative\_scan

def add(x: torch.Tensor, y: torch.Tensor):
    return x + y

xs = torch.arange(1, 5, dtype=torch.float32)  # \[1, 2, 3, 4\]
cumsum = associative\_scan(add, xs, dim=0, combine\_mode="generic")
print(cumsum)

Copy to clipboard

Here is an example computing a cumulative product:

def mul(x: torch.Tensor, y: torch.Tensor):
    return x \* y

xs = torch.arange(1, 5, dtype=torch.float32)  # \[1, 2, 3, 4\]
cumprod = associative\_scan(mul, xs, dim=0, combine\_mode="generic")
print(cumprod)

Copy to clipboard

We can export the model with associative\_scan for further transformations and deployment. This example uses dynamic shapes to allow variable sequence length:

class AssociativeScanModule(torch.nn.Module):
    def forward(self, xs: torch.Tensor) \-> torch.Tensor:
        def combine\_fn(x, y):
            return x + y

        return associative\_scan(combine\_fn, xs, dim\=0, combine\_mode\="pointwise")

mod \= AssociativeScanModule()
inp \= torch.randn(5, 3, device\="cuda")
dim\_seq \= torch.export.Dim("seq", min\=2)
ep \= torch.export.export(mod, (inp,), dynamic\_shapes\={"xs": {0: dim\_seq}})
print(ep)

Copy to clipboard

ExportedProgram:
    class GraphModule(torch.nn.Module):
        def forward(self, xs: "f32\[s83, 3\]"):
            \# File: /data/users/angelayi/pytorch2/foo.py:25 in forward, code: return associative\_scan(combine\_fn, xs, dim=0, combine\_mode="pointwise")
            movedim: "f32\[s83, 3\]" \= torch.ops.aten.movedim.int(xs, 0, 0);  xs \= None

            \# File: <eval\_with\_key>.3:6 in forward, code: select\_copy = torch.select\_copy(l\_leaves\_xs\_0\_, 0, 0);  select\_copy = None
            select\_copy: "f32\[3\]" \= torch.ops.aten.select\_copy.int(movedim, 0, 0);  select\_copy \= None

            \# File: <eval\_with\_key>.3:8 in forward, code: associative\_scan = torch.ops.higher\_order.associative\_scan(associative\_scan\_combine\_fn\_0, \[l\_leaves\_xs\_0\_\], ());  associative\_scan\_combine\_fn\_0 = l\_leaves\_xs\_0\_ = None
            associative\_scan\_combine\_graph\_0 \= self.associative\_scan\_combine\_graph\_0
            associative\_scan \= torch.ops.higher\_order.associative\_scan(associative\_scan\_combine\_graph\_0, \[movedim\], ());  associative\_scan\_combine\_graph\_0 \= movedim \= None
            getitem: "f32\[s83, 3\]" \= associative\_scan\[0\];  associative\_scan \= None

            \# File: /data/users/angelayi/pytorch2/foo.py:25 in forward, code: return associative\_scan(combine\_fn, xs, dim=0, combine\_mode="pointwise")
            movedim\_1: "f32\[s83, 3\]" \= torch.ops.aten.movedim.int(getitem, 0, 0);  getitem \= None
            return (movedim\_1,)

        class associative\_scan\_combine\_graph\_0(torch.nn.Module):
            def forward(self, arg0\_1: "f32\[3\]", arg1\_1: "f32\[3\]"):
                \# File: <eval\_with\_key>.4:5 in forward, code: add = child + child\_1;  child = child\_1 = None
                add: "f32\[3\]" \= torch.ops.aten.add.Tensor(arg0\_1, arg1\_1);  arg0\_1 \= arg1\_1 \= None
                return \[add\]

Graph signature:
    \# inputs
    xs: USER\_INPUT

    \# outputs
    movedim\_1: USER\_OUTPUT

Copy to clipboard

Notice that `torch.associative_scan` is lowered to `torch.ops.higher_order.associative_scan`, and the combine function becomes a sub-graph attribute of the top-level graph module.

Restrictions[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/associative_scan.html#restrictions "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

*   `combine_fn` must be associative: `combine_fn(combine_fn(a, b), c) == combine_fn(a, combine_fn(b, c))`.
    
*   `combine_fn` must not in-place mutate its inputs.
    
*   `combine_fn` must not reference variables from an outer scope (closures are not supported).
    
*   `combine_fn`’s output cannot alias any of the inputs.
    

API Reference[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/associative_scan.html#api-reference "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

torch.\_higher\_order\_ops.associative\_scan.associative\_scan(_combine\_fn_, _xs_, _dim_, _reverse\=False_, _combine\_mode\='pointwise'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_higher_order_ops/associative_scan.py#L153)
[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/associative_scan.html#torch._higher_order_ops.associative_scan.associative_scan "Link to this definition")

Performs an inclusive scan with an associative combine function.

Warning

`torch.associative_scan` is a prototype feature in PyTorch. It currently does not support autograd and you may run into miscompiles. Read more about feature classification at: [https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype](https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype)

With `combine_mode="pointwise"`, efficient execution requires runtime code generation via `torch.compile`, and codegen is only supported on backends with scan support (currently CUDA and XPU). On other devices the operator still runs eagerly via the generic fallback.

Parameters:

*   **combine\_fn** (_Callable_) – A binary callable with type `(Tensor, Tensor) -> Tensor`, or if input is a pytree `(pytree, pytree) -> pytree`. This function must be pure, satisfy the associative property and have no side-effects. It may close over lifted arguments (e.g. freevars). On the autograd path in eager mode, tensor freevars are permitted as long as they do not require gradients (gradients for lifted arguments are not supported). Under `torch.compile` with `backend="inductor"` tensor freevars are still rejected outright; only `int`/`SymInt` lifted arguments are supported there.
    
*   **xs** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – The input tensor, or nested pytree of tensors.
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – the dimension to scan over
    
*   **reverse** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – A boolean stating if the scan should be reversed with respect to `dim`, default `False`.
    
*   **combine\_mode** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – A string indicating whether the `combine_fn` is `pointwise` or `generic`, default `pointwise`. If `combine_mode=pointwise`, `combine_fn` must be pure and may only contain pointwise operations; under `torch.compile` `xs` must be on a backend with scan codegen support (CUDA or XPU), otherwise the generic fallback is used. In all other cases `combine_mode=generic` should be used. Note: `combine_mode=pointwise` is more efficient than `combine_mode=generic`.
    

Returns:

A pytree of the same structure and shape as `xs`. If the scan dimension has size 0, the output mirrors the (empty) input unchanged. The gradient with respect to `xs` is also empty (size 0 along `dim`), since there are no elements to differentiate through.

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Example:

def add(x: torch.Tensor, y: torch.Tensor):
    return x + y

cumsum \= associative\_scan(add, x, dim)

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/higher_order_ops/associative_scan.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/higher_order_ops/associative_scan.md.txt)

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