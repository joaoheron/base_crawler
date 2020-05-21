import sys
import src.extractor as extractor
import src.vars as vars
import time

if len(sys.argv) < 4:
    print('This program allows the following args: \nbrowser, timeout, actions')
    sys.exit(1)
elif len(sys.argv) == 4:
    extractor.extract(sys.argv[1], sys.argv[2], sys.argv[3])
#  python -m src.main chrome 30 actions_play_youtube_video
else:
    print('Unsupported args.')
    sys.exit(1)

time.sleep(10)