Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/notes/windows.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/notes/windows.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/notes/windows.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/notes/windows.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/notes/windows.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/notes/windows.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/notes/windows.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/notes/windows.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/notes/windows.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/notes/windows.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/notes/windows.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/notes/windows.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/notes/windows.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/notes/windows.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/notes/windows.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/notes/windows.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/notes/windows.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/notes/windows.html)
[v1.13](https://docs.pytorch.org/docs/1.13/notes/windows.html)
[v1.12](https://docs.pytorch.org/docs/1.12/notes/windows.html)
[v1.11](https://docs.pytorch.org/docs/1.11/notes/windows.html)
[v1.10](https://docs.pytorch.org/docs/1.10/notes/windows.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/notes/windows.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/notes/windows.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/notes/windows.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/notes/windows.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/notes/windows.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/notes/windows.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/notes/windows.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/notes/windows.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/notes/windows.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/notes/windows.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/notes/windows.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/notes/windows.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/notes/windows.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/notes/windows.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/notes/windows.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/notes/windows.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/notes/windows.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/notes/windows.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/notes/windows.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/notes/windows.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/notes/windows.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/notes/windows.html)

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

Windows FAQ[#](https://docs.pytorch.org/docs/2.15/notes/windows.html#windows-faq "Link to this heading")

=========================================================================================================

Created On: May 06, 2026 | Last Updated On: May 06, 2026

Building from source[#](https://docs.pytorch.org/docs/2.15/notes/windows.html#building-from-source "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

### Include optional components[#](https://docs.pytorch.org/docs/2.15/notes/windows.html#include-optional-components "Link to this heading")

There are two supported components for Windows PyTorch: MKL and MAGMA. Here are the steps to build with them.

REM Make sure you have 7z and curl installed.

REM Download MKL files
curl https://s3.amazonaws.com/ossci-windows/mkl\_2020.2.254.7z -k -O
7z x -aoa mkl\_2020.2.254.7z -omkl

REM Download MAGMA files
REM version available:
REM 2.5.4 (CUDA 10.1 10.2 11.0 11.1) x (Debug Release)
REM 2.5.3 (CUDA 10.1 10.2 11.0) x (Debug Release)
REM 2.5.2 (CUDA 9.2 10.0 10.1 10.2) x (Debug Release)
REM 2.5.1 (CUDA 9.2 10.0 10.1 10.2) x (Debug Release)
set "CUDA\_PREFIX=cuda102"
set "CONFIG=release"
set "HOST=https://s3.amazonaws.com/ossci-windows"
curl -k "%HOST%/magma\_2.5.4\_%CUDA\_PREFIX%\_%CONFIG%.7z" -o magma.7z
7z x -aoa magma.7z -omagma

REM Setting essential environment variables
set "CMAKE\_INCLUDE\_PATH=%cd%\\mkl\\include"
set "LIB=%cd%\\mkl\\lib;%LIB%"
set "MAGMA\_HOME=%cd%\\magma"

Copy to clipboard

### Speeding CUDA build for Windows[#](https://docs.pytorch.org/docs/2.15/notes/windows.html#speeding-cuda-build-for-windows "Link to this heading")

Visual Studio doesn’t support parallel custom task currently. As an alternative, we can use `Ninja` to parallelize CUDA build tasks. It can be used by typing only a few lines of code.

REM Let's install ninja first.
pip install ninja

REM Set it as the cmake generator
set CMAKE\_GENERATOR\=Ninja

Copy to clipboard

### One key install script[#](https://docs.pytorch.org/docs/2.15/notes/windows.html#one-key-install-script "Link to this heading")

You can take a look at [this set of scripts](https://github.com/peterjc123/pytorch-scripts)
. It will lead the way for you.

Extension[#](https://docs.pytorch.org/docs/2.15/notes/windows.html#extension "Link to this heading")

-----------------------------------------------------------------------------------------------------

### CFFI Extension[#](https://docs.pytorch.org/docs/2.15/notes/windows.html#cffi-extension "Link to this heading")

The support for CFFI Extension is very experimental. You must specify additional `libraries` in `Extension` object to make it build on Windows.

ffi \= create\_extension(
    '\_ext.my\_lib',
    headers\=headers,
    sources\=sources,
    define\_macros\=defines,
    relative\_to\=\_\_file\_\_,
    with\_cuda\=with\_cuda,
    extra\_compile\_args\=\["-std=c99"\],
    libraries\=\['ATen', '\_C'\] \# Append cuda libraries when necessary, like cudart
)

Copy to clipboard

### Cpp Extension[#](https://docs.pytorch.org/docs/2.15/notes/windows.html#cpp-extension "Link to this heading")

This type of extension has better support compared with the previous one. However, it still needs some manual configuration. First, you should open the **x86\_x64 Cross Tools Command Prompt for VS 2017**. And then, you can start your compiling process.

Installation[#](https://docs.pytorch.org/docs/2.15/notes/windows.html#installation "Link to this heading")

-----------------------------------------------------------------------------------------------------------

### Package not found in win-32 channel.[#](https://docs.pytorch.org/docs/2.15/notes/windows.html#package-not-found-in-win-32-channel "Link to this heading")

Solving environment: failed

PackagesNotFoundError: The following packages are not available from current channels:

- pytorch

Current channels:
- https://repo.continuum.io/pkgs/main/win-32
- https://repo.continuum.io/pkgs/main/noarch
- https://repo.continuum.io/pkgs/free/win-32
- https://repo.continuum.io/pkgs/free/noarch
- https://repo.continuum.io/pkgs/r/win-32
- https://repo.continuum.io/pkgs/r/noarch
- https://repo.continuum.io/pkgs/pro/win-32
- https://repo.continuum.io/pkgs/pro/noarch
- https://repo.continuum.io/pkgs/msys2/win-32
- https://repo.continuum.io/pkgs/msys2/noarch

Copy to clipboard

PyTorch doesn’t work on 32-bit system. Please use Windows and Python 64-bit version.

### Import error[#](https://docs.pytorch.org/docs/2.15/notes/windows.html#import-error "Link to this heading")

from torch.\_C import \*

ImportError: DLL load failed: The specified module could not be found.

Copy to clipboard

The problem is caused by the missing of the essential files. For the wheels package, since we didn’t pack some libraries and VS2017 redistributable files in, please make sure you install them manually. The [VS 2017 redistributable installer](https://aka.ms/vs/15/release/VC_redist.x64.exe)
 can be downloaded. And you should also pay attention to your installation of Numpy. Make sure it uses MKL instead of OpenBLAS. You may type in the following command.

pip install numpy mkl intel-openmp mkl\_fft

Copy to clipboard

Usage (multiprocessing)[#](https://docs.pytorch.org/docs/2.15/notes/windows.html#usage-multiprocessing "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

### Multiprocessing error without if-clause protection[#](https://docs.pytorch.org/docs/2.15/notes/windows.html#multiprocessing-error-without-if-clause-protection "Link to this heading")

RuntimeError:
       An attempt has been made to start a new process before the
       current process has finished its bootstrapping phase.

   This probably means that you are not using fork to start your
   child processes and you have forgotten to use the proper idiom
   in the main module:

       if \_\_name\_\_ \== '\_\_main\_\_':
           freeze\_support()
           ...

   The "freeze\_support()" line can be omitted if the program
   is not going to be frozen to produce an executable.

Copy to clipboard

The implementation of `multiprocessing` is different on Windows, which uses `spawn` instead of `fork`. So we have to wrap the code with an if-clause to protect the code from executing multiple times. Refactor your code into the following structure.

import torch

def main()
    for i, data in enumerate(dataloader):
        \# do something here

if \_\_name\_\_ \== '\_\_main\_\_':
    main()

Copy to clipboard

### Multiprocessing error “Broken pipe”[#](https://docs.pytorch.org/docs/2.15/notes/windows.html#multiprocessing-error-broken-pipe "Link to this heading")

ForkingPickler(file, protocol).dump(obj)

BrokenPipeError: \[Errno 32\] Broken pipe

Copy to clipboard

This issue happens when the child process ends before the parent process finishes sending data. There may be something wrong with your code. You can debug your code by reducing the `num_worker` of [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
 to zero and see if the issue persists.

### Multiprocessing error “driver shut down”[#](https://docs.pytorch.org/docs/2.15/notes/windows.html#multiprocessing-error-driver-shut-down "Link to this heading")

Couldn't open shared file mapping: <torch\_14808\_1591070686>, error code: <1455> at torch\\lib\\TH\\THAllocator.c:154

\[windows\] driver shut down

Copy to clipboard

Please update your graphics driver. If this persists, this may be that your graphics card is too old or the calculation is too heavy for your card. Please update the TDR settings according to this [post](https://www.pugetsystems.com/labs/hpc/Working-around-TDR-in-Windows-for-a-better-GPU-computing-experience-777/)
.

### CUDA IPC operations[#](https://docs.pytorch.org/docs/2.15/notes/windows.html#cuda-ipc-operations "Link to this heading")

THCudaCheck FAIL file\=torch\\csrc\\generic\\StorageSharing.cpp line\=252 error\=63 : OS call failed or operation not supported on this OS

Copy to clipboard

They are not supported on Windows. Something like doing multiprocessing on CUDA tensors cannot succeed, there are two alternatives for this.

1.  Don’t use `multiprocessing`. Set the `num_worker` of [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
     to zero.
    
2.  Share CPU tensors instead. Make sure your custom `DataSet` returns CPU tensors.
    

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/notes/windows.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/notes/windows.md.txt)

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