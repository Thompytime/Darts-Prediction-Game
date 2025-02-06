# Use an official Python runtime
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Run the app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
