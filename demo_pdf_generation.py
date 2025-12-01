"""
Demo script to test PDF generation without needing full RAG setup
"""
import json
import os

# Create a sample chat history for testing
sample_history = [
    {
        "role": "user",
        "content": "I need to draft a breach of contract notice. The contract was dated January 15, 2024 between Ahmad Khan and Bilal Ahmed. Payment of PKR 500,000 was due on February 1, 2024 but remains unpaid."
    },
    {
        "role": "assistant",
        "content": "I can help you draft a breach of contract notice. Based on the information provided, this is a case of non-payment constituting breach of contract under Pakistani law..."
    },
    {
        "role": "user",
        "content": "Please include that the payment was for supply of merchandise and the breach has caused significant financial loss."
    },
    {
        "role": "assistant",
        "content": "Understood. I'll include those details in the notice. The breach relates to non-payment for merchandise supply, and you've suffered financial loss as a result..."
    }
]

# Save sample history
with open("chat_history.json", "w", encoding="utf-8") as f:
    json.dump(sample_history, f, ensure_ascii=False, indent=2)

print("✓ Sample chat history created!")
print("\nSample conversation:")
print("-" * 50)
for msg in sample_history:
    print(f"\n{msg['role'].upper()}: {msg['content'][:100]}...")

print("\n" + "=" * 50)
print("\nNow you can test PDF generation:")
print("  python chroma_test.py --generate-pdf")
print("\nOr view the history:")
print("  python chroma_test.py --show-history")
print("\n" + "=" * 50)
