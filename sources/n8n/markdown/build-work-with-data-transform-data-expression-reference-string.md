For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string.md)
.

`_String_`.`**base64Decode()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringbase64decode)

------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Converts plain text to a base64-encoded string

**Syntax:** `_String_`.base64Encode()

**Returns:** String

**Source:** Custom n8n functionality

**Examples:**

Copy

    "aGVsbG8=".base64Decode() //=> "hello"

`_String_`.`**base64Encode()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringbase64encode)

------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Converts a base64-encoded string to plain text

**Syntax:** `_String_`.base64Encode()

**Returns:** String

**Source:** Custom n8n functionality

**Examples:**

Copy

    "hello".base64Encode() //=> "aGVsbG8="

`_String_`.`**concat()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringconcat)

------------------------------------------------------------------------------------------------------------------------------

**Description:** Joins one or more strings onto the end of the base string. Alternatively, use the `+` operator (see examples).

**Syntax:** `_String_`.concat(string1, string2?, ..., stringN?)

**Returns:** String

**Source:** JavaScript function

**Parameters:**

*   `string1` (String) - The first string to append
    
*   `string2` (String) - optional - The second string to append
    
*   `stringN` (String) - optional - The Nth string to append
    

**Examples:**

Copy

    'sea'.concat('food') //=> 'seafood'
    'sea' + 'food' //=> 'seafood'

Copy

    'work'.concat('a', 'holic') //=> 'workaholic'

`_String_`.`**extractDomain()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringextractdomain)

--------------------------------------------------------------------------------------------------------------------------------------------

**Description:** If the string is an email address or URL, returns its domain (or `undefined` if nothing found).

If the string also contains other content, try using `extractEmail()` or `extractUrl()` first.

**Syntax:** `_String_`.extractDomain()

**Returns:** String

**Source:** Custom n8n functionality

**Examples:**

Copy

    "me@example.com".extractDomain() //=> 'example.com'

Copy

    "http://n8n.io/workflows".extractDomain() //=> 'n8n.io'

Copy

    "It's me@example.com".extractEmail().extractDomain() //=> 'example.com'

`_String_`.`**extractEmail()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringextractemail)

------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Extracts the first email found in the string. Returns `undefined` if none is found.

**Syntax:** `_String_`.extractEmail()

**Returns:** String

**Source:** Custom n8n functionality

**Examples:**

Copy

    "My email is me@example.com".extractEmail() //=> 'me@example.com'

`_String_`.`**extractUrl()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringextracturl)

--------------------------------------------------------------------------------------------------------------------------------------

**Description:** Extracts the first URL found in the string. Returns `undefined` if none is found. Only recognizes full URLs, e.g. those starting with `http`.

**Syntax:** `_String_`.extractUrl()

**Returns:** String

**Source:** Custom n8n functionality

**Examples:**

Copy

    "Check out http://n8n.io".extractUrl() //=> 'http://n8n.io'

`_String_`.`**extractUrlPath()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringextracturlpath)

----------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns the part of a URL after the domain, or `undefined` if no URL found.

If the string also contains other content, try using `extractUrl()` first.

**Syntax:** `_String_`.extractUrlPath()

**Returns:** String

**Source:** Custom n8n functionality

**Examples:**

Copy

    "http://n8n.io/workflows".extractUrlPath() //=> '/workflows'

Copy

    "Check out http://n8n.io/workflows".extractUrl().extractUrlPath() //=> '/workflows'

`_String_`.`**hash()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringhash)

--------------------------------------------------------------------------------------------------------------------------

**Description:** Returns the string hashed with the given algorithm. Defaults to md5 if not specified.

**Syntax:** `_String_`.hash(algo?)

**Returns:** String

**Source:** Custom n8n functionality

**Parameters:**

*   `algo` (String) - optional - The hashing algorithm to use. One of `md5`, `base64`, `sha1`, `sha224`, `sha256`, `sha384`, `sha512`, `sha3`, `ripemd160`
    

**Examples:**

