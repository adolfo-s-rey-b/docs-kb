For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object.md)
.

`_Object_`.`**compact()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objectcompact)

--------------------------------------------------------------------------------------------------------------------------------

**Description:** Removes all fields that have empty values, i.e. are `null` or `""`

**Syntax:** `_Object_`.compact()

**Returns:** Object

**Source:** Custom n8n functionality

**Examples:**

Copy

    // obj = {'x':null, 'y':2, 'z':''}
    obj.compact() //=> {'y':2}

`_Object_`.`**hasField()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objecthasfield)

----------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if there is a field called `name`. Only checks top-level keys. Comparison is case-sensitive.

**Syntax:** `_Object_`.hasField(name)

**Returns:** Boolean

**Source:** Custom n8n functionality

**Parameters:**

*   `name` (String) - The name of the key to search for
    

**Examples:**

Copy

    // obj = {'name':'Nathan', 'age':42}
    obj.hasField('name') //=> true

Copy

    // obj = {'name':'Nathan', 'age':42}
    obj.hasField('Name') //=> false
    obj.hasField('inventedField') //=> false

`_Object_`.`**isEmpty()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objectisempty)

--------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the Object has no keys (fields) set or is `null` or `undefined`

**Syntax:** `_Object_`.isEmpty()

**Returns:** Boolean

**Source:** Custom n8n functionality

**Examples:**

Copy

    // obj = {'name': 'Nathan'}
    obj.isEmpty() //=> false

Copy

    // obj = {}
    obj.isEmpty() //=> true

`_Object_`.`**isNotEmpty()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objectisnotempty)

--------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the Object has at least one key (field) set

**Syntax:** `_Object_`.isNotEmpty()

**Returns:** Boolean

**Source:** Custom n8n functionality

**Examples:**

Copy

    // obj = {'name': 'Nathan'}
    obj.isNotEmpty() //=> true

Copy

    // obj = {}
    obj.isNotEmpty() //=> false

`_Object_`.`**keepFieldsContaining()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objectkeepfieldscontaining)

----------------------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Removes any fields whose values don’t at least partly match the given `value`. Comparison is case-sensitive. Fields that aren’t strings will always be removed.

**Syntax:** `_Object_`.keepFieldsContaining(value)

**Returns:** Object

**Source:** Custom n8n functionality

**Parameters:**

*   `value` (String) - The text that a value must contain in order to be kept
    

**Examples:**

Copy

    // obj = {'name': 'Mr Nathan', 'city':'hanoi', age: 42 }
    obj.keepFieldsContaining('Nathan') //=> {'name': 'Mr Nathan'}

Copy

    // obj = {'name': 'Mr Nathan', 'city':'hanoi', age: 42 }
    obj.keepFieldsContaining('nathan') //=> {}
    obj.keepFieldsContaining('han') //=> {'name': 'Mr Nathan', 'city':'hanoi'}

`_Object_`.`**keys()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objectkeys)

--------------------------------------------------------------------------------------------------------------------------

**Description:** Returns an array with all the field names (keys) the object contains. The same as JavaScript’s `Object.keys(obj)`.

**Syntax:** `_Object_`.keys()

**Returns:** Array

**Source:** Custom n8n functionality

**Examples:**

Copy

    // obj = {'name': 'Mr Nathan', age: 42 }
    obj.keys() //=> ['name', 'age']

`_Object_`.`**merge()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objectmerge)

----------------------------------------------------------------------------------------------------------------------------

**Description:** Merges the two Objects into a single one. If a key (field name) exists in both Objects, the value from the first (base) Object is used.

**Syntax:** `_Object_`.merge(otherObject)

**Returns:** Object

**Source:** Custom n8n functionality

**Parameters:**

*   `otherObject` (Object) - The Object to merge with the base Object.
    

**Examples:**

Copy

    // obj1 = {'name':'Nathan', 'age': 42}
    // obj2 = {'name':'Jan', 'city': 'hanoi'}
    obj1.merge(obj2) //=> {'name':'Jan', 'city': 'hanoi', 'age':42}

`_Object_`.`**removeField()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objectremovefield)

----------------------------------------------------------------------------------------------------------------------------------------

**Description:** Removes a field from the Object. The same as JavaScript’s `delete`.

**Syntax:** `_Object_`.removeField(key)

**Returns:** Object

**Source:** Custom n8n functionality

**Parameters:**

*   `key` (String) - The name of the field to remove
    

**Examples:**

Copy

    // obj = {'name':'Nathan', 'city':'hanoi'}
    obj.removeField('name') //=> {'city':'hanoi'}

`_Object_`.`**removeFieldsContaining()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objectremovefieldscontaining)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Removes keys (fields) whose values at least partly match the given `value`. Comparison is case-sensitive. Fields that aren’t strings are always kept.

**Syntax:** `_Object_`.removeFieldsContaining(value)

**Returns:** Object

**Source:** Custom n8n functionality

**Parameters:**

*   `value` (String) - The text that a value must contain in order to be removed
    

**Examples:**

Copy

    // obj = {'name': 'Mr Nathan', 'city':'hanoi', age: 42}
    obj.removeFieldsContaining('Nathan') //=> {'city':'hanoi', age: 42}

Copy

    // obj = {'name': 'Mr Nathan', 'city':'hanoi', age: 42}
    obj.removeFieldsContaining('han') //=> {age: 42}
    obj.removeFieldsContaining('nathan') //=> {'name': 'Mr Nathan', 'city':'hanoi', age: 42}

`_Object_`.`**toJsonString()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objecttojsonstring)

------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Converts the Object to a JSON string. Similar to JavaScript’s `JSON.stringify()`.

**Syntax:** `_Object_`.toJsonString()

**Returns:** String

**Source:** Custom n8n functionality

**Examples:**

Copy

    // obj = {'name':'Nathan', age:42}
    obj.toJsonString() //=> '{"name":"Nathan","age":42}'
    

`_Object_`.`**urlEncode()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objecturlencode)

------------------------------------------------------------------------------------------------------------------------------------

**Description:** Generates a URL parameter string from the Object’s keys and values. Only top-level keys are supported.

**Syntax:** `_Object_`.urlEncode()

**Returns:** String

**Source:** Custom n8n functionality

**Examples:**

Copy

    // obj = {'name':'Mr Nathan', 'city':'hanoi'}
    obj.urlEncode() //=> 'name=Mr+Nathan&city=hanoi'

`_Object_`.`**values()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#objectvalues)

------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns an array with all the values of the fields the Object contains. The same as JavaScript’s `Object.values(obj)`.

**Syntax:** `_Object_`.values()

**Returns:** Array

**Source:** Custom n8n functionality

**Examples:**

Copy

    // obj = {'name': 'Mr Nathan', age: 42 }
    obj.values() //=> ['Mr Nathan', 42]

Related resources[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object#related-resources)

---------------------------------------------------------------------------------------------------------------------------

*   [Expression reference](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference)
    

[PreviousNumber](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number)
[NextPrevnodedata](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/prevnodedata)

Last updated 10 days ago

Was this helpful?