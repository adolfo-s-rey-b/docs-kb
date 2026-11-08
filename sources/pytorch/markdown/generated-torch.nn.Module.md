Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.nn.Module.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.nn.Module.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.nn.Module.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.nn.Module.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.nn.Module.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.nn.Module.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.nn.Module.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.nn.Module.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.nn.Module.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.nn.Module.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.nn.Module.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.nn.Module.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.nn.Module.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.nn.Module.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.nn.Module.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.nn.Module.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.nn.Module.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.nn.Module.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.nn.Module.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.nn.Module.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.nn.Module.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.nn.Module.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.nn.Module.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.nn.Module.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.nn.Module.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.nn.Module.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.nn.Module.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.nn.Module.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.nn.Module.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.nn.Module.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.nn.Module.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.nn.Module.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.nn.Module.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.nn.Module.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.nn.Module.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.nn.Module.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.nn.Module.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.nn.Module.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.nn.Module.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.nn.Module.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.nn.Module.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.nn.Module.html)

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

Module[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#module "Link to this heading")

===========================================================================================================

_class_ torch.nn.Module(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L407)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "Link to this definition")

Base class for all neural network modules.

Your models should also subclass this class.

Modules can also contain other Modules, allowing them to be nested in a tree structure. You can assign the submodules as regular attributes:

import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
    def \_\_init\_\_(self) \-> None:
        super().\_\_init\_\_()
        self.conv1 \= nn.Conv2d(1, 20, 5)
        self.conv2 \= nn.Conv2d(20, 20, 5)

    def forward(self, x):
        x \= F.relu(self.conv1(x))
        return F.relu(self.conv2(x))

Copy to clipboard

Submodules assigned in this way will be registered, and will also have their parameters converted when you call [`to()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.to "torch.nn.Module.to")
, etc.

Note

As per the example above, an `__init__()` call to the parent class must be made before assignment on the child.

Variables:

**training** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
) – Boolean represents whether this module is in training or evaluation mode.

add\_module(_name_, _module_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L642)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.add_module "Link to this definition")

Add a child module to the current module.

The module can be accessed as an attribute using the given name.

Parameters:

*   **name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – name of the child module. The child module can be accessed from this module using the given name
    
*   **module** ([_Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
    ) – child module to be added to the module.
    

apply(_fn_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1040)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.apply "Link to this definition")

Apply `fn` recursively to every submodule (as returned by `.children()`) as well as self.

Typical use includes initializing the parameters of a model (see also [torch.nn.init](https://docs.pytorch.org/docs/2.15/nn.init.html#nn-init-doc)
).

Parameters:

**fn** ([`Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
 -> None) – function to be applied to each submodule

Returns:

self

Return type:

[Module](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")

Example:

\>>> @torch.no\_grad()
\>>> def init\_weights(m):
\>>>     print(m)
\>>>     if type(m) is nn.Linear:
\>>>         m.weight.fill\_(1.0)
\>>>         print(m.weight)
\>>> net \= nn.Sequential(nn.Linear(2, 2), nn.Linear(2, 2))
\>>> net.apply(init\_weights)
Linear(in\_features=2, out\_features=2, bias=True)
Parameter containing:
tensor(\[\[1., 1.\],\
        \[1., 1.\]\], requires\_grad=True)
Linear(in\_features=2, out\_features=2, bias=True)
Parameter containing:
tensor(\[\[1., 1.\],\
        \[1., 1.\]\], requires\_grad=True)
Sequential(
  (0): Linear(in\_features=2, out\_features=2, bias=True)
  (1): Linear(in\_features=2, out\_features=2, bias=True)
)

Copy to clipboard

bfloat16()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1215)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.bfloat16 "Link to this definition")

Casts all floating point parameters and buffers to `bfloat16` datatype.

Note

This method modifies the module in-place.

Returns:

self

Return type:

[Module](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")

buffers(_recurse\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L2735)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.buffers "Link to this definition")

Return an iterator over module buffers.

Parameters:

**recurse** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
) – if True, then yields buffers of this module and all submodules. Otherwise, yields only buffers that are direct members of this module.

Yields:

_torch.Tensor_ – module buffer

Return type:

[_Iterator_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.15)")
\[[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]

Example:

\>>> for buf in model.buffers():
\>>>     print(type(buf), buf.size())
<class 'torch.Tensor'> (20L,)
<class 'torch.Tensor'> (20L, 1L, 5L, 5L)

Copy to clipboard

children()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L2789)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.children "Link to this definition")

Return an iterator over immediate children modules.

Yields:

_Module_ – a child module

Return type:

