### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/utilities.html "Utilities")
     |
*   [previous](https://docs.python.org/3/c-api/extension-modules.html "Defining extension modules")
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
*   [Definition slots](https://docs.python.org/3/c-api/slots.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Definition slots[¶](https://docs.python.org/3/c-api/slots.html#definition-slots "Link to this heading")

========================================================================================================

To define [module objects](https://docs.python.org/3/c-api/module.html#moduleobjects)
 and [classes](https://docs.python.org/3/c-api/type.html#creating-heap-types)
 using the C API, you may use an array of _slots_ – essentially, key-value pairs that describe features of the object to create. This decouples the data from the structures used at runtime, allowing CPython – and other Python C API implementations – to update the structures without breaking backwards compatibility.

This section documents slots in general. For object-specific behavior and slot values, see documentation for functions that apply slots:

*   [`PyType_FromSlots()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSlots "PyType_FromSlots")
     for types;
    
*   [`PyModule_FromSlotsAndSpec()`](https://docs.python.org/3/c-api/module.html#c.PyModule_FromSlotsAndSpec "PyModule_FromSlotsAndSpec")
     and [Extension export hook](https://docs.python.org/3/c-api/extension-modules.html#extension-export-hook)
     for modules.
    

When slots are passed to a function that applies them, the function will not modify the slot array, nor any data it points to (recursively). After the function is done, the caller is allowed to modify or deallocate the array and any data it points to (recursively), except data explicitly marked with [`PySlot_STATIC`](https://docs.python.org/3/c-api/slots.html#c.PySlot_STATIC "PySlot_STATIC")
.

Except when documented otherwise, multiple slots with the same ID ([`sl_id`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
) may not occur in a single slots array.

Added in version 3.15: Slot arrays generalize an earlier way of defining objects: using [`PyType_Spec`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec "PyType_Spec")
 with [`PyType_Slot`](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 for types, and [`PyModuleDef`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 with [`PyModuleDef_Slot`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef_Slot "PyModuleDef_Slot")
 for modules. The earlier API is [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
; there are no plans to remove it.

Entries of the slots array use the following structure:

type PySlot[¶](https://docs.python.org/3/c-api/slots.html#c.PySlot "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (including all members) since version 3.15._

An entry in a slots array. Defined as:

typedef struct {
    uint16\_t sl\_id;
    uint16\_t sl\_flags;
    union {
        uint32\_t sl\_reserved;  // must be 0
    };
    union {
        void \*sl\_ptr;
        void (\*sl\_func)(void);
        Py\_ssize\_t sl\_size;
        int64\_t sl\_int64;
        uint64\_t sl\_uint64;
    };
} PySlot;

uint16\_t sl\_id[¶](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "Link to this definition")
  

A slot ID, chosen from:

*   `Py_slot_*` values documented in [Common slot IDs](https://docs.python.org/3/c-api/slots.html#pyslot-common-ids)
     below;
    
*   `Py_mod_*` values for modules, as documented in [Module definition](https://docs.python.org/3/c-api/module.html#c-module-slots)
    ;
    
*   Values for types, as documented in [Type slot IDs](https://docs.python.org/3/c-api/type.html#pyslot-type-slot-ids)
    .
    

A `sl_id` of zero ([`Py_slot_end`](https://docs.python.org/3/c-api/slots.html#c.Py_slot_end "Py_slot_end")
) marks the end of a slots array.

void \*sl\_ptr[¶](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_ptr "Link to this definition")
  

void (\*sl\_func)(void)[¶](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_func "Link to this definition")
  

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 sl\_size[¶](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_size "Link to this definition")
  

int64\_t sl\_int64[¶](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_int64 "Link to this definition")
  

uint64\_t sl\_uint64[¶](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_uint64 "Link to this definition")
  

The data for the slot. These members are part of an anonymous union; the member to use depends on which data type is required by the slot ID: data pointer, function pointer, size, signed or unsigned integer, respectively.

Except when documented otherwise for a specific slot ID, pointers (that is `sl_ptr` and `sl_func`) may not be NULL.

uint16\_t sl\_flags[¶](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_flags "Link to this definition")
  

Zero or more of the following flags, OR-ed together:

PySlot\_STATIC[¶](https://docs.python.org/3/c-api/slots.html#c.PySlot_STATIC "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

All data the slot points to is statically allocated and constant. Thus, the interpreter does not need to copy the information.

This flag is implied for function pointers.

The flag applies even to data the slot points to “indirectly”, except for slots nested via [`Py_slot_subslots`](https://docs.python.org/3/c-api/slots.html#c.Py_slot_subslots "Py_slot_subslots")
 which may have their own `PySlot_STATIC` flags. For example, if applied to a [`Py_tp_members`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_members "Py_tp_members")
 slot that points to an array of [`PyMemberDef`](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef "PyMemberDef")
 structures, then the entire array, as well as the name and doc strings in its elements, must be static and constant.

PySlot\_INTPTR[¶](https://docs.python.org/3/c-api/slots.html#c.PySlot_INTPTR "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

The data is stored in `sl_ptr`; CPython will cast it to the appropriate type.

This flag can simplify porting from the older [`PyType_Slot`](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 and [`PyModuleDef_Slot`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef_Slot "PyModuleDef_Slot")
 structures.

PySlot\_OPTIONAL[¶](https://docs.python.org/3/c-api/slots.html#c.PySlot_OPTIONAL "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

If the slot ID is unknown, the interpreter should ignore the slot, rather than fail.

For example, if Python 3.16 adds a new feature with a new slot ID,attr the corresponding slot may be marked `PySlot_OPTIONAL` so that Python 3.15 ignores it.

Note that the “optionality” only applies to unknown slot IDs. This flag does not make Python skip invalid values of known slots.

Added in version 3.15.

Convenience macros[¶](https://docs.python.org/3/c-api/slots.html#convenience-macros "Link to this heading")

------------------------------------------------------------------------------------------------------------

PySlot\_DATA(name, value)[¶](https://docs.python.org/3/c-api/slots.html#c.PySlot_DATA "Link to this definition")
  

PySlot\_FUNC(name, value)[¶](https://docs.python.org/3/c-api/slots.html#c.PySlot_FUNC "Link to this definition")
  

PySlot\_SIZE(name, value)[¶](https://docs.python.org/3/c-api/slots.html#c.PySlot_SIZE "Link to this definition")
  

PySlot\_INT64(name, value)[¶](https://docs.python.org/3/c-api/slots.html#c.PySlot_INT64 "Link to this definition")
  

PySlot\_UINT64(name, value)[¶](https://docs.python.org/3/c-api/slots.html#c.PySlot_UINT64 "Link to this definition")
  

PySlot\_STATIC\_DATA(name, value)[¶](https://docs.python.org/3/c-api/slots.html#c.PySlot_STATIC_DATA "Link to this definition")
  

_This macro is available when compiling for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Convenience macros to define `PySlot` structures with [`sl_id`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 and a particular union member set.

`PySlot_STATIC_DATA` sets the [`PySlot_STATIC`](https://docs.python.org/3/c-api/slots.html#c.PySlot_STATIC "PySlot_STATIC")
 flag; others set no flags.

Note that these macros use _designated initializers_, a C language feature that C++ added in the 2020 version of the standard. If your code needs to be compatible with C++11 or older, use [`PySlot_PTR`](https://docs.python.org/3/c-api/slots.html#c.PySlot_PTR "PySlot_PTR")
 instead.

Defined as:

#define PySlot\_DATA(NAME, VALUE) \\
   {.sl\_id=NAME, .sl\_ptr=(void\*)(VALUE)}

#define PySlot\_FUNC(NAME, VALUE) \\
   {.sl\_id=NAME, .sl\_func=(VALUE)}

#define PySlot\_SIZE(NAME, VALUE) \\
   {.sl\_id=NAME, .sl\_size=(VALUE)}

#define PySlot\_INT64(NAME, VALUE) \\
   {.sl\_id=NAME, .sl\_int64=(VALUE)}

#define PySlot\_UINT64(NAME, VALUE) \\
   {.sl\_id=NAME, .sl\_uint64=(VALUE)}

#define PySlot\_STATIC\_DATA(NAME, VALUE) \\
   {.sl\_id=NAME, .sl\_flags=PySlot\_STATIC, .sl\_ptr=(VALUE)}

Added in version 3.15.

PySlot\_END[¶](https://docs.python.org/3/c-api/slots.html#c.PySlot_END "Link to this definition")
  

_This macro is available when compiling for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Convenience macro to mark the end of a `PySlot` array.

Defined as:

#define PySlot\_END {0}

Added in version 3.15.

PySlot\_PTR(name, value)[¶](https://docs.python.org/3/c-api/slots.html#c.PySlot_PTR "Link to this definition")
  

PySlot\_PTR\_STATIC(name, value)[¶](https://docs.python.org/3/c-api/slots.html#c.PySlot_PTR_STATIC "Link to this definition")
  

_This macro is available when compiling for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Convenience macros for use in C++11-compatible code. This version of C++ does not allow setting arbitrary union members in literals; instead, these macros set the [`PySlot_INTPTR`](https://docs.python.org/3/c-api/slots.html#c.PySlot_INTPTR "PySlot_INTPTR")
 flag and cast the value to `(void*)`.

Defined as:

#define PySlot\_PTR(NAME, VALUE) \\
   {NAME, PySlot\_INTPTR, {0}, {(void\*)(VALUE)}}

#define PySlot\_PTR\_STATIC(NAME, VALUE) \\
   {NAME, PySlot\_INTPTR|PySlot\_STATIC, {0}, {(void\*)(VALUE)}}

Added in version 3.15.

Common slot IDs[¶](https://docs.python.org/3/c-api/slots.html#common-slot-ids "Link to this heading")

------------------------------------------------------------------------------------------------------

The following slot IDs may be used in both type and module definitions.

Py\_slot\_end[¶](https://docs.python.org/3/c-api/slots.html#c.Py_slot_end "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Marks the end of a slots array. Defined as zero.

Added in version 3.15.

Py\_slot\_subslots[¶](https://docs.python.org/3/c-api/slots.html#c.Py_slot_subslots "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Nested slots array.

The value ([`sl_ptr`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_ptr "PySlot.sl_ptr")
) should point to an array of [`PySlot`](https://docs.python.org/3/c-api/slots.html#c.PySlot "PySlot")
 structures. The slots in the array (up to but not including the zero-ID terminator) will be treated as if they were inserted if the current slot array, at the point `Py_slot_subslots` appears.

Slot nesting depth is limited to 5 levels. This restriction may be lifted in the future.

Added in version 3.15.

Py\_slot\_invalid[¶](https://docs.python.org/3/c-api/slots.html#c.Py_slot_invalid "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Reserved; will always be treated as an unknown slot ID. Defined as `UINT16_MAX` (`0xFFFF`).

When used with the [`PySlot_OPTIONAL`](https://docs.python.org/3/c-api/slots.html#c.PySlot_OPTIONAL "PySlot_OPTIONAL")
 flag, defines a slot with no effect. Without the flag, processing a slot with this ID will fail.

Added in version 3.15.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Definition slots](https://docs.python.org/3/c-api/slots.html#)
    *   [Convenience macros](https://docs.python.org/3/c-api/slots.html#convenience-macros)
        
    *   [Common slot IDs](https://docs.python.org/3/c-api/slots.html#common-slot-ids)
        

#### Previous topic

[Defining extension modules](https://docs.python.org/3/c-api/extension-modules.html "previous chapter")

#### Next topic

[Utilities](https://docs.python.org/3/c-api/utilities.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Definition+slots&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fslots.html&pagesource=c-api%2Fslots.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/slots.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/utilities.html "Utilities")
     |
*   [previous](https://docs.python.org/3/c-api/extension-modules.html "Defining extension modules")
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
*   [Definition slots](https://docs.python.org/3/c-api/slots.html)
    
*    
    
    |
*   Theme Auto Light Dark |