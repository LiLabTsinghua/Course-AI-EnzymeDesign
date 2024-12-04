# 🏁 AI Enzyme Design Software Tutorial 

This tutorial provides instructions for installing and configuring Visual Studio Code (VSCode), as well as running Python code on a remote server.

## ☯ 1. Visual Studio Code (VSCode) 

VSCode is a lightweight but powerful source code editor. You can download it from the official website:  
[https://code.visualstudio.com/download](https://code.visualstudio.com/download)  
Choose the appropriate version based on your operating system. The tutorial below is an example for Windows 10.

### ⚙️ 1.1 Installation Steps for Windows 10

1. **Download the VSCode installer** and choose the *System Installer* version.
2. **Run the downloaded installer** and agree to the license agreement by checking "I accept the agreement."
3. **Choose an installation path** (ensure the path doesn't contain Chinese characters). It's recommended to install it on a non-system drive.
4. **Select the start menu folder** (usually the default is fine).
5. **Choose additional tasks** to be included in the installation (it's recommended to check all options).
6. **Proceed to install** and click *Install* to start the installation process.
7. Once the installation is complete, click *Finish*.

### ⚙️ 1.2 Configuring VSCode

1. **Set the interface language to Chinese (if desired)**:
   - In the Extensions(Ctrl+Shift+x) view on the left sidebar, search for "Chinese" to find the plugin.
   - Install the plugin, and after installation, click *Restart* when prompted to restart VSCode.

2. **Install Jupyter extension**:
   - In the Extensions view, search for "Python" and "Jupyter", and install the extensions. This is essential for reading and running notebooks.

## 🌐 2. Connecting to a Remote Server

1. **Install Remote extensions**:
   - In the Extensions view, search for "Remote" and install the necessary extensions(Remote SSH、Remote Explorer).

2. **Connecting to the remote server**:
   - After the Remote extensions are installed, click on the 💻**Remote Explorer** icon in the left sidebar.
   - Click the ➕ button to create a new window.
   - connect to our server(Please notice the message in the Wechat Group):

3. **Accessing directories**:
   - Click on the **Explorer** tab on the top left of VSCode.
   - Navigate to the directory you want to work in, typically `/home/<account>/`.
   - After selecting the directory, you’ll be asked for your password again.

For a more detailed setup guide, refer to the following resources:👇
- [CSDN Tutorial 1](https://blog.csdn.net/msdcp/article/details/127033151)
- [CSDN Tutorial 2](https://blog.csdn.net/zhaxun/article/details/120568402)

### 👉 Other Information:
- The server is pre-configured with Anaconda and CUDA.

