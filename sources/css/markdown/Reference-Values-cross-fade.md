*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade#mdn-search)
    

`cross-fade()` CSS function
===========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/55)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`cross-fade()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 can be used to blend two or more images at a defined transparency. It can be used for many basic image manipulations, such as tinting an image with a solid color or highlighting a particular area of the page by combining an image with a radial gradient.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade#syntax)

----------------------------------------------------------------------------------------------

**Warning:** The specification and current implementations have different syntaxes. The specification syntax is explained first.

### [Specification syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade#specification_syntax)

The `cross-fade()` function takes a list of images with a percentage defining how much of each image is retained in terms of opacity when it is blended with the other images. The percent value must be coded without quotes, must contain the `'%'` symbol, and its value must be between 0% and 100%.

The function can be used in CSS anywhere an ordinary image reference can be used.

#### Cross-fade percentages

Think of the percentage as an opacity value for each image. This means a value of 0% means the image is fully transparent while a value of 100% makes the image fully opaque.

css

    cross-fade(url("white.png") 0%, url("black.png") 100%); /* fully black */
    cross-fade(url("white.png") 25%, url("black.png") 75%); /* 25% white, 75% black */
    cross-fade(url("white.png") 50%, url("black.png") 50%); /* 50% white, 50% black */
    cross-fade(url("white.png") 75%, url("black.png") 25%); /* 75% white, 25% black */
    cross-fade(url("white.png") 100%, url("black.png") 0%); /* fully white */
    cross-fade(url("green.png") 75%, url("red.png") 75%); /* both green and red at 75% */
    

If any percentages are omitted, all the specified percentages are summed together and subtracted from `100%`. If the result is greater than 0%, the result is then divided equally between all images with omitted percentages.

In the simplest case, two images are faded between each other. To do that, only one of the images needs to have a percentage, the other one will be faded accordingly. For example, a value of 0% defined for the first image yields only the second image, while 100% yields only the first. A 25% value renders the first image at 25% and the second at 75%. The 75% value is the inverse, showing the first image at 75% and the second at 25%.

The above could also have been written as:

css

    cross-fade(url("white.png") 0%, url("black.png")); /* fully black */
    cross-fade(url("white.png") 25%, url("black.png")); /* 25% white, 75% black */
    cross-fade(url("white.png"), url("black.png")); /* 50% white, 50% black */
    cross-fade(url("white.png") 75%, url("black.png")); /* 75% white, 25% black */
    cross-fade(url("white.png") 100%, url("black.png")); /* fully white */
    cross-fade(url("green.png") 75%, url("red.png") 75%); /* both green and red at 75% */
    

If no percentages are declared, both the images will be 50% opaque, with a cross-fade rendering as an even merge of both images. The 50%/50% example seen above did not need to have the percentages listed, as when a percentage value is omitted, the included percentages are added together and subtracted from 100%. The result, if greater than 0, is then divided equally between all images with omitted percentages.

In the last example, the sum of both percentages is not 100%, and therefore both images include their respective opacities.

If no percentages are declared and three images are included, each image will be 33.33% opaque. The two following are lines (almost) identical:

css

    cross-fade(url("red.png"), url("yellow.png"), url("blue.png")); /* all three will be 33.3333% opaque */
    cross-fade(url("red.png") 33.33%, url("yellow.png") 33.33%, url("blue.png") 33.33%);
    

### [Older, implemented syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade#older_implemented_syntax)

css

    cross-fade( <image>, <image>, <percentage> )
    

The specification for the `cross-fade()` function allows for multiple images and for each image to have transparency values independent of the other values. This was not always the case. The original syntax, which has been implemented in some browsers, only allowed for two images, with the sum of the transparency of those two images being exactly 100%. The original syntax is supported in Safari and supported with the `-webkit-` prefix in Chrome, Opera, and other blink-based browsers.

css

    cross-fade(url("white.png"), url("black.png"), 0%);   /* fully black */
    cross-fade(url("white.png"), url("black.png"), 25%);  /* 25% white, 75% black */
    cross-fade(url("white.png"), url("black.png"), 50%);  /* 50% white, 50% black */
    cross-fade(url("white.png"), url("black.png"), 75%);  /* 75% white, 25% black */
    cross-fade(url("white.png"), url("black.png"), 100%); /* fully white */
    

In the implemented syntax, the two comma-separated images are declared first, followed by a comma and required percent value. Omitting the comma or percent invalidates the value. The percent is the opacity of the first declared image. The included percentage is subtracted from 100%, with the difference being the opacity of the second image.

The green/red example (with the percentages totaling 150%) and the yellow/red/blue example (with three images) from the specification syntax section, are not possible in this implementation.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade#accessibility)

------------------------------------------------------------------------------------------------------------

Browsers do not provide any special information on background images to assistive technology. This is important primarily for screen readers, as a screen reader will not announce its presence and therefore convey nothing to its users. If the image contains information critical to understanding the page's overall purpose, it is better to describe it semantically in the document. When using background images, make sure the contrast in color is great enough that any text is legible over the image as well as if the images are missing.

*   [MDN Understanding WCAG, Guideline 1.1 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.1_%E2%80%94_providing_text_alternatives_for_non-text_content)
    
*   [Understanding Success Criterion 1.1.1 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/text-equiv-all.html "External link (opens in new tab)")
    

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade#formal_syntax)

------------------------------------------------------------------------------------------------------------

<cross-fade()> =   
  cross-fade( <cf-image>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
<cf-image> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
  
  [<percentage \[0,100\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
[<image>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 =   
  [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image()>       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <image-set()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<cross-fade()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
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
    
  
<id-selector> =   
  <hash-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade#examples)

--------------------------------------------------------------------------------------------------

### [Older syntax for cross-fade](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade#older_syntax_for_cross-fade)

#### HTML

html

    <div class="cross-fade"></div>
    

#### CSS

css

    .cross-fade {
      width: 300px;
      height: 300px;
      background-image: -webkit-cross-fade(url("br.png"), url("tr.png"), 75%);
      background-image: cross-fade(url("br.png"), url("tr.png"), 75%);
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Images Module Level 4  <br>\# cross-fade-function](https://drafts.csswg.org/css-images-4/#cross-fade-function) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade#see_also)

--------------------------------------------------------------------------------------------------

*   [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
    
*   [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
    
*   [`image()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image)
    
*   [`image-set()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set)
    
*   [`element()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element)
    
*   [Using CSS gradients](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Using_gradients)
    
*   Gradient functions: [`linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)
    , [`radial-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/radial-gradient)
    , [`repeating-linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient)
    , [`repeating-radial-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-radial-gradient)
    , [`conic-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/conic-gradient)
    , [`repeating-conic-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-conic-gradient)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/cross-fade/index.md?plain=1 "Folder: en-us/web/css/reference/values/cross-fade (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcross-fade&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcross-fade%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcross-fade%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcross-fade%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")