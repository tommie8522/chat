
def read_file(filename) :
	lines=[]
	with open(filename,'r',encoding='utf-8-sig') as f :
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new=[]
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line== 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ':' + line)
	return new
	#print(new)

def write(filename, lines):
	with open(filename,'w') as f:
		for r in lines :
			f.write(r+'\n')


def main():
	lines=read_file('input.txt')
	lines=convert(lines)
	write('output.txt',lines)

main()