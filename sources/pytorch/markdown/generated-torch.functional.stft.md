Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/generated/torch.functional.stft.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/generated/torch.functional.stft.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/generated/torch.functional.stft.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/generated/torch.functional.stft.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/generated/torch.functional.stft.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/generated/torch.functional.stft.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/generated/torch.functional.stft.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/generated/torch.functional.stft.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/generated/torch.functional.stft.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/generated/torch.functional.stft.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/generated/torch.functional.stft.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/generated/torch.functional.stft.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/generated/torch.functional.stft.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/generated/torch.functional.stft.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/generated/torch.functional.stft.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/generated/torch.functional.stft.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/generated/torch.functional.stft.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/generated/torch.functional.stft.html)
[v1.13](https://docs.pytorch.org/docs/1.13/generated/torch.functional.stft.html)
[v1.12](https://docs.pytorch.org/docs/1.12/generated/torch.functional.stft.html)
[v1.11](https://docs.pytorch.org/docs/1.11/generated/torch.functional.stft.html)
[v1.10](https://docs.pytorch.org/docs/1.10/generated/torch.functional.stft.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/generated/torch.functional.stft.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/generated/torch.functional.stft.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/generated/torch.functional.stft.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/generated/torch.functional.stft.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/generated/torch.functional.stft.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/generated/torch.functional.stft.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/generated/torch.functional.stft.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/generated/torch.functional.stft.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/generated/torch.functional.stft.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/generated/torch.functional.stft.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/generated/torch.functional.stft.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/generated/torch.functional.stft.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/generated/torch.functional.stft.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/generated/torch.functional.stft.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/generated/torch.functional.stft.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/generated/torch.functional.stft.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/generated/torch.functional.stft.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/generated/torch.functional.stft.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/generated/torch.functional.stft.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/generated/torch.functional.stft.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/generated/torch.functional.stft.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/generated/torch.functional.stft.html)

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

torch.functional.stft[#](https://docs.pytorch.org/docs/2.15/generated/torch.functional.stft.html#torch-functional-stft "Link to this heading")

===============================================================================================================================================

torch.functional.stft(_input_, _n\_fft_, _hop\_length\=None_, _win\_length\=None_, _window\=None_, _center\=True_, _pad\_mode\='reflect'_, _normalized\=False_, _onesided\=None_, _return\_complex\=None_, _align\_to\_window\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/functional.py#L507)
[#](https://docs.pytorch.org/docs/2.15/generated/torch.functional.stft.html#torch.functional.stft "Link to this definition")

Short-time Fourier transform (STFT).

Warning

From version 1.8.0, `return_complex` must always be given explicitly for real inputs and return\_complex=False has been deprecated. Strongly prefer return\_complex=True as in a future pytorch release, this function will only return complex tensors.

Note that [`torch.view_as_real()`](https://docs.pytorch.org/docs/2.15/generated/torch.view_as_real.html#torch.view_as_real "torch.view_as_real")
 can be used to recover a real tensor with an extra last dimension for real and imaginary components.

Warning

From version 2.1, a warning will be provided if a `window` is not specified. In a future release, this attribute will be required. Not providing a window currently defaults to using a rectangular window, which may result in undesirable artifacts. Consider using tapered windows, such as [`torch.hann_window()`](https://docs.pytorch.org/docs/2.15/generated/torch.hann_window.html#torch.hann_window "torch.hann_window")
.

The STFT computes the Fourier transform of short overlapping windows of the input. This gives frequency components of the signal as they change over time. The interface of this function is modeled after (but _not_ a drop-in replacement for) [librosa](https://librosa.org/doc/latest/generated/librosa.stft.html)
 stft function.

Ignoring the optional batch dimension, this method computes the following expression:

X\[ω,m\]\=∑k\=0win\_length-1window\[k\] input\[m×hop\_length+k\] exp⁡(−j2π⋅ωkn\_fft),X\[\\omega, m\] = \\sum\_{k = 0}^{\\text{win\\\_length-1}}% \\text{window}\[k\]\\ \\text{input}\[m \\times \\text{hop\\\_length} + k\]\\ % \\exp\\left(- j \\frac{2 \\pi \\cdot \\omega k}{\\text{n\\\_fft}}\\right), X\[ω,m\]\=k\=0∑win\_length-1​window\[k\] input\[m×hop\_length+k\] exp(−jn\_fft2π⋅ωk​),

where mmm is the index of the sliding window, and ω\\omegaω is the frequency 0≤ω<n\_fft0 \\leq \\omega < \\text{n\\\_fft}0≤ω<n\_fft for `onesided=False`, or 0≤ω<⌊n\_fft/2⌋+10 \\leq \\omega < \\lfloor \\text{n\\\_fft} / 2 \\rfloor + 10≤ω<⌊n\_fft/2⌋+1 for `onesided=True`.

*   `input` must be either a 1-D time sequence or a 2-D batch of time sequences.
    
*   If `hop_length` is `None` (default), it is treated as equal to `floor(n_fft / 4)`.
    
*   If `win_length` is `None` (default), it is treated as equal to `n_fft`.
    
*   `window` can be a 1-D tensor of size `win_length`, e.g., from [`torch.hann_window()`](https://docs.pytorch.org/docs/2.15/generated/torch.hann_window.html#torch.hann_window "torch.hann_window")
    . If `window` is `None` (default), it is treated as if having 111 everywhere in the window. If win\_length<n\_fft\\text{win\\\_length} < \\text{n\\\_fft}win\_length<n\_fft, `window` will be padded on both sides to length `n_fft` before being applied.
    
*   If `center` is `True` (default), `input` will be padded on both sides so that the ttt\-th frame is centered at time t×hop\_lengtht \\times \\text{hop\\\_length}t×hop\_length. Otherwise, the ttt\-th frame begins at time t×hop\_lengtht \\times \\text{hop\\\_length}t×hop\_length.
    
*   `pad_mode` determines the padding method used on `input` when `center` is `True`. See [`torch.nn.functional.pad()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.pad.html#torch.nn.functional.pad "torch.nn.functional.pad")
     for all available options. Default is `"reflect"`.
    
*   If `onesided` is `True` (default for real input), only values for ω\\omegaω in \[0,1,2,…,⌊n\_fft2⌋+1\]\\left\[0, 1, 2, \\dots, \\left\\lfloor \\frac{\\text{n\\\_fft}}{2} \\right\\rfloor + 1\\right\]\[0,1,2,…,⌊2n\_fft​⌋+1\] are returned because the real-to-complex Fourier transform satisfies the conjugate symmetry, i.e., X\[m,ω\]\=X\[m,n\_fft−ω\]∗X\[m, \\omega\] = X\[m, \\text{n\\\_fft} - \\omega\]^\*X\[m,ω\]\=X\[m,n\_fft−ω\]∗. Note if the input or window tensors are complex, then `onesided` output is not possible.
    
*   If `normalized` is `True` (default is `False`), the function returns the normalized STFT results, i.e., multiplied by (frame\_length)−0.5(\\text{frame\\\_length})^{-0.5}(frame\_length)−0.5.
    
*   If `return_complex` is `True` (default if input is complex), the return is a `input.dim() + 1` dimensional complex tensor. If `False`, the output is a `input.dim() + 2` dimensional real tensor where the last dimension represents the real and imaginary components.
    

Returns either a complex tensor of size (∗×N×T)(\* \\times N \\times T)(∗×N×T) if `return_complex` is true, or a real tensor of size (∗×N×T×2)(\* \\times N \\times T \\times 2)(∗×N×T×2). Where ∗\*∗ is the optional batch size of `input`, NNN is the number of frequencies where STFT is applied and TTT is the total number of frames used.

Warning

This function changed signature at version 0.4.1. Calling with the previous signature may cause error or return incorrect result.

Parameters:

*   **input** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    ) – the input tensor of shape (B?, L) where B? is an optional batch dimension
    
*   **n\_fft** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – size of Fourier transform
    
*   **hop\_length** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – the distance between neighboring sliding window frames. Default: `None` (treated as equal to `floor(n_fft / 4)`)
    
*   **win\_length** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – the size of window frame and STFT filter. Default: `None` (treated as equal to `n_fft`)
    
*   **window** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
    _,_ _optional_) – the optional window function. Shape must be 1d and <= n\_fft Default: `None` (treated as window of all 111 s)
    
*   **center** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – whether to pad `input` on both sides so that the ttt\-th frame is centered at time t×hop\_lengtht \\times \\text{hop\\\_length}t×hop\_length. Default: `True`
    
*   **pad\_mode** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – controls the padding method used when `center` is `True`. Default: `"reflect"`
    
*   **normalized** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – controls whether to return the normalized STFT results Default: `False`
    
*   **onesided** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – controls whether to return half of results to avoid redundancy for real inputs. Default: `True` for real `input` and `window`, `False` otherwise.
    
*   **return\_complex** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) –
    
    whether to return a complex tensor, or a real tensor with an extra last dimension for the real and imaginary components.
    
    Changed in version 2.0: `return_complex` is now a required argument for real inputs, as the default is being transitioned to `True`.
    
    Deprecated since version 2.0: `return_complex=False` is deprecated, instead use `return_complex=True` Note that calling [`torch.view_as_real()`](https://docs.pytorch.org/docs/2.15/generated/torch.view_as_real.html#torch.view_as_real "torch.view_as_real")
     on the output will recover the deprecated output format.
    

Returns:

A tensor containing the STFT result with shape (B?, N, T, C?) where

*   B? is an optional batch dimension from the input.
    
*   N is the number of frequency samples, (n\_fft // 2) + 1 for onesided=True, or otherwise n\_fft.
    
*   T is the number of frames, 1 + L // hop\_length for center=True, or 1 + (L - n\_fft) // hop\_length otherwise.
    
*   C? is an optional length-2 dimension of real and imaginary components, present when return\_complex=False.
    

Return type:

[Tensor](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")

On this page

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/generated/torch.functional.stft.rst.txt)

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