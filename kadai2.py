import matplotlib.pyplot as plt

# サンプルデータを作成
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

# 散布図を描画
plt.scatter(x, y, color='blue', label='Sample Points')

# グラフのタイトルと軸ラベルを設定
plt.title('kadai')
plt.xlabel('X')
plt.ylabel('Y')

# 凡例を表示
plt.legend()

# グラフを表示
plt.show()
