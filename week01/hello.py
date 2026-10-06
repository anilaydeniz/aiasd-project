# Anıl Aydeniz - Student ID: 220504045
# AI-Assisted Software Development (AIASD) - Week 01

user_name = input("Enter your name to start today's development log: ")

tasks = [
    "Review Transformer architecture paper",
    "Configure Git environment and SSH credentials",
    "Build initial mobile/web project proposal",
    "Prepare weekly AI prompt log reflection",
]

print(f"\nWelcome back, {user_name}! Here are your key focus areas for this week:")
for index, task in enumerate(tasks, start=1):
    print(f"[{index}] {task}")
