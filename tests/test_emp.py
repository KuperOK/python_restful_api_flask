import pytest
from main import app
from app import db
from models.models import Employee, Department
from datetime import datetime
import json


def create_empty_db():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    db.drop_all()
    db.create_all()

def create_db_insert_dep():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    db.drop_all()
    db.create_all()
    db.session.add(Department(dep_name='IT'))
    db.session.add(Employee(emp_name='KLM', date_of_birth=datetime.strptime('1980-11-11', '%Y-%m-%d'), salary='1500', dep_id='1'))
    db.session.commit()


@pytest.fixture
def client():
    create_db_insert_dep()
    with app.test_client() as client:
        yield client

@pytest.fixture
def client2():
    create_empty_db()
    with app.test_client() as client2:
        yield client2

def test_e1(client):
    """check status code from get Department table"""
    res = client.get('/api/employees')
    assert res.status_code == 200
    assert res.headers['Content-Type'] == 'application/json'
    assert len(res.json) == 1


def test_e2(client2):
    """check "No content" in Department table"""
    res = client2.get('/api/employees')
    assert res.status_code == 204


def test_e3(client):
    """check get department by id if exists"""
    res = client.get('/api/employees/1', )
    assert res.status_code == 200

def test_e4(client):
    """check get department by id if  not exists"""
    res = client.get('/api/employees/2', )
    assert res.status_code == 204

def test_e5(client):
    """check get department by name if exists"""
    res = client.get('/api/employees/KLM', )
    assert res.json[0]['emp_name'] == 'KLM'

def test_e6(client):
    """check get department by name if not exists"""
    res = client.get('/api/employees/SEC', )
    assert res.status_code == 204

def test_e7(client):
    """check delete Department by id if dept exists"""
    res = client.delete('/api/employees/1')
    assert res.status_code == 204

def test_e8(client):
    """check delete Department by id if dept not exists"""
    res = client.delete('/api/employees/105')
    assert res.status_code == 404

def test_e9(client):
    """check delete Department by name if dept exists"""
    res = client.delete('/api/employees/KLM')
    assert res.status_code == 204

def test_e10(client):
    """check delete Department by name if dept not exists"""
    res = client.delete('/api/employees/SEC')
    assert res.status_code == 404


def test_e11(client):
    """check update Department by id if dept exists"""
    res = client.put('/api/employees/1', data=json.dumps({'emp_name': 'IVAN'}),\
                     content_type='application/json')
    assert res.status_code == 204

def test_e12(client):
    """check Update Department by id if dept not exists"""
    res = client.put('/api/employees/101', data=json.dumps({'emp_name': 'IVAN'}),\
                     content_type='application/json')
    assert res.status_code == 404

def test_e13(client):
    """check update Department by name if dept exists"""
    res = client.put('/api/employees/KLM', data=json.dumps({'emp_name': 'IVAN'}),\
                     content_type='application/json')
    assert res.status_code == 204

def test_e14(client):
    """check Update Department by name if dept not exists"""
    res = client.put('/api/employees/ivan', data=json.dumps({'dep_name': 'KLM'}),\
                     content_type='application/json')
    assert res.status_code == 404


def test_e15(client):
    """check  post Department if dept not exists"""
    res = client.post('/api/employees/add', data=json.dumps({'emp_name': 'IVAN', 'date_of_birth':'1980-11-11',
                                                             'salary':'1500','dep_id':'1'}),\
                     content_type='application/json')
    assert res.status_code == 201

def test_e16(client):
    """check  post Department if dept exists"""
    res = client.post('/api/employees/add', data=json.dumps({'emp_name': 'KLM', 'date_of_birth':'2001-10-10',
                                                             'salary':'2500.50','dep_id':'1'}),\
                     content_type='application/json')
    assert res.status_code == 409

