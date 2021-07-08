import server.server as server
import db.connect as connect


class run:

    def __init__(self):
        self.db = connect.mongo()
        self.server = server.server()



run = run()