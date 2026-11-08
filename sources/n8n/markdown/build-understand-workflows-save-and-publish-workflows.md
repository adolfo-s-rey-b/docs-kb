For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/understand-workflows/save-and-publish-workflows.md)
.

n8n auto saves your workflow while you're editing. When you're ready to put the workflow into production, publish your workflow. This approach prevents accidental production changes while enabling safe iteration and review.

How saving works[](https://docs.n8n.io/build/understand-workflows/save-and-publish-workflows#how-saving-works)

---------------------------------------------------------------------------------------------------------------

Changes save automatically as you edit, typically within 1 to 5 seconds. No manual save button is required. All edits remain in draft until you publish.

How publishing works[](https://docs.n8n.io/build/understand-workflows/save-and-publish-workflows#how-publishing-works)

-----------------------------------------------------------------------------------------------------------------------

Publishing makes your workflow live and locks it to a specific version. Production executions will use this published version, not your latest edits. When you publish, your workflow will enable the following:

*   Webhook and form triggers will use their production URLs
    
*   Schedules will run at the times you've defined
    
*   Events from connected apps will trigger this workflow
    

Publishing is asynchronous. When you publish, n8n works out which triggers changed between your last published version and the new one, then applies only those changes in the background. Triggers that haven't changed keep running without interruption. The new version goes live as part of this process. The **Publish** button shows **Publishing** until n8n confirms the result. n8n stores this state on the server, so if you reload the page during a publish, the button still shows **Publishing** and updates when the result arrives.

**Initial state** When you open a workflow with no publishable changes, the Publish button is disabled.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-7e75fcd594243f7fbcdc973f833e6856b9a32d1b%252Fpublish-initial.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=4512f3db4359e7bac03a39a701e5c637&sv=3)

Disabled, greyed-out Publish button because there are no unpublished changes

**Ready to publish** When the workflow is not yet published but has changes, the button becomes active.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-67180df0edf843f217f4c815d128824e1db5dc5a%252Fpublish-ready.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d97adf244fd19faf5b380709c01c1aa8&sv=3)

Active Publish button for a workflow that has unpublished changes

**Published, up to date** The workflow is currently published and there are no new changes since the last publish.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-7cf5a4b8484f79fc52ad97780de87805ff4a17b5%252Fpublished.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=5241d0586781cd1e824426ce339fa8cc&sv=3)

Publish button showing the workflow is published and up to date, with no pending changes

**Published, has changes** The workflow is published, but you've made changes since the last publish that haven't gone live yet.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-5380e84da259d8291e39d6da3c45ebe983087f76%252Fpublished-changes.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=94a742d7ce1026d506cf6373843a10a3&sv=3)

Publish button showing the workflow is published but has changes not yet live

**Published, invalid changes** The workflow is published, but it's not in a state to be republished (no trigger requires publishing).

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-783c9274c41e628253880bd4750dfe6f27cbea3c%252Fpublished-invalid.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7a0bcb52e59ee666f4e6b19b18f7f962&sv=3)

Publish button showing the workflow can't be republished because no trigger requires publishing

**Published, error** The workflow is published, but there are errors in your recent changes that need to be fixed before you can publish again.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-62416548ab410d66a04fd87f531ecb059ada407a%252Fpublished-error.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=e01d5a1f2fe5f149e1e588477cea367a&sv=3)

Publish button showing an error state because recent changes contain errors to fix

**Publishing** After you publish, n8n registers your triggers in the background. The button shows this state until n8n confirms the result.

**Published, partial** n8n published the new version, but at least one trigger failed to activate, for example because a connected app was unavailable. The workflow keeps running the triggers that did activate, and n8n doesn't unpublish it. Hover over the button to see which triggers failed, then publish again to retry them.

**Failed to publish** None of the workflow's triggers activated, so the workflow isn't running. The published version stays set, so you can publish again to retry.

