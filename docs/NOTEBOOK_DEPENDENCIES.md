# Notebook dependencies and handoffs

Review based on the supplied notebook source, saved outputs and user-provided Version 2 configuration. The notebooks have not been rerun as a complete pipeline. Paths and filenames below describe what the supplied notebooks reference; do not assume these references resolve automatically.

| Stage | Inputs to locate | Outputs consumed later |
| --- | --- | --- |
| 01–02 | Raw FFIEC, FDIC and macro data in the original `Data Final/Raw Data` layout | V2 config, raw file inventory and FFIEC code inventory |
| 03–05 | FFIEC source and code mappings; historical FDIC classifications | Harmonised and commercial-bank panels, `bank_predictor_source_v2.parquet`, `locked_v1_bank_feature_manifest_v2.csv` |
| 06–07 | FDIC input workbook; commercial-bank panel and CERT–IDRSSD crosswalk | Cleaned genuine-failure data and one-year target parquet |
| 08–09 | Raw macro series; target; bank predictor source and identifier-adjudication records | Lagged macro handoff and `v2_final_modelling_panel_2001Q2_2025Q2.parquet` |
| 10–11 | Modelling panel and Phase 1 locked feature manifest | Chronological row membership, selection rule and bank-only / bank-plus-macro feature manifests |
| 12–14 | Modelling panel, fold membership, feature manifests and selection rule | Configuration files, selected validation predictions and preprocessing manifests |
| 15 | Selected configuration, prediction and preprocessing handoffs from all three model notebooks | `v2_model_lock_manifest.json` and locked thresholds |
| 16 | V2 modelling panel, chronological design, model lock and validation outputs | Final-test aggregate discrimination, capacity and threshold tables; Notebook 16 → 17 handoff |
| 17 | Notebook 16 handoff and outputs; archived V1 artifacts for sensitivity; crisis inputs | Robustness tables, figures and final dissertation handoff |

## Known compatibility checks

1. Notebooks 01–05 write under `Data Final/Version 2 Main Analysis`, while the saved outputs of Notebooks 06–09 refer to a shared config and handoffs under `Data Final/Notebook Outputs/v2_bank_lag1_main`. Multiple roots are deliberate in parts of the original project but exact file lineage is not proven by matching counts.
2. Notebook 07 references `ffiec_commercial_bank_panel_2001_2026.csv` and `cell_05_fdic_cert_idrssd_crosswalk.csv` in the root-level Notebook 04 folder. The supplied V2 Notebook 04 names its principal output `commercial_bank_ffiec_panel_v2.parquet` and its crosswalk `cert_idrssd_crosswalk_v2.csv`. Compare contents, schemas, keys and provenance before creating an adapter or changing a path; do not assume the names are aliases.
3. Notebook 09 references `ffiec_commercial_bank_full_working_panel_2001Q1_2026Q1.parquet` and a predictor-panel CSV in a root-level Notebook 05 folder, whereas supplied Notebook 05 produces `bank_predictor_source_v2.parquet` under Version 2. Confirm equivalence and expected schema before connecting these files.
4. Later notebooks can resolve candidate roots or use `DISSERTATION_PROJECT_ROOT` and `V2_CONFIG_PATH`, but the supplied Version 2 config itself defines a hard-coded Colab Drive project root. Notebooks 01–05 also contain explicit `/content/drive/MyDrive/Data Final` assumptions. Environment variables alone have not been verified to make the full workflow portable.
5. Notebook 17 reads archived Version 1 data for sensitivity. Its V1 and V2 comparison is non-causal and is not required for reading the main final-test aggregate tables. Preserve the original input hashes and audit metadata if rerunning.

## Immediate evidence gaps

- The exact configuration files as stored on Drive and the referenced root-level NB04 / NB05 handoff file schemas and checksums. Both configurations have been provided as pasted text and compared; byte-level identity has not been verified.
- Verified source snapshots, the model-panel inputs and the selected intermediate artifacts (or the ability to regenerate them).
- Exact software environment; Notebook 16 references `cell_01_software_versions.csv`, which should be inspected if available.

Do not overwrite original Google Drive files during testing; work on a separate copy. Do not infer that a full independent replication is complete from saved PASS outputs alone.

## Configuration comparison (pasted by author)

The root config describes an earlier layout and has `RANDOM_SEED = 42` and training starting in 2001Q1. The Version 2 config has `RANDOM_SEED = 20260804`, specifies exact previous-quarter bank inputs, and starts the reference calendar in 2001Q2. Both use a 365-day target, the same evaluation windows and eligible N/NM/SM bank classes. They should not be swapped blindly.

The executed Notebook 06 output says it loaded the root config; Notebook 06 falls back to Version 2 defaults for fields absent from that file. Notebooks 07–09 similarly look for `V2_CONFIG_PATH`, then root-level `config_v2.py` / `config.py`, and implement some Version 2 timing in notebook code or defaults. Thus using the root config in those notebooks does not itself prove an incorrect analysis. Later notebooks normally resolve the V2 config. Do not assume that setting an environment variable fully fixes all historical references or seed usage. Validate each notebook and compare input/output hashes and schemas before changing anything.

## Notebook 04 root-output reconciliation

The author-provided `notebook_04_final_summary.csv` identifies `ffiec_commercial_bank_panel_2001_2026.csv` as its authoritative output: 666,699 input rows, 600,618 retained, 66,072 noncommercial and 9 unmatched exclusions, 9,699 RSSDIDs, 9,679 CERTs and 101 quarters. These counts agree with the supplied V2 Phase 1 workbook. The root crosswalk summary reports 11,319 historical CERT–IDRSSD pairs, with 80 CERTs linked to multiple historical IDRSSDs and 56 IDRSSDs linked to multiple CERTs; these two ambiguity counts match the V2 Phase 1 audit. Matching totals do not establish row-level equality, source hashes or identical schema; no identity claim is made. The root-level panel is reported as 164.2 MB and has not been uploaded or inspected.

## Root Notebook 05 handoff reviewed

The author-provided root Notebook 05 handoff summary reports 600,618 observations, 101 quarters, a 22-column compact panel (three identifiers and 19 candidate predictors), and an 87-column working panel. The summary states no imputation, winsorisation or scaling was applied at this stage. This agrees in broad row and timing coverage with the V2 Phase 1 audit, but does not establish row-level equality.

Comparing the root candidate manifest with the 19 bank inputs in the selected V2 model lock after removing the `_lag1` suffix yields 18 shared names. The root candidate list includes `loans_to_deposits`, which is not in the V2 model lock; the V2 lock includes `insufficient_history_5q`, which is not in this candidate manifest. These files describe different pipeline stages: a candidate list is not the final selected model feature manifest. This comparison does not contradict Notebook 17's comparison of the V1 and V2 final locked feature sets. The compact panel and working-panel schemas and values have not been compared directly with the V2 source.
