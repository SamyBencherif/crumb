
# Because it looks so much more impressive minified!

import os

for f in os.listdir(os.getcwd()):
	if f[-4:] == '.cmb' and f[-8:] != '_min.cmb' and \
		not os.path.exists(f[:-4] + '_min.cmb'):
		open(f[:-4] + '_min.cmb', 'wt').write(
			''.join(open(f, 'rt').read().split())
		)
	elif f[-4:] == '.cmb' and f[-8:] != '_min.cmb':
		if ''.join(open(f, 'r').read().split()) != open(f[:-4] + '_min.cmb', 'r').read():
			print (f + ' has already been minified but has been updated since. Please delete the existing _min file and rerun to minify the updates.')
