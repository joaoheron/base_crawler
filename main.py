import sys
import extractor
import vars
import time

if len(sys.argv) < 2:
    print('This program allows the following args: \nbrowser, timeout')
    sys.exit(1)
elif len(sys.argv) < 5:
    try:
        extractor.extract(sys.argv[1], sys.argv[2])
    except:
        print('Error during download.')
        sys.exit(1)
else:
    print('Unsupported args.')
    sys.exit(1)

time.sleep(10)