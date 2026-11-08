Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/fft.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/fft.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/fft.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/fft.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/fft.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/fft.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/fft.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/fft.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/fft.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/fft.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/fft.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/fft.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/fft.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/fft.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/fft.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/fft.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/fft.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/fft.html)
[v1.13](https://docs.pytorch.org/docs/1.13/fft.html)
[v1.12](https://docs.pytorch.org/docs/1.12/fft.html)
[v1.11](https://docs.pytorch.org/docs/1.11/fft.html)
[v1.10](https://docs.pytorch.org/docs/1.10/fft.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/fft.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/fft.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/fft.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/fft.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/fft.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/fft.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/fft.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/fft.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/fft.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/fft.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/fft.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/fft.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/fft.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/fft.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/fft.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/fft.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/fft.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/fft.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/fft.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/fft.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/fft.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/fft.html)

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

torch.fft[#](https://docs.pytorch.org/docs/2.15/fft.html#torch-fft "Link to this heading")

===========================================================================================

Created On: Aug 06, 2020 | Last Updated On: Jun 13, 2025

Discrete Fourier transforms and related functions.

Fast Fourier Transforms[#](https://docs.pytorch.org/docs/2.15/fft.html#fast-fourier-transforms "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`fft`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.fft.html#torch.fft.fft "torch.fft.fft") | Computes the one dimensional discrete Fourier transform of `input`. |
| [`ifft`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.ifft.html#torch.fft.ifft "torch.fft.ifft") | Computes the one dimensional inverse discrete Fourier transform of `input`. |
| [`fft2`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.fft2.html#torch.fft.fft2 "torch.fft.fft2") | Computes the 2 dimensional discrete Fourier transform of `input`. |
| [`ifft2`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.ifft2.html#torch.fft.ifft2 "torch.fft.ifft2") | Computes the 2 dimensional inverse discrete Fourier transform of `input`. |
| [`fftn`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.fftn.html#torch.fft.fftn "torch.fft.fftn") | Computes the N dimensional discrete Fourier transform of `input`. |
| [`ifftn`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.ifftn.html#torch.fft.ifftn "torch.fft.ifftn") | Computes the N dimensional inverse discrete Fourier transform of `input`. |
| [`rfft`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.rfft.html#torch.fft.rfft "torch.fft.rfft") | Computes the one dimensional Fourier transform of real-valued `input`. |
| [`irfft`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.irfft.html#torch.fft.irfft "torch.fft.irfft") | Computes the inverse of [`rfft()`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.rfft.html#torch.fft.rfft "torch.fft.rfft")<br>. |
| [`rfft2`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.rfft2.html#torch.fft.rfft2 "torch.fft.rfft2") | Computes the 2-dimensional discrete Fourier transform of real `input`. |
| [`irfft2`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.irfft2.html#torch.fft.irfft2 "torch.fft.irfft2") | Computes the inverse of [`rfft2()`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.rfft2.html#torch.fft.rfft2 "torch.fft.rfft2")<br>. |
| [`rfftn`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.rfftn.html#torch.fft.rfftn "torch.fft.rfftn") | Computes the N-dimensional discrete Fourier transform of real `input`. |
| [`irfftn`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.irfftn.html#torch.fft.irfftn "torch.fft.irfftn") | Computes the inverse of [`rfftn()`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.rfftn.html#torch.fft.rfftn "torch.fft.rfftn")<br>. |
| [`hfft`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.hfft.html#torch.fft.hfft "torch.fft.hfft") | Computes the one dimensional discrete Fourier transform of a Hermitian symmetric `input` signal. |
| [`ihfft`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.ihfft.html#torch.fft.ihfft "torch.fft.ihfft") | Computes the inverse of [`hfft()`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.hfft.html#torch.fft.hfft "torch.fft.hfft")<br>. |
| [`hfft2`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.hfft2.html#torch.fft.hfft2 "torch.fft.hfft2") | Computes the 2-dimensional discrete Fourier transform of a Hermitian symmetric `input` signal. |
| [`ihfft2`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.ihfft2.html#torch.fft.ihfft2 "torch.fft.ihfft2") | Computes the 2-dimensional inverse discrete Fourier transform of real `input`. |
| [`hfftn`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.hfftn.html#torch.fft.hfftn "torch.fft.hfftn") | Computes the n-dimensional discrete Fourier transform of a Hermitian symmetric `input` signal. |
| [`ihfftn`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.ihfftn.html#torch.fft.ihfftn "torch.fft.ihfftn") | Computes the N-dimensional inverse discrete Fourier transform of real `input`. |

Helper Functions[#](https://docs.pytorch.org/docs/2.15/fft.html#helper-functions "Link to this heading")

---------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`fftfreq`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.fftfreq.html#torch.fft.fftfreq "torch.fft.fftfreq") | Computes the discrete Fourier Transform sample frequencies for a signal of size `n`. |
| [`rfftfreq`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.rfftfreq.html#torch.fft.rfftfreq "torch.fft.rfftfreq") | Computes the sample frequencies for [`rfft()`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.rfft.html#torch.fft.rfft "torch.fft.rfft")<br> with a signal of size `n`. |
| [`fftshift`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.fftshift.html#torch.fft.fftshift "torch.fft.fftshift") | Reorders n-dimensional FFT data, as provided by [`fftn()`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.fftn.html#torch.fft.fftn "torch.fft.fftn")<br>, to have negative frequency terms first. |
| [`ifftshift`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.ifftshift.html#torch.fft.ifftshift "torch.fft.ifftshift") | Inverse of [`fftshift()`](https://docs.pytorch.org/docs/2.15/generated/torch.fft.fftshift.html#torch.fft.fftshift "torch.fft.fftshift")<br>. |

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/fft.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/fft.md.txt)

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