from __future__ import division
from datetime import datetime, date, time
import re
import sys




fhand = open(sys.argv[1])

#Extracting all times from the file and writing them in lists defined above
time = []

#Extracting all counters values from the file and writing them in lists defined above
counter_206_152_32_20 = []
counter_206_152_32_21 = []
counter_206_152_32_22 = []
counter_206_152_32_23 = []
counter_206_152_32_24 = []
counter_206_152_32_25 = []
counter_206_152_32_26 = []
counter_206_152_32_27 = []
counter_206_152_32_28 = []
counter_206_152_32_29 = []
counter_206_152_32_30 = []
counter_206_152_32_31 = []
counter_206_152_32_32 = []
counter_206_152_32_39 = []
counter_206_152_32_50 = []
counter_206_152_32_54 = []
counter_206_152_32_57 = []
counter_206_152_32_62 = []
counter_206_152_32_65 = []
counter_206_152_32_114 = []
counter_206_152_32_190 = []
counter_206_152_32_201 = []
counter_206_152_32_204 = []
counter_206_152_32_211 = []
counter_206_152_32_223 = []
counter_206_152_32_231 = []
counter_206_152_32_232 = []
counter_206_152_32_247 = []
counter_206_152_33_5 = []
counter_206_152_33_46 = []
counter_206_152_33_50 = []
counter_206_152_33_55 = []
counter_206_152_33_111 = []
counter_206_152_33_126 = []
counter_206_152_33_137 = []
counter_206_152_33_150 = []
counter_206_152_33_171 = []
counter_206_152_33_217 = []
counter_206_152_33_218 = []
counter_206_152_33_219 = []
counter_206_152_33_238 = []
counter_206_152_33_239 = []
counter_206_152_33_240 = []
counter_206_152_33_241 = []
counter_206_152_33_242 = []
counter_206_152_34_2 = []
counter_206_152_34_116 = []
counter_206_152_34_117 = []
counter_206_152_34_157 = []
counter_206_152_34_218 = []
counter_206_152_35_91 = []
counter_206_152_35_92 = []
counter_206_152_35_93 = []
counter_206_152_35_94 = []
counter_206_152_35_123 = []
counter_206_152_35_129 = []
counter_206_152_35_130 = []
counter_206_152_35_146 = []
counter_206_152_35_147 = []
counter_206_152_35_150 = []
counter_206_152_35_161 = []
counter_206_152_35_222 = []



