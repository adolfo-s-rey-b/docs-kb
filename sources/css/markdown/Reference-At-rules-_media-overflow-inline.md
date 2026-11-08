*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/overflow-inline#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/overflow-inline#mdn-search)
    

`overflow-inline` CSS media feature
===================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/overflow-inline#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`overflow-inline`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 can be used to test how the output device handles content that overflows the initial [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
 along the inline axis.

**Note:** The `overflow-inline` property does not determine whether overflow occurs; rather, it reveals the device's handling of such overflow. Typically, on screens in most browsers, the behavior will be "scroll": when content exceeds the available horizontal space, the device allows you to scroll to access the overflowed content.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/overflow-inline#syntax)

------------------------------------------------------------------------------------------------------------

The `overflow-inline` feature is specified as a keyword value chosen from the list below.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/overflow-inline#none)

Content that overflows the inline axis is not displayed.

[`scroll`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/overflow-inline#scroll)

Content that overflows the inline axis can be seen by scrolling to it.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/overflow-inline#examples)

----------------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/overflow-inline#html)

html

    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ac turpis
      eleifend, fringilla velit ac, aliquam tellus. Vestibulum ante ipsum primis in
      faucibus orci luctus et ultrices posuere cubilia Curae; Nunc velit erat,
      tempus id rutrum sed, dapibus ut urna. Integer vehicula nibh a justo imperdiet
      rutrum. Nam faucibus pretium orci imperdiet sollicitudin. Nunc id facilisis
      dui. Proin elementum et massa et feugiat. Integer rutrum ullamcorper eleifend.
      Proin sit amet tincidunt risus. Sed nec augue congue eros accumsan tincidunt
      sed eget ex.
    </p>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/overflow-inline#css)

css

    p {
      white-space: nowrap;
    }
    
    @media (overflow-inline: scroll) {
      p {
        color: red;
      }
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/overflow-inline#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/overflow-inline#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Media Queries Level 4  <br>\# mf-overflow-inline](https://drafts.csswg.org/mediaqueries/#mf-overflow-inline) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/overflow-inline#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/overflow-inline/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/overflow-inline/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/overflow-inline (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Foverflow-inline&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Foverflow-inline%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Foverflow-inline%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Foverflow-inline%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F67d40334c8b90e4623f3b0d3aea466b9882d8236%0A*+Document+last+modified%3A+2026-04-20T16%3A07%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")