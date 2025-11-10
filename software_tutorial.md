# 🏁 AI Enzyme Design Software Tutorial

This tutorial provides step-by-step instructions for installing and configuring Visual Studio Code (VSCode), as well as a simple guide on how to run Python code on a remote server.

## ☯ 1. Visual Studio Code (VSCode)

VSCode is a lightweight yet powerful source code editor. You can download it from the official website:  
[https://code.visualstudio.com/download](https://code.visualstudio.com/download)  
We recommend using version [1.96.4](https://code.visualstudio.com/updates/v1_96) and disabling automatic updates in settings to ensure stable SSH remote connections.  
Please select the appropriate version for your operating system. The following instructions assume you are using **Windows 10**.

### ⚙️ 1.1 Installing VSCode on Windows 10

1. **Download the VSCode installer**, and choose the *System Installer* version.
2. **Run the downloaded installer**, accept the license agreement, and check “I accept the agreement.”
3. **Choose an installation path** (ensure the path contains no Chinese characters). It is recommended to install it on a non-system drive.
4. **Select the Start Menu folder** (default settings are usually fine).
5. **Select additional tasks** (it is recommended to check all options).
6. **Begin installation** by clicking *Install*.
7. Once installation is complete, click *Finish*.

### ⚙️ 1.2 Configuring VSCode

1. **Set the interface language to Chinese (optional)**:
   - Open the Extensions sidebar (Ctrl+Shift+X), search for “Chinese,” and install the Chinese Language Pack extension.
   - After installation, click *Restart* to apply the language change.

## 🌐 2. Connecting to a Remote Server

1. **Install Remote Development extensions**:
   - In the Extensions view, search for “Remote” and install the relevant extensions (**Remote - SSH** and **Remote Explorer**).

2. **Connect to the remote server**:
   - After installing the Remote extensions, click the 💻 **Remote Explorer** icon on the left sidebar.
   - Click the ➕ button to add a new SSH host.
   - Connect to our course server (the server IP address, username, and password will be announced in the course group chat).

3. **Access your working directory**:
   - Click the **Explorer** tab in the top-left corner of VSCode.
   - Navigate to your working directory, typically located at `/data/home/<your_account>/`.
   - You may be prompted to enter your password again.

4. **Install Python and Jupyter extensions on the remote server**:
   - In the Extensions view, switch the installation context to **SSH: xx.xxx.xx.xxx** (your connected server).
   - Search for and install the **Python** and **Jupyter** extensions.

For more detailed setup instructions, please refer to the following resources 👇  
- [CSDN Tutorial 1](https://blog.csdn.net/msdcp/article/details/127033151)  
- [CSDN Tutorial 2](https://blog.csdn.net/zhaxun/article/details/120568402)

## 🚩 3. Running Code

1. **Running example notebooks**:
   - Ensure that **Python** and the **Jupyter** extension are installed on the **remote server**.
   - Open the provided Jupyter Notebook files (with the `.ipynb` extension).
   - To open a terminal, go to the top menu bar: **View → Terminal**. Use this terminal to install any required packages or environments.
   - In the opened Jupyter Notebook, click the kernel name in the top-right corner → **Change Kernel** → **Select Another Kernel**, then choose the environment specified for each lesson.

### 👉 Additional Information:
- The server has been pre-configured with **Anaconda** and **CUDA**.
