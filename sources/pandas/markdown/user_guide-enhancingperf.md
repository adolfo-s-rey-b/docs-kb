[Skip to main content](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/user_guide/enhancingperf.html)
[3.1 (stable)](https://pandas.pydata.org/docs/user_guide/enhancingperf.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/user_guide/enhancingperf.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/user_guide/enhancingperf.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/user_guide/enhancingperf.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/user_guide/enhancingperf.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/enhancingperf.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/user_guide/enhancingperf.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/user_guide/enhancingperf.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/user_guide/enhancingperf.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/user_guide/enhancingperf.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/user_guide/enhancingperf.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/user_guide/enhancingperf.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Enhancing performance[#](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#enhancing-performance "Link to this heading")

====================================================================================================================================

In this part of the tutorial, we will investigate how to speed up certain functions operating on pandas [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 using Cython, Numba and [`pandas.eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
. Generally, using Cython and Numba can offer a larger speedup than using [`pandas.eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
 but will require a lot more code.

Note

In addition to following the steps in this tutorial, users interested in enhancing performance are highly encouraged to install the [recommended dependencies](https://pandas.pydata.org/docs/getting_started/install.html#install-recommended-dependencies)
 for pandas. These dependencies are often not installed by default, but will offer speed improvements if present.

Cython (writing C extensions for pandas)[#](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#cython-writing-c-extensions-for-pandas "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For many use cases writing pandas in pure Python and NumPy is sufficient. In some computationally heavy applications however, it can be possible to achieve sizable speed-ups by offloading work to [cython](https://cython.org/)
.

This tutorial assumes you have refactored as much as possible in Python, for example by trying to remove for-loops and making use of NumPy vectorization. It’s always worth optimising in Python first.

This tutorial walks through a “typical” process of cythonizing a slow computation. We use an [example from the Cython documentation](https://docs.cython.org/en/latest/src/quickstart/cythonize.html)
 but in the context of pandas. Our final cythonized solution is around 100 times faster than the pure Python solution.

### Pure Python[#](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#pure-python "Link to this heading")

We have a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 to which we want to apply a function row-wise.

In \[1\]: df \= pd.DataFrame(
   ...:    {
   ...:        "a": np.random.randn(1000),
   ...:        "b": np.random.randn(1000),
   ...:        "N": np.random.randint(100, 1000, (1000), dtype\="int64"),
   ...:        "x": "x",
   ...:    }
   ...: )
   ...: 

In \[2\]: df
Out\[2\]: 
            a         b    N  x
0    0.469112 -0.218470  585  x
1   -0.282863 -0.061645  841  x
2   -1.509059 -0.723780  251  x
3   -1.135632  0.551225  972  x
4    1.212112 -0.497767  181  x
..        ...       ...  ... ..
995 -1.512743  0.874737  374  x
996  0.933753  1.120790  246  x
997 -0.308013  0.198768  157  x
998 -0.079915  1.757555  977  x
999 -1.010589 -1.115680  770  x

\[1000 rows x 4 columns\]

Copy to clipboard

Here’s the function in pure Python:

In \[3\]: def f(x):
   ...:    return x \* (x \- 1)
   ...: 

In \[4\]: def integrate\_f(a, b, N):
   ...:    s \= 0
   ...:    dx \= (b \- a) / N
   ...:    for i in range(N):
   ...:        s += f(a + i \* dx)
   ...:    return s \* dx
   ...: 

Copy to clipboard

We achieve our result by using [`DataFrame.apply()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply "pandas.DataFrame.apply")
 (row-wise):

In \[5\]: %timeit df.apply(lambda x: integrate\_f(x\["a"\], x\["b"\], x\["N"\]), axis=1)
50.9 ms +- 116 us per loop (mean +- std. dev. of 7 runs, 10 loops each)

Copy to clipboard

Let’s take a look and see where the time is spent during this operation using the [prun ipython magic function](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-prun)
:

\# most time consuming 4 calls
In \[6\]: %prun -l 4 df.apply(lambda x: integrate\_f(x\['a'\], x\['b'\], x\['N'\]), axis=1)
         617888 function calls (617863 primitive calls) in 0.150 seconds

   Ordered by: internal time
   List reduced from 173 to 4 due to restriction <4>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1000    0.083    0.000    0.126    0.000 <ipython-input-4-c2a74e076cf0>:1(integrate\_f)
   552423    0.043    0.000    0.043    0.000 <ipython-input-3-c138bdd570e3>:1(f)
     3000    0.003    0.000    0.016    0.000 series.py:1088(\_\_getitem\_\_)
    19098    0.002    0.000    0.003    0.000 {built-in method builtins.isinstance}

Copy to clipboard

By far the majority of time is spend inside either `integrate_f` or `f`, hence we’ll concentrate our efforts cythonizing these two functions.

### Plain Cython[#](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#plain-cython "Link to this heading")

First we’re going to need to import the Cython magic function to IPython:

In \[7\]: %load\_ext Cython

Copy to clipboard

Now, let’s simply copy our functions over to Cython:

In \[8\]: %%cython
   ...: def f\_plain(x):
   ...:    return x \* (x - 1)
   ...: def integrate\_f\_plain(a, b, N):
   ...:    s = 0
   ...:    dx = (b - a) / N
   ...:    for i in range(N):
   ...:        s += f\_plain(a + i \* dx)
   ...:    return s \* dx
   ...: 

Copy to clipboard

In \[9\]: %timeit df.apply(lambda x: integrate\_f\_plain(x\["a"\], x\["b"\], x\["N"\]), axis=1)
43.9 ms +- 195 us per loop (mean +- std. dev. of 7 runs, 10 loops each)

Copy to clipboard

This has improved the performance compared to the pure Python approach by one-third.

### Declaring C types[#](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#declaring-c-types "Link to this heading")

We can annotate the function variables and return types as well as use `cdef` and `cpdef` to improve performance:

In \[10\]: %%cython
   ....: cdef double f\_typed(double x) except? -2:
   ....:    return x \* (x - 1)
   ....: cpdef double integrate\_f\_typed(double a, double b, int N):
   ....:    cdef int i
   ....:    cdef double s, dx
   ....:    s = 0
   ....:    dx = (b - a) / N
   ....:    for i in range(N):
   ....:        s += f\_typed(a + i \* dx)
   ....:    return s \* dx
   ....: 

Copy to clipboard

In \[11\]: %timeit df.apply(lambda x: integrate\_f\_typed(x\["a"\], x\["b"\], x\["N"\]), axis=1)
7.08 ms +- 23.3 us per loop (mean +- std. dev. of 7 runs, 100 loops each)

Copy to clipboard

Annotating the functions with C types yields an over ten times performance improvement compared to the original Python implementation.

### Using ndarray[#](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#using-ndarray "Link to this heading")

When re-profiling, time is spent creating a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 from each row, and calling `__getitem__` from both the index and the series (three times for each row). These Python function calls are expensive and can be improved by passing an `np.ndarray`.

In \[12\]: %prun -l 4 df.apply(lambda x: integrate\_f\_typed(x\['a'\], x\['b'\], x\['N'\]), axis=1)
         64465 function calls (64440 primitive calls) in 0.023 seconds

   Ordered by: internal time
   List reduced from 171 to 4 due to restriction <4>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     3000    0.003    0.000    0.016    0.000 series.py:1088(\_\_getitem\_\_)
    19098    0.002    0.000    0.003    0.000 {built-in method builtins.isinstance}
     3000    0.002    0.000    0.008    0.000 series.py:1172(\_get\_value)
     3000    0.002    0.000    0.002    0.000 base.py:3771(get\_loc)

Copy to clipboard

In \[13\]: %%cython
   ....: cimport numpy as np
   ....: import numpy as np
   ....: np.import\_array()
   ....: cdef double f\_typed(double x) except? -2:
   ....:    return x \* (x - 1)
   ....: cpdef double integrate\_f\_typed(double a, double b, int N):
   ....:    cdef int i
   ....:    cdef double s, dx
   ....:    s = 0
   ....:    dx = (b - a) / N
   ....:    for i in range(N):
   ....:        s += f\_typed(a + i \* dx)
   ....:    return s \* dx
   ....: cpdef np.ndarray\[double\] apply\_integrate\_f(np.ndarray col\_a, np.ndarray col\_b,
   ....:                                           np.ndarray col\_N):
   ....:    assert (col\_a.dtype == np.float64
   ....:            and col\_b.dtype == np.float64 and col\_N.dtype == np.dtype(int))
   ....:    cdef Py\_ssize\_t i, n = len(col\_N)
   ....:    assert (len(col\_a) == len(col\_b) == n)
   ....:    cdef np.ndarray\[double\] res = np.empty(n)
   ....:    for i in range(len(col\_a)):
   ....:        res\[i\] = integrate\_f\_typed(col\_a\[i\], col\_b\[i\], col\_N\[i\])
   ....:    return res
   ....: 

Copy to clipboard

This implementation creates an array of zeros and inserts the result of `integrate_f_typed` applied over each row. Looping over an `ndarray` is faster in Cython than looping over a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 object.

Since `apply_integrate_f` is typed to accept an `np.ndarray`, [`Series.to_numpy()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "pandas.Series.to_numpy")
 calls are needed to utilize this function.

In \[14\]: %timeit apply\_integrate\_f(df\['a'\].to\_numpy(), df\['b'\].to\_numpy(), df\['N'\].to\_numpy())
776 us +- 2.83 us per loop (mean +- std. dev. of 7 runs, 1,000 loops each)

Copy to clipboard

Performance has improved from the prior implementation by almost ten times.

### Disabling compiler directives[#](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#disabling-compiler-directives "Link to this heading")

The majority of the time is now spent in `apply_integrate_f`. Disabling Cython’s `boundscheck` and `wraparound` checks can yield more performance.

In \[15\]: %prun -l 4 apply\_integrate\_f(df\['a'\].to\_numpy(), df\['b'\].to\_numpy(), df\['N'\].to\_numpy())
         195 function calls in 0.001 seconds

   Ordered by: internal time
   List reduced from 48 to 4 due to restriction <4>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '\_lsprof.Profiler' objects}
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        3    0.000    0.000    0.000    0.000 array.py:1046(\_\_getitem\_\_)

Copy to clipboard

In \[16\]: %%cython
   ....: cimport cython
   ....: cimport numpy as np
   ....: import numpy as np
   ....: np.import\_array()
   ....: cdef np.float64\_t f\_typed(np.float64\_t x) except? -2:
   ....:    return x \* (x - 1)
   ....: cpdef np.float64\_t integrate\_f\_typed(np.float64\_t a, np.float64\_t b, np.int64\_t N):
   ....:    cdef np.int64\_t i
   ....:    cdef np.float64\_t s = 0.0, dx
   ....:    dx = (b - a) / N
   ....:    for i in range(N):
   ....:        s += f\_typed(a + i \* dx)
   ....:    return s \* dx
   ....: @cython.boundscheck(False)
   ....: @cython.wraparound(False)
   ....: cpdef np.ndarray\[np.float64\_t\] apply\_integrate\_f\_wrap(
   ....:    np.ndarray\[np.float64\_t\] col\_a,
   ....:    np.ndarray\[np.float64\_t\] col\_b,
   ....:    np.ndarray\[np.int64\_t\] col\_N
   ....: ):
   ....:    cdef np.int64\_t i, n = len(col\_N)
   ....:    assert len(col\_a) == len(col\_b) == n
   ....:    cdef np.ndarray\[np.float64\_t\] res = np.empty(n, dtype=np.float64)
   ....:    for i in range(n):
   ....:        res\[i\] = integrate\_f\_typed(col\_a\[i\], col\_b\[i\], col\_N\[i\])
   ....:    return res
   ....: 

Copy to clipboard

In \[17\]: %timeit apply\_integrate\_f\_wrap(df\['a'\].to\_numpy(), df\['b'\].to\_numpy(), df\['N'\].to\_numpy())
671 us +- 8.02 us per loop (mean +- std. dev. of 7 runs, 1,000 loops each)

Copy to clipboard

However, a loop indexer `i` accessing an invalid location in an array would cause a segfault because memory access isn’t checked. For more about `boundscheck` and `wraparound`, see the Cython docs on [compiler directives](https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#compiler-directives)
.

Numba (JIT compilation)[#](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#numba-jit-compilation "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

An alternative to statically compiling Cython code is to use a dynamic just-in-time (JIT) compiler with [Numba](https://numba.pydata.org/)
.

Numba allows you to write a pure Python function which can be JIT compiled to native machine instructions, similar in performance to C, C++ and Fortran, by decorating your function with `@jit`.

Numba works by generating optimized machine code using the LLVM compiler infrastructure at import time, runtime, or statically (using the included pycc tool). Numba supports compilation of Python to run on either CPU or GPU hardware and is designed to integrate with the Python scientific software stack.

Note

The `@jit` compilation will add overhead to the runtime of the function, so performance benefits may not be realized especially when using small data sets. Consider [caching](https://numba.readthedocs.io/en/stable/developer/caching.html)
 your function to avoid compilation overhead each time your function is run.

Numba can be used in 2 ways with pandas:

1.  Specify the `engine="numba"` keyword in select pandas methods
    
2.  Define your own Python function decorated with `@jit` and pass the underlying NumPy array of [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
     or [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
     (using [`Series.to_numpy()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "pandas.Series.to_numpy")
    ) into the function
    

### pandas Numba Engine[#](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#pandas-numba-engine "Link to this heading")

If Numba is installed, one can specify `engine="numba"` in select pandas methods to execute the method using Numba. Methods that support `engine="numba"` will also have an `engine_kwargs` keyword that accepts a dictionary that allows one to specify `"nogil"` and `"parallel"` keys with boolean values to pass into the `@jit` decorator. If `engine_kwargs` is not specified, it defaults to `{"nogil": False, "parallel": False}` unless otherwise specified.

Note

In terms of performance, **the first time a function is run using the Numba engine will be slow** as Numba will have some function compilation overhead. However, the JIT compiled functions are cached, and subsequent calls will be fast. In general, the Numba engine is performant with a larger amount of data points (e.g. 1+ million).

In \[1\]: data \= pd.Series(range(1\_000\_000))  \# noqa: E225

In \[2\]: roll \= data.rolling(10)

In \[3\]: def f(x):
   ...:    return np.sum(x) + 5
\# Run the first time, compilation time will affect performance
In \[4\]: %timeit -r 1 -n 1 roll.apply(f, engine='numba', raw=True)
1.23 s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)
\# Function is cached and performance will improve
In \[5\]: %timeit roll.apply(f, engine='numba', raw=True)
188 ms ± 1.93 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

In \[6\]: %timeit roll.apply(f, engine='cython', raw=True)
3.92 s ± 59 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

Copy to clipboard

If your compute hardware contains multiple CPUs, the largest performance gain can be realized by setting `parallel` to `True` to leverage more than 1 CPU. Internally, pandas leverages numba to parallelize computations over the columns of a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
; therefore, this performance benefit is only beneficial for a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 with a large number of columns.

In \[1\]: import numba

In \[2\]: numba.set\_num\_threads(1)

In \[3\]: df \= pd.DataFrame(np.random.randn(10\_000, 100))

In \[4\]: roll \= df.rolling(100)

In \[5\]: %timeit roll.mean(engine="numba", engine\_kwargs={"parallel": True})
347 ms ± 26 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In \[6\]: numba.set\_num\_threads(2)

In \[7\]: %timeit roll.mean(engine="numba", engine\_kwargs={"parallel": True})
201 ms ± 2.97 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

Copy to clipboard

### Custom Function Examples[#](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#custom-function-examples "Link to this heading")

A custom Python function decorated with `@jit` can be used with pandas objects by passing their NumPy array representations with [`Series.to_numpy()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "pandas.Series.to_numpy")
.

import numba

@numba.jit
def f\_plain(x):
    return x \* (x \- 1)

@numba.jit
def integrate\_f\_numba(a, b, N):
    s \= 0
    dx \= (b \- a) / N
    for i in range(N):
        s += f\_plain(a + i \* dx)
    return s \* dx

@numba.jit
def apply\_integrate\_f\_numba(col\_a, col\_b, col\_N):
    n \= len(col\_N)
    result \= np.empty(n, dtype\="float64")
    assert len(col\_a) \== len(col\_b) \== n
    for i in range(n):
        result\[i\] \= integrate\_f\_numba(col\_a\[i\], col\_b\[i\], col\_N\[i\])
    return result

def compute\_numba(df):
    result \= apply\_integrate\_f\_numba(
        df\["a"\].to\_numpy(), df\["b"\].to\_numpy(), df\["N"\].to\_numpy()
    )
    return pd.Series(result, index\=df.index, name\="result")

Copy to clipboard

In \[4\]: %timeit compute\_numba(df)
1000 loops, best of 3: 798 us per loop

Copy to clipboard

In this example, using Numba was faster than Cython.

Numba can also be used to write vectorized functions that do not require the user to explicitly loop over the observations of a vector; a vectorized function will be applied to each row automatically. Consider the following example of doubling each observation:

import numba

def double\_every\_value\_nonumba(x):
    return x \* 2

@numba.vectorize
def double\_every\_value\_withnumba(x):  \# noqa E501
    return x \* 2

Copy to clipboard

\# Custom function without numba
In \[5\]: %timeit df\["col1\_doubled"\] = df\["a"\].apply(double\_every\_value\_nonumba)  # noqa E501
1000 loops, best of 3: 797 us per loop

\# Standard implementation (faster than a custom function)
In \[6\]: %timeit df\["col1\_doubled"\] = df\["a"\] \* 2
1000 loops, best of 3: 233 us per loop

\# Custom function with numba
In \[7\]: %timeit df\["col1\_doubled"\] = double\_every\_value\_withnumba(df\["a"\].to\_numpy())
1000 loops, best of 3: 145 us per loop

Copy to clipboard

### Caveats[#](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#caveats "Link to this heading")

Numba is best at accelerating functions that apply numerical functions to NumPy arrays. If you try to `@jit` a function that contains unsupported [Python](https://numba.readthedocs.io/en/stable/reference/pysupported.html)
 or [NumPy](https://numba.readthedocs.io/en/stable/reference/numpysupported.html)
 code, compilation will revert [object mode](https://numba.readthedocs.io/en/stable/glossary.html#term-object-mode)
 which will mostly likely not speed up your function. For more on troubleshooting Numba modes, see the [Numba troubleshooting page](https://numba.readthedocs.io/en/stable/user/troubleshoot.html)
.

Using `parallel=True` (e.g. `@jit(parallel=True)`) may result in a `SIGABRT` if the threading layer leads to unsafe behavior. You can first [specify a safe threading layer](https://numba.readthedocs.io/en/stable/user/threading-layer.html#selecting-a-threading-layer-for-safe-parallel-execution)
 before running a JIT function with `parallel=True`.

Generally if the you encounter a segfault (`SIGSEGV`) while using Numba, please report the issue to the [Numba issue tracker.](https://github.com/numba/numba/issues/new/choose)

Expression evaluation via [`eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
[#](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#expression-evaluation-via-eval "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The top-level function [`pandas.eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
 implements expression evaluation of [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 and [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
. Expression evaluation allows operations to be expressed as strings and can potentially provide a performance improvement by evaluating arithmetic and boolean expressions all at once for large [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 with sufficiently complex expressions.

Note

You should not use [`eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
 for simple expressions or for expressions involving small DataFrames. In fact, [`eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
 is many orders of magnitude slower for smaller expressions or objects than plain Python. A good rule of thumb is to only use [`eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
 when you have a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 with more than 100,000 rows **and** an expression that involves multiple operations. For simple expressions (e.g., a single comparison or arithmetic operation), [`eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
 adds overhead and will be slower regardless of [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 size.

### Supported syntax[#](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#supported-syntax "Link to this heading")

These operations are supported by [`pandas.eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
:

*   Arithmetic operations except for the left shift (`<<`) and right shift (`>>`) operators, e.g., `df + 2 * pi / s ** 4 % 42 - the_golden_ratio`
    
*   Comparison operations, including chained comparisons, e.g., `2 < df < df2`
    
*   Boolean operations, e.g., `df < df2 and df3 < df4 or not df_bool`
    
*   `list` and `tuple` literals, e.g., `[1, 2]` or `(1, 2)`
    
*   Attribute access, e.g., `df.a`
    
*   Subscript expressions, e.g., `df[0]`
    
*   Simple variable evaluation, e.g., `pd.eval("df")` (this is not very useful)
    
*   Math functions: `sin`, `cos`, `exp`, `log`, `expm1`, `log1p`, `sqrt`, `sinh`, `cosh`, `tanh`, `arcsin`, `arccos`, `arctan`, `arccosh`, `arcsinh`, `arctanh`, `abs`, `arctan2` and `log10`.
    

The following Python syntax is **not** allowed:

*   Expressions
    
    > *   Function calls other than math functions.
    >     
    > *   `is`/`is not` operations
    >     
    > *   `if` expressions
    >     
    > *   `lambda` expressions
    >     
    > *   `list`/`set`/`dict` comprehensions
    >     
    > *   Literal `dict` and `set` expressions
    >     
    > *   `yield` expressions
    >     
    > *   Generator expressions
    >     
    > *   Boolean expressions consisting of only scalar values
    >     
    
*   Statements
    
    > *   Neither [simple](https://docs.python.org/3/reference/simple_stmts.html)
    >      or [compound](https://docs.python.org/3/reference/compound_stmts.html)
    >      statements are allowed. This includes `for`, `while`, and `if`.
    >     
    

### Local variables[#](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#local-variables "Link to this heading")

You must _explicitly reference_ any local variable that you want to use in an expression by placing the `@` character in front of the name. This mechanism is the same for both [`DataFrame.query()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query "pandas.DataFrame.query")
 and [`DataFrame.eval()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eval.html#pandas.DataFrame.eval "pandas.DataFrame.eval")
. For example,

In \[18\]: df \= pd.DataFrame(np.random.randn(5, 2), columns\=list("ab"))

In \[19\]: newcol \= np.random.randn(len(df))

In \[20\]: df.eval("b + @newcol")
Out\[20\]: 
0   -0.206122
1   -1.029587
2    0.519726
3   -2.052589
4    1.453210
Name: b, dtype: float64

In \[21\]: df.query("b < @newcol")
Out\[21\]: 
          a         b
1  0.160268 -0.848896
3  0.333758 -1.180355
4  0.572182  0.439895

Copy to clipboard

If you don’t prefix the local variable with `@`, pandas will raise an exception telling you the variable is undefined.

When using [`DataFrame.eval()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eval.html#pandas.DataFrame.eval "pandas.DataFrame.eval")
 and [`DataFrame.query()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query "pandas.DataFrame.query")
, this allows you to have a local variable and a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 column with the same name in an expression.

In \[22\]: a \= np.random.randn()

In \[23\]: df.query("@a < a")
Out\[23\]: 
          a         b
0  0.473349  0.891236
1  0.160268 -0.848896
2  0.803311  1.662031
3  0.333758 -1.180355
4  0.572182  0.439895

In \[24\]: df.loc\[a < df\["a"\]\]  \# same as the previous expression
Out\[24\]: 
          a         b
0  0.473349  0.891236
1  0.160268 -0.848896
2  0.803311  1.662031
3  0.333758 -1.180355
4  0.572182  0.439895

Copy to clipboard

Warning

[`pandas.eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
 will raise an exception if you cannot use the `@` prefix because it isn’t defined in that context.

In \[25\]: a, b \= 1, 2

In \[26\]: pd.eval("@a + b")
Traceback (most recent call last):

  File ~/work/pandas/pandas/.pixi/envs/docs-and-web/lib/python3.12/site-packages/IPython/core/interactiveshell.py:3823 in run\_code
    exec(code\_obj, self.user\_global\_ns, self.user\_ns)

  Cell In\[26\], line 1
    pd.eval("@a + b")

  File ~/work/pandas/pandas/pandas/core/computation/eval.py:405 in eval
    \_check\_for\_locals(expr, level, parser)

  File ~/work/pandas/pandas/pandas/core/computation/eval.py:197 in \_check\_for\_locals
    raise SyntaxError(msg)

  File <string>
    
SyntaxError: The '@' prefix is not allowed in top-level eval calls.
please refer to your variables by name without the '@' prefix.

Copy to clipboard

In this case, you should simply refer to the variables like you would in standard Python.

In \[27\]: pd.eval("a + b")
Out\[27\]: np.int64(3)

Copy to clipboard

### [`pandas.eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
 parsers[#](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#pandas-eval-parsers "Link to this heading")

There are two different expression syntax parsers.

The default `'pandas'` parser allows a more intuitive syntax for expressing query-like operations (comparisons, conjunctions and disjunctions). In particular, the precedence of the `&` and `|` operators is made equal to the precedence of the corresponding boolean operations `and` and `or`.

For example, the above conjunction can be written without parentheses. Alternatively, you can use the `'python'` parser to enforce strict Python semantics.

In \[28\]: nrows, ncols \= 20000, 100

In \[29\]: df1, df2, df3, df4 \= \[pd.DataFrame(np.random.randn(nrows, ncols)) for \_ in range(4)\]

In \[30\]: expr \= "(df1 > 0) & (df2 > 0) & (df3 > 0) & (df4 > 0)"

In \[31\]: x \= pd.eval(expr, parser\="python")

In \[32\]: expr\_no\_parens \= "df1 > 0 & df2 > 0 & df3 > 0 & df4 > 0"

In \[33\]: y \= pd.eval(expr\_no\_parens, parser\="pandas")

In \[34\]: np.all(x \== y)
Out\[34\]: np.True\_

Copy to clipboard

The same expression can be “anded” together with the word [`and`](https://docs.python.org/3/reference/expressions.html#and "(in Python v3.15)")
 as well:

In \[35\]: expr \= "(df1 > 0) & (df2 > 0) & (df3 > 0) & (df4 > 0)"

In \[36\]: x \= pd.eval(expr, parser\="python")

In \[37\]: expr\_with\_ands \= "df1 > 0 and df2 > 0 and df3 > 0 and df4 > 0"

In \[38\]: y \= pd.eval(expr\_with\_ands, parser\="pandas")

In \[39\]: np.all(x \== y)
Out\[39\]: np.True\_

Copy to clipboard

The [`and`](https://docs.python.org/3/reference/expressions.html#and "(in Python v3.15)")
 and [`or`](https://docs.python.org/3/reference/expressions.html#or "(in Python v3.15)")
 operators here have the same precedence that they would in Python.

### [`pandas.eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
 engines[#](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#pandas-eval-engines "Link to this heading")

There are two different expression engines.

The `'numexpr'` engine is the more performant engine that can yield performance improvements compared to standard Python syntax for large [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
. This engine requires the optional dependency `numexpr` to be installed.

The `'python'` engine is generally _not_ useful except for testing other evaluation engines against it. You will achieve **no** performance benefits using [`eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
 with `engine='python'` and may incur a performance hit.

In \[40\]: %timeit df1 + df2 + df3 + df4
7.49 ms +- 195 us per loop (mean +- std. dev. of 7 runs, 100 loops each)

Copy to clipboard

In \[41\]: %timeit pd.eval("df1 + df2 + df3 + df4", engine="python")
8.15 ms +- 91.1 us per loop (mean +- std. dev. of 7 runs, 100 loops each)

Copy to clipboard

### The [`DataFrame.eval()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eval.html#pandas.DataFrame.eval "pandas.DataFrame.eval")
 method[#](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#the-dataframe-eval-method "Link to this heading")

In addition to the top level [`pandas.eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
 function you can also evaluate an expression in the “context” of a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
.

In \[42\]: df \= pd.DataFrame(np.random.randn(5, 2), columns\=\["a", "b"\])

In \[43\]: df.eval("a + b")
Out\[43\]: 
0   -0.161099
1    0.805452
2    0.747447
3    1.189042
4   -2.057490
dtype: float64

Copy to clipboard

Any expression that is a valid [`pandas.eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
 expression is also a valid [`DataFrame.eval()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eval.html#pandas.DataFrame.eval "pandas.DataFrame.eval")
 expression, with the added benefit that you don’t have to prefix the name of the [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 to the column(s) you’re interested in evaluating.

In addition, you can perform assignment of columns within an expression. This allows for _formulaic evaluation_. The assignment target can be a new column name or an existing column name, and it must be a valid Python identifier.

In \[44\]: df \= pd.DataFrame(dict(a\=range(5), b\=range(5, 10)))

In \[45\]: df \= df.eval("c = a + b")

In \[46\]: df \= df.eval("d = a + b + c")

In \[47\]: df \= df.eval("a = 1")

In \[48\]: df
Out\[48\]: 
   a  b   c   d
0  1  5   5  10
1  1  6   7  14
2  1  7   9  18
3  1  8  11  22
4  1  9  13  26

Copy to clipboard

A copy of the [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 with the new or modified columns is returned, and the original frame is unchanged.

In \[49\]: df
Out\[49\]: 
   a  b   c   d
0  1  5   5  10
1  1  6   7  14
2  1  7   9  18
3  1  8  11  22
4  1  9  13  26

In \[50\]: df.eval("e = a - c")
Out\[50\]: 
   a  b   c   d   e
0  1  5   5  10  -4
1  1  6   7  14  -6
2  1  7   9  18  -8
3  1  8  11  22 -10
4  1  9  13  26 -12

In \[51\]: df
Out\[51\]: 
   a  b   c   d
0  1  5   5  10
1  1  6   7  14
2  1  7   9  18
3  1  8  11  22
4  1  9  13  26

Copy to clipboard

Multiple column assignments can be performed by using a multi-line string.

In \[52\]: df.eval(
   ....:"""
   ....: c = a + b
   ....: d = a + b + c
   ....: a = 1""",
   ....: )
   ....: 
Out\[52\]: 
   a  b   c   d
0  1  5   6  12
1  1  6   7  14
2  1  7   8  16
3  1  8   9  18
4  1  9  10  20

Copy to clipboard

The equivalent in standard Python would be

In \[53\]: df \= pd.DataFrame(dict(a\=range(5), b\=range(5, 10)))

In \[54\]: df\["c"\] \= df\["a"\] + df\["b"\]

In \[55\]: df\["d"\] \= df\["a"\] + df\["b"\] + df\["c"\]

In \[56\]: df\["a"\] \= 1

In \[57\]: df
Out\[57\]: 
   a  b   c   d
0  1  5   5  10
1  1  6   7  14
2  1  7   9  18
3  1  8  11  22
4  1  9  13  26

Copy to clipboard

### [`eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
 performance comparison[#](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#eval-performance-comparison "Link to this heading")

[`pandas.eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
 works well with expressions containing large arrays.

In \[58\]: nrows, ncols \= 20000, 100

In \[59\]: df1, df2, df3, df4 \= \[pd.DataFrame(np.random.randn(nrows, ncols)) for \_ in range(4)\]

Copy to clipboard

[`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 arithmetic:

In \[60\]: %timeit df1 + df2 + df3 + df4
3.5 ms +- 60 us per loop (mean +- std. dev. of 7 runs, 100 loops each)

Copy to clipboard

In \[61\]: %timeit pd.eval("df1 + df2 + df3 + df4")
4.39 ms +- 89 us per loop (mean +- std. dev. of 7 runs, 100 loops each)

Copy to clipboard

[`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 comparison:

In \[62\]: %timeit (df1 > 0) & (df2 > 0) & (df3 > 0) & (df4 > 0)
5.4 ms +- 22.3 us per loop (mean +- std. dev. of 7 runs, 100 loops each)

Copy to clipboard

In \[63\]: %timeit pd.eval("(df1 > 0) & (df2 > 0) & (df3 > 0) & (df4 > 0)")
8.97 ms +- 31.6 us per loop (mean +- std. dev. of 7 runs, 100 loops each)

Copy to clipboard

[`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 arithmetic with unaligned axes.

In \[64\]: s \= pd.Series(np.random.randn(50))

In \[65\]: %timeit df1 + df2 + df3 + df4 + s
5.02 ms +- 120 us per loop (mean +- std. dev. of 7 runs, 100 loops each)

Copy to clipboard

In \[66\]: %timeit pd.eval("df1 + df2 + df3 + df4 + s")
5.69 ms +- 90 us per loop (mean +- std. dev. of 7 runs, 100 loops each)

Copy to clipboard

Note

Operations such as

1 and 2  \# would parse to 1 & 2, but should evaluate to 2
3 or 4  \# would parse to 3 | 4, but should evaluate to 3
~1  \# this is okay, but slower when using eval

Copy to clipboard

should be performed in Python. An exception will be raised if you try to perform any boolean/bitwise operations with scalar operands that are not of type `bool` or `np.bool_`.

Here is a plot showing the running time of [`pandas.eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
 as function of the size of the frame involved in the computation. The two lines are two different engines.

![../_images/eval-perf.png](https://pandas.pydata.org/docs/_images/eval-perf.png)

You will only see the performance benefits of using the `numexpr` engine with [`pandas.eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
 if your [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 has more than approximately 100,000 rows. Even then, the benefit depends on expression complexity: the more operations in the expression, the greater the potential speedup. For simple expressions (e.g., `df["a"] + df["b"]`), standard Python/NumPy operations will be faster regardless of [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 size because [`eval()`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")
 has parsing and compilation overhead that outweighs any benefit from `numexpr`.

This plot was created using a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 with 3 columns each containing floating point values generated using `numpy.random.randn()` and the expression `a + b * (c ** 2 + b ** 2 - a) / (a * c) ** 3`.

### Expression evaluation limitations with `numexpr`[#](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#expression-evaluation-limitations-with-numexpr "Link to this heading")

Expressions that would result in an object dtype or involve datetime operations because of `NaT` must be evaluated in Python space, but part of an expression can still be evaluated with `numexpr`. For example:

In \[67\]: df \= pd.DataFrame(
   ....:    {"strings": np.repeat(list("cba"), 3), "nums": np.repeat(range(3), 3)}
   ....: )
   ....: 

In \[68\]: df
Out\[68\]: 
  strings  nums
0       c     0
1       c     0
2       c     0
3       b     1
4       b     1
5       b     1
6       a     2
7       a     2
8       a     2

In \[69\]: df.query("strings == 'a' and nums == 1")
Out\[69\]: 
Empty DataFrame
Columns: \[strings, nums\]
Index: \[\]

Copy to clipboard

The numeric part of the comparison (`nums == 1`) will be evaluated by `numexpr` and the object part of the comparison (`"strings == 'a'`) will be evaluated by Python.

On this page