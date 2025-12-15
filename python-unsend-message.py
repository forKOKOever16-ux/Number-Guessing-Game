# Unsend Message Simulation using seek() and truncate()

# Create and write the original sent message
sent_message = 'Hey there! This is a secret message.'

with open('sent_message.txt', 'w') as file:
    file.write(sent_message)

# Read, seek, modify, and truncate the message
# All file operations are handled inside this block
with open('sent_message.txt', 'r+') as file:
    # 1️⃣ Read the original message
    original_message = file.read()

    # 2️⃣ Move the cursor back to the beginning of the file
    file.seek(0)

    # 3️⃣ New message to simulate "unsending"
    unsent_message = 'This message has been unsent.'

    # 4️⃣ Overwrite the original message
    file.write(unsent_message)

    # 5️⃣ Remove any leftover text from the original message
    file.truncate(len(unsent_message))

# Display results
print('Original Message:', original_message)
print('Unsent Message:', unsent_message)
