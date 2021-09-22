from flask import render_template, redirect, flash
from . import admin
from decorators import role_required



@admin.route('/home[admin]')
@role_required('admin, super')
def home():
    return render_template('admin/home.html')