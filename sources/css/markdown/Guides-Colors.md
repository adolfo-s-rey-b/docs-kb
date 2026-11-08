*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors#mdn-search)
    

CSS colors
==========

The **CSS colors** module defines colors, color types, color blending, opacity, and how you can apply these colors and effects to HTML content.

While this module has only two CSS properties, [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 and [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
, over 20 CSS and SVG properties, CSS images, at-rules, and @media rules depend on these two properties.

[Colors in action](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors#colors_in_action)

----------------------------------------------------------------------------------------------------

The color syntax converter below shows the values of the currently selected color in [red-green-blue](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb)
 (RGB), [hexadecimal](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color)
 (HEX), [hue, saturation, and lightness](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl)
 (HSL), and [hue, whiteness, and blackness](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hwb)
 (HWB) CSS color formats. All the RGB, HEX, HSL, and HWB color values here, while written differently, represent the same color value.

Selecting a color via the [color picker](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color)
 and an opacity via the [slider](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range)
 updates the RGB, HEX, HSL, and HWB values. When you choose a new color or opacity value, the color of the background and the slider update via the CSS properties [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 and [`accent-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/accent-color)
, respectively.

To see the code for this color syntax converter, [view the source on GitHub](https://github.com/mdn/css-examples/blob/main/modules/colors.html "External link (opens in new tab)")
.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors#reference)

--------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors#properties)

*   [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
    
*   [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
    

### [At-rules and descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors#at-rules_and_descriptors)

The CSS colors module also introduces the [`@color-profile`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile)
 at-rule, along with its `components`, `rendering-intent` and `src` descriptors. Currently, no browsers support these features.

### [Functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors#functions)

*   Color functions:
    *   [`rgb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb)
        
    *   [`hsl()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl)
        
    *   [`hwb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hwb)
        
    *   [`lab()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/lab)
        
    *   [`lch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/lch)
        
    *   [`oklab()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklab)
        
    *   [`oklch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklch)
        
    *   [`color()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color)
        
*   [`alpha()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha)
    
*   [`color-mix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix)
    
*   [`contrast-color()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color)
    
*   [`light-dark()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark)
    

The CSS color modules also introduce the [`device-cmyk()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/device-cmyk)
 function. Currently, no browsers support this feature.

### [Data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors#data_types)

*   [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
    
*   [`<color-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors#functions)
    
*   [`<hex-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color)
    
*   [`<named-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color)
    
*   [`<alpha-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value)
    
*   [`<hue>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue)
    
*   [`<system-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/system-color)
    
*   [`<colorspace-params>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color#using_predefined_color_spaces_with_color)
    

### [Glossary terms and keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors#glossary_terms_and_keywords)

*   [Color space](https://developer.mozilla.org/en-US/docs/Glossary/Color_space)
    
*   [`currentColor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#currentcolor_keyword)
    
*   [Interpolation](https://developer.mozilla.org/en-US/docs/Glossary/Interpolation)
    
*   [RGB](https://developer.mozilla.org/en-US/docs/Glossary/RGB)
    
*   [`transparent`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color#transparent)
    

### [Interfaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors#interfaces)

The CSS color module also introduces the `CSSColorProfileRule` interface. Currently, no browsers support this feature.

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors#guides)

--------------------------------------------------------------------------------

[Applying color to HTML elements using CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color)

A guide to using CSS to apply color to a variety of types of content, including all CSS properties that accept `<color>` as a value.

[CSS color values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Color_values)

An overview of color spaces and the different `<color>` functional notations available in CSS.

[Using color wisely](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_color_wisely)

Color theory and resources, including finding the right colors to create an accessible color palette, contrast, and printing in color.

[Using relative colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors)

This article explains relative CSS color syntax, shows what the different options are, and looks at some illustrative examples.

[Understanding color and luminance](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Colors_and_Luminance)

Color perception and using colors with color insensitive (color blind) users, reduced vision users and users with vestibular disorders or other neurological disorders in mind.

[WCAG 1.4.1: Color contrast](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable/Color_contrast)

Explanation of contrast requirements between background and foreground content to ensure legibility.

[CSS value serialization](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Object_Model/CSS_value_serialization)

How [CSSOM APIs](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Object_Model)
 serialize color and other values into standardized string representations.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors#related_concepts)

----------------------------------------------------------------------------------------------------

*   CSS properties that are part of other specifications:
    *   [`accent-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/accent-color)
        
    *   [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
        
    *   [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
        
    *   [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
        
    *   [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
        
    *   [`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)
        
    *   [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
        
    *   [`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme)
        
    *   [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
        
    *   [`dynamic-range-limit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit)
        
    *   [`outline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)
        
    *   [`scrollbar-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color)
        
    *   [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
        
    *   [`text-emphasis-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-color)
        
    *   [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
        
    *   [`-webkit-tap-highlight-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-tap-highlight-color)
        
*   [`dynamic-range-limit-mix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix)
     function
*   SVG color properties that are part of other specifications:
    *   [`fill`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill)
        
    *   [`flood-color`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/flood-color)
        
    *   [`lighting-color`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/lighting-color)
        
    *   [`stop-color`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stop-color)
        
    *   [`stroke`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke)
        
*   SVG [`color`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/color)
     attribute
*   [Color wheel](https://developer.mozilla.org/en-US/docs/Glossary/Color_wheel)
     glossary term
*   [Interpolation](https://developer.mozilla.org/en-US/docs/Glossary/Interpolation)
     glossary term
*   The [`@font-palette-values`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values)
     at-rule [`override-colors`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors)
     descriptor
*   The [`@color-profile`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile)
     at-rule
*   The [`color-gamut`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/color-gamut)
     @media feature
*   The [`forced-colors`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors)
     @media feature

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors#specifications)

------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Color Module Level 4](https://drafts.csswg.org/css-color/) |
| [CSS Color Module Level 5](https://drafts.csswg.org/css-color-5/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors#see_also)

------------------------------------------------------------------------------------

*   [CSS color adjustment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Color_adjustment)
     module and [`print-color-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust)
    
*   [`<gradient>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
     defined in [CSS images](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images)
     module
*   The [`VideoColorSpace`](https://developer.mozilla.org/en-US/docs/Web/API/VideoColorSpace)
     interface
*   [`<feColorMatrix>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feColorMatrix)
     SVG element
*   [Canvas API: applying styles and colors](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Applying_styles_and_colors#colors)
    
*   Tools:
    *   [Color format converter](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Color_format_converter)
        
    *   [Color mixer](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Color_mixer)
        

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 1, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/colors/index.md?plain=1 "Folder: en-us/web/css/guides/colors (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FColors&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fcolors%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FColors%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fcolors%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1055ee79c55c33ef82e2efc27ed248a561365724%0A*+Document+last+modified%3A+2026-07-01T16%3A45%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")