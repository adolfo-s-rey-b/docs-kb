*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set#mdn-search)
    

`image-set()` CSS function
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`image-set()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [functional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 notation is a method of letting the browser pick the most appropriate CSS image from a given set, primarily for high pixel density screens.

Resolution and bandwidth differ by device and network access. The `image-set()` function delivers the most appropriate image resolution for a user's device, providing a set of image options — each with an associated resolution declaration — from which the browser picks the most appropriate for the device and settings. Resolution can be used as a proxy for filesize — a user agent on a slow mobile connection with a high-resolution screen may prefer to receive lower-resolution images rather than waiting for a higher resolution image to load.

`image-set()` allows the author to provide options rather than determining what each individual user needs.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set#syntax)

---------------------------------------------------------------------------------------------------

css

    /* Select image based on resolution */
    image-set(
      "image1.jpg" 1x,
      "image2.jpg" 2x
    );
    
    image-set(
      url("image1.jpg") 1x,
      url("image2.jpg") 2x
    );
    
    /* Select gradient based on resolution */
    image-set(
      linear-gradient(blue, white) 1x,
      linear-gradient(blue, green) 2x
    );
    
    /* Select image based on supported formats */
    image-set(
      url("image1.avif") type("image/avif"),
      url("image2.jpg") type("image/jpeg")
    );
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set#values)

[`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set#image)

The [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 can be any image type except for an image set. The `image-set()` function may not be nested inside another `image-set()` function.

[`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set#string)

A URL to an image.

[`<resolution>` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set#resolution)

[`<resolution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)
 units include `x` or `dppx`, for dots per pixel unit, `dpi`, for dots per inch, and `dpcm` for dots per centimeter. Every image within an `image-set()` must have a unique resolution.

[`type(<string>)` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set#typestring)

A valid MIME type string, for example "image/jpeg".

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

<image-set()> =   
  image-set( <image-set-option>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
<image-set-option> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<resolution>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 type( [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 ) [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
[<image>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 =   
  [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image()>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<image-set()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set)
   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <cross-fade()>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <element()>     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<gradient>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
        
  
[<image()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 =   
  image( <image-tags>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image-src>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 , [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
! )    
  
[<cross-fade()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade)
 =   
  cross-fade( <cf-image>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<element()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element)
 =   
  element( <id-selector> )    
  
<image-tags> =   
  ltr  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  rtl    
  
<image-src> =   
  [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
    
  
<cf-image> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  [<percentage \[0,100\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<id-selector> =   
  <hash-token>    

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set#accessibility)

-----------------------------------------------------------------------------------------------------------------

Browsers do not provide any special information on background images to assistive technology. This is important primarily for screen readers, as a screen reader will not announce its presence and therefore convey nothing to its users. If the image contains information critical to understanding the page's overall purpose, it is better to describe it semantically in the document.

*   [MDN Understanding WCAG, Guideline 1.1 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.1_%E2%80%94_providing_text_alternatives_for_non-text_content)
    
*   [Understanding Success Criterion 1.1.1 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/text-equiv-all.html "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set#examples)

-------------------------------------------------------------------------------------------------------

### [Using image-set() to provide alternative background-image options](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set#using_image-set_to_provide_alternative_background-image_options)

This example shows how to use [`image-set()`](https://drafts.csswg.org/css-images-4/#funcdef-image-set "External link (opens in new tab)")
 to provide two alternative [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 options, chosen depending on the resolution needed: a normal version and a high-resolution version.

html

    <div class="box"></div>
    

css

    .box {
      width: 400px;
      height: 200px;
      background-repeat: no-repeat;
      background-size: cover;
    
      background-image: image-set(
        url("https://mdn.github.io/shared-assets/images/examples/balloons-small.jpg")
          1x,
        url("https://mdn.github.io/shared-assets/images/examples/balloons-landscape.jpg")
          2x
      );
    }
    

### [Using image-set() to provide alternative image formats](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set#using_image-set_to_provide_alternative_image_formats)

In the next example the `type()` function is used to serve the image in AVIF and JPEG formats. If the browser supports avif, it will choose that version. Otherwise it will use the jpeg version.

html

    <div class="box"></div>
    

css

    .box {
      width: 400px;
      height: 200px;
      background-repeat: no-repeat;
      background-size: cover;
    
      background-image: image-set(
        "https://mdn.github.io/shared-assets/images/examples/balloons-landscape.avif"
          type("image/avif"),
        "https://mdn.github.io/shared-assets/images/examples/balloons-landscape.jpg"
          type("image/jpeg")
      );
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Images Module Level 4  <br>\# image-set-notation](https://drafts.csswg.org/css-images-4/#image-set-notation) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set#see_also)

-------------------------------------------------------------------------------------------------------

*   [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
    
*   [`image()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image)
    
*   [`element()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element)
    
*   [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
    
*   [`<gradient>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
    
*   [`cross-fade()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/image/image-set/index.md?plain=1 "Folder: en-us/web/css/reference/values/image/image-set (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fimage%2Fimage-set&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fimage%2Fimage-set%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fimage%2Fimage-set%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fimage%2Fimage-set%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")