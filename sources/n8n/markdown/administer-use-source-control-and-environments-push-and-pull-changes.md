For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes.md)
.

If your n8n instance connects to a Git repository, you need to keep your work in sync with Git.

This document assumes some familiarity with Git concepts and terminology. Refer to [Git and n8n](https://docs.n8n.io/administer/use-source-control-and-environments/use-git-in-n8n)
 for an introduction to how n8n works with Git.

**Recommendation: don't push and pull to the same n8n instance**

You can push work from an instance to a branch, and pull to the same instance. n8n doesn't recommend this. To reduce the risk of merge conflicts and overwriting work, try to create a process where work goes in one direction: either to Git, or from Git, but not both.

Fetch other people's work[](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes#fetch-other-peoples-work)

-----------------------------------------------------------------------------------------------------------------------------------------------

**n8n roles control which users can pull (fetch) changes**

You must be an instance owner or instance admin to pull changes from git.

To pull work from Git, select **Pull** ![Pull icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1614847662-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FwMJrGrimpx3PxCJpUswm%252Fuploads%252Fgit-blob-48755d1a037ee367e5205304c20598fa890889fa%252Fpull-icon.png%3Falt%3Dmedia&width=41&dpr=3&quality=100&sign=b93ee34eb9bbf3e8efbe9647c481ccc0&sv=3) in the main menu.

View screenshot[](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes#view-screenshot)

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2738857267-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FGixZThfitWP21x2gQFpD%252Fuploads%252Fgit-blob-98a82c8be4b7330fdc9f319a5471025b0c074331%252Fpull-push-menu-closed.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=345322b8ab1197c316af40114124419e&sv=3)

Pull and push buttons when menu is closed

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2738857267-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FGixZThfitWP21x2gQFpD%252Fuploads%252Fgit-blob-32ef0c500c113d20ae64455432c0d9bd3f6acb2c%252Fpull-push-menu-open.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=69a6302d8f562d2bd809a99b70a0c3ec&sv=3)

Pull and push buttons when menu is open

n8n may display a warning about overriding local changes. Select **Pull and override** to override your local work with the content in Git.

When the changes include new variable or credential stubs, n8n notifies you that you need to populate the values for the items before using them.

**How deleted resources are handled**

When workflows, credentials, variables, tags, and data tables are deleted from the repository, your local versions of these resources aren't deleted automatically. Instead, when you pull repository changes, n8n notifies you about any outdated resources and asks if you'd like to delete them.

### Workflow and credential owner may change on pull[](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes#workflow-and-credential-owner-may-change-on-pull)

When you pull from Git to an n8n instance, n8n tries to assign workflows and credentials to a matching user or project.

If the original owner is a user:

If the same owner is available on both instances (matching email), the owner remains the same. If the original owner isn't on the new instance, n8n sets the user performing the pull as the workflow owner.

If the original owner is a [project](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac)
:

n8n matches the project by its ID. If no project with that ID exists on the new instance, n8n creates one with the same ID and name. The user who pulls becomes its project admin. n8n then imports the workflows and credentials into the project.

### Auto publish workflows on pull[](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes#auto-publish-workflows-on-pull)

When pulling, you can choose to automatically publish workflows using the **Auto publish** dropdown in the pull modal. This has three modes:

*   **Off** (default): Don't attempt to publish any workflows. Workflows keep their current local publish state.
    
*   **If workflow already published**: Only attempt to publish workflows that are already published on this instance. New workflows aren't published.
    
*   **On**: Attempt to publish all pulled workflows, including new ones.
    

n8n never auto publishes archived workflows, regardless of the auto publish setting.

After a pull with auto publish enabled, n8n displays a results modal showing which workflows were successfully published and which failed. Publishing can fail if a workflow has validation errors or missing credentials.

