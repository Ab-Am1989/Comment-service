FROM python

RUN mkdir /service
COPY protobufs/ service/protobufs/
COPY comments/ service/comments/
WORKDIR service/comments
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/comments.proto
EXPOSE 50051
ENTRYPOINT ["python","comments.py"]