for line in fhand:
    if line.startswith('2017'):
        time_temp = re.findall('20.*:[0-5][0-9]', line)
        time.extend(time_temp)
    if '206.152.32.20_counter' in line:
        temp = line.split()
        counter_206_152_32_20.append(int(temp[2]))
    if '206.152.32.21_counter' in line:
        temp = line.split()
        counter_206_152_32_21.append(int(temp[2]))
    if '206.152.32.22_counter' in line:
        temp = line.split()
        counter_206_152_32_22.append(int(temp[2]))
    if '206.152.32.23_counter' in line:
        temp = line.split()
        counter_206_152_32_23.append(int(temp[2]))
    if '206.152.32.24_counter' in line:
        temp = line.split()
        counter_206_152_32_24.append(int(temp[2]))
    if '206.152.32.25_counter' in line:
        temp = line.split()
        counter_206_152_32_25.append(int(temp[2]))
    if '206.152.32.26_counter' in line:
        temp = line.split()
        counter_206_152_32_26.append(int(temp[2]))
    if '206.152.32.27_counter' in line:
        temp = line.split()
        counter_206_152_32_27.append(int(temp[2]))
    if '206.152.32.28_counter' in line:
        temp = line.split()
        counter_206_152_32_28.append(int(temp[2]))
    if '206.152.32.29_counter' in line:
        temp = line.split()
        counter_206_152_32_29.append(int(temp[2]))
    if '206.152.32.30_counter' in line:
        temp = line.split()
        counter_206_152_32_30.append(int(temp[2]))
    if '206.152.32.31_counter' in line:
        temp = line.split()
        counter_206_152_32_31.append(int(temp[2]))
    if '206.152.32.32_counter' in line:
        temp = line.split()
        counter_206_152_32_32.append(int(temp[2]))
    if '206.152.32.39_counter' in line:
        temp = line.split()
        counter_206_152_32_39.append(int(temp[2]))
    if '206.152.32.50_counter' in line:
        temp = line.split()
        counter_206_152_32_50.append(int(temp[2]))
    if '206.152.32.54_counter' in line:
        temp = line.split()
        counter_206_152_32_54.append(int(temp[2]))
    if '206.152.32.57_counter' in line:
        temp = line.split()
        counter_206_152_32_57.append(int(temp[2]))
    if '206.152.32.62_counter' in line:
        temp = line.split()
        counter_206_152_32_62.append(int(temp[2]))
    if '206.152.32.65_counter' in line:
        temp = line.split()
        counter_206_152_32_65.append(int(temp[2]))
    if '206.152.32.114_counter' in line:
        temp = line.split()
        counter_206_152_32_114.append(int(temp[2]))
    if '206.152.32.190_counter' in line:
        temp = line.split()
        counter_206_152_32_190.append(int(temp[2]))
    if '206.152.32.201_counter' in line:
        temp = line.split()
        counter_206_152_32_201.append(int(temp[2]))
    if '206.152.32.204_counter' in line:
        temp = line.split()
        counter_206_152_32_204.append(int(temp[2]))
    if '206.152.32.211_counter' in line:
        temp = line.split()
        counter_206_152_32_211.append(int(temp[2]))
    if '206.152.32.223_counter' in line:
        temp = line.split()
        counter_206_152_32_223.append(int(temp[2]))
    if '206.152.32.231_counter' in line:
        temp = line.split()
        counter_206_152_32_231.append(int(temp[2]))
    if '206.152.32.232_counter' in line:
        temp = line.split()
        counter_206_152_32_232.append(int(temp[2]))
    if '206.152.32.247_counter' in line:
        temp = line.split()
        counter_206_152_32_247.append(int(temp[2]))
    if '206.152.33.5_counter' in line:
        temp = line.split()
        counter_206_152_33_5.append(int(temp[2]))
    if '206.152.33.46_counter' in line:
        temp = line.split()
        counter_206_152_33_46.append(int(temp[2]))
    if '206.152.33.50_counter' in line:
        temp = line.split()
        counter_206_152_33_50.append(int(temp[2]))
    if '206.152.33.55_counter' in line:
        temp = line.split()
        counter_206_152_33_55.append(int(temp[2]))
    if '206.152.33.111_counter' in line:
        temp = line.split()
        counter_206_152_33_111.append(int(temp[2]))
    if '206.152.33.126_counter' in line:
        temp = line.split()
        counter_206_152_33_126.append(int(temp[2]))
    if '206.152.33.137_counter' in line:
        temp = line.split()
        counter_206_152_33_137.append(int(temp[2]))
    if '206.152.33.150_counter' in line:
        temp = line.split()
        counter_206_152_33_150.append(int(temp[2]))
    if '206.152.33.171_counter' in line:
        temp = line.split()
        counter_206_152_33_171.append(int(temp[2]))
    if '206.152.33.217_counter' in line:
        temp = line.split()
        counter_206_152_33_217.append(int(temp[2]))
    if '206.152.33.218_counter' in line:
        temp = line.split()
        counter_206_152_33_218.append(int(temp[2]))
    if '206.152.33.219_counter' in line:
        temp = line.split()
        counter_206_152_33_219.append(int(temp[2]))
    if '206.152.33.238_counter' in line:
        temp = line.split()
        counter_206_152_33_238.append(int(temp[2]))
    if '206.152.33.239_counter' in line:
        temp = line.split()
        counter_206_152_33_239.append(int(temp[2]))
    if '206.152.33.240_counter' in line:
        temp = line.split()
        counter_206_152_33_240.append(int(temp[2]))
    if '206.152.33.241_counter' in line:
        temp = line.split()
        counter_206_152_33_241.append(int(temp[2]))
    if '206.152.33.242_counter' in line:
        temp = line.split()
        counter_206_152_33_242.append(int(temp[2]))
    if '206.152.34.2_counter' in line:
        temp = line.split()
        counter_206_152_34_2.append(int(temp[2]))
    if '206.152.34.116_counter' in line:
        temp = line.split()
        counter_206_152_34_116.append(int(temp[2]))
    if '206.152.34.117_counter' in line:
        temp = line.split()
        counter_206_152_34_117.append(int(temp[2]))
    if '206.152.34.157_counter' in line:
        temp = line.split()
        counter_206_152_34_157.append(int(temp[2]))
    if '206.152.34.218_counter' in line:
        temp = line.split()
        counter_206_152_34_218.append(int(temp[2]))
    if '206.152.35.91_counter' in line:
        temp = line.split()
        counter_206_152_35_91.append(int(temp[2]))
    if '206.152.35.92_counter' in line:
        temp = line.split()
        counter_206_152_35_92.append(int(temp[2]))
    if '206.152.35.93_counter' in line:
        temp = line.split()
        counter_206_152_35_93.append(int(temp[2]))
    if '206.152.35.94_counter' in line:
        temp = line.split()
        counter_206_152_35_94.append(int(temp[2]))
    if '206.152.35.123_counter' in line:
        temp = line.split()
        counter_206_152_35_123.append(int(temp[2]))
    if '206.152.35.129_counter' in line:
        temp = line.split()
        counter_206_152_35_129.append(int(temp[2]))
    if '206.152.35.130_counter' in line:
        temp = line.split()
        counter_206_152_35_130.append(int(temp[2]))
    if '206.152.35.146_counter' in line:
        temp = line.split()
        counter_206_152_35_146.append(int(temp[2]))
    if '206.152.35.147_counter' in line:
        temp = line.split()
        counter_206_152_35_147.append(int(temp[2]))
    if '206.152.35.150_counter' in line:
        temp = line.split()
        counter_206_152_35_150.append(int(temp[2]))
    if '206.152.35.161_counter' in line:
        temp = line.split()
        counter_206_152_35_161.append(int(temp[2]))
    if '206.152.35.222_counter' in line:
        temp = line.split()
        counter_206_152_35_222.append(int(temp[2]))
