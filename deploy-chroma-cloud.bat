@echo off
echo ================================================
echo Setting Chroma Cloud Variables on Railway
echo ================================================
echo.

echo Setting CHROMA_API_KEY...
railway variables --kv CHROMA_API_KEY=ck-WN7siQucBorxSYYta76sUbAzMbnFCuk8GiMXcdYgsnd

echo Setting CHROMA_TENANT...
railway variables --kv CHROMA_TENANT=632db25e-e86a-4b90-808a-a221877d15d1

echo Setting CHROMA_DATABASE...
railway variables --kv CHROMA_DATABASE=Law-Mate

echo.
echo ================================================
echo Variables Set! Now deploying...
echo ================================================
echo.

railway up

echo.
echo ================================================
echo Deployment Complete!
echo ================================================
echo.
echo Your chatbot should now work with Chroma Cloud!
echo Test in your mobile app.
echo.
pause
