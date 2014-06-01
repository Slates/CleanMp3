import eyeD3
import glob
import sys

indir = sys.argv[1] + "*"
# indir = "/home/mcslater/Music/*.mp3"

for fname in glob.glob(indir):
	if fname.endswith('.mp3'):
		tag = eyeD3.Tag()
		tag.link(fname)
		songtitle = tag.getArtist() + " - " + tag.getTitle()
		print songtitle
