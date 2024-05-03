##これは反分極最小値といえるのだろうか。

import numpy as np
import matplotlib.pyplot as plt

# 正規化された自由エネルギー関数
def normalized_free_energy(Q, q, t, e):
    a = (1 + t) * Q**2 + t * q**2 + Q**4 + q**4 + 6 * Q**2 * q**2 - e * Q
    return a

# qの範囲を定義
# q_range = np.linspace(-1.16, 1.16, 400)
q_range = np.linspace(-5, 5, 400)


# 温度と外部場の値を設定
# t_values = [-3.0,-2.0, -1.5, -1, 0, 2.0, -10]  # 温度の例
t_values = [0,-5,-10]
e_values = [0]  # 外部場の例

# 図を描画
plt.figure(figsize=(10, 6))

# 異なる温度に対して自由エネルギーのプロットを生成
for t in t_values:
    # Qは0として固定
    Q = 0
    # 自由エネルギーを計算
    a = normalized_free_energy(Q, q_range, t, e_values[0])
    # プロット
    plt.plot(q_range, a, label=f't={t}')

    # 自由エネルギーの最小値を見つける
    min_index = np.argmin(a)
    min_q = q_range[min_index]
    min_a = a[min_index]

    # 最小値をプロット
    plt.scatter(min_q, min_a, color='red', s=50)  # 赤い点で最小値を表示

# タイトルと軸ラベルを設定
plt.title('')
plt.xlabel('q')
plt.ylabel('Free Energy')
plt.legend()

plt.show()