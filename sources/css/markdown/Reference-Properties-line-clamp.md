*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-clamp#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-clamp#mdn-search)
    

`line-clamp` CSS property
=========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/267)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-clamp#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`line-clamp`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property allows limiting of the contents of a [block](https://developer.mozilla.org/en-US/docs/Glossary/Block)
 to the specified number of lines. Optionally, it also allows inserting content into the last line to indicate that content was truncated.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-clamp#syntax)

--------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    line-clamp: none;
    
    /* <integer> value only */
    line-clamp: 3;
    line-clamp: 10;
    
    /* <integer> and <'block-ellipsis'> values */
    line-clamp: 3 no-ellipsis;
    line-clamp: 10 "… (there is extra content)";
    
    /* <'block-ellipsis'> value only */
    line-clamp: no-ellipsis;
    line-clamp: "… (there is extra content)";
    
    /* Global values */
    line-clamp: inherit;
    line-clamp: initial;
    line-clamp: revert;
    line-clamp: revert-layer;
    line-clamp: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-clamp#values)

This property is specified as one or two space-separated values from the following list:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-clamp#none)

Specifies that content is not clamped. This keyword cannot be combined with the other values. This is the default.

[`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 Optional

Specifies the number of lines after which content is clamped. It must be greater than 0.

[`<’block-ellipsis’>` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-clamp#%E2%80%99block-ellipsis%E2%80%99)

Specifies the content inserted into the last line. It can take one of the following values:

*   `no-ellipsis`: No ellipsis (character U+2026) is added if the text is truncated due to the number of line specified.
*   `auto`: Renders an ellipsis character (U+2026) if the text is truncated.
*   [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
    : Renders the specified string at the end of the affected line. Browsers may truncate this string if it is very long. An empty string behaves like the `no-ellipsis` value.

**Note:** If `<’block-ellipsis’>` is specified without an `<integer>`, it applies only when content is clamped by the height of the container.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-clamp#description)

------------------------------------------------------------------------------------------------------------

In most cases you will also want to set [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 to `hidden`, otherwise the contents won't be clipped but an ellipsis will still be shown after the specified number of lines.

When applied to anchor elements, the truncating can happen in the middle of the text, not necessarily at the end.

**Note:** For legacy support, the vendor-prefixed `-webkit-line-clamp` property only works in combination with the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property set to `-webkit-box` or `-webkit-inline-box` and the [`-webkit-box-orient`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient)
 property set to `vertical`. Despite these prefixed properties being deprecated, the co-dependency of these three properties is a fully specified behavior and will continue to be supported.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-clamp#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | Block containers except multi-column containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | an [integer](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer#interpolation "Values of the <integer> CSS data type are interpolated via integer discrete steps. The calculation is done as if they were real, floating-point numbers and the discrete value is obtained using the floor function.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-clamp#formal_syntax)

----------------------------------------------------------------------------------------------------------------

line-clamp =   
  none                                                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <'max-lines'> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <'block-ellipsis'> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 \-webkit-legacy[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<max-lines> =   
  auto             [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  <integer \[1,∞\]>    
  
<block-ellipsis> =   
  no-ellipsis  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ellipsis     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
       
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-clamp#examples)

------------------------------------------------------------------------------------------------------

### [Truncating content with an ellipsis or a custom string](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-clamp#truncating_content_with_an_ellipsis_or_a_custom_string)

In this example, there are three cards, each with a different `line-clamp` value:

*   The first has only an `<integer>` to restrict the number of lines.
*   The second has an `<integer>` and the `no-ellipsis` value.
*   The third has an `<integer>` and a custom `<string>`.

#### HTML

html

    <section>
      <div class="card">
        <h2>number of lines</h2>
        <p class="integer">
          In this card, the <em>number of lines</em> is specified by an
          <code>&lt;integer&gt;</code>. Any content that does not fit is truncated
          and an ellipsis is shown.
        </p>
      </div>
      <div class="card">
        <h2>no ellipsis</h2>
        <p class="no-ellipsis">
          In this card, an <code>&lt;integer&gt;</code> and a
          <em>no-ellipsis</em> value are specified. Any content that does not fit is
          truncated and no ellipsis is shown.
        </p>
      </div>
      <div class="card">
        <h2>custom string</h2>
        <p class="string">
          In this card, an <code>&lt;integer&gt;</code> and a <em>string</em> value
          are specified. Any content that does not fit is truncated and the custom
          string is shown instead of an ellipsis.
        </p>
      </div>
    </section>
    

#### CSS

    /* layout for the cards */
    section {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 0.5rem;
      justify-content: space-between;
    }
    em {
      color: tomato;
    }
    .card {
      padding: 0.2rem;
      border: 1px solid tomato;
      border-radius: 0.2rem;
      max-width: 250px;
    }
    

css

    .integer {
      line-clamp: 2;
      overflow: hidden;
    }
    .no-ellipsis {
      line-clamp: 2 no-ellipsis;
      overflow: hidden;
    }
    .string {
      line-clamp: 2 "… (my custom text)";
      overflow: hidden;
    }
    

#### Result

### [Truncating a paragraph with the legacy property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-clamp#truncating_a_paragraph_with_the_legacy_property)

This example uses the legacy `-webkit-line-clamp` property with `display` set to `-webkit-box`.

**Note:** When using the legacy `-webkit-line-clamp` property, you will also want to set [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 to `hidden`, otherwise the content is not clipped, although an ellipsis is still shown after the specified number of lines.

#### HTML

html

    <p>
      In this example the <code>-webkit-line-clamp</code> property is set to
      <code>3</code>, which means the text is clamped after three lines. An ellipsis
      will be shown at the point where the text is clamped.
    </p>
    

#### CSS

css

    p {
      width: 300px;
      display: -webkit-box;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 3;
      overflow: hidden;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-clamp#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Overflow Module Level 4  <br>\# propdef-line-clamp](https://drafts.csswg.org/css-overflow-4/#propdef-line-clamp) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-clamp#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-clamp#see_also)

------------------------------------------------------------------------------------------------------

*   [Line Clampin' (Truncating Multiple Line Text)](https://css-tricks.com/line-clampin/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-clamp/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/line-clamp/index.md?plain=1 "Folder: en-us/web/css/reference/properties/line-clamp (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fline-clamp&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fline-clamp%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fline-clamp%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fline-clamp%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0451ba52048b172d3c2c1b8b5ce21950384ecbb2%0A*+Document+last+modified%3A+2026-09-14T10%3A18%3A51.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")