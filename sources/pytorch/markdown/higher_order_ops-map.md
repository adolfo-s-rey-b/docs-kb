Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/higher_order_ops/map.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/higher_order_ops/map.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/higher_order_ops/map.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/higher_order_ops/map.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/higher_order_ops/map.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/higher_order_ops/map.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/higher_order_ops/map.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/higher_order_ops/map.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/higher_order_ops/map.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/higher_order_ops/map.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/higher_order_ops/map.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/higher_order_ops/map.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/higher_order_ops/map.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/higher_order_ops/map.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/higher_order_ops/map.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/higher_order_ops/map.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/higher_order_ops/map.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/higher_order_ops/map.html)
[v1.13](https://docs.pytorch.org/docs/1.13/higher_order_ops/map.html)
[v1.12](https://docs.pytorch.org/docs/1.12/higher_order_ops/map.html)
[v1.11](https://docs.pytorch.org/docs/1.11/higher_order_ops/map.html)
[v1.10](https://docs.pytorch.org/docs/1.10/higher_order_ops/map.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/higher_order_ops/map.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/higher_order_ops/map.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/higher_order_ops/map.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/higher_order_ops/map.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/higher_order_ops/map.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/higher_order_ops/map.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/higher_order_ops/map.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/higher_order_ops/map.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/higher_order_ops/map.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/higher_order_ops/map.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/higher_order_ops/map.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/higher_order_ops/map.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/higher_order_ops/map.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/higher_order_ops/map.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/higher_order_ops/map.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/higher_order_ops/map.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/higher_order_ops/map.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/higher_order_ops/map.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/higher_order_ops/map.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/higher_order_ops/map.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/higher_order_ops/map.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/higher_order_ops/map.html)

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

Control Flow - Map[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/map.html#control-flow-map "Link to this heading")

============================================================================================================================

Created On: Feb 14, 2026 | Last Updated On: Feb 14, 2026

`torch.map` is a structured control flow operator that applies a function over the leading dimension of input tensors. It can logically be seen as implemented as follows:

def map(
    f: Callable\[\[PyTree, ...\], PyTree\],
    xs: Union\[PyTree, torch.Tensor\],
    \*args,
):
    out \= \[\]
    for idx in range(xs.size(0)):
        xs\_sliced \= xs.select(0, idx)
        out.append(f(xs\_sliced, \*args))
    return torch.stack(out)

Copy to clipboard

Warning

`torch._higher_order_ops.map` is a prototype feature in PyTorch. You may run into miscompiles. Read more about feature classification at: https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype

Examples[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/map.html#examples "Link to this heading")

----------------------------------------------------------------------------------------------------------

Below is an example that uses map to apply a function over a batch:

import torch
from torch.\_higher\_order\_ops import map

def f(x):
    return x.sin() + x.cos()

xs = torch.randn(3, 4, 5)  # batch of 3 tensors, each 4x5
# Applies f to each of the 3 slices
result = map(f, xs)  # returns tensor of shape \[3, 4, 5\]
print(result)

Copy to clipboard

We can export the model with map for further transformations and deployment. This example uses dynamic shapes to allow variable batch size:

class MapModule(torch.nn.Module):
    def \_\_init\_\_(self):
        super().\_\_init\_\_()

    def forward(self, xs: torch.Tensor) -> torch.Tensor:
        def body\_fn(x):
            return x.sin() + x.cos()

        return map(body\_fn, xs)

mod = MapModule()
inp = torch.randn(3, 4)
ep = torch.export.export(mod, (inp,), dynamic\_shapes={"xs": {0: torch.export.Dim.DYNAMIC}})
print(ep)

Copy to clipboard

Notice that `torch.map` is lowered to `torch.ops.higher_order.map_impl`, and the body function becomes a sub-graph attribute of the top-level graph module.

Restrictions[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/map.html#restrictions "Link to this heading")

------------------------------------------------------------------------------------------------------------------

*   Mapped `xs` can only consist of tensors.
    
*   Leading dimensions of all tensors in `xs` must be consistent and non-zero.
    
*   The body function must not mutate inputs.
    

API Reference[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/map.html#api-reference "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

torch.\_higher\_order\_ops.map.map(_f_, _xs_, _\*args_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_higher_order_ops/map.py#L111)
[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/map.html#torch._higher_order_ops.map.map "Link to this definition")

Performs a map of f with xs. Intuitively, you can think of the semantic being:

out \= \[\]
for idx in len(xs.size(0)):
    xs\_sliced \= xs.select(0, idx)
    out.append(f(xs\_sliced, \*args))
torch.stack(out)

Copy to clipboard

Warning

`torch._higher_order_ops.map` is a prototype feature in PyTorch. It currently does not support autograd and you may run into miscompiles. Read more about feature classification at: [https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype](https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype)

Parameters:

*   **f** (_Callable_) – a callable that takes an input x, that could either be a single Tensor or a nested dict, list of tensors and some additional inputs
    
*   **xs** ([_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")
     _|_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the inputs that’re to be mapped over. We’ll iterate over the first dim of each x and perform f on each slice.
    
*   **\*args** (_TypeVarTuple_) – additional arguments provided to each step of f. They could also be omitted and map is able to automatically figure out the read dependency.
    

Returns:

the stacked output for each step of f

Example:

def f(xs):
    return xs\[0\] + xs\[1\] + const1 + const2

xs \= \[torch.randn(2, 3), torch.randn(2, 3)\]
const1 \= torch.randn(2, 3)
const2 \= torch.randn(2, 3)
\# returns a tensor of shape \[2, 2, 3\]
torch.\_higher\_order\_ops.map(f, xs)

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/higher_order_ops/map.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/higher_order_ops/map.md.txt)

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