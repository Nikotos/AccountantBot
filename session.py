import pickle


"""
    All sessions are managed by session manager object
    
    TODO - add errorrs processing
    
    TODO - add hashing to passwords
"""
class SessionManager:
    def __init__(self):
        self.sessionMap = {}
        self.usersDatabase = {}
        with open('auth.pkl', 'rb') as f:
            self.usersDatabase = pickle.load(f)


    def __auth__(self, username, password):
        if ((username in self.usersDatabase) and (self.usersDatabase[username] == password)):
            return True
        else:
            return False

    """
        Here we checking user logging in details
        and creating new session in case of success
        
        TODO - add hashing (in case of safety)
    """
    def addSession(self, sessionID, username, password):
        if sessionID not in self.sessionMap:
            authResult = self.__auth__(username, password)
            print(authResult)
            if authResult:
                self.sessionMap[sessionID] = Session(sessionID, username)
                return True
            else:
                return False
        else:
            return True


    """
        In ideal approach we should set some Time To Live for each session
    """
    def removeSession(self, sesionID):
        if sessionID in self.sessionMap:
            del self.sessionMap[sessionID]


    def isAuthorized(self, sesionID):
        if sesionID in self.sessionMap:
            return True
        else:
            return False

"""
    User oriented object
    For each user we create new session
"""
class Session:
    def __init__(self, sesionID, username):
        self.sesionID = sesionID
        self.username = username

