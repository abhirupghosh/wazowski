from google.cloud import storage
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/aanyakhandelwal/Desktop/MoneyTree-8b6295880aab.json"

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'moneytree-95c46',
})

db = firestore.client()
doc_ref = db.collection(u'root').document(u'1')
doc_ref.set({
    u'Item': u'Apple',
    u'MRP': 1.01,
    u'Demand': 23,
    u'Supply': 20,
    u'Shelf life': 7,
    u'Date of purchase': u'12/31/17',
    u'Demand projection in one day': 37.94,
    u'Demand projection in two days': 39.96,
    u'Demand projection in three days': 42.78,
    u'Days till expiry': None,
    u'New price (if applicable)': None,
    u'Recommendation': None,
})
doc_ref = db.collection(u'root').document(u'2')
doc_ref.set({
    u'Item': u'Tomato',
    u'MRP': 2.50,
    u'Demand': 23,
    u'Supply': 40,
    u'Shelf life': 7,
    u'Date of purchase': u'12/31/17',
    u'Demand projection in one day': 18.00,
    u'Demand projection in two days': 17.34,
    u'Demand projection in three days': 19.05,
    u'Days till expiry': None,
    u'New price (if applicable)': None,
    u'Recommendation': None,
})
doc_ref = db.collection(u'root').document(u'3')
doc_ref.set({
    u'Item': u'Orange',
    u'MRP': 3,
    u'Demand': 29,
    u'Supply': 45,
    u'Shelf life': 10,
    u'Date of purchase': u'12/31/17',
    u'Demand projection in one day': 10.30,
    u'Demand projection in two days': 15.49,
    u'Demand projection in three days': 9.08,
    u'Days till expiry': None,
    u'New price (if applicable)': None,
    u'Recommendation': None,
})
doc_ref = db.collection(u'root').document(u'4')
doc_ref.set({
    u'Item': u'Salt',
    u'MRP': 4,
    u'Demand': 15,
    u'Supply': 15,
    u'Shelf life': 730,
    u'Date of purchase': u'12/31/17',
    u'Demand projection in one day': 10.64,
    u'Demand projection in two days': 15.37,
    u'Demand projection in three days': 8.32,
    u'Days till expiry': None,
    u'New price (if applicable)': None,
    u'Recommendation': None,
})
doc_ref = db.collection(u'root').document(u'5')
doc_ref.set({
    u'Item': u'Asparagus',
    u'MRP': 3.50,
    u'Demand': 17,
    u'Supply': 23,
    u'Shelf life': 4,
    u'Date of purchase': u'12/31/17',
    u'Demand projection in one day': 70.46,
    u'Demand projection in two days': 76.53,
    u'Demand projection in three days': 81.72,
    u'Days till expiry': None,
    u'New price (if applicable)': None,
    u'Recommendation': None,
})
doc_ref = db.collection(u'root').document(u'6')
doc_ref.set({
    u'Item': u'Onion',
    u'MRP': 2.62,
    u'Demand': 53,
    u'Supply': 90,
    u'Shelf life': 14,
    u'Date of purchase': u'12/31/17',
    u'Demand projection in one day': 76.08,
    u'Demand projection in two days': 70.50,
    u'Demand projection in three days': 68.62,
    u'Days till expiry': None,
    u'New price (if applicable)': None,
    u'Recommendation': None,
})
doc_ref = db.collection(u'root').document(u'7')
doc_ref.set({
    u'Item': u'Avocado',
    u'MRP': 2.10,
    u'Demand': 55,
    u'Supply': 67,
    u'Shelf life': 3,
    u'Date of purchase': u'12/31/17',
    u'Demand projection in one day': 93.25,
    u'Demand projection in two days': 76.32,
    u'Demand projection in three days': 67.61,
    u'Days till expiry': None,
    u'New price (if applicable)': None,
    u'Recommendation': None,
})
doc_ref = db.collection(u'root').document(u'8')
doc_ref.set({
    u'Item': u'Carrot',
    u'MRP': 3,
    u'Demand': 62,
    u'Supply': 77,
    u'Shelf life': 14,
    u'Date of purchase': u'12/31/17',
    u'Demand projection in one day': 61.68,
    u'Demand projection in two days': 64.70,
    u'Demand projection in three days': 76.89,
    u'Days till expiry': None,
    u'New price (if applicable)': None,
    u'Recommendation': None,
})
doc_ref = db.collection(u'root').document(u'9')
doc_ref.set({
    u'Item': u'Pear',
    u'MRP': 1.77,
    u'Demand': 50,
    u'Supply': 55,
    u'Shelf life': 6,
    u'Date of purchase': u'12/31/17',
    u'Demand projection in one day': 75.53,
    u'Demand projection in two days': 66.24,
    u'Demand projection in three days': 77.13,
    u'Days till expiry': None,
    u'New price (if applicable)': None,
    u'Recommendation': None,
})