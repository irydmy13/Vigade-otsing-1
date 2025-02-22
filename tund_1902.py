import numpy as np #x=[min,max]
import matplotlib.pyplot as plt
def Vaal(color:str):
    x1=np.arange(0,10, 1) 
    y1=(2/27)*x1**2-3

    x2=np.arange(-10, 0.5, 0.5)
    y2=0.04*x2**2-3

    x3=np.arange(-9, -2.5, 0.5)
    y3=(2/9)*(x3+6)**2+1

    x4=np.arange(-3, 9.5, 0.5)
    y4=(-1/12)*(x4-3)**2+6

    x5=np.arange(5, 8.5, 0.5)
    y5=(1/9)*(x5-5)**2+2

    x6=np.arange(5, 8.5, 0.5)
    y6=(1/8)*(x6-7)**2+1.5

    x7=np.arange(-13, -8.5, 0.5)
    y7=(-0.75)*(x7+11)**2+6

    x8=np.arange(-15, -12.5, 0.5)
    y8=(-0.5)*(x8+13)**2+3

    x9=np.arange(-15, -10.5, 0.5)
    y9=[1]*len(x9)

    x10=np.arange(3, 4, 0.5)
    y10=[3]*len(x10)

    plt.figure(facecolor=color)
    plt.title("Vaal")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)
    ax=plt.axes()
    ax.set_facecolor("lightblue")
    plt.plot(x1,y1,"r:o")
    colors=["c", "m", "y", "r", "g", "b", "w", "k", "k", "k"]
    for i in range(1,11):
        plt.plot(eval(f"x{i}"), eval(f"y{i}"), colors[i-1]+"-*") #markery
    plt.show()

def Vihmavari(color:str):
    x1=np.arange(-12, 13, 1) 
    y1=(-1/18)*x1**2+12

    x2=np.arange(-4, 5, 1)
    y2=(-1/8)*x2**2+6

    x3=np.arange(-12, -3.5, 0.5)
    y3=(-1/8)*(x3+8)**2+6

    x4=np.arange(4, 12.5, 0.5)
    y4=(-1/8)*(x4-8)**2+6

    x5=np.arange(-4, 0, 0.5)
    y5=2*(x5+3)**2-9

    x6=np.arange(-4, 0.5, 0.5)
    y6=3/2*(x6+3)**2-10

    plt.figure(facecolor="lightgreen")
    plt.title("lll")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)
    ax=plt.axes()
    ax.set_facecolor("lightblue")
    colors=["c", "m", "y", "r", "g", "b"]

    plt.plot(x1, y1, colors[0] + "-*")
    plt.plot(x2, y2, colors[1] + "-*")
    plt.plot(x3, y3, colors[2] + "-*")
    plt.plot(x4, y4, colors[3] + "-*")
    plt.plot(x5, y5, colors[4] + "-*")
    plt.plot(x6, y6, colors[5] + "-*")
   
    plt.show()

#linspace (x, y, a)  a = kol-vo tochek
def Prillid():
    x1= np.linspace(-9, -1 ,100)#min, max, punktide kogus
    y1= -1/16*(x1+5)**2+2

    x2= np.linspace(1, 9, 100)
    y2= -1/16*(x2-5)**2 + 2

    x3= np.linspace(-9, -1, 100)
    y3= 1/4*(x3+5)**2 - 2

    x4= np.linspace(1, 9, 100)
    y4= -1/4*(x4-5)**2 - 3 

    x5= np.linspace(-9, -6, 100)
    y5= -(x5+7)**2 +5

    x6= np.linspace(6, 9, 100)
    y6= -(x6-7)**2+5

    x7= np.linspace(-1, 1, 100)
    y7= -0.5*x7**2+1.5

    plt.figure(figsize=(8,6))
    for i in range(1,8):
        plt.plot(eval(f"x{i}"), eval(f"y{i}"), "b-*", label=f"prillide {i.osa}")
    plt.axhline(0, color="black", linewidth=1)
    plt.axhline(0, color="black", linewidth=0.5)
    plt.grid(True, linestyle=':')
    plt.legend(loc='best')
    """0 = 'best'
    1 = 'upper right'
    2 = 'upper left'
    3 = 'lower left'
    4 = 'lower right'
    5 = 'right'
    6 = 'center left'
    7 = 'center right'
    8 = 'lower center'
    9 = 'upper center'
    10 = 'center'"""

    plt.title("Prillid")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

