Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.vmap.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.vmap.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.vmap.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.vmap.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.vmap.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.vmap.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.vmap.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.vmap.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.vmap.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.vmap.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.vmap.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.vmap.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.vmap.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.vmap.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.vmap.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.vmap.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.vmap.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.vmap.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.vmap.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.vmap.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.vmap.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.vmap.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.vmap.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.vmap.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.vmap.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.vmap.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.vmap.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.vmap.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.vmap.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.vmap.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.vmap.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.vmap.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.vmap.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.vmap.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.vmap.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.vmap.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.vmap.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.vmap.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.vmap.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.vmap.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.vmap.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.vmap.html)

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

torch.vmap[#](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch-vmap "Link to this heading")

==============================================================================================================

torch.vmap(_func_, _in\_dims\=0_, _out\_dims\=0_, _randomness\='error'_, _\*_, _chunk\_size\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/_functorch/apis.py#L67)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "Link to this definition")

vmap is the vectorizing map; `vmap(func)` returns a new function that maps `func` over some dimension of the inputs. Semantically, vmap pushes the map into PyTorch operations called by `func`, effectively vectorizing those operations.

vmap is useful for handling batch dimensions: one can write a function `func` that runs on examples and then lift it to a function that can take batches of examples with `vmap(func)`. vmap can also be used to compute batched gradients when composed with autograd.

Note

[`torch.vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
 is aliased to [`torch.func.vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.func.vmap.html#torch.func.vmap "torch.func.vmap")
 for convenience. Use whichever one you’d like.

Parameters:

*   **func** (_function_) – A Python function that takes one or more arguments. Must return one or more Tensors.
    
*   **in\_dims** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ _nested structure_) – Specifies which dimension of the inputs should be mapped over. `in_dims` should have a structure like the inputs. If the `in_dim` for a particular input is None, then that indicates there is no map dimension. Default: 0.
    
*   **out\_dims** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _or_ _Tuple__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – Specifies where the mapped dimension should appear in the outputs. If `out_dims` is a Tuple, then it should have one element per output. Default: 0.
    
*   **randomness** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Specifies whether the randomness in this vmap should be the same or different across batches. If ‘different’, the randomness for each batch will be different. If ‘same’, the randomness will be the same across batches. If ‘error’, any calls to random functions will error. Default: ‘error’. WARNING: this flag only applies to random PyTorch operations and does not apply to Python’s random module or numpy randomness.
    
*   **chunk\_size** (_None_ _or_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – If None (default), apply a single vmap over inputs. If not None, then compute the vmap `chunk_size` samples at a time. Note that `chunk_size=1` is equivalent to computing the vmap with a for-loop. If you run into memory issues computing the vmap, please try a non-None chunk\_size.
    

Returns:

Returns a new “batched” function. It takes the same inputs as `func`, except each input has an extra dimension at the index specified by `in_dims`. It takes returns the same outputs as `func`, except each output has an extra dimension at the index specified by `out_dims`.

Return type:

[_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
\[\[~\_P\], _\_R_\]

One example of using [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
 is to compute batched dot products. PyTorch doesn’t provide a batched `torch.dot` API; instead of unsuccessfully rummaging through docs, use [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
 to construct a new function.

\>>> torch.dot  \# \[D\], \[D\] -> \[\]
\>>> batched\_dot \= torch.func.vmap(torch.dot)  \# \[N, D\], \[N, D\] -> \[N\]
\>>> x, y \= torch.randn(2, 5), torch.randn(2, 5)
\>>> batched\_dot(x, y)

Copy to clipboard

[`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
 can be helpful in hiding batch dimensions, leading to a simpler model authoring experience.

\>>> batch\_size, feature\_size \= 3, 5
\>>> weights \= torch.randn(feature\_size, requires\_grad\=True)
\>>>
\>>> def model(feature\_vec):
\>>> \# Very simple linear model with activation
\>>>     return feature\_vec.dot(weights).relu()
\>>>
\>>> examples \= torch.randn(batch\_size, feature\_size)
\>>> result \= torch.vmap(model)(examples)

Copy to clipboard

[`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
 can also help vectorize computations that were previously difficult or impossible to batch. One example is higher-order gradient computation. The PyTorch autograd engine computes vjps (vector-Jacobian products). Computing a full Jacobian matrix for some function f: R^N -> R^N usually requires N calls to `autograd.grad`, one per Jacobian row. Using [`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
, we can vectorize the whole computation, computing the Jacobian in a single call to `autograd.grad`.

\>>> \# Setup
\>>> N \= 5
\>>> f \= lambda x: x\*\*2
\>>> x \= torch.randn(N, requires\_grad\=True)
\>>> y \= f(x)
\>>> I\_N \= torch.eye(N)
\>>>
\>>> \# Sequential approach
\>>> jacobian\_rows \= \[torch.autograd.grad(y, x, v, retain\_graph\=True)\[0\]\
\>>>                  for v in I\_N.unbind()\]
\>>> jacobian \= torch.stack(jacobian\_rows)
\>>>
\>>> \# vectorized gradient computation
\>>> def get\_vjp(v):
\>>>     return torch.autograd.grad(y, x, v)
\>>> jacobian \= torch.vmap(get\_vjp)(I\_N)

Copy to clipboard

[`vmap()`](https://docs.pytorch.org/docs/2.15/generated/torch.vmap.html#torch.vmap "torch.vmap")
 can also be nested, producing an output with multiple batched dimensions

\>>> torch.dot  \# \[D\], \[D\] -> \[\]
\>>> batched\_dot \= torch.vmap(
...     torch.vmap(torch.dot)
... )  \# \[N1, N0, D\], \[N1, N0, D\] -> \[N1, N0\]
\>>> x, y \= torch.randn(2, 3, 5), torch.randn(2, 3, 5)
\>>> batched\_dot(x, y)  \# tensor of size \[2, 3\]

Copy to clipboard

If the inputs are not batched along the first dimension, `in_dims` specifies the dimension that each input is batched along as

\>>> torch.dot  \# \[N\], \[N\] -> \[\]
\>>> batched\_dot \= torch.vmap(torch.dot, in\_dims\=1)  \# \[N, D\], \[N, D\] -> \[D\]
\>>> x, y \= torch.randn(2, 5), torch.randn(2, 5)
\>>> batched\_dot(
...     x, y
... )  \# output is \[5\] instead of \[2\] if batched along the 0th dimension

Copy to clipboard

If there are multiple inputs each of which is batched along different dimensions, `in_dims` must be a tuple with the batch dimension for each input as

\>>> torch.dot  \# \[D\], \[D\] -> \[\]
\>>> batched\_dot \= torch.vmap(torch.dot, in\_dims\=(0, None))  \# \[N, D\], \[D\] -> \[N\]
\>>> x, y \= torch.randn(2, 5), torch.randn(5)
\>>> batched\_dot(
...     x, y
... )  \# second arg doesn't have a batch dim because in\_dim\[1\] was None

Copy to clipboard

If the input is a Python struct, `in_dims` must be a tuple containing a struct matching the shape of the input:

\>>> f \= lambda dict: torch.dot(dict\["x"\], dict\["y"\])
\>>> x, y \= torch.randn(2, 5), torch.randn(5)
\>>> input \= {"x": x, "y": y}
\>>> batched\_dot \= torch.vmap(f, in\_dims\=({"x": 0, "y": None},))
\>>> batched\_dot(input)

Copy to clipboard

By default, the output is batched along the first dimension. However, it can be batched along any dimension by using `out_dims`

\>>> f \= lambda x: x\*\*2
\>>> x \= torch.randn(2, 5)
\>>> batched\_pow \= torch.vmap(f, out\_dims\=1)
\>>> batched\_pow(x)  \# \[5, 2\]

Copy to clipboard

For any function that uses kwargs, the returned function will not batch the kwargs but will accept kwargs

\>>> x \= torch.randn(\[2, 5\])
\>>> def fn(x, scale\=4.):
\>>>   return x \* scale
\>>>
\>>> batched\_pow \= torch.vmap(fn)
\>>> assert torch.allclose(batched\_pow(x), x \* 4)
\>>> batched\_pow(x, scale\=x)  \# scale is not batched, output has shape \[2, 2, 5\]

Copy to clipboard

Note

vmap does not provide general autobatching or handle variable-length sequences out of the box.

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.vmap.rst.txt)

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