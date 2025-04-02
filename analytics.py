from datetime import datetime

# Log user actions
async def log_user_action(user_id, action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"User {user_id} performed action: {action} at {timestamp}")
