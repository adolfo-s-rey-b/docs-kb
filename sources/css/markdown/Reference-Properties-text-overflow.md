*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow#mdn-search)
    

`text-overflow` CSS property
============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-overflow`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets how hidden overflow content is signaled to users.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow#try_it)

-----------------------------------------------------------------------------------------------------

    text-overflow: clip;
    

    text-overflow: ellipsis;
    

    text-overflow: "-";
    

    text-overflow: "";
    

    <section id="default-example">
      <div id="example-element-container">
        <p id="example-element">"Is there any tea on this spaceship?" he asked.</p>
      </div>
    </section>
    

    #example-element-container {
      width: 100%;
      max-width: 18em;
    }
    
    #example-element {
      line-height: 50px;
      border: 1px solid #c5c5c5;
      overflow: hidden;
      white-space: nowrap;
      font-family: sans-serif;
      padding: 0 0.5em;
      text-align: left;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow#syntax)

-----------------------------------------------------------------------------------------------------

css

    text-overflow: clip;
    text-overflow: ellipsis ellipsis;
    text-overflow: ellipsis " [..]";
    
    /* Global values */
    text-overflow: inherit;
    text-overflow: initial;
    text-overflow: revert;
    text-overflow: revert-layer;
    text-overflow: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow#values)

This property is specified as one or two space-separated values, including:

[`clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow#clip)

The default for this property. This keyword value will truncate the text at the limit of the [content area](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction)
, therefore the truncation can happen in the middle of a character. To clip at the transition between characters you can specify `text-overflow` as an empty string, if that is supported in your target browsers: `text-overflow: '';`.

