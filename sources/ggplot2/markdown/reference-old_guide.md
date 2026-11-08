[Skip to content](https://ggplot2.tidyverse.org/reference/old_guide.html#container)

![](https://ggplot2.tidyverse.org/logo.png)

The previous S3 guide system
============================

Source: [`R/guide-old.R`](https://github.com/tidyverse/ggplot2/blob/v4.0.3/R/guide-old.R)

`old_guide.Rd`

The guide system has been overhauled to use the ggproto infrastructure to accommodate guide extensions with the same flexibility as layers, scales and other ggplot2 objects. In rewriting, the old S3 system has become defunct, meaning that the previous methods for guides have been superseded by ggproto methods. As a fallback option, the generics, but not the methods, that the previous S3 system used are encapsulated in the `GuideOld` ggproto class.

Usage[](https://ggplot2.tidyverse.org/reference/old_guide.html#ref-usage)

--------------------------------------------------------------------------

    guide_train(guide, scale, aesthetic = NULL)
    
    guide_merge(guide, new_guide)
    
    guide_geom(guide, layers, default_mapping = NULL)
    
    guide_transform(guide, coord, panel_params)
    
    guide_gengrob(guide, theme)
    
    old_guide(guide)

Arguments[](https://ggplot2.tidyverse.org/reference/old_guide.html#arguments)

------------------------------------------------------------------------------

guide[](https://ggplot2.tidyverse.org/reference/old_guide.html#arg-guide)

An old guide object