[_Iterator_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.15)")
\[[_Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.modules.module.Module")\
\]

compile(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L3057)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.compile "Link to this definition")

Compile this Module’s forward using [`torch.compile()`](https://docs.pytorch.org/docs/2.15/generated/torch.compile.html#torch.compile "torch.compile")
.

This Module’s \_\_call\_\_ method is compiled and all arguments are passed as-is to [`torch.compile()`](https://docs.pytorch.org/docs/2.15/generated/torch.compile.html#torch.compile "torch.compile")
.

See [`torch.compile()`](https://docs.pytorch.org/docs/2.15/generated/torch.compile.html#torch.compile "torch.compile")
 for details on the arguments for this function.

cpu()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1157)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.cpu "Link to this definition")

Move all model parameters and buffers to the CPU.

Note

This method modifies the module in-place.

Returns:

self

Return type:

[Module](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")

cuda(_device\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1081)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.cuda "Link to this definition")

Move all model parameters and buffers to the GPU.

This also makes associated parameters and buffers different objects. So it should be called before constructing the optimizer if the module will live on GPU while being optimized.

Note

This method modifies the module in-place.

Parameters:

**device** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_,_ _optional_) – if specified, all parameters will be copied to that device

Returns:

self

Return type:

[Module](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")

double()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1193)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.double "Link to this definition")

Casts all floating point parameters and buffers to `double` datatype.

Note

This method modifies the module in-place.

Returns:

self

Return type:

[Module](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")

eval()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L2920)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.eval "Link to this definition")

Set the module in evaluation mode.

This has an effect only on certain modules. See the documentation of particular modules for details of their behaviors in training/evaluation mode, i.e. whether they are affected, e.g. [`Dropout`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Dropout.html#torch.nn.Dropout "torch.nn.Dropout")
, `BatchNorm`, etc.

This is equivalent with [`self.train(False)`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.train "torch.nn.Module.train")
.

See [Locally disabling gradient computation](https://docs.pytorch.org/docs/2.15/notes/autograd.html#locally-disable-grad-doc)
 for a comparison between .eval() and several similar mechanisms that may be confused with it.

Returns:

self

Return type:

[Module](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")

extra\_repr()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L2997)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.extra_repr "Link to this definition")

Return the extra representation of the module.

To print customized extra information, you should re-implement this method in your own modules. Both single-line and multi-line strings are acceptable.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

float()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1182)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.float "Link to this definition")

Casts all floating point parameters and buffers to `float` datatype.

Note

This method modifies the module in-place.

Returns:

self

Return type:

[Module](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")

forward(_\*input_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L391)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.forward "Link to this definition")

Define the computation performed at every call.

Should be overridden by all subclasses.

Note

Although the recipe for forward pass needs to be defined within this function, one should call the [`Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
 instance afterwards instead of this since the former takes care of running the registered hooks while the latter silently ignores them.

get\_buffer(_target_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L856)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.get_buffer "Link to this definition")

Return the buffer given by `target` if it exists, otherwise throw an error.

See the docstring for `get_submodule` for a more detailed explanation of this method’s functionality as well as how to correctly specify `target`.

Parameters:

**target** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – The fully-qualified string name of the buffer to look for. (See `get_submodule` for how to specify a fully-qualified string.)

Returns:

The buffer referenced by `target`

Return type:

[torch.Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

Raises:

[**AttributeError**](https://docs.python.org/3/builtins/exceptions.html#AttributeError "(in Python v3.15)")
 – If the target string references an invalid path or resolves to something that is not a buffer

get\_extra\_state()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L892)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.get_extra_state "Link to this definition")

Return any extra state to include in the module’s state\_dict.

Implement this and a corresponding [`set_extra_state()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.set_extra_state "torch.nn.Module.set_extra_state")
 for your module if you need to store extra state. This function is called when building the module’s state\_dict().

Note that extra state should be picklable to ensure working serialization of the state\_dict. We only provide backwards compatibility guarantees for serializing Tensors; other objects may break backwards compatibility if their serialized pickled form changes.

Returns:

Any extra state to store in the module’s state\_dict

Return type:

[object](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")

get\_parameter(_target_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L820)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.get_parameter "Link to this definition")

Return the parameter given by `target` if it exists, otherwise throw an error.

See the docstring for `get_submodule` for a more detailed explanation of this method’s functionality as well as how to correctly specify `target`.

Parameters:

**target** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – The fully-qualified string name of the Parameter to look for. (See `get_submodule` for how to specify a fully-qualified string.)

Returns:

The Parameter referenced by `target`

Return type:

torch.nn.Parameter

Raises:

[**AttributeError**](https://docs.python.org/3/builtins/exceptions.html#AttributeError "(in Python v3.15)")
 – If the target string references an invalid path or resolves to something that is not an `nn.Parameter`

get\_submodule(_target_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L674)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.get_submodule "Link to this definition")

Return the submodule given by `target` if it exists, otherwise throw an error.

For example, let’s say you have an `nn.Module` `A` that looks like this:

A(
    (net\_b): Module(
        (net\_c): Module(
            (conv): Conv2d(16, 33, kernel\_size=(3, 3), stride=(2, 2))
        )
        (linear): Linear(in\_features=100, out\_features=200, bias=True)
    )
)

Copy to clipboard

(The diagram shows an `nn.Module` `A`. `A` which has a nested submodule `net_b`, which itself has two submodules `net_c` and `linear`. `net_c` then has a submodule `conv`.)

To check whether or not we have the `linear` submodule, we would call `get_submodule("net_b.linear")`. To check whether we have the `conv` submodule, we would call `get_submodule("net_b.net_c.conv")`.

The runtime of `get_submodule` is bounded by the degree of module nesting in `target`. A query against `named_modules` achieves the same result, but it is O(N) in the number of transitive modules. So, for a simple check to see if some submodule exists, `get_submodule` should always be used.

