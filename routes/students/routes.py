from flask import Blueprint, request
from models import Student


students = Blueprint('students', __name__, template_folder='students')


@students.route('/students', methods=['GET'])
def get_students_list():
    return Student.query.all()


@students.route('/students', methods=['GET'])
def get_student():
    return Student.query.filter_by(id=request.json['id'])
