import numpy as np
import matplotlib.pyplot as plt

def antiferroelectric_phase(Q, t):
    return 2 * (1 - 2 * t) * Q - 32 * Q**3

def paraelectric_phase(Q, t):
    return 2 * (1 + t) * Q + 4 * Q**3

# Qの範囲を定義
Q_range = np.linspace(0, 0.6, 400)

# 温度の値を設定
t_values = [0, -1/6, -1/2, -1, -3/2]
t_labels = ['0', '-1/6', '-1/2', '-1', '-3/2']  # 温度のラベル

# プロットの設定
plt.figure(figsize=(10, 8))

for t in t_values:
    # 反強誘電相と常誘電相のeを計算
    e_ferro = antiferroelectric_phase(Q_range, t)
    e_para = paraelectric_phase(Q_range, t)

    plt.plot(Q_range, e_ferro, label=f't={label},(anti)', linestyle='--')
    plt.plot(Q_range, e_para, label=f't={label},(para)')

# グラフのタイトルと軸ラベルを設定
plt.title('Positive side of hysteresis loop at various temperatures')
plt.xlabel('POLARIZATION Q')
plt.ylabel('EXTERNAL FIELD e')

# y軸の範囲を設定
plt.ylim(-0.5, 1.6)

plt.grid(True)
plt.legend()
plt.show()