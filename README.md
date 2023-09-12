# How to Setup MFA (Multi Factor Authentication) on Windows and Linux Subsystems?

# What is MFA?

Multi-Factor Authentication (MFA), also known as Two-Factor Authentication (2FA) or Two-Step Verification (2SV), is a security strategy used to improve the authentication process by forcing users to give multiple forms of verification before they may access an account, system, or application. MFA addresses the shortcomings of standard single-factor authentication (SFA), which frequently depends exclusively on something the user is aware of, such as a password, and is used to dramatically increase the security of digital assets and data.

# Setting up MFA on Windows

Let’s see the step-by-step procedure to set up multifactor authentication on your Windows 11

## Multi Factor Authentication for Microsoft Account

Let’s begin the configuring the MFA by login in to the Microsoft Account and click on ‘**Security**‘ tab.

## Selecting Advanced Security Options

![Picture1.png](How%20to%20Setup%20MFA%20(Multi%20Factor%20Authentication)%20on%20%20c8a1bae0f744438ab0bf16a791313c8b/Picture1.png)

## Selecting additional ways to verify or sign in

Under Advanced Security Options page, click on ‘**Add a new way to sign in or verify**‘ to add  additional ways to verify or sign in.

![Picture2.png](How%20to%20Setup%20MFA%20(Multi%20Factor%20Authentication)%20on%20%20c8a1bae0f744438ab0bf16a791313c8b/Picture2.png)

## We have 5 different ways to verify or sign in

- Using Microsoft Authenticator App
- Email a code
- Using face, fingerprint or a PIN
- Using USB, Bluetooth or NFC device
- Send a text code to the registered phone

![Picture3.png](How%20to%20Setup%20MFA%20(Multi%20Factor%20Authentication)%20on%20%20c8a1bae0f744438ab0bf16a791313c8b/Picture3.png)

## Enable Two-step verification

Under Additional security , we have ‘**Two-step verification**‘ is ‘**Off**‘ and click on ‘**Turn on**‘ to configure it.

![Picture4.png](How%20to%20Setup%20MFA%20(Multi%20Factor%20Authentication)%20on%20%20c8a1bae0f744438ab0bf16a791313c8b/Picture4.png)

**Follow the steps to install the Authenticator app in your phone and click on ‘Finish’ when setup completes**

![Picture5.png](How%20to%20Setup%20MFA%20(Multi%20Factor%20Authentication)%20on%20%20c8a1bae0f744438ab0bf16a791313c8b/Picture5.png)

## Configure to sign in to Microsoft account without password

Navigate to Advanced Security Options page, click on ‘**Add a new way to sign in or verify**‘.

![Picture6.png](How%20to%20Setup%20MFA%20(Multi%20Factor%20Authentication)%20on%20%20c8a1bae0f744438ab0bf16a791313c8b/Picture6.png)

## Configuring Windows Logon

Login with your Microsoft Account and use the authenticator app to sign in to add your Microsoft account to your windows 10 machine.

![Picture7.png](How%20to%20Setup%20MFA%20(Multi%20Factor%20Authentication)%20on%20%20c8a1bae0f744438ab0bf16a791313c8b/Picture7.png)

After Adding the Microsoft account, You’ve enabled MFA on your windows 10.

# Setting up MFA on Linux

## 

## Installing Google Authenticator on Linux OS

Log in to your linux server, with administrative privileges or as a user.

Install google authenticator using the following command:

```bash
sudo apt-get install libpam-google
sudo yum install google-authenticator
```

![Picture8.png](How%20to%20Setup%20MFA%20(Multi%20Factor%20Authentication)%20on%20%20c8a1bae0f744438ab0bf16a791313c8b/Picture8.png)

## Enable Google Authenticator

Now We need to enable google authenticator once it’s installed successfully. You can do that by using the following command:

```bash
google-authentication
```

It will prompt something and simply type Y and hit enter. Once you press enter, a QR code will be generated. Scan this from your google authenticator mobile app and it’ll enable the google authenticator on your Linux Os.

![Picture9.png](How%20to%20Setup%20MFA%20(Multi%20Factor%20Authentication)%20on%20%20c8a1bae0f744438ab0bf16a791313c8b/Picture9.png)

![Picture10.png](How%20to%20Setup%20MFA%20(Multi%20Factor%20Authentication)%20on%20%20c8a1bae0f744438ab0bf16a791313c8b/Picture10.png)

## Add Configuration in the Pam Configuration File

We need to add the following parameters to the pam configuration file in order to make the MFA enabled in the Linux Os. To do so, type the following command:

```bash
sudo vi etc/pam.d/ssh
```

This command will open up the configuration file. Inside the file, add the following line :

```bash
auth required pam_google_authenticator.so nullok
```

And save the file.

![Picture11.png](How%20to%20Setup%20MFA%20(Multi%20Factor%20Authentication)%20on%20%20c8a1bae0f744438ab0bf16a791313c8b/Picture11.png)

## Add configurations in SSHD file

After configuring the pam file, we need to add configurations ins sshd config file. To do so , type:

```bash
sudo vi etc/ssh/sshd_config
```

![Picture12.png](How%20to%20Setup%20MFA%20(Multi%20Factor%20Authentication)%20on%20%20c8a1bae0f744438ab0bf16a791313c8b/Picture12.png)

After opening the file, we need to change the ChallengeResponseAuthentication parameter to yes. Change it’s value to yes and save the file.

![Picture13.png](How%20to%20Setup%20MFA%20(Multi%20Factor%20Authentication)%20on%20%20c8a1bae0f744438ab0bf16a791313c8b/Picture13.png)

After doing modification, restart the sshd service to take effect of the changes.
Restart the sshd service by typing the following command:

```bash
sudo systemctl restart sshd
```

![Picture14.png](How%20to%20Setup%20MFA%20(Multi%20Factor%20Authentication)%20on%20%20c8a1bae0f744438ab0bf16a791313c8b/Picture14.png)

This way we have enabled MFA on Linux. I used Centos.
