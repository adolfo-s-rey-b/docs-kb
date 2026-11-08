Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/data.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/data.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/data.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/data.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/data.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/data.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/data.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/data.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/data.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/data.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/data.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/data.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/data.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/data.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/data.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/data.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/data.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/data.html)
[v1.13](https://docs.pytorch.org/docs/1.13/data.html)
[v1.12](https://docs.pytorch.org/docs/1.12/data.html)
[v1.11](https://docs.pytorch.org/docs/1.11/data.html)
[v1.10](https://docs.pytorch.org/docs/1.10/data.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/data.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/data.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/data.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/data.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/data.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/data.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/data.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/data.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/data.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/data.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/data.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/data.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/data.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/data.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/data.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/data.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/data.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/data.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/data.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/data.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/data.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/data.html)

[Go to pytorch.org](https://pytorch.org/)

 Ctrl+K

|     |     |
| --- | --- |
|     | [×](javascript:void(0) "Clear search box") |

search

Custom Search

|     |     |
| --- | --- |
|     | Sort by<br><br>Relevance<br><br>Date |

*   [X](https://x.com/PyTorch)
    
*   [GitHub](https://github.com/pytorch/pytorch)
    
*   [PyTorch Forum](https://discuss.pytorch.org/)
    
*   [PyPi](https://pypi.org/project/torch/)
    

Rate this Page

★ ★ ★ ★ ★

torch.utils.data[#](https://docs.pytorch.org/docs/2.15/data.html#module-torch.utils.data "Link to this heading")

=================================================================================================================

Created On: Jun 13, 2025 | Last Updated On: May 07, 2026

At the heart of PyTorch data loading utility is the [`torch.utils.data.DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
 class. It represents a Python iterable over a dataset, with support for

*   [map-style and iterable-style datasets](https://docs.pytorch.org/docs/2.15/data.html#dataset-types)
    ,
    
*   [customizing data loading order](https://docs.pytorch.org/docs/2.15/data.html#data-loading-order-and-sampler)
    ,
    
*   [automatic batching](https://docs.pytorch.org/docs/2.15/data.html#loading-batched-and-non-batched-data)
    ,
    
*   [single- and multi-process data loading](https://docs.pytorch.org/docs/2.15/data.html#single-and-multi-process-data-loading)
    ,
    
*   [automatic memory pinning](https://docs.pytorch.org/docs/2.15/data.html#memory-pinning)
    .
    

These options are configured by the constructor arguments of a [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
, which has signature:

DataLoader(dataset, batch\_size\=1, shuffle\=False, sampler\=None,
           batch\_sampler\=None, num\_workers\=0, collate\_fn\=None,
           pin\_memory\=False, drop\_last\=False, timeout\=0,
           worker\_init\_fn\=None, \*, prefetch\_factor\=2,
           persistent\_workers\=False)

Copy to clipboard

The sections below describe in details the effects and usages of these options.

Dataset Types[#](https://docs.pytorch.org/docs/2.15/data.html#dataset-types "Link to this heading")

----------------------------------------------------------------------------------------------------

The most important argument of [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
 constructor is [`dataset`](https://docs.pytorch.org/docs/2.15/utils.html#module-torch.utils.data.dataset "torch.utils.data.dataset")
, which indicates a dataset object to load data from. PyTorch supports two different types of datasets:

*   [Map-style datasets](https://docs.pytorch.org/docs/2.15/data.html#map-style-datasets)
    ,
    
*   [Iterable-style datasets](https://docs.pytorch.org/docs/2.15/data.html#iterable-style-datasets)
    .
    

### Map-style datasets[#](https://docs.pytorch.org/docs/2.15/data.html#map-style-datasets "Link to this heading")

A map-style dataset is one that implements the `__getitem__()` and `__len__()` protocols, and represents a map from (possibly non-integral) indices/keys to data samples.

For example, such a dataset, when accessed with `dataset[idx]`, could read the `idx`\-th image and its corresponding label from a folder on the disk.

See [`Dataset`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Dataset "torch.utils.data.Dataset")
 for more details.

### Iterable-style datasets[#](https://docs.pytorch.org/docs/2.15/data.html#iterable-style-datasets "Link to this heading")

An iterable-style dataset is an instance of a subclass of [`IterableDataset`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.IterableDataset "torch.utils.data.IterableDataset")
 that implements the `__iter__()` protocol, and represents an iterable over data samples. This type of datasets is particularly suitable for cases where random reads are expensive or even improbable, and where the batch size depends on the fetched data.

For example, such a dataset, when called `iter(dataset)`, could return a stream of data reading from a database, a remote server, or even logs generated in real time.

See [`IterableDataset`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.IterableDataset "torch.utils.data.IterableDataset")
 for more details.

Note

When using a [`IterableDataset`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.IterableDataset "torch.utils.data.IterableDataset")
 with [multi-process data loading](https://docs.pytorch.org/docs/2.15/data.html#multi-process-data-loading)
. The same dataset object is replicated on each worker process, and thus the replicas must be configured differently to avoid duplicated data. See [`IterableDataset`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.IterableDataset "torch.utils.data.IterableDataset")
 documentations for how to achieve this.

Data Loading Order and [`Sampler`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Sampler "torch.utils.data.Sampler")
[#](https://docs.pytorch.org/docs/2.15/data.html#data-loading-order-and-sampler "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For [iterable-style datasets](https://docs.pytorch.org/docs/2.15/data.html#iterable-style-datasets)
, data loading order is entirely controlled by the user-defined iterable. This allows easier implementations of chunk-reading and dynamic batch size (e.g., by yielding a batched sample at each time).

The rest of this section concerns the case with [map-style datasets](https://docs.pytorch.org/docs/2.15/data.html#map-style-datasets)
. [`torch.utils.data.Sampler`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Sampler "torch.utils.data.Sampler")
 classes are used to specify the sequence of indices/keys used in data loading. They represent iterable objects over the indices to datasets. E.g., in the common case with stochastic gradient decent (SGD), a [`Sampler`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Sampler "torch.utils.data.Sampler")
 could randomly permute a list of indices and yield each one at a time, or yield a small number of them for mini-batch SGD.

A sequential or shuffled sampler will be automatically constructed based on the `shuffle` argument to a [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
. Alternatively, users may use the [`sampler`](https://docs.pytorch.org/docs/2.15/utils.html#module-torch.utils.data.sampler "torch.utils.data.sampler")
 argument to specify a custom [`Sampler`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Sampler "torch.utils.data.Sampler")
 object that at each time yields the next index/key to fetch.

A custom [`Sampler`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Sampler "torch.utils.data.Sampler")
 that yields a list of batch indices at a time can be passed as the `batch_sampler` argument. Automatic batching can also be enabled via `batch_size` and `drop_last` arguments. See [the next section](https://docs.pytorch.org/docs/2.15/data.html#loading-batched-and-non-batched-data)
 for more details on this.

Note

Neither [`sampler`](https://docs.pytorch.org/docs/2.15/utils.html#module-torch.utils.data.sampler "torch.utils.data.sampler")
 nor `batch_sampler` is compatible with iterable-style datasets, since such datasets have no notion of a key or an index.

Loading Batched and Non-Batched Data[#](https://docs.pytorch.org/docs/2.15/data.html#loading-batched-and-non-batched-data "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

[`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
 supports automatically collating individual fetched data samples into batches via arguments `batch_size`, `drop_last`, `batch_sampler`, and `collate_fn` (which has a default function).

### Automatic batching (default)[#](https://docs.pytorch.org/docs/2.15/data.html#automatic-batching-default "Link to this heading")

This is the most common case, and corresponds to fetching a minibatch of data and collating them into batched samples, i.e., containing Tensors with one dimension being the batch dimension (usually the first).

When `batch_size` (default `1`) is not `None`, the data loader yields batched samples instead of individual samples. `batch_size` and `drop_last` arguments are used to specify how the data loader obtains batches of dataset keys. For map-style datasets, users can alternatively specify `batch_sampler`, which yields a list of keys at a time.

Note

The `batch_size` and `drop_last` arguments essentially are used to construct a `batch_sampler` from [`sampler`](https://docs.pytorch.org/docs/2.15/utils.html#module-torch.utils.data.sampler "torch.utils.data.sampler")
. For map-style datasets, the [`sampler`](https://docs.pytorch.org/docs/2.15/utils.html#module-torch.utils.data.sampler "torch.utils.data.sampler")
 is either provided by user or constructed based on the `shuffle` argument. For iterable-style datasets, the [`sampler`](https://docs.pytorch.org/docs/2.15/utils.html#module-torch.utils.data.sampler "torch.utils.data.sampler")
 is a dummy infinite one. See [this section](https://docs.pytorch.org/docs/2.15/data.html#data-loading-order-and-sampler)
 on more details on samplers.

Note

When fetching from [iterable-style datasets](https://docs.pytorch.org/docs/2.15/data.html#iterable-style-datasets)
 with [multi-processing](https://docs.pytorch.org/docs/2.15/data.html#multi-process-data-loading)
 the `drop_last` argument drops the last non-full batch of each worker’s dataset replica.

After fetching a list of samples using the indices from sampler, the function passed as the `collate_fn` argument is used to collate lists of samples into batches.

In this case, loading from a map-style dataset is roughly equivalent with:

for indices in batch\_sampler:
    yield collate\_fn(\[dataset\[i\] for i in indices\])

Copy to clipboard

and loading from an iterable-style dataset is roughly equivalent with:

dataset\_iter \= iter(dataset)
for indices in batch\_sampler:
    yield collate\_fn(\[next(dataset\_iter) for \_ in indices\])

Copy to clipboard

A custom `collate_fn` can be used to customize collation, e.g., padding sequential data to max length of a batch. See [this section](https://docs.pytorch.org/docs/2.15/data.html#dataloader-collate-fn)
 on more about `collate_fn`.

### Disable automatic batching[#](https://docs.pytorch.org/docs/2.15/data.html#disable-automatic-batching "Link to this heading")

In certain cases, users may want to handle batching manually in dataset code, or simply load individual samples. For example, it could be cheaper to directly load batched data (e.g., bulk reads from a database or reading continuous chunks of memory), or the batch size is data dependent, or the program is designed to work on individual samples. Under these scenarios, it’s likely better to not use automatic batching (where `collate_fn` is used to collate the samples), but let the data loader directly return each member of the [`dataset`](https://docs.pytorch.org/docs/2.15/utils.html#module-torch.utils.data.dataset "torch.utils.data.dataset")
 object.

When both `batch_size` and `batch_sampler` are `None` (default value for `batch_sampler` is already `None`), automatic batching is disabled. Each sample obtained from the [`dataset`](https://docs.pytorch.org/docs/2.15/utils.html#module-torch.utils.data.dataset "torch.utils.data.dataset")
 is processed with the function passed as the `collate_fn` argument.

**When automatic batching is disabled**, the default `collate_fn` simply converts NumPy arrays into PyTorch Tensors, and keeps everything else untouched.

In this case, loading from a map-style dataset is roughly equivalent with:

for index in sampler:
    yield collate\_fn(dataset\[index\])

Copy to clipboard

and loading from an iterable-style dataset is roughly equivalent with:

for data in iter(dataset):
    yield collate\_fn(data)

Copy to clipboard

See [this section](https://docs.pytorch.org/docs/2.15/data.html#dataloader-collate-fn)
 on more about `collate_fn`.

### Working with `collate_fn`[#](https://docs.pytorch.org/docs/2.15/data.html#working-with-collate-fn "Link to this heading")

The use of `collate_fn` is slightly different when automatic batching is enabled or disabled.

**When automatic batching is disabled**, `collate_fn` is called with each individual data sample, and the output is yielded from the data loader iterator. In this case, the default `collate_fn` simply converts NumPy arrays in PyTorch tensors.

**When automatic batching is enabled**, `collate_fn` is called with a list of data samples at each time. It is expected to collate the input samples into a batch for yielding from the data loader iterator. The rest of this section describes the behavior of the default `collate_fn` ([`default_collate()`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.default_collate "torch.utils.data.default_collate")
).

For instance, if each data sample consists of a 3-channel image and an integral class label, i.e., each element of the dataset returns a tuple `(image, class_index)`, the default `collate_fn` collates a list of such tuples into a single tuple of a batched image tensor and a batched class label Tensor. In particular, the default `collate_fn` has the following properties:

*   It always prepends a new dimension as the batch dimension.
    
*   It automatically converts NumPy arrays and Python numerical values into PyTorch Tensors.
    
*   It preserves the data structure, e.g., if each sample is a dictionary, it outputs a dictionary with the same set of keys but batched Tensors as values (or lists if the values can not be converted into Tensors). Same for `list` s, `tuple` s, `namedtuple` s, etc.
    

Users may use customized `collate_fn` to achieve custom batching, e.g., collating along a dimension other than the first, padding sequences of various lengths, or adding support for custom data types.

If you run into a situation where the outputs of [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
 have dimensions or type that is different from your expectation, you may want to check your `collate_fn`.

Single- and Multi-process Data Loading[#](https://docs.pytorch.org/docs/2.15/data.html#single-and-multi-process-data-loading "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

A [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
 uses single-process data loading by default.

Within a Python process, the [Global Interpreter Lock (GIL)](https://wiki.python.org/moin/GlobalInterpreterLock)
 prevents true fully parallelizing Python code across threads. To avoid blocking computation code with data loading, PyTorch provides an easy switch to perform multi-process data loading by simply setting the argument `num_workers` to a positive integer.

### Single-process data loading (default)[#](https://docs.pytorch.org/docs/2.15/data.html#single-process-data-loading-default "Link to this heading")

In this mode, data fetching is done in the same process a [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
 is initialized. Therefore, data loading may block computing. However, this mode may be preferred when resource(s) used for sharing data among processes (e.g., shared memory, file descriptors) is limited, or when the entire dataset is small and can be loaded entirely in memory. Additionally, single-process loading often shows more readable error traces and thus is useful for debugging.

### Multi-process data loading[#](https://docs.pytorch.org/docs/2.15/data.html#multi-process-data-loading "Link to this heading")

Setting the argument `num_workers` as a positive integer will turn on multi-process data loading with the specified number of loader worker processes.

Warning

After several iterations, the loader worker processes will consume the same amount of CPU memory as the parent process for all Python objects in the parent process which are accessed from the worker processes. This can be problematic if the Dataset contains a lot of data (e.g., you are loading a very large list of filenames at Dataset construction time) and/or you are using a lot of workers (overall memory usage is `number of workers * size of parent process`). The simplest workaround is to replace Python objects with non-refcounted representations such as Pandas, Numpy or PyArrow objects. Check out [issue #13246](https://github.com/pytorch/pytorch/issues/13246#issuecomment-905703662)
 for more details on why this occurs and example code for how to workaround these problems.

In this mode, each time an iterator of a [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
 is created (e.g., when you call `enumerate(dataloader)`), `num_workers` worker processes are created. At this point, the [`dataset`](https://docs.pytorch.org/docs/2.15/utils.html#module-torch.utils.data.dataset "torch.utils.data.dataset")
, `collate_fn`, and `worker_init_fn` are passed to each worker, where they are used to initialize, and fetch data. This means that dataset access together with its internal IO, transforms (including `collate_fn`) runs in the worker process.

[`torch.utils.data.get_worker_info()`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.get_worker_info "torch.utils.data.get_worker_info")
 returns various useful information in a worker process (including the worker id, dataset replica, initial seed, etc.), and returns `None` in main process. Users may use this function in dataset code and/or `worker_init_fn` to individually configure each dataset replica, and to determine whether the code is running in a worker process. For example, this can be particularly helpful in sharding the dataset.

For map-style datasets, the main process generates the indices using [`sampler`](https://docs.pytorch.org/docs/2.15/utils.html#module-torch.utils.data.sampler "torch.utils.data.sampler")
 and sends them to the workers. So any shuffle randomization is done in the main process which guides loading by assigning indices to load.

For iterable-style datasets, since each worker process gets a replica of the [`dataset`](https://docs.pytorch.org/docs/2.15/utils.html#module-torch.utils.data.dataset "torch.utils.data.dataset")
 object, naive multi-process loading will often result in duplicated data. Using [`torch.utils.data.get_worker_info()`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.get_worker_info "torch.utils.data.get_worker_info")
 and/or `worker_init_fn`, users may configure each replica independently. (See [`IterableDataset`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.IterableDataset "torch.utils.data.IterableDataset")
 documentations for how to achieve this. ) For similar reasons, in multi-process loading, the `drop_last` argument drops the last non-full batch of each worker’s iterable-style dataset replica.

Workers are shut down once the end of the iteration is reached, or when the iterator becomes garbage collected.

Warning

It is generally not recommended to return CUDA tensors in multi-process loading because of many subtleties in using CUDA and sharing CUDA tensors in multiprocessing (see [CUDA in multiprocessing](https://docs.pytorch.org/docs/2.15/notes/multiprocessing.html#multiprocessing-cuda-note)
). Instead, we recommend using [automatic memory pinning](https://docs.pytorch.org/docs/2.15/data.html#memory-pinning)
 (i.e., setting `pin_memory=True`), which enables fast data transfer to CUDA-enabled GPUs.

#### Platform-specific behaviors[#](https://docs.pytorch.org/docs/2.15/data.html#platform-specific-behaviors "Link to this heading")

Since workers rely on Python [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "(in Python v3.15)")
, worker launch behavior is different on Windows compared to Unix.

*   On Unix, The default [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "(in Python v3.15)")
     start method is `forkserver()` for Python >= 3.14; `fork()` for Python < 3.14. Using `fork()`, child workers typically can access the [`dataset`](https://docs.pytorch.org/docs/2.15/utils.html#module-torch.utils.data.dataset "torch.utils.data.dataset")
     and Python argument functions directly through the cloned address space. This can have a fast start up, but can lead to problems with multi-threaded applications. On Unix platforms that support it, `forkserver()` starts a separate server process first, and all new worker processes are then spawned by that server, providing safer isolation than `fork()` (especially with threads) while avoiding some of the overhead of pure `spawn()`.
    
*   On Windows and MacOS, `spawn()` is the default [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "(in Python v3.15)")
     start method. Using `spawn()`, another interpreter is launched which runs your main script, followed by the internal worker function that receives the [`dataset`](https://docs.pytorch.org/docs/2.15/utils.html#module-torch.utils.data.dataset "torch.utils.data.dataset")
    , `collate_fn` and other arguments through [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "(in Python v3.15)")
     serialization.
    

This separate serialization means that you should take two steps to ensure you are compatible with Windows while using multi-process data loading:

*   Wrap most of you main script’s code within `if __name__ == '__main__':` block, to make sure it doesn’t run again (most likely generating error) when each worker process is launched. You can place your dataset and [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
     instance creation logic here, as it doesn’t need to be re-executed in workers.
    
*   Make sure that any custom `collate_fn`, `worker_init_fn` or [`dataset`](https://docs.pytorch.org/docs/2.15/utils.html#module-torch.utils.data.dataset "torch.utils.data.dataset")
     code is declared as top level definitions, outside of the `__main__` check. This ensures that they are available in worker processes. (this is needed since functions are pickled as references only, not `bytecode`.)
    

#### Randomness in multi-process data loading[#](https://docs.pytorch.org/docs/2.15/data.html#randomness-in-multi-process-data-loading "Link to this heading")

By default, each worker will have its PyTorch seed set to `base_seed + worker_id`, where `base_seed` is a long generated by main process using its RNG (thereby, consuming a RNG state mandatorily) or a specified `generator`. However, seeds for other libraries may be duplicated upon initializing workers, causing each worker to return identical random numbers. (See [this section](https://docs.pytorch.org/docs/2.15/notes/faq.html#dataloader-workers-random-seed)
 in FAQ.).

In `worker_init_fn`, you may access the PyTorch seed set for each worker with either [`torch.utils.data.get_worker_info().seed`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.get_worker_info "torch.utils.data.get_worker_info")
 or [`torch.initial_seed()`](https://docs.pytorch.org/docs/2.15/generated/torch.initial_seed.html#torch.initial_seed "torch.initial_seed")
, and use it to seed other libraries before data loading.

Memory Pinning[#](https://docs.pytorch.org/docs/2.15/data.html#memory-pinning "Link to this heading")

------------------------------------------------------------------------------------------------------

Host to GPU copies are much faster when they originate from pinned (page-locked) memory. See [Use pinned memory buffers](https://docs.pytorch.org/docs/2.15/notes/cuda.html#cuda-memory-pinning)
 for more details on when and how to use pinned memory generally.

For data loading, passing `pin_memory=True` to a [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
 will automatically put the fetched data Tensors in pinned memory, and thus enables faster data transfer to CUDA-enabled GPUs.

The default memory pinning logic only recognizes Tensors and maps and iterables containing Tensors. By default, if the pinning logic sees a batch that is a custom type (which will occur if you have a `collate_fn` that returns a custom batch type), or if each element of your batch is a custom type, the pinning logic will not recognize them, and it will return that batch (or those elements) without pinning the memory. To enable memory pinning for custom batch or data type(s), define a `pin_memory()` method on your custom type(s).

See the example below.

Example:

class SimpleCustomBatch:
    def \_\_init\_\_(self, data):
        transposed\_data \= list(zip(\*data))
        self.inp \= torch.stack(transposed\_data\[0\], 0)
        self.tgt \= torch.stack(transposed\_data\[1\], 0)

    \# custom memory pinning method on custom type
    def pin\_memory(self):
        self.inp \= self.inp.pin\_memory()
        self.tgt \= self.tgt.pin\_memory()
        return self

def collate\_wrapper(batch):
    return SimpleCustomBatch(batch)

inps \= torch.arange(10 \* 5, dtype\=torch.float32).view(10, 5)
tgts \= torch.arange(10 \* 5, dtype\=torch.float32).view(10, 5)
dataset \= TensorDataset(inps, tgts)

loader \= DataLoader(dataset, batch\_size\=2, collate\_fn\=collate\_wrapper,
                    pin\_memory\=True)

for batch\_ndx, sample in enumerate(loader):
    print(sample.inp.is\_pinned())
    print(sample.tgt.is\_pinned())

Copy to clipboard

_class_ torch.utils.data.DataLoader(_dataset_, _batch\_size\=1_, _shuffle\=None_, _sampler\=None_, _batch\_sampler\=None_, _num\_workers\=0_, _collate\_fn\=None_, _pin\_memory\=False_, _drop\_last\=False_, _timeout\=0_, _worker\_init\_fn\=None_, _multiprocessing\_context\=None_, _generator\=None_, _\*_, _prefetch\_factor\=None_, _persistent\_workers\=False_, _pin\_memory\_device\=''_, _in\_order\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/dataloader.py#L149)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "Link to this definition")

Data loader combines a dataset and a sampler, and provides an iterable over the given dataset.

The [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
 supports both map-style and iterable-style datasets with single- or multi-process loading, customizing loading order and optional automatic batching (collation) and memory pinning.

See [`torch.utils.data`](https://docs.pytorch.org/docs/2.15/data.html#module-torch.utils.data "torch.utils.data")
 documentation page for more details.

Parameters:

*   **dataset** ([_Dataset_](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Dataset "torch.utils.data.Dataset")
    ) – dataset from which to load the data.
    
*   **batch\_size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – how many samples per batch to load (default: `1`).
    
*   **shuffle** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – set to `True` to have the data reshuffled at every epoch (default: `False`).
    
*   **sampler** ([_Sampler_](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Sampler "torch.utils.data.Sampler")
     _or_ _Iterable__,_ _optional_) – defines the strategy to draw samples from the dataset. Can be any `Iterable` with `__len__` implemented. If specified, `shuffle` must not be specified.
    
*   **batch\_sampler** ([_Sampler_](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Sampler "torch.utils.data.Sampler")
     _or_ _Iterable__,_ _optional_) – like [`sampler`](https://docs.pytorch.org/docs/2.15/utils.html#module-torch.utils.data.sampler "torch.utils.data.sampler")
    , but returns a batch of indices at a time. Mutually exclusive with `batch_size`, `shuffle`, [`sampler`](https://docs.pytorch.org/docs/2.15/utils.html#module-torch.utils.data.sampler "torch.utils.data.sampler")
    , and `drop_last`.
    
*   **num\_workers** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – how many subprocesses to use for data loading. `0` means that the data will be loaded in the main process. (default: `0`)
    
*   **collate\_fn** (_Callable__,_ _optional_) – merges a list of samples to form a mini-batch of Tensor(s). Used when using batched loading from a map-style dataset.
    
*   **pin\_memory** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True`, the data loader will copy Tensors into device/CUDA pinned memory before returning them. If your data elements are a custom type, or your `collate_fn` returns a batch that is a custom type, see the example below.
    
*   **drop\_last** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – set to `True` to drop the last incomplete batch, if the dataset size is not divisible by the batch size. If `False` and the size of dataset is not divisible by the batch size, then the last batch will be smaller. (default: `False`)
    
*   **timeout** (_numeric__,_ _optional_) – if positive, the timeout value for collecting a batch from workers. Should always be non-negative. (default: `0`)
    
*   **worker\_init\_fn** (_Callable__,_ _optional_) – If not `None`, this will be called on each worker subprocess with the worker id (an int in `[0, num_workers - 1]`) as input, after seeding and before data loading. (default: `None`)
    
*   **multiprocessing\_context** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _or_ _multiprocessing.context.BaseContext__,_ _optional_) – If `None`, the default [multiprocessing context](https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods)
     # noqa: D401 of your operating system will be used. (default: `None`)
    
*   **generator** ([_torch.Generator_](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch.Generator")
    _,_ _optional_) – If not `None`, this RNG will be used by RandomSampler to generate random indexes and multiprocessing to generate `base_seed` for workers. (default: `None`)
    
*   **prefetch\_factor** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional__,_ _keyword-only arg_) – Number of batches loaded in advance by each worker. `2` means there will be a total of 2 \* num\_workers batches prefetched across all workers. (default value depends on the set value for num\_workers. If value of num\_workers=0 default is `None`. Otherwise, if value of `num_workers > 0` default is `2`).
    
*   **persistent\_workers** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True`, the data loader will not shut down the worker processes after a dataset has been consumed once. This allows to maintain the workers Dataset instances alive. (default: `False`)
    
*   **pin\_memory\_device** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – Deprecated, the current [accelerator](https://docs.pytorch.org/docs/2.15/torch.html#accelerators)
     will be used as the device if `pin_memory=True`.
    
*   **in\_order** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `False`, the data loader will not enforce that batches are returned in a first-in, first-out order. Only applies when `num_workers > 0`. (default: `True`)
    

Warning

If the `spawn` start method is used, `worker_init_fn` cannot be an unpicklable object, e.g., a lambda function. See [Multiprocessing best practices](https://docs.pytorch.org/docs/2.15/notes/multiprocessing.html#multiprocessing-best-practices)
 on more details related to multiprocessing in PyTorch.

Warning

`len(dataloader)` heuristic is based on the length of the sampler used. When [`dataset`](https://docs.pytorch.org/docs/2.15/utils.html#module-torch.utils.data.dataset "torch.utils.data.dataset")
 is an [`IterableDataset`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.IterableDataset "torch.utils.data.IterableDataset")
, it instead returns an estimate based on `len(dataset) / batch_size`, with proper rounding depending on `drop_last`, regardless of multi-process loading configurations. This represents the best guess PyTorch can make because PyTorch trusts user [`dataset`](https://docs.pytorch.org/docs/2.15/utils.html#module-torch.utils.data.dataset "torch.utils.data.dataset")
 code in correctly handling multi-process loading to avoid duplicate data.

However, if sharding results in multiple workers having incomplete last batches, this estimate can still be inaccurate, because (1) an otherwise complete batch can be broken into multiple ones and (2) more than one batch worth of samples can be dropped when `drop_last` is set. Unfortunately, PyTorch can not detect such cases in general.

See [Dataset Types](https://docs.pytorch.org/docs/2.15/data.html#id1)
 for more details on these two types of datasets and how [`IterableDataset`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.IterableDataset "torch.utils.data.IterableDataset")
 interacts with [Multi-process data loading](https://docs.pytorch.org/docs/2.15/data.html#id10)
.

Warning

See [Reproducibility](https://docs.pytorch.org/docs/2.15/notes/randomness.html#reproducibility)
, and [My data loader workers return identical random numbers](https://docs.pytorch.org/docs/2.15/notes/faq.html#dataloader-workers-random-seed)
, and [Randomness in multi-process data loading](https://docs.pytorch.org/docs/2.15/data.html#data-loading-randomness)
 notes for random seed related questions.

Warning

Setting in\_order to False can harm reproducibility and may lead to a skewed data distribution being fed to the trainer in cases with imbalanced data.

_class_ torch.utils.data.Dataset[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/dataset.py#L39)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Dataset "Link to this definition")

An abstract class representing a [`Dataset`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Dataset "torch.utils.data.Dataset")
.

All datasets that represent a map from keys to data samples should subclass it. All subclasses should overwrite `__getitem__()`, supporting fetching a data sample for a given key. Subclasses could also optionally overwrite `__len__()`, which is expected to return the size of the dataset by many [`Sampler`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Sampler "torch.utils.data.Sampler")
 implementations and the default options of [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
. Subclasses could also optionally implement `__getitems__()`, for speedup batched samples loading. This method accepts list of indices of samples of batch and returns list of samples.

Note

[`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
 by default constructs an index sampler that yields integral indices. To make it work with a map-style dataset with non-integral indices/keys, a custom sampler must be provided.

_class_ torch.utils.data.IterableDataset[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/dataset.py#L73)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.IterableDataset "Link to this definition")

An iterable Dataset.

All datasets that represent an iterable of data samples should subclass it. Such form of datasets is particularly useful when data come from a stream.

All subclasses should overwrite `__iter__()`, which would return an iterator of samples in this dataset.

When a subclass is used with [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
, each item in the dataset will be yielded from the [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
 iterator. When `num_workers > 0`, each worker process will have a different copy of the dataset object, so it is often desired to configure each copy independently to avoid having duplicate data returned from the workers. [`get_worker_info()`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.get_worker_info "torch.utils.data.get_worker_info")
, when called in a worker process, returns information about the worker. It can be used in either the dataset’s `__iter__()` method or the [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
 ‘s `worker_init_fn` option to modify each copy’s behavior.

Example 1: splitting workload across all workers in `__iter__()`:

\>>> class MyIterableDataset(torch.utils.data.IterableDataset):
...     def \_\_init\_\_(self, start, end):
...         super(MyIterableDataset).\_\_init\_\_()
...         assert end \> start, "this example only works with end >= start"
...         self.start \= start
...         self.end \= end
...
...     def \_\_iter\_\_(self):
...         worker\_info \= torch.utils.data.get\_worker\_info()
...         if worker\_info is None:  \# single-process data loading, return the full iterator
...             iter\_start \= self.start
...             iter\_end \= self.end
...         else:  \# in a worker process
...             \# split workload
...             per\_worker \= int(math.ceil((self.end \- self.start) / float(worker\_info.num\_workers)))
...             worker\_id \= worker\_info.id
...             iter\_start \= self.start + worker\_id \* per\_worker
...             iter\_end \= min(iter\_start + per\_worker, self.end)
...         return iter(range(iter\_start, iter\_end))
...
\>>> \# should give same set of data as range(3, 7), i.e., \[3, 4, 5, 6\].
\>>> ds \= MyIterableDataset(start\=3, end\=7)

\>>> \# Single-process loading
\>>> print(list(torch.utils.data.DataLoader(ds, num\_workers\=0)))
\[tensor(\[3\]), tensor(\[4\]), tensor(\[5\]), tensor(\[6\])\]

\>>> \# Multi-process loading with two worker processes
\>>> \# Worker 0 fetched \[3, 4\].  Worker 1 fetched \[5, 6\].
\>>> print(list(torch.utils.data.DataLoader(ds, num\_workers\=2)))
\[tensor(\[3\]), tensor(\[5\]), tensor(\[4\]), tensor(\[6\])\]

\>>> \# With even more workers
\>>> print(list(torch.utils.data.DataLoader(ds, num\_workers\=12)))
\[tensor(\[3\]), tensor(\[5\]), tensor(\[4\]), tensor(\[6\])\]

Copy to clipboard

Example 2: splitting workload across all workers using `worker_init_fn`:

\>>> class MyIterableDataset(torch.utils.data.IterableDataset):
...     def \_\_init\_\_(self, start, end):
...         super(MyIterableDataset).\_\_init\_\_()
...         assert end \> start, "this example only works with end >= start"
...         self.start \= start
...         self.end \= end
...
...     def \_\_iter\_\_(self):
...         return iter(range(self.start, self.end))
...
\>>> \# should give same set of data as range(3, 7), i.e., \[3, 4, 5, 6\].
\>>> ds \= MyIterableDataset(start\=3, end\=7)

\>>> \# Single-process loading
\>>> print(list(torch.utils.data.DataLoader(ds, num\_workers\=0)))
\[3, 4, 5, 6\]
\>>>
\>>> \# Directly doing multi-process loading yields duplicate data
\>>> print(list(torch.utils.data.DataLoader(ds, num\_workers\=2)))
\[3, 3, 4, 4, 5, 5, 6, 6\]

\>>> \# Define a \`worker\_init\_fn\` that configures each dataset copy differently
\>>> def worker\_init\_fn(worker\_id):
...     worker\_info \= torch.utils.data.get\_worker\_info()
...     dataset \= worker\_info.dataset  \# the dataset copy in this worker process
...     overall\_start \= dataset.start
...     overall\_end \= dataset.end
...     \# configure the dataset to only process the split workload
...     per\_worker \= int(math.ceil((overall\_end \- overall\_start) / float(worker\_info.num\_workers)))
...     worker\_id \= worker\_info.id
...     dataset.start \= overall\_start + worker\_id \* per\_worker
...     dataset.end \= min(dataset.start + per\_worker, overall\_end)
...

\>>> \# Multi-process loading with the custom \`worker\_init\_fn\`
\>>> \# Worker 0 fetched \[3, 4\].  Worker 1 fetched \[5, 6\].
\>>> print(list(torch.utils.data.DataLoader(ds, num\_workers\=2, worker\_init\_fn\=worker\_init\_fn)))
\[3, 5, 4, 6\]

\>>> \# With even more workers
\>>> print(list(torch.utils.data.DataLoader(ds, num\_workers\=12, worker\_init\_fn\=worker\_init\_fn)))
\[3, 4, 5, 6\]

Copy to clipboard

_class_ torch.utils.data.TensorDataset(_\*tensors_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/dataset.py#L189)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.TensorDataset "Link to this definition")

Dataset wrapping tensors.

Each sample will be retrieved by indexing tensors along the first dimension.

Parameters:

**\*tensors** ([_Tensor_](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
) – tensors that have the same size of the first dimension.

_class_ torch.utils.data.StackDataset(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/dataset.py#L212)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.StackDataset "Link to this definition")

Dataset as a stacking of multiple datasets.

This class is useful to assemble different parts of complex input data, given as datasets.

Example

\>>> images \= ImageDataset()
\>>> texts \= TextDataset()
\>>> tuple\_stack \= StackDataset(images, texts)
\>>> tuple\_stack\[0\] \== (images\[0\], texts\[0\])
\>>> dict\_stack \= StackDataset(image\=images, text\=texts)
\>>> dict\_stack\[0\] \== {"image": images\[0\], "text": texts\[0\]}

Copy to clipboard

Parameters:

*   **\*args** ([_Dataset_](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Dataset "torch.utils.data.Dataset")
    ) – Datasets for stacking returned as tuple.
    
*   **\*\*kwargs** ([_Dataset_](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Dataset "torch.utils.data.Dataset")
    ) – Datasets for stacking returned as dict.
    

_class_ torch.utils.data.ConcatDataset(_datasets_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/dataset.py#L299)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.ConcatDataset "Link to this definition")

Dataset as a concatenation of multiple datasets.

This class is useful to assemble different existing datasets.

Parameters:

**datasets** (_sequence_) – List of datasets to be concatenated

_class_ torch.utils.data.ChainDataset(_datasets_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/dataset.py#L356)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.ChainDataset "Link to this definition")

Dataset for chaining multiple [`IterableDataset`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.IterableDataset "torch.utils.data.IterableDataset")
 s.

This class is useful to assemble different existing dataset streams. The chaining operation is done on-the-fly, so concatenating large-scale datasets with this class will be efficient.

Parameters:

**datasets** (_iterable_ _of_ [_IterableDataset_](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.IterableDataset "torch.utils.data.IterableDataset")
) – datasets to be chained together

_class_ torch.utils.data.Subset(_dataset_, _indices_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/dataset.py#L386)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Subset "Link to this definition")

Subset of a dataset at specified indices.

Note

When subclassing Subset and overriding \_\_getitem\_\_, you **must** also override \_\_getitems\_\_ to ensure DataLoader works correctly with your custom logic. If you override only \_\_getitem\_\_, a NotImplementedError will be raised when using DataLoader.

A simple implementation of \_\_getitems\_\_ can delegate to \_\_getitem\_\_:

def \_\_getitems\_\_(self, indices):
    return \[self.\_\_getitem\_\_(idx) for idx in indices\]

Copy to clipboard

For better performance, consider implementing batch-aware logic in \_\_getitems\_\_ instead of calling \_\_getitem\_\_ multiple times.

Parameters:

*   **dataset** ([_Dataset_](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Dataset "torch.utils.data.Dataset")
    ) – The whole Dataset
    
*   **indices** (_sequence_) – Indices in the whole set selected for subset
    

torch.utils.data.\_utils.collate.collate(_batch_, _\*_, _collate\_fn\_map\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/_utils/collate.py#L118)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data._utils.collate.collate "Link to this definition")

General collate function that handles collection type of element within each batch.

The function also opens function registry to deal with specific element types. default\_collate\_fn\_map provides default collate functions for tensors, numpy arrays, numbers and strings.

Parameters:

*   **batch** – a single batch to be collated
    
*   **collate\_fn\_map** ([_dict_](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
    _\[_[_type_](https://docs.python.org/3/builtins/functions.html#type "(in Python v3.15)")\
     _|_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
    _\[_[_type_](https://docs.python.org/3/builtins/functions.html#type "(in Python v3.15)")\
    _,_ _...__\]__,_ [_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")\
    _\]_ _|_ _None_) – Optional dictionary mapping from element type to the corresponding collate function. If the element type isn’t present in this dictionary, this function will go through each key of the dictionary in the insertion order to invoke the corresponding collate function if the element type is a subclass of the key.
    

Examples

\>>> def collate\_tensor\_fn(batch, \*, collate\_fn\_map):
...     \# Extend this function to handle batch of tensors
...     return torch.stack(batch, 0)
\>>> def custom\_collate(batch):
...     collate\_map \= {torch.Tensor: collate\_tensor\_fn}
...     return collate(batch, collate\_fn\_map\=collate\_map)
\>>> \# Extend \`default\_collate\` by in-place modifying \`default\_collate\_fn\_map\`
\>>> default\_collate\_fn\_map.update({torch.Tensor: collate\_tensor\_fn})

Copy to clipboard

Note

Each collate function requires a positional argument for batch and a keyword argument for the dictionary of collate functions as collate\_fn\_map.

torch.utils.data.default\_collate(_batch_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/_utils/collate.py#L340)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.default_collate "Link to this definition")

Take in a batch of data and put the elements within the batch into a tensor with an additional outer dimension - batch size.

The exact output type can be a [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
, a Sequence of [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
, a Collection of [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
, or left unchanged, depending on the input type. This is used as the default function for collation when batch\_size or batch\_sampler is defined in [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
.

Here is the general input type (based on the type of the element within the batch) to output type mapping:

> *   [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
>      -> [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
>      (with an added outer dimension batch size)
>     
> *   NumPy Arrays -> [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
>     
> *   float -> [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
>     
> *   int -> [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
>     
> *   str -> str (unchanged)
>     
> *   bytes -> bytes (unchanged)
>     
> *   Mapping\[K, V\_i\] -> Mapping\[K, default\_collate(\[V\_1, V\_2, …\])\]
>     
> *   NamedTuple\[V1\_i, V2\_i, …\] -> NamedTuple\[default\_collate(\[V1\_1, V1\_2, …\]), default\_collate(\[V2\_1, V2\_2, …\]), …\]
>     
> *   Sequence\[V1\_i, V2\_i, …\] -> Sequence\[default\_collate(\[V1\_1, V1\_2, …\]), default\_collate(\[V2\_1, V2\_2, …\]), …\]
>     

Parameters:

**batch** – a single batch to be collated

Examples

\>>> \# Example with a batch of \`int\`s:
\>>> default\_collate(\[0, 1, 2, 3\])
tensor(\[0, 1, 2, 3\])
\>>> \# Example with a batch of \`str\`s:
\>>> default\_collate(\["a", "b", "c"\])
\['a', 'b', 'c'\]
\>>> \# Example with \`Map\` inside the batch:
\>>> default\_collate(\[{"A": 0, "B": 1}, {"A": 100, "B": 100}\])
{'A': tensor(\[  0, 100\]), 'B': tensor(\[  1, 100\])}
\>>> \# Example with \`NamedTuple\` inside the batch:
\>>> Point \= namedtuple("Point", \["x", "y"\])
\>>> default\_collate(\[Point(0, 0), Point(1, 1)\])
Point(x=tensor(\[0, 1\]), y=tensor(\[0, 1\]))
\>>> \# Example with \`Tuple\` inside the batch:
\>>> default\_collate(\[(0, 1), (2, 3)\])
\[tensor(\[0, 2\]), tensor(\[1, 3\])\]
\>>> \# Example with \`List\` inside the batch:
\>>> default\_collate(\[\[0, 1\], \[2, 3\]\])
\[tensor(\[0, 2\]), tensor(\[1, 3\])\]
\>>> \# Two options to extend \`default\_collate\` to handle specific type
\>>> \# Option 1: Write custom collate function and invoke \`default\_collate\`
\>>> def custom\_collate(batch):
...     elem \= batch\[0\]
...     if isinstance(elem, CustomType):  \# Some custom condition
...         return ...
...     else:  \# Fall back to \`default\_collate\`
...         return default\_collate(batch)
\>>> \# Option 2: In-place modify \`default\_collate\_fn\_map\`
\>>> def collate\_customtype\_fn(batch, \*, collate\_fn\_map\=None):
...     return ...
\>>> default\_collate\_fn\_map.update(CustomType, collate\_customtype\_fn)
\>>> default\_collate(batch)  \# Handle \`CustomType\` automatically

Copy to clipboard

torch.utils.data.default\_convert(_data_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/_utils/collate.py#L23)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.default_convert "Link to this definition")

Convert each NumPy array element into a [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
.

If the input is a Sequence, Collection, or Mapping, it tries to convert each element inside to a [`torch.Tensor`](https://docs.pytorch.org/docs/2.15/tensors.html#torch.Tensor "torch.Tensor")
. If the input is not a NumPy array, it is left unchanged. This is used as the default function for collation when both batch\_sampler and batch\_size are NOT defined in [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
.

The general input type to output type mapping is similar to that of [`default_collate()`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.default_collate "torch.utils.data.default_collate")
. See the description there for more details.

Parameters:

**data** – a single data point to be converted

Examples

\>>> \# Example with \`int\`
\>>> default\_convert(0)
0
\>>> \# Example with NumPy array
\>>> default\_convert(np.array(\[0, 1\]))
tensor(\[0, 1\])
\>>> \# Example with NamedTuple
\>>> Point \= namedtuple("Point", \["x", "y"\])
\>>> default\_convert(Point(0, 0))
Point(x=0, y=0)
\>>> default\_convert(Point(np.array(0), np.array(0)))
Point(x=tensor(0), y=tensor(0))
\>>> \# Example with List
\>>> default\_convert(\[np.array(\[0, 1\]), np.array(\[2, 3\])\])
\[tensor(\[0, 1\]), tensor(\[2, 3\])\]

Copy to clipboard

torch.utils.data.get\_worker\_info()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/_utils/worker.py#L99)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.get_worker_info "Link to this definition")

Returns the information about the current [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
 iterator worker process.

When called in a worker, this returns an object guaranteed to have the following attributes:

*   `id`: the current worker id.
    
*   `num_workers`: the total number of workers.
    
*   `seed`: the random seed set for the current worker. This value is determined by main process RNG and the worker id. See [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
    ’s documentation for more details.
    
*   [`dataset`](https://docs.pytorch.org/docs/2.15/utils.html#module-torch.utils.data.dataset "torch.utils.data.dataset")
    : the copy of the dataset object in **this** process. Note that this will be a different object in a different process than the one in the main process.
    

When called in the main process, this returns `None`.

Note

When used in a `worker_init_fn` passed over to [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
, this method can be useful to set up each worker process differently, for instance, using `worker_id` to configure the `dataset` object to only read a specific fraction of a sharded dataset, or use `seed` to seed other libraries used in dataset code.

Return type:

_WorkerInfo_ | None

torch.utils.data.dataset.random\_split(_dataset_, _lengths_, _generator=<torch.\_C.Generator object>_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/dataset.py#L449)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.dataset.random_split "Link to this definition")

Randomly split a dataset into non-overlapping new datasets of given lengths.

If a list of fractions that sum up to 1 is given, the lengths will be computed automatically as floor(frac \* len(dataset)) for each fraction provided.

After computing the lengths, if there are any remainders, 1 count will be distributed in round-robin fashion to the lengths until there are no remainders left.

Optionally fix the generator for reproducible results, e.g.:

Example

\>>> generator1 \= torch.Generator().manual\_seed(42)
\>>> generator2 \= torch.Generator().manual\_seed(42)
\>>> random\_split(range(10), \[3, 7\], generator\=generator1)
\>>> random\_split(range(30), \[0.3, 0.3, 0.4\], generator\=generator2)

Copy to clipboard

Parameters:

*   **dataset** ([_Dataset_](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Dataset "torch.utils.data.dataset.Dataset")
    ) – Dataset to be split
    
*   **lengths** (_sequence_) – lengths or fractions of splits to be produced
    
*   **generator** ([_Generator_](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch.Generator")
    ) – Generator used for the random permutation.
    

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[_Subset_](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Subset "torch.utils.data.dataset.Subset")\
\[_\_T_\]\]

_class_ torch.utils.data.Sampler[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/sampler.py#L28)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Sampler "Link to this definition")

Base class for all Samplers.

Every Sampler subclass has to provide an `__iter__()` method, providing a way to iterate over indices or lists of indices (batches) of dataset elements, and may provide a `__len__()` method that returns the length of the returned iterators.

Example

\>>> class AccedingSequenceLengthSampler(Sampler\[int\]):
\>>>     def \_\_init\_\_(self, data: List\[str\]) \-> None:
\>>>         self.data \= data
\>>>
\>>>     def \_\_len\_\_(self) \-> int:
\>>>         return len(self.data)
\>>>
\>>>     def \_\_iter\_\_(self) \-> Iterator\[int\]:
\>>>         sizes \= torch.tensor(\[len(x) for x in self.data\])
\>>>         yield from torch.argsort(sizes).tolist()
\>>>
\>>> class AccedingSequenceLengthBatchSampler(Sampler\[List\[int\]\]):
\>>>     def \_\_init\_\_(self, data: List\[str\], batch\_size: int) \-> None:
\>>>         self.data \= data
\>>>         self.batch\_size \= batch\_size
\>>>
\>>>     def \_\_len\_\_(self) \-> int:
\>>>         return (len(self.data) + self.batch\_size \- 1) // self.batch\_size
\>>>
\>>>     def \_\_iter\_\_(self) \-> Iterator\[List\[int\]\]:
\>>>         sizes \= torch.tensor(\[len(x) for x in self.data\])
\>>>         for batch in torch.chunk(torch.argsort(sizes), len(self)):
\>>>             yield batch.tolist()

Copy to clipboard

Note

The `__len__()` method isn’t strictly required by [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
, but is expected in any calculation involving the length of a [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
.

_class_ torch.utils.data.SequentialSampler(_data\_source_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/sampler.py#L97)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.SequentialSampler "Link to this definition")

Samples elements sequentially, always in the same order.

Parameters:

**data\_source** (_Sized_) – data source to sample from. Must implement \_\_len\_\_.

_class_ torch.utils.data.RandomSampler(_data\_source_, _replacement\=False_, _num\_samples\=None_, _generator\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/sampler.py#L116)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.RandomSampler "Link to this definition")

Samples elements randomly. If without replacement, then sample from a shuffled dataset.

If with replacement, then user can specify `num_samples` to draw.

Parameters:

*   **data\_source** (_Sized_) – data source to sample from. Must implement \_\_len\_\_.
    
*   **replacement** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – samples are drawn on-demand with replacement if `True`, default=\`\`False\`\`
    
*   **num\_samples** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – number of samples to draw, default=\`len(dataset)\`.
    
*   **generator** ([_Generator_](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch.Generator")
    ) – Generator used in sampling.
    

_class_ torch.utils.data.SubsetRandomSampler(_indices_, _generator\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/sampler.py#L191)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.SubsetRandomSampler "Link to this definition")

Samples elements randomly from a given list of indices, without replacement.

Parameters:

*   **indices** (_sequence_) – a sequence of indices
    
*   **generator** ([_Generator_](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch.Generator")
    ) – Generator used in sampling.
    

_class_ torch.utils.data.WeightedRandomSampler(_weights_, _num\_samples_, _replacement\=True_, _generator\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/sampler.py#L213)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.WeightedRandomSampler "Link to this definition")

Samples elements from `[0,..,len(weights)-1]` with given probabilities (weights).

Parameters:

*   **weights** (_sequence_) – a sequence of weights, not necessary summing up to one
    
*   **num\_samples** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – number of samples to draw
    
*   **replacement** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – if `True`, samples are drawn with replacement. If not, they are drawn without replacement, which means that when a sample index is drawn for a row, it cannot be drawn again for that row.
    
*   **generator** ([_Generator_](https://docs.pytorch.org/docs/2.15/generated/torch.Generator.html#torch.Generator "torch.Generator")
    ) – Generator used in sampling.
    

Example

\>>> list(
...     WeightedRandomSampler(
...         \[0.1, 0.9, 0.4, 0.7, 3.0, 0.6\], 5, replacement\=True
...     )
... )
\[4, 4, 1, 4, 5\]
\>>> list(
...     WeightedRandomSampler(
...         \[0.9, 0.4, 0.05, 0.2, 0.3, 0.1\], 5, replacement\=False
...     )
... )
\[0, 1, 4, 3, 2\]

Copy to clipboard

_class_ torch.utils.data.BatchSampler(_sampler_, _batch\_size_, _drop\_last_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/sampler.py#L286)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.BatchSampler "Link to this definition")

Wraps another sampler to yield a mini-batch of indices.

Parameters:

*   **sampler** ([_Sampler_](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Sampler "torch.utils.data.Sampler")
     _or_ _Iterable_) – Base sampler. Can be any iterable object
    
*   **batch\_size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – Size of mini-batch.
    
*   **drop\_last** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If `True`, the sampler will drop the last batch if its size would be less than `batch_size`
    

Example

\>>> list(
...     BatchSampler(
...         SequentialSampler(range(10)), batch\_size\=3, drop\_last\=False
...     )
... )
\[\[0, 1, 2\], \[3, 4, 5\], \[6, 7, 8\], \[9\]\]
\>>> list(
...     BatchSampler(SequentialSampler(range(10)), batch\_size\=3, drop\_last\=True)
... )
\[\[0, 1, 2\], \[3, 4, 5\], \[6, 7, 8\]\]

Copy to clipboard

_class_ torch.utils.data.distributed.DistributedSampler(_dataset_, _num\_replicas\=None_, _rank\=None_, _shuffle\=True_, _seed\=0_, _drop\_last\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/distributed.py#L17)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.distributed.DistributedSampler "Link to this definition")

Sampler that restricts data loading to a subset of the dataset.

It is especially useful in conjunction with [`torch.nn.parallel.DistributedDataParallel`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")
. In such a case, each process can pass a `DistributedSampler` instance as a [`DataLoader`](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader")
 sampler, and load a subset of the original dataset that is exclusive to it.

Note

Dataset is assumed to be of constant size and that any instance of it always returns the same elements in the same order.

Parameters:

*   **dataset** ([_Dataset_](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.Dataset "torch.utils.data.dataset.Dataset")
    ) – Dataset used for sampling.
    
*   **num\_replicas** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – Number of processes participating in distributed training. By default, `world_size` is retrieved from the current distributed group.
    
*   **rank** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – Rank of the current process within `num_replicas`. By default, `rank` is retrieved from the current distributed group.
    
*   **shuffle** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True` (default), sampler will shuffle the indices.
    
*   **seed** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    _,_ _optional_) – random seed used to shuffle the sampler if `shuffle=True`. This number should be identical across all processes in the distributed group. Default: `0`.
    
*   **drop\_last** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – if `True`, then the sampler will drop the tail of the data to make it evenly divisible across the number of replicas. If `False`, the sampler will add extra indices to make the data evenly divisible across the replicas. Default: `False`.
    

Warning

In distributed mode, calling the `set_epoch()` method at the beginning of each epoch **before** creating the `DataLoader` iterator is necessary to make shuffling work properly across multiple epochs. Otherwise, the same ordering will be always used.

Example:

\>>> sampler \= DistributedSampler(dataset) if is\_distributed else None
\>>> loader \= DataLoader(dataset, shuffle\=(sampler is None),
...                     sampler\=sampler)
\>>> for epoch in range(start\_epoch, n\_epochs):
...     if is\_distributed:
...         sampler.set\_epoch(epoch)
...     train(loader)

Copy to clipboard

torch.utils.data.graph.traverse(_datapipe_, _only\_datapipe\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/graph.py#L109)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.graph.traverse "Link to this definition")

Traverse the DataPipes and their attributes to extract the DataPipe graph.

\[Deprecated\] When `only_dataPipe` is specified as `True`, it would only look into the attribute from each DataPipe that is either a DataPipe and a Python collection object such as `list`, `tuple`, `set` and `dict`.

Note

This function is deprecated. Please use traverse\_dps instead.

Parameters:

*   **datapipe** (_IterDataPipe_ _|_ _MapDataPipe_) – the end DataPipe of the graph
    
*   **only\_datapipe** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
     _|_ _None_) – If `False` (default), all attributes of each DataPipe are traversed. This argument is deprecated and will be removed after the next release.
    

Returns:

A graph represented as a nested dictionary, where keys are ids of DataPipe instances and values are tuples of DataPipe instance and the sub-graph

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[_IterDataPipe_ | _MapDataPipe_, [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[_IterDataPipe_ | _MapDataPipe_, DataPipeGraph\]\]\]\]

torch.utils.data.graph.traverse\_dps(_datapipe_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/graph.py#L91)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.graph.traverse_dps "Link to this definition")

Traverse the DataPipes and their attributes to extract the DataPipe graph.

This only looks into the attribute from each DataPipe that is either a DataPipe and a Python collection object such as `list`, `tuple`, `set` and `dict`.

Parameters:

**datapipe** (_IterDataPipe_ _|_ _MapDataPipe_) – the end DataPipe of the graph

Returns:

A graph represented as a nested dictionary, where keys are ids of DataPipe instances and values are tuples of DataPipe instance and the sub-graph

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[_IterDataPipe_ | _MapDataPipe_, [dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
\[_IterDataPipe_ | _MapDataPipe_, DataPipeGraph\]\]\]\]

torch.utils.data.datapipes.utils.decoder.basichandlers(_extension_, _data_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/datapipes/utils/decoder.py#L32)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.datapipes.utils.decoder.basichandlers "Link to this definition")

Transforms raw data (byte stream) into python objects.

Looks at the extension and loads the data into a python object supporting the corresponding extension.

Parameters:

*   **extension** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The file extension
    
*   **data** (_byte stream_) – Data to load into a python object.
    

Returns:

The data loaded into a corresponding python object

supporting the extension.

Return type:

[object](https://docs.python.org/3/builtins/functions.html#object "(in Python v3.15)")

Example

\>>> import pickle
\>>> data \= pickle.dumps("some data")
\>>> new\_data \= basichandlers("pickle", data)
\>>> new\_data
some data

Copy to clipboard

The transformation of data for extensions are:

*   txt, text, transcript: utf-8 decoded data of str format
    
*   cls, cls2, class, count, index, inx, id: int
    
*   json, jsn: json loaded data
    
*   pickle, pyd: pickle loaded data
    
*   pt: torch loaded data
    

torch.utils.data.datapipes.utils.decoder.handle\_extension(_extensions_, _f_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/datapipes/utils/decoder.py#L115)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.datapipes.utils.decoder.handle_extension "Link to this definition")

Return a decoder handler function for the list of extensions.

Extensions can be a space separated list of extensions. Extensions can contain dots, in which case the corresponding number of extension components must be present in the key given to f. Comparisons are case insensitive. Examples: handle\_extension(“jpg jpeg”, my\_decode\_jpg) # invoked for any file.jpg handle\_extension(“seg.jpg”, special\_case\_jpg) # invoked only for file.seg.jpg

torch.utils.data.datapipes.utils.common.validate\_input\_col(_fn_, _input\_col_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/utils/data/datapipes/utils/common.py#L28)
[#](https://docs.pytorch.org/docs/2.15/data.html#torch.utils.data.datapipes.utils.common.validate_input_col "Link to this definition")

Check that function used in a callable datapipe works with the input column.

This simply ensures that the number of positional arguments matches the size of the input column. The function must not contain any non-default keyword-only arguments.

Examples

\>>> def f(a, b, \*, c\=1):
\>>>     return a + b + c
\>>> def f\_def(a, b\=1, \*, c\=1):
\>>>     return a + b + c
\>>> assert validate\_input\_col(f, \[1, 2\])
\>>> assert validate\_input\_col(f\_def, 1)
\>>> assert validate\_input\_col(f\_def, \[1, 2\])

Copy to clipboard

Notes

If the function contains variable positional (`inspect.VAR_POSITIONAL`) arguments, for example, `f(a, *args)`, the validator will accept any size of input column greater than or equal to the number of positional arguments. (in this case, 1).

Parameters:

*   **fn** ([_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
    ) – The function to check.
    
*   **input\_col** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ [_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
     _|_ [_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
     _|_ _None_) – The input column to check.
    

Raises:

[**ValueError**](https://docs.python.org/3/builtins/exceptions.html#ValueError "(in Python v3.15)")
 – If the function is not compatible with the input column.

|     |     |
| --- | --- |
| [`StreamReaderIterDataPipe`](https://docs.pytorch.org/docs/2.15/generated/torch.utils.data.datapipes.iter.streamreader.StreamReaderIterDataPipe.html#torch.utils.data.datapipes.iter.streamreader.StreamReaderIterDataPipe "torch.utils.data.datapipes.iter.streamreader.StreamReaderIterDataPipe") | Given IO streams and their label names, yield bytes with label name as tuple. |

|     |     |
| --- | --- |
| [`StreamWrapper`](https://docs.pytorch.org/docs/2.15/generated/torch.utils.data.datapipes.utils.common.StreamWrapper.html#torch.utils.data.datapipes.utils.common.StreamWrapper "torch.utils.data.datapipes.utils.common.StreamWrapper") | StreamWrapper is introduced to wrap file handler generated by DataPipe operation like FileOpener. |

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/data.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/data.md.txt)

PyTorch Libraries

*   [ExecuTorch](https://docs.pytorch.org/executorch)
    
*   [Helion](https://docs.pytorch.org/helion)
    
*   [torchao](https://docs.pytorch.org/ao)
    
*   [kineto](https://github.com/pytorch/kineto)
    
*   [torchtitan](https://github.com/pytorch/torchtitan)
    
*   [TorchRL](https://docs.pytorch.org/rl)
    
*   [torchvision](https://docs.pytorch.org/vision)
    
*   [torchaudio](https://docs.pytorch.org/audio)
    
*   [tensordict](https://docs.pytorch.org/tensordict)
    
*   [PyTorch on XLA Devices](https://docs.pytorch.org/xla)
    

Docs
----

Access comprehensive developer documentation for PyTorch

[View Docs](https://docs.pytorch.org/docs/stable/index.html)

Tutorials
---------

Get in-depth tutorials for beginners and advanced developers

[View Tutorials](https://docs.pytorch.org/tutorials)

Resources
---------

Find development resources and get your questions answered

[View Resources](https://pytorch.org/resources)

To analyze traffic and optimize your experience, we serve cookies on this site. By clicking or navigating, you agree to allow our usage of cookies. As the current maintainers of this site, Facebook’s Cookies Policy applies. Learn more, including about available controls: [Cookies Policy](https://opensource.fb.com/legal/cookie-policy)
.

|     |     |
| --- | --- |
|     |     |

|     |     |
| --- | --- |
|     |     |