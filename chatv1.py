
def read_file(filename) :
	lines=[]
	with open(filename,'r',encoding='utf-8-sig') as f :
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	person = None
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count=0
	viki_sticker_count=0
	for line in lines:
		s = line.split(' ')
		name=s[1]
		time=s[0]
		if name == 'Allen' :
			if s[2]=='貼圖':
				allen_sticker_count+=1
			else:
				for m in s[2:]:
			 		allen_word_count+=len(m)
		elif name == 'Viki':
			if s[2]=='貼圖':
				viki_sticker_count+=1
			else:
				for m in s[2:]:
				 	viki_word_count+=len(m)
	print('allen說了', allen_word_count,'allen傳了',allen_sticker_count)		
	print('viki說了', viki_word_count,'viki傳了',viki_sticker_count) 

	return len
	#print(new)

def write(filename, lines):
	with open(filename,'w') as f:
		for r in lines :
			f.write(r+'\n')


def main():
	lines=read_file('LINE-Viki.txt')
	lines=convert(lines)
	#write('output.txt',lines)

main()