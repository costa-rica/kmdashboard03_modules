import os
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv()
print(f"- .env: {find_dotenv()}")


with open(os.path.join(os.environ.get('CONFIG_PATH'), os.environ.get('CONFIG_FILE_NAME'))) as config_json_file:
    config_json_dict = json.load(config_json_file)

print(f"PROJE0 Resoureces: {os.environ.get('PROJECT_RESOURCES')}")


class ConfigBasic():

    def __init__(self):
        self.SECRET_KEY = config_json_dict.get('SECRET_KEY')
        self.WEB_ROOT = os.environ.get('WEB_ROOT')

        # Database
        self.PROJECT_RESOURCES = os.environ.get('PROJECT_RESOURCES')
        # self.DB_ROOT = os.environ.get('DB_ROOT')
        # DB_ROOT = "/Users/nick/Documents/_databases/kmDashDemo/"
        self.DB_NAME = "kmDashDemo.db"
        self.DB_ROOT = os.path.join(self.PROJECT_RESOURCES,"database")
        self.SQL_URI = f"sqlite:///{os.path.join(self.DB_ROOT,self.DB_NAME)}"

        #Email stuff
        self.MAIL_SERVER = config_json_dict.get('MAIL_SERVER_MSOFFICE')
        self.MAIL_PORT = config_json_dict.get('MAIL_PORT')
        self.MAIL_USE_TLS = True
        self.MAIL_USERNAME = config_json_dict.get('EMAIL')
        self.MAIL_PASSWORD = config_json_dict.get('EMAIL_PASSWORD')
        self.GUEST_EMAIL = config_json_dict.get('GUEST_EMAIL')
        self.GUEST_EMAIL_PASSWORD = config_json_dict.get('GUEST_EMAIL_PASSWORD')

        #web Guest
        self.GUEST_EMAIL = config_json_dict.get('GUEST_EMAIL')
        self.GUEST_PASSWORD = config_json_dict.get('GUEST_PASSWORD')

        #API
        self.API_URL = os.environ.get("API_URL")

        # back up database and file via scheduler
        self.BACKER_UPPER_ROOT = os.environ.get("BACKER_UPPER_ROOT")
        self.BACKUP_ROOT = os.environ.get("BACKUP_ROOT")

        self.TR_VERIFICATION_PASSWORD = os.environ.get("TR_VERIFICATION_PASSWORD")

        print(f"DB_ROOT : {self.DB_ROOT}")
        print(f"DB_ROOT / files : {os.path.join(self.DB_ROOT, 'files')}")

        self.DIR_DB_FILES = os.path.join(self.DB_ROOT, 'files')#UPLOADED_FILES_FOLDER
        self.DIR_DB_FILES_UTILITY = os.path.join(self.DB_ROOT, 'files_utility')#UTILITY_FILES_FOLDER
        self.DIR_DB_QUERIES = os.path.join(self.DB_ROOT, 'queries')#QUERIES_FOLDER
        self.DIR_DB_FILES_DATABASE = os.path.join(self.DB_ROOT, 'files_database')#FILES_DATABASE
        self.DIR_DB_FILES_TEMPORARY = os.path.join(self.DB_ROOT, 'files_temp')#UPLOADED_TEMP_DATA


class ConfigLocal(ConfigBasic):
    
    def __init__(self):
        super().__init__()

    DEBUG = True
    # TEMPLATES_AUTO_RELOAD = False
    ## removed 2023-03-06: not clear why I had it but it certainly no good for working on the front end.
    SCHED_CONFIG_STRING = "ConfigLocal"


class ConfigDev(ConfigBasic):

    def __init__(self):
        super().__init__()

    DEBUG = True
    SQL_URI = config_json_dict.get('SQL_URI_DEVELOPMENT')
    TEMPLATES_AUTO_RELOAD = True
    SCHED_CONFIG_STRING = "ConfigDev"


class ConfigProd(ConfigBasic):
        
    def __init__(self):
        super().__init__()

    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = True
    SCHED_CONFIG_STRING = "ConfigProd"
