import scipy.io as mat
datalist=[]
uidmax=5000
file=open('Gowalla_edges.txt')
line=file.readline()
while(line):
    line=line.split(' ')
    line=line[0].split('\t')
    a=int(line[0])
    b=int(line[1].split('\n')[0])
    if(a>=uidmax):
        break
    if(b<uidmax):
        templist=[a,b]
        datalist.append(templist)
    line=file.readline()
print('finished!')
data={'trust':datalist}
mat.savemat('trust.mat',data)

