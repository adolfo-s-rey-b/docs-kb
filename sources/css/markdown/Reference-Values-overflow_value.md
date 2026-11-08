*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value#mdn-search)
    

`<overflow>` CSS type
=====================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<overflow>`** [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 value type represents the keyword values for the [`overflow-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block)
, [`overflow-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline)
, [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)
, and [`overflow-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)
 longhand properties and the [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 shorthand property. These properties apply to block containers, flex containers, and grid containers.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value#syntax)

--------------------------------------------------------------------------------------------------

<overflow> = visible | hidden | clip | scroll | auto

[Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value#values)

--------------------------------------------------------------------------------------------------

The `<overflow>` enumerated value type is specified using one of the values listed below.

[`visible`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value#visible)

Overflow content is not clipped and may be visible outside the element's padding box. The element box is not a [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
. This is the default value for all the properties that have the `<overflow>` enumerated value type.

[`hidden`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value#hidden)

Overflow content is clipped at the element's padding box. There are no scroll bars, and the clipped content is not visible (i.e., clipped content is hidden), but the content still exists. User agents do not add scrollbars and also do not allow users to view the content outside the clipped region by actions such as dragging on a touch screen or using the scroll wheel on a mouse. The content _can_ be scrolled programmatically (for example, by setting the value of the [`scrollLeft`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollLeft "scrollLeft")
 property or the [`scrollTo()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollTo "scrollTo()")
 method). The content can also be scrolled via keyboard interaction; arrows enable scrolling through the content and tabbing to a focusable element within the hidden content enables scrolling the focused element into view. The element box on which this value is set is a scroll container.

[`clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value#clip)

Overflow content is clipped at the element's _overflow clip edge_ that is defined using the [`overflow-clip-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-clip-margin)
 property. As a result, content overflows the element's padding box by the [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value of `overflow-clip-margin` or by `0px` if not set. Overflow content outside the clipped region is not visible, user agents do not add a scrollbar, and programmatic scrolling is also not supported. No new [formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
 is created.

[`scroll`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value#scroll)

Overflow content is clipped at the element's padding box, and overflow content can be scrolled into view using scrollbars. User agents display scrollbars in both horizontal and vertical directions if only one value is set, whether or not any content is overflowing or clipped. The use of this keyword value, therefore, can prevent scrollbars from appearing and disappearing as content changes. Printers may still print overflowing content. The element box on which this value is set is a scroll container.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value#auto)

Overflow content is clipped at the element's padding box, and overflow content can be scrolled into view. Unlike `scroll`, user agents display scrollbars _only if_ the content is overflowing and hide scrollbars by default. If content fits inside the element's padding box, it looks the same as with `visible` but still establishes a new formatting context. The element box on which this value is set is a scroll container.

**Note:** The keyword value `overlay` is a legacy value alias for `auto`. With `overlay`, the scroll bars are drawn on top of the content instead of taking up space.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value#examples)

------------------------------------------------------------------------------------------------------

This example demos all the `<overflow>` enumerated values for the [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 property.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value#html)

The HTML in this example contains some lyrics within the [`<pre>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre)
 element. The HTML also contains a link text to enable testing the effects of keyboard focus on overflow and scroll behaviors. The same HTML code is repeated multiple times to show the effect of each `<overflow>` enumerated value.

html

    <pre>&nbsp;
    Oh, Rubber Duckie, you're the one
    You make bath time lots of fun
    Rubber Duckie, I'm awfully fond of you
    
    Rubber Duckie, joy of joys
    When I squeeze you, you make noise
    Rubber Duckie, you're my very best friend, it's true
    
    Oh, every day when I make my way to the tubby
    I find a little fella who's cute and yellow and chubby
    Rub-a-dub-dubby
    
    <a href="#">Rubber Duckie</a>, you're so fine
    And I'm lucky that you're mine
    Rubber Duckie, I'm awfully fond of you
    </pre>
    

    <pre>&nbsp;
    Oh, Rubber Duckie, you're the one
    You make bath time lots of fun
    Rubber Duckie, I'm awfully fond of you
    
    Rubber Duckie, joy of joys
    When I squeeze you, you make noise
    Rubber Duckie, you're my very best friend, it's true
    
    Oh, every day when I make my way to the tubby
    I find a little fella who's cute and yellow and chubby
    Rub-a-dub-dubby
    
    <a href="#">Rubber Duckie</a>, you're so fine
    And I'm lucky that you're mine
    Rubber Duckie, I'm awfully fond of you
    </pre>
    
    <pre>&nbsp;
    Oh, Rubber Duckie, you're the one
    You make bath time lots of fun
    Rubber Duckie, I'm awfully fond of you
    
    Rubber Duckie, joy of joys
    When I squeeze you, you make noise
    Rubber Duckie, you're my very best friend, it's true
    
    Oh, every day when I make my way to the tubby
    I find a little fella who's cute and yellow and chubby
    Rub-a-dub-dubby
    
    <a href="#">Rubber Duckie</a>, you're so fine
    And I'm lucky that you're mine
    Rubber Duckie, I'm awfully fond of you
    </pre>
    
    <pre>&nbsp;
    Oh, Rubber Duckie, you're the one
    You make bath time lots of fun
    Rubber Duckie, I'm awfully fond of you
    
    Rubber Duckie, joy of joys
    When I squeeze you, you make noise
    Rubber Duckie, you're my very best friend, it's true
    
    Oh, every day when I make my way to the tubby
    I find a little fella who's cute and yellow and chubby
    Rub-a-dub-dubby
    
    <a href="#">Rubber Duckie</a>, you're so fine
    And I'm lucky that you're mine
    Rubber Duckie, I'm awfully fond of you
    </pre>
    
    <pre>&nbsp;
    Oh, Rubber Duckie, you're the one
    You make bath time lots of fun
    Rubber Duckie, I'm awfully fond of you
    
    Rubber Duckie, joy of joys
    When I squeeze you, you make noise
    Rubber Duckie, you're my very best friend, it's true
    
    Oh, every day when I make my way to the tubby
    I find a little fella who's cute and yellow and chubby
    Rub-a-dub-dubby
    
    <a href="#">Rubber Duckie</a>, you're so fine
    And I'm lucky that you're mine
    Rubber Duckie, I'm awfully fond of you
    </pre>
    
    <pre>&nbsp;
    Oh, Rubber Duckie, you're the one
    You make bath time lots of fun
    Rubber Duckie, I'm awfully fond of you
    
    Rubber Duckie, joy of joys
    When I squeeze you, you make noise
    Rubber Duckie, you're my very best friend, it's true
    
    Oh, every day when I make my way to the tubby
    I find a little fella who's cute and yellow and chubby
    Rub-a-dub-dubby
    
    <a href="#">Rubber Duckie</a>, you're so fine
    And I'm lucky that you're mine
    Rubber Duckie, I'm awfully fond of you
    </pre>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value#css)

For the purpose of demonstration, the size of the `<pre>` element box has been defined to ensure that the content overflows its container in both the inline and block directions. A different `<overflow>` value is set for each of the repeating `<pre>` elements. For the `clip` value demonstration, an [`overflow-clip-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-clip-margin)
 has been added.

    pre {
      border: 2px dashed red;
      margin-bottom: 3em;
    }
    
    ::before {
      font-weight: bold;
      color: white;
      background: crimson;
      display: inline-block;
      width: 100%;
      padding: 3px 5px;
      box-sizing: border-box;
    }
    

css

    pre {
      block-size: 100px;
      inline-size: 295px;
    }
    
    pre:nth-of-type(1) {
      overflow: hidden;
    }
    pre:nth-of-type(1)::before {
      content: "hidden: ";
    }
    
    pre:nth-of-type(2) {
      overflow: clip;
      overflow-clip-margin: 1em;
    }
    pre:nth-of-type(2)::before {
      content: "clip: ";
    }
    
    pre:nth-of-type(3) {
      overflow: scroll;
    }
    pre:nth-of-type(3)::before {
      content: "scroll: ";
    }
    
    pre:nth-of-type(4) {
      overflow: auto;
    }
    pre:nth-of-type(4)::before {
      content: "auto: ";
    }
    
    pre:nth-of-type(5) {
      overflow: clip;
      overflow: overlay;
      overflow-clip-margin: 3em;
    }
    pre:nth-of-type(5)::before {
      content: "overlay (or clip if not supported): ";
    }
    
    pre:nth-of-type(6) {
      overflow: visible;
    }
    pre:nth-of-type(6)::before {
      content: "visible: ";
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value#result)

To see the effect of keyboard focus on overflow and scroll behaviors, try tabbing through all the links in the example. Notice that the `clip` box does not create a scroll container, and the link does not come into view when the link is focused. The `visible` value, which has the link always in view, is also not a scroll container.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Overflow Module Level 3  <br>\# propdef-overflow](https://drafts.csswg.org/css-overflow/#propdef-overflow) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value#see_also)

------------------------------------------------------------------------------------------------------

*   Properties that use this data type: [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)
    , [`overflow-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)
    , [`overflow-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline)
    , [`overflow-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block)
     and [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
    
*   [CSS overflow module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/overflow_value/index.md?plain=1 "Folder: en-us/web/css/reference/values/overflow_value (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Foverflow_value&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Foverflow_value%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Foverflow_value%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Foverflow_value%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")