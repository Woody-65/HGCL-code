import scipy.io as mat
import math
datalist=[]
uidmax=5000
file=open('Gowalla_totalCheckins.txt')
line=file.readline()
while(line):
    line=line.split(' ')
    line=line[0].split('\t')
    a=float(line[0])
    if(a>=uidmax):
        break
    b = round(float(line[2]))
    c = round(float(line[3]))#每1划分，总量为180*360
    d=math.floor(float(line[2])/10)
    e=math.floor(float(line[3])/10)#每10划分的区域，总量为36*18
    category=e+18+36*(d+9)
    bno=b+90
    cno=c+180
    loactionid=bno*360+cno
    templist=[int(a),int(loactionid),int(category)]
    datalist.append(templist)
    line=file.readline()
print('finished!')
data={'rating':datalist}
mat.savemat('rating.mat',data)