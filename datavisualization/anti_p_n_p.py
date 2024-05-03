#図より反分極状態は分極状態よりも常に安定していることがわかる（エネルギーが小さいから）

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 自由エネルギー関数の定義
def free_energy(Q, q, t):
    return (1 + t) * Q**2 + t * q**2 + Q**4 + q**4 + 6 * Q**2 * q**2

# 温度範囲の設定
t_values = np.linspace(-3.0, 1.0, 400)

# 各状態に対するQ, qの計算
Q_para = np.zeros_like(t_values)  # 非分極状態
q_para = np.zeros_like(t_values)

Q_ferro = np.sqrt(-(1 + t_values) / 2)  # 分極状態
q_ferro = np.zeros_like(t_values)

Q_antiferro = np.zeros_like(t_values)  # 反分極状態
q_antiferro = np.sqrt(-t_values / 2)

# 自由エネルギーの計算
F_para = free_energy(Q_para, q_para, t_values)
F_ferro = free_energy(Q_ferro, q_ferro, t_values)
F_antiferro = free_energy(Q_antiferro, q_antiferro, t_values)

# 3Dプロットの作成
fig = plt.figure(figsize=(14, 6))
ax = fig.add_subplot(121, projection='3d')

# 非分極状態のプロット
ax.plot(t_values, Q_para, q_para, label='Non-polarized State', color='blue')

# 分極状態のプロット
ax.plot(t_values[t_values < -1], Q_ferro[t_values < -1], q_ferro[t_values < -1], label='Polarized State', color='red')

# 反分極状態のプロット
ax.plot(t_values[t_values < 0], Q_antiferro[t_values < 0], q_antiferro[t_values < 0], label='Antiferroelectric State', color='green')

ax.set_xlabel('Temperature (t)')
ax.set_ylabel('Q')
ax.set_zlabel('q')
ax.legend()

# 自由エネルギーのプロット
ax2 = fig.add_subplot(122)
ax2.plot(t_values, F_para, label='Non-polarized State', color='blue')
ax2.plot(t_values[t_values < -1], F_ferro[t_values < -1], label='Polarized State', color='red')
ax2.plot(t_values[t_values < 0], F_antiferro[t_values < 0], label='Antiferroelectric State', color='green')
ax2.set_xlabel('Temperature (t)')
ax2.set_ylabel('Free Energy')
ax2.legend()

plt.show()