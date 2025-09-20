FROM python:3.11-slim
   
   WORKDIR /app
   
   # Copy requirements first for better caching
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   
   # Copy the rest of your application
   COPY . .
   
   # Expose the port your app runs on
   EXPOSE 80
   
   # Command to run your application
   CMD ["python", "WEBSCRAPER.py"]