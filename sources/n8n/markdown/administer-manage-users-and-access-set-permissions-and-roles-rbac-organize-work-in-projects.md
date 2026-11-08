For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects.md)
.

**Feature availability**

RBAC is available on:

*   **n8n Cloud:** All plans
    
*   **Self-hosted:** Registered Community, Business, Enterprise
    

Different plans have different numbers of projects and roles.

n8n uses projects to group workflows and credentials, and assigns [roles](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles)
 to users in each project. This means that a single user can have different roles in different projects, giving them different levels of access.

### Create a project[](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects#create-a-project)

Instance owners and instance admins can create projects.

To create a project:

1.  Select ![Plus icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1614847662-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FwMJrGrimpx3PxCJpUswm%252Fuploads%252Fgit-blob-a47910ee526fed1a81f6e9872b40dd80df8ae8c8%252Fplus.png%3Falt%3Dmedia&width=40&dpr=3&quality=100&sign=40c894fc3912cd0793d991e99e05af08&sv=3) **Add project**.
    
2.  Fill out the project settings.
    
3.  Select **Save**.
    

### Add and remove users in a project[](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects#add-and-remove-users-in-a-project)

Project admins can add and remove users.

To add a user to a project:

1.  Select the project.
    
2.  Select **Project settings**.
    
3.  Under **Project members**, browse for users or search by username or email address.
    
4.  Select the user you want to add.
    
5.  Check the [role type](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles)
     and change it if needed.
    
6.  Select **Save**.
    

To remove a user from a project:

1.  Select the project.
    
2.  Select **Project settings**.
    
3.  In the **three-dot menu** for the user you want to remove, select **Remove user**.
    
4.  Select **Save**.
    

### Delete a project[](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects#delete-a-project)

To delete a project:

1.  Select the project.
    
2.  Select **Project settings**.
    
3.  Select **Delete project**.
    
4.  Choose what to do with the workflows and credentials. You can select:
    
    *   **Transfer its workflows and credentials to another project**: n8n prompts you to choose a project to move the data to.
        
    *   **Delete its workflows and credentials**: n8n prompts you to confirm that you want to delete all the data in the project.
        
    

### Favorite a project[](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects#favorite-a-project)

You can favorite a team project to pin it for quick access. Open the project and select the star icon in the project header, or select its **three-dot menu** and select **Favorite**. See [Favorite items](https://docs.n8n.io/build/manage-workflows/favorite-items)
 for details, including how to favorite workflows, folders, and data tables the same way.

### Move workflows and credentials between projects or users[](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects#move-workflows-and-credentials-between-projects-or-users)

Workflow and credential owners can move workflows or credentials (changing ownership) to other users or projects they have access to.

**Moving revokes sharing**

Moving workflows or credentials removes all existing sharing. Be aware that this could impact other workflows currently sharing these resources.

1.  Select **Workflow menu** ![Workflow menu icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1614847662-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FwMJrGrimpx3PxCJpUswm%252Fuploads%252Fgit-blob-f19a4d097d364587b73864eaed77b12bfd8f516b%252Fthree-dot-options-menu.png%3Falt%3Dmedia&width=19&dpr=3&quality=100&sign=234ac33681406b52134b16435d881cc7&sv=3) or **Credential menu** ![Workflow menu icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1614847662-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FwMJrGrimpx3PxCJpUswm%252Fuploads%252Fgit-blob-f19a4d097d364587b73864eaed77b12bfd8f516b%252Fthree-dot-options-menu.png%3Falt%3Dmedia&width=19&dpr=3&quality=100&sign=234ac33681406b52134b16435d881cc7&sv=3) > **Move**.
    
    **Moving workflows with credentials**
    
    When moving a workflow with credentials you have permission to share, you can choose to share the credentials as well. This ensures that the workflow continues to have access to the credentials it needs to execute. n8n will note any credentials that can't be moved (credentials you don't have permission to share).
    
2.  Select the project or user you want to move to.
    
3.  Select **Next**.
    
4.  Confirm you understand the impact of the move: workflows may stop working if the credentials they need aren't available in the target project, and n8n removes any current individual sharing.
    
5.  Select **Confirm move to new project**.
    

### Use personal credentials in team projects[](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects#use-personal-credentials-in-team-projects)

Project members can select their own personal credentials in any workflow in a team project they belong to, without sharing the credential with the project. The credential selector groups credentials into **Available to you** (your personal credentials) and **Available in** _project name_.

Only the owner and people they share the credential with directly can run or publish workflows with it. To let every project member use it, share it with the project. Refer to [Use personal credentials in projects](https://docs.n8n.io/administer/manage-credentials/use-personal-credentials-in-projects)
.

Related resources[](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Set permissions and roles (RBAC)](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac)
    
*   [See available roles](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles)
    
*   [Custom roles](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles)
    

[PreviousSee available roles](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles)
[NextCustom roles](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles)

Last updated 10 days ago

Was this helpful?