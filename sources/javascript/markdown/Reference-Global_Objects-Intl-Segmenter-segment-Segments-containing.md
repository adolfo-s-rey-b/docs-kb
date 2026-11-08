*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment/Segments/containing#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment/Segments/containing#mdn-search)
    

Segments.prototype.containing()
===============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2024.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment/Segments/containing#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`containing()`** method of [`Segments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment/Segments)
 instances returns an object describing the segment in the string that includes the code unit at the specified index.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment/Segments/containing#try_it)

---------------------------------------------------------------------------------------------------------------------------------------------

    const segmenterFr = new Intl.Segmenter("fr", { granularity: "word" });
    const string = "Que ma joie demeure";
    
    const segments = segmenterFr.segment(string);
    
    console.log(segments.containing(5));
    // Expected output:
    // Object {segment: 'ma', index: 4, input: 'Que ma joie demeure', isWordLike: true}
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment/Segments/containing#syntax)

---------------------------------------------------------------------------------------------------------------------------------------------

js

    containing(codeUnitIndex)
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment/Segments/containing#parameters)

[`codeUnitIndex` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment/Segments/containing#codeunitindex)

A number specifying the index of the code unit in the original input string. If the value is omitted, it defaults to `0`.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment/Segments/containing#return_value)

An object describing the segment of the original string with the following properties, or `undefined` if the supplied index value is out of bounds.

[`segment`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment/Segments/containing#segment)

A string containing the segment extracted from the original input string.

[`index`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment/Segments/containing#index)

The code unit index in the original input string at which the segment begins.

[`input`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment/Segments/containing#input)

The complete input string that was segmented.

[`isWordLike`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment/Segments/containing#iswordlike)

A boolean value only if `granularity` is `"word"`; otherwise, `undefined`. If `granularity` is `"word"`, then `isWordLike` is `true` when the segment is word-like (i.e., consists of letters/numbers/ideographs/etc.); otherwise, `false`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment/Segments/containing#examples)

-------------------------------------------------------------------------------------------------------------------------------------------------

js

    // ┃0 1 2 3 4 5┃6┃7┃8┃9  ← code unit index
    // ┃A l l o n s┃-┃y┃!┃   ← code unit
    const input = "Allons-y!";
    
    const segmenter = new Intl.Segmenter("fr", { granularity: "word" });
    const segments = segmenter.segment(input);
    
    let current = segments.containing();
    // { index: 0, segment: "Allons", isWordLike: true }
    
    current = segments.containing(4);
    // { index: 0, segment: "Allons", isWordLike: true }
    
    current = segments.containing(6);
    // { index: 6, segment: "-", isWordLike: false }
    
    current = segments.containing(current.index + current.segment.length);
    // { index: 7, segment: "y", isWordLike: true }
    
    current = segments.containing(current.index + current.segment.length);
    // { index: 8, segment: "!", isWordLike: false }
    
    current = segments.containing(current.index + current.segment.length);
    // undefined
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment/Segments/containing#specifications)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Internationalization API Specification  <br>\# sec-%intlsegmentsprototype%.containing](https://tc39.es/ecma402/#sec-%intlsegmentsprototype%.containing) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment/Segments/containing#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment/Segments/containing#see_also)

-------------------------------------------------------------------------------------------------------------------------------------------------

*   [`Intl.Segmenter`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter)
    
*   [`Intl.Segmenter.prototype.segment()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 20, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter/segment/Segments/containing/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/intl/segmenter/segment/segments/containing/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/intl/segmenter/segment/segments/containing (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FSegmenter%2Fsegment%2FSegments%2Fcontaining&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Fsegmenter%2Fsegment%2Fsegments%2Fcontaining%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FSegmenter%2Fsegment%2FSegments%2Fcontaining%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Fsegmenter%2Fsegment%2Fsegments%2Fcontaining%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcd22b9f18cf2450c0cc488379b8b780f0f343397%0A*+Document+last+modified%3A+2025-07-20T13%3A51%3A13.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")