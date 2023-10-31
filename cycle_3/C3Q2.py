import matplotlib.pyplot as plt
days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri']
drinks_sales = [300, 450, 150, 400, 650]
food_sales = [400, 500, 350, 300, 500]
plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.plot(days, drinks_sales, linestyle='dotted', color='cyan', label='Sales Data1', marker='H', markersize=8,
         markerfacecolor='magenta', markeredgecolor='black')
plt.xlabel('Days of the Week')
plt.ylabel('Sale of Drinks')
plt.title('Sales Data1', loc='right')
plt.grid(color='blue', linestyle='--')
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(days, food_sales, linestyle='--', color='yellow', label='Sales Data2', marker='D', markersize=8,
         markerfacecolor='green', markeredgecolor='red')
plt.xlabel('Days of the Week')
plt.ylabel('Sale of Food')
plt.title('Sales Data2', loc='center')
plt.grid(color='blue', linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()