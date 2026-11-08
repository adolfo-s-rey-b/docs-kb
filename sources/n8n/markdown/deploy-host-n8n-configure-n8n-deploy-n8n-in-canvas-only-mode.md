For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/deploy-n8n-in-canvas-only-mode.md)
.

In canvas-only mode, when you open a workflow you see only that workflow's canvas. Elements that would navigate away from it, like the command bar, are hidden.

**Feature availability**

Canvas-only mode is available from n8n 2.15.0.

Turn on canvas-only mode[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/deploy-n8n-in-canvas-only-mode#turn-on-canvas-only-mode)

--------------------------------------------------------------------------------------------------------------------------------------

Set `N8N_CANVAS_ONLY` to `true`:

Copy

    export N8N_CANVAS_ONLY=true

Canvas-only mode applies to the whole instance. You can't turn it on for individual workflows or users.

What changes in canvas-only mode[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/deploy-n8n-in-canvas-only-mode#what-changes-in-canvas-only-mode)

------------------------------------------------------------------------------------------------------------------------------------------------------

On the workflow details route, canvas-only mode hides:

*   **The Canvas header.** The workflow name, breadcrumbs, save controls, and tags no longer show.
    
*   **The left menu.** n8n's main navigation isn't visible.
    
*   **Overlay elements.** The command bar and "Ask AI assistant" button are no longer shown.
    
*   **Keyboard shortcuts.** The following keyboard shortcuts are disabled in canvas-only mode: **Ctrl/Cmd** + **s** (save), **Ctrl/Cmd** + **Alt** + **n** (create new workflow), **Ctrl/Cmd** + **p** (publish), **Ctrl/Cmd** + **u** (unpublish), **Ctrl/Cmd** + **k** (command bar)
    

n8n keeps the following visible:

*   **The workflow canvas and its nodes.** You can still pan, zoom, and edit the workflow.
    
*   **The tab bar** for switching between the editor, executions, and evaluations. It floats near the top of the screen instead of sitting inside the header.
    
*   **The logs panel** to display execution logs of individual nodes.
    
*   **The node creator panel.** The "Add a node" panel still opens from the canvas, repositioned to the top of the screen instead of below the header.
    

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/deploy-n8n-in-canvas-only-mode#related-resources)

------------------------------------------------------------------------------------------------------------------------

*   [Configure n8n](https://docs.n8n.io/deploy/host-n8n/configure-n8n)
    

[PreviousSet up n8n Assistant](https://docs.n8n.io/deploy/host-n8n/configure-n8n/set-up-n8n-assistant)
[NextManage your license](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-your-license)

Last updated 10 days ago

Was this helpful?