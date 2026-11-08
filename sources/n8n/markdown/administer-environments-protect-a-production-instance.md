For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/administer/environments/protect-a-production-instance.md)
.

On instances that only apply changes, such as production, turn on **Protected instance** in **Settings** > **Environments**.

**Preview status**

Environments are in Preview and may change in future releases. Try them on test instances before you set them up for your production instances.

**Protected instance** stops people from doing these things in the UI:

*   Edit workflows, or create workflows, credentials, projects, folders, variables, or data tables.
    
*   Run workflows manually. Published workflows still run from their triggers.
    
*   Change data table columns.
    

People can still:

*   Edit existing credentials, variable values, and data table rows.
    
*   Create missing credentials and variables while they resolve Apply blockers.
    
*   Add missing projects from the environment they apply from.
    
*   Publish and unpublish workflows.
    
*   Promote and apply.
    

The public API still allows most other changes.

Environments (Classic) uses the same setting. Turning it on or off changes it for both.

Related resources[](https://docs.n8n.io/administer/environments/protect-a-production-instance#related-resources)

-----------------------------------------------------------------------------------------------------------------

*   [Environments](https://docs.n8n.io/administer/environments)
    
*   [Plan your environments](https://docs.n8n.io/administer/environments/plan-your-environments)
    
*   [Your first promotion](https://docs.n8n.io/administer/environments/first-promotion)
    
*   [Promote changes](https://docs.n8n.io/administer/environments/promote-changes)
    
*   [Apply changes](https://docs.n8n.io/administer/environments/apply-changes)
    
*   [Promotion reviews](https://docs.n8n.io/administer/environments/promotion-reviews)
    
*   [Git-based promotion](https://docs.n8n.io/administer/environments/git-based-promotion)
    
*   [Known limitations](https://docs.n8n.io/administer/environments/known-limitations)
    
*   [Upgrade from Environments (Classic)](https://docs.n8n.io/administer/environments/upgrade-from-environments-classic)
    

[PreviousApply changes](https://docs.n8n.io/administer/environments/apply-changes)
[NextPromotion reviews](https://docs.n8n.io/administer/environments/promotion-reviews)

Last updated 5 days ago

Was this helpful?