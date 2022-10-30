from typing import Optional
from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials, firestore

# Use a service account.
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# create
doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})

# read
users_ref = db.collection(u'users')
docs = users_ref.stream()
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')

# update
res = db.collection(u'users').document('user01').update({
    'born': 300
})

# delete
# db.collection(u'users').document('user01').delete()

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}