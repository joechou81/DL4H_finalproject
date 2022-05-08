import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


"""
# learning curve
with pd.ExcelFile('losstrain.xls') as reader:
    output = pd.read_excel(reader,  sheet_name = 'stageNet')
    
    
trainloss = output['train_loss']
valloss = output['val_loss']
# plot lines 
plt.grid(color='gray', linestyle='-', linewidth=1, alpha= 0.8)
plt.plot(range(0,50), trainloss, label = "train loss")
plt.plot(range(0,50), valloss, label = "validation loss")
plt.plot((6, 6),(5, 30),color='r', label = "Best epoch")
plt.ylim((5, 30))
plt.xlim((0, 50))
plt.legend()
plt.xticks((0, 6, 10, 20, 30, 40, 50))
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.show()



# dataset
with pd.ExcelFile('losstrain.xls') as reader:
    output = pd.read_excel(reader,  sheet_name = 'dataset')
    
    
auprc = output['auprc'][:6]    
auroc = output['auroc'][:6]
datasize = output['dataset'][:6]
plt.xticks(ticks = datasize)
plt.grid(color='gray', linestyle='-', linewidth=1, alpha= 0.8)
plt.plot(datasize, auprc, label = 'AUPRC', marker='o')
plt.xlim((datasize[0], datasize[5]))
plt.ylim((0.23,0.28))
plt.legend()
plt.xlabel("Data Size")
plt.xticks(rotation=45, ha='right')
plt.ylabel("AUC of PRC")
plt.legend(loc='lower right')
plt.show()

"""

# seed

with pd.ExcelFile('losstrain.xls') as reader:
    output = pd.read_excel(reader,  sheet_name = 'seed')
    
output = output.sort_values(by = ['seed'], ascending=True)
auprc = output['auprc']
auroc = output['auroc']
minpse = output['minpse']

x = np.array([auprc, auroc, minpse]).transpose();
mins = x.min(0)
maxes = x.max(0)
means = x.mean(0)
std = x.std(0)

# create stacked errorbars:
plt.grid(color='gray', linestyle='-', linewidth=1, alpha= 0.8)
plt.errorbar(np.arange(3), means, std, fmt='o', lw=20, alpha= 0.7)
plt.errorbar(np.arange(3), means, [means - mins, maxes - means],
              fmt='or', ecolor='b', lw=2, capsize = 2, capthick = 2)
plt.xlim(-1, 3)
plt.xticks([0, 1, 2],['AUPRC','AUROC','MIN(P+, Se)'], rotation=0)
plt.xlabel('Accuracy Indicator')
plt.ylabel('Value')
