[Skip to main content](https://numpy.org/doc/stable/user/how-to-verify-bug.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/user/how-to-verify-bug.html)
[2.5 (stable)](https://numpy.org/doc/stable/user/how-to-verify-bug.html)
[2.4](https://numpy.org/doc/2.4/user/how-to-verify-bug.html)
[2.3](https://numpy.org/doc/2.3/user/how-to-verify-bug.html)
[2.2](https://numpy.org/doc/2.2/user/how-to-verify-bug.html)
[2.1](https://numpy.org/doc/2.1/user/how-to-verify-bug.html)
[2.0](https://numpy.org/doc/2.0/user/how-to-verify-bug.html)
[1.26](https://numpy.org/doc/1.26/user/how-to-verify-bug.html)
[1.25](https://numpy.org/doc/1.25/user/how-to-verify-bug.html)
[1.24](https://numpy.org/doc/1.24/user/how-to-verify-bug.html)
[1.23](https://numpy.org/doc/1.23/user/how-to-verify-bug.html)
[1.22](https://numpy.org/doc/1.22/user/how-to-verify-bug.html)
[1.21](https://numpy.org/doc/1.21/user/how-to-verify-bug.html)
[1.20](https://numpy.org/doc/1.20/user/how-to-verify-bug.html)
[1.19](https://numpy.org/doc/1.19/user/how-to-verify-bug.html)
[1.18](https://numpy.org/doc/1.18/user/how-to-verify-bug.html)
[1.17](https://numpy.org/doc/1.17/user/how-to-verify-bug.html)
[1.16](https://numpy.org/doc/1.16/user/how-to-verify-bug.html)
[1.15](https://numpy.org/doc/1.15/user/how-to-verify-bug.html)
[1.14](https://numpy.org/doc/1.14/user/how-to-verify-bug.html)
[1.13](https://numpy.org/doc/1.13/user/how-to-verify-bug.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Verifying bugs and bug fixes in NumPy[#](https://numpy.org/doc/stable/user/how-to-verify-bug.html#verifying-bugs-and-bug-fixes-in-numpy "Link to this heading")

================================================================================================================================================================

In this how-to you will learn how to:

*   Verify the existence of a bug in NumPy
    
*   Verify the fix, if any, made for the bug
    

While you walk through the verification process, you will learn how to:

*   Set up a Python virtual environment (using `virtualenv`)
    
*   Install appropriate versions of NumPy, first to see the bug in action, then to verify its fix
    

[Issue 16354](https://github.com/numpy/numpy/issues/16354)
 is used as an example.

This issue was:

> **Title**: _np.polymul return type is np.float64 or np.complex128 when given an all-zero argument_
> 
> _np.polymul returns an object with type np.float64 when one argument is all zero, and both arguments have type np.int64 or np.float32. Something similar happens with all zero np.complex64 giving result type np.complex128._
> 
> _This doesn’t happen with non-zero arguments; there the result is as expected._
> 
> _This bug isn’t present in np.convolve._
> 
> **Reproducing code example**:
> 
> \>>> import numpy as np
> \>>> np.\_\_version\_\_
> '1.18.4'
> \>>> a \= np.array(\[1,2,3\])
> \>>> z \= np.array(\[0,0,0\])
> \>>> np.polymul(a.astype(np.int64), a.astype(np.int64)).dtype
> dtype('int64')
> \>>> np.polymul(a.astype(np.int64), z.astype(np.int64)).dtype
> dtype('float64')
> \>>> np.polymul(a.astype(np.float32), z.astype(np.float32)).dtype
> dtype('float64')
> \>>> np.polymul(a.astype(np.complex64), z.astype(np.complex64)).dtype
> dtype('complex128')
> Numpy/Python version information:
> \>>> import sys, numpy; print(numpy.\_\_version\_\_, sys.version)
> 1.18.4 3.7.5 (default, Nov  7 2019, 10:50:52) \[GCC 8.3.0\]
> 
> Copy to clipboard

1\. Set up a virtual environment[#](https://numpy.org/doc/stable/user/how-to-verify-bug.html#set-up-a-virtual-environment "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

Create a new directory, enter into it, and set up a virtual environment using your preferred method. For example, this is how to do it using `virtualenv` on linux or macOS:

virtualenv venv\_np\_bug
source venv\_np\_bug/bin/activate

Copy to clipboard

This ensures the system/global/default Python/NumPy installation will not be altered.

2\. Install the NumPy version in which the bug was reported[#](https://numpy.org/doc/stable/user/how-to-verify-bug.html#install-the-numpy-version-in-which-the-bug-was-reported "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The report references NumPy version 1.18.4, so that is the version you need to install in this case.

Since this bug is tied to a release and not a specific commit, a pre-built wheel installed in your virtual environment via `pip` will suffice:

pip install numpy\==1.18.4

Copy to clipboard

Some bugs may require you to build the NumPy version referenced in the issue report. To learn how to do that, visit [Building from source](https://numpy.org/doc/stable/building/index.html#building-from-source)
.

3\. Reproduce the bug[#](https://numpy.org/doc/stable/user/how-to-verify-bug.html#reproduce-the-bug "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

The issue reported in [#16354](https://github.com/numpy/numpy/issues/16354)
 is that the wrong `dtype` is returned if one of the inputs of the method [`numpy.polymul`](https://numpy.org/doc/stable/reference/generated/numpy.polymul.html#numpy.polymul "numpy.polymul")
 is a zero array.

To reproduce the bug, start a Python terminal, enter the code snippet shown in the bug report, and ensure that the results match those in the issue:

\>>> import numpy as np
\>>> np.\_\_version\_\_
'...' # 1.18.4
\>>> a \= np.array(\[1,2,3\])
\>>> z \= np.array(\[0,0,0\])
\>>> np.polymul(a.astype(np.int64), a.astype(np.int64)).dtype
dtype('int64')
\>>> np.polymul(a.astype(np.int64), z.astype(np.int64)).dtype
dtype('...') # float64
\>>> np.polymul(a.astype(np.float32), z.astype(np.float32)).dtype
dtype('...') # float64
\>>> np.polymul(a.astype(np.complex64), z.astype(np.complex64)).dtype
dtype('...') # complex128

Copy to clipboard

As reported, whenever the zero array, `z` in the example above, is one of the arguments to [`numpy.polymul`](https://numpy.org/doc/stable/reference/generated/numpy.polymul.html#numpy.polymul "numpy.polymul")
, an incorrect `dtype` is returned.

4\. Check for fixes in the latest version of NumPy[#](https://numpy.org/doc/stable/user/how-to-verify-bug.html#check-for-fixes-in-the-latest-version-of-numpy "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If the issue report for your bug has not yet been resolved, further action or patches need to be submitted.

In this case, however, the issue was resolved by [PR 17577](https://github.com/numpy/numpy/pull/17577)
 and is now closed. So you can try to verify the fix.

To verify the fix:

1.  Uninstall the version of NumPy in which the bug still exists:
    
    pip uninstall numpy
    
    Copy to clipboard
    
2.  Install the latest version of NumPy:
    
    pip install numpy
    
    Copy to clipboard
    
3.  In your Python terminal, run the reported code snippet you used to verify the existence of the bug and confirm that the issue has been resolved:
    
    \>>> import numpy as np
    \>>> np.\_\_version\_\_
    '...' # 1.18.4
    \>>> a \= np.array(\[1,2,3\])
    \>>> z \= np.array(\[0,0,0\])
    \>>> np.polymul(a.astype(np.int64), a.astype(np.int64)).dtype
    dtype('int64')
    \>>> np.polymul(a.astype(np.int64), z.astype(np.int64)).dtype
    dtype('int64')
    \>>> np.polymul(a.astype(np.float32), z.astype(np.float32)).dtype
    dtype('float32')
    \>>> np.polymul(a.astype(np.complex64), z.astype(np.complex64)).dtype
    dtype('complex64')
    
    Copy to clipboard
    

Note that the correct `dtype` is now returned even when a zero array is one of the arguments to [`numpy.polymul`](https://numpy.org/doc/stable/reference/generated/numpy.polymul.html#numpy.polymul "numpy.polymul")
.

5\. Support NumPy development by verifying and fixing bugs[#](https://numpy.org/doc/stable/user/how-to-verify-bug.html#support-numpy-development-by-verifying-and-fixing-bugs "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Go to the [NumPy GitHub issues page](https://github.com/numpy/numpy/issues)
 and see if you can confirm the existence of any other bugs which have not been confirmed yet. In particular, it is useful for the developers to know if a bug can be reproduced on a newer version of NumPy.

Comments verifying the existence of bugs alert the NumPy developers that more than one user can reproduce the issue.

On this page