Copy

    "hello".hash() //=> '5d41402abc4b2a76b9719d911017c592'

`_String_`.`**includes()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringincludes)

----------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the string contains the `searchString`. Case-sensitive.

**Syntax:** `_String_`.includes(searchString, start?)

**Returns:** Boolean

**Source:** JavaScript function

**Parameters:**

*   `searchString` (String) - The text to search for
    
*   `start` (Number) - optional - The position (index) to start searching from
    

**Examples:**

Copy

    'team'.includes('tea') //=> true
    'team'.includes('i') //=> false 

Copy

    // Returns false if the case doesn't match, so consider using .toLowerCase() first
    'team'.includes('Tea') //=> false
    'Team'.toLowerCase().includes('tea') //=> true

`_String_`.`**indexOf()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringindexof)

--------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns the index (position) of the first occurrence of `searchString` within the base string, or -1 if not found. Case-sensitive.

**Syntax:** `_String_`.indexOf(searchString, start?)

**Returns:** Number

**Source:** JavaScript function

**Parameters:**

*   `searchString` (String) - The text to search for
    
*   `start` (Number) - optional - The position (index) to start searching from
    

**Examples:**

Copy

    'steam'.indexOf('tea') //=> 1
    'steam'.indexOf('i') //=> -1 

Copy

    // Returns -1 if the case doesn't match, so consider using .toLowerCase() first
    'STEAM'.indexOf('tea') //=> -1
    'STEAM'.toLowerCase().indexOf('tea') //=> 1

`_String_`.`**isDomain()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringisdomain)

----------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the string is a domain

**Syntax:** `_String_`.isDomain()

**Returns:** Boolean

**Source:** Custom n8n functionality

**Examples:**

Copy

    "n8n.io".isDomain() //=> true

Copy

    "http://n8n.io".isDomain() //=> false

Copy

    "hello".isDomain() //=> false

`_String_`.`**isEmail()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringisemail)

--------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the string is an email

**Syntax:** `_String_`.isEmail()

**Returns:** Boolean

**Source:** Custom n8n functionality

**Examples:**

Copy

    "me@example.com".isEmail() //=> true

Copy

    "It's me@example.com".isEmail() //=> false

Copy

    "hello".isEmail() //=> false

`_String_`.`**isEmpty()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringisempty)

--------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the string has no characters or is `null` or `undefined`

**Syntax:** `_String_`.isEmpty()

**Returns:** Boolean

**Source:** Custom n8n functionality

**Examples:**

Copy

    "".isEmpty() // => true

Copy

    "hello".isEmpty() // => false

`_String_`.`**isNotEmpty()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringisnotempty)

--------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the string has at least one character

**Syntax:** `_String_`.isNotEmpty()

**Returns:** Boolean

**Source:** Custom n8n functionality

**Examples:**

Copy

    "hello".isNotEmpty() // => true

Copy

    "".isNotEmpty() // => false

`_String_`.`**isNumeric()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringisnumeric)

------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the string represents a number

**Syntax:** `_String_`.isNumeric()

**Returns:** Boolean

**Source:** Custom n8n functionality

**Examples:**

Copy

    "1.2234".isNumeric() // true

Copy

    "hello".isNumeric() // false

Copy

    "123E23".isNumeric() // true

`_String_`.`**isUrl()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringisurl)

----------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the string is a valid URL

**Syntax:** `_String_`.isUrl()

**Returns:** Boolean

**Source:** Custom n8n functionality

**Examples:**

Copy

    "https://n8n.io".isUrl() //=> true

Copy

    "n8n.io".isUrl() //=> false

Copy

    "hello".isUrl() //=> false

`_String_`.`**length**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringlength)

----------------------------------------------------------------------------------------------------------------------------

**Description:** The number of characters in the string

**Syntax:** `_String_`.length

**Returns:** Number

**Source:** JavaScript function

**Examples:**

Copy

    "hello".length //=> 5

`_String_`.`**match()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringmatch)

----------------------------------------------------------------------------------------------------------------------------

