*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope#mdn-search)
    

`timeline-scope` CSS property
=============================

Baseline 2026

Newly available

\*

Since October 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`timeline-scope`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property modifies the scope of a named animation timeline.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope#syntax)

------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    timeline-scope: all;
    timeline-scope: none;
    
    /* Custom name values */
    timeline-scope: --custom_name_for_timeline;
    timeline-scope: --timeline_name_one, --timeline_name_two;
    
    /* Global values */
    timeline-scope: inherit;
    timeline-scope: initial;
    timeline-scope: revert;
    timeline-scope: revert-layer;
    timeline-scope: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope#values)

This property is specified as a keyword or a comma-separated list of custom timeline names:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope#none)

Applies no change to the timeline scope. This is the default.

[`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope#all)

Sets the scope so that any timeline names set on the element or in its subtree are matched only by elements within the same subtree.

[`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope#dashed-ident)

Specifies one or more comma-separated timeline names that are declared using [`scroll-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name)
 or [`view-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)
. Sets the scope so that when the specified `scroll-timeline-name` or `view-timeline-name` values are set on the element or in its subtree, they are matched only by elements within the same subtree.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope#description)

----------------------------------------------------------------------------------------------------------------

The `timeline-scope` property modifies the scope of a named animation timeline. By default, a [named timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#animation_timelines)
 (i.e., declared using [`scroll-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name)
 or [`view-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)
) can only be set as the controlling timeline of a direct descendant element (i.e., by setting [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
 on it with the timeline name as its value). This is the default "scope" for the timeline.

The value of the `timeline-scope` is the name of a timeline defined on a descendant element; this changes the scope of the timeline to include the targeted element and its descendants. In other words, that element on which the `timeline-scope` property is defined, and all of its descendant elements, can be controlled using that timeline.

If no timeline (or more than one timeline) exists with the name given for the `timeline-scope` value, an inactive timeline with the specified name is created. The `timeline-scope` property only works with named timelines, and therefore cannot be used in conjunction with anonymous timelines created using the [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
 or [`scroll()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll)
 animation timeline functions.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | `none` or an ordered list of identifiers |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

timeline-scope =   
  none             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  all              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope#examples)

----------------------------------------------------------------------------------------------------------

In this example, we animated an element in response to the scrolling of another element by increasing the timeline scope with the `timeline-scope` property.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope#html)

The HTML includes an element to animate and an element to scroll:

html

    <div class="content">
      <div class="box animation"></div>
    </div>
    
    <div class="scroller">
      <div class="long-element"></div>
    </div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope#css)

A scroll timeline named `--my-scroller` is defined using the [`scroll-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name)
 property on a scrolling element. This scroll timeline name is used in two other places: it is applied as the [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
 on the element we want to animate, and as `timeline-scope` on an ancestor of both the scroller and the animated element, increasing the scope.

We set the `<body>`'s height to `100vh`, and lay its two child elements out as two equal columns using flexbox. To increase the timeline scope from the `<div class="scroller">` element to the whole `<body>`, we set `timeline-scope: --my-scroller` on it. By doing so, the `--my-scroller` timeline can be set as the controlling timeline for an animation set on the `<body>` or any element nested inside it.

css

    body {
      margin: 0;
      height: 100vh;
      display: flex;
    
      timeline-scope: --my-scroller;
    }
    
    .content,
    .scroller {
      flex: 1;
    }
    

We set `--my-scroller` as the [`scroll-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name)
 on the scrolling element that should provide the scroll progress timeline for our animated element. We add [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 to enable scrolling, adding a background color to make its boundary visible. We set a large [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 on the contents of our scrolling element so the element actually scrolls.

css

    .scroller {
      overflow: scroll;
      scroll-timeline-name: --my-scroller;
      background: deeppink;
    }
    
    .long-element {
      height: 2000px;
    }
    

Next, we give the animated element some rudimentary styles and apply an animation to it using the [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 shorthand property. We set the [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
 to the named scroll timeline: `--my-scroller`. To reiterate, animating the element based on the scroll progress of its cousin element is only possible because we set `timeline-scope` on a mutual ancestor; the animated element is **not** a descendant of the scrolling element.

css

    .box {
      width: 100px;
      height: 100px;
      border-radius: 10px;
      background-color: rebeccapurple;
    }
    
    .animation {
      animation: rotate-appear 1ms linear;
      animation-timeline: --my-scroller;
    }
    
    @keyframes rotate-appear {
      from {
        rotate: 0deg;
        translate: 0;
      }
    
      to {
        rotate: 720deg;
        translate: 100%;
      }
    }
    

    @layer supports {
      @supports not (timeline-scope: none) {
        body::before {
          content: "Your browser does not support the 'timeline-scope' property.";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem;
        }
      }
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope#result)

Scroll the vertical bar on the pink area to see the square animate.

The key point to note here is that the animated element is not a descendant of the scrolling element — to make this work, we increase the scope of the `--my-scroller` timeline by setting `timeline-scope: --my-scroller` on the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scroll-driven Animations  <br>\# propdef-timeline-scope](https://drafts.csswg.org/scroll-animations/#propdef-timeline-scope) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope#see_also)

----------------------------------------------------------------------------------------------------------

*   [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
    
*   [`scroll-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline)
    , [`scroll-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name)
    
*   [`view-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline)
    , [`view-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)
    
*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/timeline-scope/index.md?plain=1 "Folder: en-us/web/css/reference/properties/timeline-scope (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftimeline-scope&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftimeline-scope%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftimeline-scope%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftimeline-scope%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2a3061b6905ba8a8fe2654e1a6a978bc614bfd66%0A*+Document+last+modified%3A+2026-09-14T15%3A38%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")