from .modelsMain import login_manager, sess, engine, text, Base, \
    Users, Investigations, Tracking_inv, Saved_queries_inv, \
    Recalls, Tracking_re, Saved_queries_re

import os


############################################################################
## This is one of the first files to execute so make dirs here

if not os.path.exists(os.environ.get('DB_ROOT')):
    os.makedirs(os.environ.get('DB_ROOT'))

# config.UPLOADED_TEMP_DATA directory:
if not os.path.exists(os.path.join(os.environ.get('DB_ROOT'),"files_temp")):
    os.makedirs(os.path.join(os.environ.get('DB_ROOT'),"files_temp"))

# config.UTILITY_FILES_FOLDER directory:
if not os.path.exists(os.path.join(os.environ.get('DB_ROOT'),"files_utility")):
    os.makedirs(os.path.join(os.environ.get('DB_ROOT'),"files_utility"))

# config.QUERIES_FOLDER directory:
if not os.path.exists(os.path.join(os.environ.get('DB_ROOT'),"queries")):
    os.makedirs(os.path.join(os.environ.get('DB_ROOT'),"queries"))
# #######################################################################################
# ## NOTE: Unsure if needed since html files will be stored in templates directory ##
# if not os.path.exists(os.path.join(os.environ.get('DB_ROOT'),"blog_html_files")):
#     os.makedirs(os.path.join(os.environ.get('DB_ROOT'),"blog_html_files"))
######################################################################################



#Build db
if os.path.exists(os.path.join(os.environ.get('DB_ROOT'),os.environ.get('DB_NAME'))):
    print(f"db already exists: {os.path.join(os.environ.get('DB_ROOT'),os.environ.get('DB_NAME'))}")
else:
    Base.metadata.create_all(engine)
    print(f"NEW db created: {os.path.join(os.environ.get('DB_ROOT'),os.environ.get('DB_NAME'))}")