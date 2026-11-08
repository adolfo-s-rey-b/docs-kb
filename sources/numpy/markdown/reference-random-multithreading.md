[Skip to main content](https://numpy.org/doc/stable/reference/random/multithreading.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Multithreaded generation[#](https://numpy.org/doc/stable/reference/random/multithreading.html#multithreaded-generation "Link to this heading")

===============================================================================================================================================

The four core distributions ([`random`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random "numpy.random.Generator.random")
, [`standard_normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_normal.html#numpy.random.Generator.standard_normal "numpy.random.Generator.standard_normal")
, [`standard_exponential`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_exponential.html#numpy.random.Generator.standard_exponential "numpy.random.Generator.standard_exponential")
, and [`standard_gamma`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_gamma.html#numpy.random.Generator.standard_gamma "numpy.random.Generator.standard_gamma")
) all allow existing arrays to be filled using the `out` keyword argument. Existing arrays need to be contiguous and well-behaved (writable and aligned). Under normal circumstances, arrays created using the common constructors such as [`numpy.empty`](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")
 will satisfy these requirements.

See also

[Thread Safety](https://numpy.org/doc/stable/reference/thread_safety.html#thread-safety)
 for general information about thread safety in NumPy.

This example makes use of [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures "(in Python v3.14)")
 to fill an array using multiple threads. Threads are long-lived so that repeated calls do not require any additional overheads from thread creation.

The random numbers generated are reproducible in the sense that the same seed will produce the same outputs, given that the number of threads does not change.

from numpy.random import default\_rng, SeedSequence
import multiprocessing
import concurrent.futures
import numpy as np

class MultithreadedRNG:
    def \_\_init\_\_(self, n, seed\=None, threads\=None):
        if threads is None:
            threads \= multiprocessing.cpu\_count()
        self.threads \= threads

        seq \= SeedSequence(seed)
        self.\_random\_generators \= \[default\_rng(s)\
                                   for s in seq.spawn(threads)\]

        self.n \= n
        self.executor \= concurrent.futures.ThreadPoolExecutor(threads)
        self.values \= np.empty(n)
        self.step \= np.ceil(n / threads).astype(np.int\_)

    def fill(self):
        def \_fill(random\_state, out, first, last):
            random\_state.standard\_normal(out\=out\[first:last\])

        futures \= {}
        for i in range(self.threads):
            args \= (\_fill,
                    self.\_random\_generators\[i\],
                    self.values,
                    i \* self.step,
                    (i + 1) \* self.step)
            futures\[self.executor.submit(\*args)\] \= i
        concurrent.futures.wait(futures)

    def \_\_del\_\_(self):
        self.executor.shutdown(False)

Copy to clipboard

The multithreaded random number generator can be used to fill an array. The `values` attributes shows the zero-value before the fill and the random value after.

In \[2\]: mrng \= MultithreadedRNG(10000000, seed\=12345)
   ...: print(mrng.values\[\-1\])
Out\[2\]: 0.0

In \[3\]: mrng.fill()
   ...: print(mrng.values\[\-1\])
Out\[3\]: 2.4545724517479104

Copy to clipboard

The time required to produce using multiple threads can be compared to the time required to generate using a single thread.

In \[4\]: print(mrng.threads)
   ...: %timeit mrng.fill()

Out\[4\]: 4
   ...: 32.8 ms ± 2.71 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

Copy to clipboard

The single threaded call directly uses the BitGenerator.

In \[5\]: values \= np.empty(10000000)
   ...: rg \= default\_rng()
   ...: %timeit rg.standard\_normal(out=values)

Out\[5\]: 99.6 ms ± 222 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

Copy to clipboard

The gains are substantial and the scaling is reasonable even for arrays that are only moderately large. The gains are even larger when compared to a call that does not use an existing array due to array creation overhead.

In \[6\]: rg \= default\_rng()
   ...: %timeit rg.standard\_normal(10000000)

Out\[6\]: 125 ms ± 309 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

Copy to clipboard

Note that if `threads` is not set by the user, it will be determined by `multiprocessing.cpu_count()`.

In \[7\]: \# simulate the behavior for \`threads=None\`, if the machine had only one thread
   ...: mrng \= MultithreadedRNG(10000000, seed\=12345, threads\=1)
   ...: print(mrng.values\[\-1\])
Out\[7\]: 1.1800150052158556

Copy to clipboard