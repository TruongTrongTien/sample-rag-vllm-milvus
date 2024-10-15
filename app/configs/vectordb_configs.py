from pymilvus import connections, db

conn = connections.connect(alias='default', host='localhost', port='19530')