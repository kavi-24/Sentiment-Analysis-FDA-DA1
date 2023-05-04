from rpy2.rinterface_lib.embedded import RRuntimeError
from rpy2.robjects.packages import importr
utils = importr('utils')

def importr_tryhard(packname):
    try:
        rpack = importr(packname)
    except RRuntimeError:
        utils.install_packages(
            packname,
            # contriburl = contriburl
        )
        rpack = importr(packname)
    return rpack
