# -*- coding: utf-8 -*-

# Copy and rename this file to local_settings.py,
# fill these settings, leave blank if not used, don't delete the lines

# DEVELOPERS: names, secrets and site customizable details should be kept here

import datetime

SECRET_KEY = 'change this!'

DATABASE_NAME = ''
DATABASE_USER = ''
DATABASE_PASSWORD = ''

ALLOWED_HOSTS = ['*']
SITE_URL = ''

ADMINS = (
    ('SITCON Developers', 'sitcon-dev@googlegroups.com'),
)

MANAGERS = ADMINS

SITE_NAME = 'SITCON 行政系統'
SITE_TITLE = 'SITCON'

EMAIL_HOST = 'localhost'
EMAIL_PORT = '25'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

SMS_API_KEY = ''
SMS_API_SECRET = ''

DEFAULT_SMS_SENDER = 'ROBOCONF'
DEFAULT_SMS_COUNTRY_CODE = '886'    # Taiwan

DEFAULT_FROM_EMAIL = '"SITCON 行政系統" <admin@staff.sitcon.org>'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
BROADCAST_EMAIL = 'sitcon@googlegroups.com'

DEFAULT_NOTIFICATION_SENDER = 'SITCON 行政系統:notifications@staff.sitcon.org'
DEFAULT_ACCOUNTS_SENDER =  'SITCON 行政系統:accounts@staff.sitcon.org'
DEFAULT_ISSUE_SENDER = 'SITCON 行政系統:issues@staff.sitcon.org'

SUBMITTER_ACCOUNTS_SENDER = 'SITCON:accounts@staff.sitcon.org'
USER_ISSUE_SENDER = '{0} (SITCON):issues@staff.sitcon.org'

SUBMISSION_START = datetime.datetime(2014, 12, 5, 12, 0, 0)
SUBMISSION_END = datetime.datetime(2015, 1, 31, 6, 38, 0)
SUBMISSION_RULE_DOCID = 'MUY'

STAFF_GROUP_NAME = '工作人員'
STAFF_GROUP_ID = 1
SUBMITTER_GROUP_NAME = '投稿講者'
SUBMITTER_GROUP_ID = 2

URGENT_ISSUE_ID = 2

GROUP_PRIORITY = [3, 1, 6, 7, 5, 8, 4, 9, 2, 14, 19, 20, 15, 13, 18, 12, 11, 10]    # Sort by team lead -> staff -> consultant

RESIDENCE_OPTIONS = (
    '基隆市', '臺北市', '新北市', '桃園市',
    '新竹市', '新竹縣', '苗栗縣', '臺中市',
    '彰化縣', '南投縣', '雲林縣', '嘉義市',
    '嘉義縣', '臺南市', '高雄市', '屏東縣',
    '臺東縣', '花蓮縣', '宜蘭縣', '澎湖縣',
    '金門縣', '連江縣', '國外',
)

SHIRT_SIZE_OPTIONS = (
    'XS', 'S', 'M', 'L', 'XL', '2XL',
)

DIET_OPTIONS = (
    '葷',
    '忌牛肉', '忌豬肉', '忌海鮮',
    '方便素', '蛋奶素', '全素',
)