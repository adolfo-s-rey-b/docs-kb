Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/notes/mps.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/notes/mps.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/notes/mps.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/notes/mps.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/notes/mps.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/notes/mps.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/notes/mps.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/notes/mps.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/notes/mps.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/notes/mps.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/notes/mps.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/notes/mps.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/notes/mps.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/notes/mps.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/notes/mps.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/notes/mps.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/notes/mps.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/notes/mps.html)
[v1.13](https://docs.pytorch.org/docs/1.13/notes/mps.html)
[v1.12](https://docs.pytorch.org/docs/1.12/notes/mps.html)
[v1.11](https://docs.pytorch.org/docs/1.11/notes/mps.html)
[v1.10](https://docs.pytorch.org/docs/1.10/notes/mps.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/notes/mps.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/notes/mps.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/notes/mps.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/notes/mps.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/notes/mps.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/notes/mps.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/notes/mps.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/notes/mps.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/notes/mps.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/notes/mps.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/notes/mps.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/notes/mps.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/notes/mps.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/notes/mps.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/notes/mps.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/notes/mps.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/notes/mps.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/notes/mps.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/notes/mps.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/notes/mps.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/notes/mps.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/notes/mps.html)

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

MPS backend[#](https://docs.pytorch.org/docs/2.15/notes/mps.html#mps-backend "Link to this heading")

=====================================================================================================

Created On: May 11, 2026 | Last Updated On: Oct 12, 2026

`mps` device enables high-performance training on GPU for macOS devices with Metal programming framework. It introduces a new device to map Machine Learning computational graphs and primitives on highly efficient Metal Performance Shaders Graph framework and tuned kernels provided by Metal Performance Shaders framework respectively.

The new MPS backend extends the PyTorch ecosystem and provides existing scripts capabilities to setup and run operations on GPU.

To get started, simply move your Tensor and Module to the `mps` device:

\# Check that MPS is available
if not torch.backends.mps.is\_available():
    if not torch.backends.mps.is\_built():
        print("MPS not available because the current PyTorch install was not "
              "built with MPS enabled.")
    else:
        print("MPS not available because the current macOS version is not 15.0+ "
              "and/or you do not have an MPS-enabled device on this machine.")

else:
    mps\_device \= torch.device("mps")

    \# Create a Tensor directly on the mps device
    x \= torch.ones(5, device\=mps\_device)
    \# Or
    x \= torch.ones(5, device\="mps")

    \# Any operation happens on the GPU
    y \= x \* 2

    \# Move your model to mps just like any other device
    model \= YourFavoriteNet()
    model.to(mps\_device)

    \# Now every call runs on the GPU
    pred \= model(x)

Copy to clipboard

Double-precision types[#](https://docs.pytorch.org/docs/2.15/notes/mps.html#double-precision-types "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

The MPS backend does not support `torch.float64` (`torch.double`) or `torch.complex128` (`torch.cdouble`) because Metal Shading Language has no `double` type:

\>>> torch.ones(3, dtype\=torch.float64, device\="mps")
TypeError: Cannot convert a MPS Tensor to float64 dtype as the MPS framework
doesn't support float64. Please use float32 instead.

Copy to clipboard

This is a fundamental limitation of Metal Shading Language rather than an unimplemented PyTorch operator. Consequently, `PYTORCH_ENABLE_MPS_FALLBACK=1` does not apply: tensors with double-precision types cannot be allocated or copied to MPS in the first place. `Tensor.to("mps")` on a float64 tensor raises for the same reason, rather than downcasting implicitly.

A computation that genuinely requires double precision has to run on the CPU.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/notes/mps.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/notes/mps.md.txt)

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