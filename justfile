# Command to generate proto files for supported languages(Python)
gen-all:
  # Linting proto files
  buf lint proto
  # Generating grpc files
  buf generate proto
