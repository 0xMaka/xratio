import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from data import data as p

x, y = [], []

for i in p:
  x.append(f'{int(i)}')
  y.append(f'{float(p[i]):.3f}')

# init chart
plt.figure(facecolor='#0A0226')
plt.style.use('dark_background')

plt.plot(x,y, '-.', c='#D621C1', lw=5)
f0 = {'family':'Source Code Pro','color':'#27DEF2','size':40} 
f1 = {'family':'Source Code Pro','color':'#D621C1','size':30}

plt.title('xSushi Historical Ratio', pad=20, fontdict=f0)
plt.xlabel('Block', labelpad=10, fontdict=f1)
plt.ylabel('Ratio', labelpad=10, fontdict=f1)

# make readable
plt.tick_params(axis='both', which='major', labelsize=15)

plt.xticks(rotation=75)
ax = plt.gca()
ax.set_facecolor('#100459')

plt.grid(1, ls=':', c='#27DEF2', lw='.2')

for label in ax.get_xaxis().get_ticklabels()[::2]:
  label.set_visible(False)

for label in ax.get_yaxis().get_ticklabels()[::2]:
  label.set_visible(False)

plt.show()
