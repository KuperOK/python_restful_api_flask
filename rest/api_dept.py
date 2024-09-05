from app import app
from app import db
from models.models import Department
from flask import jsonify, request, json


@app.route("/api/departments", methods=['GET'])
def get_all_d1():
    """READ operation from table Department"""
    get_all_dep = Department.query.all()
    if not get_all_dep:
        return jsonify({'message': 'Department table is empty'}), 204
    all_dep = [{"dep_id": department.dep_id, "dep_name": department.dep_name} for department in get_all_dep]
    return jsonify(all_dep), 200


@app.route('/api/departments/<param>', methods=['GET'])
def get_dep_id_name(param):
    """get department by id or name"""
    if param.isdigit():
        get_dep = Department.query.filter(Department.dep_id == int(param))
    else:
        get_dep = Department.query.filter(Department.dep_name == param)
    some_depts = [{"dep_id": department.dep_id, "dep_name": department.dep_name} for department in get_dep]
    if not some_depts:
        return jsonify({"message": "Not found"}), 204
    return jsonify(some_depts), 200


@app.route("/api/departments/add", methods=['POST'])
def add_dep():
    """create operation
       add new record in Department table"""
    dep_name = request.json.get('dep_name')
    get_dep = Department.query.filter(Department.dep_name == dep_name)
    if get_dep.count() > 0:
        return jsonify({"message": "Dept {} is already exist".format(dep_name)}), 409
    dept = Department(dep_name=dep_name)
    db.session.add(dept)
    db.session.commit()
    return jsonify({"message": "Created"}), 201

#
# @app.route('/api/departments/<int:param>', methods=['PUT'])
# def put_dep_name(param):
#     """update department name by id """
#     params = request.json.get('dep_name')
#     put_dep = Department.query.filter(Department.dep_id == param).first()
#     # if param.isdigit():
#     #     put_dep = Department.query.filter(Department.dep_id == int(param)).first()
#     # else:
#     #     put_dep = Department.query.filter(Department.dep_name == param).first()
#     if not put_dep:
#         return jsonify({"message": "No such dept: {}".format(param)}), 204
#     db.session.query(Department).filter(Department.dep_id == int(param)).update({Department.dep_name: params})
#     db.session.commit()
#     return jsonify({"message": "Updated"}), 200


@app.route('/api/departments/<param>', methods=['PUT'])
def put_dep_name(param):
    """update department name by id or name"""
    params = request.json.get('dep_name')

    #put_dep = Department.query.filter(Department.dep_id == param).first()
    if param.isdigit():
        put_dep = Department.query.filter(Department.dep_id == int(param))#.first()
    else:
        put_dep = Department.query.filter(Department.dep_name == param)#.first()
    if put_dep.count() == 0:
        return jsonify({"message": "No such dept".format(param)}), 404
    if param.isdigit():
        db.session.query(Department).filter(Department.dep_id == int(param)).update({Department.dep_name: params})
    else:
        db.session.query(Department).filter(Department.dep_name == param).update({Department.dep_name: params})
    db.session.commit()
    return jsonify({"message": "Updated"}), 204


@app.route('/api/departments/<param>', methods=['DELETE'])
def dep_del_by_name(param):
    """del by id or name"""
    if param.isdigit():
        del_dep = Department.query.filter(Department.dep_id == int(param)).delete()
    else:
        del_dep = Department.query.filter(Department.dep_name == param).delete()
    if not del_dep:
        return jsonify({"message": "Not found"}), 404
    db.session.commit()
    return jsonify({"message": "Deleted"}), 204
