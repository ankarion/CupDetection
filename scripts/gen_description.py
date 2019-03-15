import os
size = 100
def create_pos_n_neg():
	for file_type in ['pos','neg']:
		for img in os.listdir("images/"+file_type):
			if file_type == 'pos':
				line = file_type+'/'+img+' 1 0 0 {0} {0}\n'.format(size)
				with open('images/info.dat','a') as f:
					f.write(line)
			elif file_type == 'neg':
				line = file_type+'/'+img+'\n'
				with open('images/bg.txt','a') as f:
					f.write(line)

create_pos_n_neg()
