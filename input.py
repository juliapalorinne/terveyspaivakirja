from app import app
from flask import redirect, render_template, request, session
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash

def check_name(input):
    if len(input)>0 and len(input)<=100:
        return True
    return False


def check_username(input):
    if len(input)>0 and len(input)<=30:
        return True
    return False


def check_password(input):
    if len(input)>0 and len(input)<=50:
        return True
    return False


def check_text(input):
    if len(input)>0 and len(input)<=1000:
        return True
    return False


def check_number(input):
    if len(input)>0 and input.isnumeric():
        return True
    return False


def not_empty(input):
    if not input:
        return False
    return True
