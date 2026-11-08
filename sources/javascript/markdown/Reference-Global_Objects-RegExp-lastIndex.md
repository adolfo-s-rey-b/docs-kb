*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex#mdn-search)
    

RegExp: lastIndex
=================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`lastIndex`** data property of a [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
 instance specifies the index at which to start the next match.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex#try_it)

-------------------------------------------------------------------------------------------------------------------

    const regex = /foo/g;
    const str = "table football, foosball";
    
    regex.test(str);
    
    console.log(regex.lastIndex);
    // Expected output: 9
    
    regex.test(str);
    
    console.log(regex.lastIndex);
    // Expected output: 19
    

[Value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex#value)

-----------------------------------------------------------------------------------------------------------------

A non-negative integer.

|     |     |
| --- | --- |
| Writable | yes |
| Enumerable | no  |
| Configurable | no  |

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex#description)

-----------------------------------------------------------------------------------------------------------------------------

This property is set only if the regular expression instance used the `g` flag to indicate a global search, or the `y` flag to indicate a sticky search. The following rules apply when [`exec()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec)
 is called on a given input:

*   If `lastIndex` is greater than the length of the input, `exec()` will not find a match, and `lastIndex` will be set to 0.
*   If `lastIndex` is equal to or less than the length of the input, `exec()` will attempt to match the input starting from `lastIndex`.
    *   If `exec()` finds a match, then `lastIndex` will be set to the position of the end of the matched string in the input.
    *   If `exec()` does not find a match, then `lastIndex` will be set to 0.

Other regex-related methods, such as [`RegExp.prototype.test()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/test)
, [`String.prototype.match()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match)
, [`String.prototype.replace()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)
, etc., call `exec()` under the hood, so they have different effects on `lastIndex`. See their respective pages for details.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex#examples)

-----------------------------------------------------------------------------------------------------------------------

### [Using lastIndex](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex#using_lastindex)

Consider the following sequence of statements:

js

    const re = /(hi)?/g;
    

Matches the empty string.

js

    console.log(re.exec("hi"));
    console.log(re.lastIndex);
    

Returns `["hi", "hi"]` with `lastIndex` equal to 2.

js

    console.log(re.exec("hi"));
    console.log(re.lastIndex);
    

Returns `["", undefined]`, an empty array whose zeroth element is the match string. In this case, the empty string because `lastIndex` was 2 (and still is 2) and `hi` has length 2.

### [Using lastIndex with sticky regexes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex#using_lastindex_with_sticky_regexes)

The `lastIndex` property is writable. You can set it to make the regex start its next search at a given index.

The `y` flag almost always requires setting `lastIndex`. It always matches strictly at `lastIndex` and does not attempt any later positions. This is usually useful for writing parsers, when you want to match tokens only at the current position.

js

    const stringPattern = /"[^"]*"/y;
    const input = `const message = "Hello world";`;
    
    stringPattern.lastIndex = 6;
    console.log(stringPattern.exec(input)); // null
    
    stringPattern.lastIndex = 16;
    console.log(stringPattern.exec(input)); // ['"Hello world"']
    

### [Rewinding lastIndex](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex#rewinding_lastindex)

The `g` flag also benefits from setting `lastIndex`. One common use case is when the string is modified in the middle of a global search. In this case, we may miss a particular match if the string is shortened. We can avoid this by rewinding `lastIndex`.

js

    const mdLinkPattern = /\[[^[\]]+\]\((?<link>[^()\s]+)\)/dg;
    
    function resolveMDLink(line) {
      let match;
      let modifiedLine = line;
      while ((match = mdLinkPattern.exec(modifiedLine))) {
        const originalLink = match.groups.link;
        const resolvedLink = originalLink.replaceAll(/^files|\/index\.md$/g, "");
        modifiedLine =
          modifiedLine.slice(0, match.indices.groups.link[0]) +
          resolvedLink +
          modifiedLine.slice(match.indices.groups.link[1]);
        // Rewind the pattern to the end of the resolved link
        mdLinkPattern.lastIndex += resolvedLink.length - originalLink.length;
      }
      return modifiedLine;
    }
    
    console.log(
      resolveMDLink(
        "[`lastIndex`](files/en-us/web/javascript/reference/global_objects/regexp/lastindex/index.md)",
      ),
    ); // [`lastIndex`](/en-us/web/javascript/reference/global_objects/regexp/lastindex)
    console.log(
      resolveMDLink(
        "[`ServiceWorker`](files/en-us/web/api/serviceworker/index.md) and [`SharedWorker`](files/en-us/web/api/sharedworker/index.md)",
      ),
    ); // [`ServiceWorker`](/en-us/web/api/serviceworker) and [`SharedWorker`](/en-us/web/api/sharedworker)
    

Try deleting the `mdLinkPattern.lastIndex += resolvedLink.length - originalLink.length` line and running the second example. You will find that the second link is not replaced correctly, because the `lastIndex` is already past the link's index after the string is shortened.

**Warning:** This example is for demonstration only. To deal with Markdown, you should probably use a parsing library instead of regex.

### [Optimizing searching](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex#optimizing_searching)

You can optimize searching by setting `lastIndex` to a point where previous possible occurrences can be ignored. For example, instead of this:

js

    const stringPattern = /"[^"]*"/g;
    const input = `const message = "Hello " + "world";`;
    
    // Pretend we've already dealt with the previous parts of the string
    let offset = 26;
    const remainingInput = input.slice(offset);
    const nextString = stringPattern.exec(remainingInput);
    console.log(nextString[0]); // "world"
    offset += nextString.index + nextString.length;
    