fhand.close()
c_206_152_32_20_value = []
c_206_152_32_21_value = []
c_206_152_32_22_value = []
c_206_152_32_23_value = []
c_206_152_32_24_value = []
c_206_152_32_25_value = []
c_206_152_32_26_value = []
c_206_152_32_27_value = []
c_206_152_32_28_value = []
c_206_152_32_29_value = []
c_206_152_32_30_value = []
c_206_152_32_31_value = []
c_206_152_32_32_value = []
c_206_152_32_39_value = []
c_206_152_32_50_value = []
c_206_152_32_54_value = []
c_206_152_32_57_value = []
c_206_152_32_62_value = []
c_206_152_32_65_value = []
c_206_152_32_114_value = []
c_206_152_32_190_value = []
c_206_152_32_201_value = []
c_206_152_32_204_value = []
c_206_152_32_211_value = []
c_206_152_32_223_value = []
c_206_152_32_231_value = []
c_206_152_32_232_value = []
c_206_152_32_247_value = []
c_206_152_33_5_value = []
c_206_152_33_46_value = []
c_206_152_33_50_value = []
c_206_152_33_55_value = []
c_206_152_33_111_value = []
c_206_152_33_126_value = []
c_206_152_33_137_value = []
c_206_152_33_150_value = []
c_206_152_33_171_value = []
c_206_152_33_217_value = []
c_206_152_33_218_value = []
c_206_152_33_219_value = []
c_206_152_33_238_value = []
c_206_152_33_239_value = []
c_206_152_33_240_value = []
c_206_152_33_241_value = []
c_206_152_33_242_value = []
c_206_152_34_2_value = []
c_206_152_34_116_value = []
c_206_152_34_117_value = []
c_206_152_34_157_value = []
c_206_152_34_218_value = []
c_206_152_35_91_value = []
c_206_152_35_92_value = []
c_206_152_35_93_value = []
c_206_152_35_94_value = []
c_206_152_35_123_value = []
c_206_152_35_129_value = []
c_206_152_35_130_value = []
c_206_152_35_146_value = []
c_206_152_35_147_value = []
c_206_152_35_150_value = []
c_206_152_35_161_value = []
c_206_152_35_222_value = []

