# Notebook dependencies

The notebooks were written for Google Colab and depend on data and intermediate files from the original Google Drive project. The full workflow has not been independently rerun from this repository.

| Notebooks | Main inputs | Main outputs |
| --- | --- | --- |
| 01–05 | Raw FFIEC, FDIC and economic data | Cleaned commercial-bank data and bank predictors |
| 06–09 | Failure records, bank data and economic indicators | One-year target and final modelling dataset |
| 10–11 | Modelling dataset and feature information | Time-based folds and selected features |
| 12–14 | Modelling dataset, folds and selected features | Trained specifications and validation predictions |
| 15 | Validation predictions and model settings | Model comparison and locked settings |
| 16 | Modelling dataset, time splits and locked settings | Final-test results |
| 17 | Final-test outputs and archived analysis files | Robustness results and figures |

Some notebooks refer to different source folders and file names. The original project used a main configuration and an analysis-specific configuration. These contain different timing and random-seed settings, so they should not be substituted without checking each notebook. Matching row counts across saved summaries do not establish that datasets are identical.

The notebooks retain the original file paths and names because changing them could break their dependencies. To reproduce the full workflow, obtain the original input data and intermediate handoffs, review the configuration, and run the notebooks in order. See [REPRODUCIBILITY.md](REPRODUCIBILITY.md) for the remaining checks.

Notebook 17 compares the main results with an earlier specification. This is a sensitivity comparison and does not establish a causal effect.
