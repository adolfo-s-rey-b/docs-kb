Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.func.functionalize.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.func.functionalize.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.func.functionalize.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.func.functionalize.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.func.functionalize.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.func.functionalize.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.func.functionalize.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.func.functionalize.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.func.functionalize.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.func.functionalize.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.func.functionalize.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.func.functionalize.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.func.functionalize.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.func.functionalize.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.func.functionalize.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.func.functionalize.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.func.functionalize.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.func.functionalize.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.func.functionalize.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.func.functionalize.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.func.functionalize.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.func.functionalize.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.func.functionalize.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.func.functionalize.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.func.functionalize.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.func.functionalize.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.func.functionalize.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.func.functionalize.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.func.functionalize.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.func.functionalize.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.func.functionalize.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.func.functionalize.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.func.functionalize.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.func.functionalize.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.func.functionalize.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.func.functionalize.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.func.functionalize.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.func.functionalize.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.func.functionalize.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.func.functionalize.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.func.functionalize.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.func.functionalize.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.func.functionalize.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.func.functionalize.html)

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

torch.func.functionalize[#](https://docs.pytorch.org/docs/2.15/generated/torch.func.functionalize.html#torch-func-functionalize "Link to this heading")

========================================================================================================================================================

torch.func.functionalize(_func_, _\*_, _remove\='mutations'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_functorch/eager_transforms.py#L1603)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.func.functionalize.html#torch.func.functionalize "Link to this definition")

functionalize is a transform that can be used to remove (intermediate) mutations and aliasing from a function, while preserving the function’s semantics.

`functionalize(func)` returns a new function with the same semantics as `func`, but with all intermediate mutations removed. Every inplace operation performed on an intermediate tensor: `intermediate.foo_()` gets replaced by its out-of-place equivalent: `intermediate_updated = intermediate.foo()`.

functionalize is useful for shipping a pytorch program off to backends or compilers that aren’t able to easily represent mutations or aliasing operators.

Parameters:

*   **func** (_Callable__\[__...__,_ _Any__\]_) – A Python function that takes one or more arguments.
    
*   **remove** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – An optional string argument, that takes on either the value ‘mutations’ or ‘mutations\_and\_views’. If ‘mutations’ is passed in then all mutating operators will be replaced with their non-mutating equivalents. If ‘mutations\_and\_views’ is passed in, then additionally, all aliasing operators will be replaced with their non-aliasing equivalents. Default: ‘mutations’.
    

Returns:

Returns a new “functionalized” function. It takes the same inputs as `func`, and has the same behavior, but any mutations (and optionally aliasing) performed on intermediate tensors in the function will be removed.

Return type:

Callable\[…, Any\]

functionalize will also remove mutations (and views) that were performed on function inputs. However to preserve semantics, functionalize will “fix up” the mutations after the transform has finished running, by detecting if any tensor inputs “should have” been mutated, and copying the new data back to the inputs if necessary.

Example:

\>>> import torch
\>>> from torch.fx.experimental.proxy\_tensor import make\_fx
\>>> from torch.func import functionalize
\>>>
\>>> \# A function that uses mutations and views, but only on intermediate tensors.
\>>> def f(a):
...     b \= a + 1
...     c \= b.view(\-1)
...     c.add\_(1)
...     return b
...
\>>> inpt \= torch.randn(2)
\>>>
\>>> out1 \= f(inpt)
\>>> out2 \= functionalize(f)(inpt)
\>>>
\>>> \# semantics are the same (outputs are equivalent)
\>>> print(torch.allclose(out1, out2))
True
\>>>
\>>> f\_traced \= make\_fx(f)(inpt)
\>>> f\_no\_mutations\_traced \= make\_fx(functionalize(f))(inpt)
\>>> f\_no\_mutations\_and\_views\_traced \= make\_fx(functionalize(f, remove\='mutations\_and\_views'))(inpt)
\>>>
\>>> print(f\_traced.code)

def forward(self, a\_1):
    add = torch.ops.aten.add(a\_1, 1);  a\_1 = None
    view = torch.ops.aten.view(add, \[-1\])
    add\_ = torch.ops.aten.add\_(view, 1);  view = None
    return add

\>>> print(f\_no\_mutations\_traced.code)

def forward(self, a\_1):
    add = torch.ops.aten.add(a\_1, 1);  a\_1 = None
    view = torch.ops.aten.view(add, \[-1\]);  add = None
    add\_1 = torch.ops.aten.add(view, 1);  view = None
    view\_1 = torch.ops.aten.view(add\_1, \[2\]);  add\_1 = None
    return view\_1

\>>> print(f\_no\_mutations\_and\_views\_traced.code)

def forward(self, a\_1):
    add = torch.ops.aten.add(a\_1, 1);  a\_1 = None
    view\_copy = torch.ops.aten.view\_copy(add, \[-1\]);  add = None
    add\_1 = torch.ops.aten.add(view\_copy, 1);  view\_copy = None
    view\_copy\_1 = torch.ops.aten.view\_copy(add\_1, \[2\]);  add\_1 = None
    return view\_copy\_1

\>>> \# A function that mutates its input tensor
\>>> def f(a):
...     b \= a.view(\-1)
...     b.add\_(1)
...     return a
...
\>>> f\_no\_mutations\_and\_views\_traced \= make\_fx(functionalize(f, remove\='mutations\_and\_views'))(inpt)
\>>> #
\>>> \# All mutations and views have been removed,
\>>> \# but there is an extra copy\_ in the graph to correctly apply the mutation to the input
\>>> \# after the function has completed.
\>>> print(f\_no\_mutations\_and\_views\_traced.code)

def forward(self, a\_1):
    view\_copy = torch.ops.aten.view\_copy(a\_1, \[-1\])
    add = torch.ops.aten.add(view\_copy, 1);  view\_copy = None
    view\_copy\_1 = torch.ops.aten.view\_copy(add, \[2\]);  add = None
    copy\_ = torch.ops.aten.copy\_(a\_1, view\_copy\_1);  a\_1 = None
    return view\_copy\_1

Copy to clipboard

There are a few “failure modes” for functionalize that are worth calling out:

1.  Like other torch.func transforms, functionalize() doesn’t work with functions that directly use .backward(). The same is true for torch.autograd.grad. If you want to use autograd, you can compute gradients directly with functionalize(grad(f)).
    
2.  Like other torch.func transforms, functionalize() doesn’t work with global state. If you call functionalize(f) on a function that takes views / mutations of non-local state, functionalization will simply no-op and pass the view/mutation calls directly to the backend. One way to work around this is to ensure that any non-local state creation is wrapped into a larger function, which you then call functionalize on.
    
3.  resize\_() has some limitations: functionalize will only work on programs that use resize\_()\` as long as the tensor being resized is not a view.
    
4.  as\_strided() has some limitations: functionalize will not work on as\_strided() calls that result in tensors with overlapping memory.
    

Finally, a helpful mental model for understanding functionalization is that most user pytorch programs are writing with the public torch API. When executed, torch operators are generally decomposed into our internal C++ “ATen” API. The logic for functionalization happens entirely at the level of ATen. Functionalization knows how to take every aliasing operator in ATen, and map it to its non-aliasing equivalent (e.g. `tensor.view({-1})` -> `at::view_copy(tensor, {-1})`), and how to take every mutating operator in ATen, and map it to its non-mutating equivalent (e.g. `tensor.add_(1)` -> `at::add(tensor, -1)`), while tracking aliases and mutations out-of-line to know when to fix things up. Information about which ATen operators are aliasing or mutating all comes from [pytorch/pytorch](https://github.com/pytorch/pytorch/blob/master/aten/src/ATen/native/native_functions.yaml)
.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.func.functionalize.rst.txt)

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