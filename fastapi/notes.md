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