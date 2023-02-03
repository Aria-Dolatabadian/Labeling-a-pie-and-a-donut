import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
recipe = ["375 RLK", "75 RLP", "250  CNL", "300  TNL"]
data = [float(x.split()[0]) for x in recipe]
ingredients = [x.split()[-1] for x in recipe]
def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)
wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))
ax.legend(wedges, ingredients,
          title="RGAs",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
plt.setp(autotexts, size=8, weight="bold")
ax.set_title("RGAs number and percentage")
plt.show()
