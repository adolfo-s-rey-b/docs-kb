*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using_for_accessibility#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using_for_accessibility#mdn-search)
    

Using media queries for accessibility
=====================================

[**CSS media queries**](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
 can be used to help users with disabilities better experience your website.

[Reduced Motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using_for_accessibility#reduced_motion)

-------------------------------------------------------------------------------------------------------------------------------

Blinking and flashing animation can be problematic for people with cognitive concerns such as Attention Deficit Hyperactivity Disorder (ADHD). Additionally, certain kinds of motion can be a trigger for Vestibular disorders, epilepsy, and migraine and Scotopic sensitivity. Reducing animations or switching animation off completely based on the user's preference can also benefit users with low battery or low-end devices.

The [`prefers-reduced-motion`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion)
 media query enables providing an experience with fewer animations and transitions to users who have set their operating system's accessibility preferences to reduce motion. It has two possible values:

[`no-preference`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using_for_accessibility#no-preference)

Indicates that the user has made no preference known to the system.

[`reduce`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using_for_accessibility#reduce)

Indicates that user has notified the system that they prefer an interface that minimizes the amount of movement or animation, preferably to the point where all non-essential movement is removed.

### [Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using_for_accessibility#example)

This example has an annoying animation unless you turn on Reduce Motion in [your accessibility preferences](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Browsing_safely)
.

#### HTML

html

    <div class="animation">animated box</div>
    

#### CSS

css

    .animation {
      animation: vibrate 0.3s linear infinite both;
    }
    
    @media (prefers-reduced-motion: reduce) {
      .animation {
        animation: none;
      }
    }
    

The value of `prefers-reduced-motion` is `reduce`, not "none". This preference does not mean all animations must be removed, which could be achieved with `* {animation: none !important;}`. Rather, users expect motion animation, including those triggered by user interaction, to be disabled unless the animation is essential to the functionality or the information being conveyed (see [WCAG: Animation from Interactions](https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions.html "External link (opens in new tab)")
).

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using_for_accessibility#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [`prefers-contrast`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-contrast)
    : to adjust page styles based on user's contrast preference
*   [`prefers-reduced-transparency`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-transparency)
    
*   [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)
    
*   [`inverted-colors`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/inverted-colors)
    
*   [Designing With Reduced Motion For Motion Sensitivities](https://www.smashingmagazine.com/2020/09/design-reduced-motion-sensitivities/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using_for_accessibility/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/media_queries/using_for_accessibility/index.md?plain=1 "Folder: en-us/web/css/guides/media_queries/using_for_accessibility (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMedia_queries%2FUsing_for_accessibility&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fmedia_queries%2Fusing_for_accessibility%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMedia_queries%2FUsing_for_accessibility%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fmedia_queries%2Fusing_for_accessibility%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")