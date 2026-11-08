*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style#mdn-search)
    

`text-wrap-style` CSS property
==============================

Baseline 2024

Newly available

\*

Since October 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-wrap-style`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property controls how text inside an element is wrapped, providing alternate ways of determining where to create line breaks in order to fit the content within a block element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style#try_it)

-------------------------------------------------------------------------------------------------------

    text-wrap-style: auto;
    

    text-wrap-style: balance;
    

    text-wrap-style: pretty;
    

    text-wrap-style: stable;
    

    <section class="default-example" id="default-example">
      <div class="whole-content-wrapper">
        <p>Edit the text in the box:</p>
        <div class="transition-all" id="example-element">
          <p contenteditable>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatem aut
            cum eum id quos est.
          </p>
        </div>
      </div>
    </section>
    

    .whole-content-wrapper {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
    }
    
    #example-element {
      border: 1px solid #c5c5c5;
      width: 250px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    text-wrap-style: auto;
    text-wrap-style: balance;
    text-wrap-style: pretty;
    text-wrap-style: stable;
    
    /* Global values */
    text-wrap-style: inherit;
    text-wrap-style: initial;
    text-wrap-style: revert;
    text-wrap-style: revert-layer;
    text-wrap-style: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style#values)

The `text-wrap-style` property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style#auto)

Text is wrapped in the most performant way for the browser and does not take into account the number of characters.

[`balance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style#balance)

Text is wrapped in a way that best balances the number of characters on each line, enhancing layout quality and legibility. Because counting characters and balancing them across multiple lines is computationally expensive, this value is only supported for blocks of text spanning a limited number of lines (six or less for Chromium and ten or less for Firefox).

[`pretty`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style#pretty)

Text is wrapped using a slower algorithm that favors better layout over speed. This is intended for body copy where good typography is favored over performance (for example, when the number of [orphans](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/orphans)
 should be kept to a minimum).

[`stable`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style#stable)

Text is wrapped such that when the user is editing the content, the lines that come before the lines they are editing remain static rather than the whole block of text re-wrapping.

The specification also defines an `avoid-orphans` value in which browsers consider more than one line when making break decisions to avoid excessively short last lines. This value is not yet supported in any browser.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style#description)

-----------------------------------------------------------------------------------------------------------------

The `text-wrap-style` property can be used to provide a hint as to how the user agent should insert soft line breaks when the content is allowed to wrap. Each value defines a different approach to wrapping lines, balancing speed, quality, layout style, and stability, providing alternative ways to wrap the content of a block element.

When the content is allowed to wrap — the usual behavior because the default value of the [`text-wrap-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode)
 property is `wrap` — the single keyword value of the `text-wrap-style` property specifies _how_ the developer would like the text to be wrapped. The values have no effect on where a soft wrap opportunity exists, just how the browser should selects among them. If `text-wrap-mode` is set to `nowrap`, this property has no effect.

### [Selecting a value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style#selecting_a_value)

The value you choose, for `text-wrap-style`, depends on how many lines of text you anticipate styling, whether the text is `contenteditable`, and whether you need to prioritize appearance or performance.

When the styled content will be limited to a short number of lines, such as headings, captions, and blockquotes, `text-wrap-style: balance` can be added to balance the number of characters on each line, enhancing layout quality and legibility. As browsers limit the number of lines impacted by this property, this value's impact on performance is negligible.

For longer sections of text, `text-wrap-style: pretty` can be used. Note that `pretty` has a negative effect on performance, so it should be only used for longer blocks of text when the layout is more important than speed.

The `stable` value improves user experience when used on content that is [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
. This value ensures that, as the user is editing text, the previous lines in the area being edited remain stable.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | text and block containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

text-wrap-style =   
  auto                   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  balance                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  stable                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  pretty                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  avoid-short-last-line    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style#examples)

-----------------------------------------------------------------------------------------------------------

### [Balanced text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style#balanced_text)

This example has two paragraphs, the first is the default `auto` and the second is `balance`.

#### HTML

html

    <h2>Unbalanced</h2>
    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit, ad. Impedit
      adipisci rerum modi praesentium atque aperiam vitae nesciunt consectetur
      assumenda deleniti repudiandae perferendis sed odio doloremque, aliquid natus
      laboriosam?
    </p>
    <h2>Balanced</h2>
    <p class="balanced">
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit, ad. Impedit
      adipisci rerum modi praesentium atque aperiam vitae nesciunt consectetur
      assumenda deleniti repudiandae perferendis sed odio doloremque, aliquid natus
      laboriosam?
    </p>
    

#### CSS

css

    p {
      max-width: 60ch;
    }
    .balanced {
      text-wrap-style: balance;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 4  <br>\# text-wrap-style](https://drafts.csswg.org/css-text-4/#text-wrap-style) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`text-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap)
    
*   [`text-wrap-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode)
    
*   [`hyphens`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens)
    
*   [`hyphenate-limit-chars`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-limit-chars)
    
*   [CSS text](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jun 8, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-wrap-style/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-wrap-style (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-wrap-style&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-wrap-style%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-wrap-style%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-wrap-style%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7d82de65fb43700d2053f13d8344ec4a78759b2c%0A*+Document+last+modified%3A+2026-06-08T08%3A24%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")