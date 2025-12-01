# Railway Testing Guide

## After Deployment

Once your Railway deployment is live, use this guide to test all endpoints.

## Finding Your Railway URL

1. Go to https://railway.app
2. Click on your project
3. Click on the service
4. Go to "Settings" tab
5. Look for "Domains" section
6. Your URL will be: `https://lawmate-new.up.railway.app` (or similar)

## Health Check

### Test 1: Health Endpoint
```bash
curl https://YOUR_RAILWAY_URL/health
```

**Expected Response**:
```json
{"status": "healthy"}
```

### Test 2: Status Endpoint
```bash
curl https://YOUR_RAILWAY_URL/api/status
```

**Expected Response**:
```json
{
  "status": "running",
  "version": "1.0.0",
  "chroma_connected": true,
  "gemini_available": true
}
```

## Chat Endpoint Tests

### Test 3: Simple Chat Query
```bash
curl -X POST https://YOUR_RAILWAY_URL/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What is the Pakistani Constitution?",
    "mode": "detailed"
  }'
```

**Expected Response**:
```json
{
  "response": "The Pakistani Constitution is...",
  "sources": [
    {
      "title": "Constitution of Pakistan",
      "excerpt": "..."
    }
  ]
}
```

### Test 4: Yes/No Query
```bash
curl -X POST https://YOUR_RAILWAY_URL/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Is capital punishment legal in Pakistan?",
    "mode": "yes_no"
  }'
```

**Expected Response**:
```json
{
  "response": "Yes",
  "explanation": "Capital punishment is legal in Pakistan under...",
  "confidence": 0.95
}
```

### Test 5: Chat with History
```bash
curl -X POST https://YOUR_RAILWAY_URL/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Tell me more about that",
    "mode": "detailed",
    "include_history": true
  }'
```

## History Endpoints

### Test 6: Get Chat History
```bash
curl https://YOUR_RAILWAY_URL/api/history
```

**Expected Response**:
```json
{
  "history": [
    {
      "timestamp": "2025-01-15T10:30:00",
      "question": "What is the Pakistani Constitution?",
      "answer": "..."
    }
  ]
}
```

### Test 7: Clear History
```bash
curl -X DELETE https://YOUR_RAILWAY_URL/api/history/clear
```

**Expected Response**:
```json
{"message": "History cleared successfully"}
```

## PDF Generation

### Test 8: Generate PDF from History
```bash
curl -X POST https://YOUR_RAILWAY_URL/api/generate-pdf \
  -H "Content-Type: application/json" \
  -d '{}' \
  --output chat_history.pdf
```

**Expected**: PDF file downloaded

## Error Handling Tests

### Test 9: Invalid Query
```bash
curl -X POST https://YOUR_RAILWAY_URL/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": ""
  }'
```

**Expected Response** (400 error):
```json
{"detail": "Message cannot be empty"}
```

### Test 10: Server Error
```bash
curl https://YOUR_RAILWAY_URL/api/nonexistent
```

**Expected Response** (404 error):
```json
{"detail": "Not Found"}
```

## Performance Testing

### Test 11: Response Time
```bash
# Measure response time
time curl -X POST https://YOUR_RAILWAY_URL/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is the law?"}'
```

**Expected**: Response within 5-10 seconds

### Test 12: Concurrent Requests
```bash
# Test 5 concurrent requests
for i in {1..5}; do
  curl -X POST https://YOUR_RAILWAY_URL/api/chat \
    -H "Content-Type: application/json" \
    -d '{"message": "Test query '$i'"}' &
done
wait
```

## Monitoring in Railway

### View Logs
1. Go to Railway Dashboard
2. Click your service
3. Go to "Logs" tab
4. View real-time logs

### View Metrics
1. Go to Railway Dashboard
2. Click your service
3. Go to "Metrics" tab
4. Monitor:
   - CPU usage
   - Memory usage
   - Network I/O
   - Request count

### Check Deployment Status
1. Go to Railway Dashboard
2. Click your service
3. Go to "Deployments" tab
4. View deployment history

## Troubleshooting

### Service Returns 502 Bad Gateway
**Cause**: Service crashed or not responding
**Fix**:
1. Check logs for errors
2. Verify environment variables
3. Restart service in Railway Dashboard

### Slow Response Times
**Cause**: High CPU/Memory usage
**Fix**:
1. Check metrics
2. Optimize queries
3. Upgrade Railway plan

### ChromaDB Connection Error
**Cause**: Invalid credentials or network issue
**Fix**:
1. Verify CHROMA_API_KEY
2. Check CHROMA_TENANT_ID
3. Verify network connectivity

### CORS Errors
**Cause**: Frontend making requests from different domain
**Fix**:
1. Check CORS configuration in backend_api.py
2. Add frontend domain to allowed origins

## Automated Testing

### Using Python
```python
import requests

BASE_URL = "https://YOUR_RAILWAY_URL"

# Test health
response = requests.get(f"{BASE_URL}/health")
assert response.status_code == 200
print("✓ Health check passed")

# Test chat
response = requests.post(
    f"{BASE_URL}/api/chat",
    json={"message": "What is the law?"}
)
assert response.status_code == 200
print("✓ Chat endpoint passed")

# Test history
response = requests.get(f"{BASE_URL}/api/history")
assert response.status_code == 200
print("✓ History endpoint passed")

print("\n✅ All tests passed!")
```

### Using cURL Script
```bash
#!/bin/bash

BASE_URL="https://YOUR_RAILWAY_URL"

echo "Testing health endpoint..."
curl -f $BASE_URL/health || exit 1

echo "Testing status endpoint..."
curl -f $BASE_URL/api/status || exit 1

echo "Testing chat endpoint..."
curl -f -X POST $BASE_URL/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "test"}' || exit 1

echo "✅ All tests passed!"
```

## Checklist

- [ ] Health endpoint responds
- [ ] Status endpoint shows all systems OK
- [ ] Chat endpoint returns valid responses
- [ ] History endpoint works
- [ ] PDF generation works
- [ ] Error handling works
- [ ] Response times acceptable
- [ ] Logs show no errors
- [ ] Metrics look healthy
- [ ] Concurrent requests handled

## Next Steps

1. ✅ Deploy to Railway
2. ✅ Run all tests
3. ✅ Monitor metrics
4. ✅ Update documentation
5. ✅ Notify users of new URL
6. ✅ Decommission Render (optional)

## Support

- Railway Docs: https://docs.railway.app
- API Documentation: See API_DOCUMENTATION.md
- Issues: Check GitHub issues
