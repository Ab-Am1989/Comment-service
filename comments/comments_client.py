import grpc
import comments_pb2_grpc as pb2_grpc
import comments_pb2 as pb2

class CommentClient(object):
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.client = pb2_grpc.commentsStub(self.channel)

    def get_comments(self, course_id):
        request = pb2.CourseRequest(course_id=course_id)
        return self.client.get_comments(request)
# This is only for test
if __name__ == "__main__":
    client = CommentClient()
    course_id = int(input("Enter course_id..."))
    result = client.get_comments(course_id=course_id)
    print(f'   {result}')
    print((result.results))