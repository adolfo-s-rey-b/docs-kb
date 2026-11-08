### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/gcsupport.html "Supporting Cyclic Garbage Collection")
     |
*   [previous](https://docs.python.org/3/c-api/structures.html "Common Object Structures")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Object Implementation Support](https://docs.python.org/3/c-api/objimpl.html)
     »
*   [Type Object Structures](https://docs.python.org/3/c-api/typeobj.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Type Object Structures[¶](https://docs.python.org/3/c-api/typeobj.html#type-object-structures "Link to this heading")

======================================================================================================================

Perhaps one of the most important structures of the Python object system is the structure that defines a new type: the [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 structure. Type objects can be handled using any of the `PyObject_*` or `PyType_*` functions, but do not offer much that’s interesting to most Python applications. These objects are fundamental to how objects behave, so they are very important to the interpreter itself and to any extension module that implements new types.

Type objects are fairly large compared to most of the standard types. The reason for the size is that each type object stores a large number of values, mostly C function pointers, each of which implements a small part of the type’s functionality. The fields of the type object are examined in detail in this section. The fields will be described in the order in which they occur in the structure.

In addition to the following quick reference, the [Examples](https://docs.python.org/3/c-api/typeobj.html#typedef-examples)
 section provides at-a-glance insight into the meaning and use of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.

Quick Reference[¶](https://docs.python.org/3/c-api/typeobj.html#quick-reference "Link to this heading")

--------------------------------------------------------------------------------------------------------

### “tp slots”[¶](https://docs.python.org/3/c-api/typeobj.html#tp-slots "Link to this heading")

      
| PyTypeObject Slot [\[1\]](https://docs.python.org/3/c-api/typeobj.html#slots) | [Type](https://docs.python.org/3/c-api/typeobj.html#slot-typedefs-table) | special methods/attrs | Info [\[2\]](https://docs.python.org/3/c-api/typeobj.html#cols) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| O   | T   | D   | I   |
| --- | --- | --- | --- | --- | --- | --- |
| <R> [`tp_name`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_name "PyTypeObject.tp_name") | const char \* | \_\_name\_\_ | X   | X   |     |     |
| [`tp_basicsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_basicsize "PyTypeObject.tp_basicsize") | [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t") |     | X   | X   |     | X   |
| [`tp_itemsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_itemsize "PyTypeObject.tp_itemsize") | [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t") |     |     | X   |     | X   |
| [`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc") | [`destructor`](https://docs.python.org/3/c-api/typeobj.html#c.destructor "destructor") |     | X   | X   |     | X   |
| [`tp_vectorcall_offset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_vectorcall_offset "PyTypeObject.tp_vectorcall_offset") | [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t") |     |     | X   |     | X   |
| ([`tp_getattr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getattr "PyTypeObject.tp_getattr")<br>) | [`getattrfunc`](https://docs.python.org/3/c-api/typeobj.html#c.getattrfunc "getattrfunc") | \_\_getattribute\_\_, \_\_getattr\_\_ |     |     |     | G   |
| ([`tp_setattr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_setattr "PyTypeObject.tp_setattr")<br>) | [`setattrfunc`](https://docs.python.org/3/c-api/typeobj.html#c.setattrfunc "setattrfunc") | \_\_setattr\_\_, \_\_delattr\_\_ |     |     |     | G   |
| [`tp_as_async`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_async "PyTypeObject.tp_as_async") | [`PyAsyncMethods`](https://docs.python.org/3/c-api/typeobj.html#c.PyAsyncMethods "PyAsyncMethods")<br> \* | [sub-slots](https://docs.python.org/3/c-api/typeobj.html#sub-slots) |     |     |     | %   |
| [`tp_repr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_repr "PyTypeObject.tp_repr") | [`reprfunc`](https://docs.python.org/3/c-api/typeobj.html#c.reprfunc "reprfunc") | \_\_repr\_\_ | X   | X   |     | X   |
| [`tp_as_number`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_number "PyTypeObject.tp_as_number") | [`PyNumberMethods`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")<br> \* | [sub-slots](https://docs.python.org/3/c-api/typeobj.html#sub-slots) |     |     |     | %   |
| [`tp_as_sequence`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_sequence "PyTypeObject.tp_as_sequence") | [`PySequenceMethods`](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods "PySequenceMethods")<br> \* | [sub-slots](https://docs.python.org/3/c-api/typeobj.html#sub-slots) |     |     |     | %   |
| [`tp_as_mapping`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_mapping "PyTypeObject.tp_as_mapping") | [`PyMappingMethods`](https://docs.python.org/3/c-api/typeobj.html#c.PyMappingMethods "PyMappingMethods")<br> \* | [sub-slots](https://docs.python.org/3/c-api/typeobj.html#sub-slots) |     |     |     | %   |
| [`tp_hash`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_hash "PyTypeObject.tp_hash") | [`hashfunc`](https://docs.python.org/3/c-api/typeobj.html#c.hashfunc "hashfunc") | \_\_hash\_\_ | X   |     |     | G   |
| [`tp_call`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_call "PyTypeObject.tp_call") | [`ternaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.ternaryfunc "ternaryfunc") | \_\_call\_\_ |     | X   |     | X   |
| [`tp_str`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_str "PyTypeObject.tp_str") | [`reprfunc`](https://docs.python.org/3/c-api/typeobj.html#c.reprfunc "reprfunc") | \_\_str\_\_ | X   |     |     | X   |
| [`tp_getattro`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getattro "PyTypeObject.tp_getattro") | [`getattrofunc`](https://docs.python.org/3/c-api/typeobj.html#c.getattrofunc "getattrofunc") | \_\_getattribute\_\_, \_\_getattr\_\_ | X   | X   |     | G   |
| [`tp_setattro`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_setattro "PyTypeObject.tp_setattro") | [`setattrofunc`](https://docs.python.org/3/c-api/typeobj.html#c.setattrofunc "setattrofunc") | \_\_setattr\_\_, \_\_delattr\_\_ | X   | X   |     | G   |
| [`tp_as_buffer`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_buffer "PyTypeObject.tp_as_buffer") | [`PyBufferProcs`](https://docs.python.org/3/c-api/typeobj.html#c.PyBufferProcs "PyBufferProcs")<br> \* | [sub-slots](https://docs.python.org/3/c-api/typeobj.html#sub-slots) |     |     |     | %   |
| [`tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags") | unsigned long |     | X   | X   |     | ?   |
| [`tp_doc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_doc "PyTypeObject.tp_doc") | const char \* | \_\_doc\_\_ | X   | X   |     |     |
| [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse") | [`traverseproc`](https://docs.python.org/3/c-api/gcsupport.html#c.traverseproc "traverseproc") |     |     | X   |     | G   |
| [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear") | [`inquiry`](https://docs.python.org/3/c-api/gcsupport.html#c.inquiry "inquiry") |     |     | X   |     | G   |
| [`tp_richcompare`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_richcompare "PyTypeObject.tp_richcompare") | [`richcmpfunc`](https://docs.python.org/3/c-api/typeobj.html#c.richcmpfunc "richcmpfunc") | \_\_lt\_\_, \_\_le\_\_, \_\_eq\_\_, \_\_ne\_\_, \_\_gt\_\_, \_\_ge\_\_ | X   |     |     | G   |
| ([`tp_weaklistoffset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_weaklistoffset "PyTypeObject.tp_weaklistoffset")<br>) | [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t") |     |     | X   |     | ?   |
| [`tp_iter`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_iter "PyTypeObject.tp_iter") | [`getiterfunc`](https://docs.python.org/3/c-api/typeobj.html#c.getiterfunc "getiterfunc") | \_\_iter\_\_ |     |     |     | X   |
| [`tp_iternext`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_iternext "PyTypeObject.tp_iternext") | [`iternextfunc`](https://docs.python.org/3/c-api/typeobj.html#c.iternextfunc "iternextfunc") | \_\_next\_\_ |     |     |     | X   |
| [`tp_methods`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_methods "PyTypeObject.tp_methods") | [`PyMethodDef`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")<br> \[\] |     | X   | X   |     |     |
| [`tp_members`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_members "PyTypeObject.tp_members") | [`PyMemberDef`](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef "PyMemberDef")<br> \[\] |     |     | X   |     |     |
| [`tp_getset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getset "PyTypeObject.tp_getset") | [`PyGetSetDef`](https://docs.python.org/3/c-api/structures.html#c.PyGetSetDef "PyGetSetDef")<br> \[\] |     | X   | X   |     |     |
| [`tp_base`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_base "PyTypeObject.tp_base") | [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")<br> \* | \_\_base\_\_ |     |     | X   |     |
| [`tp_dict`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dict "PyTypeObject.tp_dict") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | \_\_dict\_\_ |     |     | ?   |     |
| [`tp_descr_get`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_descr_get "PyTypeObject.tp_descr_get") | [`descrgetfunc`](https://docs.python.org/3/c-api/typeobj.html#c.descrgetfunc "descrgetfunc") | \_\_get\_\_ |     |     |     | X   |
| [`tp_descr_set`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_descr_set "PyTypeObject.tp_descr_set") | [`descrsetfunc`](https://docs.python.org/3/c-api/typeobj.html#c.descrsetfunc "descrsetfunc") | \_\_set\_\_, \_\_delete\_\_ |     |     |     | X   |
| ([`tp_dictoffset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dictoffset "PyTypeObject.tp_dictoffset")<br>) | [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t") |     |     | X   |     | ?   |
| [`tp_init`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_init "PyTypeObject.tp_init") | [`initproc`](https://docs.python.org/3/c-api/typeobj.html#c.initproc "initproc") | \_\_init\_\_ | X   | X   |     | X   |
| [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc") | [`allocfunc`](https://docs.python.org/3/c-api/typeobj.html#c.allocfunc "allocfunc") |     | X   |     | ?   | ?   |
| [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new") | [`newfunc`](https://docs.python.org/3/c-api/typeobj.html#c.newfunc "newfunc") | \_\_new\_\_ | X   | X   | ?   | ?   |
| [`tp_free`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_free "PyTypeObject.tp_free") | [`freefunc`](https://docs.python.org/3/c-api/typeobj.html#c.freefunc "freefunc") |     | X   | X   | ?   | ?   |
| [`tp_is_gc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_is_gc "PyTypeObject.tp_is_gc") | [`inquiry`](https://docs.python.org/3/c-api/gcsupport.html#c.inquiry "inquiry") |     |     | X   |     | X   |
| <[`tp_bases`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_bases "PyTypeObject.tp_bases")<br>\> | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | \_\_bases\_\_ |     |     | ~   |     |
| <[`tp_mro`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_mro "PyTypeObject.tp_mro")<br>\> | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | \_\_mro\_\_ |     |     | ~   |     |
| \[[`tp_cache`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_cache "PyTypeObject.tp_cache")<br>\] | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* |     |     |     |     |     |
| \[[`tp_subclasses`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_subclasses "PyTypeObject.tp_subclasses")<br>\] | void \* | \_\_subclasses\_\_ |     |     |     |     |
| \[[`tp_weaklist`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_weaklist "PyTypeObject.tp_weaklist")<br>\] | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* |     |     |     |     |     |
| ([`tp_del`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_del "PyTypeObject.tp_del")<br>) | [`destructor`](https://docs.python.org/3/c-api/typeobj.html#c.destructor "destructor") |     |     |     |     |     |
| \[[`tp_version_tag`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_version_tag "PyTypeObject.tp_version_tag")<br>\] | unsigned int |     |     |     |     |     |
| [`tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "PyTypeObject.tp_finalize") | [`destructor`](https://docs.python.org/3/c-api/typeobj.html#c.destructor "destructor") | \_\_del\_\_ |     |     |     | X   |
| [`tp_vectorcall`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_vectorcall "PyTypeObject.tp_vectorcall") | [`vectorcallfunc`](https://docs.python.org/3/c-api/call.html#c.vectorcallfunc "vectorcallfunc") |     |     |     |     |     |
| \[[`tp_watched`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_watched "PyTypeObject.tp_watched")<br>\] | unsigned char |     |     |     |     |     |

### sub-slots[¶](https://docs.python.org/3/c-api/typeobj.html#sub-slots "Link to this heading")

  
| Slot | [Type](https://docs.python.org/3/c-api/typeobj.html#slot-typedefs-table) | special methods |
| --- | --- | --- |
| [`am_await`](https://docs.python.org/3/c-api/typeobj.html#c.PyAsyncMethods.am_await "PyAsyncMethods.am_await") | [`unaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc") | \_\_await\_\_ |
| [`am_aiter`](https://docs.python.org/3/c-api/typeobj.html#c.PyAsyncMethods.am_aiter "PyAsyncMethods.am_aiter") | [`unaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc") | \_\_aiter\_\_ |
| [`am_anext`](https://docs.python.org/3/c-api/typeobj.html#c.PyAsyncMethods.am_anext "PyAsyncMethods.am_anext") | [`unaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc") | \_\_anext\_\_ |
| [`am_send`](https://docs.python.org/3/c-api/typeobj.html#c.PyAsyncMethods.am_send "PyAsyncMethods.am_send") | [`sendfunc`](https://docs.python.org/3/c-api/typeobj.html#c.sendfunc "sendfunc") |     |
|     |     |     |
| [`nb_add`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_add "PyNumberMethods.nb_add") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_add\_\_ \_\_radd\_\_ |
| [`nb_inplace_add`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_add "PyNumberMethods.nb_inplace_add") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_iadd\_\_ |
| [`nb_subtract`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_subtract "PyNumberMethods.nb_subtract") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_sub\_\_ \_\_rsub\_\_ |
| [`nb_inplace_subtract`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_subtract "PyNumberMethods.nb_inplace_subtract") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_isub\_\_ |
| [`nb_multiply`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_multiply "PyNumberMethods.nb_multiply") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_mul\_\_ \_\_rmul\_\_ |
| [`nb_inplace_multiply`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_multiply "PyNumberMethods.nb_inplace_multiply") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_imul\_\_ |
| [`nb_remainder`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_remainder "PyNumberMethods.nb_remainder") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_mod\_\_ \_\_rmod\_\_ |
| [`nb_inplace_remainder`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_remainder "PyNumberMethods.nb_inplace_remainder") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_imod\_\_ |
| [`nb_divmod`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_divmod "PyNumberMethods.nb_divmod") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_divmod\_\_ \_\_rdivmod\_\_ |
| [`nb_power`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_power "PyNumberMethods.nb_power") | [`ternaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.ternaryfunc "ternaryfunc") | \_\_pow\_\_ \_\_rpow\_\_ |
| [`nb_inplace_power`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_power "PyNumberMethods.nb_inplace_power") | [`ternaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.ternaryfunc "ternaryfunc") | \_\_ipow\_\_ |
| [`nb_negative`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_negative "PyNumberMethods.nb_negative") | [`unaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc") | \_\_neg\_\_ |
| [`nb_positive`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_positive "PyNumberMethods.nb_positive") | [`unaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc") | \_\_pos\_\_ |
| [`nb_absolute`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_absolute "PyNumberMethods.nb_absolute") | [`unaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc") | \_\_abs\_\_ |
| [`nb_bool`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_bool "PyNumberMethods.nb_bool") | [`inquiry`](https://docs.python.org/3/c-api/gcsupport.html#c.inquiry "inquiry") | \_\_bool\_\_ |
| [`nb_invert`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_invert "PyNumberMethods.nb_invert") | [`unaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc") | \_\_invert\_\_ |
| [`nb_lshift`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_lshift "PyNumberMethods.nb_lshift") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_lshift\_\_ \_\_rlshift\_\_ |
| [`nb_inplace_lshift`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_lshift "PyNumberMethods.nb_inplace_lshift") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_ilshift\_\_ |
| [`nb_rshift`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_rshift "PyNumberMethods.nb_rshift") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_rshift\_\_ \_\_rrshift\_\_ |
| [`nb_inplace_rshift`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_rshift "PyNumberMethods.nb_inplace_rshift") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_irshift\_\_ |
| [`nb_and`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_and "PyNumberMethods.nb_and") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_and\_\_ \_\_rand\_\_ |
| [`nb_inplace_and`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_and "PyNumberMethods.nb_inplace_and") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_iand\_\_ |
| [`nb_xor`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_xor "PyNumberMethods.nb_xor") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_xor\_\_ \_\_rxor\_\_ |
| [`nb_inplace_xor`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_xor "PyNumberMethods.nb_inplace_xor") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_ixor\_\_ |
| [`nb_or`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_or "PyNumberMethods.nb_or") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_or\_\_ \_\_ror\_\_ |
| [`nb_inplace_or`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_or "PyNumberMethods.nb_inplace_or") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_ior\_\_ |
| [`nb_int`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_int "PyNumberMethods.nb_int") | [`unaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc") | \_\_int\_\_ |
| [`nb_reserved`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_reserved "PyNumberMethods.nb_reserved") | void \* |     |
| [`nb_float`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_float "PyNumberMethods.nb_float") | [`unaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc") | \_\_float\_\_ |
| [`nb_floor_divide`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_floor_divide "PyNumberMethods.nb_floor_divide") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_floordiv\_\_ |
| [`nb_inplace_floor_divide`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_floor_divide "PyNumberMethods.nb_inplace_floor_divide") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_ifloordiv\_\_ |
| [`nb_true_divide`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_true_divide "PyNumberMethods.nb_true_divide") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_truediv\_\_ |
| [`nb_inplace_true_divide`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_true_divide "PyNumberMethods.nb_inplace_true_divide") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_itruediv\_\_ |
| [`nb_index`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_index "PyNumberMethods.nb_index") | [`unaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc") | \_\_index\_\_ |
| [`nb_matrix_multiply`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_matrix_multiply "PyNumberMethods.nb_matrix_multiply") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_matmul\_\_ \_\_rmatmul\_\_ |
| [`nb_inplace_matrix_multiply`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_matrix_multiply "PyNumberMethods.nb_inplace_matrix_multiply") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_imatmul\_\_ |
|     |     |     |
| [`mp_length`](https://docs.python.org/3/c-api/typeobj.html#c.PyMappingMethods.mp_length "PyMappingMethods.mp_length") | [`lenfunc`](https://docs.python.org/3/c-api/typeobj.html#c.lenfunc "lenfunc") | \_\_len\_\_ |
| [`mp_subscript`](https://docs.python.org/3/c-api/typeobj.html#c.PyMappingMethods.mp_subscript "PyMappingMethods.mp_subscript") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_getitem\_\_ |
| [`mp_ass_subscript`](https://docs.python.org/3/c-api/typeobj.html#c.PyMappingMethods.mp_ass_subscript "PyMappingMethods.mp_ass_subscript") | [`objobjargproc`](https://docs.python.org/3/c-api/typeobj.html#c.objobjargproc "objobjargproc") | \_\_setitem\_\_, \_\_delitem\_\_ |
|     |     |     |
| [`sq_length`](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods.sq_length "PySequenceMethods.sq_length") | [`lenfunc`](https://docs.python.org/3/c-api/typeobj.html#c.lenfunc "lenfunc") | \_\_len\_\_ |
| [`sq_concat`](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods.sq_concat "PySequenceMethods.sq_concat") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_add\_\_ |
| [`sq_repeat`](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods.sq_repeat "PySequenceMethods.sq_repeat") | [`ssizeargfunc`](https://docs.python.org/3/c-api/typeobj.html#c.ssizeargfunc "ssizeargfunc") | \_\_mul\_\_ |
| [`sq_item`](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods.sq_item "PySequenceMethods.sq_item") | [`ssizeargfunc`](https://docs.python.org/3/c-api/typeobj.html#c.ssizeargfunc "ssizeargfunc") | \_\_getitem\_\_ |
| [`sq_ass_item`](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods.sq_ass_item "PySequenceMethods.sq_ass_item") | [`ssizeobjargproc`](https://docs.python.org/3/c-api/typeobj.html#c.ssizeobjargproc "ssizeobjargproc") | \_\_setitem\_\_ \_\_delitem\_\_ |
| [`sq_contains`](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods.sq_contains "PySequenceMethods.sq_contains") | [`objobjproc`](https://docs.python.org/3/c-api/typeobj.html#c.objobjproc "objobjproc") | \_\_contains\_\_ |
| [`sq_inplace_concat`](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods.sq_inplace_concat "PySequenceMethods.sq_inplace_concat") | [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | \_\_iadd\_\_ |
| [`sq_inplace_repeat`](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods.sq_inplace_repeat "PySequenceMethods.sq_inplace_repeat") | [`ssizeargfunc`](https://docs.python.org/3/c-api/typeobj.html#c.ssizeargfunc "ssizeargfunc") | \_\_imul\_\_ |
|     |     |     |
| [`bf_getbuffer`](https://docs.python.org/3/c-api/typeobj.html#c.PyBufferProcs.bf_getbuffer "PyBufferProcs.bf_getbuffer") | [`getbufferproc()`](https://docs.python.org/3/c-api/typeobj.html#c.getbufferproc "getbufferproc") | \_\_buffer\_\_ |
| [`bf_releasebuffer`](https://docs.python.org/3/c-api/typeobj.html#c.PyBufferProcs.bf_releasebuffer "PyBufferProcs.bf_releasebuffer") | [`releasebufferproc()`](https://docs.python.org/3/c-api/typeobj.html#c.releasebufferproc "releasebufferproc") | \_\_release\_buffer\_\_ |

### slot typedefs[¶](https://docs.python.org/3/c-api/typeobj.html#slot-typedefs "Link to this heading")

| typedef | Parameter Types | Return Type |
| --- | --- | --- |
| [`allocfunc`](https://docs.python.org/3/c-api/typeobj.html#c.allocfunc "allocfunc") | [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")<br> \*<br><br>[`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* |
| [`destructor`](https://docs.python.org/3/c-api/typeobj.html#c.destructor "destructor") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | void |
| [`freefunc`](https://docs.python.org/3/c-api/typeobj.html#c.freefunc "freefunc") | void \* | void |
| [`traverseproc`](https://docs.python.org/3/c-api/gcsupport.html#c.traverseproc "traverseproc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`visitproc`](https://docs.python.org/3/c-api/gcsupport.html#c.visitproc "visitproc")<br><br>void \* | int |
| [`newfunc`](https://docs.python.org/3/c-api/typeobj.html#c.newfunc "newfunc") | [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")<br> \*<br><br>[`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* |
| [`initproc`](https://docs.python.org/3/c-api/typeobj.html#c.initproc "initproc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | int |
| [`reprfunc`](https://docs.python.org/3/c-api/typeobj.html#c.reprfunc "reprfunc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* |
| [`getattrfunc`](https://docs.python.org/3/c-api/typeobj.html#c.getattrfunc "getattrfunc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>const char \* | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* |
| [`setattrfunc`](https://docs.python.org/3/c-api/typeobj.html#c.setattrfunc "setattrfunc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>const char \*<br><br>[`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | int |
| [`getattrofunc`](https://docs.python.org/3/c-api/typeobj.html#c.getattrofunc "getattrofunc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* |
| [`setattrofunc`](https://docs.python.org/3/c-api/typeobj.html#c.setattrofunc "setattrofunc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | int |
| [`descrgetfunc`](https://docs.python.org/3/c-api/typeobj.html#c.descrgetfunc "descrgetfunc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* |
| [`descrsetfunc`](https://docs.python.org/3/c-api/typeobj.html#c.descrsetfunc "descrsetfunc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | int |
| [`hashfunc`](https://docs.python.org/3/c-api/typeobj.html#c.hashfunc "hashfunc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | Py\_hash\_t |
| [`richcmpfunc`](https://docs.python.org/3/c-api/typeobj.html#c.richcmpfunc "richcmpfunc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>int | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* |
| [`getiterfunc`](https://docs.python.org/3/c-api/typeobj.html#c.getiterfunc "getiterfunc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* |
| [`iternextfunc`](https://docs.python.org/3/c-api/typeobj.html#c.iternextfunc "iternextfunc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* |
| [`lenfunc`](https://docs.python.org/3/c-api/typeobj.html#c.lenfunc "lenfunc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t") |
| [`getbufferproc`](https://docs.python.org/3/c-api/typeobj.html#c.getbufferproc "getbufferproc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`Py_buffer`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")<br> \*<br><br>int | int |
| [`releasebufferproc`](https://docs.python.org/3/c-api/typeobj.html#c.releasebufferproc "releasebufferproc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`Py_buffer`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")<br> \* | void |
| [`inquiry`](https://docs.python.org/3/c-api/gcsupport.html#c.inquiry "inquiry") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | int |
| [`unaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* |
| [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* |
| [`ternaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.ternaryfunc "ternaryfunc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* |
| [`ssizeargfunc`](https://docs.python.org/3/c-api/typeobj.html#c.ssizeargfunc "ssizeargfunc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* |
| [`ssizeobjargproc`](https://docs.python.org/3/c-api/typeobj.html#c.ssizeobjargproc "ssizeobjargproc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")<br><br>[`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | int |
| [`objobjproc`](https://docs.python.org/3/c-api/typeobj.html#c.objobjproc "objobjproc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | int |
| [`objobjargproc`](https://docs.python.org/3/c-api/typeobj.html#c.objobjargproc "objobjargproc") | [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*<br><br>[`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \* | int |

See [Slot Type typedefs](https://docs.python.org/3/c-api/typeobj.html#id6)
 below for more detail.

PyTypeObject Definition[¶](https://docs.python.org/3/c-api/typeobj.html#pytypeobject-definition "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

The structure definition for [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 can be found in `Include/cpython/object.h`. For convenience of reference, this repeats the definition found there:

typedef struct \_typeobject {
    PyObject\_VAR\_HEAD
    const char \*tp\_name; /\* For printing, in format "<module>.<name>" \*/
    Py\_ssize\_t tp\_basicsize, tp\_itemsize; /\* For allocation \*/

    /\* Methods to implement standard operations \*/

    destructor tp\_dealloc;
    Py\_ssize\_t tp\_vectorcall\_offset;
    getattrfunc tp\_getattr;
    setattrfunc tp\_setattr;
    PyAsyncMethods \*tp\_as\_async; /\* formerly known as tp\_compare (Python 2)
                                    or tp\_reserved (Python 3) \*/
    reprfunc tp\_repr;

    /\* Method suites for standard classes \*/

    PyNumberMethods \*tp\_as\_number;
    PySequenceMethods \*tp\_as\_sequence;
    PyMappingMethods \*tp\_as\_mapping;

    /\* More standard operations (here for binary compatibility) \*/

    hashfunc tp\_hash;
    ternaryfunc tp\_call;
    reprfunc tp\_str;
    getattrofunc tp\_getattro;
    setattrofunc tp\_setattro;

    /\* Functions to access object as input/output buffer \*/
    PyBufferProcs \*tp\_as\_buffer;

    /\* Flags to define presence of optional/expanded features \*/
    unsigned long tp\_flags;

    const char \*tp\_doc; /\* Documentation string \*/

    /\* Assigned meaning in release 2.0 \*/
    /\* call function for all accessible objects \*/
    traverseproc tp\_traverse;

    /\* delete references to contained objects \*/
    inquiry tp\_clear;

    /\* Assigned meaning in release 2.1 \*/
    /\* rich comparisons \*/
    richcmpfunc tp\_richcompare;

    /\* weak reference enabler \*/
    Py\_ssize\_t tp\_weaklistoffset;

    /\* Iterators \*/
    getiterfunc tp\_iter;
    iternextfunc tp\_iternext;

    /\* Attribute descriptor and subclassing stuff \*/
    PyMethodDef \*tp\_methods;
    PyMemberDef \*tp\_members;
    PyGetSetDef \*tp\_getset;
    // Strong reference on a heap type, borrowed reference on a static type
    PyTypeObject \*tp\_base;
    PyObject \*tp\_dict;
    descrgetfunc tp\_descr\_get;
    descrsetfunc tp\_descr\_set;
    Py\_ssize\_t tp\_dictoffset;
    initproc tp\_init;
    allocfunc tp\_alloc;
    newfunc tp\_new;
    freefunc tp\_free; /\* Low-level free-memory routine \*/
    inquiry tp\_is\_gc; /\* For PyObject\_IS\_GC \*/
    PyObject \*tp\_bases;
    PyObject \*tp\_mro; /\* method resolution order \*/
    PyObject \*tp\_cache; /\* no longer used \*/
    void \*tp\_subclasses;  /\* for static builtin types this is an index \*/
    PyObject \*tp\_weaklist; /\* not used for static builtin types \*/
    destructor tp\_del;

    /\* Type attribute cache version tag. Added in version 2.6.
     \* If zero, the cache is invalid and must be initialized.
     \*/
    unsigned int tp\_version\_tag;

    destructor tp\_finalize;
    vectorcallfunc tp\_vectorcall;

    /\* bitset of which type-watchers care about this type \*/
    unsigned char tp\_watched;

    /\* Number of tp\_version\_tag values used.
     \* Set to \_Py\_ATTR\_CACHE\_UNUSED if the attribute cache is
     \* disabled for this type (e.g. due to custom MRO entries).
     \* Otherwise, limited to MAX\_VERSIONS\_PER\_CLASS (defined elsewhere).
     \*/
    uint16\_t tp\_versions\_used;
} PyTypeObject;

PyObject Slots[¶](https://docs.python.org/3/c-api/typeobj.html#pyobject-slots "Link to this heading")

------------------------------------------------------------------------------------------------------

The type object structure extends the [`PyVarObject`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject "PyVarObject")
 structure. The [`ob_size`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject.ob_size "PyVarObject.ob_size")
 field is used for dynamic types (created by `type_new()`, usually called from a class statement). Note that [`PyType_Type`](https://docs.python.org/3/c-api/type.html#c.PyType_Type "PyType_Type")
 (the metatype) initializes [`tp_itemsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_itemsize "PyTypeObject.tp_itemsize")
, which means that its instances (i.e. type objects) _must_ have the `ob_size` field.

[`PyObject.ob_refcnt`](https://docs.python.org/3/c-api/structures.html#c.PyObject.ob_refcnt "PyObject.ob_refcnt")

> The type object’s reference count is initialized to `1` by the `PyObject_HEAD_INIT` macro. Note that for [statically allocated type objects](https://docs.python.org/3/c-api/typeobj.html#static-types)
> , the type’s instances (objects whose [`ob_type`](https://docs.python.org/3/c-api/structures.html#c.PyObject.ob_type "PyObject.ob_type")
>  points back to the type) do _not_ count as references. But for [dynamically allocated type objects](https://docs.python.org/3/c-api/typeobj.html#heap-types)
> , the instances _do_ count as references.
> 
> **Inheritance:**
> 
> This field is not inherited by subtypes.

[`PyObject.ob_type`](https://docs.python.org/3/c-api/structures.html#c.PyObject.ob_type "PyObject.ob_type")

> This is the type’s type, in other words its metatype. It is initialized by the argument to the `PyObject_HEAD_INIT` macro, and its value should normally be `&PyType_Type`. However, for dynamically loadable extension modules that must be usable on Windows (at least), the compiler complains that this is not a valid initializer. Therefore, the convention is to pass `NULL` to the `PyObject_HEAD_INIT` macro and to initialize this field explicitly at the start of the module’s initialization function, before doing anything else. This is typically done like this:
> 
> Foo\_Type.ob\_type \= &PyType\_Type;
> 
> This should be done before any instances of the type are created. [`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
>  checks if [`ob_type`](https://docs.python.org/3/c-api/structures.html#c.PyObject.ob_type "PyObject.ob_type")
>  is `NULL`, and if so, initializes it to the `ob_type` field of the base class. `PyType_Ready()` will not change this field if it is non-zero.
> 
> **Inheritance:**
> 
> This field is inherited by subtypes.

PyVarObject Slots[¶](https://docs.python.org/3/c-api/typeobj.html#pyvarobject-slots "Link to this heading")

------------------------------------------------------------------------------------------------------------

[`PyVarObject.ob_size`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject.ob_size "PyVarObject.ob_size")

> For [statically allocated type objects](https://docs.python.org/3/c-api/typeobj.html#static-types)
> , this should be initialized to zero. For [dynamically allocated type objects](https://docs.python.org/3/c-api/typeobj.html#heap-types)
> , this field has a special internal meaning.
> 
> This field should be accessed using the [`Py_SIZE()`](https://docs.python.org/3/c-api/structures.html#c.Py_SIZE "Py_SIZE")
>  macro.
> 
> **Inheritance:**
> 
> This field is not inherited by subtypes.

PyTypeObject Slots[¶](https://docs.python.org/3/c-api/typeobj.html#pytypeobject-slots "Link to this heading")

--------------------------------------------------------------------------------------------------------------

Each slot has a section describing inheritance. If [`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
 may set a value when the field is set to `NULL` then there will also be a “Default” section. (Note that many fields set on [`PyBaseObject_Type`](https://docs.python.org/3/c-api/structures.html#c.PyBaseObject_Type "PyBaseObject_Type")
 and [`PyType_Type`](https://docs.python.org/3/c-api/type.html#c.PyType_Type "PyType_Type")
 effectively act as defaults.)

const char \*[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_name[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_name "Link to this definition")
  

See [`Py_tp_name`](https://docs.python.org/3/c-api/type.html#c.Py_tp_name "Py_tp_name")
 for the corresponding [`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
.

Pointer to a NUL-terminated string containing the name of the type. For types that are accessible as module globals, the string should be the full module name, followed by a dot, followed by the type name; for built-in types, it should be just the type name. If the module is a submodule of a package, the full package name is part of the full module name. For example, a type named `T` defined in module `M` in subpackage `Q` in package `P` should have the [`tp_name`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_name "PyTypeObject.tp_name")
 initializer `"P.Q.M.T"`.

For [dynamically allocated type objects](https://docs.python.org/3/c-api/typeobj.html#heap-types)
, this should just be the type name, and the module name explicitly stored in the type dict as the value for key `'__module__'`.

For [statically allocated type objects](https://docs.python.org/3/c-api/typeobj.html#static-types)
, the _tp\_name_ field should contain a dot. Everything before the last dot is made accessible as the [`__module__`](https://docs.python.org/3/reference/datamodel.html#type.__module__ "type.__module__")
 attribute, and everything after the last dot is made accessible as the [`__name__`](https://docs.python.org/3/reference/datamodel.html#type.__name__ "type.__name__")
 attribute.

If no dot is present, the entire [`tp_name`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_name "PyTypeObject.tp_name")
 field is made accessible as the [`__name__`](https://docs.python.org/3/reference/datamodel.html#type.__name__ "type.__name__")
 attribute, and the [`__module__`](https://docs.python.org/3/reference/datamodel.html#type.__module__ "type.__module__")
 attribute is undefined (unless explicitly set in the dictionary, as explained above). This means your type will be impossible to pickle. Additionally, it will not be listed in module documentations created with pydoc.

This field must not be `NULL`. It is the only required field in [`PyTypeObject()`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 (other than potentially [`tp_itemsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_itemsize "PyTypeObject.tp_itemsize")
).

**Inheritance:**

This field is not inherited by subtypes.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_basicsize[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_basicsize "Link to this definition")
  

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_itemsize[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_itemsize "Link to this definition")
  

These fields allow calculating the size in bytes of instances of the type.

See [`Py_tp_basicsize`](https://docs.python.org/3/c-api/type.html#c.Py_tp_basicsize "Py_tp_basicsize")
, [`Py_tp_extra_basicsize`](https://docs.python.org/3/c-api/type.html#c.Py_tp_extra_basicsize "Py_tp_extra_basicsize")
 and [`Py_tp_itemsize`](https://docs.python.org/3/c-api/type.html#c.Py_tp_itemsize "Py_tp_itemsize")
 for the corresponding [`Slot IDs`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
.

There are two kinds of types: types with fixed-length instances have a zero `tp_itemsize` field, types with variable-length instances have a non-zero `tp_itemsize` field. For a type with fixed-length instances, all instances have the same size, given in `tp_basicsize`. (Exceptions to this rule can be made using [`PyUnstable_Object_GC_NewWithExtraData()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyUnstable_Object_GC_NewWithExtraData "PyUnstable_Object_GC_NewWithExtraData")
.)

For a type with variable-length instances, the instances must have an [`ob_size`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject.ob_size "PyVarObject.ob_size")
 field, and the instance size is `tp_basicsize` plus N times `tp_itemsize`, where N is the “length” of the object.

Functions like [`PyObject_NewVar()`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_NewVar "PyObject_NewVar")
 will take the value of N as an argument, and store in the instance’s [`ob_size`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject.ob_size "PyVarObject.ob_size")
 field. Note that the `ob_size` field may later be used for other purposes. For example, [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
 instances use the bits of `ob_size` in an implementation-defined way; the underlying storage and its size should be accessed using [`PyLong_Export()`](https://docs.python.org/3/c-api/long.html#c.PyLong_Export "PyLong_Export")
.

Note

The [`ob_size`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject.ob_size "PyVarObject.ob_size")
 field should be accessed using the [`Py_SIZE()`](https://docs.python.org/3/c-api/structures.html#c.Py_SIZE "Py_SIZE")
 and [`Py_SET_SIZE()`](https://docs.python.org/3/c-api/structures.html#c.Py_SET_SIZE "Py_SET_SIZE")
 macros.

Also, the presence of an [`ob_size`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject.ob_size "PyVarObject.ob_size")
 field in the instance layout doesn’t mean that the instance structure is variable-length. For example, the [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
 type has fixed-length instances, yet those instances have a `ob_size` field. (As with [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
, avoid reading lists’ `ob_size` directly. Call [`PyList_Size()`](https://docs.python.org/3/c-api/list.html#c.PyList_Size "PyList_Size")
 instead.)

The `tp_basicsize` includes size needed for data of the type’s [`tp_base`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_base "PyTypeObject.tp_base")
, plus any extra data needed by each instance.

The correct way to set `tp_basicsize` is to use the `sizeof` operator on the struct used to declare the instance layout. This struct must include the struct used to declare the base type. In other words, `tp_basicsize` must be greater than or equal to the base’s `tp_basicsize`.

Since every type is a subtype of [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
, this struct must include [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 or [`PyVarObject`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject "PyVarObject")
 (depending on whether [`ob_size`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject.ob_size "PyVarObject.ob_size")
 should be included). These are usually defined by the macro [`PyObject_HEAD`](https://docs.python.org/3/c-api/structures.html#c.PyObject_HEAD "PyObject_HEAD")
 or [`PyObject_VAR_HEAD`](https://docs.python.org/3/c-api/structures.html#c.PyObject_VAR_HEAD "PyObject_VAR_HEAD")
, respectively.

The basic size does not include the GC header size, as that header is not part of [`PyObject_HEAD`](https://docs.python.org/3/c-api/structures.html#c.PyObject_HEAD "PyObject_HEAD")
.

For cases where struct used to declare the base type is unknown, see [`PyType_Spec.basicsize`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.basicsize "PyType_Spec.basicsize")
 and [`PyType_FromMetaclass()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromMetaclass "PyType_FromMetaclass")
.

Notes about alignment:

*   `tp_basicsize` must be a multiple of `_Alignof(PyObject)`. When using `sizeof` on a `struct` that includes [`PyObject_HEAD`](https://docs.python.org/3/c-api/structures.html#c.PyObject_HEAD "PyObject_HEAD")
    , as recommended, the compiler ensures this. When not using a C `struct`, or when using compiler extensions like `__attribute__((packed))`, it is up to you.
    
*   If the variable items require a particular alignment, `tp_basicsize` and `tp_itemsize` must each be a multiple of that alignment. For example, if a type’s variable part stores a `double`, it is your responsibility that both fields are a multiple of `_Alignof(double)`.
    

**Inheritance:**

These fields are inherited separately by subtypes. (That is, if the field is set to zero, [`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
 will copy the value from the base type, indicating that the instances do not need additional storage.)

If the base type has a non-zero [`tp_itemsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_itemsize "PyTypeObject.tp_itemsize")
, it is generally not safe to set `tp_itemsize` to a different non-zero value in a subtype (though this depends on the implementation of the base type).

[destructor](https://docs.python.org/3/c-api/typeobj.html#c.destructor "destructor")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_dealloc[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_dealloc` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

A pointer to the instance destructor function. The function signature is:

void tp\_dealloc(PyObject \*self);

The destructor function should remove all references which the instance owns (e.g., call [`Py_CLEAR()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_CLEAR "Py_CLEAR")
), free all memory buffers owned by the instance, and call the type’s [`tp_free`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_free "PyTypeObject.tp_free")
 function to free the object itself.

If you may call functions that may set the error indicator, you must use [`PyErr_GetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetRaisedException "PyErr_GetRaisedException")
 and [`PyErr_SetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetRaisedException "PyErr_SetRaisedException")
 to ensure you don’t clobber a preexisting error indicator (the deallocation could have occurred while processing a different error):

static void
foo\_dealloc(foo\_object \*self)
{
    PyObject \*et, \*ev, \*etb;
    PyObject \*exc \= PyErr\_GetRaisedException();
    ...
    PyErr\_SetRaisedException(exc);
}

The dealloc handler itself must not raise an exception; if it hits an error case it should call [`PyErr_FormatUnraisable()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_FormatUnraisable "PyErr_FormatUnraisable")
 to log (and clear) an unraisable exception.

No guarantees are made about when an object is destroyed, except:

*   Python will destroy an object immediately or some time after the final reference to the object is deleted, unless its finalizer ([`tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "PyTypeObject.tp_finalize")
    ) subsequently resurrects the object.
    
*   An object will not be destroyed while it is being automatically finalized ([`tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "PyTypeObject.tp_finalize")
    ) or automatically cleared ([`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
    ).
    

CPython currently destroys an object immediately from [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
 when the new reference count is zero, but this may change in a future version.

It is recommended to call [`PyObject_CallFinalizerFromDealloc()`](https://docs.python.org/3/c-api/lifecycle.html#c.PyObject_CallFinalizerFromDealloc "PyObject_CallFinalizerFromDealloc")
 at the beginning of `tp_dealloc` to guarantee that the object is always finalized before destruction.

If the type supports garbage collection (the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 flag is set), the destructor should call [`PyObject_GC_UnTrack()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_UnTrack "PyObject_GC_UnTrack")
 before clearing any member fields.

It is permissible to call [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
 from `tp_dealloc` to reduce code duplication and to guarantee that the object is always cleared before destruction. Beware that `tp_clear` might have already been called.

If the type is heap allocated ([`Py_TPFLAGS_HEAPTYPE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HEAPTYPE "Py_TPFLAGS_HEAPTYPE")
), the deallocator should release the owned reference to its type object (via [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
) after calling the type deallocator. See the example code below.:

static void
foo\_dealloc(PyObject \*op)
{
   foo\_object \*self \= (foo\_object \*) op;
   PyObject\_GC\_UnTrack(self);
   Py\_CLEAR(self\->ref);
   Py\_TYPE(self)\->tp\_free(self);
}

`tp_dealloc` must leave the exception status unchanged. If it needs to call something that might raise an exception, the exception state must be backed up first and restored later (after logging any exceptions with [`PyErr_WriteUnraisable()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WriteUnraisable "PyErr_WriteUnraisable")
).

Example:

static void
foo\_dealloc(PyObject \*self)
{
    PyObject \*exc \= PyErr\_GetRaisedException();

    if (PyObject\_CallFinalizerFromDealloc(self) < 0) {
        // self was resurrected.
        goto done;
    }

    PyTypeObject \*tp \= Py\_TYPE(self);

    if (tp\->tp\_flags & Py\_TPFLAGS\_HAVE\_GC) {
        PyObject\_GC\_UnTrack(self);
    }

    // Optional, but convenient to avoid code duplication.
    if (tp\->tp\_clear && tp\->tp\_clear(self) < 0) {
        PyErr\_WriteUnraisable(self);
    }

    // Any additional destruction goes here.

    tp\->tp\_free(self);
    self \= NULL;  // In case PyErr\_WriteUnraisable() is called below.

    if (tp\->tp\_flags & Py\_TPFLAGS\_HEAPTYPE) {
        Py\_CLEAR(tp);
    }

done:
    // Optional, if something was called that might have raised an
    // exception.
    if (PyErr\_Occurred()) {
        PyErr\_WriteUnraisable(self);
    }
    PyErr\_SetRaisedException(exc);
}

`tp_dealloc` may be called from any Python thread, not just the thread which created the object (if the object becomes part of a refcount cycle, that cycle might be collected by a garbage collection on any thread). This is not a problem for Python API calls, since the thread on which `tp_dealloc` is called with an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
. However, if the object being destroyed in turn destroys objects from some other C library, care should be taken to ensure that destroying those objects on the thread which called `tp_dealloc` will not violate any assumptions of the library.

**Inheritance:**

This field is inherited by subtypes.

See also

[Object Life Cycle](https://docs.python.org/3/c-api/lifecycle.html#life-cycle)
 for details about how this slot relates to other slots.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_vectorcall\_offset[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_vectorcall_offset "Link to this definition")
  

An optional offset to a per-instance function that implements calling the object using the [vectorcall protocol](https://docs.python.org/3/c-api/call.html#vectorcall)
, a more efficient alternative of the simpler [`tp_call`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_call "PyTypeObject.tp_call")
.

This field is only used if the flag [`Py_TPFLAGS_HAVE_VECTORCALL`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_VECTORCALL "Py_TPFLAGS_HAVE_VECTORCALL")
 is set. If so, this must be a positive integer containing the offset in the instance of a [`vectorcallfunc`](https://docs.python.org/3/c-api/call.html#c.vectorcallfunc "vectorcallfunc")
 pointer.

The _vectorcallfunc_ pointer may be `NULL`, in which case the instance behaves as if [`Py_TPFLAGS_HAVE_VECTORCALL`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_VECTORCALL "Py_TPFLAGS_HAVE_VECTORCALL")
 was not set: calling the instance falls back to [`tp_call`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_call "PyTypeObject.tp_call")
.

Any class that sets `Py_TPFLAGS_HAVE_VECTORCALL` must also set [`tp_call`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_call "PyTypeObject.tp_call")
 and make sure its behaviour is consistent with the _vectorcallfunc_ function. This can be done by setting _tp\_call_ to [`PyVectorcall_Call()`](https://docs.python.org/3/c-api/call.html#c.PyVectorcall_Call "PyVectorcall_Call")
.

Changed in version 3.8: Before version 3.8, this slot was named `tp_print`. In Python 2.x, it was used for printing to a file. In Python 3.0 to 3.7, it was unused.

Changed in version 3.12: Before version 3.12, it was not recommended for [mutable heap types](https://docs.python.org/3/c-api/typeobj.html#heap-types)
 to implement the vectorcall protocol. When a user sets [`__call__`](https://docs.python.org/3/reference/datamodel.html#object.__call__ "object.__call__")
 in Python code, only _tp\_call_ is updated, likely making it inconsistent with the vectorcall function. Since 3.12, setting `__call__` will disable vectorcall optimization by clearing the [`Py_TPFLAGS_HAVE_VECTORCALL`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_VECTORCALL "Py_TPFLAGS_HAVE_VECTORCALL")
 flag.

**Inheritance:**

This field is always inherited. However, the [`Py_TPFLAGS_HAVE_VECTORCALL`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_VECTORCALL "Py_TPFLAGS_HAVE_VECTORCALL")
 flag is not always inherited. If it’s not set, then the subclass won’t use [vectorcall](https://docs.python.org/3/c-api/call.html#vectorcall)
, except when [`PyVectorcall_Call()`](https://docs.python.org/3/c-api/call.html#c.PyVectorcall_Call "PyVectorcall_Call")
 is explicitly called.

[getattrfunc](https://docs.python.org/3/c-api/typeobj.html#c.getattrfunc "getattrfunc")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_getattr[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getattr "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_getattr` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to the get-attribute-string function.

This field is deprecated. When it is defined, it should point to a function that acts the same as the [`tp_getattro`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getattro "PyTypeObject.tp_getattro")
 function, but taking a C string instead of a Python string object to give the attribute name.

**Inheritance:**

Group: [`tp_getattr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getattr "PyTypeObject.tp_getattr")
, [`tp_getattro`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getattro "PyTypeObject.tp_getattro")

This field is inherited by subtypes together with [`tp_getattro`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getattro "PyTypeObject.tp_getattro")
: a subtype inherits both [`tp_getattr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getattr "PyTypeObject.tp_getattr")
 and `tp_getattro` from its base type when the subtype’s `tp_getattr` and `tp_getattro` are both `NULL`.

[setattrfunc](https://docs.python.org/3/c-api/typeobj.html#c.setattrfunc "setattrfunc")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_setattr[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_setattr "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_setattr` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to the function for setting and deleting attributes.

This field is deprecated. When it is defined, it should point to a function that acts the same as the [`tp_setattro`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_setattro "PyTypeObject.tp_setattro")
 function, but taking a C string instead of a Python string object to give the attribute name.

**Inheritance:**

Group: [`tp_setattr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_setattr "PyTypeObject.tp_setattr")
, [`tp_setattro`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_setattro "PyTypeObject.tp_setattro")

This field is inherited by subtypes together with [`tp_setattro`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_setattro "PyTypeObject.tp_setattro")
: a subtype inherits both [`tp_setattr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_setattr "PyTypeObject.tp_setattr")
 and `tp_setattro` from its base type when the subtype’s `tp_setattr` and `tp_setattro` are both `NULL`.

[PyAsyncMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyAsyncMethods "PyAsyncMethods")
 \*[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_as\_async[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_async "Link to this definition")
  

Pointer to an additional structure that contains fields relevant only to objects which implement [awaitable](https://docs.python.org/3/glossary.html#term-awaitable)
 and [asynchronous iterator](https://docs.python.org/3/glossary.html#term-asynchronous-iterator)
 protocols at the C-level. See [Async Object Structures](https://docs.python.org/3/c-api/typeobj.html#async-structs)
 for details.

Added in version 3.5: Formerly known as `tp_compare` and `tp_reserved`.

**Inheritance:**

The [`tp_as_async`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_async "PyTypeObject.tp_as_async")
 field is not inherited, but the contained fields are inherited individually.

[reprfunc](https://docs.python.org/3/c-api/typeobj.html#c.reprfunc "reprfunc")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_repr[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_repr "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_repr` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to a function that implements the built-in function [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
.

The signature is the same as for [`PyObject_Repr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Repr "PyObject_Repr")
:

PyObject \*tp\_repr(PyObject \*self);

The function must return a string or a Unicode object. Ideally, this function should return a string that, when passed to [`eval()`](https://docs.python.org/3/builtins/functions.html#eval "eval")
, given a suitable environment, returns an object with the same value. If this is not feasible, it should return a string starting with `'<'` and ending with `'>'` from which both the type and the value of the object can be deduced.

**Inheritance:**

This field is inherited by subtypes.

**Default:**

When this field is not set, a string of the form `<%s object at %p>` is returned, where `%s` is replaced by the type name, and `%p` by the object’s memory address.

[PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
 \*[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_as\_number[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_number "Link to this definition")
  

Pointer to an additional structure that contains fields relevant only to objects which implement the number protocol. These fields are documented in [Number Object Structures](https://docs.python.org/3/c-api/typeobj.html#number-structs)
.

**Inheritance:**

The [`tp_as_number`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_number "PyTypeObject.tp_as_number")
 field is not inherited, but the contained fields are inherited individually.

[PySequenceMethods](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods "PySequenceMethods")
 \*[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_as\_sequence[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_sequence "Link to this definition")
  

Pointer to an additional structure that contains fields relevant only to objects which implement the sequence protocol. These fields are documented in [Sequence Object Structures](https://docs.python.org/3/c-api/typeobj.html#sequence-structs)
.

**Inheritance:**

The [`tp_as_sequence`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_sequence "PyTypeObject.tp_as_sequence")
 field is not inherited, but the contained fields are inherited individually.

[PyMappingMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyMappingMethods "PyMappingMethods")
 \*[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_as\_mapping[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_mapping "Link to this definition")
  

Pointer to an additional structure that contains fields relevant only to objects which implement the mapping protocol. These fields are documented in [Mapping Object Structures](https://docs.python.org/3/c-api/typeobj.html#mapping-structs)
.

**Inheritance:**

The [`tp_as_mapping`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_mapping "PyTypeObject.tp_as_mapping")
 field is not inherited, but the contained fields are inherited individually.

[hashfunc](https://docs.python.org/3/c-api/typeobj.html#c.hashfunc "hashfunc")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_hash[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_hash "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_hash` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to a function that implements the built-in function [`hash()`](https://docs.python.org/3/builtins/functions.html#hash "hash")
.

The signature is the same as for [`PyObject_Hash()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Hash "PyObject_Hash")
:

Py\_hash\_t tp\_hash(PyObject \*);

The value `-1` should not be returned as a normal return value; when an error occurs during the computation of the hash value, the function should set an exception and return `-1`.

When this field is not set (_and_ [`tp_richcompare`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_richcompare "PyTypeObject.tp_richcompare")
 is not set), an attempt to take the hash of the object raises [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
. This is the same as setting it to [`PyObject_HashNotImplemented()`](https://docs.python.org/3/c-api/object.html#c.PyObject_HashNotImplemented "PyObject_HashNotImplemented")
.

This field can be set explicitly to [`PyObject_HashNotImplemented()`](https://docs.python.org/3/c-api/object.html#c.PyObject_HashNotImplemented "PyObject_HashNotImplemented")
 to block inheritance of the hash method from a parent type. This is interpreted as the equivalent of `__hash__ = None` at the Python level, causing `isinstance(o, collections.Hashable)` to correctly return `False`. Note that the converse is also true - setting `__hash__ = None` on a class at the Python level will result in the `tp_hash` slot being set to `PyObject_HashNotImplemented()`.

**Inheritance:**

Group: [`tp_hash`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_hash "PyTypeObject.tp_hash")
, [`tp_richcompare`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_richcompare "PyTypeObject.tp_richcompare")

This field is inherited by subtypes together with [`tp_richcompare`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_richcompare "PyTypeObject.tp_richcompare")
: a subtype inherits both of `tp_richcompare` and [`tp_hash`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_hash "PyTypeObject.tp_hash")
, when the subtype’s `tp_richcompare` and `tp_hash` are both `NULL`.

**Default:**

[`PyBaseObject_Type`](https://docs.python.org/3/c-api/structures.html#c.PyBaseObject_Type "PyBaseObject_Type")
 uses [`PyObject_GenericHash()`](https://docs.python.org/3/c-api/hash.html#c.PyObject_GenericHash "PyObject_GenericHash")
.

[ternaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.ternaryfunc "ternaryfunc")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_call[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_call "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_call` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to a function that implements calling the object. This should be `NULL` if the object is not callable. The signature is the same as for [`PyObject_Call()`](https://docs.python.org/3/c-api/call.html#c.PyObject_Call "PyObject_Call")
:

PyObject \*tp\_call(PyObject \*self, PyObject \*args, PyObject \*kwargs);

**Inheritance:**

This field is inherited by subtypes.

[reprfunc](https://docs.python.org/3/c-api/typeobj.html#c.reprfunc "reprfunc")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_str[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_str "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_str` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to a function that implements the built-in operation [`str()`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
. (Note that [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 is a type now, and `str()` calls the constructor for that type. This constructor calls [`PyObject_Str()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Str "PyObject_Str")
 to do the actual work, and `PyObject_Str()` will call this handler.)

The signature is the same as for [`PyObject_Str()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Str "PyObject_Str")
:

PyObject \*tp\_str(PyObject \*self);

The function must return a string or a Unicode object. It should be a “friendly” string representation of the object, as this is the representation that will be used, among other things, by the [`print()`](https://docs.python.org/3/builtins/functions.html#print "print")
 function.

**Inheritance:**

This field is inherited by subtypes.

**Default:**

When this field is not set, [`PyObject_Repr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Repr "PyObject_Repr")
 is called to return a string representation.

[getattrofunc](https://docs.python.org/3/c-api/typeobj.html#c.getattrofunc "getattrofunc")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_getattro[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getattro "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_getattro` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to the get-attribute function.

The signature is the same as for [`PyObject_GetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAttr "PyObject_GetAttr")
:

PyObject \*tp\_getattro(PyObject \*self, PyObject \*attr);

It is usually convenient to set this field to [`PyObject_GenericGetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GenericGetAttr "PyObject_GenericGetAttr")
, which implements the normal way of looking for object attributes.

**Inheritance:**

Group: [`tp_getattr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getattr "PyTypeObject.tp_getattr")
, [`tp_getattro`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getattro "PyTypeObject.tp_getattro")

This field is inherited by subtypes together with [`tp_getattr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getattr "PyTypeObject.tp_getattr")
: a subtype inherits both `tp_getattr` and [`tp_getattro`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getattro "PyTypeObject.tp_getattro")
 from its base type when the subtype’s `tp_getattr` and `tp_getattro` are both `NULL`.

**Default:**

[`PyBaseObject_Type`](https://docs.python.org/3/c-api/structures.html#c.PyBaseObject_Type "PyBaseObject_Type")
 uses [`PyObject_GenericGetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GenericGetAttr "PyObject_GenericGetAttr")
.

[setattrofunc](https://docs.python.org/3/c-api/typeobj.html#c.setattrofunc "setattrofunc")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_setattro[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_setattro "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_setattro` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to the function for setting and deleting attributes.

The signature is the same as for [`PyObject_SetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_SetAttr "PyObject_SetAttr")
:

int tp\_setattro(PyObject \*self, PyObject \*attr, PyObject \*value);

In addition, setting _value_ to `NULL` to delete an attribute must be supported. It is usually convenient to set this field to [`PyObject_GenericSetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GenericSetAttr "PyObject_GenericSetAttr")
, which implements the normal way of setting object attributes.

**Inheritance:**

Group: [`tp_setattr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_setattr "PyTypeObject.tp_setattr")
, [`tp_setattro`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_setattro "PyTypeObject.tp_setattro")

This field is inherited by subtypes together with [`tp_setattr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_setattr "PyTypeObject.tp_setattr")
: a subtype inherits both `tp_setattr` and [`tp_setattro`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_setattro "PyTypeObject.tp_setattro")
 from its base type when the subtype’s `tp_setattr` and `tp_setattro` are both `NULL`.

**Default:**

[`PyBaseObject_Type`](https://docs.python.org/3/c-api/structures.html#c.PyBaseObject_Type "PyBaseObject_Type")
 uses [`PyObject_GenericSetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GenericSetAttr "PyObject_GenericSetAttr")
.

[PyBufferProcs](https://docs.python.org/3/c-api/typeobj.html#c.PyBufferProcs "PyBufferProcs")
 \*[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_as\_buffer[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_buffer "Link to this definition")
  

Pointer to an additional structure that contains fields relevant only to objects which implement the buffer interface. These fields are documented in [Buffer Object Structures](https://docs.python.org/3/c-api/typeobj.html#buffer-structs)
.

**Inheritance:**

The [`tp_as_buffer`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_buffer "PyTypeObject.tp_as_buffer")
 field is not inherited, but the contained fields are inherited individually.

unsigned long [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_flags[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "Link to this definition")
  

See [`Py_tp_flags`](https://docs.python.org/3/c-api/type.html#c.Py_tp_flags "Py_tp_flags")
 for the corresponding [`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
.

This field is a bit mask of various flags. Some flags indicate variant semantics for certain situations; others are used to indicate that certain fields in the type object (or in the extension structures referenced via [`tp_as_number`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_number "PyTypeObject.tp_as_number")
, [`tp_as_sequence`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_sequence "PyTypeObject.tp_as_sequence")
, [`tp_as_mapping`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_mapping "PyTypeObject.tp_as_mapping")
, and [`tp_as_buffer`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_buffer "PyTypeObject.tp_as_buffer")
) that were historically not always present are valid; if such a flag bit is clear, the type fields it guards must not be accessed and must be considered to have a zero or `NULL` value instead.

**Inheritance:**

Inheritance of this field is complicated. Most flag bits are inherited individually, i.e. if the base type has a flag bit set, the subtype inherits this flag bit. The flag bits that pertain to extension structures are strictly inherited if the extension structure is inherited, i.e. the base type’s value of the flag bit is copied into the subtype together with a pointer to the extension structure. The [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 flag bit is inherited together with the [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
 and [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
 fields, i.e. if the `Py_TPFLAGS_HAVE_GC` flag bit is clear in the subtype and the `tp_traverse` and `tp_clear` fields in the subtype exist and have `NULL` values.

**Default:**

[`PyBaseObject_Type`](https://docs.python.org/3/c-api/structures.html#c.PyBaseObject_Type "PyBaseObject_Type")
 uses `Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE`.

**Bit Masks:**

The following bit masks are currently defined; these can be ORed together using the `|` operator to form the value of the [`tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags")
 field. The macro [`PyType_HasFeature()`](https://docs.python.org/3/c-api/type.html#c.PyType_HasFeature "PyType_HasFeature")
 takes a type and a flags value, _tp_ and _f_, and checks whether `tp->tp_flags & f` is non-zero.

Py\_TPFLAGS\_HEAPTYPE[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HEAPTYPE "Link to this definition")
  

This bit is set when the type object itself is allocated on the heap, for example, types created dynamically using [`PyType_FromSpec()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSpec "PyType_FromSpec")
. In this case, the [`ob_type`](https://docs.python.org/3/c-api/structures.html#c.PyObject.ob_type "PyObject.ob_type")
 field of its instances is considered a reference to the type, and the type object is INCREF’ed when a new instance is created, and DECREF’ed when an instance is destroyed (this does not apply to instances of subtypes; only the type referenced by the instance’s ob\_type gets INCREF’ed or DECREF’ed). Heap types should also [support garbage collection](https://docs.python.org/3/c-api/gcsupport.html#supporting-cycle-detection)
 as they can form a reference cycle with their own module object.

**Inheritance:**

???

Py\_TPFLAGS\_BASETYPE[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_BASETYPE "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This bit is set when the type can be used as the base type of another type. If this bit is clear, the type cannot be subtyped (similar to a “final” class in Java).

**Inheritance:**

???

Py\_TPFLAGS\_READY[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_READY "Link to this definition")
  

This bit is set when the type object has been fully initialized by [`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
.

**Inheritance:**

???

Py\_TPFLAGS\_READYING[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_READYING "Link to this definition")
  

This bit is set while [`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
 is in the process of initializing the type object.

**Inheritance:**

???

Py\_TPFLAGS\_HAVE\_GC[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This bit is set when the object supports garbage collection. If this bit is set, memory for new instances (see [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
) must be allocated using [`PyObject_GC_New`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_New "PyObject_GC_New")
 or [`PyType_GenericAlloc()`](https://docs.python.org/3/c-api/type.html#c.PyType_GenericAlloc "PyType_GenericAlloc")
 and deallocated (see [`tp_free`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_free "PyTypeObject.tp_free")
) using [`PyObject_GC_Del()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_Del "PyObject_GC_Del")
. More information in section [Supporting Cyclic Garbage Collection](https://docs.python.org/3/c-api/gcsupport.html#supporting-cycle-detection)
.

**Inheritance:**

Group: [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
, [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
, [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")

The [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 flag bit is inherited together with the [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
 and [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
 fields, i.e. if the `Py_TPFLAGS_HAVE_GC` flag bit is clear in the subtype and the `tp_traverse` and `tp_clear` fields in the subtype exist and have `NULL` values.

Py\_TPFLAGS\_DEFAULT[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_DEFAULT "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is a bitmask of all the bits that pertain to the existence of certain fields in the type object and its extension structures. Currently, it includes the following bits: [`Py_TPFLAGS_HAVE_STACKLESS_EXTENSION`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_STACKLESS_EXTENSION "Py_TPFLAGS_HAVE_STACKLESS_EXTENSION")
.

**Inheritance:**

???

Py\_TPFLAGS\_METHOD\_DESCRIPTOR[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_METHOD_DESCRIPTOR "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.8._

This bit indicates that objects behave like unbound methods.

If this flag is set for `type(meth)`, then:

*   `meth.__get__(obj, cls)(*args, **kwds)` (with `obj` not None) must be equivalent to `meth(obj, *args, **kwds)`.
    
*   `meth.__get__(None, cls)(*args, **kwds)` must be equivalent to `meth(*args, **kwds)`.
    

This flag enables an optimization for typical method calls like `obj.meth()`: it avoids creating a temporary “bound method” object for `obj.meth`.

Added in version 3.8.

**Inheritance:**

This flag is never inherited by types without the [`Py_TPFLAGS_IMMUTABLETYPE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE "Py_TPFLAGS_IMMUTABLETYPE")
 flag set. For extension types, it is inherited whenever [`tp_descr_get`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_descr_get "PyTypeObject.tp_descr_get")
 is inherited.

Py\_TPFLAGS\_MANAGED\_DICT[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT "Link to this definition")
  

This bit indicates that instances of the class have a [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")
 attribute, and that the space for the dictionary is managed by the VM.

If this flag is set, [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 must also be set.

The type traverse function must call [`PyObject_VisitManagedDict()`](https://docs.python.org/3/c-api/object.html#c.PyObject_VisitManagedDict "PyObject_VisitManagedDict")
 and its clear function must call [`PyObject_ClearManagedDict()`](https://docs.python.org/3/c-api/object.html#c.PyObject_ClearManagedDict "PyObject_ClearManagedDict")
.

Added in version 3.12.

**Inheritance:**

This flag is inherited unless the [`tp_dictoffset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dictoffset "PyTypeObject.tp_dictoffset")
 field is set in a superclass.

Py\_TPFLAGS\_MANAGED\_WEAKREF[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_WEAKREF "Link to this definition")
  

This bit indicates that instances of the class should be weakly referenceable.

If this flag is set, [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 must also be set.

Added in version 3.12.

**Inheritance:**

This flag is inherited unless the [`tp_weaklistoffset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_weaklistoffset "PyTypeObject.tp_weaklistoffset")
 field is set in a superclass.

Py\_TPFLAGS\_PREHEADER[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_PREHEADER "Link to this definition")
  

These bits indicate that the VM will manage some fields by storing them before the object. Currently, this macro is equivalent to [Py\_TPFLAGS\_MANAGED\_DICT](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT "Py_TPFLAGS_MANAGED_DICT")
 | [Py\_TPFLAGS\_MANAGED\_WEAKREF](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_WEAKREF "Py_TPFLAGS_MANAGED_WEAKREF")
.

This macro value relies on the implementation of the VM, so its value is not stable and may change in a future version. Prefer using individual flags instead.

Added in version 3.12.

Py\_TPFLAGS\_ITEMS\_AT\_END[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_ITEMS_AT_END "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

Only usable with variable-size types, i.e. ones with non-zero [`tp_itemsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_itemsize "PyTypeObject.tp_itemsize")
.

Indicates that the variable-sized portion of an instance of this type is at the end of the instance’s memory area, at an offset of `Py_TYPE(obj)->tp_basicsize` (which may be different in each subclass).

When setting this flag, be sure that all superclasses either use this memory layout, or are not variable-sized. Python does not check this.

Added in version 3.12.

**Inheritance:**

This flag is inherited.

Py\_TPFLAGS\_LONG\_SUBCLASS[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_LONG_SUBCLASS "Link to this definition")
  

Py\_TPFLAGS\_LIST\_SUBCLASS[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_LIST_SUBCLASS "Link to this definition")
  

Py\_TPFLAGS\_TUPLE\_SUBCLASS[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_TUPLE_SUBCLASS "Link to this definition")
  

Py\_TPFLAGS\_BYTES\_SUBCLASS[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_BYTES_SUBCLASS "Link to this definition")
  

Py\_TPFLAGS\_UNICODE\_SUBCLASS[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_UNICODE_SUBCLASS "Link to this definition")
  

Py\_TPFLAGS\_DICT\_SUBCLASS[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_DICT_SUBCLASS "Link to this definition")
  

Py\_TPFLAGS\_BASE\_EXC\_SUBCLASS[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_BASE_EXC_SUBCLASS "Link to this definition")
  

Py\_TPFLAGS\_TYPE\_SUBCLASS[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_TYPE_SUBCLASS "Link to this definition")
  

Functions such as [`PyLong_Check()`](https://docs.python.org/3/c-api/long.html#c.PyLong_Check "PyLong_Check")
 will call [`PyType_FastSubclass()`](https://docs.python.org/3/c-api/type.html#c.PyType_FastSubclass "PyType_FastSubclass")
 with one of these flags to quickly determine if a type is a subclass of a built-in type; such specific checks are faster than a generic check, like [`PyObject_IsInstance()`](https://docs.python.org/3/c-api/object.html#c.PyObject_IsInstance "PyObject_IsInstance")
. Custom types that inherit from built-ins should have their [`tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags")
 set appropriately, or the code that interacts with such types will behave differently depending on what kind of check is used.

Py\_TPFLAGS\_HAVE\_FINALIZE[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_FINALIZE "Link to this definition")
  

This bit is set when the [`tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "PyTypeObject.tp_finalize")
 slot is present in the type structure.

Added in version 3.4.

Deprecated since version 3.8: This flag isn’t necessary anymore, as the interpreter assumes the [`tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "PyTypeObject.tp_finalize")
 slot is always present in the type structure.

Py\_TPFLAGS\_HAVE\_VECTORCALL[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_VECTORCALL "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

This bit is set when the class implements the [vectorcall protocol](https://docs.python.org/3/c-api/call.html#vectorcall)
. See [`tp_vectorcall_offset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_vectorcall_offset "PyTypeObject.tp_vectorcall_offset")
 for details.

**Inheritance:**

This bit is inherited if [`tp_call`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_call "PyTypeObject.tp_call")
 is also inherited.

Added in version 3.8: as `_Py_TPFLAGS_HAVE_VECTORCALL`

Changed in version 3.9: Renamed to the current name, without the leading underscore. The old provisional name is [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
.

Changed in version 3.12: This flag is now removed from a class when the class’s [`__call__()`](https://docs.python.org/3/reference/datamodel.html#object.__call__ "object.__call__")
 method is reassigned.

This flag can now be inherited by mutable classes.

Py\_TPFLAGS\_IMMUTABLETYPE[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE "Link to this definition")
  

This bit is set for type objects that are immutable: type attributes cannot be set nor deleted.

[`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
 automatically applies this flag to [static types](https://docs.python.org/3/c-api/typeobj.html#static-types)
.

**Inheritance:**

This flag is not inherited.

Added in version 3.10.

Py\_TPFLAGS\_DISALLOW\_INSTANTIATION[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_DISALLOW_INSTANTIATION "Link to this definition")
  

Disallow creating instances of the type: set [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 to NULL and don’t create the `__new__` key in the type dictionary.

The flag must be set before creating the type, not after. For example, it must be set before [`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
 is called on the type.

The flag is set automatically on [static types](https://docs.python.org/3/c-api/typeobj.html#static-types)
 if [`tp_base`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_base "PyTypeObject.tp_base")
 is NULL or `&PyBaseObject_Type` and [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 is NULL.

**Inheritance:**

This flag is not inherited. However, subclasses will not be instantiable unless they provide a non-NULL [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 (which is only possible via the C API).

Note

To disallow instantiating a class directly but allow instantiating its subclasses (e.g. for an [abstract base class](https://docs.python.org/3/glossary.html#term-abstract-base-class)
), do not use this flag. Instead, make [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 only succeed for subclasses.

Added in version 3.10.

Py\_TPFLAGS\_MAPPING[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MAPPING "Link to this definition")
  

This bit indicates that instances of the class may match mapping patterns when used as the subject of a [`match`](https://docs.python.org/3/reference/compound_stmts.html#match)
 block. It is automatically set when registering or subclassing [`collections.abc.Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "collections.abc.Mapping")
, and unset when registering [`collections.abc.Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")
.

Note

[`Py_TPFLAGS_MAPPING`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MAPPING "Py_TPFLAGS_MAPPING")
 and [`Py_TPFLAGS_SEQUENCE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_SEQUENCE "Py_TPFLAGS_SEQUENCE")
 are mutually exclusive; it is an error to enable both flags simultaneously.

**Inheritance:**

This flag is inherited by types that do not already set [`Py_TPFLAGS_SEQUENCE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_SEQUENCE "Py_TPFLAGS_SEQUENCE")
.

See also

[**PEP 634**](https://peps.python.org/pep-0634/)
 – Structural Pattern Matching: Specification

Added in version 3.10.

Py\_TPFLAGS\_SEQUENCE[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_SEQUENCE "Link to this definition")
  

This bit indicates that instances of the class may match sequence patterns when used as the subject of a [`match`](https://docs.python.org/3/reference/compound_stmts.html#match)
 block. It is automatically set when registering or subclassing [`collections.abc.Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")
, and unset when registering [`collections.abc.Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "collections.abc.Mapping")
.

Note

[`Py_TPFLAGS_MAPPING`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MAPPING "Py_TPFLAGS_MAPPING")
 and [`Py_TPFLAGS_SEQUENCE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_SEQUENCE "Py_TPFLAGS_SEQUENCE")
 are mutually exclusive; it is an error to enable both flags simultaneously.

**Inheritance:**

This flag is inherited by types that do not already set [`Py_TPFLAGS_MAPPING`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MAPPING "Py_TPFLAGS_MAPPING")
.

See also

[**PEP 634**](https://peps.python.org/pep-0634/)
 – Structural Pattern Matching: Specification

Added in version 3.10.

Py\_TPFLAGS\_VALID\_VERSION\_TAG[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_VALID_VERSION_TAG "Link to this definition")
  

Internal. Do not set or unset this flag. To indicate that a class has changed call [`PyType_Modified()`](https://docs.python.org/3/c-api/type.html#c.PyType_Modified "PyType_Modified")

Warning

This flag is present in header files, but is not be used. It will be removed in a future version of CPython

Py\_TPFLAGS\_HAVE\_VERSION\_TAG[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_VERSION_TAG "Link to this definition")
  

This macro does nothing. Historically, this would indicate that the [`tp_version_tag`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_version_tag "PyTypeObject.tp_version_tag")
 field was available and initialized.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.13.

Py\_TPFLAGS\_INLINE\_VALUES[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_INLINE_VALUES "Link to this definition")
  

This bit indicates that instances of this type will have an “inline values” array (containing the object’s attributes) placed directly after the end of the object.

This requires that [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 is set.

**Inheritance:**

This flag is not inherited.

Added in version 3.13.

Py\_TPFLAGS\_IS\_ABSTRACT[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_IS_ABSTRACT "Link to this definition")
  

This bit indicates that this is an abstract type and therefore cannot be instantiated.

**Inheritance:**

This flag is not inherited.

See also

[`abc`](https://docs.python.org/3/library/abc.html#module-abc "abc: Abstract base classes according to :pep:`3119`.")

Py\_TPFLAGS\_HAVE\_STACKLESS\_EXTENSION[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_STACKLESS_EXTENSION "Link to this definition")
  

Internal. Do not set or unset this flag. Historically, this was a reserved flag for use in Stackless Python.

Warning

This flag is present in header files, but is not be used. This may be removed in a future version of CPython.

const char \*[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_doc[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_doc "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_doc` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to a NUL-terminated C string giving the docstring for this type object. This is exposed as the [`__doc__`](https://docs.python.org/3/reference/datamodel.html#type.__doc__ "type.__doc__")
 attribute on the type and instances of the type.

**Inheritance:**

This field is _not_ inherited by subtypes.

[traverseproc](https://docs.python.org/3/c-api/gcsupport.html#c.traverseproc "traverseproc")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_traverse[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_traverse` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to a traversal function for the garbage collector. This is only used if the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 flag bit is set.

See [Traversal](https://docs.python.org/3/c-api/gcsupport.html#gc-traversal)
 for documentation.

**Inheritance:**

Group: [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
, [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
, [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")

This field is inherited by subtypes together with [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
 and the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 flag bit: the flag bit, [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
, and `tp_clear` are all inherited from the base type if they are all zero in the subtype.

[inquiry](https://docs.python.org/3/c-api/gcsupport.html#c.inquiry "inquiry")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_clear[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_clear` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to a clear function. The signature is:

int tp\_clear(PyObject \*);

The purpose of this function is to break reference cycles that are causing a [cyclic isolate](https://docs.python.org/3/glossary.html#term-cyclic-isolate)
 so that the objects can be safely destroyed. A cleared object is a partially destroyed object; the object is not obligated to satisfy design invariants held during normal use.

`tp_clear` does not need to delete references to objects that can’t participate in reference cycles, such as Python strings or Python integers. However, it may be convenient to clear all references, and write the type’s [`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
 function to invoke `tp_clear` to avoid code duplication. (Beware that `tp_clear` might have already been called. Prefer calling idempotent functions like [`Py_CLEAR()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_CLEAR "Py_CLEAR")
.)

Any non-trivial cleanup should be performed in [`tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "PyTypeObject.tp_finalize")
 instead of `tp_clear`.

Note

If `tp_clear` fails to break a reference cycle then the objects in the [cyclic isolate](https://docs.python.org/3/glossary.html#term-cyclic-isolate)
 may remain indefinitely uncollectable (“leak”). See [`gc.garbage`](https://docs.python.org/3/library/gc.html#gc.garbage "gc.garbage")
.

Note

Referents (direct and indirect) might have already been cleared; they are not guaranteed to be in a consistent state.

Note

The [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
 function can be called from any thread.

Note

An object is not guaranteed to be automatically cleared before its destructor ([`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
) is called.

This function differs from the destructor ([`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
) in the following ways:

*   The purpose of clearing an object is to remove references to other objects that might participate in a reference cycle. The purpose of the destructor, on the other hand, is a superset: it must release _all_ resources it owns, including references to objects that cannot participate in a reference cycle (e.g., integers) as well as the object’s own memory (by calling [`tp_free`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_free "PyTypeObject.tp_free")
    ).
    
*   When `tp_clear` is called, other objects might still hold references to the object being cleared. Because of this, `tp_clear` must not deallocate the object’s own memory ([`tp_free`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_free "PyTypeObject.tp_free")
    ). The destructor, on the other hand, is only called when no (strong) references exist, and as such, must safely destroy the object itself by deallocating it.
    
*   `tp_clear` might never be automatically called. An object’s destructor, on the other hand, will be automatically called some time after the object becomes unreachable (i.e., either there are no references to the object or the object is a member of a [cyclic isolate](https://docs.python.org/3/glossary.html#term-cyclic-isolate)
    ).
    

No guarantees are made about when, if, or how often Python automatically clears an object, except:

*   Python will not automatically clear an object if it is reachable, i.e., there is a reference to it and it is not a member of a [cyclic isolate](https://docs.python.org/3/glossary.html#term-cyclic-isolate)
    .
    
*   Python will not automatically clear an object if it has not been automatically finalized (see [`tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "PyTypeObject.tp_finalize")
    ). (If the finalizer resurrected the object, the object may or may not be automatically finalized again before it is cleared.)
    
*   If an object is a member of a [cyclic isolate](https://docs.python.org/3/glossary.html#term-cyclic-isolate)
    , Python will not automatically clear it if any member of the cyclic isolate has not yet been automatically finalized ([`tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "PyTypeObject.tp_finalize")
    ).
    
*   Python will not destroy an object until after any automatic calls to its `tp_clear` function have returned. This ensures that the act of breaking a reference cycle does not invalidate the `self` pointer while `tp_clear` is still executing.
    
*   Python will not automatically call `tp_clear` multiple times concurrently.
    

CPython currently only automatically clears objects as needed to break reference cycles in a [cyclic isolate](https://docs.python.org/3/glossary.html#term-cyclic-isolate)
, but future versions might clear objects regularly before their destruction.

Taken together, all [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
 functions in the system must combine to break all reference cycles. This is subtle, and if in any doubt supply a `tp_clear` function. For example, the tuple type does not implement a `tp_clear` function, because it’s possible to prove that no reference cycle can be composed entirely of tuples. Therefore the `tp_clear` functions of other types are responsible for breaking any cycle containing a tuple. This isn’t immediately obvious, and there’s rarely a good reason to avoid implementing `tp_clear`.

Implementations of [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
 should drop the instance’s references to those of its members that may be Python objects, and set its pointers to those members to `NULL`, as in the following example:

static int
local\_clear(PyObject \*op)
{
    localobject \*self \= (localobject \*) op;
    Py\_CLEAR(self\->key);
    Py\_CLEAR(self\->args);
    Py\_CLEAR(self\->kw);
    Py\_CLEAR(self\->dict);
    return 0;
}

The [`Py_CLEAR()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_CLEAR "Py_CLEAR")
 macro should be used, because clearing references is delicate: the reference to the contained object must not be released (via [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
) until after the pointer to the contained object is set to `NULL`. This is because releasing the reference may cause the contained object to become trash, triggering a chain of reclamation activity that may include invoking arbitrary Python code (due to finalizers, or weakref callbacks, associated with the contained object). If it’s possible for such code to reference _self_ again, it’s important that the pointer to the contained object be `NULL` at that time, so that _self_ knows the contained object can no longer be used. The `Py_CLEAR()` macro performs the operations in a safe order.

If the [`Py_TPFLAGS_MANAGED_DICT`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT "Py_TPFLAGS_MANAGED_DICT")
 bit is set in the [`tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags")
 field, the clear function must call [`PyObject_ClearManagedDict()`](https://docs.python.org/3/c-api/object.html#c.PyObject_ClearManagedDict "PyObject_ClearManagedDict")
 like this:

PyObject\_ClearManagedDict((PyObject\*)self);

More information about Python’s garbage collection scheme can be found in section [Supporting Cyclic Garbage Collection](https://docs.python.org/3/c-api/gcsupport.html#supporting-cycle-detection)
.

**Inheritance:**

Group: [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
, [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
, [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")

This field is inherited by subtypes together with [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
 and the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 flag bit: the flag bit, `tp_traverse`, and [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
 are all inherited from the base type if they are all zero in the subtype.

See also

[Object Life Cycle](https://docs.python.org/3/c-api/lifecycle.html#life-cycle)
 for details about how this slot relates to other slots.

[richcmpfunc](https://docs.python.org/3/c-api/typeobj.html#c.richcmpfunc "richcmpfunc")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_richcompare[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_richcompare "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_richcompare` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to the rich comparison function, whose signature is:

PyObject \*tp\_richcompare(PyObject \*self, PyObject \*other, int op);

The first parameter is guaranteed to be an instance of the type that is defined by [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.

The function should return the result of the comparison (usually `Py_True` or `Py_False`). If the comparison is undefined, it must return `Py_NotImplemented`, if another error occurred it must return `NULL` and set an exception condition.

The following constants are defined to be used as the third argument for [`tp_richcompare`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_richcompare "PyTypeObject.tp_richcompare")
 and for [`PyObject_RichCompare()`](https://docs.python.org/3/c-api/object.html#c.PyObject_RichCompare "PyObject_RichCompare")
:

| Constant | Comparison |
| --- | --- |
| Py\_LT[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_LT "Link to this definition") | `<` |
| Py\_LE[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_LE "Link to this definition") | `<=` |
| Py\_EQ[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_EQ "Link to this definition") | `==` |
| Py\_NE[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_NE "Link to this definition") | `!=` |
| Py\_GT[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_GT "Link to this definition") | `>` |
| Py\_GE[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_GE "Link to this definition") | `>=` |

The following macro is defined to ease writing rich comparison functions:

Py\_RETURN\_RICHCOMPARE(VAL\_A, VAL\_B, op)[¶](https://docs.python.org/3/c-api/typeobj.html#c.Py_RETURN_RICHCOMPARE "Link to this definition")
  

Return `Py_True` or `Py_False` from the function, depending on the result of a comparison. VAL\_A and VAL\_B must be orderable by C comparison operators (for example, they may be C ints or floats). The third argument specifies the requested operation, as for [`PyObject_RichCompare()`](https://docs.python.org/3/c-api/object.html#c.PyObject_RichCompare "PyObject_RichCompare")
.

The returned value is a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
.

On error, sets an exception and returns `NULL` from the function.

Added in version 3.7.

**Inheritance:**

Group: [`tp_hash`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_hash "PyTypeObject.tp_hash")
, [`tp_richcompare`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_richcompare "PyTypeObject.tp_richcompare")

This field is inherited by subtypes together with [`tp_hash`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_hash "PyTypeObject.tp_hash")
: a subtype inherits [`tp_richcompare`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_richcompare "PyTypeObject.tp_richcompare")
 and `tp_hash` when the subtype’s `tp_richcompare` and `tp_hash` are both `NULL`.

**Default:**

[`PyBaseObject_Type`](https://docs.python.org/3/c-api/structures.html#c.PyBaseObject_Type "PyBaseObject_Type")
 provides a [`tp_richcompare`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_richcompare "PyTypeObject.tp_richcompare")
 implementation, which may be inherited. However, if only [`tp_hash`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_hash "PyTypeObject.tp_hash")
 is defined, not even the inherited function is used and instances of the type will not be able to participate in any comparisons.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_weaklistoffset[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_weaklistoffset "Link to this definition")
  

While this field is still supported, [`Py_TPFLAGS_MANAGED_WEAKREF`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_WEAKREF "Py_TPFLAGS_MANAGED_WEAKREF")
 should be used instead, if at all possible.

If the instances of this type are weakly referenceable, this field is greater than zero and contains the offset in the instance structure of the weak reference list head (ignoring the GC header, if present); this offset is used by [`PyObject_ClearWeakRefs()`](https://docs.python.org/3/c-api/weakref.html#c.PyObject_ClearWeakRefs "PyObject_ClearWeakRefs")
 and the `PyWeakref_*` functions. The instance structure needs to include a field of type [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\* which is initialized to `NULL`.

Do not confuse this field with [`tp_weaklist`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_weaklist "PyTypeObject.tp_weaklist")
; that is the list head for weak references to the type object itself.

It is an error to set both the [`Py_TPFLAGS_MANAGED_WEAKREF`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_WEAKREF "Py_TPFLAGS_MANAGED_WEAKREF")
 bit and [`tp_weaklistoffset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_weaklistoffset "PyTypeObject.tp_weaklistoffset")
.

**Inheritance:**

This field is inherited by subtypes, but see the rules listed below. A subtype may override this offset; this means that the subtype uses a different weak reference list head than the base type. Since the list head is always found via [`tp_weaklistoffset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_weaklistoffset "PyTypeObject.tp_weaklistoffset")
, this should not be a problem.

**Default:**

If the [`Py_TPFLAGS_MANAGED_WEAKREF`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_WEAKREF "Py_TPFLAGS_MANAGED_WEAKREF")
 bit is set in the [`tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags")
 field, then [`tp_weaklistoffset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_weaklistoffset "PyTypeObject.tp_weaklistoffset")
 will be set to a negative value, to indicate that it is unsafe to use this field.

[getiterfunc](https://docs.python.org/3/c-api/typeobj.html#c.getiterfunc "getiterfunc")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_iter[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_iter "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_iter` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to a function that returns an [iterator](https://docs.python.org/3/glossary.html#term-iterator)
 for the object. Its presence normally signals that the instances of this type are [iterable](https://docs.python.org/3/glossary.html#term-iterable)
 (although sequences may be iterable without this function).

This function has the same signature as [`PyObject_GetIter()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetIter "PyObject_GetIter")
:

PyObject \*tp\_iter(PyObject \*self);

**Inheritance:**

This field is inherited by subtypes.

[iternextfunc](https://docs.python.org/3/c-api/typeobj.html#c.iternextfunc "iternextfunc")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_iternext[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_iternext "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_iternext` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to a function that returns the next item in an [iterator](https://docs.python.org/3/glossary.html#term-iterator)
. The signature is:

PyObject \*tp\_iternext(PyObject \*self);

When the iterator is [exhausted](https://docs.python.org/3/glossary.html#term-exhausted)
, the `tp_iternext` function must return `NULL`; a [`StopIteration`](https://docs.python.org/3/builtins/exceptions.html#StopIteration "StopIteration")
 exception may or may not be set. When another error occurs, it must return `NULL` too. The presence of `tp_iternext` signals that the instances of this type are iterators.

Iterator types should also define the [`tp_iter`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_iter "PyTypeObject.tp_iter")
 function, and that function should return the iterator instance itself (not a new iterator instance).

This function has the same signature as [`PyIter_Next()`](https://docs.python.org/3/c-api/iter.html#c.PyIter_Next "PyIter_Next")
.

**Inheritance:**

This field is inherited by subtypes.

struct [PyMethodDef](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")
 \*[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_methods[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_methods "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_methods` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to a static `NULL`\-terminated array of [`PyMethodDef`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")
 structures, declaring regular methods of this type.

For each entry in the array, an entry is added to the type’s dictionary (see [`tp_dict`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dict "PyTypeObject.tp_dict")
 below) containing a method descriptor.

**Inheritance:**

This field is not inherited by subtypes (methods are inherited through a different mechanism).

struct [PyMemberDef](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef "PyMemberDef")
 \*[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_members[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_members "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_members` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to a static `NULL`\-terminated array of [`PyMemberDef`](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef "PyMemberDef")
 structures, declaring regular data members (fields or slots) of instances of this type.

For each entry in the array, an entry is added to the type’s dictionary (see [`tp_dict`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dict "PyTypeObject.tp_dict")
 below) containing a member descriptor.

**Inheritance:**

This field is not inherited by subtypes (members are inherited through a different mechanism).

struct [PyGetSetDef](https://docs.python.org/3/c-api/structures.html#c.PyGetSetDef "PyGetSetDef")
 \*[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_getset[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getset "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_getset` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to a static `NULL`\-terminated array of [`PyGetSetDef`](https://docs.python.org/3/c-api/structures.html#c.PyGetSetDef "PyGetSetDef")
 structures, declaring computed attributes of instances of this type.

For each entry in the array, an entry is added to the type’s dictionary (see [`tp_dict`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dict "PyTypeObject.tp_dict")
 below) containing a getset descriptor.

**Inheritance:**

This field is not inherited by subtypes (computed attributes are inherited through a different mechanism).

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_base[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_base "Link to this definition")
  

An optional pointer to a base type from which type properties are inherited. At this level, only single inheritance is supported; multiple inheritance require dynamically creating a type object by calling the metatype.

For the corresponding slot ID, see [`Py_tp_base`](https://docs.python.org/3/c-api/type.html#c.Py_tp_base "Py_tp_base")
.

Note

Slot initialization is subject to the rules of initializing globals. C99 requires the initializers to be “address constants”. Function designators like [`PyType_GenericNew()`](https://docs.python.org/3/c-api/type.html#c.PyType_GenericNew "PyType_GenericNew")
, with implicit conversion to a pointer, are valid C99 address constants.

However, the unary ‘&’ operator applied to a non-static variable like [`PyBaseObject_Type`](https://docs.python.org/3/c-api/structures.html#c.PyBaseObject_Type "PyBaseObject_Type")
 is not required to produce an address constant. Compilers may support this (gcc does), MSVC does not. Both compilers are strictly standard conforming in this particular behavior.

Consequently, [`tp_base`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_base "PyTypeObject.tp_base")
 should be set in the extension module’s init function.

**Inheritance:**

This field is not inherited by subtypes (obviously).

**Default:**

This field defaults to `&PyBaseObject_Type` (which to Python programmers is known as the type [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
).

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_dict[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dict "Link to this definition")
  

The type’s dictionary is stored here by [`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
.

This field should normally be initialized to `NULL` before PyType\_Ready is called; it may also be initialized to a dictionary containing initial attributes for the type. Once [`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
 has initialized the type, extra attributes for the type may be added to this dictionary only if they don’t correspond to overloaded operations (like [`__add__()`](https://docs.python.org/3/reference/datamodel.html#object.__add__ "object.__add__")
). Once initialization for the type has finished, this field should be treated as read-only.

Some types may not store their dictionary in this slot. Use [`PyType_GetDict()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetDict "PyType_GetDict")
 to retrieve the dictionary for an arbitrary type.

Changed in version 3.12: Internals detail: For static builtin types, this is always `NULL`. Instead, the dict for such types is stored on `PyInterpreterState`. Use [`PyType_GetDict()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetDict "PyType_GetDict")
 to get the dict for an arbitrary type.

**Inheritance:**

This field is not inherited by subtypes (though the attributes defined in here are inherited through a different mechanism).

**Default:**

If this field is `NULL`, [`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
 will assign a new dictionary to it.

Warning

It is not safe to use [`PyDict_SetItem()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_SetItem "PyDict_SetItem")
 on or otherwise modify [`tp_dict`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dict "PyTypeObject.tp_dict")
 with the dictionary C-API.

[descrgetfunc](https://docs.python.org/3/c-api/typeobj.html#c.descrgetfunc "descrgetfunc")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_descr\_get[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_descr_get "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_descr_get` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to a “descriptor get” function.

The function signature is:

PyObject \* tp\_descr\_get(PyObject \*self, PyObject \*obj, PyObject \*type);

**Inheritance:**

This field is inherited by subtypes.

[descrsetfunc](https://docs.python.org/3/c-api/typeobj.html#c.descrsetfunc "descrsetfunc")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_descr\_set[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_descr_set "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_descr_set` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to a function for setting and deleting a descriptor’s value.

The function signature is:

int tp\_descr\_set(PyObject \*self, PyObject \*obj, PyObject \*value);

The _value_ argument is set to `NULL` to delete the value.

**Inheritance:**

This field is inherited by subtypes.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_dictoffset[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dictoffset "Link to this definition")
  

While this field is still supported, [`Py_TPFLAGS_MANAGED_DICT`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT "Py_TPFLAGS_MANAGED_DICT")
 should be used instead, if at all possible.

If the instances of this type have a dictionary containing instance variables, this field is non-zero and contains the offset in the instances of the type of the instance variable dictionary; this offset is used by [`PyObject_GenericGetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GenericGetAttr "PyObject_GenericGetAttr")
.

Do not confuse this field with [`tp_dict`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dict "PyTypeObject.tp_dict")
; that is the dictionary for attributes of the type object itself.

The value specifies the offset of the dictionary from the start of the instance structure.

The [`tp_dictoffset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dictoffset "PyTypeObject.tp_dictoffset")
 should be regarded as write-only. To get the pointer to the dictionary call [`PyObject_GenericGetDict()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GenericGetDict "PyObject_GenericGetDict")
. Calling `PyObject_GenericGetDict()` may need to allocate memory for the dictionary, so it is may be more efficient to call [`PyObject_GetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAttr "PyObject_GetAttr")
 when accessing an attribute on the object.

It is an error to set both the [`Py_TPFLAGS_MANAGED_DICT`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT "Py_TPFLAGS_MANAGED_DICT")
 bit and [`tp_dictoffset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dictoffset "PyTypeObject.tp_dictoffset")
.

**Inheritance:**

This field is inherited by subtypes. A subtype should not override this offset; doing so could be unsafe, if C code tries to access the dictionary at the previous offset. To properly support inheritance, use [`Py_TPFLAGS_MANAGED_DICT`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT "Py_TPFLAGS_MANAGED_DICT")
.

**Default:**

This slot has no default. For [static types](https://docs.python.org/3/c-api/typeobj.html#static-types)
, if the field is `NULL` then no [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")
 gets created for instances.

If the [`Py_TPFLAGS_MANAGED_DICT`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT "Py_TPFLAGS_MANAGED_DICT")
 bit is set in the [`tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags")
 field, then [`tp_dictoffset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dictoffset "PyTypeObject.tp_dictoffset")
 will be set to `-1`, to indicate that it is unsafe to use this field.

[initproc](https://docs.python.org/3/c-api/typeobj.html#c.initproc "initproc")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_init[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_init "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_init` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to an instance initialization function.

This function corresponds to the [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__")
 method of classes. Like `__init__()`, it is possible to create an instance without calling `__init__()`, and it is possible to reinitialize an instance by calling its `__init__()` method again.

The function signature is:

int tp\_init(PyObject \*self, PyObject \*args, PyObject \*kwds);

The self argument is the instance to be initialized; the _args_ and _kwds_ arguments represent positional and keyword arguments of the call to [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__")
.

The [`tp_init`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_init "PyTypeObject.tp_init")
 function, if not `NULL`, is called when an instance is created normally by calling its type, after the type’s [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 function has returned an instance of the type. If the `tp_new` function returns an instance of some other type that is not a subtype of the original type, no `tp_init` function is called; if `tp_new` returns an instance of a subtype of the original type, the subtype’s `tp_init` is called.

Returns `0` on success, `-1` and sets an exception on error.

**Inheritance:**

This field is inherited by subtypes.

**Default:**

For [static types](https://docs.python.org/3/c-api/typeobj.html#static-types)
 this field does not have a default.

[allocfunc](https://docs.python.org/3/c-api/typeobj.html#c.allocfunc "allocfunc")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_alloc[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_alloc` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to an instance allocation function.

The function signature is:

PyObject \*tp\_alloc(PyTypeObject \*self, Py\_ssize\_t nitems);

**Inheritance:**

Static subtypes inherit this slot, which will be [`PyType_GenericAlloc()`](https://docs.python.org/3/c-api/type.html#c.PyType_GenericAlloc "PyType_GenericAlloc")
 if inherited from [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
.

[Heap subtypes](https://docs.python.org/3/c-api/typeobj.html#heap-types)
 do not inherit this slot.

**Default:**

For heap subtypes, this field is always set to [`PyType_GenericAlloc()`](https://docs.python.org/3/c-api/type.html#c.PyType_GenericAlloc "PyType_GenericAlloc")
.

For static subtypes, this slot is inherited (see above).

[newfunc](https://docs.python.org/3/c-api/typeobj.html#c.newfunc "newfunc")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_new[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_new` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to an instance creation function.

The function signature is:

PyObject \*tp\_new(PyTypeObject \*subtype, PyObject \*args, PyObject \*kwds);

The _subtype_ argument is the type of the object being created; the _args_ and _kwds_ arguments represent positional and keyword arguments of the call to the type. Note that _subtype_ doesn’t have to equal the type whose [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 function is called; it may be a subtype of that type (but not an unrelated type).

The [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 function should call `subtype->tp_alloc(subtype, nitems)` to allocate space for the object, and then do only as much further initialization as is absolutely necessary. Initialization that can safely be ignored or repeated should be placed in the [`tp_init`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_init "PyTypeObject.tp_init")
 handler. A good rule of thumb is that for immutable types, all initialization should take place in `tp_new`, while for mutable types, most initialization should be deferred to `tp_init`.

Set the [`Py_TPFLAGS_DISALLOW_INSTANTIATION`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_DISALLOW_INSTANTIATION "Py_TPFLAGS_DISALLOW_INSTANTIATION")
 flag to disallow creating instances of the type in Python.

**Inheritance:**

This field is inherited by subtypes, except it is not inherited by [static types](https://docs.python.org/3/c-api/typeobj.html#static-types)
 whose [`tp_base`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_base "PyTypeObject.tp_base")
 is `NULL` or `&PyBaseObject_Type`.

**Default:**

For [static types](https://docs.python.org/3/c-api/typeobj.html#static-types)
 this field has no default. This means if the slot is defined as `NULL`, the type cannot be called to create new instances; presumably there is some other way to create instances, like a factory function.

[freefunc](https://docs.python.org/3/c-api/typeobj.html#c.freefunc "freefunc")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_free[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_free "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_free` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to an instance deallocation function. Its signature is:

void tp\_free(void \*self);

This function must free the memory allocated by [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
.

**Inheritance:**

Static subtypes inherit this slot, which will be [`PyObject_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Free "PyObject_Free")
 if inherited from [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
. Exception: If the type supports garbage collection (i.e., the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 flag is set in [`tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags")
) and it would inherit `PyObject_Free()`, then this slot is not inherited but instead defaults to [`PyObject_GC_Del()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_Del "PyObject_GC_Del")
.

[Heap subtypes](https://docs.python.org/3/c-api/typeobj.html#heap-types)
 do not inherit this slot.

**Default:**

For [heap subtypes](https://docs.python.org/3/c-api/typeobj.html#heap-types)
, this slot defaults to a deallocator suitable to match [`PyType_GenericAlloc()`](https://docs.python.org/3/c-api/type.html#c.PyType_GenericAlloc "PyType_GenericAlloc")
 and the value of the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 flag.

For static subtypes, this slot is inherited (see above).

[inquiry](https://docs.python.org/3/c-api/gcsupport.html#c.inquiry "inquiry")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_is\_gc[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_is_gc "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_is_gc` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

An optional pointer to a function called by the garbage collector.

The garbage collector needs to know whether a particular object is collectible or not. Normally, it is sufficient to look at the object’s type’s [`tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags")
 field, and check the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 flag bit. But some types have a mixture of statically and dynamically allocated instances, and the statically allocated instances are not collectible. Such types should define this function; it should return `1` for a collectible instance, and `0` for a non-collectible instance. The signature is:

int tp\_is\_gc(PyObject \*self);

(The only example of this are types themselves. The metatype, [`PyType_Type`](https://docs.python.org/3/c-api/type.html#c.PyType_Type "PyType_Type")
, defines this function to distinguish between statically and [dynamically allocated types](https://docs.python.org/3/c-api/typeobj.html#heap-types)
.)

**Inheritance:**

This field is inherited by subtypes.

**Default:**

This slot has no default. If this field is `NULL`, [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 is used as the functional equivalent.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_bases[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_bases "Link to this definition")
  

Tuple of base types.

This field should be set to `NULL` and treated as read-only. Python will fill it in when the type is [`initialized`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
.

For the corresponding slot ID, see [`Py_tp_bases`](https://docs.python.org/3/c-api/type.html#c.Py_tp_bases "Py_tp_bases")
.

Warning

Multiple inheritance does not work well for statically defined types. If you set `tp_bases` to a tuple, Python will not raise an error, but some slots will only be inherited from the first base.

**Inheritance:**

This field is not inherited.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_mro[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_mro "Link to this definition")
  

Tuple containing the expanded set of base types, starting with the type itself and ending with [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
, in Method Resolution Order.

This field should be set to `NULL` and treated as read-only. Python will fill it in when the type is [`initialized`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
.

**Inheritance:**

This field is not inherited; it is calculated fresh by [`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_cache[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_cache "Link to this definition")
  

Unused. Internal use only.

**Inheritance:**

This field is not inherited.

void \*[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_subclasses[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_subclasses "Link to this definition")
  

A collection of subclasses. Internal use only. May be an invalid pointer.

To get a list of subclasses, call the Python method [`__subclasses__()`](https://docs.python.org/3/reference/datamodel.html#type.__subclasses__ "type.__subclasses__")
.

Changed in version 3.12: For some types, this field does not hold a valid [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*. The type was changed to void\* to indicate this.

**Inheritance:**

This field is not inherited.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_weaklist[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_weaklist "Link to this definition")
  

Weak reference list head, for weak references to this type object. Not inherited. Internal use only.

Changed in version 3.12: Internals detail: For the static builtin types this is always `NULL`, even if weakrefs are added. Instead, the weakrefs for each are stored on `PyInterpreterState`. Use the public C-API or the internal `_PyObject_GET_WEAKREFS_LISTPTR()` macro to avoid the distinction.

**Inheritance:**

This field is not inherited.

[destructor](https://docs.python.org/3/c-api/typeobj.html#c.destructor "destructor")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_del[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_del "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_del` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This field is deprecated. Use [`tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "PyTypeObject.tp_finalize")
 instead.

unsigned int [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_version\_tag[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_version_tag "Link to this definition")
  

Used to index into the method cache. Internal use only.

**Inheritance:**

This field is not inherited.

[destructor](https://docs.python.org/3/c-api/typeobj.html#c.destructor "destructor")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_finalize[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_finalize` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.5._

An optional pointer to an instance finalization function. This is the C implementation of the [`__del__()`](https://docs.python.org/3/reference/datamodel.html#object.__del__ "object.__del__")
 special method. Its signature is:

void tp\_finalize(PyObject \*self);

The primary purpose of finalization is to perform any non-trivial cleanup that must be performed before the object is destroyed, while the object and any other objects it directly or indirectly references are still in a consistent state. The finalizer is allowed to execute arbitrary Python code.

Before Python automatically finalizes an object, some of the object’s direct or indirect referents might have themselves been automatically finalized. However, none of the referents will have been automatically cleared ([`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
) yet.

Other non-finalized objects might still be using a finalized object, so the finalizer must leave the object in a sane state (e.g., invariants are still met).

Note

After Python automatically finalizes an object, Python might start automatically clearing ([`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
) the object and its referents (direct and indirect). Cleared objects are not guaranteed to be in a consistent state; a finalized object must be able to tolerate cleared referents.

Note

An object is not guaranteed to be automatically finalized before its destructor ([`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
) is called. It is recommended to call [`PyObject_CallFinalizerFromDealloc()`](https://docs.python.org/3/c-api/lifecycle.html#c.PyObject_CallFinalizerFromDealloc "PyObject_CallFinalizerFromDealloc")
 at the beginning of `tp_dealloc` to guarantee that the object is always finalized before destruction.

Note

The [`tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "PyTypeObject.tp_finalize")
 function can be called from any thread, although the [GIL](https://docs.python.org/3/glossary.html#term-GIL)
 will be held.

Note

The `tp_finalize` function can be called during shutdown, after some global variables have been deleted. See the documentation of the [`__del__()`](https://docs.python.org/3/reference/datamodel.html#object.__del__ "object.__del__")
 method for details.

When Python finalizes an object, it behaves like the following algorithm:

1.  Python might mark the object as _finalized_. Currently, Python always marks objects whose type supports garbage collection (i.e., the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
     flag is set in [`tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags")
    ) and never marks other types of objects; this might change in a future version.
    
2.  If the object is not marked as _finalized_ and its `tp_finalize` finalizer function is non-`NULL`, the finalizer function is called.
    
3.  If the finalizer function was called and the finalizer made the object reachable (i.e., there is a reference to the object and it is not a member of a [cyclic isolate](https://docs.python.org/3/glossary.html#term-cyclic-isolate)
    ), then the finalizer is said to have _resurrected_ the object. It is unspecified whether the finalizer can also resurrect the object by adding a new reference to the object that does not make it reachable, i.e., the object is (still) a member of a cyclic isolate.
    
4.  If the finalizer resurrected the object, the object’s pending destruction is canceled and the object’s _finalized_ mark might be removed if present. Currently, Python never removes the _finalized_ mark; this might change in a future version.
    

_Automatic finalization_ refers to any finalization performed by Python except via calls to [`PyObject_CallFinalizer()`](https://docs.python.org/3/c-api/lifecycle.html#c.PyObject_CallFinalizer "PyObject_CallFinalizer")
 or [`PyObject_CallFinalizerFromDealloc()`](https://docs.python.org/3/c-api/lifecycle.html#c.PyObject_CallFinalizerFromDealloc "PyObject_CallFinalizerFromDealloc")
. No guarantees are made about when, if, or how often an object is automatically finalized, except:

*   Python will not automatically finalize an object if it is reachable, i.e., there is a reference to it and it is not a member of a [cyclic isolate](https://docs.python.org/3/glossary.html#term-cyclic-isolate)
    .
    
*   Python will not automatically finalize an object if finalizing it would not mark the object as _finalized_. Currently, this applies to objects whose type does not support garbage collection, i.e., the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
     flag is not set. Such objects can still be manually finalized by calling [`PyObject_CallFinalizer()`](https://docs.python.org/3/c-api/lifecycle.html#c.PyObject_CallFinalizer "PyObject_CallFinalizer")
     or [`PyObject_CallFinalizerFromDealloc()`](https://docs.python.org/3/c-api/lifecycle.html#c.PyObject_CallFinalizerFromDealloc "PyObject_CallFinalizerFromDealloc")
    .
    
*   Python will not automatically finalize any two members of a [cyclic isolate](https://docs.python.org/3/glossary.html#term-cyclic-isolate)
     concurrently.
    
*   Python will not automatically finalize an object after it has automatically cleared ([`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
    ) the object.
    
*   If an object is a member of a [cyclic isolate](https://docs.python.org/3/glossary.html#term-cyclic-isolate)
    , Python will not automatically finalize it after automatically clearing (see [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
    ) any other member.
    
*   Python will automatically finalize every member of a [cyclic isolate](https://docs.python.org/3/glossary.html#term-cyclic-isolate)
     before it automatically clears (see [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
    ) any of them.
    
*   If Python is going to automatically clear an object ([`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
    ), it will automatically finalize the object first.
    

Python currently only automatically finalizes objects that are members of a [cyclic isolate](https://docs.python.org/3/glossary.html#term-cyclic-isolate)
, but future versions might finalize objects regularly before their destruction.

To manually finalize an object, do not call this function directly; call [`PyObject_CallFinalizer()`](https://docs.python.org/3/c-api/lifecycle.html#c.PyObject_CallFinalizer "PyObject_CallFinalizer")
 or [`PyObject_CallFinalizerFromDealloc()`](https://docs.python.org/3/c-api/lifecycle.html#c.PyObject_CallFinalizerFromDealloc "PyObject_CallFinalizerFromDealloc")
 instead.

[`tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "PyTypeObject.tp_finalize")
 should leave the current exception status unchanged. The recommended way to write a non-trivial finalizer is to back up the exception at the beginning by calling [`PyErr_GetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetRaisedException "PyErr_GetRaisedException")
 and restore the exception at the end by calling [`PyErr_SetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetRaisedException "PyErr_SetRaisedException")
. If an exception is encountered in the middle of the finalizer, log and clear it with [`PyErr_WriteUnraisable()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WriteUnraisable "PyErr_WriteUnraisable")
 or [`PyErr_FormatUnraisable()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_FormatUnraisable "PyErr_FormatUnraisable")
. For example:

static void
foo\_finalize(PyObject \*self)
{
    // Save the current exception, if any.
    PyObject \*exc \= PyErr\_GetRaisedException();

    // ...

    if (do\_something\_that\_might\_raise() != success\_indicator) {
        PyErr\_WriteUnraisable(self);
        goto done;
    }

done:
    // Restore the saved exception.  This silently discards any exception
    // raised above, so be sure to call PyErr\_WriteUnraisable first if
    // necessary.
    PyErr\_SetRaisedException(exc);
}

**Inheritance:**

This field is inherited by subtypes.

Added in version 3.4.

Changed in version 3.8: Before version 3.8 it was necessary to set the [`Py_TPFLAGS_HAVE_FINALIZE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_FINALIZE "Py_TPFLAGS_HAVE_FINALIZE")
 flags bit in order for this field to be used. This is no longer required.

See also

*   [**PEP 442**](https://peps.python.org/pep-0442/)
    : “Safe object finalization”
    
*   [Object Life Cycle](https://docs.python.org/3/c-api/lifecycle.html#life-cycle)
     for details about how this slot relates to other slots.
    
*   [`PyObject_CallFinalizer()`](https://docs.python.org/3/c-api/lifecycle.html#c.PyObject_CallFinalizer "PyObject_CallFinalizer")
    
*   [`PyObject_CallFinalizerFromDealloc()`](https://docs.python.org/3/c-api/lifecycle.html#c.PyObject_CallFinalizerFromDealloc "PyObject_CallFinalizerFromDealloc")
    

[vectorcallfunc](https://docs.python.org/3/c-api/call.html#c.vectorcallfunc "vectorcallfunc")
 [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_vectorcall[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_vectorcall "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_tp_vectorcall` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.14._

A [vectorcall function](https://docs.python.org/3/c-api/call.html#vectorcall)
 to use for calls of this type object (rather than instances). In other words, `tp_vectorcall` can be used to optimize `type.__call__`, which typically returns a new instance of _type_.

As with any vectorcall function, if `tp_vectorcall` is `NULL`, the _tp\_call_ protocol (`Py_TYPE(type)->tp_call`) is used instead.

Note

The [vectorcall protocol](https://docs.python.org/3/c-api/call.html#vectorcall)
 requires that the vectorcall function has the same behavior as the corresponding `tp_call`. This means that `type->tp_vectorcall` must match the behavior of `Py_TYPE(type)->tp_call`.

Specifically, if _type_ uses the default metaclass, `type->tp_vectorcall` must behave the same as `Py_TYPE(type)->tp_call`, which:

*   calls `type->tp_new`,
    
*   if the result is a subclass of _type_, calls `type->tp_init` on the result of `tp_new`, and
    
*   returns the result of `tp_new`.
    

Typically, `tp_vectorcall` is overridden to optimize this process for specific [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 and [`tp_init`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_init "PyTypeObject.tp_init")
. When doing this for user-subclassable types, note that both can be overridden (using [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__")
 and [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__")
, respectively).

**Inheritance:**

This field is never inherited.

Added in version 3.9: (the field exists since 3.8 but it’s only used since 3.9)

unsigned char [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
.tp\_watched[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_watched "Link to this definition")
  

Internal. Do not use.

Added in version 3.12.

Static Types[¶](https://docs.python.org/3/c-api/typeobj.html#static-types "Link to this heading")

--------------------------------------------------------------------------------------------------

Traditionally, types defined in C code are _static_, that is, a static [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 structure is defined directly in code and initialized using [`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
.

This results in types that are limited relative to types defined in Python:

*   Static types are limited to one base, i.e. they cannot use multiple inheritance.
    
*   Static type objects (but not necessarily their instances) are immutable. It is not possible to add or modify the type object’s attributes from Python.
    
*   Static type objects are shared across [sub-interpreters](https://docs.python.org/3/c-api/subinterpreters.html#sub-interpreter-support)
    , so they should not include any subinterpreter-specific state.
    

Also, since [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 is only part of the [Limited API](https://docs.python.org/3/c-api/stable.html#limited-c-api)
 as an opaque struct, any extension modules using static types must be compiled for a specific Python minor version.

Heap Types[¶](https://docs.python.org/3/c-api/typeobj.html#heap-types "Link to this heading")

----------------------------------------------------------------------------------------------

An alternative to [static types](https://docs.python.org/3/c-api/typeobj.html#static-types)
 is _heap-allocated types_, or _heap types_ for short, which correspond closely to classes created by Python’s `class` statement. Heap types have the [`Py_TPFLAGS_HEAPTYPE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HEAPTYPE "Py_TPFLAGS_HEAPTYPE")
 flag set.

This is done by filling a [`PyType_Spec`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec "PyType_Spec")
 structure and calling [`PyType_FromSpec()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSpec "PyType_FromSpec")
, [`PyType_FromSpecWithBases()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSpecWithBases "PyType_FromSpecWithBases")
, [`PyType_FromModuleAndSpec()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromModuleAndSpec "PyType_FromModuleAndSpec")
, or [`PyType_FromMetaclass()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromMetaclass "PyType_FromMetaclass")
.

Number Object Structures[¶](https://docs.python.org/3/c-api/typeobj.html#number-object-structures "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

type PyNumberMethods[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "Link to this definition")
  

This structure holds pointers to the functions which an object uses to implement the number protocol. Each function is used by the function of similar name documented in the [Number Protocol](https://docs.python.org/3/c-api/number.html#number)
 section.

Here is the structure definition:

typedef struct {
     binaryfunc nb\_add;
     binaryfunc nb\_subtract;
     binaryfunc nb\_multiply;
     binaryfunc nb\_remainder;
     binaryfunc nb\_divmod;
     ternaryfunc nb\_power;
     unaryfunc nb\_negative;
     unaryfunc nb\_positive;
     unaryfunc nb\_absolute;
     inquiry nb\_bool;
     unaryfunc nb\_invert;
     binaryfunc nb\_lshift;
     binaryfunc nb\_rshift;
     binaryfunc nb\_and;
     binaryfunc nb\_xor;
     binaryfunc nb\_or;
     unaryfunc nb\_int;
     void \*nb\_reserved;
     unaryfunc nb\_float;

     binaryfunc nb\_inplace\_add;
     binaryfunc nb\_inplace\_subtract;
     binaryfunc nb\_inplace\_multiply;
     binaryfunc nb\_inplace\_remainder;
     ternaryfunc nb\_inplace\_power;
     binaryfunc nb\_inplace\_lshift;
     binaryfunc nb\_inplace\_rshift;
     binaryfunc nb\_inplace\_and;
     binaryfunc nb\_inplace\_xor;
     binaryfunc nb\_inplace\_or;

     binaryfunc nb\_floor\_divide;
     binaryfunc nb\_true\_divide;
     binaryfunc nb\_inplace\_floor\_divide;
     binaryfunc nb\_inplace\_true\_divide;

     unaryfunc nb\_index;

     binaryfunc nb\_matrix\_multiply;
     binaryfunc nb\_inplace\_matrix\_multiply;
} PyNumberMethods;

Note

Binary and ternary functions must check the type of all their operands, and implement the necessary conversions (at least one of the operands is an instance of the defined type). If the operation is not defined for the given operands, binary and ternary functions must return `Py_NotImplemented`, if another error occurred they must return `NULL` and set an exception.

Note

The [`nb_reserved`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_reserved "PyNumberMethods.nb_reserved")
 field should always be `NULL`. It was previously called `nb_long`, and was renamed in Python 3.0.1.

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_add[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_add "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_add` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_subtract[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_subtract "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_subtract` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_multiply[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_multiply "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_multiply` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_remainder[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_remainder "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_remainder` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_divmod[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_divmod "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_divmod` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[ternaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.ternaryfunc "ternaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_power[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_power "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_power` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[unaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_negative[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_negative "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_negative` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[unaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_positive[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_positive "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_positive` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[unaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_absolute[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_absolute "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_absolute` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[inquiry](https://docs.python.org/3/c-api/gcsupport.html#c.inquiry "inquiry")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_bool[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_bool "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_bool` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[unaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_invert[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_invert "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_invert` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_lshift[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_lshift "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_lshift` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_rshift[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_rshift "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_rshift` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_and[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_and "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_and` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_xor[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_xor "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_xor` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_or[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_or "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_or` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[unaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_int[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_int "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_int` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

void \*[PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_reserved[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_reserved "Link to this definition")
  

[unaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_float[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_float "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_float` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_inplace\_add[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_add "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_inplace_add` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_inplace\_subtract[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_subtract "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_inplace_subtract` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_inplace\_multiply[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_multiply "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_inplace_multiply` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_inplace\_remainder[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_remainder "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_inplace_remainder` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[ternaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.ternaryfunc "ternaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_inplace\_power[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_power "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_inplace_power` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_inplace\_lshift[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_lshift "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_inplace_lshift` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_inplace\_rshift[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_rshift "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_inplace_rshift` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_inplace\_and[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_and "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_inplace_and` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_inplace\_xor[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_xor "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_inplace_xor` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_inplace\_or[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_or "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_inplace_or` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_floor\_divide[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_floor_divide "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_floor_divide` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_true\_divide[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_true_divide "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_true_divide` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_inplace\_floor\_divide[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_floor_divide "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_inplace_floor_divide` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_inplace\_true\_divide[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_true_divide "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_inplace_true_divide` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[unaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_index[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_index "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_index` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_matrix\_multiply[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_matrix_multiply "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_matrix_multiply` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.5._

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyNumberMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
.nb\_inplace\_matrix\_multiply[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_matrix_multiply "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_nb_inplace_matrix_multiply` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.5._

Mapping Object Structures[¶](https://docs.python.org/3/c-api/typeobj.html#mapping-object-structures "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

type PyMappingMethods[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyMappingMethods "Link to this definition")
  

This structure holds pointers to the functions which an object uses to implement the mapping protocol. It has three members:

[lenfunc](https://docs.python.org/3/c-api/typeobj.html#c.lenfunc "lenfunc")
 [PyMappingMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyMappingMethods "PyMappingMethods")
.mp\_length[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyMappingMethods.mp_length "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_mp_length` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This function is used by [`PyMapping_Size()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_Size "PyMapping_Size")
 and [`PyObject_Size()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Size "PyObject_Size")
, and has the same signature. This slot may be set to `NULL` if the object has no defined length.

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PyMappingMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyMappingMethods "PyMappingMethods")
.mp\_subscript[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyMappingMethods.mp_subscript "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_mp_subscript` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This function is used by [`PyObject_GetItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetItem "PyObject_GetItem")
 and [`PySequence_GetSlice()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_GetSlice "PySequence_GetSlice")
, and has the same signature as `PyObject_GetItem()`. This slot must be filled for the [`PyMapping_Check()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_Check "PyMapping_Check")
 function to return `1`, it can be `NULL` otherwise.

[objobjargproc](https://docs.python.org/3/c-api/typeobj.html#c.objobjargproc "objobjargproc")
 [PyMappingMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyMappingMethods "PyMappingMethods")
.mp\_ass\_subscript[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyMappingMethods.mp_ass_subscript "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_mp_ass_subscript` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This function is used by [`PyObject_SetItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_SetItem "PyObject_SetItem")
, [`PyObject_DelItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_DelItem "PyObject_DelItem")
, [`PySequence_SetSlice()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_SetSlice "PySequence_SetSlice")
 and [`PySequence_DelSlice()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_DelSlice "PySequence_DelSlice")
. It has the same signature as `PyObject_SetItem()`, but _v_ can also be set to `NULL` to delete an item. If this slot is `NULL`, the object does not support item assignment and deletion.

Sequence Object Structures[¶](https://docs.python.org/3/c-api/typeobj.html#sequence-object-structures "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

type PySequenceMethods[¶](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods "Link to this definition")
  

This structure holds pointers to the functions which an object uses to implement the sequence protocol.

[lenfunc](https://docs.python.org/3/c-api/typeobj.html#c.lenfunc "lenfunc")
 [PySequenceMethods](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods "PySequenceMethods")
.sq\_length[¶](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods.sq_length "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_sq_length` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This function is used by [`PySequence_Size()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Size "PySequence_Size")
 and [`PyObject_Size()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Size "PyObject_Size")
, and has the same signature. It is also used for handling negative indices via the [`sq_item`](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods.sq_item "PySequenceMethods.sq_item")
 and the [`sq_ass_item`](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods.sq_ass_item "PySequenceMethods.sq_ass_item")
 slots.

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PySequenceMethods](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods "PySequenceMethods")
.sq\_concat[¶](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods.sq_concat "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_sq_concat` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This function is used by [`PySequence_Concat()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Concat "PySequence_Concat")
 and has the same signature. It is also used by the `+` operator, after trying the numeric addition via the [`nb_add`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_add "PyNumberMethods.nb_add")
 slot.

[ssizeargfunc](https://docs.python.org/3/c-api/typeobj.html#c.ssizeargfunc "ssizeargfunc")
 [PySequenceMethods](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods "PySequenceMethods")
.sq\_repeat[¶](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods.sq_repeat "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_sq_repeat` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This function is used by [`PySequence_Repeat()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Repeat "PySequence_Repeat")
 and has the same signature. It is also used by the `*` operator, after trying numeric multiplication via the [`nb_multiply`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_multiply "PyNumberMethods.nb_multiply")
 slot.

[ssizeargfunc](https://docs.python.org/3/c-api/typeobj.html#c.ssizeargfunc "ssizeargfunc")
 [PySequenceMethods](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods "PySequenceMethods")
.sq\_item[¶](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods.sq_item "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_sq_item` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This function is used by [`PySequence_GetItem()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_GetItem "PySequence_GetItem")
 and has the same signature. It is also used by [`PyObject_GetItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetItem "PyObject_GetItem")
, after trying the subscription via the [`mp_subscript`](https://docs.python.org/3/c-api/typeobj.html#c.PyMappingMethods.mp_subscript "PyMappingMethods.mp_subscript")
 slot. This slot must be filled for the [`PySequence_Check()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Check "PySequence_Check")
 function to return `1`, it can be `NULL` otherwise.

Negative indexes are handled as follows: if the [`sq_length`](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods.sq_length "PySequenceMethods.sq_length")
 slot is filled, it is called and the sequence length is used to compute a positive index which is passed to [`sq_item`](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods.sq_item "PySequenceMethods.sq_item")
. If `sq_length` is `NULL`, the index is passed as is to the function.

[ssizeobjargproc](https://docs.python.org/3/c-api/typeobj.html#c.ssizeobjargproc "ssizeobjargproc")
 [PySequenceMethods](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods "PySequenceMethods")
.sq\_ass\_item[¶](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods.sq_ass_item "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_sq_ass_item` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This function is used by [`PySequence_SetItem()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_SetItem "PySequence_SetItem")
 and has the same signature. It is also used by [`PyObject_SetItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_SetItem "PyObject_SetItem")
 and [`PyObject_DelItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_DelItem "PyObject_DelItem")
, after trying the item assignment and deletion via the [`mp_ass_subscript`](https://docs.python.org/3/c-api/typeobj.html#c.PyMappingMethods.mp_ass_subscript "PyMappingMethods.mp_ass_subscript")
 slot. This slot may be left to `NULL` if the object does not support item assignment and deletion.

[objobjproc](https://docs.python.org/3/c-api/typeobj.html#c.objobjproc "objobjproc")
 [PySequenceMethods](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods "PySequenceMethods")
.sq\_contains[¶](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods.sq_contains "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_sq_contains` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This function may be used by [`PySequence_Contains()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Contains "PySequence_Contains")
 and has the same signature. This slot may be left to `NULL`, in this case `PySequence_Contains()` simply traverses the sequence until it finds a match.

[binaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
 [PySequenceMethods](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods "PySequenceMethods")
.sq\_inplace\_concat[¶](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods.sq_inplace_concat "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_sq_inplace_concat` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This function is used by [`PySequence_InPlaceConcat()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_InPlaceConcat "PySequence_InPlaceConcat")
 and has the same signature. It should modify its first operand, and return it. This slot may be left to `NULL`, in this case `PySequence_InPlaceConcat()` will fall back to [`PySequence_Concat()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Concat "PySequence_Concat")
. It is also used by the augmented assignment `+=`, after trying numeric in-place addition via the [`nb_inplace_add`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_add "PyNumberMethods.nb_inplace_add")
 slot.

[ssizeargfunc](https://docs.python.org/3/c-api/typeobj.html#c.ssizeargfunc "ssizeargfunc")
 [PySequenceMethods](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods "PySequenceMethods")
.sq\_inplace\_repeat[¶](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods.sq_inplace_repeat "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_sq_inplace_repeat` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This function is used by [`PySequence_InPlaceRepeat()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_InPlaceRepeat "PySequence_InPlaceRepeat")
 and has the same signature. It should modify its first operand, and return it. This slot may be left to `NULL`, in this case `PySequence_InPlaceRepeat()` will fall back to [`PySequence_Repeat()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Repeat "PySequence_Repeat")
. It is also used by the augmented assignment `*=`, after trying numeric in-place multiplication via the [`nb_inplace_multiply`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_inplace_multiply "PyNumberMethods.nb_inplace_multiply")
 slot.

Buffer Object Structures[¶](https://docs.python.org/3/c-api/typeobj.html#buffer-object-structures "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

type PyBufferProcs[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyBufferProcs "Link to this definition")
  

This structure holds pointers to the functions required by the [Buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects)
. The protocol defines how an exporter object can expose its internal data to consumer objects.

[getbufferproc](https://docs.python.org/3/c-api/typeobj.html#c.getbufferproc "getbufferproc")
 [PyBufferProcs](https://docs.python.org/3/c-api/typeobj.html#c.PyBufferProcs "PyBufferProcs")
.bf\_getbuffer[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyBufferProcs.bf_getbuffer "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_bf_getbuffer` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

The signature of this function is:

int (PyObject \*exporter, Py\_buffer \*view, int flags);

Handle a request to _exporter_ to fill in _view_ as specified by _flags_. Except for point (3), an implementation of this function MUST take these steps:

1.  Check if the request can be met. If not, raise [`BufferError`](https://docs.python.org/3/builtins/exceptions.html#BufferError "BufferError")
    , set `view->obj` to `NULL` and return `-1`.
    
2.  Fill in the requested fields.
    
3.  Increment an internal counter for the number of exports.
    
4.  Set `view->obj` to _exporter_ and increment `view->obj`.
    
5.  Return `0`.
    

**Thread safety:**

In the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
, implementations must ensure:

*   The export counter increment in step (3) is atomic.
    
*   The underlying buffer data remains valid and at a stable memory location for the lifetime of all exports.
    
*   For objects that support resizing or reallocation (such as [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
    ), the export counter is checked atomically before such operations, and [`BufferError`](https://docs.python.org/3/builtins/exceptions.html#BufferError "BufferError")
     is raised if exports exist.
    
*   The function is safe to call concurrently from multiple threads.
    

See also [Thread safety for memoryview objects](https://docs.python.org/3/builtins/threadsafety.html#thread-safety-memoryview)
 for the Python-level thread safety guarantees of [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
 objects.

If _exporter_ is part of a chain or tree of buffer providers, two main schemes can be used:

*   Re-export: Each member of the tree acts as the exporting object and sets `view->obj` to a new reference to itself.
    
*   Redirect: The buffer request is redirected to the root object of the tree. Here, `view->obj` will be a new reference to the root object.
    

The individual fields of _view_ are described in section [Buffer structure](https://docs.python.org/3/c-api/buffer.html#buffer-structure)
, the rules how an exporter must react to specific requests are in section [Buffer request types](https://docs.python.org/3/c-api/buffer.html#buffer-request-types)
.

All memory pointed to in the [`Py_buffer`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
 structure belongs to the exporter and must remain valid until there are no consumers left. [`format`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.format "Py_buffer.format")
, [`shape`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.shape "Py_buffer.shape")
, [`strides`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.strides "Py_buffer.strides")
, [`suboffsets`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.suboffsets "Py_buffer.suboffsets")
 and [`internal`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.internal "Py_buffer.internal")
 are read-only for the consumer.

[`PyBuffer_FillInfo()`](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_FillInfo "PyBuffer_FillInfo")
 provides an easy way of exposing a simple bytes buffer while dealing correctly with all request types.

[`PyObject_GetBuffer()`](https://docs.python.org/3/c-api/buffer.html#c.PyObject_GetBuffer "PyObject_GetBuffer")
 is the interface for the consumer that wraps this function.

[releasebufferproc](https://docs.python.org/3/c-api/typeobj.html#c.releasebufferproc "releasebufferproc")
 [PyBufferProcs](https://docs.python.org/3/c-api/typeobj.html#c.PyBufferProcs "PyBufferProcs")
.bf\_releasebuffer[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyBufferProcs.bf_releasebuffer "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_bf_releasebuffer` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

The signature of this function is:

void (PyObject \*exporter, Py\_buffer \*view);

Handle a request to release the resources of the buffer. If no resources need to be released, [`PyBufferProcs.bf_releasebuffer`](https://docs.python.org/3/c-api/typeobj.html#c.PyBufferProcs.bf_releasebuffer "PyBufferProcs.bf_releasebuffer")
 may be `NULL`. Otherwise, a standard implementation of this function will take these optional steps:

1.  Decrement an internal counter for the number of exports.
    
2.  If the counter is `0`, free all memory associated with _view_.
    

**Thread safety:**

In the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
:

*   The export counter decrement in step (1) must be atomic.
    
*   Resource cleanup when the counter reaches zero must be done atomically, as the final release may race with concurrent releases from other threads and deallocation must only happen once.
    

The exporter MUST use the [`internal`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.internal "Py_buffer.internal")
 field to keep track of buffer-specific resources. This field is guaranteed to remain constant, while a consumer MAY pass a copy of the original buffer as the _view_ argument.

This function MUST NOT decrement `view->obj`, since that is done automatically in [`PyBuffer_Release()`](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_Release "PyBuffer_Release")
 (this scheme is useful for breaking reference cycles).

[`PyBuffer_Release()`](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_Release "PyBuffer_Release")
 is the interface for the consumer that wraps this function.

Async Object Structures[¶](https://docs.python.org/3/c-api/typeobj.html#async-object-structures "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

Added in version 3.5.

type PyAsyncMethods[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyAsyncMethods "Link to this definition")
  

This structure holds pointers to the functions required to implement [awaitable](https://docs.python.org/3/glossary.html#term-awaitable)
 and [asynchronous iterator](https://docs.python.org/3/glossary.html#term-asynchronous-iterator)
 objects.

Here is the structure definition:

typedef struct {
    unaryfunc am\_await;
    unaryfunc am\_aiter;
    unaryfunc am\_anext;
    sendfunc am\_send;
} PyAsyncMethods;

[unaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc")
 [PyAsyncMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyAsyncMethods "PyAsyncMethods")
.am\_await[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyAsyncMethods.am_await "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_am_await` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.5._

The signature of this function is:

PyObject \*am\_await(PyObject \*self);

The returned object must be an [iterator](https://docs.python.org/3/glossary.html#term-iterator)
, i.e. [`PyIter_Check()`](https://docs.python.org/3/c-api/iter.html#c.PyIter_Check "PyIter_Check")
 must return `1` for it.

This slot may be set to `NULL` if an object is not an [awaitable](https://docs.python.org/3/glossary.html#term-awaitable)
.

[unaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc")
 [PyAsyncMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyAsyncMethods "PyAsyncMethods")
.am\_aiter[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyAsyncMethods.am_aiter "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_am_aiter` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.5._

The signature of this function is:

PyObject \*am\_aiter(PyObject \*self);

Must return an [asynchronous iterator](https://docs.python.org/3/glossary.html#term-asynchronous-iterator)
 object. See [`__anext__()`](https://docs.python.org/3/reference/datamodel.html#object.__anext__ "object.__anext__")
 for details.

This slot may be set to `NULL` if an object does not implement asynchronous iteration protocol.

[unaryfunc](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc")
 [PyAsyncMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyAsyncMethods "PyAsyncMethods")
.am\_anext[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyAsyncMethods.am_anext "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_am_anext` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.5._

The signature of this function is:

PyObject \*am\_anext(PyObject \*self);

Must return an [awaitable](https://docs.python.org/3/glossary.html#term-awaitable)
 object. See [`__anext__()`](https://docs.python.org/3/reference/datamodel.html#object.__anext__ "object.__anext__")
 for details. This slot may be set to `NULL`.

[sendfunc](https://docs.python.org/3/c-api/typeobj.html#c.sendfunc "sendfunc")
 [PyAsyncMethods](https://docs.python.org/3/c-api/typeobj.html#c.PyAsyncMethods "PyAsyncMethods")
.am\_send[¶](https://docs.python.org/3/c-api/typeobj.html#c.PyAsyncMethods.am_send "Link to this definition")
  

_The corresponding [slot ID](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 `Py_am_send` is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

The signature of this function is:

PySendResult am\_send(PyObject \*self, PyObject \*arg, PyObject \*\*result);

See [`PyIter_Send()`](https://docs.python.org/3/c-api/iter.html#c.PyIter_Send "PyIter_Send")
 for details. This slot may be set to `NULL`.

Added in version 3.10.

Slot Type typedefs[¶](https://docs.python.org/3/c-api/typeobj.html#slot-type-typedefs "Link to this heading")

--------------------------------------------------------------------------------------------------------------

typedef [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*(\*allocfunc)([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*cls, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 nitems)[¶](https://docs.python.org/3/c-api/typeobj.html#c.allocfunc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The purpose of this function is to separate memory allocation from memory initialization. It should return a pointer to a block of memory of adequate length for the instance, suitably aligned, and initialized to zeros, but with [`ob_refcnt`](https://docs.python.org/3/c-api/structures.html#c.PyObject.ob_refcnt "PyObject.ob_refcnt")
 set to `1` and [`ob_type`](https://docs.python.org/3/c-api/structures.html#c.PyObject.ob_type "PyObject.ob_type")
 set to the type argument. If the type’s [`tp_itemsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_itemsize "PyTypeObject.tp_itemsize")
 is non-zero, the object’s [`ob_size`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject.ob_size "PyVarObject.ob_size")
 field should be initialized to _nitems_ and the length of the allocated memory block should be `tp_basicsize + nitems*tp_itemsize`, rounded up to a multiple of `sizeof(void*)`; otherwise, _nitems_ is not used and the length of the block should be [`tp_basicsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_basicsize "PyTypeObject.tp_basicsize")
.

This function should not do any other instance initialization, not even to allocate additional memory; that should be done by [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
.

typedef void (\*destructor)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*)[¶](https://docs.python.org/3/c-api/typeobj.html#c.destructor "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

typedef void (\*freefunc)(void\*)[¶](https://docs.python.org/3/c-api/typeobj.html#c.freefunc "Link to this definition")
  

See [`tp_free`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_free "PyTypeObject.tp_free")
.

typedef [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*(\*newfunc)([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
\*, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*)[¶](https://docs.python.org/3/c-api/typeobj.html#c.newfunc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

See [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
.

typedef int (\*initproc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*)[¶](https://docs.python.org/3/c-api/typeobj.html#c.initproc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

See [`tp_init`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_init "PyTypeObject.tp_init")
.

typedef [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*(\*reprfunc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*)[¶](https://docs.python.org/3/c-api/typeobj.html#c.reprfunc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

See [`tp_repr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_repr "PyTypeObject.tp_repr")
.

typedef [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*(\*getattrfunc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*self, char \*attr)[¶](https://docs.python.org/3/c-api/typeobj.html#c.getattrfunc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the value of the named attribute for the object.

typedef int (\*setattrfunc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*self, char \*attr, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*value)[¶](https://docs.python.org/3/c-api/typeobj.html#c.setattrfunc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Set the value of the named attribute for the object. The value argument is set to `NULL` to delete the attribute.

typedef [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*(\*getattrofunc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*self, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*attr)[¶](https://docs.python.org/3/c-api/typeobj.html#c.getattrofunc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the value of the named attribute for the object.

See [`tp_getattro`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getattro "PyTypeObject.tp_getattro")
.

typedef int (\*setattrofunc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*self, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*attr, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*value)[¶](https://docs.python.org/3/c-api/typeobj.html#c.setattrofunc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Set the value of the named attribute for the object. The value argument is set to `NULL` to delete the attribute.

See [`tp_setattro`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_setattro "PyTypeObject.tp_setattro")
.

typedef [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*(\*descrgetfunc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*)[¶](https://docs.python.org/3/c-api/typeobj.html#c.descrgetfunc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

See [`tp_descr_get`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_descr_get "PyTypeObject.tp_descr_get")
.

typedef int (\*descrsetfunc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*)[¶](https://docs.python.org/3/c-api/typeobj.html#c.descrsetfunc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

See [`tp_descr_set`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_descr_set "PyTypeObject.tp_descr_set")
.

typedef [Py\_hash\_t](https://docs.python.org/3/c-api/hash.html#c.Py_hash_t "Py_hash_t")
 (\*hashfunc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*)[¶](https://docs.python.org/3/c-api/typeobj.html#c.hashfunc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

See [`tp_hash`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_hash "PyTypeObject.tp_hash")
.

typedef [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*(\*richcmpfunc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, int)[¶](https://docs.python.org/3/c-api/typeobj.html#c.richcmpfunc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

See [`tp_richcompare`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_richcompare "PyTypeObject.tp_richcompare")
.

typedef [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*(\*getiterfunc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*)[¶](https://docs.python.org/3/c-api/typeobj.html#c.getiterfunc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

See [`tp_iter`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_iter "PyTypeObject.tp_iter")
.

typedef [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*(\*iternextfunc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*)[¶](https://docs.python.org/3/c-api/typeobj.html#c.iternextfunc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

See [`tp_iternext`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_iternext "PyTypeObject.tp_iternext")
.

typedef [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 (\*lenfunc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*)[¶](https://docs.python.org/3/c-api/typeobj.html#c.lenfunc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

typedef int (\*getbufferproc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, [Py\_buffer](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
\*, int)[¶](https://docs.python.org/3/c-api/typeobj.html#c.getbufferproc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

typedef void (\*releasebufferproc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, [Py\_buffer](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
\*)[¶](https://docs.python.org/3/c-api/typeobj.html#c.releasebufferproc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

typedef [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*(\*unaryfunc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*)[¶](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

typedef [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*(\*binaryfunc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*)[¶](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

typedef [PySendResult](https://docs.python.org/3/c-api/iter.html#c.PySendResult "PySendResult")
 (\*sendfunc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*\*)[¶](https://docs.python.org/3/c-api/typeobj.html#c.sendfunc "Link to this definition")
  

See [`am_send`](https://docs.python.org/3/c-api/typeobj.html#c.PyAsyncMethods.am_send "PyAsyncMethods.am_send")
.

typedef [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*(\*ternaryfunc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*)[¶](https://docs.python.org/3/c-api/typeobj.html#c.ternaryfunc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

typedef [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*(\*ssizeargfunc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
)[¶](https://docs.python.org/3/c-api/typeobj.html#c.ssizeargfunc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

typedef int (\*ssizeobjargproc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*)[¶](https://docs.python.org/3/c-api/typeobj.html#c.ssizeobjargproc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

typedef int (\*objobjproc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*)[¶](https://docs.python.org/3/c-api/typeobj.html#c.objobjproc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

typedef int (\*objobjargproc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*)[¶](https://docs.python.org/3/c-api/typeobj.html#c.objobjargproc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Examples[¶](https://docs.python.org/3/c-api/typeobj.html#examples "Link to this heading")

------------------------------------------------------------------------------------------

The following are simple examples of Python type definitions. They include common usage you may encounter. Some demonstrate tricky corner cases. For more examples, practical info, and a tutorial, see [Defining Extension Types: Tutorial](https://docs.python.org/3/extending/newtypes_tutorial.html#defining-new-types)
 and [Defining Extension Types: Assorted Topics](https://docs.python.org/3/extending/newtypes.html#new-types-topics)
.

A basic [static type](https://docs.python.org/3/c-api/typeobj.html#static-types)
:

typedef struct {
    PyObject\_HEAD
    const char \*data;
} MyObject;

static PyTypeObject MyObject\_Type \= {
    PyVarObject\_HEAD\_INIT(NULL, 0)
    .tp\_name \= "mymod.MyObject",
    .tp\_basicsize \= sizeof(MyObject),
    .tp\_doc \= PyDoc\_STR("My objects"),
    .tp\_new \= myobj\_new,
    .tp\_dealloc \= (destructor)myobj\_dealloc,
    .tp\_repr \= (reprfunc)myobj\_repr,
};

You may also find older code (especially in the CPython code base) with a more verbose initializer:

static PyTypeObject MyObject\_Type \= {
    PyVarObject\_HEAD\_INIT(NULL, 0)
    "mymod.MyObject",               /\* tp\_name \*/
    sizeof(MyObject),               /\* tp\_basicsize \*/
    0,                              /\* tp\_itemsize \*/
    (destructor)myobj\_dealloc,      /\* tp\_dealloc \*/
    0,                              /\* tp\_vectorcall\_offset \*/
    0,                              /\* tp\_getattr \*/
    0,                              /\* tp\_setattr \*/
    0,                              /\* tp\_as\_async \*/
    (reprfunc)myobj\_repr,           /\* tp\_repr \*/
    0,                              /\* tp\_as\_number \*/
    0,                              /\* tp\_as\_sequence \*/
    0,                              /\* tp\_as\_mapping \*/
    0,                              /\* tp\_hash \*/
    0,                              /\* tp\_call \*/
    0,                              /\* tp\_str \*/
    0,                              /\* tp\_getattro \*/
    0,                              /\* tp\_setattro \*/
    0,                              /\* tp\_as\_buffer \*/
    0,                              /\* tp\_flags \*/
    PyDoc\_STR("My objects"),        /\* tp\_doc \*/
    0,                              /\* tp\_traverse \*/
    0,                              /\* tp\_clear \*/
    0,                              /\* tp\_richcompare \*/
    0,                              /\* tp\_weaklistoffset \*/
    0,                              /\* tp\_iter \*/
    0,                              /\* tp\_iternext \*/
    0,                              /\* tp\_methods \*/
    0,                              /\* tp\_members \*/
    0,                              /\* tp\_getset \*/
    0,                              /\* tp\_base \*/
    0,                              /\* tp\_dict \*/
    0,                              /\* tp\_descr\_get \*/
    0,                              /\* tp\_descr\_set \*/
    0,                              /\* tp\_dictoffset \*/
    0,                              /\* tp\_init \*/
    0,                              /\* tp\_alloc \*/
    myobj\_new,                      /\* tp\_new \*/
};

A type that supports weakrefs, instance dicts, and hashing:

typedef struct {
    PyObject\_HEAD
    const char \*data;
} MyObject;

static PyTypeObject MyObject\_Type \= {
    PyVarObject\_HEAD\_INIT(NULL, 0)
    .tp\_name \= "mymod.MyObject",
    .tp\_basicsize \= sizeof(MyObject),
    .tp\_doc \= PyDoc\_STR("My objects"),
    .tp\_flags \= Py\_TPFLAGS\_DEFAULT | Py\_TPFLAGS\_BASETYPE |
         Py\_TPFLAGS\_HAVE\_GC | Py\_TPFLAGS\_MANAGED\_DICT |
         Py\_TPFLAGS\_MANAGED\_WEAKREF,
    .tp\_new \= myobj\_new,
    .tp\_traverse \= (traverseproc)myobj\_traverse,
    .tp\_clear \= (inquiry)myobj\_clear,
    .tp\_alloc \= PyType\_GenericAlloc,
    .tp\_dealloc \= (destructor)myobj\_dealloc,
    .tp\_repr \= (reprfunc)myobj\_repr,
    .tp\_hash \= (hashfunc)myobj\_hash,
    .tp\_richcompare \= PyBaseObject\_Type.tp\_richcompare,
};

A str subclass that cannot be subclassed and cannot be called to create instances (e.g. uses a separate factory func) using [`Py_TPFLAGS_DISALLOW_INSTANTIATION`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_DISALLOW_INSTANTIATION "Py_TPFLAGS_DISALLOW_INSTANTIATION")
 flag:

typedef struct {
    PyUnicodeObject raw;
    char \*extra;
} MyStr;

static PyTypeObject MyStr\_Type \= {
    PyVarObject\_HEAD\_INIT(NULL, 0)
    .tp\_name \= "mymod.MyStr",
    .tp\_basicsize \= sizeof(MyStr),
    .tp\_base \= NULL,  // set to &PyUnicode\_Type in module init
    .tp\_doc \= PyDoc\_STR("my custom str"),
    .tp\_flags \= Py\_TPFLAGS\_DEFAULT | Py\_TPFLAGS\_DISALLOW\_INSTANTIATION,
    .tp\_repr \= (reprfunc)myobj\_repr,
};

The simplest [static type](https://docs.python.org/3/c-api/typeobj.html#static-types)
 with fixed-length instances:

typedef struct {
    PyObject\_HEAD
} MyObject;

static PyTypeObject MyObject\_Type \= {
    PyVarObject\_HEAD\_INIT(NULL, 0)
    .tp\_name \= "mymod.MyObject",
};

The simplest [static type](https://docs.python.org/3/c-api/typeobj.html#static-types)
 with variable-length instances:

typedef struct {
    PyObject\_VAR\_HEAD
    const char \*data\[1\];
} MyObject;

static PyTypeObject MyObject\_Type \= {
    PyVarObject\_HEAD\_INIT(NULL, 0)
    .tp\_name \= "mymod.MyObject",
    .tp\_basicsize \= sizeof(MyObject) \- sizeof(char \*),
    .tp\_itemsize \= sizeof(char \*),
};

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Type Object Structures](https://docs.python.org/3/c-api/typeobj.html#)
    *   [Quick Reference](https://docs.python.org/3/c-api/typeobj.html#quick-reference)
        *   [“tp slots”](https://docs.python.org/3/c-api/typeobj.html#tp-slots)
            
        *   [sub-slots](https://docs.python.org/3/c-api/typeobj.html#sub-slots)
            
        *   [slot typedefs](https://docs.python.org/3/c-api/typeobj.html#slot-typedefs)
            
    *   [PyTypeObject Definition](https://docs.python.org/3/c-api/typeobj.html#pytypeobject-definition)
        
    *   [PyObject Slots](https://docs.python.org/3/c-api/typeobj.html#pyobject-slots)
        
    *   [PyVarObject Slots](https://docs.python.org/3/c-api/typeobj.html#pyvarobject-slots)
        
    *   [PyTypeObject Slots](https://docs.python.org/3/c-api/typeobj.html#pytypeobject-slots)
        
    *   [Static Types](https://docs.python.org/3/c-api/typeobj.html#static-types)
        
    *   [Heap Types](https://docs.python.org/3/c-api/typeobj.html#heap-types)
        
    *   [Number Object Structures](https://docs.python.org/3/c-api/typeobj.html#number-object-structures)
        
    *   [Mapping Object Structures](https://docs.python.org/3/c-api/typeobj.html#mapping-object-structures)
        
    *   [Sequence Object Structures](https://docs.python.org/3/c-api/typeobj.html#sequence-object-structures)
        
    *   [Buffer Object Structures](https://docs.python.org/3/c-api/typeobj.html#buffer-object-structures)
        
    *   [Async Object Structures](https://docs.python.org/3/c-api/typeobj.html#async-object-structures)
        
    *   [Slot Type typedefs](https://docs.python.org/3/c-api/typeobj.html#slot-type-typedefs)
        
    *   [Examples](https://docs.python.org/3/c-api/typeobj.html#examples)
        

#### Previous topic

[Common Object Structures](https://docs.python.org/3/c-api/structures.html "previous chapter")

#### Next topic

[Supporting Cyclic Garbage Collection](https://docs.python.org/3/c-api/gcsupport.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Type+Object+Structures&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Ftypeobj.html&pagesource=c-api%2Ftypeobj.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/typeobj.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/gcsupport.html "Supporting Cyclic Garbage Collection")
     |
*   [previous](https://docs.python.org/3/c-api/structures.html "Common Object Structures")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Object Implementation Support](https://docs.python.org/3/c-api/objimpl.html)
     »
*   [Type Object Structures](https://docs.python.org/3/c-api/typeobj.html)
    
*    
    
    |
*   Theme Auto Light Dark |