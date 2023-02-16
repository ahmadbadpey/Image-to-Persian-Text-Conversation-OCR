from flask import Blueprint

converting_blueprint = Blueprint('converting_blueprint', __name__)


@converting_blueprint.route('/convert', methods=['POST'])
def index():
    return 'Converting....'