Parameters:

**target** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – The fully-qualified string name of the submodule to look for. (See above example for how to specify a fully-qualified string.)

Returns:

The submodule referenced by `target`

Return type:

[torch.nn.Module](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")

Raises:

[**AttributeError**](https://docs.python.org/3/builtins/exceptions.html#AttributeError "(in Python v3.15)")
 – If at any point along the path resulting from the target string the (sub)path resolves to a non-existent attribute name or an object that is not an instance of `nn.Module`.

half()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1204)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.half "Link to this definition")

Casts all floating point parameters and buffers to `half` datatype.

Note

This method modifies the module in-place.

Returns:

self

Return type:

[Module](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")

ipu(_device\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1100)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.ipu "Link to this definition")

Move all model parameters and buffers to the IPU.

This also makes associated parameters and buffers different objects. So it should be called before constructing the optimizer if the module will live on IPU while being optimized.

Note

This method modifies the module in-place.

Parameters:

**device** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_,_ _optional_) – if specified, all parameters will be copied to that device

Returns:

self

Return type:

[Module](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")

load\_state\_dict(_state\_dict_, _strict\=True_, _assign\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L2539)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.load_state_dict "Link to this definition")

Copy parameters and buffers from [`state_dict`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.state_dict "torch.nn.Module.state_dict")
 into this module and its descendants.

If `strict` is `True`, then the keys of [`state_dict`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.state_dict "torch.nn.Module.state_dict")
 must exactly match the keys returned by this module’s [`state_dict()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.state_dict "torch.nn.Module.state_dict")
 function.

Warning

If `assign` is `True` the optimizer must be created after the call to [`load_state_dict`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.load_state_dict "torch.nn.Module.load_state_dict")
 unless [`get_swap_module_params_on_conversion()`](https://docs.pytorch.org/docs/2.15/future_mod.html#torch.__future__.get_swap_module_params_on_conversion "torch.__future__.get_swap_module_params_on_conversion")
 is `True`.

Parameters:

*   **state\_dict** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    ) – a dict containing parameters and persistent buffers.
    
*   **strict** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether to strictly enforce that the keys in [`state_dict`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.state_dict "torch.nn.Module.state_dict")
     match the keys returned by this module’s [`state_dict()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.state_dict "torch.nn.Module.state_dict")
     function. Default: `True`
    
*   **assign** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – When set to `False`, the properties of the tensors in the current module are preserved whereas setting it to `True` preserves properties of the Tensors in the state dict. The only exception is the `requires_grad` field of `Parameter` for which the value from the module is preserved. Default: `False`
    

Returns:

*   `missing_keys` is a list of str containing any keys that are expected
    
    by this module but missing from the provided `state_dict`.
    
*   `unexpected_keys` is a list of str containing the keys that are not
    
    expected by this module but present in the provided `state_dict`.
    

Return type:

`NamedTuple` with `missing_keys` and `unexpected_keys` fields

Note

