num_classes = 10

def extract(filename):
    tar = tarfile.open(filename)
    tar.extractall()
    tar.close()
    root = os.path.splitext(os.path.splitext(filename)[0])[0]  # remove .tar.gz
    data_folders = [os.path.join(root, d) for d in sorted(os.listdir(root))]
    if len(data_folders) != num_classes:
        raise Exception(
                'Expected %d folders, one per class. Found %d instead.' % (
                    num_classes, len(data_folders)))
    print(data_folders)
    return data_folders

train_folders = extract('notMNIST_large.tar.gz')
test_folders = extract('notMNIST_small.tar.gz')
