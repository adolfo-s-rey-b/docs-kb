*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name#mdn-search)
    

`view-transition-name` CSS property
===================================

Baseline 2025

Newly available

Since October 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`view-transition-name`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the [view transition](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)
 snapshot that selected elements will participate in. This enables you to animate those elements separately from the rest of the page, which uses the default cross-fade animation during a view transition. You can then define custom animation styles for these elements.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name#syntax)

------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name#values)

[`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)

An identifying name that causes the selected element to participate in a separate snapshot from the root snapshot. The `<custom-ident>` cannot be `auto`, `match-element`, `none`, or a [CSS-wide keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#css-wide_keywords)
 value.

[`match-element`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name#match-element)

The browser automatically assigns a unique name to the selected element. This name is used to snapshot the element separately from all other elements on the page. (This name is internal and cannot be read from the DOM.)

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name#none)

The selected element will not participate in a separate snapshot, unless it has a parent element with a `view-transition-name` set, in which case it will be snapshotted as part of that element.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name#description)

----------------------------------------------------------------------------------------------------------------------

By default, when a view transition is applied to a web app, all changes to the UI that occur during that transition are snapshotted and animated together. This is the default — or `root` — snapshot (see [The view transition pseudo-element tree](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using#the_view_transition_pseudo-element_tree)
). By default, this animation is a smooth cross-fade, which can be seen in action in the [View Transitions SPA demo](https://mdn.github.io/dom-examples/view-transitions/spa/ "External link (opens in new tab)")
.

If you want certain elements to be animated differently from the `root` snapshot during the view transition, you can do so by giving them a different `view-transition-name`, for example:

You can then specify which animations you want for the before and after snapshots using the relevant view transition pseudo-elements — [`::view-transition-old()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old)
 and [`::view-transition-new()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-new)
. For example:

If you don't want an element to be snapshotted separately, you can specify a `view-transition-name` value of `none`:

The `view-transition-name` `<custom-ident>` must be unique for each rendered element taking part in the view transition. If two rendered elements have the same `view-transition-name` at the same time, the [`ViewTransition.ready`](https://developer.mozilla.org/en-US/docs/Web/API/ViewTransition/ready)
 [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 will reject and the transition will be skipped.

### [Specifying `view-transition-name` values automatically](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name#specifying_view-transition-name_values_automatically)

Sometimes you will want to animate multiple UI elements separately in a view transition. This is often the case when you have a list of elements on a page and want to rearrange them in some way:

Giving each one a unique name can be inconvenient, especially as the number of elements gets larger:

To get around this problem, you can use the `match-element` value, which causes the browser to give each selected element a unique internal `view-transition-name`:

Because `match-element` assigns automatic `view-transition-name` values based on element identity, it can only be used for same-document view transitions. The auto-generated internal identifiers are not transferrable across different elements or documents.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name#formal_definition)

----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------

view-transition-name =   
  none            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name#examples)

----------------------------------------------------------------------------------------------------------------

### [Basic `view-transition-name` usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name#basic_view-transition-name_usage)

This example comes from the [View Transitions SPA demo](https://mdn.github.io/dom-examples/view-transitions/spa/ "External link (opens in new tab)")
, which is a basic image gallery. The [Basic SPA view transition](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using#basic_spa_view_transition)
 provides a more detailed explanation of how this demo works.

Most of the UI changes are animated using the `root` transition snapshot. However, the `<figcaption>` is given a `view-transition-name` of `figure-caption` to allow it to be animated differently from the rest of the page:

The following code applies a custom animation just to the `<figcaption>`:

We create a custom CSS animation and apply it to the `::view-transition-old(figure-caption)` and `::view-transition-new(figure-caption)` pseudo-elements. We also apply other styles to keep them both in the same place and to stop the default styling from interfering with our custom animations.

### [Using the `match-element` value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name#using_the_match-element_value)

This example contains a list of technologies–HTML, CSS, SVG, and JS–that are displayed in a sidebar next to a main content area, which starts out empty. Clicking a technology's heading animates its content into the adjoining content area that shows more details.

#### HTML

The [`<main>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main)
 element contains an [unordered list](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
 and an [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
 element. The multiple child [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 elements inside the list each contain an [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 element inside a [heading](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
.

#### CSS

We use [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
 to lay out the `<li>` and the `<article>` side by side, and to make the list items share equal amount of space in the first column. The list takes up 35% of the container's width, while the `<article>` fills the remaining available horizontal space.

We also define a rule that selects elements with the `active-item` class. When this class is applied to an element, the rule causes it to be positioned exactly over the top of the `<article>` element. This class will be applied to the list items via JavaScript when their links are clicked, which will initiate a view transition.

By default, all elements in a view transition are animated together in a single cross-fade. In this example, however, we don't want this — we want each list item to have its own movement animation. We can achieve this by applying `view-transition-name: match-element` to every list item:

The `match-element-applied` class is applied to the `<main>` element by default, which is why the checkbox in the Result frame is initially selected. If you uncheck it, the class is removed and the default cross-fade animation comes into effect instead. You can toggle the checkbox to compare the default animation with the one applied when `view-transition-name: match-element` is used.

Next, we customize the animation by using the [`::view-transition-group()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group)
 pseudo-element to apply an [`animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
 to all the view transition groups (signified by the `*` identifier) and give all the old and new snapshots a [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 of `100%`. This works around differences in the aspect ratios of the old and new snapshots and makes the animations look smoother:

#### JavaScript

In this example, the `active-item` class is applied to the list items when their links are clicked; this is achieved via the `updateActiveItem()` function:

Running the `updateActiveItem()` function via the `startViewTransition()` function animates the display of technology details smoothly.

#### Result

Click a technology heading in the sidebar and notice the animation effect of its content into the main content area.

There is also a checkbox, which is selected by default, so `view-transition-name: match-element` is applied. Uncheck the checkbox and click a heading again to see how the view-transition works without `view-transition-name: match-element`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS View Transitions Module Level 1  <br>\# view-transition-name-prop](https://drafts.csswg.org/css-view-transitions/#view-transition-name-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name#see_also)

----------------------------------------------------------------------------------------------------------------

*   [`view-transition-class`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class)
    
*   [`::view-transition-group()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group)
    
*   [`::view-transition-old()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old)
    
*   [`::view-transition-new()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-new)
    
*   [View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)
    
*   [Smooth transitions with the View Transition API](https://developer.chrome.com/docs/web-platform/view-transitions/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/view-transition-name/index.md?plain=1 "Folder: en-us/web/css/reference/properties/view-transition-name (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fview-transition-name&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fview-transition-name%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fview-transition-name%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fview-transition-name%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")