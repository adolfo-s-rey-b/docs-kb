*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope#mdn-search)
    

trigger-scope CSS property
==========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/961)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope#browser_compatibility)
 carefully before using this in production.

The **`trigger-scope`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property can be used to limit the scope of a [scroll-triggered animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)
 trigger name to a document subtree.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope#syntax)

-----------------------------------------------------------------------------------------------------

css

    /* Keywords */
    trigger-scope: none;
    trigger-scope: all;
    
    /* <dashed-ident> */
    trigger-scope: --my-trigger;
    
    /* Multiple values */
    trigger-scope: --my-trigger, --another-trigger;
    
    /* Global values */
    trigger-scope: inherit;
    trigger-scope: initial;
    trigger-scope: revert;
    trigger-scope: revert-layer;
    trigger-scope: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope#values)

Specified as `none`, `all`, or a comma-separated list of [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
 values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope#none)

Specifies that no trigger scoping is set. This is the default value.

[`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope#all)

Sets the scope so that _any_ `timeline-trigger-name` values set in the subtree can only be associated with animated elements in the same subtree.

[`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)

A trigger name. Sets the scope so that the specified `timeline-trigger-name` values, when set in the subtree, can only be associated with animated elements in the same subtree.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope#description)

---------------------------------------------------------------------------------------------------------------

The `trigger-scope` property is used to limit trigger scope to specific element subtrees in [scroll-triggered animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)
.

Trigger names, defined with the [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
 property, are global by default. When an animated element is associated with a trigger name via its [`animation-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger)
 property, the browser determines what its trigger element is as follows:

1.  It walks up the animated element's ancestor tree until it finds an ancestor with a `timeline-trigger-name` set that is the same as the name referenced in its `animation-trigger` property value. If the animated element is also the trigger, it will be found instantly.
2.  If it can't find a suitable ancestor trigger, it will use the _last_ element in the HTML source order with that `timeline-trigger-name` value.
3.  If it can't find an element anywhere in the DOM with that `timeline-trigger-name` value, the animated element won't be scroll-triggered; having no associated timeline, the animation will not happen.

If multiple elements define triggers with the same trigger name, only the last one in the document tree will be used as the trigger for animated elements referencing that trigger name in their `animation-trigger` properties. This is likely not the desired behavior.

The `trigger-scope` property can solve this problem by limiting the scope of a trigger name to a subtree of the document. This means the trigger is visible only to elements within the same subtree and has no effect on elements outside the subtree. When `trigger-scope` is set on an element, and that element or its descendants are defined as triggers, animated elements are associated with those triggers only if they are within the same subtree.

Which trigger names are included in the scope depends on the `trigger-scope` value set:

*   `trigger-scope: all` means that all trigger names are included in the scope.
*   `trigger-scope: --my-trigger, --another-trigger` means that only triggers with names of `--my-trigger` and/or `--another-trigger` are included in the scope.
*   `trigger-scope: none` means that no trigger scoping is set on the element.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

trigger-scope =   
  none             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  all              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope#examples)

---------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope#basic_usage)

This example demonstrates using the `trigger-scope` property to limit the scope of an `animation-trigger-name`.

#### HTML

We include three [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 elements, each containing two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements: an `.animated` element and a `.trigger` element.

Most of the HTML, including a [checkbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox)
 toggle that enables or disables the `trigger-scope` property, has been hidden for brevity.

html

    <section id="one">
      <div class="animated"></div>
      ...
      <div class="trigger">Trigger for first animation</div>
      ...
    </section>
    <section id="two">
      <div class="animated"></div>
      ...
      <div class="trigger">Trigger for second animation</div>
      ...
    </section>
    <section id="three">
      <div class="animated"></div>
      ...
      <div class="trigger">Trigger for third animation</div>
      ...
    </section>
    

    <section id="one">
      <div class="animated"></div>
    
      <p>
        Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
        purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
        ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
        euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
        Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
        sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
        facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
        suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
        iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
        luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
        tristique tellus, sed tincidunt velit.
      </p>
    
      <div class="trigger">Trigger for first animation</div>
    
      <p>
        Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
        purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
        ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
        euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
        Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
        sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
        facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
        suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
        iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
        luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
        tristique tellus, sed tincidunt velit.
      </p>
    </section>
    <section id="two">
      <div class="animated"></div>
      <p>
        Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
        purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
        ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
        euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
        Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
        sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
        facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
        suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
        iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
        luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
        tristique tellus, sed tincidunt velit.
      </p>
    
      <div class="trigger">Trigger for second animation</div>
    
      <p>
        Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
        purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
        ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
        euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
        Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
        sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
        facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
        suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
        iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
        luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
        tristique tellus, sed tincidunt velit.
      </p>
    </section>
    <section id="three">
      <div class="animated"></div>
    
      <p>
        Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
        purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
        ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
        euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
        Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
        sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
        facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
        suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
        iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
        luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
        tristique tellus, sed tincidunt velit.
      </p>
    
      <div class="trigger">Trigger for third animation</div>
    
      <p>
        Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
        purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
        ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
        euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
        Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
        sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
        facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
        suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
        iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
        luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
        tristique tellus, sed tincidunt velit.
      </p>
    </section>
    <label for="trigger-scope"
      >Set <code>trigger-scope</code> to <code>none</code>
      <input id="trigger-scope" type="checkbox" />
    </label>
    

#### CSS

We define three [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 animations. Each will be applied to a different `.animated` element.

css

    @keyframes fade-in {
      from {
        opacity: 1;
      }
    
      to {
        opacity: 0;
      }
    }
    
    @keyframes color-cycle {
      from {
        background: red;
        scale: 1;
      }
    
      to {
        background: blue;
        scale: 2;
      }
    }
    
    @keyframes move-up-down {
      25% {
        translate: 0 -20px;
      }
    
      75% {
        translate: 0 20px;
      }
    }
    

    body {
      width: 60%;
      margin: 0 auto;
      font-size: 1.3rem;
      font-family: "Helvetica", "Arial";
    }
    
    p {
      line-height: 1.5;
    }
    
    section {
      background: #eeeeee;
      padding: 10px 20px;
      margin-top: 20px;
    }
    
    .animated {
      width: 50px;
      height: 50px;
      background: red;
      border: 5px solid black;
    }
    
    label {
      position: fixed;
      bottom: 2px;
      right: 2px;
      padding: 5px;
      border: 2px solid black;
      background: white;
    }
    

The animated elements' [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 is set to `fixed`, positioning them near the top of the scrollport to keep them visible at all times.

Each animated element has the same `animation-trigger` value: their animations are triggered by a trigger with a `timeline-trigger-name` of `--t`, and the animations will play when their trigger activates and then reset when their trigger deactivates.

css

    .animated {
      position: fixed;
      top: 10px;
      animation-trigger: --t play reset;
    }
    

Using the [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 shorthand, each `.animated` element is given a different [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
. They each also have a different [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
 value so that they are not positioned on top of one another.

css

    #one .animated {
      animation: fade-in 1s infinite alternate ease-in;
      left: 10px;
    }
    
    #two .animated {
      animation: color-cycle 1s infinite alternate linear;
      left: 110px;
    }
    
    #three .animated {
      animation: move-up-down 2s infinite linear;
      left: 210px;
    }
    

The `.trigger` elements are set as triggers for the `.animated` elements by giving them a [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
 value that references the same identifier, `--t`, and a [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
 of `view()`. We set the [`timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
 to `contain` and let the [`timeline-trigger-active-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
 default to the same value. As a result, activation and deactivation occur while the trigger is still visible. We also set some rudimentary styles to make them stand out from the rest of the text.

css

    .trigger {
      timeline-trigger-name: --t;
      timeline-trigger-source: view();
      timeline-trigger-activation-range: contain;
    
      padding: 10px;
      border: 2px solid black;
      background: black;
      color: white;
    }
    

Finally, we set the `trigger-scope` on the [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 element to `all`. This limits the effect of each trigger named `--t` to their `<section>` ancestor.

css

    section {
      trigger-scope: all;
    }
    

    :has(:checked) section {
      trigger-scope: none;
    }
    
    @supports not (trigger-scope: all) {
      body::before {
        content: "Your browser does not support the trigger-scope property.";
        background-color: wheat;
        text-align: center;
        padding: 1rem 0;
    
        z-index: 1;
        position: fixed;
        inset: 40% 0 auto;
      }
    }
    

#### Result

Scroll down the example. One square animates at a time. This is because each square animates only when the trigger element located in the same scope (the same `<section>`) is visible in the scrollport. Even though the three triggers share the same trigger name, each `.animated` element's animation is triggered by a different trigger.

Now check the checkbox to remove `trigger-scope: all` from the `<section>` elements. Scroll through the content again. None of the squares animate until the third `.trigger` is visible in the scrollport, at which point all of the squares start animating at the same time. Because scoping has been removed, each `.animated` element's animation is activated and deactivated by the last element with `--t` as a `timeline-trigger-name`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Animation Triggers  <br>\# propdef-trigger-scope](https://drafts.csswg.org/animation-triggers-1/#propdef-trigger-scope) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope#see_also)

---------------------------------------------------------------------------------------------------------

*   [`animation-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger)
    
*   [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
    , [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
    , [`timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
    , and [`timeline-trigger-active-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
    
*   [`timeline-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger)
     shorthand property
*   [`<animation-action>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action)
     type
*   [Using CSS scroll-triggered animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)
    
*   [CSS animation triggers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers)
     module
*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/trigger-scope/index.md?plain=1 "Folder: en-us/web/css/reference/properties/trigger-scope (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftrigger-scope&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftrigger-scope%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftrigger-scope%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftrigger-scope%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1a2a5b56a689b441ebf3be91b90f15746c5a5a01%0A*+Document+last+modified%3A+2026-10-12T05%3A04%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")