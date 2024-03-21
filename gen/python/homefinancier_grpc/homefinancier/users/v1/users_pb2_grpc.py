# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from homefinancier.users.v1 import users_pb2 as homefinancier_dot_users_dot_v1_dot_users__pb2


class UsersServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary(
                '/homefinancier.users.v1.UsersService/CreateUser',
                request_serializer=homefinancier_dot_users_dot_v1_dot_users__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=homefinancier_dot_users_dot_v1_dot_users__pb2.CreateUserResponse.FromString,
                )


class UsersServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UsersServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=homefinancier_dot_users_dot_v1_dot_users__pb2.CreateUserRequest.FromString,
                    response_serializer=homefinancier_dot_users_dot_v1_dot_users__pb2.CreateUserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'homefinancier.users.v1.UsersService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UsersService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/homefinancier.users.v1.UsersService/CreateUser',
            homefinancier_dot_users_dot_v1_dot_users__pb2.CreateUserRequest.SerializeToString,
            homefinancier_dot_users_dot_v1_dot_users__pb2.CreateUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
