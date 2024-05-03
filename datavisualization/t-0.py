import numpy as np
import matplotlib.pyplot as plt

# 正規化された自由エネルギー関数
def normalized_free_energy(Q, q, t, e):
    return (1 + t) * Q**2 + t * q**2 + Q**4 + q**4 + 6 * Q**2 * q**2 - e * Q

# Qとqの範囲を定義
Q_range = np.linspace(0, 1.0, 400)
q_range = np.linspace(0, 1.0, 400)

# 温度と外部場の値を設定
t = -1/10  # 温度の例
e_values = np.linspace(-1.5, 1.5, 200)  # 外部電場の範囲

# 安定点を格納するリスト
stable_points = []

# 異なる外部電場の値に対して自由エネルギーの最小値を見つける
for e in e_values:
    Q, q = np.meshgrid(Q_range, q_range)
    a = normalized_free_energy(Q, q, t, e)
    min_index = np.unravel_index(np.argmin(a), Q.shape)
    min_Q = Q[min_index]
    min_q = q[min_index]
    stable_points.append((min_Q, min_q))

# 安定点の軌跡をプロット
stable_points = np.array(stable_points)
plt.figure(figsize=(8, 6))
plt.plot(stable_points[:, 0], stable_points[:, 1], 'o-', color='blue')
plt.title('Stable Points Trajectory on Q-q Plane , t=-0.1')
plt.xlabel('Q')
plt.ylabel('q')
plt.grid(True)
plt.show()