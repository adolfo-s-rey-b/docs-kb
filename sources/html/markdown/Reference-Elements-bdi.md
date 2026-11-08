*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi#mdn-search)
    

`<bdi>` HTML bidirectional isolate element
==========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<bdi>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element tells the browser's bidirectional algorithm to treat the text it contains in isolation from its surrounding text. It's particularly useful when a website dynamically inserts some text and doesn't know the directionality of the text being inserted.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi#try_it)

------------------------------------------------------------------------------------------

    <h1>World wrestling championships</h1>
    
    <ul>
      <li><bdi class="name">Evil Steven</bdi>: 1st place</li>
      <li><bdi class="name">François fatale</bdi>: 2nd place</li>
      <li><span class="name">سما</span>: 3rd place</li>
      <li><bdi class="name">الرجل القوي إيان</bdi>: 4th place</li>
      <li><span class="name" dir="auto">سما</span>: 5th place</li>
    </ul>
    

    html {
      font-family: sans-serif;
    }
    
    bdi {
      /* Add your styles here */
    }
    
    .name {
      color: red;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi#attributes)

--------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

If the [`dir`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir)
 attribute is unspecified, the element still behaves as if `dir="auto"` is specified.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi#usage_notes)

----------------------------------------------------------------------------------------------------

Bidirectional text is text that may contain both sequences of characters that are arranged left-to-right (LTR) and sequences of characters that are arranged right-to-left (RTL), such as an Arabic quotation embedded in an English string. Browsers implement the [Unicode Bidirectional Algorithm](https://www.w3.org/International/articles/inline-bidi-markup/uba-basics "External link (opens in new tab)")
 to handle this. In this algorithm, characters are given an implicit directionality: for example, Latin characters are treated as LTR while Arabic characters are treated as RTL. Some other characters (such as spaces and some punctuation) are treated as neutral and are assigned directionality based on that of their surrounding characters.

Usually, the bidirectional algorithm will do the right thing without the author having to provide any special markup but, occasionally, the algorithm needs help. That's where `<bdi>` comes in.

The `<bdi>` element is used to wrap a span of text and instructs the bidirectional algorithm to treat this text in isolation from its surroundings. This works in two ways:

*   The directionality of text embedded in `<bdi>` _does not influence_ the directionality of the surrounding text.
*   The directionality of text embedded in `<bdi>` _is not influenced by_ the directionality of the surrounding text.

For example, consider some text like:

EMBEDDED-TEXT - 1st place

If `EMBEDDED-TEXT` is LTR, this works fine. But if `EMBEDDED-TEXT` is RTL, then `- 1` will be treated as RTL text (because it consists of neutral and weak characters). The result will be garbled:

1 - EMBEDDED-TEXTst place

If you know the directionality of `EMBEDDED-TEXT` in advance, you can fix this problem by wrapping `EMBEDDED-TEXT` in a [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 with the [`dir`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir)
 attribute set to the known directionality. But if you don't know the directionality - for example, because `EMBEDDED-TEXT` is being read from a database or entered by the user - you should use `<bdi>` to prevent the directionality of `EMBEDDED-TEXT` from affecting its surroundings.

Though the same visual effect can be achieved using the CSS rule [`unicode-bidi: isolate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi)
 on a [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 or another text-formatting element, HTML authors should not use this approach because it is not semantic and browsers are allowed to ignore CSS styling.

If a semantic element such as [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite)
 is appropriate, prefer using `<cite dir="auto">` instead of `<bdi>`. If no semantic element is appropriate and the intended direction is `auto` (infer from content), `<bdi>` is shorter than `<span dir="auto">` and conveys the author intent better. When specifying explicit directionalities such as `ltr`, `<bdi dir="ltr">` and `<span dir="ltr">` are exactly equivalent.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi#examples)

----------------------------------------------------------------------------------------------

### [No bdi with only LTR](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi#no_bdi_with_only_ltr)

This example lists the winners of a competition using [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 elements only. When the names only contain LTR text the results look fine:

html

    <ul>
      <li><span class="name">Henrietta Boffin</span> - 1st place</li>
      <li><span class="name">Jerry Cruncher</span> - 2nd place</li>
    </ul>
    

    body {
      border: 1px solid #3f87a6;
      max-width: calc(100% - 40px - 6px);
      padding: 20px;
      width: calc(100% - 40px - 6px);
      border-width: 1px 1px 1px 5px;
    }
    

### [No bdi with RTL text](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi#no_bdi_with_rtl_text)

This example lists the winners of a competition using [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 elements only, and one of the winners has a name consisting of RTL text. In this case the `- 1`, which consists of characters with neutral or weak directionality, will adopt the directionality of the RTL text, and the result will be garbled:

html

    <ul>
      <li><span class="name">اَلأَعْشَى</span> - 1st place</li>
      <li><span class="name">Jerry Cruncher</span> - 2nd place</li>
    </ul>
    

    body {
      border: 1px solid #3f87a6;
      max-width: calc(100% - 40px - 6px);
      padding: 20px;
      width: calc(100% - 40px - 6px);
      border-width: 1px 1px 1px 5px;
    }
    

### [Using bdi with LTR and RTL text](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi#using_bdi_with_ltr_and_rtl_text)

This example lists the winners of a competition using `<bdi>` elements. These elements instruct the browser to treat the name in isolation from its embedding context, so the example output is properly ordered:

html

    <ul>
      <li><bdi class="name">اَلأَعْشَى</bdi> - 1st place</li>
      <li><bdi class="name">Jerry Cruncher</bdi> - 2nd place</li>
    </ul>
    

    body {
      border: 1px solid #3f87a6;
      max-width: calc(100% - 40px - 6px);
      padding: 20px;
      width: calc(100% - 40px - 6px);
      border-width: 1px 1px 1px 5px;
    }
    

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi#technical_summary)

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | `[generic](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/generic_role) ` |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-bdi-element](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-bdi-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi#see_also)

----------------------------------------------------------------------------------------------

*   [Inline markup and bidirectional text in HTML](https://www.w3.org/International/articles/inline-bidi-markup/ "External link (opens in new tab)")
    
*   [Unicode Bidirectional Algorithm basics](https://www.w3.org/International/articles/inline-bidi-markup/uba-basics "External link (opens in new tab)")
    
*   [Localization](https://developer.mozilla.org/en-US/docs/Glossary/Localization)
    
*   Related HTML element: [`<bdo>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo)
    
*   Related CSS properties: [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
    , [`unicode-bidi`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 28, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/bdi/index.md?plain=1 "Folder: en-us/web/html/reference/elements/bdi (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fbdi&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fbdi%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fbdi%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fbdi%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fda275ce3eae1d8d250f1079b4643213a7a2bbb90%0A*+Document+last+modified%3A+2026-08-28T22%3A26%3A59.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")