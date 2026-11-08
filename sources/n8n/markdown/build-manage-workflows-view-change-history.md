For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/manage-workflows/view-change-history.md)
.

**Feature availability**

Full workflow history is available on:

*   **n8n Cloud:** Enterprise
    
*   **Self-hosted:** Enterprise
    

Versions from the last 24 hours are available for all users. Versions from the last five days are available on n8n Cloud Pro.

Use workflow history to view and restore previous versions of your workflows.

Understand workflow history[](https://docs.n8n.io/build/manage-workflows/view-change-history#understand-workflow-history)

--------------------------------------------------------------------------------------------------------------------------

n8n creates a new version when you:

*   Save your workflow.
    
*   Restore an old version. n8n saves the latest version before restoring.
    
*   Pull from a Git repository using [Source control](https://docs.n8n.io/administer/use-source-control-and-environments)
    . Note that n8n saves versions to the instance database, not to Git.
    

Changes to workflow settings do not create a new version.

**Workflow history and execution history**

Don't confuse workflow history with the [Workflow-level executions list](https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow)
.

Executions are workflow runs. With the executions list, you can see previous runs of the current version of the workflow. You can copy previous executions into the editor to [Debug and re-run past executions](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
 in your current workflow.

Workflow history is previous versions of the workflow: for example, a version with a different node, or different parameters set.

View workflow history[](https://docs.n8n.io/build/manage-workflows/view-change-history#view-workflow-history)

--------------------------------------------------------------------------------------------------------------

To view a workflow's history:

1.  Open the workflow.
    
2.  Select **Workflow history** ![Workflow history icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-a8e7ec9a91dc1491d7e6a0f4e3695e5ff1bc1d93%252Fworkflow-history.png%3Falt%3Dmedia&width=36&dpr=3&quality=100&sign=d725f10e22013c2e1f641e447b9b4067&sv=3). n8n opens a menu showing the saved workflow versions, and a canvas with a preview of the selected version.
    

Restore or copy previous versions[](https://docs.n8n.io/build/manage-workflows/view-change-history#restore-or-copy-previous-versions)

--------------------------------------------------------------------------------------------------------------------------------------

You can restore a previous workflow version, or make a copy of it:

1.  On the version you want to restore or copy, select **Options** ![Options icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-f19a4d097d364587b73864eaed77b12bfd8f516b%252Fthree-dot-options-menu.png%3Falt%3Dmedia&width=19&dpr=3&quality=100&sign=71816d7d4b7eec8ac467fd97f3d76f22&sv=3).
    
2.  Choose what you want to do:
    
    *   **Restore version**: replace your current workflow with the selected version.
        
    *   **Clone to new workflow**: create a new workflow based on the selected version.
        
    *   **Open version in new tab**: open a second tab displaying the selected version. Use this to compare versions.
        
    *   **Download**: download the version as JSON.
        
    *   **Name version**: give the version a name and description. n8n never prunes named versions automatically. Refer to [Naming versions](https://docs.n8n.io/build/understand-workflows/save-and-publish-workflows#naming-versions)
         for more details. Named versions are available on n8n Cloud Pro and Enterprise, and self-hosted Business and Enterprise.
        
    

Related resources[](https://docs.n8n.io/build/manage-workflows/view-change-history#related-resources)

------------------------------------------------------------------------------------------------------

*   [Manage workflows](https://docs.n8n.io/build/manage-workflows)
    
*   [Configure workflow settings](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings)
    
*   [Tag workflows](https://docs.n8n.io/build/manage-workflows/tag-workflows)
    
*   [Favorite items](https://docs.n8n.io/build/manage-workflows/favorite-items)
    
*   [Review workflows](https://docs.n8n.io/build/manage-workflows/workflow-reviews)
    
*   [Export and import](https://docs.n8n.io/build/manage-workflows/export-and-import)
    
*   [n8n packages](https://docs.n8n.io/build/manage-workflows/n8n-packages)
    
*   [Share with others](https://docs.n8n.io/build/manage-workflows/share-with-others)
    

[PreviousFavorite items](https://docs.n8n.io/build/manage-workflows/favorite-items)
[NextReview workflows](https://docs.n8n.io/build/manage-workflows/workflow-reviews)

Last updated 10 days ago

Was this helpful?