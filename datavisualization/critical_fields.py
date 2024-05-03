import numpy as np
import matplotlib.pyplot as plt

# 温度の範囲を定義
temperatures = np.linspace(-1, 0, 100)

# 臨界電場ek1とek2を計算する関数
def calculate_critical_fields(t):
    # 方程式(15)からQの範囲を計算
    Q_ek1 = np.sqrt(-t / 6)

    # 方程式(13)の後者からQの範囲を計算
    Q_ek2 = np.sqrt((1-2*t) / 48)

    # 方程式(14)を使用してek1を計算
    ek1 = 2 * (1 + t) * Q_ek1 + 4 * Q_ek1**3

    # 方程式(11)を使用してek2を計算
    ek2 = 2 * (1 -2*t) * Q_ek2 - 32 * Q_ek2**3

    return ek1, ek2

# 各温度における臨界電場を計算
ek1_values, ek2_values = zip(*[calculate_critical_fields(t) for t in temperatures])

# グラフをプロット
plt.figure(figsize=(10, 6))
plt.plot(temperatures, ek1_values, label='Critical Field ek1 (paraelectric to Antiferroelectric)')
plt.plot(temperatures, ek2_values, label='Critical Field ek2 (Antiferroelectric to paraelectric)', linestyle='--')
plt.xlabel('Temperature')
plt.ylabel('Critical Field')
plt.title('Critical Field ek1 and ek2 vs. Temperature')
plt.legend()
plt.grid(True)
plt.ylim(0.00, 0.70)
plt.show()