Consider this:

js

    stringPattern.lastIndex = offset;
    const nextString = stringPattern.exec(remainingInput);
    console.log(nextString[0]); // "world"
    offset = stringPattern.lastIndex;
    

This is potentially more performant because we avoid string slicing.

### [Avoiding side effects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex#avoiding_side_effects)

The side effects caused by `exec()` can be confusing, especially if the input is different for each `exec()`.

js

    const re = /foo/g;
    console.log(re.test("foo bar")); // true
    console.log(re.test("foo baz")); // false, because lastIndex is non-zero
    

This is even more confusing when you are hand-modifying `lastIndex`. To contain the side effects, remember to reset `lastIndex` after each input is completely processed.

js

    const re = /foo/g;
    console.log(re.test("foo bar")); // true
    re.lastIndex = 0;
    console.log(re.test("foo baz")); // true
    

With some abstraction, you can require `lastIndex` to be set to a particular value before each `exec()` call.

js

    function createMatcher(pattern) {
      // Create a copy, so that the original regex is never updated
      const regex = new RegExp(pattern, "g");
      return (input, offset) => {
        regex.lastIndex = offset;
        return regex.exec(input);
      };
    }
    
    const matchFoo = createMatcher(/foo/);
    console.log(matchFoo("foo bar", 0)[0]); // "foo"
    console.log(matchFoo("foo baz", 0)[0]); // "foo"
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex#specifications)

-----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-properties-of-regexp-instances](https://tc39.es/ecma262/multipage/text-processing.html#sec-properties-of-regexp-instances) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex#see_also)

-----------------------------------------------------------------------------------------------------------------------

*   [`RegExp.prototype.dotAll`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/dotAll)
    
*   [`RegExp.prototype.global`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/global)
    
*   [`RegExp.prototype.hasIndices`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/hasIndices)
    
*   [`RegExp.prototype.ignoreCase`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/ignoreCase)
    
*   [`RegExp.prototype.multiline`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/multiline)
    
*   [`RegExp.prototype.source`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/source)
    
*   [`RegExp.prototype.sticky`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/sticky)
    
*   [`RegExp.prototype.unicode`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 20, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/lastIndex/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/regexp/lastindex/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/regexp/lastindex (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FRegExp%2FlastIndex&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fregexp%2Flastindex%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FRegExp%2FlastIndex%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fregexp%2Flastindex%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcd22b9f18cf2450c0cc488379b8b780f0f343397%0A*+Document+last+modified%3A+2025-07-20T13%3A51%3A13.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")