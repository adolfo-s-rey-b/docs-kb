*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit#mdn-search)
    

`dynamic-range-limit` CSS property
==================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/553)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`dynamic-range-limit`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the maximum luminance allowed for High Dynamic Range (HDR) content.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit#syntax)

-----------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    dynamic-range-limit: standard;
    dynamic-range-limit: no-limit;
    dynamic-range-limit: constrained;
    
    /* dynamic-range-limit-mix() function */
    dynamic-range-limit: dynamic-range-limit-mix(standard 70%, no-limit 30%);
    
    /* Global values */
    dynamic-range-limit: inherit;
    dynamic-range-limit: initial;
    dynamic-range-limit: revert;
    dynamic-range-limit: revert-layer;
    dynamic-range-limit: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit#values)

This property is specified as a single value from the following list:

[`standard`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit#standard)

Specifies the maximum luminance as High Dynamic Range (HDR) reference white, which is the CSS color `white`.

[`no-limit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit#no-limit)

Specifies the maximum luminance as much greater than that of HDR reference white. The precise level is not specified. This is the initial value.

[`constrained`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit#constrained)

Specifies the maximum luminance as somewhat greater than that of HDR reference white, such that a mix of Standard Dynamic Range (SDR) and HDR content can be comfortably viewed together. The precise level is not specified.

[`dynamic-range-limit-mix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix)

Specifies the maximum luminance as a custom value that is a combination of the different keyword values proportionate to the provided percentages. It takes two or more pairs, each consisting of a `dynamic-range-limit` keyword or a nested `dynamic-range-limit-mix()` function and a percentage.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit#description)

---------------------------------------------------------------------------------------------------------------------

The `dynamic-range-limit` property specifies the maximum luminance allowed in displays capable of displaying high dynamic range colors. A **dynamic range** is the difference in luminance (brightness) between the lightest and darkest parts of content. Dynamic range is measured in photographic stops, where an increase of one stop represents a doubling of the luminance.

### [SDR, HDR, and headroom](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit#sdr_hdr_and_headroom)

Traditional web content uses **Standard Dynamic Range (SDR)**, where the brightest color is equivalent to the CSS color `white` (`#ffffff` in hexadecimal). The brightness in **High Dynamic Range (HDR)** content, on the other hand, can go beyond the standard white. In HDR terminology, the standard CSS `white` is also called the HDR reference white.

The peak luminance at which content can be displayed depends on the content, the available display hardware, and user preferences. The amount by which the peak luminance of white can exceed HDR reference white is termed **HDR headroom** and is typically expressed in photographic stops.

SDR content always has an HDR headroom of `0` because its brightest white _is_ the HDR reference white. Older monitors may also have an HDR headroom of `0` because they are not able to display brighter colors. Newer monitors may have an HDR headroom greater than `0`, allowing them to display the brighter colors available in HDR content.

### [The use-case for `dynamic-range-limit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit#the_use-case_for_dynamic-range-limit)

The brightness of HDR content can be jarring to the viewer. This is especially apparent in apps where a mixture of HDR and SDR content is displayed, leading to inconsistency in the brightness.

The `dynamic-range-limit` property allows you to control the brightness of HDR content. For example, you might want to constrain the maximum brightness of all thumbnails in a photo or video gallery to HDR reference white (this is what the `standard` keyword value does) or to a brightness only slightly more than the HDR reference white (using the `constrained` keyword value or a custom limit created using [`dynamic-range-limit-mix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix)
). When a user views a single HDR image, or if the user selects a preference to enable it, you could then set the image's `dynamic-range-limit` to `no-limit`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `no-limit` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | See [Computed value for dynamic-range-limit](https://drafts.csswg.org/css-color-hdr/#computing-dynamic-range-limit "External link (opens in new tab)") |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | By [`dynamic-range-limit-mix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix) |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

dynamic-range-limit =   
  standard                     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  no-limit                     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  constrained                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <dynamic-range-limit-mix()>    
  
[<dynamic-range-limit-mix()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix)
 =   
  dynamic-range-limit-mix( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<'dynamic-range-limit'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit)\
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")\
 [<percentage \[0,100\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
<dynamic-range-limit> =   
  standard                     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  no-limit                     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  constrained                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <dynamic-range-limit-mix()>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit#examples)

---------------------------------------------------------------------------------------------------------------

### [Basic `dynamic-range-limit` usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit#basic_dynamic-range-limit_usage)

This example demonstrates the basic use of the `dynamic-range-limit` property and the difference between HDR and SDR images.

#### HTML

In the markup, we embed an HDR image using an [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 element. We include a [`tabindex`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex)
 value of `0` to make the image focusable via the keyboard.

html

    <img
      src="https://mdn.github.io/shared-assets/images/examples/ultra-hdr.jpg"
      alt="A subway station platform with bright white overhead strip lights"
      tabindex="0" />
    

#### CSS

We constrain the image to SDR brightness by setting the `dynamic-range-limit` property to `standard`, which makes the image no brighter than HDR reference white. We also set a [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
 property so that the `<img>` element's `dynamic-range-limit` value transitions over `0.6` seconds when its state changes.

css

    img {
      dynamic-range-limit: standard;
      transition: dynamic-range-limit 0.6s;
    }
    

On hover or focus, we change the value of the `<img>` element's `dynamic-range-limit` to `no-limit` so that it displays as brightly as the browser and display setup allow.

css

    img:hover,
    img:focus {
      dynamic-range-limit: no-limit;
    }
    

    img {
      max-height: 100vh;
    }
    @media not (dynamic-range: high) {
      body::before {
        content: "Your device may not display the image at full brightness.";
        background-color: wheat;
        display: block;
        text-align: center;
      }
    }
    @supports not (dynamic-range-limit: standard) {
      body::before {
        content: "Your browser doesn't support the dynamic-range-limit property.";
        background-color: wheat;
        display: block;
        text-align: center;
      }
    }
    

#### Results

The image is ultra HDR but is constrained to SDR brightness by default. Hover over or focus the image. Note how it transitions to vivid HDR colors on capable displays.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Color HDR Module Level 1  <br>\# the-dynamic-range-limit-property](https://drafts.csswg.org/css-color-hdr/#the-dynamic-range-limit-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`dynamic-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/dynamic-range)
     and [`video-dynamic-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/video-dynamic-range)
     media features

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/dynamic-range-limit/index.md?plain=1 "Folder: en-us/web/css/reference/properties/dynamic-range-limit (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fdynamic-range-limit&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fdynamic-range-limit%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fdynamic-range-limit%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fdynamic-range-limit%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F737b931225e92e0cba47e57a150878b1a78ee45a%0A*+Document+last+modified%3A+2026-08-24T15%3A52%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")