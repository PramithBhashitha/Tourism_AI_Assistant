import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("negotiation_efficiency_results.json")


sns.scatterplot(x="negotiation_rounds", y="proposal_score_final", data=df)
plt.title("Negotiation Rounds vs Final Proposal Score")
plt.xlabel("Rounds")
plt.ylabel("Final Proposal Score")
plt.tight_layout()
plt.savefig("rounds_vs_proposal_score.png")