for i in (range(len(time) - 1)):
    dt = datetime.strptime(time[i], "%Y-%m-%d %H:%M:%S")
    dt1 = datetime.strptime(time[i+1], "%Y-%m-%d %H:%M:%S")
    delta = dt1 - dt 
    c_206_152_32_20_value.append((counter_206_152_32_20[i+1] - counter_206_152_32_20[i])/delta.seconds)
    c_206_152_32_21_value.append((counter_206_152_32_21[i+1] - counter_206_152_32_21[i])/delta.seconds)
    c_206_152_32_22_value.append((counter_206_152_32_22[i+1] - counter_206_152_32_22[i])/delta.seconds)
    c_206_152_32_23_value.append((counter_206_152_32_23[i+1] - counter_206_152_32_23[i])/delta.seconds)
    c_206_152_32_24_value.append((counter_206_152_32_24[i+1] - counter_206_152_32_24[i])/delta.seconds)
    c_206_152_32_25_value.append((counter_206_152_32_25[i+1] - counter_206_152_32_25[i])/delta.seconds)
    c_206_152_32_26_value.append((counter_206_152_32_26[i+1] - counter_206_152_32_26[i])/delta.seconds)
    c_206_152_32_27_value.append((counter_206_152_32_27[i+1] - counter_206_152_32_27[i])/delta.seconds)
    c_206_152_32_28_value.append((counter_206_152_32_28[i+1] - counter_206_152_32_28[i])/delta.seconds)
    c_206_152_32_29_value.append((counter_206_152_32_29[i+1] - counter_206_152_32_29[i])/delta.seconds)
    c_206_152_32_30_value.append((counter_206_152_32_30[i+1] - counter_206_152_32_30[i])/delta.seconds)
    c_206_152_32_31_value.append((counter_206_152_32_31[i+1] - counter_206_152_32_31[i])/delta.seconds)
    c_206_152_32_32_value.append((counter_206_152_32_32[i+1] - counter_206_152_32_32[i])/delta.seconds)
    c_206_152_32_39_value.append((counter_206_152_32_39[i+1] - counter_206_152_32_39[i])/delta.seconds)
    c_206_152_32_50_value.append((counter_206_152_32_50[i+1] - counter_206_152_32_50[i])/delta.seconds)
    c_206_152_32_54_value.append((counter_206_152_32_54[i+1] - counter_206_152_32_54[i])/delta.seconds)
    c_206_152_32_57_value.append((counter_206_152_32_57[i+1] - counter_206_152_32_57[i])/delta.seconds)
    c_206_152_32_62_value.append((counter_206_152_32_62[i+1] - counter_206_152_32_62[i])/delta.seconds)
    c_206_152_32_65_value.append((counter_206_152_32_65[i+1] - counter_206_152_32_65[i])/delta.seconds)
    c_206_152_32_114_value.append((counter_206_152_32_114[i+1] - counter_206_152_32_114[i])/delta.seconds)
    c_206_152_32_190_value.append((counter_206_152_32_190[i+1] - counter_206_152_32_190[i])/delta.seconds)
    c_206_152_32_201_value.append((counter_206_152_32_201[i+1] - counter_206_152_32_201[i])/delta.seconds)
    c_206_152_32_204_value.append((counter_206_152_32_204[i+1] - counter_206_152_32_204[i])/delta.seconds)
    c_206_152_32_211_value.append((counter_206_152_32_211[i+1] - counter_206_152_32_211[i])/delta.seconds)
    c_206_152_32_223_value.append((counter_206_152_32_223[i+1] - counter_206_152_32_223[i])/delta.seconds)
    c_206_152_32_231_value.append((counter_206_152_32_231[i+1] - counter_206_152_32_231[i])/delta.seconds)
    c_206_152_32_232_value.append((counter_206_152_32_232[i+1] - counter_206_152_32_232[i])/delta.seconds)
    c_206_152_32_247_value.append((counter_206_152_32_247[i+1] - counter_206_152_32_247[i])/delta.seconds)
    c_206_152_33_5_value.append((counter_206_152_33_5[i+1] - counter_206_152_33_5[i])/delta.seconds)
    c_206_152_33_46_value.append((counter_206_152_33_46[i+1] - counter_206_152_33_46[i])/delta.seconds)
    c_206_152_33_50_value.append((counter_206_152_33_50[i+1] - counter_206_152_33_50[i])/delta.seconds)
    c_206_152_33_55_value.append((counter_206_152_33_55[i+1] - counter_206_152_33_55[i])/delta.seconds)
    c_206_152_33_111_value.append((counter_206_152_33_111[i+1] - counter_206_152_33_111[i])/delta.seconds)
    c_206_152_33_126_value.append((counter_206_152_33_126[i+1] - counter_206_152_33_126[i])/delta.seconds)
    c_206_152_33_137_value.append((counter_206_152_33_137[i+1] - counter_206_152_33_137[i])/delta.seconds)
    c_206_152_33_150_value.append((counter_206_152_33_150[i+1] - counter_206_152_33_150[i])/delta.seconds)
    c_206_152_33_171_value.append((counter_206_152_33_171[i+1] - counter_206_152_33_171[i])/delta.seconds)
    c_206_152_33_217_value.append((counter_206_152_33_217[i+1] - counter_206_152_33_217[i])/delta.seconds)
    c_206_152_33_218_value.append((counter_206_152_33_218[i+1] - counter_206_152_33_218[i])/delta.seconds)
    c_206_152_33_219_value.append((counter_206_152_33_219[i+1] - counter_206_152_33_219[i])/delta.seconds)
    c_206_152_33_238_value.append((counter_206_152_33_238[i+1] - counter_206_152_33_238[i])/delta.seconds)
    c_206_152_33_239_value.append((counter_206_152_33_239[i+1] - counter_206_152_33_239[i])/delta.seconds)
    c_206_152_33_240_value.append((counter_206_152_33_240[i+1] - counter_206_152_33_240[i])/delta.seconds)
    c_206_152_33_241_value.append((counter_206_152_33_241[i+1] - counter_206_152_33_241[i])/delta.seconds)
    c_206_152_33_242_value.append((counter_206_152_33_242[i+1] - counter_206_152_33_242[i])/delta.seconds)
    c_206_152_34_2_value.append((counter_206_152_34_2[i+1] - counter_206_152_34_2[i])/delta.seconds)
    c_206_152_34_116_value.append((counter_206_152_34_116[i+1] - counter_206_152_34_116[i])/delta.seconds)
    c_206_152_34_117_value.append((counter_206_152_34_117[i+1] - counter_206_152_34_117[i])/delta.seconds)
    c_206_152_34_157_value.append((counter_206_152_34_157[i+1] - counter_206_152_34_157[i])/delta.seconds)
    c_206_152_34_218_value.append((counter_206_152_34_218[i+1] - counter_206_152_34_218[i])/delta.seconds)
    c_206_152_35_91_value.append((counter_206_152_35_91[i+1] - counter_206_152_35_91[i])/delta.seconds)
    c_206_152_35_92_value.append((counter_206_152_35_92[i+1] - counter_206_152_35_92[i])/delta.seconds)
    c_206_152_35_93_value.append((counter_206_152_35_93[i+1] - counter_206_152_35_93[i])/delta.seconds)
    c_206_152_35_94_value.append((counter_206_152_35_94[i+1] - counter_206_152_35_94[i])/delta.seconds)
    c_206_152_35_123_value.append((counter_206_152_35_123[i+1] - counter_206_152_35_123[i])/delta.seconds)
    c_206_152_35_129_value.append((counter_206_152_35_129[i+1] - counter_206_152_35_129[i])/delta.seconds)
    c_206_152_35_130_value.append((counter_206_152_35_130[i+1] - counter_206_152_35_130[i])/delta.seconds)
    c_206_152_35_146_value.append((counter_206_152_35_146[i+1] - counter_206_152_35_146[i])/delta.seconds)
    c_206_152_35_147_value.append((counter_206_152_35_147[i+1] - counter_206_152_35_147[i])/delta.seconds)
    c_206_152_35_150_value.append((counter_206_152_35_150[i+1] - counter_206_152_35_150[i])/delta.seconds)
    c_206_152_35_161_value.append((counter_206_152_35_161[i+1] - counter_206_152_35_161[i])/delta.seconds)
    c_206_152_35_222_value.append((counter_206_152_35_222[i+1] - counter_206_152_35_222[i])/delta.seconds)

