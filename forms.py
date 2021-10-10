from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, HiddenField, validators, ValidationError


class CommentForm(FlaskForm):
    course_id = HiddenField('Course_id', [validators.Required()])
    comment_id = HiddenField('Comment_id', [validators.Required()], default=None)
    comment = TextAreaField('CommentBox', [validators.Required("نظر خود را وارد کنید.")])
    submit = SubmitField("ارسال")
