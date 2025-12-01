  
  /// Get the appropriate server URL based on platform and build mode
  static String get baseUrl {
    if (useProductionServer) {
      // Use Vercel production server for 24/7 availability
      return _vercelUrl;
    } else if (kIsWeb) {
      // Web builds can use localhost
      return 'http://$_devServerHost:$_serverPort';
    } else if (kDebugMode && (Platform.isAndroid || Platform.isIOS)) {
      // Mobile debug builds need the computer's IP address
      return 'http://$_mobileServerHost:$_serverPort';
    } else {
      // Desktop or release builds
      return 'http://$_devServerHost:$_serverPort';
    }
  }
  
  /// Get the server host for display purposes
  static String get serverHost {
    if (useProductionServer) {
      return _vercelUrl.replaceAll('https://', '').replaceAll('http://', '');
    } else if (kIsWeb) {
      return _devServerHost;
    } else if (kDebugMode && (Platform.isAndroid || Platform.isIOS)) {
      return _mobileServerHost;
    } else {
      return _devServerHost;
    }
  }
  
  /// Get the server port
  static int get serverPort => _serverPort;
  
  /// Check if we're running on mobile in debug mode
  static bool get isMobileDebug {
    return kDebugMode && (Platform.isAndroid || Platform.isIOS);
  }
  
  /// Get connection instructions for current platform
  static String get connectionInstructions {
    final serverType = useRealAI ? "Real AI Server (Python + Gemini)" : "Sample Server (Node.js)";
    final deploymentType = useProductionServer ? "Vercel (24/7)" : "Local Development";
    
    if (useProductionServer) {
      return '''
Server Type: $serverType
Deployment: $deploymentType

✅ Your AI Assistant is running 24/7 on Vercel!

Features:
- Global availability from anywhere
- Automatic HTTPS security
- Fast response times
- No setup required for users

Current server URL: $baseUrl
''';
    } else if (isMobileDebug) {
      return '''
Server Type: $serverType
Deployment: $deploymentType

To connect from mobile device:
1. Make sure your computer and mobile device are on the same WiFi network
2. Find your computer's IP address:
   - Windows: Run 'ipconfig' in Command Prompt
   - Mac/Linux: Run 'ifconfig' in Terminal
3. Update _mobileServerHost in server_config.dart with your IP
4. Start the backend server: python backend_api.py
5. Rebuild and run the app

Current server URL: $baseUrl
''';
    } else {
      return '''
Server Type: $serverType
Deployment: $deploymentType

Desktop/Web connection:
1. Start the backend server: python backend_api.py
2. The app will connect to: $baseUrl

Current server URL: $baseUrl
''';
    }
  }
}

import 'dart:io';
import 'package:flutter/foundation.dart';