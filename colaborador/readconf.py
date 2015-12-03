# -*- coding: utf-8 -*-
# https://github.com/jpadilla/django-dotenv

# try:
#     open(os.path.join(os.path.dirname(os.path.dirname(__file__)), SETTINGS_EXTRA), "r")
# except IOError:
#     from django.utils.crypto import get_random_string
#     chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
#     content = '# SECURITY WARNING: keep the secret key used in production secret!\n'
#     content += 'SECRET_KEY = \'{}\'\n'.format(get_random_string(50, chars))
#     content += '\n'
#     content += '# SECURITY WARNING: don\'t run with debug turned on in production!\n'
#     content += 'DEBUG = False\n'
#     content += 'TEMPLATE_DEBUG = DEBUG\n'
#     content += 'ALLOWED_HOSTS = [\'.localhost\', \'127.0.0.1\']\n'
#     content += '\n'
#     content += 'LDAP_SERVER_URI = \'ldap://<ip>:389\'\n'
#     content += 'LDAP_PREBINDDN = \'<common_name>\'\n'
#     content += 'LDAP_PREBINDPW = \'<password>\'\n'
#     content += 'LDAP_SEARCHDN = \'OU=<organizational_unit>,DC=<domain_component>,DC=com\'\n'
#
#     open(os.path.join(os.path.dirname(os.path.dirname(__file__)), SETTINGS_EXTRA), "w").write(content)
#     execfile(os.path.join(os.path.dirname(os.path.dirname(__file__)), SETTINGS_EXTRA))
#     pass


import os
import re
import sys
import warnings
import settings


line_re = re.compile(r"""
    ^
    (?:export\s+)?      # optional export
    ([\w\.]+)           # key
    (?:\s*=\s*|:\s+?)   # separator
    (                   # optional value begin
        '(?:\'|[^'])*'  #   single quoted value
        |               #   or
        "(?:\"|[^"])*"  #   double quoted value
        |               #   or
        [^#\n]+         #   unquoted value
    )?                  # value end
    (?:\s*\#.*)?        # optional comment
    $
""", re.VERBOSE)

variable_re = re.compile(r"""
    (\\)?               # is it escaped with a backslash?
    (\$)                # literal $
    (                   # collect braces with var for sub
        \{?             #   allow brace wrapping
        ([A-Z0-9_]+)    #   match the variable
        \}?             #   closing brace
    )                   # braces end
""", re.IGNORECASE | re.VERBOSE)


def read_conf(conf=None):
    """
    Read a conf file into os.environ.

    If not given a path to a conf path, does filthy magic stack backtracking
    to find manage.py and then find the conf.
    """
    if conf is None:
        frame_filename = sys._getframe().f_back.f_code.co_filename
        conf = os.path.join(os.path.dirname(frame_filename), settings.SETTINGS_EXTRA)

    if os.path.exists(conf):
        with open(conf) as f:
            for k, v in parse_conf(f.read()).items():
                os.environ.setdefault(k, v)
    else:
        warnings.warn("Not reading {0} - it doesn't exist.".format(conf))
        from django.utils.crypto import get_random_string
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

        content = '# SECURITY WARNING: keep the secret key used in production secret!\n'
        content += 'SECRET_KEY = \'{}\'\n'.format(get_random_string(50, chars))
        content += '\n'
        content += '# SECURITY WARNING: don\'t run with debug turned on in production!\n'
        content += 'DEBUG = False\n'
        content += 'ALLOWED_HOSTS = [\'.localhost\', \'127.0.0.1\']\n'
        content += '\n'
        content += 'LDAP_SERVER_URI = \'ldap://<ip>:389\'\n'
        content += 'LDAP_PREBINDDN = \'<common_name>\'\n'
        content += 'LDAP_PREBINDPW = \'<password>\'\n'
        content += 'LDAP_SEARCHDN = \'OU=<organizational_unit>,DC=<domain_component>,DC=com\'\n'

        open((conf), "w").write(content)
        read_conf(conf)
        # execfile(os.path.join(os.path.dirname(os.path.dirname(__file__)), SETTINGS_EXTRA))
        # pass


def parse_conf(content):
    env = {}

    for line in content.splitlines():
        m1 = line_re.search(line)

        if m1:
            key, value = m1.groups()

            if value is None:
                value = ''

            # Remove leading/trailing whitespace
            value = value.strip()

            # Remove surrounding quotes
            m2 = re.match(r'^([\'"])(.*)\1$', value)

            if m2:
                quotemark, value = m2.groups()
            else:
                quotemark = None

            # Unescape all chars except $ so variables can be escaped properly
            if quotemark == '"':
                value = re.sub(r'\\([^$])', '\1', value)

            if quotemark != "'":
                # Substitute variables in a value
                for parts in variable_re.findall(value):
                    if parts[0] == '\\':
                        # Variable is escaped, don't replace it
                        replace = ''.join(parts[1:-1])
                    else:
                        # Replace it with the value from the environment
                        replace = env.get(
                            parts[-1],
                            os.environ.get(parts[-1], '')
                        )

                    value = value.replace(''.join(parts[0:-1]), replace)

            env[key] = value

        elif not re.search(r'^\s*(?:#.*)?$', line):  # not comment or blank
            warnings.warn(
                "Line {0} doesn't match format".format(repr(line)),
                SyntaxWarning
            )

    return env
