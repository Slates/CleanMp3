import eyeD3
import glob
import sys

indir = sys.argv[1]

for fname in glob.glob(indir):
	tag = eyeD3.Tag()
	tag.link(fname)
	print fname
