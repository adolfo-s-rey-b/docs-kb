*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion#mdn-search)
    

`prefers-reduced-motion` CSS media feature
==========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Warning:** An embedded example at the bottom of this page has a scaling movement that may be problematic for some readers. Readers with vestibular motion disorders may wish to enable the reduce motion feature on their device before viewing the animation.

The **`prefers-reduced-motion`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 is used to detect if a user has enabled a setting on their device to minimize the amount of non-essential motion. The setting is used to convey to the browser on the device that the user prefers an interface that removes, reduces, or replaces motion-based animations.

Such animations can trigger discomfort for those with [vestibular motion disorders](https://www.a11yproject.com/posts/understanding-vestibular-disorders/ "External link (opens in new tab)")
. Animations such as scaling or panning large objects can be vestibular motion triggers.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion#syntax)

-------------------------------------------------------------------------------------------------------------------

[`no-preference`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion#no-preference)

Indicates that a user has made no preference known on the device. This keyword value evaluates as false.

[`reduce`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion#reduce)

Indicates that a user has enabled the setting on their device for reduced motion. The `reduce` keyword value evaluates as true; therefore, `@media (prefers-reduced-motion)` is equivalent to `@media (prefers-reduced-motion: reduce)`.

[User preferences](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion#user_preferences)

---------------------------------------------------------------------------------------------------------------------------------------

Use the following settings to honor the `reduce` request:

*   In GTK/GNOME: Settings > Accessibility > Seeing > turn on "Reduced animation".
    
    *   In older versions of GNOME, GNOME Tweaks > General tab (or Appearance, depending on version) > Animations is turned off.
    *   Alternatively, add `gtk-enable-animations = false` to the `[Settings]` block of [the GTK 3 configuration file](https://wiki.archlinux.org/title/GTK#Configuration "External link (opens in new tab)")
        .
    *   Additionally, try running `gsettings set org.gnome.desktop.interface enable-animations false` to make Firefox (and other programs relying on GTK version 4) respect the `reduce` setting.
*   In Plasma/KDE: System Settings > Workspace Behavior > General Behavior > set "Animation speed" to "Instant".
    
    *   Alternatively, add `AnimationDurationFactor=0` to the `[KDE]` block of `~/.config/kdeglobals`.
    *   Or just run `kwriteconfig6 --key AnimationDurationFactor 0` in your terminal.
*   In Windows 10: Settings > Ease of Access > Display > Show animations in Windows.
    
*   In Windows 11: Settings > Accessibility > Visual Effects > Animation Effects.
    
*   In macOS up to 15 (Sequoia): System Settings > Accessibility > Display > Reduce motion.
    
*   In macOS 25 (Tahoe) onwards: System Settings > Accessibility > Motion > Reduce motion.
    
*   In iOS: Settings > Accessibility > Motion.
    
*   In Android 9+: Settings > Accessibility > Remove animations.
    
*   In Firefox `about:config`: Add a number preference called `ui.prefersReducedMotion` and set its value to either `0` for full animation or to `1` to indicate a preference for reduced motion. Changes to this preference take effect immediately.
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion#examples)

-----------------------------------------------------------------------------------------------------------------------

This example uses a scaling animation to demonstrate `prefers-reduced-motion`. If you enable the setting for reducing motion in the accessibility preferences on your device, the `prefers-reduced-motion` media query will detect your preference and the CSS within the reduced motion rules, with the same [specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
 but coming later in the [CSS source order](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Handling_conflicts#source_order)
, will take precedence. As a result, the [animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)
 on the box will tone down to the `dissolve` animation, which is a more muted animation that is not a vestibular motion trigger.

### [Toning down the animation scaling](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion#toning_down_the_animation_scaling)

#### HTML

html

    <div class="animation">animated box</div>
    

#### CSS

css

    .animation {
      animation: pulse 1s linear infinite both;
      background-color: purple;
    }
    
    /* Tone down the animation to avoid vestibular motion triggers. */
    @media (prefers-reduced-motion: reduce) {
      .animation {
        animation: dissolve 4s linear infinite both;
        background-color: green;
        text-decoration: overline;
      }
    }
    

    .animation {
      color: white;
      font: 1.2em sans-serif;
      width: 10em;
      padding: 1em;
      border-radius: 1em;
      text-align: center;
    }
    
    @keyframes pulse {
      0% {
        transform: scale(1);
      }
      25% {
        transform: scale(0.9);
      }
      50% {
        transform: scale(1);
      }
      75% {
        transform: scale(1.1);
      }
      100% {
        transform: scale(1);
      }
    }
    
    @keyframes dissolve {
      0% {
        opacity: 1;
      }
      50% {
        opacity: 0.3;
      }
      100% {
        opacity: 1;
      }
    }
    

#### Result

You can enable the setting for reducing motion on [your device](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion#user_preferences)
 to view the change in animation scaling. This example uses the background color and the line over the text to visually highlight when the keyframe animation switches in response to the setting being enabled or disabled.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion#specifications)

-----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Media Queries Level 5  <br>\# prefers-reduced-motion](https://drafts.csswg.org/mediaqueries-5/#prefers-reduced-motion) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion#see_also)

-----------------------------------------------------------------------------------------------------------------------

*   [`Sec-CH-Prefers-Reduced-Motion`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-CH-Prefers-Reduced-Motion)
     HTTP Header [User Agent Client Hint](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Client_hints#user_agent_client_hints)
    
*   [An introduction to the reduced motion media query](https://css-tricks.com/introduction-reduced-motion-media-query/ "External link (opens in new tab)")
     on CSS-Tricks (2019)
*   [Responsive design for motion](https://webkit.org/blog/7551/responsive-design-for-motion/ "External link (opens in new tab)")
     on WebKit Blog (2017)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jun 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/prefers-reduced-motion/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/prefers-reduced-motion (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fprefers-reduced-motion&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fprefers-reduced-motion%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fprefers-reduced-motion%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fprefers-reduced-motion%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2d5e55258ef3f001d0d9fea6b48486bd3056fca6%0A*+Document+last+modified%3A+2026-06-10T10%3A02%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")