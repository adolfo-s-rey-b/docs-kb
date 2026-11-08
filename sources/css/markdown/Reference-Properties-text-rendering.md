*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-rendering#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-rendering#mdn-search)
    

`text-rendering` CSS property
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-rendering#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-rendering`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property provides information to the rendering engine about what to optimize for when rendering text.

The browser makes trade-offs among speed, legibility, and geometric precision.

**Note:** The `text-rendering` property is an SVG property that is not defined in any CSS standard. However, Gecko and WebKit browsers let you apply this property to HTML and XML content on Windows, macOS, and Linux.

One very visible effect is `optimizeLegibility`, which enables ligatures (ff, fi, fl, etc.) in text smaller than 20px for some fonts (for example, Microsoft's _Calibri_, _Candara_, _Constantia_, and _Corbel_, or the _DejaVu_ font family).

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-rendering#syntax)

------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    text-rendering: auto;
    text-rendering: optimizeSpeed;
    text-rendering: optimizeLegibility;
    text-rendering: geometricPrecision;
    
    /* Global values */
    text-rendering: inherit;
    text-rendering: initial;
    text-rendering: revert;
    text-rendering: revert-layer;
    text-rendering: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-rendering#values)

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-rendering#auto)

The browser makes educated guesses about when to optimize for speed, legibility, and geometric precision while drawing text. For differences in how this value is interpreted by the browser, see the compatibility table.

The `auto` value is a good default for balancing quality and performance, especially for extended bodies of plain text.

[`optimizeSpeed`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-rendering#optimizespeed)

The browser emphasizes rendering speed over legibility and geometric precision when drawing text. It disables kerning and ligatures.

The `optimizeSpeed` value is preferable in resource-constrained rendering scenarios, such as slow processors or low battery.

[`optimizeLegibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-rendering#optimizelegibility)

The browser emphasizes legibility over rendering speed and geometric precision. This enables kerning and optional ligatures.

The `optimizeLegibility` value is preferable for texts that are large in size but short in content, such as headers or banners, to enhance their readability. It could also be used for high-quality professional typography such as published articles. It's not recommended for typical articles due to potential performance impacts.

[`geometricPrecision`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-rendering#geometricprecision)

The browser emphasizes geometric precision over rendering speed and legibility. Certain aspects of fonts — such as kerning — don't scale linearly. So this value can make text using those fonts look good.

In SVG, when text is scaled up or down, browsers calculate the final size of the text (which is determined by the specified font size and the applied scale) and request a font of that computed size from the platform's font system. But if you request a font size of, say, 9 with a scale of 140%, the resulting font size of 12.6 doesn't explicitly exist in the font system, so the browser rounds the font size to 12 instead. This results in stair-step scaling of text.

But the `geometricPrecision` property — when fully supported by the rendering engine — lets you scale your text fluidly. For large scale factors, you might see less-than-beautiful text rendering, but the size is what you would expect—neither rounded up nor down to the nearest font size supported by Windows or Linux.

The `geometricPrecision` value optimizes neither readability nor performance. It usually makes sense in SVG, where you want your graphic to scale faithfully without distorting the text dimensions.

**Note:** WebKit precisely applies the specified value, but Gecko treats the value the same as `optimizeLegibility`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-rendering#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | text elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-rendering#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

text-rendering =   
  auto                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  optimizeSpeed       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  optimizeLegibility  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  geometricPrecision    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-rendering#examples)

----------------------------------------------------------------------------------------------------------

### [Automatic application of optimizeLegibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-rendering#automatic_application_of_optimizelegibility)

This demonstrates how `optimizeLegibility` is used by browsers automatically when the `font-size` is smaller than `20px`.

#### HTML

html

    <p class="small">LYoWAT - ff fi fl ffl</p>
    <p class="big">LYoWAT - ff fi fl ffl</p>
    

#### CSS

css

    .small {
      font:
        19.9px "Constantia",
        "Times New Roman",
        "Georgia",
        "Palatino",
        serif;
    }
    .big {
      font:
        20px "Constantia",
        "Times New Roman",
        "Georgia",
        "Palatino",
        serif;
    }
    

#### Result

### [optimizeSpeed vs. optimizeLegibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-rendering#optimizespeed_vs._optimizelegibility)

This example shows the difference between the appearance of `optimizeSpeed` and `optimizeLegibility` (in your browser; other browsers may vary).

#### HTML

html

    <p class="speed">LYoWAT - ff fi fl ffl</p>
    <p class="legibility">LYoWAT - ff fi fl ffl</p>
    

#### CSS

css

    p {
      font:
        1.5em "Constantia",
        "Times New Roman",
        "Georgia",
        "Palatino",
        serif;
    }
    
    .speed {
      text-rendering: optimizeSpeed;
    }
    .legibility {
      text-rendering: optimizeLegibility;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-rendering#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scalable Vector Graphics (SVG) 2  <br>\# TextRenderingProperty](https://w3c.github.io/svgwg/svg2-draft/painting.html#TextRenderingProperty) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-rendering#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-rendering#see_also)

----------------------------------------------------------------------------------------------------------

*   [Drawing text in a `<canvas>`](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Drawing_text)
    
*   [CSS Text Decoration](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text_decoration)
     CSS module
    
*   Related CSS properties
    
    *   [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
         (and its longhand properties, such as [`text-decoration-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line)
        , [`text-decoration-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-style)
        , and [`text-decoration-thickness`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness)
        )
    *   [`text-emphasis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis)
         (and its longhand properties, including [`text-emphasis-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-color)
        , [`text-emphasis-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position)
        , and [`text-emphasis-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style)
        )
    *   [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
        
    *   [`text-transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform)
        
*   The [SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
     [`text-rendering`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/text-rendering)
     attribute
    
*   [SVG and CSS](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch/SVG_and_CSS)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-rendering/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-rendering/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-rendering (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-rendering&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-rendering%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-rendering%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-rendering%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")