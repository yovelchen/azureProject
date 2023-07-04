# azure_project
[Module 07 - Azure Project.pdf](https://github.com/yovelchen/azure_project/files/11929569/Module.07.-.Azure.Project.pdf)

# steps vm-gifts-yovel-db

- install postgres:
1.sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt   $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
3. wget --quiet -O -   https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
4. sudo apt-get update
5. sudo apt-get -y install postgresql

- create user: 
1. sudo -i -u postgres
2. ALTER USER postgres PASSWORD 'PASSWORD';
3. \q

- create db and table: 
1. CREATE DATABASE flask_db;
2. \l
3. \c flask_db
4. CREATE TABLE table_gifts_yovel ( name VARCHAR, age_value NUMERIC, time VARCHAR );
5. \d
6. \d table_gifts_yovel


- enable remote connection: 
1. ss -nlt >> ADDRESS:PORT
2. sudo find / -name "postgresql.conf"
3. sudo vi /etc/postgresql/15/main/postgresql.conf >> change #listen_addresses = 'localhost' to listen_addresses = '*' 
3. sudo systemctl restart postgresql
4. ss -nlt >> * 

- allow client connections to all databases:
1. sudo vi /etc/postgresql/14/main/pg_hba.conf >> add line at the end of the file:
"#Allow client connections to all data bases and users 
host    all          all            0.0.0.0/0  md5"

# steps vm-gifts-yovel-web
1. sudo apt-get install postgresql-client
2. psql -h 10.0.2.4 -U postgres
3. mkdir flaskApp 
4. cd flaskApp 
5. create vim azureApp.py >> file azureApp.py :  https://github.com/yovelchen/azure_project/blob/main/azureApp.py
6. pip install psycopg2-binary
7. python3 azureApp.py

# steps postman
1. POST
2. http://108.142.197.95:8080/data
3. Body, raw
4. change text to JSON
5. {
"name": "lior",
"age_value": 100,
"time": "10/1/38"
}
6. Send

# check if data is saved in vm-gifts-yovel-db
1. \c flask_db
2. SELECT * FROM table_gifts_yovel;
   
# credits:
1. https://www.postgresql.org/download/linux/ubuntu/
2. https://devopscube.com/install-postgresql-on-ubuntu/
3. chatGPT
