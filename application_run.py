import os
#os.environ['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://user:pass@ipmachine/database"

import logging
from app import app, db

if __name__ == '__main__':
    logging.basicConfig() 
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    app.run(host='127.0.0.1', port=8080, debug=True)