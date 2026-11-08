Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/elastic/run.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/elastic/run.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/elastic/run.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/elastic/run.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/elastic/run.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/elastic/run.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/elastic/run.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/elastic/run.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/elastic/run.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/elastic/run.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/elastic/run.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/elastic/run.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/elastic/run.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/elastic/run.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/elastic/run.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/elastic/run.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/elastic/run.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/elastic/run.html)
[v1.13](https://docs.pytorch.org/docs/1.13/elastic/run.html)
[v1.12](https://docs.pytorch.org/docs/1.12/elastic/run.html)
[v1.11](https://docs.pytorch.org/docs/1.11/elastic/run.html)
[v1.10](https://docs.pytorch.org/docs/1.10/elastic/run.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/elastic/run.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/elastic/run.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/elastic/run.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/elastic/run.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/elastic/run.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/elastic/run.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/elastic/run.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/elastic/run.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/elastic/run.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/elastic/run.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/elastic/run.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/elastic/run.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/elastic/run.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/elastic/run.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/elastic/run.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/elastic/run.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/elastic/run.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/elastic/run.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/elastic/run.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/elastic/run.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/elastic/run.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/elastic/run.html)

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

torchrun (Elastic Launch)[#](https://docs.pytorch.org/docs/2.15/elastic/run.html#module-torch.distributed.run "Link to this heading")

======================================================================================================================================

Created On: May 12, 2026 | Last Updated On: May 12, 2026

Module `torch.distributed.run`.

`torch.distributed.run` is a module that spawns up multiple distributed training processes on each of the training nodes.

`torchrun` is a python [console script](https://packaging.python.org/en/latest/specifications/entry-points/#use-for-scripts)
 to the main module [torch.distributed.run](https://github.com/pytorch/pytorch/blob/master/torch/distributed/run.py)
 declared in the `entry_points` configuration in [setup.py](https://github.com/pytorch/pytorch/blob/master/setup.py)
. It is equivalent to invoking `python -m torch.distributed.run`.

`torchrun` can be used for single-node distributed training, in which one or more processes per node will be spawned. It can be used for either CPU training or GPU training. If it is used for GPU training, each distributed process will be operating on a single GPU. This can achieve well-improved single-node training performance. `torchrun` can also be used in multi-node distributed training, by spawning up multiple processes on each node for well-improved multi-node distributed training performance as well. This will especially be beneficial for systems with multiple Infiniband interfaces that have direct-GPU support, since all of them can be utilized for aggregated communication bandwidth.

In both cases of single-node distributed training or multi-node distributed training, `torchrun` will launch the given number of processes per node (`--nproc-per-node`). If used for GPU training, this number needs to be less or equal to the number of GPUs on the current system (`nproc_per_node`), and each process will be operating on a single GPU from _GPU 0 to GPU (nproc\_per\_node - 1)_.

Changed in version 2.0.0: `torchrun` will pass the `--local-rank=<rank>` argument to your script. From PyTorch 2.0.0 onwards, the dashed `--local-rank` is preferred over the previously used underscored `--local_rank`.

For backward compatibility, it may be necessary for users to handle both cases in their argument parsing code. This means including both `"--local-rank"` and `"--local_rank"` in the argument parser. If only `"--local_rank"` is provided, `torchrun` will trigger an error: “error: unrecognized arguments: –local-rank=<rank>”. For training code that only supports PyTorch 2.0.0+, including `"--local-rank"` should be sufficient.

\>>> import argparse
\>>> parser \= argparse.ArgumentParser()
\>>> parser.add\_argument("--local-rank", "--local\_rank", type\=int)
\>>> args \= parser.parse\_args()

Copy to clipboard

Usage[#](https://docs.pytorch.org/docs/2.15/elastic/run.html#usage "Link to this heading")

-------------------------------------------------------------------------------------------

### Single-node multi-worker[#](https://docs.pytorch.org/docs/2.15/elastic/run.html#single-node-multi-worker "Link to this heading")

torchrun
    --standalone
    --nnodes=1
    --nproc-per-node=$NUM\_TRAINERS
    YOUR\_TRAINING\_SCRIPT.py (--arg1 ... train script args...)

Copy to clipboard

Note

`--nproc-per-node` may be `"gpu"` (spawn one process per GPU), `"cpu"` (spawn one process per CPU), `"xpu"` (spawn one process per XPU), `"auto"` (equivalent to `"gpu"` if CUDA is available, else equivalent to `"xpu"` if XPU is available, else equivalent to `"cpu"`), or an integer specifying the number of processes. See [torch.distributed.run.determine\_local\_world\_size](https://github.com/pytorch/pytorch/blob/0a94bb432ed75cc2d950d81b2921363218a7e459/torch/distributed/run.py#L673-L716)
 for more details.

### Stacked single-node multi-worker[#](https://docs.pytorch.org/docs/2.15/elastic/run.html#stacked-single-node-multi-worker "Link to this heading")

To run multiple instances (separate jobs) of single-node, multi-worker on the same host, we need to make sure that each instance (job) is setup on different ports to avoid port conflicts (or worse, two jobs being merged as a single job). To do this you have to run with `--rdzv-backend=c10d` and specify a different port by setting `--rdzv-endpoint=localhost:$PORT_k`. For `--nodes=1`, its often convenient to let `torchrun` pick a free random port automatically instead of manually assigning different ports for each run.

torchrun
    --rdzv-backend=c10d
    --rdzv-endpoint=localhost:0
    --nnodes=1
    --nproc-per-node=$NUM\_TRAINERS
    YOUR\_TRAINING\_SCRIPT.py (--arg1 ... train script args...)

Copy to clipboard

### Fault tolerant (fixed sized number of workers, no elasticity, tolerates 3 failures)[#](https://docs.pytorch.org/docs/2.15/elastic/run.html#fault-tolerant-fixed-sized-number-of-workers-no-elasticity-tolerates-3-failures "Link to this heading")

torchrun
    --nnodes=$NUM\_NODES
    --nproc-per-node=$NUM\_TRAINERS
    --max-restarts=3
    --rdzv-id=$JOB\_ID
    --rdzv-backend=c10d
    --rdzv-endpoint=$HOST\_NODE\_ADDR
    YOUR\_TRAINING\_SCRIPT.py (--arg1 ... train script args...)

Copy to clipboard

`HOST_NODE_ADDR`, in form <host>\[:<port>\] (e.g. node1.example.com:29400), specifies the node and the port on which the C10d rendezvous backend should be instantiated and hosted. It can be any node in your training cluster, but ideally you should pick a node that has a high bandwidth.

Note

If no port number is specified `HOST_NODE_ADDR` defaults to 29400.

### Elastic (`min=1`, `max=4`, tolerates up to 3 membership changes or failures)[#](https://docs.pytorch.org/docs/2.15/elastic/run.html#elastic-min-1-max-4-tolerates-up-to-3-membership-changes-or-failures "Link to this heading")

torchrun
    --nnodes=1:4
    --nproc-per-node=$NUM\_TRAINERS
    --max-restarts=3
    --rdzv-id=$JOB\_ID
    --rdzv-backend=c10d
    --rdzv-endpoint=$HOST\_NODE\_ADDR
    YOUR\_TRAINING\_SCRIPT.py (--arg1 ... train script args...)

Copy to clipboard

`HOST_NODE_ADDR`, in form <host>\[:<port>\] (e.g. node1.example.com:29400), specifies the node and the port on which the C10d rendezvous backend should be instantiated and hosted. It can be any node in your training cluster, but ideally you should pick a node that has a high bandwidth.

Note

If no port number is specified `HOST_NODE_ADDR` defaults to 29400.

Shell completion[#](https://docs.pytorch.org/docs/2.15/elastic/run.html#shell-completion "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

`torchrun` can emit a completion script for `bash`, `zsh` or `tcsh`. The script is generated from the argument parser, so it stays in sync with the options above. This requires the optional [shtab](https://tqdm.github.io/shtab)
 package (`pip install shtab`); torchrun only imports it when the flag is used.

\# zsh
torchrun \--print\-completion zsh \> ~/.zsh/completions/\_torchrun

\# bash
torchrun \--print\-completion bash \> ~/.local/share/bash\-completion/completions/torchrun

Copy to clipboard

Refer to your shell’s documentation for the directory it loads completions from; the paths above are the common defaults.

Note on rendezvous backend[#](https://docs.pytorch.org/docs/2.15/elastic/run.html#note-on-rendezvous-backend "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

For multi-node training you need to specify:

1.  `--rdzv-id`: A unique job id (shared by all nodes participating in the job)
    
2.  `--rdzv-backend`: An implementation of [`torch.distributed.elastic.rendezvous.RendezvousHandler`](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousHandler "torch.distributed.elastic.rendezvous.RendezvousHandler")
    
3.  `--rdzv-endpoint`: The endpoint where the rendezvous backend is running; usually in form `host:port`.
    

Currently `c10d` (recommended), `etcd-v2`, and `etcd` (legacy) rendezvous backends are supported out of the box. To use `etcd-v2` or `etcd`, setup an etcd server with the `v2` api enabled (e.g. `--enable-v2`).

Warning

`etcd-v2` and `etcd` rendezvous use etcd API v2. You MUST enable the v2 API on the etcd server. Our tests use etcd v3.4.3.

Warning

For etcd-based rendezvous we recommend using `etcd-v2` over `etcd` which is functionally equivalent, but uses a revised implementation. `etcd` is in maintenance mode and will be removed in a future version.

Definitions[#](https://docs.pytorch.org/docs/2.15/elastic/run.html#definitions "Link to this heading")

-------------------------------------------------------------------------------------------------------

1.  `Node` - A physical instance or a container; maps to the unit that the job manager works with.
    
2.  `Worker` - A worker in the context of distributed training.
    
3.  `WorkerGroup` - The set of workers that execute the same function (e.g. trainers).
    
4.  `LocalWorkerGroup` - A subset of the workers in the worker group running on the same node.
    
5.  `RANK` - The rank of the worker within a worker group.
    
6.  `WORLD_SIZE` - The total number of workers in a worker group.
    
7.  `LOCAL_RANK` - The rank of the worker within a local worker group.
    
8.  `LOCAL_WORLD_SIZE` - The size of the local worker group.
    
9.  `rdzv_id` - A user-defined id that uniquely identifies the worker group for a job. This id is used by each node to join as a member of a particular worker group.
    

9.  `rdzv_backend` - The backend of the rendezvous (e.g. `c10d`). This is typically a strongly consistent key-value store.
    
10.  `rdzv_endpoint` - The rendezvous backend endpoint; usually in form `<host>:<port>`.
    

A `Node` runs `LOCAL_WORLD_SIZE` workers which comprise a `LocalWorkerGroup`. The union of all `LocalWorkerGroups` in the nodes in the job comprise the `WorkerGroup`.

Environment Variables[#](https://docs.pytorch.org/docs/2.15/elastic/run.html#environment-variables "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

The following environment variables are made available to you in your script:

1.  `LOCAL_RANK` - The local rank.
    
2.  `RANK` - The global rank.
    
3.  `GROUP_RANK` - The rank of the worker group. A number between 0 and `max_nnodes`. When running a single worker group per node, this is the rank of the node.
    
4.  `ROLE_RANK` - The rank of the worker across all the workers that have the same role. The role of the worker is specified in the `WorkerSpec`.
    
5.  `LOCAL_WORLD_SIZE` - The local world size (e.g. number of workers running locally); equals to `--nproc-per-node` specified on `torchrun`.
    
6.  `WORLD_SIZE` - The world size (total number of workers in the job).
    
7.  `ROLE_WORLD_SIZE` - The total number of workers that was launched with the same role specified in `WorkerSpec`.
    
8.  `MASTER_ADDR` - The FQDN of the host that is running worker with rank 0; used to initialize the Torch Distributed backend.
    
9.  `MASTER_PORT` - The port on the `MASTER_ADDR` that can be used to host the C10d TCP store.
    
10.  `TORCHELASTIC_RESTART_COUNT` - The number of worker group restarts so far.
    
11.  `TORCHELASTIC_MAX_RESTARTS` - The configured maximum number of restarts.
    
12.  `TORCHELASTIC_RUN_ID` - Equal to the rendezvous `run_id` (e.g. unique job id).
    
13.  `PYTHON_EXEC` - System executable override. If provided, the python user script will use the value of `PYTHON_EXEC` as executable. The sys.executable is used by default.
    

Logging[#](https://docs.pytorch.org/docs/2.15/elastic/run.html#logging "Link to this heading")

-----------------------------------------------------------------------------------------------

By default each worker’s `stdout`/`stderr` go to the console unchanged, which interleaves the output of every rank with no way to tell them apart.

`--redirects` writes the streams to log files under `--log-dir` instead of the console; `--tee` writes them to log files _and_ echoes them to the console. Both take the same format: a single value applies to all workers (`3` for both streams, `1` for stdout, `2` for stderr), or a per-local-rank mapping such as `0:1,1:2`. For example `--tee 3` tees both streams for every worker.

Tee’d console lines are prefixed with `[${role_name}${local_rank}]:` (e.g. `[default3]: foobar`). Use `--log-line-prefix-template` to change that; the macros `${role_name}`, `${local_rank}`, `${rank}` and `${hostname}` are substituted per worker. `${hostname}` is the name of the node the worker runs on, which is what identifies the offending host in a multi-node job:

torchrun --nnodes 2 --nproc-per-node 8 --tee 3              --log-line-prefix-template "${hostname}:${rank}: " train.py

r12i0n8:3: python: src/psm2\_nccl\_net.c:756: Assertion \`r->used' failed.
r12i0n8:3: Fatal Python error: Segmentation fault

Copy to clipboard

The template may also be set with the `TORCHELASTIC_LOG_LINE_PREFIX_TEMPLATE` environment variable; the command line option takes precedence. `--local-ranks-filter` restricts which ranks reach the console, without affecting the log files written by `--redirects`/`--tee`.

Deployment[#](https://docs.pytorch.org/docs/2.15/elastic/run.html#deployment "Link to this heading")

-----------------------------------------------------------------------------------------------------

1.  (Not needed for the C10d backend) Start the rendezvous backend server and get the endpoint (to be passed as `--rdzv-endpoint` to `torchrun`)
    
2.  Single-node multi-worker: Start `torchrun` on the host to start the agent process which creates and monitors a local worker group.
    
3.  Multi-node multi-worker: Start `torchrun` with the same arguments on all the nodes participating in training.
    

When using a job/cluster manager, the entry point command to the multi-node job should be `torchrun`.

Failure Modes[#](https://docs.pytorch.org/docs/2.15/elastic/run.html#failure-modes "Link to this heading")

-----------------------------------------------------------------------------------------------------------

1.  Worker failure: For a training job with `n` workers, if `k<=n` workers fail all workers are stopped and restarted up to `max_restarts`.
    
2.  Agent failure: An agent failure results in a local worker group failure. It is up to the job manager to fail the entire job (gang semantics) or attempt to replace the node. Both behaviors are supported by the agent.
    
3.  Node failure: Same as agent failure.
    

Membership Changes[#](https://docs.pytorch.org/docs/2.15/elastic/run.html#membership-changes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

1.  Node departure (scale-down): The agent is notified of the departure, all existing workers are stopped, a new `WorkerGroup` is formed, and all workers are started with a new `RANK` and `WORLD_SIZE`.
    
2.  Node arrival (scale-up): The new node is admitted to the job, all existing workers are stopped, a new `WorkerGroup` is formed, and all workers are started with a new `RANK` and `WORLD_SIZE`.
    

NUMA Binding[#](https://docs.pytorch.org/docs/2.15/elastic/run.html#numa-binding "Link to this heading")

---------------------------------------------------------------------------------------------------------

On multi-GPU systems with NUMA (Non-Uniform Memory Access) architecture, you can improve performance by binding worker processes to CPUs near their assigned GPUs. Use the `--numa-binding` flag:

torchrun \--numa\-binding\=node \--nproc\-per\-node\=8 train.py

Copy to clipboard

See [NUMA Binding](https://docs.pytorch.org/docs/2.15/elastic/numa.html#numa-api)
 for more details.

Important Notices[#](https://docs.pytorch.org/docs/2.15/elastic/run.html#important-notices "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

1.  This utility and multi-process distributed (single-node or multi-node) GPU training currently only achieves the best performance using the NCCL distributed backend. Thus NCCL backend is the recommended backend to use for GPU training.
    
2.  The environment variables necessary to initialize a Torch process group are provided to you by this module, no need for you to pass `RANK` manually. To initialize a process group in your training script, simply run:
    

\>>> import torch.distributed as dist
\>>> dist.init\_process\_group(backend\="gloo|nccl")

Copy to clipboard

3.  In your training program, you can either use regular distributed functions or use [`torch.nn.parallel.DistributedDataParallel()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")
     module. If your training program uses GPUs for training and you would like to use [`torch.nn.parallel.DistributedDataParallel()`](https://docs.pytorch.org/docs/2.15/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel "torch.nn.parallel.DistributedDataParallel")
     module, here is how to configure it.
    

local\_rank \= int(os.environ\["LOCAL\_RANK"\])
model \= torch.nn.parallel.DistributedDataParallel(
    model, device\_ids\=\[local\_rank\], output\_device\=local\_rank
)

Copy to clipboard

Please ensure that `device_ids` argument is set to be the only GPU device id that your code will be operating on. This is generally the local rank of the process. In other words, the `device_ids` needs to be `[int(os.environ("LOCAL_RANK"))]`, and `output_device` needs to be `int(os.environ("LOCAL_RANK"))` in order to use this utility

4.  On failures or membership changes ALL surviving workers are killed immediately. Make sure to checkpoint your progress. The frequency of checkpoints should depend on your job’s tolerance for lost work.
    
5.  This module only supports homogeneous `LOCAL_WORLD_SIZE`. That is, it is assumed that all nodes run the same number of local workers (per role).
    
6.  `RANK` is NOT stable. Between restarts, the local workers on a node can be assigned a different range of ranks than before. NEVER hard code any assumptions about the stable-ness of ranks or some correlation between `RANK` and `LOCAL_RANK`.
    
7.  When using elasticity (`min_size!=max_size`) DO NOT hard code assumptions about `WORLD_SIZE` as the world size can change as nodes are allowed to leave and join.
    
8.  It is recommended for your script to have the following structure:
    

def main():
    load\_checkpoint(checkpoint\_path)
    initialize()
    train()

def train():
    for batch in iter(dataset):
        train\_step(batch)

        if should\_checkpoint:
            save\_checkpoint(checkpoint\_path)

Copy to clipboard

9.  (Recommended) On worker errors, this tool will summarize the details of the error (e.g. time, rank, host, pid, traceback, etc). On each node, the first error (by timestamp) is heuristically reported as the “Root Cause” error. To get tracebacks as part of this error summary print out, you must decorate your main entrypoint function in your training script as shown in the example below. If not decorated, then the summary will not include the traceback of the exception and will only contain the exitcode. For details on torchelastic error handling see: [https://pytorch.org/docs/stable/elastic/errors.html](https://pytorch.org/docs/stable/elastic/errors.html)
    

from torch.distributed.elastic.multiprocessing.errors import record

@record
def main():
    \# do train
    pass

if \_\_name\_\_ \== "\_\_main\_\_":
    main()

Copy to clipboard

|     |     |
| --- | --- |
| [`config_from_args`](https://docs.pytorch.org/docs/2.15/elastic/generated/torch.distributed.run.config_from_args.html#torch.distributed.run.config_from_args "torch.distributed.run.config_from_args") |     |
| [`determine_local_world_size`](https://docs.pytorch.org/docs/2.15/elastic/generated/torch.distributed.run.determine_local_world_size.html#torch.distributed.run.determine_local_world_size "torch.distributed.run.determine_local_world_size") |     |
| [`main`](https://docs.pytorch.org/docs/2.15/elastic/generated/torch.distributed.run.main.html#torch.distributed.run.main "torch.distributed.run.main") |     |
| [`parse_args`](https://docs.pytorch.org/docs/2.15/elastic/generated/torch.distributed.run.parse_args.html#torch.distributed.run.parse_args "torch.distributed.run.parse_args") |     |
| [`parse_min_max_nnodes`](https://docs.pytorch.org/docs/2.15/elastic/generated/torch.distributed.run.parse_min_max_nnodes.html#torch.distributed.run.parse_min_max_nnodes "torch.distributed.run.parse_min_max_nnodes") |     |
| [`run`](https://docs.pytorch.org/docs/2.15/elastic/generated/torch.distributed.run.run.html#torch.distributed.run.run "torch.distributed.run.run") |     |
| [`run_script_path`](https://docs.pytorch.org/docs/2.15/elastic/generated/torch.distributed.run.run_script_path.html#torch.distributed.run.run_script_path "torch.distributed.run.run_script_path") | Run the provided training\_script from within this interpreter. |

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/elastic/run.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/elastic/run.md.txt)

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