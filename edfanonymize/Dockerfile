# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install build tools (for gcc)
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

# Copy the C source file and compile it
COPY . .
RUN gcc edf-anonymize.c -o edf-anonymize

# Create default input/output folders
RUN mkdir /app/input /app/output

# Set the default command to run the script using the compiled binary
CMD ["python", "batch_deid.py", "./edf-anonymize"]
