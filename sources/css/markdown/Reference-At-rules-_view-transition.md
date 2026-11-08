*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition#mdn-search)
    

`@view-transition` CSS at-rule
==============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/248)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`@view-transition`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 is used to opt in the current and destination documents to undergo a [view transition](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)
, in the case of a cross-document navigation.

For a cross-document view transition to work, the current and destination documents of the navigation need to be on the same origin.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition#syntax)

------------------------------------------------------------------------------------------------------

css

    @view-transition {
      navigation: auto | none;
      types: none | <custom-ident>#;
    }
    

### [Descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition#descriptors)

[`navigation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition#navigation)

A keyword specifying the effect this at-rule will have on the document's view transition behavior. Possible values are:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition#auto)

The document will undergo a view transition when taking part in a navigation, provided the navigation is [same-origin](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy)
, without cross-origin redirects, and its [`navigationType`](https://developer.mozilla.org/en-US/docs/Web/API/NavigateEvent/navigationType "navigationType")
 is `traverse`, `push`, or `replace`. In the case of `push` or `replace`, the navigation must be initiated by a user interacting with the page content, not by a browser UI feature.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition#none)

The document will not undergo a view transition.

[`types`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition#types)

Specifies the view transition [types](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using_types)
 to set on the active view transition for the current and destination documents. Possible values are:

[`<custom-ident>+`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition#custom-ident)

One or more space-separated [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 values representing the types to set.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition#none_2)

No types are set.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

@view-transition =   
  @view-transition { <declaration-list> }    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition#examples)

----------------------------------------------------------------------------------------------------------

### [Transitioning page view](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition#transitioning_page_view)

The following code snippets show key concepts used in a page transition demo. The demo uses cross-document view-transitions; a half second transition that occurs when navigating between two pages of a site. For the full demo, see the [View transitions multi-page app demo](https://mdn.github.io/dom-examples/view-transitions/mpa/ "External link (opens in new tab)")
.

The `@view-transition` at-rule is specified in the CSS for both your current and destination documents of a navigation to opt them both in to the view transition:

css

    @view-transition {
      navigation: auto;
    }
    

In addition to the `@view-transition` at-rule, we use the [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 at-rule to define two keyframe animations and use the [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 shorthand property to apply those keyframe animations to the elements in the outbound ([`::view-transition-old()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old)
) and inbound ([`::view-transition-new()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-new)
) pages that we want to animate.

css

    /* Create a custom animation */
    @keyframes move-out {
      from {
        transform: translateY(0%);
      }
    
      to {
        transform: translateY(-100%);
      }
    }
    
    @keyframes move-in {
      from {
        transform: translateY(100%);
      }
    
      to {
        transform: translateY(0%);
      }
    }
    
    /* Apply the custom animation to the old and new page states */
    ::view-transition-old(root) {
      animation: 0.4s ease-in both move-out;
    }
    
    ::view-transition-new(root) {
      animation: 0.4s ease-in both move-in;
    }
    

See this [transitions multi-page app](https://mdn.github.io/dom-examples/view-transitions/mpa/ "External link (opens in new tab)")
 demo live.

### [Using view transition types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition#using_view_transition_types)

Our [MPA transition types example](https://mdn.github.io/dom-examples/view-transitions/mpa-chapter-nav-transition-types/ "External link (opens in new tab)")
 ([source code](https://github.com/mdn/dom-examples/tree/main/view-transitions/mpa-chapter-nav-transition-types "External link (opens in new tab)")
) demonstrates how to use `types` via `@view-transition`:

css

    @view-transition {
      navigation: auto;
      types: slide;
    }
    

See [Using types with cross-document view transitions via `@view-transition`](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using_types#using_types_with_cross-document_view_transitions_via_view-transition)
 for a walkthrough of the referenced example.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS View Transitions Module Level 2  <br>\# view-transition-rule](https://drafts.csswg.org/css-view-transitions-2/#view-transition-rule) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition#see_also)

----------------------------------------------------------------------------------------------------------

*   [`::view-transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition)
    
*   [`::view-transition-new()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-new)
    
*   [`::view-transition-old()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old)
    
*   [`::view-transition-group()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group)
    
*   [`::view-transition-image-pair()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair)
    
*   [View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)
    
*   [Using view transition types](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using_types)
    
*   [CSS at-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
    
*   [CSS at-rule functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/At-rule_functions)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@view-transition/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@view-transition (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40view-transition&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40view-transition%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40view-transition%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40view-transition%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe328268bb418551ab451881845881b5837c9da83%0A*+Document+last+modified%3A+2026-04-20T16%3A14%3A00.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")