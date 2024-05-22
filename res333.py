import matplotlib.pyplot as plt

# Data from the table
methods = ['VOCA', 'MeshTalk', 'FaceFormer', 'EmoTalk', 'Proposed']
EVE_data = [4.188, 3.386, 3.757, 2.493, 1.760]
LVE_data = [5.091, 3.459, 3.247, 2.762, 2.693]

# Plotting the bar graph
x = range(len(methods))
width = 0.4

plt.figure(figsize=(10, 6))

# Specifying colors
eve_color = '#87CEEB'  # SkyBlue
lve_color = '#FFA07A'  # LightSalmon

plt.bar(x, EVE_data, width=width, label='EVE(mm)', color=eve_color, align='center')
plt.bar([i + width for i in x], LVE_data, width=width, label='LVE(mm)', color=lve_color, align='center')

plt.xlabel('Methods')
plt.ylabel('Error (mm)')
plt.title('The Comparison of Proposed Method with Baselines based on EVE and LVE using RAVDESS dataset')
plt.xticks([i + width / 2 for i in x], methods)
plt.legend()

plt.tight_layout()
plt.savefig('res333.svg', format='svg')
plt.show()
