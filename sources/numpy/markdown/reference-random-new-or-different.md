[Skip to main content](https://numpy.org/doc/stable/reference/random/new-or-different.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/new-or-different.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/new-or-different.html)
[2.4](https://numpy.org/doc/2.4/reference/random/new-or-different.html)
[2.3](https://numpy.org/doc/2.3/reference/random/new-or-different.html)
[2.2](https://numpy.org/doc/2.2/reference/random/new-or-different.html)
[2.1](https://numpy.org/doc/2.1/reference/random/new-or-different.html)
[2.0](https://numpy.org/doc/2.0/reference/random/new-or-different.html)
[1.26](https://numpy.org/doc/1.26/reference/random/new-or-different.html)
[1.25](https://numpy.org/doc/1.25/reference/random/new-or-different.html)
[1.24](https://numpy.org/doc/1.24/reference/random/new-or-different.html)
[1.23](https://numpy.org/doc/1.23/reference/random/new-or-different.html)
[1.22](https://numpy.org/doc/1.22/reference/random/new-or-different.html)
[1.21](https://numpy.org/doc/1.21/reference/random/new-or-different.html)
[1.20](https://numpy.org/doc/1.20/reference/random/new-or-different.html)
[1.19](https://numpy.org/doc/1.19/reference/random/new-or-different.html)
[1.18](https://numpy.org/doc/1.18/reference/random/new-or-different.html)
[1.17](https://numpy.org/doc/1.17/reference/random/new-or-different.html)
[1.16](https://numpy.org/doc/1.16/reference/random/new-or-different.html)
[1.15](https://numpy.org/doc/1.15/reference/random/new-or-different.html)
[1.14](https://numpy.org/doc/1.14/reference/random/new-or-different.html)
[1.13](https://numpy.org/doc/1.13/reference/random/new-or-different.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

What’s new or different[#](https://numpy.org/doc/stable/reference/random/new-or-different.html#what-s-new-or-different "Link to this heading")

===============================================================================================================================================

NumPy 1.17.0 introduced [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 as an improved replacement for the [legacy](https://numpy.org/doc/stable/reference/random/legacy.html#legacy)
 [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
. Here is a quick comparison of the two implementations.

|     |     |     |
| --- | --- | --- |
| Feature | Older Equivalent | Notes |
| [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator") | [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState") | [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")<br> requires a stream source, called a [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")<br> A number of these are provided. [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")<br> uses the Mersenne Twister [`MT19937`](https://numpy.org/doc/stable/reference/random/bit_generators/mt19937.html#numpy.random.MT19937 "numpy.random.MT19937")<br> by default, but can also be instantiated with any BitGenerator. |
| [`random`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random "numpy.random.Generator.random") | [`random_sample`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_sample.html#numpy.random.random_sample "numpy.random.random_sample")<br>, [`rand`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand") | Access the values in a BitGenerator, convert them to `float64` in the interval `[0.0., 1.0)`. In addition to the `size` kwarg, now supports `dtype='d'` or `dtype='f'`, and an `out` kwarg to fill a user-supplied array.<br><br>Many other distributions are also supported. |\
| [`integers`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.integers.html#numpy.random.Generator.integers "numpy.random.Generator.integers") | [`randint`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint "numpy.random.randint")<br>, [`random_integers`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_integers.html#numpy.random.random_integers "numpy.random.random_integers") | Use the `endpoint` kwarg to adjust the inclusion or exclusion of the `high` interval endpoint. |\
\
*   The normal, exponential and gamma generators use 256-step Ziggurat methods which are 2-10 times faster than NumPy’s default implementation in [`standard_normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_normal.html#numpy.random.Generator.standard_normal "numpy.random.Generator.standard_normal")\
    , [`standard_exponential`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_exponential.html#numpy.random.Generator.standard_exponential "numpy.random.Generator.standard_exponential")\
     or [`standard_gamma`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_gamma.html#numpy.random.Generator.standard_gamma "numpy.random.Generator.standard_gamma")\
    . Because of the change in algorithms, it is not possible to reproduce the exact random values using [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")\
     for these distributions or any distribution method that relies on them.\
    \
\
In \[1\]: import numpy.random\
\
In \[2\]: rng \= np.random.default\_rng()\
\
In \[3\]: %timeit -n 1 rng.standard\_normal(100000)\
   ...: %timeit -n 1 numpy.random.standard\_normal(100000)\
   ...: \
1.04 ms +- 24.2 us per loop (mean +- std. dev. of 7 runs, 1 loop each)\
1.75 ms +- 8.26 us per loop (mean +- std. dev. of 7 runs, 1 loop each)\
\
Copy to clipboard\
\
In \[4\]: %timeit -n 1 rng.standard\_exponential(100000)\
   ...: %timeit -n 1 numpy.random.standard\_exponential(100000)\
   ...: \
490 us +- 4.59 us per loop (mean +- std. dev. of 7 runs, 1 loop each)\
1.26 ms +- 14.2 us per loop (mean +- std. dev. of 7 runs, 1 loop each)\
\
Copy to clipboard\
\
In \[5\]: %timeit -n 1 rng.standard\_gamma(3.0, 100000)\
   ...: %timeit -n 1 numpy.random.standard\_gamma(3.0, 100000)\
   ...: \
1.86 ms +- 9.67 us per loop (mean +- std. dev. of 7 runs, 1 loop each)\
3.44 ms +- 17.1 us per loop (mean +- std. dev. of 7 runs, 1 loop each)\
\
Copy to clipboard\
\
*   [`integers`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.integers.html#numpy.random.Generator.integers "numpy.random.Generator.integers")\
     is now the canonical way to generate integer random numbers from a discrete uniform distribution. This replaces both [`randint`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint "numpy.random.randint")\
     and the deprecated [`random_integers`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_integers.html#numpy.random.random_integers "numpy.random.random_integers")\
    .\
    \
*   The [`rand`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")\
     and [`randn`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")\
     methods are only available through the legacy [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")\
    .\
    \
*   [`Generator.random`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random "numpy.random.Generator.random")\
     is now the canonical way to generate floating-point random numbers, which replaces [`RandomState.random_sample`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.random_sample.html#numpy.random.RandomState.random_sample "numpy.random.RandomState.random_sample")\
    , [`sample`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.sample.html#numpy.random.sample "numpy.random.sample")\
    , and [`ranf`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.ranf.html#numpy.random.ranf "numpy.random.ranf")\
    , all of which were aliases. This is consistent with Python’s [`random.random`](https://docs.python.org/3/library/random.html#random.random "(in Python v3.14)")\
    .\
    \
*   All bit generators can produce doubles, uint64s and uint32s via CTypes ([`ctypes`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.PCG64.ctypes.html#numpy.random.PCG64.ctypes "numpy.random.PCG64.ctypes")\
    ) and CFFI ([`cffi`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.PCG64.cffi.html#numpy.random.PCG64.cffi "numpy.random.PCG64.cffi")\
    ). This allows these bit generators to be used in numba.\
    \
*   The bit generators can be used in downstream projects via Cython.\
    \
*   All bit generators use [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")\
     to [convert seed integers to initialized states](https://numpy.org/doc/stable/reference/random/bit_generators/index.html#seeding-and-entropy)\
    .\
    \
*   Optional `dtype` argument that accepts `np.float32` or `np.float64` to produce either single or double precision uniform random variables for select distributions. [`integers`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.integers.html#numpy.random.Generator.integers "numpy.random.Generator.integers")\
     accepts a `dtype` argument with any signed or unsigned integer dtype.\
    \
    *   Uniforms ([`random`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random "numpy.random.Generator.random")\
         and [`integers`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.integers.html#numpy.random.Generator.integers "numpy.random.Generator.integers")\
        )\
        \
    *   Normals ([`standard_normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_normal.html#numpy.random.Generator.standard_normal "numpy.random.Generator.standard_normal")\
        )\
        \
    *   Standard Gammas ([`standard_gamma`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_gamma.html#numpy.random.Generator.standard_gamma "numpy.random.Generator.standard_gamma")\
        )\
        \
    *   Standard Exponentials ([`standard_exponential`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_exponential.html#numpy.random.Generator.standard_exponential "numpy.random.Generator.standard_exponential")\
        )\
        \
\
In \[6\]: rng \= np.random.default\_rng()\
\
In \[7\]: rng.random(3, dtype\=np.float64)\
Out\[7\]: array(\[0.76759948, 0.88825294, 0.21580722\])\
\
In \[8\]: rng.random(3, dtype\=np.float32)\
Out\[8\]: array(\[0.01490843, 0.74982375, 0.6904811 \], dtype=float32)\
\
In \[9\]: rng.integers(0, 256, size\=3, dtype\=np.uint8)\
Out\[9\]: array(\[ 94, 145, 119\], dtype=uint8)\
\
Copy to clipboard\
\
*   Optional `out` argument that allows existing arrays to be filled for select distributions\
    \
    *   Uniforms ([`random`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random "numpy.random.Generator.random")\
        )\
        \
    *   Normals ([`standard_normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_normal.html#numpy.random.Generator.standard_normal "numpy.random.Generator.standard_normal")\
        )\
        \
    *   Standard Gammas ([`standard_gamma`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_gamma.html#numpy.random.Generator.standard_gamma "numpy.random.Generator.standard_gamma")\
        )\
        \
    *   Standard Exponentials ([`standard_exponential`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_exponential.html#numpy.random.Generator.standard_exponential "numpy.random.Generator.standard_exponential")\
        )\
        \
    \
    This allows multithreading to fill large arrays in chunks using suitable BitGenerators in parallel.\
    \
\
In \[10\]: rng \= np.random.default\_rng()\
\
In \[11\]: existing \= np.zeros(4)\
\
In \[12\]: rng.random(out\=existing\[:2\])\
Out\[12\]: array(\[0.09459523, 0.99734979\])\
\
In \[13\]: print(existing)\
\[0.09459523 0.99734979 0.         0.        \]\
\
Copy to clipboard\
\
*   Optional `axis` argument for methods like [`choice`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html#numpy.random.Generator.choice "numpy.random.Generator.choice")\
    , [`permutation`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permutation.html#numpy.random.Generator.permutation "numpy.random.Generator.permutation")\
     and [`shuffle`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.shuffle.html#numpy.random.Generator.shuffle "numpy.random.Generator.shuffle")\
     that controls which axis an operation is performed over for multi-dimensional arrays.\
    \
\
In \[14\]: rng \= np.random.default\_rng()\
\
In \[15\]: a \= np.arange(12).reshape((3, 4))\
\
In \[16\]: a\
Out\[16\]: \
array(\[\[ 0,  1,  2,  3\],\
       \[ 4,  5,  6,  7\],\
       \[ 8,  9, 10, 11\]\])\
\
In \[17\]: rng.choice(a, axis\=1, size\=5)\
Out\[17\]: \
array(\[\[ 2,  2,  1,  0,  1\],\
       \[ 6,  6,  5,  4,  5\],\
       \[10, 10,  9,  8,  9\]\])\
\
In \[18\]: rng.shuffle(a, axis\=1)        \# Shuffle in-place\
\
In \[19\]: a\
Out\[19\]: \
array(\[\[ 2,  3,  1,  0\],\
       \[ 6,  7,  5,  4\],\
       \[10, 11,  9,  8\]\])\
\
Copy to clipboard\
\
*   Added a method to sample from the complex normal distribution (_complex\_normal_)