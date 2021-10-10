from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_required

from comments import comments_client
from forms import CommentForm

from db import db
import datetime

app = Flask(__name__)
app.secret_key = 'DevelopmentKey'
login_manager = LoginManager()


@app.route('/comment', methods=['POST'])
# Because of we haven't any user now we commented line below. after project runs really we will uncomment it
# @login_required
def add_comment():
    try:
        form = CommentForm()
        course_id = form.course_id
        if request.method == 'POST':
            if not form.validate():
                return redirect(url_for('course_details', course_id=course_id))
            else:
                comment = form.comment
                student_id = current_user.id
                course_id = form.course_id  # How can we catch the course_id and comment_id?
                comment_id = form.comment_id

                # add comment to db ...
                # We need insert to database a comment, comment_id(if we want to reply) user_id and course_id
                db.insert_comment(comment, student_id, course_id, comment_id)

                flash('نظر شما با موفقیت ثبت شد.')
                return render_template('add_comment.html', form=form)
    except Exception as e:
        return str(e)


@app.route('/course/details/<int:course_id>')
def course_details(course_id):
    # Search course_id in database and return its rows. if don't exist a database object with such ...
    # ...course_id return None
    rows = db.show_course(course_id)
    # This is just sample data
    # rows = {"id": 2, "student_id": 1, "teacher_id": 1, "name": 'history', "grade": 'c', "price": 50,
    #        "CreatedTime": datetime.datetime(2021, 10, 4, 16, 48, 57), "UpdatedTime": None}
    # After course's fields fetches, data for front end will be prepare and send
    if rows is not None:
        form = CommentForm()
        form.course_id = rows.id
        client = comments_client.CommentClient()
        all_comments = client.get_comments(course_id=course_id)
        all_comments_list = all_comments.results
        context = {
            'rows': rows,
            'form': form,
            'all_comments': all_comments_list,
        }
        return render_template('course_details.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)
