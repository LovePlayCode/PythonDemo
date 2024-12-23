import pandas as pd
import matplotlib.pyplot as plt

# 1. 读取快递业务量.csv文件，获取数据
df = pd.read_csv('快递业务量.csv')

# 2. 绘制反映2018年、2019年快递业务量对比的堆叠柱形图
# 设置月份为索引
df.set_index('月份', inplace=True)

# 绘制堆叠柱形图
ax = df.plot(kind='bar', stacked=True, color=['#F4A460', '#6490ED'], width=0.6)

# 3. 配置图表属性
ax.set_xlabel('月份')  # 设置x轴标签
ax.set_ylabel('业务量（亿件）')  # 设置y轴标签
ax.set_title('2018年、2019年快递业务量对比')  # 设置标题

# 4. 添加图例
ax.legend(['2018年', '2019年'], loc='upper left')

# 5. 显示图表
plt.xticks(rotation=45)  # 让x轴的月份标签倾斜45度，避免重叠
plt.tight_layout()  # 调整布局，使得标签不会被遮挡
plt.show()
