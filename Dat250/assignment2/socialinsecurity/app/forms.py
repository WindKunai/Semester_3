from datetime import datetime
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import (
    BooleanField,
    DateField,
    FileField,
    FormField,
    PasswordField,
    StringField,
    SubmitField,
    TextAreaField,
)

class LoginForm(FlaskForm):
    """Provides the login form for the application."""

    username = StringField(label="Username", render_kw={"placeholder": "Username"}, validators=[DataRequired()])
    password = PasswordField(label="Password", render_kw={"placeholder": "Password"}, validators=[DataRequired()])
    remember_me = BooleanField(
        label="Remember me"
    )
    submit = SubmitField(label="Sign In")

class RegisterForm(FlaskForm):
    """Provides the registration form for the application."""

    first_name = StringField(label="First Name", render_kw={"placeholder": "First Name"}, validators=[DataRequired()])
    last_name = StringField(label="Last Name", render_kw={"placeholder": "Last Name"}, validators=[DataRequired()])
    username = StringField(label="Username", render_kw={"placeholder": "Username"}, validators=[DataRequired()])
    password = PasswordField(label="Password", render_kw={"placeholder": "Password"}, validators=[DataRequired()])
    confirm_password = PasswordField(label="Confirm Password", render_kw={"placeholder": "Confirm Password"}, validators=[DataRequired()])
    submit = SubmitField(label="Sign Up")

class IndexForm(FlaskForm):
    """Provides the composite form for the index page."""
    
    login = FormField(LoginForm)
    register = FormField(RegisterForm)
    csrf_token = StringField()

class PostForm(FlaskForm):
    """Provides the post form for the application."""

    content = TextAreaField(label="New Post", render_kw={"placeholder": "What are you thinking about?"})
    image = FileField(label="Image")
    submit = SubmitField(label="Post")

class CommentsForm(FlaskForm):
    """Provides the comment form for the application."""

    comment = TextAreaField(label="New Comment", render_kw={"placeholder": "What do you have to say?"})
    submit = SubmitField(label="Comment")

class FriendsForm(FlaskForm):
    """Provides the friend form for the application."""

    username = StringField(label="Friend's username", render_kw={"placeholder": "Username"})
    submit = SubmitField(label="Add Friend")

class ProfileForm(FlaskForm):
    """Provides the profile form for the application."""

    education = StringField(label="Education", render_kw={"placeholder": "Highest education"})
    employment = StringField(label="Employment", render_kw={"placeholder": "Current employment"})
    music = StringField(label="Favorite song", render_kw={"placeholder": "Favorite song"})
    movie = StringField(label="Favorite movie", render_kw={"placeholder": "Favorite movie"})
    nationality = StringField(label="Nationality", render_kw={"placeholder": "Your nationality"})
    birthday = DateField(label="Birthday", default=datetime.now())
    submit = SubmitField(label="Update Profile")
