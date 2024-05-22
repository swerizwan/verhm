import matplotlib.pyplot as plt

# Data from the table
methods = ['VOCA', 'MeshTalk', 'FaceFormer', 'EmoTalk', 'Proposed']
VOCASET_data = [2.292, 2.070, 1.944, 1.914, 1.089]
RAVDESS_data = [2.700, 2.139, 1.958, 1.648, 0.718]
MEAD_data = [2.236, 2.058, 1.852, 1.498, 1.010]

# Plotting the bar graph
x = range(len(methods))
width = 0.2

plt.figure(figsize=(10, 6))

# Specifying colors
colors = ['#CCD3CA', '#F5E8DD', '#EED3D9']

plt.bar(x, VOCASET_data, width=width, label='VOCASET', color=colors[0])
plt.bar([i + width for i in x], RAVDESS_data, width=width, label='RAVDESS', color=colors[1])
plt.bar([i + 2*width for i in x], MEAD_data, width=width, label='MEAD', color=colors[2])

plt.xlabel('Methods')
plt.ylabel('Error (mm)')
plt.title('The Comparison of Proposed Method with Baselines based on LAE using VOCASET, RAVDESS, and MEAD datasets')
plt.xticks([i + width for i in x], methods)
plt.legend()

plt.tight_layout()
plt.savefig('res.svg', format='svg')
plt.show()
