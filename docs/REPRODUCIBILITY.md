# Reproducing the research

The research notebooks were originally run in Google Colab using files stored in Google Drive. The full workflow has not been independently rerun from this repository. The included chart can be recreated separately from the aggregate results.

To attempt a full rerun:

1. Obtain the original input snapshots and intermediate handoff files, or regenerate the handoffs from the original inputs. Check the data sources and sharing conditions.
2. Review the configuration and the file paths described in [NOTEBOOK_DEPENDENCIES.md](NOTEBOOK_DEPENDENCIES.md). Some notebooks expect files in different folders or under different names.
3. Set up the required libraries. The exact package versions used in the original run have not been verified; see [ENVIRONMENT.md](ENVIRONMENT.md).
4. Run the notebooks in order using a separate working copy. Check the audit messages before proceeding between stages.
5. Compare the dataset counts, selected model, final-test metrics and capacity results with the submitted dissertation.

The public copies use simpler explanations and code headings. Saved outputs and execution counts were removed. The code was checked against the supplied notebooks, but the full models have not been rerun during this cleanup.
