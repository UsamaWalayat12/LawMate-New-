"""
Upload legal documents to Chroma Cloud
This script uploads sample legal documents to your Chroma Cloud database
"""
import os
import chromadb
from sentence_transformers import SentenceTransformer

print("=" * 70)
print("UPLOADING DOCUMENTS TO CHROMA CLOUD")
print("=" * 70)

# Get credentials
CHROMA_API_KEY = os.environ.get("CHROMA_API_KEY")
CHROMA_TENANT = os.environ.get("CHROMA_TENANT")
CHROMA_DATABASE = os.environ.get("CHROMA_DATABASE")

if not all([CHROMA_API_KEY, CHROMA_TENANT, CHROMA_DATABASE]):
    print("\n❌ ERROR: Missing environment variables!")
    print("Set these first:")
    print("  set CHROMA_API_KEY=your_key")
    print("  set CHROMA_TENANT=your_tenant")
    print("  set CHROMA_DATABASE=your_database")
    exit(1)

try:
    print("\n1. Connecting to Chroma Cloud...")
    client = chromadb.CloudClient(
        api_key=CHROMA_API_KEY,
        tenant=CHROMA_TENANT,
        database=CHROMA_DATABASE
    )
    print("   ✓ Connected")
    
    print("\n2. Creating/getting collection...")
    col = client.get_or_create_collection(name="pakistan_law")
    print("   ✓ Collection 'pakistan_law' ready")
    
    print("\n3. Loading embedding model...")
    model = SentenceTransformer("all-mpnet-base-v2")
    print("   ✓ Model loaded")
    
    # Sample Pakistani legal documents
    documents = [
        {
            "id": "doc_1",
            "text": """
            CONTRACT LAW IN PAKISTAN
            
            A contract is an agreement between two or more parties that creates legal obligations. 
            In Pakistan, contract law is governed by the Indian Contract Act, 1872.
            
            Key elements of a valid contract:
            1. Offer and Acceptance - One party makes an offer, the other accepts it
            2. Consideration - Something of value must be exchanged
            3. Intention to Create Legal Relations - Parties must intend to be legally bound
            4. Capacity - Parties must be legally capable (not minors, not of unsound mind)
            5. Legality - The contract must be for a legal purpose
            
            Breach of Contract:
            When one party fails to fulfill their obligations, it constitutes a breach of contract.
            The injured party can seek remedies including:
            - Damages (compensation for losses)
            - Specific Performance (court orders the breaching party to perform)
            - Rescission (cancellation of the contract)
            
            Types of Damages:
            1. Ordinary Damages - Direct losses from the breach
            2. Consequential Damages - Indirect losses resulting from the breach
            3. Liquidated Damages - Pre-agreed amount for breach
            4. Nominal Damages - Small amount when no actual loss occurred
            """,
            "metadata": {"topic": "contract_law", "lang": "en"}
        },
        {
            "id": "doc_2",
            "text": """
            PROPERTY TRANSFER IN PAKISTAN
            
            Property transfer is the process of transferring ownership of immovable property 
            (land and buildings) from one person to another.
            
            Legal Framework:
            - Transfer of Property Act, 1882
            - Registration Act, 1908
            - Land Revenue Act, 1967
            
            Steps for Property Transfer:
            
            1. AGREEMENT TO SELL
               - Buyer and seller agree on terms
               - Usually in writing
               - Not compulsory but recommended
            
            2. SALE DEED
               - Main document transferring ownership
               - Must be registered with Sub-Registrar
               - Contains details of property and parties
               - Stamp duty must be paid
            
            3. REGISTRATION
               - Registration is compulsory for immovable property
               - Provides legal evidence of ownership
               - Protects against fraud
               - Registered with Sub-Registrar's office
            
            4. POSSESSION
               - Physical possession of property
               - Buyer takes possession after registration
               - Seller vacates the property
            
            Documents Required:
            - Original title deeds
            - CNIC of buyer and seller
            - NOC from relevant authorities
            - Tax clearance certificate
            - Affidavit (if needed)
            
            Costs Involved:
            - Stamp duty (varies by province)
            - Registration fee
            - Lawyer's fee
            - Survey charges (if needed)
            """,
            "metadata": {"topic": "property_transfer", "lang": "en"}
        },
        {
            "id": "doc_3",
            "text": """
            LEGAL NOTICE IN PAKISTAN
            
            A legal notice is a formal written communication sent before initiating legal proceedings.
            It serves as a warning and gives the other party a chance to comply.
            
            Purpose of Legal Notice:
            1. Inform the other party of their breach or violation
            2. Demand compliance or compensation
            3. Create evidence of communication
            4. Demonstrate good faith before litigation
            5. Sometimes required by law before filing a case
            
            Contents of a Legal Notice:
            
            1. HEADER
               - Sender's name and address
               - Recipient's name and address
               - Date
            
            2. SUBJECT LINE
               - "LEGAL NOTICE" or "NOTICE OF DEMAND"
            
            3. BODY
               - Description of the issue
               - Reference to relevant laws
               - Specific demands
               - Consequences of non-compliance
            
            4. TIMELINE
               - Usually 7-30 days to comply
               - Depends on nature of issue
            
            5. SIGNATURE
               - Sender's signature
               - Lawyer's signature (if sent through lawyer)
            
            Types of Legal Notices:
            - Demand Notice (for payment or performance)
            - Termination Notice (to end contract)
            - Defamation Notice (for false statements)
            - Eviction Notice (to vacate property)
            - Cease and Desist Notice (to stop illegal activity)
            
            Legal Effect:
            - Creates documentary evidence
            - Shows attempt at settlement
            - May be required before filing suit
            - Can be used as evidence in court
            - Strengthens your case if recipient ignores it
            """,
            "metadata": {"topic": "legal_notice", "lang": "en"}
        },
        {
            "id": "doc_4",
            "text": """
            EMPLOYMENT LAW IN PAKISTAN
            
            Employment law in Pakistan is governed by various laws protecting workers' rights 
            and regulating employer-employee relationships.
            
            Key Laws:
            1. Industrial Relations Act, 2012
            2. Factories Act, 1934
            3. Shops and Establishments Ordinance, 1969
            4. Workmen's Compensation Act, 1923
            5. Minimum Wages Ordinance, 1961
            
            Employee Rights:
            
            1. RIGHT TO FAIR WAGES
               - Minimum wage as per law
               - Timely payment of salary
               - Overtime compensation
            
            2. WORKING HOURS
               - Maximum 48 hours per week
               - One day rest per week
               - Paid leave (annual, sick, casual)
            
            3. SAFE WORKING CONDITIONS
               - Safe workplace
               - Proper ventilation and lighting
               - Safety equipment
               - First aid facilities
            
            4. PROTECTION FROM HARASSMENT
               - No sexual harassment
               - No discrimination
               - No forced labor
            
            5. TERMINATION PROTECTION
               - Notice period required
               - Severance pay
               - Gratuity benefits
               - Unemployment benefits
            
            Employer Obligations:
            - Maintain safe workplace
            - Pay minimum wages
            - Provide leave
            - Maintain records
            - Comply with labor laws
            - Provide social security
            
            Remedies for Violations:
            - Complaint to labor department
            - Claim before labor court
            - Compensation for damages
            - Reinstatement of job
            """,
            "metadata": {"topic": "employment_law", "lang": "en"}
        },
        {
            "id": "doc_5",
            "text": """
            BREACH OF CONTRACT - REMEDIES AND PROCEDURES
            
            When a party fails to perform their contractual obligations, the injured party 
            has several remedies available under Pakistani law.
            
            Types of Breach:
            
            1. MATERIAL BREACH
               - Substantial failure to perform
               - Goes to the heart of the contract
               - Allows other party to terminate
            
            2. MINOR BREACH
               - Partial or incomplete performance
               - Doesn't go to the heart of contract
               - Other party must still perform
            
            3. ANTICIPATORY BREACH
               - Party indicates they won't perform
               - Before performance is due
               - Other party can sue immediately
            
            Available Remedies:
            
            1. DAMAGES
               - Monetary compensation
               - Calculated based on actual losses
               - Must be reasonably foreseeable
               - Types: ordinary, consequential, liquidated, nominal
            
            2. SPECIFIC PERFORMANCE
               - Court orders breaching party to perform
               - Available when damages are inadequate
               - Common in property disputes
               - Not available for personal services
            
            3. RESCISSION
               - Cancellation of contract
               - Returns parties to original position
               - Requires restitution of benefits
            
            4. INJUNCTION
               - Court order to stop certain action
               - Prevents further breach
               - Can be temporary or permanent
            
            Procedure for Claiming Breach:
            
            1. SEND LEGAL NOTICE
               - Formal demand for compliance
               - Usually 7-30 days to respond
               - Creates evidence of breach
            
            2. FILE SUIT
               - If notice is ignored
               - In appropriate court
               - With all supporting documents
            
            3. EVIDENCE PRESENTATION
               - Contract document
               - Proof of breach
               - Proof of damages
               - Witness testimony
            
            4. JUDGMENT
               - Court decides the case
               - Awards appropriate remedy
               - May award costs and interest
            
            Limitation Period:
            - Generally 3 years from breach
            - Can be extended in certain circumstances
            - Starts from date of breach
            """,
            "metadata": {"topic": "breach_of_contract", "lang": "en"}
        }
    ]
    
    print(f"\n4. Uploading {len(documents)} documents...")
    
    # Generate embeddings and add documents
    ids = []
    texts = []
    metadatas = []
    
    for doc in documents:
        ids.append(doc["id"])
        texts.append(doc["text"])
        metadatas.append(doc["metadata"])
    
    # Generate embeddings
    embeddings = model.encode(texts, convert_to_numpy=True).tolist()
    
    # Add to collection
    col.add(
        ids=ids,
        documents=texts,
        metadatas=metadatas,
        embeddings=embeddings
    )
    
    print(f"   ✓ Uploaded {len(documents)} documents")
    
    # Verify
    count = col.count()
    print(f"\n5. Verification:")
    print(f"   ✓ Collection now has {count} documents")
    
    print("\n" + "=" * 70)
    print("✅ SUCCESS: Documents uploaded to Chroma Cloud!")
    print("=" * 70)
    print("\nYour chatbot should now be able to answer questions about:")
    print("  - Contract law and breach of contract")
    print("  - Property transfer procedures")
    print("  - Legal notices")
    print("  - Employment law")
    print("  - Remedies for breach of contract")
    
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
