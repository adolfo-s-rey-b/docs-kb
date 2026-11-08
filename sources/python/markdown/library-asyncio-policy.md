### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-platforms.html "Platform Support")
     |
*   [previous](https://docs.python.org/3/library/asyncio-protocol.html "Transports and Protocols")
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
*   [Policies](https://docs.python.org/3/library/asyncio-policy.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Policies[¶](https://docs.python.org/3/library/asyncio-policy.html#policies "Link to this heading")

===================================================================================================

Warning

Policies are deprecated and will be removed in Python 3.16. Users are encouraged to use the [`asyncio.run()`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.run "asyncio.run")
 function or the [`asyncio.Runner`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.Runner "asyncio.Runner")
 with _loop\_factory_ to use the desired loop implementation.

An event loop policy is a global object used to get and set the current [event loop](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-event-loop)
, as well as create new event loops. The default policy can be [replaced](https://docs.python.org/3/library/asyncio-policy.html#asyncio-policy-get-set)
 with [built-in alternatives](https://docs.python.org/3/library/asyncio-policy.html#asyncio-policy-builtin)
 to use different event loop implementations, or substituted by a [custom policy](https://docs.python.org/3/library/asyncio-policy.html#asyncio-custom-policies)
 that can override these behaviors.

The [policy object](https://docs.python.org/3/library/asyncio-policy.html#asyncio-policy-objects)
 gets and sets a separate event loop per _context_. This is per-thread by default, though custom policies could define _context_ differently.

Custom event loop policies can control the behavior of [`get_event_loop()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.get_event_loop "asyncio.get_event_loop")
, [`set_event_loop()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.set_event_loop "asyncio.set_event_loop")
, and [`new_event_loop()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.new_event_loop "asyncio.new_event_loop")
.

Policy objects should implement the APIs defined in the [`AbstractEventLoopPolicy`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.AbstractEventLoopPolicy "asyncio.AbstractEventLoopPolicy")
 abstract base class.

Getting and Setting the Policy[¶](https://docs.python.org/3/library/asyncio-policy.html#getting-and-setting-the-policy "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

The following functions can be used to get and set the policy for the current process:

asyncio.get\_event\_loop\_policy()[¶](https://docs.python.org/3/library/asyncio-policy.html#asyncio.get_event_loop_policy "Link to this definition")

Return the current process-wide policy.

Deprecated since version 3.14: The `get_event_loop_policy()` function is deprecated and will be removed in Python 3.16.

asyncio.set\_event\_loop\_policy(_policy_)[¶](https://docs.python.org/3/library/asyncio-policy.html#asyncio.set_event_loop_policy "Link to this definition")

Set the current process-wide policy to _policy_.

If _policy_ is set to `None`, the default policy is restored.

Deprecated since version 3.14: The `set_event_loop_policy()` function is deprecated and will be removed in Python 3.16.

Policy Objects[¶](https://docs.python.org/3/library/asyncio-policy.html#policy-objects "Link to this heading")

---------------------------------------------------------------------------------------------------------------

The abstract event loop policy base class is defined as follows:

class asyncio.AbstractEventLoopPolicy[¶](https://docs.python.org/3/library/asyncio-policy.html#asyncio.AbstractEventLoopPolicy "Link to this definition")

An abstract base class for asyncio policies.

get\_event\_loop()[¶](https://docs.python.org/3/library/asyncio-policy.html#asyncio.AbstractEventLoopPolicy.get_event_loop "Link to this definition")

Get the event loop for the current context.

Return an event loop object implementing the [`AbstractEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.AbstractEventLoop "asyncio.AbstractEventLoop")
 interface.

This method should never return `None`.

Changed in version 3.6.

set\_event\_loop(_loop_)[¶](https://docs.python.org/3/library/asyncio-policy.html#asyncio.AbstractEventLoopPolicy.set_event_loop "Link to this definition")

Set the event loop for the current context to _loop_.

new\_event\_loop()[¶](https://docs.python.org/3/library/asyncio-policy.html#asyncio.AbstractEventLoopPolicy.new_event_loop "Link to this definition")

Create and return a new event loop object.

This method should never return `None`.

Deprecated since version 3.14: The `AbstractEventLoopPolicy` class is deprecated and will be removed in Python 3.16.

asyncio ships with the following built-in policies:

class asyncio.DefaultEventLoopPolicy[¶](https://docs.python.org/3/library/asyncio-policy.html#asyncio.DefaultEventLoopPolicy "Link to this definition")

The default asyncio policy. Uses [`SelectorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop")
 on Unix and [`ProactorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop")
 on Windows.

There is no need to install the default policy manually. asyncio is configured to use the default policy automatically.

Changed in version 3.8: On Windows, [`ProactorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop")
 is now used by default.

Changed in version 3.14: The [`get_event_loop()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.get_event_loop "asyncio.get_event_loop")
 method of the default asyncio policy now raises a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 if there is no set event loop.

Deprecated since version 3.14: The `DefaultEventLoopPolicy` class is deprecated and will be removed in Python 3.16.

class asyncio.WindowsSelectorEventLoopPolicy[¶](https://docs.python.org/3/library/asyncio-policy.html#asyncio.WindowsSelectorEventLoopPolicy "Link to this definition")

An alternative event loop policy that uses the [`SelectorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop")
 event loop implementation.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

Deprecated since version 3.14: The `WindowsSelectorEventLoopPolicy` class is deprecated and will be removed in Python 3.16.

class asyncio.WindowsProactorEventLoopPolicy[¶](https://docs.python.org/3/library/asyncio-policy.html#asyncio.WindowsProactorEventLoopPolicy "Link to this definition")

An alternative event loop policy that uses the [`ProactorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop")
 event loop implementation.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

Deprecated since version 3.14: The `WindowsProactorEventLoopPolicy` class is deprecated and will be removed in Python 3.16.

Custom Policies[¶](https://docs.python.org/3/library/asyncio-policy.html#custom-policies "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

To implement a new event loop policy, it is recommended to subclass [`DefaultEventLoopPolicy`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.DefaultEventLoopPolicy "asyncio.DefaultEventLoopPolicy")
 and override the methods for which custom behavior is wanted, e.g.:

Copy

class MyEventLoopPolicy(asyncio.DefaultEventLoopPolicy):

    def get\_event\_loop(self):
        """Get the event loop.

        This may be None or an instance of EventLoop.
        """
        loop \= super().get\_event\_loop()
        \# Do something with loop ...
        return loop

asyncio.set\_event\_loop\_policy(MyEventLoopPolicy())

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Policies](https://docs.python.org/3/library/asyncio-policy.html#)
    *   [Getting and Setting the Policy](https://docs.python.org/3/library/asyncio-policy.html#getting-and-setting-the-policy)
        
    *   [Policy Objects](https://docs.python.org/3/library/asyncio-policy.html#policy-objects)
        
    *   [Custom Policies](https://docs.python.org/3/library/asyncio-policy.html#custom-policies)
        

#### Previous topic

[Transports and Protocols](https://docs.python.org/3/library/asyncio-protocol.html "previous chapter")

#### Next topic

[Platform Support](https://docs.python.org/3/library/asyncio-platforms.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Policies&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fasyncio-policy.html&pagesource=library%2Fasyncio-policy.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/asyncio-policy.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-platforms.html "Platform Support")
     |
*   [previous](https://docs.python.org/3/library/asyncio-protocol.html "Transports and Protocols")
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
*   [Policies](https://docs.python.org/3/library/asyncio-policy.html)
    
*    
    
    |
*   Theme Auto Light Dark |