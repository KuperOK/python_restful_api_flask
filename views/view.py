from app import app
#from app import db
from flask import render_template, request, jsonify, g, redirect, json
from models.models import *
#import json
# from rest.api_dept import *
# from sqlalchemy import update

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/departments", methods=['GET'])
def get_all_d():
    """READ operation from table Department"""
    get_all_dep = Department.query.all()
    objects = [{"dep_id": department.dep_id, "dep_name": department.dep_name} for department in get_all_dep]
    return render_template("departments.html", objects=objects)


@app.route("/employees", methods=['GET'])
def get_all_e():
    """READ operation from table Department"""
    get_all_emp = db.session.query(Employee, Department).filter(Employee.dep_id == Department.dep_id).all()
    objects = [{"emp_id": employee.emp_id, "emp_name": employee.emp_name,\
                 'date_of_birth': employee.date_of_birth, 'salary': employee.salary, 'dep_name': department.dep_name} for employee, department in get_all_emp]
    return render_template("employees.html", objects=objects)


# @app.route("/api/departments", methods=['GET'])
# def get_all_d1():
#     """READ operation from table Department"""
#     get_all_dep = Department.query.all()
#     if not get_all_dep:
#         return jsonify({'message':'Department table is empty'}), 204
#     all_dep = [{"dep_id": department.dep_id, "dep_name": department.dep_name} for department in get_all_dep]
#     return jsonify(all_dep), 200


# @app.route("/api/employee", methods=['GET'])
# def get_all_e():
#     """READ operation from table Employee all records"""
#     get_all_emp = Employee.query.all()
#     return render_template("employees.html", objects = get_all_emp)


# @app.route("/api/departments/add", methods=['POST'])
# def add_dep():
#     """create operation
#        add new record in Department table"""
#     dep_name = request.json.get('dep_name')
#     get_dep = Department.query.filter(Department.dep_name == dep_name).first()
#     if get_dep:
#         return jsonify({"message": "Dept {} is already exist".format(dep_name)}), 409
#     dept = Department(dep_name=dep_name)
#     db.session.add(dept)
#     db.session.commit()
#     return jsonify({"message": "Created"}), 201


# @app.route('/api/departments/<param>', methods=['DELETE'])
# def dep_del_by_name(param):
#     """del by id or name"""
#     if param.isdigit():
#         del_dep = Department.query.filter(Department.dep_id == int(param)).delete()
#     else:
#         del_dep = Department.query.filter(Department.dep_name == param).delete()
#     if not del_dep:
#         return jsonify({"message": "Not found"}), 404
#     db.session.commit()
#     return jsonify({"message": "Deleted"}), 204


# @app.route('/api/departments/<param>', methods=['GET'])
# def get_dep_id_name(param):
#     """get department by id or name"""
#     if param.isdigit():
#         get_dep = Department.query.filter(Department.dep_id == int(param))
#     else:
#         get_dep = Department.query.filter(Department.dep_name == param)
#     some_depts = [{"dep_id": department.dep_id, "dep_name": department.dep_name} for department in get_dep]
#     if not some_depts:
#         return jsonify({"message": "Not found"}), 204
#     return jsonify(some_depts), 200

# @app.route('/api/departments/<int:_id>', methods=['PUT'])
# def put_dep_name(_id):
#     """update department name by id or name"""
#     put_dep = Department.query.filter(Department.dep_id == _id).first()
#     params = request.json
#     if not put_dep:
#         return jsonify({"message": "No dept with id: {}".format(_id)}), 400
#     for k, v in params.items():
#         setattr(put_dep, k, v)
#     db.session.commit()
#     return jsonify({"message": "Updated"}), 201