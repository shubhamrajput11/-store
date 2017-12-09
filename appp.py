from flask import Flask,jsonify,request,render_template

app=Flask(__name__)

stores=[
    {
       'name':'my wonderfull store',
       'items':[
          {
          'name':'my item',
          'price':15
          }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

#POST /store data: {name:,price}
@app.route('/store',methods=['POST'])
def create_store():
    request_data=request.ret_json()
    new_store={
        'name':request_data['name'],
        'items':[]
    }
    store.append(new_store)
    return jsonify(new_store)

#GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify({'message':'store not found'})


#GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

#POST /store/<string:name>/item: , price:
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    request_data=request.get.json()
    for store in stores:
        if store['name']==name:
            new_item={
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})

#GET /Store/<string:name>/item
@app.route('/Store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify({'items':store['items']})
    return jsonify({'message':'store not found'})



app.run(port=5567)
