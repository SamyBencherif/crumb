import crumb

# sanity check

print(crumb.execute('vCfmCbvS0sS1vi0Uvx0vy0cxiyxy4axffxS0016vx0ayfaiffyS0016'))

# insanity check

print(crumb.execute('waah bah bah foo fo fo fooo foo U f2hu23h uhf9uwb  bwfiu3bfiwubncjwnj j'))

# generate programs
charset=[chr(i) for i in range(65,65+26)]+[chr(i) for i in range(97,97+26)]+[chr(i) for i in range(48,48+10)]
def genprog(x, y):
	p = ""
	while x:
		p += charset[x%len(charset)]
		x//=len(charset)
	# p += 'U'  # seems unnecessary. U's are cropping up plenty on their own
	while y:
		p += charset[y%len(charset)]
		y//=len(charset)
	return p

MAGIC = 2**(11*2**9)

zrange = lambda n: range(1, n+1)

for x in zrange(1000):
	for y in zrange(1000):
		if crumb.execute(genprog(x*MAGIC, y*MAGIC)):
			# found an interesting one!
			print(x,y)
			print('Begin Src')
			print('-------------------')
			print('\n\n')
			print(genprog(x*MAGIC, y*MAGIC))
			exit()