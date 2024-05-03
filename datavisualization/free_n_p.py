import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 自由エネルギー関数
def free_energy(Q, q, t):
    return (1 + t) * Q**2 + t * q**2 + Q**4 + q**4 + 6 * Q**2 * q**2

# 温度範囲
t_values = np.linspace(-50, 10, 400)

# 各状態に対するQとqの値を計算
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
fig = plt.figure(figsize=(14, 7))

# 非分極状態と分極状態のプロット
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot(t_values, Q_para, F_para, label='Non-polarized')
ax1.plot(t_values, Q_ferro, F_ferro, label='Polarized')
ax1.set_xlabel('t')
ax1.set_ylabel('Q')
ax1.set_zlabel('Free Energy F')
ax1.legend()

# 反分極状態のプロット
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot(t_values, q_antiferro, F_antiferro, label='Anti-polarized')
ax2.set_xlabel('t')
ax2.set_ylabel('q')
ax2.set_zlabel('Free Energy F')
ax2.legend()

plt.show()

# 非対称分極（フェリ電気）状態の4次元表現
Q_ferrie = np.sqrt((1 - 2 * t_values) / 4)
q_ferrie = np.sqrt((-3 - 2 * t_values) / 4)
F_ferrie = free_energy(Q_ferrie, q_ferrie, t_values)

fig, ax = plt.subplots()
sc = ax.scatter(t_values, Q_ferrie, c=F_ferrie, cmap='viridis', label='Q vs t')
cb = plt.colorbar(sc, ax=ax)
cb.set_label('Free Energy F')
ax.set_xlabel('t')
ax.set_ylabel('Q')
ax.legend()
plt.title('Ferroelectric (Ferrielectric)')
plt.show()