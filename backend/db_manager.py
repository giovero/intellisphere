from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()

class Alunni(Base):
    __tablename__ = 'alunni'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    additional_req = Column(String)
    image_url = Column(String)


class FileGenerati(Base):
    __tablename__ = 'generated_files'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    id_studente = Column(Integer)
    prompt = Column(String)


class DbManager(object):
    
    def __init__(self):
        self.session = None
        backend_dir = os.getcwd()
        full_db_path = os.path.join(backend_dir, 'database.db')
        engine = create_engine('sqlite:///' + full_db_path)
        self.s_maker = sessionmaker(bind=engine)
        Base.metadata.create_all(engine)

    def openSession(self):
        self.session = self.s_maker()

    def closeSession(self):
        # Close the session
        self.session.close()
    
    def addAlunno(self, vals):
        self.openSession()
        try:
            for kkk, vvv in vals.copy().items():
                if not hasattr(Alunni, kkk):
                    del vals[kkk]
            record1 = Alunni(**vals)
            self.session.add(record1)
            self.session.commit()
        except Exception as ex:
            raise Exception("Cannot create Alunno due to error %r" % (ex))
        finally:
            self.closeSession()
        return True
        
    def getAunnoById(self, id_alunno):
        self.openSession()
        ret = self._getAlunnoId(id_alunno)
        self.closeSession()
        return ret
        
    def _getAlunnoId(self, id_alunno):
        return  self.session.query(Alunni).filter(Alunni.id == id_alunno).all()

    def getAlunni(self):
        self.openSession()
        ret = self.session.query(Alunni).all()
        self.closeSession()
        return ret

    def addFileGenerati(self, vals):
        self.openSession()
        try:
            record1 = FileGenerati(**vals)
            self.session.add(record1)
            self.session.commit()
        except Exception as ex:
            raise Exception("Cannot create File Object due to error %r" % (ex))
        finally:
            self.closeSession()
        return True
        
    def getFileGeneratiById(self, id_alunno):
        self.openSession()
        ret = self.session.query(FileGenerati).filter(FileGenerati.id == id_alunno).all()
        self.closeSession()
        return ret
        
    def getFileGenerati(self):
        self.openSession()
        ret = self.session.query(FileGenerati).all()
        self.closeSession()
        return ret

    def updateAlunno(self, alunno_id, vals):
        self.openSession()
        alunni = self._getAlunnoId(alunno_id)
        for alunno in alunni:
            for key, val in vals.items():
                if key == 'name':
                    alunno.name = val
                elif key == 'age':
                    alunno.age = val
                elif key == 'additional_req':
                    alunno.additional_req = val
        self.session.commit()
        self.closeSession()

# # Example 1: Query all rows
# all_rows = session.query(MyTable).all()
#
# # Example 2: Query with conditions
# filtered_rows = session.query(MyTable).filter(MyTable.age >= 18).all()
#
# # Example 3: Query specific columns
# column_values = session.query(MyTable.name, MyTable.age).all()
#
# # Example 4: Filter and order
# filtered_and_ordered = session.query(MyTable).filter(MyTable.age >= 18).order_by(MyTable.name).all()






