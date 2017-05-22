from ConfigParser import SafeConfigParser
from const import LOCAL_CONF

def local_conf_parser():
    return get_conf_parser(LOCAL_CONF)

def get_conf_parser(conf_file_path):
    parser = SafeConfigParser()
    parser.read(conf_file_path)
    return parser

def get_wechat_conf():
    local_conf = local_conf_parser()
    wechat_conf = dict(local_conf.items('wechat'))
    return wechat_conf

wechat_conf = get_wechat_conf()
