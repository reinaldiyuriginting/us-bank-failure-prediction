# Reproducibility and publication checklist

This is a working review package, not an independently verified pipeline.

1. Confirm the notebook versions and connect every phase handoff. Phase 1 uses a Version 2 Main Analysis path; Phase 2 and later refer to another Data Final root for some inputs. Verify actual lineage, hashes and config generation.
2. Collect the raw source files, shared configuration, feature manifests, selected model settings, validation predictions and model-lock handoffs. Verify rights before distributing data.
3. Review all code, notebook metadata and dependency-installation commands for privacy and safety. The outputs have been removed, but paths and operational assumptions remain. Check whether institutional bank-level audit files should be shared.
4. Capture a tested environment and actual package versions; add a requirements file only after checking the executed environment.
5. Run from clean inputs in a controlled environment and compare sample counts, selected model, test metrics and capacity calculations with the submitted dissertation. Do not claim reproduction before this succeeds.
6. Check data access conditions, project licence, third-party attribution and university policies; do not publish the dissertation without confirming permission.
7. Add Medium and dashboard links only after those assets exist.

Execution note: Notebook 01 and Notebook 13 had saved outputs but some missing execution counts in the supplied originals. Preserve originals privately; these review copies deliberately have all outputs and counts cleared.

## Notebook cleanup

All 17 notebooks have standardised code-cell headings. Conversational instructions to send audit outputs were reworded as review instructions. Executable logic, model settings, data processing and validation gates were preserved; Python syntax-tree comparisons against the supplied originals confirmed only print-message strings were changed. Saved outputs and execution counts remain cleared. Original Colab Drive path assumptions remain and the full pipeline has not been rerun.
