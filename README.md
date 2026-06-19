# Azure Flask App - Deployment Guide

This is a sample Python Flask application configured for deployment to Azure App Services.

## Project Structure

```
azureappservices/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── web.config          # Azure App Services configuration
├── .gitignore          # Git ignore rules
└── startup_commands.txt # Optional startup commands reference
```

## Prerequisites

- Python 3.8 or higher
- VS Code with Azure App Services extension installed
- Azure account with an active subscription
- Already logged in to Azure via VS Code

## Local Development

### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application locally
```bash
python app.py
```

The app will be available at `http://localhost:5000`

## Deployment to Azure App Services

### Option 1: Using VS Code Azure App Services Extension (Recommended)

1. **Open the Azure view** in VS Code (click the Azure icon in the left sidebar)

2. **In the App Services section:**
   - Click the **+** button to create a new App Service
   - Or right-click on "App Services" and select "Create New Web App"

3. **Follow the prompts:**
   - Enter a unique name for your app (e.g., `myflaskapp-1234`)
   - Select **Python** as the runtime stack
   - Choose **Python 3.9** or higher
   - Select the resource group and region
   - Wait for the App Service to be created

4. **Deploy your code:**
   - Right-click on your newly created App Service in the explorer
   - Select **Deploy to Web App**
   - Choose the local folder (`/home/azureuser/azureappservices`)
   - Click **Deploy** to start the deployment process

5. **Monitor the deployment:**
   - You'll see deployment progress in the Output panel
   - Wait for the message confirming successful deployment

### Option 2: Quick Deploy from Command Palette

1. Open Command Palette (Ctrl+Shift+P)
2. Type "Azure App Services: Deploy to Web App"
3. Select the target App Service
4. Choose the workspace folder
5. Confirm deployment

## Testing After Deployment

Once deployed, your Flask app will be available at:
```
https://<your-app-name>.azurewebsites.net
```

Test these endpoints:
- Home page: `https://<your-app-name>.azurewebsites.net/`
- API Hello: `https://<your-app-name>.azurewebsites.net/api/hello`
- Status: `https://<your-app-name>.azurewebsites.net/api/status`
- Config: `https://<your-app-name>.azurewebsites.net/api/config`

## Environment Variables

To set environment variables in Azure App Services:

1. In VS Code, right-click the App Service
2. Select **View Properties** or go to Azure Portal
3. Navigate to Configuration → Application settings
4. Add new settings:
   - `FLASK_ENV`: Set to `production`
   - `PORT`: Set to `8000` (or Azure will use default)

## Troubleshooting

### Check deployment logs:
1. Right-click your App Service
2. Select **View Logs in Portal** or **Stream Logs**

### Common issues:
- **Module not found**: Ensure requirements.txt is in the root directory
- **Port binding**: Azure automatically assigns a PORT environment variable
- **Startup timeout**: Check web.config startupTimeLimit value

## Dependencies Added

- **Flask 3.0.0**: Web framework
- **Werkzeug 3.0.1**: WSGI utilities (dependency of Flask)

The application includes error handling and returns JSON responses for API endpoints.
