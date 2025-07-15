import os
from datetime import datetime

class LoggerObj:
    def __init__(self, log_file: str):
        self.log_file = log_file

    def __str__(self):
        return f'{self.log_file}'
    
    def log(self, msg: str):
        file_path = f'{self.log_file}/log.txt'
        
        try:
            now = datetime.now()
            
            if (os.path.exists(self.log_file)): 
                with open(file_path, 'a', encoding='utf-8') as file:
                    file.write(f'{now} | {msg} \n')
            else:
                os.mkdir(self.log_file)
                self.log(msg)
                
        except Exception as ex:
            print(ex)