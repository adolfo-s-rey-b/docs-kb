Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.div.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.div.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.div.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.div.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.div.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.div.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.div.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.div.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.div.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.div.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.div.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.div.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.div.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.div.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.div.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.div.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.div.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.div.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.div.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.div.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.div.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.div.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.div.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.div.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.div.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.div.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.div.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.div.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.div.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.div.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.div.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.div.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.div.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.div.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.div.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.div.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.div.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.div.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.div.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.div.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.div.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.div.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.div.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.div.html)

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

torch.div[#](https://docs.pytorch.org/docs/2.15/generated/torch.div.html#torch-div "Link to this heading")

===========================================================================================================

torch.div(_input_, _other_, _\*_, _rounding\_mode\=None_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[#](https://docs.pytorch.org/docs/2.15/generated/torch.div.html#torch.div "Link to this definition")

Divides each element of the input `input` by the corresponding element of `other`.

outi\=inputiotheri\\text{out}\_i = \\frac{\\text{input}\_i}{\\text{other}\_i} outi​\=otheri​inputi​​

Note

By default, this performs a “true” division like Python 3. See the `rounding_mode` argument for floor division.

Supports [broadcasting to a common shape](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html#broadcasting-semantics)
, [type promotion](https://docs.pytorch.org/docs/2.15/tensor_attributes.html#type-promotion-doc)
, and integer, float, and complex inputs. Always promotes integer types to the default scalar type.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the dividend
    
*   **other** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
     _or_ _Number_) – the divisor
    

Keyword Arguments:

*   **rounding\_mode** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) –
    
    Type of rounding applied to the result:
    
    *   None - default behavior. Performs no rounding and, if both `input` and `other` are integer types, promotes the inputs to the default scalar type. Equivalent to true division in Python (the `/` operator) and NumPy’s `np.true_divide`.
        
    *   `"trunc"` - rounds the results of the division towards zero. Equivalent to C-style integer division.
        
    *   `"floor"` - rounds the results of the division down. Equivalent to floor division in Python (the `//` operator) and NumPy’s `np.floor_divide`.
        
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the output tensor.
    

Examples:

\>>> x \= torch.tensor(\[ 0.3810,  1.2774, \-0.2972, \-0.3719,  0.4637\])
\>>> torch.div(x, 0.5)
tensor(\[ 0.7620,  2.5548, -0.5944, -0.7438,  0.9274\])

\>>> a \= torch.tensor(\[\[\-0.3711, \-1.9353, \-0.4605, \-0.2917\],\
...                   \[ 0.1815, \-1.0111,  0.9805, \-1.5923\],\
...                   \[ 0.1062,  1.4581,  0.7759, \-1.2344\],\
...                   \[\-0.1830, \-0.0313,  1.1908, \-1.4757\]\])
\>>> b \= torch.tensor(\[ 0.8032,  0.2930, \-0.8113, \-0.2308\])
\>>> torch.div(a, b)
tensor(\[\[-0.4620, -6.6051,  0.5676,  1.2639\],\
        \[ 0.2260, -3.4509, -1.2086,  6.8990\],\
        \[ 0.1322,  4.9764, -0.9564,  5.3484\],\
        \[-0.2278, -0.1068, -1.4678,  6.3938\]\])

\>>> torch.div(a, b, rounding\_mode\='trunc')
tensor(\[\[-0., -6.,  0.,  1.\],\
        \[ 0., -3., -1.,  6.\],\
        \[ 0.,  4., -0.,  5.\],\
        \[-0., -0., -1.,  6.\]\])

\>>> torch.div(a, b, rounding\_mode\='floor')
tensor(\[\[-1., -7.,  0.,  1.\],\
        \[ 0., -4., -2.,  6.\],\
        \[ 0.,  4., -1.,  5.\],\
        \[-1., -1., -2.,  6.\]\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.div.rst.txt)

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