from flask import Flask, jsonify, request


app = Flask(__name__)

name = {'name':'ehdwn1tp'}
string = {'value':'string'}
weapons = [
    {'id':1, 'name':'sword', 'stock':3},
    {'id':2, 'name':'gun', 'stock':2}
]


@app.route('/whoami')
def get_id():
    return jsonify(name)


@app.route('/echo')
def return_string():
    args = request.args.get('string', None, str)
    
    if args != 'string':
        return 'wrong query'
    
    return jsonify(string)


@app.route('/weapon', methods=['GET', 'POST'])
def read_create_weapon():

    # GET
    if request.method == 'GET':
        return jsonify(weapons)

    # POST
    elif request.method == 'POST':
        q = request.get_json()
        next_id = weapons[-1]['id'] + 1

        if check_post_data(q):
            new_weapon = {'id' : next_id, 'name' : q['name'], 'stock' : q['stock']}
            weapons.append(new_weapon)
            return jsonify(new_weapon)
        
        else:
            return 'Wrong Attempt'
        
    else:
        return 'WRONG REQUEST'


@app.route('/weapon/<int:id_>', methods=['PUT', 'DELETE'])
def update_delete_weapon(id_):

    #  PUT
    if request.method == 'PUT':
        q = request.get_json()
        idx = find_weapon_by_id(weapons, id_)

        if idx == -1:
            return 'Wrong ID'
        
        else:
            update_weapon = {'id' : id_, 'name' : q['name'], 'stock' : q['stock']}
            weapons[idx] = update_weapon
            return jsonify(update_weapon)
    
    # DELETE
    elif request.method == 'DELETE':
        idx = find_weapon_by_id(weapons, id_)

        if idx == -1:
            return 'Wrong ID'
        
        else:
            del weapons[idx]
            return jsonify(weapons)

    else:
        return 'WRONG REQUEST'


@app.route('/reset')
def reset_db():
    global weapons
    weapons = [
        {'id':1, 'name':'sword', 'stock':3},
        {'id':2, 'name':'gun', 'stock':2}
    ]
    return jsonify(weapons)



############## 데이터 검수 및 처리용 함수
def check_post_data(data):
    if list(data.keys()) == ['name', 'stock']:
        return True
    else:
        return False

def find_weapon_by_id(weapons, id_):
    # id_가 0 또는 음수일 경우, -1을 반환
    if id_ <= 0:
        return -1

    # 인덱스 탐색
    for idx, w in enumerate(weapons):
        if w['id'] == id_:
            return idx
        else: continue
    
    # 없을 경우 -1 반환
    else:
        return -1


if __name__ == '__main__':
    app.run()