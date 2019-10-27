def _rev_dict(choices):
    return {v: k for k, v in choices}


def _dict(choices):
    return {k: v for k, v in choices}


OMS = 'oms'
DMS = 'dms'

TYPES = (
    (OMS, 'ОМС'),
    (DMS, 'ДМС'),
)
TYPES_REV_DICT = _rev_dict(TYPES)
TYPES_DICT = _dict(TYPES)
