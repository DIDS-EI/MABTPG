import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams['font.size'] = 30
matplotlib.rcParams['mathtext.fontset'] = 'stix'

font1 = {'family': 'Times New Roman', 'color': 'Black', 'weight': 'bold', 'size': 40}  # normal
font2 = {'family': 'Times New Roman', 'size': 40, 'weight': 'bold'}  # label
font3 = {'family': 'Times New Roman', 'size': 38, 'weight': 'bold'}  # legend
font4 = {'family': 'Times New Roman', 'color': 'Black', 'weight': 'bold', 'size': 38}

# Data 1
# homogeneity_1 = [0.25, 0.5, 0.75, 1]
# heterogeneity_1 = [0.75,0.5,0.25,0]
heterogeneity_1 = [1, 0.67, 0.33,0]
success_0_1_1 = [10.38, 11.47, 10.34, 10.21]
success_0_3_1 = [4.28, 6.31, 5.47, 5.28]

# Data 2
# homogeneity_2 = [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1]
# heterogeneity_2 = [0.875, 0.75, 0.625, 0.5, 0.375, 0.25, 0.125, 0] # [1 - x for x in original_list]
step = 1 / 7
heterogeneity_2 = [round(i * step, 2) for i in range(8)]
heterogeneity_2[-1] = int(heterogeneity_2[-1])
heterogeneity_2 = heterogeneity_2[::-1]
success_0_1_2 = [3.28, 9.38, 9.38, 9.38, 9.38, 9.58, 9.44, 9.21]
success_0_3_2 = [3.28, 3.28, 3.27, 3.28, 3.28, 3.59, 3.29, 3.51]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8), sharey=True)

# Plot 1
line1, = ax1.plot(heterogeneity_1, success_0_1_1, marker='o', color='#9467bd', label='Subtask Chaining Disabled', linewidth=4, markersize=15)
line2, = ax1.plot(heterogeneity_1, success_0_3_1, marker='s', color='#d62728', label='Subtask Chaining Enabled', linewidth=4, markersize=15)

ax1.set_xlabel('Heterogeneity', fontdict=font2)
ax1.set_ylabel('Total Steps', fontdict=font2)
ax1.set_xticks(heterogeneity_1)
ax1.set_xticklabels(heterogeneity_1, fontsize=40, fontfamily='Times New Roman', fontweight='bold')
ax1.tick_params(axis='x', labelsize=40)
ax1.tick_params(axis='y', labelsize=40)
ax1.set_yticks(range(0, 15, 2))
ax1.set_yticklabels(ax1.get_yticks(), fontsize=40, fontfamily='Times New Roman', fontweight='bold')
ax1.grid(True)
ax1.set_title('4 Robots', fontdict=font2)
ax2.set_title('8 Robots', fontdict=font2)

# Plot 2
line4, = ax2.plot(heterogeneity_2, success_0_1_2, marker='o', color='#9467bd', label='use_atom_subtask_chain=False', linewidth=4, markersize=15)
line5, = ax2.plot(heterogeneity_2, success_0_3_2, marker='s', color='#d62728', label='use_atom_subtask_chain=True', linewidth=4, markersize=15)

ax2.set_xlabel('Heterogeneity', fontdict=font2)
# ax2.set_xticks(heterogeneity_2[1::2])
# ax2.set_xticklabels(heterogeneity_2[1::2], fontsize=40, fontfamily='Times New Roman', fontweight='bold')
ax2.set_xticks(heterogeneity_2[0:7:2]+[heterogeneity_2[-1]])
ax2.set_xticklabels(heterogeneity_2[0:7:2]+[heterogeneity_2[-1]], fontsize=40, fontfamily='Times New Roman', fontweight='bold')

ax2.tick_params(axis='x', labelsize=40)
ax2.tick_params(axis='y', labelsize=40)
ax2.set_yticks(range(0, 15, 2))
ax2.set_yticklabels(ax2.get_yticks(), fontsize=40, fontfamily='Times New Roman', fontweight='bold')
ax2.grid(True)

# Shared legend
fig.legend(handles=[line1, line2], loc='upper center', bbox_to_anchor=(0.53, 1), prop=font3, ncol=2)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.88])

# Save figure as PDF
plt.savefig('exp-parallel-combined.pdf')

# Show plot
plt.show()
