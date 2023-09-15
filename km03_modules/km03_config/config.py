import os
import json
from dotenv import load_dotenv

load_dotenv()


with open(os.path.join(os.environ.get('CONFIG_PATH'), os.environ.get('CONFIG_FILE_NAME'))) as env_file:
    env_dict = json.load(env_file)



class ConfigBasic():

    def __init__(self):
        self.SECRET_KEY = env_dict.get('SECRET_KEY')
        self.DB_ROOT = os.environ.get('DB_ROOT')
        self.SQL_URI = f"sqlite:///{self.DB_ROOT}{os.environ.get('DB_NAME')}"

        #Email stuff
        self.MAIL_SERVER = env_dict.get('MAIL_SERVER_MSOFFICE')
        self.MAIL_PORT = env_dict.get('MAIL_PORT')
        self.MAIL_USE_TLS = True
        self.MAIL_USERNAME = env_dict.get('EMAIL')
        self.MAIL_PASSWORD = env_dict.get('EMAIL_PASSWORD')
        self.GUEST_EMAIL = env_dict.get('GUEST_EMAIL')
        self.GUEST_EMAIL_PASSWORD = env_dict.get('GUEST_EMAIL_PASSWORD')


        #web Guest
        self.GUEST_EMAIL = env_dict.get('GUEST_EMAIL')
        self.GUEST_PASSWORD = env_dict.get('GUEST_PASSWORD')

        #API
        self.API_URL = os.environ.get("API_URL")

        # back up database and file via scheduler
        self.BACKER_UPPER_ROOT = os.environ.get("BACKER_UPPER_ROOT")
        self.BACKUP_ROOT = os.environ.get("BACKUP_ROOT")

        self.TR_VERIFICATION_PASSWORD = os.environ.get("TR_VERIFICATION_PASSWORD")

        self.DIR_DB_FILES = os.path.join(os.environ.get('DB_ROOT'), 'files')#UPLOADED_FILES_FOLDER
        self.DIR_DB_FILES_UTILITY = os.path.join(os.environ.get('DB_ROOT'), 'files_utility')#UTILITY_FILES_FOLDER
        self.DIR_DB_QUERIES = os.path.join(os.environ.get('DB_ROOT'), 'queries')#QUERIES_FOLDER
        self.DIR_DB_FILES_DATABASE = os.path.join(os.environ.get('DB_ROOT'), 'files_database')#FILES_DATABASE
        self.DIR_DB_FILES_TEMPORARY = os.path.join(os.environ.get('DB_ROOT'), 'files_temp')#UPLOADED_TEMP_DATA


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
    SQL_URI = env_dict.get('SQL_URI_DEVELOPMENT')
    TEMPLATES_AUTO_RELOAD = True
    SCHED_CONFIG_STRING = "ConfigDev"


class ConfigProd(ConfigBasic):
        
    def __init__(self):
        super().__init__()

    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = True
    SCHED_CONFIG_STRING = "ConfigProd"
