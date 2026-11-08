[Skip to main content](https://numpy.org/doc/stable/user/how-to-how-to.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/user/how-to-how-to.html)
[2.5 (stable)](https://numpy.org/doc/stable/user/how-to-how-to.html)
[2.4](https://numpy.org/doc/2.4/user/how-to-how-to.html)
[2.3](https://numpy.org/doc/2.3/user/how-to-how-to.html)
[2.2](https://numpy.org/doc/2.2/user/how-to-how-to.html)
[2.1](https://numpy.org/doc/2.1/user/how-to-how-to.html)
[2.0](https://numpy.org/doc/2.0/user/how-to-how-to.html)
[1.26](https://numpy.org/doc/1.26/user/how-to-how-to.html)
[1.25](https://numpy.org/doc/1.25/user/how-to-how-to.html)
[1.24](https://numpy.org/doc/1.24/user/how-to-how-to.html)
[1.23](https://numpy.org/doc/1.23/user/how-to-how-to.html)
[1.22](https://numpy.org/doc/1.22/user/how-to-how-to.html)
[1.21](https://numpy.org/doc/1.21/user/how-to-how-to.html)
[1.20](https://numpy.org/doc/1.20/user/how-to-how-to.html)
[1.19](https://numpy.org/doc/1.19/user/how-to-how-to.html)
[1.18](https://numpy.org/doc/1.18/user/how-to-how-to.html)
[1.17](https://numpy.org/doc/1.17/user/how-to-how-to.html)
[1.16](https://numpy.org/doc/1.16/user/how-to-how-to.html)
[1.15](https://numpy.org/doc/1.15/user/how-to-how-to.html)
[1.14](https://numpy.org/doc/1.14/user/how-to-how-to.html)
[1.13](https://numpy.org/doc/1.13/user/how-to-how-to.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

How to write a NumPy how-to[#](https://numpy.org/doc/stable/user/how-to-how-to.html#how-to-write-a-numpy-how-to "Link to this heading")

========================================================================================================================================

How-tos get straight to the point – they

*   answer a focused question, or
    
*   narrow a broad question into focused questions that the user can choose among.
    

A stranger has asked for directions…[#](https://numpy.org/doc/stable/user/how-to-how-to.html#a-stranger-has-asked-for-directions "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

**“I need to refuel my car.”**

Give a brief but explicit answer[#](https://numpy.org/doc/stable/user/how-to-how-to.html#give-a-brief-but-explicit-answer "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

*   _“Three kilometers/miles, take a right at Hayseed Road, it’s on your left.”_
    

Add helpful details for newcomers (“Hayseed Road”, even though it’s the only turnoff at three km/mi). But not irrelevant ones:

*   Don’t also give directions from Route 7.
    
*   Don’t explain why the town has only one filling station.
    

If there’s related background (tutorial, explanation, reference, alternative approach), bring it to the user’s attention with a link (“Directions from Route 7,” “Why so few filling stations?”).

Delegate[#](https://numpy.org/doc/stable/user/how-to-how-to.html#delegate "Link to this heading")

--------------------------------------------------------------------------------------------------

*   _“Three km/mi, take a right at Hayseed Road, follow the signs.”_
    

If the information is already documented and succinct enough for a how-to, just link to it, possibly after an introduction (“Three km/mi, take a right”).

If the question is broad, narrow and redirect it[#](https://numpy.org/doc/stable/user/how-to-how-to.html#if-the-question-is-broad-narrow-and-redirect-it "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**“I want to see the sights.”**

The _See the sights_ how-to should link to a set of narrower how-tos:

*   Find historic buildings
    
*   Find scenic lookouts
    
*   Find the town center
    

and these might in turn link to still narrower how-tos – so the town center page might link to

*   Find the court house
    
*   Find city hall
    

By organizing how-tos this way, you not only display the options for people who need to narrow their question, you also have provided answers for users who start with narrower questions (“I want to see historic buildings,” “Which way to city hall?”).

If there are many steps, break them up[#](https://numpy.org/doc/stable/user/how-to-how-to.html#if-there-are-many-steps-break-them-up "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

If a how-to has many steps:

*   Consider breaking a step out into an individual how-to and linking to it.
    
*   Include subheadings. They help readers grasp what’s coming and return where they left off.
    

Why write how-tos when there’s Stack Overflow, Reddit, Gitter…?[#](https://numpy.org/doc/stable/user/how-to-how-to.html#why-write-how-tos-when-there-s-stack-overflow-reddit-gitter "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   We have authoritative answers.
    
*   How-tos make the site less forbidding to non-experts.
    
*   How-tos bring people into the site and help them discover other information that’s here .
    
*   Creating how-tos helps us see NumPy usability through new eyes.
    

Aren’t how-tos and tutorials the same thing?[#](https://numpy.org/doc/stable/user/how-to-how-to.html#aren-t-how-tos-and-tutorials-the-same-thing "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

People use the terms “how-to” and “tutorial” interchangeably, but we draw a distinction, following Daniele Procida’s [taxonomy of documentation](https://documentation.divio.com/)
.

Documentation needs to meet users where they are. _How-tos_ offer get-it-done information; the user wants steps to copy and doesn’t necessarily want to understand NumPy. _Tutorials_ are warm-fuzzy information; the user wants a feel for some aspect of NumPy (and again, may or may not care about deeper knowledge).

We distinguish both tutorials and how-tos from _Explanations_, which are deep dives intended to give understanding rather than immediate assistance, and _References_, which give complete, authoritative data on some concrete part of NumPy (like its API) but aren’t obligated to paint a broader picture.

For more on tutorials, see [Learn to write a NumPy tutorial](https://numpy.org/numpy-tutorials/tutorial-style-guide "(in  vundefined)")

Is this page an example of a how-to?[#](https://numpy.org/doc/stable/user/how-to-how-to.html#is-this-page-an-example-of-a-how-to "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

Yes – until the sections with question-mark headings; they explain rather than giving directions. In a how-to, those would be links.

On this page