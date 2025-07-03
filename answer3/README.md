*IMPORTANT:* 

This answer contains database logic, therefore, it's neccessary to create the database with its respective table. To do so, you should run in your Postgres client the queries placed in `answer3/database/DATABASE.sql`

*RUN:*

Placed in "answer3" folder, execute the following command:
```
python main.py
```

*ARGS:*

In order to run this answer is neccesary to connect to DB. The connection info must be setted by commandline arguments.
To set them, run the project with the followig command: 
```
python main.py --username [USER] --password [PASSWORD] --database [NAME DATABASE] --host (Optional - default = localhost) [HOST] --port (Optional - default = 5432) [PORT]
```
example: 
```
python main.py --username postgres --password postgres --database prueba --host localhost
```