# VS Code Azure App Services Extension - Deployment Guide

## Quick Start Steps

### 1. Verify Installation and Login
- ✅ You have the Azure App Services extension installed
- ✅ You are already logged into your Azure account
- Look for the **Azure** icon in the left sidebar (looks like a mountain)

### 2. Create an App Service

**Method A: Using the Explorer Button**

1. Click the **Azure icon** in the left sidebar
2. In the explorer, you'll see **AZURE** section
3. Expand **RESOURCES** → **Microsoft Azure Enterprise** → Click **+** next to "App Services"
4. A wizard will appear asking for:
   - **App name**: Enter a unique name (e.g., `myflaskapp123`)
   - **Runtime**: Select **Python**
   - **Python version**: Select **3.9** or **3.11**
   - **Resource group**: Create new or select existing
   - **Region**: Select closest to you (e.g., `East US`, `West Europe`)
5. Click **Create** and wait (this takes 2-3 minutes)

**Method B: Using Command Palette**

1. Press **Ctrl+Shift+P** (or **Cmd+Shift+P** on Mac)
2. Type: `Azure App Services: Create New Web App`
3. Follow the same prompts as above

### 3. Deploy Your Flask Application

**Method A: Right-Click Deploy (Easiest)**

1. In the Azure explorer, expand **App Services**
2. Find your newly created app service
3. **Right-click** on it
4. Select **Deploy to Web App**
5. Choose the folder: `/home/azureuser/azureappservices`
6. VS Code will ask for confirmation - click **Deploy** or press Enter
7. Watch the output panel for progress

**Method B: Command Palette**

1. Press **Ctrl+Shift+P**
2. Type: `Azure App Services: Deploy to Web App`
3. Select your App Service from the list
4. Choose the workspace folder
5. Confirm deployment

### 4. Monitor Deployment Progress

- Look at the **Output** panel (or press **Ctrl+J**)
- You'll see logs like:
  ```
  Deploying to myflaskapp123...
  Building...
  Installing dependencies...
  Starting application...
  ```

### 5. Access Your App

Once deployed (you'll see a success message):
- Your app URL: `https://myflaskapp123.azurewebsites.net`
- Test it by visiting this URL in your browser

## Testing Your Deployment

After deployment, test these URLs:

1. **Home Page**: `https://myflaskapp123.azurewebsites.net/`
   - Shows server time, environment, and available endpoints

2. **API Endpoints**:
   - `/api/hello` - Returns JSON greeting
   - `/api/status` - Returns service status
   - `/api/config` - Returns app configuration

## Viewing Logs

To see application logs and debug issues:

1. **Stream logs live**:
   - Right-click your App Service
   - Select **Stream Logs**
   - Logs will appear in real-time as requests come in

2. **View Application Insights**:
   - Right-click your App Service
   - Select **View in Portal**
   - In Azure Portal, go to **Logs** or **Application Insights**

## Updating Your App

To deploy updates after code changes:

1. Edit your code locally (e.g., modify `app.py`)
2. Right-click your App Service again
3. Select **Deploy to Web App**
4. Confirm
5. Wait for deployment to complete

## Restarting Your App Service

If your app isn't responding:

1. Right-click your App Service
2. Select **Restart** (if available)
3. Or go to **View in Portal** → Click **Restart** button

## Setting Environment Variables

For production configuration:

1. Right-click your App Service
2. Select **View Properties** or **Open in Portal**
3. Go to **Settings** → **Configuration**
4. Under **Application settings**, add new settings:
   - **Name**: `FLASK_ENV`
   - **Value**: `production`
5. Click **Save**

## Troubleshooting

### Issue: Deployment fails with "Module not found"
- **Solution**: Ensure `requirements.txt` is in the root folder with all dependencies listed

### Issue: App shows 500 error after deployment
- **Solution**: 
  - Stream the logs to see the error message
  - Check if Python version is correct
  - Verify startup command in Configuration settings

### Issue: App takes too long to start
- **Solution**: 
  - In Portal → Configuration → Startup Command
  - Make sure it's set correctly (should use gunicorn for Python)
  - Or add: `python -m gunicorn --workers 4 --timeout 600 app:app`

### Issue: Cannot see logs
- **Solution**: 
  - Right-click App Service → **Stream Logs**
  - Or view in Portal → **Log stream** or **Application Insights**

## VS Code Keyboard Shortcuts

- **Open Azure explorer**: Click the Azure icon (left sidebar)
- **Open Command Palette**: `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
- **Deploy quickly**: Ctrl+K Ctrl+O → Select App Service

## Next Steps

- Monitor your app's performance in Azure Portal
- Set up continuous deployment from Git (right-click App Service → Configure deployment)
- Add custom domain name (in Azure Portal → Custom domains)
- Enable HTTPS/SSL certificates (automatic with `.azurewebsites.net` domain)

## Getting Help

1. **In VS Code**: Right-click App Service → **Help**
2. **Azure Portal**: Your App Service resource page has all settings and monitoring
3. **Output Panel**: All deployment logs are visible here
