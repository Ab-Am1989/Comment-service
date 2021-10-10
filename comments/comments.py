from concurrent import futures
import grpc

from comments_pb2 import CourseRequest, CommentProp, CommentResponse
import comments_pb2_grpc
import db


class CommentsService(comments_pb2_grpc.commentsServicer):
    def get_comments(self, request, context):
        # Get course_id from grpc client
        course_id = request.course_id
        # Fetch all comments and comment's IDs from DB
        print("course_id", course_id)
        comments_data = db.show_comment(course_id)
        comments_data_list = list()
        for comment in comments_data:
            res = CommentProp(comment=str(comment[0]), comment_id=comment[1])
            comments_data_list.append(res)

        # This sample data are created for test only here we need connect to db
        # ---------------------------------------------------------------------------------------
        # print("course_id", course_id)
        # cr1 = CourseRequest(course_id=10)
        # c2 = CourseRequest(course_id=15)
        # c3 = CourseRequest(course_id=20)
        #
        # res11 = CommentProp(comment='hi', comment_id=11)
        # res12 = CommentProp(comment='very bad', comment_id=12)
        # res13 = CommentProp(comment='not bad', comment_id=13)
        # res21 = CommentProp(comment='great', comment_id=21)
        # res22 = CommentProp(comment='i love this teacher', comment_id=22)
        # res23 = CommentProp(comment='he is not tolerant', comment_id=23)
        # res24 = CommentProp(comment='he reads your mind', comment_id=24)
        # res31 = CommentProp(comment='some comments', comment_id=31)
        # res32 = CommentProp(comment='it was so bad', comment_id=32)
        #
        # if course_id <= 10:
        #     return CommentResponse(results=[res11, res12, res13])
        # elif course_id >= 20:
        #     return CommentResponse(results=(res31, res32))
        # else:
        #     return CommentResponse(results=(res21, res22, res23, res24))
        # ---------------------------------------------------------------------------------------
        return CommentResponse(results=comments_data_list)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    comments_pb2_grpc.add_commentsServicer_to_server(CommentsService(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
