### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-policy.html "Policies")
     |
*   [previous](https://docs.python.org/3/library/asyncio-future.html "Futures")
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
*   [Transports and Protocols](https://docs.python.org/3/library/asyncio-protocol.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Transports and Protocols[¶](https://docs.python.org/3/library/asyncio-protocol.html#transports-and-protocols "Link to this heading")

=====================================================================================================================================

Preface

Transports and Protocols are used by the **low-level** event loop APIs such as [`loop.create_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection")
. They use callback-based programming style and enable high-performance implementations of network or IPC protocols (e.g. HTTP).

Essentially, transports and protocols should only be used in libraries and frameworks and never in high-level asyncio applications.

This documentation page covers both [Transports](https://docs.python.org/3/library/asyncio-protocol.html#transports)
 and [Protocols](https://docs.python.org/3/library/asyncio-protocol.html#protocols)
.

Introduction

At the highest level, the transport is concerned with _how_ bytes are transmitted, while the protocol determines _which_ bytes to transmit (and to some extent when).

A different way of saying the same thing: a transport is an abstraction for a socket (or similar I/O endpoint) while a protocol is an abstraction for an application, from the transport’s point of view.

Yet another view is the transport and protocol interfaces together define an abstract interface for using network I/O and interprocess I/O.

There is always a 1:1 relationship between transport and protocol objects: the protocol calls transport methods to send data, while the transport calls protocol methods to pass it data that has been received.

Most of connection oriented event loop methods (such as [`loop.create_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection")
) usually accept a _protocol\_factory_ argument used to create a _Protocol_ object for an accepted connection, represented by a _Transport_ object. Such methods usually return a tuple of `(transport, protocol)`.

Contents

This documentation page contains the following sections:

*   The [Transports](https://docs.python.org/3/library/asyncio-protocol.html#transports)
     section documents asyncio [`BaseTransport`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseTransport "asyncio.BaseTransport")
    , [`ReadTransport`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.ReadTransport "asyncio.ReadTransport")
    , [`WriteTransport`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport "asyncio.WriteTransport")
    , [`Transport`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.Transport "asyncio.Transport")
    , [`DatagramTransport`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.DatagramTransport "asyncio.DatagramTransport")
    , and [`SubprocessTransport`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessTransport "asyncio.SubprocessTransport")
     classes.
    
*   The [Protocols](https://docs.python.org/3/library/asyncio-protocol.html#protocols)
     section documents asyncio [`BaseProtocol`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol "asyncio.BaseProtocol")
    , [`Protocol`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.Protocol "asyncio.Protocol")
    , [`BufferedProtocol`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BufferedProtocol "asyncio.BufferedProtocol")
    , [`DatagramProtocol`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.DatagramProtocol "asyncio.DatagramProtocol")
    , and [`SubprocessProtocol`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessProtocol "asyncio.SubprocessProtocol")
     classes.
    
*   The [Examples](https://docs.python.org/3/library/asyncio-protocol.html#examples)
     section showcases how to work with transports, protocols, and low-level event loop APIs.
    

Transports[¶](https://docs.python.org/3/library/asyncio-protocol.html#transports "Link to this heading")

---------------------------------------------------------------------------------------------------------

**Source code:** [Lib/asyncio/transports.py](https://github.com/python/cpython/tree/3.15/Lib/asyncio/transports.py)

* * *

Transports are classes provided by [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.")
 in order to abstract various kinds of communication channels.

Transport objects are always instantiated by an [asyncio event loop](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-event-loop)
.

asyncio implements transports for TCP, UDP, SSL, and subprocess pipes. The methods available on a transport depend on the transport’s kind.

The transport classes are [not thread safe](https://docs.python.org/3/library/asyncio-dev.html#asyncio-multithreading)
.

### Transports Hierarchy[¶](https://docs.python.org/3/library/asyncio-protocol.html#transports-hierarchy "Link to this heading")

class asyncio.BaseTransport[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseTransport "Link to this definition")

Base class for all transports. Contains methods that all asyncio transports share.

class asyncio.WriteTransport(_BaseTransport_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport "Link to this definition")

A base transport for write-only connections.

Instances of the _WriteTransport_ class are returned from the [`loop.connect_write_pipe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.connect_write_pipe "asyncio.loop.connect_write_pipe")
 event loop method and are also used by subprocess-related methods like [`loop.subprocess_exec()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec "asyncio.loop.subprocess_exec")
.

class asyncio.ReadTransport(_BaseTransport_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.ReadTransport "Link to this definition")

A base transport for read-only connections.

Instances of the _ReadTransport_ class are returned from the [`loop.connect_read_pipe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.connect_read_pipe "asyncio.loop.connect_read_pipe")
 event loop method and are also used by subprocess-related methods like [`loop.subprocess_exec()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec "asyncio.loop.subprocess_exec")
.

class asyncio.Transport(_WriteTransport_, _ReadTransport_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.Transport "Link to this definition")

Interface representing a bidirectional transport, such as a TCP connection.

The user does not instantiate a transport directly; they call a utility function, passing it a protocol factory and other information necessary to create the transport and protocol.

Instances of the _Transport_ class are returned from or used by event loop methods like [`loop.create_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection")
, [`loop.create_unix_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_connection "asyncio.loop.create_unix_connection")
, [`loop.create_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server")
, [`loop.sendfile()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sendfile "asyncio.loop.sendfile")
, etc.

class asyncio.DatagramTransport(_BaseTransport_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.DatagramTransport "Link to this definition")

A transport for datagram (UDP) connections.

Instances of the _DatagramTransport_ class are returned from the [`loop.create_datagram_endpoint()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint "asyncio.loop.create_datagram_endpoint")
 event loop method.

class asyncio.SubprocessTransport(_BaseTransport_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessTransport "Link to this definition")

An abstraction to represent a connection between a parent and its child OS process.

Instances of the _SubprocessTransport_ class are returned from event loop methods [`loop.subprocess_shell()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_shell "asyncio.loop.subprocess_shell")
 and [`loop.subprocess_exec()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec "asyncio.loop.subprocess_exec")
.

### Base Transport[¶](https://docs.python.org/3/library/asyncio-protocol.html#base-transport "Link to this heading")

BaseTransport.close()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseTransport.close "Link to this definition")

Close the transport.

If the transport has a buffer for outgoing data, buffered data will be flushed asynchronously. No more data will be received. After all buffered data is flushed, the protocol’s [`protocol.connection_lost()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol.connection_lost "asyncio.BaseProtocol.connection_lost")
 method will be called with [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
 as its argument. The transport should not be used once it is closed.

BaseTransport.is\_closing()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseTransport.is_closing "Link to this definition")

Return `True` if the transport is closing or is closed.

BaseTransport.get\_extra\_info(_name_, _default\=None_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseTransport.get_extra_info "Link to this definition")

Return information about the transport or underlying resources it uses.

_name_ is a string representing the piece of transport-specific information to get.

_default_ is the value to return if the information is not available, or if the transport does not support querying it with the given third-party event loop implementation or on the current platform.

For example, the following code attempts to get the underlying socket object of the transport:

Copy

sock \= transport.get\_extra\_info('socket')
if sock is not None:
    print(sock.getsockopt(...))

Categories of information that can be queried on some transports:

*   socket:
    
    *   `'peername'`: the remote address to which the socket is connected, result of [`socket.socket.getpeername()`](https://docs.python.org/3/library/socket.html#socket.socket.getpeername "socket.socket.getpeername")
         (`None` on error)
        
    *   `'socket'`: [`socket.socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
         instance
        
    *   `'sockname'`: the socket’s own address, result of [`socket.socket.getsockname()`](https://docs.python.org/3/library/socket.html#socket.socket.getsockname "socket.socket.getsockname")
        
*   SSL socket:
    
    *   `'compression'`: the compression algorithm being used as a string, or `None` if the connection isn’t compressed; result of [`ssl.SSLSocket.compression()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.compression "ssl.SSLSocket.compression")
        
    *   `'cipher'`: a three-value tuple containing the name of the cipher being used, the version of the SSL protocol that defines its use, and the number of secret bits being used; result of [`ssl.SSLSocket.cipher()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.cipher "ssl.SSLSocket.cipher")
        
    *   `'peercert'`: peer certificate; result of [`ssl.SSLSocket.getpeercert()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.getpeercert "ssl.SSLSocket.getpeercert")
        
    *   `'sslcontext'`: [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")
         instance
        
    *   `'ssl_object'`: [`ssl.SSLObject`](https://docs.python.org/3/library/ssl.html#ssl.SSLObject "ssl.SSLObject")
         or [`ssl.SSLSocket`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket "ssl.SSLSocket")
         instance
        
*   pipe:
    
    *   `'pipe'`: pipe object
        
*   subprocess:
    
    *   `'subprocess'`: [`subprocess.Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen")
         instance
        

BaseTransport.set\_protocol(_protocol_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseTransport.set_protocol "Link to this definition")

Set a new protocol.

Switching protocol should only be done when both protocols are documented to support the switch.

BaseTransport.get\_protocol()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseTransport.get_protocol "Link to this definition")

Return the current protocol.

### Read-only Transports[¶](https://docs.python.org/3/library/asyncio-protocol.html#read-only-transports "Link to this heading")

ReadTransport.is\_reading()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.ReadTransport.is_reading "Link to this definition")

Return `True` if the transport is receiving new data.

Added in version 3.7.

ReadTransport.pause\_reading()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.ReadTransport.pause_reading "Link to this definition")

Pause the receiving end of the transport. No data will be passed to the protocol’s [`protocol.data_received()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.Protocol.data_received "asyncio.Protocol.data_received")
 method until [`resume_reading()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.ReadTransport.resume_reading "asyncio.ReadTransport.resume_reading")
 is called.

Changed in version 3.7: The method is idempotent, i.e. it can be called when the transport is already paused or closed.

ReadTransport.resume\_reading()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.ReadTransport.resume_reading "Link to this definition")

Resume the receiving end. The protocol’s [`protocol.data_received()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.Protocol.data_received "asyncio.Protocol.data_received")
 method will be called once again if some data is available for reading.

Changed in version 3.7: The method is idempotent, i.e. it can be called when the transport is already reading.

### Write-only Transports[¶](https://docs.python.org/3/library/asyncio-protocol.html#write-only-transports "Link to this heading")

WriteTransport.abort()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.abort "Link to this definition")

Close the transport immediately, without waiting for pending operations to complete. Buffered data will be lost. No more data will be received. The protocol’s [`protocol.connection_lost()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol.connection_lost "asyncio.BaseProtocol.connection_lost")
 method will eventually be called with [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
 as its argument.

WriteTransport.can\_write\_eof()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.can_write_eof "Link to this definition")

Return [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
 if the transport supports [`write_eof()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.write_eof "asyncio.WriteTransport.write_eof")
, [`False`](https://docs.python.org/3/builtins/constants.html#False "False")
 if not.

WriteTransport.get\_write\_buffer\_size()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.get_write_buffer_size "Link to this definition")

Return the current size of the output buffer used by the transport.

WriteTransport.get\_write\_buffer\_limits()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.get_write_buffer_limits "Link to this definition")

Get the _high_ and _low_ watermarks for write flow control. Return a tuple `(low, high)` where _low_ and _high_ are positive number of bytes.

Use [`set_write_buffer_limits()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.set_write_buffer_limits "asyncio.WriteTransport.set_write_buffer_limits")
 to set the limits.

Added in version 3.4.2.

WriteTransport.set\_write\_buffer\_limits(_high\=None_, _low\=None_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.set_write_buffer_limits "Link to this definition")

Set the _high_ and _low_ watermarks for write flow control.

These two values (measured in number of bytes) control when the protocol’s [`protocol.pause_writing()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol.pause_writing "asyncio.BaseProtocol.pause_writing")
 and [`protocol.resume_writing()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol.resume_writing "asyncio.BaseProtocol.resume_writing")
 methods are called. If specified, the low watermark must be less than or equal to the high watermark. Neither _high_ nor _low_ can be negative.

[`pause_writing()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol.pause_writing "asyncio.BaseProtocol.pause_writing")
 is called when the buffer size becomes greater than or equal to the _high_ value. If writing has been paused, [`resume_writing()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol.resume_writing "asyncio.BaseProtocol.resume_writing")
 is called when the buffer size becomes less than or equal to the _low_ value.

The defaults are implementation-specific. If only the high watermark is given, the low watermark defaults to an implementation-specific value less than or equal to the high watermark. Setting _high_ to zero forces _low_ to zero as well, and causes [`pause_writing()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol.pause_writing "asyncio.BaseProtocol.pause_writing")
 to be called whenever the buffer becomes non-empty. Setting _low_ to zero causes [`resume_writing()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol.resume_writing "asyncio.BaseProtocol.resume_writing")
 to be called only once the buffer is empty. Use of zero for either limit is generally sub-optimal as it reduces opportunities for doing I/O and computation concurrently.

Use [`get_write_buffer_limits()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.get_write_buffer_limits "asyncio.WriteTransport.get_write_buffer_limits")
 to get the limits.

WriteTransport.write(_data_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.write "Link to this definition")

Write some _data_ bytes to the transport.

This method does not block; it buffers the data and arranges for it to be sent out asynchronously.

WriteTransport.writelines(_list\_of\_data_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.writelines "Link to this definition")

Write a list (or any iterable) of data bytes to the transport. This is functionally equivalent to calling [`write()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.write "asyncio.WriteTransport.write")
 on each element yielded by the iterable, but may be implemented more efficiently.

WriteTransport.write\_eof()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.write_eof "Link to this definition")

Close the write end of the transport after flushing all buffered data. Data may still be received.

This method can raise [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError "NotImplementedError")
 if the transport (e.g. SSL) doesn’t support half-closed connections.

### Datagram Transports[¶](https://docs.python.org/3/library/asyncio-protocol.html#datagram-transports "Link to this heading")

DatagramTransport.sendto(_data_, _addr\=None_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.DatagramTransport.sendto "Link to this definition")

Send the _data_ bytes to the remote peer given by _addr_ (a transport-dependent target address). If _addr_ is [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
, the data is sent to the target address given on transport creation.

This method does not block; it buffers the data and arranges for it to be sent out asynchronously.

Changed in version 3.13: This method can be called with an empty bytes object to send a zero-length datagram. The buffer size calculation used for flow control is also updated to account for the datagram header.

DatagramTransport.abort()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.DatagramTransport.abort "Link to this definition")

Close the transport immediately, without waiting for pending operations to complete. Buffered data will be lost. No more data will be received. The protocol’s [`protocol.connection_lost()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol.connection_lost "asyncio.BaseProtocol.connection_lost")
 method will eventually be called with [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
 as its argument.

### Subprocess Transports[¶](https://docs.python.org/3/library/asyncio-protocol.html#subprocess-transports "Link to this heading")

SubprocessTransport.get\_pid()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.get_pid "Link to this definition")

Return the subprocess process id as an integer.

SubprocessTransport.get\_pipe\_transport(_fd_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.get_pipe_transport "Link to this definition")

Return the transport for the communication pipe corresponding to the integer file descriptor _fd_:

*   `0`: writable streaming transport of the standard input (_stdin_), or [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
     if the subprocess was not created with `stdin=PIPE`
    
*   `1`: readable streaming transport of the standard output (_stdout_), or [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
     if the subprocess was not created with `stdout=PIPE`
    
*   `2`: readable streaming transport of the standard error (_stderr_), or [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
     if the subprocess was not created with `stderr=PIPE`
    
*   other _fd_: [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
    

SubprocessTransport.get\_returncode()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.get_returncode "Link to this definition")

Return the subprocess return code as an integer or [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
 if it hasn’t returned, which is similar to the [`subprocess.Popen.returncode`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.returncode "subprocess.Popen.returncode")
 attribute.

SubprocessTransport.kill()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.kill "Link to this definition")

Kill the subprocess.

On POSIX systems, the function sends SIGKILL to the subprocess. On Windows, this method is an alias for [`terminate()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.terminate "asyncio.SubprocessTransport.terminate")
.

See also [`subprocess.Popen.kill()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.kill "subprocess.Popen.kill")
.

SubprocessTransport.send\_signal(_signal_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.send_signal "Link to this definition")

Send the _signal_ number to the subprocess, as in [`subprocess.Popen.send_signal()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.send_signal "subprocess.Popen.send_signal")
.

SubprocessTransport.terminate()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.terminate "Link to this definition")

Stop the subprocess.

On POSIX systems, this method sends [`SIGTERM`](https://docs.python.org/3/library/signal.html#signal.SIGTERM "signal.SIGTERM")
 to the subprocess. On Windows, the Windows API function `TerminateProcess()` is called to stop the subprocess.

See also [`subprocess.Popen.terminate()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.terminate "subprocess.Popen.terminate")
.

SubprocessTransport.close()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.close "Link to this definition")

Kill the subprocess by calling the [`kill()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.kill "asyncio.SubprocessTransport.kill")
 method.

If the subprocess hasn’t returned yet, and close transports of _stdin_, _stdout_, and _stderr_ pipes.

Protocols[¶](https://docs.python.org/3/library/asyncio-protocol.html#protocols "Link to this heading")

-------------------------------------------------------------------------------------------------------

**Source code:** [Lib/asyncio/protocols.py](https://github.com/python/cpython/tree/3.15/Lib/asyncio/protocols.py)

* * *

asyncio provides a set of abstract base classes that should be used to implement network protocols. Those classes are meant to be used together with [transports](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-transport)
.

Subclasses of abstract base protocol classes may implement some or all methods. All these methods are callbacks: they are called by transports on certain events, for example when some data is received. A base protocol method should be called by the corresponding transport.

### Base Protocols[¶](https://docs.python.org/3/library/asyncio-protocol.html#base-protocols "Link to this heading")

class asyncio.BaseProtocol[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol "Link to this definition")

Base protocol with methods that all protocols share.

class asyncio.Protocol(_BaseProtocol_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.Protocol "Link to this definition")

The base class for implementing streaming protocols (TCP, Unix sockets, etc).

class asyncio.BufferedProtocol(_BaseProtocol_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BufferedProtocol "Link to this definition")

A base class for implementing streaming protocols with manual control of the receive buffer.

class asyncio.DatagramProtocol(_BaseProtocol_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.DatagramProtocol "Link to this definition")

The base class for implementing datagram (UDP) protocols.

class asyncio.SubprocessProtocol(_BaseProtocol_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessProtocol "Link to this definition")

The base class for implementing protocols communicating with child processes (unidirectional pipes).

### Base Protocol[¶](https://docs.python.org/3/library/asyncio-protocol.html#base-protocol "Link to this heading")

All asyncio protocols can implement Base Protocol callbacks.

Connection Callbacks

Connection callbacks are called on all protocols, exactly once per a successful connection. All other protocol callbacks can only be called between those two methods.

BaseProtocol.connection\_made(_transport_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol.connection_made "Link to this definition")

Called when a connection is made.

The _transport_ argument is the transport representing the connection. The protocol is responsible for storing the reference to its transport.

BaseProtocol.connection\_lost(_exc_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol.connection_lost "Link to this definition")

Called when the connection is lost or closed.

The argument is either an exception object or [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
. The latter means a regular EOF is received, or the connection was aborted or closed by this side of the connection.

Flow Control Callbacks

Flow control callbacks can be called by transports to pause or resume writing performed by the protocol.

See the documentation of the [`set_write_buffer_limits()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.set_write_buffer_limits "asyncio.WriteTransport.set_write_buffer_limits")
 method for more details.

BaseProtocol.pause\_writing()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol.pause_writing "Link to this definition")

Called when the transport’s buffer goes over the high watermark.

BaseProtocol.resume\_writing()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol.resume_writing "Link to this definition")

Called when the transport’s buffer drains below the low watermark.

If the buffer size equals the high watermark, [`pause_writing()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol.pause_writing "asyncio.BaseProtocol.pause_writing")
 is not called: the buffer size must go strictly over.

Conversely, [`resume_writing()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol.resume_writing "asyncio.BaseProtocol.resume_writing")
 is called when the buffer size is equal or lower than the low watermark. These end conditions are important to ensure that things go as expected when either mark is zero.

### Streaming Protocols[¶](https://docs.python.org/3/library/asyncio-protocol.html#streaming-protocols "Link to this heading")

Event methods, such as [`loop.create_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server")
, [`loop.create_unix_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_server "asyncio.loop.create_unix_server")
, [`loop.create_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection")
, [`loop.create_unix_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_connection "asyncio.loop.create_unix_connection")
, [`loop.connect_accepted_socket()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.connect_accepted_socket "asyncio.loop.connect_accepted_socket")
, [`loop.connect_read_pipe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.connect_read_pipe "asyncio.loop.connect_read_pipe")
, and [`loop.connect_write_pipe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.connect_write_pipe "asyncio.loop.connect_write_pipe")
 accept factories that return streaming protocols.

Protocol.data\_received(_data_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.Protocol.data_received "Link to this definition")

Called when some data is received. _data_ is a non-empty bytes object containing the incoming data.

Whether the data is buffered, chunked or reassembled depends on the transport. In general, you shouldn’t rely on specific semantics and instead make your parsing generic and flexible. However, data is always received in the correct order.

The method can be called an arbitrary number of times while a connection is open.

However, [`protocol.eof_received()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.Protocol.eof_received "asyncio.Protocol.eof_received")
 is called at most once. Once `eof_received()` is called, `data_received()` is not called anymore.

Protocol.eof\_received()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.Protocol.eof_received "Link to this definition")

Called when the other end signals it won’t send any more data (for example by calling [`transport.write_eof()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.write_eof "asyncio.WriteTransport.write_eof")
, if the other end also uses asyncio).

This method may return a false value (including `None`), in which case the transport will close itself. Conversely, if this method returns a true value, the protocol used determines whether to close the transport. Since the default implementation returns `None`, it implicitly closes the connection.

Some transports, including SSL, don’t support half-closed connections, in which case returning true from this method will result in the connection being closed.

State machine:

start -> connection\_made
    \[-> data\_received\]\*
    \[-> eof\_received\]?
-> connection\_lost -> end

### Buffered Streaming Protocols[¶](https://docs.python.org/3/library/asyncio-protocol.html#buffered-streaming-protocols "Link to this heading")

Added in version 3.7.

Buffered Protocols can be used with any event loop method that supports [Streaming Protocols](https://docs.python.org/3/library/asyncio-protocol.html#streaming-protocols)
.

`BufferedProtocol` implementations allow explicit manual allocation and control of the receive buffer. Event loops can then use the buffer provided by the protocol to avoid unnecessary data copies. This can result in noticeable performance improvement for protocols that receive big amounts of data. Sophisticated protocol implementations can significantly reduce the number of buffer allocations.

The following callbacks are called on [`BufferedProtocol`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BufferedProtocol "asyncio.BufferedProtocol")
 instances:

BufferedProtocol.get\_buffer(_sizehint_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BufferedProtocol.get_buffer "Link to this definition")

Called to allocate a new receive buffer.

_sizehint_ is the recommended minimum size for the returned buffer. It is acceptable to return smaller or larger buffers than what _sizehint_ suggests. When set to -1, the buffer size can be arbitrary. It is an error to return a buffer with a zero size.

`get_buffer()` must return an object implementing the [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects)
.

BufferedProtocol.buffer\_updated(_nbytes_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BufferedProtocol.buffer_updated "Link to this definition")

Called when the buffer was updated with the received data.

_nbytes_ is the total number of bytes that were written to the buffer.

BufferedProtocol.eof\_received()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BufferedProtocol.eof_received "Link to this definition")

See the documentation of the [`protocol.eof_received()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.Protocol.eof_received "asyncio.Protocol.eof_received")
 method.

[`get_buffer()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BufferedProtocol.get_buffer "asyncio.BufferedProtocol.get_buffer")
 can be called an arbitrary number of times during a connection. However, [`protocol.eof_received()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.Protocol.eof_received "asyncio.Protocol.eof_received")
 is called at most once and, if called, `get_buffer()` and [`buffer_updated()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BufferedProtocol.buffer_updated "asyncio.BufferedProtocol.buffer_updated")
 won’t be called after it.

State machine:

start -> connection\_made
    \[-> get\_buffer\
        \[-> buffer\_updated\]?\
    \]\*
    \[-> eof\_received\]?
-> connection\_lost -> end

### Datagram Protocols[¶](https://docs.python.org/3/library/asyncio-protocol.html#datagram-protocols "Link to this heading")

Datagram Protocol instances should be constructed by protocol factories passed to the [`loop.create_datagram_endpoint()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint "asyncio.loop.create_datagram_endpoint")
 method.

DatagramProtocol.datagram\_received(_data_, _addr_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.DatagramProtocol.datagram_received "Link to this definition")

Called when a datagram is received. _data_ is a bytes object containing the incoming data. _addr_ is the address of the peer sending the data; the exact format depends on the transport.

DatagramProtocol.error\_received(_exc_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.DatagramProtocol.error_received "Link to this definition")

Called when a previous send or receive operation raises an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
. _exc_ is the `OSError` instance.

This method is called in rare conditions, when the transport (e.g. UDP) detects that a datagram could not be delivered to its recipient. In many conditions though, undeliverable datagrams will be silently dropped.

Note

On BSD systems (macOS, FreeBSD, etc.) flow control is not supported for datagram protocols, because there is no reliable way to detect send failures caused by writing too many packets.

The socket always appears ‘ready’ and excess packets are dropped. An [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 with `errno` set to [`errno.ENOBUFS`](https://docs.python.org/3/library/errno.html#errno.ENOBUFS "errno.ENOBUFS")
 may or may not be raised; if it is raised, it will be reported to [`DatagramProtocol.error_received()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.DatagramProtocol.error_received "asyncio.DatagramProtocol.error_received")
 but otherwise ignored.

### Subprocess Protocols[¶](https://docs.python.org/3/library/asyncio-protocol.html#subprocess-protocols "Link to this heading")

Subprocess Protocol instances should be constructed by protocol factories passed to the [`loop.subprocess_exec()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec "asyncio.loop.subprocess_exec")
 and [`loop.subprocess_shell()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_shell "asyncio.loop.subprocess_shell")
 methods.

SubprocessProtocol.pipe\_data\_received(_fd_, _data_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessProtocol.pipe_data_received "Link to this definition")

Called when the child process writes data into its stdout or stderr pipe.

_fd_ is the integer file descriptor of the pipe.

_data_ is a non-empty bytes object containing the received data.

SubprocessProtocol.pipe\_connection\_lost(_fd_, _exc_)[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessProtocol.pipe_connection_lost "Link to this definition")

Called when one of the pipes communicating with the child process is closed.

_fd_ is the integer file descriptor that was closed.

SubprocessProtocol.process\_exited()[¶](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessProtocol.process_exited "Link to this definition")

Called when the child process has exited.

It can be called before [`pipe_data_received()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessProtocol.pipe_data_received "asyncio.SubprocessProtocol.pipe_data_received")
 and [`pipe_connection_lost()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessProtocol.pipe_connection_lost "asyncio.SubprocessProtocol.pipe_connection_lost")
 methods.

Examples[¶](https://docs.python.org/3/library/asyncio-protocol.html#examples "Link to this heading")

-----------------------------------------------------------------------------------------------------

### TCP Echo Server[¶](https://docs.python.org/3/library/asyncio-protocol.html#tcp-echo-server "Link to this heading")

Create a TCP echo server using the [`loop.create_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server")
 method, send back received data, and close the connection:

Copy

import asyncio

class EchoServerProtocol(asyncio.Protocol):
    def connection\_made(self, transport):
        peername \= transport.get\_extra\_info('peername')
        print(f'Connection from {peername}')
        self.transport \= transport

    def data\_received(self, data):
        message \= data.decode()
        print(f'Data received: {message!r}')

        print(f'Send: {message!r}')
        self.transport.write(data)

        print('Close the client socket')
        self.transport.close()

async def main():
    \# Get a reference to the event loop as we plan to use
    \# low-level APIs.
    loop \= asyncio.get\_running\_loop()

    server \= await loop.create\_server(
        EchoServerProtocol,
        '127.0.0.1', 8888)

    async with server:
        await server.serve\_forever()

asyncio.run(main())

See also

The [TCP echo server using streams](https://docs.python.org/3/library/asyncio-stream.html#asyncio-tcp-echo-server-streams)
 example uses the high-level [`asyncio.start_server()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.start_server "asyncio.start_server")
 function.

### TCP Echo Client[¶](https://docs.python.org/3/library/asyncio-protocol.html#tcp-echo-client "Link to this heading")

A TCP echo client using the [`loop.create_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection")
 method, sends data, and waits until the connection is closed:

Copy

import asyncio

class EchoClientProtocol(asyncio.Protocol):
    def \_\_init\_\_(self, message, on\_con\_lost):
        self.message \= message
        self.on\_con\_lost \= on\_con\_lost

    def connection\_made(self, transport):
        transport.write(self.message.encode())
        print(f'Data sent: {message!r}')

    def data\_received(self, data):
        print(f'Data received: {data.decode()!r}')

    def connection\_lost(self, exc):
        print('The server closed the connection')
        self.on\_con\_lost.set\_result(True)

async def main():
    \# Get a reference to the event loop as we plan to use
    \# low-level APIs.
    loop \= asyncio.get\_running\_loop()

    on\_con\_lost \= loop.create\_future()
    message \= 'Hello World!'

    transport, protocol \= await loop.create\_connection(
        lambda: EchoClientProtocol(message, on\_con\_lost),
        '127.0.0.1', 8888)

    \# Wait until the protocol signals that the connection
    \# is lost and close the transport.
    try:
        await on\_con\_lost
    finally:
        transport.close()

asyncio.run(main())

See also

The [TCP echo client using streams](https://docs.python.org/3/library/asyncio-stream.html#asyncio-tcp-echo-client-streams)
 example uses the high-level [`asyncio.open_connection()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.open_connection "asyncio.open_connection")
 function.

### UDP Echo Server[¶](https://docs.python.org/3/library/asyncio-protocol.html#udp-echo-server "Link to this heading")

A UDP echo server, using the [`loop.create_datagram_endpoint()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint "asyncio.loop.create_datagram_endpoint")
 method, sends back received data:

Copy

import asyncio

class EchoServerProtocol:
    def connection\_made(self, transport):
        self.transport \= transport

    def datagram\_received(self, data, addr):
        message \= data.decode()
        print(f'Received {message!r} from {addr}')
        print(f'Send {message!r} to {addr}')
        self.transport.sendto(data, addr)

async def main():
    print("Starting UDP server")

    \# Get a reference to the event loop as we plan to use
    \# low-level APIs.
    loop \= asyncio.get\_running\_loop()

    \# One protocol instance will be created to serve all
    \# client requests.
    transport, protocol \= await loop.create\_datagram\_endpoint(
        EchoServerProtocol,
        local\_addr\=('127.0.0.1', 9999))

    try:
        await asyncio.sleep(3600)  \# Serve for 1 hour.
    finally:
        transport.close()

asyncio.run(main())

### UDP Echo Client[¶](https://docs.python.org/3/library/asyncio-protocol.html#udp-echo-client "Link to this heading")

A UDP echo client, using the [`loop.create_datagram_endpoint()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint "asyncio.loop.create_datagram_endpoint")
 method, sends data and closes the transport when it receives the answer:

Copy

import asyncio

class EchoClientProtocol:
    def \_\_init\_\_(self, message, on\_con\_lost):
        self.message \= message
        self.on\_con\_lost \= on\_con\_lost
        self.transport \= None

    def connection\_made(self, transport):
        self.transport \= transport
        print('Send:', self.message)
        self.transport.sendto(self.message.encode())

    def datagram\_received(self, data, addr):
        print("Received:", data.decode())

        print("Close the socket")
        self.transport.close()

    def error\_received(self, exc):
        print('Error received:', exc)

    def connection\_lost(self, exc):
        print("Connection closed")
        self.on\_con\_lost.set\_result(True)

async def main():
    \# Get a reference to the event loop as we plan to use
    \# low-level APIs.
    loop \= asyncio.get\_running\_loop()

    on\_con\_lost \= loop.create\_future()
    message \= "Hello World!"

    transport, protocol \= await loop.create\_datagram\_endpoint(
        lambda: EchoClientProtocol(message, on\_con\_lost),
        remote\_addr\=('127.0.0.1', 9999))

    try:
        await on\_con\_lost
    finally:
        transport.close()

asyncio.run(main())

### Connecting Existing Sockets[¶](https://docs.python.org/3/library/asyncio-protocol.html#connecting-existing-sockets "Link to this heading")

Wait until a socket receives data using the [`loop.create_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection")
 method with a protocol:

Copy

import asyncio
import socket

class MyProtocol(asyncio.Protocol):

    def \_\_init\_\_(self, on\_con\_lost):
        self.transport \= None
        self.on\_con\_lost \= on\_con\_lost

    def connection\_made(self, transport):
        self.transport \= transport

    def data\_received(self, data):
        print("Received:", data.decode())

        \# We are done: close the transport;
        \# connection\_lost() will be called automatically.
        self.transport.close()

    def connection\_lost(self, exc):
        \# The socket has been closed
        self.on\_con\_lost.set\_result(True)

async def main():
    \# Get a reference to the event loop as we plan to use
    \# low-level APIs.
    loop \= asyncio.get\_running\_loop()
    on\_con\_lost \= loop.create\_future()

    \# Create a pair of connected sockets
    rsock, wsock \= socket.socketpair()

    \# Register the socket to wait for data.
    transport, protocol \= await loop.create\_connection(
        lambda: MyProtocol(on\_con\_lost), sock\=rsock)

    \# Simulate the reception of data from the network.
    loop.call\_soon(wsock.send, 'abc'.encode())

    try:
        await protocol.on\_con\_lost
    finally:
        transport.close()
        wsock.close()

asyncio.run(main())

See also

The [watch a file descriptor for read events](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-example-watch-fd)
 example uses the low-level [`loop.add_reader()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.add_reader "asyncio.loop.add_reader")
 method to register an FD.

The [register an open socket to wait for data using streams](https://docs.python.org/3/library/asyncio-stream.html#asyncio-example-create-connection-streams)
 example uses high-level streams created by the [`open_connection()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.open_connection "asyncio.open_connection")
 function in a coroutine.

### loop.subprocess\_exec() and SubprocessProtocol[¶](https://docs.python.org/3/library/asyncio-protocol.html#loop-subprocess-exec-and-subprocessprotocol "Link to this heading")

An example of a subprocess protocol used to get the output of a subprocess and to wait for the subprocess exit.

The subprocess is created by the [`loop.subprocess_exec()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec "asyncio.loop.subprocess_exec")
 method:

Copy

import asyncio
import sys

class DateProtocol(asyncio.SubprocessProtocol):
    def \_\_init\_\_(self, exit\_future):
        self.exit\_future \= exit\_future
        self.output \= bytearray()
        self.pipe\_closed \= False
        self.exited \= False

    def pipe\_connection\_lost(self, fd, exc):
        self.pipe\_closed \= True
        self.check\_for\_exit()

    def pipe\_data\_received(self, fd, data):
        self.output.extend(data)

    def process\_exited(self):
        self.exited \= True
        \# process\_exited() method can be called before
        \# pipe\_connection\_lost() method: wait until both methods are
        \# called.
        self.check\_for\_exit()

    def check\_for\_exit(self):
        if self.pipe\_closed and self.exited:
            self.exit\_future.set\_result(True)

async def get\_date():
    \# Get a reference to the event loop as we plan to use
    \# low-level APIs.
    loop \= asyncio.get\_running\_loop()

    code \= 'import datetime as dt; print(dt.datetime.now())'
    exit\_future \= asyncio.Future(loop\=loop)

    \# Create the subprocess controlled by DateProtocol;
    \# redirect the standard output into a pipe.
    transport, protocol \= await loop.subprocess\_exec(
        lambda: DateProtocol(exit\_future),
        sys.executable, '-c', code,
        stdin\=None, stderr\=None)

    \# Wait for the subprocess exit using the process\_exited()
    \# method of the protocol.
    await exit\_future

    \# Close the stdout pipe.
    transport.close()

    \# Read the output which was collected by the
    \# pipe\_data\_received() method of the protocol.
    data \= bytes(protocol.output)
    return data.decode('ascii').rstrip()

date \= asyncio.run(get\_date())
print(f"Current date: {date}")

See also the [same example](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio-example-create-subprocess-exec)
 written using high-level APIs.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Transports and Protocols](https://docs.python.org/3/library/asyncio-protocol.html#)
    *   [Transports](https://docs.python.org/3/library/asyncio-protocol.html#transports)
        *   [Transports Hierarchy](https://docs.python.org/3/library/asyncio-protocol.html#transports-hierarchy)
            
        *   [Base Transport](https://docs.python.org/3/library/asyncio-protocol.html#base-transport)
            
        *   [Read-only Transports](https://docs.python.org/3/library/asyncio-protocol.html#read-only-transports)
            
        *   [Write-only Transports](https://docs.python.org/3/library/asyncio-protocol.html#write-only-transports)
            
        *   [Datagram Transports](https://docs.python.org/3/library/asyncio-protocol.html#datagram-transports)
            
        *   [Subprocess Transports](https://docs.python.org/3/library/asyncio-protocol.html#subprocess-transports)
            
    *   [Protocols](https://docs.python.org/3/library/asyncio-protocol.html#protocols)
        *   [Base Protocols](https://docs.python.org/3/library/asyncio-protocol.html#base-protocols)
            
        *   [Base Protocol](https://docs.python.org/3/library/asyncio-protocol.html#base-protocol)
            
        *   [Streaming Protocols](https://docs.python.org/3/library/asyncio-protocol.html#streaming-protocols)
            
        *   [Buffered Streaming Protocols](https://docs.python.org/3/library/asyncio-protocol.html#buffered-streaming-protocols)
            
        *   [Datagram Protocols](https://docs.python.org/3/library/asyncio-protocol.html#datagram-protocols)
            
        *   [Subprocess Protocols](https://docs.python.org/3/library/asyncio-protocol.html#subprocess-protocols)
            
    *   [Examples](https://docs.python.org/3/library/asyncio-protocol.html#examples)
        *   [TCP Echo Server](https://docs.python.org/3/library/asyncio-protocol.html#tcp-echo-server)
            
        *   [TCP Echo Client](https://docs.python.org/3/library/asyncio-protocol.html#tcp-echo-client)
            
        *   [UDP Echo Server](https://docs.python.org/3/library/asyncio-protocol.html#udp-echo-server)
            
        *   [UDP Echo Client](https://docs.python.org/3/library/asyncio-protocol.html#udp-echo-client)
            
        *   [Connecting Existing Sockets](https://docs.python.org/3/library/asyncio-protocol.html#connecting-existing-sockets)
            
        *   [loop.subprocess\_exec() and SubprocessProtocol](https://docs.python.org/3/library/asyncio-protocol.html#loop-subprocess-exec-and-subprocessprotocol)
            

#### Previous topic

[Futures](https://docs.python.org/3/library/asyncio-future.html "previous chapter")

#### Next topic

[Policies](https://docs.python.org/3/library/asyncio-policy.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Transports+and+Protocols&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fasyncio-protocol.html&pagesource=library%2Fasyncio-protocol.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/asyncio-protocol.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-policy.html "Policies")
     |
*   [previous](https://docs.python.org/3/library/asyncio-future.html "Futures")
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
*   [Transports and Protocols](https://docs.python.org/3/library/asyncio-protocol.html)
    
*    
    
    |
*   Theme Auto Light Dark |