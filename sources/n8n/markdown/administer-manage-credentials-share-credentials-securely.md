For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/administer/manage-credentials/share-credentials-securely.md)
.

**Feature availability**

Credential sharing is available on:

*   **n8n Cloud:** All plans
    
*   **Self-hosted:** Business, Enterprise
    

You can share a credential directly with other users to use in their own workflows. Or share a credential in a project for all members of that project to use. Any users using a shared credential won't be able to view or edit the credential details.

You don't need to share your own credentials to use them in a team project you're a member of. Share a credential when other people need to run or publish workflows with it. Refer to [Use personal credentials in projects](https://docs.n8n.io/administer/manage-credentials/use-personal-credentials-in-projects)
 for how personal credentials work in team projects and who a workflow run acts as.

Users can share credentials they created and own. Only project admins can share credentials created in and owned by a project. Instance owners and instance admins can view and share all credentials on an instance. On the **Sharing** tab, only the credential's owner, or users with permission to share credentials, can change who the credential is shared with.

Refer to [Instance roles](https://docs.n8n.io/administer/manage-users-and-access/understand-instance-roles)
 for more information about owners and admins.

In [projects](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac)
, a user's role controls how they can interact with the workflows and credentials associated to the projects they're a member of.

**Sharing end-user credentials**

Sharing an [end-user credential](https://docs.n8n.io/administer/manage-credentials/end-user-credentials)
 shares the credential itself, not a connection. Users you share it with connect their own account, they don't use yours.

Share a credential[](https://docs.n8n.io/administer/manage-credentials/share-credentials-securely#share-a-credential)

----------------------------------------------------------------------------------------------------------------------

To share a credential:

1.  From the left menu, select either **Overview** or a project.
    
2.  Select **Credentials** to see a list of your credentials.
    
3.  Select the credential you want to share.
    
4.  Select **Sharing**.
    
5.  In the **Share with projects or users** dropdown, browse or search for the user or project with which you want to share your credentials.
    
6.  Select a user or project.
    
7.  Select **Save** to apply the changes.
    

People you share a credential with get the **Can use** role: they can run and publish workflows with it, but can't see or edit its details.

Understand the Sharing tab[](https://docs.n8n.io/administer/manage-credentials/share-credentials-securely#understand-the-sharing-tab)

--------------------------------------------------------------------------------------------------------------------------------------

The **Sharing** tab lists everyone with access to the credential, and every project that uses it:

*   **Shared projects:** members can use the credential, according to their [project role](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles)
    .
    
*   **Projects that use it without a share:** a member added their personal credential to one of the project's workflows. The project has the **Can view** label, so its members can see the credential on the workflow but can't use or edit it. Members you shared the credential with directly can still use it. To give the whole project access, select **Share**.
    

In team projects, Owners and Admins follow the same sharing rules as everyone else: they can use your credential only after you share it with them. Their instance role only extends to their own personal space.

Remove access to a credential[](https://docs.n8n.io/administer/manage-credentials/share-credentials-securely#remove-access-to-a-credential)

--------------------------------------------------------------------------------------------------------------------------------------------

To unshare a credential:

1.  From the left menu, select either **Overview** or a project.
    
2.  Select **Credentials** to see a list of your credentials.
    
3.  Select the credential you want to unshare.
    
4.  Select **Sharing**.
    
5.  Select **trash icon**![Trash icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1614847662-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FwMJrGrimpx3PxCJpUswm%252Fuploads%252Fgit-blob-3e59223f23216d4a14726e8ab618776bf6dd61ab%252Fdelete-node.png%3Falt%3Dmedia&width=39&dpr=3&quality=100&sign=aaba1ce5f1f2cba73a437f1551c870ab&sv=3) on the user or project you want to remove from the list of shared users and projects.
    
6.  Select **Save** to apply the changes.
    

Related resources[](https://docs.n8n.io/administer/manage-credentials/share-credentials-securely#related-resources)

--------------------------------------------------------------------------------------------------------------------

*   [Manage credentials](https://docs.n8n.io/administer/manage-credentials)
    
*   [Use personal credentials in projects](https://docs.n8n.io/administer/manage-credentials/use-personal-credentials-in-projects)
    
*   [End-user credentials](https://docs.n8n.io/administer/manage-credentials/end-user-credentials)
    
*   [Credential overwrites](https://docs.n8n.io/administer/manage-credentials/credential-overwrites)
    
*   [Use external secret stores](https://docs.n8n.io/administer/manage-credentials/use-external-secret-stores)
    

[PreviousManage credentials](https://docs.n8n.io/administer/manage-credentials)
[NextEnd-user credentials](https://docs.n8n.io/administer/manage-credentials/end-user-credentials)

Last updated 10 days ago

Was this helpful?