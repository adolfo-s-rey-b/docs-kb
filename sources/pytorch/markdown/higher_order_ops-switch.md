Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/higher_order_ops/switch.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/higher_order_ops/switch.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/higher_order_ops/switch.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/higher_order_ops/switch.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/higher_order_ops/switch.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/higher_order_ops/switch.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/higher_order_ops/switch.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/higher_order_ops/switch.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/higher_order_ops/switch.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/higher_order_ops/switch.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/higher_order_ops/switch.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/higher_order_ops/switch.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/higher_order_ops/switch.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/higher_order_ops/switch.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/higher_order_ops/switch.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/higher_order_ops/switch.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/higher_order_ops/switch.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/higher_order_ops/switch.html)
[v1.13](https://docs.pytorch.org/docs/1.13/higher_order_ops/switch.html)
[v1.12](https://docs.pytorch.org/docs/1.12/higher_order_ops/switch.html)
[v1.11](https://docs.pytorch.org/docs/1.11/higher_order_ops/switch.html)
[v1.10](https://docs.pytorch.org/docs/1.10/higher_order_ops/switch.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/higher_order_ops/switch.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/higher_order_ops/switch.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/higher_order_ops/switch.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/higher_order_ops/switch.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/higher_order_ops/switch.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/higher_order_ops/switch.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/higher_order_ops/switch.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/higher_order_ops/switch.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/higher_order_ops/switch.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/higher_order_ops/switch.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/higher_order_ops/switch.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/higher_order_ops/switch.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/higher_order_ops/switch.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/higher_order_ops/switch.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/higher_order_ops/switch.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/higher_order_ops/switch.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/higher_order_ops/switch.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/higher_order_ops/switch.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/higher_order_ops/switch.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/higher_order_ops/switch.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/higher_order_ops/switch.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/higher_order_ops/switch.html)

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

Control Flow - Switch[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/switch.html#control-flow-switch "Link to this heading")

=====================================================================================================================================

Created On: Jun 24, 2026 | Last Updated On: Jun 24, 2026

`torch.switch` is a structured control flow operator for multi-way branching. It can be used to specify switch-case like control flow and can logically be seen as implemented as follows:

def switch(
    index: Union\[int, torch.Tensor\],
    branches: Tuple\[Callable, ...\],
    operands: Tuple\[torch.Tensor\]
):
    return branches\[index\](\*operands)

Copy to clipboard

Its unique power lies in its ability to express **data-dependent multi-way control flow**: it lowers to a switch operator (`torch.ops.higher_order.switch`), which preserves the index, all branch functions, and operands. This enables efficient compilation and deployment of models with N-way branching based on the **value** or **shape** of inputs or intermediate outputs.

Warning

`torch.switch` is a prototype feature in PyTorch. It has limited support for input and output types. Please look forward to a more stable implementation in a future version of PyTorch. Read more about feature classification at: https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype

Examples[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/switch.html#examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------

Below is an example that uses switch to select between multiple operations based on an input index:

import torch
from torch.\_higher\_order\_ops.switch import switch

def branch0(x: torch.Tensor):
    return x.cos()

def branch1(x: torch.Tensor):
    return x.sin()

def branch2(x: torch.Tensor):
    return x.tan()

class BasicSwitch(torch.nn.Module):
    """
    A basic usage of switch with multiple branches.
    """

    def \_\_init\_\_(self):
        super().\_\_init\_\_()

    def forward(self, index: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
        return switch(index, \[branch0, branch1, branch2\], (x,))

switch\_mod = BasicSwitch()

Copy to clipboard

We can eagerly run the model and expect the results vary based on the index:

x = torch.randn(3)
idx0 = torch.tensor(0)
idx1 = torch.tensor(1)
idx2 = torch.tensor(2)
print(switch\_mod(idx0, x), branch0(x))
print(switch\_mod(idx1, x), branch1(x))
print(switch\_mod(idx2, x), branch2(x))

Copy to clipboard

We can export the model for further transformations and deployment:

x = torch.randn(4, 3)
idx = torch.tensor(1)
ep = torch.export.export(
    BasicSwitch(),
    (idx, x),
    dynamic\_shapes={"index": None, "x": {0: torch.export.Dim.DYNAMIC}}
)
print(ep)

Copy to clipboard

Notice that `torch.switch` is lowered to `torch.ops.higher_order.switch`, and branch functions become sub-graph attributes of the top level graph module.

Here is another example showcasing switch with data-dependent index:

def branch0(x: torch.Tensor):
    return x \* 2

def branch1(x: torch.Tensor):
    return x + 10

def branch2(x: torch.Tensor):
    return x \*\* 2

class DataDependentSwitch(torch.nn.Module):
    """
    A usage of switch with data-dependent index.
    """
    def \_\_init\_\_(self):
        super().\_\_init\_\_()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Select branch based on the sign of the sum
        index = torch.clamp((x.sum() > 0).long() + (x.sum() > 5).long(), 0, 2)
        return switch(index, \[branch0, branch1, branch2\], (x,))

x = torch.randn(4, 3)
ep = torch.export.export(
    DataDependentSwitch(),
    (x,),
    dynamic\_shapes={"x": {0: torch.export.Dim.DYNAMIC}}
)
print(ep)

Copy to clipboard

Invariants of torch.ops.higher\_order.switch[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/switch.html#invariants-of-torch-ops-higher-order-switch "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are several useful invariants for `torch.ops.higher_order.switch`:

*   For index:
    
    *   If the index is a constant (e.g. a Python int), the operator may specialize to a single branch
        
    *   If the index is a tensor, it must be a single-element tensor
        
    *   Out-of-range indices are clamped to \[0, len(branches)-1\]
        
*   For branches:
    
    *   All branches must have the same input and output signature
        
    *   The input and output signature will be a flattened tuple
        
    *   They are `torch.fx.GraphModule`
        
    *   Closures in original functions become explicit inputs. No closures.
        
    *   No mutations on inputs or globals are allowed
        
    *   Branch outputs must be tensors or possibly nested tuples/lists/dicts of tensors. Non-tensor leaves must be `int` or `None`. Diverging `int` values across branches are merged into a SymInt for dynamic shapes; `None` must match positionally across every branch.
        
*   For operands:
    
    *   It will be a flat tuple of tensors
        
*   Nesting of `torch.switch` in user program becomes nested graph modules
    

API Reference[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/switch.html#api-reference "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

torch.\_higher\_order\_ops.switch.switch(_index_, _branches_, _operands\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_higher_order_ops/switch.py#L95)
[#](https://docs.pytorch.org/docs/2.15/higher_order_ops/switch.html#torch._higher_order_ops.switch.switch "Link to this definition")

Selects and runs one of N branch functions by index.

Warning

torch.switch is a prototype feature in PyTorch. It has limited support for input and output types. Please look forward to a more stable implementation in a future version of PyTorch. Read more about feature classification at: [https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype](https://pytorch.org/blog/pytorch-feature-classification-changes/#prototype)

Equivalent to: `branches[index](*operands)` with index in `[0, len(branches))`.\
\
Parameters:\
\
*   **index** (_Union__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _,_ [_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]_) – An int or single-element integer tensor indicating which branch to run. Out-of-range values are clamped into `[0, len(branches))`.\
    \
*   **branches** (_Union__\[_[_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
    _\[__Callable__,_ _...__\]__,_ [_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
    _\[__Callable__\]__\]_) – Non-empty sequence of callables. Each must accept operands and return the same structure of outputs.\
    \
*   **operands** (_Tuple_ _of_ _possibly nested dict/list/tuple_ _of_ [_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    ) – Inputs to the branch functions. Defaults to ().\
    \
\
Return type:\
\
[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\
Restrictions:\
\
*   Each branch must have the same signature as operands and return the same output structure (shape, dtype, etc.). Constant `int` and `None` leaves are also permitted in branch outputs and are merged across branches (an unbacked SymInt is introduced when `int` leaves differ between branches).\
    \
*   Branches cannot have in-place mutations on inputs or global variables.\
    \
\
On this page\
\
[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/higher_order_ops/switch.md)\
\
[Show Source](https://docs.pytorch.org/docs/2.15/_sources/higher_order_ops/switch.md.txt)\
\
PyTorch Libraries\
\
*   [ExecuTorch](https://docs.pytorch.org/executorch)\
    \
*   [Helion](https://docs.pytorch.org/helion)\
    \
*   [torchao](https://docs.pytorch.org/ao)\
    \
*   [kineto](https://github.com/pytorch/kineto)\
    \
*   [torchtitan](https://github.com/pytorch/torchtitan)\
    \
*   [TorchRL](https://docs.pytorch.org/rl)\
    \
*   [torchvision](https://docs.pytorch.org/vision)\
    \
*   [torchaudio](https://docs.pytorch.org/audio)\
    \
*   [tensordict](https://docs.pytorch.org/tensordict)\
    \
*   [PyTorch on XLA Devices](https://docs.pytorch.org/xla)\
    \
\
Docs\
----\
\
Access comprehensive developer documentation for PyTorch\
\
[View Docs](https://docs.pytorch.org/docs/stable/index.html)\
\
Tutorials\
---------\
\
Get in-depth tutorials for beginners and advanced developers\
\
[View Tutorials](https://docs.pytorch.org/tutorials)\
\
Resources\
---------\
\
Find development resources and get your questions answered\
\
[View Resources](https://pytorch.org/resources)\
\
To analyze traffic and optimize your experience, we serve cookies on this site. By clicking or navigating, you agree to allow our usage of cookies. As the current maintainers of this site, Facebook’s Cookies Policy applies. Learn more, including about available controls: [Cookies Policy](https://opensource.fb.com/legal/cookie-policy)\
.\
\
|     |     |\
| --- | --- |\
|     |     |\
\
|     |     |\
| --- | --- |\
|     |     |