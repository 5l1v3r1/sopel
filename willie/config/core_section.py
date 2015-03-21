# coding=utf-8

from __future__ import unicode_literals

from willie.config.types import (
    StaticSection, ValidatedAttribute, ListAttribute, ChoiceAttribute
)
from willie.tools import Identifier


class CoreSection(StaticSection):
    #  5.x backwards compat; remove for 6.0.0
    def __getattr__(self, name):
        if self._parser.has_option(self._section_name, name):
            print('deprecated', self._section_name, name)  # TODO
            return self._parser.get(self._section_name, name)
        else:
            return None

    def get_list(self, name):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            return ','.split(self._parser.get(self._section_name, name))

    admins = ListAttribute('admins')
    """The list of people (other than the owner) who can administer the bot"""

    auth_method = ChoiceAttribute('auth_method', ['nickserv', 'authserv',
                                                  'sasl', 'server'])
    """The method to use to authenticate with the server.

    Can be ``nickserv``, ``authserv``, ``sasl``, or ``server``."""

    auth_password = ValidatedAttribute('auth_password')
    """The password to use to authenticate with the server."""

    auth_target = ValidatedAttribute('auth_target')
    """The user to use for nickserv authentication.

    May not apply, depending on ``auth_method``"""

    auth_username = ValidatedAttribute('auth_username')
    """The username/account to use to authenticate with the server.

    May not apply, depending on ``auth_method``."""

    bind_host = ValidatedAttribute('bind_host')
    """Bind the connection to a specific IP"""

    ca_certs = ValidatedAttribute('ca_certs', default='/etc/pki/tls/cert.pem')
    """The path of the CA certs pem file"""

    channels = ListAttribute('channels')
    """List of channels for the bot to join when it connects"""

    default_time_format = ValidatedAttribute('default_time_format',
                                             default='%F - %T%Z')
    """The default format to use for time in messages."""

    default_timezone = ValidatedAttribute('default_timezone')
    """The default timezone to use for time in messages."""

    delay = ValidatedAttribute('delay')  # TODO wat
    dotdir = ValidatedAttribute('dotdir')  # TODO wat

    enable = ListAttribute('enable')
    """A whitelist of the only modules you want to enable."""

    exclude = ListAttribute('exclude')
    """A list of modules which should not be loaded."""

    exit_on_error = ValidatedAttribute('exit_on_error')  # TODO wat

    extra = ListAttribute('extra')
    """A list of other directories you'd like to include modules from."""

    help_prefix = ValidatedAttribute('help_prefix', default='.')
    """The prefix to use in help"""

    homedir = ValidatedAttribute('homedir')  # TODO wat

    host = ValidatedAttribute('host')
    """The server to connect to."""

    host_blocks = ListAttribute('host_blocks')
    """A list of hostmasks which Willie should ignore.

    Regular expression syntax is used"""

    log_raw = ValidatedAttribute('log_raw', bool, default=False)
    """Whether a log of raw lines as sent and recieved should be kept."""

    logdir = ValidatedAttribute('logdir')  # TODO default
    """Directory in which to place logs."""

    logging_channel = ValidatedAttribute('logging_channel', Identifier)
    """The channel to send logging messages to."""

    logging_level = ChoiceAttribute('logging_level',
                                    ['CRITICAL', 'ERROR', 'WARNING', 'INFO',
                                     'DEBUG'],
                                    'WARNING')
    """The lowest severity of logs to display."""

    modes = ValidatedAttribute('modes', default='B')
    """User modes to be set on connection."""

    name = ValidatedAttribute('name', default='Willie: http://willie.dftba.net')
    """The "real name" of your bot for WHOIS responses."""

    nick = ValidatedAttribute('nick', Identifier, default=Identifier('Willie'))
    """The nickname for the bot"""

    nick_blocks = ListAttribute('nick_blocks')
    """A list of nicks which Willie should ignore.

    Regular expression syntax is used."""

    owner = ValidatedAttribute('owner')
    """The IRC name of the owner of the bot."""

    pid_file_path = ValidatedAttribute('pid_file_path')  # TODO wat

    port = ValidatedAttribute('port', int, default=6667)
    """The port to connect on."""

    prefix = ValidatedAttribute('prefix', default='\.')
    """The prefix to add to the beginning of commands.

    It is a regular expression (so the default, ``\.``, means commands start
    with a period), though using capturing groups will create problems."""

    timeout = ValidatedAttribute('timeout')  # TODO default?
    """The amount of time acceptable between pings before timing out."""

    use_ssl = ValidatedAttribute('use_ssl', bool, default=False)
    """Whether to use a SSL secured connection."""

    user = ValidatedAttribute('user')
    """The "user" for your bot (the part before the @ in the hostname)."""

    verbose = ValidatedAttribute('verbose')  # TODO remove

    verify_ssl = ValidatedAttribute('verify_ssl', default=True)
    """Whether to require a trusted SSL certificate for SSL connections."""
