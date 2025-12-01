"""
Upload local ChromaDB data to Chroma Cloud
"""
import chromadb
from tqdm import tqdm

print("=" * 60)
print("ChromaDB to Chroma Cloud Migration")
print("=" * 60)

# Connect to local ChromaDB
print("\n1. Connecting to local ChromaDB...")
try:
    local_client = chromadb.PersistentClient(path="ChromaDB")
    local_collection = local_client.get_collection("pakistan_law")
    print(f"   ✓ Connected to local database")
except Exception as e:
    print(f"   ✗ Error: {e}")
    exit(1)

# Connect to Chroma Cloud
print("\n2. Connecting to Chroma Cloud...")
try:
    cloud_client = chromadb.CloudClient(
        api_key='ck-WN7siQucBorxSYYta76sUbAzMbnFCuk8GiMXcdYgsnd',
        tenant='632db25e-e86a-4b90-808a-a221877d15d1',
        database='Law-Mate'
    )
    print(f"   ✓ Connected to Chroma Cloud")
except Exception as e:
    print(f"   ✗ Error: {e}")
    exit(1)

# Create or get collection in cloud
print("\n3. Creating collection in cloud...")
try:
    # Try to get existing collection first
    try:
        cloud_collection = cloud_client.get_collection("pakistan_law")
        print(f"   ✓ Found existing collection")
    except:
        # Create new collection if it doesn't exist
        cloud_collection = cloud_client.create_collection("pakistan_law")
        print(f"   ✓ Created new collection")
except Exception as e:
    print(f"   ✗ Error: {e}")
    exit(1)

# Get all data from local
print("\n4. Fetching data from local database...")
try:
    all_data = local_collection.get()
    total = len(all_data['ids'])
    print(f"   ✓ Found {total} documents to upload")
except Exception as e:
    print(f"   ✗ Error: {e}")
    exit(1)

# Upload to cloud in batches
print("\n5. Uploading to Chroma Cloud...")
batch_size = 5  # VERY small batches to avoid timeout (was 50)
uploaded = 0
failed_batches = []

import time

try:
    for i in tqdm(range(0, total, batch_size), desc="Uploading"):
        end = min(i + batch_size, total)
        
        batch_data = {
            'ids': all_data['ids'][i:end],
            'documents': all_data['documents'][i:end] if all_data['documents'] else None,
        }
        
        # Add optional fields if they exist
        if all_data.get('metadatas'):
            batch_data['metadatas'] = all_data['metadatas'][i:end]
        if all_data.get('embeddings'):
            batch_data['embeddings'] = all_data['embeddings'][i:end]
        
        # Retry logic for network errors
        max_retries = 3
        for attempt in range(max_retries):
            try:
                cloud_collection.add(**batch_data)
                uploaded = end
                break  # Success, exit retry loop
            except Exception as batch_error:
                if attempt < max_retries - 1:
                    print(f"\n   Retry {attempt + 1}/{max_retries} for batch {i}-{end}...")
                    time.sleep(2)  # Wait before retry
                else:
                    print(f"\n   ✗ Failed batch {i}-{end} after {max_retries} attempts: {batch_error}")
                    failed_batches.append((i, end))
        
        # Small delay between batches to avoid overwhelming the server
        time.sleep(0.5)
        
    if failed_batches:
        print(f"\n   ⚠️  Uploaded {uploaded}/{total} documents with {len(failed_batches)} failed batches")
        print(f"   Failed batches: {failed_batches}")
    else:
        print(f"\n   ✓ Successfully uploaded {uploaded}/{total} documents!")
    
except Exception as e:
    print(f"\n   ✗ Error at document {uploaded}: {e}")
    print(f"   Uploaded {uploaded}/{total} documents before error")
    exit(1)

print("\n" + "=" * 60)
print("Migration Complete!")
print("=" * 60)
print(f"\nUploaded {uploaded} documents to Chroma Cloud")
print("\nNext steps:")
print("1. Set environment variables on Railway")
print("2. Deploy: railway up")
print("3. Test your chatbot!")
