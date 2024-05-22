import matplotlib.pyplot as plt

# Data from the table
methods = ['VOCA', 'MeshTalk', 'FaceFormer', 'EmoTalk']
EVE_data = [4.188, 3.386, 3.757, 2.493]
LVE_data = [5.091, 3.459, 3.247, 2.762]
proposed_EVE = 1.760
proposed_LVE = 2.693

# Calculating the differences for the proposed method
EVE_diff = [value - proposed_EVE for value in EVE_data]
LVE_diff = [value - proposed_LVE for value in LVE_data]

# Plotting the bar graph
x = range(len(methods))
width = 0.4

plt.figure(figsize=(10, 6))

# Specifying colors
eve_color = '#87CEEB'  # Light Blue
lve_color = '#FFA07A'  # Light Coral

plt.bar([i - width / 2 for i in x], EVE_diff, width=width, label='EVE(mm) Improvement', color=eve_color, align='center')
plt.bar([i + width / 2 for i in x], LVE_diff, width=width, label='LVE(mm) Improvement', color=lve_color, align='center')

plt.xlabel('Methods')
plt.ylabel('Improvement in Error (mm)')
plt.title('Improvement of Proposed Method over Baselines based on EVE and LVE using RAVDESS dataset')
plt.xticks(x, methods)
plt.legend()

plt.tight_layout()
plt.savefig('res3333.svg', format='svg')
plt.show()
