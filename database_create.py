import sqlite3

class Database_create:
  def __init__(self):
    pass

  def create(self):
      conn=sqlite3.connect('user.db')
      cursor = conn.cursor()

      cursor.execute("""
          CREATE TABLE IF NOT EXISTS USER 
          (phone TEXT PRIMARY KEY NOT NULL,
          fname TEXT, 
          lname TEXT, 
          photo TEXT,
          Birth_day TEXT,
          password TEXT NOT NULL,
          genderId INTEGER,
          insuranceId INTEGER, 
          Foreign Key (genderId) REFERENCES  GENDER(genderId),
          Foreign Key (insuranceId) REFERENCES  INSURANCE(insuranceId)                
          )"""
          )
      # conn.commit()
      cursor.execute("""
          CREATE TABLE IF NOT EXISTS is_family_of 
          (fuserPhone TEXT,
          suserPhone TEXT,
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          Foreign Key (fuserPhone) REFERENCES  USER(phone),
          Foreign Key (suserPhone) REFERENCES  USER(phone)                
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
          Foreign Key (dieseaseId) REFERENCES  DISEASE(dieseaseId),
          Foreign Key (insuranceId) REFERENCES  INSURANCE(insuranceId)        
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
          Foreign Key (doc_username) REFERENCES  DOCTOR(username),
          Foreign Key (medical_council_code) REFERENCES  DOCTOR(medical_council_code),
          Foreign Key (insuranceId) REFERENCES INSURANCE(insuranceId)         
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
          Photo TEXT,
          visit_price INTEGER,
          password TEXT NOT NULL,
          specialtyId INTEGER,
          PRIMARY KEY (medical_council_code, username), 
          Foreign Key (specialtyId) REFERENCES  SPECIALTY(specialtyId)
          )"""  
      )
      # conn.commit()
      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS saved 
          (phone INTEGER NOT NULL,
          medical_council_code INTERGER NOT NULL,
          doc_username TEXT,
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          Foreign Key (doc_username) REFERENCES  DOCTOR(username),
          Foreign Key (medical_council_code) REFERENCES  DOCTOR(medical_council_code),
          Foreign Key (phone) REFERENCES  USER(phone)         
          )"""  
      )
      # conn.commit()
      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS APPOINTMENT 
          (appointmentId INTEGER PRIMARY KEY NOT NULL,
          phone INTERGER,
          paymentId INTEGER,
          medical_council_code INTEGER,
          doc_username TEXT,
          dhhId INTEGER,
          dohId INTEGER,
          Foreign Key (dohId) REFERENCES  DOH(dohId),
          Foreign Key (dhhId) REFERENCES  DHH(dhhId),
          Foreign Key (doc_username) REFERENCES  DOCTOR(username),
          Foreign Key (medical_council_code) REFERENCES  DOCTOR(medical_council_code),
          Foreign Key (phone) REFERENCES  USER(phone), 
          Foreign Key (paymentId) REFERENCES  PAYMENT(paymentId)    
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
          Foreign Key (appointmentId) REFERENCES  APPOINTMENT(appointmentId),
          Foreign Key (doc_username) REFERENCES  DOCTOR(username),
          Foreign Key (medical_council_code) REFERENCES  DOCTOR(medical_council_code),
          Foreign Key (docofficeId) REFERENCES  DOCTOR_OFFICE(docofficeId) 
          )"""  
      )
      # conn.commit()
      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS DOCTOR_OFFICE
          (docofficeId INTEGER PRIMARY KEY NOT NULL,
          addressId INTEGER,
          phone INTEGER,
          Foreign Key (addressId) REFERENCES  ADDRESS(addressId)
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
          Foreign Key (healthcareId) REFERENCES  HEALTHCARE(healthcareId),
          Foreign Key (docofficeId) REFERENCES  DOCTOR_OFFICE(docofficeId) 
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
          Foreign Key (dhhId) REFERENCES  DHH(dhhId),
          Foreign Key (dohId) REFERENCES  DOH(dohId)  
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
          Foreign Key (appointmentId) REFERENCES  APPOINTMENT(appointmentId),
          Foreign Key (doc_username) REFERENCES  DOCTOR(username),
          Foreign Key (medical_council_code) REFERENCES  DOCTOR(medical_council_code),
          Foreign Key (healthcareId) REFERENCES  HEALTHCARE(healthcareId) 
          )"""  
      )
      # conn.commit()
      cursor.execute(
        """
          CREATE TABLE IF NOT EXISTS HEALTHCARE 
          (healthcareId INTEGER PRIMARY KEY AUTOINCREMENT,
          phone TEXT,
          addressId INTEGER,
          Foreign Key (addressId) REFERENCES ADDRESS(addressId)

          )"""  
      )
      conn.commit()
      # cursor.close()
      # conn.close()