If a parameter or buffer is registered as `None` and its corresponding key exists in [`state_dict`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.state_dict "torch.nn.Module.state_dict")
, [`load_state_dict()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.load_state_dict "torch.nn.Module.load_state_dict")
 will raise a `RuntimeError`.

modules(_remove\_duplicate\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L2818)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.modules "Link to this definition")

Return an iterator over all modules in the network.

Parameters:

**remove\_duplicate** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
) – whether to remove the duplicated module instances in the result or not.

Yields:

_Module_ – a module in the network

Return type:

[_Iterator_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.15)")
\[[_Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.modules.module.Module")\
\]

Note

Duplicate modules are returned only once by default. In the following example, `l` will be returned only once.

Example:

\>>> l \= nn.Linear(2, 2)
\>>> net \= nn.Sequential(l, l)
\>>> for idx, m in enumerate(net.modules()):
...     print(idx, '->', m)

0 -> Sequential(
  (0): Linear(in\_features=2, out\_features=2, bias=True)
  (1): Linear(in\_features=2, out\_features=2, bias=True)
)
1 -> Linear(in\_features=2, out\_features=2, bias=True)

Copy to clipboard

mtia(_device\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1138)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.mtia "Link to this definition")

Move all model parameters and buffers to the MTIA.

This also makes associated parameters and buffers different objects. So it should be called before constructing the optimizer if the module will live on MTIA while being optimized.

Note

This method modifies the module in-place.

Parameters:

**device** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_,_ _optional_) – if specified, all parameters will be copied to that device

Returns:

self

Return type:

[Module](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")

named\_buffers(_prefix\=''_, _recurse\=True_, _remove\_duplicate\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L2758)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.named_buffers "Link to this definition")

Return an iterator over module buffers, yielding both the name of the buffer as well as the buffer itself.

Parameters:

*   **prefix** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – prefix to prepend to all buffer names.
    
*   **recurse** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – if True, then yields buffers of this module and all submodules. Otherwise, yields only buffers that are direct members of this module. Defaults to True.
    
*   **remove\_duplicate** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether to remove the duplicated buffers in the result. Defaults to True.
    

Yields:

_(str, torch.Tensor)_ – Tuple containing the name and buffer

Return type:

[_Iterator_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.15)")
\[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
\]\]

Example:

\>>> for name, buf in self.named\_buffers():
\>>>     if name in \['running\_var'\]:
\>>>         print(buf.size())

Copy to clipboard

named\_children()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L2798)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.named_children "Link to this definition")

Return an iterator over immediate children modules, yielding both the name of the module as well as the module itself.

Yields:

_(str, Module)_ – Tuple containing a name and child module

Return type:

[_Iterator_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.15)")
\[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [_Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.modules.module.Module")\
\]\]

Example:

\>>> for name, module in model.named\_children():
\>>>     if name in \['conv4', 'conv5'\]:
\>>>         print(module)

Copy to clipboard

named\_modules(_memo\=None_, _prefix\=''_, _remove\_duplicate\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L2849)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.named_modules "Link to this definition")

Return an iterator over all modules in the network, yielding both the name of the module as well as the module itself.

Parameters:

*   **memo** ([_set_](https://docs.python.org/3/builtins/stdtypes.html#set "(in Python v3.15)")
    _\[_[_Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.modules.module.Module")\
    _\]_ _|_ _None_) – a memo to store the set of modules already added to the result
    
*   **prefix** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – a prefix that will be added to the name of the module
    
*   **remove\_duplicate** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – whether to remove the duplicated module instances in the result or not
    

Yields:

_(str, Module)_ – Tuple of name and module

Note

Duplicate modules are returned only once. In the following example, `l` will be returned only once.

Example:

\>>> l \= nn.Linear(2, 2)
\>>> net \= nn.Sequential(l, l)
\>>> for idx, m in enumerate(net.named\_modules()):
...     print(idx, '->', m)

0 -> ('', Sequential(
  (0): Linear(in\_features=2, out\_features=2, bias=True)
  (1): Linear(in\_features=2, out\_features=2, bias=True)
))
1 -> ('0', Linear(in\_features=2, out\_features=2, bias=True))

Copy to clipboard

named\_parameters(_prefix\=''_, _recurse\=True_, _remove\_duplicate\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L2703)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.named_parameters "Link to this definition")

Return an iterator over module parameters, yielding both the name of the parameter as well as the parameter itself.

Parameters:

*   **prefix** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – prefix to prepend to all parameter names.
    
*   **recurse** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – if True, then yields parameters of this module and all submodules. Otherwise, yields only parameters that are direct members of this module.
    
*   **remove\_duplicate** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether to remove the duplicated parameters in the result. Defaults to True.
    

Yields:

_(str, Parameter)_ – Tuple containing the name and parameter

Return type:

[_Iterator_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.15)")
\[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [_Parameter_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "torch.nn.parameter.Parameter")\
\]\]

Example:

\>>> for name, param in self.named\_parameters():
\>>>     if name in \['bias'\]:
\>>>         print(param.size())

Copy to clipboard

parameters(_recurse\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L2674)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.parameters "Link to this definition")

Return an iterator over module parameters.

The exact order of the returned parameters is unspecified, but repeated calls to the `parameters()` method of an unchanged module return the parameters in the same order.

This is typically passed to an optimizer.

Parameters:

**recurse** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
) – if True, then yields parameters of this module and all submodules. Otherwise, yields only parameters that are direct members of this module.

Yields:

_Parameter_ – module parameter

Return type:

[_Iterator_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.15)")
\[[_Parameter_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "torch.nn.parameter.Parameter")\
\]

Example:

\>>> for param in model.parameters():
\>>>     print(type(param), param.size())
<class 'torch.Tensor'> (20L,)
<class 'torch.Tensor'> (20L, 1L, 5L, 5L)

Copy to clipboard

register\_backward\_hook(_hook_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1443)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.register_backward_hook "Link to this definition")

Register a backward hook on the module.

This function is deprecated in favor of [`register_full_backward_hook()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.register_full_backward_hook "torch.nn.Module.register_full_backward_hook")
 and the behavior of this function will change in future versions.

Returns:

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`

register\_buffer(_name_, _tensor_, _persistent\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L528)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.register_buffer "Link to this definition")

Add a buffer to the module.

This is typically used to register a buffer that should not be considered a model parameter. For example, BatchNorm’s `running_mean` is not a parameter, but is part of the module’s state. Buffers, by default, are persistent and will be saved alongside parameters. This behavior can be changed by setting `persistent` to `False`. The only difference between a persistent buffer and a non-persistent buffer is that the latter will not be a part of this module’s [`state_dict`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.state_dict "torch.nn.Module.state_dict")
.

Buffers can be accessed as attributes using given names.

Parameters:

*   **name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – name of the buffer. The buffer can be accessed from this module using the given name
    
*   **tensor** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _or_ _None_) – buffer to be registered. If `None`, then operations that run on buffers, such as [`cuda`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.cuda "torch.nn.Module.cuda")
    , are ignored. If `None`, the buffer is **not** included in the module’s [`state_dict`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.state_dict "torch.nn.Module.state_dict")
    .
    
*   **persistent** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – whether the buffer is part of this module’s [`state_dict`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.state_dict "torch.nn.Module.state_dict")
    .
    

Example:

\>>> self.register\_buffer('running\_mean', torch.zeros(num\_features))

Copy to clipboard

register\_forward\_hook(_hook_, _\*_, _prepend\=False_, _with\_kwargs\=False_, _always\_call\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1696)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.register_forward_hook "Link to this definition")

Register a forward hook on the module.

The hook will be called every time after [`forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.forward "torch.nn.Module.forward")
 has computed an output.

