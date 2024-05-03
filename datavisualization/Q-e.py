import numpy as np
import matplotlib.pyplot as plt

def antiferroelectric_phase(Q, t):
    return 2 * (1 - 2 * t) * Q - 32 * Q**3

# 常誘電相の関数
def paraelectric_phase(Q, t):
    return 2 * (1 + t) * Q + 4 * Q**3

# Qの範囲を定義
Q_range = np.linspace(0, 0.4, 400)

# 温度の値を設定
t_values = [-1/3]  # 例として3つの異なる温度

# プロットの設定
plt.figure(figsize=(10, 8))

for t in t_values:
    # 強誘電相と常誘電相のeを計算
    e_ferro = ferroelectric_phase(Q_range, t)
    e_para = paraelectric_phase(Q_range, t)

    # プロット
    plt.plot(Q_range, e_ferro, label=f't={t}')
    plt.plot(Q_range, e_para, label=f't={t}', linestyle='--')

# グラフのタイトルと軸ラベルを設定
plt.title('Q-e ')
plt.xlabel('Q')
plt.ylabel('e')
plt.grid(True)
plt.legend()
plt.show()