from portal import create_app
from portal import db
from portal.models import Student, Lecturer, Admin, SuperAdmin



app = create_app('dev')


@app.shell_context_processor
def context_processor():
    return dict(db = db, Student = Student, Lecturer = Lecturer, Admin = Admin, SuperAdmin = SuperAdmin)


if __name__ == "__main__":
    app.run()