If `with_kwargs` is `False` or not specified, the input contains only the positional arguments given to the module. Keyword arguments won’t be passed to the hooks and only to the `forward`. The hook can modify the output. It can modify the input inplace but it will not have effect on forward since this is called after [`forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.forward "torch.nn.Module.forward")
 is called. The hook should have the following signature:

hook(module, args, output) \-> None or modified output

Copy to clipboard

If `with_kwargs` is `True`, the forward hook will be passed the `kwargs` given to the forward function and be expected to return the output possibly modified. The hook should have the following signature:

hook(module, args, kwargs, output) \-> None or modified output

Copy to clipboard

Parameters:

*   **hook** (_Callable_) – The user defined hook to be registered.
    
*   **prepend** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True`, the provided `hook` will be fired before all existing `forward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
    . Otherwise, the provided `hook` will be fired after all existing `forward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
    . Note that global `forward` hooks registered with `register_module_forward_hook()` will fire before all hooks registered by this method. Default: `False`
    
*   **with\_kwargs** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True`, the `hook` will be passed the kwargs given to the forward function. Default: `False`
    
*   **always\_call** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True` the `hook` will be run regardless of whether an exception is raised while calling the Module. Default: `False`
    

Returns:

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`

register\_forward\_pre\_hook(_hook_, _\*_, _prepend\=False_, _with\_kwargs\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1633)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.register_forward_pre_hook "Link to this definition")

Register a forward pre-hook on the module.

The hook will be called every time before [`forward()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.forward "torch.nn.Module.forward")
 is invoked.

If `with_kwargs` is false or not specified, the input contains only the positional arguments given to the module. Keyword arguments won’t be passed to the hooks and only to the `forward`. The hook can modify the input. User can either return a tuple or a single modified value in the hook. We will wrap the value into a tuple if a single value is returned (unless that value is already a tuple). The hook should have the following signature:

hook(module, args) \-> None or modified input

Copy to clipboard

If `with_kwargs` is true, the forward pre-hook will be passed the kwargs given to the forward function. And if the hook modifies the input, both the args and kwargs should be returned. The hook should have the following signature:

hook(module, args, kwargs) \-> None or a tuple of modified input and kwargs

Copy to clipboard

Parameters:

*   **hook** (_Callable_) – The user defined hook to be registered.
    
*   **prepend** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If true, the provided `hook` will be fired before all existing `forward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
    . Otherwise, the provided `hook` will be fired after all existing `forward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
    . Note that global `forward_pre` hooks registered with `register_module_forward_pre_hook()` will fire before all hooks registered by this method. Default: `False`
    
*   **with\_kwargs** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If true, the `hook` will be passed the kwargs given to the forward function. Default: `False`
    

Returns:

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`

register\_full\_backward\_hook(_hook_, _prepend\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1469)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.register_full_backward_hook "Link to this definition")

Register a backward hook on the module.

The hook will be called every time the gradients with respect to a module are computed, and its firing rules are as follows:

> 1.  Ordinarily, the hook fires when the gradients are computed with respect to the module inputs.
>     
> 2.  If none of the module inputs require gradients, the hook will fire when the gradients are computed with respect to module outputs.
>     
> 3.  If none of the module outputs require gradients, then the hooks will not fire.
>     

The hook should have the following signature:

hook(module, grad\_input, grad\_output) \-> tuple(Tensor) or None

Copy to clipboard

The `grad_input` and `grad_output` are tuples that contain the gradients with respect to the inputs and outputs respectively. The hook should not modify its arguments, but it can optionally return a new gradient with respect to the input that will be used in place of `grad_input` in subsequent computations. `grad_input` will only correspond to the inputs given as positional arguments and all kwarg arguments are ignored. Entries in `grad_input` and `grad_output` will be `None` for all non-Tensor arguments.

For technical reasons, when this hook is applied to a Module, its forward function will receive a view of each Tensor passed to the Module. Similarly the caller will receive a view of each Tensor returned by the Module’s forward function.

Warning

Modifying inputs or outputs inplace is not allowed when using backward hooks and will raise an error.

Parameters:

*   **hook** (_Callable_) – The user-defined hook to be registered.
    
*   **prepend** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If true, the provided `hook` will be fired before all existing `backward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
    . Otherwise, the provided `hook` will be fired after all existing `backward` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
    . Note that global `backward` hooks registered with `register_module_full_backward_hook()` will fire before all hooks registered by this method.
    

