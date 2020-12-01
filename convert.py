import os
import soundfile as sf
fname = os.path.splitext(input('Input a file name to convert.\n'))
data, samplerate = sf.read(fname[0]+fname[1])
data = data*1.5

data3 = []
for i in range(0,len(data)):
    if i % 5 == 0:
        if not i == 0:
            sv = data[i-5]
            ev = data[i]
            dif = (ev - sv)/5
            data3.extend([sv,sv+dif,sv+dif*2,sv+dif*3,sv+dif*4])

sf.write(fname[0]+'_c'+fname[1],data3,samplerate=samplerate)