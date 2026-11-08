[Skip to main content](https://numpy.org/doc/stable/user/c-info.ufunc-tutorial.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/user/c-info.ufunc-tutorial.html)
[2.5 (stable)](https://numpy.org/doc/stable/user/c-info.ufunc-tutorial.html)
[2.4](https://numpy.org/doc/2.4/user/c-info.ufunc-tutorial.html)
[2.3](https://numpy.org/doc/2.3/user/c-info.ufunc-tutorial.html)
[2.2](https://numpy.org/doc/2.2/user/c-info.ufunc-tutorial.html)
[2.1](https://numpy.org/doc/2.1/user/c-info.ufunc-tutorial.html)
[2.0](https://numpy.org/doc/2.0/user/c-info.ufunc-tutorial.html)
[1.26](https://numpy.org/doc/1.26/user/c-info.ufunc-tutorial.html)
[1.25](https://numpy.org/doc/1.25/user/c-info.ufunc-tutorial.html)
[1.24](https://numpy.org/doc/1.24/user/c-info.ufunc-tutorial.html)
[1.23](https://numpy.org/doc/1.23/user/c-info.ufunc-tutorial.html)
[1.22](https://numpy.org/doc/1.22/user/c-info.ufunc-tutorial.html)
[1.21](https://numpy.org/doc/1.21/user/c-info.ufunc-tutorial.html)
[1.20](https://numpy.org/doc/1.20/user/c-info.ufunc-tutorial.html)
[1.19](https://numpy.org/doc/1.19/user/c-info.ufunc-tutorial.html)
[1.18](https://numpy.org/doc/1.18/user/c-info.ufunc-tutorial.html)
[1.17](https://numpy.org/doc/1.17/user/c-info.ufunc-tutorial.html)
[1.16](https://numpy.org/doc/1.16/user/c-info.ufunc-tutorial.html)
[1.15](https://numpy.org/doc/1.15/user/c-info.ufunc-tutorial.html)
[1.14](https://numpy.org/doc/1.14/user/c-info.ufunc-tutorial.html)
[1.13](https://numpy.org/doc/1.13/user/c-info.ufunc-tutorial.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Writing your own ufunc[#](https://numpy.org/doc/stable/user/c-info.ufunc-tutorial.html#writing-your-own-ufunc "Link to this heading")

======================================================================================================================================

I have the Power!

— _He-Man_

Creating a new universal function[#](https://numpy.org/doc/stable/user/c-info.ufunc-tutorial.html#creating-a-new-universal-function "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

Before reading this, it may help to familiarize yourself with the basics of C extensions for Python by reading/skimming the tutorials in Section 1 of [Extending and Embedding the Python Interpreter](https://docs.python.org/extending/index.html)
 and in [How to extend NumPy](https://numpy.org/doc/stable/user/c-info.how-to-extend.html)

The umath module is a computer-generated C-module that creates many ufuncs. It provides a great many examples of how to create a universal function. Creating your own ufunc that will make use of the ufunc machinery is not difficult either. Suppose you have a function that you want to operate element-by-element over its inputs. By creating a new ufunc you will obtain a function that handles

*   broadcasting
    
*   N-dimensional looping
    
*   automatic type-conversions with minimal memory usage
    
*   optional output arrays
    

It is not difficult to create your own ufunc. All that is required is a 1-d loop for each data-type you want to support. Each 1-d loop must have a specific signature, and only ufuncs for fixed-size data-types can be used. The function call used to create a new ufunc to work on built-in data-types is given below. A different mechanism is used to register ufuncs for user-defined data-types.

In the next several sections we give example code that can be easily modified to create your own ufuncs. The examples are successively more complete or complicated versions of the logit function, a common function in statistical modeling. Logit is also interesting because, due to the magic of IEEE standards (specifically IEEE 754), all of the logit functions created below automatically have the following behavior.

\>>> logit(0)
\-inf
\>>> logit(1)
inf
\>>> logit(2)
nan
\>>> logit(\-2)
nan

Copy to clipboard

This is wonderful because the function writer doesn’t have to manually propagate infs or nans.

Example non-ufunc extension[#](https://numpy.org/doc/stable/user/c-info.ufunc-tutorial.html#example-non-ufunc-extension "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

For comparison and general edification of the reader we provide a simple implementation of a C extension of `logit` that uses no numpy.

To do this we need three files. The first is the C file which contains the actual code, and the others are two project files that describe how to create the module.

> #define PY\_SSIZE\_T\_CLEAN
> #include <Python.h>
> #include <math.h>
> 
> /\*
>  \* spammodule.c
>  \* This is the C code for a non-numpy Python extension to
>  \* define the logit function, where logit(p) = log(p/(1-p)).
>  \* This function will not work on numpy arrays automatically.
>  \* numpy.vectorize must be called in python to generate
>  \* a numpy-friendly function.
>  \*
>  \* Details explaining the Python-C API can be found under
>  \* 'Extending and Embedding' and 'Python/C API' at
>  \* docs.python.org .
>  \*/
> 
> /\* This declares the logit function \*/
> static PyObject \*spam\_logit(PyObject \*self, PyObject \*args);
> 
> /\*
>  \* This tells Python what methods this module has.
>  \* See the Python-C API for more information.
>  \*/
> static PyMethodDef SpamMethods\[\] \= {
>     {"logit",
>         spam\_logit,
>         METH\_VARARGS, "compute logit"},
>     {NULL, NULL, 0, NULL}
> };
> 
> /\*
>  \* This actually defines the logit function for
>  \* input args from Python.
>  \*/
> 
> static PyObject \*spam\_logit(PyObject \*self, PyObject \*args)
> {
>     double p;
> 
>     /\* This parses the Python argument into a double \*/
>     if(!PyArg\_ParseTuple(args, "d", &p)) {
>         return NULL;
>     }
> 
>     /\* THE ACTUAL LOGIT FUNCTION \*/
>     p \= p/(1\-p);
>     p \= log(p);
> 
>     /\*This builds the answer back into a python object \*/
>     return Py\_BuildValue("d", p);
> }
> 
> /\* This initiates the module using the above definitions. \*/
> static struct PyModuleDef moduledef \= {
>     PyModuleDef\_HEAD\_INIT,
>     "spam",
>     NULL,
>     \-1,
>     SpamMethods,
>     NULL,
>     NULL,
>     NULL,
>     NULL
> };
> 
> PyMODINIT\_FUNC PyInit\_spam(void)
> {
>     PyObject \*m;
>     m \= PyModule\_Create(&moduledef);
>     if (!m) {
>         return NULL;
>     }
>     return m;
> }
> 
> Copy to clipboard

To create the module, one proceeds as one would for a Python package, creating a `pyproject.toml` file, which defines a build back-end, and then another file for that backend which describes how to compile the code. For the backend, we recommend `meson-python`, as we use it for numpy itself, but below we also show how to use the older `setuptools`.

 meson

Sample `pyproject.toml` and `meson.build`.

\[project\]
name \= "spam"
version \= "0.1"

\[build-system\]
requires \= \["meson-python"\]
build-backend \= "mesonpy"

Copy to clipboard

project('spam', 'c')

py \= import('python').find\_installation()

sources \= files('spammodule.c')

extension\_module \= py.extension\_module(
  'spam',
  sources,
  install: true,
)

Copy to clipboard

 setuptools

Sample `pyproject.toml` and `setup.py`.

\[project\]
name \= "spam"
version \= "0.1"

\[build-system\]
requires \= \["setuptools"\]
build-backend \= "setuptools.build\_meta"

Copy to clipboard

from setuptools import setup, Extension

spammodule \= Extension('spam', sources\=\['spammodule.c'\])

setup(name\='spam', version\='1.0',
      ext\_modules\=\[spammodule\])

Copy to clipboard

With either of the above, one can build and install the `spam` package with,

pip install .

Copy to clipboard

Once the `spam` module is imported into python, you can call logit via `spam.logit`. Note that the function used above cannot be applied as-is to numpy arrays. To do so we must call [`numpy.vectorize`](https://numpy.org/doc/stable/reference/generated/numpy.vectorize.html#numpy.vectorize "numpy.vectorize")
 on it. For example:

\>>> import numpy as np
\>>> import spam
\>>> spam.logit(0)
\-inf
\>>> spam.logit(1)
inf
\>>> spam.logit(0.5)
0.0
\>>> x \= np.linspace(0,1,10)
\>>> spam.logit(x)
TypeError: only length-1 arrays can be converted to Python scalars
\>>> f \= np.vectorize(spam.logit)
\>>> f(x)
array(\[       -inf, -2.07944154, -1.25276297, -0.69314718, -0.22314355,\
    0.22314355,  0.69314718,  1.25276297,  2.07944154,         inf\])

Copy to clipboard

THE RESULTING LOGIT FUNCTION IS NOT FAST! `numpy.vectorize` simply loops over `spam.logit`. The loop is done at the C level, but the numpy array is constantly being parsed and build back up. This is expensive. When the author compared `numpy.vectorize(spam.logit)` against the logit ufuncs constructed below, the logit ufuncs were almost exactly 4 times faster. Larger or smaller speedups are, of course, possible depending on the nature of the function.

Example NumPy ufunc for one dtype[#](https://numpy.org/doc/stable/user/c-info.ufunc-tutorial.html#example-numpy-ufunc-for-one-dtype "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

For simplicity we give a ufunc for a single dtype, the `'f8'` `double`. As in the previous section, we first give the `.c` file and then the files used to create a `npufunc` module containing the ufunc.

The place in the code corresponding to the actual computations for the ufunc are marked with `/* BEGIN main ufunc computation */` and `/* END main ufunc computation */`. The code in between those lines is the primary thing that must be changed to create your own ufunc.

> #define PY\_SSIZE\_T\_CLEAN
> #include <Python.h>
> #include "numpy/ndarraytypes.h"
> #include "numpy/ufuncobject.h"
> #include "numpy/npy\_3kcompat.h"
> #include <math.h>
> 
> /\*
>  \* single\_type\_logit.c
>  \* This is the C code for creating your own
>  \* NumPy ufunc for a logit function.
>  \*
>  \* In this code we only define the ufunc for
>  \* a single dtype. The computations that must
>  \* be replaced to create a ufunc for
>  \* a different function are marked with BEGIN
>  \* and END.
>  \*
>  \* Details explaining the Python-C API can be found under
>  \* 'Extending and Embedding' and 'Python/C API' at
>  \* docs.python.org .
>  \*/
> 
> static PyMethodDef LogitMethods\[\] \= {
>     {NULL, NULL, 0, NULL}
> };
> 
> /\* The loop definition must precede the PyMODINIT\_FUNC. \*/
> 
> static void double\_logit(char \*\*args, const npy\_intp \*dimensions,
>                          const npy\_intp \*steps, void \*data)
> {
>     npy\_intp i;
>     npy\_intp n \= dimensions\[0\];
>     char \*in \= args\[0\], \*out \= args\[1\];
>     npy\_intp in\_step \= steps\[0\], out\_step \= steps\[1\];
> 
>     double tmp;
> 
>     for (i \= 0; i < n; i++) {
>         /\* BEGIN main ufunc computation \*/
>         tmp \= \*(double \*)in;
>         tmp /= 1 \- tmp;
>         \*((double \*)out) \= log(tmp);
>         /\* END main ufunc computation \*/
> 
>         in += in\_step;
>         out += out\_step;
>     }
> }
> 
> /\* This a pointer to the above function \*/
> PyUFuncGenericFunction funcs\[1\] \= {&double\_logit};
> 
> /\* These are the input and return dtypes of logit.\*/
> static const char types\[2\] \= {NPY\_DOUBLE, NPY\_DOUBLE};
> 
> static struct PyModuleDef moduledef \= {
>     PyModuleDef\_HEAD\_INIT,
>     "npufunc",
>     NULL,
>     \-1,
>     LogitMethods,
>     NULL,
>     NULL,
>     NULL,
>     NULL
> };
> 
> PyMODINIT\_FUNC PyInit\_npufunc(void)
> {
>     PyObject \*m, \*logit, \*d;
> 
>     import\_array();
>     import\_umath();
> 
>     m \= PyModule\_Create(&moduledef);
>     if (!m) {
>         return NULL;
>     }
> 
>     logit \= PyUFunc\_FromFuncAndData(funcs, NULL, types, 1, 1, 1,
>                                     PyUFunc\_None, "logit",
>                                     "logit\_docstring", 0);
> 
>     d \= PyModule\_GetDict(m);
> 
>     PyDict\_SetItemString(d, "logit", logit);
>     Py\_DECREF(logit);
> 
>     return m;
> }
> 
> Copy to clipboard

For the files needed to create the module, the main difference from our previous example is that we now need to declare dependencies on numpy.

 meson

Sample `pyproject.toml` and `meson.build`.

\[project\]
name \= "npufunc"
dependencies \= \["numpy"\]
version \= "0.1"

\[build-system\]
requires \= \["meson-python", "numpy"\]
build-backend \= "mesonpy"

Copy to clipboard

project('npufunc', 'c')

py \= import('python').find\_installation()
np\_dep \= dependency('numpy')

sources \= files('single\_type\_logit.c')

extension\_module \= py.extension\_module(
  'npufunc',
  sources,
  dependencies: \[np\_dep\],
  install: true,
)

Copy to clipboard

 setuptools

Sample `pyproject.toml` and `setup.py`.

\[project\]
name \= "npufunc"
dependencies \= \["numpy"\]
version \= "0.1"

\[build-system\]
requires \= \["setuptools", "numpy"\]
build-backend \= "setuptools.build\_meta"

Copy to clipboard

from setuptools import setup, Extension
from numpy import get\_include

npufunc \= Extension('npufunc',
                    sources\=\['single\_type\_logit.c'\],
                    include\_dirs\=\[get\_include()\])

setup(name\='npufunc', version\='1.0', ext\_modules\=\[npufunc\])

Copy to clipboard

After the above has been installed, it can be imported and used as follows:

\>>> import numpy as np
\>>> import npufunc
\>>> npufunc.logit(0.5)
np.float64(0.0)
\>>> a \= np.linspace(0, 1, 5)
\>>> npufunc.logit(a)
array(\[       -inf, -1.09861229,  0.        ,  1.09861229,         inf\])

Copy to clipboard

Example NumPy ufunc with multiple dtypes[#](https://numpy.org/doc/stable/user/c-info.ufunc-tutorial.html#example-numpy-ufunc-with-multiple-dtypes "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We now extend the above to a full `logit` ufunc, with inner loops for floats, doubles, and long doubles. Here, we can use the same build files as above, except we need to change the source file from `single_type_logit.c` to `multi_type_logit.c`.

The places in the code corresponding to the actual computations for the ufunc are marked with `/* BEGIN main ufunc computation */` and `/* END main ufunc computation */`. The code in between those lines is the primary thing that must be changed to create your own ufunc.

> #define PY\_SSIZE\_T\_CLEAN
> #include <Python.h>
> #include "numpy/ndarraytypes.h"
> #include "numpy/ufuncobject.h"
> #include <math.h>
> 
> /\*
>  \* multi\_type\_logit.c
>  \* This is the C code for creating your own
>  \* NumPy ufunc for a logit function.
>  \*
>  \* Each function of the form type\_logit defines the
>  \* logit function for a different numpy dtype. Each
>  \* of these functions must be modified when you
>  \* create your own ufunc. The computations that must
>  \* be replaced to create a ufunc for
>  \* a different function are marked with BEGIN
>  \* and END.
>  \*
>  \* Details explaining the Python-C API can be found under
>  \* 'Extending and Embedding' and 'Python/C API' at
>  \* docs.python.org .
>  \*
>  \*/
> 
> static PyMethodDef LogitMethods\[\] \= {
>     {NULL, NULL, 0, NULL}
> };
> 
> /\* The loop definitions must precede the PyMODINIT\_FUNC. \*/
> 
> static void long\_double\_logit(char \*\*args, const npy\_intp \*dimensions,
>                               const npy\_intp \*steps, void \*data)
> {
>     npy\_intp i;
>     npy\_intp n \= dimensions\[0\];
>     char \*in \= args\[0\], \*out \= args\[1\];
>     npy\_intp in\_step \= steps\[0\], out\_step \= steps\[1\];
> 
>     long double tmp;
> 
>     for (i \= 0; i < n; i++) {
>         /\* BEGIN main ufunc computation \*/
>         tmp \= \*(long double \*)in;
>         tmp /= 1 \- tmp;
>         \*((long double \*)out) \= logl(tmp);
>         /\* END main ufunc computation \*/
> 
>         in += in\_step;
>         out += out\_step;
>     }
> }
> 
> static void double\_logit(char \*\*args, const npy\_intp \*dimensions,
>                          const npy\_intp \*steps, void \*data)
> {
>     npy\_intp i;
>     npy\_intp n \= dimensions\[0\];
>     char \*in \= args\[0\], \*out \= args\[1\];
>     npy\_intp in\_step \= steps\[0\], out\_step \= steps\[1\];
> 
>     double tmp;
> 
>     for (i \= 0; i < n; i++) {
>         /\* BEGIN main ufunc computation \*/
>         tmp \= \*(double \*)in;
>         tmp /= 1 \- tmp;
>         \*((double \*)out) \= log(tmp);
>         /\* END main ufunc computation \*/
> 
>         in += in\_step;
>         out += out\_step;
>     }
> }
> 
> static void float\_logit(char \*\*args, const npy\_intp \*dimensions,
>                        const npy\_intp \*steps, void \*data)
> {
>     npy\_intp i;
>     npy\_intp n \= dimensions\[0\];
>     char \*in \= args\[0\], \*out \= args\[1\];
>     npy\_intp in\_step \= steps\[0\], out\_step \= steps\[1\];
> 
>     float tmp;
> 
>     for (i \= 0; i < n; i++) {
>         /\* BEGIN main ufunc computation \*/
>         tmp \= \*(float \*)in;
>         tmp /= 1 \- tmp;
>         \*((float \*)out) \= logf(tmp);
>         /\* END main ufunc computation \*/
> 
>         in += in\_step;
>         out += out\_step;
>     }
> }
> 
> /\*This gives pointers to the above functions\*/
> PyUFuncGenericFunction funcs\[3\] \= {&float\_logit,
>                                    &double\_logit,
>                                    &long\_double\_logit};
> 
> static const char types\[6\] \= {NPY\_FLOAT, NPY\_FLOAT,
>                               NPY\_DOUBLE, NPY\_DOUBLE,
>                               NPY\_LONGDOUBLE, NPY\_LONGDOUBLE};
> 
> static struct PyModuleDef moduledef \= {
>     PyModuleDef\_HEAD\_INIT,
>     "npufunc",
>     NULL,
>     \-1,
>     LogitMethods,
>     NULL,
>     NULL,
>     NULL,
>     NULL
> };
> 
> PyMODINIT\_FUNC PyInit\_npufunc(void)
> {
>     PyObject \*m, \*logit, \*d;
> 
>     import\_array();
>     import\_umath();
> 
>     m \= PyModule\_Create(&moduledef);
>     if (!m) {
>         return NULL;
>     }
> 
>     logit \= PyUFunc\_FromFuncAndData(funcs, NULL, types, 4, 1, 1,
>                                     PyUFunc\_None, "logit",
>                                     "logit\_docstring", 0);
> 
>     d \= PyModule\_GetDict(m);
> 
>     PyDict\_SetItemString(d, "logit", logit);
>     Py\_DECREF(logit);
> 
>     return m;
> }
> 
> Copy to clipboard

After the above has been installed, it can be imported and used as follows.

\>>> import numpy as np
\>>> import npufunc
\>>> npufunc.logit(0.5)
np.float64(0.0)
\>>> a \= np.linspace(0, 1, 5, dtype\=np.float32)
\>>> npufunc.logit(a)
<python-input-4>:1: RuntimeWarning: divide by zero encountered in logit
array(\[      -inf, -1.0986123,  0.       ,  1.0986123,        inf\],
      dtype=float32)

Copy to clipboard

Note

Supporting `float16` (half-precision) in custom ufuncs is more complex due to its non-standard C representation and conversion requirements. The above code can process `float16` input, but will do so by converting it to `float32`. The result will then be `float32` too, but one can convert it back to `float16` by passing in a suitable output, as in `npufunc.logit(a, out=np.empty_like(a))`. For examples of actual `float16` loops, see the numpy source code.

Example NumPy ufunc with multiple arguments/return values[#](https://numpy.org/doc/stable/user/c-info.ufunc-tutorial.html#example-numpy-ufunc-with-multiple-arguments-return-values "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Creating a ufunc with multiple arguments is not difficult. Here, we make a modification of the code for a logit ufunc, where we compute `(A * B, logit(A * B))`. For simplicity, we only create a loop for doubles.

We again only give the C code as the files needed to create the module are the same as before, but with the source file name replaced by `multi_arg_logit.c`.

The C file is given below. The ufunc generated takes two arguments `A` and `B`. It returns a tuple whose first element is `A * B` and whose second element is `logit(A * B)`. Note that it automatically supports broadcasting, as well as all other properties of a ufunc.

> #define PY\_SSIZE\_T\_CLEAN
> #include <Python.h>
> #include "numpy/ndarraytypes.h"
> #include "numpy/ufuncobject.h"
> #include <math.h>
> 
> /\*
>  \* multi\_arg\_logit.c
>  \* This is the C code for creating your own
>  \* NumPy ufunc for a multiple argument, multiple
>  \* return value ufunc. The places where the
>  \* ufunc computation is carried out are marked
>  \* with comments.
>  \*
>  \* Details explaining the Python-C API can be found under
>  \* 'Extending and Embedding' and 'Python/C API' at
>  \* docs.python.org.
>  \*/
> 
> static PyMethodDef LogitMethods\[\] \= {
>     {NULL, NULL, 0, NULL}
> };
> 
> /\* The loop definition must precede the PyMODINIT\_FUNC. \*/
> 
> static void double\_logitprod(char \*\*args, const npy\_intp \*dimensions,
>                              const npy\_intp \*steps, void \*data)
> {
>     npy\_intp i;
>     npy\_intp n \= dimensions\[0\];
>     char \*in1 \= args\[0\], \*in2 \= args\[1\];
>     char \*out1 \= args\[2\], \*out2 \= args\[3\];
>     npy\_intp in1\_step \= steps\[0\], in2\_step \= steps\[1\];
>     npy\_intp out1\_step \= steps\[2\], out2\_step \= steps\[3\];
> 
>     double tmp;
> 
>     for (i \= 0; i < n; i++) {
>         /\* BEGIN main ufunc computation \*/
>         tmp \= \*(double \*)in1;
>         tmp \*= \*(double \*)in2;
>         \*((double \*)out1) \= tmp;
>         \*((double \*)out2) \= log(tmp / (1 \- tmp));
>         /\* END main ufunc computation \*/
> 
>         in1 += in1\_step;
>         in2 += in2\_step;
>         out1 += out1\_step;
>         out2 += out2\_step;
>     }
> }
> 
> /\*This a pointer to the above function\*/
> PyUFuncGenericFunction funcs\[1\] \= {&double\_logitprod};
> 
> /\* These are the input and return dtypes of logit.\*/
> 
> static const char types\[4\] \= {NPY\_DOUBLE, NPY\_DOUBLE,
>                               NPY\_DOUBLE, NPY\_DOUBLE};
> 
> static struct PyModuleDef moduledef \= {
>     PyModuleDef\_HEAD\_INIT,
>     "npufunc",
>     NULL,
>     \-1,
>     LogitMethods,
>     NULL,
>     NULL,
>     NULL,
>     NULL
> };
> 
> PyMODINIT\_FUNC PyInit\_npufunc(void)
> {
>     PyObject \*m, \*logit, \*d;
> 
>     import\_array();
>     import\_umath();
> 
>     m \= PyModule\_Create(&moduledef);
>     if (!m) {
>         return NULL;
>     }
> 
>     logit \= PyUFunc\_FromFuncAndData(funcs, NULL, types, 1, 2, 2,
>                                     PyUFunc\_None, "logit",
>                                     "logit\_docstring", 0);
> 
>     d \= PyModule\_GetDict(m);
> 
>     PyDict\_SetItemString(d, "logit", logit);
>     Py\_DECREF(logit);
> 
>     return m;
> }
> 
> Copy to clipboard

Example NumPy ufunc with structured array dtype arguments[#](https://numpy.org/doc/stable/user/c-info.ufunc-tutorial.html#example-numpy-ufunc-with-structured-array-dtype-arguments "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This example shows how to create a ufunc for a structured array dtype. For the example we show a trivial ufunc for adding two arrays with dtype `'u8,u8,u8'`. The process is a bit different from the other examples since a call to [`PyUFunc_FromFuncAndData`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_FromFuncAndData "PyUFunc_FromFuncAndData")
 cannot register ufuncs for custom dtypes and structured array dtypes. We need to also call [`PyUFunc_RegisterLoopForDescr`](https://numpy.org/doc/stable/reference/c-api/ufunc.html#c.PyUFunc_RegisterLoopForDescr "PyUFunc_RegisterLoopForDescr")
 to finish setting up the ufunc.

We only give the C code as the files needed to construct the module are again exactly the same as before, except that the source file is now `add_triplet.c`.

> #define PY\_SSIZE\_T\_CLEAN
> #include <Python.h>
> #include "numpy/ndarraytypes.h"
> #include "numpy/ufuncobject.h"
> #include "numpy/npy\_3kcompat.h"
> #include <math.h>
> 
> /\*
>  \* add\_triplet.c
>  \* This is the C code for creating your own
>  \* NumPy ufunc for a structured array dtype.
>  \*
>  \* Details explaining the Python-C API can be found under
>  \* 'Extending and Embedding' and 'Python/C API' at
>  \* docs.python.org.
>  \*/
> 
> static PyMethodDef StructUfuncTestMethods\[\] \= {
>     {NULL, NULL, 0, NULL}
> };
> 
> /\* The loop definition must precede the PyMODINIT\_FUNC. \*/
> 
> static void add\_uint64\_triplet(char \*\*args, const npy\_intp \*dimensions,
>                                const npy\_intp \*steps, void \*data)
> {
>     npy\_intp i;
>     npy\_intp is1 \= steps\[0\];
>     npy\_intp is2 \= steps\[1\];
>     npy\_intp os \= steps\[2\];
>     npy\_intp n \= dimensions\[0\];
>     uint64\_t \*x, \*y, \*z;
> 
>     char \*i1 \= args\[0\];
>     char \*i2 \= args\[1\];
>     char \*op \= args\[2\];
> 
>     for (i \= 0; i < n; i++) {
> 
>         x \= (uint64\_t \*)i1;
>         y \= (uint64\_t \*)i2;
>         z \= (uint64\_t \*)op;
> 
>         z\[0\] \= x\[0\] + y\[0\];
>         z\[1\] \= x\[1\] + y\[1\];
>         z\[2\] \= x\[2\] + y\[2\];
> 
>         i1 += is1;
>         i2 += is2;
>         op += os;
>     }
> }
> 
> static struct PyModuleDef moduledef \= {
>     PyModuleDef\_HEAD\_INIT,
>     "npufunc",
>     NULL,
>     \-1,
>     StructUfuncTestMethods,
>     NULL,
>     NULL,
>     NULL,
>     NULL
> };
> 
> PyMODINIT\_FUNC PyInit\_npufunc(void)
> {
>     PyObject \*m, \*add\_triplet, \*d;
>     PyObject \*dtype\_dict;
>     PyArray\_Descr \*dtype;
>     PyArray\_Descr \*dtypes\[3\];
> 
>     import\_array();
>     import\_umath();
> 
>     m \= PyModule\_Create(&moduledef);
>     if (m \== NULL) {
>         return NULL;
>     }
> 
>     /\* Create a new ufunc object \*/
>     add\_triplet \= PyUFunc\_FromFuncAndData(NULL, NULL, NULL, 0, 2, 1,
>                                           PyUFunc\_None, "add\_triplet",
>                                           "add\_triplet\_docstring", 0);
> 
>     dtype\_dict \= Py\_BuildValue("\[(s, s), (s, s), (s, s)\]",
>                                "f0", "u8", "f1", "u8", "f2", "u8");
>     PyArray\_DescrConverter(dtype\_dict, &dtype);
>     Py\_DECREF(dtype\_dict);
> 
>     dtypes\[0\] \= dtype;
>     dtypes\[1\] \= dtype;
>     dtypes\[2\] \= dtype;
> 
>     /\* Register ufunc for structured dtype \*/
>     PyUFunc\_RegisterLoopForDescr((PyUFuncObject \*)add\_triplet,
>                                  dtype,
>                                  &add\_uint64\_triplet,
>                                  dtypes,
>                                  NULL);
> 
>     d \= PyModule\_GetDict(m);
> 
>     PyDict\_SetItemString(d, "add\_triplet", add\_triplet);
>     Py\_DECREF(add\_triplet);
>     return m;
> }
> 
> Copy to clipboard

Sample usage:

\>>> import npufunc
\>>> import numpy as np
\>>> a \= np.array(\[(1, 2, 3), (4, 5, 6)\], "u8,u8,u8")
\>>> npufunc.add\_triplet(a, a)
array(\[(2,  4,  6), (8, 10, 12)\],
      dtype=\[('f0', '<u8'), ('f1', '<u8'), ('f2', '<u8')\])

Copy to clipboard

On this page