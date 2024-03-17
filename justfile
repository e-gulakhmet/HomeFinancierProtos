# Command to generate Python proto files
gen-python:
    # Ensure the output directory exists
    mkdir -p generated/python
    # Generate Python gRPC files
    python -m grpc_tools.protoc \
    -I ./protos/ \
    --python_out=generated/python \
    --pyi_out=generated/python \
    --grpc_python_out=generated/python \
    homefinancier/v1/greeter.proto


# Command to generate proto files for supported languages(Python)
gen-all: gen-python