**Description:** Matches the string against a <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular\_expressions”>regular expression. Returns an array containing the first match, or all matches if the `g` flag is set in the regular expression. Returns `null` if no matches are found.

For checking whether text is present, consider `includes()` instead.

**Syntax:** `_String_`.match(regexp)

**Returns:** Array

**Source:** JavaScript function

**Parameters:**

*   `regexp` (RegExp) - A <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular\_expressions”>regular expression with the pattern to look for. Will look for multiple matches if the `g` flag is present (see examples).
    

**Examples:**

Copy

    // Match all words starting with 'r'
    "rock and roll".match(/r[^ ]*/g) //=> ['rock', 'roll']

Copy

    // Match first word starting with 'r' (no 'g' flag)
    "rock and roll".match(/r[^ ]*/) //=> ['rock']

Copy

    // For case-insensitive, add 'i' flag
    "ROCK and roll".match(/r[^ ]*/ig) //=> ['ROCK', 'roll']

`_String_`.`**parseJson()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringparsejson)

------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns the JavaScript Object or value represented by the string, or `undefined` if the string isn’t valid JSON. Single-quoted JSON is not supported.

**Syntax:** `_String_`.parseJson()

**Returns:** any

**Source:** Custom n8n functionality

**Examples:**

Copy

    '{"name":"Nathan"}'.parseJson() //=> {"name":"Nathan"}

Copy

    "{'name':'Nathan'}".parseJson() //=> undefined

Copy

    'hello'.parseJson() //=> undefined

`_String_`.`**quote()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringquote)

----------------------------------------------------------------------------------------------------------------------------

**Description:** Wraps a string in quotation marks, and escapes any quotation marks already in the string. Useful when constructing JSON, SQL, etc.

**Syntax:** `_String_`.quote(mark?)

**Returns:** String

**Source:** Custom n8n functionality

**Parameters:**

*   `mark` (String) - optional - The type of quotation mark to use
    

**Examples:**

Copy

    'Nathan says "hi"'.quote() //=> '"Nathan says \"hi\""'

`_String_`.`**removeMarkdown()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringremovemarkdown)

----------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Removes any Markdown formatting from the string. Also removes HTML tags.

**Syntax:** `_String_`.removeMarkdown()

**Returns:** String

**Source:** Custom n8n functionality

**Examples:**

Copy

    "*bold*, [link]()".removeMarkdown() //=> "bold, link"

`_String_`.`**removeTags()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringremovetags)

--------------------------------------------------------------------------------------------------------------------------------------

**Description:** Removes tags, such as HTML or XML, from the string

**Syntax:** `_String_`.removeTags()

**Returns:** String

**Source:** Custom n8n functionality

**Examples:**

Copy

    "<b>bold</b>, <a>link</a>".removeTags() //=> "bold, link"

`_String_`.`**replace()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringreplace)

--------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns a string with the first occurrence of `pattern` replaced by `replacement`.

To replace all occurrences, use `replaceAll()` instead.

**Syntax:** `_String_`.replace(pattern, replacement)

**Returns:** String

**Source:** JavaScript function

**Parameters:**

*   `pattern` (String|RegExp) - The pattern in the string to replace. Can be a string to match or a <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular\_expressions”>regular expression.
    
*   `replacement` (String) - The new text to replace with
    

**Examples:**

Copy

    'Red or blue or green'.replace('or', 'and') //=> 'Red and blue or green'

Copy

    // A global, case-insensitive replacement:
    let text = "Mr Blue has a blue house and a blue car";
    let result = text.replace(/blue/gi, "red");

Copy

    // A function to return the replacement text:
    let text = "Mr Blue has a blue house and a blue car";
    let result = text.replace(/blue|house|car/i, function (x) {
      return x.toUpperCase();
    });

`_String_`.`**replaceAll()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringreplaceall)

--------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns a string with all occurrences of `pattern` replaced by `replacement`

**Syntax:** `_String_`.replaceAll(pattern, replacement)

