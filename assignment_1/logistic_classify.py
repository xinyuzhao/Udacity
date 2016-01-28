def logistic_classify(X, Y):
    clf = LogisticRegression(C = 1)
    clf.fit(X, Y)
    
    return clf