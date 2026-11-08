Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/notes/mkldnn.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/notes/mkldnn.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/notes/mkldnn.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/notes/mkldnn.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/notes/mkldnn.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/notes/mkldnn.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/notes/mkldnn.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/notes/mkldnn.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/notes/mkldnn.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/notes/mkldnn.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/notes/mkldnn.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/notes/mkldnn.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/notes/mkldnn.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/notes/mkldnn.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/notes/mkldnn.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/notes/mkldnn.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/notes/mkldnn.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/notes/mkldnn.html)
[v1.13](https://docs.pytorch.org/docs/1.13/notes/mkldnn.html)
[v1.12](https://docs.pytorch.org/docs/1.12/notes/mkldnn.html)
[v1.11](https://docs.pytorch.org/docs/1.11/notes/mkldnn.html)
[v1.10](https://docs.pytorch.org/docs/1.10/notes/mkldnn.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/notes/mkldnn.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/notes/mkldnn.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/notes/mkldnn.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/notes/mkldnn.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/notes/mkldnn.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/notes/mkldnn.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/notes/mkldnn.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/notes/mkldnn.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/notes/mkldnn.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/notes/mkldnn.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/notes/mkldnn.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/notes/mkldnn.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/notes/mkldnn.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/notes/mkldnn.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/notes/mkldnn.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/notes/mkldnn.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/notes/mkldnn.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/notes/mkldnn.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/notes/mkldnn.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/notes/mkldnn.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/notes/mkldnn.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/notes/mkldnn.html)

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

MKLDNN backend[#](https://docs.pytorch.org/docs/2.15/notes/mkldnn.html#mkldnn-backend "Link to this heading")

==============================================================================================================

Created On: May 07, 2026 | Last Updated On: Jul 08, 2026

MKLDNN is an open-source cross-platform performance library of basic building blocks for deep learning applications.

\# The flag below controls whether enable MKLDNN backend in PyTorch.
torch.backends.mkldnn.enabled \= True

Copy to clipboard

Users can disable MKLDNN backend by:

torch.backends.mkldnn.enabled \= False

Copy to clipboard

Bfloat16 (BF16) on MKLDNN backend[#](https://docs.pytorch.org/docs/2.15/notes/mkldnn.html#bfloat16-bf16-on-mkldnn-backend "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

Starting in PyTorch 2.9, there is a set of APIs to control the internal computation precision for `float32` operators.

\# The flag below controls the internal computation precision for mkldnn matmul. Default ieee is float32.
torch.backends.mkldnn.matmul.fp32\_precision \= "ieee"

\# The flag below controls the internal computation precision for mkldnn conv. Default ieee is float32.
torch.backends.mkldnn.conv.fp32\_precision \= "ieee"

\# The flag below controls the internal computation precision for mkldnn rnn. Default ieee is float32.
torch.backends.mkldnn.rnn.fp32\_precision \= "ieee"

Copy to clipboard

Note that besides matmuls and convolutions themselves, functions and nn modules that internally uses matmuls or convolutions are also affected. These include [`torch.nn.Linear`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Linear.html#torch.nn.Linear "torch.nn.Linear")
, `torch.nn._ConvNd`, [`torch.cdist()`](https://docs.pytorch.org/docs/2.15/generated/torch.cdist.html#torch.cdist "torch.cdist")
, [`torch.tensordot()`](https://docs.pytorch.org/docs/2.15/generated/torch.tensordot.html#torch.tensordot "torch.tensordot")
, [`torch.nn.functional.affine_grid()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.affine_grid.html#torch.nn.functional.affine_grid "torch.nn.functional.affine_grid")
 and [`torch.nn.functional.grid_sample()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.functional.grid_sample.html#torch.nn.functional.grid_sample "torch.nn.functional.grid_sample")
, [`torch.nn.AdaptiveLogSoftmaxWithLoss`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.AdaptiveLogSoftmaxWithLoss.html#torch.nn.AdaptiveLogSoftmaxWithLoss "torch.nn.AdaptiveLogSoftmaxWithLoss")
, [`torch.nn.GRU`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.GRU.html#torch.nn.GRU "torch.nn.GRU")
 and [`torch.nn.LSTM`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.LSTM.html#torch.nn.LSTM "torch.nn.LSTM")
.

To get an idea of the precision and speed, see the example code and benchmark data (on SPR) below:

torch.manual\_seed(0)
a\_full \= torch.randn(10240, 10240, dtype\=torch.double)
b\_full \= torch.randn(10240, 10240, dtype\=torch.double)
ab\_full \= a\_full @ b\_full
mean \= ab\_full.abs().mean()  \# 80.7451

a \= a\_full.float()
b \= b\_full.float()

\# Do matmul at BF16 mode.
torch.backends.mkldnn.matmul.fp32\_precision \= 'bf16'
ab\_bf16 \= a @ b  \# expected speedup with BF16 dot-product acceleration
error \= (ab\_bf16 \- ab\_full).abs().max()  \# 1.3704
relative\_error \= error / mean  \# 0.0170
print(error, relative\_error)

\# Do matmul at TF32 mode.
torch.backends.mkldnn.matmul.fp32\_precision \= 'tf32'
ab\_tf32 \= a @ b  \# expected speedup with TF32 dot-product acceleration
error \= (ab\_tf32 \- ab\_full).abs().max()  \# 0.0004
relative\_error \= error / mean  \# 0.00000552
print(error, relative\_error)

\# Do matmul FP32 mode.
torch.backends.mkldnn.matmul.fp32\_precision \= 'ieee'
ab\_fp32 \= a @ b
error \= (ab\_fp32 \- ab\_full).abs().max()  \# 0.0003
relative\_error \= error / mean  \# 0.00000317
print(error, relative\_error)

Copy to clipboard

From the above example, we can see that with BF16, the speed is ~7x faster on SPR, and that relative error compared to double precision is approximately 2 orders of magnitude larger. If full FP32 precision is needed, users can disable BF16 by:

torch.backends.mkldnn.matmul.fp32\_precision \= 'ieee'
torch.backends.mkldnn.conv.fp32\_precision \= 'ieee'
torch.backends.mkldnn.rnn.fp32\_precision \= 'ieee'

Copy to clipboard

To toggle the BF16 flags off in C++, you can do

at::globalContext().setFloat32Precision("ieee", "mkldnn", "matmul");
at::globalContext().setFloat32Precision("ieee", "mkldnn", "conv");
at::globalContext().setFloat32Precision("ieee", "mkldnn", "rnn");

Copy to clipboard

We can override a generic setting for a specific operator or backend if the fp32\_precision is set to `ieee`.

torch.backends.fp32\_precision \= "bf16"
torch.backends.mkldnn.fp32\_precision \= "ieee"
torch.backends.mkldnn.matmul.fp32\_precision \= "ieee"

Copy to clipboard

For such case, both `torch.backends.mkldnn.fp32_precision` and `torch.backends.mkldnn.matmul.fp32_precision` is overridden to bf16.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/notes/mkldnn.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/notes/mkldnn.md.txt)

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