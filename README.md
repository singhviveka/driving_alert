# driving_alert
main.py contains all api.
Code is written in Python using FastAPI and mysql. 
execute create table alert(id int not null AUTO_INCREMENT,message varchar(255),PRIMARY KEY (id)); in mysql to create alert table.
For starting the server please use:
uvicorn main:app --reload
Then open :
 http://127.0.0.1:8000/docs on browser and get all api. make sure the app is connected with mysql.
