# 🚂 Railway Deployment Guide - 24/7 AI Assistant

## 🎯 Overview
Deploy your Pakistani Legal AI Assistant to Railway for 24/7 global availability.

---

## 📋 **Step-by-Step Deployment**

### **Step 1: Prepare Your Files**
✅ All deployment files are ready:
- `Dockerfile` - Container configuration
- `requirements.txt` - Python dependencies
- `railway.json` - Railway configuration
- `.env.example` - Environment variables template

### **Step 2: Create Railway Account**
1. Go to [railway.app](https://railway.app)
2. Click "Start a New Project"
3. Sign up with GitHub (recommended)

### **Step 3: Create New Project**
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Connect your GitHub account
4. Upload your project files to GitHub first (or use Railway CLI)

### **Step 4: Alternative - Deploy via CLI**

#### Install Railway CLI:
```bash
# Windows (using npm)
npm install -g @railway/cli

# Or download from: https://railway.app/cli
```

#### Deploy:
```bash
# Login to Railway
railway login

# Initialize project
railway init

# Set environment variables
railway variables set GEMINI_API_KEY=your_actual_api_key_here

# Deploy
railway up
```

### **Step 5: Configure Environment Variables**
In Railway dashboard, go to Variables and add:
```
GEMINI_API_KEY=your_google_gemini_api_key
PORT=8000
HOST=0.0.0.0
ENVIRONMENT=production
```

### **Step 6: Deploy and Get URL**
1. Railway will automatically build and deploy
2. You'll get a URL like: `https://your-app-name.railway.app`
3. Test the deployment: `https://your-app-name.railway.app/health`

---

## 🔧 **Manual Deployment (Without GitHub)**

### **Option A: Railway CLI**
```bash
# 1. Install Railway CLI
npm install -g @railway/cli

# 2. Login
railway login

# 3. Initialize in your project directory
railway init

# 4. Set environment variables
railway variables set GOOGLE_API_KEY=your_api_key_here

# 5. Deploy
railway up
```

### **Option B: GitHub Integration**
1. Create GitHub repository
2. Upload all your files to GitHub
3. Connect Railway to your GitHub repo
4. Automatic deployment on every push

---

## 🌍 **Update Flutter App for Production**

Once deployed, update your Flutter app:

### **Step 1: Update Server Configuration**
Edit `lib/config/server_config.dart`:
```dart
class ServerConfig {
  // Production server URL (replace with your Railway URL)
  static const String _productionServerUrl = 'https://your-app-name.railway.app';
  
  // Development server configuration
  static const String _devServerHost = 'localhost';
  static const int _serverPort = 8000;
  
  // Mobile server configuration
  static const String _mobileServerHost = '192.168.0.103';
  
  // AI Server Type
  static const bool useRealAI = true;
  static const bool useProductionServer = true; // Set to true for production
  
  /// Get the appropriate server URL
  static String get baseUrl {
    if (useProductionServer) {
      return _productionServerUrl;
    } else if (kIsWeb) {
      return 'http://$_devServerHost:$_serverPort';
    } else if (kDebugMode && (Platform.isAndroid || Platform.isIOS)) {
      return 'http://$_mobileServerHost:$_serverPort';
    } else {
      return 'http://$_devServerHost:$_serverPort';
    }
  }
}
```

### **Step 2: Build Production APK**
```bash
cd New-Legal-Connect
flutter clean
flutter pub get
flutter build apk --release
```

---

## ✅ **Verification Steps**

### **Test Your Deployment:**
1. **Health Check**: `https://your-app-name.railway.app/health`
2. **API Docs**: `https://your-app-name.railway.app/docs`
3. **Chat Test**: Send POST to `/api/chat` with a legal question

### **Test Flutter App:**
1. Install APK on mobile device
2. Open AI Assistant
3. Ask: "What is a contract in Pakistani law?"
4. Should get intelligent AI response

---

## 💰 **Railway Pricing**
- **Hobby Plan**: $5/month
- **Pro Plan**: $20/month
- **Free Trial**: Available for testing

---

## 🚀 **Benefits of Railway Deployment**

### **For You:**
✅ **24/7 Availability** - Server never goes down  
✅ **Global Access** - Users can access from anywhere  
✅ **Automatic Scaling** - Handles multiple users  
✅ **HTTPS Security** - Secure connections  
✅ **Easy Updates** - Deploy new versions easily  

### **For Your Users:**
✅ **Always Available** - AI assistant works anytime  
✅ **Fast Responses** - Global CDN for speed  
✅ **Reliable Service** - Professional hosting  
✅ **No Network Restrictions** - Works on any internet connection  

---

## 🛠️ **Troubleshooting**

### **Deployment Fails:**
- Check `requirements.txt` has all dependencies
- Verify `GOOGLE_API_KEY` is set correctly
- Check Railway logs for error messages

### **App Can't Connect:**
- Verify Railway URL is correct in Flutter app
- Check if Railway service is running
- Test API endpoints manually

### **AI Responses Not Working:**
- Verify Google API key is valid
- Check if ChromaDB files are included
- Review Railway logs for AI errors

---

## 🎉 **Success!**

Once deployed, your AI Assistant will be:
- ✅ **Available 24/7** from anywhere in the world
- ✅ **Professionally hosted** on Railway infrastructure
- ✅ **Scalable** to handle multiple users
- ✅ **Secure** with HTTPS encryption

Your users can now access intelligent Pakistani legal advice anytime, anywhere! 🤖⚖️

---

## 📞 **Next Steps**

1. **Deploy to Railway** using the steps above
2. **Update Flutter app** with production URL
3. **Test thoroughly** on multiple devices
4. **Share with users** - they can access 24/7!
5. **Monitor usage** via Railway dashboard

**Ready to deploy? Follow the steps above and your AI Assistant will be live in 30 minutes!** 🚀