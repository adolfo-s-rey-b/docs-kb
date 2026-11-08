*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark#mdn-search)
    

`light-dark()` CSS function
===========================

Baseline 2024

Newly available

Since May 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`light-dark()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 accepts two colors or two images and returns a color or an image based on the active color scheme, without needing a [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using#targeting_media_features)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark#syntax)

----------------------------------------------------------------------------------------------------------

css

    /* Named color values */
    light-dark(
      black,
      white
    );
    
    /* RGB color values */
    light-dark(
      rgb(0 0 0),
      rgb(255 255 255)
    );
    
    /* image url values */
    light-dark(
      url("light-icon.png"),
      url("dark-icon.png")
    );
    
    /* linear-gradient values */
    light-dark(
      linear-gradient(135deg, ghostwhite 20%, tomato),
      linear-gradient(45deg, darkslategray 20%, gold)
    );
    
    /* Custom properties */
    light-dark(
      var(--light),
      var(--dark)
    );
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark#values)

The light-dark() function has two forms:

*   Accepts two `<color>` values:
    
    [`<color>` (light)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark#color)
    
    The [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
     value used when the [`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme)
     is `light` or no preference is set.
    
    [`<color>` (dark)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark#color_2)
    
    The [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
     value used when the [`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme)
     is `dark`.
    
*   Accepts two `<image>` values:
    
    [`<image>` (light)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark#image)
    
    The [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
     value used when the [`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme)
     is `light` or no preference is set.
    
    [`<image>` (dark)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark#image_2)
    
    The [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
     value used when the [`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme)
     is `dark`.
    
    [`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark#none)
    
    The `none` keyword produces a fully transparent image with no natural size.
    

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark#description)

--------------------------------------------------------------------------------------------------------------------

Users can indicate their color scheme preference through their operating system settings (e.g., light or dark mode) or their user agent settings. The `light-dark()` function enables providing either two color values where any `<color>` value is accepted or two image values where any `<image>` value is accepted. The `light-dark()` function returns the first value if the used color scheme is `light` or if no preference is set and the second value if the used color scheme is `dark`.

To enable support for the `light-dark()` color function, the [`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme)
 must have a value of `light dark`, usually set on the [`:root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:root)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
.

css

    :root {
      color-scheme: light dark;
    }
    body {
      color: light-dark(#333b3c, #efefec);
      background-color: light-dark(#efedea, #223a2c);
    }
    

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark#formal_syntax)

------------------------------------------------------------------------------------------------------------------------

<light-dark()> =   
  <light-dark-color>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <light-dark-image>    
  
<light-dark-color> =   
  light-dark( [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 , [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 )    
  
<light-dark-image> =   
  light-dark( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 none [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 , [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <image> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 none [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 )    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark#examples)

--------------------------------------------------------------------------------------------------------------

### [Setting colors based on a color scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark#setting_colors_based_on_a_color_scheme)

By default, in supporting browsers, the color returned by the `light-dark()` color function depends on the user preference set through an operating system's settings (e.g., light or dark mode) or from a user agent setting. You can also change this setting in the browser's [developer tools](https://developer.mozilla.org/en-US/docs/Glossary/Developer_Tools)
.

#### HTML

We include three sections to enable targeting light colors, dark colors, and the colors selected based on the user's preferred color scheme.

html

    <h1><code>light-dark()</code> CSS function</h1>
    <section>
      <h2>Automatic</h2>
      <p>This section will react to the users system or user agent setting.</p>
    </section>
    <section class="light">
      <h2>Light</h2>
      <p>
        This section will be light due to the <code>color-scheme: light;</code>.
      </p>
    </section>
    <section class="dark">
      <h2>Dark</h2>
      <p>This section will be dark due to the <code>color-scheme: dark;</code>.</p>
    </section>
    

#### CSS

We include colors for both light and dark themes. We also define `color-scheme` for the document on the `:root` to enable the `light-dark()` color function for the entire document.

css

    :root {
      /* this has to be set to switch between light or dark */
      color-scheme: light dark;
    
      --light-bg: ghostwhite;
      --light-color: darkslategray;
      --light-code: tomato;
    
      --dark-bg: darkslategray;
      --dark-color: ghostwhite;
      --dark-code: gold;
    }
    * {
      background-color: light-dark(var(--light-bg), var(--dark-bg));
      color: light-dark(var(--light-color), var(--dark-color));
    }
    code {
      color: light-dark(var(--light-code), var(--dark-code));
    }
    

In addition to enabling the `light-dark()` function, the `color-scheme` property enables overriding a user's color scheme for document sections. Forcing a page section to only use a light or dark color scheme can be done by setting the `color-scheme` property to `light` or `dark`.

**Note:** Generally this should not be done, we are using it here for demonstration purposes. If the user has made a preference, you generally should not override their preferences.

css

    .light {
      /* forces light color-scheme */
      color-scheme: light;
    }
    .dark {
      /* forces dark color-scheme */
      color-scheme: dark;
    }
    

    section {
      padding: 0.8rem;
    }
    

#### Result

### [Setting gradient background based on a color scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark#setting_gradient_background_based_on_a_color_scheme)

This example uses the same HTML code as the previous example but includes a `<div>` instead of a `<p>`.

    <h1><code>light-dark()</code> CSS function with images</h1>
    <p class="supports">
      Your browser does not support <code>light-dark()</code> with images.
    </p>
    <div class="wrapper">
      <section>
        <h2>Automatic</h2>
        <div></div>
      </section>
      <section class="light">
        <h2>Light</h2>
        <div></div>
      </section>
      <section class="dark">
        <h2>Dark</h2>
        <div></div>
      </section>
    </div>
    

#### CSS

    :root {
      /* this has to be set to switch between light or dark */
      color-scheme: light dark;
    
      --light-bg: ghostwhite;
      --light-color: darkslategray;
      --light-code: tomato;
    
      --dark-bg: darkslategray;
      --dark-color: ghostwhite;
      --dark-code: gold;
    }
    * {
      background-color: light-dark(var(--light-bg), var(--dark-bg));
      color: light-dark(var(--light-color), var(--dark-color));
    }
    .wrapper {
      display: flex;
      justify-content: space-around;
      padding: 0.8rem;
    }
    .light {
      /* forces light color-scheme */
      color-scheme: light;
    }
    .dark {
      /* forces dark color-scheme */
      color-scheme: dark;
    }
    section {
      width: 25%;
      padding: 5px;
      color: light-dark(
        var(--light-code),
        var(--dark-code)
      );
      border: 2px solid light-dark(var(--light-code), var(--dark-code));
    }
    @supports (background-image: light-dark(url("light.png"), url("dark.png"))) {
      .supports {display:none;}
    }
    

Firstly, we define light and dark `linear-gradient()` values as custom properties.

css

    :root {
      /*  light dark gradients  */
      --light-grad: linear-gradient(135deg, var(--light-bg) 20%, var(--light-code));
      --dark-grad: linear-gradient(45deg, var(--dark-bg) 30%, var(--dark-code));
    }
    

    section div {
      width: 80%;
      aspect-ratio: 1/1;
      margin: auto;
      border: 1px solid light-dark(var(--light-code), var(--dark-code));
    }
    @supports not (
      background-image: light-dark(url("light.png"), url("dark.png"))
    ) {
      section div {
        width: 60%;
      }
    }
    

Then we use the custom properties with `light-dark()` to set the `background-image` property based on the active color scheme.

css

    section div {
      background-image: light-dark(
        var(--light-grad),
        var(--dark-grad)
      );
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Color Module Level 5  <br>\# light-dark](https://drafts.csswg.org/css-color-5/#light-dark) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark#see_also)

--------------------------------------------------------------------------------------------------------------

*   [`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme)
    
*   [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
    
*   [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
    
*   [CSS colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors)
     module
*   [`prefers-contrast`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-contrast)
     [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
     feature
*   [`contrast()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast)
    
*   [WCAG: color contrast](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable/Color_contrast)
    
*   [CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
     and [`var()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/color_value/light-dark/index.md?plain=1 "Folder: en-us/web/css/reference/values/color_value/light-dark (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcolor_value%2Flight-dark&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcolor_value%2Flight-dark%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fcolor_value%2Flight-dark%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fcolor_value%2Flight-dark%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")