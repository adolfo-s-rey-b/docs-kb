*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-inset#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-inset#mdn-search)
    

`text-decoration-inset` CSS property
====================================

The **`text-decoration-inset`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property enables adjusting the start and end points of an element's text decoration so it can be shortened, lengthened, or have its position shifted with respect to the rendered text.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-inset#try_it)

-------------------------------------------------------------------------------------------------------------

    text-decoration-inset: 20px;
    

    text-decoration-inset: -0.5em;
    

    text-decoration-inset: 20px 1em;
    

    text-decoration-inset: -0.5rem -1.5rem;
    

    text-decoration-inset: -2ex 10vw;
    

    <section id="default-example">
      <p id="example-element">Karmadrome</p>
    </section>
    

    #example-element {
      font: 2.5em sans-serif;
      text-decoration: underline 0.3em limegreen;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-inset#syntax)

-------------------------------------------------------------------------------------------------------------

css

    /* auto keyword */
    text-decoration-inset: auto;
    
    /* One <length> value */
    text-decoration-inset: 20px;
    text-decoration-inset: -2rem;
    text-decoration-inset: 5%;
    
    /* Two <length> values */
    text-decoration-inset: 20px 1em;
    text-decoration-inset: -0.5rem -1.5rem;
    text-decoration-inset: -2ex 1vw;
    text-decoration-inset: -5% -5%;
    
    /* Global values */
    text-decoration-inset: inherit;
    text-decoration-inset: initial;
    text-decoration-inset: revert;
    text-decoration-inset: revert-layer;
    text-decoration-inset: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-inset#values)

This property is specified as one or two of the following value or the keyword `auto`:

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

Specifies the amount to adjust the text decoration position by. Positive values inset the text decoration (make it shorter) while negative values outset the text decoration (make it longer). If one value is specified, it applies to both the text decoration start and end points. If two values are specified, the first one applies to the text decoration start point and the second one applies to the text decoration end point. Percentage values either refer to the total inline size of the [decorating box](https://developer.mozilla.org/en-US/docs/Glossary/decorating_box)
 if [`box-decoration-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break)
 is set to [`slice`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break#slice)
, or to the inline size of each individual [box fragment](https://developer.mozilla.org/en-US/docs/Glossary/box_fragment)
, if it is set to [`clone`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break#clone)
.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-inset#auto)

The browser chooses a start and end inset amount to ensure that, if two decorated text boxes appear side-by-side, the appearance of a gap is created between their text decorations so they do not appear to have a single text decoration.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-inset#description)

-----------------------------------------------------------------------------------------------------------------------

By default, an element's text decoration, as set by the [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
 shorthand and associated longhand properties, is the same size as the rendered text.

The `text-decoration-inset` property allows you to adjust the start and/or end points of a text container's text decoration. This is useful for creating effects where you want the text decoration to be inset or outset from the text itself, or shifted in position. See [Basic use cases](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-inset#basic_use_cases)
 for an example of each.

A single `<length-percentage>` value will set the inset (if positive) or outset (if negative) on the start and end positions of the text decoration. To set the start and end positions separately, you can use two `<length-percentage>` values — the first one applies to the start position of the text decoration and the second one applies to the end.

**Note:** A percentage value depends on the value of [`box-decoration-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break)
, if it is set to `slice` (the initial value) it refers to the inline size of the decorating box or if it is set to `clone` it refers to each individual box fragment.

The `text-decoration-inset` property can also take the `auto` keyword. This causes the browser to inset the text decoration start and end points to ensure that, if two decorated text boxes appear side-by-side, they do not appear to have a single text decoration. The `auto` value is particularly important when rendering Chinese text, where underlining is used to [punctuate proper nouns](https://www.w3.org/International/clreq/#id88 "External link (opens in new tab)")
, and adjacent proper nouns should have separate underlines. See [Effect of the `auto` value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-inset#effect_of_the_auto_value)
 for an example.

The `auto` value does not have the same effect as the initial value `0`. Setting `text-decoration-inset` to `0` causes there to be no space between decorations.

The `text-decoration-inset` property is not inherited, and it is not a constituent property of the [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
 shorthand.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-inset#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the size of the box itself |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | for percentage and length values, the absolute length, otherwise the keyword as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-inset#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

text-decoration-inset =   
  <length-percentage>[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto                        
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-inset#examples)

-----------------------------------------------------------------------------------------------------------------

### [Basic use cases](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-inset#basic_use_cases)

In this example, we demonstrate the outset, inset, and "shifted" use cases.

#### HTML

We define an unordered list with three list items, each with a separate `id`.

html

    <ul>
      <li id="one">Outset decoration</li>
      <li id="two">Inset decoration</li>
      <li id="three">Shifted decoration</li>
    </ul>
    

#### CSS

We give each list item a different [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
 and `text-decoration-inset`:

*   The first one has a thick lime green underline, which is outset equally by `10px` on both sides.
*   The second one has a medium thickness white strike-through, which is inset equally by `0.5em` on both sides.
*   The third one has a thin wavy blue underline, which is moved to the right by `1em`.

    li {
      font-family: sans-serif;
      font-size: 2em;
      margin-bottom: 20px;
    }
    
    @supports not (text-decoration-inset: auto) {
      body::before {
        content: "Your browser doesn't support the text-decoration-inset property.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

css

    #one {
      text-decoration: underline 0.3em limegreen;
      text-decoration-inset: -10px;
    }
    
    #two {
      text-decoration: line-through 5px white;
      text-decoration-inset: 0.5em;
    }
    
    #three {
      text-decoration: underline wavy 2px blue;
      text-decoration-inset: 1em -1em;
    }
    

#### Result

This renders like so:

### [Effect of the `auto` value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-inset#effect_of_the_auto_value)

This example demonstrates the effect of the `text-decoration-inset: auto` value.

#### HTML

We define two groups of side-by-side [`<u>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u)
 elements:

html

    <p lang="zh" id="one"><u>石井</u><u>艾俐俐</u></p>
    
    <p lang="zh" id="two"><u>石井</u><u>艾俐俐</u></p>
    

#### CSS

Each `<u>` element has a `red` color and `3px` thickness set on its underline. The first group of `<u>` elements has a `text-decoration-inset` value of `auto` set on them, while the second set has the initial `text-decoration-inset` value of `0` explicitly set on them, for comparison purposes:

    u {
      font-family: sans-serif;
      font-size: 2em;
    }
    
    @supports not (text-decoration-inset: auto) {
      body::before {
        content: "Your browser doesn't support the text-decoration-inset property.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

css

    u {
      text-decoration-color: red;
      text-decoration-thickness: 3px;
    }
    
    #one u {
      text-decoration-inset: auto;
    }
    
    #two u {
      text-decoration-inset: 0;
    }
    

#### Result

This renders like so:

Note how the `auto` value insets the text decoration subtly on both sides, creating a gap in between the underlines of the two elements (no space is added between the two elements themselves). The `0` value results in no gap.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-inset#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Decoration Module Level 4  <br>\# propdef-text-decoration-inset](https://drafts.csswg.org/css-text-decor-4/#propdef-text-decoration-inset) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-inset#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-inset#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
    
*   The [CSS text decoration](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 23, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-inset/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-decoration-inset/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-decoration-inset (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-decoration-inset&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-decoration-inset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-decoration-inset%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-decoration-inset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85577061e99da7082b48263fa19f9b1ef4187eda%0A*+Document+last+modified%3A+2026-10-23T05%3A11%3A29.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")