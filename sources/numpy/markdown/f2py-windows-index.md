[Skip to main content](https://numpy.org/doc/stable/f2py/windows/index.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

F2PY and Windows[#](https://numpy.org/doc/stable/f2py/windows/index.html#f2py-and-windows "Link to this heading")

==================================================================================================================

Warning

F2PY support for Windows is not always at par with Linux support

Note

[SciPy’s documentation](https://scipy.github.io/devdocs/building/index.html#system-level-dependencies)
 has some information on system-level dependencies which are well tested for Fortran as well.

Broadly speaking, there are two issues working with F2PY on Windows:

*   the lack of actively developed FOSS Fortran compilers, and,
    
*   the linking issues related to the C runtime library for building Python-C extensions.
    

The focus of this section is to establish a guideline for developing and extending Fortran modules for Python natively, via F2PY on Windows.

Currently supported toolchains are:

*   Mingw-w64 C/C++/Fortran compilers
    
*   Intel compilers
    
*   Clang-cl + Flang
    
*   MSVC + Flang
    

Overview[#](https://numpy.org/doc/stable/f2py/windows/index.html#overview "Link to this heading")

--------------------------------------------------------------------------------------------------

From a user perspective, the most UNIX compatible Windows development environment is through emulation, either via the Windows Subsystem on Linux, or facilitated by Docker. In a similar vein, traditional virtualization methods like VirtualBox are also reasonable methods to develop UNIX tools on Windows.

Native Windows support is typically stunted beyond the usage of commercial compilers. However, as of 2022, most commercial compilers have free plans which are sufficient for general use. Additionally, the Fortran language features supported by `f2py` (partial coverage of Fortran 2003), means that newer toolchains are often not required. Briefly, then, for an end user, in order of use:

Classic Intel Compilers (commercial)

These are maintained actively, though licensing restrictions may apply as further detailed in [F2PY and Windows Intel Fortran](https://numpy.org/doc/stable/f2py/windows/intel.html#f2py-win-intel)
.

Suitable for general use for those building native Windows programs by building off of MSVC.

MSYS2 (FOSS)

In conjunction with the `mingw-w64` project, `gfortran` and `gcc` toolchains can be used to natively build Windows programs.

Windows Subsystem for Linux

Assuming the usage of `gfortran`, this can be used for cross-compiling Windows applications, but is significantly more complicated.

Conda

Windows support for GNU compilers in `conda` is provided by [conda-forge](https://conda-forge.org/docs/maintainer/infrastructure/#compilers-supplied-by-conda-forge)
 channel.

PGI Compilers (commercial)

Unmaintained but sufficient if an existing license is present. Works natively, but has been superseded by the Nvidia HPC SDK, with no [native Windows support](https://developer.nvidia.com/nvidia-hpc-sdk-downloads#collapseFour)
.

Cygwin (FOSS)

Can also be used for `gfortran`. However, the POSIX API compatibility layer provided by Cygwin is meant to compile UNIX software on Windows, instead of building native Windows programs. This means cross compilation is required.

Intel oneAPI

The newer Intel compilers (`ifx`, `icx`) are based on LLVM and can be used for native compilation. Licensing requirements can be onerous.

Classic Flang (FOSS)

The backbone of the PGI compilers were cannibalized to form the “classic” or [legacy version of Flang](https://github.com/flang-compiler/flang)
. This may be compiled from source and used natively. [LLVM Flang](https://releases.llvm.org/11.0.0/tools/flang/docs/ReleaseNotes.html)
 does not support Windows yet (30-01-2022).

LFortran (FOSS)

One of two LLVM based compilers. Not all of F2PY supported Fortran can be compiled yet (30-01-2022) but uses MSVC for native linking.

Baseline[#](https://numpy.org/doc/stable/f2py/windows/index.html#baseline "Link to this heading")

--------------------------------------------------------------------------------------------------

For this document we will assume the following basic tools:

*   The IDE being considered is the community supported [Microsoft Visual Studio Code](https://code.visualstudio.com/Download)
    
*   The terminal being used is the [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab)
    
*   The shell environment is assumed to be [Powershell 7.x](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.1)
    
*   Python 3.10 from [the Microsoft Store](https://www.microsoft.com/en-us/p/python-310/9pjpw5ldxlz5)
     and this can be tested with
    
    `Get-Command python.exe` resolving to `C:\Users\$USERNAME\AppData\Local\Microsoft\WindowsApps\python.exe`
    
*   The Microsoft Visual C++ (MSVC) toolset
    

With this baseline configuration, we will further consider a configuration matrix as follows:

|     |     |     |
| --- | --- | --- |Support matrix, exe implies a Windows installer[#](https://numpy.org/doc/stable/f2py/windows/index.html#id1 "Link to this table")
| **Fortran Compiler** | **C/C++ Compiler** | **Source** |
| --- | --- | --- |
| Intel Fortran | MSVC / ICC | exe |
| GFortran | MSVC | MSYS2/exe |
| GFortran | GCC | WSL |
| Classic Flang | MSVC | Source / Conda |
| Anaconda GFortran | Anaconda GCC | exe |

For an understanding of the key issues motivating the need for such a matrix [Pauli Virtanen’s in-depth post on wheels with Fortran for Windows](https://pav.iki.fi/blog/2017-10-08/pywingfortran.html#building-python-wheels-with-fortran-for-windows)
 is an excellent resource. An entertaining explanation of an application binary interface (ABI) can be found in this post by [JeanHeyd Meneide](https://thephd.dev/binary-banshees-digital-demons-abi-c-c++-help-me-god-please)
.

PowerShell and MSVC[#](https://numpy.org/doc/stable/f2py/windows/index.html#powershell-and-msvc "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

MSVC is installed either via the Visual Studio Bundle or the lighter (preferred) [Build Tools for Visual Studio](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019)
 with the `Desktop development with C++` setting.

Note

This can take a significant amount of time as it includes a download of around 2GB and requires a restart.

It is possible to use the resulting environment from a [standard command prompt](https://docs.microsoft.com/en-us/cpp/build/building-on-the-command-line?view=msvc-160#developer_command_file_locations)
. However, it is more pleasant to use a [developer powershell](https://docs.microsoft.com/en-us/visualstudio/ide/reference/command-prompt-powershell?view=vs-2019)
, with a [profile in Windows Terminal](https://techcommunity.microsoft.com/t5/microsoft-365-pnp-blog/add-developer-powershell-and-developer-command-prompt-for-visual/ba-p/2243078)
. This can be achieved by adding the following block to the `profiles->list` section of the JSON file used to configure Windows Terminal (see `Settings->Open JSON file`):

{
"name": "Developer PowerShell for VS 2019",
"commandline": "powershell.exe -noe -c \\"$vsPath = (Join-Path ${env:ProgramFiles(x86)} -ChildPath 'Microsoft Visual Studio\\\\2019\\\\BuildTools'); Import-Module (Join-Path $vsPath 'Common7\\\\Tools\\\\Microsoft.VisualStudio.DevShell.dll'); Enter-VsDevShell -VsInstallPath $vsPath -SkipAutomaticLocation\\"",
"icon": "ms-appx:///ProfileIcons/{61c54bbd-c2c6-5271-96e7-009a87ff44bf}.png"
}

Copy to clipboard

Now, testing the compiler toolchain could look like:

 \# New Windows Developer Powershell instance / tab
 \# or
 $vsPath \= (Join-Path ${env:ProgramFiles(x86)} \-ChildPath 'Microsoft Visual Studio\\\\2019\\\\BuildTools');
 Import-Module (Join-Path $vsPath 'Common7\\\\Tools\\\\Microsoft.VisualStudio.DevShell.dll');
 Enter-VsDevShell \-VsInstallPath $vsPath \-SkipAutomaticLocation
 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
 \*\* Visual Studio 2019 Developer PowerShell v16.11.9
 \*\* Copyright (c) 2021 Microsoft Corporation
 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
 cd $HOME
 echo "#include<stdio.h>" \> blah.cpp; echo 'int main(){printf("Hi");return 1;}' \>> blah.cpp
 cl blah.cpp
.\\blah.exe
 \# Hi
 rm blah.cpp

Copy to clipboard

It is also possible to check that the environment has been updated correctly with `$ENV:PATH`.

Microsoft Store Python paths[#](https://numpy.org/doc/stable/f2py/windows/index.html#microsoft-store-python-paths "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

The MS Windows version of Python discussed here installs to a non-deterministic path using a hash. This needs to be added to the `PATH` variable.

$Env:Path += ";$env:LOCALAPPDATA\\packages\\pythonsoftwarefoundation.python.3.10\_qbz5n2kfra8p0\\localcache\\local-packages\\python310\\scripts"

Copy to clipboard

*   [F2PY and Windows Intel Fortran](https://numpy.org/doc/stable/f2py/windows/intel.html)
    
*   [F2PY and Windows with MSYS2](https://numpy.org/doc/stable/f2py/windows/msys2.html)
    
*   [F2PY and Conda on Windows](https://numpy.org/doc/stable/f2py/windows/conda.html)
    
*   [F2PY and PGI Fortran on Windows](https://numpy.org/doc/stable/f2py/windows/pgi.html)
    

On this page