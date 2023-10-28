import os
def pair_all_chr(resolution=500000,prefix='all_chr',path='./raw/'):
	f = open(prefix+'.'+str(resolution)+'.pair','w')
	for file in os.listdir(path):
		file_path=os.path.join(path,file)
		name = file.split('_')
		with open(file_path,'r') as input:
			i = -1
			for line in input:
				i = i + 1
				j = 0
				t = line.strip().split()
				for each in t:
					f.write(name[1]+'_'+str(i*resolution)+'\t'+name[1]+'_'+str(j*resolution)+'\t'+str(int(float(each)))+'\n')
					j = j + 1
	f.close()
#test  
pair_all_chr(40000,'colon')
		
