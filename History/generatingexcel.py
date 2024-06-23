import pickle
import  xlwt
import numpy as np
filename='SR-HAN_CiaoDVD_1718697146_hide_dim_32_lr_0.055_reg_0.065_topK_10-ssl_ureg_0.04-ssl_ireg_0.05.his'
with open(filename,'rb') as f:
    output=pickle.load(f)
a=output['loss']
b=output['hr']
c=output['ndcg']
rows=len(a)
cols=3
table=np.zeros((rows,cols))
table[:,0]=a
table[:,1]=b
table[:,2]=c
wb=xlwt.Workbook()
ws=wb.add_sheet('Result')
ws.write(0,0,'epoch')
ws.write(0,1,'loss')
ws.write(0,2,'HR')
ws.write(0,3,'HDCG')
for i in range(rows):
    ws.write(i+1, 0, i+1)
    ws.write(i+1, 1, table[i][0])
    ws.write(i+1, 2, table[i][1])
    ws.write(i+1, 3, table[i][2])
dataname=filename.split('_')[1]

wb.save(f'./{dataname}_Result.xls')

