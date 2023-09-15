from flask import Flask, send_file
import subprocess

app = Flask(__name__)


@app.route('/dumpdb')
def dumpdb():
    cmd = "PGPASSWORD='jrp3UEF-neu3qvx2frh' pg_dump -h 10.24.32.2 -U postgres -F plain math_app > /tmp/schema.sql"
    subprocess.call(cmd, shell=True)
    cmd = "gsutil cp / tmp/schema.sql gs: // math-app-transfer"
    subprocess.call(cmd, shell=True)
    return


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
