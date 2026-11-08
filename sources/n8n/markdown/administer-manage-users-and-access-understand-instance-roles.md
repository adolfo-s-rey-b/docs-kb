For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/administer/manage-users-and-access/understand-instance-roles.md)
.

Every user has one instance role. The instance role determines the user's permissions and access across the n8n instance.

There are four built-in instance roles: Owner, Admin, Member, and Chat user. If these don't meet your needs, you can create [custom instance roles](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles/create-custom-instance-roles)
 with granular permissions.

**Feature availability**

The **Admin** role is available on:

*   **n8n Cloud:** Pro, Enterprise
    
*   **Self-hosted:** Enterprise
    

**Feature availability**

The **Chat user** role is available on:

*   **n8n Cloud:** Pro, Enterprise
    
*   **Self-hosted:** Enterprise
    

The Chat user role requires the Chat feature to be enabled.

**Instance roles and project roles**

n8n has two levels of roles. Instance roles control what a user can do across the entire instance. Project roles (part of [RBAC](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac)
) control what a user can do within a specific project, and a user can have different project roles in different projects.

**Create a Member role account for the owner**

n8n recommends that owners create a second account with the **Member** role for themselves. Owners can see and edit all workflows, credentials, and projects. However, there is no way to see who created a particular workflow, so there is a risk of overriding other people's work if you build and edit workflows as an owner.

Permission

Owner

Admin

Member

Chat user

Manage own email and password

✅

✅

✅

✅

Manage own workflows

✅

✅

✅

❌

View, create, and use tags

✅

✅

✅

❌

Delete tags

✅

✅

❌

❌

View and share all workflows

✅

✅

❌

❌

View, edit, and share all credentials

✅

✅

❌

❌

Set up and use [Source control](https://docs.n8n.io/administer/use-source-control-and-environments)

✅

✅

❌

❌

Create [projects](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects)

✅

✅

❌

❌

View all projects

✅

✅

❌

❌

Add and remove users

✅

✅

❌

❌

Access the n8n Cloud console

✅

❌

❌

❌

Chat user role[](https://docs.n8n.io/administer/manage-users-and-access/understand-instance-roles#chat-user-role)

------------------------------------------------------------------------------------------------------------------

The Chat user role is for people who only need to use n8n through Chat. Chat users can't build workflows or access other n8n features.

**Chat users can:**

*   Send messages in Chat.
    
*   Create, edit, and delete their own Chat agents.
    
*   Run the workflows and agents that are shared with them in Chat.
    

**Chat users can't:**

*   Create, view, or edit workflows or credentials.
    
*   Create projects or view projects they don't belong to.
    
*   Create API keys.
    
*   Use some Chat tool types. Refer to the Chat documentation for details.
    

When the Chat feature is enabled, n8n opens Chat for Chat users after they sign in.

**Change a user's role to or from Chat user**

Changing the role of a user to Chat user has these effects:

*   n8n removes the user from all projects they share with others. If the user is the only admin of a project, n8n blocks the change. Assign another admin to the project first.
    
*   The user's personal project becomes read-only.
    
*   n8n deletes all API keys of the user.
    
*   Changing a Chat user to another role gives the user ownership of their personal project again. n8n doesn't restore the projects or API keys the user lost when they became a Chat user.
    

Custom instance roles[](https://docs.n8n.io/administer/manage-users-and-access/understand-instance-roles#custom-instance-roles)

--------------------------------------------------------------------------------------------------------------------------------

If the built-in roles don't match your access needs, you can create custom instance roles with granular permissions. Custom instance roles let you grant specific instance-level capabilities (such as managing users, tags, or API keys) without giving full Admin access.

Refer to [Create custom instance roles](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles/create-custom-instance-roles)
 for instructions on creating and managing them.

Related resources[](https://docs.n8n.io/administer/manage-users-and-access/understand-instance-roles#related-resources)

------------------------------------------------------------------------------------------------------------------------

*   [Manage users and access](https://docs.n8n.io/administer/manage-users-and-access)
    
*   [Set up for Cloud](https://docs.n8n.io/administer/manage-users-and-access/set-up-for-cloud)
    
*   [Add and remove users](https://docs.n8n.io/administer/manage-users-and-access/add-and-remove-users)
    
*   [Set permissions and roles (RBAC)](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac)
    
*   [Verify user identity](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity)
    
*   [Follow best practices](https://docs.n8n.io/administer/manage-users-and-access/follow-best-practices)
    

[PreviousAdd and remove users](https://docs.n8n.io/administer/manage-users-and-access/add-and-remove-users)
[NextControl node availability](https://docs.n8n.io/administer/manage-users-and-access/control-node-availability)

Last updated 10 days ago

Was this helpful?