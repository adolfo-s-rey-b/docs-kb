Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.functional.meshgrid.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.functional.meshgrid.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.functional.meshgrid.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.functional.meshgrid.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.functional.meshgrid.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.functional.meshgrid.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.functional.meshgrid.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.functional.meshgrid.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.functional.meshgrid.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.functional.meshgrid.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.functional.meshgrid.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.functional.meshgrid.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.functional.meshgrid.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.functional.meshgrid.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.functional.meshgrid.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.functional.meshgrid.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.functional.meshgrid.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.functional.meshgrid.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.functional.meshgrid.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.functional.meshgrid.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.functional.meshgrid.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.functional.meshgrid.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.functional.meshgrid.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.functional.meshgrid.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.functional.meshgrid.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.functional.meshgrid.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.functional.meshgrid.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.functional.meshgrid.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.functional.meshgrid.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.functional.meshgrid.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.functional.meshgrid.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.functional.meshgrid.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.functional.meshgrid.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.functional.meshgrid.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.functional.meshgrid.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.functional.meshgrid.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.functional.meshgrid.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.functional.meshgrid.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.functional.meshgrid.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.functional.meshgrid.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.functional.meshgrid.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.functional.meshgrid.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.functional.meshgrid.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.functional.meshgrid.html)

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

torch.functional.meshgrid[#](https://docs.pytorch.org/docs/2.15/generated/torch.functional.meshgrid.html#torch-functional-meshgrid "Link to this heading")

===========================================================================================================================================================

torch.functional.meshgrid(_\*tensors_, _indexing\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/functional.py#L395)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.functional.meshgrid.html#torch.functional.meshgrid "Link to this definition")

Creates grids of coordinates specified by the 1D inputs in attr:tensors.

This is helpful when you want to visualize data over some range of inputs. See below for a plotting example.

Given NNN 1D tensors T0…TN−1T\_0 \\ldots T\_{N-1}T0​…TN−1​ as inputs with corresponding sizes S0…SN−1S\_0 \\ldots S\_{N-1}S0​…SN−1​, this creates NNN N-dimensional tensors G0…GN−1G\_0 \\ldots G\_{N-1}G0​…GN−1​, each with shape (S0,...,SN−1)(S\_0, ..., S\_{N-1})(S0​,...,SN−1​) where the output GiG\_iGi​ is constructed by expanding TiT\_iTi​ to the result shape.

Note

0D inputs are treated equivalently to 1D inputs of a single element.

Warning

torch.meshgrid(\*tensors) currently has the same behavior as calling numpy.meshgrid(\*arrays, indexing=’ij’).

In the future torch.meshgrid will transition to indexing=’xy’ as the default.

[pytorch/pytorch#50276](https://github.com/pytorch/pytorch/issues/50276)
 tracks this issue with the goal of migrating to NumPy’s behavior.

See also

[`torch.cartesian_prod()`](https://docs.pytorch.org/docs/2.15/generated/torch.cartesian_prod.html#torch.cartesian_prod "torch.cartesian_prod")
 has the same effect but it collects the data in a tensor of vectors.

Parameters:

*   **tensors** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
     _of_ [_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – list of scalars or 1 dimensional tensors. Scalars will be treated as tensors of size (1,)(1,)(1,) automatically
    
*   **indexing** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _None_) –
    
    (str, optional): the indexing mode, either “xy” or “ij”, defaults to “ij”. See warning for future changes.
    
    If “xy” is selected, the first dimension corresponds to the cardinality of the second input and the second dimension corresponds to the cardinality of the first input.
    
    If “ij” is selected, the dimensions are in the same order as the cardinality of the inputs.
    

Returns:

If the input has NNN tensors of size S0…SN−1‘S\_0 \\ldots S\_{N-1}\`S0​…SN−1​‘, then the output will also have NNN tensors, where each tensor is of shape (S0,...,SN−1)(S\_0, ..., S\_{N-1})(S0​,...,SN−1​).

Return type:

seq (sequence of Tensors)

Example:

\>>> x \= torch.tensor(\[1, 2, 3\])
\>>> y \= torch.tensor(\[4, 5, 6\])

Observe the element-wise pairings across the grid, (1, 4),
(1, 5), ..., (3, 6). This is the same thing as the
cartesian product.
\>>> grid\_x, grid\_y \= torch.meshgrid(x, y, indexing\='ij')
\>>> grid\_x
tensor(\[\[1, 1, 1\],\
        \[2, 2, 2\],\
        \[3, 3, 3\]\])
\>>> grid\_y
tensor(\[\[4, 5, 6\],\
        \[4, 5, 6\],\
        \[4, 5, 6\]\])

This correspondence can be seen when these grids are
stacked properly.
\>>> torch.equal(torch.cat(tuple(torch.dstack(\[grid\_x, grid\_y\]))),
...             torch.cartesian\_prod(x, y))
True

\`torch.meshgrid\` is commonly used to produce a grid for
plotting.
\>>> import matplotlib.pyplot as plt
\>>> xs \= torch.linspace(\-5, 5, steps\=100)
\>>> ys \= torch.linspace(\-5, 5, steps\=100)
\>>> x, y \= torch.meshgrid(xs, ys, indexing\='xy')
\>>> z \= torch.sin(torch.sqrt(x \* x + y \* y))
\>>> ax \= plt.axes(projection\='3d')
\>>> ax.plot\_surface(x.numpy(), y.numpy(), z.numpy())
\>>> plt.show()

Copy to clipboard

[![../_images/meshgrid.png](https://docs.pytorch.org/docs/2.15/_images/meshgrid.png)](https://docs.pytorch.org/docs/2.15/_images/meshgrid.png)

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.functional.meshgrid.rst.txt)

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