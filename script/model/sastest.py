# test connection to SAS on-demand server

import saspy

# this will prompt the user for credentials - they are not stored in the repo!
# to avoid this, create a .authinfo file that contains
sas = saspy.SASsession(cfgfile='/workspace/CDISC-SDMX/conf/sascfg_personal.py')

result = sas.submit(
    """
    proc datasets library=work; quit;
    """,
    results = "TEXT"
)

