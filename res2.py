import matplotlib.pyplot as plt

# Data from the table
methods = ['VOCA', 'MeshTalk', 'FaceFormer', 'EmoTalk']
VOCASET_diff = [2.292 - 1.089, 2.070 - 1.089, 1.944 - 1.089, 1.914 - 1.089]
RAVDESS_diff = [2.700 - 0.718, 2.139 - 0.718, 1.958 - 0.718, 1.648 - 0.718]
MEAD_diff = [2.236 - 1.010, 2.058 - 1.010, 1.852 - 1.010, 1.498 - 1.010]

# Plotting the bar graph
x = range(len(methods))
width = 0.2

plt.figure(figsize=(10, 6))

# Specifying light colors
colors_diff = ['#CCD3CA', '#F5E8DD', '#EED3D9']

plt.bar(x, VOCASET_diff, width=width, label='VOCASET', color=colors_diff[0])
plt.bar([i + width for i in x], RAVDESS_diff, width=width, label='RAVDESS', color=colors_diff[1])
plt.bar([i + 2*width for i in x], MEAD_diff, width=width, label='MEAD', color=colors_diff[2])

plt.xlabel('Baseline Methods')
plt.ylabel('Improvement in Error (mm)')
plt.title('Improvement of Proposed Method over Baselines based on LAE using VOCASET, RAVDESS, and MEAD datasets')
plt.xticks([i + width for i in x], methods)
plt.legend()

plt.tight_layout()
plt.savefig('res2.svg', format='svg')
plt.show()
