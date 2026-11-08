*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position#mdn-search)
    

`text-underline-position` CSS property
======================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2020.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-underline-position`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the position of the underline which is set using the [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
 property's `underline` value.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position#try_it)

---------------------------------------------------------------------------------------------------------------

    text-underline-position: auto;
    

    text-underline-position: under;
    

    <section id="default-example">
      <p>
        <span class="transition-all" id="example-element"
          >C<sub>8</sub>H<sub>10</sub>N<sub>4</sub>O<sub>2</sub></span
        >
        is the chemical formula for caffeine.
      </p>
    </section>
    

    p {
      font: 1.5em sans-serif;
    }
    
    #example-element {
      text-decoration-line: underline;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position#syntax)

---------------------------------------------------------------------------------------------------------------

css

    /* Single keyword */
    text-underline-position: auto;
    text-underline-position: under;
    text-underline-position: left;
    text-underline-position: right;
    
    /* Multiple keywords */
    text-underline-position: under left;
    text-underline-position: right under;
    
    /* Global values */
    text-underline-position: inherit;
    text-underline-position: initial;
    text-underline-position: revert;
    text-underline-position: revert-layer;
    text-underline-position: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position#auto)

The [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 uses its own algorithm to place the line at or under the [alphabetic baseline](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Typography)
.

[`from-font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position#from-font)

If the font file includes information about a preferred position, use that value. If the font file doesn't include this information, behave as if `auto` was set, with the browser choosing an appropriate position.

[`under`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position#under)

Forces the line to be set below the alphabetic baseline, at a position where it won't cross any descenders. This is useful for ensuring legibility with chemical and mathematical formulas, which make a large use of subscripts.

[`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position#left)

In vertical writing-modes, this keyword forces the line to be placed on the _left_ side of the text. In horizontal writing-modes, it is a synonym of `auto`.

[`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position#right)

In vertical writing-modes, this keyword forces the line to be placed on the _right_ side of the text. In horizontal writing-modes, it is a synonym of `auto`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------------

text-underline-position =   
  auto                                       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 from-font [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 under [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position#examples)

-------------------------------------------------------------------------------------------------------------------

### [A basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position#a_basic_example)

We create two example paragraphs:

html

    <p class="horizontal">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam consectetur ac
      turpis vel laoreet. Nullam volutpat pharetra lorem, sit amet feugiat tortor
      volutpat quis. Nam eget sodales quam. Aliquam accumsan tellus ac erat posuere.
    </p>
    
    <p class="vertical">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam consectetur ac
      turpis vel laoreet. Nullam volutpat pharetra lorem, sit amet feugiat tortor
      volutpat quis. Nam eget sodales quam. Aliquam accumsan tellus ac erat posuere.
    </p>
    

Our CSS looks like this:

css

    p {
      font-size: 1.5rem;
      text-transform: capitalize;
      text-decoration: underline;
      text-decoration-thickness: 2px;
    }
    
    .horizontal {
      text-underline-position: under;
    }
    
    .vertical {
      writing-mode: vertical-rl;
      text-underline-position: left;
    }
    

In this example we set both the paragraphs to have a thick underline. In the horizontal text we use `text-underline-position: under;` to put the underline below all the descenders.

In the text with a vertical [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 set, we can then use values of `left` or `right` to make the underline appear on the left or right of the text as required.

The live example looks like this:

### [Setting text-underline-position globally](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position#setting_text-underline-position_globally)

Because the `text-underline-position` property inherits and is not reset by the [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
 shorthand property, it may be appropriate to set its value at a global level. For example, the `under` value may be appropriate for a document with lots of chemical and mathematical formulas, which make a large use of subscripts.

css

    :root {
      text-underline-position: under;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position#specifications)

-------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Decoration Module Level 3  <br>\# text-underline-position-property](https://drafts.csswg.org/css-text-decor/#text-underline-position-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position#see_also)

-------------------------------------------------------------------------------------------------------------------

*   The [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
     property is a shorthand for setting most text-decoration properties, including [`text-decoration-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line)
    , [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
    , and [`text-decoration-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-style)
    . However, it does not set `text-underline-position`.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-underline-position/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-underline-position (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-underline-position&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-underline-position%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-underline-position%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-underline-position%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")