import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# İkinci ve üçüncü parametreleri düzeltilmiş haliyle kullanın
data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], 2000)
data = pd.DataFrame(data, columns=['x', 'y'])

# Histogramları çizmek için matplotlib.pyplot.hist kullanın
plt.hist(data["x"], alpha=0.5)
plt.hist(data["y"], alpha=0.5)
plt.show()
