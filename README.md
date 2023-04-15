# EncryptedString
#使用
上线前#define DPCodeHardening_IsOpen宏定义打开，或者设置其他开关，然后confusion.py中修改srcPath = '../EncryptedString'为自己需要加密字符串的目录，执行

python3 confusion.py

前提confusion_NSSTRING("Hello World")，已经对需要加密字符串添加

需要解密字符串decrypt.py修改srcPath = '../EncryptedString'为自己需要加密字符串的目录，执行

python3 decrypt.py