c_206_152_32_20 = []
c_206_152_32_21 = []
c_206_152_32_22 = []
c_206_152_32_23 = []
c_206_152_32_24 = []
c_206_152_32_25 = []
c_206_152_32_26 = []
c_206_152_32_27 = []
c_206_152_32_28 = []
c_206_152_32_29 = []
c_206_152_32_30 = []
c_206_152_32_31 = []
c_206_152_32_32 = []
c_206_152_32_39 = []
c_206_152_32_50 = []
c_206_152_32_54 = []
c_206_152_32_57 = []
c_206_152_32_62 = []
c_206_152_32_65 = []
c_206_152_32_114 = []
c_206_152_32_190 = []
c_206_152_32_201 = []
c_206_152_32_204 = []
c_206_152_32_211 = []
c_206_152_32_223 = []
c_206_152_32_231 = []
c_206_152_32_232 = []
c_206_152_32_247 = []
c_206_152_33_5 = []
c_206_152_33_46 = []
c_206_152_33_50 = []
c_206_152_33_55 = []
c_206_152_33_111 = []
c_206_152_33_126 = []
c_206_152_33_137 = []
c_206_152_33_150 = []
c_206_152_33_171 = []
c_206_152_33_217 = []
c_206_152_33_218 = []
c_206_152_33_219 = []
c_206_152_33_238 = []
c_206_152_33_239 = []
c_206_152_33_240 = []
c_206_152_33_241 = []
c_206_152_33_242 = []
c_206_152_34_2 = []
c_206_152_34_116 = []
c_206_152_34_117 = []
c_206_152_34_157 = []
c_206_152_34_218 = []
c_206_152_35_91 = []
c_206_152_35_92 = []
c_206_152_35_93 = []
c_206_152_35_94 = []
c_206_152_35_123 = []
c_206_152_35_129 = []
c_206_152_35_130 = []
c_206_152_35_146 = []
c_206_152_35_147 = []
c_206_152_35_150 = []
c_206_152_35_161 = []
c_206_152_35_222 = []
time.pop(0)
c_206_152_32_20 = zip(c_206_152_32_20_value,time) 
c_206_152_32_21 = zip(c_206_152_32_21_value,time) 
c_206_152_32_22 = zip(c_206_152_32_22_value,time) 
c_206_152_32_23 = zip(c_206_152_32_23_value,time) 
c_206_152_32_24 = zip(c_206_152_32_24_value,time) 
c_206_152_32_25 = zip(c_206_152_32_25_value,time) 
c_206_152_32_26 = zip(c_206_152_32_26_value,time) 
c_206_152_32_27 = zip(c_206_152_32_27_value,time) 
c_206_152_32_28 = zip(c_206_152_32_28_value,time) 
c_206_152_32_29 = zip(c_206_152_32_29_value,time) 
c_206_152_32_30 = zip(c_206_152_32_30_value,time) 
c_206_152_32_31 = zip(c_206_152_32_31_value,time) 
c_206_152_32_32 = zip(c_206_152_32_32_value,time) 
c_206_152_32_39 = zip(c_206_152_32_39_value,time) 
c_206_152_32_50 = zip(c_206_152_32_50_value,time) 
c_206_152_32_54 = zip(c_206_152_32_54_value,time) 
c_206_152_32_57 = zip(c_206_152_32_57_value,time) 
c_206_152_32_62 = zip(c_206_152_32_62_value,time) 
c_206_152_32_65 = zip(c_206_152_32_65_value,time) 
c_206_152_32_114 = zip(c_206_152_32_114_value,time) 
c_206_152_32_190 = zip(c_206_152_32_190_value,time) 
c_206_152_32_201 = zip(c_206_152_32_201_value,time) 
c_206_152_32_204 = zip(c_206_152_32_204_value,time) 
c_206_152_32_211 = zip(c_206_152_32_211_value,time) 
c_206_152_32_223 = zip(c_206_152_32_223_value,time) 
c_206_152_32_231 = zip(c_206_152_32_231_value,time) 
c_206_152_32_232 = zip(c_206_152_32_232_value,time) 
c_206_152_32_247 = zip(c_206_152_32_247_value,time) 
c_206_152_33_5 = zip(c_206_152_33_5_value,time) 
c_206_152_33_46 = zip(c_206_152_33_46_value,time) 
c_206_152_33_50 = zip(c_206_152_33_50_value,time) 
c_206_152_33_55 = zip(c_206_152_33_55_value,time) 
c_206_152_33_111 = zip(c_206_152_33_111_value,time) 
c_206_152_33_126 = zip(c_206_152_33_126_value,time) 
c_206_152_33_137 = zip(c_206_152_33_137_value,time) 
c_206_152_33_150 = zip(c_206_152_33_150_value,time) 
c_206_152_33_171 = zip(c_206_152_33_171_value,time) 
c_206_152_33_217 = zip(c_206_152_33_217_value,time) 
c_206_152_33_218 = zip(c_206_152_33_218_value,time) 
c_206_152_33_219 = zip(c_206_152_33_219_value,time) 
c_206_152_33_238 = zip(c_206_152_33_238_value,time) 
c_206_152_33_239 = zip(c_206_152_33_239_value,time) 
c_206_152_33_240 = zip(c_206_152_33_240_value,time) 
c_206_152_33_241 = zip(c_206_152_33_241_value,time) 
c_206_152_33_242 = zip(c_206_152_33_242_value,time) 
c_206_152_34_2 = zip(c_206_152_34_2_value,time) 
c_206_152_34_116 = zip(c_206_152_34_116_value,time) 
c_206_152_34_117 = zip(c_206_152_34_117_value,time) 
c_206_152_34_157 = zip(c_206_152_34_157_value,time) 
c_206_152_34_218 = zip(c_206_152_34_218_value,time) 
c_206_152_35_91 = zip(c_206_152_35_91_value,time) 
c_206_152_35_92 = zip(c_206_152_35_92_value,time) 
c_206_152_35_93 = zip(c_206_152_35_93_value,time) 
c_206_152_35_94 = zip(c_206_152_35_94_value,time) 
c_206_152_35_123 = zip(c_206_152_35_123_value,time) 
c_206_152_35_129 = zip(c_206_152_35_129_value,time) 
c_206_152_35_130 = zip(c_206_152_35_130_value,time) 
c_206_152_35_146 = zip(c_206_152_35_146_value,time) 
c_206_152_35_147 = zip(c_206_152_35_147_value,time) 
c_206_152_35_150 = zip(c_206_152_35_150_value,time) 
c_206_152_35_161 = zip(c_206_152_35_161_value,time) 
c_206_152_35_222 = zip(c_206_152_35_222_value,time) 
c_206_152_32_20.sort(reverse=True)
c_206_152_32_21.sort(reverse=True)
c_206_152_32_22.sort(reverse=True)
c_206_152_32_23.sort(reverse=True)
c_206_152_32_24.sort(reverse=True)
c_206_152_32_25.sort(reverse=True)
c_206_152_32_26.sort(reverse=True)
c_206_152_32_27.sort(reverse=True)
c_206_152_32_28.sort(reverse=True)
c_206_152_32_29.sort(reverse=True)
c_206_152_32_30.sort(reverse=True)
c_206_152_32_31.sort(reverse=True)
c_206_152_32_32.sort(reverse=True)
c_206_152_32_39.sort(reverse=True)
c_206_152_32_50.sort(reverse=True)
c_206_152_32_54.sort(reverse=True)
c_206_152_32_57.sort(reverse=True)
c_206_152_32_62.sort(reverse=True)
c_206_152_32_65.sort(reverse=True)
c_206_152_32_114.sort(reverse=True)
c_206_152_32_190.sort(reverse=True)
c_206_152_32_201.sort(reverse=True)
c_206_152_32_204.sort(reverse=True)
c_206_152_32_211.sort(reverse=True)
c_206_152_32_223.sort(reverse=True)
c_206_152_32_231.sort(reverse=True)
c_206_152_32_232.sort(reverse=True)
c_206_152_32_247.sort(reverse=True)
c_206_152_33_5.sort(reverse=True)
c_206_152_33_46.sort(reverse=True)
c_206_152_33_50.sort(reverse=True)
c_206_152_33_55.sort(reverse=True)
c_206_152_33_111.sort(reverse=True)
c_206_152_33_126.sort(reverse=True)
c_206_152_33_137.sort(reverse=True)
c_206_152_33_150.sort(reverse=True)
c_206_152_33_171.sort(reverse=True)
c_206_152_33_217.sort(reverse=True)
c_206_152_33_218.sort(reverse=True)
c_206_152_33_219.sort(reverse=True)
c_206_152_33_238.sort(reverse=True)
c_206_152_33_239.sort(reverse=True)
c_206_152_33_240.sort(reverse=True)
c_206_152_33_241.sort(reverse=True)
c_206_152_33_242.sort(reverse=True)
c_206_152_34_2.sort(reverse=True)
c_206_152_34_116.sort(reverse=True)
c_206_152_34_117.sort(reverse=True)
c_206_152_34_157.sort(reverse=True)
c_206_152_34_218.sort(reverse=True)
c_206_152_35_91.sort(reverse=True)
c_206_152_35_92.sort(reverse=True)
c_206_152_35_93.sort(reverse=True)
c_206_152_35_94.sort(reverse=True)
c_206_152_35_123.sort(reverse=True)
c_206_152_35_129.sort(reverse=True)
c_206_152_35_130.sort(reverse=True)
c_206_152_35_146.sort(reverse=True)
c_206_152_35_147.sort(reverse=True)
c_206_152_35_150.sort(reverse=True)
c_206_152_35_161.sort(reverse=True)
c_206_152_35_222.sort(reverse=True)
print('--- \n')
for key, val in c_206_152_32_20[:5]:
    print('UDP PPS to 206.152.32.20  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_21[:5]:
    print('UDP PPS to 206.152.32.21  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_22[:5]:
    print('UDP PPS to 206.152.32.22  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_23[:5]:
    print('UDP PPS to 206.152.32.23  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_24[:5]:
    print('UDP PPS to 206.152.32.24  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_25[:5]:
    print('UDP PPS to 206.152.32.25  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_26[:5]:
    print('UDP PPS to 206.152.32.26  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_27[:5]:
    print('UDP PPS to 206.152.32.27  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_28[:5]:
    print('UDP PPS to 206.152.32.28  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_29[:5]:
    print('UDP PPS to 206.152.32.29  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_30[:5]:
    print('UDP PPS to 206.152.32.30  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_31[:5]:
    print('UDP PPS to 206.152.32.31  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_32[:5]:
    print('UDP PPS to 206.152.32.32  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_39[:5]:
    print('UDP PPS to 206.152.32.39  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_50[:5]:
    print('UDP PPS to 206.152.32.50  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_54[:5]:
    print('UDP PPS to 206.152.32.54  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_57[:5]:
    print('UDP PPS to 206.152.32.57  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_62[:5]:
    print('UDP PPS to 206.152.32.62  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_65[:5]:
    print('UDP PPS to 206.152.32.65  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_114[:5]:
    print('UDP PPS to 206.152.32.114  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_190[:5]:
    print('UDP PPS to 206.152.32.190  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_201[:5]:
    print('UDP PPS to 206.152.32.201  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_204[:5]:
    print('UDP PPS to 206.152.32.204  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_211[:5]:
    print('UDP PPS to 206.152.32.211  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_223[:5]:
    print('UDP PPS to 206.152.32.223  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_231[:5]:
    print('UDP PPS to 206.152.32.231  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_232[:5]:
    print('UDP PPS to 206.152.32.232  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_32_247[:5]:
    print('UDP PPS to 206.152.32.247  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_33_5[:5]:
    print('UDP PPS to 206.152.33.5  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_33_46[:5]:
    print('UDP PPS to 206.152.33.46  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_33_50[:5]:
    print('UDP PPS to 206.152.33.50  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_33_55[:5]:
    print('UDP PPS to 206.152.33.55  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_33_111[:5]:
    print('UDP PPS to 206.152.33.111  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_33_126[:5]:
    print('UDP PPS to 206.152.33.126  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_33_137[:5]:
    print('UDP PPS to 206.152.33.137  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_33_150[:5]:
    print('UDP PPS to 206.152.33.150  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_33_171[:5]:
    print('UDP PPS to 206.152.33.171  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_33_217[:5]:
    print('UDP PPS to 206.152.33.217  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_33_218[:5]:
    print('UDP PPS to 206.152.33.218  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_33_219[:5]:
    print('UDP PPS to 206.152.33.219  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_33_238[:5]:
    print('UDP PPS to 206.152.33.238  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_33_239[:5]:
    print('UDP PPS to 206.152.33.239  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_33_240[:5]:
    print('UDP PPS to 206.152.33.240  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_33_241[:5]:
    print('UDP PPS to 206.152.33.241  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_33_242[:5]:
    print('UDP PPS to 206.152.33.242  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_34_2[:5]:
    print('UDP PPS to 206.152.34.2  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_34_116[:5]:
    print('UDP PPS to 206.152.34.116  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_34_117[:5]:
    print('UDP PPS to 206.152.34.117  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_34_157[:5]:
    print('UDP PPS to 206.152.34.157  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_34_218[:5]:
    print('UDP PPS to 206.152.34.218  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_35_91[:5]:
    print('UDP PPS to 206.152.35.91  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_35_92[:5]:
    print('UDP PPS to 206.152.35.92  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_35_93[:5]:
    print('UDP PPS to 206.152.35.93  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_35_94[:5]:
    print('UDP PPS to 206.152.35.94  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_35_123[:5]:
    print('UDP PPS to 206.152.35.123  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_35_129[:5]:
    print('UDP PPS to 206.152.35.129  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_35_130[:5]:
    print('UDP PPS to 206.152.35.130  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_35_146[:5]:
    print('UDP PPS to 206.152.35.146  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_35_147[:5]:
    print('UDP PPS to 206.152.35.147  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_35_150[:5]:
    print('UDP PPS to 206.152.35.150  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_35_161[:5]:
    print('UDP PPS to 206.152.35.161  at %s: %.1f' % (val, key))
print('--- \n')
for key, val in c_206_152_35_222[:5]:
    print('UDP PPS to 206.152.35.222  at %s: %.1f' % (val, key))
