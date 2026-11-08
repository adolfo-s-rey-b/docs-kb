Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.fft.irfft.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.fft.irfft.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.fft.irfft.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.fft.irfft.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.fft.irfft.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.fft.irfft.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.fft.irfft.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.fft.irfft.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.fft.irfft.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.fft.irfft.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.fft.irfft.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.fft.irfft.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.fft.irfft.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.fft.irfft.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.fft.irfft.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.fft.irfft.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.fft.irfft.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.fft.irfft.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.fft.irfft.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.fft.irfft.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.fft.irfft.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.fft.irfft.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.fft.irfft.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.fft.irfft.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.fft.irfft.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.fft.irfft.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.fft.irfft.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.fft.irfft.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.fft.irfft.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.fft.irfft.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.fft.irfft.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.fft.irfft.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.fft.irfft.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.fft.irfft.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.fft.irfft.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.fft.irfft.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.fft.irfft.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.fft.irfft.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.fft.irfft.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.fft.irfft.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.fft.irfft.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.fft.irfft.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.fft.irfft.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.fft.irfft.html)

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

torch.fft.irfft[#](https://docs.pytorch.org/docs/2.15/generated/torch.fft.irfft.html#torch-fft-irfft "Link to this heading")

=============================================================================================================================

torch.fft.irfft(_input_, _n\=None_, _dim\=\-1_, _norm\=None_, _\*_, _out\=None_) → [Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/fft/__init__.py#L411)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.fft.irfft.html#torch.fft.irfft "Link to this definition")

Computes the inverse of [`rfft()`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.rfft.html#torch.fft.rfft "torch.fft.rfft")
.

`input` is interpreted as a one-sided Hermitian signal in the Fourier domain, as produced by [`rfft()`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.rfft.html#torch.fft.rfft "torch.fft.rfft")
. By the Hermitian property, the output will be real-valued.

Note

Some input frequencies must be real-valued to satisfy the Hermitian property. In these cases the imaginary component will be ignored. For example, any imaginary component in the zero-frequency term cannot be represented in a real output and so will always be ignored.

Note

The correct interpretation of the Hermitian input depends on the length of the original data, as given by `n`. This is because each input shape could correspond to either an odd or even length signal. By default, the signal is assumed to be even length and odd signals will not round-trip properly. So, it is recommended to always pass the signal length `n`.

Note

Supports torch.half and torch.chalf on CUDA with GPU Architecture SM53 or greater. However it only supports powers of 2 signal length in every transformed dimension. With default arguments, size of the transformed dimension should be (2^n + 1) as argument n defaults to even output size = 2 \* (transformed\_dim\_size - 1)

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor representing a half-Hermitian signal
    
*   **n** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – Output signal length. This determines the length of the output signal. If given, the input will either be zero-padded or trimmed to this length before computing the real IFFT. Defaults to even output: `n=2*(input.size(dim) - 1)`.
    
*   **dim** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – The dimension along which to take the one dimensional real IFFT.
    
*   **norm** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) –
    
    Normalization mode. For the backward transform ([`irfft()`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.irfft.html#torch.fft.irfft "torch.fft.irfft")
    ), these correspond to:
    
    *   `"forward"` - no normalization
        
    *   `"backward"` - normalize by `1/n`
        
    *   `"ortho"` - normalize by `1/sqrt(n)` (making the real IFFT orthonormal)
        
    
    Calling the forward transform ([`rfft()`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.rfft.html#torch.fft.rfft "torch.fft.rfft")
    ) with the same normalization mode will apply an overall normalization of `1/n` between the two transforms. This is required to make [`irfft()`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.irfft.html#torch.fft.irfft "torch.fft.irfft")
     the exact inverse.
    
    Default is `"backward"` (normalize by `1/n`).
    

Keyword Arguments:

**out** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
_,_ _optional_) – the output tensor.

Example

\>>> t \= torch.linspace(0, 1, 5)
\>>> t
tensor(\[0.0000, 0.2500, 0.5000, 0.7500, 1.0000\])
\>>> T \= torch.fft.rfft(t)
\>>> T
tensor(\[ 2.5000+0.0000j, -0.6250+0.8602j, -0.6250+0.2031j\])

Copy to clipboard

Without specifying the output length to [`irfft()`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.irfft.html#torch.fft.irfft "torch.fft.irfft")
, the output will not round-trip properly because the input is odd-length:

\>>> torch.fft.irfft(T)
tensor(\[0.1562, 0.3511, 0.7812, 1.2114\])

Copy to clipboard

So, it is recommended to always pass the signal length `n`:

\>>> roundtrip \= torch.fft.irfft(T, t.numel())
\>>> torch.testing.assert\_close(roundtrip, t, check\_stride\=False)

Copy to clipboard

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.fft.irfft.rst.txt)

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