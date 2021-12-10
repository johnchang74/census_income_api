# Census object
class Census:
    # Initial object
    def __init__(self, header, record):
        # parse record by comma delimiter
        head = header.split(',', -1)
        rec = record.split(',', -1)
        self.headAge = str(head[0]).strip()
        self.age = str(rec[0]).strip()
        self.headWorkClass = str(head[1]).strip()
        self.workClass = str(rec[1]).strip()
        self.headFnlWgt = str(head[2]).strip()
        self.fnlWgt = str(rec[2]).strip()
        self.headEducation = str(head[3]).strip()
        self.education = str(rec[3]).strip()
        self.headMaritalStatus = str(head[4]).strip()
        self.maritalStatus = str(rec[4]).strip()
        self.headOccupation = str(head[5]).strip()
        self.occupation = str(rec[5]).strip()
        self.headRelationship = str(head[6]).strip()
        self.relationship = str(rec[6]).strip()
        self.headRace = str(head[7]).strip()
        self.race = str(rec[7]).strip()
        self.headSex = str(head[8]).strip()
        self.sex = str(rec[8]).strip()
        self.headHoursPerWeek = str(head[9]).strip()
        self.hoursPerWeek = str(rec[9]).strip()
        self.headNativeCountry = str(head[10]).strip()
        self.nativeCountry = str(rec[10]).strip()
        self.headCapital = str(head[11]).strip()
        self.capital = str(rec[11]).strip()
        self.headIncome = str(head[12]).strip()
        self.income = str(rec[12]).strip()

    # return age
    def get_age(self):
        return self.age

    # return education
    def get_education(self):
        return self.education

    # return country
    def get_country(self):
        return self.nativeCountry

    # return census record in JSON format
    def get_json_block(self):
        # initialize JSON record block
        data_block = {
            self.headAge: self.age,
            self.headWorkClass: self.workClass,
            self.headFnlWgt: self.fnlWgt,
            self.headEducation: self.education,
            self.headMaritalStatus: self.maritalStatus,
            self.headOccupation: self.occupation,
            self.headRelationship: self.relationship,
            self.headRace: self.race,
            self.headSex: self.sex,
            self.headHoursPerWeek: self.hoursPerWeek,
            self.headNativeCountry: self.nativeCountry,
            self.headCapital: self.capital,
            self.headIncome: self.income
        }
        return data_block

    def to_string(self):
        return self.age + '|' + self.education + '|' + self.nativeCountry

