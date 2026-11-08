Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/cuda._sanitizer.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/cuda._sanitizer.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/cuda._sanitizer.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/cuda._sanitizer.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/cuda._sanitizer.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/cuda._sanitizer.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/cuda._sanitizer.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/cuda._sanitizer.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/cuda._sanitizer.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/cuda._sanitizer.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/cuda._sanitizer.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/cuda._sanitizer.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/cuda._sanitizer.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/cuda._sanitizer.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/cuda._sanitizer.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/cuda._sanitizer.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/cuda._sanitizer.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/cuda._sanitizer.html)
[v1.13](https://docs.pytorch.org/docs/1.13/cuda._sanitizer.html)
[v1.12](https://docs.pytorch.org/docs/1.12/cuda._sanitizer.html)
[v1.11](https://docs.pytorch.org/docs/1.11/cuda._sanitizer.html)
[v1.10](https://docs.pytorch.org/docs/1.10/cuda._sanitizer.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/cuda._sanitizer.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/cuda._sanitizer.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/cuda._sanitizer.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/cuda._sanitizer.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/cuda._sanitizer.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/cuda._sanitizer.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/cuda._sanitizer.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/cuda._sanitizer.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/cuda._sanitizer.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/cuda._sanitizer.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/cuda._sanitizer.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/cuda._sanitizer.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/cuda._sanitizer.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/cuda._sanitizer.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/cuda._sanitizer.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/cuda._sanitizer.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/cuda._sanitizer.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/cuda._sanitizer.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/cuda._sanitizer.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/cuda._sanitizer.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/cuda._sanitizer.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/cuda._sanitizer.html)

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

CUDA Stream Sanitizer[#](https://docs.pytorch.org/docs/2.15/cuda._sanitizer.html#cuda-stream-sanitizer "Link to this heading")

===============================================================================================================================

Created On: May 13, 2026 | Last Updated On: May 13, 2026

Note

This is a prototype feature, which means it is at an early stage for feedback and testing, and its components are subject to change.

Overview[#](https://docs.pytorch.org/docs/2.15/cuda._sanitizer.html#module-torch.cuda._sanitizer "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

This module introduces CUDA Sanitizer, a tool for detecting synchronization errors between kernels ran on different streams.

It stores information on accesses to tensors to determine if they are synchronized or not. When enabled in a python program and a possible data race is detected, a detailed warning will be printed and the program will exit.

It can be enabled either by importing this module and calling [`enable_cuda_sanitizer()`](https://docs.pytorch.org/docs/2.15/cuda._sanitizer.html#torch.cuda._sanitizer.enable_cuda_sanitizer "torch.cuda._sanitizer.enable_cuda_sanitizer")
 or by exporting the `TORCH_CUDA_SANITIZER` environment variable.

Usage[#](https://docs.pytorch.org/docs/2.15/cuda._sanitizer.html#usage "Link to this heading")

-----------------------------------------------------------------------------------------------

Here is an example of a simple synchronization error in PyTorch:

import torch

a \= torch.rand(4, 2, device\="cuda")

with torch.cuda.stream(torch.cuda.Stream()):
    torch.mul(a, 5, out\=a)

Copy to clipboard

The `a` tensor is initialized on the default stream and, without any synchronization methods, modified on a new stream. The two kernels will run concurrently on the same tensor, which might cause the second kernel to read uninitialized data before the first one was able to write it, or the first kernel might overwrite part of the result of the second. When this script is run on the commandline with:

TORCH\_CUDA\_SANITIZER\=1 python example\_error.py

Copy to clipboard

the following output is printed by CSAN:

\============================
CSAN detected a possible data race on tensor with data pointer 139719969079296
Access by stream 94646435460352 during kernel:
aten::mul.out(Tensor self, Tensor other, \*, Tensor(a!) out) -> Tensor(a!)
writing to argument(s) self, out, and to the output
With stack trace:
  File "example\_error.py", line 6, in <module>
    torch.mul(a, 5, out=a)
  ...
  File "pytorch/torch/cuda/\_sanitizer.py", line 364, in \_handle\_kernel\_launch
    stack\_trace = traceback.StackSummary.extract(

Previous access by stream 0 during kernel:
aten::rand(int\[\] size, \*, int? dtype=None, Device? device=None) -> Tensor
writing to the output
With stack trace:
  File "example\_error.py", line 3, in <module>
    a = torch.rand(10000, device="cuda")
  ...
  File "pytorch/torch/cuda/\_sanitizer.py", line 364, in \_handle\_kernel\_launch
    stack\_trace = traceback.StackSummary.extract(

Tensor was allocated with stack trace:
  File "example\_error.py", line 3, in <module>
    a = torch.rand(10000, device="cuda")
  ...
  File "pytorch/torch/cuda/\_sanitizer.py", line 420, in \_handle\_memory\_allocation
    traceback.StackSummary.extract(

Copy to clipboard

This gives extensive insight into the origin of the error:

*   A tensor was incorrectly accessed from streams with ids: 0 (default stream) and 94646435460352 (new stream)
    
*   The tensor was allocated by invoking `a = torch.rand(10000, device="cuda")`
    
*   The faulty accesses were caused by operators
    
    *   `a = torch.rand(10000, device="cuda")` on stream 0
        
    *   `torch.mul(a, 5, out=a)` on stream 94646435460352
        
*   The error message also displays the schemas of the invoked operators, along with a note showing which arguments of the operators correspond to the affected tensor.
    
    *   In the example, it can be seen that tensor `a` corresponds to arguments `self`, `out` and the `output` value of the invoked operator `torch.mul`.
        

See also

The list of supported torch operators and their schemas can be viewed [here](https://docs.pytorch.org/docs/2.15/torch.html)
.

The bug can be fixed by forcing the new stream to wait for the default stream:

with torch.cuda.stream(torch.cuda.Stream()):
    torch.cuda.current\_stream().wait\_stream(torch.cuda.default\_stream())
    torch.mul(a, 5, out\=a)

Copy to clipboard

When the script is run again, there are no errors reported.

API Reference[#](https://docs.pytorch.org/docs/2.15/cuda._sanitizer.html#api-reference "Link to this heading")

---------------------------------------------------------------------------------------------------------------

torch.cuda.\_sanitizer.enable\_cuda\_sanitizer()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/_sanitizer.py#L659)
[#](https://docs.pytorch.org/docs/2.15/cuda._sanitizer.html#torch.cuda._sanitizer.enable_cuda_sanitizer "Link to this definition")

Enable CUDA Sanitizer.

The sanitizer will begin to analyze low-level CUDA calls invoked by torch functions for synchronization errors. All data races found will be printed to the standard error output along with stack traces of suspected causes. For best results, the sanitizer should be enabled at the very beginning of the program.

torch.cuda.\_sanitizer.zip\_arguments(_schema_, _args_, _kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/_sanitizer.py#L474)
[#](https://docs.pytorch.org/docs/2.15/cuda._sanitizer.html#torch.cuda._sanitizer.zip_arguments "Link to this definition")

Return type:

[_Iterator_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.15)")
\[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[_Argument_, [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\]\]

torch.cuda.\_sanitizer.zip\_by\_key(_a_, _b_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/cuda/_sanitizer.py#L468)
[#](https://docs.pytorch.org/docs/2.15/cuda._sanitizer.html#torch.cuda._sanitizer.zip_by_key "Link to this definition")

Return type:

[_Iterator_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.15)")
\[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[_TK_, _TVa_, _TVb_\]\]

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/cuda._sanitizer.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/cuda._sanitizer.md.txt)

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