
## Project Description
This has been an ongoing project where over the course of 2 years, I have explored 
different machine learning technologies and independently defined a problem I
would like like to address through the utilization of such tools. Given my interest in social 
enterpreneurship and technology, I am motivated to address the challenges faced by minority populations, particularly individuals with disabilities. I focus on enhancing inclusivity and accessibility by harnessing machine learning capabilities in image and language processing. This aligns with my values and represents a meaningful contribution to creating a more inclusive society.



## Building For Impact

The aim of my project is to provide a proof of concept on what it means to build systems that are truly inclusive by develop solutions that naturally accommodate the diverse needs and capabilities of people as they are rather than those that individuals must adapt to. I create a considerate environment to facilitate seamless exchanges between deaf or hard-of-hearing and hearing individuals. While it may be a simple demonstration on the surface, its significance lies in showcasing the potential for technology to prioritize the needs of minority populations, consider diverse perspectives, and design solutions that cater to their specific requirements. Through iterative development, user-centric design principles, and integration of user feedback, I exemplify the iterative process of creating impactful technology that addresses real-world challenges. My POC inspires further exploration and innovation in leveraging technology for social good, emphasizing its transformative power when wielded responsibly and with a focus on creating positive societal impact.

DEMO: [link](https://www.loom.com/share/39db33465cde41598c96ef0ebde2e1b4?sid=ae7f2371-0187-4c31-8958-a2534e655ead) 

## BREAKDOWN 

Below is a breakdown of the project: 


### 1. Image Processing
This contains the model for sign language detection.
Main files include:
1. collect_imgs.py
2. create_dataset.py
3. train_classifier.py
4. inference_classifier.py


### 2. Language Processing 
This contains the model for speech-to-text conversion


### 3. Integrated Model 
This is the integrated model (stil in progress)

## How to run the model 


### 1. Local Setup 

First, install SQLAlchemy in terminal with:

```bash
$ pip install sqlalchemy
```

### 2. Setup on a Python Module 

#### Import SQLALchemy 

```python 
import sqlalchemy
``` 

#### Create Engine 

```python
from sqlalchemy import create_engine 
engine = create_engine('sqlite:///:memory:', echo = True)
```
 
What's happening with the `create_engine()` function?

The engine connects to the database, and this function specifies which database it should connect to.

What is `sqlite:///`? Firstly, this initialises an SQLite Database, which allows us to use SQLite syntax the way we have learnt in prior classes.

`:memory:` simply implies that the SQLite database will not persist beyond individual sessions.
The database will only persist as long as the application instance is running. 

If we do: 

```python
engine = create_engine('sqlite:///try_database.db') 
```

Then this creates a local .db file named `try_database.db` (if it doesn't exist already on your path). We will learn how to use SQLAlchemy to open up the .db file and see if there are any new entries. This `database.db` file will persist locally.

#### Connect to engine 

Now, connect to the engine interface that you created using the default `connect()` function. 

```python
engine.connect() 
```

#### Declare a Base 

The base maintains a catalogue of classes and tables in the base; each application will usually have one. 

```python
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base() 
```

After declaring a base, we will be able to define classes relative to the base. So each class should be created as class `'tablename'(Base)`.

#### Create a Table Mapping

Let's initialise a simple table `Users` by initialising a User class and writing a `__repr__()`method to represent the schema. 

```python
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship, sessionmaker 

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key = True)
	name = Column(String)
	insurance_id = Column(Integer)

	def __repr__(self):
		return "<User(id={0}, name={1}, insurance_id={2})>".format(self.id, self.name, self.insurance_id)
```

Let's create another table to display foreign relationships.

```python
class Insurance(Base):
	__tablename__ = 'insurance'
	id = Column(Integer, ForeignKey('users.insurance_id'), primary_key = True)
	claim_id = Column(Integer)
	users = relationship(User)
```

#### Create the Table Schema

After defining the schema of the table, we will need to actually create it in our database.

We have to call: 

```python
Base.metadata.create_all(engine)
```

This is very important, as without calling `create_all(engine)` and binding it to the engine, the schema will not be initialised. Your table should now be created, and you will be able to add elements to it. 

## Adding Elements to the SQLAlchemy 

Create an instance of your `User` class with: 

```python
user = User(id = 1, name='sterne', insurance_id=1234)
```

And then add it to your DB, by starting a session. 

```python
from sqlalchemy.orm import sessionmaker  

Session = sessionmaker(bind=engine)
session = Session() 
session.add(user)
session.commit()
```

`user` should now be in your database! 

## Querying your Table

Let's check if `user` is in the database.

```python
print(session.query(User).filter_by(name='sterne').first())
```

It should print out: 

```
<User(id=1, name=sterne, insurance_id=1234)>
```
 
Great! 

## Reflecting an Existing Database with SQLAlchemy

Reflecting a table simply means being able to read its metadata, and being able to use SQLAlchemy to read the contents of the table. 

```python
from sqlalchemy import Table, MetaData
metadata = MetaData()
users = Table('users', metadata, autoload=True, autoload_with=engine)
```
Load the table `users` that you initialised before with the above function.

The `autoload_with=engine` parameter ensures that it's connecting to the right engine interface.

### Print table metadata

The `__repr__()` method that you defined in your `User(Base)` class will return a string detailing the details of your database in the format you chose.

```
print(repr(users))
```


## Questions

Use the tutorial above as a guide to the following exercises. After reading the tutorial, check out the `SQLAlchemySample.py` file for a working implementation. 

### Bank loans

From the bank loan exercise at the beginning of the unit:
1. Rewrite all the `CREATE TABLE` commands for the Clients and Loans tables
to now use SQLAlchemy. The SQLAlchemy commands should also create primary key
and foreign key constraints where appropriate.
2. Rewrite an `INSERT` command to now use SQLAlchemy. In particular, you
should hold all the values in a standard Python container (e.g. list,
dictionary, or namedtuple), or a combination of Python containers (e.g. list of
dictionaries).  The insertions should all happen in a single transaction.
3. Rewrite a `SELECT` query and an `UPDATE` command to now use SQLAlchemy.


https://github.com/zzzeek/sqlalchemy/blob/master/lib/sqlalchemy/orm/unitofwork.py
 

