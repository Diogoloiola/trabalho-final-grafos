import sys

if __name__ == "__main__":
    f = open('test/ex1.txt','r')
    u, v = f.readline().split(' ')
    u = int(u)
    v = int(v)
    for j in range(0, u):
        edge = f.readline().replace("\n","").split(" ")
        print(edge)