Auto publish is also available through the [API](https://docs.n8n.io/connect/n8n-api/api-reference)
 using the `autoPublish` parameter on the pull endpoint, with values `none`, `published`, or `all`.

### Pulling may cause brief service interruption[](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes#pulling-may-cause-brief-service-interruption)

If you pull changes to a published workflow, n8n unpublishes the workflow while pulling, then republishes it. This may result in a few seconds of downtime for the workflow.

Send your work to Git[](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes#send-your-work-to-git)

----------------------------------------------------------------------------------------------------------------------------------------

**n8n roles control which users can push changes**

You must be an instance owner, instance admin, or project admin to push changes to git.

To push work to Git:

1.  Select **Push** ![Push icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2738857267-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FGixZThfitWP21x2gQFpD%252Fuploads%252Fgit-blob-1209b96071e902f51f10f21f3744e2ada861a5cf%252Fpush-icon.png%3Falt%3Dmedia&width=40&dpr=3&quality=100&sign=7b8629e1846c74f4bea1b950bcffb833&sv=3) in the main menu.
    
2.  In the **Commit and push changes** modal, select which workflows and data tables you want to push. You can filter by status (new, modified, deleted) and search for items. n8n automatically pushes tags, and variable and credential stubs.
    
    n8n pushes the current saved version, not the published version, of the workflow. You need to then separately publish versions on the remote server.
    
3.  Enter a commit message. This should be a one sentence description of the changes you're making.
    
4.  Select **Commit and Push**. n8n sends the work to Git, and displays a success message on completion.
    

What gets committed[](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes#what-gets-committed)

------------------------------------------------------------------------------------------------------------------------------------

n8n commits the following to Git:

*   Workflows, including their tags and the email address of the workflow owner. You can choose which workflows to push.
    
*   Credential stubs - ID, name and type. Any other fields are included only if they are [expressions](https://docs.n8n.io/data/expressions/)
    . You can choose which credentials to push.
    
*   Variable stubs (ID and name)
    
*   Data table schemas (table name and column definitions, not row data). You can choose which data tables to push.
    
*   Projects
    
*   Folders
    

Merge behaviors and conflicts[](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes#merge-behaviors-and-conflicts)

--------------------------------------------------------------------------------------------------------------------------------------------------------

n8n's implementation of source control is opinionated. It resolves merge conflicts for credentials and variables automatically. n8n can't detect conflicts on workflows.

### Workflows[](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes#workflows)

You have to explicitly tell n8n what to do about workflows when pushing or pulling. The Git repository acts as the source of truth.

When pulling, you might get warned that your local copy of a workflow differs from Git, and if you accept, your local copy would be overridden. Be careful not to lose relevant changes when pulling.

When you push, your local workflow will override what's in Git, so make sure that you have the most up to date version or you risk overriding recent changes.

To prevent the issue described above, you should immediately push your changes to a workflow once you finish working on it. Then it's safe to pull.

To avoid losing data:

*   Design your source control setup so that workflows flow in one direction. For example, make edits on a development instance, push to Git, then pull to production. Don't make edits on the production instance and push them.
    
*   Don't push all workflows. Select the ones you need.
    
*   Be cautious about manually editing files in the Git repository.
    

### Credentials, variables and workflow tags[](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes#credentials-variables-and-workflow-tags)

Credentials and variables can't have merge issues, as n8n chooses the version to keep.

On pull:

*   If the tag, variable or credential doesn't exist, n8n creates it.
    
*   If the tag, variable or credential already exists, n8n doesn't update it, unless:
    
    *   You set the value of a variable using the API or externally. The new value overwrites any existing value.
        
    *   The credential name has changed. n8n uses the version in Git.
        
    *   The name of a tag has changed. n8n updates the tag name. Be careful when renaming tags as tag names are unique and this could cause database issues when it comes to uniqueness during the pull process.
        
    

On push:

*   n8n overwrites the entire variables and tags files.
    
*   If a credential already exists, n8n overwrites it with the changes, but doesn't apply these changes to existing credentials on pull.
    

### Data tables[](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes#data-tables)

n8n syncs data table schemas (table structure and column definitions) across environments. Row data isn't synced.

On push:

*   You can select which data tables to include.
    
*   n8n exports the table name, column names, column types, and column order.
    

On pull:

*   n8n creates data tables that don't exist locally.
    
*   n8n updates existing data tables to match the schema in Git: it adds new columns and removes columns that no longer exist in the remote version. n8n keeps the data in the remaining columns.
    
*   n8n matches data tables by their name within a project. If you delete and recreate a data table with the same name in the source environment, or create it manually with the same name in both environments, n8n treats it as the same table: it reconciles the local table's ID to the incoming one, updates the schema like any other change, and keeps the local rows.
    
*   If a data table exists locally but not in Git, pulling deletes it, including all its row data. Interactive pulls list the table as **Deleted** in the confirmation dialog before anything happens. Pulls that use the force option, for example, through the API or in automated setups, delete the table without asking. To keep such a table, push it before pulling.
    

**Column removal causes data loss**

If a pulled data table has columns removed compared to your local version, n8n deletes those columns and their data. This can't be undone. n8n displays a warning in the pull modal when this will happen.

**Manage credentials with an external secrets vault**

If you need different credentials on different n8n environments, use [external secrets](https://docs.n8n.io/administer/manage-credentials/use-external-secret-stores)
.

Related resources[](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes#related-resources)

--------------------------------------------------------------------------------------------------------------------------------

*   [Use source control and environments](https://docs.n8n.io/administer/use-source-control-and-environments)
    
*   [Understand source control](https://docs.n8n.io/administer/use-source-control-and-environments/understand-source-control)
    
*   [Work with environments](https://docs.n8n.io/administer/use-source-control-and-environments/work-with-environments)
    
*   [Use Git in n8n](https://docs.n8n.io/administer/use-source-control-and-environments/use-git-in-n8n)
    
*   [Choose branching patterns](https://docs.n8n.io/administer/use-source-control-and-environments/choose-branching-patterns)
    
*   [Set up source control](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control)
    
*   [Compare versions](https://docs.n8n.io/administer/use-source-control-and-environments/compare-versions)
    
*   [Move work between environments](https://docs.n8n.io/administer/use-source-control-and-environments/move-work-between-environments)
    
*   [Use environments programmatically with the public API](https://docs.n8n.io/administer/use-source-control-and-environments/use-environments-via-api)
    
*   [Tutorial: Create environments with source control](https://docs.n8n.io/administer/use-source-control-and-environments/tutorial-create-environments-with-source-control)
    

[PreviousSet up source control](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control)
[NextCompare versions](https://docs.n8n.io/administer/use-source-control-and-environments/compare-versions)

Last updated 5 days ago

Was this helpful?