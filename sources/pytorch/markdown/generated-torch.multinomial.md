Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.multinomial.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.multinomial.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.multinomial.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.multinomial.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.multinomial.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.multinomial.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.multinomial.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.multinomial.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.multinomial.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.multinomial.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.multinomial.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.multinomial.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.multinomial.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.multinomial.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.multinomial.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.multinomial.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.multinomial.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.multinomial.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.multinomial.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.multinomial.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.multinomial.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.multinomial.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.multinomial.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.multinomial.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.multinomial.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.multinomial.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.multinomial.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.multinomial.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.multinomial.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.multinomial.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.multinomial.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.multinomial.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.multinomial.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.multinomial.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.multinomial.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.multinomial.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.multinomial.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.multinomial.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.multinomial.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.multinomial.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.multinomial.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.multinomial.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.multinomial.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.multinomial.html)

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

torch.multinomial[#](https://docs.pytorch.org/docs/2.15/generated/torch.multinomial.html#torch-multinomial "Link to this heading")

===================================================================================================================================

torch.multinomial(_input_, _num\_samples_, _replacement\=False_, _\*_, _generator\=None_, _out\=None_) → LongTensor[#](https://docs.pytorch.org/docs/2.15/generated/torch.multinomial.html#torch.multinomial "Link to this definition")

Returns a tensor where each row contains `num_samples` indices sampled from the multinomial (a stricter definition would be multivariate, refer to [`torch.distributions.multinomial.Multinomial`](https://docs.pytorch.org/docs/2.15/distributions.html#torch.distributions.multinomial.Multinomial "torch.distributions.multinomial.Multinomial")
 for more details) probability distribution located in the corresponding row of tensor `input`.

Note

The rows of `input` do not need to sum to one (in which case we use the values as weights), but must be non-negative, finite and have a non-zero sum.

Indices are ordered from left to right according to when each was sampled (first samples are placed in first column).

If `input` is a vector, `out` is a vector of size `num_samples`.

If `input` is a matrix with m rows, `out` is an matrix of shape (m×num\_samples)(m \\times \\text{num\\\_samples})(m×num\_samples).

If replacement is `True`, samples are drawn with replacement.

If not, they are drawn without replacement, which means that when a sample index is drawn for a row, it cannot be drawn again for that row.

Note

When drawn without replacement, `num_samples` must be lower than number of non-zero elements in `input` (or the min number of non-zero elements in each row of `input` if it is a matrix).

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor containing probabilities
    
*   **num\_samples** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – number of samples to draw
    
*   **replacement** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether to draw with replacement or not
    

Keyword Arguments:

*   **generator** ([`torch.Generator`](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch.Generator")
    , optional) – a pseudorandom number generator for sampling
    
*   **out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the output tensor.
    

Example:

\>>> weights \= torch.tensor(\[0, 10, 3, 0\], dtype\=torch.float) \# create a tensor of weights
\>>> torch.multinomial(weights, 2)
tensor(\[1, 2\])
\>>> torch.multinomial(weights, 5) \# ERROR!
RuntimeError: cannot sample n\_sample > prob\_dist.size(-1) samples without replacement
\>>> torch.multinomial(weights, 4, replacement\=True)
tensor(\[ 2,  1,  1,  1\])

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.multinomial.rst.txt)

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