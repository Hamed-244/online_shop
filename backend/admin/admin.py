from flask import Blueprint , jsonify

admin_blueprint = Blueprint('admin_blueprint', __name__ ,url_prefix='/admin')

@admin_blueprint.route('/')
def hello_admin():
    return jsonify({'message' : 'this is a panel admin preview!'})