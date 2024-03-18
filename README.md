# HomeFinancierProtos Repository

This repository contains the gRPC proto files for the HomeFinancier project. It is structured to support multiple microservices and versions, and it provides a build system to generate code for different languages.

## Repository Structure

- `proto/`: Contains all the proto files, organized by microservice and version.
- `gen/`: Contains the generated code for different languages, created by the build system.

## Using guide
Before star you need to install:
1. [`buf`](https://github.com/bufbuild/buf) - CLI tool for working with Protocol Buffers.
2. [`just`](https://github.com/casey/just) - Command runner.

### Generating proto files
To generate proto files, run `just gen-all` command.
This command __validates__ proto files and __generate__ languages' specific gRPC files.