Returns:

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`

register\_full\_backward\_pre\_hook(_hook_, _prepend\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1394)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.register_full_backward_pre_hook "Link to this definition")

Register a backward pre-hook on the module.

The hook will be called every time the gradients for the module are computed. The hook should have the following signature:

hook(module, grad\_output) \-> tuple\[Tensor, ...\], Tensor or None

Copy to clipboard

The `grad_output` is a tuple. The hook should not modify its arguments, but it can optionally return a new gradient with respect to the output that will be used in place of `grad_output` in subsequent computations. Entries in `grad_output` will be `None` for all non-Tensor arguments.

For technical reasons, when this hook is applied to a Module, its forward function will receive a view of each Tensor passed to the Module. Similarly the caller will receive a view of each Tensor returned by the Module’s forward function.

Warning

Modifying inputs inplace is not allowed when using backward hooks and will raise an error.

Parameters:

*   **hook** (_Callable_) – The user-defined hook to be registered.
    
*   **prepend** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If true, the provided `hook` will be fired before all existing `backward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
    . Otherwise, the provided `hook` will be fired after all existing `backward_pre` hooks on this [`torch.nn.Module`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")
    . Note that global `backward_pre` hooks registered with `register_module_full_backward_pre_hook()` will fire before all hooks registered by this method.
    

Returns:

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`

register\_load\_state\_dict\_post\_hook(_hook_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L2325)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.register_load_state_dict_post_hook "Link to this definition")

Register a post-hook to be run after module’s `load_state_dict()` is called.

It should have the following signature::

hook(module, incompatible\_keys) -> None

The `module` argument is the current module that this hook is registered on, and the `incompatible_keys` argument is a `NamedTuple` consisting of attributes `missing_keys` and `unexpected_keys`. `missing_keys` is a `list` of `str` containing the missing keys and `unexpected_keys` is a `list` of `str` containing the unexpected keys.

The given incompatible\_keys can be modified inplace if needed.

Note that the checks performed when calling [`load_state_dict()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.load_state_dict "torch.nn.Module.load_state_dict")
 with `strict=True` are affected by modifications the hook makes to `missing_keys` or `unexpected_keys`, as expected. Additions to either set of keys will result in an error being thrown when `strict=True`, and clearing out both missing and unexpected keys will avoid an error.

Returns:

a handle that can be used to remove the added hook by calling `handle.remove()`

Return type:

`torch.utils.hooks.RemovableHandle`

register\_load\_state\_dict\_pre\_hook(_hook_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L2313)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.register_load_state_dict_pre_hook "Link to this definition")

Register a pre-hook to be run before module’s `load_state_dict()` is called.

It should have the following signature::

hook(module, state\_dict, prefix, local\_metadata, strict, missing\_keys, unexpected\_keys, error\_msgs) -> None # noqa: B950

Parameters:

**hook** (_Callable_) – Callable hook that will be invoked before loading the state dict.

register\_module(_name_, _module_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L670)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.register_module "Link to this definition")

Alias for [`add_module()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.add_module "torch.nn.Module.add_module")
.

register\_parameter(_name_, _param_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L592)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.register_parameter "Link to this definition")

Add a parameter to the module.

The parameter can be accessed as an attribute using given name.

Parameters:

*   **name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – name of the parameter. The parameter can be accessed from this module using the given name
    
*   **param** ([_Parameter_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter "torch.nn.parameter.Parameter")
     _or_ _None_) – parameter to be added to the module. If `None`, then operations that run on parameters, such as [`cuda`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.cuda "torch.nn.Module.cuda")
    , are ignored. If `None`, the parameter is **not** included in the module’s [`state_dict`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.state_dict "torch.nn.Module.state_dict")
    .
    

register\_state\_dict\_post\_hook(_hook_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L2115)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.register_state_dict_post_hook "Link to this definition")

Register a post-hook for the [`state_dict()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.state_dict "torch.nn.Module.state_dict")
 method.

It should have the following signature::

hook(module, state\_dict, prefix, local\_metadata) -> None

The registered hooks can modify the `state_dict` inplace.

register\_state\_dict\_pre\_hook(_hook_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L2139)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.register_state_dict_pre_hook "Link to this definition")

