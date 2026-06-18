import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("decision_quality_results.json")


sns.countplot(x="budget_violation", data=df)
plt.title("Budget Violation Frequency")
plt.xlabel("Budget Violation")
plt.ylabel("Count")
plt.savefig("budget_violation_frequency.png")



