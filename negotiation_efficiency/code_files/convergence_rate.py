import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("negotiation_efficiency_results.json")

sns.countplot(x="converged", data=df)
plt.title("Convergence Success Rate")
plt.xlabel("Converged")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("convergence_success_rate.png")