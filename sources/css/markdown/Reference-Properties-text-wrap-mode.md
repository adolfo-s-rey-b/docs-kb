*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode#mdn-search)
    

`text-wrap-mode` CSS property
=============================

Baseline 2024

Newly available

Since October 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-wrap-mode`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property controls whether the text inside an element is wrapped.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode#try_it)

------------------------------------------------------------------------------------------------------

    text-wrap-mode: wrap;
    

    text-wrap-mode: nowrap;
    

    <section class="default-example" id="default-example">
      <div class="whole-content-wrapper">
        <p>Edit the text in the box:</p>
        <div class="transition-all" id="example-element">
          <p contenteditable>
            You can edit this lorem ipsum dolor sit amet consectetur adipisicing
            elit. Voluptatem aut cum eum id quos est text.
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
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode#syntax)

------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    text-wrap-mode: wrap;
    text-wrap-mode: nowrap;
    
    /* Global values */
    text-wrap-mode: inherit;
    text-wrap-mode: initial;
    text-wrap-mode: revert;
    text-wrap-mode: revert-layer;
    text-wrap-mode: unset;
    

[Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode#values)

------------------------------------------------------------------------------------------------------

The `text-wrap-mode` property is specified as one of the following keyword values:

[`wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode#wrap)

Text is wrapped across lines at appropriate characters (for example spaces, in languages like English that use space separators) to minimize overflow. This is the default value.

[`nowrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode#nowrap)

Text does not wrap across lines. It will overflow its containing element rather than breaking onto a new line.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode#description)

----------------------------------------------------------------------------------------------------------------

The `text-wrap-mode` property can be used to control text wrapping inside an element. The different values provide alternate ways of wrapping the content of a block element, specifying whether lines may wrap at unforced soft wrap opportunities (`wrap`), or not (`nowrap`).

When set to `nowrap`, text will overflow rather than break onto multiple lines. As the [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 property defaults to `visible`, when content is larger than the container's inline-size, it will overflow in the inline direction. To enable scrolling in the inline direction, instead of overflow, set the [`overflow-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline)
 property to `auto` or `scroll`. To ensure the container at least as wide as the longest word, set the [`min-inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-inline-size)
 to [`min-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content)
.

When set to `wrap`, content flows onto new lines as necessary, wrapping at word break opportunities, such as [`<wbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr)
 and hyphens, and other language-specific soft-wrap opportunities. The property does not prevent non-breakable pieces of content from overflowing in the inline direction if larger than the container's inline-size.

The `text-wrap-mode` is part of two shorthand properties. The `text-wrap-mode`, along with the [`white-space-collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse)
 property, can be declared using the [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
 shorthand. It can also be set and reset, along with the [`text-wrap-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style)
 property, using the [`text-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap)
 shorthand.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `wrap` |
| Applies to | text and block containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

text-wrap-mode =   
  wrap    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  nowrap    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode#examples)

----------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode#basic_usage)

In this example, we compare the effect of the `text-wrap-mode` property's two values.

#### HTML

We include two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements that are the same except for their class names.

html

    <div class="wrap">CSS IS AWESOME</div>
    <div class="nowrap">CSS IS AWESOME</div>
    

#### CSS

We apply the same styles to both containers, limiting their width.

css

    div {
      font-family: "Arial", sans-serif;
      font-weight: bold;
      font-size: 4rem;
      box-sizing: border-box;
      border: 0.25rem solid black;
      padding: 0 4px;
      width: 14rem;
      margin: 1rem;
    }
    

We give the examples different `text-wrap-mode` values:

css

    .wrap {
      text-wrap-mode: wrap;
    }
    .nowrap {
      text-wrap-mode: nowrap;
    }
    

#### Result

In the `wrap` example, the content flows over to the next line so that it fits in the box. "Awesome" is wider than the containing box, and contains no soft break opportunities, so it overflows.

In the `nowrap` example, the content does **not** flow to the next line as the content has been specifically set to not wrap, so it is all on one line, overflowing the container.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 4  <br>\# text-wrap-mode](https://drafts.csswg.org/css-text-4/#text-wrap-mode) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode#see_also)

----------------------------------------------------------------------------------------------------------

*   [`text-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap)
    
*   [`text-wrap-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style)
    
*   [`hyphens`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens)
    
*   [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
    
*   [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
    
*   [CSS text](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text)
     module
*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jun 8, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-wrap-mode/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-wrap-mode (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-wrap-mode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-wrap-mode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-wrap-mode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-wrap-mode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F7d82de65fb43700d2053f13d8344ec4a78759b2c%0A*+Document+last+modified%3A+2026-06-08T08%3A24%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")