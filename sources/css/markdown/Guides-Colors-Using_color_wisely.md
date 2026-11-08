*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_color_wisely#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_color_wisely#mdn-search)
    

Using color wisely
==================

Choosing the right colors for a website can be tricky, especially if you aren't well-grounded in art, design, or at least basic color theory. The wrong color choice can render your site unattractive, or worse, leave the content unreadable due to problems with contrast or conflicting colors. Using the wrong colors can result in your content being outright unusable by people with certain vision problems, particularly color blindness.

[Finding the right colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_color_wisely#finding_the_right_colors)

---------------------------------------------------------------------------------------------------------------------------------------

There are tools and processes available to help you pick a good color scheme. While they can't replace having a good designer helping you make these decisions, they can get you started.

### [Base color](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_color_wisely#base_color)

The first step is to choose your **base color**. This color represents your website or its subject matter. Just as we associate green with the beverage [Mountain Dew](https://en.wikipedia.org/wiki/Mountain_Dew "External link (opens in new tab)")
 blue with the sky or the ocean, choosing an appropriate base color to represent your site is a good place to start. There are plenty of ways to select a base color; a few ideas include:

*   A color that is naturally associated with the topic of your content, such as the existing color identified with a product or idea or a color representative of the emotion you wish to convey.
*   A color that comes from imagery associated with your subject matter. If you're creating a website about a given item or product, choose a color that's physically present on that item.
*   Browse websites that let you look at lots of existing color palettes and images to find inspiration.

Several useful browser extensions can help pick base colors. For example, the [ColorZilla](https://www.colorzilla.com/ "External link (opens in new tab)")
 browser extension provides an eyedropper tool for picking colors from any webpage. It can also take averages of the colors of an area of a page.

An "average color" grab is useful because sometimes what may look like a solid block of color might actually be multiple related colors, such as grabbing the blue in a photograph of an ocean or the sky. A single pixel of blue selected from a photo may result in a color that looks out of place.

### [Fleshing out the palette](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_color_wisely#fleshing_out_the_palette)

Once you have decided on your base color, the next step is to build a palette of appropriate colors to use alongside it. Several tools are available to apply color theory to your base color and output appropriate added colors. Online tools, like the free [Adobe Color CC online color wheel](https://color.adobe.com/create/color-wheel "External link (opens in new tab)")
 can help you pick an accessible color palette.

Many of these tools can also apply filters to your palette so you can see what they look like to people with various forms of color blindness. See [Color and accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_color_wisely#color_and_accessibility)
 for a brief explanation of why this matters.

When designing your palette, you'll probably also need to supplement it with some core neutral colors such as white (or nearly white), black (or nearly black), and one or more shades of gray.

**Note:** Usually, you are better off using the smallest number of colors possible. Using color to highlight important content rather than adding color to everything will have more impact and your content will be more readable.

[Color theory resources](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_color_wisely#color_theory_resources)

-----------------------------------------------------------------------------------------------------------------------------------

A full review of color theory is beyond the scope of this article, however, there are plenty of articles about color theory available. We found the following resources particularly useful:

[Color Science](https://www.khanacademy.org/computing/pixar/color "External link (opens in new tab)")
 ([Khan Academy](https://www.khanacademy.org/ "External link (opens in new tab)")
 in association with [Pixar](https://www.pixar.com/ "External link (opens in new tab)")
)

An online course that introduces concepts such as what color is, how it's perceived, and how to use colors to express ideas. Presented by Pixar artists and designers.

[Color theory](https://en.wikipedia.org/wiki/Color_theory "External link (opens in new tab)")
 on Wikipedia

Wikipedia's entry on color theory has great information from a technical perspective. It likely won't help your color selection process, but is still full of useful information.

[Color and accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_color_wisely#color_and_accessibility)

-------------------------------------------------------------------------------------------------------------------------------------

Make sure your content is [accessible](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
. There are several ways color can create an [accessibility](https://developer.mozilla.org/en-US/docs/Glossary/Accessibility)
 problem. Improper or careless use of color can result in a website or app that a percentage of your target audience may not be able to use adequately, resulting in lost traffic, lost business, and possibly even a public relations problem or a lawsuit. So it's important to consider your use of color carefully.

It's important to [understand color and luminance](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Colors_and_Luminance)
 and to always consider [color blindness](https://medlineplus.gov/colorblindness.html "External link (opens in new tab)")
 and [vestibular disorders](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Seizure_disorders)
. There are several kinds; the most common is red-green color blindness, which causes people to be unable to differentiate between the colors red and green. There are others, too, ranging from an inability to tell the difference between certain colors to the total inability to see color at all. There are even color and animation combinations that can lead your photosensitive users to experience [seizures](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Seizure_disorders#colors)
.

While higher [color contrast](https://digital.gov/guides/accessibility-for-teams/visual-design/#color-and-contrast "External link (opens in new tab)")
 is often a good thing when it comes to accessibility, when animating, especially rapidly, [reducing color contrast](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Seizure_disorders#reduce_contrast)
 on animating elements reduces seizure risk. If you include animations, use the [`prefers-reduced-motion`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion)
 [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
 query feature to reduce animations for users who have selected that preference.

That said, ensure you have enough [color contrast](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable/Color_contrast)
 between your background and foreground content to ensure legibility. Also, never use color as the only way to convey information. If, for example, you indicate the success of an operation with a green border around the associated UI element, and failure with a red border, users with red-green color blindness won't be able to use your site properly. Instead, use text and color indicators together to include those users. For example, a green check mark and a red cross mark would be better.

[Palette design example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_color_wisely#palette_design_example)

-----------------------------------------------------------------------------------------------------------------------------------

In this example, we will create an appropriate color palette for a website for a game that takes place on the planet Mars. A [Google search for photos of Mars](https://www.google.com/search?q=Mars&tbm=isch "External link (opens in new tab)")
 will output several color photos.

Use a color picker tool to select a color sample for the base color. For this example, we've selected `#D79C7A`, which is a rusty orange-red color. We can use [Paletton](https://www.paletton.com/ "External link (opens in new tab)")
 to come up with the other colors for our palette. Upon opening Paletton, we see:

![Right after loading Paletton.](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_color_wisely/paletton1.png)

Next, we enter our color's hex code (`D79C7A`) into the "Base RGB" box at the bottom-left corner of the tool:

![After entering base color](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_color_wisely/paletton2.png)

We now see a monochromatic palette based on the color we picked from the Mars photo. If you need related colors, these are likely good options. To find an accent color that pop alongside the base color, we click the "add complementary" toggle underneath the menu that lets you select the palette type. The default was "Monochromatic". Paletton computes an appropriate accent color; clicking on the accent color in the bottom-right corner tells us that this color is `#508D7C`.

![Now with complementary colors included.](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_color_wisely/paletton3.png)

If the proposed color doesn't work for your needs, you can change the color scheme. For example, if the proposed greenish-blue color doesn't work, select the Triad color scheme icon, which results in the following:

![Triad color scheme selected](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_color_wisely/paletton4.png)

Click on the grayish blue in the top-right. The color is `#556E8D`. This can be used as an accent color to make things stand out, such as for headlines, tabs highlights, or other indicators on the site:

![Triad color scheme selected](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_color_wisely/paletton-color-detail.png)

Now we have our base color and our accent. We also have a few complementary shades of both, which can be used to create gradients or as an accent color to indicate focus, such as for link hover states. The colors can be exported in several formats for you to use.

You should also select neutral colors. Find a color that provides enough contrast for your text to be crisp and readable while ensuring it isn't harsh for the eyes. If the contrast is too low, your text will be washed out by the background, leaving it unreadable, but if your contrast is too high, the user may find your site garish and unpleasant to look at.

[Color, backgrounds, contrast, and printing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_color_wisely#color_backgrounds_contrast_and_printing)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Your site may look very different when printed from what the user sees on their screen. When printing your page, the user may select to print in black and white only. Most browsers, by default, remove background colors and images when printing documents.

What matters most is usually the text itself, but if your background colors and images have been selected carefully and/or are crucial to the usefulness of the content, you can use the CSS [`print-color-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust)
 property to tell the browser that it should not make adjustments to the appearance of content.

The default value of `print-color-adjust: economy`, indicates that the browser is allowed to make appearance changes as it deems necessary to try to optimize the legibility and/or print economy of the content, given the type of output device the document is being drawn onto.

You can set `print-color-adjust: exact` to tell the browser that the element or elements on which you use it have been designed specifically to best work with the colors and images left as they are. With this set, the browser won't tamper with the appearance of the element on which this value is applied, and will draw it as indicated by your CSS.

**Note:** There is no guarantee, though, that `print-color-adjust: exact` will result in your CSS being used exactly as given. If the browser provides user preferences to change the output (such as a "don't print backgrounds" checkbox in a print dialog box), that overrides the value of `print-color-adjust`.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_color_wisely#see_also)

-------------------------------------------------------------------------------------------------------

*   [CSS colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors)
     module
*   [Applying color to HTML elements using CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color)
    
*   [CSS color values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Color_values)
    
*   [Using relative colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors)
    
*   [Understanding color and luminance](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Colors_and_Luminance)
    
*   [WCAG 1.4.1: Color contrast](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable/Color_contrast)
    
*   [Paletton](https://paletton.com/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_color_wisely/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/colors/using_color_wisely/index.md?plain=1 "Folder: en-us/web/css/guides/colors/using_color_wisely (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FColors%2FUsing_color_wisely&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fcolors%2Fusing_color_wisely%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FColors%2FUsing_color_wisely%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fcolors%2Fusing_color_wisely%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd19dec85109590176f946fcceef48c787d578b1e%0A*+Document+last+modified%3A+2026-08-27T15%3A03%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")