Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/elastic/timer.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/elastic/timer.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/elastic/timer.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/elastic/timer.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/elastic/timer.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/elastic/timer.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/elastic/timer.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/elastic/timer.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/elastic/timer.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/elastic/timer.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/elastic/timer.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/elastic/timer.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/elastic/timer.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/elastic/timer.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/elastic/timer.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/elastic/timer.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/elastic/timer.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/elastic/timer.html)
[v1.13](https://docs.pytorch.org/docs/1.13/elastic/timer.html)
[v1.12](https://docs.pytorch.org/docs/1.12/elastic/timer.html)
[v1.11](https://docs.pytorch.org/docs/1.11/elastic/timer.html)
[v1.10](https://docs.pytorch.org/docs/1.10/elastic/timer.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/elastic/timer.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/elastic/timer.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/elastic/timer.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/elastic/timer.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/elastic/timer.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/elastic/timer.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/elastic/timer.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/elastic/timer.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/elastic/timer.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/elastic/timer.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/elastic/timer.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/elastic/timer.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/elastic/timer.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/elastic/timer.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/elastic/timer.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/elastic/timer.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/elastic/timer.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/elastic/timer.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/elastic/timer.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/elastic/timer.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/elastic/timer.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/elastic/timer.html)

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

Expiration Timers[#](https://docs.pytorch.org/docs/2.15/elastic/timer.html#module-torch.distributed.elastic.timer "Link to this heading")

==========================================================================================================================================

Created On: May 04, 2021 | Last Updated On: May 06, 2026

Expiration timers are set up on the same process as the agent and used from your script to deal with stuck workers. When you go into a code-block that has the potential to get stuck you can acquire an expiration timer, which instructs the timer server to kill the process if it does not release the timer by the self-imposed expiration deadline.

Usage:

import torchelastic.timer as timer
import torchelastic.agent.server as agent

def main():
    start\_method \= "spawn"
    message\_queue \= mp.get\_context(start\_method).Queue()
    server \= timer.LocalTimerServer(message, max\_interval\=0.01)
    server.start() \# non-blocking

    spec \= WorkerSpec(
                fn\=trainer\_func,
                args\=(message\_queue,),
                ...<OTHER\_PARAMS...>)
    agent \= agent.LocalElasticAgent(spec, start\_method)
    agent.run()

def trainer\_func(message\_queue):
    timer.configure(timer.LocalTimerClient(message\_queue))
    with timer.expires(after\=60): \# 60 second expiry
        \# do some work

Copy to clipboard

In the example above if `trainer_func` takes more than 60 seconds to complete, then the worker process is killed and the agent retries the worker group.

Client Methods[#](https://docs.pytorch.org/docs/2.15/elastic/timer.html#client-methods "Link to this heading")

---------------------------------------------------------------------------------------------------------------

torch.distributed.elastic.timer.configure(_timer\_client_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/timer/api.py#L240)
[#](https://docs.pytorch.org/docs/2.15/elastic/timer.html#torch.distributed.elastic.timer.configure "Link to this definition")

Configures a timer client. Must be called before using `expires`.

torch.distributed.elastic.timer.expires(_after_, _scope\=None_, _client\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/timer/api.py#L249)
[#](https://docs.pytorch.org/docs/2.15/elastic/timer.html#torch.distributed.elastic.timer.expires "Link to this definition")

Acquires a countdown timer that expires in `after` seconds from now, unless the code-block that it wraps is finished within the timeframe. When the timer expires, this worker is eligible to be reaped. The exact meaning of “reaped” depends on the client implementation. In most cases, reaping means to terminate the worker process. Note that the worker is NOT guaranteed to be reaped at exactly `time.now() + after`, but rather the worker is “eligible” for being reaped and the `TimerServer` that the client talks to will ultimately make the decision when and how to reap the workers with expired timers.

Usage:

torch.distributed.elastic.timer.configure(LocalTimerClient())
with expires(after\=10):
    torch.distributed.all\_reduce(...)

Copy to clipboard

Server/Client Implementations[#](https://docs.pytorch.org/docs/2.15/elastic/timer.html#server-client-implementations "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

Below are the timer server and client pairs that are provided by torchelastic.

Note

Timer server and clients always have to be implemented and used in pairs since there is a messaging protocol between the server and client.

Below is a pair of timer server and client that is implemented based on a `multiprocess.Queue`.

_class_ torch.distributed.elastic.timer.LocalTimerServer(_mp\_queue_, _max\_interval\=60_, _daemon\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/timer/local_timer.py#L78)
[#](https://docs.pytorch.org/docs/2.15/elastic/timer.html#torch.distributed.elastic.timer.LocalTimerServer "Link to this definition")

Server that works with `LocalTimerClient`. Clients are expected to be subprocesses to the parent process that is running this server. Each host in the job is expected to start its own timer server locally and each server instance manages timers for local workers (running on processes on the same host).

_class_ torch.distributed.elastic.timer.LocalTimerClient(_mp\_queue_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/timer/local_timer.py#L23)
[#](https://docs.pytorch.org/docs/2.15/elastic/timer.html#torch.distributed.elastic.timer.LocalTimerClient "Link to this definition")

Client side of `LocalTimerServer`. This client is meant to be used on the same host that the `LocalTimerServer` is running on and uses pid to uniquely identify a worker. This is particularly useful in situations where one spawns a subprocess (trainer) per GPU on a host with multiple GPU devices.

Below is another pair of timer server and client that is implemented based on a named pipe.

_class_ torch.distributed.elastic.timer.FileTimerServer(_file\_path_, _run\_id_, _max\_interval\=10_, _daemon\=True_, _log\_event\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/timer/file_based_local_timer.py#L179)
[#](https://docs.pytorch.org/docs/2.15/elastic/timer.html#torch.distributed.elastic.timer.FileTimerServer "Link to this definition")

Server that works with `FileTimerClient`. Clients are expected to be running on the same host as the process that is running this server. Each host in the job is expected to start its own timer server locally and each server instance manages timers for local workers (running on processes on the same host).

Parameters:

*   **file\_path** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – str, the path of a FIFO special file to be created.
    
*   **max\_interval** ([_float_](https://docs.python.org/3/builtins/functions.html#float "(in Python v3.15)")
    ) – float, max interval in seconds for each watchdog loop.
    
*   **daemon** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – bool, running the watchdog thread in daemon mode or not. A daemon thread will not block a process to stop.
    
*   **log\_event** ([_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
    _\[__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _,_ _FileTimerRequest_ _|_ _None__\]__,_ _None__\]_ _|_ _None_) – Callable\[\[Dict\[str, str\]\], None\], an optional callback for logging the events in JSON format.
    

_class_ torch.distributed.elastic.timer.FileTimerClient(_file\_path_, _signal\=Signals.SIGKILL_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/timer/file_based_local_timer.py#L107)
[#](https://docs.pytorch.org/docs/2.15/elastic/timer.html#torch.distributed.elastic.timer.FileTimerClient "Link to this definition")

Client side of `FileTimerServer`. This client is meant to be used on the same host that the `FileTimerServer` is running on and uses pid to uniquely identify a worker. This client uses a named\_pipe to send timer requests to the `FileTimerServer`. This client is a producer while the `FileTimerServer` is a consumer. Multiple clients can work with the same `FileTimerServer`.

Parameters:

*   **file\_path** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – str, the path of a FIFO special file. `FileTimerServer` must have created it by calling os.mkfifo().
    
*   **signal** – signal, the signal to use to kill the process. Using a negative or zero signal will not kill the process.
    

Writing a custom timer server/client[#](https://docs.pytorch.org/docs/2.15/elastic/timer.html#writing-a-custom-timer-server-client "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

To write your own timer server and client extend the `torch.distributed.elastic.timer.TimerServer` for the server and `torch.distributed.elastic.timer.TimerClient` for the client. The `TimerRequest` object is used to pass messages between the server and client.

_class_ torch.distributed.elastic.timer.TimerRequest(_worker\_id_, _scope\_id_, _expiration\_time_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/timer/api.py#L28)
[#](https://docs.pytorch.org/docs/2.15/elastic/timer.html#torch.distributed.elastic.timer.TimerRequest "Link to this definition")

Data object representing a countdown timer acquisition and release that is used between the `TimerClient` and `TimerServer`. A negative `expiration_time` should be interpreted as a “release” request.

Note

the type of `worker_id` is implementation specific. It is whatever the TimerServer and TimerClient implementations have on to uniquely identify a worker.

_class_ torch.distributed.elastic.timer.TimerServer(_request\_queue_, _max\_interval_, _daemon\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/timer/api.py#L113)
[#](https://docs.pytorch.org/docs/2.15/elastic/timer.html#torch.distributed.elastic.timer.TimerServer "Link to this definition")

Entity that monitors active timers and expires them in a timely fashion. This server is responsible for reaping workers that have expired timers.

_abstract_ clear\_timers(_worker\_ids_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/timer/api.py#L145)
[#](https://docs.pytorch.org/docs/2.15/elastic/timer.html#torch.distributed.elastic.timer.TimerServer.clear_timers "Link to this definition")

Clears all timers for the given `worker_ids`.

_abstract_ get\_expired\_timers(_deadline_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/timer/api.py#L151)
[#](https://docs.pytorch.org/docs/2.15/elastic/timer.html#torch.distributed.elastic.timer.TimerServer.get_expired_timers "Link to this definition")

Returns all expired timers for each worker\_id. An expired timer is a timer for which the expiration\_time is less than or equal to the provided deadline.

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[_TimerRequest_](https://docs.pytorch.org/docs/2.15/elastic/timer.html#torch.distributed.elastic.timer.TimerRequest "torch.distributed.elastic.timer.api.TimerRequest")\
\]\]

_abstract_ register\_timers(_timer\_requests_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/timer/api.py#L136)
[#](https://docs.pytorch.org/docs/2.15/elastic/timer.html#torch.distributed.elastic.timer.TimerServer.register_timers "Link to this definition")

Processes the incoming timer requests and registers them with the server. The timer request can either be an acquire-timer or release-timer request. Timer requests with a negative expiration\_time should be interpreted as a release-timer request.

_class_ torch.distributed.elastic.timer.TimerClient[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/timer/api.py#L57)
[#](https://docs.pytorch.org/docs/2.15/elastic/timer.html#torch.distributed.elastic.timer.TimerClient "Link to this definition")

Client library to acquire and release countdown timers by communicating with the TimerServer.

_abstract_ acquire(_scope\_id_, _expiration\_time_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/timer/api.py#L63)
[#](https://docs.pytorch.org/docs/2.15/elastic/timer.html#torch.distributed.elastic.timer.TimerClient.acquire "Link to this definition")

Acquires a timer for the worker that holds this client object given the scope\_id and expiration\_time. Typically registers the timer with the TimerServer.

_abstract_ release(_scope\_id_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/timer/api.py#L71)
[#](https://docs.pytorch.org/docs/2.15/elastic/timer.html#torch.distributed.elastic.timer.TimerClient.release "Link to this definition")

Releases the timer for the `scope_id` on the worker this client represents. After this method is called, the countdown timer on the scope is no longer in effect.

Debug info logging[#](https://docs.pytorch.org/docs/2.15/elastic/timer.html#module-torch.distributed.elastic.timer.debug_info_logging "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

torch.distributed.elastic.timer.debug\_info\_logging.log\_debug\_info\_for\_expired\_timers(_run\_id_, _expired\_timers_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/distributed/elastic/timer/debug_info_logging.py#L19)
[#](https://docs.pytorch.org/docs/2.15/elastic/timer.html#torch.distributed.elastic.timer.debug_info_logging.log_debug_info_for_expired_timers "Link to this definition")

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/elastic/timer.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/elastic/timer.md.txt)

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