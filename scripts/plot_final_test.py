#!/usr/bin/env python3
"""Recreate the historical final-test figure from the included aggregate CSV.

This visualises previously saved results; it does not train models or reproduce
predictions. Requires matplotlib. Run from any working directory.
"""
from pathlib import Path
import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "v2_final_test_discrimination_with_clustered_ci.csv"
OUTPUT = ROOT / "figures" / "final_test_pr_auc.png"
LABELS = {
    "logistic_regression__bank_only": "Logistic regression · Bank",
    "logistic_regression__bank_plus_macro": "Logistic regression · Bank + macro",
    "random_forest__bank_only": "Random forest · Bank",
    "random_forest__bank_plus_macro": "Random forest · Bank + macro *",
    "xgboost__bank_only": "XGBoost · Bank",
    "xgboost__bank_plus_macro": "XGBoost · Bank + macro",
}
with SOURCE.open(newline="", encoding="utf-8-sig") as stream:
    records = {row["source_id"]: row for row in csv.DictReader(stream)}
assert set(LABELS).issubset(records), "Some required model results are missing"
models = list(LABELS)
values = [float(records[name]["pr_auc"]) for name in models]
lower = [float(records[name]["pr_auc_ci_lower"]) for name in models]
upper = [float(records[name]["pr_auc_ci_upper"]) for name in models]
assert all(0 <= lo <= v <= hi <= 1 for lo, v, hi in zip(lower, values, upper))
prevalences = {float(records[name]["prevalence"]) for name in models}
assert len(prevalences) == 1
prevalence = prevalences.pop()

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
fig, ax = plt.subplots(figsize=(10.8, 6.2), layout="constrained")
fig.set_facecolor("#ffffff")
ypos = list(range(len(models)))
for y, name, v, lo, hi in zip(ypos, models, values, lower, upper):
    color = "#087e86" if name == "random_forest__bank_plus_macro" else "#486783"
    ax.hlines(y, lo, hi, color=color, lw=2.4, alpha=.85)
    ax.plot(v, y, "o", color=color, markersize=8)
    ax.annotate(f"{v:.3f}", (v, y), xytext=(8, 8), textcoords="offset points", fontsize=9, color=color)
ax.axvline(prevalence, color="#bf8a32", linestyle="--", lw=1.4)
ax.set_yticks(ypos, [LABELS[name] for name in models])
ax.invert_yaxis()
ax.set_xlim(0, .37)
ax.set_xlabel("Precision–recall AUC (higher is better)", labelpad=10)
ax.xaxis.set_major_formatter(FormatStrFormatter("%.2f"))
ax.xaxis.grid(True, color="#e5eaef")
ax.set_axisbelow(True)
for spine in ("top", "right", "left"):
    ax.spines[spine].set_visible(False)
ax.tick_params(axis="y", length=0)
ax.set_title("How did the models perform on later data?", loc="left", fontsize=17, fontweight="bold", color="#142e45", pad=18)
fig.text(.13, -.015, "2020 Q1–2025 Q2  |  92,229 bank-quarters  |  13 failed banks", fontsize=10, color="#43596b")
fig.text(.13, -.045, "Points: PR-AUC   •   Lines: 95% bank-clustered bootstrap intervals   •   Dashed: prevalence 0.000434", fontsize=9, color="#43596b")
fig.text(.13, -.075, "* Selected during validation. Intervals are wide; model differences are uncertain.", fontsize=9, color="#43596b")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUTPUT, dpi=180, bbox_inches="tight", facecolor="white")
print(f"Saved {OUTPUT.relative_to(ROOT)} from {SOURCE.relative_to(ROOT)}")
