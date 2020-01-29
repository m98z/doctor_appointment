import sqlite3

class Database_create:
  def __init__(self):
    pass

  def create(self):
      conn=sqlite3.connect('tabib.db')
      cursor = conn.cursor()

      cursor.execute("""
          CREATE TABLE IF NOT EXISTS COMMENT 
          (commentId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
          comment_txt TEXT, 
          appointmentId INTEGER, 
          Foreign Key (appointmentId) REFERENCES  APPOINTMENT(appointmentId) ON DELETE CASCADE ON UPDATE CASCADE               
          )"""
          )
          
      cursor.execute("""
          CREATE TABLE IF NOT EXISTS USER 
          (phone TEXT PRIMARY KEY NOT NULL,
          fname TEXT, 
          lname TEXT, 
          photo BLOB,
          Birth_day TEXT,
          password TEXT NOT NULL,
          genderId INTEGER,
          insuranceId INTEGER, 
          Foreign Key (genderId) REFERENCES  GENDER(genderId) ON DELETE CASCADE ON UPDATE CASCADE,
          Foreign Key (insuranceId) REFERENCES  INSURANCE(insuranceId) ON DELETE CASCADE ON UPDATE CASCADE               
          )"""
          )
      # conn.commit()
      cursor.execute("""
          CREATE TABLE IF NOT EXISTS is_family_of 
          (fuserPhone TEXT,
          suserPhone TEXT,
          PRIMARY KEY (fuserPhone,suserPhone),
          Foreign Key (fuserPhone) REFERENCES  USER(phone) ON DELETE CASCADE ON UPDATE CASCADE,
          Foreign Key (suserPhone) REFERENCES  USER(phone) ON DELETE CASCADE ON UPDATE CASCADE               
          )"""
      )
      
      # conn.commit()
      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS PAYMENT 
          (paymentId INTEGER PRIMARY KEY NOT NULL,
          code TEXT            
          )"""  
      )

      # conn.commit()
      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS GENDER 
          (genderId INTEGER PRIMARY KEY NOT NULL,
          title TEXT         
          )"""  
      )
      # conn.commit()
      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS INSURANCE 
          (insuranceId INTEGER PRIMARY KEY NOT NULL,
          name TEXT             
          )"""  
      )
      # conn.commit()
      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS support 
          (insuranceId INTEGER NOT NULL,
          dieseaseId INTEGER NOT NULL,
          discount_percent INTEGER,
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          Foreign Key (dieseaseId) REFERENCES  DISEASE(dieseaseId) ON DELETE CASCADE ON UPDATE CASCADE,
          Foreign Key (insuranceId) REFERENCES  INSURANCE(insuranceId) ON DELETE CASCADE ON UPDATE CASCADE       
          )"""  
      )
      # conn.commit()
      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS DISEASE 
          (dieseaseId INTEGER PRIMARY KEY NOT NULL,
          title TEXT       
          )"""  
      )
      # conn.commit()
      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS in_contract_with 
          (insuranceId INTEGER,
          medical_council_code INTERGER,
          doc_username TEXT,
          id INTEGER PRIMARY KEY AUTOINCREMENT, 
          Foreign Key (doc_username,medical_council_code) REFERENCES  DOCTOR(username,medical_council_code) ON DELETE CASCADE ON UPDATE CASCADE,
          Foreign Key (insuranceId) REFERENCES INSURANCE(insuranceId) ON DELETE CASCADE ON UPDATE CASCADE        
          )"""  
      )
      # conn.commit()
      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS DOCTOR 
          (medical_council_code INTEGER NOT NULL,
          username TEXT NOT NULL,
          fname TEXT, 
          lname TEXT, 
          Photo BLOB,
          visit_price INTEGER,
          password TEXT NOT NULL,
          specialtyId INTEGER,
          PRIMARY KEY (medical_council_code, username), 
          Foreign Key (specialtyId) REFERENCES  SPECIALTY(specialtyId) ON DELETE CASCADE ON UPDATE CASCADE
          )"""  
      )
      # conn.commit()
      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS SPECIALTY 
          (
          name TEXT,
          specialtyId INTEGER PRIMARY KEY         
          )"""  
      )
      
      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS saved 
          (phone INTEGER NOT NULL,
          medical_council_code INTERGER NOT NULL,
          doc_username TEXT,
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          Foreign Key (doc_username,medical_council_code) REFERENCES  DOCTOR(username,medical_council_code) ON DELETE CASCADE ON UPDATE CASCADE,
          Foreign Key (phone) REFERENCES  USER(phone) ON DELETE CASCADE ON UPDATE CASCADE        
          )"""  
      )
      # conn.commit()
      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS APPOINTMENT 
          (appointmentId INTEGER PRIMARY KEY AUTOINCREMENT,
          phone TEXT,
          paymentId INTEGER,
          medical_council_code INTEGER,
          doc_username TEXT,
          dhhId INTEGER,
          dohId INTEGER,
          score INTEGER,
          Foreign Key (dohId) REFERENCES  DOH(dohId) ON DELETE CASCADE ON UPDATE CASCADE,
          Foreign Key (dhhId) REFERENCES  DHH(dhhId) ON DELETE CASCADE ON UPDATE CASCADE,
          Foreign Key (doc_username,medical_council_code) REFERENCES  DOCTOR(username,medical_council_code) ON DELETE CASCADE ON UPDATE CASCADE,
          Foreign Key (phone) REFERENCES  USER(phone) ON DELETE CASCADE ON UPDATE CASCADE, 
          Foreign Key (paymentId) REFERENCES  PAYMENT(paymentId) ON DELETE CASCADE ON UPDATE CASCADE    
          )"""  
      )
      # conn.commit()
      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS DOH 
          (docofficeId INTEGER,
          medical_council_code INTEGER,
          doc_username TEXT,
          appointmentId INTEGER,
          dohId INTEGER PRIMARY KEY AUTOINCREMENT,
          Foreign Key (appointmentId) REFERENCES  APPOINTMENT(appointmentId) ON DELETE CASCADE ON UPDATE CASCADE,
          Foreign Key (doc_username,medical_council_code) REFERENCES  DOCTOR(username,medical_council_code) ON DELETE CASCADE ON UPDATE CASCADE,
          Foreign Key (docofficeId) REFERENCES  DOCTOR_OFFICE(docofficeId) ON DELETE CASCADE ON UPDATE CASCADE
          )"""  
      )
      # conn.commit()
      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS DOCTOR_OFFICE
          (docofficeId INTEGER PRIMARY KEY NOT NULL,
          addressId INTEGER,
          phone INTEGER,
          Foreign Key (addressId) REFERENCES  ADDRESS(addressId) ON DELETE CASCADE ON UPDATE CASCADE
          )"""  
      )
      # conn.commit()
      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS ADDRESS 
          (addressId INTEGER PRIMARY KEY NOT NULL,
          docofficeId INTEGER,
          healthcareId INTEGER,
          street TEXT,
          alley TEXT,
          plaque TEXT, 
          Foreign Key (healthcareId) REFERENCES  HEALTHCARE(healthcareId) ON DELETE CASCADE ON UPDATE CASCADE,
          Foreign Key (docofficeId) REFERENCES  DOCTOR_OFFICE(docofficeId) ON DELETE CASCADE ON UPDATE CASCADE
          )"""  
      )
      # conn.commit()
      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS WORK_HOUR 
          (workhourId INTEGER PRIMARY KEY NOT NULL,
          starthour TEXT,
          endhour TEXT,
          date TEXT,
          dhhId INTEGER,
          dohId INTEGER,
          Foreign Key (dhhId) REFERENCES  DHH(dhhId) ON DELETE CASCADE ON UPDATE CASCADE,
          Foreign Key (dohId) REFERENCES  DOH(dohId) ON DELETE CASCADE ON UPDATE CASCADE 
          )"""  
      )
      # conn.commit()
      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS DHH 
          (healthcareId INTEGER,
          medical_council_code INTEGER,
          doc_username TEXT,
          appointmentId INTEGER,
          dhhId INTEGER PRIMARY KEY AUTOINCREMENT,
          Foreign Key (appointmentId) REFERENCES  APPOINTMENT(appointmentId) ON DELETE CASCADE ON UPDATE CASCADE,
          Foreign Key (doc_username,medical_council_code) REFERENCES  DOCTOR(username,medical_council_code) ON DELETE CASCADE ON UPDATE CASCADE,
          Foreign Key (healthcareId) REFERENCES  HEALTHCARE(healthcareId) ON DELETE CASCADE ON UPDATE CASCADE
          )"""  
      )
      # conn.commit()
      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS HEALTHCARE 
          (healthcareId INTEGER PRIMARY KEY AUTOINCREMENT,
          phone TEXT,
          addressId INTEGER,
          name TEXT,
          Foreign Key (addressId) REFERENCES ADDRESS(addressId) ON DELETE CASCADE ON UPDATE CASCADE

          )"""  
      )
      conn.commit()
      # cursor.close()
      # conn.close()