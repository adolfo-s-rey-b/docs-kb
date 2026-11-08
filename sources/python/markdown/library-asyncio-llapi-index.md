### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-dev.html "Developing with asyncio")
     |
*   [previous](https://docs.python.org/3/library/asyncio-api-index.html "High-level API Index")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html)
     »
*   [`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
     »
*   [Low-level API Index](https://docs.python.org/3/library/asyncio-llapi-index.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Low-level API Index[¶](https://docs.python.org/3/library/asyncio-llapi-index.html#low-level-api-index "Link to this heading")

==============================================================================================================================

This page lists all low-level asyncio APIs.

Obtaining the Event Loop[¶](https://docs.python.org/3/library/asyncio-llapi-index.html#obtaining-the-event-loop "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- | 
| [`asyncio.get_running_loop()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.get_running_loop "asyncio.get_running_loop") | The **preferred** function to get the running event loop. |
| [`asyncio.get_event_loop()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.get_event_loop "asyncio.get_event_loop") | Get an event loop instance (running or current via the current policy). |
| [`asyncio.set_event_loop()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.set_event_loop "asyncio.set_event_loop") | Set the event loop as current via the current policy. |
| [`asyncio.new_event_loop()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.new_event_loop "asyncio.new_event_loop") | Create a new event loop. |

Examples

*   [Using asyncio.get\_running\_loop()](https://docs.python.org/3/library/asyncio-future.html#asyncio-example-future)
    .
    

Event Loop Methods[¶](https://docs.python.org/3/library/asyncio-llapi-index.html#event-loop-methods "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

See also the main documentation section about the [Event loop methods](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-event-loop-methods)
.

Lifecycle

|     |     |
| --- | --- | 
| [`loop.run_until_complete()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_until_complete "asyncio.loop.run_until_complete") | Run a Future/Task/awaitable until complete. |
| [`loop.run_forever()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_forever "asyncio.loop.run_forever") | Run the event loop forever. |
| [`loop.stop()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.stop "asyncio.loop.stop") | Stop the event loop. |
| [`loop.close()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.close "asyncio.loop.close") | Close the event loop. |
| [`loop.is_running()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.is_running "asyncio.loop.is_running") | Return `True` if the event loop is running. |
| [`loop.is_closed()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.is_closed "asyncio.loop.is_closed") | Return `True` if the event loop is closed. |
| `await` [`loop.shutdown_asyncgens()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.shutdown_asyncgens "asyncio.loop.shutdown_asyncgens") | Close asynchronous generators. |

Debugging

|     |     |
| --- | --- | 
| [`loop.set_debug()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.set_debug "asyncio.loop.set_debug") | Enable or disable the debug mode. |
| [`loop.get_debug()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.get_debug "asyncio.loop.get_debug") | Get the current debug mode. |

Scheduling Callbacks

|     |     |
| --- | --- | 
| [`loop.call_soon()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon "asyncio.loop.call_soon") | Invoke a callback soon. |
| [`loop.call_soon_threadsafe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon_threadsafe "asyncio.loop.call_soon_threadsafe") | A thread-safe variant of [`loop.call_soon()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon "asyncio.loop.call_soon")<br>. |
| [`loop.call_later()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_later "asyncio.loop.call_later") | Invoke a callback _after_ the given time. |
| [`loop.call_at()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_at "asyncio.loop.call_at") | Invoke a callback _at_ the given time. |

Thread/Interpreter/Process Pool

|     |     |
| --- | --- | 
| `await` [`loop.run_in_executor()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "asyncio.loop.run_in_executor") | Run a CPU-bound or other blocking function in a [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures "concurrent.futures: Execute computations concurrently using threads or processes.")<br> executor. |
| [`loop.set_default_executor()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.set_default_executor "asyncio.loop.set_default_executor") | Set the default executor for [`loop.run_in_executor()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "asyncio.loop.run_in_executor")<br>. |

Tasks and Futures

|     |     |
| --- | --- | 
| [`loop.create_future()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_future "asyncio.loop.create_future") | Create a [`Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future")<br> object. |
| [`loop.create_task()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_task "asyncio.loop.create_task") | Schedule coroutine as a [`Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")<br>. |
| [`loop.set_task_factory()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.set_task_factory "asyncio.loop.set_task_factory") | Set a factory used by [`loop.create_task()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_task "asyncio.loop.create_task")<br> to create [`Tasks`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")<br>. |
| [`loop.get_task_factory()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.get_task_factory "asyncio.loop.get_task_factory") | Get the factory [`loop.create_task()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_task "asyncio.loop.create_task")<br> uses to create [`Tasks`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")<br>. |

DNS

|     |     |
| --- | --- | 
| `await` [`loop.getaddrinfo()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.getaddrinfo "asyncio.loop.getaddrinfo") | Asynchronous version of [`socket.getaddrinfo()`](https://docs.python.org/3/library/socket.html#socket.getaddrinfo "socket.getaddrinfo")<br>. |
| `await` [`loop.getnameinfo()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.getnameinfo "asyncio.loop.getnameinfo") | Asynchronous version of [`socket.getnameinfo()`](https://docs.python.org/3/library/socket.html#socket.getnameinfo "socket.getnameinfo")<br>. |

Networking and IPC

|     |     |
| --- | --- | 
| `await` [`loop.create_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection") | Open a TCP connection. |
| `await` [`loop.create_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server") | Create a TCP server. |
| `await` [`loop.create_unix_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_connection "asyncio.loop.create_unix_connection") | Open a Unix socket connection. |
| `await` [`loop.create_unix_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_server "asyncio.loop.create_unix_server") | Create a Unix socket server. |
| `await` [`loop.connect_accepted_socket()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.connect_accepted_socket "asyncio.loop.connect_accepted_socket") | Wrap a [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")<br> into a `(transport, protocol)` pair. |
| `await` [`loop.create_datagram_endpoint()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint "asyncio.loop.create_datagram_endpoint") | Open a datagram (UDP) connection. |
| `await` [`loop.sendfile()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sendfile "asyncio.loop.sendfile") | Send a file over a transport. |
| `await` [`loop.start_tls()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.start_tls "asyncio.loop.start_tls") | Upgrade an existing connection to TLS. |
| `await` [`loop.connect_read_pipe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.connect_read_pipe "asyncio.loop.connect_read_pipe") | Wrap a read end of a pipe into a `(transport, protocol)` pair. |
| `await` [`loop.connect_write_pipe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.connect_write_pipe "asyncio.loop.connect_write_pipe") | Wrap a write end of a pipe into a `(transport, protocol)` pair. |

Sockets

|     |     |
| --- | --- | 
| `await` [`loop.sock_recv()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sock_recv "asyncio.loop.sock_recv") | Receive data from the [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")<br>. |
| `await` [`loop.sock_recv_into()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sock_recv_into "asyncio.loop.sock_recv_into") | Receive data from the [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")<br> into a buffer. |
| `await` [`loop.sock_recvfrom()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sock_recvfrom "asyncio.loop.sock_recvfrom") | Receive a datagram from the [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")<br>. |
| `await` [`loop.sock_recvfrom_into()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sock_recvfrom_into "asyncio.loop.sock_recvfrom_into") | Receive a datagram from the [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")<br> into a buffer. |
| `await` [`loop.sock_sendall()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sock_sendall "asyncio.loop.sock_sendall") | Send data to the [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")<br>. |
| `await` [`loop.sock_sendto()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sock_sendto "asyncio.loop.sock_sendto") | Send a datagram via the [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")<br> to the given address. |
| `await` [`loop.sock_connect()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sock_connect "asyncio.loop.sock_connect") | Connect the [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")<br>. |
| `await` [`loop.sock_accept()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sock_accept "asyncio.loop.sock_accept") | Accept a [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")<br> connection. |
| `await` [`loop.sock_sendfile()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sock_sendfile "asyncio.loop.sock_sendfile") | Send a file over the [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")<br>. |
| [`loop.add_reader()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.add_reader "asyncio.loop.add_reader") | Start watching a file descriptor for read availability. |
| [`loop.remove_reader()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.remove_reader "asyncio.loop.remove_reader") | Stop watching a file descriptor for read availability. |
| [`loop.add_writer()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.add_writer "asyncio.loop.add_writer") | Start watching a file descriptor for write availability. |
| [`loop.remove_writer()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.remove_writer "asyncio.loop.remove_writer") | Stop watching a file descriptor for write availability. |

Unix Signals

|     |     |
| --- | --- | 
| [`loop.add_signal_handler()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.add_signal_handler "asyncio.loop.add_signal_handler") | Add a handler for a [`signal`](https://docs.python.org/3/library/signal.html#module-signal "signal: Set handlers for asynchronous events.")<br>. |
| [`loop.remove_signal_handler()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.remove_signal_handler "asyncio.loop.remove_signal_handler") | Remove a handler for a [`signal`](https://docs.python.org/3/library/signal.html#module-signal "signal: Set handlers for asynchronous events.")<br>. |

Subprocesses

|     |     |
| --- | --- | 
| [`loop.subprocess_exec()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec "asyncio.loop.subprocess_exec") | Spawn a subprocess. |
| [`loop.subprocess_shell()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_shell "asyncio.loop.subprocess_shell") | Spawn a subprocess from a shell command. |

Error Handling

|     |     |
| --- | --- | 
| [`loop.call_exception_handler()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_exception_handler "asyncio.loop.call_exception_handler") | Call the exception handler. |
| [`loop.set_exception_handler()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.set_exception_handler "asyncio.loop.set_exception_handler") | Set a new exception handler. |
| [`loop.get_exception_handler()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.get_exception_handler "asyncio.loop.get_exception_handler") | Get the current exception handler. |
| [`loop.default_exception_handler()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.default_exception_handler "asyncio.loop.default_exception_handler") | The default exception handler implementation. |

Examples

*   [Using asyncio.new\_event\_loop() and loop.run\_forever()](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-example-lowlevel-helloworld)
    .
    
*   [Using loop.call\_later()](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-example-call-later)
    .
    
*   Using `loop.create_connection()` to implement [an echo-client](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-example-tcp-echo-client-protocol)
    .
    
*   Using `loop.create_connection()` to [connect a socket](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-example-create-connection)
    .
    
*   [Using add\_reader() to watch an FD for read events](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-example-watch-fd)
    .
    
*   [Using loop.add\_signal\_handler()](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-example-unix-signals)
    .
    
*   [Using loop.subprocess\_exec()](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-example-subprocess-proto)
    .
    

Transports[¶](https://docs.python.org/3/library/asyncio-llapi-index.html#transports "Link to this heading")

------------------------------------------------------------------------------------------------------------

All transports implement the following methods:

|     |     |
| --- | --- | 
| [`transport.close()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseTransport.close "asyncio.BaseTransport.close") | Close the transport. |
| [`transport.is_closing()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseTransport.is_closing "asyncio.BaseTransport.is_closing") | Return `True` if the transport is closing or is closed. |
| [`transport.get_extra_info()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseTransport.get_extra_info "asyncio.BaseTransport.get_extra_info") | Request for information about the transport. |
| [`transport.set_protocol()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseTransport.set_protocol "asyncio.BaseTransport.set_protocol") | Set a new protocol. |
| [`transport.get_protocol()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseTransport.get_protocol "asyncio.BaseTransport.get_protocol") | Return the current protocol. |

Transports that can receive data (TCP and Unix connections, pipes, etc). Returned from methods like [`loop.create_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection")
, [`loop.create_unix_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_connection "asyncio.loop.create_unix_connection")
, [`loop.connect_read_pipe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.connect_read_pipe "asyncio.loop.connect_read_pipe")
, etc:

Read Transports

|     |     |
| --- | --- | 
| [`transport.is_reading()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.ReadTransport.is_reading "asyncio.ReadTransport.is_reading") | Return `True` if the transport is receiving. |
| [`transport.pause_reading()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.ReadTransport.pause_reading "asyncio.ReadTransport.pause_reading") | Pause receiving. |
| [`transport.resume_reading()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.ReadTransport.resume_reading "asyncio.ReadTransport.resume_reading") | Resume receiving. |

Transports that can Send data (TCP and Unix connections, pipes, etc). Returned from methods like [`loop.create_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection")
, [`loop.create_unix_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_connection "asyncio.loop.create_unix_connection")
, [`loop.connect_write_pipe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.connect_write_pipe "asyncio.loop.connect_write_pipe")
, etc:

Write Transports

|     |     |
| --- | --- | 
| [`transport.write()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.write "asyncio.WriteTransport.write") | Write data to the transport. |
| [`transport.writelines()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.writelines "asyncio.WriteTransport.writelines") | Write buffers to the transport. |
| [`transport.can_write_eof()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.can_write_eof "asyncio.WriteTransport.can_write_eof") | Return [`True`](https://docs.python.org/3/builtins/constants.html#True "True")<br> if the transport supports sending EOF. |
| [`transport.write_eof()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.write_eof "asyncio.WriteTransport.write_eof") | Close and send EOF after flushing buffered data. |
| [`transport.abort()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.abort "asyncio.WriteTransport.abort") | Close the transport immediately. |
| [`transport.get_write_buffer_size()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.get_write_buffer_size "asyncio.WriteTransport.get_write_buffer_size") | Return the current size of the output buffer. |
| [`transport.get_write_buffer_limits()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.get_write_buffer_limits "asyncio.WriteTransport.get_write_buffer_limits") | Return high and low water marks for write flow control. |
| [`transport.set_write_buffer_limits()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.set_write_buffer_limits "asyncio.WriteTransport.set_write_buffer_limits") | Set new high and low water marks for write flow control. |

Transports returned by [`loop.create_datagram_endpoint()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint "asyncio.loop.create_datagram_endpoint")
:

Datagram Transports

|     |     |
| --- | --- | 
| [`transport.sendto()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.DatagramTransport.sendto "asyncio.DatagramTransport.sendto") | Send data to the remote peer. |
| [`transport.abort()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.DatagramTransport.abort "asyncio.DatagramTransport.abort") | Close the transport immediately. |

Low-level transport abstraction over subprocesses. Returned by [`loop.subprocess_exec()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec "asyncio.loop.subprocess_exec")
 and [`loop.subprocess_shell()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_shell "asyncio.loop.subprocess_shell")
:

Subprocess Transports

|     |     |
| --- | --- | 
| [`transport.get_pid()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.get_pid "asyncio.SubprocessTransport.get_pid") | Return the subprocess process id. |
| [`transport.get_pipe_transport()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.get_pipe_transport "asyncio.SubprocessTransport.get_pipe_transport") | Return the transport for the requested communication pipe (_stdin_, _stdout_, or _stderr_). |
| [`transport.get_returncode()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.get_returncode "asyncio.SubprocessTransport.get_returncode") | Return the subprocess return code. |
| [`transport.kill()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.kill "asyncio.SubprocessTransport.kill") | Kill the subprocess. |
| [`transport.send_signal()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.send_signal "asyncio.SubprocessTransport.send_signal") | Send a signal to the subprocess. |
| [`transport.terminate()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.terminate "asyncio.SubprocessTransport.terminate") | Stop the subprocess. |
| [`transport.close()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.close "asyncio.SubprocessTransport.close") | Kill the subprocess and close all pipes. |

Protocols[¶](https://docs.python.org/3/library/asyncio-llapi-index.html#protocols "Link to this heading")

----------------------------------------------------------------------------------------------------------

Protocol classes can implement the following **callback methods**:

|     |     |
| --- | --- | 
| `callback` [`connection_made()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol.connection_made "asyncio.BaseProtocol.connection_made") | Called when a connection is made. |
| `callback` [`connection_lost()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol.connection_lost "asyncio.BaseProtocol.connection_lost") | Called when the connection is lost or closed. |
| `callback` [`pause_writing()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol.pause_writing "asyncio.BaseProtocol.pause_writing") | Called when the transport’s buffer goes over the high water mark. |
| `callback` [`resume_writing()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol.resume_writing "asyncio.BaseProtocol.resume_writing") | Called when the transport’s buffer drains below the low water mark. |

Streaming Protocols (TCP, Unix Sockets, Pipes)

|     |     |
| --- | --- | 
| `callback` [`data_received()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.Protocol.data_received "asyncio.Protocol.data_received") | Called when some data is received. |
| `callback` [`eof_received()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.Protocol.eof_received "asyncio.Protocol.eof_received") | Called when an EOF is received. |

Buffered Streaming Protocols

|     |     |
| --- | --- | 
| `callback` [`get_buffer()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BufferedProtocol.get_buffer "asyncio.BufferedProtocol.get_buffer") | Called to allocate a new receive buffer. |
| `callback` [`buffer_updated()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BufferedProtocol.buffer_updated "asyncio.BufferedProtocol.buffer_updated") | Called when the buffer was updated with the received data. |
| `callback` [`eof_received()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BufferedProtocol.eof_received "asyncio.BufferedProtocol.eof_received") | Called when an EOF is received. |

Datagram Protocols

|     |     |
| --- | --- | 
| `callback` [`datagram_received()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.DatagramProtocol.datagram_received "asyncio.DatagramProtocol.datagram_received") | Called when a datagram is received. |
| `callback` [`error_received()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.DatagramProtocol.error_received "asyncio.DatagramProtocol.error_received") | Called when a previous send or receive operation raises an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")<br>. |

Subprocess Protocols

|     |     |
| --- | --- | 
| `callback` [`pipe_data_received()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessProtocol.pipe_data_received "asyncio.SubprocessProtocol.pipe_data_received") | Called when the child process writes data into its _stdout_ or _stderr_ pipe. |
| `callback` [`pipe_connection_lost()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessProtocol.pipe_connection_lost "asyncio.SubprocessProtocol.pipe_connection_lost") | Called when one of the pipes communicating with the child process is closed. |
| `callback` [`process_exited()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessProtocol.process_exited "asyncio.SubprocessProtocol.process_exited") | Called when the child process has exited. It can be called before [`pipe_data_received()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessProtocol.pipe_data_received "asyncio.SubprocessProtocol.pipe_data_received")<br> and [`pipe_connection_lost()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessProtocol.pipe_connection_lost "asyncio.SubprocessProtocol.pipe_connection_lost")<br> methods. |

Event Loop Policies[¶](https://docs.python.org/3/library/asyncio-llapi-index.html#event-loop-policies "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

Policies is a low-level mechanism to alter the behavior of functions like [`asyncio.get_event_loop()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.get_event_loop "asyncio.get_event_loop")
. See also the main [policies section](https://docs.python.org/3/library/asyncio-policy.html#asyncio-policies)
 for more details.

Accessing Policies

|     |     |
| --- | --- | 
| [`asyncio.get_event_loop_policy()`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.get_event_loop_policy "asyncio.get_event_loop_policy") | Return the current process-wide policy. |
| [`asyncio.set_event_loop_policy()`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.set_event_loop_policy "asyncio.set_event_loop_policy") | Set a new process-wide policy. |
| [`AbstractEventLoopPolicy`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.AbstractEventLoopPolicy "asyncio.AbstractEventLoopPolicy") | Base class for policy objects. |

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Low-level API Index](https://docs.python.org/3/library/asyncio-llapi-index.html#)
    *   [Obtaining the Event Loop](https://docs.python.org/3/library/asyncio-llapi-index.html#obtaining-the-event-loop)
        
    *   [Event Loop Methods](https://docs.python.org/3/library/asyncio-llapi-index.html#event-loop-methods)
        
    *   [Transports](https://docs.python.org/3/library/asyncio-llapi-index.html#transports)
        
    *   [Protocols](https://docs.python.org/3/library/asyncio-llapi-index.html#protocols)
        
    *   [Event Loop Policies](https://docs.python.org/3/library/asyncio-llapi-index.html#event-loop-policies)
        

#### Previous topic

[High-level API Index](https://docs.python.org/3/library/asyncio-api-index.html "previous chapter")

#### Next topic

[Developing with asyncio](https://docs.python.org/3/library/asyncio-dev.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Low-level+API+Index&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fasyncio-llapi-index.html&pagesource=library%2Fasyncio-llapi-index.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/asyncio-llapi-index.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-dev.html "Developing with asyncio")
     |
*   [previous](https://docs.python.org/3/library/asyncio-api-index.html "High-level API Index")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html)
     »
*   [`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
     »
*   [Low-level API Index](https://docs.python.org/3/library/asyncio-llapi-index.html)
    
*    
    
    |
*   Theme Auto Light Dark |