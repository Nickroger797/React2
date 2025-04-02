# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the code to the container
COPY . .

# Set environment variables for the bot
ENV BOT_TOKEN="your_bot_token_here"
ENV OWNER_CHAT_ID="your_owner_chat_id_here"
ENV MONGODB_URI="your_mongodb_uri_here"
ENV LOGGING_LEVEL="INFO"

# Expose the port (optional, depends on bot's config)
EXPOSE 5000

# Command to run the bot
CMD ["python", "bot.py"]
