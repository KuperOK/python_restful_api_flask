from app import db
# from datetime import datetime
# import re


class Department(db.Model):
    dep_id = db.Column(db.Integer, primary_key=True)
    dep_name = db.Column(db.String(140), unique=True, nullable=False)
    employee = db.relationship('Employee', backref='department', lazy=True)


    def __init__(self, *args, **kwargs):
        super(Department, self).__init__(*args, **kwargs)
    #    self.generate_slug()

#    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))


    def __repr__(self):
        return '<Dep id: {}, dep_name: {}>'.format(self.dep_id, self.dep_name)


class Employee(db.Model):
    emp_id = db.Column(db.Integer, primary_key=True)
    emp_name = db.Column(db.String(100), nullable=False)
    date_of_birth= db.Column(db.DateTime, nullable=False)
    salary = db.Column(db.Float(100), nullable=False)
    dep_id = db.Column(db.Integer, db.ForeignKey('department.dep_id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super(Employee, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<Emp id: {}, emp_name: {}>'.format(self.emp_id, self.emp_name, self.dep_id)
