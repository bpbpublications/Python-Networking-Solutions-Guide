import matplotlib.pyplot as plt

a = [1,2,3,4,5]
b = [10,20,30,40,50]

plt.figure(figsize=(8,8), facecolor="#FFCEB4")

plt.plot(a, b, color="Red")

plt.xlabel("Value of 'a'")
plt.ylabel("Value of 'b'")
plt.title("Chart of 'a' and 'b' Values")
plt.grid(True)
plt.show()
