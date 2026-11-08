*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image#mdn-search)
    

`background-image` CSS property
===============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`background-image`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets one or more background images on an element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image#try_it)

--------------------------------------------------------------------------------------------------------

    background-image: url("/shared-assets/images/examples/lizard.png");
    

    background-image:
      url("/shared-assets/images/examples/lizard.png"),
      url("/shared-assets/images/examples/star.png");
    

    background-image:
      url("/shared-assets/images/examples/star.png"),
      url("/shared-assets/images/examples/lizard.png");
    

    background-image:
      linear-gradient(rgb(0 0 255 / 0.5), rgb(255 255 0 / 0.5)),
      url("/shared-assets/images/examples/lizard.png");
    

    <section id="default-example">
      <div id="example-element"></div>
    </section>
    

    #example-element {
      min-width: 100%;
      min-height: 100%;
      padding: 10%;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image#syntax)

--------------------------------------------------------------------------------------------------------

css

    /* single image */
    background-image: linear-gradient(black, white);
    background-image: url("cat-front.png");
    
    /* multiple images */
    background-image:
      radial-gradient(circle, transparent 45%, black 48%),
      radial-gradient(ellipse farthest-corner, #fc1c14 20%, #cf15cf 80%);
    
    /* Global values */
    background-image: inherit;
    background-image: initial;
    background-image: revert;
    background-image: revert-layer;
    background-image: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image#values)

This property is specified as the keyword `none` or as a comma-separated list of [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 values.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image#none)

Is a keyword denoting the absence of images.

[`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image#image)

Is an [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 denoting the image to display.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image#description)

------------------------------------------------------------------------------------------------------------------

The `background-image` property sets background images on an element.

You can define [multiple backgrounds](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Using_multiple_backgrounds)
 on an element by specifying a list of comma-separated image. The background images are drawn on stacking context layers on top of each other. The first layer specified is drawn as if it is closest to the user.

The [borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
 of the element are then drawn on top of them, and the [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 is drawn beneath them. How the images are drawn relative to the box and its borders is defined by the [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
 and [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
 CSS properties.

If a specified image cannot be drawn (for example, when the file denoted by the specified URI cannot be loaded), browsers handle it as they would a `none` value.

**Note:** Even if the images are opaque and the color won't be displayed in normal circumstances, web developers should always specify a [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
. If the images cannot be loaded—for instance, when the network is down—the background color will be used as a fallback.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image#accessibility)

----------------------------------------------------------------------------------------------------------------------

Browsers do not provide any special information on background images to assistive technology. This is important primarily for screen readers, as a screen reader will not announce its presence and therefore convey nothing to its users. If the image contains information critical to understanding the page's overall purpose, it is better to describe it semantically in the document.

*   [MDN Understanding WCAG, Guideline 1.1 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.1_%E2%80%94_providing_text_alternatives_for_non-text_content)
    
*   [Understanding Success Criterion 1.1.1 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/text-equiv-all.html "External link (opens in new tab)")
    

Additionally, it is important to ensure that the contrast ratio between the background image and the foreground text is high enough that people with low vision can read the page content.

Color contrast ratio is determined by comparing the luminance of the text and background color values. To meet [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/ "External link (opens in new tab)")
, a ratio of 4.5:1 is required for body text content and 3:1 for larger text such as headings. Large text is defined as 24px or larger, or [bolded](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
 18.66px or larger.

*   [WebAIM: Color Contrast Checker](https://webaim.org/resources/contrastchecker/ "External link (opens in new tab)")
    
*   [Understanding WCAG, Guideline 1.4 explanation](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [Understanding Success Criterion 1.4.3 | Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html "External link (opens in new tab)")
    , W3C (2023)

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image#formal_definition)

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified, but with [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)<br> values made absolute |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image#formal_syntax)

----------------------------------------------------------------------------------------------------------------------

background-image =   
  <bg-image>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<bg-image> =   
  <image>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none       
  
[<image>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 =   
  [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image()>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image-set()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
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
  
[<image-set()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set)
 =   
  image-set( <image-set-option>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image#examples)

------------------------------------------------------------------------------------------------------------

### [Layering background images](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image#layering_background_images)

Note that the star image is partially transparent and is layered over the cat image.

#### HTML

html

    <div>
      <p class="cats-and-stars">This paragraph is full of cats<br />and stars.</p>
      <p>This paragraph is not.</p>
      <p class="cats-and-stars">Here are more cats for you.<br />Look at them!</p>
      <p>And no more.</p>
    </div>
    

#### CSS

css

    p {
      font-weight: bold;
      font-size: 1.5em;
      color: white;
      text-shadow: 0.07em 0.07em 0.05em black;
      background-image: none;
      background-color: transparent;
    }
    
    div {
      background-image: url("mdn_logo_only_color.png");
    }
    
    .cats-and-stars {
      background-image: url("star-transparent.gif"), url("cat-front.png");
      background-color: transparent;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3  <br>\# background-image](https://drafts.csswg.org/css-backgrounds/#background-image) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image#see_also)

------------------------------------------------------------------------------------------------------------

*   [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
    
*   Image-related functions:
    
    *   [`linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)
        
    *   [`radial-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/radial-gradient)
        
    *   [`conic-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/conic-gradient)
        
    *   [`repeating-linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient)
        
    *   [`repeating-radial-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-radial-gradient)
        
    *   [`repeating-conic-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-conic-gradient)
        
    *   [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
        
*   [Using CSS gradients](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Using_gradients)
    
*   [Implementing image sprites in CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Implementing_image_sprites)
    
*   [CSS images](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images)
     module
    
*   Background-related properties
    
    *   [`background-attachment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment)
        
    *   [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
        
    *   [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
        
    *   [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
        
    *   [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
        
    *   [`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
        
    *   [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
        
    *   [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
         shorthand
*   [Learn: Backgrounds and borders](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Backgrounds_and_borders)
    
*   [Using multiple backgrounds](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Using_multiple_backgrounds)
    
*   [Resizing background images](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Resizing_background_images)
    
*   [CSS backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
     module
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/background-image/index.md?plain=1 "Folder: en-us/web/css/reference/properties/background-image (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-image&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-image%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-image%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-image%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")