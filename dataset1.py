# フォント設定
import matplotlib
import matplotlib.font_manager as font_manager
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_prop = font_manager.FontProperties(fname = font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 真値
def true_function(x):
    x = np.array(x)
    return np.sin(np.pi * x * 0.8) * 10

# 演習1.1
def ex1_1(filename="ex1.1.png"):
    x = np.linspace(-1, 1, 100)
    y = true_function(x)
    plt.figure()
    plt.plot(x, y, label="y = 10sin(0.8πx)")
    plt.xlim(-1, 1)
    plt.legend()
    plt.savefig(filename)
    plt.show()

# 観測点設定
def create_dataset(n=20, seed=0):
    np.random.seed(seed)
    x_obs = np.random.uniform(-1, 1, n)
    y_true = true_function(x_obs)
    # ノイズ作成
    noise = np.random.normal(0.0, np.sqrt(2.0), n) / 2
    y_obs = y_true + noise
    # DataFrame型
    DF = pd.DataFrame({"観測点": x_obs, "真値": y_true, "観測値": y_obs})

    return DF

# 演習1.2
def ex1_2(DF, filename="ex1.2.png"):
    x = np.linspace(-1, 1, 100)
    y = true_function(x)
    plt.figure()
    plt.plot(x, y, label="y = 10sin(0.8πx)")
    plt.scatter(DF["観測点"], DF["真値"], label="サンプル集合", s=50)
    plt.xlim(-1, 1)
    plt.legend()
    plt.savefig(filename)
    plt.show()

# 演習1.3
def ex1_3(DF, filename="ex1.3.png"):
    x = np.linspace(-1, 1, 100)
    y = true_function(x)
    plt.figure()
    plt.plot(x, y, label="y = 10sin(0.8πx)")
    plt.scatter(DF["観測点"], DF["真値"], label="サンプル集合", s=50)
    plt.scatter(DF["観測点"], DF["観測値"], label="観測値",s=50)
    plt.xlim(-1, 1)
    plt.legend()
    plt.savefig(filename)
    plt.show()

# 演習1.4(TSV形式で保存)
def ex1_4(DF, filename="ex1.4.tsv"):
    DF.to_csv("ex1.4.tsv", sep="\t", index=False)

# 演習1.5(TSVをDFで読み込み)
def ex1_5(filename="ex1.4.tsv"):
    DF = pd.read_csv("ex1.4.tsv", sep="\t")
    return DF

# 演習1.8(戦型回帰モデルの準備)
from sklearn.linear_model import LinearRegression
def ex1_8():
    model = LinearRegression()
    return model