**Returns:** String

**Source:** JavaScript function

**Parameters:**

*   `pattern` (String|RegExp) - The pattern in the string to replace. Can be a string to match or a <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular\_expressions”>regular expression.
    
*   `replacement` (String|function) - The new text to replace with. Can be a string or a function that returns a string (see examples).
    

**Examples:**

Copy

    'Red or blue or green'.replace('or', 'and') //=> 'Red and blue and green'

Copy

    // Uppercase any occurrences of 'blue' or 'car'
    // (You must include the 'g' flag when using a regex)
    
    // text = 'Mr Blue has a blue car'
    text.replaceAll(/blue|car/gi, x => x.toUpperCase()) //=> 'Mr BLUE has a BLUE CAR'
    
    // Or with traditional function notation:
    text.replaceAll(/blue|car/gi, function(x){return x.toUpperCase()}) //=> 'Mr BLUE has a BLUE CAR'

`_String_`.`**replaceSpecialChars()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringreplacespecialchars)

--------------------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Replaces special characters in the string with the closest ASCII character

**Syntax:** `_String_`.replaceSpecialChars()

**Returns:** String

**Source:** Custom n8n functionality

**Examples:**

Copy

    "déjà".replaceSpecialChars() //=> "deja"

`_String_`.`**search()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringsearch)

------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns the index (position) of the first occurrence of a pattern within the string, or -1 if not found. The pattern is specified using a <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular\_expressions”>regular expression. To use text instead, see `indexOf()`.

**Syntax:** `_String_`.search(regexp)

**Returns:** Number

**Source:** JavaScript function

**Parameters:**

*   `regexp` (RegExp) - A <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular\_expressions”>regular expression with the pattern to look for
    

**Examples:**

Copy

    // Pos of first word starting with 'n'
    "Neat n8n node".search(/n[^ ]*/) //=> 5

Copy

    // Case-insensitive match with 'i'
    // Pos of first word starting with 'n' or 'N'
    "Neat n8n node".search(/n[^ ]*/i) //=> 0

`_String_`.`**slice()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringslice)

----------------------------------------------------------------------------------------------------------------------------

**Description:** Extracts a fragment of the string at the given position. For more advanced extraction, see `match()`.

**Syntax:** `_String_`.slice(start, end?)

**Returns:** String

**Source:** JavaScript function

**Parameters:**

*   `start` (Number) - The position to start from. Positions start at 0. Negative numbers count back from the end of the string.
    
*   `end` (String) - optional - The position to select up to. The character at the end position is not included. Negative numbers select from the end of the string. If omitted, will extract to the end of the string.
    

**Examples:**

Copy

    'Hello from n8n'.slice(0, 5) //=> 'Hello'

Copy

    'Hello from n8n'.slice(6) //=> 'from n8n'

Copy

    'Hello from n8n'.slice(-3) //=> 'n8n'

`_String_`.`**split()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringsplit)

----------------------------------------------------------------------------------------------------------------------------

**Description:** Splits the string into an array of substrings. Each split is made at the `separator`, and the separator isn’t included in the output.

The opposite of using `join()` on an array.

**Syntax:** `_String_`.split(separator?, limit?)

**Returns:** Array

**Source:** JavaScript function

**Parameters:**

*   `separator` (String) - optional - The string (or regular expression) to use for splitting. If omitted, an array with the original string is returned.
    
*   `limit` (Number) - optional - The max number of array elements to return. Returns all elements if omitted.
    

**Examples:**

Copy

    "wind,fire,water".split(",") //=> ['wind', 'fire', 'water']

Copy

    "me and you and her".split("and") //=> ['me ', ' you ', ' her']

Copy

    // Split one or more of space, comma and '?' using a regular expression
    "me? you, and her".split(/[ ,?]+/) //=> ['me', 'you', 'and', 'her']

