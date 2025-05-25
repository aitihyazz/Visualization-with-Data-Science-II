import matplotlib.pyplot as plt
x=[0,5,10,20,25,20]
y1=[10,15,20,20,15,5]
y2=[10,12,15,12,20,0]
plt.plot(x,y1,linestyle="dashed",marker="D")
plt.plot(x,y2,linestyle="dashed",marker="D")
plt.title("V-T Graph")
plt.xlabel("v m/s")
plt.ylabel("T s")
plt.xlim(5,22)
plt.ylim(10,20)
plt.legend()
plt.show()
