from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
from my_lib import database_worker, encrypt_password, check_password
from werkzeug.utils import secure_filename
from functools import wraps
import jwt, pycountry, dotenv, os
from datetime import datetime, timedelta



app = Flask(__name__) # Initialize Flask application
app.secret_key = 'you-will-never-guess' # Define a secret key for the application. This is used to keep client-side sessions secure
app.config['UPLOAD_FOLDER'] = 'upload_folder' # Define the folder where user uploads (such as images) will be stored


dotenv.load_dotenv() # Load environment variables from .env file
token_key = os.getenv('TOKEN_ENCRYPTION_KEY') # Retrieve the token encryption key from environment variables

# Define a function to parse dates and return only the date part (excluding time)
def parse_date(value):
    return value.split(' ')[0]

# Define a function to calculate how much time has passed since a given datetime
def how_much_time_ago(value):
    now = datetime.now()
    post_date = datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f')
    time_diff = now - post_date

    # Define a list of time units and their lengths in seconds
    time_units = [
        ('year', 60*60*24*365),
        ('month', 60*60*24*30),
        ('week', 60*60*24*7),
        ('day', 60*60*24),
        ('hour', 60*60),
        ('minute', 60),
        ('second', 1)
    ]

    # Loop through each time unit, checking if the time difference is greater than the unit length
    for unit, unit_length in time_units:
        if time_diff.total_seconds() > unit_length:
            num_units = int(time_diff.total_seconds() // unit_length)
            unit = unit if num_units == 1 else unit + 's'  # Handle plural units
            return f"{num_units} {unit} ago"

    return "Just now"

# Define a function to convert country names to their corresponding flag code
def flag(country):
    try:
        return pycountry.countries.get(name=country).alpha_2.lower()
    except:
        return 'unknown'

# Register the custom functions as filters in Jinja2 environment
app.jinja_env.filters['parse_date'] = parse_date
app.jinja_env.filters['how_much_time_ago'] = how_much_time_ago
app.jinja_env.filters['flag'] = flag


# Define a decorator function for routes that require a user to be logged in
def token_required(f):
    # Use the wraps function from functools to preserve the original function's name and docstring
    @wraps(f)
    def decorated(*args, **kwargs):
        # If there is no token in the user's session, redirect them to the login page
        if 'token' not in session:
            return redirect(url_for('login'))
        try:
            # Attempt to decode the token using the secret key
            # If the token is valid, this will return the data encoded in the token
            data = jwt.decode(session['token'], token_key, algorithms=['HS256'])
        except:
            # If an error occurs (such as if the token is expired or tampered with), redirect the user to the login page
            return redirect(url_for('login'))

        # If the token is valid, continue to the original function with the original arguments
        return f(*args, **kwargs)

    # Return the new decorated function
    return decorated


@app.route('/like_post/<int:post_id>', methods=['POST'])
@token_required
def like_post(post_id):
    current_user = jwt.decode(session['token'], token_key, algorithms=['HS256'])
    user_id = current_user['user_id']

    db = database_worker("shelfshare.db")
    check_like_query = f"SELECT * FROM likes WHERE user_id = {user_id} AND post_id = {post_id}"
    like_record = db.run_fetchone(query=check_like_query)

    # count the number of times a post_id appears in the like table
    count_likes_query = f"SELECT COUNT(*) FROM likes WHERE post_id = {post_id}"
    count_likes = db.run_fetchone(query=count_likes_query)[0]

    if like_record:
        # If the like record exists, delete it (unlike)
        unlike_query = f"DELETE FROM likes WHERE user_id = {user_id} AND post_id = {post_id}"
        db.run_save(query=unlike_query)

    else:
        # If the like record doesn't exist, create it (like)
        like_query = f"INSERT INTO likes (user_id, post_id) VALUES ('{user_id}', '{post_id}')"
        db.run_save(query=like_query)

    return redirect('/post/' + str(post_id))


@app.route('/delete_comment/<int:comment_id>')
@token_required
def delete_comment(comment_id):
    db = database_worker("shelfshare.db")
    delete_comment = f"DELETE FROM comments WHERE id = {comment_id}"
    db.run_save(query=delete_comment)
    return redirect('/profile')

@app.route('/delete_post/<int:post_id>')
@token_required
def delete_post(post_id):
    db = database_worker("shelfshare.db")
    delete_post = f"DELETE FROM posts WHERE id = {post_id}"
    db.run_save(query=delete_post)
    return redirect('/profile')

@app.route('/edit_comment/<int:comment_id>', methods=['GET', 'POST'])
@token_required
def edit_comment(comment_id):
    db = database_worker("shelfshare.db")
    comment = db.search(f"SELECT * FROM comments WHERE id = {comment_id}")

    if request.method == 'POST':
        content = request.form['content']

        query = f"UPDATE comments SET content='{content}'"
        db.run_save(query=query)
        return redirect(url_for('profile'))

    return render_template('edit_comment.html', comment=comment[0])


@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
@token_required
def edit_post(post_id):
    db = database_worker("shelfshare.db")
    post = db.search(f"SELECT * FROM posts WHERE id = {post_id}")
    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        content = request.form['content']
        image = request.files.get('image')

        # If an image was uploaded, save it and get its filename
        if image:
            image_name = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
        else:
            image_name = None

        # SQL query to update the post data in the database
        query = f"UPDATE posts SET title='{title}', category='{category}', content='{content}', image_name='{image_name}' WHERE id={post_id}"
        db.run_save(query)
        return redirect(url_for('profile'))
    return render_template('edit_post.html', post=post[0])

@app.route('/delete_profile/<int:user_id>')
@token_required
def delete_profile(user_id):
    db = database_worker("shelfshare.db")
    db.run_save(f"DELETE FROM posts WHERE user_id = {user_id}")
    db.run_save(f"DELETE FROM comments WHERE user_id = {user_id}")
    db.run_save(f"DELETE FROM users WHERE id = {user_id}")
    return redirect('/logout')

@app.route('/profile')
@token_required
def profile():
    current_user = jwt.decode(session['token'], token_key, algorithms=['HS256'])
    user_id = current_user['user_id']
    db = database_worker("shelfshare.db")
    user = db.search(f"SELECT * FROM users WHERE id = {user_id}")
    posts = db.search(f"SELECT * FROM posts WHERE user_id = {user_id} ORDER BY posts.datetime DESC")
    comments = db.search(f"SELECT * FROM comments WHERE user_id = {user_id} ORDER BY comments.datetime DESC")
    liked_posts = db.search(f"SELECT posts.* FROM likes INNER JOIN posts ON likes.post_id = posts.id WHERE likes.user_id = {user_id}")
    return render_template('profile.html', posts=posts, comments=comments, liked_posts=liked_posts, user=user[0])


@app.route('/add_comment/<int:post_id>', methods=['POST'])
@token_required
def add_comment(post_id):
    db = database_worker("shelfshare.db")
    if request.method == 'POST':
        comment = request.form['comment']
        user_id = jwt.decode(session['token'], token_key, algorithms=['HS256'])
        create_comment = f"INSERT INTO comments (content, datetime, user_id, post_id) VALUES ('{comment}', '{datetime.now()}', '{user_id['user_id']}', '{post_id}')"
        db.run_save(query=create_comment)
    return redirect('/post/' + str(post_id))

@app.route('/post/<int:post_id>')
@token_required
def view_post(post_id):
    current_user = jwt.decode(session['token'], token_key, algorithms=['HS256'])
    db = database_worker("shelfshare.db")
    post = db.search(f"SELECT posts.*, users.name FROM posts INNER JOIN users ON posts.user_id = users.id WHERE posts.id = {post_id}")
    comments = db.search(f"SELECT comments.*, users.name FROM comments INNER JOIN users ON comments.user_id = users.id WHERE comments.post_id = {post_id} ORDER BY comments.datetime DESC")

    # Check if the current user has liked the post
    user_like = db.run_fetchone(f"SELECT * FROM likes WHERE post_id = {post_id} AND user_id = {current_user['user_id']}")
    is_liked = user_like is not None

    if post:
        return render_template('post.html', post=post[0], comments=comments, is_liked=is_liked)

    return render_template('index.html')

@app.route('/create_post', methods=['GET', 'POST'])
@token_required
def create_post():
    if 'image' in request.files:
        image = request.files['image']
        if image.filename != '':
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            filename = None
    else:
        filename = None

    current_user = jwt.decode(session['token'], token_key, algorithms=['HS256'])
    db = database_worker("shelfshare.db")

    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        content = request.form['content']
        user_id = current_user['user_id']
        create_post = (f"INSERT INTO posts (title, category, content, datetime, image_name, user_id) VALUES ('{title}', '{category}', '{content}', '{datetime.now()}', '{filename}','{user_id}')")
        db.run_save(query=create_post)

        return redirect(url_for('index'))

    return render_template('create_post.html')

@app.route('/file/<filename>')
def file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/discussions')
@token_required
def discussions():
    db = database_worker("shelfshare.db")
    posts = db.search("SELECT posts.*, users.name FROM posts INNER JOIN users ON posts.user_id = users.id WHERE posts.category = 'Discussion' ORDER BY posts.datetime DESC")
    return render_template('discussions.html', posts=posts)

@app.route('/book_recommendations')
@token_required
def book_recommendations():
    db = database_worker("shelfshare.db")
    posts = db.search("SELECT posts.*, users.name FROM posts INNER JOIN users ON posts.user_id = users.id WHERE posts.category = 'Book Recommendation' ORDER BY posts.datetime DESC")
    return render_template('book_recommendations.html', posts=posts)

@app.route('/book_reviews')
def book_reviews():
    db = database_worker("shelfshare.db")
    posts = db.search("SELECT posts.*, users.name FROM posts INNER JOIN users ON posts.user_id = users.id WHERE posts.category = 'Book Review' ORDER BY posts.datetime DESC")
    return render_template('book_reviews.html', posts=posts)

@app.route('/reminders')
@token_required
def reminders():
    db = database_worker("shelfshare.db")
    posts = db.search("SELECT posts.*, users.name FROM posts INNER JOIN users ON posts.user_id = users.id WHERE posts.category = 'Reminder' ORDER BY posts.datetime DESC")
    return render_template('reminders.html', posts=posts)

@app.route('/announcements')
@token_required
def annoucements():
    db = database_worker("shelfshare.db")
    posts = db.search("SELECT posts.*, users.name FROM posts INNER JOIN users ON posts.user_id = users.id WHERE posts.category = 'Announcement' ORDER BY posts.datetime DESC")
    return render_template('announcements.html', posts=posts)

@app.route('/top_liked')
@token_required
def top_liked():
    db = database_worker("shelfshare.db")
    most_liked_posts = db.search("SELECT posts.*, users.name FROM posts INNER JOIN users ON posts.user_id = users.id WHERE posts.id IN (SELECT post_id FROM likes GROUP BY post_id ORDER BY COUNT(*) DESC)")
    return render_template('top_liked.html', most_liked_posts=most_liked_posts)

@app.route('/')
@token_required
def index():
    db = database_worker("shelfshare.db")
    posts = db.search("SELECT posts.*, users.name FROM posts INNER JOIN users ON posts.user_id = users.id ORDER BY posts.datetime DESC")
    return render_template('index.html', posts=posts)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        # Check if email and password fields are not empty
        if len(email) > 0 and len(password) > 0:
            # Create a database worker to interact with the database
            db = database_worker("shelfshare.db")
            # SQL query to get user information by email
            login = f"SELECT * FROM users WHERE email = '{email}'"
            # Fetch user information from database
            user = db.search(query=login)
            # Check if user exists
            if user:
                # Unpack user data
                id, name, username, country, email, hash = user[0]
                # Check if password is correct
                if check_password(user_password=password, hashed_password=hash):
                    # Create a new JWT token for the user
                    token = jwt.encode({'user_id': id, 'exp': datetime.utcnow() + timedelta(minutes=180)}, token_key,algorithm='HS256')
                    # Store the JWT token in the user session
                    session['token'] = token
                    # Redirect the user to the home page
                    return redirect("/")
                else:
                    # Flash a message indicating that the password is incorrect
                    flash(('Login failed. Password Incorrect', 'danger'))
            else:
                # Flash a message indicating that the login credentials are incorrect
                flash(('Login failed. Incorrect Credentials', 'danger'))

    return render_template('login.html')

@app.route('/register', methods = ["GET", "POST"])
def register():
    db = database_worker("shelfshare.db")

    if request.method == "POST":
        name = request.form['fullname']
        username = request.form['username']
        country = request.form['country']
        email = request.form['email']
        password = request.form['password']
        password_confirm = request.form['password_confirm']
        if len(name)>0 and len(username)>0 and len(country)>0 and len(email)>0 and len(password)>0:
            if password != password_confirm:
                flash(('Passwords do not match.', 'danger'))
            elif len(password) < 8:
                flash(('Password must be at least 8 characters.', 'danger'))

            else:
                if '@schoolx.edu' not in email:
                    flash(("Invalid email address, not a 'School X email.", 'danger'))
                elif len(name) > 0 and len(username) > 0 and len(country) > 0 and len(email) > 0 and len(password) > 0:
                    register = f"INSERT into users(name, username, country, email, password) values('{name}', '{username}', '{country}', '{email}', '{encrypt_password(password)}')"
                    db.run_save(query=register)
                    flash(('Registration completed. Please log in.', 'success'))

                    return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('token', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()