Register a pre-hook for the [`state_dict()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.state_dict "torch.nn.Module.state_dict")
 method.

It should have the following signature::

hook(module, prefix, keep\_vars) -> None

The registered hooks can be used to perform pre-processing before the `state_dict` call is made.

requires\_grad\_(_requires\_grad\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L2938)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.requires_grad_ "Link to this definition")

Change if autograd should record operations on parameters in this module.

This method sets the parameters’ `requires_grad` attributes in-place.

This method is helpful for freezing part of the module for finetuning or training parts of a model individually (e.g., GAN training).

See [Locally disabling gradient computation](https://docs.pytorch.org/docs/2.15/notes/autograd.html#locally-disable-grad-doc)
 for a comparison between .requires\_grad\_() and several similar mechanisms that may be confused with it.

Parameters:

**requires\_grad** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
) – whether autograd should record operations on parameters in this module. Default: `True`.

Returns:

self

Return type:

[Module](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")

set\_extra\_state(_state_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L913)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.set_extra_state "Link to this definition")

Set extra state contained in the loaded state\_dict.

This function is called from [`load_state_dict()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.load_state_dict "torch.nn.Module.load_state_dict")
 to handle any extra state found within the state\_dict. Implement this function and a corresponding [`get_extra_state()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.get_extra_state "torch.nn.Module.get_extra_state")
 for your module if you need to store extra state within its state\_dict.

Parameters:

**state** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
) – Extra state from the state\_dict

set\_submodule(_target_, _module_, _strict\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L739)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.set_submodule "Link to this definition")

Set the submodule given by `target` if it exists, otherwise throw an error.

Note

If `strict` is set to `False` (default), the method will replace an existing submodule or create a new submodule if the parent module exists. If `strict` is set to `True`, the method will only attempt to replace an existing submodule and throw an error if the submodule does not exist.

For example, let’s say you have an `nn.Module` `A` that looks like this:

A(
    (net\_b): Module(
        (net\_c): Module(
            (conv): Conv2d(3, 3, 3)
        )
        (linear): Linear(3, 3)
    )
)

Copy to clipboard

(The diagram shows an `nn.Module` `A`. `A` has a nested submodule `net_b`, which itself has two submodules `net_c` and `linear`. `net_c` then has a submodule `conv`.)

To override the `Conv2d` with a new submodule `Linear`, you could call `set_submodule("net_b.net_c.conv", nn.Linear(1, 1))` where `strict` could be `True` or `False`

To add a new submodule `Conv2d` to the existing `net_b` module, you would call `set_submodule("net_b.conv", nn.Conv2d(1, 1, 1))`.

In the above if you set `strict=True` and call `set_submodule("net_b.conv", nn.Conv2d(1, 1, 1), strict=True)`, an AttributeError will be raised because `net_b` does not have a submodule named `conv`.

Parameters:

*   **target** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The fully-qualified string name of the submodule to look for. (See above example for how to specify a fully-qualified string.)
    
*   **module** ([_Module_](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.modules.module.Module")
    ) – The module to set the submodule to.
    
*   **strict** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `False`, the method will replace an existing submodule or create a new submodule if the parent module exists. If `True`, the method will only attempt to replace an existing submodule and throw an error if the submodule doesn’t already exist.
    

Raises:

*   [**ValueError**](https://docs.python.org/3/builtins/exceptions.html#ValueError "(in Python v3.15)")
     – If the `target` string is empty or if `module` is not an instance of `nn.Module`.
    
*   [**AttributeError**](https://docs.python.org/3/builtins/exceptions.html#AttributeError "(in Python v3.15)")
     – If at any point along the path resulting from the `target` string the (sub)path resolves to a non-existent attribute name or an object that is not an instance of `nn.Module`.
    

share\_memory()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L2990)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.share_memory "Link to this definition")

See [`torch.Tensor.share_memory_()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.share_memory_.html#torch.Tensor.share_memory_ "torch.Tensor.share_memory_")
.

Return type:

[_Self_](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.15)")

state\_dict(_\*_, _destination: T\_destination_, _prefix: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 \= ''_, _keep\_vars: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= False_) → T\_destination[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L2203)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.state_dict "Link to this definition")

state\_dict(_\*_, _prefix: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 \= ''_, _keep\_vars: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= False_) → [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\]

Return a dictionary containing references to the whole state of the module.

Both parameters and persistent buffers (e.g. running averages) are included. Keys are corresponding parameter and buffer names. Parameters and buffers set to `None` are not included.

Note

The returned object is a shallow copy. It contains references to the module’s parameters and buffers.

Warning

Currently `state_dict()` also accepts positional arguments for `destination`, `prefix` and `keep_vars` in order. However, this is being deprecated and keyword arguments will be enforced in future releases.

Warning

Please avoid the use of argument `destination` as it is not designed for end-users.

Parameters:

*   **destination** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _,_ _optional_) – If provided, the state of module will be updated into the dict and the same object is returned. Otherwise, an `OrderedDict` will be created and returned. Default: `None`.
    
*   **prefix** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – a prefix added to parameter and buffer names to compose the keys in state\_dict. Default: `''`.
    
*   **keep\_vars** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – by default the [`Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     s returned in the state dict are detached from autograd. If it’s set to `True`, detaching will not be performed. Default: `False`.
    

Returns:

a dictionary containing a whole state of the module

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")

Example:

\>>> module.state\_dict().keys()
\['bias', 'weight'\]

Copy to clipboard

to(_device: [str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
 | [device](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
 | [int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= ..._, _dtype: [dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
 | [None](https://docs.python.org/3/builtins/constants.html#None "(in Python v3.15)")
 \= ..._, _non\_blocking: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= ..._) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.15)")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1259)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.to "Link to this definition")

to(_dtype: [dtype](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
_, _non\_blocking: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= ..._) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.15)")

to(_tensor: [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_, _non\_blocking: [bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
 \= ..._) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.15)")

to(_memory\_format: [memory\_format](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")
_) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.15)")

Move and/or cast the parameters and buffers.

This can be called as

to(_device\=None_, _dtype\=None_, _non\_blocking\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1259)

to(_dtype_, _non\_blocking\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1259)

to(_tensor_, _non\_blocking\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1259)

to(_memory\_format\=torch.channels\_last_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1259)

Its signature is similar to [`torch.Tensor.to()`](https://docs.pytorch.org/docs/2.15/generated/torch.Tensor.to.html#torch.Tensor.to "torch.Tensor.to")
, but only accepts floating point or complex `dtype`s. In addition, this method will only cast the floating point or complex parameters and buffers to `dtype` (if given). The integral parameters and buffers will be moved `device`, if that is given, but with dtypes unchanged. When `non_blocking` is set, it tries to convert/move asynchronously with respect to the host if possible, e.g., moving CPU Tensors with pinned memory to CUDA devices.

See below for examples.

Note

This method modifies the module in-place.

Parameters:

*   **device** ([`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    ) – the desired device of the parameters and buffers in this module
    
