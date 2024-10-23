import os
from km03_config import ConfigDev, ConfigProd, ConfigLocal

if os.environ.get('FLASK_CONFIG_TYPE')=='workstation':
    config = ConfigLocal()
    print('- km03_models/config: Local')
elif os.environ.get('FLASK_CONFIG_TYPE')=='dev':
    config = ConfigDev()
    print('- km03_models/config: Development')
elif os.environ.get('FLASK_CONFIG_TYPE')=='prod':
    config = ConfigProd()
    print('- km03_models/config: Production')