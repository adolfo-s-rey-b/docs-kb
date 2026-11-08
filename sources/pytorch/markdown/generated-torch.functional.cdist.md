Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.functional.cdist.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.functional.cdist.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.functional.cdist.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.functional.cdist.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.functional.cdist.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.functional.cdist.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.functional.cdist.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.functional.cdist.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.functional.cdist.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.functional.cdist.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.functional.cdist.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.functional.cdist.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.functional.cdist.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.functional.cdist.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.functional.cdist.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.functional.cdist.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.functional.cdist.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.functional.cdist.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.functional.cdist.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.functional.cdist.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.functional.cdist.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.functional.cdist.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.functional.cdist.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.functional.cdist.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.functional.cdist.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.functional.cdist.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.functional.cdist.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.functional.cdist.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.functional.cdist.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.functional.cdist.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.functional.cdist.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.functional.cdist.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.functional.cdist.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.functional.cdist.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.functional.cdist.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.functional.cdist.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.functional.cdist.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.functional.cdist.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.functional.cdist.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.functional.cdist.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.functional.cdist.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.functional.cdist.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.functional.cdist.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.functional.cdist.html)

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

torch.functional.cdist[#](https://docs.pytorch.org/docs/2.15/generated/torch.functional.cdist.html#torch-functional-cdist "Link to this heading")

==================================================================================================================================================

torch.functional.cdist(_x1_, _x2_, _p\=2.0_, _compute\_mode\='use\_mm\_for\_euclid\_dist\_if\_necessary'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/functional.py#L1483)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.functional.cdist.html#torch.functional.cdist "Link to this definition")

Computes the batched p-norm distance between each pair of the two collections of row vectors.

Parameters:

*   **x1** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – input tensor where the last two dimensions represent the points and the feature dimension respectively. The shape can be D1×D2×⋯×Dn×P×MD\_1 \\times D\_2 \\times \\cdots \\times D\_n \\times P \\times MD1​×D2​×⋯×Dn​×P×M, where PPP is the number of points and MMM is the feature dimension.
    
*   **x2** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – input tensor where the last two dimensions also represent the points and the feature dimension respectively. The shape can be D1′×D2′×⋯×Dm′×R×MD\_1' \\times D\_2' \\times \\cdots \\times D\_m' \\times R \\times MD1′​×D2′​×⋯×Dm′​×R×M, where RRR is the number of points and MMM is the feature dimension, which should match the feature dimension of x1.
    
*   **p** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – p value for the p-norm distance to calculate between each vector pair ∈\[0,∞\]\\in \[0, \\infty\]∈\[0,∞\].
    
*   **compute\_mode** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – ‘use\_mm\_for\_euclid\_dist\_if\_necessary’ - will use matrix multiplication approach to calculate euclidean distance (p = 2) if P > 25 or R > 25 ‘use\_mm\_for\_euclid\_dist’ - will always use matrix multiplication approach to calculate euclidean distance (p = 2) ‘donot\_use\_mm\_for\_euclid\_dist’ - will never use matrix multiplication approach to calculate euclidean distance (p = 2) Default: use\_mm\_for\_euclid\_dist\_if\_necessary.
    

Return type:

[_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

If x1 has shape B×P×MB \\times P \\times MB×P×M and x2 has shape B×R×MB \\times R \\times MB×R×M then the output will have shape B×P×RB \\times P \\times RB×P×R.

This function is equivalent to scipy.spatial.distance.cdist(input,’minkowski’, p=p) if p∈(0,∞)p \\in (0, \\infty)p∈(0,∞). When p\=0p = 0p\=0 it is equivalent to scipy.spatial.distance.cdist(input, ‘hamming’) \* M. When p\=∞p = \\inftyp\=∞, the closest scipy function is scipy.spatial.distance.cdist(xn, lambda x, y: np.abs(x - y).max()).

Example

\>>> a \= torch.tensor(\[\[0.9041, 0.0196\], \[\-0.3108, \-2.4423\], \[\-0.4821, 1.059\]\])
\>>> a
tensor(\[\[ 0.9041,  0.0196\],\
        \[-0.3108, -2.4423\],\
        \[-0.4821,  1.0590\]\])
\>>> b \= torch.tensor(\[\[\-2.1763, \-0.4713\], \[\-0.6986, 1.3702\]\])
\>>> b
tensor(\[\[-2.1763, -0.4713\],\
        \[-0.6986,  1.3702\]\])
\>>> torch.cdist(a, b, p\=2)
tensor(\[\[3.1193, 2.0959\],\
        \[2.7138, 3.8322\],\
        \[2.2830, 0.3791\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.functional.cdist.rst.txt)

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