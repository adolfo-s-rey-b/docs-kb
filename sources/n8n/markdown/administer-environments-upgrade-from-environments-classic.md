For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/administer/environments/upgrade-from-environments-classic.md)
.

Environments improve on and replace [Environments (Classic)](https://docs.n8n.io/administer/use-source-control-and-environments)
, the earlier source control feature. Each instance uses either Classic or Environments, and you can switch back to Classic while Environments are in Preview.

**Preview status**

Environments are in Preview and may change in future releases. Try them on test instances before you set them up for your production instances.

Compare Classic and Environments[](https://docs.n8n.io/administer/environments/upgrade-from-environments-classic#compare-classic-and-environments)

---------------------------------------------------------------------------------------------------------------------------------------------------

Environments (Classic)

Environments

Model

The instance pushes to and pulls from one branch.

The instance promotes to one environment and applies from another. Each can use its own repository and branch.

Git hosts

Any Git host over SSH or HTTPS.

Any Git host through Generic Git, as in Classic. GitLab adds repository and branch lists.

Reviews

Manually on the Git host.

Promotion reviews in n8n with a visual diff, based on merge requests that n8n opens on GitLab.

Selecting changes

You choose what to push. Pull brings in everything.

You choose changes in both directions with a project promote or project apply, or move all team projects with an instance promote or instance apply.

Dependencies

You select workflows, credentials, and data tables. n8n adds tags and variable stubs.

n8n includes everything the selected workflows use. Selecting dependencies yourself is planned.

Before changes land

Pull can overwrite local changes after you confirm.

Apply checks for blockers first and asks you to confirm destructive changes.

Credentials

Stubs without values.

Must exist on the target, or you create them during Apply.

Variables

Stubs without values.

Written to the repository with their values. Must exist on the target, or you create them during Apply.

Who can use it

Instance owners and admins. Project admins can push.

Instance owners and admins. Support for project admins in project promotes and project applies is planned.

Personal projects

Included.

Not included.

Automation

Source control endpoints in the public API, and a pull command in the n8n CLI.

Promotion endpoints in the public API, and promotion commands in the n8n CLI.

Classic features Environments don't support yet[](https://docs.n8n.io/administer/environments/upgrade-from-environments-classic#classic-features-environments-dont-support-yet)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Environments don't cover everything Environments (Classic) does yet. Check these before you upgrade:

*   **Personal projects:** Classic includes them. Environments promote team projects only.
    
*   **Project admins:** in Classic, project admins can push. In Environments, only instance owners and instance admins can promote and apply. Support for project admins in project promotes and project applies is planned.
    
*   **Auto publish:** Classic can publish workflows when you pull. Apply doesn't change whether a workflow is published. Auto publish is planned.
    
*   **Instance color:** Classic lets you set a color for the instance. Environments don't have this setting.
    
*   **Selecting dependencies:** Classic lets you push credentials and data tables on their own. Environments include every dependency of the selected workflows, and you can't select dependencies yourself. Selecting dependencies is planned.
    
*   **Cross-project moves:** Classic pull moves workflows to the project they belong to in Git. A project promote or project apply can't move workflows or folders between projects, so use an instance promote and instance apply. See [Moving workflows and folders between projects](https://docs.n8n.io/administer/environments/known-limitations#moving-workflows-and-folders-between-projects)
    .
    
*   **Workflow descriptions:** Classic syncs them. Environments don't.
    
*   **Credential settings:** Classic syncs whether a credential is shared with all users and projects, and whether each user connects their own account to it. Environments don't, so set these options again on the target instance.
    

Environments also have limitations that don't relate to Classic. See [Known limitations](https://docs.n8n.io/administer/environments/known-limitations)
.

Migrate from Environments (Classic)[](https://docs.n8n.io/administer/environments/upgrade-from-environments-classic#migrate-from-environments-classic)

-------------------------------------------------------------------------------------------------------------------------------------------------------

Classic and Environments store content in Git in different formats, so Apply can't read what Classic pushed. Environments can technically share a repository with Classic content, but n8n recommends a new repository or an empty branch.

Try this on test instances first. Your Classic setup stays connected in the background, so you can switch back.

Before you start:

1.  Switch any CI pipelines that call the Classic endpoints of the public API to the promotion endpoints. Upgrading only changes the UI, so those endpoints keep running Classic push and pull. n8n plans to block them on instances that use Environments.
    
2.  On every instance, such as development and production, go to **Settings** > **Environments (Classic)**, select **Upgrade**, and confirm.
    
3.  Create a new repository or an empty branch for the Production environment.
    
4.  Add the environment configurations, as in [Development and production](https://docs.n8n.io/administer/environments/plan-your-environments#development-and-production)
    . Don't apply on production while the branch is empty.
    

Then fill the branch in one of two ways.

### Start from development[](https://docs.n8n.io/administer/environments/upgrade-from-environments-classic#start-from-development)

If development has no changes that you aren't ready to bring to production, follow [Your first promotion](https://docs.n8n.io/administer/environments/first-promotion#promote-and-apply)
 from step 3.

### Start from production[](https://docs.n8n.io/administer/environments/upgrade-from-environments-classic#start-from-production)

If development has changes that aren't ready for production, fill the branch from production instead. The branch then matches production, and you promote changes from development when they're ready.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1614847662-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FwMJrGrimpx3PxCJpUswm%252Fuploads%252Fgit-blob-d4f2b2f0afea263ec3d3ebc3cc462e96219d0911%252Fenvironments-migrate-from-classic.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3d7be344d5a9b8a8d31f4996c141e500&sv=3)

Migration from Environments (Classic): 1, the production instance runs one instance promote to the Production environment's Git branch. 2, the development instance promotes changes to the branch. 3, the production instance applies them.

1.  On production, add a Production promote environment configuration, pointing to the same repository and branch, and run an [instance promote](https://docs.n8n.io/administer/environments/promote-changes#instance-promote)
    . Then remove the promote environment configuration from production.
    
2.  From then on, promote changes from development with a [project promote](https://docs.n8n.io/administer/environments/promote-changes#project-promote)
     when they're ready. An instance promote would also send the changes that aren't ready.
    
3.  On production, [apply](https://docs.n8n.io/administer/environments/apply-changes)
     the changes.
    

In both cases, Classic pull kept the source's IDs, so Apply updates the content on production in place. Workflows keep their version history and executions, variables keep their values, and credentials keep their secrets. When you're done, [protect the production instance](https://docs.n8n.io/administer/environments/protect-a-production-instance)
.

Switch back to Environments (Classic)[](https://docs.n8n.io/administer/environments/upgrade-from-environments-classic#switch-back-to-environments-classic)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

1.  Go to **Settings** > **Environments**.
    
2.  Select **Switch back**, then confirm.
    

Switching back affects only this instance. You can upgrade again at any time.

Related resources[](https://docs.n8n.io/administer/environments/upgrade-from-environments-classic#related-resources)

---------------------------------------------------------------------------------------------------------------------

*   [Environments](https://docs.n8n.io/administer/environments)
    
*   [Plan your environments](https://docs.n8n.io/administer/environments/plan-your-environments)
    
*   [Your first promotion](https://docs.n8n.io/administer/environments/first-promotion)
    
*   [Promote changes](https://docs.n8n.io/administer/environments/promote-changes)
    
*   [Apply changes](https://docs.n8n.io/administer/environments/apply-changes)
    
*   [Promotion reviews](https://docs.n8n.io/administer/environments/promotion-reviews)
    
*   [Git-based promotion](https://docs.n8n.io/administer/environments/git-based-promotion)
    
*   [Known limitations](https://docs.n8n.io/administer/environments/known-limitations)
    
*   [Environments (Classic)](https://docs.n8n.io/administer/use-source-control-and-environments)
    

[PreviousKnown limitations](https://docs.n8n.io/administer/environments/known-limitations)
[NextEnvironments (Classic)](https://docs.n8n.io/administer/use-source-control-and-environments)

Last updated 5 days ago

Was this helpful?