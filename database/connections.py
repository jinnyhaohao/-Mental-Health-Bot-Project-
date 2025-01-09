from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:5137/")  # Replace with your MongoDB URI if hosted remotely.

# Access the database
db = client["mental_health_app"]

# Access a collection
collection = db["users"]

# Insert a document
user_document = {
    "name": "John Doe",
    "age": 30,
    "mood": "Positive"
}

result = collection.insert_one(user_document)
print(f"Document inserted with ID: {result.inserted_id}")

# Query the collection
for user in collection.find():
    print(user)

# Close the connection
client.close()
