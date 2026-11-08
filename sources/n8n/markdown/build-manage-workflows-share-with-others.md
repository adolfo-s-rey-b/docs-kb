For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/manage-workflows/share-with-others.md)
.

**Feature availability**

Workflow sharing is available on:

*   **n8n Cloud:** All plans
    
*   **Self-hosted:** Business, Enterprise
    

Workflow sharing allows you to share workflows between users of the same n8n instance.

Users can share workflows they created. Instance owners, and users with the admin role, can view and share all workflows in the instance. Refer to [Instance roles](https://docs.n8n.io/administer/manage-users-and-access/understand-instance-roles)
 for more information about owners and admins.

Share a workflow[](https://docs.n8n.io/build/manage-workflows/share-with-others#share-a-workflow)

--------------------------------------------------------------------------------------------------

1.  Open the workflow you want to share.
    
2.  Select **Share**.
    
3.  In **Add users**, find and select the users you want to share with.
    
4.  Select **Save**.
    

**Note:** This option is only available when sharing a workflow that is inside a **Personal** workspace. When trying to use the "Add users" option for a workflow that's **inside a project**, you'll get this pop-up instead:

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-d9212e166e09178d7906e11bc8188bf995021e6b%252Fsharing-within-projects.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=dace57b464490740e256601170eeb9cc&sv=3)

Pop-up explaining that the project shares this workflow with everyone in it

This is intended behavior, and it means that the workflow is shared with everyone inside that specific project. Instead of adding the user directly to the workflow, you need to add the user to the project in which the workflow is located.

View shared workflows[](https://docs.n8n.io/build/manage-workflows/share-with-others#view-shared-workflows)

------------------------------------------------------------------------------------------------------------

You can browse and search workflows on the **Workflows** list. The workflows in the list depend on the project:

*   **Overview** lists all workflows you can access. This includes:
    
    *   Your own workflows.
        
    *   Workflows shared with you.
        
    *   Workflows in projects you're a member of.
        
    *   If you log in as the instance owner or admin: all workflows in the instance.
        
    
*   Other projects: all workflows in the project.
    

Workflow roles and permissions[](https://docs.n8n.io/build/manage-workflows/share-with-others#workflow-roles-and-permissions)

------------------------------------------------------------------------------------------------------------------------------

There are two workflow roles: creator and editor. The creator is the user who created the workflow. Editors are other users with access to the workflow.

You can't change the workflow owner, except when deleting the user.

**Credentials**

Workflow sharing allows editors to use all credentials used in the workflow. This includes credentials that aren't explicitly shared with them using [credential sharing](https://docs.n8n.io/administer/manage-credentials/share-credentials-securely)
.

### Permissions[](https://docs.n8n.io/build/manage-workflows/share-with-others#permissions)

Permissions

Creator

Editor

View workflow (read-only)

✅

✅

View executions

✅

✅

Update (including tags)

✅

✅

Run

✅

✅

Share

✅

❌

Export

✅

✅

Delete

✅

❌

Node editing restrictions with unshared credentials[](https://docs.n8n.io/build/manage-workflows/share-with-others#node-editing-restrictions-with-unshared-credentials)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sharing in n8n works on the principle of least privilege. This means that if a user shares a workflow with you, but they don't share their credentials, you can't edit the nodes within the workflow that use those credentials. You can view and run the workflow, and edit nodes that don't use unshared credentials.

Refer to [Credential sharing](https://docs.n8n.io/administer/manage-credentials/share-credentials-securely)
 for guidance on sharing credentials.

Related resources[](https://docs.n8n.io/build/manage-workflows/share-with-others#related-resources)

----------------------------------------------------------------------------------------------------

*   [Manage workflows](https://docs.n8n.io/build/manage-workflows)
    
*   [Configure workflow settings](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings)
    
*   [Tag workflows](https://docs.n8n.io/build/manage-workflows/tag-workflows)
    
*   [Favorite items](https://docs.n8n.io/build/manage-workflows/favorite-items)
    
*   [View change history](https://docs.n8n.io/build/manage-workflows/view-change-history)
    
*   [Review workflows](https://docs.n8n.io/build/manage-workflows/workflow-reviews)
    
*   [Export and import](https://docs.n8n.io/build/manage-workflows/export-and-import)
    
*   [n8n packages](https://docs.n8n.io/build/manage-workflows/n8n-packages)
    

[PreviousLimits and permissions](https://docs.n8n.io/build/manage-workflows/n8n-packages/limits-and-permissions)
[NextFlow logic](https://docs.n8n.io/build/flow-logic)

Last updated 10 days ago

Was this helpful?