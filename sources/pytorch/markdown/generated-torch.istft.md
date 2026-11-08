Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.istft.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.istft.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.istft.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.istft.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.istft.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.istft.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.istft.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.istft.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.istft.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.istft.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.istft.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.istft.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.istft.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.istft.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.istft.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.istft.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.istft.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.istft.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.istft.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.istft.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.istft.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.istft.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.istft.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.istft.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.istft.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.istft.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.istft.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.istft.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.istft.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.istft.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.istft.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.istft.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.istft.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.istft.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.istft.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.istft.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.istft.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.istft.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.istft.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.istft.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.istft.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.istft.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.istft.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.istft.html)

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

torch.istft[#](https://docs.pytorch.org/docs/2.15/generated/torch.istft.html#torch-istft "Link to this heading")

=================================================================================================================

torch.istft(_input_, _n\_fft_, _hop\_length\=None_, _win\_length\=None_, _window\=None_, _center\=True_, _normalized\=False_, _onesided\=None_, _length\=None_, _return\_complex\=False_) → Tensor:[#](https://docs.pytorch.org/docs/2.15/generated/torch.istft.html#torch.istft "Link to this definition")

Inverse short time Fourier Transform. This is expected to be the inverse of [`stft()`](https://docs.pytorch.org/docs/2.15/generated/torch.stft.html#torch.stft "torch.stft")
.

Warning

From version 2.1, a warning will be provided if a `window` is not specified. In a future release, this attribute will be required. Please provide the same window used in the stft call.

It has the same parameters (+ additional optional parameter of `length`) and it should return the least squares estimation of the original signal. The algorithm will check using the NOLA condition ( nonzero overlap).

Important consideration in the parameters `window` and `center` so that the envelope created by the summation of all the windows is never zero at certain point in time. Specifically, ∑t\=−∞∞∣w∣2\[n−t×hop\_length\]\=0\\sum\_{t=-\\infty}^{\\infty} |w|^2\[n-t\\times hop\\\_length\] \\cancel{=} 0∑t\=−∞∞​∣w∣2\[n−t×hop\_length\]\=​0.

Since [`stft()`](https://docs.pytorch.org/docs/2.15/generated/torch.stft.html#torch.stft "torch.stft")
 discards elements at the end of the signal if they do not fit in a frame, `istft` may return a shorter signal than the original signal (can occur if `center` is False since the signal isn’t padded). If length is given in the arguments and is longer than expected, `istft` will pad zeros to the end of the returned signal.

If `center` is `True`, then there will be padding e.g. `'constant'`, `'reflect'`, etc. Left padding can be trimmed off exactly because they can be calculated but right padding cannot be calculated without additional information.

Example: Suppose the last window is: `[17, 18, 0, 0, 0]` vs `[18, 0, 0, 0, 0]`

The `n_fft`, `hop_length`, `win_length` are all the same which prevents the calculation of right padding. These additional values could be zeros or a reflection of the signal so providing `length` could be useful. If `length` is `None` then padding will be aggressively removed (some loss of signal).

\[1\] D. W. Griffin and J. S. Lim, “Signal estimation from modified short-time Fourier transform,” IEEE Trans. ASSP, vol.32, no.2, pp.236-243, Apr. 1984.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) –
    
    The input tensor. Expected to be in the format of [`stft()`](https://docs.pytorch.org/docs/2.15/generated/torch.stft.html#torch.stft "torch.stft")
    , output. That is a complex tensor of shape (B?, N, T) where
    
    *   B? is an optional batch dimension
        
    *   N is the number of frequency samples, (n\_fft // 2) + 1 for onesided input, or otherwise n\_fft.
        
    *   T is the number of frames, 1 + length // hop\_length for centered stft, or 1 + (length - n\_fft) // hop\_length otherwise.
        
    
    Changed in version 2.0: Real datatype inputs are no longer supported. Input must now have a complex datatype, as returned by `stft(..., return_complex=True)`.
    
*   **n\_fft** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Size of Fourier transform
    
*   **hop\_length** (_Optional__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – The distance between neighboring sliding window frames. (Default: `n_fft // 4`)
    
*   **win\_length** (_Optional__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – The size of window frame and STFT filter. (Default: `n_fft`)
    
*   **window** (_Optional__\[_[_torch.Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")\
    _\]_) – The optional window function. Shape must be 1d and <= n\_fft (Default: `torch.ones(win_length)`)
    
*   **center** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether `input` was padded on both sides so that the ttt\-th frame is centered at time t×hop\_lengtht \\times \\text{hop\\\_length}t×hop\_length. (Default: `True`)
    
*   **normalized** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Whether the STFT was normalized. (Default: `False`)
    
*   **onesided** (_Optional__\[_[_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _\]_) – Whether the STFT was onesided. (Default: `True` if n\_fft != fft\_size in the input size)
    
*   **length** (_Optional__\[_[_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – The amount to trim the signal by (i.e. the original signal length). Defaults to (T - 1) \* hop\_length for centered stft, or n\_fft + (T - 1) \* hop\_length otherwise, where T is the number of input frames.
    
*   **return\_complex** (_Optional__\[_[_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _\]_) – Whether the output should be complex, or if the input should be assumed to derive from a real signal and window. Note that this is incompatible with `onesided=True`. (Default: `False`)
    

Returns:

Least squares estimation of the original signal of shape (B?, length) where

B? is an optional batch dimension from the input tensor.

Return type:

[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.istft.rst.txt)

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