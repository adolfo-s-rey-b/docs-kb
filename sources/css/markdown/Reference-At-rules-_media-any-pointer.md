*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/any-pointer#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/any-pointer#mdn-search)
    

`any-pointer` CSS media feature
===============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since December 2018.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/any-pointer#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`any-pointer`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 tests whether the user has _any_ pointing device (such as a mouse), and if so, how accurate it is.

**Note:** If you want to test the accuracy of the _primary_ pointing device, use [`pointer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/pointer)
 instead.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/any-pointer#syntax)

--------------------------------------------------------------------------------------------------------

The `any-pointer` feature is specified as a keyword value chosen from the list below.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/any-pointer#none)

No pointing device is available.

[`coarse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/any-pointer#coarse)

At least one input mechanism includes a pointing device of limited accuracy.

[`fine`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/any-pointer#fine)

At least one input mechanism includes an accurate pointing device.

**Note:** More than one value can match if the available devices have different characteristics, although `none` only matches when none of them are pointing devices.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/any-pointer#examples)

------------------------------------------------------------------------------------------------------------

This example creates a small checkbox for users with at least one fine pointer and a large checkbox for users with at least one coarse pointer. The big checkbox takes precedence because it is declared after the small one.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/any-pointer#html)

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/any-pointer#css)

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/any-pointer#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/any-pointer#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Media Queries Level 4  <br>\# descdef-media-any-pointer](https://drafts.csswg.org/mediaqueries/#descdef-media-any-pointer) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/any-pointer#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/any-pointer#see_also)

------------------------------------------------------------------------------------------------------------

*   [The `pointer` media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/pointer)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/any-pointer/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/any-pointer/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/any-pointer (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fany-pointer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fany-pointer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fany-pointer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fany-pointer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F67d40334c8b90e4623f3b0d3aea466b9882d8236%0A*+Document+last+modified%3A+2026-04-20T16%3A07%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")