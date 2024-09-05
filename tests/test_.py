import pytest
from main import app
from app import db
from models.models import Department
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

def test_d1(client):
    """check status code from get Department table"""
    res = client.get('/api/departments')
    assert res.status_code == 200
    assert res.headers['Content-Type'] == 'application/json'
    assert len(res.json) == 1


def test_d2(client2):
    """check "No content" in Department table"""
    res = client2.get('/api/departments')
    assert res.status_code == 204


def test_d3(client):
    """check get department by id if exists"""
    res = client.get('/api/departments/1', )
    assert res.status_code == 200

def test_d4(client):
    """check get department by id if  not exists"""
    res = client.get('/api/departments/2', )
    assert res.status_code == 204

def test_d5(client):
    """check get department by name if exists"""
    res = client.get('/api/departments/IT', )
    assert res.json[0]['dep_name'] == 'IT'

def test_d6(client):
    """check get department by name if not exists"""
    res = client.get('/api/departments/SEC', )
    assert res.status_code == 204

def test_d7(client):
    """check delete Department by id if dept exists"""
    res = client.delete('/api/departments/1')
    assert res.status_code == 204

def test_d8(client):
    """check delete Department by id if dept not exists"""
    res = client.delete('/api/departments/105')
    assert res.status_code == 404

def test_d9(client):
    """check delete Department by name if dept exists"""
    res = client.delete('/api/departments/IT')
    assert res.status_code == 204

def test_d10(client):
    """check delete Department by name if dept not exists"""
    res = client.delete('/api/departments/SEC')
    assert res.status_code == 404


def test_d11(client):
    """check update Department by id if dept exists"""
    res = client.put('/api/departments/1', data=json.dumps({'dep_name': 'Finance'}),\
                     content_type='application/json')
    assert res.status_code == 204

def test_d12(client):
    """check Update Department by id if dept not exists"""
    res = client.put('/api/departments/101', data=json.dumps({'dep_name': 'Finance'}),\
                     content_type='application/json')
    assert res.status_code == 404

def test_d13(client):
    """check update Department by name if dept exists"""
    res = client.put('/api/departments/IT', data=json.dumps({'dep_name': 'Finance'}),\
                     content_type='application/json')
    assert res.status_code == 204

def test_d14(client):
    """check Update Department by name if dept not exists"""
    res = client.put('/api/departments/SEC', data=json.dumps({'dep_name': 'Finance'}),\
                     content_type='application/json')
    assert res.status_code == 404


def test_d15(client):
    """check  post Department if dept not exists"""
    res = client.post('/api/departments/add', data=json.dumps({'dep_name': 'Finance'}),\
                     content_type='application/json')
    # assert res.status_code == 201
    assert res.status_code == 201

def test_d16(client):
    """check  post Department if dept exists"""
    res = client.post('/api/departments/add', data=json.dumps({'dep_name': 'IT'}),\
                     content_type='application/json')
    # assert res.status_code == 201
    assert res.status_code == 409

