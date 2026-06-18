import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("C:\\Users\\bhashitha\\OneDrive\\Documents\\4th-yr-1st-sem\\research\\tourism research\\results\\workflow_stability_results.json")

sns.countplot(x="converged", data=df)
plt.title("Negotiation Convergence Rate")
plt.xlabel("Converged")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("negotiation_convergence_rate.png")