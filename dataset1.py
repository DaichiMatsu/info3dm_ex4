# フォント設定
import matplotlib
import matplotlib.font_manager as font_manager
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_prop = font_manager.FontProperties(fname = font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()
import numpy as np

def true_function(x):
    x = np.array(x)
    return np.sin(np.pi * x * 0.8) * 10

# x=0の時のyの値のテスト
y = true_function(0)
print(y)


# -1<=x<=1のxyグラフ
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
y = true_function(x)

plt.plot(x, y, label="y = 10sin(0.8πx)")
plt.xlim(-1, 1)
plt.legend()
plt.savefig("ex1.1.png")
plt.show()
