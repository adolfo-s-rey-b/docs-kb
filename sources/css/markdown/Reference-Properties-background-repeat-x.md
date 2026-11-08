*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x#mdn-search)
    

`background-repeat-x` CSS property
==================================

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x#browser_compatibility)
 carefully before using this in production.

The **`background-repeat-x`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets how background images are repeated, or not, along the horizontal axis.

The `background-repeat-x` and [`background-repeat-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y)
 properties can also be set using the [`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
 or [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
 shorthand properties.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x#try_it)

-----------------------------------------------------------------------------------------------------------

    background-repeat-x: repeat;
    

    background-repeat-x: space;
    

    background-repeat-x: round;
    

    background-repeat-x: no-repeat;
    

    <section id="default-example">
      <div id="example-element"></div>
    </section>
    

    #example-element {
      background: #cccccc url("/shared-assets/images/examples/moon.jpg") no-repeat
        center / 120px;
      min-width: 100%;
      min-height: 100%;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x#syntax)

-----------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    background-repeat-x: repeat;
    background-repeat-x: space;
    background-repeat-x: round;
    background-repeat-x: no-repeat;
    
    /* Global values */
    background-repeat-x: inherit;
    background-repeat-x: initial;
    background-repeat-x: revert;
    background-repeat-x: revert-layer;
    background-repeat-x: unset;
    

The `background-repeat-x` property is specified as one or more values, separated by commas.

[Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x#values)

-----------------------------------------------------------------------------------------------------------

[`repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x#repeat)

The default value. The image is repeated as many times as needed to cover the entire width of the background image painting area. The edge image is clipped if multiple images do not fit exactly into the background width.

[`no-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x#no-repeat)

The image is not repeated. The position of the non-repeated background image is defined by the [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
 CSS property.

[`space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x#space)

The image is repeated as much as possible without clipping. The first and last images are pinned to the left and right of the element, and the whitespace is evenly distributed between them. The [`background-position-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x)
 property is ignored unless one or more images can be displayed without clipping. If the image is wider than the element, it is clipped, as there isn't enough room to display it.

[`round`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x#round)

The image is repeated horizontally. As the available space increases in size, the repeated images will stretch (leaving no gaps) until there is room for another one to be added. If multiple images don't fit the background exactly, they are rescaled to fit.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x#description)

---------------------------------------------------------------------------------------------------------------------

The `background-repeat-x` property accepts a comma-separated list of [`<repetition>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x#values)
 keyterms, which define how the background image(s) should repeat horizontally, or not repeat at all.

The default value is `repeat`. With this value, the background image repeats horizontally, covering the entire width of the background paint area, with edge images being clipped to the size of the element. Whether the left, right, or both edges are clipped depends on the value of the corresponding [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
 value. How many times images are repeated and how much the images on the edges are clipped depends on the size of the background painting area and width value of the corresponding [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
 property.

The repeating images can be evenly spaced apart, ensuring the repeated images aren't clipped in the horizontal direction. With the `space` value, if the width of the background paint area is not a multiple of the width of the image or does not otherwise have a size that is a multiple of the background size in the width direction, there will be areas not covered by the background image.

Alternatively, the repeated background image can be stretched to cover the entire width of the background area without clipping. With `round`, the repeated image is stretched to fill all the available space until there is room to add an additional repeated image.

For example, given a background image that is `100px` x `100px` and a background paint area that is `1099px` wide, the image will be resized to `109.9px wide` and repeated 10 times in the horizontal direction. This will alter the image's [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
 and distort it. If the width of the paint area increases by `1px` to `1100px`, an 11th image will fit horizontally, with each image being painted at `100px` wide, and no longer distorted horizontally.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

Value not found in DB!

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

background-repeat-x =   
  <repetition>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<repetition> =   
  repeat     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  space      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  round      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  no-repeat    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x#examples)

---------------------------------------------------------------------------------------------------------------

### [Setting background-repeat-x](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x#setting_background-repeat-x)

#### HTML

html

    <ol>
      <li>
        no-repeat
        <div class="one"></div>
      </li>
      <li>
        repeat
        <div class="two"></div>
      </li>
      <li>
        space
        <div class="three"></div>
      </li>
      <li>
        round
        <div class="four"></div>
      </li>
    </ol>
    

#### CSS

css

    ol,
    li {
      margin: 0;
      padding: 0;
    }
    li {
      margin-bottom: 12px;
    }
    div {
      background-image: url("star-solid.gif");
      width: 160px;
      height: 70px;
    }
    
    /* Background repeats */
    .one {
      background-repeat-x: no-repeat;
    }
    .two {
      background-repeat-x: repeat;
    }
    .three {
      background-repeat-x: space;
    }
    .four {
      background-repeat-x: round;
    }
    

    @layer no-support {
      @supports not (background-repeat-x: repeat) {
        body::before {
          content: "Your browser doesn't support the `background-repeat-x` property.";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

#### Result

In this example, each list item is matched with a different value of `background-repeat-x`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds Module Level 4  <br>\# background-repeat-longhands](https://drafts.csswg.org/css-backgrounds-4/#background-repeat-longhands) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`background-repeat-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y)
     and the [`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
     shorthand.
*   [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
     shorthand components: [`background-attachment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment)
    , [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
    , [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    , [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
    , [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
    , [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
     ([`background-position-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x)
     and [`background-position-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-y)
    ), and [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
    
*   [Using multiple backgrounds](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Using_multiple_backgrounds)
    
*   [CSS backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Using_multiple_backgrounds)
     module
*   [Understanding aspect ratios](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/background-repeat-x/index.md?plain=1 "Folder: en-us/web/css/reference/properties/background-repeat-x (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-repeat-x&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-repeat-x%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-repeat-x%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-repeat-x%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa8b7faffbd3fdeae5c0be97793d963d8a31cd1cf%0A*+Document+last+modified%3A+2026-04-22T11%3A39%3A37.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")