For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/administer/environments.md)
.

Environments let you move workflows and other n8n resources, such as credentials, variables, and data tables, through the steps of your release process, such as development and production. You build and test changes on one instance, then promote them to the next step.

**Feature availability**

Environments are available on:

*   **n8n Cloud:** Enterprise
    
*   **Self-hosted:** Enterprise
    

Only instance owners and instance admins can set up environments, promote, apply, and review promotions.

**Preview status**

Environments are in Preview and may change in future releases. Try them on test instances before you set them up for your production instances.

**Limited enterprise readiness**

Environments have **Limited enterprise readiness**. See [Enterprise readiness](https://docs.n8n.io/administer/environments/known-limitations#enterprise-readiness)
 for the Enterprise capabilities they don't support yet.

Why use environments[](https://docs.n8n.io/administer/environments#why-use-environments)

-----------------------------------------------------------------------------------------

Separate environments let you change workflows without breaking the ones running in production. A common setup:

*   **Development:** build and change workflows.
    
*   **Production:** run the live workflows.
    

How environments work[](https://docs.n8n.io/administer/environments#how-environments-work)

-------------------------------------------------------------------------------------------

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1614847662-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FwMJrGrimpx3PxCJpUswm%252Fuploads%252Fgit-blob-e35f2b24854f3f574febfc6de07e53c5c3d3efc7%252Fenvironments-how-it-works.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=5800d27555703bc585c58d9b99813b4c&sv=3)

Example: changes move from the development instance, after an optional review, to the Production environment's Git branch, then to the production instance

Changes move between instances through an environment:

1.  On the development instance, you promote changes to the Production environment.
    
2.  Optional: someone approves the changes in a [promotion review](https://docs.n8n.io/administer/environments/promotion-reviews)
     before they reach the environment.
    
3.  On the production instance, you apply the changes from the Production environment.
    

With Git-based promotion, promoting commits the changes to the Production environment's Git branch.

Concepts[](https://docs.n8n.io/administer/environments#concepts)

-----------------------------------------------------------------

### Environment[](https://docs.n8n.io/administer/environments#environment)

Conceptually, an environment is a step in your release process together with the instance that runs it, such as a staging or production instance. You promote changes to the next environment, and its instance applies them.

Technically, with Git-based promotion, promoted changes wait in a branch of a remote Git repository until the instance applies them. On the instance that promotes, the promote environment configuration points to that repository and branch, and defines how changes reach the branch, for example by pushing a feature branch or opening a merge request. On the instance that applies, the apply environment configuration points to the same repository and branch.

### Promote and apply[](https://docs.n8n.io/administer/environments#promote-and-apply)

Promote and apply are the two promotion actions:

*   **Promote** sends changes from your instance to an environment.
    
*   **Apply** brings changes from an environment into your instance.
    

The instance that promotes is the source instance, and the instance that applies is the target instance.

You can promote or apply at two levels:

*   **Project:** promotes or applies one team project. You choose which changes to include.
    
*   **Instance:** promotes or applies every team project on the instance.
    

An instance apply overwrites every team project on the instance to match the environment. It also deletes projects that aren't in the environment.

### What you promote[](https://docs.n8n.io/administer/environments#what-you-promote)

Workflows are the main unit of promotion. When you select workflows, n8n includes their dependencies: credentials, variables, data tables, and tags. n8n never writes credential secrets, data table rows, or executions to the repository. Variables travel with their values.

Promote and apply use [n8n packages](https://docs.n8n.io/build/manage-workflows/n8n-packages)
 to export and import content. To learn what Apply changes on an instance, see [Apply changes](https://docs.n8n.io/administer/environments/apply-changes#what-apply-changes-on-the-instance)
.

### Promotion model[](https://docs.n8n.io/administer/environments#promotion-model)

A promotion model is how changes travel between environments. n8n currently supports Git-based promotion, where changes travel through a Git repository. Other models, such as promoting directly from one instance to another, may follow. See [Git-based promotion](https://docs.n8n.io/administer/environments/git-based-promotion)
.

### Provider[](https://docs.n8n.io/administer/environments#provider)

A provider holds the details n8n uses to connect and authenticate to a Git host, such as an access token or an SSH key. Several environments can use the same provider. The Git provider type you choose decides which extra features you get, such as listing the repositories and branches the provider can access.

Environments and Environments (Classic)[](https://docs.n8n.io/administer/environments#environments-and-environments-classic)

-----------------------------------------------------------------------------------------------------------------------------

Environments replace [Environments (Classic)](https://docs.n8n.io/administer/use-source-control-and-environments)
, the earlier source control feature. An instance uses one or the other. See [Upgrade from Environments (Classic)](https://docs.n8n.io/administer/environments/upgrade-from-environments-classic)
.

In this section[](https://docs.n8n.io/administer/environments#in-this-section)

-------------------------------------------------------------------------------

*   [Plan your environments](https://docs.n8n.io/administer/environments/plan-your-environments)
    : choose how your instances and environments connect.
    
*   [Your first promotion](https://docs.n8n.io/administer/environments/first-promotion)
    : bring your work to a new target instance for the first time.
    
*   [Promote changes](https://docs.n8n.io/administer/environments/promote-changes)
    : send a project or the whole instance to an environment.
    
*   [Apply changes](https://docs.n8n.io/administer/environments/apply-changes)
    : bring changes from an environment into a project or the whole instance.
    
*   [Protect a production instance](https://docs.n8n.io/administer/environments/protect-a-production-instance)
    : limit changes in the UI on instances that only apply.
    
*   [Promotion reviews](https://docs.n8n.io/administer/environments/promotion-reviews)
    : approve promoted changes before they reach the environment's branch.
    
*   [Git-based promotion](https://docs.n8n.io/administer/environments/git-based-promotion)
    : how environments use Git, and the supported Git providers.
    
*   [Known limitations](https://docs.n8n.io/administer/environments/known-limitations)
    : what Environments don't support yet, and workarounds.
    
*   [Upgrade from Environments (Classic)](https://docs.n8n.io/administer/environments/upgrade-from-environments-classic)
    : compare the two versions, migrate your instances, and switch back.
    

Related resources[](https://docs.n8n.io/administer/environments#related-resources)

-----------------------------------------------------------------------------------

*   [Administer](https://docs.n8n.io/administer)
    
*   [Set permissions and roles](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac)
    
*   [n8n packages](https://docs.n8n.io/build/manage-workflows/n8n-packages)
    

[PreviousFollow best practices](https://docs.n8n.io/administer/manage-users-and-access/follow-best-practices)
[NextPlan your environments](https://docs.n8n.io/administer/environments/plan-your-environments)

Last updated 5 days ago

Was this helpful?