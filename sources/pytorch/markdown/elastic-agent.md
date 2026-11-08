Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/elastic/agent.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/elastic/agent.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/elastic/agent.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/elastic/agent.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/elastic/agent.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/elastic/agent.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/elastic/agent.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/elastic/agent.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/elastic/agent.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/elastic/agent.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/elastic/agent.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/elastic/agent.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/elastic/agent.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/elastic/agent.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/elastic/agent.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/elastic/agent.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/elastic/agent.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/elastic/agent.html)
[v1.13](https://docs.pytorch.org/docs/1.13/elastic/agent.html)
[v1.12](https://docs.pytorch.org/docs/1.12/elastic/agent.html)
[v1.11](https://docs.pytorch.org/docs/1.11/elastic/agent.html)
[v1.10](https://docs.pytorch.org/docs/1.10/elastic/agent.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/elastic/agent.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/elastic/agent.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/elastic/agent.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/elastic/agent.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/elastic/agent.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/elastic/agent.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/elastic/agent.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/elastic/agent.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/elastic/agent.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/elastic/agent.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/elastic/agent.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/elastic/agent.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/elastic/agent.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/elastic/agent.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/elastic/agent.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/elastic/agent.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/elastic/agent.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/elastic/agent.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/elastic/agent.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/elastic/agent.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/elastic/agent.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/elastic/agent.html)

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

Elastic Agent[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#module-torch.distributed.elastic.agent "Link to this heading")

======================================================================================================================================

Created On: May 04, 2021 | Last Updated On: May 14, 2026

Server[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#module-torch.distributed.elastic.agent.server "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

The elastic agent is the control plane of torchelastic.

It is a process that launches and manages underlying worker processes. The agent is responsible for:

1.  Working with distributed torch: the workers are started with all the necessary information to successfully and trivially call `torch.distributed.init_process_group()`.
    
2.  Fault tolerance: monitors workers and upon detecting worker failures or unhealthiness, tears down all workers and restarts everyone.
    
3.  Elasticity: Reacts to membership changes and restarts workers with the new members.
    

The simplest agents are deployed per node and work with local processes. A more advanced agent can launch and manage workers remotely. Agents can be completely decentralized, making decisions based on the workers it manages. Or can be coordinated, communicating to other agents (that manage workers in the same job) to make a collective decision.

Below is a diagram of an agent that manages a local group of workers.

![../_images/agent_diagram.jpg](https://docs.pytorch.org/docs/2.15/_images/agent_diagram.jpg)

Concepts[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#concepts "Link to this heading")

---------------------------------------------------------------------------------------------------

This section describes the high-level classes and concepts that are relevant to understanding the role of the `agent` in torchelastic.

_class_ torch.distributed.elastic.agent.server.ElasticAgent[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/api.py#L392)
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.ElasticAgent "Link to this definition")

An agent process responsible for managing one or more worker processes.

The worker processes are assumed to be regular distributed PyTorch scripts. When the worker process is created by the agent, the agent provides the necessary information for the worker processes to properly initialize a torch process group.

The exact deployment topology and ratio of agent-to-worker is dependent on the specific implementation of the agent and the user’s job placement preferences. For instance, to run a distributed training job on GPU with 8 trainers (one per GPU) one can:

1.  Use 8 x single GPU instances, place an agent per instance, managing 1 worker per agent.
    
2.  Use 4 x double GPU instances, place an agent per instance, managing 2 workers per agent.
    
3.  Use 2 x quad GPU instances, place an agent per instance, managing 4 workers per agent.
    
4.  Use 1 x 8 GPU instance, place an agent per instance, managing 8 workers per agent.
    

Usage

group\_result \= agent.run()
 if group\_result.is\_failed():
   \# workers failed
   failure \= group\_result.failures\[0\]
   logger.exception("worker 0 failed with exit code : %s", failure.exit\_code)
 else:
   return group\_result.return\_values\[0\] \# return rank 0's results

Copy to clipboard

_abstract_ get\_worker\_group(_role\='default'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/api.py#L442)
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.ElasticAgent.get_worker_group "Link to this definition")

Return the `WorkerGroup` for the given `role`.

Note that the worker group is a mutable object and hence in a multi-threaded/process environment it may change state. Implementers are encouraged (but not required) to return a defensive read-only copy.

Return type:

[_WorkerGroup_](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.WorkerGroup "torch.distributed.elastic.agent.server.api.WorkerGroup")

_abstract_ run(_role\='default'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/api.py#L427)
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.ElasticAgent.run "Link to this definition")

Run the agent.

Supports retrying the worker group on failures up to `max_restarts`.

Returns:

The result of the execution, containing the return values or failure details for each worker mapped by the worker’s global rank.

Raises:

**Exception - any other failures NOT related to worker process** –

Return type:

[_RunResult_](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.api.RunResult "torch.distributed.elastic.agent.server.api.RunResult")

_class_ torch.distributed.elastic.agent.server.WorkerSpec(_role_, _local\_world\_size_, _rdzv\_handler_, _fn\=None_, _entrypoint\=None_, _args\=()_, _max\_restarts\=3_, _monitor\_interval\=0.1_, _master\_port\=None_, _master\_addr\=None_, _local\_addr\=None_, _event\_log\_handler\='null'_, _numa\_options\=None_, _duplicate\_stdout\_filters\=None_, _duplicate\_stderr\_filters\=None_, _virtual\_local\_rank\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/api.py#L49)
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.WorkerSpec "Link to this definition")

Blueprint information about a particular type of worker.

For a given role, there must only exist a single worker spec. Worker spec is expected to be homogeneous across all nodes (machine), that is each node runs the same number of workers for a particular spec.

Parameters:

*   **role** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – user-defined role for the workers with this spec
    
*   **local\_world\_size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – number local workers to run
    
*   **fn** ([_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
     _|_ _None_) – (deprecated use entrypoint instead)
    
*   **entrypoint** ([_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
     _|_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _None_) – worker function or command
    
*   **args** ([_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")
    ) – arguments to pass to `entrypoint`
    
*   **rdzv\_handler** ([_RendezvousHandler_](https://docs.pytorch.org/docs/2.15/elastic/rendezvous.html#torch.distributed.elastic.rendezvous.RendezvousHandler "torch.distributed.elastic.rendezvous.api.RendezvousHandler")
    ) – handles rdzv for this set of workers
    
*   **max\_restarts** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – number of max retries for the workers
    
*   **monitor\_interval** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – monitor status of workers every `n` seconds
    
*   **master\_port** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
     _|_ _None_) – fixed port to run the c10d store on rank 0 if not specified then will choose a random free port
    
*   **master\_addr** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ _None_) – fixed master\_addr to run the c10d store on rank 0 if not specified then will choose hostname on agent rank 0
    
*   **redirects** – redirect std streams to a file, selectively redirect for a particular local rank by passing a map
    
*   **tee** – tees the specified std stream(s) to console + file, selectively tee for a particular local rank by passing a map, takes precedence over `redirects` settings.
    
*   **event\_log\_handler** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – name of the event logging handler as registered in [elastic/events/handlers.py](https://docs.pytorch.org/docs/stable/elastic/events.html)
    .
    
*   **duplicate\_stdout\_filters** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ _None_) – If non-empty, duplicates stdout to a file containing only lines that match \_any\_ of the filter strings.
    
*   **duplicate\_stderr\_filters** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ _None_) – If non-empty, duplicates stderr to a file containing only lines that match \_any\_ of the filter strings.
    
*   **virtual\_local\_rank** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – Enable virtual local rank mode for workers (defaults to False). When enabled, LOCAL\_RANK is set to 0 for all workers and CUDA\_VISIBLE\_DEVICES is adjusted so each worker accesses its assigned GPU at device index 0.
    

get\_entrypoint\_name()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/api.py#L124)
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.WorkerSpec.get_entrypoint_name "Link to this definition")

Get the entry point name.

If the entrypoint is a function (e.g. `Callable`) returns its `__qualname__` else if the entrypoint is a binary (e.g. `str`), returns the binary name.

_class_ torch.distributed.elastic.agent.server.WorkerState(_value_, _names\=None_, _\*_, _module\=None_, _qualname\=None_, _type\=None_, _start\=1_, _boundary\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/api.py#L211)
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.WorkerState "Link to this definition")

A state of the `WorkerGroup`.

Workers in a worker group change state as a unit. If a single worker in a worker group fails the entire set is considered failed:

UNKNOWN - agent lost track of worker group state, unrecoverable
INIT - worker group object created not yet started
HEALTHY - workers running and healthy
UNHEALTHY - workers running and unhealthy
STOPPED - workers stopped (interrupted) by the agent
SUCCEEDED - workers finished running (exit 0)
FAILED - workers failed to successfully finish (exit !0)

Copy to clipboard

A worker group starts from an initial `INIT` state, then progresses to `HEALTHY` or `UNHEALTHY` states, and finally reaches a terminal `SUCCEEDED` or `FAILED` state.

Worker groups can be interrupted and temporarily put into `STOPPED` state by the agent. Workers in `STOPPED` state are scheduled to be restarted in the near future by the agent. Some examples of workers being put into `STOPPED` state are:

1.  Worker group failure|unhealthy observed
    
2.  Membership change detected
    

When actions (start, stop, rdzv, retry, etc) on worker group fail and results in the action being partially applied to the worker group the state will be `UNKNOWN`. Typically this happens on uncaught/unhandled exceptions during state change events on the agent. The agent is not expected to recover worker groups in `UNKNOWN` state and is better off self terminating and allowing the job manager to retry the node.

_static_ is\_running(_state_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/api.py#L254)
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.WorkerState.is_running "Link to this definition")

Return the state of the Worker.

Returns:

True if the worker state represents workers still running (e.g. that the process exists but not necessarily healthy).

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

_class_ torch.distributed.elastic.agent.server.Worker(_local\_rank_, _global\_rank\=\-1_, _role\_rank\=\-1_, _world\_size\=\-1_, _role\_world\_size\=\-1_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/api.py#L138)
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.Worker "Link to this definition")

A worker instance.

Contrast this with `WorkerSpec` that represents the specifications of a worker. A `Worker` is created from a `WorkerSpec`. A `Worker` is to a `WorkerSpec` as an object is to a class.

The `id` of the worker is interpreted by the specific implementation of `ElasticAgent`. For a local agent, it could be the `pid (int)` of the worker, for a remote agent it could be encoded as `host:port (string)`.

Parameters:

*   **local\_rank** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – local rank of the worker
    
*   **global\_rank** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – global rank of the worker
    
*   **role\_rank** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – rank of the worker across all workers that have the same role
    
*   **world\_size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – number of workers (globally)
    
*   **role\_world\_size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")
    ) – number of workers that have the same role
    

_class_ torch.distributed.elastic.agent.server.WorkerGroup(_spec_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/api.py#L265)
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.WorkerGroup "Link to this definition")

A set of `Worker` instances.

The class defines a set of `Worker` instances for the given `WorkerSpec` managed by `ElasticAgent`. Whether the worker group contains cross instance workers or not depends on the implementation of the agent.

Implementations[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#implementations "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

Below are the agent implementations provided by torchelastic.

_class_ torch.distributed.elastic.agent.server.local\_elastic\_agent.LocalElasticAgent(_spec_, _logs\_specs_, _start\_method\='spawn'_, _exit\_barrier\_timeout\=300_, _log\_line\_prefix\_template\=None_, _shutdown\_timeout\=30_, _health\_check\_server\=None_, _uninterruptible\_state\_timeout\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/local_elastic_agent.py#L118)
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.local_elastic_agent.LocalElasticAgent "Link to this definition")

An implementation of `torchelastic.agent.server.ElasticAgent` that handles host-local workers.

This agent is deployed per host and is configured to spawn `n` workers. When using GPUs, `n` maps to the number of GPUs available on the host.

The local agent does not communicate to other local agents deployed on other hosts, even if the workers may communicate inter-host. The worker id is interpreted to be a local process. The agent starts and stops all worker processes as a single unit.

The worker function and argument passed to the worker function must be python multiprocessing compatible. To pass multiprocessing data structures to the workers you may create the data structure in the same multiprocessing context as the specified `start_method` and pass it as a function argument.

The `exit_barrier_timeout` specifies the amount of time (in seconds) to wait for other agents to finish. This acts as a safety net to handle cases where workers finish at different times, to prevent agents from viewing workers that finished early as a scale-down event. It is strongly advised that the user code deal with ensuring that workers are terminated in a synchronous manner rather than relying on the exit\_barrier\_timeout.

A named pipe based watchdog can be enabled in `` `LocalElasticAgent` `` if an environment variable `TORCHELASTIC_ENABLE_FILE_TIMER` with value 1 has been defined in the `` `LocalElasticAgent` `` process. Optionally, another environment variable `` `TORCHELASTIC_TIMER_FILE` `` can be set with a unique file name for the named pipe. If the environment variable `` `TORCHELASTIC_TIMER_FILE` `` is not set, `` `LocalElasticAgent` `` will internally create a unique file name and set it to the environment variable `` `TORCHELASTIC_TIMER_FILE` ``, and this environment variable will be propagated to the worker processes to allow them to connect to the same named pipe that `` `LocalElasticAgent` `` uses.

Logs are written to the specified log directory. Each log line will be by default prefixed by `[${role_name}${local_rank}]:` (e.g. `[trainer0]: foobar`). Log prefixes can be customized by passing a [template string](https://docs.python.org/3/library/string.html#template-strings)
 as the `log_line_prefix_template` argument. The following macros (identifiers) are substituted at runtime: `${role_name}, ${local_rank}, ${rank}, ${hostname}`. For example, to prefix each log line with global rank instead of the local rank, set `log_line_prefix_template = "[${rank}]:`. `${hostname}` expands to the name of the node the agent runs on, which identifies the offending node in a multi-node job; for example `log_line_prefix_template = "${hostname}:${rank}: "` renders as `r12i0n8:3: foobar`.

Example launching function

def trainer(args) \-> str:
    return "do train"

def main():
    start\_method\="spawn"
    shared\_queue\= multiprocessing.get\_context(start\_method).Queue()
    spec \= WorkerSpec(
                role\="trainer",
                local\_world\_size\=nproc\_per\_process,
                entrypoint\=trainer,
                args\=("foobar",),
                ...<OTHER\_PARAMS...>)
    agent \= LocalElasticAgent(spec, start\_method)
    results \= agent.run()

    if results.is\_failed():
        print("trainer failed")
    else:
        print(f"rank 0 return value: {results.return\_values\[0\]}")
        \# prints -> rank 0 return value: do train

Copy to clipboard

Example launching binary

def main():
    spec \= WorkerSpec(
                role\="trainer",
                local\_world\_size\=nproc\_per\_process,
                entrypoint\="/usr/local/bin/trainer",
                args\=("--trainer-args", "foobar"),
                ...<OTHER\_PARAMS...>)
    agent \= LocalElasticAgent(spec)
    results \= agent.run()

    if not results.is\_failed():
        print("binary launches do not have return values")

Copy to clipboard

Extending the Agent[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#extending-the-agent "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

To extend the agent you can implement `ElasticAgent` directly, however we recommend you extend `SimpleElasticAgent` instead, which provides most of the scaffolding and leaves you with a few specific abstract methods to implement.

_class_ torch.distributed.elastic.agent.server.SimpleElasticAgent(_spec_, _exit\_barrier\_timeout\=300_, _shutdown\_timeout\=30_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/api.py#L454)
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.SimpleElasticAgent "Link to this definition")

An `ElasticAgent` that manages one particular type of worker role.

An `ElasticAgent` that manages workers (`WorkerGroup`) for a single `WorkerSpec` such as one particular type of worker role.

\_assign\_worker\_ranks(_store_, _group\_rank_, _group\_world\_size_, _spec_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/api.py#L583)
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.SimpleElasticAgent._assign_worker_ranks "Link to this definition")

Determine proper ranks for worker processes.

Fast Path: when all workers have the same role and world size. We calculate the global rank to be group\_rank \* group\_world\_size + local\_rank. And the role\_world\_size is the same as global\_world\_size. No TCP store is used in this case. This is only enabled when users set the environment variable TORCH\_ELASTIC\_WORKER\_IDENTICAL to 1.

Time complexity: each worker O(1), overall O(1)

Slow Path: when workers have different roles and world sizes. We use the following algorithm:

1.  Each agent writes its configuration(group\_rank, group\_world\_size , num\_workers) to the common store.
    
2.  The rank 0 agent reads all the role\_info from the store and determines each agent’s worker ranks.
    
3.  Determine the global rank: the global rank of the workers is computed by cumulative sum of the local\_world\_size for all workers in front of it. For efficiency reasons each worker is assigned a base global rank such that its workers are in the range \[base\_global\_rank, base\_global\_rank + local\_world\_size).\
    \
4.  Determine the role rank: The role rank is determined using the algorithms in the point 3 with the exception that the ranks are calculated with respect to the role name.\
    \
5.  The rank 0 agent writes the assigned ranks to the store.\
    \
6.  Each agent reads the assigned ranks from the store.\
    \
\
Time complexity: each worker O(1), rank0 O(n), overall O(n)\
\
Return type:\
\
[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[_Worker_](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.Worker "torch.distributed.elastic.agent.server.api.Worker")\
\]\
\
\_exit\_barrier()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/api.py#L975)\
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.SimpleElasticAgent._exit_barrier "Link to this definition")\
\
Define a barrier that keeps the agent process alive until all workers finish.\
\
Wait for `exit_barrier_timeout` seconds for all agents to finish executing their local workers (either successfully or not). This acts as a safety guard against user scripts that terminate at different times.\
\
\_initialize\_workers(_worker\_group_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/api.py#L693)\
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.SimpleElasticAgent._initialize_workers "Link to this definition")\
\
Start a fresh set of workers for the worker\_group.\
\
Essentially, a rendezvous followed by a `start_workers`. The caller should first call `_stop_workers()` to stop running workers prior to calling this method.\
\
Optimistically sets the state of the worker group that just started as `HEALTHY` and delegates the actual monitoring of state to `_monitor_workers()` method\
\
_abstract_ \_monitor\_workers(_worker\_group_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/api.py#L497)\
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.SimpleElasticAgent._monitor_workers "Link to this definition")\
\
Check on the workers for the `worker_group`.\
\
This function also returns the new state of the worker group.\
\
Return type:\
\
[_RunResult_](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.api.RunResult "torch.distributed.elastic.agent.server.api.RunResult")\
\
\_rendezvous(_worker\_group_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/api.py#L517)\
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.SimpleElasticAgent._rendezvous "Link to this definition")\
\
Run rendezvous for the workers specified by the worker spec.\
\
Assigns workers a new global rank and world size. Updates the rendezvous store for the worker group.\
\
\_restart\_workers(_worker\_group_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/api.py#L728)\
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.SimpleElasticAgent._restart_workers "Link to this definition")\
\
Restart (stops, rendezvous, starts) all local workers in the group.\
\
_abstract_ \_shutdown(_death\_sig\=Signals.SIGTERM_, _timeout\=30_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/api.py#L505)\
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.SimpleElasticAgent._shutdown "Link to this definition")\
\
Clean up any resources that were allocated during the agent’s work.\
\
Parameters:\
\
*   **death\_sig** ([_Signals_](https://docs.python.org/3/library/signal.html#signal.Signals "(in Python v3.15)")\
    ) – Signal to send to the child process, SIGTERM is default\
    \
*   **timeout** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – Time to wait for graceful shutdown before sending SIGKILL\
    \
\
_abstract_ \_start\_workers(_worker\_group_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/api.py#L478)\
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.SimpleElasticAgent._start_workers "Link to this definition")\
\
Start `worker_group.spec.local_world_size` number of workers.\
\
This is according to worker spec for the worker group . Returns a map of `local_rank` to worker `id`.\
\
Return type:\
\
[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")\
\[[int](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
, [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
\]\
\
_abstract_ \_stop\_workers(_worker\_group_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/api.py#L487)\
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.SimpleElasticAgent._stop_workers "Link to this definition")\
\
Stop all workers in the given worker group.\
\
Implementers must deal with workers in all states defined by `WorkerState`. That is, it must gracefully handle stopping non-existent workers, unhealthy (stuck) workers, etc.\
\
_class_ torch.distributed.elastic.agent.server.api.RunResult(_state_, _return\_values=<factory>_, _failures=<factory>_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/api.py#L354)\
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.api.RunResult "Link to this definition")\
\
Return results of the worker executions.\
\
Run results follow an “all-or-nothing” policy where the run is successful if and only if ALL local workers managed by this agent complete successfully.\
\
If the result is successful (e.g. `is_failed() = False`) then the `return_values` field contains the outputs (return values) of the workers managed by THIS agent mapped by their GLOBAL ranks. That is `result.return_values[0]` is the return value of global rank 0.\
\
Note\
\
`return_values` are only meaningful for when the worker entrypoint is a function. Workers specified as a binary entrypoint do not canonically have a return value and the `return_values` field is meaningless and may be empty.\
\
If `is_failed()` returns `True` then the `failures` field contains the failure information, again, mapped by the GLOBAL rank of the worker that failed.\
\
The keys in `return_values` and `failures` are mutually exclusive, that is, a worker’s final state can only be one of: succeeded, failed. Workers intentionally terminated by the agent according to the agent’s restart policy, are not represented in either `return_values` nor `failures`.\
\
Watchdog in the Agent[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#watchdog-in-the-agent "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------------\
\
A named pipe based watchdog can be enabled in `LocalElasticAgent` if an environment variable `TORCHELASTIC_ENABLE_FILE_TIMER` with value 1 has been defined in the `LocalElasticAgent` process. Optionally, another environment variable `TORCHELASTIC_TIMER_FILE` can be set with a unique file name for the named pipe. If the environment variable `TORCHELASTIC_TIMER_FILE` is not set, `LocalElasticAgent` will internally create a unique file name and set it to the environment variable `TORCHELASTIC_TIMER_FILE`, and this environment variable will be propagated to the worker processes to allow them to connect to the same named pipe that `LocalElasticAgent` uses.\
\
Health Check Server[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#health-check-server "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------\
\
A health check monitoring server can be enabled in `LocalElasticAgent` if an environment variable `TORCHELASTIC_HEALTH_CHECK_PORT` has been defined in the `LocalElasticAgent` process. Adding interface for health check server which can be extended by starting tcp/http server on the specified port number. Additionally, health check server will have callback to check watchdog is alive.\
\
_class_ torch.distributed.elastic.agent.server.health\_check\_server.HealthCheckServer(_alive\_callback_, _port_, _timeout_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/health_check_server.py#L19)\
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.health_check_server.HealthCheckServer "Link to this definition")\
\
Interface for health check monitoring server, which can be extended by starting tcp/http server on the specified port.\
\
Parameters:\
\
*   **alive\_callback** ([_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")\
    _\[__\[__\]__,_ [_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    _\]_) – Callable\[\[\], int\], callback to last progress time of agent\
    \
*   **port** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – int, port number to start tcp/http server\
    \
*   **timeout** ([_int_](https://docs.python.org/3/builtins/functions.html#int "(in Python v3.15)")\
    ) – int, timeout seconds to decide agent is alive/dead\
    \
\
start()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/health_check_server.py#L44)\
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.health_check_server.HealthCheckServer.start "Link to this definition")\
\
Unsupported functionality for PyTorch, doesn’t start any health check server\
\
stop()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/health_check_server.py#L50)\
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.health_check_server.HealthCheckServer.stop "Link to this definition")\
\
Function to stop health check server\
\
torch.distributed.elastic.agent.server.health\_check\_server.create\_healthcheck\_server(_alive\_callback_, _port_, _timeout_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/agent/server/health_check_server.py#L61)\
[#](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.health_check_server.create_healthcheck_server "Link to this definition")\
\
creates health check server object\
\
Return type:\
\
[_HealthCheckServer_](https://docs.pytorch.org/docs/2.15/elastic/agent.html#torch.distributed.elastic.agent.server.health_check_server.HealthCheckServer "torch.distributed.elastic.agent.server.health_check_server.HealthCheckServer")\
\
On this page\
\
[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/elastic/agent.md)\
\
[Show Source](https://docs.pytorch.org/docs/2.15/_sources/elastic/agent.md.txt)\
\
PyTorch Libraries\
\
*   [ExecuTorch](https://docs.pytorch.org/executorch)\
    \
*   [Helion](https://docs.pytorch.org/helion)\
    \
*   [torchao](https://docs.pytorch.org/ao)\
    \
*   [kineto](https://github.com/pytorch/kineto)\
    \
*   [torchtitan](https://github.com/pytorch/torchtitan)\
    \
*   [TorchRL](https://docs.pytorch.org/rl)\
    \
*   [torchvision](https://docs.pytorch.org/vision)\
    \
*   [torchaudio](https://docs.pytorch.org/audio)\
    \
*   [tensordict](https://docs.pytorch.org/tensordict)\
    \
*   [PyTorch on XLA Devices](https://docs.pytorch.org/xla)\
    \
\
Docs\
----\
\
Access comprehensive developer documentation for PyTorch\
\
[View Docs](https://docs.pytorch.org/docs/stable/index.html)\
\
Tutorials\
---------\
\
Get in-depth tutorials for beginners and advanced developers\
\
[View Tutorials](https://docs.pytorch.org/tutorials)\
\
Resources\
---------\
\
Find development resources and get your questions answered\
\
[View Resources](https://pytorch.org/resources)\
\
To analyze traffic and optimize your experience, we serve cookies on this site. By clicking or navigating, you agree to allow our usage of cookies. As the current maintainers of this site, Facebook’s Cookies Policy applies. Learn more, including about available controls: [Cookies Policy](https://opensource.fb.com/legal/cookie-policy)\
.\
\
|     |     |\
| --- | --- |\
|     |     |\
\
|     |     |\
| --- | --- |\
|     |     |