import os
import pymssql
from dotenv import load_dotenv


# Function for insert comments
def insert_comment(course_id: int, comment: str, student_id: int):
    load_dotenv()
    conn = pymssql.connect(host='185.128.82.62:11433', user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'),
                           database='Consulet')
    cursor = conn.cursor()
    params = (course_id, comment, student_id)
    cursor.callproc('insert_comment', params)
    conn.commit()
    cursor.close()
    conn.close()
    return True


# Function for select all comments with special course_id
def show_comment(course_id: int):
    load_dotenv()
    conn = pymssql.connect(host='185.128.82.62:11433', user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'),
                           database='Consulet')
    cursor = conn.cursor()
    cursor.execute(f"SELECT comment,id from comment where course_id = '{course_id}'")
    t = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    if t:
        # print(t[0])
        return t
    else:
        return None


# Function for select a record in course table with special course_id
def show_course(course_id: int):
    load_dotenv()
    conn = pymssql.connect(host='185.128.82.62:11433', user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'),
                           database='Consulet')
    cursor = conn.cursor()
    cursor.execute(f"SELECT \
    course.student_id,course.teacher_id,course.[name],course.grade,course.price,course.CreatedTime,course.UpdatedTime \
    FROM course inner join comment \
    on course.id = comment.course_id \
    WHERE  comment.course_id  = '{course_id}'")
    t = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    if t:
        # print(t[0])
        return t
    else:
        return None
