# -*- coding: utf-8 -*-

import os
from config_default import configs as default_configs
from config_prod import configs as prod_configs

all_config = default_configs

if os.getenv('ENV') == 'prod':
    all_config = prod_configs
