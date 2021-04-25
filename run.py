from app import myapp_obj

from app import db
db.create_all()

myapp_obj.run()