`_String_`.`**startsWith()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringstartswith)

--------------------------------------------------------------------------------------------------------------------------------------

**Description:** Returns `true` if the string starts with `searchString`. Case-sensitive.

**Syntax:** `_String_`.startsWith(searchString, start?)

**Returns:** Boolean

**Source:** JavaScript function

**Parameters:**

*   `searchString` (String) - The text to check against the start of the base string
    
*   `start` (Number) - optional - The position (index) to start searching from
    

**Examples:**

Copy

    'team'.startsWith('tea') //=> true
    'team'.startsWith('Tea') //=> false

Copy

    // Returns false if the case doesn't match, so consider using .toLowerCase() first
    'Team'.toLowerCase().startsWith('tea') //=> true

`_String_`.`**substring()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringsubstring)

------------------------------------------------------------------------------------------------------------------------------------

**Description:** Extracts a fragment of the string at the given position. For more advanced extraction, see `match()`.

**Syntax:** `_String_`.substring(start, end?)

**Returns:** String

**Source:** JavaScript function

**Parameters:**

*   `start` (Number) - The position to start from. Positions start at 0.
    
*   `end` (String) - optional - The position to select up to. The character at the end position is not included. If omitted, will extract to the end of the string.
    

**Examples:**

Copy

    'Hello from n8n'.substring(0, 5) //=> 'Hello'

Copy

    'Hello from n8n'.substring(6) //=> 'from n8n'

`_String_`.`**toBoolean()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringtoboolean)

------------------------------------------------------------------------------------------------------------------------------------

**Description:** Converts the string to a boolean value. `0`, `false` and `no` resolve to `false`, everything else to `true`. Case-insensitive.

**Syntax:** `_String_`.toBoolean()

**Returns:** Boolean

**Source:** Custom n8n functionality

**Examples:**

Copy

    "true".toBoolean() //=> true

Copy

    "false".toBoolean() //=> false

Copy

    "0".toBoolean() //=> false

Copy

    "hello".toBoolean() //=> true

`_String_`.`**toDateTime()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringtodatetime)

--------------------------------------------------------------------------------------------------------------------------------------

**Description:** Converts the string to a DateTime. Useful for further transformation. Supported formats for the string are ISO 8601, HTTP, RFC2822, SQL and Unix timestamp in milliseconds.

To parse other formats, use <a href=”https://moment.github.io/luxon/api-docs/index.html#datetimefromformat”> `DateTime.fromFormat()`.

**Syntax:** `_String_`.toDateTime()

**Returns:** DateTime

**Source:** Custom n8n functionality

**Examples:**

Copy

    "2024-03-29T18:06:31.798+01:00".toDateTime()

Copy

    "Fri, 29 Mar 2024 18:08:01 +0100".toDateTime()

Copy

    "20240329".toDateTime()

Copy

    "1711732132990".toDateTime()

`_String_`.`**toJsonString()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringtojsonstring)

------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Prepares the string to be inserted into a JSON object. Escapes any quotes and special characters (e.g. new lines), and wraps the string in quotes.

The same as JavaScript’s `JSON.stringify()`.

**Syntax:** `_String_`.toJsonString()

**Returns:** String

**Source:** Custom n8n functionality

**Examples:**

Copy

    // str = 'The "best" colours: red\nbrown'
    str.toJsonString() //=> '"The \\"best\\" colours: red\\nbrown"'

`_String_`.`**toLowerCase()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringtolowercase)

----------------------------------------------------------------------------------------------------------------------------------------

**Description:** Converts all letters in the string to lower case

**Syntax:** `_String_`.toLowerCase()

**Returns:** String

**Source:** JavaScript function

**Examples:**

Copy

    "I'm SHOUTing".toLowerCase() //=> "i'm shouting"

`_String_`.`**toNumber()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringtonumber)

----------------------------------------------------------------------------------------------------------------------------------

**Description:** Converts a string representing a number to a number. Throws an error if the string doesn’t start with a valid number.

**Syntax:** `_String_`.toNumber()

**Returns:** Number

**Source:** Custom n8n functionality

**Examples:**

Copy

    "123".toNumber() //=> 123

Copy

    "1.23E10".toNumber() //=> 12300000000

`_String_`.`**toSentenceCase()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringtosentencecase)

