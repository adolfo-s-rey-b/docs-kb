*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts#mdn-search)
    

Variable fonts
==============

**Variable fonts** are an evolution of the OpenType font specification that enables many different variations of a typeface to be incorporated into a single file, rather than having a separate font file for every width, weight, or style. They let you access all the variations contained in a given font file via CSS and a single [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
 reference. This article will give you all you need to know to get you started using variable fonts.

**Note:** To use variable fonts on your operating system, you need to make sure that it is up to date. For example, Linux OSes need the latest Linux FreeType version, and macOS prior to High Sierra (10.13) does not support variable fonts. If your operating system is not up to date, you will not be able to use variable fonts in web pages or the Firefox Developer Tools.

[Variable Fonts: what they are, and how they differ](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts#variable_fonts_what_they_are_and_how_they_differ)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To better understand what's different about variable fonts, it is worth reviewing what non-variable ones are like and how they compare.

### [Standard (or Static) fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts#standard_or_static_fonts)

In the past, a typeface would be produced as several individual fonts, and each font would represent one specific width/weight/style combination. So you would have separate files for 'Roboto Regular', 'Roboto Bold', and 'Roboto Bold Italic' — meaning that you could end up with 20 or 30 different font files to represent a complete typeface (it could be several times that for a large typeface that has different widths as well).

In such a scenario, to use a typeface for typical use on a site for body copy you would need at least four files: regular, italic, bold, and bold italic. If you wanted to add more weights, like a lighter one for captions or a heavier one for extra emphasis, that would mean several more files. This results in more HTTP requests, and more data being downloaded (usually around 20k or more per file).

### [Variable fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts#variable_fonts)

With a variable font, all of those permutations can be contained in a single file. That file would be larger than a single font, but in most cases smaller or about the same size as the 4 you might load for body copy. The advantage in choosing the variable font is that you have access to the entire range of weights, widths, and styles available, rather than being constrained to only the few that you previously would have loaded separately.

This allows for common typographic techniques such as setting different size headings in different weights for better readability at each size or using a slightly narrower width for data-dense displays. For comparison, it is typical in a typographic system for a magazine to use 10–15 or more different weight and width combinations throughout the publication — giving a much wider range of styles than currently typical on the web (or indeed practical for performance reasons alone).

#### A note about font families, weights, and variants

You might notice that we have been talking about having a specific font file for every weight and style (i.e., bold and italic and bold italic), rather than relying upon the browser to synthesize them. The reason for this is that most typefaces have very specific designs for bolder weights and italics that often include completely different characters (lower-case 'a' and 'g's are often quite different in italics, for example). To most accurately reflect the typeface design and avoid differences between browsers and how they may or may not synthesize the different styles, it's more accurate to load the specific font files where needed when using a non-variable font.

You may also find that some variable fonts come split into two files: one for uprights and all their variations, and one containing the italic variations. This is sometimes done to reduce the overall file size in cases where the italics aren't needed or used. In all cases, it is still possible to link them with a common [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
 name so you can call them using the same `font-family` and appropriate [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
.

[Introducing the 'variation axis'](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts#introducing_the_variation_axis)

------------------------------------------------------------------------------------------------------------------------------------------------

The heart of the new variable fonts format is the concept of an **axis of variation** describing the allowable range of that particular aspect of the typeface design. So the 'weight axis' describes how light or how bold the letterforms can be; the 'width axis' describes how narrow or how wide they can be; the 'italic axis' describes if italic letterforms are present and can be turned on or off accordingly, etc. Note that an axis can be a range or a binary choice. Weight might range from 1–999, whereas italic might be 0 or 1 (off or on).

As defined in the specification, there are two kinds of axes: **registered** and **custom**:

*   Registered axes are those that are most frequently encountered, and common enough that the authors of the specification felt it was worth standardizing. The five currently registered axes are weight, width, slant, italic, and optical size. The W3C has undertaken to map them to existing CSS attributes, and in one case introduced a new one, which you'll see below.
*   Custom axes are limitless: the typeface designer can define and scope any axis they like and are just required to give it a four-letter **tag** to identify it within the font file format itself. You can use these four-letter tags in CSS to specify a point along that axis of variation, as will be shown in the code examples below.

### [Registered axes and existing CSS attributes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts#registered_axes_and_existing_css_attributes)

In this section we'll demonstrate the five registered axes defined with examples and the corresponding CSS. Where possible, both the standard and lower-level syntax are included. The lower-level syntax ([`font-variation-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings)
) was the first mechanism implemented to test the early implementations of variable font support and is necessary to utilize new or custom axes beyond the five registered ones. However, the W3C's intent was for this syntax not to be used when other attributes are available. Therefore wherever possible, the appropriate property should be used, with the lower-level syntax of `font-variation-settings` only being used to set values or axes not available otherwise.

#### Notes

1.  When using `font-variation-settings` it is important to note that axis names are case-sensitive. The registered axis names must be in lower case, and custom axes must be in upper case. For example:
    
    `wght` (weight) is a registered axis, and `GRAD` (grade) is a custom one.
    
2.  If you have set values using `font-variation-settings` and want to change one of those values, you must redeclare all of them (in the same way as when you set OpenType font features using [`font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings)
    ). You can work around this limitation by using [CSS Custom Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties)
     (CSS variables) for the individual values, and modifying the value of an individual custom property. Example code follows at the end of the guide.
    

### [Weight](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts#weight)

Weight (represented by the `wght` tag) defines the design axis of how thin or thick (light or heavy, in typical typographic terms) the strokes of the letterforms can be. For a long time in CSS there has existed the ability to specify this via the [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
 property, which takes numeric values ranging from 100 to 900 in increments of 100, and keywords like `normal` or `bold`, which are aliases for their corresponding numeric values (400 and 700 in this case). These are still applied when dealing with non-variable or variable fonts, but with variable ones, any number from 1 to 1000 is now valid.

It should be noted that at this point there is no way in the `@font-face` declaration to 'map' a specific point on the variation axis of a variable font to the keyword `bold` (or any other keyword). This can generally be resolved fairly easily, but does require an extra step in writing your CSS:

Click "Play" in the code blocks below to edit the example in the MDN Playground. Edit the CSS code to play with font-weight values.

### [Width](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts#width)

Width (represented by the `wdth` tag) defines the design axis of how narrow or wide (condensed or extended, in typographic terms) the letterforms can be. This is typically set in CSS using the [`font-stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch)
 property, with values expressed as a percentage above or below 'normal' (100%), any number greater than 0 is technically valid—though it is far more likely that the range would fall closer to the 100% mark, such as 75%-125%. If a number value supplied is outside the range encoded in the font, the browser should render the font at the closest value allowed.

**Note:** The % symbol is not used when utilizing `font-variation-settings`.

Click "Play" in the code blocks below to edit the example in the MDN Playground. Edit the CSS code to play with font width values.

    <div>
      <p class="p1">Width</p>
      <span>(font-stretch: 60%)</span>
    </div>
    <div>
      <p class="p2">Width</p>
      <span>(font-variation-settings: "wdth" 60)</span>
    </div>
    <div class="adjustable">
      <p class="p3">Width</p>
      (font-variation-settings: "wdth" <span id="angle-text">60</span>)<br />
    
      <label for="text-axis">Adjust Width: </label>
      <input
        type="range"
        id="text-axis"
        name="text-axis"
        min="55"
        max="100"
        value="60" />
    </div>
    

    @font-face {
      font-family: "Amstelvar VF";
      src: url("https://mdn.github.io/shared-assets/fonts/variable-fonts/AmstelvarAlpha-VF.woff2")
        format("woff2-variations");
      font-weight: 300 900;
      font-stretch: 35% 100%;
      font-style: normal;
      font-display: swap;
    }
    
    p {
      font:
        1.2em "Amstelvar VF",
        "Georgia",
        serif;
      font-size: 4rem;
      margin: 1rem;
      display: inline-block;
    }
    
    .adjustable {
      border: 1px dashed;
      --text-axis: 60;
    }
    

css

    /* width range is 55% to 100% */
    .p1 {
      font-stretch: 60%;
    }
    
    /* width range is an integer from 55 to 100 */
    .p2 {
      font-variation-settings: "wdth" 60;
    }
    
    /* Adjust with slider & custom property */
    .p3 {
      font-variation-settings: "wdth" var(--text-axis);
    }
    

    const angle = document.querySelector("#text-axis");
    const text = document.querySelector("#angle-text");
    const adjustable = document.querySelector(".adjustable");
    
    angle.addEventListener("input", (e) => {
      const angle = e.target.value;
      text.innerText = angle;
      adjustable.style.setProperty("--text-axis", angle);
    });
    

### [Italic](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts#italic)

The Italic (`ital`) axis can be set in the range `[0-1]`, where `0` specifies "not italic," `0.5` specifies "halfway italic," and `1` specifies "fully italic." Italic designs often include dramatically different letterforms from their upright counterparts, so in the transition from upright to italic, several glyph (or character) substitutions usually occur. Italic and oblique are often used somewhat interchangeably, but in truth are quite different. Oblique is defined in this context with the term `slant` (see the below section), and a typeface would typically have one or the other, but not both.

In CSS, both italic and oblique are applied to text using the [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
 property. Also note the introduction of `font-synthesis: none;` — which will prevent browsers from accidentally applying the variation axis and a synthesized italic. This can be used to prevent faux-bolding as well.

Click "Play" in the code blocks below to edit the example in the MDN Playground. Edit the CSS code to play with font-italics.

    <div>
      <p class="p1">Italic</p>
      <span>(font-style: italic)</span>
      <p class=".p1-no-synthesis">Italic</p>
      <span>(font-style: italic; font-synthesis: none)</span>
    </div>
    <div>
      <p class="p2">Italic</p>
      <span>(font-variation-settings: "ital" 1)</span>
    </div>
    <div class="adjustable">
      <p class="p3">Italic</p>
      (font-variation-settings: "ital" <span id="angle-text">1</span>)<br />
    
      <label for="slant-angle">Adjust Italic: </label>
      <input
        type="range"
        id="text-axis"
        name="text-axis"
        min="0"
        max="1"
        value="1" />
    </div>
    

    @font-face {
      font-family: "Jost VF";
      src: url("https://mdn.github.io/shared-assets/fonts/variable-fonts/jost-VF.woff2")
        format("woff2-variations");
      font-weight: 300 900;
      font-stretch: 75% 150%;
      font-display: swap;
    }
    
    p {
      font:
        1.2em "Jost VF",
        "Helvetica",
        "Arial",
        sans-serif;
      font-size: 4rem;
      margin: 1rem;
      display: inline-block;
    }
    
    .adjustable {
      border: 1px dashed;
      --text-axis: 1;
    }
    

css

    /* font-style: italic, with and without font-synthesis */
    .p1 {
      font-style: italic;
    }
    
    .p1-no-synthesis {
      font-style: italic;
      font-synthesis: none;
    }
    
    /* italic range is 0 or 1 */
    .p2 {
      font-variation-settings: "ital" 1;
      font-synthesis: none;
    }
    
    /* Adjust with slider & custom property */
    .p3 {
      font-synthesis: none;
      font-variation-settings: "ital" var(--text-axis);
    }
    

    const angle = document.querySelector("#text-axis");
    const text = document.querySelector("#angle-text");
    const adjustable = document.querySelector(".adjustable");
    
    angle.addEventListener("input", (e) => {
      const angle = e.target.value;
      text.innerText = angle;
      adjustable.style.setProperty("--text-axis", angle);
    });
    

### [Slant](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts#slant)

Slant (represented by the `slnt` tag), or as it's often referred to, 'oblique' — is different from true italics in that it changes the angle of the letterforms but doesn't perform any kind of character substitution. It is also variable, in that it is expressed as a numeric range. This allows the font to be varied anywhere along the slant axis. The allowed range is from -90 to 90 degrees.

The two properties that can control the slant are [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
 and [`font-variation-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings)
. The following two property declarations are the same:

font-style: oblique 14deg;

font-variation-settings: "slnt" -14;

Prefer the `font-style` property over the `font-variation-settings` property. The `deg` keyword is not used when using the `font-variation-settings` property. Also, in the case of the `font-variation-settings` property, a positive angle means a counter-clockwise slant.

In the following live example, you can adjust the slant.

    <div>
      <p class="font-style">Slant</p>
      <span>(font-style: oblique 5deg)</span>
    </div>
    <div>
      <p class="font-variation">Slant</p>
      <span>(font-variation-settings: 'slnt' -5)</span>
    </div>
    <div class="adjustable-box">
      <p class="adjustable">Slant</p>
      (font-variation-settings: 'slnt' <span id="angle-text">-5</span>)<br />
    
      <label for="slant-angle">Adjust Slant: </label>
      <input
        type="range"
        name="range-slider"
        value="5"
        id="slant-angle"
        min="-15"
        max="15" />
    </div>
    

    @font-face {
      font-family: "SlantFont";
      font-style: oblique -15deg 15deg;
      src: url("https://mdn.github.io/shared-assets/fonts/font_with_slant_axis.woff2")
        format("woff2");
    }
    
    p {
      font-family: "SlantFont", sans-serif;
      display: inline-block;
      margin: 1rem;
      font-size: 4rem;
    }
    
    .adjustable-box {
      border: 1px dashed;
      --text-axis: -5;
    }
    

css

    .font-style {
      font-style: oblique 5deg;
    }
    
    .font-variation {
      font-variation-settings: "slnt" -5;
    }
    
    .adjustable {
      font-variation-settings: "slnt" var(--slant-angle);
    }
    

    const angle = document.querySelector("#slant-angle");
    const text = document.querySelector("#angle-text");
    const adjustable = document.querySelector(".adjustable");
    
    angle.addEventListener("input", (e) => {
      const angle = -1 * e.target.value;
      text.innerText = angle;
      adjustable.style.setProperty("--slant-angle", angle);
    });
    

### [Optical size](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts#optical_size)

This is something new to digital fonts and CSS, but is a centuries-old technique in designing and creating metal type. Optical sizing refers to the practice of varying the overall stroke thickness of letterforms based on physical size. If the size was very small (such as an equivalent to 10 or 12px), the characters would have an overall thicker stroke, and perhaps other small modifications to ensure that it would reproduce and be readable at a physically smaller size. Conversely, when a much larger size was being used (like 48 or 60px), there might be much greater variation in thick and thin stroke weights, showing the typeface design more in line with the original intent.

While this was originally done to compensate for the ink and paper printing process (very thin lines at small sizes often didn't print, giving the letterforms a broken appearance), it translates well to digital displays when compensating for screen quality and physical size rendering.

Optical size values are generally intended to be automatically applied corresponding to `font-size`, but can also be manipulated using the lower-level `font-variation-settings` syntax.

There is a new attribute, [`font-optical-sizing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-optical-sizing)
, created to support variable fonts in CSS. When using `font-optical-sizing`, the only allowed values are `auto` or `none` — so this attribute only allows for turning optical sizing on or off. However when using `font-variation-settings: 'opsz' <num>`, you can supply a numeric value. In most cases you would want to match the `font-size` (the physical size the type is being rendered) with the `opsz` value (which is how optical sizing is intended to be applied when using `auto`). The option to provide a specific value is provided so that should it be necessary to override the default — for legibility, aesthetic, or some other reason — a specific value can be applied.

Click "Play" in the code blocks below to edit the example in the MDN Playground. Edit the CSS code to play with optical size values.

    <div>
      <p class="p1">Optical Size</p>
      <span>(font-optical-sizing: none)</span>
    </div>
    <div>
      <p class="p2">Optical Size</p>
      <span>(font-optical-sizing: auto)</span>
    </div>
    <div>
      <p class="p3">Optical Size</p>
      <span>(font-variation-settings: "opsz" 64)</span>
    </div>
    
    <div class="adjustable">
      <p class="p4">Optical Size</p>
      (font-variation-settings: "opsz" <span id="angle-text">-64</span>)<br />
    
      <label for="slant-angle">Adjust Optical Sizing: </label>
      <input
        type="range"
        name="text-axis"
        value="64"
        id="text-axis"
        min="8"
        max="144" />
    </div>
    

    @font-face {
      font-family: "Amstelvar VF";
      src: url("https://mdn.github.io/shared-assets/fonts/variable-fonts/AmstelvarAlpha-VF.woff2")
        format("woff2-variations");
      font-weight: 300 900;
      font-stretch: 75% 150%;
      font-style: normal;
      font-display: swap;
    }
    
    p {
      font:
        1.2em "Amstelvar VF",
        "Georgia",
        serif;
      font-size: 4rem;
      margin: 1rem;
      display: inline-block;
    }
    
    .adjustable {
      border: 1px dashed;
      --text-axis: 64;
    }
    

css

    .p1 {
      font-optical-sizing: none;
    }
    /* font-optical-sizing can be auto or none */
    .p2 {
      font-optical-sizing: auto;
    }
    
    /* optical range is from 8 to 144 */
    .p3 {
      font-variation-settings: "opsz" 64;
    }
    
    /* Adjust with slider & custom property */
    .p4 {
      font-variation-settings: "opsz" var(--text-axis);
    }
    

    const angle = document.querySelector("#text-axis");
    const text = document.querySelector("#angle-text");
    const adjustable = document.querySelector(".adjustable");
    
    angle.addEventListener("input", (e) => {
      const angle = e.target.value;
      text.innerText = angle;
      adjustable.style.setProperty("--text-axis", angle);
    });
    

### [Custom axes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts#custom_axes)

Custom axes are just that: they can be any axis of design variation that the typeface designer imagines. There may be some that become fairly common — or even become registered — but only time will tell.

### [Grade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts#grade)

Grade may become one of the more common custom axes as it has a known history in typeface design. The practice of designing different grades of a typeface was often done in reaction to intended use and printing technique. The term 'grade' refers to the relative weight or density of the typeface design, but differs from traditional 'weight' in that the physical space the text occupies does not change, so changing the text grade doesn't change the overall layout of the text or elements around it. This makes grade a useful axis of variation as it can be varied or animated without causing a reflow of the text itself.

Click "Play" in the code blocks below to edit the example in the MDN Playground. Edit the CSS code to play with font-grade values.

    <div>
      <p class="p1">Grade</p>
      <span>(font-variation-settings: 'GRAD' 88)</span>
    </div>
    
    <div class="adjustable">
      <p class="p2">Grade</p>
      (font-variation-settings: 'GRAD' <span id="angle-text">88</span>)<br />
    
      <label for="slant-angle">Adjust Grade: </label>
      <input
        type="range"
        name="text-axis"
        value="88"
        id="text-axis"
        min="88"
        max="150" />
    </div>
    

    @font-face {
      font-family: "Amstelvar VF";
      src: url("https://mdn.github.io/shared-assets/fonts/variable-fonts/AmstelvarAlpha-VF.woff2")
        format("woff2-variations");
      font-weight: 300 900;
      font-stretch: 75% 150%;
      font-style: normal;
      font-display: swap;
    }
    
    p {
      font:
        1.2em "Amstelvar VF",
        "Georgia",
        serif;
      font-size: 64px;
      margin: 1rem;
      display: inline-block;
    }
    
    .adjustable {
      border: 1px dashed;
      --text-axis: 88;
    }
    

css

    /* grade range is 88 to 150 */
    .p1 {
      font-size: 64px;
      font-variation-settings: "GRAD" 88;
    }
    
    /* Adjust with slider & custom property */
    .p2 {
      font-size: 64px;
      font-variation-settings: "GRAD" var(--text-axis);
    }
    

    const angle = document.querySelector("#text-axis");
    const text = document.querySelector("#angle-text");
    const adjustable = document.querySelector(".adjustable");
    
    angle.addEventListener("input", (e) => {
      const angle = e.target.value;
      text.innerText = angle;
      adjustable.style.setProperty("--text-axis", angle);
    });
    

### [Using a variable font: @font-face changes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts#using_a_variable_font_font-face_changes)

The syntax for loading variable fonts is very similar to any other web font, with a few notable differences, which are provided via upgrades to the traditional [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
 syntax now available in modern browsers.

The basic syntax is the same, but the font technology can be specified, and allowable ranges for descriptors like `font-weight` and `font-stretch` can be supplied, rather than named according to the font file being loaded.

#### Example for a standard upright (Roman) font

In this case, the `font-style: normal` declaration indicates that this font file should be used when `font-family` is set to `MyVariableFontName` and [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
 is set to `normal`. As an alternative, you could use `font-style: oblique 0deg` or `font-style: oblique 0deg 20deg` to indicate that the font has normal upright glyphs (indicated by `0deg`).

#### Example for a font that contains only italics and no upright characters

In this case, the `font-style: italic` declaration indicates that this font file should be used when `font-family` is set to `MyVariableFontName` and [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
 is set to `italic`. As an alternative, you could use `font-style: oblique 14deg` to indicate that the font has italic glyphs.

#### Example for a font that contains an oblique (slant) axis

In this case, the `oblique 0deg 12deg` value indicates that this font file should be used when in a style rule the `font-family` property is `MyVariableFontName` and the [font-style](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
 property is oblique with an angle between zero and 12 degrees inclusive.

**Note:** Not all browsers have implemented the full syntax for font format, so test carefully. All browsers that support variable fonts will still render them if you set the format to just the file format, rather than format-variations (i.e., `woff2` instead of `woff2-variations`), but it's best to use the proper syntax if possible.

**Note:** Supplying value ranges for `font-weight`, `font-stretch`, and `font-style` will keep the browser from attempting to render an axis outside that range if you are using the appropriate attribute (i.e., `font-weight` or `font-stretch`), but will not block you from supplying an invalid value via `font-variation-settings`, so use with care.

[Working with older browsers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts#working_with_older_browsers)

----------------------------------------------------------------------------------------------------------------------------------------

Variable font support can be checked with CSS Feature Queries (see [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
), so it's possible to use variable fonts in production and scope the CSS calling the variable fonts inside a feature query block.

[Sample pages](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts#sample_pages)

----------------------------------------------------------------------------------------------------------

The following example pages show two different ways to structure your CSS. The first uses the standard attributes wherever possible. The second example uses CSS Custom Properties to set values for a `font-variation-settings` string and shows how you can more easily update single variable values by overriding a single variable rather than rewriting the whole string. Note the hover effect on the `h2`, which only alters the grade axis custom property value. Click "Play" in the code blocks below to edit the example in the MDN Playground:

    <div class="container container1">
      <h1>Moby-Dick</h1>
      <h2>CHAPTER 1. Loomings.</h2>
      <p>
        Call me Ishmael. Some years ago—never mind how long precisely–having little
        or no money in my purse, and nothing particular to interest me on shore, I
        thought I would sail about a little and see the watery part of the world. It
        is a way I have of driving off the spleen and regulating the circulation.
        Whenever I find myself growing grim about the mouth; whenever it is a damp,
        drizzly November in my soul; whenever I find myself involuntarily pausing
        before coffin warehouses, and bringing up the rear of every funeral I meet;
        and especially whenever my hypos get such an upper hand of me, that it
        requires a strong moral principle to prevent me from deliberately stepping
        into the street, and methodically knocking people's hats off then, I account
        it high time to get to sea as soon as I can.
      </p>
    </div>
    <hr />
    <div class="container container2 demo2">
      <h1>Moby-Dick</h1>
      <h2>CHAPTER 1. (hover here)</h2>
      <p>
        Call me Ishmael. Some years ago—never mind how long precisely–having little
        or no money in my purse, and nothing particular to interest me on shore, I
        thought I would sail about a little and see the watery part of the world. It
        is a way I have of driving off the spleen and regulating the circulation.
        Whenever I find myself growing grim about the mouth; whenever it is a damp,
        drizzly November in my soul; whenever I find myself involuntarily pausing
        before coffin warehouses, and bringing up the rear of every funeral I meet;
        and especially whenever my hypos get such an upper hand of me, that it
        requires a strong moral principle to prevent me from deliberately stepping
        into the street, and methodically knocking people's hats off then, I account
        it high time to get to sea as soon as I can.
      </p>
    </div>
    

    @font-face {
      font-family: "Amstelvar VF";
      src: url("https://mdn.github.io/shared-assets/fonts/variable-fonts/AmstelvarAlpha-VF.woff2")
        format("woff2-variations");
      font-weight: 300 900;
      font-stretch: 75% 150%;
      font-style: normal;
      font-display: swap;
    }
    
    body {
      font:
        1.2em "Amstelvar VF",
        "Georgia",
        serif;
      margin: 20px;
      padding: 0;
    }
    
    .container * {
      margin: 0.5rem auto 1rem;
      max-width: 42rem;
    }
    

css

    .container1 h1 {
      font-optical-sizing: auto;
      font-size: 5rem;
      font-stretch: 85%;
      font-weight: 450;
    }
    .container1 h2 {
      font-optical-sizing: auto;
      font-size: 2.25rem;
      font-stretch: 90%;
      font-weight: 575;
    }
    .container1 p {
      font-optical-sizing: auto;
      font-size: 1rem;
      font-stretch: 100%;
      font-weight: 375;
    }
    .demo2 {
      --text-wght: 375;
      --text-wdth: 100;
      --text-opsz: 16;
      --text-GRAD: 88;
    }
    .container2 > * {
      font-size: 5rem;
      font-variation-settings:
        "wght" var(--text-wght),
        "wdth" var(--text-wdth),
        "opsz" var(--text-opsz),
        "GRAD" var(--text-GRAD);
    }
    .container2 h1 {
      --text-wght: 450;
      --text-wdth: 85;
      --text-opsz: 80;
      font-size: 5rem;
    }
    .container2 h2 {
      --text-wght: 575;
      --text-wdth: 95;
      --text-opsz: 36;
      font-size: 2.25rem;
    }
    .container2 h2:hover {
      --text-GRAD: 130;
    }
    .container2 p {
      font-size: 1rem;
    }
    

[Resources](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts#resources)

----------------------------------------------------------------------------------------------------

*   [W3C CSS Fonts Module 4 Specification](https://drafts.csswg.org/css-fonts-4/ "External link (opens in new tab)")
     (editor's draft)
*   [W3C GitHub issue queue](https://github.com/w3c/csswg-drafts/issues "External link (opens in new tab)")
    
*   [Microsoft Open Type Variations introduction](https://learn.microsoft.com/en-us/typography/opentype/spec/otvaroverview "External link (opens in new tab)")
    
*   [Microsoft OpenType Design-Variation Axis Tag Registry](https://learn.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg "External link (opens in new tab)")
    
*   [Wakamai Fondue](https://wakamaifondue.com/ "External link (opens in new tab)")
     (a site that will tell you what your font can do via a drag-and-drop inspection interface)
*   [Axis Praxis](https://www.axis-praxis.org/ "External link (opens in new tab)")
     (the original variable fonts playground site)
*   [V-Fonts.com](https://v-fonts.com/ "External link (opens in new tab)")
     (a catalog of variable fonts and where to get them)
*   [Font Playground](https://play.typedetail.com/ "External link (opens in new tab)")
     (another playground for variable fonts with some very unique approaches to user interface)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Feb 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/fonts/variable_fonts/index.md?plain=1 "Folder: en-us/web/css/guides/fonts/variable_fonts (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FFonts%2FVariable_fonts&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Ffonts%2Fvariable_fonts%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FFonts%2FVariable_fonts%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Ffonts%2Fvariable_fonts%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3c91c067a4d36b532a4bce72e5d8a2c5a9279db5%0A*+Document+last+modified%3A+2026-02-27T15%3A24%3A40.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")