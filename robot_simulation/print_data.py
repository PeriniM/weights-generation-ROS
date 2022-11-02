
from numpy import load 

data = load('talos_walking_traj_lipm.npz')
lst = data.files
for item in lst:
    print(item)
    print(data[item])
    
