import sys
import extractor
import vars

if len(sys.argv) < 2:
    print('This program allows the following args: \nurl, download_dir, timeout, browser, fileformat')
    sys.exit(1)
elif len(sys.argv) == 2:
    # OPTS: url, download_dir, timeout, gecko/chrome, fileformat
    try:
        extractor.download_file(sys.argv[1])
    except:
        print('Error during download.')
        sys.exit(1)
else:
    print('Unsupported args.')
    sys.exit(1)
