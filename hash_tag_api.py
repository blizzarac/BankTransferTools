import bank_api
import alphabet_ml
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def classify_transfers():
	transfers = bank_api.getAllTransfers()
	words = dict()

	for transfer in transfers:
		info1 = str(transfer['zweck'])
		info2 = str(transfer['zweck2'])
		info3 = str(transfer['zweck3'])
	
		alphabet_ml.hash_string(info1 + ' '+ info2 + ' ' +info3, words)


