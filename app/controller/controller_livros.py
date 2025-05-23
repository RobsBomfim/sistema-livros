from flask import Blueprint, request, jsonify
from http import HTTPStatus
from app.service.service_livros import ConsultaService
from app.repository.repository_livros import ConsultaRepository

consulta_bp = Blueprint('consulta', __name__)
repo = ConsultaRepository()
service = ConsultaService(repo)

@consulta_bp.route('/consultas', methods=['POST'])
def criar_consulta():
    data = request.get_json()
    try:
        nova_consulta = service.criar(data)
        return jsonify(nova_consulta), HTTPStatus.CREATED
    except Exception as e:
        return jsonify({"erro": str(e)}), HTTPStatus.BAD_REQUEST

@consulta_bp.route('/consultas', methods=['GET'])
def listar_consultas():
    try:
        consultas = service.listar_todas()
        return jsonify(consultas), HTTPStatus.OK
    except Exception as e:
        return jsonify({"erro": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

@consulta_bp.route('/consultas/<int:consulta_id>', methods=['GET'])
def obter_consulta(consulta_id):
    consulta = repo.pegar_por_id(consulta_id)
    if not consulta:
        return jsonify({"erro": "Consulta não encontrada"}), HTTPStatus.NOT_FOUND
    return jsonify(consulta), HTTPStatus.OK

@consulta_bp.route('/consultas/<int:consulta_id>', methods=['DELETE'])
def deletar_consulta(consulta_id):
    resultado = service.deletar(consulta_id)
    if not resultado:
        return jsonify({"erro": "Consulta não encontrada"}), HTTPStatus.NOT_FOUND
    return '', HTTPStatus.NO_CONTENT