*   **dtype** ([`torch.dtype`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.dtype "torch.dtype")
    ) – the desired floating point or complex dtype of the parameters and buffers in this module
    
*   **tensor** ([_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – Tensor whose dtype and device are the desired dtype and device for all parameters and buffers in this module
    
*   **memory\_format** ([`torch.memory_format`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.memory_format "torch.memory_format")
    ) – the desired memory format for 4D parameters and buffers in this module (keyword only argument)
    

Returns:

self

Return type:

[Module](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")

Examples:

\>>> linear \= nn.Linear(2, 2)
\>>> linear.weight
Parameter containing:
tensor(\[\[ 0.1913, -0.3420\],\
        \[-0.5113, -0.2325\]\])
\>>> linear.to(torch.double)
Linear(in\_features=2, out\_features=2, bias=True)
\>>> linear.weight
Parameter containing:
tensor(\[\[ 0.1913, -0.3420\],\
        \[-0.5113, -0.2325\]\], dtype=torch.float64)
\>>> gpu1 \= torch.device("cuda:1")
\>>> linear.to(gpu1, dtype\=torch.half, non\_blocking\=True)
Linear(in\_features=2, out\_features=2, bias=True)
\>>> linear.weight
Parameter containing:
tensor(\[\[ 0.1914, -0.3420\],\
        \[-0.5112, -0.2324\]\], dtype=torch.float16, device='cuda:1')
\>>> cpu \= torch.device("cpu")
\>>> linear.to(cpu)
Linear(in\_features=2, out\_features=2, bias=True)
\>>> linear.weight
Parameter containing:
tensor(\[\[ 0.1914, -0.3420\],\
        \[-0.5112, -0.2324\]\], dtype=torch.float16)

\>>> linear \= nn.Linear(2, 2, bias\=None).to(torch.cdouble)
\>>> linear.weight
Parameter containing:
tensor(\[\[ 0.3741+0.j,  0.2382+0.j\],\
        \[ 0.5593+0.j, -0.4443+0.j\]\], dtype=torch.complex128)
\>>> linear(torch.ones(3, 2, dtype\=torch.cdouble))
tensor(\[\[0.6122+0.j, 0.1150+0.j\],\
        \[0.6122+0.j, 0.1150+0.j\],\
        \[0.6122+0.j, 0.1150+0.j\]\], dtype=torch.complex128)

Copy to clipboard

to\_empty(_\*_, _device_, _recurse\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1226)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.to_empty "Link to this definition")

Move the parameters and buffers to the specified device without copying storage.

Parameters:

*   **device** ([`torch.device`](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#torch.device "torch.device")
    ) – The desired device of the parameters and buffers in this module.
    
*   **recurse** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether parameters and buffers of submodules should be recursively moved to the specified device.
    

Returns:

self

Return type:

[Module](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")

train(_mode\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L2898)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.train "Link to this definition")

Set the module in training mode.

This has an effect only on certain modules. See the documentation of particular modules for details of their behaviors in training/evaluation mode, i.e., whether they are affected, e.g. [`Dropout`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Dropout.html#torch.nn.Dropout "torch.nn.Dropout")
, `BatchNorm`, etc.

Parameters:

**mode** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
) – whether to set training mode (`True`) or evaluation mode (`False`). Default: `True`.

Returns:

self

Return type:

[Module](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")

type(_dst\_type_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1168)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.type "Link to this definition")

Casts all parameters and buffers to `dst_type`.

Note

This method modifies the module in-place.

Parameters:

**dst\_type** ([_type_](https://docs.python.org/3/builtins/functions.html#type "(in Python v3.15)")
 _or_ _string_) – the desired type

Returns:

self

Return type:

[Module](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")

xpu(_device\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L1119)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.xpu "Link to this definition")

Move all model parameters and buffers to the XPU.

This also makes associated parameters and buffers different objects. So it should be called before constructing optimizer if the module will live on XPU while being optimized.

Note

This method modifies the module in-place.

Parameters:

**device** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
_,_ _optional_) – if specified, all parameters will be copied to that device

Returns:

self

Return type:

[Module](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module "torch.nn.Module")

zero\_grad(_set\_to\_none\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/nn/modules/module.py#L2961)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Module.html#torch.nn.Module.zero_grad "Link to this definition")

Reset gradients of all model parameters.

See similar function under [`torch.optim.Optimizer`](https://docs.pytorch.org/docs/2.15/optim.html#torch.optim.Optimizer "torch.optim.Optimizer")
 for more context.

Parameters:

**set\_to\_none** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
) – instead of setting to zero, set the grads to None. See [`torch.optim.Optimizer.zero_grad()`](https://docs.pytorch.org/docs/2.15/generated/torch.optim.Optimizer.zero_grad.html#torch.optim.Optimizer.zero_grad "torch.optim.Optimizer.zero_grad")
 for details.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.nn.Module.rst.txt)

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