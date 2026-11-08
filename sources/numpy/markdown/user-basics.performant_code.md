[Skip to main content](https://numpy.org/doc/stable/user/basics.performant_code.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/user/basics.performant_code.html)
[2.5 (stable)](https://numpy.org/doc/stable/user/basics.performant_code.html)
[2.4](https://numpy.org/doc/2.4/user/basics.performant_code.html)
[2.3](https://numpy.org/doc/2.3/user/basics.performant_code.html)
[2.2](https://numpy.org/doc/2.2/user/basics.performant_code.html)
[2.1](https://numpy.org/doc/2.1/user/basics.performant_code.html)
[2.0](https://numpy.org/doc/2.0/user/basics.performant_code.html)
[1.26](https://numpy.org/doc/1.26/user/basics.performant_code.html)
[1.25](https://numpy.org/doc/1.25/user/basics.performant_code.html)
[1.24](https://numpy.org/doc/1.24/user/basics.performant_code.html)
[1.23](https://numpy.org/doc/1.23/user/basics.performant_code.html)
[1.22](https://numpy.org/doc/1.22/user/basics.performant_code.html)
[1.21](https://numpy.org/doc/1.21/user/basics.performant_code.html)
[1.20](https://numpy.org/doc/1.20/user/basics.performant_code.html)
[1.19](https://numpy.org/doc/1.19/user/basics.performant_code.html)
[1.18](https://numpy.org/doc/1.18/user/basics.performant_code.html)
[1.17](https://numpy.org/doc/1.17/user/basics.performant_code.html)
[1.16](https://numpy.org/doc/1.16/user/basics.performant_code.html)
[1.15](https://numpy.org/doc/1.15/user/basics.performant_code.html)
[1.14](https://numpy.org/doc/1.14/user/basics.performant_code.html)
[1.13](https://numpy.org/doc/1.13/user/basics.performant_code.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Writing Performant NumPy Code with Multi-Core CPUs[#](https://numpy.org/doc/stable/user/basics.performant_code.html#writing-performant-numpy-code-with-multi-core-cpus "Link to this heading")

===============================================================================================================================================================================================

Introduction[#](https://numpy.org/doc/stable/user/basics.performant_code.html#introduction "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

NumPy is designed for high performance numerical computing in Python by leveraging vectorized operations. However, vectorization does not always fully utilize the capabilities of multi-core processors. To exploit parallelism, additional strategies are necessary.

In this section, we cover the following topics:

*   [General concepts for using multi-core processors in Python](https://numpy.org/doc/stable/user/basics.performant_code.html#basics-performant-code-general-concepts-for-multi-core-processors)
    
*   [Using multi-core processors with Python standard libraries](https://numpy.org/doc/stable/user/basics.performant_code.html#basics-performant-code-multi-core-with-standard-libraries)
    
*   [Third party libraries for multi-core processing](https://numpy.org/doc/stable/user/basics.performant_code.html#basics-performant-code-third-party-libraries)
    

General concepts for multi-core processors in Python[#](https://numpy.org/doc/stable/user/basics.performant_code.html#general-concepts-for-multi-core-processors-in-python "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Multiprocessing[#](https://numpy.org/doc/stable/user/basics.performant_code.html#multiprocessing "Link to this heading")

Multiprocessing is a technique that allows the execution of multiple processes simultaneously, each with its own Python interpreter and memory space. As a high-level API, Python provides the [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "(in Python v3.14)")
 class to facilitate multiprocessing.

Firstly, we introduce brief Pros and Cons of multiprocessing:

#### Pros[#](https://numpy.org/doc/stable/user/basics.performant_code.html#pros "Link to this heading")

*   Bypasses the Global Interpreter Lock (GIL), allowing true parallelism
    
*   Avoids accidental data sharing due to separate memory spaces
    

#### Cons[#](https://numpy.org/doc/stable/user/basics.performant_code.html#cons "Link to this heading")

*   Higher memory usage due to separate memory spaces for each process
    
*   Difficulty in sharing data between processes, requiring serialization (pickling) of objects
    

#### General tips[#](https://numpy.org/doc/stable/user/basics.performant_code.html#general-tips "Link to this heading")

The following are general tips for utilizing multiprocessing. Some of these tips are used in the [Multiprocessing Example](https://numpy.org/doc/stable/user/basics.performant_code.html#multiprocessing-example)
.

##### Reduce creation overhead[#](https://numpy.org/doc/stable/user/basics.performant_code.html#reduce-creation-overhead "Link to this heading")

Process creation has a higher overhead compared to thread creation due to the need to initialize a new Python interpreter and memory space. To mitigate this overhead, consider the following strategies:

*   Use process pools to reuse existing processes instead of creating new ones for each task. [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "(in Python v3.14)")
     provides this feature.
    
*   Select appropriate startup methods. Avoid explicitly selecting `fork` unless you know that it is safe in your application. Forking a multithreaded process is problematic and can lead to deadlocks or crashes. Python 3.14 changed the default start method on POSIX platforms from `fork` to `forkserver` to avoid common multithreaded process incompatibilities. See the [multiprocessing documentation](https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods)
     for more details.
    

##### Reduce communication overhead[#](https://numpy.org/doc/stable/user/basics.performant_code.html#reduce-communication-overhead "Link to this heading")

Inter-process communication (IPC) can introduce significant overhead due to data serialization and transfer between processes. In Python, only picklable objects are allowed to be passed between processes. Due to this limitation, multiprocessing is not suitable for programs which need to serialize data between processes frequently.

To reduce communication overhead, consider the following strategies:

*   Minimize the amount of data transferred between processes.
    
*   Use shared memory constructs such as [`multiprocessing.shared_memory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#module-multiprocessing.shared_memory "(in Python v3.14)")
    , [`multiprocessing.Array`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Array "(in Python v3.14)")
     or [`multiprocessing.Value`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Value "(in Python v3.14)")
     for large data that needs to be accessed by multiple processes.
    
*   [Balance processing load](https://numpy.org/doc/stable/user/basics.performant_code.html#balance-processing-load)
     to ensure that all processes are utilized efficiently and avoid idle time.
    

##### Pickling considerations[#](https://numpy.org/doc/stable/user/basics.performant_code.html#pickling-considerations "Link to this heading")

The worker function and its arguments must be picklable when using multiprocessing. This requirement can become a limitation when working with complex data structures or dynamically defined functions.

If you encounter pickling-related issues, consider the following strategies:

*   Refactor your code to use simpler data structures or functions. For example, define worker functions at the top level of a module and avoid lambda or nested functions.
    
*   Consider third-party libraries such as [joblib](https://github.com/joblib/joblib)
    . `joblib`’s default backend `loky` relies on [cloudpickle](https://github.com/cloudpipe/cloudpickle)
     for serialization and can handle a wider range of Python objects than the standard `pickle` module. See the `joblib` documentaion on [Serialization of un-picklable objects](https://joblib.readthedocs.io/en/latest/auto_examples/serialization_and_wrappers.html)
     for more details.
    

### Multithreading[#](https://numpy.org/doc/stable/user/basics.performant_code.html#multithreading "Link to this heading")

Multithreading allows multiple threads to run within the same process, sharing the same memory space.

Free-threaded Python was introduced experimentally in Python 3.13 and became a supported (non-experimental) feature in Python 3.14. When combined with libraries that are explicitly designed to be thread-safe, this can enable true parallel execution with threads. For details on free-threaded Python builds, see the [Python Free-Threading Guide](https://py-free-threading.github.io/)
.

As a high-level API, Python provides the [`concurrent.futures.ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "(in Python v3.14)")
 class for thread-based parallelism. Python also provides the [concurrent.futures.InterpreterPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.InterpreterPoolExecutor)
, which uses multiple interpreters running in separate threads and avoids sharing Python objects between them. However, it is not yet available in NumPy. (See [gh-24755](https://github.com/numpy/numpy/issues/24755)
 for details.)

The main pros and cons of multithreading are as follows:

#### Pros[#](https://numpy.org/doc/stable/user/basics.performant_code.html#id1 "Link to this heading")

*   Lower memory usage since threads share the same memory space
    
*   Easier communication between threads
    

#### Cons[#](https://numpy.org/doc/stable/user/basics.performant_code.html#id2 "Link to this heading")

*   Possibility of race conditions when mutating shared data simultaneously with reads in other threads
    
*   Limited performance improvement if using Python libraries are not thread-safe or have limited support for free-threaded Python builds
    

#### General tips[#](https://numpy.org/doc/stable/user/basics.performant_code.html#id3 "Link to this heading")

The following are general tips for utilizing multithreading. For more details on thread safety guarantees for built-in types in Python’s free-threaded build, see the Python documentation on [Thread Safety Guarantees](https://docs.python.org/3.15/library/threadsafety.html#thread-safety-guarantees)
. Some of these tips are used in the [Multithreading Example](https://numpy.org/doc/stable/user/basics.performant_code.html#multithreading-example)
.

##### Avoid race conditions[#](https://numpy.org/doc/stable/user/basics.performant_code.html#avoid-race-conditions "Link to this heading")

Race conditions occur when multiple threads update shared data simultaneously, leading to unpredictable results. To avoid race conditions, consider the following strategies:

*   Minimize the amount of shared data between threads by designing your program to use thread-local storage or by passing data explicitly to threads.
    
*   Prefer immutable NumPy arrays or read-only access patterns when possible, since they reduce the need for explicit synchronization.
    
*   Use thread-safe data structures or synchronization primitives like locks, semaphores, or condition variables to manage access to shared data. Note that improper use of these synchronization mechanisms can cause deadlocks, so they should be used with care.
    

##### Avoid CPU oversubscription[#](https://numpy.org/doc/stable/user/basics.performant_code.html#avoid-cpu-oversubscription "Link to this heading")

Some NumPy operations, such as matrix multiplication and linear algebra functions (See [Linear Algebra](https://numpy.org/doc/stable/reference/routines.linalg.html#routines-linalg)
), may use multiple threads provided by the underlying BLAS library (e.g. OpenBLAS, MKL).

If these operations are executed from another thread pool that already uses all available CPU cores, CPU oversubscription can occur. In this situation, both the outer thread pool and the BLAS threads compete for the same CPU resources, which can reduce performance.

To avoid CPU oversubscription, consider the following strategies:

*   Limit the number of threads in BLAS to 1, for example using [threadpoolctl](https://github.com/joblib/threadpoolctl)
    

### Common tips for both multiprocessing and multithreading[#](https://numpy.org/doc/stable/user/basics.performant_code.html#common-tips-for-both-multiprocessing-and-multithreading "Link to this heading")

#### Balance processing load[#](https://numpy.org/doc/stable/user/basics.performant_code.html#balance-processing-load "Link to this heading")

If the processing load is not evenly distributed among workers, some workers may finish their tasks earlier and remain idle while others are still working. It leads to inefficient use of resources and longer overall execution time.

To achieve better load balancing, consider the following strategies:

*   Use dynamic task allocation where tasks are assigned to workers as they become available, rather than pre-allocating tasks.
    
*   Check `chunksize` parameter to ensure that tasks are neither too small (causing excessive overhead) nor too large (leading to load imbalance).
    

#### Determine the correct number of cpus[#](https://numpy.org/doc/stable/user/basics.performant_code.html#determine-the-correct-number-of-cpus "Link to this heading")

Pythons provides [`os.cpu_count`](https://docs.python.org/3/library/os.html#os.cpu_count "(in Python v3.14)")
 and [os.process\_cpu\_count](https://docs.python.org/3/library/os.html#os.process_cpu_count)
 functions to get the number of CPUs in the system and the current process, respectively. However, in some environments (e.g., Docker containers or HPC clusters), this may not reflect the actual number of CPUs available to the process.

To get a more accurate count of available CPUs, consider the following strategies:

*   Use [joblib.cpu\_count()](https://joblib.readthedocs.io/en/latest/generated/joblib.cpu_count.html)
    , which takes into account constraints such as CPU affinity settings and Linux CFS scheduler quotas. (See [joblib](https://numpy.org/doc/stable/user/basics.performant_code.html#joblib)
     section for more details about joblib.)
    

Using multi-core processors with Python standard libraries[#](https://numpy.org/doc/stable/user/basics.performant_code.html#using-multi-core-processors-with-python-standard-libraries "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this section, we demonstrate how to use Python’s standard libraries to leverage multi-core processors with NumPy.

As an example, we use [Mandelbrot set](https://en.wikipedia.org/wiki/Mandelbrot_set)
 generation. Mandelbrot set is defined as the set of complex numbers `c` for which the sequence defined by the iterative function does not diverge to infinity:

\\\[z\_{n+1} = z\_n^2 + c, \\quad z\_0 = 0\\\]

If the absolute value of \\(z\_n\\) remains bounded (i.e., does not exceed a certain threshold, typically `2` ) after a fixed number of iterations, then `c` is considered to be in the Mandelbrot set.

Following to this definition, we can calculate each point in the complex plane independently, making it suited for parallel computation.

The hot colors in the image below represent the number of iterations it took for the sequence to diverge for each point in the complex plane.

[![Mandelbrot set](https://numpy.org/doc/stable/_images/np_mandelbrot.png)](https://numpy.org/doc/stable/_images/np_mandelbrot.png)

### Multiprocessing Example[#](https://numpy.org/doc/stable/user/basics.performant_code.html#multiprocessing-example "Link to this heading")

The following code demonstrates how to use [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "(in Python v3.14)")
 to parallelize the Mandelbrot set generation across multiple processes.

This example prioritizes clarity over efficiency. In practice, transferring large NumPy arrays between processes can be expensive. Defining shared-memory arrays or creating arrays within each process may be more efficient implementation.

from concurrent.futures import ProcessPoolExecutor

import numpy as np
from numpy.typing import NDArray

def mandelbrot\_block(
    c\_block: NDArray\[np.complex128\], max\_iter: int
) \-> NDArray\[np.int64\]:
    z \= np.zeros(c\_block.shape, dtype\=np.complex128)
    steps \= np.zeros(c\_block.shape, dtype\=np.int64)

    for \_ in range(max\_iter):
        mask \= np.abs(z) <= 2
        z\[mask\] \= z\[mask\] \* z\[mask\] + c\_block\[mask\]
        steps\[mask\] += 1
    return steps

def mandelbrot\_set(
    arr: NDArray\[np.complex128\],
    max\_iter: int,
    n\_workers: int,
) \-> NDArray\[np.int64\]:
    n\_workers \= min(n\_workers, arr.size)
    arrs \= np.array\_split(arr, n\_workers)

    with ProcessPoolExecutor(max\_workers\=n\_workers) as pool:
        futures \= \[\
            pool.submit(mandelbrot\_block, \_arr, max\_iter) for \_arr in arrs\
        \]
        results \= \[future.result() for future in futures\]

    return np.concatenate(results)

if \_\_name\_\_ \== '\_\_main\_\_':

    xmin, xmax, ymin, ymax \= \-2.0, 1.0, \-1.5, 1.5
    nx, ny \= 800, 800
    max\_iter \= 10000
    n\_workers \= 10

    real \= np.linspace(xmin, xmax, nx, dtype\=np.float64)
    imag \= np.linspace(ymin, ymax, ny, dtype\=np.float64)

    arr \= (real\[:, np.newaxis\] + 1j \* imag\[np.newaxis, :\]).ravel()
    mandelbrot\_image \= mandelbrot\_set(arr, max\_iter, n\_workers)
    mandelbrot\_image \= mandelbrot\_image.reshape((nx, ny))

Copy to clipboard

### Multithreading Example[#](https://numpy.org/doc/stable/user/basics.performant_code.html#multithreading-example "Link to this heading")

As in the multiprocessing example, we demonstrate how to use [`concurrent.futures.ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "(in Python v3.14)")
 to parallelize the Mandelbrot set generation across multiple threads. For more detailed explanations and additional examples, see [Examples Demonstrating Free-Threaded Python](https://py-free-threading.github.io/examples/)
.

#### Setup[#](https://numpy.org/doc/stable/user/basics.performant_code.html#setup "Link to this heading")

##### Install a free-threaded build Python[#](https://numpy.org/doc/stable/user/basics.performant_code.html#install-a-free-threaded-build-python "Link to this heading")

Before running the multithreading example, ensure you have a free-threaded build of Python 3.13 or later. About how to install a free-threaded build of Python, please refer to the [Installing Free-Threaded Python](https://py-free-threading.github.io/installing-cpython/)
.

According to the [Python documentation](https://docs.python.org/3/howto/free-threading-python.html)
, there are several ways to verify if your Python build is free-threaded.

*   Run `python -VV` in your terminal and check `free-threading build` is shown
    
*   Check the value of _sys.\_is\_gil\_enabled()_ in a Python shell, which should return _False_.
    

#### Code Example[#](https://numpy.org/doc/stable/user/basics.performant_code.html#code-example "Link to this heading")

The following code demonstrates how to use [`concurrent.futures.ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "(in Python v3.14)")
 to parallelize the Mandelbrot set generation across multiple threads.

This implementation shares several arrays between threads. For example, `SHARED_readonly_arr` is a read-only array that holds the complex numbers to be evaluated, and `SHARED_updating_steps` is an array that holds the number of iterations for each point.

import sys
from concurrent.futures import ThreadPoolExecutor

import numpy as np

def mandelbrot\_block(start: int, stop: int, max\_iter: int) \-> None:
    z\_target \= np.zeros(stop \- start, dtype\=np.complex128)

    indexes \= slice(start, stop)
    arr\_target \= SHARED\_readonly\_arr\[indexes\]
    steps\_target \= SHARED\_updating\_steps\[indexes\]

    threshold \= 2.0
    for \_ in range(max\_iter):
        mask \= np.abs(z\_target) <= threshold
        z\_target\[mask\] \= z\_target\[mask\] \* z\_target\[mask\] + arr\_target\[mask\]
        steps\_target\[mask\] += 1
    SHARED\_updating\_steps\[indexes\] \= steps\_target
    return None

def mandelbrot\_set(
    total\_size: int,
    max\_iter: int,
    n\_workers: int,
) \-> None:

    chunksize \= total\_size // n\_workers
    with ThreadPoolExecutor(max\_workers\=n\_workers) as pool:
        futures \= \[\
            pool.submit(\
                mandelbrot\_block, start, min(start + chunksize, total\_size), max\_iter\
            )\
            for start in range(0, total\_size, chunksize)\
        \]
        \_ \= \[future.result() for future in futures\]

if \_\_name\_\_ \== '\_\_main\_\_':

    print("Python version is free-threaded:", not sys.\_is\_gil\_enabled())
    assert not sys.\_is\_gil\_enabled()

    xmin, xmax, ymin, ymax \= \-2.0, 1.0, \-1.5, 1.5
    nx, ny \= 800, 800
    max\_iter \= 10000
    n\_workers \= 10

    real \= np.linspace(xmin, xmax, nx, dtype\=np.float64)
    imag \= np.linspace(ymin, ymax, ny, dtype\=np.float64)

    SHARED\_readonly\_arr \= (real\[:, np.newaxis\] + 1j \* imag\[np.newaxis, :\]).ravel()
    SHARED\_readonly\_arr.flags.writeable \= False

    SHARED\_updating\_steps \= np.zeros(SHARED\_readonly\_arr.shape, dtype\=np.int64)

    mandelbrot\_set(SHARED\_readonly\_arr.size, max\_iter, n\_workers)
    mandelbrot\_image \= SHARED\_updating\_steps.reshape((nx, ny))

Copy to clipboard

Third Party Libraries for Multi-Core Processing[#](https://numpy.org/doc/stable/user/basics.performant_code.html#third-party-libraries-for-multi-core-processing "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In many practical scenarios, third-party libraries can provide more convenient and efficient solutions than using Python’s standard libraries.

### Dask[#](https://numpy.org/doc/stable/user/basics.performant_code.html#dask "Link to this heading")

Dask is an open-source library that provides parallel compuing features not only for a single machine but also for a cluster of machines. It also provides `DaskArray` which has a similar API to NumPy’s `ndarray`. If you are familiar with NumPy, you can easily get started with `DaskArray`.

*   Dask Documentaion: [https://docs.dask.org/en/stable/](https://docs.dask.org/en/stable/)
    
*   Dask GitHub Repository: [dask/dask](https://github.com/dask/dask)
    

### joblib[#](https://numpy.org/doc/stable/user/basics.performant_code.html#joblib "Link to this heading")

`joblib` is a library that provides helper functions which make it easy to parallelize tasks.

For example,

*   `joblib`’s default backend `loky` relies on [cloudpickle](https://github.com/cloudpipe/cloudpickle)
     for serialization and can handle a wider range of Python objects than the standard `pickle` module. (e.g., lambda functions)
    
*   [joblib.cpu\_count()](https://joblib.readthedocs.io/en/latest/generated/joblib.cpu_count.html)
     returns the number of CPUs available to the current process, taking into account constraints such as CPU affinity settings and Linux CFS scheduler quotas. This may provide a more accurate value than [`os.cpu_count`](https://docs.python.org/3/library/os.html#os.cpu_count "(in Python v3.14)")
     and [os.process\_cpu\_count](https://docs.python.org/3/library/os.html#os.process_cpu_count)
     functions in Docker containers and other resource-constrained environments.
    

For more details on `joblib`, see the following resources:

*   joblib Documentation: [https://joblib.readthedocs.io/en/latest/](https://joblib.readthedocs.io/en/latest/)
    
*   joblib GitHub Repository: [joblib/joblib](https://github.com/joblib/joblib)
    

### threadpoolctl[#](https://numpy.org/doc/stable/user/basics.performant_code.html#threadpoolctl "Link to this heading")

`threadpoolctl` is a library that provides utilities to control the behavior of thread pools in Python, including other thread pools used by libraries such as BLAS and OpenMP. It allows you to avoid CPU oversubscription when using multiple libraries that utilize threads.

For more details on `threadpoolctl`, see the following resources:

*   threadpoolctl GitHub Repository: [joblib/threadpoolctl](https://github.com/joblib/threadpoolctl)
    

On this page