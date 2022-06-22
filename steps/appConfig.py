app_android_desired_caps = {
    "deviceName":"Galaxy S20",
    "platformName":"Android",
    "platformVersion":"10",
    "build":"Python Behave - Android",
    "name":"Sample Test Android",
    "isRealMobile":True,
    "network":True,
    "visual":True,
    "video":True,
    "app":"lt://", #Enter app_url here


    # ADD THE APP URL OF OTHER APPS THAT YOU'D LIKE TO INSTALL ON THE SAME DEVICE

    "otherApps":["lt:// ", "lt:// "]   #ENTER THE OTHER APP URLs HERE IN AN ARRAY FORMAT


}

app_ios_desired_caps = {
    "deviceName":"iPhone 12",
    "platformName":"ios",
    "platformVersion":"14",
    "build":"Python Behave - iOS",
    "name":"Sample Test iOS",
    "isRealMobile":True,
    "network":True,
    "visual":True,
    "video":True,
    "app":"lt://", #Enter app_url here


    # ADD THE APP URL OF OTHER APPS THAT YOU'D LIKE TO INSTALL ON THE SAME DEVICE

    "otherApps":["lt:// ", "lt:// "]   #ENTER THE OTHER APP URLs HERE IN AN ARRAY FORMAT

}
