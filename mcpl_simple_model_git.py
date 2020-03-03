# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:14:39 2020

@author: Yoon
"""

#%% 과장님 operability window for 72wt% glycerol/water in 20 Celcius degree.
import numpy as np
import matplotlib.pyplot as plt

# Operabiltiy window 
c=1.0   # cos term
H0=200  # Uniform die lip configuration in MCPL
Ld=800.0  #Ld=Lu

def jiweepingreal(q,c,H0,Ld):     #Weeping
    a=6.0*(Ld/H0)*25/61           #Unit=[m/s]
    model=1.0/H0*q + c/a/2.0*60   #Unit=[m/min]
    return model

def jibreakupreal(q,c,H0,Ld):   #Bead Break-up
    a=6.0*(Ld/H0)*25/61         #Unit=[m/s]
    model=2.0/H0*q + c/a*60     #Unit=[m/min]
    return model

Q=np.linspace(0,100,11)     #[mL/min]
q=Q/0.1     #폭당 유량 = Q/폭 = Q/0.1 for MCPL [mL/m/min]

result_w=jiweepingreal(q,c,H0,Ld)
result_bb=jibreakupreal(q,c,H0,Ld)

# Experiment and operability window
Rgt1=2.0
Rgt2=2.9
Rgt=np.array([Rgt1,Rgt2])
h0=H0/Rgt    #for Rgt1, Rgt2

rgtline1=q/h0[0] #for Rgt1
rgtline2=q/h0[1] #for Rgt2

#Plot
fig=plt.figure(figsize=(6,5))

ax1=fig.add_subplot(1,1,1)
ax1.set_title(r' $ H_{0}= %.1f , \:  \cos{\theta_\mathrm{d}}+\cos{\theta_\mathrm{s}} = %.1f   $ '%(H0,c))

ax1.plot(Q,result_bb, 'r' ,linestyle='-', label='Bead Break-up', marker='o')
ax1.plot(Q,result_w, label='Weeping', marker='o',linestyle='-')

ax1.plot(Q,rgtline1, 'g', linestyle=':', marker='o', label= r' $ R_\mathrm{gt}= %.2f $'%(Rgt[0]))
ax1.plot(Q,rgtline2, 'g', linestyle='--', marker='o', label= r' $ R_\mathrm{gt}= %.2f $'%(Rgt[1]))


ax1.set_xlabel(r'$ Q [\mathrm{mL/min}] $' , fontsize=18)
ax1.set_ylabel(r'$ V_\mathrm{w} [\mathrm{m/min}]$' , fontsize=18)
ax1.set_xlim(2.0, 120.0)
ax1.set_ylim(0, )

plt.legend()
plt.grid()
#plt.title('72wt% Glycerol/Water Solution')

#%% 과장님 operability window for 72wt% glycerol/water in 20 Celcius degree.  위에서 단순히 x축 y축 뒤바꿈
import numpy as np
import matplotlib.pyplot as plt

# Operabiltiy window 
c=1.0   # cos term
H0=200  # Uniform die lip configuration in MCPL
Ld=800.0  #Ld=Lu

def jiweepingreal(q,c,H0,Ld):     #Weeping
    a=6.0*(Ld/H0)*25/61           #Unit=[m/s]
    model=1.0/H0*q + c/a/2.0*60   #Unit=[m/min]
    return model

def jibreakupreal(q,c,H0,Ld):   #Bead Break-up
    a=6.0*(Ld/H0)*25/61         #Unit=[m/s]
    model=2.0/H0*q + c/a*60     #Unit=[m/min]
    return model

Q=np.linspace(0,100,11)     #[mL/min]
q=Q/0.1     #폭당 유량 = Q/폭 = Q/0.1 for MCPL [mL/m/min]

result_w=jiweepingreal(q,c,H0,Ld)
result_bb=jibreakupreal(q,c,H0,Ld)

# Experiment and operability window
Rgt1=2.0
Rgt2=2.9
Rgt=np.array([Rgt1,Rgt2])
h0=H0/Rgt    #for Rgt1, Rgt2

rgtline1=q/h0[0] #for Rgt1
rgtline2=q/h0[1] #for Rgt2

#Plot
plt.clf()  # clear the current figure
fig=plt.figure(figsize=(6,5))

ax1=fig.add_subplot(1,1,1)
ax1.set_title(r' $ H_{0}= %.1f , \:  \cos{\theta_\mathrm{d}}+\cos{\theta_\mathrm{s}} = %.1f   $ '%(H0,c))

ax1.plot(result_bb,Q, 'r' ,linestyle='-', label='Bead Break-up', marker='o')
ax1.plot(result_w, Q, label='Weeping', marker='o',linestyle='-')

ax1.plot(rgtline1, Q, 'g', linestyle=':', marker='o', label= r' $ R_\mathrm{gt}= %.2f $'%(Rgt[0]))
ax1.plot(rgtline2, Q, 'g', linestyle='--', marker='o', label= r' $ R_\mathrm{gt}= %.2f $'%(Rgt[1]))


ax1.set_ylabel(r'$ Q [\mathrm{mL/min}] $' , fontsize=18)
ax1.set_xlabel(r'$ V_\mathrm{w} [\mathrm{m/min}]$' , fontsize=18)
ax1.set_ylim(2.0, 120.0)
ax1.set_xlim(0, )

for X,Y in zip(result_w, Q):
        ax1.annotate('{:.1f}'.format(X), (X,Y))
for X,Y in zip(result_bb, Q):
        ax1.annotate('{:.1f}'.format(X), (X,Y))
for X,Y in zip(rgtline1, Q):
        ax1.annotate('{:.1f}'.format(X), (X,Y))
for X,Y in zip(rgtline2, Q):
        ax1.annotate('{:.1f}'.format(X), (X,Y))
        
plt.legend()
plt.grid()
#plt.title('72wt% Glycerol/Water Solution')

#%% 과장님 operability window for Water in 20 Celcius degree.
import numpy as np
import matplotlib.pyplot as plt

# Operabiltiy window 
c=1.0   # cos term
H0=200  # Uniform die lip configuration in MCPL
Ld=800.0  #Ld=Lu

def jiweepingreal(q,c,H0,Ld):     #Weeping
    a=6.0*(Ld/H0)*1.0/64.42           #Unit=[m/s]
    model=1.0/H0*q + c/a/2.0*60   #Unit=[m/min]
    return model

def jibreakupreal(q,c,H0,Ld):   #Bead Break-up
    a=6.0*(Ld/H0)*1.0/64.42         #Unit=[m/s]
    model=2.0/H0*q + c/a*60     #Unit=[m/min]
    return model

Q=np.linspace(0,100,11)     #[mL/min]
q=Q/0.1     #폭당 유량 = Q/폭 = Q/0.1 for MCPL [mL/m/min]

result_w=jiweepingreal(q,c,H0,Ld)
result_bb=jibreakupreal(q,c,H0,Ld)

# Experiment and operability window
Rgt1=2.0
Rgt2=2.9
Rgt=np.array([Rgt1,Rgt2])
h0=H0/Rgt    #for Rgt1, Rgt2

rgtline1=q/h0[0] #for Rgt1
rgtline2=q/h0[1] #for Rgt2

#Plot
fig=plt.figure(figsize=(6,5))

ax1=fig.add_subplot(1,1,1)
ax1.set_title(r' $ H_{0}= %.1f , \:  \cos{\theta_\mathrm{d}}+\cos{\theta_\mathrm{s}} = %.1f   $ '%(H0,c))

ax1.plot(Q,result_bb, 'r' ,linestyle='-', label='Bead Break-up', marker='o')
ax1.plot(Q,result_w, label='Weeping', marker='o',linestyle='-')

ax1.plot(Q,rgtline1, 'g', linestyle=':', marker='o', label= r' $ R_\mathrm{gt}= %.2f $'%(Rgt[0]))
ax1.plot(Q,rgtline2, 'g', linestyle='--', marker='o', label= r' $ R_\mathrm{gt}= %.2f $'%(Rgt[1]))


ax1.set_xlabel(r'$ Q [\mathrm{mL/min}] $' , fontsize=18)
ax1.set_ylabel(r'$ V_\mathrm{w} [\mathrm{m/min}]$' , fontsize=18)
ax1.set_xlim(2.0, 120.0)
ax1.set_ylim(0, )

plt.legend()
plt.grid()
#plt.title('Water')

#%% 과장님 operability window for Water in 20 Celcius degree. 위에서 단순히 x축 y축 뒤바꿈
import numpy as np
import matplotlib.pyplot as plt

# Operabiltiy window 
c=1.0   # cos term
H0=200  # Uniform die lip configuration in MCPL
Ld=800.0  #Ld=Lu

def jiweepingreal(q,c,H0,Ld):     #Weeping
    a=6.0*(Ld/H0)*1.0/64.42           #Unit=[m/s]
    model=1.0/H0*q + c/a/2.0*60   #Unit=[m/min]
    return model

def jibreakupreal(q,c,H0,Ld):   #Bead Break-up
    a=6.0*(Ld/H0)*1.0/64.42         #Unit=[m/s]
    model=2.0/H0*q + c/a*60     #Unit=[m/min]
    return model

Q=np.linspace(0,100,11)     #[mL/min]
q=Q/0.1     #폭당 유량 = Q/폭 = Q/0.1 for MCPL [mL/m/min]

result_w=jiweepingreal(q,c,H0,Ld)
result_bb=jibreakupreal(q,c,H0,Ld)

# Experiment and operability window
Rgt1=2.0
Rgt2=2.9
Rgt=np.array([Rgt1,Rgt2])
h0=H0/Rgt    #for Rgt1, Rgt2

rgtline1=q/h0[0] #for Rgt1
rgtline2=q/h0[1] #for Rgt2

#Plot
fig=plt.figure(figsize=(6,5))

ax1=fig.add_subplot(1,1,1)
ax1.set_title(r' $ H_{0}= %.1f , \:  \cos{\theta_\mathrm{d}}+\cos{\theta_\mathrm{s}} = %.1f   $ '%(H0,c))

ax1.plot(result_bb,Q, 'r' ,linestyle='-', label='Bead Break-up', marker='o')
ax1.plot(result_w,Q, label='Weeping', marker='o',linestyle='-')

ax1.plot(rgtline1,Q, 'g', linestyle=':', marker='o', label= r' $ R_\mathrm{gt}= %.2f $'%(Rgt[0]))
ax1.plot(rgtline2,Q, 'g', linestyle='--', marker='o', label= r' $ R_\mathrm{gt}= %.2f $'%(Rgt[1]))

for X,Y in zip(result_w, Q):
        ax1.annotate('{:.1f}'.format(X), (X,Y))
for X,Y in zip(result_bb, Q):
        ax1.annotate('{:.1f}'.format(X), (X,Y))
for X,Y in zip(rgtline1, Q):
        ax1.annotate('{:.1f}'.format(X), (X,Y), textcoords='offset points',xytext=(-10,-5))
for X,Y in zip(rgtline2, Q):
        ax1.annotate('{:.1f}'.format(X), (X,Y), textcoords='offset points',xytext=(0,5))

ax1.set_ylabel(r'$ Q [\mathrm{mL/min}] $' , fontsize=18)
ax1.set_xlabel(r'$ V_\mathrm{w} [\mathrm{m/min}]$' , fontsize=18)
ax1.set_ylim(2.0, 120.0)
ax1.set_xlim(0, )

plt.legend()
plt.grid()
#plt.title('40 wt% Glycerol/Water solution')

#%%



#%% General 1
import numpy as np
import matplotlib.pyplot as plt

#Liquid property
mu=3.7       #Viscosity [mPas]
sigma=70   #Surface tension [mN/m]

# Operabiltiy window 
c=1.0   # cos term
H0=200  # Uniform die lip configuration in MCPL
Ld=800.0  #Ld=Lu

def jiweepingreal(q,c,H0,Ld,mu,sigma):     #Weeping
    a=6.0*(Ld/H0)*mu/sigma           #Unit=[m/s]
    model=1.0/H0*q + c/a/2.0*60   #Unit=[m/min]
    return model

def jibreakupreal(q,c,H0,Ld,mu,sigma):   #Bead Break-up
    a=6.0*(Ld/H0)*mu/sigma         #Unit=[m/s]
    model=2.0/H0*q + c/a*60     #Unit=[m/min]
    return model

Q=np.linspace(0,100,11)     #[mL/min]
q=Q/0.1     #폭당 유량 = Q/폭 = Q/0.1 for MCPL [mL/m/min]

result_w=jiweepingreal(q,c,H0,Ld,mu,sigma)
result_bb=jibreakupreal(q,c,H0,Ld,mu,sigma)

# Experiment and operability window
Rgt1=2.0
Rgt2=2.9
Rgt=np.array([Rgt1,Rgt2])
h0=H0/Rgt    #for Rgt1, Rgt2

rgtline1=q/h0[0] #for Rgt1
rgtline2=q/h0[1] #for Rgt2

#Plot
fig=plt.figure(figsize=(6,5))

ax1=fig.add_subplot(1,1,1)
ax1.set_title(r' $ H_{0}= %.1f , \:  \cos{\theta_\mathrm{d}}+\cos{\theta_\mathrm{s}} = %.1f   $ '%(H0,c))

ax1.plot(Q,result_bb, 'r' ,linestyle='-', label='Bead Break-up', marker='o')
ax1.plot(Q,result_w, label='Weeping', marker='o',linestyle='-')

ax1.plot(Q,rgtline1, 'g', linestyle=':', marker='o', label= r' $ R_\mathrm{gt}= %.2f $'%(Rgt[0]))
ax1.plot(Q,rgtline2, 'g', linestyle='--', marker='o', label= r' $ R_\mathrm{gt}= %.2f $'%(Rgt[1]))


ax1.set_xlabel(r'$ Q [\mathrm{mL/min}] $' , fontsize=18)
ax1.set_ylabel(r'$ V_\mathrm{w} [\mathrm{m/min}]$' , fontsize=18)
ax1.set_xlim(2.0, 120.0)
ax1.set_ylim(0, )

plt.legend()
plt.grid()

#%% General 2  <=General 1에서 x축 y축 뒤바꾼 것
import numpy as np
import matplotlib.pyplot as plt

#Liquid property
mu=3.7       #Viscosity [mPas]
sigma=70   #Surface tension [mN/m]

# Operabiltiy window 
c=1.0   # cos term
H0=200  # Uniform die lip configuration in MCPL
Ld=800.0  #Ld=Lu

def jiweepingreal(q,c,H0,Ld,mu,sigma):     #Weeping
    a=6.0*(Ld/H0)*mu/sigma           #Unit=[m/s]
    model=1.0/H0*q + c/a/2.0*60   #Unit=[m/min]
    return model

def jibreakupreal(q,c,H0,Ld,mu,sigma):   #Bead Break-up
    a=6.0*(Ld/H0)*mu/sigma         #Unit=[m/s]
    model=2.0/H0*q + c/a*60     #Unit=[m/min]
    return model

Q=np.linspace(0,100,11)     #[mL/min]
q=Q/0.1     #폭당 유량 = Q/폭 = Q/0.1 for MCPL [mL/m/min]

result_w=jiweepingreal(q,c,H0,Ld,mu,sigma)
result_bb=jibreakupreal(q,c,H0,Ld,mu,sigma)

# Experiment and operability window
Rgt1=2.0
Rgt2=2.9
Rgt=np.array([Rgt1,Rgt2])
h0=H0/Rgt    #for Rgt1, Rgt2

rgtline1=q/h0[0] #for Rgt1
rgtline2=q/h0[1] #for Rgt2

#Plot
fig=plt.figure(figsize=(6,5))

ax1=fig.add_subplot(1,1,1)
ax1.set_title(r' $ H_{0}= %.1f , \:  \cos{\theta_\mathrm{d}}+\cos{\theta_\mathrm{s}} = %.1f   $ '%(H0,c))

ax1.plot(result_bb,Q, 'r' ,linestyle='-', label='Bead Break-up', marker='o')
ax1.plot(result_w,Q, label='Weeping', marker='o',linestyle='-')

ax1.plot(rgtline1,Q, 'g', linestyle=':', marker='o', label= r' $ R_\mathrm{gt}= %.2f $'%(Rgt[0]))
ax1.plot(rgtline2,Q, 'g', linestyle='--', marker='o', label= r' $ R_\mathrm{gt}= %.2f $'%(Rgt[1]))

for X,Y in zip(result_w, Q):
        ax1.annotate('{:.1f}'.format(X), (X,Y))
for X,Y in zip(result_bb, Q):
        ax1.annotate('{:.1f}'.format(X), (X,Y))
for X,Y in zip(rgtline1, Q):
        ax1.annotate('{:.1f}'.format(X), (X,Y), textcoords='offset points',xytext=(-10,-5))
for X,Y in zip(rgtline2, Q):
        ax1.annotate('{:.1f}'.format(X), (X,Y), textcoords='offset points',xytext=(0,5))

ax1.set_ylabel(r'$ Q [\mathrm{mL/min}] $' , fontsize=18)
ax1.set_xlabel(r'$ V_\mathrm{w} [\mathrm{m/min}]$' , fontsize=18)
ax1.set_ylim(2.0, 120.0)
ax1.set_xlim(0, )

plt.legend()
plt.grid()

# %%
