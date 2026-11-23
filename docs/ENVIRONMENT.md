# Runtime and environment inventory

The notebooks were written around Google Colab and Google Drive. A dependency scan of the supplied source identified `numpy`, `pandas`, `pyarrow`, `openpyxl`, `requests`, `urllib3`, `tqdm`, `scikit-learn`, `xgboost`, `scipy`, `matplotlib`, `joblib` and IPython / Jupyter. Python standard-library imports are also used. Google Colab supplies `google.colab`; it is not an ordinary portable dependency for a local Jupyter environment.

This is an inventory, not a validated lockfile. Exact Python and package versions, compatibility and installation commands remain unverified. Notebooks 03–05 include conditional `pip install pyarrow` code, and Notebook 14 refers to installing XGBoost if missing. Review all such commands before execution; reproducible environments should install dependencies explicitly rather than silently modifying a running runtime.

Several later notebooks recognise `DISSERTATION_PROJECT_ROOT` and `V2_CONFIG_PATH`. Earlier notebooks and the original configuration also contain hard-coded Colab Drive paths. Setting these variables is not sufficient to guarantee portability. Notebook 04 and parts of Notebook 17 may depend on external FDIC data or API access; data availability, response changes and snapshots must be checked.

The saved Phase 4 summary reports a Random Forest development run of about 239 minutes in its original environment; runtimes depend on hardware and data access. The notebooks and data were not rerun for this repository draft.
