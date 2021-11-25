#
# saspy configuration file. This file should be explicitly loaded when a new session is started"
#
# sas = saspy.SASsession(cfgfile='/some/path/to/your/config/sascfg_personal.py')
#
SAS_config_names=['oda']

oda = {'java' : '/home/gitpod/.sdkman/candidates/java/11.0.13.fx-zulu/bin/java',
    #European Home Region
    'iomhost' : ['odaws01-euw1.oda.sas.com','odaws02-euw1.oda.sas.com'],
    'iomport' : 8591,
    'authkey' : 'oda',
    'encoding' : 'utf-8'
}

