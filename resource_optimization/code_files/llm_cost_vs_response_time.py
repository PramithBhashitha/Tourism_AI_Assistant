import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("resource_optimization_results.json")

sns.scatterplot(x="llm_cost_usd", y="workflow_runtime_ms", data=df)
plt.title("LLM Cost vs Workflow Runtime")
plt.xlabel("LLM Cost (USD)")
plt.ylabel("Runtime (ms)")
plt.tight_layout()
plt.savefig("llm_cost_vs_runtime.png")