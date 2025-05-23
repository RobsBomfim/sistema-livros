from flask import Flask, request,jsonify
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    dbname = 'catalogo',
    user = 'postgres',
    password = 'rafael2014',
    host = 'localhost',
    port = '5432'
)

cur = conn.cursor()