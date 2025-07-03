class Config: 
    username: str
    password: str
    host: str
    port: int
    database: str

    def __init__(self, username: str, password: str, database: str, host: str, port: int):
        if username is None: 
            raise ValueError('Username is required')
        
        if password is None:
            raise ValueError('Password is required')
        
        if database is None:
            raise ValueError('Database name is required')
        
        if host is None:
            raise ValueError('Host is required')
        
        if port is None:
            raise ValueError('Port is required')
        
        #Si pasamos las validaciones es porque los argumentos están correctos
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def __str__(self):
        return f'Config(username={self.username}, password={self.password}, database={self.database}, host={self.host}, port={self.port})'