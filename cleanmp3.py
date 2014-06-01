import eyeD3
import glob

indir = '/home/mcslater/Music/NIG*.mp3'

for fname in glob.glob(indir):
	tag = eyeD3.Tag()
	tag.link(fname)
	print fname
	tag.setArtist('Turtles')
	print tag.getArtist()
