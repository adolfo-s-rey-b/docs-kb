[Skip to main content](https://numpy.org/doc/stable/f2py/windows/intel.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

F2PY and Windows Intel Fortran[#](https://numpy.org/doc/stable/f2py/windows/intel.html#f2py-and-windows-intel-fortran "Link to this heading")

==============================================================================================================================================

As of NumPy 1.23, only the classic Intel compilers (`ifort`) are supported.

Note

The licensing restrictions for beta software [have been relaxed](https://www.intel.com/content/www/us/en/developer/articles/release-notes/oneapi-fortran-compiler-release-notes.html)
 during the transition to the LLVM backed `ifx/icc` family of compilers. However this document does not endorse the usage of Intel in downstream projects due to the issues pertaining to [disassembly of components and liability](https://www.intel.com/content/www/us/en/developer/articles/license/end-user-license-agreement.html)
.

Neither the Python Intel installation nor the _Classic Intel C/C++ Compiler_ are required.

*   The [Intel Fortran Compilers](https://www.intel.com/content/www/us/en/developer/articles/tool/oneapi-standalone-components.html#inpage-nav-6-1)
     come in a combined installer providing both Classic and Beta versions; these also take around a gigabyte and a half or so.
    

We will consider the classic example of the generation of Fibonnaci numbers, `fib1.f`, given by:

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

For `cmd.exe` fans, using the Intel oneAPI command prompt is the easiest approach, as it loads the required environment for both `ifort` and `msvc`. Helper batch scripts are also provided.

\# cmd.exe
"C:\\Program Files (x86)\\Intel\\oneAPI\\setvars.bat"
python -m numpy.f2py -c fib1.f -m fib1
python -c "import fib1; import numpy as np; a=np.zeros(8); fib1.fib(a); print(a)"

Copy to clipboard

Powershell usage is a little less pleasant, and this configuration now works with MSVC as:

\# Powershell
python \-m numpy.f2py \-c fib1.f \-m fib1 \-\-f77exec\='C:\\Program Files (x86)\\Intel\\oneAPI\\compiler\\latest\\windows\\bin\\intel64\\ifort.exe' \-\-f90exec\='C:\\Program Files (x86)\\Intel\\oneAPI\\compiler\\latest\\windows\\bin\\intel64\\ifort.exe' \-L'C:\\Program Files (x86)\\Intel\\oneAPI\\compiler\\latest\\windows\\compiler\\lib\\ia32'
python \-c "import fib1; import numpy as np; a=np.zeros(8); fib1.fib(a); print(a)"
\# Alternatively, set environment and reload Powershell in one line
cmd.exe /k '"C:\\Program Files (x86)\\Intel\\oneAPI\\setvars.bat" && powershell'
python \-m numpy.f2py \-c fib1.f \-m fib1
python \-c "import fib1; import numpy as np; a=np.zeros(8); fib1.fib(a); print(a)"

Copy to clipboard

Note that the actual path to your local installation of _ifort_ may vary, and the command above will need to be updated accordingly.