----------------------------------------------------------------------------------------------------------------------------------------------

**Description:** Changes the capitalization of the string to sentence case. The first letter of each sentence is capitalized and all others are lowercased.

**Syntax:** `_String_`.toSentenceCase()

**Returns:** String

**Source:** Custom n8n functionality

**Examples:**

Copy

    "quick! brown FOX".toSentenceCase() //=> "Quick! Brown fox"

`_String_`.`**toSnakeCase()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringtosnakecase)

----------------------------------------------------------------------------------------------------------------------------------------

**Description:** Changes the format of the string to snake case. Spaces and dashes are replaced by `_`, symbols are removed and all letters are lowercased.

**Syntax:** `_String_`.toSnakeCase()

**Returns:** String

**Source:** Custom n8n functionality

**Examples:**

Copy

    "quick brown $FOX".toSnakeCase() //=> "quick_brown_fox"

`_String_`.`**toTitleCase()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringtotitlecase)

----------------------------------------------------------------------------------------------------------------------------------------

**Description:** Changes the capitalization of the string to title case. The first letter of each word is capitalized and the others left unchanged. Short prepositions and conjunctions aren’t capitalized (e.g. ‘a’, ‘the’).

**Syntax:** `_String_`.toTitleCase()

**Returns:** String

**Source:** Custom n8n functionality

**Examples:**

Copy

    "quick a brown FOX".toTitleCase() //=> "Quick a Brown Fox"

`_String_`.`**toUpperCase()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringtouppercase)

----------------------------------------------------------------------------------------------------------------------------------------

**Description:** Converts all letters in the string to upper case (capitals)

**Syntax:** `_String_`.toUpperCase()

**Source:** JavaScript function

**Examples:**

Copy

    "I'm not angry".toUpperCase() //=> "I'M NOT ANGRY"

`_String_`.`**trim()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringtrim)

--------------------------------------------------------------------------------------------------------------------------

**Description:** Removes whitespace from both ends of the string. Whitespace includes new lines, tabs, spaces, etc.

**Syntax:** `_String_`.trim()

**Returns:** String

**Source:** JavaScript function

**Examples:**

Copy

    '   lonely   '.trim() //=> 'lonely'

`_String_`.`**urlDecode()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringurldecode)

------------------------------------------------------------------------------------------------------------------------------------

**Description:** Decodes a URL-encoded string. Replaces any character codes in the form of `%XX` with their corresponding characters.

**Syntax:** `_String_`.urlDecode(allChars?)

**Returns:** String

**Source:** Custom n8n functionality

**Parameters:**

*   `allChars` (Boolean) - optional - Whether to decode characters that are part of the URI syntax (e.g. `=`, `?`)
    

**Examples:**

Copy

    "name%3DNathan%20Automat".urlDecode() //=> "name=Nathan Automat"

Copy

    "name%3DNathan%20Automat".urlDecode(true) //=> "name%3DNathan Automat"

`_String_`.`**urlEncode()**`[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#stringurlencode)

------------------------------------------------------------------------------------------------------------------------------------

**Description:** Encodes the string so that it can be used in a URL. Spaces and special characters are replaced with codes of the form `%XX`.

**Syntax:** `_String_`.urlEncode(allChars?)

**Returns:** String

**Source:** Custom n8n functionality

**Parameters:**

*   `allChars` (Boolean) - optional - Whether to encode characters that are part of the URI syntax (e.g. `=`, `?`)
    

**Examples:**

Copy

    "name=Nathan Automat".urlEncode() //=> "name%3DNathan%20Automat"

Copy

    "name=Nathan Automat".urlEncode(true) //=> "name=Nathan%20Automat"

Related resources[](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string#related-resources)

---------------------------------------------------------------------------------------------------------------------------

*   [Expression reference](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference)
    

[PreviousRoot](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root)
[NextWorkflowdata](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/workflowdata)

Last updated 10 days ago

Was this helpful?