from flask import Flask, request, jsonify, render_template, session, redirect, url_for, flash
from datetime import datetime
import sqlite3
import logging
import re 
import os


app = Flask(__name__)

# 路徑修改
def get_db_connection():
    conn = sqlite3.connect('')
    if not os.path.exists(''):
        logging.error(f"Database file not found at {''}")
        return None
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

# 補齊空缺程式碼
@app.route()
def page_login():
        return 
    
@app.route('/page_register', methods=[])
def page_register():
    if request.method == 'POST':
        data = request.get_json()
       # 補齊空缺程式碼
        if ...
            return jsonify({"status": "error", "message": "此名稱已被使用"})

        if len(password) < 8:
       ...
       
    return render_template('page_register.html')

# 補齊剩餘副程式


# 補齊空缺程式碼
if __name__ == '__main__':
    app.run()


