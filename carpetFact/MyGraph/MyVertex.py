import json
import os.path


class CarpetClass :
    _main_carpet_file_path = '../Files/carpet.json'
    color = str

    def __init__(self):
        self.LinkedPeople = dict()
    def setData1(self , color):
        self.color = color


    @staticmethod
    def getUsers(path): # static function
        f = open(path)
        data = json.load(f)
        users = list()

        for item in data:
            u = CarpetClass()
            u.setData(item['id'], item['name'] , item['dateOfBirth'] , item['universityLocation'] , item['field'] , item['workplace'] , item['email'] , item['specialties'] , item['connectionId'])
            users.append(u)
        return users

    def getLocalUsers(path): # static function
        f = open(path)
        data = json.load(f)
        users = list()

        for item in data:
            u = CarpetClass()
            u.setData1(item['username'],item['password'] ,item['name'] , item['dateOfBirth'] , item['universityLocation'] , item['field'] , item['workplace'] , item['email'] , item['specialties'] , item['connectionId'])
            users.append(u)
        return users


    @staticmethod
    def toUser(item):
        u = CarpetClass()
        u.setData(item['id'],item['name'], item['dateOfBirth'], item['universityLocation'], item['field'], item['workplace'],item['email'], item['specialties'], item['connectionId'])
        return u
    def saveFile(self , path):

        if os.stat(path).st_size == 0: #to avoid reading empty file
            tmp = open(path , 'w')
            tmp.write('[]')
            tmp.close()

        f = open(path)
        data = json.load(f)
        f.close()
        f = open(path , 'w')
        data.append(self.__dict__)
        #print(json.dumps(self.__dict__))
        f.write(json.dumps(data))
        print(self.__dict__)
        f.close()
    @staticmethod
    def findInFile(username , password , path):
        f = open(path)
        data = json.load(f)
        f.close()
        for item in data:
            if item['username'] == username and item['password'] == password:
                u = CarpetClass()
                u.setData1(item['username'], item['password'],item['name'], item['dateOfBirth'], item['universityLocation'], item['field'],item['workplace'] , item['email'], item['specialties'] , item['connectionId'])
                return u
        return None




    @staticmethod
    def searchByEmail(email , password , path):
        f = open(path)
        data = json.load(f)
        f.close()
        for item in data:
            if item['email'] == email and password == '****':
                u = CarpetClass()
                u.setData(item['id'], item['name'], item['dateOfBirth'], item['universityLocation'], item['field'],
                          item['workplace'], item['email'], item['specialties'], item['connectionId'])
                return u
        return None



    @staticmethod
    def searchByName(name , path):
        f = open(path)
        data = json.load(f)
        f.close()
        for item in data:
            if item['name'] == name:
                return CarpetClass.toUser(item)
        return None

    @staticmethod
    def isInFile(name , path):
        f = open(path)
        data = json.load(f)
        f.close()
        for item in data:
            if item['name'] == name:
                return True
        return False

    def addLink(self , u , e):
        self.LinkedPeople[u] = e

    def toString(self):
        print('Name : ' + self.name)
        print('Birthday : ' + self.dateOfBirth)
        print('University Location : ' + self.universityLocation)
        print('Field : ' + self.field)
        print('Work place : ' + self.workplace)
        print('Email : ' + self.email)
        print('Specialties : ' , end= '')
        print(self.specialties)