## Crud 1:25:17
### Create
```python
@app.posts("/posts")
```
### Read
```python
@app.get("/posts/{id}")
@app.get("/posts")
```
### Update
```python
@app.put("/posts/{id}")
```
### Delete
```python
@app.delete("/posts/{id}")
```

### RUN
```bash
uvicorn app.main:app --reload
```

## Databases
### What is a database
- Database is a collection of organized data that can be easaly accessed and managed

### DBMS
- We don't work or interact with databases directly
- Instead we make use of a software referred to as a Database Management System(DBMS)

### Popular DBMS 2:25:30
| Relational | NoSQL      |
|------------|------------|
| MySQL      | MongoDB    |
| PostgreSQL | DynamoDB   |
| Oracle     | Oracle     |
| SQL Server | SQL Server |

### Ralational Database & SQL
- Structured Query Languege(SQL) - Language used to cummunicate with DBMS

### Postgres
- Each instance of postgres can be carved into multiple separete databases
- By Default every Postgres installation comes with one database already created called "postgres"
- This is important because Postgres requires you to specify the name of a database to make a connection. So there needs to always be one database

### Tables
- A table represents a subject or event in an application

### Columns Vs Rows
- A table is made up of columns and rows
- Each Column represents a different attribute
- Each row represents a different entry in the table

### Postgres DataTypes
- Databases have datatypes just like any programming language
| DataType | Postgres                | Python     |
|----------|-------------------------|------------|
| Numeric  | int, decimal, precision | Int, float |
| Text     | Varchar, text           | string     |
| Bool     | boolean                 | boolean    |
| Sequence | array                   | list       |

### Primary Key
- Is a column or group of columns that uniquely identifies each row in a table
- Table can have one and only one primary key

### Unique Constraints
- A UNIQUE constraint can be applied to any column to make sure every record has a unique value for that column

### Null Constraints
- By default, when adding a new entry to a database, any column can be left blank. When a column is left blank, it has a null value
- If you need column to be properly filled in to create a new record, a NOT NULL constraint can be added to yhe column to ensure that the column is never left blank

### Setting up postgres portable
[Setting up postgres portable](https://stackoverflow.com/questions/26441873/starting-postgresql-and-pgadmin-in-windows-without-installation)