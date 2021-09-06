from portal import create_app
from portal import db
from portal.student.models import Student


app = create_app('dev')

@app.shell_context_processor
def context_processor():
    return dict(db = db, Student = Student)

if __name__ == "__main__":
    app.run()