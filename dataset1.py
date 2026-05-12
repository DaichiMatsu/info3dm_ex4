# フォント設定
import matplotlib
import matplotlib.font_manager as font_manager
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_prop = font_manager.FontProperties(fname = font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 観測点設定
np.random.seed(0)
n = 20
x_obs = np.random.uniform(-1, 1, n)

# 真値
def true_function(x):
    x = np.array(x)
    return np.sin(np.pi * x * 0.8) * 10

y_true = true_function(x_obs)

# ノイズ作成
noise = np.random.normal(0.0, np.sqrt(2.0), 20) / 2

# DataFrame型
DF = pd.DataFrame({"観測点": x_obs, "真値": y_true})
DF["観測値"] = DF["真値"] + noise

# サンプル集合をプロット
x = np.linspace(-1, 1, 100)
y = true_function(x)
plt.plot(x, y, label="y = 10sin(0.8πx)")
plt.scatter(DF["観測点"], DF["真値"], label="サンプル集合", s=50)
plt.scatter(DF["観測点"], DF["観測値"], label="観測値",s=50)
plt.xlim(-1, 1)
plt.legend()
plt.savefig("ex1.3.png")
plt.show()

# TSV形式で保存
DF.to_csv("ex1.4.tsv", sep="\t", index=False)

DF = pd.read_csv("ex1.4.tsv", sep="\t")