import sys
import src.extractor as extractor
import src.vars as vars
import time

if len(sys.argv) < 3:
    print('This program allows the following args: \nbrowser, timeout')
    sys.exit(1)
elif len(sys.argv) == 3:
    extractor.extract(sys.argv[1], sys.argv[2])
#  python -m src.main chrome 30 actions_play_youtube_video
else:
    print('Unsupported args.')
    sys.exit(1)
