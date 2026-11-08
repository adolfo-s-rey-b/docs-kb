Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/signal.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/signal.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/signal.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/signal.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/signal.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/signal.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/signal.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/signal.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/signal.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/signal.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/signal.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/signal.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/signal.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/signal.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/signal.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/signal.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/signal.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/signal.html)
[v1.13](https://docs.pytorch.org/docs/1.13/signal.html)
[v1.12](https://docs.pytorch.org/docs/1.12/signal.html)
[v1.11](https://docs.pytorch.org/docs/1.11/signal.html)
[v1.10](https://docs.pytorch.org/docs/1.10/signal.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/signal.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/signal.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/signal.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/signal.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/signal.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/signal.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/signal.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/signal.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/signal.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/signal.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/signal.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/signal.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/signal.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/signal.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/signal.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/signal.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/signal.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/signal.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/signal.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/signal.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/signal.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/signal.html)

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

torch.signal[#](https://docs.pytorch.org/docs/2.15/signal.html#module-torch.signal "Link to this heading")

===========================================================================================================

Created On: Oct 14, 2022 | Last Updated On: May 15, 2026

The `torch.signal` module, modeled after SciPy’s [signal](https://docs.scipy.org/doc/scipy/reference/signal.html)
module.

torch.signal.windows[#](https://docs.pytorch.org/docs/2.15/signal.html#module-torch.signal.windows "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`bartlett`](https://docs.pytorch.org/docs/2.15/generated/torch.signal.windows.windows.bartlett.html#torch.signal.windows.windows.bartlett "torch.signal.windows.windows.bartlett") | Computes the Bartlett window. |
| [`blackman`](https://docs.pytorch.org/docs/2.15/generated/torch.signal.windows.windows.blackman.html#torch.signal.windows.windows.blackman "torch.signal.windows.windows.blackman") | Computes the Blackman window. |
| [`cosine`](https://docs.pytorch.org/docs/2.15/generated/torch.signal.windows.windows.cosine.html#torch.signal.windows.windows.cosine "torch.signal.windows.windows.cosine") | Computes a window with a simple cosine waveform, following the same implementation as SciPy. |
| [`exponential`](https://docs.pytorch.org/docs/2.15/generated/torch.signal.windows.windows.exponential.html#torch.signal.windows.windows.exponential "torch.signal.windows.windows.exponential") | Computes a window with an exponential waveform. |
| [`gaussian`](https://docs.pytorch.org/docs/2.15/generated/torch.signal.windows.windows.gaussian.html#torch.signal.windows.windows.gaussian "torch.signal.windows.windows.gaussian") | Computes a window with a gaussian waveform. |
| [`general_cosine`](https://docs.pytorch.org/docs/2.15/generated/torch.signal.windows.windows.general_cosine.html#torch.signal.windows.windows.general_cosine "torch.signal.windows.windows.general_cosine") | Computes the general cosine window. |
| [`general_hamming`](https://docs.pytorch.org/docs/2.15/generated/torch.signal.windows.windows.general_hamming.html#torch.signal.windows.windows.general_hamming "torch.signal.windows.windows.general_hamming") | Computes the general Hamming window. |
| [`hamming`](https://docs.pytorch.org/docs/2.15/generated/torch.signal.windows.windows.hamming.html#torch.signal.windows.windows.hamming "torch.signal.windows.windows.hamming") | Computes the Hamming window. |
| [`hann`](https://docs.pytorch.org/docs/2.15/generated/torch.signal.windows.windows.hann.html#torch.signal.windows.windows.hann "torch.signal.windows.windows.hann") | Computes the Hann window. |
| [`kaiser`](https://docs.pytorch.org/docs/2.15/generated/torch.signal.windows.windows.kaiser.html#torch.signal.windows.windows.kaiser "torch.signal.windows.windows.kaiser") | Computes the Kaiser window. |
| [`nuttall`](https://docs.pytorch.org/docs/2.15/generated/torch.signal.windows.windows.nuttall.html#torch.signal.windows.windows.nuttall "torch.signal.windows.windows.nuttall") | Computes the minimum 4-term Blackman-Harris window according to Nuttall. |

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/signal.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/signal.md.txt)

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