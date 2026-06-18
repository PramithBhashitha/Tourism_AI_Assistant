import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("decision_quality_results.json")

sns.scatterplot(x="negotiation_rounds", y="constraint_violations_count", data=df)
plt.title("Negotiation Rounds vs Constraint Violations")
plt.xlabel("Negotiation Rounds")
plt.ylabel("Constraint Violations")
plt.tight_layout()
plt.savefig("negotiation_vs_violations.png")