[`ellipsis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow#ellipsis)

This keyword value will display an ellipsis (`'…'`, `U+2026 HORIZONTAL ELLIPSIS`) to represent clipped text. The ellipsis is displayed inside the [content area](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction)
, decreasing the amount of text displayed. If there is not enough space to display the ellipsis, it is clipped.

[`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow#string)

The [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
 to be used to represent clipped text. The string is displayed inside the [content area](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction)
, shortening the size of the displayed text. If there is not enough space to display the string itself, it is clipped.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow#description)

---------------------------------------------------------------------------------------------------------------

The `text-overflow` property sets how hidden overflow content is signaled to users. It can be clipped, display an ellipsis (`…`), or display a custom string.

The `text-overflow` property doesn't force an overflow to occur. To make text overflow its container, you have to set other CSS properties: [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 and [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
. For example:

css

    overflow: hidden;
    white-space: nowrap;
    

The `text-overflow` property only affects content that is overflowing a block container element in its _inline_ progression direction (not text overflowing at the bottom of a box, for example).

The `text-overflow` property may be specified using one or two values. If one value is given, it specifies overflow behavior for the end of the line (the right end for left-to-right text, the left end for right-to-left text). If two values are given, the first specifies overflow behavior for the left end of the line, and the second specifies it for the right end of the line.

### [`ellipsis` behaving as `clip` for editable elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow#ellipsis_behaving_as_clip_for_editable_elements)

When `text-overflow: ellipsis` is applied to editable elements such as textual [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
, [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
, and [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
 elements, browsers generally treat it as `text-overflow: clip`, either all the time or when the element is focused. The exact behavior differs across browsers; see [Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow#browser_compatibility)
.

This behavior is to ensure that the text can be moved through and edited, even when overflowing. If the overflowing text remained covered by an ellipsis, it would not be visible or editable.

You can see the behavior in the following live example, which has this CSS applied:

css

    p[contenteditable],
    input,
    textarea {
      width: 150px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    

    <p contenteditable>
      contenteditable paragraph. The text in here is overflowing.
    </p>
    
    <hr />
    
    <input type="text" value="Text input. The text in here is overflowing." />
    
    <hr />
    
    <textarea>Textarea. The text in here is overflowing.</textarea>
    

Focus the different elements and try editing their text content.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `clip` |
| Applies to | block container elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

text-overflow =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 clip [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 ellipsis [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 fade [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <fade()> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
<fade()> =   
  fade( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow#examples)

---------------------------------------------------------------------------------------------------------

### [One-value syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow#one-value_syntax)

This example shows different values for `text-overflow` applied to a paragraph, for left-to-right and right-to-left text.

#### HTML

html

    <div class="ltr">
      <h2>Left to right text</h2>
      <pre>clip</pre>
      <p class="overflow-clip">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit.
      </p>
      <pre>ellipsis</pre>
      <p class="overflow-ellipsis">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit.
      </p>
      <pre>" [..]"</pre>
      <p class="overflow-string">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit.
      </p>
    </div>
    
    <div class="rtl">
      <h2>Right to left text</h2>
      <pre>clip</pre>
      <p class="overflow-clip">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit.
      </p>
      <pre>ellipsis</pre>
      <p class="overflow-ellipsis">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit.
      </p>
      <pre>" [..]"</pre>
      <p class="overflow-string">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit.
      </p>
    </div>
    

#### CSS

css

    p {
      width: 200px;
      border: 1px solid;
      padding: 2px 5px;
    
      /* Both of the following are required for text-overflow */
      white-space: nowrap;
      overflow: hidden;
    }
    
    .overflow-clip {
      text-overflow: clip;
    }
    
    .overflow-ellipsis {
      text-overflow: ellipsis;
    }
    
    .overflow-string {
      text-overflow: " [..]";
    }
    
    body {
      display: flex;
      justify-content: space-around;
    }
    
    .ltr > p {
      direction: ltr;
    }
    
    .rtl > p {
      direction: rtl;
    }
    

#### Result

### [Two-value syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow#two-value_syntax)

This example shows the two-value syntax for `text-overflow`, where you can define different overflow behavior for the start and end of the text. To show the effect we have to scroll the line so the start of the line is also hidden.

#### HTML

html

    <pre>clip clip</pre>
    <p class="overflow-clip-clip">
      Lorem ipsum dolor sit amet, consectetur adipisicing elit.
    </p>
    <pre>clip ellipsis</pre>
    <p class="overflow-clip-ellipsis">
      Lorem ipsum dolor sit amet, consectetur adipisicing elit.
    </p>
    <pre>ellipsis ellipsis</pre>
    <p class="overflow-ellipsis-ellipsis">
      Lorem ipsum dolor sit amet, consectetur adipisicing elit.
    </p>
    <pre>ellipsis " [..]"</pre>
    <p class="overflow-ellipsis-string">
      Lorem ipsum dolor sit amet, consectetur adipisicing elit.
    </p>
    

#### CSS

css

    p {
      width: 200px;
      border: 1px solid;
      padding: 2px 5px;
    
      /* Both of the following are required for text-overflow */
      white-space: nowrap;
      overflow: scroll;
    }
    
    .overflow-clip-clip {
      text-overflow: clip clip;
    }
    
    .overflow-clip-ellipsis {
      text-overflow: clip ellipsis;
    }
    
    .overflow-ellipsis-ellipsis {
      text-overflow: ellipsis ellipsis;
    }
    
    .overflow-ellipsis-string {
      text-overflow: ellipsis " [..]";
    }
    

#### JavaScript

js

    // Scroll each paragraph so the start is also hidden
    const paras = document.querySelectorAll("p");
    
    for (const para of paras) {
      para.scroll(100, 0);
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Overflow Module Level 3  <br>\# text-overflow](https://drafts.csswg.org/css-overflow/#text-overflow) |
| [Scalable Vector Graphics (SVG) 2  <br>\# TextOverflowProperty](https://w3c.github.io/svgwg/svg2-draft/text.html#TextOverflowProperty) |

A previous version of this interface reached the _Candidate Recommendation_ status. As some not-listed-at-risk features needed to be removed, the spec was demoted to the _Working Draft_ level, explaining why browsers implemented this property unprefixed, though not at the CR state.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow#see_also)

---------------------------------------------------------------------------------------------------------

*   Related CSS properties: [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
    , [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
    
*   CSS properties that control line breaks in words: [`overflow-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap)
    , [`word-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-overflow/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-overflow (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-overflow&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-overflow%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-overflow%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-overflow%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1a2a5b56a689b441ebf3be91b90f15746c5a5a01%0A*+Document+last+modified%3A+2026-10-12T05%3A04%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")