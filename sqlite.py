import sqlite3

con = sqlite3.connect('employee_db')

cursor = con.cursor()

sqlite_query ='''CREATE TABLE employee (empCode INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,phone TEXT NOT NULL UNIQUE,email TEXT NOT NULL UNIQUE,designation TEXT NOT NULL,salary REAL NOT NULL,companyName TEXT NOT NULL'''

sqlite_insert_query='''INSERT INTO employee (name ,phone ,email,designation,salary, companyName) VALUES (value1,value2 ,...);'''


sqlite_select_query = '''select * from empployee;'''

sqlite_select_query =  '''SELECT * FROM employee WHERE name = 'requiredValue';'''

sqlite_update_query= '''UPDATE employee SET column_1 = new_value_1, column_2 = new_value_2 WHERE empCode=value;'''

sqlite_delete_query ='''DELETE FROM employee WHERE empCode=value;'''

sqlite_select_query ='''SELECT * from employee WHERE salary>50000 ;'''

sqlite_select_query =''' SELECT count(*) FROM employee;'''

sqlite_select_query='''SELECT  *  FROM employee WHERE salary>=lowerRange AND salary<=higherRange ORDER BY name ASC;'''

sqlite_select_query='''SELECT *, avg(salary)  avg_sal FROM employee GROUP BY employee.salary HAVING employee.salary<avg_leng ;'''

sqlite_select_query='''SELECT *,avg(salary)  avg_sal FROM employee GROUP BY employee.name  // either group by employee.name or employee.empCode HAVING employee.salary<avg_leng ;'''


con.commit()

con.close()