*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/EPSILON#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/EPSILON#mdn-search)
    

Number.EPSILON
==============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/EPSILON#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`Number.EPSILON`** static data property represents the difference between 1 and the smallest floating point number greater than 1.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/EPSILON#try_it)

-----------------------------------------------------------------------------------------------------------------

[Value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/EPSILON#value)

---------------------------------------------------------------------------------------------------------------

2\-52, or approximately `2.2204460492503130808472633361816E-16`.

|     |     |
| --- | --- |
| Writable | no  |
| Enumerable | no  |
| Configurable | no  |

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/EPSILON#description)

---------------------------------------------------------------------------------------------------------------------------

`Number.EPSILON` is the difference between 1 and the next greater number representable in the Number format, because [double precision floating point format](https://en.wikipedia.org/wiki/Double_precision_floating-point_format "External link (opens in new tab)")
 only has 52 bits to represent the [mantissa](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number#number_encoding)
, and the lowest bit has a significance of 2\-52.

Note that the absolute accuracy of floating numbers decreases as the number gets larger, because the exponent grows while the mantissa's accuracy stays the same. [`Number.MIN_VALUE`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MIN_VALUE)
 is the smallest representable positive number, which is much smaller than `Number.EPSILON`.

Because `EPSILON` is a static property of [`Number`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)
, you always use it as `Number.EPSILON`, rather than as a property of a number value.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/EPSILON#examples)

---------------------------------------------------------------------------------------------------------------------

### [Testing equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/EPSILON#testing_equality)

Any number encoding system occupying a finite number of bits, of whatever base you choose (e.g., decimal or binary), will _necessarily_ be unable to represent all numbers exactly, because you are trying to represent an infinite number of points on the number line using a finite amount of memory. For example, a base-10 (decimal) system cannot represent 1/3 exactly, and a base-2 (binary) system cannot represent `0.1` exactly. Thus, for example, `0.1 + 0.2` is not exactly equal to `0.3`:

For this reason, it is often advised that **floating point numbers should never be compared with `===`**. Instead, we can deem two numbers as equal if they are _close enough_ to each other. The `Number.EPSILON` constant is usually a reasonable threshold for errors if the arithmetic is around the magnitude of `1`, because `EPSILON`, in essence, specifies how accurate the number "1" is.

However, `Number.EPSILON` is inappropriate for any arithmetic operating on a larger magnitude. If your data is on the 103 order of magnitude, the decimal part will have a much smaller accuracy than `Number.EPSILON`:

In this case, a larger tolerance is required. As the numbers compared have a magnitude of approximately `2000`, a multiplier such as `2000 * Number.EPSILON` creates enough tolerance for this instance.

In addition to magnitude, it is important to consider the _accuracy_ of your input. For example, if the numbers are collected from a form input and the input value can only be adjusted by steps of `0.1` (i.e., [`<input type="number" step="0.1">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/step)
), it usually makes sense to allow a much larger tolerance, such as `0.01`, since the data only has a precision of `0.1`.

**Note:** Important takeaway: do not simply use `Number.EPSILON` as a threshold for equality testing. Use a threshold that is appropriate for the magnitude and accuracy of the numbers you are comparing.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/EPSILON#specifications)

---------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-number.epsilon](https://tc39.es/ecma262/multipage/numbers-and-dates.html#sec-number.epsilon) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/EPSILON#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/EPSILON#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [Polyfill of `Number.EPSILON` in `core-js`](https://core-js.io/docs/features/ecmascript/number "External link (opens in new tab)")
    
*   [es-shims polyfill of `Number.EPSILON`](https://www.npmjs.com/package/es-constants "External link (opens in new tab)")
    
*   [`Number`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/EPSILON/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/number/epsilon/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/number/epsilon (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FNumber%2FEPSILON&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fnumber%2Fepsilon%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FNumber%2FEPSILON%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fnumber%2Fepsilon%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")