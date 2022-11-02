import numpy as np
import matplotlib.pyplot as plt
T = 1
dt = 0.02
x0 = np.array([2.,3.,5.])
x1 = np.array([5.,5.,7.])
dim = x0.size
N = int(T/dt)+1 #number of ticks
coeff = np.empty((4,dim))*np.nan
A = np.array([[1, 0, 0, 0],
              [1, T, T**2, T**3],
              [0, 1, 0, 0],
              [0, 1, 2*T, 3*T**2]])
for s in range(dim):
    b = np.array([x0[s], x1[s], 0, 0]).transpose()
    # solving poly_coeff = A^-1*b
    coeff[:,s] = np.dot(np.linalg.inv(A), b)

x = np.empty((dim,N))*np.nan
dx = np.empty((dim,N))*np.nan
ddx = np.empty((dim,N))*np.nan
for i in range(dim):
    for j in range(N):
        x[i,j]=coeff[0,i]+dt*j*coeff[1,i]+(dt*j)**2*coeff[2,i]+(dt*j)**3*coeff[3,i]
        dx[i,j]=coeff[1,i]+2*dt*j*coeff[2,i]+3*(dt*j)**2*coeff[3,i]
        ddx[i,j]=2*coeff[2,i]+6*dt*j*coeff[3,i]

print(x)
plt.plot(range(N),x[0,:])
""" plt.plot(range(N),dx[0,:])
plt.plot(range(N),ddx[0,:]) """
plt.show()


""" b = np.load('talos_walking_traj_lipm.npz')
print(b['foot_steps']) """