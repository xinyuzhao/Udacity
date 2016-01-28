def split_train_valid(X, Y):
    
    train_size = round(0.7 * Y.shape[0])
    valid_size = round(0.3 * Y.shape[0])
    
    valid_dataset = X[:valid_size,:,:]
    valid_labels = Y[:valid_size]
    train_dataset = X[valid_size:valid_size+train_size,:,:]
    train_labels = Y[valid_size:valid_size+train_size]
    print('Training', train_dataset.shape, train_labels.shape)
    print('Validation', valid_dataset.shape, valid_labels.shape)
    
    return valid_dataset, valid_labels, train_dataset, train_labels

valid_dataset, valid_labels, train_dataset, train_labels = split_train_valid(train_dataset, train_labels)
    