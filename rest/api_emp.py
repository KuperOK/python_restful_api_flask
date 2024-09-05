from app import app
from app import db
from models.models import Employee, Department
from flask import jsonify, request
from datetime import datetime


@app.route("/api/employees", methods=['GET'])
def get_all_e1():
    """READ operation from table Employee"""
    get_all_emp = db.session.query(Employee, Department).filter(Employee.dep_id == Department.dep_id).all()
    if not get_all_emp:
        return jsonify({'message': 'Employee table is empty'}), 204
    objects = [{"emp_id": employee.emp_id, "emp_name": employee.emp_name, \
                'date_of_birth': employee.date_of_birth, 'salary': employee.salary, 'dep_name': department.dep_name}\
               for employee, department in get_all_emp]
    return jsonify(objects), 200


@app.route('/api/employees/<param>', methods=['GET'])
def get_emp_id_name(param):
    """get employee by id or name"""
    if param.isdigit():
        get_emp = Employee.query.filter(Employee.emp_id == int(param))
    else:
        get_emp = Employee.query.filter(Employee.emp_name == param)
    some_empts = [{'emp_id': employee.emp_id, 'emp_name': employee.emp_name,\
                  'date_of_birth': employee.date_of_birth, 'salary': employee.salary, 'dep_id': employee.dep_id}\
                  for employee in get_emp]
    if not some_empts:
        return jsonify({"message": "Not found"}), 204
    return jsonify(some_empts), 200


@app.route("/api/employees/add", methods=['POST'])
def add_emp():
    """create operation
       add new record in Employee table"""
    emp_name = request.json.get('emp_name')
    emp_date = request.json.get('date_of_birth')
    emp_sal = request.json.get('salary')
    emp_dep_id = request.json.get('dep_id')
    get_emp = Employee.query.filter(Employee.emp_name == emp_name)
    if get_emp.count() > 0:
        return jsonify({"message": "Empt {} is already exist".format(emp_name)}), 409
    emp = Employee(emp_name=emp_name, date_of_birth=datetime.strptime(emp_date, '%Y-%m-%d'), salary=emp_sal, dep_id=emp_dep_id)
    db.session.add(emp)
    db.session.commit()
    return jsonify({"message": "Created"}), 201


@app.route('/api/employees/<param>', methods=['PUT'])
def put_emp_name(param):
    """update employee name by id or name"""
    params = request.json.get('emp_name')
    if param.isdigit():
        put_emp = Employee.query.filter(Employee.emp_id == int(param))
    else:
        put_emp = Employee.query.filter(Employee.emp_name == param)
    if put_emp.count() == 0:
        return jsonify({"message": "No employee {}".format(param)}), 404
    if param.isdigit():
        db.session.query(Employee).filter(Employee.emp_id == int(param)).update({Employee.emp_name: params})
    else:
        db.session.query(Employee).filter(Employee.emp_name == param).update({Employee.emp_name: params})
    db.session.commit()
    return jsonify({"message": "Updated"}), 204


@app.route('/api/employees/<param>', methods=['DELETE'])
def emp_del_by_name(param):
    """del by id or name"""
    if param.isdigit():
        del_emp = Employee.query.filter(Employee.emp_id == int(param)).delete()
    else:
        del_emp = Employee.query.filter(Employee.emp_name == param).delete()
    if not del_emp:
        return jsonify({"message": "Not found"}), 404
    db.session.commit()
    return jsonify({"message": "Deleted"}), 204
