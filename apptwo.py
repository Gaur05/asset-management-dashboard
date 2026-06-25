from flask import Flask, render_template, request, redirect, session
import psycopg2
import re
import logging
import os

app = Flask(__name__)

app.secret_key = "secretkey"

# LOG FILE SAME DIRECTORY

log_file = os.path.join(
    os.path.dirname(__file__),
    "log.txt"
)

logging.basicConfig(
    filename=log_file,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# PostgreSQL Connection

try:

    db = psycopg2.connect(
        host="localhost",
        database="login_db",
        user="postgres",
        password="mypassword123",
        port="5432"
    )

    cursor = db.cursor()


except psycopg2.Error as err:

    logging.error(
        "Database Connection Error: %s",
        err
    )


@app.route('/')
def home():

    return render_template('login.html')


@app.route('/signup')
def signup():

    return render_template('signup.html')


@app.route('/dashboard')
def dashboard():

    if 'name' not in session:
        return redirect('/')


    cursor.execute(
        "SELECT * FROM assets"
    )

    assets = cursor.fetchall()


    cursor.execute(
        "SELECT COUNT(*) FROM assets"
    )

    total_assets = cursor.fetchone()[0]


    cursor.execute(
        "SELECT COUNT(*) FROM assets WHERE status='Assigned'"
    )

    assigned_count = cursor.fetchone()[0]


    cursor.execute(
        "SELECT COUNT(*) FROM assets WHERE status='Available'"
    )

    available_count = cursor.fetchone()[0]


    cursor.execute(
        "SELECT COUNT(*) FROM assets WHERE status='Maintenance'"
    )

    maintenance_count = cursor.fetchone()[0]


    return render_template(
        'dashboard.html',
        assets=assets,
        total_assets=total_assets,
        assigned_count=assigned_count,
        available_count=available_count,
        maintenance_count=maintenance_count
    )


@app.route('/add_asset', methods=['GET','POST'])
def add_asset():

    if 'name' not in session:
        return redirect('/')


    if request.method == 'POST':


        asset_name = request.form['asset_name']

        category = request.form['category']

        status = request.form['status']

        assigned_to = request.form['assigned_to']

        asset_value = request.form['asset_value']


        query = """

        INSERT INTO assets
        (asset_name, category, status, assigned_to, asset_value)

        VALUES(%s,%s,%s,%s,%s)

        """


        cursor.execute(
            query,
            (
                asset_name,
                category,
                status,
                assigned_to,
                asset_value
            )
        )


        db.commit()


        return redirect('/dashboard')


    return render_template('add_asset.html')



@app.route('/delete_asset/<int:id>')
def delete_asset(id):

    if 'name' not in session:
        return redirect('/')


    cursor.execute(
        "DELETE FROM assets WHERE id=%s",
        (id,)
    )

    db.commit()

    return redirect('/dashboard')


@app.route('/logout')
def logout():


    session.pop('name',None)

    session.pop('user_id',None)

    session.pop('email',None)


    return redirect('/')



@app.route('/login',methods=['POST'])
def login():


    user_id = request.form['user_id']

    password = request.form['password']


    if user_id == "" or password == "":


        return """
        <script>
        alert("Please fill all fields");
        window.location.href='/';
        </script>
        """


    cursor.execute(

        """
        SELECT * FROM user_details
        WHERE user_id=%s AND password=%s
        """,

        (
            user_id,
            password
        )

    )

    user = cursor.fetchone()


    if user:


        session['name'] = user[1]

        session['user_id'] = user[2]

        session['email'] = user[3]


        return """
        <script>
        alert("Login Successful");
        window.location.href='/dashboard';
        </script>
        """


    else:


        return """
        <script>
        alert("Invalid User ID or Password");
        window.location.href='/';
        </script>
        """


@app.route('/register',methods=['POST'])
def register():


    name = request.form['name']

    user_id = request.form['user_id']

    email = request.form['email']

    password = request.form['password']

    re_password = request.form['re_password']


    if (
        name=="" or
        user_id=="" or
        email=="" or
        password=="" or
        re_password==""
    ):


        return """
        <script>
        alert("Please fill all fields");
        window.location.href='/signup';
        </script>
        """


    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'


    if not re.match(email_pattern,email):


        return """
        <script>
        alert("Invalid Email Format");
        window.location.href='/signup';
        </script>
        """


    if len(password)<8:


        return """
        <script>
        alert("Password must be at least 8 characters");
        window.location.href='/signup';
        </script>
        """


    if password != re_password:


        return """
        <script>
        alert("Passwords do not match");
        window.location.href='/signup';
        </script>
        """


    cursor.execute(

        """
        SELECT * FROM user_details
        WHERE user_id=%s OR email=%s
        """,

        (
            user_id,
            email
        )

    )


    existing_user = cursor.fetchone()


    if existing_user:


        return """
        <script>
        alert("User Already Exists");
        window.location.href='/signup';
        </script>
        """


    cursor.execute(

        """
        INSERT INTO user_details
        (name,user_id,email,password)

        VALUES(%s,%s,%s,%s)

        """,

        (
            name,
            user_id,
            email,
            password
        )

    )


    db.commit()


    return """
    <script>
    alert("User Registered Successfully");
    window.location.href='/';
    </script>
    """


@app.errorhandler(Exception)
def handle_error(error):


    logging.error(
        "Application Error: %s",
        error,
        exc_info=True
    )


    return "Something went wrong. Check log.txt"



if __name__ == '__main__':
    app.run(debug=True)
