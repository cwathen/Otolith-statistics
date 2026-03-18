import pandas as pd
from scipy.stats import shapiro, kstest, ttest_rel
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import shapiro, ttest_rel, probplot
from statsmodels.stats.diagnostic import lilliefors

# Load data
df = pd.read_csv("data/otolith_data.csv") #input the data path here from the supplemental excel file, this best fits with the matched and unmatched workbooks in that file. Adjust the path and filename as needed.
df = df.dropna(subset=["NoResinSr", "ResinSr"])

# Unique Otoliths (you can limit to first 5 for space)
otoliths = df["Otolith"].unique()[:5]

# Create figure with subplots: 2 columns (hist+KDE, Q-Q) per Otolith
fig, axes = plt.subplots(len(otoliths), 2, figsize=(12, 4*len(otoliths)))

if len(otoliths) == 1:
    axes = np.array([axes])  # Ensure axes is 2D for consistent indexing

for i, otolith in enumerate(otoliths):
    df_pair = df[df["Otolith"] == otolith].copy()
    df_pair["Sr_Diff"] = df_pair["NoResinSr"] - df_pair["ResinSr"]
    
    # Histogram + KDE
    sns.histplot(df_pair["Sr_Diff"], kde=True, ax=axes[i,0])
    axes[i,0].set_title(f"Otolith {otolith} - Distribution of Sr_Diff")
    axes[i,0].set_xlabel("Sr_Diff")
    axes[i,0].set_ylabel("Density")
    
    # Q-Q plot
    probplot(df_pair["Sr_Diff"], dist="norm", plot=axes[i,1])
    axes[i,1].set_title(f"Otolith {otolith} - Q-Q Plot")

plt.tight_layout()
plt.show()
