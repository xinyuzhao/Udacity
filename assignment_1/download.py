url = 'http://yaroslavvb.com/upload/notMNIST/'

def maybe_download(filename, expected_bytes):
    """Download a file if not present, and make sure it's the right size."""
    if not os.path.exists(filename):
        filename, _ = urllib.request.urlretrieve(url + filename, filename)
    statinfo = os.stat(filename)
    if statinfo.st_size == expected_bytes:
        print ('Found and verified', filename)
    else:
        raise Exception(
                'Failed to verify' + filename + '. Can you get to it with a browser?')
        return filename

 train_filename = maybe_download('notMNIST_large.tar.gz', 247336696)
 test_filename = maybe_download('notMNIST_small.tar.gz', 8458043)
