#!/home/pi/Projects/smhome/ENV2/bin/python3
# EASY-INSTALL-DEV-SCRIPT: 'Django==1.8.dev20140713153525','django-admin.py'
__requires__ = 'Django==1.8.dev20140713153525'
import sys
from pkg_resources import require
require('Django==1.8.dev20140713153525')
del require
__file__ = '/home/pi/Projects/lib/django-trunk/django/bin/django-admin.py'
if sys.version_info < (3, 0):
    execfile(__file__)
else:
    exec(compile(open(__file__).read(), __file__, 'exec'))
