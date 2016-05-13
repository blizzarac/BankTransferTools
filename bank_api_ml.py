__author__ = 'alexanderstolz'

import bank_api
from sklearn import linear_model

# Predicts the saldo for a given date using a bayesianridge linear model regression
def prefict_saldo(year, month, day):
    all_transfers = bank_api.getAllTransfers()

    clf = linear_model.BayesianRidge()

    features = []
    labels = []

    for trsf in all_transfers:
        features.append([trsf['datum'].year, trsf['datum'].month, trsf['datum'].day])
        labels.append(trsf['saldo'])

    clf = clf.fit(features, labels)

    return clf.predict([year, month, day])