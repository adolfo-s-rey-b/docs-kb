### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/ssl.html "ssl — TLS/SSL wrapper for socket objects")
     |
*   [previous](https://docs.python.org/3/library/asyncio-threading.html "asyncio and free-threaded Python")
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
*   [`socket` — Low-level networking interface](https://docs.python.org/3/library/socket.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`socket` — Low-level networking interface[¶](https://docs.python.org/3/library/socket.html#module-socket "Link to this heading")

=================================================================================================================================

**Source code:** [Lib/socket.py](https://github.com/python/cpython/tree/3.15/Lib/socket.py)

* * *

This module provides access to the BSD _socket_ interface. It is available on all modern Unix systems, Windows, MacOS, and probably additional platforms.

Note

Some behavior may be platform dependent, since calls are made to the operating system socket APIs.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability)
 for more information.

The Python interface is a straightforward transliteration of the Unix system call and library interface for sockets to Python’s object-oriented style: the [`socket()`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
 function returns a _socket object_ whose methods implement the various socket system calls. Parameter types are somewhat higher-level than in the C interface: as with `read()` and `write()` operations on Python files, buffer allocation on receive operations is automatic, and buffer length is implicit on send operations.

See also

Module [`socketserver`](https://docs.python.org/3/library/socketserver.html#module-socketserver "socketserver: A framework for network servers.")

Classes that simplify writing network servers.

Module [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")

A TLS/SSL wrapper for socket objects.

Socket families[¶](https://docs.python.org/3/library/socket.html#socket-families "Link to this heading")

---------------------------------------------------------------------------------------------------------

Depending on the system and the build options, various socket families are supported by this module.

The address format required by a particular socket object is automatically selected based on the address family specified when the socket object was created. Socket addresses are represented as follows:

*   The address of an [`AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX")
     socket bound to a file system node is represented as a string, using the file system encoding and the `'surrogateescape'` error handler (see [**PEP 383**](https://peps.python.org/pep-0383/)
    ). An address in Linux’s abstract namespace is returned as a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
     with an initial null byte; note that sockets in this namespace can communicate with normal file system sockets, so programs intended to run on Linux may need to deal with both types of address. A string or bytes-like object can be used for either type of address when passing it as an argument.
    
    Changed in version 3.3: Previously, [`AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX")
     socket paths were assumed to use UTF-8 encoding.
    
    Changed in version 3.5: Writable [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
     is now accepted.
    

*   A pair `(host, port)` is used for the [`AF_INET`](https://docs.python.org/3/library/socket.html#socket.AF_INET "socket.AF_INET")
     address family, where _host_ is a string representing either a hostname in internet domain notation like `'daring.cwi.nl'` or an IPv4 address like `'100.50.200.5'`, and _port_ is an integer.
    
    *   For IPv4 addresses, two special forms are accepted instead of a host address: `''` represents `INADDR_ANY`, which is used to bind to all interfaces, and the string `'<broadcast>'` represents `INADDR_BROADCAST`. This behavior is not compatible with IPv6, therefore, you may want to avoid these if you intend to support IPv6 with your Python programs.
        
*   For [`AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6")
     address family, a four-tuple `(host, port, flowinfo, scope_id)` is used, where _flowinfo_ and _scope\_id_ represent the `sin6_flowinfo` and `sin6_scope_id` members in `struct sockaddr_in6` in C. For `socket` module methods, _flowinfo_ and _scope\_id_ can be omitted just for backward compatibility. Note, however, omission of _scope\_id_ can cause problems in manipulating scoped IPv6 addresses.
    
    Changed in version 3.7: For multicast addresses (with _scope\_id_ meaningful) _address_ may not contain `%scope_id` (or `zone id`) part. This information is superfluous and may be safely omitted (recommended).
    
*   `AF_NETLINK` sockets are represented as pairs `(pid, groups)`.
    
*   Linux-only support for TIPC is available using the `AF_TIPC` address family. TIPC is an open, non-IP based networked protocol designed for use in clustered computer environments. Addresses are represented by a tuple, and the fields depend on the address type. The general tuple form is `(addr_type, v1, v2, v3 [, scope])`, where:
    
    *   _addr\_type_ is one of `TIPC_ADDR_NAMESEQ`, `TIPC_ADDR_NAME`, or `TIPC_ADDR_ID`.
        
    *   _scope_ is one of `TIPC_ZONE_SCOPE`, `TIPC_CLUSTER_SCOPE`, and `TIPC_NODE_SCOPE`.
        
    *   If _addr\_type_ is `TIPC_ADDR_NAME`, then _v1_ is the server type, _v2_ is the port identifier, and _v3_ should be 0.
        
        If _addr\_type_ is `TIPC_ADDR_NAMESEQ`, then _v1_ is the server type, _v2_ is the lower port number, and _v3_ is the upper port number.
        
        If _addr\_type_ is `TIPC_ADDR_ID`, then _v1_ is the node, _v2_ is the reference, and _v3_ should be set to 0.
        
*   A tuple `(interface, )` is used for the [`AF_CAN`](https://docs.python.org/3/library/socket.html#socket.AF_CAN "socket.AF_CAN")
     address family, where _interface_ is a string representing a network interface name like `'can0'`. The network interface name `''` can be used to receive packets from all network interfaces of this family.
    
    *   [`CAN_ISOTP`](https://docs.python.org/3/library/socket.html#socket.CAN_ISOTP "socket.CAN_ISOTP")
         protocol requires a tuple `(interface, rx_addr, tx_addr)` where both additional parameters are unsigned long integer that represent a CAN identifier (standard or extended).
        
    *   [`CAN_J1939`](https://docs.python.org/3/library/socket.html#socket.CAN_J1939 "socket.CAN_J1939")
         protocol requires a tuple `(interface, name, pgn, addr)` where additional parameters are 64-bit unsigned integer representing the ECU name, a 32-bit unsigned integer representing the Parameter Group Number (PGN), and an 8-bit integer representing the address.
        
*   A string or a tuple `(id, unit)` is used for the `SYSPROTO_CONTROL` protocol of the `PF_SYSTEM` family. The string is the name of a kernel control using a dynamically assigned ID. The tuple can be used if ID and unit number of the kernel control are known or if a registered ID is used.
    
    Added in version 3.3.
    
*   [`AF_BLUETOOTH`](https://docs.python.org/3/library/socket.html#socket.AF_BLUETOOTH "socket.AF_BLUETOOTH")
     supports the following protocols and address formats:
    
    *   [`BTPROTO_L2CAP`](https://docs.python.org/3/library/socket.html#socket.BTPROTO_L2CAP "socket.BTPROTO_L2CAP")
         accepts a tuple `(bdaddr, psm[, cid[, bdaddr_type]])` where:
        
        *   `bdaddr` is a string specifying the Bluetooth address.
            
        *   `psm` is an integer specifying the Protocol/Service Multiplexer.
            
        *   `cid` is an optional integer specifying the Channel Identifier. If not given, defaults to zero.
            
        *   `bdaddr_type` is an optional integer specifying the address type; one of [`BDADDR_BREDR`](https://docs.python.org/3/library/socket.html#socket.BDADDR_BREDR "socket.BDADDR_BREDR")
             (default), [`BDADDR_LE_PUBLIC`](https://docs.python.org/3/library/socket.html#socket.BDADDR_LE_PUBLIC "socket.BDADDR_LE_PUBLIC")
            , [`BDADDR_LE_RANDOM`](https://docs.python.org/3/library/socket.html#socket.BDADDR_LE_RANDOM "socket.BDADDR_LE_RANDOM")
            .
            
        
        Changed in version 3.14: Added `cid` and `bdaddr_type` fields.
        
    *   [`BTPROTO_RFCOMM`](https://docs.python.org/3/library/socket.html#socket.BTPROTO_RFCOMM "socket.BTPROTO_RFCOMM")
         accepts `(bdaddr, channel)` where `bdaddr` is the Bluetooth address as a string and `channel` is an integer.
        
    *   [`BTPROTO_HCI`](https://docs.python.org/3/library/socket.html#socket.BTPROTO_HCI "socket.BTPROTO_HCI")
         accepts a format that depends on your OS.
        
        *   On Linux it accepts an integer `device_id` or a tuple `(device_id, [channel])` where `device_id` specifies the number of the Bluetooth device, and `channel` is an optional integer specifying the HCI channel ([`HCI_CHANNEL_RAW`](https://docs.python.org/3/library/socket.html#socket.HCI_CHANNEL_RAW "socket.HCI_CHANNEL_RAW")
             by default).
            
        *   On FreeBSD, NetBSD and DragonFly BSD it accepts `bdaddr` where `bdaddr` is the Bluetooth address as a string.
            
        
        Changed in version 3.2: NetBSD and DragonFlyBSD support added.
        
        Changed in version 3.13.3: FreeBSD support added.
        
        Changed in version 3.14: Added `channel` field. `device_id` not packed in a tuple is now accepted.
        
    *   [`BTPROTO_SCO`](https://docs.python.org/3/library/socket.html#socket.BTPROTO_SCO "socket.BTPROTO_SCO")
         accepts `bdaddr` where `bdaddr` is the Bluetooth address as a string or a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
         object. (ex. `'12:23:34:45:56:67'` or `b'12:23:34:45:56:67'`)
        
        Changed in version 3.14: FreeBSD support added.
        
*   [`AF_ALG`](https://docs.python.org/3/library/socket.html#socket.AF_ALG "socket.AF_ALG")
     is a Linux-only socket based interface to Kernel cryptography. An algorithm socket is configured with a tuple of two to four elements `(type, name [, feat [, mask]])`, where:
    
    *   _type_ is the algorithm type as string, e.g. `aead`, `hash`, `skcipher` or `rng`.
        
    *   _name_ is the algorithm name and operation mode as string, e.g. `sha256`, `hmac(sha256)`, `cbc(aes)` or `drbg_nopr_ctr_aes256`.
        
    *   _feat_ and _mask_ are unsigned 32bit integers.
        
    
    [Availability](https://docs.python.org/3/library/intro.html#availability)
    : Linux >= 2.6.38.
    
    Some algorithm types require more recent Kernels.
    
    Added in version 3.6.
    
*   [`AF_VSOCK`](https://docs.python.org/3/library/socket.html#socket.AF_VSOCK "socket.AF_VSOCK")
     allows communication between virtual machines and their hosts. The sockets are represented as a `(CID, port)` tuple where the context ID or CID and port are integers.
    
    [Availability](https://docs.python.org/3/library/intro.html#availability)
    : Linux >= 3.9
    
    See _[vsock(7)](https://manpages.debian.org/vsock(7))
    _
    
    Added in version 3.7.
    
*   [`AF_PACKET`](https://docs.python.org/3/library/socket.html#socket.AF_PACKET "socket.AF_PACKET")
     is a low-level interface directly to network devices. The addresses are represented by the tuple `(ifname, proto[, pkttype[, hatype[, addr]]])` where:
    
    *   _ifname_ - String specifying the device name.
        
    *   _proto_ - The Ethernet protocol number. May be [`ETH_P_ALL`](https://docs.python.org/3/library/socket.html#socket.ETH_P_ALL "socket.ETH_P_ALL")
         to capture all protocols, one of the [ETHERTYPE\_\* constants](https://docs.python.org/3/library/socket.html#socket-ethernet-types)
         or any other Ethernet protocol number.
        
    *   _pkttype_ - Optional integer specifying the packet type:
        
        *   `PACKET_HOST` (the default) - Packet addressed to the local host.
            
        *   `PACKET_BROADCAST` - Physical-layer broadcast packet.
            
        *   `PACKET_MULTICAST` - Packet sent to a physical-layer multicast address.
            
        *   `PACKET_OTHERHOST` - Packet to some other host that has been caught by a device driver in promiscuous mode.
            
        *   `PACKET_OUTGOING` - Packet originating from the local host that is looped back to a packet socket.
            
    *   _hatype_ - Optional integer specifying the ARP hardware address type.
        
    *   _addr_ - Optional bytes-like object specifying the hardware physical address, whose interpretation depends on the device.
        
    
    [Availability](https://docs.python.org/3/library/intro.html#availability)
    : Linux >= 2.2.
    
*   [`AF_QIPCRTR`](https://docs.python.org/3/library/socket.html#socket.AF_QIPCRTR "socket.AF_QIPCRTR")
     is a Linux-only socket based interface for communicating with services running on co-processors in Qualcomm platforms. The address family is represented as a `(node, port)` tuple where the _node_ and _port_ are non-negative integers.
    
    [Availability](https://docs.python.org/3/library/intro.html#availability)
    : Linux >= 4.7.
    
    Added in version 3.8.
    
*   `IPPROTO_UDPLITE` is a variant of UDP which allows you to specify what portion of a packet is covered with the checksum. It adds two socket options that you can change. `self.setsockopt(IPPROTO_UDPLITE, UDPLITE_SEND_CSCOV, length)` will change what portion of outgoing packets are covered by the checksum and `self.setsockopt(IPPROTO_UDPLITE, UDPLITE_RECV_CSCOV, length)` will filter out packets which cover too little of their data. In both cases `length` should be in `range(8, 2**16, 8)`.
    
    Such a socket should be constructed with `socket(AF_INET, SOCK_DGRAM, IPPROTO_UDPLITE)` for IPv4 or `socket(AF_INET6, SOCK_DGRAM, IPPROTO_UDPLITE)` for IPv6.
    
    [Availability](https://docs.python.org/3/library/intro.html#availability)
    : Linux >= 2.6.20, FreeBSD >= 10.1
    
    Added in version 3.9.
    
*   [`AF_HYPERV`](https://docs.python.org/3/library/socket.html#socket.AF_HYPERV "socket.AF_HYPERV")
     is a Windows-only socket based interface for communicating with Hyper-V hosts and guests. The address family is represented as a `(vm_id, service_id)` tuple where the `vm_id` and `service_id` are UUID strings.
    
    The `vm_id` is the virtual machine identifier or a set of known VMID values if the target is not a specific virtual machine. Known VMID constants defined on `socket` are:
    
    *   `HV_GUID_ZERO`
        
    *   `HV_GUID_BROADCAST`
        
    *   `HV_GUID_WILDCARD` - Used to bind on itself and accept connections from all partitions.
        
    *   `HV_GUID_CHILDREN` - Used to bind on itself and accept connection from child partitions.
        
    *   `HV_GUID_LOOPBACK` - Used as a target to itself.
        
    *   `HV_GUID_PARENT` - When used as a bind accepts connection from the parent partition. When used as an address target it will connect to the parent partition.
        
    
    The `service_id` is the service identifier of the registered service.
    
    Added in version 3.12.
    

If you use a hostname in the _host_ portion of IPv4/v6 socket address, the program may show a nondeterministic behavior, as Python uses the first address returned from the DNS resolution. The socket address will be resolved differently into an actual IPv4/v6 address, depending on the results from DNS resolution and/or the host configuration. For deterministic behavior use a numeric address in _host_ portion.

All errors raise exceptions. The normal exceptions for invalid argument types and out-of-memory conditions can be raised. Errors related to socket or address semantics raise [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 or one of its subclasses.

Non-blocking mode is supported through [`setblocking()`](https://docs.python.org/3/library/socket.html#socket.socket.setblocking "socket.socket.setblocking")
. A generalization of this based on timeouts is supported through [`settimeout()`](https://docs.python.org/3/library/socket.html#socket.socket.settimeout "socket.socket.settimeout")
.

Module contents[¶](https://docs.python.org/3/library/socket.html#module-contents "Link to this heading")

---------------------------------------------------------------------------------------------------------

The module `socket` exports the following elements.

### Exceptions[¶](https://docs.python.org/3/library/socket.html#exceptions "Link to this heading")

exception socket.error[¶](https://docs.python.org/3/library/socket.html#socket.error "Link to this definition")

A deprecated alias of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
.

Changed in version 3.3: Following [**PEP 3151**](https://peps.python.org/pep-3151/)
, this class was made an alias of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
.

exception socket.herror[¶](https://docs.python.org/3/library/socket.html#socket.herror "Link to this definition")

A subclass of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
, this exception is raised for address-related errors, i.e. for functions that use _h\_errno_ in the POSIX C API, including [`gethostbyname_ex()`](https://docs.python.org/3/library/socket.html#socket.gethostbyname_ex "socket.gethostbyname_ex")
 and [`gethostbyaddr()`](https://docs.python.org/3/library/socket.html#socket.gethostbyaddr "socket.gethostbyaddr")
. The accompanying value is a pair `(h_errno, string)` representing an error returned by a library call. _h\_errno_ is a numeric value, while _string_ represents the description of _h\_errno_, as returned by the `hstrerror()` C function.

Changed in version 3.3: This class was made a subclass of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
.

exception socket.gaierror[¶](https://docs.python.org/3/library/socket.html#socket.gaierror "Link to this definition")

A subclass of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
, this exception is raised for address-related errors by [`getaddrinfo()`](https://docs.python.org/3/library/socket.html#socket.getaddrinfo "socket.getaddrinfo")
 and [`getnameinfo()`](https://docs.python.org/3/library/socket.html#socket.getnameinfo "socket.getnameinfo")
. The accompanying value is a pair `(error, string)` representing an error returned by a library call. _string_ represents the description of _error_, as returned by the `gai_strerror()` C function. The numeric _error_ value will match one of the `EAI_*` constants defined in this module.

Changed in version 3.3: This class was made a subclass of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
.

exception socket.timeout[¶](https://docs.python.org/3/library/socket.html#socket.timeout "Link to this definition")

A deprecated alias of [`TimeoutError`](https://docs.python.org/3/builtins/exceptions.html#TimeoutError "TimeoutError")
.

A subclass of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
, this exception is raised when a timeout occurs on a socket which has had timeouts enabled via a prior call to [`settimeout()`](https://docs.python.org/3/library/socket.html#socket.socket.settimeout "socket.socket.settimeout")
 (or implicitly through [`setdefaulttimeout()`](https://docs.python.org/3/library/socket.html#socket.setdefaulttimeout "socket.setdefaulttimeout")
). The accompanying value is a string whose value is currently always “timed out”.

Changed in version 3.3: This class was made a subclass of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
.

Changed in version 3.10: This class was made an alias of [`TimeoutError`](https://docs.python.org/3/builtins/exceptions.html#TimeoutError "TimeoutError")
.

### Constants[¶](https://docs.python.org/3/library/socket.html#constants "Link to this heading")

The AF\_\* and SOCK\_\* constants are now `AddressFamily` and `SocketKind` [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum")
 collections.

Added in version 3.4.

socket.AF\_UNIX[¶](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "Link to this definition")

socket.AF\_INET[¶](https://docs.python.org/3/library/socket.html#socket.AF_INET "Link to this definition")

socket.AF\_INET6[¶](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "Link to this definition")

These constants represent the address (and protocol) families, used for the first argument to [`socket()`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
. If the [`AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX")
 constant is not defined then this protocol is unsupported. More constants may be available depending on the system.

socket.AF\_UNSPEC[¶](https://docs.python.org/3/library/socket.html#socket.AF_UNSPEC "Link to this definition")

[`AF_UNSPEC`](https://docs.python.org/3/library/socket.html#socket.AF_UNSPEC "socket.AF_UNSPEC")
 means that [`getaddrinfo()`](https://docs.python.org/3/library/socket.html#socket.getaddrinfo "socket.getaddrinfo")
 should return socket addresses for any address family (either IPv4, IPv6, or any other) that can be used.

socket.SOCK\_STREAM[¶](https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM "Link to this definition")

socket.SOCK\_DGRAM[¶](https://docs.python.org/3/library/socket.html#socket.SOCK_DGRAM "Link to this definition")

socket.SOCK\_RAW[¶](https://docs.python.org/3/library/socket.html#socket.SOCK_RAW "Link to this definition")

socket.SOCK\_RDM[¶](https://docs.python.org/3/library/socket.html#socket.SOCK_RDM "Link to this definition")

socket.SOCK\_SEQPACKET[¶](https://docs.python.org/3/library/socket.html#socket.SOCK_SEQPACKET "Link to this definition")

These constants represent the socket types, used for the second argument to [`socket()`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
. More constants may be available depending on the system. (Only [`SOCK_STREAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM "socket.SOCK_STREAM")
 and [`SOCK_DGRAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_DGRAM "socket.SOCK_DGRAM")
 appear to be generally useful.)

socket.SOCK\_CLOEXEC[¶](https://docs.python.org/3/library/socket.html#socket.SOCK_CLOEXEC "Link to this definition")

socket.SOCK\_NONBLOCK[¶](https://docs.python.org/3/library/socket.html#socket.SOCK_NONBLOCK "Link to this definition")

These two constants, if defined, can be combined with the socket types and allow you to set some flags atomically (thus avoiding possible race conditions and the need for separate calls).

See also

[Secure File Descriptor Handling](https://udrepper.livejournal.com/20407.html)
 for a more thorough explanation.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.27.

Added in version 3.2.

SO\_\*

socket.SOMAXCONN[¶](https://docs.python.org/3/library/socket.html#socket.SOMAXCONN "Link to this definition")

MSG\_\*

SOL\_\*

SCM\_\*

IPPROTO\_\*

IPPORT\_\*

INADDR\_\*

IP\_\*

IPV6\_\*

EAI\_\*

AI\_\*

NI\_\*

TCP\_\*

Many constants of these forms, documented in the Unix documentation on sockets and/or the IP protocol, are also defined in the socket module. They are generally used in arguments to the [`setsockopt()`](https://docs.python.org/3/library/socket.html#socket.socket.setsockopt "socket.socket.setsockopt")
 and [`getsockopt()`](https://docs.python.org/3/library/socket.html#socket.socket.getsockopt "socket.socket.getsockopt")
 methods of socket objects. In most cases, only those symbols that are defined in the Unix header files are defined; for a few symbols, default values are provided.

Changed in version 3.6: `SO_DOMAIN`, `SO_PROTOCOL`, `SO_PEERSEC`, `SO_PASSSEC`, `TCP_USER_TIMEOUT`, `TCP_CONGESTION` were added.

Changed in version 3.6.5: Added support for `TCP_FASTOPEN`, `TCP_KEEPCNT` on Windows platforms when available.

Changed in version 3.7: `TCP_NOTSENT_LOWAT` was added.

Added support for `TCP_KEEPIDLE`, `TCP_KEEPINTVL` on Windows platforms when available.

Changed in version 3.10: `IP_RECVTOS` was added. Added `TCP_KEEPALIVE`. On MacOS this constant can be used in the same way that `TCP_KEEPIDLE` is used on Linux.

Changed in version 3.11: Added `TCP_CONNECTION_INFO`. On MacOS this constant can be used in the same way that `TCP_INFO` is used on Linux and BSD.

Changed in version 3.12: Added `SO_RTABLE` and `SO_USER_COOKIE`. On OpenBSD and FreeBSD respectively those constants can be used in the same way that `SO_MARK` is used on Linux. Also added missing TCP socket options from Linux: `TCP_MD5SIG`, `TCP_THIN_LINEAR_TIMEOUTS`, `TCP_THIN_DUPACK`, `TCP_REPAIR`, `TCP_REPAIR_QUEUE`, `TCP_QUEUE_SEQ`, `TCP_REPAIR_OPTIONS`, `TCP_TIMESTAMP`, `TCP_CC_INFO`, `TCP_SAVE_SYN`, `TCP_SAVED_SYN`, `TCP_REPAIR_WINDOW`, `TCP_FASTOPEN_CONNECT`, `TCP_ULP`, `TCP_MD5SIG_EXT`, `TCP_FASTOPEN_KEY`, `TCP_FASTOPEN_NO_COOKIE`, `TCP_ZEROCOPY_RECEIVE`, `TCP_INQ`, `TCP_TX_DELAY`. Added `IP_PKTINFO`, `IP_UNBLOCK_SOURCE`, `IP_BLOCK_SOURCE`, `IP_ADD_SOURCE_MEMBERSHIP`, `IP_DROP_SOURCE_MEMBERSHIP`.

Changed in version 3.13: Added `SO_BINDTOIFINDEX`. On Linux this constant can be used in the same way that `SO_BINDTODEVICE` is used, but with the index of a network interface instead of its name.

Changed in version 3.14: Added missing `IP_FREEBIND`, `IP_RECVERR`, `IPV6_RECVERR`, `IP_RECVTTL`, and `IP_RECVORIGDSTADDR` on Linux.

Changed in version 3.14: Added support for `TCP_QUICKACK` on Windows platforms when available.

Changed in version 3.15: `IPV6_HDRINCL` was added. Added support for `SO_PASSRIGHTS` on Linux platforms when available.

socket.AF\_CAN[¶](https://docs.python.org/3/library/socket.html#socket.AF_CAN "Link to this definition")

socket.PF\_CAN[¶](https://docs.python.org/3/library/socket.html#socket.PF_CAN "Link to this definition")

SOL\_CAN\_\*

CAN\_\*

Many constants of these forms, documented in the Linux documentation, are also defined in the socket module.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.25, NetBSD >= 8.

Added in version 3.3.

Changed in version 3.11: NetBSD support was added.

Changed in version 3.14: Restored missing `CAN_RAW_ERR_FILTER` on Linux.

socket.CAN\_BCM[¶](https://docs.python.org/3/library/socket.html#socket.CAN_BCM "Link to this definition")

CAN\_BCM\_\*

CAN\_BCM, in the CAN protocol family, is the broadcast manager (BCM) protocol. Broadcast manager constants, documented in the Linux documentation, are also defined in the socket module.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.25.

Note

The `CAN_BCM_CAN_FD_FRAME` flag is only available on Linux >= 4.8.

Added in version 3.4.

socket.CAN\_RAW\_FD\_FRAMES[¶](https://docs.python.org/3/library/socket.html#socket.CAN_RAW_FD_FRAMES "Link to this definition")

Enables CAN FD support in a CAN\_RAW socket. This is disabled by default. This allows your application to send both CAN and CAN FD frames; however, you must accept both CAN and CAN FD frames when reading from the socket.

This constant is documented in the Linux documentation.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 3.6.

Added in version 3.5.

socket.CAN\_RAW\_JOIN\_FILTERS[¶](https://docs.python.org/3/library/socket.html#socket.CAN_RAW_JOIN_FILTERS "Link to this definition")

Joins the applied CAN filters such that only CAN frames that match all given CAN filters are passed to user space.

This constant is documented in the Linux documentation.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.1.

Added in version 3.9.

socket.CAN\_ISOTP[¶](https://docs.python.org/3/library/socket.html#socket.CAN_ISOTP "Link to this definition")

CAN\_ISOTP, in the CAN protocol family, is the ISO-TP (ISO 15765-2) protocol. ISO-TP constants, documented in the Linux documentation.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.25.

Added in version 3.7.

socket.CAN\_J1939[¶](https://docs.python.org/3/library/socket.html#socket.CAN_J1939 "Link to this definition")

CAN\_J1939, in the CAN protocol family, is the SAE J1939 protocol. J1939 constants, documented in the Linux documentation.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 5.4.

Added in version 3.9.

socket.AF\_DIVERT[¶](https://docs.python.org/3/library/socket.html#socket.AF_DIVERT "Link to this definition")

socket.PF\_DIVERT[¶](https://docs.python.org/3/library/socket.html#socket.PF_DIVERT "Link to this definition")

These two constants, documented in the FreeBSD divert(4) manual page, are also defined in the socket module.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: FreeBSD >= 14.0.

Added in version 3.12.

socket.AF\_PACKET[¶](https://docs.python.org/3/library/socket.html#socket.AF_PACKET "Link to this definition")

socket.PF\_PACKET[¶](https://docs.python.org/3/library/socket.html#socket.PF_PACKET "Link to this definition")

PACKET\_\*

Many constants of these forms, documented in the Linux documentation, are also defined in the socket module.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.2.

socket.ETH\_P\_ALL[¶](https://docs.python.org/3/library/socket.html#socket.ETH_P_ALL "Link to this definition")

`ETH_P_ALL` can be used in the [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
 constructor as _proto_ for the [`AF_PACKET`](https://docs.python.org/3/library/socket.html#socket.AF_PACKET "socket.AF_PACKET")
 family in order to capture every packet, regardless of protocol.

For more information, see the _[packet(7)](https://manpages.debian.org/packet(7))
_ manpage.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux.

Added in version 3.12.

socket.AF\_RDS[¶](https://docs.python.org/3/library/socket.html#socket.AF_RDS "Link to this definition")

socket.PF\_RDS[¶](https://docs.python.org/3/library/socket.html#socket.PF_RDS "Link to this definition")

socket.SOL\_RDS[¶](https://docs.python.org/3/library/socket.html#socket.SOL_RDS "Link to this definition")

RDS\_\*

Many constants of these forms, documented in the Linux documentation, are also defined in the socket module.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.30.

Added in version 3.3.

socket.SIO\_RCVALL[¶](https://docs.python.org/3/library/socket.html#socket.SIO_RCVALL "Link to this definition")

socket.SIO\_KEEPALIVE\_VALS[¶](https://docs.python.org/3/library/socket.html#socket.SIO_KEEPALIVE_VALS "Link to this definition")

socket.SIO\_LOOPBACK\_FAST\_PATH[¶](https://docs.python.org/3/library/socket.html#socket.SIO_LOOPBACK_FAST_PATH "Link to this definition")

RCVALL\_\*

Constants for Windows’ WSAIoctl(). The constants are used as arguments to the [`ioctl()`](https://docs.python.org/3/library/socket.html#socket.socket.ioctl "socket.socket.ioctl")
 method of socket objects.

Changed in version 3.6: `SIO_LOOPBACK_FAST_PATH` was added.

TIPC\_\*

TIPC related constants, matching the ones exported by the C socket API. See the TIPC documentation for more information.

socket.AF\_ALG[¶](https://docs.python.org/3/library/socket.html#socket.AF_ALG "Link to this definition")

socket.SOL\_ALG[¶](https://docs.python.org/3/library/socket.html#socket.SOL_ALG "Link to this definition")

ALG\_\*

Constants for Linux Kernel cryptography.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.38.

Added in version 3.6.

socket.AF\_VSOCK[¶](https://docs.python.org/3/library/socket.html#socket.AF_VSOCK "Link to this definition")

socket.IOCTL\_VM\_SOCKETS\_GET\_LOCAL\_CID[¶](https://docs.python.org/3/library/socket.html#socket.IOCTL_VM_SOCKETS_GET_LOCAL_CID "Link to this definition")

VMADDR\*

SO\_VM\*

Constants for Linux host/guest communication.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.8.

Added in version 3.7.

socket.AF\_LINK[¶](https://docs.python.org/3/library/socket.html#socket.AF_LINK "Link to this definition")

[Availability](https://docs.python.org/3/library/intro.html#availability)
: BSD, macOS.

Added in version 3.4.

socket.has\_ipv6[¶](https://docs.python.org/3/library/socket.html#socket.has_ipv6 "Link to this definition")

This constant contains a boolean value which indicates if IPv6 is supported on this platform.

socket.AF\_BLUETOOTH[¶](https://docs.python.org/3/library/socket.html#socket.AF_BLUETOOTH "Link to this definition")

socket.BTPROTO\_L2CAP[¶](https://docs.python.org/3/library/socket.html#socket.BTPROTO_L2CAP "Link to this definition")

socket.BTPROTO\_RFCOMM[¶](https://docs.python.org/3/library/socket.html#socket.BTPROTO_RFCOMM "Link to this definition")

socket.BTPROTO\_HCI[¶](https://docs.python.org/3/library/socket.html#socket.BTPROTO_HCI "Link to this definition")

socket.BTPROTO\_SCO[¶](https://docs.python.org/3/library/socket.html#socket.BTPROTO_SCO "Link to this definition")

Integer constants for use with Bluetooth addresses.

socket.BDADDR\_ANY[¶](https://docs.python.org/3/library/socket.html#socket.BDADDR_ANY "Link to this definition")

socket.BDADDR\_LOCAL[¶](https://docs.python.org/3/library/socket.html#socket.BDADDR_LOCAL "Link to this definition")

These are string constants containing Bluetooth addresses with special meanings. For example, [`BDADDR_ANY`](https://docs.python.org/3/library/socket.html#socket.BDADDR_ANY "socket.BDADDR_ANY")
 can be used to indicate any address when specifying the binding socket with [`BTPROTO_RFCOMM`](https://docs.python.org/3/library/socket.html#socket.BTPROTO_RFCOMM "socket.BTPROTO_RFCOMM")
.

socket.BDADDR\_BREDR[¶](https://docs.python.org/3/library/socket.html#socket.BDADDR_BREDR "Link to this definition")

socket.BDADDR\_LE\_PUBLIC[¶](https://docs.python.org/3/library/socket.html#socket.BDADDR_LE_PUBLIC "Link to this definition")

socket.BDADDR\_LE\_RANDOM[¶](https://docs.python.org/3/library/socket.html#socket.BDADDR_LE_RANDOM "Link to this definition")

These constants describe the Bluetooth address type when binding or connecting a [`BTPROTO_L2CAP`](https://docs.python.org/3/library/socket.html#socket.BTPROTO_L2CAP "socket.BTPROTO_L2CAP")
 socket.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux, FreeBSD

Added in version 3.14.

socket.SOL\_RFCOMM[¶](https://docs.python.org/3/library/socket.html#socket.SOL_RFCOMM "Link to this definition")

socket.SOL\_L2CAP[¶](https://docs.python.org/3/library/socket.html#socket.SOL_L2CAP "Link to this definition")

socket.SOL\_HCI[¶](https://docs.python.org/3/library/socket.html#socket.SOL_HCI "Link to this definition")

socket.SOL\_SCO[¶](https://docs.python.org/3/library/socket.html#socket.SOL_SCO "Link to this definition")

socket.SOL\_BLUETOOTH[¶](https://docs.python.org/3/library/socket.html#socket.SOL_BLUETOOTH "Link to this definition")

Used in the level argument to the [`setsockopt()`](https://docs.python.org/3/library/socket.html#socket.socket.setsockopt "socket.socket.setsockopt")
 and [`getsockopt()`](https://docs.python.org/3/library/socket.html#socket.socket.getsockopt "socket.socket.getsockopt")
 methods of Bluetooth socket objects.

[`SOL_BLUETOOTH`](https://docs.python.org/3/library/socket.html#socket.SOL_BLUETOOTH "socket.SOL_BLUETOOTH")
 is only available on Linux. Other constants are available if the corresponding protocol is supported.

SO\_L2CAP\_\*

socket.L2CAP\_LM[¶](https://docs.python.org/3/library/socket.html#socket.L2CAP_LM "Link to this definition")

L2CAP\_LM\_\*

SO\_RFCOMM\_\*

RFCOMM\_LM\_\*

SO\_SCO\_\*

SO\_BTH\_\*

BT\_\*

Used in the option name and value argument to the [`setsockopt()`](https://docs.python.org/3/library/socket.html#socket.socket.setsockopt "socket.socket.setsockopt")
 and [`getsockopt()`](https://docs.python.org/3/library/socket.html#socket.socket.getsockopt "socket.socket.getsockopt")
 methods of Bluetooth socket objects.

`BT_*` and [`L2CAP_LM`](https://docs.python.org/3/library/socket.html#socket.L2CAP_LM "socket.L2CAP_LM")
 are only available on Linux. `SO_BTH_*` are only available on Windows. Other constants may be available on Linux and various BSD platforms.

Added in version 3.14.

socket.HCI\_FILTER[¶](https://docs.python.org/3/library/socket.html#socket.HCI_FILTER "Link to this definition")

socket.HCI\_TIME\_STAMP[¶](https://docs.python.org/3/library/socket.html#socket.HCI_TIME_STAMP "Link to this definition")

socket.HCI\_DATA\_DIR[¶](https://docs.python.org/3/library/socket.html#socket.HCI_DATA_DIR "Link to this definition")

socket.SO\_HCI\_EVT\_FILTER[¶](https://docs.python.org/3/library/socket.html#socket.SO_HCI_EVT_FILTER "Link to this definition")

socket.SO\_HCI\_PKT\_FILTER[¶](https://docs.python.org/3/library/socket.html#socket.SO_HCI_PKT_FILTER "Link to this definition")

Option names for use with [`BTPROTO_HCI`](https://docs.python.org/3/library/socket.html#socket.BTPROTO_HCI "socket.BTPROTO_HCI")
. Availability and format of the option values depend on platform.

Changed in version 3.14: Added `SO_HCI_EVT_FILTER` and `SO_HCI_PKT_FILTER` on NetBSD and DragonFly BSD. Added `HCI_DATA_DIR` on FreeBSD, NetBSD and DragonFly BSD.

socket.HCI\_DEV\_NONE[¶](https://docs.python.org/3/library/socket.html#socket.HCI_DEV_NONE "Link to this definition")

The `device_id` value used to create an HCI socket that isn’t specific to a single Bluetooth adapter.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux

Added in version 3.14.

socket.HCI\_CHANNEL\_RAW[¶](https://docs.python.org/3/library/socket.html#socket.HCI_CHANNEL_RAW "Link to this definition")

socket.HCI\_CHANNEL\_USER[¶](https://docs.python.org/3/library/socket.html#socket.HCI_CHANNEL_USER "Link to this definition")

socket.HCI\_CHANNEL\_MONITOR[¶](https://docs.python.org/3/library/socket.html#socket.HCI_CHANNEL_MONITOR "Link to this definition")

socket.HCI\_CHANNEL\_CONTROL[¶](https://docs.python.org/3/library/socket.html#socket.HCI_CHANNEL_CONTROL "Link to this definition")

socket.HCI\_CHANNEL\_LOGGING[¶](https://docs.python.org/3/library/socket.html#socket.HCI_CHANNEL_LOGGING "Link to this definition")

Possible values for `channel` field in the [`BTPROTO_HCI`](https://docs.python.org/3/library/socket.html#socket.BTPROTO_HCI "socket.BTPROTO_HCI")
 address.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux

Added in version 3.14.

socket.AF\_QIPCRTR[¶](https://docs.python.org/3/library/socket.html#socket.AF_QIPCRTR "Link to this definition")

Constant for Qualcomm’s IPC router protocol, used to communicate with service providing remote processors.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.7.

socket.SCM\_CREDS2[¶](https://docs.python.org/3/library/socket.html#socket.SCM_CREDS2 "Link to this definition")

socket.LOCAL\_CREDS[¶](https://docs.python.org/3/library/socket.html#socket.LOCAL_CREDS "Link to this definition")

socket.LOCAL\_CREDS\_PERSISTENT[¶](https://docs.python.org/3/library/socket.html#socket.LOCAL_CREDS_PERSISTENT "Link to this definition")

LOCAL\_CREDS and LOCAL\_CREDS\_PERSISTENT can be used with SOCK\_DGRAM, SOCK\_STREAM sockets, equivalent to Linux/DragonFlyBSD SO\_PASSCRED, while LOCAL\_CREDS sends the credentials at first read, LOCAL\_CREDS\_PERSISTENT sends for each read, SCM\_CREDS2 must be then used for the latter for the message type.

Added in version 3.11.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: FreeBSD.

socket.SO\_INCOMING\_CPU[¶](https://docs.python.org/3/library/socket.html#socket.SO_INCOMING_CPU "Link to this definition")

Constant to optimize CPU locality, to be used in conjunction with `SO_REUSEPORT`.

Added in version 3.11.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 3.9

socket.SO\_REUSEPORT\_LB[¶](https://docs.python.org/3/library/socket.html#socket.SO_REUSEPORT_LB "Link to this definition")

> Constant to enable duplicate address and port bindings with load balancing.

Added in version 3.14.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: FreeBSD >= 12.0

socket.AF\_HYPERV[¶](https://docs.python.org/3/library/socket.html#socket.AF_HYPERV "Link to this definition")

socket.HV\_PROTOCOL\_RAW[¶](https://docs.python.org/3/library/socket.html#socket.HV_PROTOCOL_RAW "Link to this definition")

socket.HVSOCKET\_CONNECT\_TIMEOUT[¶](https://docs.python.org/3/library/socket.html#socket.HVSOCKET_CONNECT_TIMEOUT "Link to this definition")

socket.HVSOCKET\_CONNECT\_TIMEOUT\_MAX[¶](https://docs.python.org/3/library/socket.html#socket.HVSOCKET_CONNECT_TIMEOUT_MAX "Link to this definition")

socket.HVSOCKET\_CONNECTED\_SUSPEND[¶](https://docs.python.org/3/library/socket.html#socket.HVSOCKET_CONNECTED_SUSPEND "Link to this definition")

socket.HVSOCKET\_ADDRESS\_FLAG\_PASSTHRU[¶](https://docs.python.org/3/library/socket.html#socket.HVSOCKET_ADDRESS_FLAG_PASSTHRU "Link to this definition")

socket.HV\_GUID\_ZERO[¶](https://docs.python.org/3/library/socket.html#socket.HV_GUID_ZERO "Link to this definition")

socket.HV\_GUID\_WILDCARD[¶](https://docs.python.org/3/library/socket.html#socket.HV_GUID_WILDCARD "Link to this definition")

socket.HV\_GUID\_BROADCAST[¶](https://docs.python.org/3/library/socket.html#socket.HV_GUID_BROADCAST "Link to this definition")

socket.HV\_GUID\_CHILDREN[¶](https://docs.python.org/3/library/socket.html#socket.HV_GUID_CHILDREN "Link to this definition")

socket.HV\_GUID\_LOOPBACK[¶](https://docs.python.org/3/library/socket.html#socket.HV_GUID_LOOPBACK "Link to this definition")

socket.HV\_GUID\_PARENT[¶](https://docs.python.org/3/library/socket.html#socket.HV_GUID_PARENT "Link to this definition")

Constants for Windows Hyper-V sockets for host/guest communications.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

Added in version 3.12.

socket.ETHERTYPE\_ARP[¶](https://docs.python.org/3/library/socket.html#socket.ETHERTYPE_ARP "Link to this definition")

socket.ETHERTYPE\_IP[¶](https://docs.python.org/3/library/socket.html#socket.ETHERTYPE_IP "Link to this definition")

socket.ETHERTYPE\_IPV6[¶](https://docs.python.org/3/library/socket.html#socket.ETHERTYPE_IPV6 "Link to this definition")

socket.ETHERTYPE\_VLAN[¶](https://docs.python.org/3/library/socket.html#socket.ETHERTYPE_VLAN "Link to this definition")

[IEEE 802.3 protocol number](https://www.iana.org/assignments/ieee-802-numbers/ieee-802-numbers.txt)
. constants.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux, FreeBSD, macOS.

Added in version 3.12.

socket.SHUT\_RD[¶](https://docs.python.org/3/library/socket.html#socket.SHUT_RD "Link to this definition")

socket.SHUT\_WR[¶](https://docs.python.org/3/library/socket.html#socket.SHUT_WR "Link to this definition")

socket.SHUT\_RDWR[¶](https://docs.python.org/3/library/socket.html#socket.SHUT_RDWR "Link to this definition")

These constants are used by the [`shutdown()`](https://docs.python.org/3/library/socket.html#socket.socket.shutdown "socket.socket.shutdown")
 method of socket objects.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

### Functions[¶](https://docs.python.org/3/library/socket.html#functions "Link to this heading")

#### Creating sockets[¶](https://docs.python.org/3/library/socket.html#creating-sockets "Link to this heading")

The following functions all create [socket objects](https://docs.python.org/3/library/socket.html#socket-objects)
.

The [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
 class constructor creates a new socket directly; see [Socket Objects](https://docs.python.org/3/library/socket.html#socket-objects)
 for its parameters and full description.

socket.socketpair(\[_family_\[, _type_\[, _proto_\]\]\])[¶](https://docs.python.org/3/library/socket.html#socket.socketpair "Link to this definition")

Build a pair of connected socket objects using the given address family, socket type, and protocol number. Address family, socket type, and protocol number are as for the [`socket()`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
 function. The default family is [`AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX")
 if defined on the platform; otherwise, the default is [`AF_INET`](https://docs.python.org/3/library/socket.html#socket.AF_INET "socket.AF_INET")
.

The newly created sockets are [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance)
.

Changed in version 3.2: The returned socket objects now support the whole socket API, rather than a subset.

Changed in version 3.4: The returned sockets are now non-inheritable.

Changed in version 3.5: Windows support added.

socket.create\_connection(_address_, _timeout\=GLOBAL\_DEFAULT_, _source\_address\=None_, _\*_, _all\_errors\=False_)[¶](https://docs.python.org/3/library/socket.html#socket.create_connection "Link to this definition")

Connect to a TCP service listening on the internet _address_ (a 2-tuple `(host, port)`), and return the socket object. This is a higher-level function than [`socket.connect()`](https://docs.python.org/3/library/socket.html#socket.socket.connect "socket.socket.connect")
: if _host_ is a non-numeric hostname, it will try to resolve it for both [`AF_INET`](https://docs.python.org/3/library/socket.html#socket.AF_INET "socket.AF_INET")
 and [`AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6")
, and then try to connect to all possible addresses in turn until a connection succeeds. This makes it easy to write clients that are compatible to both IPv4 and IPv6.

Passing the optional _timeout_ parameter will set the timeout on the socket instance before attempting to connect. If no _timeout_ is supplied, the global default timeout setting returned by [`getdefaulttimeout()`](https://docs.python.org/3/library/socket.html#socket.getdefaulttimeout "socket.getdefaulttimeout")
 is used.

If supplied, _source\_address_ must be a 2-tuple `(host, port)` for the socket to bind to as its source address before connecting. If host or port are ‘’ or 0 respectively the OS default behavior will be used.

When a connection cannot be created, an exception is raised. By default, it is the exception from the last address in the list. If _all\_errors_ is `True`, it is an [`ExceptionGroup`](https://docs.python.org/3/builtins/exceptions.html#ExceptionGroup "ExceptionGroup")
 containing the errors of all attempts.

Changed in version 3.2: _source\_address_ was added.

Changed in version 3.11: _all\_errors_ was added.

socket.create\_server(_address_, _\*_, _family\=AF\_INET_, _backlog\=None_, _reuse\_port\=False_, _dualstack\_ipv6\=False_)[¶](https://docs.python.org/3/library/socket.html#socket.create_server "Link to this definition")

Convenience function which creates a TCP socket bound to _address_ (a 2-tuple `(host, port)`) and returns the socket object.

_family_ should be either [`AF_INET`](https://docs.python.org/3/library/socket.html#socket.AF_INET "socket.AF_INET")
 or [`AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6")
. _backlog_ is the queue size passed to [`socket.listen()`](https://docs.python.org/3/library/socket.html#socket.socket.listen "socket.socket.listen")
; if not specified , a default reasonable value is chosen. _reuse\_port_ dictates whether to set the `SO_REUSEPORT` socket option.

If _dualstack\_ipv6_ is true, _family_ is [`AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6")
 and the platform supports it the socket will be able to accept both IPv4 and IPv6 connections, else it will raise [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
. Most POSIX platforms and Windows are supposed to support this functionality. When this functionality is enabled the address returned by [`socket.getpeername()`](https://docs.python.org/3/library/socket.html#socket.socket.getpeername "socket.socket.getpeername")
 when an IPv4 connection occurs will be an IPv6 address represented as an IPv4-mapped IPv6 address. If _dualstack\_ipv6_ is false it will explicitly disable this functionality on platforms that enable it by default (e.g. Linux). This parameter can be used in conjunction with [`has_dualstack_ipv6()`](https://docs.python.org/3/library/socket.html#socket.has_dualstack_ipv6 "socket.has_dualstack_ipv6")
:

Copy

import socket

addr \= ("", 8080)  \# all interfaces, port 8080
if socket.has\_dualstack\_ipv6():
    s \= socket.create\_server(addr, family\=socket.AF\_INET6, dualstack\_ipv6\=True)
else:
    s \= socket.create\_server(addr)

Note

On POSIX platforms the `SO_REUSEADDR` socket option is set in order to immediately reuse previous sockets which were bound on the same _address_ and remained in TIME\_WAIT state.

Added in version 3.8.

socket.has\_dualstack\_ipv6()[¶](https://docs.python.org/3/library/socket.html#socket.has_dualstack_ipv6 "Link to this definition")

Return `True` if the platform supports creating a TCP socket which can handle both IPv4 and IPv6 connections.

Added in version 3.8.

socket.fromfd(_fd_, _family_, _type_, _proto\=0_)[¶](https://docs.python.org/3/library/socket.html#socket.fromfd "Link to this definition")

Duplicate the file descriptor _fd_ (an integer as returned by a file object’s [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno")
 method) and build a socket object from the result. Address family, socket type and protocol number are as for the [`socket()`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
 function. The file descriptor should refer to a socket, but this is not checked — subsequent operations on the object may fail if the file descriptor is invalid. This function is rarely needed, but can be used to get or set socket options on a socket passed to a program as standard input or output (such as a server started by the Unix inet daemon). The socket is assumed to be in blocking mode.

The newly created socket is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance)
.

Changed in version 3.4: The returned socket is now non-inheritable.

socket.fromshare(_data_)[¶](https://docs.python.org/3/library/socket.html#socket.fromshare "Link to this definition")

Instantiate a socket from data obtained from the [`socket.share()`](https://docs.python.org/3/library/socket.html#socket.socket.share "socket.socket.share")
 method. The socket is assumed to be in blocking mode.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

Added in version 3.3.

#### Other functions[¶](https://docs.python.org/3/library/socket.html#other-functions "Link to this heading")

The `socket` module also offers various network-related services:

socket.close(_fd_)[¶](https://docs.python.org/3/library/socket.html#socket.close "Link to this definition")

Close a socket file descriptor. This is like [`os.close()`](https://docs.python.org/3/library/os.html#os.close "os.close")
, but for sockets. On some platforms (most notably Windows) `os.close()` does not work for socket file descriptors.

Added in version 3.7.

socket.getaddrinfo(_host_, _port_, _family\=AF\_UNSPEC_, _type\=0_, _proto\=0_, _flags\=0_)[¶](https://docs.python.org/3/library/socket.html#socket.getaddrinfo "Link to this definition")

This function wraps the C function `getaddrinfo` of the underlying system.

Translate the _host_/_port_ argument into a sequence of 5-tuples that contain all the necessary arguments for creating a socket connected to that service. _host_ is a domain name, a string representation of an IPv4/v6 address or `None`. _port_ is a string service name such as `'http'`, a numeric port number or `None`. By passing `None` as the value of _host_ and _port_, you can pass `NULL` to the underlying C API.

The _family_, _type_ and _proto_ arguments can be optionally specified in order to provide options and limit the list of addresses returned. Pass their default values ([`AF_UNSPEC`](https://docs.python.org/3/library/socket.html#socket.AF_UNSPEC "socket.AF_UNSPEC")
, 0, and 0, respectively) to not limit the results. See the note below for details.

The _flags_ argument can be one or several of the `AI_*` constants, and will influence how results are computed and returned. For example, `AI_NUMERICHOST` will disable domain name resolution and will raise an error if _host_ is a domain name.

The function returns a list of 5-tuples with the following structure:

`(family, type, proto, canonname, sockaddr)`

In these tuples, _family_, _type_, _proto_ are all integers and are meant to be passed to the [`socket()`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
 function. _canonname_ will be a string representing the canonical name of the _host_ if `AI_CANONNAME` is part of the _flags_ argument; else _canonname_ will be empty. _sockaddr_ is a tuple describing a socket address, whose format depends on the returned _family_ and flags Python was compiled with, and is meant to be passed to the [`socket.connect()`](https://docs.python.org/3/library/socket.html#socket.socket.connect "socket.socket.connect")
 method.

_sockaddr_ can be one of the following:

*   a `(address, port)` 2-tuple for [`AF_INET`](https://docs.python.org/3/library/socket.html#socket.AF_INET "socket.AF_INET")
    
*   a `(address, port, flowinfo, scope_id)` 4-tuple for [`AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6")
     if Python was compiled with `--enable-ipv6` (the default)
    
*   a 2-tuple containing raw data for [`AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6")
     if Python was compiled with `--disable-ipv6`
    

Note

If you intend to use results from `getaddrinfo()` to create a socket (rather than, for example, retrieve _canonname_), consider limiting the results by _type_ (e.g. [`SOCK_STREAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM "socket.SOCK_STREAM")
 or [`SOCK_DGRAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_DGRAM "socket.SOCK_DGRAM")
) and/or _proto_ (e.g. `IPPROTO_TCP` or `IPPROTO_UDP`) that your application can handle.

The behavior with default values of _family_, _type_, _proto_ and _flags_ is system-specific.

Many systems (for example, most Linux configurations) will return a sorted list of all matching addresses. These addresses should generally be tried in order until a connection succeeds (possibly tried in parallel, for example, using a [Happy Eyeballs](https://en.wikipedia.org/wiki/Happy_Eyeballs)
 algorithm). In these cases, limiting the _type_ and/or _proto_ can help eliminate unsuccessful or unusable connection attempts.

Some systems will, however, only return a single address. (For example, this was reported on Solaris and AIX configurations.) On these systems, limiting the _type_ and/or _proto_ helps ensure that this address is usable.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `socket.getaddrinfo` with arguments `host`, `port`, `family`, `type`, `protocol`.

The following example fetches address information for a hypothetical TCP connection to `example.org` on port 80 (results may differ on your system if IPv6 isn’t enabled):

Copy

\>>> socket.getaddrinfo("example.org", 80, proto\=socket.IPPROTO\_TCP)
\[(socket.AF\_INET6, socket.SOCK\_STREAM,\
 6, '', ('2606:2800:220:1:248:1893:25c8:1946', 80, 0, 0)),\
 (socket.AF\_INET, socket.SOCK\_STREAM,\
 6, '', ('93.184.216.34', 80))\]

Changed in version 3.2: parameters can now be passed using keyword arguments.

Changed in version 3.7: for IPv6 multicast addresses, string representing an address will not contain `%scope_id` part.

Changed in version 3.15.2 (unreleased): Null characters are now rejected in the _host_ and _port_ parameters.

socket.getfqdn(\[_name_\])[¶](https://docs.python.org/3/library/socket.html#socket.getfqdn "Link to this definition")

Return a fully qualified domain name for _name_. If _name_ is omitted or empty, it is interpreted as the local host. To find the fully qualified name, the hostname returned by [`gethostbyaddr()`](https://docs.python.org/3/library/socket.html#socket.gethostbyaddr "socket.gethostbyaddr")
 is checked, followed by aliases for the host, if available. The first name which includes a period is selected. In case no fully qualified domain name is available and _name_ was provided, it is returned unchanged. If _name_ was empty or equal to `'0.0.0.0'`, the hostname from [`gethostname()`](https://docs.python.org/3/library/socket.html#socket.gethostname "socket.gethostname")
 is returned.

socket.gethostbyname(_hostname_)[¶](https://docs.python.org/3/library/socket.html#socket.gethostbyname "Link to this definition")

Translate a host name to IPv4 address format. The IPv4 address is returned as a string, such as `'100.50.200.5'`. If the host name is an IPv4 address itself it is returned unchanged. See [`gethostbyname_ex()`](https://docs.python.org/3/library/socket.html#socket.gethostbyname_ex "socket.gethostbyname_ex")
 for a more complete interface. `gethostbyname()` does not support IPv6 name resolution, and [`getaddrinfo()`](https://docs.python.org/3/library/socket.html#socket.getaddrinfo "socket.getaddrinfo")
 should be used instead for IPv4/v6 dual stack support.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `socket.gethostbyname` with argument `hostname`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

socket.gethostbyname\_ex(_hostname_)[¶](https://docs.python.org/3/library/socket.html#socket.gethostbyname_ex "Link to this definition")

Translate a host name to IPv4 address format, extended interface. Return a 3-tuple `(hostname, aliaslist, ipaddrlist)` where _hostname_ is the host’s primary host name, _aliaslist_ is a (possibly empty) list of alternative host names for the same address, and _ipaddrlist_ is a list of IPv4 addresses for the same interface on the same host (often but not always a single address). `gethostbyname_ex()` does not support IPv6 name resolution, and [`getaddrinfo()`](https://docs.python.org/3/library/socket.html#socket.getaddrinfo "socket.getaddrinfo")
 should be used instead for IPv4/v6 dual stack support.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `socket.gethostbyname` with argument `hostname`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

socket.gethostname()[¶](https://docs.python.org/3/library/socket.html#socket.gethostname "Link to this definition")

Return a string containing the hostname of the machine where the Python interpreter is currently executing.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `socket.gethostname` with no arguments.

Note: `gethostname()` doesn’t always return the fully qualified domain name; use [`getfqdn()`](https://docs.python.org/3/library/socket.html#socket.getfqdn "socket.getfqdn")
 for that.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

socket.gethostbyaddr(_ip\_address_)[¶](https://docs.python.org/3/library/socket.html#socket.gethostbyaddr "Link to this definition")

Return a 3-tuple `(hostname, aliaslist, ipaddrlist)` where _hostname_ is the primary host name responding to the given _ip\_address_, _aliaslist_ is a (possibly empty) list of alternative host names for the same address, and _ipaddrlist_ is a list of IPv4/v6 addresses for the same interface on the same host (most likely containing only a single address). To find the fully qualified domain name, use the function [`getfqdn()`](https://docs.python.org/3/library/socket.html#socket.getfqdn "socket.getfqdn")
. `gethostbyaddr()` supports both IPv4 and IPv6.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `socket.gethostbyaddr` with argument `ip_address`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

socket.getnameinfo(_sockaddr_, _flags_)[¶](https://docs.python.org/3/library/socket.html#socket.getnameinfo "Link to this definition")

Translate a socket address _sockaddr_ into a 2-tuple `(host, port)`. Depending on the settings of _flags_, the result can contain a fully qualified domain name or numeric address representation in _host_. Similarly, _port_ can contain a string port name or a numeric port number.

For IPv6 addresses, `%scope_id` is appended to the host part if _sockaddr_ contains meaningful _scope\_id_. Usually this happens for multicast addresses.

For more information about _flags_ you can consult _[getnameinfo(3)](https://manpages.debian.org/getnameinfo(3))
_.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `socket.getnameinfo` with argument `sockaddr`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

socket.getprotobyname(_protocolname_)[¶](https://docs.python.org/3/library/socket.html#socket.getprotobyname "Link to this definition")

Translate an internet protocol name (for example, `'icmp'`) to a constant suitable for passing as the (optional) third argument to the [`socket()`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
 function. This is usually only needed for sockets opened in “raw” mode ([`SOCK_RAW`](https://docs.python.org/3/library/socket.html#socket.SOCK_RAW "socket.SOCK_RAW")
); for the normal socket modes, the correct protocol is chosen automatically if the protocol is omitted or zero.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

socket.getservbyname(_servicename_\[, _protocolname_\])[¶](https://docs.python.org/3/library/socket.html#socket.getservbyname "Link to this definition")

Translate an internet service name and protocol name to a port number for that service. The optional protocol name, if given, should be `'tcp'` or `'udp'`, otherwise any protocol will match.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `socket.getservbyname` with arguments `servicename`, `protocolname`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

socket.getservbyport(_port_\[, _protocolname_\])[¶](https://docs.python.org/3/library/socket.html#socket.getservbyport "Link to this definition")

Translate an internet port number and protocol name to a service name for that service. The optional protocol name, if given, should be `'tcp'` or `'udp'`, otherwise any protocol will match.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `socket.getservbyport` with arguments `port`, `protocolname`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

socket.ntohl(_x_)[¶](https://docs.python.org/3/library/socket.html#socket.ntohl "Link to this definition")

Convert 32-bit positive integers from network to host byte order. On machines where the host byte order is the same as network byte order, this is a no-op; otherwise, it performs a 4-byte swap operation.

socket.ntohs(_x_)[¶](https://docs.python.org/3/library/socket.html#socket.ntohs "Link to this definition")

Convert 16-bit positive integers from network to host byte order. On machines where the host byte order is the same as network byte order, this is a no-op; otherwise, it performs a 2-byte swap operation.

Changed in version 3.10: Raises [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
 if _x_ does not fit in a 16-bit unsigned integer.

socket.htonl(_x_)[¶](https://docs.python.org/3/library/socket.html#socket.htonl "Link to this definition")

Convert 32-bit positive integers from host to network byte order. On machines where the host byte order is the same as network byte order, this is a no-op; otherwise, it performs a 4-byte swap operation.

socket.htons(_x_)[¶](https://docs.python.org/3/library/socket.html#socket.htons "Link to this definition")

Convert 16-bit positive integers from host to network byte order. On machines where the host byte order is the same as network byte order, this is a no-op; otherwise, it performs a 2-byte swap operation.

Changed in version 3.10: Raises [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
 if _x_ does not fit in a 16-bit unsigned integer.

socket.inet\_aton(_ip\_string_)[¶](https://docs.python.org/3/library/socket.html#socket.inet_aton "Link to this definition")

Convert an IPv4 address from dotted-quad string format (for example, ‘123.45.67.89’) to 32-bit packed binary format, as a bytes object four characters in length. This is useful when conversing with a program that uses the standard C library and needs objects of type `in_addr`, which is the C type for the 32-bit packed binary this function returns.

`inet_aton()` also accepts strings with less than three dots; see the Unix manual page _[inet(3)](https://manpages.debian.org/inet(3))
_ for details.

If the IPv4 address string passed to this function is invalid, [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 will be raised. Note that exactly what is valid depends on the underlying C implementation of `inet_aton()`.

`inet_aton()` does not support IPv6, and [`inet_pton()`](https://docs.python.org/3/library/socket.html#socket.inet_pton "socket.inet_pton")
 should be used instead for IPv4/v6 dual stack support.

socket.inet\_ntoa(_packed\_ip_)[¶](https://docs.python.org/3/library/socket.html#socket.inet_ntoa "Link to this definition")

Convert a 32-bit packed IPv4 address (a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 four bytes in length) to its standard dotted-quad string representation (for example, ‘123.45.67.89’). This is useful when conversing with a program that uses the standard C library and needs objects of type `in_addr`, which is the C type for the 32-bit packed binary data this function takes as an argument.

If the byte sequence passed to this function is not exactly 4 bytes in length, [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 will be raised. `inet_ntoa()` does not support IPv6, and [`inet_ntop()`](https://docs.python.org/3/library/socket.html#socket.inet_ntop "socket.inet_ntop")
 should be used instead for IPv4/v6 dual stack support.

Changed in version 3.5: Writable [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 is now accepted.

socket.inet\_pton(_address\_family_, _ip\_string_)[¶](https://docs.python.org/3/library/socket.html#socket.inet_pton "Link to this definition")

Convert an IP address from its family-specific string format to a packed, binary format. `inet_pton()` is useful when a library or network protocol calls for an object of type `in_addr` (similar to [`inet_aton()`](https://docs.python.org/3/library/socket.html#socket.inet_aton "socket.inet_aton")
) or `in6_addr`.

Supported values for _address\_family_ are currently [`AF_INET`](https://docs.python.org/3/library/socket.html#socket.AF_INET "socket.AF_INET")
 and [`AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6")
. If the IP address string _ip\_string_ is invalid, [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 will be raised. Note that exactly what is valid depends on both the value of _address\_family_ and the underlying implementation of `inet_pton()`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows.

Changed in version 3.4: Windows support added

socket.inet\_ntop(_address\_family_, _packed\_ip_)[¶](https://docs.python.org/3/library/socket.html#socket.inet_ntop "Link to this definition")

Convert a packed IP address (a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 of some number of bytes) to its standard, family-specific string representation (for example, `'7.10.0.5'` or `'5aef:2b::8'`). `inet_ntop()` is useful when a library or network protocol returns an object of type `in_addr` (similar to [`inet_ntoa()`](https://docs.python.org/3/library/socket.html#socket.inet_ntoa "socket.inet_ntoa")
) or `in6_addr`.

Supported values for _address\_family_ are currently [`AF_INET`](https://docs.python.org/3/library/socket.html#socket.AF_INET "socket.AF_INET")
 and [`AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6")
. If the bytes object _packed\_ip_ is not the correct length for the specified address family, [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 will be raised. [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised for errors from the call to `inet_ntop()`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows.

Changed in version 3.4: Windows support added

Changed in version 3.5: Writable [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 is now accepted.

socket.CMSG\_LEN(_length_)[¶](https://docs.python.org/3/library/socket.html#socket.CMSG_LEN "Link to this definition")

Return the total length, without trailing padding, of an ancillary data item with associated data of the given _length_. This value can often be used as the buffer size for [`recvmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.recvmsg "socket.socket.recvmsg")
 to receive a single item of ancillary data, but [**RFC 3542**](https://datatracker.ietf.org/doc/html/rfc3542.html)
 requires portable applications to use [`CMSG_SPACE()`](https://docs.python.org/3/library/socket.html#socket.CMSG_SPACE "socket.CMSG_SPACE")
 and thus include space for padding, even when the item will be the last in the buffer. Raises [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
 if _length_ is outside the permissible range of values.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Most Unix platforms.

Added in version 3.3.

socket.CMSG\_SPACE(_length_)[¶](https://docs.python.org/3/library/socket.html#socket.CMSG_SPACE "Link to this definition")

Return the buffer size needed for [`recvmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.recvmsg "socket.socket.recvmsg")
 to receive an ancillary data item with associated data of the given _length_, along with any trailing padding. The buffer space needed to receive multiple items is the sum of the `CMSG_SPACE()` values for their associated data lengths. Raises [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
 if _length_ is outside the permissible range of values.

Note that some systems might support ancillary data without providing this function. Also note that setting the buffer size using the results of this function may not precisely limit the amount of ancillary data that can be received, since additional data may be able to fit into the padding area.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

most Unix platforms.

Added in version 3.3.

socket.getdefaulttimeout()[¶](https://docs.python.org/3/library/socket.html#socket.getdefaulttimeout "Link to this definition")

Return the default timeout in seconds (float) for new socket objects. A value of `None` indicates that new socket objects have no timeout. When the socket module is first imported, the default is `None`.

socket.setdefaulttimeout(_timeout_)[¶](https://docs.python.org/3/library/socket.html#socket.setdefaulttimeout "Link to this definition")

Set the default timeout in seconds (real number) for new socket objects. When the socket module is first imported, the default is `None`. See [`settimeout()`](https://docs.python.org/3/library/socket.html#socket.socket.settimeout "socket.socket.settimeout")
 for possible values and their respective meanings.

Changed in version 3.15: Accepts any real number, not only integer or float.

socket.sethostname(_name_)[¶](https://docs.python.org/3/library/socket.html#socket.sethostname "Link to this definition")

Set the machine’s hostname to _name_. This will raise an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 if you don’t have enough rights.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `socket.sethostname` with argument `name`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not Android.

Added in version 3.3.

socket.if\_nameindex()[¶](https://docs.python.org/3/library/socket.html#socket.if_nameindex "Link to this definition")

Return a list of network interface information (index int, name string) tuples. [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 if the system call fails.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows, not WASI.

Added in version 3.3.

Changed in version 3.8: Windows support was added.

Note

On Windows network interfaces have different names in different contexts (all names are examples):

*   UUID: `{FB605B73-AAC2-49A6-9A2F-25416AEA0573}`
    
*   name: `ethernet_32770`
    
*   friendly name: `vEthernet (nat)`
    
*   description: `Hyper-V Virtual Ethernet Adapter`
    

This function returns names of the second form from the list, `ethernet_32770` in this example case.

socket.if\_nametoindex(_if\_name_)[¶](https://docs.python.org/3/library/socket.html#socket.if_nametoindex "Link to this definition")

Return a network interface index number corresponding to an interface name. [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 if no interface with the given name exists.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows, not WASI.

Added in version 3.3.

Changed in version 3.8: Windows support was added.

See also

“Interface name” is a name as documented in [`if_nameindex()`](https://docs.python.org/3/library/socket.html#socket.if_nameindex "socket.if_nameindex")
.

socket.if\_indextoname(_if\_index_)[¶](https://docs.python.org/3/library/socket.html#socket.if_indextoname "Link to this definition")

Return a network interface name corresponding to an interface index number. [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 if no interface with the given index exists.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows, not WASI.

Added in version 3.3.

Changed in version 3.8: Windows support was added.

See also

“Interface name” is a name as documented in [`if_nameindex()`](https://docs.python.org/3/library/socket.html#socket.if_nameindex "socket.if_nameindex")
.

socket.send\_fds(_sock_, _buffers_, _fds_\[, _flags_\[, _address_\]\])[¶](https://docs.python.org/3/library/socket.html#socket.send_fds "Link to this definition")

Send the list of file descriptors _fds_ over an [`AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX")
 socket _sock_. The _fds_ parameter is a sequence of file descriptors. Consult [`sendmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.sendmsg "socket.socket.sendmsg")
 for the documentation of these parameters.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Unix platforms supporting [`sendmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.sendmsg "socket.socket.sendmsg")
 and `SCM_RIGHTS` mechanism.

Added in version 3.9.

socket.recv\_fds(_sock_, _bufsize_, _maxfds_\[, _flags_\])[¶](https://docs.python.org/3/library/socket.html#socket.recv_fds "Link to this definition")

Receive up to _maxfds_ file descriptors from an [`AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX")
 socket _sock_. Return `(msg, list(fds), flags, addr)`. Consult [`recvmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.recvmsg "socket.socket.recvmsg")
 for the documentation of these parameters.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Unix platforms supporting [`recvmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.recvmsg "socket.socket.recvmsg")
 and `SCM_RIGHTS` mechanism.

Added in version 3.9.

Note

Any truncated integers at the end of the list of file descriptors.

Socket Objects[¶](https://docs.python.org/3/library/socket.html#socket-objects "Link to this heading")

-------------------------------------------------------------------------------------------------------

class socket.socket(_family\=AF\_INET_, _type\=SOCK\_STREAM_, _proto\=0_, _fileno\=None_)[¶](https://docs.python.org/3/library/socket.html#socket.socket "Link to this definition")

Create a new socket using the given address family, socket type and protocol number. The address family should be [`AF_INET`](https://docs.python.org/3/library/socket.html#socket.AF_INET "socket.AF_INET")
 (the default), [`AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6")
, [`AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX")
, [`AF_CAN`](https://docs.python.org/3/library/socket.html#socket.AF_CAN "socket.AF_CAN")
, [`AF_PACKET`](https://docs.python.org/3/library/socket.html#socket.AF_PACKET "socket.AF_PACKET")
, or [`AF_RDS`](https://docs.python.org/3/library/socket.html#socket.AF_RDS "socket.AF_RDS")
. The socket type should be [`SOCK_STREAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM "socket.SOCK_STREAM")
 (the default), [`SOCK_DGRAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_DGRAM "socket.SOCK_DGRAM")
, [`SOCK_RAW`](https://docs.python.org/3/library/socket.html#socket.SOCK_RAW "socket.SOCK_RAW")
 or perhaps one of the other `SOCK_` constants. The protocol number is usually zero and may be omitted or in the case where the address family is `AF_CAN` the protocol should be one of `CAN_RAW`, [`CAN_BCM`](https://docs.python.org/3/library/socket.html#socket.CAN_BCM "socket.CAN_BCM")
, [`CAN_ISOTP`](https://docs.python.org/3/library/socket.html#socket.CAN_ISOTP "socket.CAN_ISOTP")
 or [`CAN_J1939`](https://docs.python.org/3/library/socket.html#socket.CAN_J1939 "socket.CAN_J1939")
.

If _fileno_ is specified, the values for _family_, _type_, and _proto_ are auto-detected from the specified file descriptor. Auto-detection can be overruled by calling the function with explicit _family_, _type_, or _proto_ arguments. This only affects how Python represents e.g. the return value of [`socket.getpeername()`](https://docs.python.org/3/library/socket.html#socket.socket.getpeername "socket.socket.getpeername")
 but not the actual OS resource. Unlike [`socket.fromfd()`](https://docs.python.org/3/library/socket.html#socket.fromfd "socket.fromfd")
, _fileno_ will return the same socket and not a duplicate. This may help close a detached socket using [`close()`](https://docs.python.org/3/library/socket.html#socket.socket.close "socket.socket.close")
.

The newly created socket is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance)
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `socket.__new__` with arguments `self`, `family`, `type`, `protocol`.

Changed in version 3.3: The AF\_CAN family was added. The AF\_RDS family was added.

Changed in version 3.4: The CAN\_BCM protocol was added.

Changed in version 3.4: The returned socket is now non-inheritable.

Changed in version 3.7: The CAN\_ISOTP protocol was added.

Changed in version 3.7: When [`SOCK_NONBLOCK`](https://docs.python.org/3/library/socket.html#socket.SOCK_NONBLOCK "socket.SOCK_NONBLOCK")
 or [`SOCK_CLOEXEC`](https://docs.python.org/3/library/socket.html#socket.SOCK_CLOEXEC "socket.SOCK_CLOEXEC")
 bit flags are applied to _type_ they are cleared, and [`socket.type`](https://docs.python.org/3/library/socket.html#socket.socket.type "socket.socket.type")
 will not reflect them. They are still passed to the underlying system `socket()` call. Therefore,

Copy

sock \= socket.socket(
    socket.AF\_INET,
    socket.SOCK\_STREAM | socket.SOCK\_NONBLOCK)

will still create a non-blocking socket on OSes that support `SOCK_NONBLOCK`, but `sock.type` will be set to `socket.SOCK_STREAM`.

Changed in version 3.9: The CAN\_J1939 protocol was added.

Changed in version 3.10: The IPPROTO\_MPTCP protocol was added.

Socket objects have the following methods. Except for [`makefile()`](https://docs.python.org/3/library/socket.html#socket.socket.makefile "socket.socket.makefile")
, these correspond to Unix system calls applicable to sockets.

Changed in version 3.2: Support for the [context manager](https://docs.python.org/3/glossary.html#term-context-manager)
 protocol was added. Exiting the context manager is equivalent to calling [`close()`](https://docs.python.org/3/library/socket.html#socket.socket.close "socket.socket.close")
.

accept()[¶](https://docs.python.org/3/library/socket.html#socket.socket.accept "Link to this definition")

Accept a connection. The socket must be bound to an address and listening for connections. The return value is a pair `(conn, address)` where _conn_ is a _new_ socket object usable to send and receive data on the connection, and _address_ is the address bound to the socket on the other end of the connection.

The newly created socket is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance)
.

Changed in version 3.4: The socket is now non-inheritable.

Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the method now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/builtins/exceptions.html#InterruptedError "InterruptedError")
 exception (see [**PEP 475**](https://peps.python.org/pep-0475/)
 for the rationale).

bind(_address_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.bind "Link to this definition")

Bind the socket to _address_. The socket must not already be bound. The format of _address_ depends on the address family — see [Socket families](https://docs.python.org/3/library/socket.html#socket-addresses)
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `socket.bind` with arguments `self`, `address`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

close()[¶](https://docs.python.org/3/library/socket.html#socket.socket.close "Link to this definition")

Mark the socket closed. The underlying system resource (e.g. a file descriptor) is also closed when all file objects from [`makefile()`](https://docs.python.org/3/library/socket.html#socket.socket.makefile "socket.socket.makefile")
 are closed. Once that happens, all future operations on the socket object will fail. The remote end will receive no more data (after queued data is flushed).

Sockets are automatically closed when they are garbage-collected, but it is recommended to `close()` them explicitly, or to use a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement around them.

Changed in version 3.6: [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is now raised if an error occurs when the underlying `close()` call is made.

Note

`close()` releases the resource associated with a connection but does not necessarily close the connection immediately. If you want to close the connection in a timely fashion, call [`shutdown()`](https://docs.python.org/3/library/socket.html#socket.socket.shutdown "socket.socket.shutdown")
 before `close()`.

connect(_address_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.connect "Link to this definition")

Connect to a remote socket at _address_. The format of _address_ depends on the address family — see [Socket families](https://docs.python.org/3/library/socket.html#socket-addresses)
.

If the connection is interrupted by a signal, the method waits until the connection completes, or raises a [`TimeoutError`](https://docs.python.org/3/builtins/exceptions.html#TimeoutError "TimeoutError")
 on timeout, if the signal handler doesn’t raise an exception and the socket is blocking or has a timeout. For non-blocking sockets, the method raises an [`InterruptedError`](https://docs.python.org/3/builtins/exceptions.html#InterruptedError "InterruptedError")
 exception if the connection is interrupted by a signal (or the exception raised by the signal handler).

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `socket.connect` with arguments `self`, `address`.

Changed in version 3.5: The method now waits until the connection completes instead of raising an [`InterruptedError`](https://docs.python.org/3/builtins/exceptions.html#InterruptedError "InterruptedError")
 exception if the connection is interrupted by a signal, the signal handler doesn’t raise an exception and the socket is blocking or has a timeout (see the [**PEP 475**](https://peps.python.org/pep-0475/)
 for the rationale).

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

connect\_ex(_address_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.connect_ex "Link to this definition")

Like `connect(address)`, but return an error indicator instead of raising an exception for errors returned by the C-level `connect()` call (other problems, such as “host not found,” can still raise exceptions). The error indicator is `0` if the operation succeeded, otherwise the value of the `errno` variable. This is useful to support, for example, asynchronous connects.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `socket.connect` with arguments `self`, `address`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

detach()[¶](https://docs.python.org/3/library/socket.html#socket.socket.detach "Link to this definition")

Put the socket object into closed state without actually closing the underlying file descriptor. The file descriptor is returned, and can be reused for other purposes.

Added in version 3.2.

dup()[¶](https://docs.python.org/3/library/socket.html#socket.socket.dup "Link to this definition")

Duplicate the socket.

The newly created socket is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance)
.

Changed in version 3.4: The socket is now non-inheritable.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

fileno()[¶](https://docs.python.org/3/library/socket.html#socket.socket.fileno "Link to this definition")

Return the socket’s file descriptor (a small integer), or -1 on failure. This is useful with [`select.select()`](https://docs.python.org/3/library/select.html#select.select "select.select")
.

Under Windows the small integer returned by this method cannot be used where a file descriptor can be used (such as [`os.fdopen()`](https://docs.python.org/3/library/os.html#os.fdopen "os.fdopen")
). Unix does not have this limitation.

get\_inheritable()[¶](https://docs.python.org/3/library/socket.html#socket.socket.get_inheritable "Link to this definition")

Get the [inheritable flag](https://docs.python.org/3/library/os.html#fd-inheritance)
 of the socket’s file descriptor or socket’s handle: `True` if the socket can be inherited in child processes, `False` if it cannot.

Added in version 3.4.

getpeername()[¶](https://docs.python.org/3/library/socket.html#socket.socket.getpeername "Link to this definition")

Return the remote address to which the socket is connected. This is useful to find out the port number of a remote IPv4/v6 socket, for instance. The format of the address returned depends on the address family — see [Socket families](https://docs.python.org/3/library/socket.html#socket-addresses)
. On some systems this function is not supported.

getsockname()[¶](https://docs.python.org/3/library/socket.html#socket.socket.getsockname "Link to this definition")

Return the socket’s own address. This is useful to find out the port number of an IPv4/v6 socket, for instance. The format of the address returned depends on the address family — see [Socket families](https://docs.python.org/3/library/socket.html#socket-addresses)
.

getsockopt(_level_, _optname_\[, _buflen_\])[¶](https://docs.python.org/3/library/socket.html#socket.socket.getsockopt "Link to this definition")

Return the value of the given socket option (see the Unix man page _[getsockopt(2)](https://manpages.debian.org/getsockopt(2))
_). The needed symbolic constants ([SO\_\* etc.](https://docs.python.org/3/library/socket.html#socket-unix-constants)
) are defined in this module. If _buflen_ is absent, an integer option is assumed and its integer value is returned by the function. If _buflen_ is present, it specifies the maximum length of the buffer used to receive the option in, and this buffer is returned as a bytes object. It is up to the caller to decode the contents of the buffer (see the optional built-in module [`struct`](https://docs.python.org/3/library/struct.html#module-struct "struct: Interpret bytes as packed binary data.")
 for a way to decode C structures encoded as byte strings).

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

getblocking()[¶](https://docs.python.org/3/library/socket.html#socket.socket.getblocking "Link to this definition")

Return `True` if socket is in blocking mode, `False` if in non-blocking.

This is equivalent to checking `socket.gettimeout() != 0`.

Added in version 3.7.

gettimeout()[¶](https://docs.python.org/3/library/socket.html#socket.socket.gettimeout "Link to this definition")

Return the timeout in seconds (float) associated with socket operations, or `None` if no timeout is set. This reflects the last call to [`setblocking()`](https://docs.python.org/3/library/socket.html#socket.socket.setblocking "socket.socket.setblocking")
 or [`settimeout()`](https://docs.python.org/3/library/socket.html#socket.socket.settimeout "socket.socket.settimeout")
.

ioctl(_control_, _option_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.ioctl "Link to this definition")

The `ioctl()` method is a limited interface to the WSAIoctl system interface. Please refer to the [Win32 documentation](https://msdn.microsoft.com/en-us/library/ms741621%28VS.85%29.aspx)
 for more information.

On other platforms, the generic [`fcntl.fcntl()`](https://docs.python.org/3/library/fcntl.html#fcntl.fcntl "fcntl.fcntl")
 and [`fcntl.ioctl()`](https://docs.python.org/3/library/fcntl.html#fcntl.ioctl "fcntl.ioctl")
 functions may be used; they accept a socket object as their first argument.

Currently only the following control codes are supported: `SIO_RCVALL`, `SIO_KEEPALIVE_VALS`, and `SIO_LOOPBACK_FAST_PATH`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows

Changed in version 3.6: `SIO_LOOPBACK_FAST_PATH` was added.

listen(\[_backlog_\])[¶](https://docs.python.org/3/library/socket.html#socket.socket.listen "Link to this definition")

Enable a server to accept connections. If _backlog_ is specified, it must be at least 0 (if it is lower, it is set to 0); it specifies the number of unaccepted connections that the system will allow before refusing new connections. If not specified, a default reasonable value is chosen.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

Changed in version 3.5: The _backlog_ parameter is now optional.

makefile(_mode\='r'_, _buffering\=None_, _\*_, _encoding\=None_, _errors\=None_, _newline\=None_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.makefile "Link to this definition")

Return a [file object](https://docs.python.org/3/glossary.html#term-file-object)
 associated with the socket. The exact returned type depends on the arguments given to `makefile()`. These arguments are interpreted the same way as by the built-in [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
 function, except the only supported _mode_ values are `'r'` (default), `'w'`, `'b'`, or a combination of those.

The socket must be in blocking mode; it can have a timeout, but the file object’s internal buffer may end up in an inconsistent state if a timeout occurs.

Closing the file object returned by `makefile()` won’t close the original socket unless all other file objects have been closed and [`close()`](https://docs.python.org/3/library/socket.html#socket.socket.close "socket.socket.close")
 has been called on the socket object.

Note

On Windows, the file-like object created by `makefile()` cannot be used where a file object with a file descriptor is expected, such as the stream arguments of [`subprocess.Popen()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen")
.

recv(_bufsize_\[, _flags_\])[¶](https://docs.python.org/3/library/socket.html#socket.socket.recv "Link to this definition")

Receive data from the socket. The return value is a bytes object representing the data received. The maximum amount of data to be received at once is specified by _bufsize_. A returned empty bytes object indicates that the client has disconnected. See the Unix manual page _[recv(2)](https://manpages.debian.org/recv(2))
_ for the meaning of the optional argument _flags_; it defaults to zero.

Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the method now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/builtins/exceptions.html#InterruptedError "InterruptedError")
 exception (see [**PEP 475**](https://peps.python.org/pep-0475/)
 for the rationale).

recvfrom(_bufsize_\[, _flags_\])[¶](https://docs.python.org/3/library/socket.html#socket.socket.recvfrom "Link to this definition")

Receive data from the socket. The return value is a pair `(bytes, address)` where _bytes_ is a bytes object representing the data received and _address_ is the address of the socket sending the data. See the Unix manual page _[recv(2)](https://manpages.debian.org/recv(2))
_ for the meaning of the optional argument _flags_; it defaults to zero. The format of _address_ depends on the address family — see [Socket families](https://docs.python.org/3/library/socket.html#socket-addresses)
.

Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the method now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/builtins/exceptions.html#InterruptedError "InterruptedError")
 exception (see [**PEP 475**](https://peps.python.org/pep-0475/)
 for the rationale).

Changed in version 3.7: For multicast IPv6 address, first item of _address_ does not contain `%scope_id` part anymore. In order to get full IPv6 address use [`getnameinfo()`](https://docs.python.org/3/library/socket.html#socket.getnameinfo "socket.getnameinfo")
.

recvmsg(_bufsize_\[, _ancbufsize_\[, _flags_\]\])[¶](https://docs.python.org/3/library/socket.html#socket.socket.recvmsg "Link to this definition")

Receive normal data (up to _bufsize_ bytes) and ancillary data from the socket. The _ancbufsize_ argument sets the size in bytes of the internal buffer used to receive the ancillary data; it defaults to 0, meaning that no ancillary data will be received. Appropriate buffer sizes for ancillary data can be calculated using [`CMSG_SPACE()`](https://docs.python.org/3/library/socket.html#socket.CMSG_SPACE "socket.CMSG_SPACE")
 or [`CMSG_LEN()`](https://docs.python.org/3/library/socket.html#socket.CMSG_LEN "socket.CMSG_LEN")
, and items which do not fit into the buffer might be truncated or discarded. The _flags_ argument defaults to 0 and has the same meaning as for [`recv()`](https://docs.python.org/3/library/socket.html#socket.socket.recv "socket.socket.recv")
.

The return value is a 4-tuple: `(data, ancdata, msg_flags, address)`. The _data_ item is a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object holding the non-ancillary data received. The _ancdata_ item is a list of zero or more tuples `(cmsg_level, cmsg_type, cmsg_data)` representing the ancillary data (control messages) received: _cmsg\_level_ and _cmsg\_type_ are integers specifying the protocol level and protocol-specific type respectively, and _cmsg\_data_ is a `bytes` object holding the associated data. The _msg\_flags_ item is the bitwise OR of various flags indicating conditions on the received message; see your system documentation for details. If the receiving socket is unconnected, _address_ is the address of the sending socket, if available; otherwise, its value is unspecified.

On some systems, [`sendmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.sendmsg "socket.socket.sendmsg")
 and `recvmsg()` can be used to pass file descriptors between processes over an [`AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX")
 socket. When this facility is used (it is often restricted to [`SOCK_STREAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM "socket.SOCK_STREAM")
 sockets), `recvmsg()` will return, in its ancillary data, items of the form `(socket.SOL_SOCKET, socket.SCM_RIGHTS, fds)`, where _fds_ is a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object representing the new file descriptors as a binary array of the native C int type. If `recvmsg()` raises an exception after the system call returns, it will first attempt to close any file descriptors received via this mechanism.

Some systems do not indicate the truncated length of ancillary data items which have been only partially received. If an item appears to extend beyond the end of the buffer, `recvmsg()` will issue a [`RuntimeWarning`](https://docs.python.org/3/builtins/exceptions.html#RuntimeWarning "RuntimeWarning")
, and will return the part of it which is inside the buffer provided it has not been truncated before the start of its associated data.

On systems which support the `SCM_RIGHTS` mechanism, the following function will receive up to _maxfds_ file descriptors, returning the message data and a list containing the descriptors (while ignoring unexpected conditions such as unrelated control messages being received). See also [`sendmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.sendmsg "socket.socket.sendmsg")
.

Copy

import socket, array

def recv\_fds(sock, msglen, maxfds):
    fds \= array.array("i")   \# Array of ints
    msg, ancdata, flags, addr \= sock.recvmsg(msglen, socket.CMSG\_LEN(maxfds \* fds.itemsize))
    for cmsg\_level, cmsg\_type, cmsg\_data in ancdata:
        if cmsg\_level \== socket.SOL\_SOCKET and cmsg\_type \== socket.SCM\_RIGHTS:
            \# Append data, ignoring any truncated integers at the end.
            fds.frombytes(cmsg\_data\[:len(cmsg\_data) \- (len(cmsg\_data) % fds.itemsize)\])
    return msg, list(fds)

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Most Unix platforms.

Added in version 3.3.

Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the method now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/builtins/exceptions.html#InterruptedError "InterruptedError")
 exception (see [**PEP 475**](https://peps.python.org/pep-0475/)
 for the rationale).

recvmsg\_into(_buffers_\[, _ancbufsize_\[, _flags_\]\])[¶](https://docs.python.org/3/library/socket.html#socket.socket.recvmsg_into "Link to this definition")

Receive normal data and ancillary data from the socket, behaving as [`recvmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.recvmsg "socket.socket.recvmsg")
 would, but scatter the non-ancillary data into a series of buffers instead of returning a new bytes object. The _buffers_ argument must be an iterable of objects that export writable buffers (e.g. [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
 objects); these will be filled with successive chunks of the non-ancillary data until it has all been written or there are no more buffers. The operating system may set a limit ([`sysconf()`](https://docs.python.org/3/library/os.html#os.sysconf "os.sysconf")
 value `SC_IOV_MAX`) on the number of buffers that can be used. The _ancbufsize_ and _flags_ arguments have the same meaning as for `recvmsg()`.

The return value is a 4-tuple: `(nbytes, ancdata, msg_flags, address)`, where _nbytes_ is the total number of bytes of non-ancillary data written into the buffers, and _ancdata_, _msg\_flags_ and _address_ are the same as for [`recvmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.recvmsg "socket.socket.recvmsg")
.

Example:

Copy

\>>> import socket
\>>> s1, s2 \= socket.socketpair()
\>>> b1 \= bytearray(b'----')
\>>> b2 \= bytearray(b'0123456789')
\>>> b3 \= bytearray(b'--------------')
\>>> s1.send(b'Mary had a little lamb')
22
\>>> s2.recvmsg\_into(\[b1, memoryview(b2)\[2:9\], b3\])
(22, \[\], 0, None)
\>>> \[b1, b2, b3\]
\[bytearray(b'Mary'), bytearray(b'01 had a 9'), bytearray(b'little lamb---')\]

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Most Unix platforms.

Added in version 3.3.

recvfrom\_into(_buffer_\[, _nbytes_\[, _flags_\]\])[¶](https://docs.python.org/3/library/socket.html#socket.socket.recvfrom_into "Link to this definition")

Receive data from the socket, writing it into _buffer_ instead of creating a new bytestring. The return value is a pair `(nbytes, address)` where _nbytes_ is the number of bytes received and _address_ is the address of the socket sending the data. See the Unix manual page _[recv(2)](https://manpages.debian.org/recv(2))
_ for the meaning of the optional argument _flags_; it defaults to zero. The format of _address_ depends on the address family — see [Socket families](https://docs.python.org/3/library/socket.html#socket-addresses)
.

recv\_into(_buffer_\[, _nbytes_\[, _flags_\]\])[¶](https://docs.python.org/3/library/socket.html#socket.socket.recv_into "Link to this definition")

Receive up to _nbytes_ bytes from the socket, storing the data into a buffer rather than creating a new bytestring. If _nbytes_ is not specified (or 0), receive up to the size available in the given buffer. Returns the number of bytes received. See the Unix manual page _[recv(2)](https://manpages.debian.org/recv(2))
_ for the meaning of the optional argument _flags_; it defaults to zero.

send(_bytes_\[, _flags_\])[¶](https://docs.python.org/3/library/socket.html#socket.socket.send "Link to this definition")

Send data to the socket. The socket must be connected to a remote socket. The optional _flags_ argument has the same meaning as for [`recv()`](https://docs.python.org/3/library/socket.html#socket.socket.recv "socket.socket.recv")
. Returns the number of bytes sent. Applications are responsible for checking that all data has been sent; if only some of the data was transmitted, the application needs to attempt delivery of the remaining data. For further information on this topic, consult the [Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html#socket-howto)
.

Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the method now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/builtins/exceptions.html#InterruptedError "InterruptedError")
 exception (see [**PEP 475**](https://peps.python.org/pep-0475/)
 for the rationale).

sendall(_bytes_\[, _flags_\])[¶](https://docs.python.org/3/library/socket.html#socket.socket.sendall "Link to this definition")

Send data to the socket. The socket must be connected to a remote socket. The optional _flags_ argument has the same meaning as for [`recv()`](https://docs.python.org/3/library/socket.html#socket.socket.recv "socket.socket.recv")
. Unlike [`send()`](https://docs.python.org/3/library/socket.html#socket.socket.send "socket.socket.send")
, this method continues to send data from _bytes_ until either all data has been sent or an error occurs. `None` is returned on success. On error, an exception is raised, and there is no way to determine how much data, if any, was successfully sent.

Changed in version 3.5: The socket timeout is no longer reset each time data is sent successfully. The socket timeout is now the maximum total duration to send all data.

Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the method now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/builtins/exceptions.html#InterruptedError "InterruptedError")
 exception (see [**PEP 475**](https://peps.python.org/pep-0475/)
 for the rationale).

sendto(_bytes_, _address_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.sendto "Link to this definition")

sendto(_bytes_, _flags_, _address_)

Send data to the socket. The socket should not be connected to a remote socket, since the destination socket is specified by _address_. The optional _flags_ argument has the same meaning as for [`recv()`](https://docs.python.org/3/library/socket.html#socket.socket.recv "socket.socket.recv")
. Return the number of bytes sent. The format of _address_ depends on the address family — see [Socket families](https://docs.python.org/3/library/socket.html#socket-addresses)
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `socket.sendto` with arguments `self`, `address`.

Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the method now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/builtins/exceptions.html#InterruptedError "InterruptedError")
 exception (see [**PEP 475**](https://peps.python.org/pep-0475/)
 for the rationale).

sendmsg(_buffers_\[, _ancdata_\[, _flags_\[, _address_\]\]\])[¶](https://docs.python.org/3/library/socket.html#socket.socket.sendmsg "Link to this definition")

Send normal and ancillary data to the socket, gathering the non-ancillary data from a series of buffers and concatenating it into a single message. The _buffers_ argument specifies the non-ancillary data as an iterable of [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 (e.g. [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 objects); the operating system may set a limit ([`sysconf()`](https://docs.python.org/3/library/os.html#os.sysconf "os.sysconf")
 value `SC_IOV_MAX`) on the number of buffers that can be used. The _ancdata_ argument specifies the ancillary data (control messages) as an iterable of zero or more tuples `(cmsg_level, cmsg_type, cmsg_data)`, where _cmsg\_level_ and _cmsg\_type_ are integers specifying the protocol level and protocol-specific type respectively, and _cmsg\_data_ is a bytes-like object holding the associated data. Note that some systems (in particular, systems without [`CMSG_SPACE()`](https://docs.python.org/3/library/socket.html#socket.CMSG_SPACE "socket.CMSG_SPACE")
) might support sending only one control message per call. The _flags_ argument defaults to 0 and has the same meaning as for [`send()`](https://docs.python.org/3/library/socket.html#socket.socket.send "socket.socket.send")
. If _address_ is supplied and not `None`, it sets a destination address for the message. The return value is the number of bytes of non-ancillary data sent.

The following function sends the list of file descriptors _fds_ over an [`AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX")
 socket, on systems which support the `SCM_RIGHTS` mechanism. See also [`recvmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.recvmsg "socket.socket.recvmsg")
.

Copy

import socket, array

def send\_fds(sock, msg, fds):
    return sock.sendmsg(\[msg\], \[(socket.SOL\_SOCKET, socket.SCM\_RIGHTS, array.array("i", fds))\])

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Most Unix platforms.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `socket.sendmsg` with arguments `self`, `address`.

Added in version 3.3.

Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the method now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/builtins/exceptions.html#InterruptedError "InterruptedError")
 exception (see [**PEP 475**](https://peps.python.org/pep-0475/)
 for the rationale).

sendmsg\_afalg(\[_msg_, \]_\*_, _op_\[, _iv_\[, _assoclen_\[, _flags_\]\]\])[¶](https://docs.python.org/3/library/socket.html#socket.socket.sendmsg_afalg "Link to this definition")

Specialized version of [`sendmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.sendmsg "socket.socket.sendmsg")
 for [`AF_ALG`](https://docs.python.org/3/library/socket.html#socket.AF_ALG "socket.AF_ALG")
 socket. Set mode, IV, AEAD associated data length and flags for `AF_ALG` socket.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.38.

Added in version 3.6.

sendfile(_file_, _offset\=0_, _count\=None_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.sendfile "Link to this definition")

Send a file until EOF is reached by using high-performance [`os.sendfile`](https://docs.python.org/3/library/os.html#os.sendfile "os.sendfile")
 and return the total number of bytes which were sent. _file_ must be a regular file object opened in binary mode. If `os.sendfile` is not available (e.g. Windows) or _file_ is not a regular file [`send()`](https://docs.python.org/3/library/socket.html#socket.socket.send "socket.socket.send")
 will be used instead. _offset_ tells from where to start reading the file. If specified, _count_ is the total number of bytes to transmit as opposed to sending the file until EOF is reached. File position is updated on return or also in case of error in which case [`file.tell()`](https://docs.python.org/3/library/io.html#io.IOBase.tell "io.IOBase.tell")
 can be used to figure out the number of bytes which were sent. The socket must be of [`SOCK_STREAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM "socket.SOCK_STREAM")
 type. Non-blocking sockets are not supported.

Added in version 3.5.

set\_inheritable(_inheritable_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.set_inheritable "Link to this definition")

Set the [inheritable flag](https://docs.python.org/3/library/os.html#fd-inheritance)
 of the socket’s file descriptor or socket’s handle.

Added in version 3.4.

setblocking(_flag_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.setblocking "Link to this definition")

Set blocking or non-blocking mode of the socket: if _flag_ is false, the socket is set to non-blocking, else to blocking mode.

This method is a shorthand for certain [`settimeout()`](https://docs.python.org/3/library/socket.html#socket.socket.settimeout "socket.socket.settimeout")
 calls:

*   `sock.setblocking(True)` is equivalent to `sock.settimeout(None)`
    
*   `sock.setblocking(False)` is equivalent to `sock.settimeout(0.0)`
    

Changed in version 3.7: The method no longer applies [`SOCK_NONBLOCK`](https://docs.python.org/3/library/socket.html#socket.SOCK_NONBLOCK "socket.SOCK_NONBLOCK")
 flag on [`socket.type`](https://docs.python.org/3/library/socket.html#socket.socket.type "socket.socket.type")
.

settimeout(_value_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.settimeout "Link to this definition")

Set a timeout on blocking socket operations. The _value_ argument can be a nonnegative real number expressing seconds, or `None`. If a non-zero value is given, subsequent socket operations will raise a [`timeout`](https://docs.python.org/3/library/socket.html#socket.timeout "socket.timeout")
 exception if the timeout period _value_ has elapsed before the operation has completed. If zero is given, the socket is put in non-blocking mode. If `None` is given, the socket is put in blocking mode.

For further information, please consult the [notes on socket timeouts](https://docs.python.org/3/library/socket.html#socket-timeouts)
.

Changed in version 3.7: The method no longer toggles [`SOCK_NONBLOCK`](https://docs.python.org/3/library/socket.html#socket.SOCK_NONBLOCK "socket.SOCK_NONBLOCK")
 flag on [`socket.type`](https://docs.python.org/3/library/socket.html#socket.socket.type "socket.socket.type")
.

Changed in version 3.15: Accepts any real number, not only integer or float.

setsockopt(_level_, _optname_, _value: [int](https://docs.python.org/3/builtins/functions.html#int "int")
 | [Buffer](https://docs.python.org/3/library/collections.abc.html#collections.abc.Buffer "collections.abc.Buffer")
_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.setsockopt "Link to this definition")

setsockopt(_level_, _optname_, _None_, _optlen: [int](https://docs.python.org/3/builtins/functions.html#int "int")
_)

Set the value of the given socket option (see the Unix manual page _[setsockopt(2)](https://manpages.debian.org/setsockopt(2))
_). The needed symbolic constants are defined in this module (SO\_\* etc. <socket-unix-constants>). The value can be an integer, `None` or a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 representing a buffer. In the latter case it is up to the caller to ensure that the bytestring contains the proper bits (see the optional built-in module [`struct`](https://docs.python.org/3/library/struct.html#module-struct "struct: Interpret bytes as packed binary data.")
 for a way to encode C structures as bytestrings). When _value_ is set to `None`, _optlen_ argument is required. It’s equivalent to calling `setsockopt()` C function with `optval=NULL` and `optlen=optlen`.

Changed in version 3.5: Writable [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 is now accepted.

Changed in version 3.6: setsockopt(level, optname, None, optlen: int) form added.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

shutdown(_how_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.shutdown "Link to this definition")

Shut down one or both halves of the connection. If _how_ is [`SHUT_RD`](https://docs.python.org/3/library/socket.html#socket.SHUT_RD "socket.SHUT_RD")
, further receives are disallowed. If _how_ is [`SHUT_WR`](https://docs.python.org/3/library/socket.html#socket.SHUT_WR "socket.SHUT_WR")
, further sends are disallowed. If _how_ is [`SHUT_RDWR`](https://docs.python.org/3/library/socket.html#socket.SHUT_RDWR "socket.SHUT_RDWR")
, further sends and receives are disallowed.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

share(_process\_id_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.share "Link to this definition")

Duplicate a socket and prepare it for sharing with a target process. The target process must be provided with _process\_id_. The resulting bytes object can then be passed to the target process using some form of interprocess communication and the socket can be recreated there using [`fromshare()`](https://docs.python.org/3/library/socket.html#socket.fromshare "socket.fromshare")
. Once this method has been called, it is safe to close the socket since the operating system has already duplicated it for the target process.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

Added in version 3.3.

Note that there are no methods `read()` or `write()`; use [`recv()`](https://docs.python.org/3/library/socket.html#socket.socket.recv "socket.socket.recv")
 and [`send()`](https://docs.python.org/3/library/socket.html#socket.socket.send "socket.socket.send")
 without _flags_ argument instead.

Socket objects also have these (read-only) attributes that correspond to the values given to the `socket` constructor.

family[¶](https://docs.python.org/3/library/socket.html#socket.socket.family "Link to this definition")

The socket family.

type[¶](https://docs.python.org/3/library/socket.html#socket.socket.type "Link to this definition")

The socket type.

proto[¶](https://docs.python.org/3/library/socket.html#socket.socket.proto "Link to this definition")

The socket protocol.

class socket.SocketType[¶](https://docs.python.org/3/library/socket.html#socket.SocketType "Link to this definition")

The base class of the [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
 type, re-exported from `_socket`. An instance check such as `isinstance(socket(...), SocketType)` is true, but `SocketType` is not the same as `type(socket(...))`, which is `socket` itself.

Notes on socket timeouts[¶](https://docs.python.org/3/library/socket.html#notes-on-socket-timeouts "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

A socket object can be in one of three modes: blocking, non-blocking, or timeout. Sockets are by default always created in blocking mode, but this can be changed by calling [`setdefaulttimeout()`](https://docs.python.org/3/library/socket.html#socket.setdefaulttimeout "socket.setdefaulttimeout")
.

*   In _blocking mode_, operations block until complete or the system returns an error (such as connection timed out).
    
*   In _non-blocking mode_, operations fail (with an error that is unfortunately system-dependent) if they cannot be completed immediately: functions from the [`select`](https://docs.python.org/3/library/select.html#module-select "select: Wait for I/O completion on multiple streams.")
     module can be used to know when and whether a socket is available for reading or writing.
    
*   In _timeout mode_, operations fail if they cannot be completed within the timeout specified for the socket (they raise a [`timeout`](https://docs.python.org/3/library/socket.html#socket.timeout "socket.timeout")
     exception) or if the system returns an error.
    

Note

At the operating system level, sockets in _timeout mode_ are internally set in non-blocking mode. Also, the blocking and timeout modes are shared between file descriptors and socket objects that refer to the same network endpoint. This implementation detail can have visible consequences if e.g. you decide to use the [`fileno()`](https://docs.python.org/3/library/socket.html#socket.socket.fileno "socket.socket.fileno")
 of a socket.

### Timeouts and the `connect` method[¶](https://docs.python.org/3/library/socket.html#timeouts-and-the-connect-method "Link to this heading")

The [`connect()`](https://docs.python.org/3/library/socket.html#socket.socket.connect "socket.socket.connect")
 operation is also subject to the timeout setting, and in general it is recommended to call [`settimeout()`](https://docs.python.org/3/library/socket.html#socket.socket.settimeout "socket.socket.settimeout")
 before calling `connect()` or pass a timeout parameter to [`create_connection()`](https://docs.python.org/3/library/socket.html#socket.create_connection "socket.create_connection")
. However, the system network stack may also return a connection timeout error of its own regardless of any Python socket timeout setting.

### Timeouts and the `accept` method[¶](https://docs.python.org/3/library/socket.html#timeouts-and-the-accept-method "Link to this heading")

If [`getdefaulttimeout()`](https://docs.python.org/3/library/socket.html#socket.getdefaulttimeout "socket.getdefaulttimeout")
 is not [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
, sockets returned by the [`accept()`](https://docs.python.org/3/library/socket.html#socket.socket.accept "socket.socket.accept")
 method inherit that timeout. Otherwise, the behaviour depends on settings of the listening socket:

*   if the listening socket is in _blocking mode_ or in _timeout mode_, the socket returned by [`accept()`](https://docs.python.org/3/library/socket.html#socket.socket.accept "socket.socket.accept")
     is in _blocking mode_;
    
*   if the listening socket is in _non-blocking mode_, whether the socket returned by [`accept()`](https://docs.python.org/3/library/socket.html#socket.socket.accept "socket.socket.accept")
     is in blocking or non-blocking mode is operating system-dependent. If you want to ensure cross-platform behaviour, it is recommended you manually override this setting.
    

Example[¶](https://docs.python.org/3/library/socket.html#example "Link to this heading")

-----------------------------------------------------------------------------------------

Here are four minimal example programs using the TCP/IP protocol: a server that echoes all data that it receives back (servicing only one client), and a client using it. Note that a server must perform the sequence [`socket()`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
, [`bind()`](https://docs.python.org/3/library/socket.html#socket.socket.bind "socket.socket.bind")
, [`listen()`](https://docs.python.org/3/library/socket.html#socket.socket.listen "socket.socket.listen")
, [`accept()`](https://docs.python.org/3/library/socket.html#socket.socket.accept "socket.socket.accept")
 (possibly repeating the `accept()` to service more than one client), while a client only needs the sequence `socket()`, [`connect()`](https://docs.python.org/3/library/socket.html#socket.socket.connect "socket.socket.connect")
. Also note that the server does not [`sendall()`](https://docs.python.org/3/library/socket.html#socket.socket.sendall "socket.socket.sendall")
/[`recv()`](https://docs.python.org/3/library/socket.html#socket.socket.recv "socket.socket.recv")
 on the socket it is listening on but on the new socket returned by `accept()`.

The first two examples support IPv4 only.

Copy

\# Echo server program
import socket

HOST \= ''                 \# Symbolic name meaning all available interfaces
PORT \= 50007              \# Arbitrary non-privileged port
with socket.socket(socket.AF\_INET, socket.SOCK\_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr \= s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data \= conn.recv(1024)
            if not data: break
            conn.sendall(data)

Copy

\# Echo client program
import socket

HOST \= 'daring.cwi.nl'    \# The remote host
PORT \= 50007              \# The same port as used by the server
with socket.socket(socket.AF\_INET, socket.SOCK\_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data \= s.recv(1024)
print('Received', repr(data))

The next two examples are identical to the above two, but support both IPv4 and IPv6. The server side will listen to the first address family available (it should listen to both instead). On most of IPv6-ready systems, IPv6 will take precedence and the server may not accept IPv4 traffic. The client side will try to connect to all the addresses returned as a result of the name resolution, and sends traffic to the first one connected successfully.

Copy

\# Echo server program
import socket
import sys

HOST \= None               \# Symbolic name meaning all available interfaces
PORT \= 50007              \# Arbitrary non-privileged port
s \= None
for res in socket.getaddrinfo(HOST, PORT, socket.AF\_UNSPEC,
                              socket.SOCK\_STREAM, 0, socket.AI\_PASSIVE):
    af, socktype, proto, canonname, sa \= res
    try:
        s \= socket.socket(af, socktype, proto)
    except OSError as msg:
        s \= None
        continue
    try:
        s.bind(sa)
        s.listen(1)
    except OSError as msg:
        s.close()
        s \= None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)
conn, addr \= s.accept()
with conn:
    print('Connected by', addr)
    while True:
        data \= conn.recv(1024)
        if not data: break
        conn.send(data)

Copy

\# Echo client program
import socket
import sys

HOST \= 'daring.cwi.nl'    \# The remote host
PORT \= 50007              \# The same port as used by the server
s \= None
for res in socket.getaddrinfo(HOST, PORT, socket.AF\_UNSPEC, socket.SOCK\_STREAM):
    af, socktype, proto, canonname, sa \= res
    try:
        s \= socket.socket(af, socktype, proto)
    except OSError as msg:
        s \= None
        continue
    try:
        s.connect(sa)
    except OSError as msg:
        s.close()
        s \= None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)
with s:
    s.sendall(b'Hello, world')
    data \= s.recv(1024)
print('Received', repr(data))

The next example shows how to write a very simple network sniffer with raw sockets on Windows. The example requires administrator privileges to modify the interface:

Copy

import socket

\# the public network interface
HOST \= socket.gethostbyname(socket.gethostname())

\# create a raw socket and bind it to the public interface
s \= socket.socket(socket.AF\_INET, socket.SOCK\_RAW, socket.IPPROTO\_IP)
s.bind((HOST, 0))

\# Include IP headers
s.setsockopt(socket.IPPROTO\_IP, socket.IP\_HDRINCL, 1)

\# receive all packets
s.ioctl(socket.SIO\_RCVALL, socket.RCVALL\_ON)

\# receive a packet
print(s.recvfrom(65565))

\# disabled promiscuous mode
s.ioctl(socket.SIO\_RCVALL, socket.RCVALL\_OFF)

The next example shows how to use the socket interface to communicate to a CAN network using the raw socket protocol. To use CAN with the broadcast manager protocol instead, open a socket with:

Copy

socket.socket(socket.AF\_CAN, socket.SOCK\_DGRAM, socket.CAN\_BCM)

After binding (`CAN_RAW`) or connecting ([`CAN_BCM`](https://docs.python.org/3/library/socket.html#socket.CAN_BCM "socket.CAN_BCM")
) the socket, you can use the [`socket.send()`](https://docs.python.org/3/library/socket.html#socket.socket.send "socket.socket.send")
 and [`socket.recv()`](https://docs.python.org/3/library/socket.html#socket.socket.recv "socket.socket.recv")
 operations (and their counterparts) on the socket object as usual.

This last example might require special privileges:

Copy

import socket
import struct

\# CAN frame packing/unpacking (see 'struct can\_frame' in <linux/can.h>)

can\_frame\_fmt \= "=IB3x8s"
can\_frame\_size \= struct.calcsize(can\_frame\_fmt)

def build\_can\_frame(can\_id, data):
    can\_dlc \= len(data)
    data \= data.ljust(8, b'\\x00')
    return struct.pack(can\_frame\_fmt, can\_id, can\_dlc, data)

def dissect\_can\_frame(frame):
    can\_id, can\_dlc, data \= struct.unpack(can\_frame\_fmt, frame)
    return (can\_id, can\_dlc, data\[:can\_dlc\])

\# create a raw socket and bind it to the 'vcan0' interface
s \= socket.socket(socket.AF\_CAN, socket.SOCK\_RAW, socket.CAN\_RAW)
s.bind(('vcan0',))

while True:
    cf, addr \= s.recvfrom(can\_frame\_size)

    print('Received: can\_id=%x, can\_dlc=%x, data=%s' % dissect\_can\_frame(cf))

    try:
        s.send(cf)
    except OSError:
        print('Error sending CAN frame')

    try:
        s.send(build\_can\_frame(0x01, b'\\x01\\x02\\x03'))
    except OSError:
        print('Error sending CAN frame')

Running an example several times with too small delay between executions, could lead to this error:

Copy

OSError: \[Errno 98\] Address already in use

This is because the previous execution has left the socket in a `TIME_WAIT` state, and can’t be immediately reused.

There is a `socket` flag to set, in order to prevent this, `socket.SO_REUSEADDR`:

Copy

s \= socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)
s.setsockopt(socket.SOL\_SOCKET, socket.SO\_REUSEADDR, 1)
s.bind((HOST, PORT))

the `SO_REUSEADDR` flag tells the kernel to reuse a local socket in `TIME_WAIT` state, without waiting for its natural timeout to expire.

See also

For an introduction to socket programming (in C), see the following papers:

*   _An Introductory 4.3BSD Interprocess Communication Tutorial_, by Stuart Sechrest
    
*   _An Advanced 4.3BSD Interprocess Communication Tutorial_, by Samuel J. Leffler et al,
    

both in the UNIX Programmer’s Manual, Supplementary Documents 1 (sections PS1:7 and PS1:8). The platform-specific reference material for the various socket-related system calls are also a valuable source of information on the details of socket semantics. For Unix, refer to the manual pages; for Windows, see the WinSock (or Winsock 2) specification. For IPv6-ready APIs, readers may want to refer to [**RFC 3493**](https://datatracker.ietf.org/doc/html/rfc3493.html)
 titled Basic Socket Interface Extensions for IPv6.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`socket` — Low-level networking interface](https://docs.python.org/3/library/socket.html#)
    *   [Socket families](https://docs.python.org/3/library/socket.html#socket-families)
        
    *   [Module contents](https://docs.python.org/3/library/socket.html#module-contents)
        *   [Exceptions](https://docs.python.org/3/library/socket.html#exceptions)
            
        *   [Constants](https://docs.python.org/3/library/socket.html#constants)
            
        *   [Functions](https://docs.python.org/3/library/socket.html#functions)
            *   [Creating sockets](https://docs.python.org/3/library/socket.html#creating-sockets)
                
            *   [Other functions](https://docs.python.org/3/library/socket.html#other-functions)
                
    *   [Socket Objects](https://docs.python.org/3/library/socket.html#socket-objects)
        
    *   [Notes on socket timeouts](https://docs.python.org/3/library/socket.html#notes-on-socket-timeouts)
        *   [Timeouts and the `connect` method](https://docs.python.org/3/library/socket.html#timeouts-and-the-connect-method)
            
        *   [Timeouts and the `accept` method](https://docs.python.org/3/library/socket.html#timeouts-and-the-accept-method)
            
    *   [Example](https://docs.python.org/3/library/socket.html#example)
        

#### Previous topic

[asyncio and free-threaded Python](https://docs.python.org/3/library/asyncio-threading.html "previous chapter")

#### Next topic

[`ssl` — TLS/SSL wrapper for socket objects](https://docs.python.org/3/library/ssl.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=socket+%E2%80%94+Low-level+networking+interface&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsocket.html&pagesource=library%2Fsocket.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/socket.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/ssl.html "ssl — TLS/SSL wrapper for socket objects")
     |
*   [previous](https://docs.python.org/3/library/asyncio-threading.html "asyncio and free-threaded Python")
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
*   [`socket` — Low-level networking interface](https://docs.python.org/3/library/socket.html)
    
*    
    
    |
*   Theme Auto Light Dark |