How collaboration works[](https://docs.n8n.io/build/understand-workflows/save-and-publish-workflows#how-collaboration-works)

-----------------------------------------------------------------------------------------------------------------------------

Only one person can edit a workflow at a time. If someone else is currently editing:

*   You see the workflow in read-only mode
    
*   The edit lock releases when they stop editing or become inactive
    
*   You can then take over editing with the latest changes
    

Checking publishing status[](https://docs.n8n.io/build/understand-workflows/save-and-publish-workflows#checking-publishing-status)

-----------------------------------------------------------------------------------------------------------------------------------

On the **Workflows** page, if a workflow is published an indicator will be displayed on the card.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-2b5a85ba87d8fea854306849f9ceb8adbe4f74c4%252Fpublished-indicator-wf-list.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=30df3d6faf6619621b24b292668f5bd9&sv=3)

Published indicator badge on a workflow card in the Workflows list

Publishing a workflow[](https://docs.n8n.io/build/understand-workflows/save-and-publish-workflows#publishing-a-workflow)

-------------------------------------------------------------------------------------------------------------------------

The **Publish** button in the canvas header is enabled whenever there are unpublished changes.

Each time you make a change to a workflow, n8n autosaves those changes to a new version of the workflow. These saved versions go live in production only when you publish the workflow after the changes.

1.  Click the **Publish** button (or use hotkey `Shift` + `p`) to open the publishing modal
    
2.  The version name defaults to a UUID. Customize the name if you'd like and add a description of the version.
    
3.  Click **Publish** to make your changes live in production. Production executions always point to the currently published version.
    
    If you only update workflow settings, n8n will re-publish the version without requiring you to take any action.
    

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-1b5b4794076947c9639e9b50e5c766d0b7fc3717%252Fpublish-modal.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=5c759a4e3e90f192387ed6fd1a7f9932&sv=3)

Publish modal with an editable version name (defaulting to a UUID) and description field

**Workflow reviews**

If workflow reviews are enabled for your instance, you can submit a version for review instead of publishing immediately. While a review is open, n8n blocks publishing that workflow. Refer to [Workflow reviews](https://docs.n8n.io/build/manage-workflows/workflow-reviews)
 for plan availability and how reviews work.

Naming versions[](https://docs.n8n.io/build/understand-workflows/save-and-publish-workflows#naming-versions)

-------------------------------------------------------------------------------------------------------------

**Feature availability**

Named versions are available on:

*   **n8n Cloud:** Pro, Enterprise
    
*   **Self-hosted:** Business, Enterprise
    

Named versions let you give a meaningful name and description to any workflow version. This helps you identify important milestones in your workflow's development. Named versions are also protected from automatic [version history pruning](https://docs.n8n.io/build/manage-workflows/view-change-history)
, so they persist indefinitely.

To name a version from the canvas header:

1.  Select the dropdown arrow next to the **Publish** button (or use hotkey `Cmd/Ctrl` + `s`).
    
2.  Select **Name version**.
    
3.  Enter a name and optional description.
    
4.  Select **Save**.
    

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-1a94a6d50f6643c926cea0d87fa0d30ec130af41%252Fpublish-dropdown.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=9819bcd1585d4978f54a6f0e5002f0ce&sv=3)

Publish button's dropdown menu with the Name version option

To name a version from the version history page:

1.  Open the version history by selecting the history icon in the header.
    
2.  On the version you want to name, select **Options** ![Options icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-f19a4d097d364587b73864eaed77b12bfd8f516b%252Fthree-dot-options-menu.png%3Falt%3Dmedia&width=19&dpr=3&quality=100&sign=71816d7d4b7eec8ac467fd97f3d76f22&sv=3).
    
3.  Select **Name version**.
    
4.  Enter a name and optional description.
    
5.  Select **Save**.
    

Managing version history[](https://docs.n8n.io/build/understand-workflows/save-and-publish-workflows#managing-version-history)

-------------------------------------------------------------------------------------------------------------------------------

View and manage version history by clicking the history icon in the header. In the version history view, you can perform these actions:

*   Unpublish the workflow to remove it from production
    
*   Restore a previous version. Restoring lets you work on a version without affecting the production execution.
    
*   Publish another version of the workflow
    
*   Name a version to protect it from pruning
    

How to unpublish a workflow[](https://docs.n8n.io/build/understand-workflows/save-and-publish-workflows#how-to-unpublish-a-workflow)

-------------------------------------------------------------------------------------------------------------------------------------

Unpublish a workflow from either:

*   The dropdown arrow next to the **Publish** button in the canvas header (or use hotkey `Cmd/Ctrl` + `u`).
    
*   In the workflow list
    
*   The version history page (unpublish action on published versions)
    

Related resources[](https://docs.n8n.io/build/understand-workflows/save-and-publish-workflows#related-resources)

-----------------------------------------------------------------------------------------------------------------

*   [Understand workflows](https://docs.n8n.io/build/understand-workflows)
    
*   [Create and run workflows](https://docs.n8n.io/build/understand-workflows/create-and-run-workflows)
    
*   [Create and edit credentials](https://docs.n8n.io/build/understand-workflows/create-and-edit-credentials)
    
*   [Use Gateway credits](https://docs.n8n.io/build/understand-workflows/use-gateway-credits)
    
*   [Workflow components](https://docs.n8n.io/build/understand-workflows/workflow-components)
    
*   [Understand executions](https://docs.n8n.io/build/understand-workflows/understand-executions)
    

[PreviousCreate and run workflows](https://docs.n8n.io/build/understand-workflows/create-and-run-workflows)
[NextCreate and edit credentials](https://docs.n8n.io/build/understand-workflows/create-and-edit-credentials)

Last updated 10 days ago

Was this helpful?