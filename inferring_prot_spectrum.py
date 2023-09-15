import math

def file_reader(file):
    ans =[]
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n')
            ans.append(line)
    return ans
    
mass_dict = {'A':71.03711,'C':103.00919,'D':115.02694,'E':129.04259,'F':147.06841,
             'G':57.02146,'H':137.05891,'I':113.08406,'K':128.09496,'L':113.08406,
             'M':131.04049,'N':114.04293,'P':97.05276,'Q':128.05858,'R':156.10111,
             'S':87.03203,'T':101.04768,'V':99.06841,'W':186.07931,'Y':163.06333 
             }
num_list = file_reader('inferring_prot_spectrum.txt')
num_list_ros = [3524.8542, 3710.9335, 3841.974, 3970.0326, 4057.0646]
prot = []
for i in range(1,len(num_list)):
    weight = float(num_list[i]) - float(num_list[i-1])
    for key,value in mass_dict.items():
   
        if math.isclose(weight,value,rel_tol = 1e-05):
            prot.append(key)
            break
        
prot_str = ''.join(prot)
print(prot_str)
            
            