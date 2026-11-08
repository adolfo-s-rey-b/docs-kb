[Skip to main content](https://scikit-learn.org/stable/computing/parallelism.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/computing/parallelism.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/computing/parallelism.html)
[1.8.0](https://scikit-learn.org/1.8/computing/parallelism.html)
[1.7.2](https://scikit-learn.org/1.7/computing/parallelism.html)
[1.6.1](https://scikit-learn.org/1.6/computing/parallelism.html)
[1.5.2](https://scikit-learn.org/1.5/computing/parallelism.html)
[1.4.2](https://scikit-learn.org/1.4/computing/parallelism.html)

Collapse Sidebar Expand Sidebar

10.3. Parallelism and resource management[#](https://scikit-learn.org/stable/computing/parallelism.html#parallelism-and-resource-management "Link to this heading")

====================================================================================================================================================================

10.3.1. Parallelism[#](https://scikit-learn.org/stable/computing/parallelism.html#parallelism "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

Some scikit-learn estimators and utilities parallelize costly operations using multiple CPU cores.

Depending on the type of estimator and sometimes the values of the constructor parameters, this is either done:

*   with higher-level parallelism via [joblib](https://joblib.readthedocs.io/en/latest/)
    .
    
*   with lower-level parallelism via OpenMP, used in C or Cython code.
    
*   with lower-level parallelism via BLAS, used by NumPy and SciPy for generic operations on arrays.
    

The `n_jobs` parameters of estimators always controls the amount of parallelism managed by joblib (processes or threads depending on the joblib backend). The thread-level parallelism managed by OpenMP in scikit-learn’s own Cython code or by BLAS & LAPACK libraries used by NumPy and SciPy operations used in scikit-learn is always controlled by environment variables or `threadpoolctl` as explained below. Note that some estimators can leverage all three kinds of parallelism at different points of their training and prediction methods.

We describe these 3 types of parallelism in the following subsections in more detail.

### 10.3.1.1. Higher-level parallelism with joblib[#](https://scikit-learn.org/stable/computing/parallelism.html#higher-level-parallelism-with-joblib "Link to this heading")

When the underlying implementation uses joblib, the number of workers (threads or processes) that are spawned in parallel can be controlled via the `n_jobs` parameter.

Note

**Startup Overhead**

When using `n_jobs > 1` (or `n_jobs=-1`), you may observe a delay the first time a parallel function is called. This is expected behavior caused by the overhead of starting the Python worker processes. Subsequent calls will be faster as they reuse the existing pool of workers.

Note

Where (and how) parallelization happens in the estimators using joblib by specifying `n_jobs` is currently poorly documented. Please help us by improving our docs and tackle [issue 14228](https://github.com/scikit-learn/scikit-learn/issues/14228)
!

Joblib is able to support both multi-processing and multi-threading. Whether joblib chooses to spawn a thread or a process depends on the **backend** that it’s using.

scikit-learn generally relies on the `loky` backend, which is joblib’s default backend. Loky is a multi-processing backend. When doing multi-processing, in order to avoid duplicating the memory in each process (which isn’t reasonable with big datasets), joblib will create a [memmap](https://docs.scipy.org/doc/numpy/reference/generated/numpy.memmap.html)
 that all processes can share, when the data is bigger than 1MB.

In some specific cases (when the code that is run in parallel releases the GIL), scikit-learn will indicate to `joblib` that a multi-threading backend is preferable.

As a user, you may control the backend that joblib will use (regardless of what scikit-learn recommends) by using a context manager:

from joblib import parallel\_backend

with parallel\_backend('threading', n\_jobs\=2):
    \# Your scikit-learn code here

Copy to clipboard

Please refer to the [joblib’s docs](https://joblib.readthedocs.io/en/latest/parallel.html#thread-based-parallelism-vs-process-based-parallelism)
 for more details.

In practice, whether parallelism is helpful at improving runtime depends on many factors. It is usually a good idea to experiment rather than assuming that increasing the number of workers is always a good thing. In some cases it can be highly detrimental to performance to run multiple copies of some estimators or functions in parallel (see [oversubscription](https://scikit-learn.org/stable/computing/parallelism.html#oversubscription)
 below).

### 10.3.1.2. Lower-level parallelism with OpenMP[#](https://scikit-learn.org/stable/computing/parallelism.html#lower-level-parallelism-with-openmp "Link to this heading")

OpenMP is used to parallelize code written in Cython or C, relying on multi-threading exclusively. By default, the implementations using OpenMP will use as many threads as possible, i.e. as many threads as logical cores.

You can control the exact number of threads that are used either:

*   via the `OMP_NUM_THREADS` environment variable, for instance when: running a python script:
    
    OMP\_NUM\_THREADS\=4 python my\_script.py
    
    Copy to clipboard
    
*   or via `threadpoolctl` as explained by [this piece of documentation](https://github.com/joblib/threadpoolctl/#setting-the-maximum-size-of-thread-pools)
    .
    

[SKLEARN\_PAIRWISE\_DIST\_CHUNK\_SIZE](https://scikit-learn.org/stable/developers/global_configuration.html#envvar-sklearn-pairwise-dist-chunk-size)
 tunes chunk size for OpenMP-parallel pairwise distance kernels in Cython (e.g. nearest neighbors). This is an advanced setting.

### 10.3.1.3. Parallel NumPy and SciPy routines from numerical libraries[#](https://scikit-learn.org/stable/computing/parallelism.html#parallel-numpy-and-scipy-routines-from-numerical-libraries "Link to this heading")

scikit-learn relies heavily on NumPy and SciPy, which internally call multi-threaded linear algebra routines (BLAS & LAPACK) implemented in libraries such as MKL, OpenBLAS or BLIS.

You can control the exact number of threads used by BLAS for each library using environment variables, namely:

*   `MKL_NUM_THREADS` sets the number of threads MKL uses,
    
*   `OPENBLAS_NUM_THREADS` sets the number of threads OpenBLAS uses
    
*   `BLIS_NUM_THREADS` sets the number of threads BLIS uses
    

Note that BLAS & LAPACK implementations can also be impacted by `OMP_NUM_THREADS`. To check whether this is the case in your environment, you can inspect how the number of threads effectively used by those libraries is affected when running the following command in a bash or zsh terminal for different values of `OMP_NUM_THREADS`:

OMP\_NUM\_THREADS\=2 python \-m threadpoolctl \-i numpy scipy

Copy to clipboard

Note

At the time of writing (2022), NumPy and SciPy packages which are distributed on pypi.org (i.e. the ones installed via `pip install`) and on the conda-forge channel (i.e. the ones installed via `conda install --channel conda-forge`) are linked with OpenBLAS, while NumPy and SciPy packages shipped on the `defaults` conda channel from Anaconda.org (i.e. the ones installed via `conda install`) are linked by default with MKL.

### 10.3.1.4. Oversubscription: spawning too many threads[#](https://scikit-learn.org/stable/computing/parallelism.html#oversubscription-spawning-too-many-threads "Link to this heading")

It is generally recommended to avoid using significantly more processes or threads than the number of CPUs on a machine. Over-subscription happens when a program is running too many threads at the same time.

Suppose you have a machine with 8 CPUs. Consider a case where you’re running a [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
 (parallelized with joblib) with `n_jobs=8` over a [`HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
 (parallelized with OpenMP). Each instance of [`HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
 will spawn 8 threads (since you have 8 CPUs). That’s a total of `8 * 8 = 64` threads, which leads to oversubscription of threads for physical CPU resources and thus to scheduling overhead.

Oversubscription can arise in the exact same fashion with parallelized routines from MKL, OpenBLAS or BLIS that are nested in joblib calls.

Starting from `joblib >= 0.14`, when the `loky` backend is used (which is the default), joblib will tell its child **processes** to limit the number of threads they can use, so as to avoid oversubscription. In practice the heuristic that joblib uses is to tell the processes to use `max_threads = n_cpus // n_jobs`, via their corresponding environment variable. Back to our example from above, since the joblib backend of [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
 is `loky`, each process will only be able to use 1 thread instead of 8, thus mitigating the oversubscription issue.

Note that:

*   Manually setting one of the environment variables (`OMP_NUM_THREADS`, `MKL_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, or `BLIS_NUM_THREADS`) will take precedence over what joblib tries to do. The total number of threads will be `n_jobs * <LIB>_NUM_THREADS`. Note that setting this limit will also impact your computations in the main process, which will only use `<LIB>_NUM_THREADS`. Joblib exposes a context manager for finer control over the number of threads in its workers (see joblib docs linked below).
    
*   When joblib is configured to use the `threading` backend, there is no mechanism to avoid oversubscriptions when calling into parallel native libraries in the joblib-managed threads.
    
*   All scikit-learn estimators that explicitly rely on OpenMP in their Cython code always use `threadpoolctl` internally to automatically adapt the numbers of threads used by OpenMP and potentially nested BLAS calls so as to avoid oversubscription.
    

You will find additional details about joblib mitigation of oversubscription in [joblib documentation](https://joblib.readthedocs.io/en/latest/parallel.html#avoiding-over-subscription-of-cpu-resources)
.

You will find additional details about parallelism in numerical python libraries in [this document from Thomas J. Fan](https://thomasjpfan.github.io/parallelism-python-libraries-design/)
.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)