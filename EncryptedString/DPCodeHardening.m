//
//  DPCodeHardening.m
//  EncryptedString
//
//  Created by admin on 2023/4/15.
//

#import "DPCodeHardening.h"

@implementation DPCodeHardening
/* 字符串混淆解密函数，将char[] 形式字符数组和 aa异或运算揭秘 */
FOUNDATION_EXPORT char* decryptConfusionCS(char* string){
    char* origin_string = string;
    while(*string) {
        *string ^= 0xAA;
        string++;
    }
    return origin_string;
}
/* 字符串混淆解密函数，将char[] 形式字符数组和 aa异或运算揭秘 */
FOUNDATION_EXPORT NSString* decryptConstString(char* string){
    /* 先执行decryptConfusionString函数解密字符串 */
    char* str = decryptConfusionCS(string);
    /* 获取字符串的长度 */
    unsigned long len = strlen(str);
    NSUInteger length = [[NSString stringWithFormat:@"%lu",len] integerValue];
     NSString *resultString = [[NSString alloc]initWithBytes:str length:length encoding:NSUTF8StringEncoding];
    return resultString;
}
@end
