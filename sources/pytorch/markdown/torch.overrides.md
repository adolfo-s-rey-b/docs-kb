Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/torch.overrides.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/torch.overrides.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/torch.overrides.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/torch.overrides.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/torch.overrides.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/torch.overrides.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/torch.overrides.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/torch.overrides.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/torch.overrides.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/torch.overrides.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/torch.overrides.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/torch.overrides.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/torch.overrides.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/torch.overrides.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/torch.overrides.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/torch.overrides.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/torch.overrides.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/torch.overrides.html)
[v1.13](https://docs.pytorch.org/docs/1.13/torch.overrides.html)
[v1.12](https://docs.pytorch.org/docs/1.12/torch.overrides.html)
[v1.11](https://docs.pytorch.org/docs/1.11/torch.overrides.html)
[v1.10](https://docs.pytorch.org/docs/1.10/torch.overrides.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/torch.overrides.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/torch.overrides.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/torch.overrides.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/torch.overrides.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/torch.overrides.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/torch.overrides.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/torch.overrides.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/torch.overrides.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/torch.overrides.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/torch.overrides.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/torch.overrides.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/torch.overrides.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/torch.overrides.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/torch.overrides.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/torch.overrides.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/torch.overrides.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/torch.overrides.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/torch.overrides.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/torch.overrides.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/torch.overrides.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/torch.overrides.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/torch.overrides.html)

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

torch.overrides[#](https://docs.pytorch.org/docs/2.15/torch.overrides.html#module-torch.overrides "Link to this heading")

==========================================================================================================================

Created On: Nov 30, 2020 | Last Updated On: May 10, 2026

This module exposes various helper functions for the `__torch_function__` protocol. See [Extending torch Python API](https://docs.pytorch.org/docs/2.15/notes/extending.html#extending-torch-python)
 for more details on the `__torch_function__` protocol.

Functions[#](https://docs.pytorch.org/docs/2.15/torch.overrides.html#functions "Link to this heading")

-------------------------------------------------------------------------------------------------------

torch.overrides.get\_ignored\_functions()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/overrides.py#L103)
[#](https://docs.pytorch.org/docs/2.15/torch.overrides.html#torch.overrides.get_ignored_functions "Link to this definition")

Return public functions that cannot be overridden by `__torch_function__`.

Returns:

A tuple of functions that are publicly available in the torch API but cannot be overridden with `__torch_function__`. Mostly this is because none of the arguments of these functions are tensors or tensor-likes.

Return type:

[set](https://docs.python.org/3/builtins/stdtypes.html#set "(in Python v3.15)")
\[Callable\]

Examples

\>>> torch.Tensor.as\_subclass in torch.overrides.get\_ignored\_functions()
True
\>>> torch.add in torch.overrides.get\_ignored\_functions()
False

Copy to clipboard

torch.overrides.get\_overridable\_functions()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/overrides.py#L2047)
[#](https://docs.pytorch.org/docs/2.15/torch.overrides.html#torch.overrides.get_overridable_functions "Link to this definition")

List functions that are overridable via \_\_torch\_function\_\_

Returns:

A dictionary that maps namespaces that contain overridable functions to functions in that namespace that can be overridden.

Return type:

Dict\[Any, List\[Callable\]\]

torch.overrides.resolve\_name(_f_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/overrides.py#L2060)
[#](https://docs.pytorch.org/docs/2.15/torch.overrides.html#torch.overrides.resolve_name "Link to this definition")

Get a human readable string name for a function passed to \_\_torch\_function\_\_

Parameters:

**f** (_Callable_) – Function to resolve the name of.

Returns:

Name of the function; if eval’ed it should give back the input function.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

torch.overrides.get\_testing\_overrides()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/overrides.py#L426)
[#](https://docs.pytorch.org/docs/2.15/torch.overrides.html#torch.overrides.get_testing_overrides "Link to this definition")

Return a dict containing dummy overrides for all overridable functions

Returns:

A dictionary that maps overridable functions in the PyTorch API to lambda functions that have the same signature as the real function and unconditionally return -1. These lambda functions are useful for testing API coverage for a type that defines `__torch_function__`.

Return type:

Dict\[Callable, Callable\]

Examples

\>>> import inspect
\>>> my\_add \= torch.overrides.get\_testing\_overrides()\[torch.add\]
\>>> inspect.signature(my\_add)
<Signature (input, other, out=None)>

Copy to clipboard

torch.overrides.handle\_torch\_function(_public\_api_, _relevant\_args_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/overrides.py#L1823)
[#](https://docs.pytorch.org/docs/2.15/torch.overrides.html#torch.overrides.handle_torch_function "Link to this definition")

Implement a function with checks for `__torch_function__` overrides.

See torch::autograd::handle\_torch\_function for the equivalent of this function in the C++ implementation.

Parameters:

*   **public\_api** (_function_) – Function exposed by the public torch API originally called like `public_api(*args, **kwargs)` on which arguments are now being checked.
    
*   **relevant\_args** (_iterable_) – Iterable of arguments to check for \_\_torch\_function\_\_ methods.
    
*   **args** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    ) – Arbitrary positional arguments originally passed into `public_api`.
    
*   **kwargs** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    ) – Arbitrary keyword arguments originally passed into `public_api`.
    

Returns:

Result from calling `implementation` or an `__torch_function__` method, as appropriate.

Return type:

[object](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")

:raises TypeError : if no implementation is found.:

Example

\>>> def func(a):
...     if has\_torch\_function\_unary(a):
...         return handle\_torch\_function(func, (a,), a)
...     return a + 0

Copy to clipboard

torch.overrides.has\_torch\_function()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/overrides.py#L1912)
[#](https://docs.pytorch.org/docs/2.15/torch.overrides.html#torch.overrides.has_torch_function "Link to this definition")

Check for \_\_torch\_function\_\_ implementations in the elements of an iterable or if a \_\_torch\_function\_\_ mode is enabled. Considers exact `Tensor` s and `Parameter` s non-dispatchable. Use this to guard a call to [`handle_torch_function()`](https://docs.pytorch.org/docs/2.15/torch.overrides.html#torch.overrides.handle_torch_function "torch.overrides.handle_torch_function")
; don’t use it to test if something is Tensor-like, use [`is_tensor_like()`](https://docs.pytorch.org/docs/2.15/torch.overrides.html#torch.overrides.is_tensor_like "torch.overrides.is_tensor_like")
 instead. :param relevant\_args: Iterable of arguments to check for \_\_torch\_function\_\_ methods. :type relevant\_args: iterable

Returns:

True if any of the elements of relevant\_args have \_\_torch\_function\_\_ implementations, False otherwise.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

See also

`torch.is_tensor_like`

Checks if something is a Tensor-like, including an exact `Tensor`.

torch.overrides.is\_tensor\_like(_inp_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/overrides.py#L2115)
[#](https://docs.pytorch.org/docs/2.15/torch.overrides.html#torch.overrides.is_tensor_like "Link to this definition")

Returns `True` if the passed-in input is a Tensor-like.

Currently, this occurs whenever there’s a `__torch_function__` attribute on the type of the input.

Examples

A subclass of tensor is generally a Tensor-like.

\>>> class SubTensor(torch.Tensor): ...
\>>> is\_tensor\_like(SubTensor(\[0\]))
True

Copy to clipboard

Built-in or user types aren’t usually Tensor-like.

\>>> is\_tensor\_like(6)
False
\>>> is\_tensor\_like(None)
False
\>>> class NotATensor: ...
\>>> is\_tensor\_like(NotATensor())
False

Copy to clipboard

But, they can be made Tensor-like by implementing \_\_torch\_function\_\_.

\>>> class TensorLike:
...     @classmethod
...     def \_\_torch\_function\_\_(cls, func, types, args, kwargs):
...         return \-1
\>>> is\_tensor\_like(TensorLike())
True

Copy to clipboard

torch.overrides.is\_tensor\_method\_or\_property(_func_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/overrides.py#L2089)
[#](https://docs.pytorch.org/docs/2.15/torch.overrides.html#torch.overrides.is_tensor_method_or_property "Link to this definition")

Returns True if the function passed in is a handler for a method or property belonging to `torch.Tensor`, as passed into `__torch_function__`.

Note

For properties, their `__get__` method must be passed in.

This may be needed, in particular, for the following reasons:

1.  Methods/properties sometimes don’t contain a \_\_module\_\_ slot.
    
2.  They require that the first passed-in argument is an instance of `torch.Tensor`.
    

Examples

\>>> is\_tensor\_method\_or\_property(torch.Tensor.add)
True
\>>> is\_tensor\_method\_or\_property(torch.add)
False

Copy to clipboard

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.overrides.wrap\_torch\_function(_dispatcher_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/overrides.py#L1702)
[#](https://docs.pytorch.org/docs/2.15/torch.overrides.html#torch.overrides.wrap_torch_function "Link to this definition")

Wraps a given function with `__torch_function__` -related functionality.

Parameters:

**dispatcher** (_Callable_) – A callable that returns an iterable of Tensor-likes passed into the function.

Return type:

[_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[[_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")\
\[\[~\_P\], _\_R_\]\], [_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")\
\[\[~\_P\], _\_R_\]\]

Note

This decorator may reduce the performance of your code. Generally, it’s enough to express your code as a series of functions that, themselves, support \_\_torch\_function\_\_. If you find yourself in the rare situation where this is not the case, e.g. if you’re wrapping a low-level library and you also need it to work for Tensor-likes, then this function is available.

Examples

\>>> def dispatcher(a):  \# Must have the same signature as func
...     return (a,)
\>>> @torch.overrides.wrap\_torch\_function(dispatcher)
\>>> def func(a):  \# This will make func dispatchable by \_\_torch\_function\_\_
...     return a + 0

Copy to clipboard

torch.overrides.redispatch\_function(_func_, _types_, _args_, _kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/overrides.py#L2270)
[#](https://docs.pytorch.org/docs/2.15/torch.overrides.html#torch.overrides.redispatch_function "Link to this definition")

Skip one level of `__torch_function__` dispatch and call the function.

This is primarily useful for **Tensor subclasses** that want to call into a function’s implementation while still intercepting PyTorch operations inside that function.

Example with Tensor subclass. Only ops whose inputs include a `LoggingTensor` are intercepted; once `redispatch_function` returns a plain `torch.Tensor`, subsequent ops (here `+ 1`) are not logged.

\>>> from torch.overrides import has\_torch\_function, handle\_torch\_function
\>>> class LoggingTensor(torch.Tensor):
...     depth \= 0
...
...     @classmethod
...     def \_\_torch\_function\_\_(cls, func, types, args, kwargs\=None):
...         print(f"{'  ' \* cls.depth}Calling {func.\_\_name\_\_}")
...         cls.depth += 1
...         r \= torch.overrides.redispatch\_function(func, types, args, kwargs)
...         cls.depth \-= 1
...         return r
\>>> def scaled\_mul(a, b):
...     if has\_torch\_function((a, b)):
...         return handle\_torch\_function(scaled\_mul, (a, b), a, b)
...     return a \* b + 1
\>>> x \= LoggingTensor(torch.tensor(\[3.0\]))
\>>> y \= LoggingTensor(torch.tensor(\[4.0\]))
\>>> result \= scaled\_mul(x, y)
Calling scaled\_mul
  Calling mul
\>>> result
tensor(\[13.\])

Copy to clipboard

Note that only `mul` is logged, not `add`: `redispatch_function` returns a plain `torch.Tensor`, so the `+ 1` inside `scaled_mul` no longer sees a `LoggingTensor` input and `__torch_function__` is not triggered.

With `TorchFunctionMode` the mode stays active across all inner ops, so the `+ 1` is now visible too. Use `with self:` after `redispatch_function` to re-enable the mode for those inner calls.

\>>> from torch.overrides import TorchFunctionMode
\>>> class LoggingMode(TorchFunctionMode):
...     def \_\_init\_\_(self):
...         self.depth \= 0
...
...     def \_\_torch\_function\_\_(self, func, types, args, kwargs\=None):
...         print(f"{'  ' \* self.depth}Calling {func.\_\_name\_\_}")
...         self.depth += 1
...         with self:
...             r \= torch.overrides.redispatch\_function(
...                 func, types, args, kwargs
...             )
...         self.depth \-= 1
...         return r
\>>> a \= torch.tensor(\[3.0\])
\>>> b \= torch.tensor(\[4.0\])
\>>> with LoggingMode():
...     result \= scaled\_mul(a, b)
Calling scaled\_mul
  Calling mul
  Calling add
\>>> result
tensor(\[13.\])

Copy to clipboard

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/torch.overrides.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/torch.overrides.md.txt)

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