*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/BigInt_not_serializable#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/BigInt_not_serializable#mdn-search)
    

TypeError: BigInt value can't be serialized in JSON
===================================================

The JavaScript exception "BigInt value can't be serialized in JSON" occurs when a [`BigInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
 is encountered in [`JSON.stringify`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
 with no custom serialization method provided.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/BigInt_not_serializable#message)

--------------------------------------------------------------------------------------------------------------------

TypeError: Do not know how to serialize a BigInt (V8-based)
TypeError: BigInt value can't be serialized in JSON (Firefox)
TypeError: JSON.stringify cannot serialize BigInt. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/BigInt_not_serializable#error_type)

--------------------------------------------------------------------------------------------------------------------------

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/BigInt_not_serializable#what_went_wrong)

-------------------------------------------------------------------------------------------------------------------------------------

You are trying to serialize a BigInt value using `JSON.stringify`, which does not support BigInt values by default. Sometimes, JSON stringification happens implicitly in libraries, as part of data serialization. For example, sending data to the server, storing it in external storage, or transferring it between threads would all require serialization, which is often done using JSON.

There are several ways to handle this:

*   If you can alter the data source, avoid using BigInt values and cast it to a number first (which may lose precision for large numbers).
*   If you can alter the stringification process, pass a replacer function to `JSON.stringify` that converts BigInt values to strings or numbers.
*   You can also provide a `BigInt.prototype.toJSON` method globally that gets called whenever a BigInt value is stringified.

For more information on various tradeoffs, see [BigInt reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt#use_within_json)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/BigInt_not_serializable#examples)

----------------------------------------------------------------------------------------------------------------------

### [Providing a custom serialization method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/BigInt_not_serializable#providing_a_custom_serialization_method)

By default, BigInt values are not serializable in JSON:

Assuming you intend for the JSON to contain a number value, here are a few approaches that work:

*   Convert the BigInt to a number before stringifying:
    
*   Provide a replacer function that converts BigInt values to numbers or [raw JSON objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/rawJSON)
    :
    
*   Provide a `BigInt.prototype.toJSON` method that gets called whenever a BigInt value is stringified:
    

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/BigInt_not_serializable#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [`BigInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
    
*   [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
    
*   [`JSON.rawJSON()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/rawJSON)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/BigInt_not_serializable/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/bigint_not_serializable/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/bigint_not_serializable (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FBigInt_not_serializable&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fbigint_not_serializable%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FBigInt_not_serializable%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fbigint_not_serializable%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4026c18a22b6ceb24e69adf4851de13af8fab92d%0A*+Document+last+modified%3A+2025-09-10T12%3A36%3A38.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")