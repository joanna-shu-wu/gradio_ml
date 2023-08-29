# create a minimal linux image with Python 3.9 installed 
FROM python:3.9-slim

# create a working directory within the container
WORKDIR /app

# copy all files in the source directory to the working directory
COPY . .

# install all the requirements required for the model to serve predictions
RUN pip install -r requirements.txt

# run the command `python server.py` from within the container
CMD ["python", "server.py"]