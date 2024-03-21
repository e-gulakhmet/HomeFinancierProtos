# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from homefinancier.storages.v1 import storages_pb2 as homefinancier_dot_storages_dot_v1_dot_storages__pb2


class StoragesServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateStorage = channel.unary_unary(
                '/homefinancier.storages.v1.StoragesService/CreateStorage',
                request_serializer=homefinancier_dot_storages_dot_v1_dot_storages__pb2.CreateStorageRequest.SerializeToString,
                response_deserializer=homefinancier_dot_storages_dot_v1_dot_storages__pb2.CreateStorageResponse.FromString,
                )
        self.GetStorage = channel.unary_unary(
                '/homefinancier.storages.v1.StoragesService/GetStorage',
                request_serializer=homefinancier_dot_storages_dot_v1_dot_storages__pb2.GetStorageRequest.SerializeToString,
                response_deserializer=homefinancier_dot_storages_dot_v1_dot_storages__pb2.GetStorageResponse.FromString,
                )


class StoragesServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateStorage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStorage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StoragesServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateStorage': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateStorage,
                    request_deserializer=homefinancier_dot_storages_dot_v1_dot_storages__pb2.CreateStorageRequest.FromString,
                    response_serializer=homefinancier_dot_storages_dot_v1_dot_storages__pb2.CreateStorageResponse.SerializeToString,
            ),
            'GetStorage': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStorage,
                    request_deserializer=homefinancier_dot_storages_dot_v1_dot_storages__pb2.GetStorageRequest.FromString,
                    response_serializer=homefinancier_dot_storages_dot_v1_dot_storages__pb2.GetStorageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'homefinancier.storages.v1.StoragesService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StoragesService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateStorage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/homefinancier.storages.v1.StoragesService/CreateStorage',
            homefinancier_dot_storages_dot_v1_dot_storages__pb2.CreateStorageRequest.SerializeToString,
            homefinancier_dot_storages_dot_v1_dot_storages__pb2.CreateStorageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStorage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/homefinancier.storages.v1.StoragesService/GetStorage',
            homefinancier_dot_storages_dot_v1_dot_storages__pb2.GetStorageRequest.SerializeToString,
            homefinancier_dot_storages_dot_v1_dot_storages__pb2.GetStorageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
