### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/index.html "The Python standard library")
     |
*   [previous](https://docs.python.org/3/builtins/threadsafety.html "Thread Safety Guarantees")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python built-ins reference](https://docs.python.org/3/builtins/index.html)
     »
*   [Time complexity of operations on built-in types](https://docs.python.org/3/builtins/time-complexity.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Time complexity of operations on built-in types[¶](https://docs.python.org/3/builtins/time-complexity.html#time-complexity-of-operations-on-built-in-types "Link to this heading")

===================================================================================================================================================================================

This page documents the time complexity of various operations on built-in types in CPython. Other Python implementations may have different performance characteristics. Additionally, the listed costs assume exact built-in types, as instances of subclasses may have different costs.

We use [Big _O_ notation](https://en.wikipedia.org/wiki/Big_O_notation)
 to describe how the running time of an operation grows with the size of its inputs. Unless stated otherwise, _n_ denotes the number of elements currently in the container, and _k_ is the value of a numeric parameter, such as an index or a repeat count.

`list`[¶](https://docs.python.org/3/builtins/time-complexity.html#list "Link to this heading")

-----------------------------------------------------------------------------------------------

Lists are mutable sequences; for more detail on the implementation see [How are lists implemented in CPython?](https://docs.python.org/3/faq/design.html#how-are-lists-implemented)
. The largest costs come from growing beyond the current allocation size (because everything must move), or from inserting or deleting somewhere near the beginning (because everything after that must move). If you need to add or remove at both ends, consider using a [`collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque "collections.deque")
 instead.

| Operation | Complexity |
| --- | --- |
| Copy (`l.copy()`) | _O_(_n_) |
| Append (`l.append(x)`) [\[1\]](https://docs.python.org/3/builtins/time-complexity.html#id54) | _O_(1) |
| Pop (`l.pop(k)`) [\[1\]](https://docs.python.org/3/builtins/time-complexity.html#id54)<br> [\[2\]](https://docs.python.org/3/builtins/time-complexity.html#id55) | _O_(_n_ - _k_) |
| Insert (`l.insert(k, x)`) [\[1\]](https://docs.python.org/3/builtins/time-complexity.html#id54)<br> [\[2\]](https://docs.python.org/3/builtins/time-complexity.html#id55) | _O_(_n_ - _k_) |
| Get item (`l[k]`) | _O_(1) |
| Set item (`l[k] = x`) | _O_(1) |
| Delete item (`del l[k]`) [\[2\]](https://docs.python.org/3/builtins/time-complexity.html#id55) | _O_(_n_ - _k_) |
| Iteration | _O_(_n_) |
| Get slice (`l[i:j]`) | _O_(_j_ - _i_) |
| Set slice (`l[i:j] = t`) [\[1\]](https://docs.python.org/3/builtins/time-complexity.html#id54) | _O_(_j_ - _i_) if len(_t_) == _j_ - _i_, otherwise _O_(_n_ - _i_ + len(_t_)) |
| Delete slice (`del l[i:j]`) | _O_(_n_ - _i_) |
| Extend (`l.extend(t)`) [\[1\]](https://docs.python.org/3/builtins/time-complexity.html#id54)<br> [\[3\]](https://docs.python.org/3/builtins/time-complexity.html#id56) | _O_(len(_t_)) |
| Sort (`l.sort()`) [\[4\]](https://docs.python.org/3/builtins/time-complexity.html#id57) | _O_(_n_ log _n_) |
| Concatenate (`l1 + l2`) | _O_(len(_l1_) + len(_l2_)) |
| Multiply (`l * k`) | _O_(_nk_) |
| `x in l` | _O_(_n_) |
| `min(l)`, `max(l)` | _O_(_n_) |
| Get length (`len(l)`) [\[5\]](https://docs.python.org/3/builtins/time-complexity.html#id58) | _O_(1) |

`tuple`[¶](https://docs.python.org/3/builtins/time-complexity.html#tuple "Link to this heading")

-------------------------------------------------------------------------------------------------

A [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
 is an [immutable](https://docs.python.org/3/glossary.html#term-immutable)
 sequence. Because a tuple can never change, there are no insertion or deletion costs, and making a copy simply returns the same object, so is constant time (_O_(1)).

| Operation | Complexity |
| --- | --- |
| Copy (`tuple(t)`) | _O_(1) |
| Get item (`t[k]`) | _O_(1) |
| Get slice (`t[i:j]`) | _O_(_j_ - _i_) |
| Concatenate (`t1 + t2`) | _O_(len(_t1_) + len(_t2_)) |
| Multiply (`t * k`) | _O_(_nk_) |
| Iteration | _O_(_n_) |
| `x in t` | _O_(_n_) |
| `min(t)`, `max(t)` | _O_(_n_) |
| Get length (`len(t)`) [\[5\]](https://docs.python.org/3/builtins/time-complexity.html#id58) | _O_(1) |

`dict`, `frozendict`[¶](https://docs.python.org/3/builtins/time-complexity.html#dict-frozendict "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

The times listed for dict objects are average-case times, as they assume the hash function for the objects is sufficiently robust to make collisions uncommon. They also assume the keys are well-distributed among the set of possible keys. In the worst case, when every key hashes to the same value, each of the _O_(1) operations below instead takes _O_(_n_) time. They also assume that hashing and comparing a key is _O_(1). For more detail on the implementation, see [How are dictionaries implemented in CPython?](https://docs.python.org/3/faq/design.html#how-are-dictionaries-implemented)
.

A [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
 is immutable, so it does not support setting, deleting, or updating items. The other operations below apply to it at the same costs.

| Operation | Complexity |
| --- | --- |
| `key in d` | _O_(1) |
| Copy (`d.copy()`) [\[6\]](https://docs.python.org/3/builtins/time-complexity.html#id59)<br> [\[7\]](https://docs.python.org/3/builtins/time-complexity.html#id60) | _O_(_n_) |
| Get item (`d[key]`, `d.get(key)`) | _O_(1) |
| Set item (`d[key] = value`) [\[1\]](https://docs.python.org/3/builtins/time-complexity.html#id54) | _O_(1) |
| Delete item (`del d[key]`, `d.pop(key)`) | _O_(1) |
| Update (`d.update(t)`, `d \|= t`) [\[1\]](https://docs.python.org/3/builtins/time-complexity.html#id54)<br> [\[3\]](https://docs.python.org/3/builtins/time-complexity.html#id56)<br> [\[7\]](https://docs.python.org/3/builtins/time-complexity.html#id60) | _O_(len(_t_)) |
| Iteration [\[7\]](https://docs.python.org/3/builtins/time-complexity.html#id60) | _O_(_n_) |
| Get length (`len(d)`) [\[5\]](https://docs.python.org/3/builtins/time-complexity.html#id58) | _O_(1) |

`set`, `frozenset`[¶](https://docs.python.org/3/builtins/time-complexity.html#set-frozenset "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

See [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 as the [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
 and [`frozenset`](https://docs.python.org/3/builtins/stdtypes.html#frozenset "frozenset")
 implementations are similar, and the same caveats apply. In the worst case, _O_(1) operations instead take _O_(_n_) time, and operations that look up every element degrade accordingly.

A [`frozenset`](https://docs.python.org/3/builtins/stdtypes.html#frozenset "frozenset")
 is [immutable](https://docs.python.org/3/glossary.html#term-immutable)
, so it does not support adding, discarding, or the in-place update operations. The others below apply to it at the same costs.

| Operation | Complexity |
| --- | --- |
| `x in s` | _O_(1) |
| Copy (`s.copy()`) [\[6\]](https://docs.python.org/3/builtins/time-complexity.html#id59)<br> [\[7\]](https://docs.python.org/3/builtins/time-complexity.html#id60) | _O_(_n_) |
| Add (`s.add(x)`) [\[1\]](https://docs.python.org/3/builtins/time-complexity.html#id54) | _O_(1) |
| Discard (`s.discard(x)`, `s.remove(x)`) | _O_(1) |
| Union (`s1 \| s2`, `s1.union(s2)`) [\[7\]](https://docs.python.org/3/builtins/time-complexity.html#id60) | _O_(len(_s1_) + len(_s2_)) |
| Update (`s1 \|= s2`, `s1.update(s2)`) [\[1\]](https://docs.python.org/3/builtins/time-complexity.html#id54)<br> [\[7\]](https://docs.python.org/3/builtins/time-complexity.html#id60) | _O_(len(_s2_)) |
| Intersection (`s1 & s2`, `s1.intersection(s2)`) [\[7\]](https://docs.python.org/3/builtins/time-complexity.html#id60)<br> [\[8\]](https://docs.python.org/3/builtins/time-complexity.html#id61) | _O_(min(len(_s1_), len(_s2_))) |
| Intersection update (`s1 &= s2`, `s1.intersection_update(s2)`) [\[1\]](https://docs.python.org/3/builtins/time-complexity.html#id54)<br> [\[7\]](https://docs.python.org/3/builtins/time-complexity.html#id60)<br> [\[8\]](https://docs.python.org/3/builtins/time-complexity.html#id61) | _O_(min(len(_s1_), len(_s2_))) |
| Difference (`s1 - s2`, `s1.difference(s2)`) [\[7\]](https://docs.python.org/3/builtins/time-complexity.html#id60)<br> [\[9\]](https://docs.python.org/3/builtins/time-complexity.html#id62) | _O_(len(_s1_)) |
| Difference update (`s1 -= s2`, `s1.difference_update(s2)`) [\[1\]](https://docs.python.org/3/builtins/time-complexity.html#id54)<br> [\[7\]](https://docs.python.org/3/builtins/time-complexity.html#id60)<br> [\[8\]](https://docs.python.org/3/builtins/time-complexity.html#id61) | _O_(min(len(_s1_), len(_s2_))) |
| Symmetric difference (`s1 ^ s2`, `s1.symmetric_difference(s2)`) [\[7\]](https://docs.python.org/3/builtins/time-complexity.html#id60) | _O_(len(_s1_) + len(_s2_)) |
| Symmetric difference update (`s1 ^= s2`, `s1.symmetric_difference_update(s2)`) [\[1\]](https://docs.python.org/3/builtins/time-complexity.html#id54)<br> [\[7\]](https://docs.python.org/3/builtins/time-complexity.html#id60) | _O_(len(_s2_)) |
| Get length (`len(s)`) [\[5\]](https://docs.python.org/3/builtins/time-complexity.html#id58) | _O_(1) |

`str`, `bytes`, `bytearray`[¶](https://docs.python.org/3/builtins/time-complexity.html#str-bytes-bytearray "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

[`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 and [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 objects are immutable sequences of characters and bytes, respectively. As with tuples, copying one returns the original object. A [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
 is mutable, and additionally supports the mutating operations of [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
 (except `sort()`), at the same costs. However, deleting at the front with `del` (`del b[0]`, `del b[:k]`) only advances the start of the buffer instead of moving the remaining bytes, and is amortized _O_(1).

| Operation | Complexity |
| --- | --- |
| Get item (`s[k]`) | _O_(1) |
| Get slice (`s[i:j]`) | _O_(_j_ - _i_) |
| Concatenate (`s + t`) [\[10\]](https://docs.python.org/3/builtins/time-complexity.html#id63) | _O_(len(_s_) + len(_t_)) |
| Multiply (`s * k`) | _O_(_nk_) |
| Substring search (`x in s`, `s.find(x)`, `s.index(x)`) [\[11\]](https://docs.python.org/3/builtins/time-complexity.html#id64) | _O_(_n_) |
| Reverse substring search (`s.rfind(x)`, `s.rindex(x)`) [\[11\]](https://docs.python.org/3/builtins/time-complexity.html#id64)<br> [\[12\]](https://docs.python.org/3/builtins/time-complexity.html#id65) | _O_(_n_ × len(_x_)) |
| Encode or decode [\[13\]](https://docs.python.org/3/builtins/time-complexity.html#id66) | _O_(_n_) |
| Iteration | _O_(_n_) |
| Get length (`len(s)`) [\[5\]](https://docs.python.org/3/builtins/time-complexity.html#id58) | _O_(1) |

`memoryview`[¶](https://docs.python.org/3/builtins/time-complexity.html#memoryview "Link to this heading")

-----------------------------------------------------------------------------------------------------------

[`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
 objects allow Python code to access the internal data of an object that supports the [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects)
 without copying. In particular, slicing a memory view returns a new view onto the same buffer.

| Operation | Complexity |
| --- | --- |
| Create (`memoryview(obj)`) | _O_(1) |
| Get item (`v[k]`) | _O_(1) |
| Get slice (`v[i:j]`) | _O_(1) |
| Index (`v.index(x)`) [\[11\]](https://docs.python.org/3/builtins/time-complexity.html#id64)<br> [\[14\]](https://docs.python.org/3/builtins/time-complexity.html#id67) | _O_(_n_) |
| Count (`v.count(x)`) [\[14\]](https://docs.python.org/3/builtins/time-complexity.html#id67) | _O_(_n_) |
| Convert to bytes (`v.tobytes()`, `bytes(v)`) | _O_(_n_) |
| Get length (`len(v)`) [\[5\]](https://docs.python.org/3/builtins/time-complexity.html#id58) | _O_(1) |

`range`[¶](https://docs.python.org/3/builtins/time-complexity.html#range "Link to this heading")

-------------------------------------------------------------------------------------------------

A [`range`](https://docs.python.org/3/builtins/stdtypes.html#range "range")
 object computes its items on demand from its _start_, _stop_ and _step_ values, so most operations do not depend on the length of the range.

| Operation | Complexity |
| --- | --- |
| Get item (`r[k]`) | _O_(1) |
| Get slice (`r[i:j]`) | _O_(1) |
| `x in r` [\[15\]](https://docs.python.org/3/builtins/time-complexity.html#id68) | _O_(1) |
| Index and count (`r.index(x)`, `r.count(x)`) [\[15\]](https://docs.python.org/3/builtins/time-complexity.html#id68) | _O_(1) |
| Iteration | _O_(_n_) |
| `min(r)`, `max(r)` | _O_(_n_) |
| Get length (`len(r)`) [\[5\]](https://docs.python.org/3/builtins/time-complexity.html#id58) | _O_(1) |

Notes[¶](https://docs.python.org/3/builtins/time-complexity.html#notes "Link to this heading")

-----------------------------------------------------------------------------------------------

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Time complexity of operations on built-in types](https://docs.python.org/3/builtins/time-complexity.html#)
    *   [`list`](https://docs.python.org/3/builtins/time-complexity.html#list)
        
    *   [`tuple`](https://docs.python.org/3/builtins/time-complexity.html#tuple)
        
    *   [`dict`, `frozendict`](https://docs.python.org/3/builtins/time-complexity.html#dict-frozendict)
        
    *   [`set`, `frozenset`](https://docs.python.org/3/builtins/time-complexity.html#set-frozenset)
        
    *   [`str`, `bytes`, `bytearray`](https://docs.python.org/3/builtins/time-complexity.html#str-bytes-bytearray)
        
    *   [`memoryview`](https://docs.python.org/3/builtins/time-complexity.html#memoryview)
        
    *   [`range`](https://docs.python.org/3/builtins/time-complexity.html#range)
        
    *   [Notes](https://docs.python.org/3/builtins/time-complexity.html#notes)
        

#### Previous topic

[Thread Safety Guarantees](https://docs.python.org/3/builtins/threadsafety.html "previous chapter")

#### Next topic

[The Python standard library](https://docs.python.org/3/library/index.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Time+complexity+of+operations+on+built-in+types&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fbuiltins%2Ftime-complexity.html&pagesource=builtins%2Ftime-complexity.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/builtins/time-complexity.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/index.html "The Python standard library")
     |
*   [previous](https://docs.python.org/3/builtins/threadsafety.html "Thread Safety Guarantees")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python built-ins reference](https://docs.python.org/3/builtins/index.html)
     »
*   [Time complexity of operations on built-in types](https://docs.python.org/3/builtins/time-complexity.html)
    
*    
    
    |
*   Theme Auto Light Dark |