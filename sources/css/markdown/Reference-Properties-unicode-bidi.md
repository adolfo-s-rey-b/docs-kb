*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi#mdn-search)
    

`unicode-bidi` CSS property
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`unicode-bidi`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property, together with the [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 property, determines how bidirectional text in a document is handled. For example, if a block of content contains both left-to-right and right-to-left text, the user-agent uses a complex Unicode algorithm to decide how to display the text. The `unicode-bidi` property overrides this algorithm and allows the developer to control the text embedding.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi#try_it)

----------------------------------------------------------------------------------------------------

    unicode-bidi: normal;
    

    unicode-bidi: bidi-override;
    

    unicode-bidi: plaintext;
    

    unicode-bidi: isolate-override;
    

    <section class="default-example" id="default-example">
      <p class="transition-all" id="example-element">
        בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ.
      </p>
    </section>
    

The `unicode-bidi` and [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 properties are the only properties that are not affected by the [`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all)
 shorthand.

**Warning:** This property is intended for Document Type Definition (DTD) designers. Web designers and similar authors **should not** override it.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi#syntax)

----------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    unicode-bidi: normal;
    unicode-bidi: embed;
    unicode-bidi: isolate;
    unicode-bidi: bidi-override;
    unicode-bidi: isolate-override;
    unicode-bidi: plaintext;
    
    /* Global values */
    unicode-bidi: inherit;
    unicode-bidi: initial;
    unicode-bidi: revert;
    unicode-bidi: revert-layer;
    unicode-bidi: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi#values)

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi#normal)

The element does not offer an additional level of embedding with respect to the bidirectional algorithm. For inline elements, implicit reordering works across element boundaries.

[`embed`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi#embed)

If the element is inline, this value opens an additional level of embedding with respect to the bidirectional algorithm. The direction of this embedding level is given by the [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 property.

[`bidi-override`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi#bidi-override)

For inline elements this creates an override. For block container elements this creates an override for inline-level descendants not within another block container element. This means that inside the element, reordering is strictly in sequence according to the [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 property; the implicit part of the bidirectional algorithm is ignored.

[`isolate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi#isolate)

This keyword indicates that the element's container directionality should be calculated without considering the content of this element. The element is therefore _isolated_ from its siblings. When applying its bidirectional-resolution algorithm, its container element treats it as one or several `U+FFFC Object Replacement Character`, i.e., like an image.

[`isolate-override`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi#isolate-override)

This keyword applies the isolation behavior of the `isolate` keyword to the surrounding content and the override behavior of the `bidi-override` keyword to the inner content.

[`plaintext`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi#plaintext)

This keyword makes the elements directionality calculated without considering its parent bidirectional state or the value of the [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 property. The directionality is calculated using the P2 and P3 rules of the Unicode Bidirectional Algorithm. This value allows the display of data that is already formatted using a tool following the Unicode Bidirectional Algorithm.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements, though some values have no effect on non-inline elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi#formal_syntax)

------------------------------------------------------------------------------------------------------------------

unicode-bidi =   
  normal            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  embed             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  isolate           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  bidi-override     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  isolate-override  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  plaintext           

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi#examples)

--------------------------------------------------------------------------------------------------------

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi#css)

css

    .bible-quote {
      direction: rtl;
      unicode-bidi: embed;
    }
    

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi#html)

html

    <div class="bible-quote">A line of text</div>
    <div>Another line of text</div>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Writing Modes Level 4  <br>\# unicode-bidi](https://drafts.csswg.org/css-writing-modes/#unicode-bidi) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi#see_also)

--------------------------------------------------------------------------------------------------------

*   [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
    
*   SVG [`unicode-bidi`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/unicode-bidi)
     attribute
*   [Handling different text directions](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Handling_different_text_directions)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/unicode-bidi/index.md?plain=1 "Folder: en-us/web/css/reference/properties/unicode-bidi (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Funicode-bidi&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Funicode-bidi%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Funicode-bidi%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Funicode-bidi%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")