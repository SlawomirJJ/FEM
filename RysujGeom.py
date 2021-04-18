import numpy as np
import matplotlib as plt



def RysujGeom(x_range,WEZLY,ELEMENTY,types):
    

    

    
    plt.plot(x_range[0],0,'*') #x_range[0]
    plt.plot(x_range[1],0,'*') #x_range[1]
    plt.plot(x_range,[0,0])
    plt.plot(WEZLY,np.zeros(len(WEZLY)),'*')
    
    plt.text(x_range[0]-0.15,0,types[0])
    plt.text(x_range[1]+0.15,0,types[1])
    
    for i in range(0,len(WEZLY)):
        plt.text(WEZLY[i]-0.03,0.01,str(WEZLY[i]))
        plt.text(WEZLY[i]-0.05,-0.05,str(i+1))
    
    for i in range(0,len(WEZLY)-1):
        print((WEZLY[i]-WEZLY[i+1])/2)
        plt.text(WEZLY[i]/2+WEZLY[i+1]/2, 0.05,str(i+1))
    
    plt.xlim([x_range[0]-0.3,x_range[1]+0.3])
    plt.ylim([-0.2,0.42])

