from commonconf.backends import use_configparser_backend
from commonconf import settings
from argparse import ArgumentParser
from dao.zoom import (
    get_sub_accounts, get_account_pro_users, update_account_user_basic)
from dao.groups import get_group_members
from logging import getLogger
from email.message import EmailMessage
from smtplib import SMTP
import argparse
import os

logger = getLogger(__name__)

print('hello')
