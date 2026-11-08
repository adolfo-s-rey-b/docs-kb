[Skip to main content](https://numpy.org/doc/stable/f2py/f2py.getting-started.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/f2py/f2py.getting-started.html)
[2.5 (stable)](https://numpy.org/doc/stable/f2py/f2py.getting-started.html)
[2.4](https://numpy.org/doc/2.4/f2py/f2py.getting-started.html)
[2.3](https://numpy.org/doc/2.3/f2py/f2py.getting-started.html)
[2.2](https://numpy.org/doc/2.2/f2py/f2py.getting-started.html)
[2.1](https://numpy.org/doc/2.1/f2py/f2py.getting-started.html)
[2.0](https://numpy.org/doc/2.0/f2py/f2py.getting-started.html)
[1.26](https://numpy.org/doc/1.26/f2py/f2py.getting-started.html)
[1.25](https://numpy.org/doc/1.25/f2py/f2py.getting-started.html)
[1.24](https://numpy.org/doc/1.24/f2py/f2py.getting-started.html)
[1.23](https://numpy.org/doc/1.23/f2py/f2py.getting-started.html)
[1.22](https://numpy.org/doc/1.22/f2py/f2py.getting-started.html)
[1.21](https://numpy.org/doc/1.21/f2py/f2py.getting-started.html)
[1.20](https://numpy.org/doc/1.20/f2py/f2py.getting-started.html)
[1.19](https://numpy.org/doc/1.19/f2py/f2py.getting-started.html)
[1.18](https://numpy.org/doc/1.18/f2py/f2py.getting-started.html)
[1.17](https://numpy.org/doc/1.17/f2py/f2py.getting-started.html)
[1.16](https://numpy.org/doc/1.16/f2py/f2py.getting-started.html)
[1.15](https://numpy.org/doc/1.15/f2py/f2py.getting-started.html)
[1.14](https://numpy.org/doc/1.14/f2py/f2py.getting-started.html)
[1.13](https://numpy.org/doc/1.13/f2py/f2py.getting-started.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Three ways to wrap - getting started[#](https://numpy.org/doc/stable/f2py/f2py.getting-started.html#three-ways-to-wrap-getting-started "Link to this heading")

===============================================================================================================================================================

Wrapping Fortran or C functions to Python using F2PY consists of the following steps:

*   Creating the so-called [signature file](https://numpy.org/doc/stable/f2py/signature-file.html)
     that contains descriptions of wrappers to Fortran or C functions, also called the signatures of the functions. For Fortran routines, F2PY can create an initial signature file by scanning Fortran source codes and tracking all relevant information needed to create wrapper functions.
    
    *   Optionally, F2PY-created signature files can be edited to optimize wrapper functions, which can make them “smarter” and more “Pythonic”.
        
*   F2PY reads a signature file and writes a Python C/API module containing Fortran/C/Python bindings.
    
*   F2PY compiles all sources and builds an extension module containing the wrappers.
    
    *   In building the extension modules, F2PY uses `meson`. For different build systems, see [F2PY and build systems](https://numpy.org/doc/stable/f2py/buildtools/index.html#f2py-bldsys)
        .
        

Note

*   Depending on your operating system, you may need to install the Python development headers (which provide the file `Python.h`) separately. In Linux Debian-based distributions this package should be called `python3-dev`, in Fedora-based distributions it is `python3-devel`. For macOS, depending how Python was installed, your mileage may vary. In Windows, the headers are typically installed already, see [F2PY and Windows](https://numpy.org/doc/stable/f2py/windows/index.html#f2py-windows)
    .
    

Note

F2PY supports all the operating systems SciPy is tested on so their [system dependencies panel](https://scipy.github.io/devdocs/building/index.html#system-level-dependencies)
 is a good reference.

Depending on the situation, these steps can be carried out in a single composite command or step-by-step; in which case some steps can be omitted or combined with others.

Below, we describe three typical approaches of using F2PY with Fortran 77. These can be read in order of increasing effort, but also cater to different access levels depending on whether the Fortran code can be freely modified.

The following example Fortran 77 code will be used for illustration, save it as `fib1.f`:

C FILE: FIB1.F
      SUBROUTINE FIB(A,N)
C
C     CALCULATE FIRST N FIBONACCI NUMBERS
C
      INTEGER N
      REAL\*8 A(N)
      DO I\=1,N
         IF (I.EQ.1) THEN
            A(I) \= 0.0D0
         ELSEIF (I.EQ.2) THEN
            A(I) \= 1.0D0
         ELSE 
            A(I) \= A(I\-1) + A(I\-2)
         ENDIF
      ENDDO
      END
C END FILE FIB1.F

Copy to clipboard

Note

F2PY parses Fortran/C signatures to build wrapper functions to be used with Python. However, it is not a compiler, and does not check for additional errors in source code, nor does it implement the entire language standards. Some errors may pass silently (or as warnings) and need to be verified by the user.

The quick way[#](https://numpy.org/doc/stable/f2py/f2py.getting-started.html#the-quick-way "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

The quickest way to wrap the Fortran subroutine `FIB` for use in Python is to run

python \-m numpy.f2py \-c fib1.f \-m fib1

Copy to clipboard

or, alternatively, if the `f2py` command-line tool is available,

f2py \-c fib1.f \-m fib1

Copy to clipboard

Note

Because the `f2py` command might not be available in all system, notably on Windows, we will use the `python -m numpy.f2py` command throughout this guide.

This command compiles and wraps `fib1.f` (`-c`) to create the extension module `fib1.so` (`-m`) in the current directory. A list of command line options can be seen by executing `python -m numpy.f2py`. Now, in Python the Fortran subroutine `FIB` is accessible via `fib1.fib`:

\>>> import numpy as np
\>>> import fib1
\>>> print(fib1.fib.\_\_doc\_\_)
fib(a,\[n\])

Wrapper for \`\`fib\`\`.

Parameters
\----------
a : input rank-1 array('d') with bounds (n)

Other parameters
\----------------
n : input int, optional
    Default: len(a)

\>>> a \= np.zeros(8, 'd')
\>>> fib1.fib(a)
\>>> print(a)
\[  0.   1.   1.   2.   3.   5.   8.  13.\]

Copy to clipboard

Note

*   Note that F2PY recognized that the second argument `n` is the dimension of the first array argument `a`. Since by default all arguments are input-only arguments, F2PY concludes that `n` can be optional with the default value `len(a)`.
    
*   One can use different values for optional `n`:
    
    \>>> a1 \= np.zeros(8, 'd')
    \>>> fib1.fib(a1, 6)
    \>>> print(a1)
    \[ 0.  1.  1.  2.  3.  5.  0.  0.\]
    
    Copy to clipboard
    
    but an exception is raised when it is incompatible with the input array `a`:
    
    \>>> fib1.fib(a, 10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    fib.error: (len(a)>=n) failed for 1st keyword n: fib:n=10
    \>>>
    
    Copy to clipboard
    
    F2PY implements basic compatibility checks between related arguments in order to avoid unexpected crashes.
    
*   When a NumPy array that is [Fortran](https://numpy.org/doc/stable/glossary.html#term-Fortran-order)
     [contiguous](https://numpy.org/doc/stable/glossary.html#term-contiguous)
     and has a `dtype` corresponding to a presumed Fortran type is used as an input array argument, then its C pointer is directly passed to Fortran.
    
    Otherwise, F2PY makes a contiguous copy (with the proper `dtype`) of the input array and passes a C pointer of the copy to the Fortran subroutine. As a result, any possible changes to the (copy of) input array have no effect on the original argument, as demonstrated below:
    
    \>>> a \= np.ones(8, 'i')
    \>>> fib1.fib(a)
    \>>> print(a)
    \[1 1 1 1 1 1 1 1\]
    
    Copy to clipboard
    
    Clearly, this is unexpected, as Fortran typically passes by reference. That the above example worked with `dtype=float` is considered accidental.
    
    F2PY provides an `intent(inplace)` attribute that ensures that changes are copied back to the input argument. For example, if one specifies the `intent(inplace) a` directive (see [Attributes](https://numpy.org/doc/stable/f2py/signature-file.html#f2py-attributes)
     for details), then the example above would read:
    
    \>>> a \= np.ones(8, 'i')
    \>>> fib1.fib(a)
    \>>> print(a)
    \[  0.   1.   1.   2.   3.   5.   8.  13.\]
    
    Copy to clipboard
    
    However, the recommended way to have changes made by Fortran subroutine propagate to Python is to use the `intent(out)` attribute. That approach is more efficient and also cleaner.
    
*   The usage of `fib1.fib` in Python is very similar to using `FIB` in Fortran. However, using _in situ_ output arguments in Python is poor style, as there are no safety mechanisms in Python to protect against wrong argument types. When using Fortran or C, compilers discover any type mismatches during the compilation process, but in Python the types must be checked at runtime. Consequently, using _in situ_ output arguments in Python may lead to difficult to find bugs, not to mention the fact that the codes will be less readable when all required type checks are implemented.
    

Though the approach to wrapping Fortran routines for Python discussed so far is very straightforward, it has several drawbacks (see the comments above). The drawbacks are due to the fact that there is no way for F2PY to determine the actual intention of the arguments; that is, there is ambiguity in distinguishing between input and output arguments. Consequently, F2PY assumes that all arguments are input arguments by default.

There are ways (see below) to remove this ambiguity by “teaching” F2PY about the true intentions of function arguments, and F2PY is then able to generate more explicit, easier to use, and less error prone wrappers for Fortran functions.

The smart way[#](https://numpy.org/doc/stable/f2py/f2py.getting-started.html#the-smart-way "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

If we want to have more control over how F2PY will treat the interface to our Fortran code, we can apply the wrapping steps one by one.

*   First, we create a signature file from `fib1.f` by running:
    
    python \-m numpy.f2py fib1.f \-m fib2 \-h fib1.pyf
    
    Copy to clipboard
    
    The signature file is saved to `fib1.pyf` (see the `-h` flag) and its contents are shown below.
    
    !    -\*- f90 -\*-
    python module fib2 ! in 
        interface  ! in :fib2
            subroutine fib(a,n) ! in :fib2:fib1.f
                real\*8 dimension(n) :: a
                integer optional,check(len(a)\>=n),depend(a) :: n\=len(a)
            end subroutine fib
        end interface 
    end python module fib2
    
    ! This file was auto-generated with f2py (version:2.28.198-1366).
    ! See http://cens.ioc.ee/projects/f2py2e/
    
    Copy to clipboard
    
*   Next, we’ll teach F2PY that the argument `n` is an input argument (using the `intent(in)` attribute) and that the result, i.e., the contents of `a` after calling the Fortran function `FIB`, should be returned to Python (using the `intent(out)` attribute). In addition, an array `a` should be created dynamically using the size determined by the input argument `n` (using the `depend(n)` attribute to indicate this dependence relation).
    
    The contents of a suitably modified version of `fib1.pyf` (saved as `fib2.pyf`) are as follows:
    
    !    -\*- f90 -\*-
    python module fib2 
        interface
            subroutine fib(a,n)
                real\*8 dimension(n),intent(out),depend(n) :: a
                integer intent(in) :: n
            end subroutine fib
        end interface 
    end python module fib2
    
    Copy to clipboard
    
*   Finally, we build the extension module by running:
    
    python \-m numpy.f2py \-c fib2.pyf fib1.f
    
    Copy to clipboard
    

In Python:

\>>> import fib2
\>>> print(fib2.fib.\_\_doc\_\_)
a = fib(n)

Wrapper for \`\`fib\`\`.

Parameters
\----------
n : input int

Returns
\-------
a : rank-1 array('d') with bounds (n)

\>>> print(fib2.fib(8))
\[  0.   1.   1.   2.   3.   5.   8.  13.\]

Copy to clipboard

Note

*   The signature of `fib2.fib` now more closely corresponds to the intention of the Fortran subroutine `FIB`: given the number `n`, `fib2.fib` returns the first `n` Fibonacci numbers as a NumPy array. The new Python signature `fib2.fib` also rules out the unexpected behaviour in `fib1.fib`.
    
*   Note that by default, using a single `intent(out)` also implies `intent(hide)`. Arguments that have the `intent(hide)` attribute specified will not be listed in the argument list of a wrapper function.
    

For more details, see [Signature file](https://numpy.org/doc/stable/f2py/signature-file.html)
.

The quick and smart way[#](https://numpy.org/doc/stable/f2py/f2py.getting-started.html#the-quick-and-smart-way "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

The “smart way” of wrapping Fortran functions, as explained above, is suitable for wrapping (e.g. third party) Fortran codes for which modifications to their source codes are not desirable nor even possible.

However, if editing Fortran codes is acceptable, then the generation of an intermediate signature file can be skipped in most cases. F2PY specific attributes can be inserted directly into Fortran source codes using F2PY directives. A F2PY directive consists of special comment lines (starting with `Cf2py` or `!f2py`, for example) which are ignored by Fortran compilers but interpreted by F2PY as normal lines.

Consider a modified version of the previous Fortran code with F2PY directives, saved as `fib3.f`:

C FILE: FIB3.F
      SUBROUTINE FIB(A,N)
C
C     CALCULATE FIRST N FIBONACCI NUMBERS
C
      INTEGER N
      REAL\*8 A(N)
Cf2py intent(in) n
Cf2py intent(out) a
Cf2py depend(n) a
      DO I\=1,N
         IF (I.EQ.1) THEN
            A(I) \= 0.0D0
         ELSEIF (I.EQ.2) THEN
            A(I) \= 1.0D0
         ELSE 
            A(I) \= A(I\-1) + A(I\-2)
         ENDIF
      ENDDO
      END
C END FILE FIB3.F

Copy to clipboard

Building the extension module can be now carried out in one command:

python \-m numpy.f2py \-c \-m fib3 fib3.f

Copy to clipboard

Notice that the resulting wrapper to `FIB` is as “smart” (unambiguous) as in the previous case:

\>>> import fib3
\>>> print(fib3.fib.\_\_doc\_\_)
a = fib(n)

Wrapper for \`\`fib\`\`.

Parameters
\----------
n : input int

Returns
\-------
a : rank-1 array('d') with bounds (n)

\>>> print(fib3.fib(8))
\[  0.   1.   1.   2.   3.   5.   8.  13.\]

Copy to clipboard

On this page