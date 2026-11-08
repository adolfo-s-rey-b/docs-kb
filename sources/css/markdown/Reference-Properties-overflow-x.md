*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x#mdn-search)
    

`overflow-x` CSS property
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`overflow-x`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets what shows when content overflows a block-level element's left and right edges. This may be nothing, a scroll bar, or the overflow content. This property may also be set by using the [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 shorthand property.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x#try_it)

--------------------------------------------------------------------------------------------------

    overflow-x: visible;
    

    overflow-x: hidden;
    

    overflow-x: clip;
    

    overflow-x: scroll;
    

    overflow-x: auto;
    

    <section class="default-example" id="default-example">
      <div id="example-element">
        The value of Pi is 3.1415926535897932384626433832795029. The value of e is
        2.7182818284590452353602874713526625.
      </div>
    </section>
    

    #example-element {
      width: 15em;
      height: 9em;
      border: medium dotted;
      padding: 0.75em;
      text-align: left;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x#syntax)

--------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    overflow-x: visible;
    overflow-x: hidden;
    overflow-x: clip;
    overflow-x: scroll;
    overflow-x: auto;
    
    /* Global values */
    overflow-x: inherit;
    overflow-x: initial;
    overflow-x: revert;
    overflow-x: revert-layer;
    overflow-x: unset;
    

The `overflow-x` property is specified as a single [`<overflow>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value)
 keyword value.

If [`overflow-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)
 is `hidden`, `scroll`, or `auto`, and the `overflow-x` property is `visible` (default), the value will be implicitly computed as `auto`.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x#values)

[`visible`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x#visible)

Overflow content is not clipped and may be visible outside the element's padding box on left and right edges. The element box is not a [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
.

[`hidden`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x#hidden)

Overflow content is clipped if necessary to fit horizontally in the elements' padding box. No scroll bars are provided.

[`clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x#clip)

Overflow content is clipped at the element's _overflow clip edge_ that is defined using the [`overflow-clip-margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-clip-margin)
 property. As a result, content overflows the element's padding box by the [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value of `overflow-clip-margin` or by `0px` if not set. The difference between `clip` and `hidden` is that the `clip` keyword also forbids all scrolling, including programmatic scrolling. No new formatting context is created. To establish a formatting context, use `overflow: clip` along with [`display: flow-root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display#flow-root)
. The element box is not a scroll container.

[`scroll`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x#scroll)

Overflow content is clipped if necessary to fit horizontally inside the element's padding box. Browsers display scroll bars in the horizontal direction whether or not any content is actually clipped. (This prevents scroll bars from appearing or disappearing when the content changes.) Printers may still print overflowing content.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x#auto)

Overflow content is clipped at the element's padding box, and overflow content can be scrolled into view. Unlike `scroll`, user agents display scroll bars _only if_ the content is overflowing and hide scroll bars by default. If content fits inside the element's padding box, it looks the same as with `visible`, but still establishes a new block-formatting context. Desktop browsers provide scroll bars if content overflows.

**Note:** The keyword value `overlay` is a legacy value alias for `auto`. With `overlay`, the scroll bars are drawn on top of the content instead of taking up space.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `visible` |
| Applies to | Block-containers, flex containers, and grid containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, except with `visible`/`clip` computing to `auto`/`hidden` respectively if one of [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)<br> or [`overflow-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)<br> is neither `visible` nor clip |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x#formal_syntax)

----------------------------------------------------------------------------------------------------------------

overflow-x =   
  visible  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hidden   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  clip     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  scroll   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto       

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x#examples)

------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x#html)

html

    <ul>
      <li>
        <code>overflow-x:hidden</code> — hides the text outside the box
        <div id="div1">ABCDEFGHIJKLMOPQRSTUVWXYZABCDEFGHIJKLMOPQRSTUVWXYZ</div>
      </li>
    
      <li>
        <code>overflow-x:scroll</code> — always adds a scrollbar
        <div id="div2">ABCDEFGHIJKLMOPQRSTUVWXYZABCDEFGHIJKLMOPQRSTUVWXYZ</div>
      </li>
    
      <li>
        <code>overflow-x:visible</code> — displays the text outside the box if
        needed
        <div id="div3">ABCDEFGHIJKLMOPQRSTUVWXYZABCDEFGHIJKLMOPQRSTUVWXYZ</div>
      </li>
    
      <li>
        <code>overflow-x:auto</code> — on most browsers, equivalent to
        <code>scroll</code>
        <div id="div4">ABCDEFGHIJKLMOPQRSTUVWXYZABCDEFGHIJKLMOPQRSTUVWXYZ</div>
      </li>
    </ul>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x#css)

css

    #div1,
    #div2,
    #div3,
    #div4 {
      border: 1px solid black;
      width: 250px;
      margin-bottom: 12px;
    }
    
    #div1 {
      overflow-x: hidden;
    }
    #div2 {
      overflow-x: scroll;
    }
    #div3 {
      overflow-x: visible;
    }
    #div4 {
      overflow-x: auto;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Overflow Module Level 3  <br>\# overflow-properties](https://drafts.csswg.org/css-overflow/#overflow-properties) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x#see_also)

------------------------------------------------------------------------------------------------------

*   [`clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip)
    , [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    , [`text-overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow)
    , [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
    
*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
*   [Learn: Overflowing content](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Overflow)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/overflow-x/index.md?plain=1 "Folder: en-us/web/css/reference/properties/overflow-x (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foverflow-x&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foverflow-x%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foverflow-x%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foverflow-x%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")