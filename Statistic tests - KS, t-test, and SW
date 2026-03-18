import pandas as pd
from scipy.stats import shapiro, kstest, ttest_rel
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import shapiro, ttest_rel, probplot
from statsmodels.stats.diagnostic import lilliefors

# Load data
df = pd.read_csv("data/otolith_data.csv") #input the data path here from the supplemental excel file, this best fits with the matched and unmatched workbooks in that file. Adjust the path and filename as needed.

# Drop missing values
df = df.dropna(subset=["NoResinSr", "ResinSr"])

# Select otolith
Otolith = 5 #Change this based on the pair you want to analyze
df_pair = df[df["Otolith"] == Otolith].copy()

# Columns you want stats for 
columns = ["NoResinSr", "ResinSr"] 

# Build a summary table
summary = {}
for col in columns:
    summary[col] = {
        "Avg": df_pair[col].mean(),
        "Std": df_pair[col].std()*2,
        "Min": df_pair[col].min(),
        "Max": df_pair[col].max()
    }
summary_df = pd.DataFrame(summary)

print(f"Stats for Otolith {Otolith}:")
print(summary_df.round(4))


# Compute differences
df_pair["Sr_Diff"] = df_pair["NoResinSr"] - df_pair["ResinSr"]

# Shapiro-Wilk
shapiro_stat, shapiro_p = shapiro(df_pair["Sr_Diff"])
print(f"Shapiro-Wilk: stat={shapiro_stat:.4f}, p={shapiro_p:.4f}")

# Paired t-test
t_stat, t_p = ttest_rel(df_pair["ResinSr"], df_pair["NoResinSr"])
print(f"Paired t-test: stat={t_stat:.4f}, p={t_p:.4f}")

# Lilliefors test (SPSS-style K-S)
ks_stat, ks_p = lilliefors(df_pair["Sr_Diff"])
print(f"K-S Test (Lilliefors / SPSS): stat={ks_stat:.4f}, p={ks_p:.4f}")

# Q-Q plot
probplot(df_pair["Sr_Diff"], dist="norm", plot=plt)
plt.title(f'Q-Q Plot of Sr_Diff for Otolith {Otolith}')
plt.show()

# Distribution
sns.histplot(df_pair["Sr_Diff"], kde=True)
plt.title(f"Distribution of Sr_Diff for Otolith {Otolith}")
plt.xlabel("Sr_Diff (NoResin - Resin)")
plt.show()