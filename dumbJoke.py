import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

x = ['Kyle working with you', 'Kyle not working with you']
y = [1000000, 20000]  # 1000000 when Kyle is working, 20000 when he is not working

plt.bar(x, y, color=['#1f77b4', '#ff7f0e'])  # Blue and Orange

plt.title('Money Earned by Your Firm', fontsize=14)
plt.ylabel('Money Earned ($)', fontsize=12)

plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))

plt.show()
