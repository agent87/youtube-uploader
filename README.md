YouTube Uploader CLI Tool
Overview
The YouTube Uploader is a Python 2 script designed to simplify the process of uploading machine learning model output videos, particularly those generated in Google Colab, directly to YouTube using the YouTube API v3. This tool aims to streamline data-heavy operations, such as sharing computer vision project results.

Prerequisites
Before using the uploader, ensure the following prerequisites are met:

YouTube Developer Account/Console: Create an account and set up a project at YouTube Developer Console.

YouTube API v3 Enabled: Enable the YouTube API v3 for your project in the Developer Console.

Client ID/Secret Key: Generate a Client ID and Secret Key for authentication.

Dependencies
The script will automatically install the required dependencies. No manual installation is needed.

Usage
To run the script from a live notebook in Google Colab, follow these steps:

```python
# Clone the repository
!git clone https://github.com/agent87/youtube_uploader.git

# Change into the project directory
!cd youtube_uploader

# Setup the project
!python youtube_uploader/setup.py

# Run the uploader script
!python2 youtube_uploader/upload.py
```

Important Note
Replace your_email@gmail.com with your actual Gmail address associated with the YouTube Developer Console when prompted by the script.

Contribution
Contributions are welcome! Feel free to submit issues or pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Happy uploading with YouTube Uploader!