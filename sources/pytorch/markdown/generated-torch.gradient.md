Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.gradient.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.gradient.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.gradient.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.gradient.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.gradient.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.gradient.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.gradient.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.gradient.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.gradient.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.gradient.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.gradient.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.gradient.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.gradient.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.gradient.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.gradient.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.gradient.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.gradient.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.gradient.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.gradient.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.gradient.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.gradient.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.gradient.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.gradient.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.gradient.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.gradient.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.gradient.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.gradient.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.gradient.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.gradient.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.gradient.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.gradient.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.gradient.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.gradient.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.gradient.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.gradient.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.gradient.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.gradient.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.gradient.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.gradient.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.gradient.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.gradient.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.gradient.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.gradient.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.gradient.html)

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

torch.gradient[#](https://docs.pytorch.org/docs/2.15/generated/torch.gradient.html#torch-gradient "Link to this heading")

==========================================================================================================================

torch.gradient(_input_, _\*_, _spacing\=1_, _dim\=None_, _edge\_order\=1_) → List of Tensors[#](https://docs.pytorch.org/docs/2.15/generated/torch.gradient.html#torch.gradient "Link to this definition")

Estimates the gradient of a function g:Rn→Rg : \\mathbb{R}^n \\rightarrow \\mathbb{R}g:Rn→R in one or more dimensions using the [second-order accurate central differences method](https://www.ams.org/journals/mcom/1988-51-184/S0025-5718-1988-0935077-0/S0025-5718-1988-0935077-0.pdf)
 and either first or second order estimates at the boundaries.

The gradient of ggg is estimated using samples. By default, when `spacing` is not specified, the samples are entirely described by `input`, and the mapping of input coordinates to an output is the same as the tensor’s mapping of indices to values. For example, for a three-dimensional `input` the function described is g:R3→Rg : \\mathbb{R}^3 \\rightarrow \\mathbb{R}g:R3→R, and g(1,2,3) \=\=input\[1,2,3\]g(1, 2, 3)\\ == input\[1, 2, 3\]g(1,2,3) \==input\[1,2,3\].

When `spacing` is specified, it modifies the relationship between `input` and input coordinates. This is detailed in the “Keyword Arguments” section below.

The gradient is estimated by estimating each partial derivative of ggg independently. This estimation is accurate if ggg is in C3C^3C3 (it has at least 3 continuous derivatives), and the estimation can be improved by providing closer samples. Mathematically, the value at each interior point of a partial derivative is estimated using [Taylor’s theorem with remainder](https://en.wikipedia.org/wiki/Taylor%27s_theorem)
. Letting xxx be an interior point with x−hlx-h\_lx−hl​ and x+hrx+h\_rx+hr​ be points neighboring it to the left and right respectively, f(x+hr)f(x+h\_r)f(x+hr​) and f(x−hl)f(x-h\_l)f(x−hl​) can be estimated using:

f(x+hr)\=f(x)+hrf′(x)+hr2f′′(x)2+hr3f′′′(ξ1)6,ξ1∈(x,x+hr)f(x−hl)\=f(x)−hlf′(x)+hl2f′′(x)2−hl3f′′′(ξ2)6,ξ2∈(x,x−hl)\\begin{aligned} f(x+h\_r) = f(x) + h\_r f'(x) + {h\_r}^2 \\frac{f''(x)}{2} + {h\_r}^3 \\frac{f'''(\\xi\_1)}{6}, \\xi\_1 \\in (x, x+h\_r) \\\\ f(x-h\_l) = f(x) - h\_l f'(x) + {h\_l}^2 \\frac{f''(x)}{2} - {h\_l}^3 \\frac{f'''(\\xi\_2)}{6}, \\xi\_2 \\in (x, x-h\_l) \\\\ \\end{aligned} f(x+hr​)\=f(x)+hr​f′(x)+hr​22f′′(x)​+hr​36f′′′(ξ1​)​,ξ1​∈(x,x+hr​)f(x−hl​)\=f(x)−hl​f′(x)+hl​22f′′(x)​−hl​36f′′′(ξ2​)​,ξ2​∈(x,x−hl​)​

Using the fact that f∈C3f \\in C^3f∈C3 and solving the linear system, we derive:

f′(x)≈hl2f(x+hr)−hr2f(x−hl)+(hr2−hl2)f(x)hrhl2+hr2hlf'(x) \\approx \\frac{ {h\_l}^2 f(x+h\_r) - {h\_r}^2 f(x-h\_l) + ({h\_r}^2-{h\_l}^2 ) f(x) }{ {h\_r} {h\_l}^2 + {h\_r}^2 {h\_l} } f′(x)≈hr​hl​2+hr​2hl​hl​2f(x+hr​)−hr​2f(x−hl​)+(hr​2−hl​2)f(x)​

Note

We estimate the gradient of functions in complex domain g:Cn→Cg : \\mathbb{C}^n \\rightarrow \\mathbb{C}g:Cn→C in the same way.

The value of each partial derivative at the boundary points is computed differently. See edge\_order below.

Parameters:

**input** (`Tensor`) – the tensor that represents the values of the function

Keyword Arguments:

*   **spacing** (`scalar`, `list of scalar`, `list of Tensor`, optional) – `spacing` can be used to modify how the `input` tensor’s indices relate to sample coordinates. If `spacing` is a scalar then the indices are multiplied by the scalar to produce the coordinates. For example, if `spacing=2` the indices (1, 2, 3) become coordinates (2, 4, 6). If `spacing` is a list of scalars then the corresponding indices are multiplied. For example, if `spacing=(2, -1, 3)` the indices (1, 2, 3) become coordinates (2, -2, 9). Finally, if `spacing` is a list of one-dimensional tensors then each tensor specifies the coordinates for the corresponding dimension. For example, if the indices are (1, 2, 3) and the tensors are (t0, t1, t2), then the coordinates are (t0\[1\], t1\[2\], t2\[3\])
    
*   **dim** (`int`, `list of int`, optional) – the dimension or dimensions to approximate the gradient over. By default the partial gradient in every dimension is computed. Note that when `dim` is specified the elements of the `spacing` argument must correspond with the specified dims.”
    
*   **edge\_order** (`int`, optional) – 1 or 2, for [first-order](https://www.ams.org/journals/mcom/1988-51-184/S0025-5718-1988-0935077-0/S0025-5718-1988-0935077-0.pdf)
     or [second-order](https://www.ams.org/journals/mcom/1988-51-184/S0025-5718-1988-0935077-0/S0025-5718-1988-0935077-0.pdf)
     estimation of the boundary (“edge”) values, respectively. Note that when `edge_order` is specified, each dimension size of `input` should be at least edge\_order+1
    

Examples:

\>>> \# Estimates the gradient of f(x)=x^2 at points \[-2, -1, 2, 4\]
\>>> coordinates \= (torch.tensor(\[\-2., \-1., 1., 4.\]),)
\>>> values \= torch.tensor(\[4., 1., 1., 16.\], )
\>>> torch.gradient(values, spacing \= coordinates)
(tensor(\[-3., -2., 2., 5.\]),)

\>>> \# Estimates the gradient of the R^2 -> R function whose samples are
\>>> \# described by the tensor t. Implicit coordinates are \[0, 1\] for the outermost
\>>> \# dimension and \[0, 1, 2, 3\] for the innermost dimension, and function estimates
\>>> \# partial derivative for both dimensions.
\>>> t \= torch.tensor(\[\[1, 2, 4, 8\], \[10, 20, 40, 80\]\])
\>>> torch.gradient(t)
(tensor(\[\[ 9., 18., 36., 72.\],\
         \[ 9., 18., 36., 72.\]\]),
 tensor(\[\[ 1.0000, 1.5000, 3.0000, 4.0000\],\
         \[10.0000, 15.0000, 30.0000, 40.0000\]\]))

\>>> \# A scalar value for spacing modifies the relationship between tensor indices
\>>> \# and input coordinates by multiplying the indices to find the
\>>> \# coordinates. For example, below the indices of the innermost
\>>> \# 0, 1, 2, 3 translate to coordinates of \[0, 2, 4, 6\], and the indices of
\>>> \# the outermost dimension 0, 1 translate to coordinates of \[0, 2\].
\>>> torch.gradient(t, spacing \= 2.0) \# dim = None (implicitly \[0, 1\])
(tensor(\[\[ 4.5000, 9.0000, 18.0000, 36.0000\],\
          \[ 4.5000, 9.0000, 18.0000, 36.0000\]\]),
 tensor(\[\[ 0.5000, 0.7500, 1.5000, 2.0000\],\
          \[ 5.0000, 7.5000, 15.0000, 20.0000\]\]))
\>>> \# doubling the spacing between samples halves the estimated partial gradients.

\>>>
\>>> \# Estimates only the partial derivative for dimension 1
\>>> torch.gradient(t, dim \= 1) \# spacing = None (implicitly 1.)
(tensor(\[\[ 1.0000, 1.5000, 3.0000, 4.0000\],\
         \[10.0000, 15.0000, 30.0000, 40.0000\]\]),)

\>>> \# When spacing is a list of scalars, the relationship between the tensor
\>>> \# indices and input coordinates changes based on dimension.
\>>> \# For example, below, the indices of the innermost dimension 0, 1, 2, 3 translate
\>>> \# to coordinates of \[0, 3, 6, 9\], and the indices of the outermost dimension
\>>> \# 0, 1 translate to coordinates of \[0, 2\].
\>>> torch.gradient(t, spacing \= \[3., 2.\])
(tensor(\[\[ 4.5000, 9.0000, 18.0000, 36.0000\],\
         \[ 4.5000, 9.0000, 18.0000, 36.0000\]\]),
 tensor(\[\[ 0.3333, 0.5000, 1.0000, 1.3333\],\
         \[ 3.3333, 5.0000, 10.0000, 13.3333\]\]))

\>>> \# The following example is a replication of the previous one with explicit
\>>> \# coordinates.
\>>> coords \= (torch.tensor(\[0, 2\]), torch.tensor(\[0, 3, 6, 9\]))
\>>> torch.gradient(t, spacing \= coords)
(tensor(\[\[ 4.5000, 9.0000, 18.0000, 36.0000\],\
         \[ 4.5000, 9.0000, 18.0000, 36.0000\]\]),
 tensor(\[\[ 0.3333, 0.5000, 1.0000, 1.3333\],\
         \[ 3.3333, 5.0000, 10.0000, 13.3333\]\]))

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.gradient.rst.txt)

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