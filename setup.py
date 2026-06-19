#!/usr/bin/env python
"""
Local setup and testing script for Azure Flask App
Run this to set up and test the application locally before deployment
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(cmd, description):
    """Run a shell command and handle errors"""
    print(f"\n{'='*60}")
    print(f"📌 {description}")
    print(f"{'='*60}")
    print(f"Running: {cmd}\n")
    
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"\n❌ Error: {description} failed")
        return False
    print(f"\n✅ {description} completed successfully")
    return True

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    print(f"\n📌 Python Version Check")
    print(f"{'='*60}")
    print(f"Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Error: Python 3.8 or higher is required")
        return False
    print("✅ Python version is compatible")
    return True

def main():
    print("\n" + "="*60)
    print("🚀 Azure Flask App - Local Setup Script")
    print("="*60)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check if requirements.txt exists
    if not Path("requirements.txt").exists():
        print("\n❌ Error: requirements.txt not found")
        sys.exit(1)
    
    # Create virtual environment
    venv_path = "venv"
    if not Path(venv_path).exists():
        run_command(f"{sys.executable} -m venv {venv_path}", 
                   "Creating virtual environment")
    
    # Determine pip path
    if sys.platform == "win32":
        pip_cmd = f"{venv_path}\\Scripts\\pip"
        python_cmd = f"{venv_path}\\Scripts\\python"
        activate_cmd = f"{venv_path}\\Scripts\\activate"
    else:
        pip_cmd = f"{venv_path}/bin/pip"
        python_cmd = f"{venv_path}/bin/python"
        activate_cmd = f"source {venv_path}/bin/activate"
    
    # Upgrade pip
    run_command(f"{pip_cmd} install --upgrade pip", "Upgrading pip")
    
    # Install requirements
    run_command(f"{pip_cmd} install -r requirements.txt", 
               "Installing Python dependencies")
    
    # Run the app
    print(f"\n" + "="*60)
    print(f"📌 Starting Flask Application")
    print(f"{'='*60}")
    print(f"To activate virtual environment, run:")
    print(f"  {activate_cmd}")
    print(f"\nThen run the app:")
    print(f"  {python_cmd} app.py")
    print(f"\nThe app will be available at: http://localhost:5000")
    print(f"{'='*60}\n")
    
    # Ask if user wants to start the app
    response = input("Do you want to start the app now? (yes/no): ").strip().lower()
    if response in ['yes', 'y']:
        run_command(f"{python_cmd} app.py", "Running Flask application")

if __name__ == "__main__":
    main()
