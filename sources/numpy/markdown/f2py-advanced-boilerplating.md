[Skip to main content](https://numpy.org/doc/stable/f2py/advanced/boilerplating.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/f2py/advanced/boilerplating.html)
[2.5 (stable)](https://numpy.org/doc/stable/f2py/advanced/boilerplating.html)
[2.4](https://numpy.org/doc/2.4/f2py/advanced/boilerplating.html)
[2.3](https://numpy.org/doc/2.3/f2py/advanced/boilerplating.html)
[2.2](https://numpy.org/doc/2.2/f2py/advanced/boilerplating.html)
[2.1](https://numpy.org/doc/2.1/f2py/advanced/boilerplating.html)
[2.0](https://numpy.org/doc/2.0/f2py/advanced/boilerplating.html)
[1.26](https://numpy.org/doc/1.26/f2py/advanced/boilerplating.html)
[1.25](https://numpy.org/doc/1.25/f2py/advanced/boilerplating.html)
[1.24](https://numpy.org/doc/1.24/f2py/advanced/boilerplating.html)
[1.23](https://numpy.org/doc/1.23/f2py/advanced/boilerplating.html)
[1.22](https://numpy.org/doc/1.22/f2py/advanced/boilerplating.html)
[1.21](https://numpy.org/doc/1.21/f2py/advanced/boilerplating.html)
[1.20](https://numpy.org/doc/1.20/f2py/advanced/boilerplating.html)
[1.19](https://numpy.org/doc/1.19/f2py/advanced/boilerplating.html)
[1.18](https://numpy.org/doc/1.18/f2py/advanced/boilerplating.html)
[1.17](https://numpy.org/doc/1.17/f2py/advanced/boilerplating.html)
[1.16](https://numpy.org/doc/1.16/f2py/advanced/boilerplating.html)
[1.15](https://numpy.org/doc/1.15/f2py/advanced/boilerplating.html)
[1.14](https://numpy.org/doc/1.14/f2py/advanced/boilerplating.html)
[1.13](https://numpy.org/doc/1.13/f2py/advanced/boilerplating.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Boilerplate reduction and templating[#](https://numpy.org/doc/stable/f2py/advanced/boilerplating.html#boilerplate-reduction-and-templating "Link to this heading")

===================================================================================================================================================================

Using FYPP for binding generic interfaces[#](https://numpy.org/doc/stable/f2py/advanced/boilerplating.html#using-fypp-for-binding-generic-interfaces "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`f2py` doesn’t currently support binding interface blocks. However, there are workarounds in use. Perhaps the best known is the usage of `tempita` for using `.pyf.src` files as is done in the bindings which [are part of scipy](https://github.com/scipy/scipy/blob/c93da6f46dbed8b3cc0ccd2495b5678f7b740a03/scipy/linalg/clapack.pyf.src)
. _tempita_ support has been removed and is no longer recommended in any case.

Note

The reason interfaces cannot be supported within `f2py` itself is because they don’t correspond to exported symbols in compiled libraries.

❯ nm gen.o
 0000000000000078 T \_\_add\_mod\_MOD\_add\_complex
 0000000000000000 T \_\_add\_mod\_MOD\_add\_complex\_dp
 0000000000000150 T \_\_add\_mod\_MOD\_add\_integer
 0000000000000124 T \_\_add\_mod\_MOD\_add\_real
 00000000000000ee T \_\_add\_mod\_MOD\_add\_real\_dp

Copy to clipboard

Here we will discuss a few techniques to leverage `f2py` in conjunction with [fypp](https://fypp.readthedocs.io/en/stable/fypp.html)
 to emulate generic interfaces and to ease the binding of multiple (similar) functions.

### Basic example: Addition module[#](https://numpy.org/doc/stable/f2py/advanced/boilerplating.html#basic-example-addition-module "Link to this heading")

Let us build on the example (from the user guide, [F2PY examples](https://numpy.org/doc/stable/f2py/f2py-examples.html#f2py-examples)
) of a subroutine which takes in two arrays and returns its sum.

C
      SUBROUTINE ZADD(A,B,C,N)
C
      DOUBLE COMPLEX A(\*)
      DOUBLE COMPLEX B(\*)
      DOUBLE COMPLEX C(\*)
      INTEGER N
      DO 20 J \= 1, N
         C(J) \= A(J)+B(J)
 20   CONTINUE
      END

Copy to clipboard

We will recast this into modern fortran:

module adder
    implicit none
contains

    subroutine zadd(a, b, c, n)
        integer, intent(in) :: n
        double complex, intent(in) :: a(n), b(n)
        double complex, intent(out) :: c(n)
        integer :: j
        do j \= 1, n
            c(j) \= a(j) + b(j)
        end do
    end subroutine zadd

end module adder

Copy to clipboard

We could go on as in the original example, adding intents by hand among other things, however in production often there are other concerns. For one, we can template via FYPP the construction of similar functions:

module adder
    implicit none
contains

#:def add\_subroutine(dtype\_prefix, dtype)
    subroutine ${dtype\_prefix}$add(a, b, c, n)
        integer, intent(in) :: n
        ${dtype}$, intent(in) :: a(n), b(n)
        ${dtype}$ :: c(n)
        integer :: j
        do j = 1, n
            c(j) = a(j) + b(j)
        end do
    end subroutine ${dtype\_prefix}$add

#:enddef

#:for dtype\_prefix, dtype in \[('i', 'integer'), ('s', 'real'), ('d', 'real(kind=8)'), ('c', 'complex'), ('z', 'double complex')\]
    @:add\_subroutine(${dtype\_prefix}$, ${dtype}$)
#:endfor

end module adder

Copy to clipboard

This can be pre-processed to generate the full fortran code:

❯ fypp gen\_adder.f90.fypp \> adder.f90

Copy to clipboard

As to be expected, this can be wrapped by `f2py` subsequently.

Now we will consider maintaining the bindings in a separate file. Note the following basic `.pyf` which can be generated for a single subroutine via `f2py -m adder adder_base.f90 -h adder.pyf`:

!    -\*- f90 -\*-
! Note: the context of this file is case sensitive.

python module adder ! in
    interface  ! in :adder
        module adder ! in :adder:adder\_base.f90
            subroutine zadd(a,b,c,n) ! in :adder:adder\_base.f90:adder
                double complex dimension(n),intent(in) :: a
                double complex dimension(n),intent(in),depend(n) :: b
                double complex dimension(n),intent(out),depend(n) :: c
                integer, optional,intent(in),check(shape(a, 0) \== n),depend(a) :: n\=shape(a, 0)
            end subroutine zadd
        end module adder
    end interface
end python module adder

! This file was auto-generated with f2py (version:2.0.0.dev0+git20240101.bab7280).
! See:
! https://web.archive.org/web/20140822061353/http://cens.ioc.ee/projects/f2py2e

Copy to clipboard

With the docstring:

c = zadd(a,b,\[n\])

Wrapper for \`\`zadd\`\`.

Parameters
\----------
a : input rank-1 array('D') with bounds (n)
b : input rank-1 array('D') with bounds (n)

Other Parameters
\----------------
n : input int, optional
    Default: shape(a, 0)

Returns
\-------
c : rank-1 array('D') with bounds (n)

Copy to clipboard

Which is already pretty good. However, `n` should never be passed in the first place so we will make some minor adjustments.

!    -\*- f90 -\*-
! Note: the context of this file is case sensitive.

python module adder ! in
    interface  ! in :adder
        module adder ! in :adder:adder\_base.f90
            subroutine zadd(a,b,c,n) ! in :adder:adder\_base.f90:adder
                integer intent(hide),depend(a) :: n\=len(a)
                double complex dimension(n),intent(in) :: a
                double complex dimension(n),intent(in),depend(n) :: b
                double complex dimension(n),intent(out),depend(n) :: c
            end subroutine zadd
        end module adder
    end interface
end python module adder

! This file was auto-generated with f2py (version:2.0.0.dev0+git20240101.bab7280).
! See:
! https://numpy.org/doc/stable/f2py/

Copy to clipboard

Which corresponds to:

In \[3\]: ?adder.adder.zadd
Call signature: adder.adder.zadd(\*args, \*\*kwargs)
Type:           fortran
String form:    <fortran function zadd>
Docstring:
c = zadd(a,b)

Wrapper for \`\`zadd\`\`.

Parameters
\----------
a : input rank-1 array('D') with bounds (n)
b : input rank-1 array('D') with bounds (n)

Returns
\-------
c : rank-1 array('D') with bounds (n)

Copy to clipboard

Finally, we can template over this in a similar manner, to attain the original goal of having bindings which make use of `f2py` directives and have minimal spurious repetition.

!    -\*- f90 -\*-
! Note: the context of this file is case sensitive.

python module adder ! in
    interface  ! in :adder
        module adder ! in :adder:adder\_base.f90
#:def add\_subroutine(dtype\_prefix, dtype)
            subroutine ${dtype\_prefix}$add(a,b,c,n) ! in :adder:adder\_base.f90:adder
                integer intent(hide),depend(a) :: n=len(a)
                ${dtype}$ dimension(n),intent(in) :: a
                ${dtype}$ dimension(n),intent(in),depend(n) :: b
                ${dtype}$ dimension(n),intent(out),depend(n) :: c
            end subroutine ${dtype\_prefix}$add

#:enddef

#:for dtype\_prefix, dtype in \[('i', 'integer'), ('s', 'real'), ('d', 'real(kind=8)'), ('c', 'complex'), ('z', 'complex(kind=8)')\]
    @:add\_subroutine(${dtype\_prefix}$, ${dtype}$)
#:endfor
        end module adder
    end interface
end python module adder

! This file was auto-generated with f2py (version:2.0.0.dev0+git20240101.bab7280).
! See:
! https://numpy.org/doc/stable/f2py/

Copy to clipboard

Usage boils down to:

fypp gen\_adder.f90.fypp \> adder.f90
fypp adder.pyf.fypp \> adder.pyf
f2py \-m adder \-c adder.pyf adder.f90 \--backend meson

Copy to clipboard

On this page