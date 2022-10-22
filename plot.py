import matplotlib.pyplot as plt
from data import data as p

x, y = [], []

for i in p:
  x.append(f'{int(i)}')
  y.append(f'{float(p[i]):.3f}')

# init chart
plt.figure(facecolor='#060337')#'#0A0226')
# plt.rcParams["figure.figsize"] = (8,5.5)
plt.style.use('dark_background')

plt.plot(x,y, '-.', c='#27DEF2', linewidth=3)
#plt.grid()

f0 = {'family':'Source Code Pro','color':'#27DEF2','size':40} 
f1 = {'family':'Source Code Pro','color':'#D621C1','size':30}

plt.title('xSushi Historical Ratio', fontdict=f0)
plt.xlabel('Block', fontdict=f1)
plt.ylabel('Ratio', fontdict=f1)

# make readable
plt.tick_params(axis='both', which='major', labelsize=15)

plt.xticks(rotation=75)
ax = plt.gca()

for label in ax.get_xaxis().get_ticklabels()[::2]:
  label.set_visible(False)

for label in ax.get_yaxis().get_ticklabels()[::2]:
  label.set_visible(False)

ax.set_facecolor('#100459')

plt.show()
# plt.savefig('xSushiRatio.png')
