*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API/Houdini#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API/Houdini#mdn-search)
    

CSS Houdini
===========

**CSS Houdini** is a set of APIs that expose parts of the CSS engine, enabling developers to create CSS extensions. These extensions might polyfill features that are not yet available in browsers, experiment with new layout techniques, or add creative borders and other effects.

While many Houdini examples showcase the creative possibilities of the APIs, there are many practical use cases. For example, you can use Houdini to create advanced custom properties with type checking and default values.

[Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API/Houdini#basic_example)

-------------------------------------------------------------------------------------------------------------------------

A regular [CSS custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
 consists of a property name and a value. Therefore I might create a custom property called `--background-color` and expect it to be given a color value. The value is then used in the CSS as if it were the color value.

In the above example however, there is nothing to stop someone using some other value for this property, perhaps setting it to a length. Having done so, anywhere that the property is used would have no background color as `background-color: 12px` is not valid. When browsers come across CSS they don't recognize as valid they throw that line away.

Using [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
 however, we can declare the custom property with a [`syntax`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax)
 of `<color>`. This shows that we need this property to have a value which is a valid color.

[Houdini worklets](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API/Houdini#houdini_worklets)

-------------------------------------------------------------------------------------------------------------------------------

A feature of Houdini is the [`Worklet`](https://developer.mozilla.org/en-US/docs/Web/API/Worklet)
. A worklet is a module, written in JavaScript, that extends CSS using one of the Houdini APIs. You can see an example worklet on the [`PaintWorkletGlobalScope.registerPaint()`](https://developer.mozilla.org/en-US/docs/Web/API/PaintWorkletGlobalScope/registerPaint)
 page. Once a worklet has been registered you can use it in CSS just like any other value. This means that even if you are not a JavaScript developer, you can access Houdini APIs by using worklets other people have created.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API/Houdini#reference)

-----------------------------------------------------------------------------------------------------------------

### [CSS at-rule and descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API/Houdini#css_at-rule_and_descriptors)

The [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
 at-rule allows you to register an advanced custom property.

*   [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
    
*   [`inherits`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits)
    
*   [`initial-value`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value)
    
*   [`syntax`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax)
    

### [Houdini API references](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API/Houdini#houdini_api_references)

*   [CSS Properties and Values API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Properties_and_Values_API)
    
*   [CSS Typed Object Model API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Typed_OM_API)
    
*   [CSS Painting API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Painting_API)
    
*   [`Worklet`](https://developer.mozilla.org/en-US/docs/Web/API/Worklet)
     reference

### [Houdini guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API/Houdini#houdini_guides)

*   [Properties and Values API Guide](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Properties_and_Values_API/guide)
    
*   [Typed OM API Guide](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Typed_OM_API/Guide)
    
*   [Using the CSS Painting API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Painting_API/Guide)
    

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API/Houdini#see_also)

---------------------------------------------------------------------------------------------------------------

*   [A Practical Overview of CSS Houdini](https://www.smashingmagazine.com/2020/03/practical-overview-css-houdini/ "External link (opens in new tab)")
    
*   [Smarter custom properties with Houdini's new API](https://web.dev/articles/css-props-and-vals "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 15, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API/Houdini/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/properties_and_values_api/houdini/index.md?plain=1 "Folder: en-us/web/css/guides/properties_and_values_api/houdini (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FProperties_and_values_API%2FHoudini&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fproperties_and_values_api%2Fhoudini%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FProperties_and_values_API%2FHoudini%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fproperties_and_values_api%2Fhoudini%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F32bdfdb82cf91ce9942b694286dec62be2cc20aa%0A*+Document+last+modified%3A+2025-12-15T12%3A04%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")