import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 正規化された自由エネルギー関数
def normalized_free_energy(Q, q, t, e):
    a = (1 + t) * Q**2 + t * q**2 + Q**4 + q**4 + 6 * Q**2 * q**2 - e * Q
    return a

# Qとqの範囲を定義
Q_range = np.linspace(0, 2.0, 400)
q_range = np.linspace(0,2.0, 400)

# 温度と外部場の値を設定
t_values = [-1.0]  # 温度の例
e_values = [0,0.5,1.0,1.5]

# 図を描画
fig = plt.figure(figsize=(20, 20))

# 凡例用のラベルとカラーを格納するリスト
labels = []
colors = []

# 異なる温度と外部場の値に対して自由エネルギーの等高線図を生成
for i, t in enumerate(t_values):
    for j, e in enumerate(e_values):
        ax = fig.add_subplot(len(t_values), len(e_values), i * len(e_values) + j + 1, projection='3d')

        # Qとqのメッシュグリッドを生成
        Q, q = np.meshgrid(Q_range, q_range)

        # 自由エネルギーを計算
        a = normalized_free_energy(Q, q, t, e)

        # 自由エネルギーが最小のインデックスを見つける
        min_index = np.argmin(a)
        min_coords = np.unravel_index(min_index, Q.shape)

        # 等高線図をプロット
        ax.contour3D(Q, q, a, 50, cmap='viridis')

        # 最小自由エネルギーの点をプロット
        min_Q, min_q, min_a = Q[min_coords], q[min_coords], a[min_coords]
        ax.scatter(min_Q, min_q, min_a, color='red', s=50)

        if i == 0 and j == 0:  # 凡例は一度だけ追加する
            colors.append('red')

        # タイトルと軸ラベルを設定
        ax.set_title(f't={t}, e={e}')
        ax.set_xlabel('Q')
        ax.set_ylabel('q')
        ax.set_zlabel('a')


plt.tight_layout()
plt.show()