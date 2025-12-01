# Vercel Deployment with Chroma Cloud

## Railway Failed - Using Vercel Instead

Railway deployments kept failing with dependency conflicts. Vercel is better for Python serverless APIs.

## Prerequisites

1. **Install Vercel CLI:**
```bash
npm install -g vercel
```

2. **Login to Vercel:**
```bash
vercel login
```

## Deployment Steps

### 1. Set Environment Variables

```bash
vercel env add CHROMA_API_KEY
# Paste: ck-WN7siQucBorxSYYta76sUbAzMbnFCuk8GiMXcdYgsnd

vercel env add CHROMA_TENANT  
# Paste: 632db25e-e86a-4b90-808a-a221877d15d1

vercel env add CHROMA_DATABASE
# Paste: Law-Mate

vercel env add GEMINI_API_KEY
# Paste: AIzaSyBO7g1SWj-fxSsWIxslHsK7zrjfSPfhoG8
```

### 2. Deploy

```bash
cd c:\Users\AHMAD\Desktop\New
vercel --prod
```

### 3. Get Your URL

After deployment, Vercel will give you a URL like:
```
https://your-project.vercel.app
```

### 4. Test

```bash
curl https://your-project.vercel.app/health
```

## Update Flutter App

Edit `lib/config/server_config.dart`:
```dart
static const String _productionServerUrl = 'https://your-project.vercel.app';
static const bool useProductionServer = true;
```

## Why Vercel Instead of Railway?

- ✅ Better for Python serverless functions
- ✅ Faster deployments
- ✅ Better dependency handling
- ✅ Free tier available
- ✅ Automatic HTTPS

## Troubleshooting

If deployment fails:
1. Check Vercel logs: `vercel logs`
2. Verify environment variables: `vercel env ls`
3. Test locally: `vercel dev`
