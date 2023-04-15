//
//  DPCodeHardening.h
//  EncryptedString
//
//  Created by admin on 2023/4/15.
//

#import <Foundation/Foundation.h>


///* 使用confusion_NSSTRING宏包含需要加密的NSString字符串 */
//NSString *str = confusion_NSSTRING("Hello World");
//NSLog(@"%@",str);
///* 使用confusion_NSSTRING宏包含需要加密的char*字符串 */
//char* cStr = confusion_CSTRING("Super Man");
//NSLog(@"%s",cStr);


/*
 * 使用DPCodeHardening_IsOpen宏控制加密解密
 * 当DPCodeHardening_IsOpen宏被定义的时候，执行加密脚本，对字符串进行加密
 * 当DPCodeHardening_IsOpen宏被删除或为定义时，执行解密脚本，对字符串解密
 */
#define DPCodeHardening_IsOpen

#ifdef DPCodeHardening_IsOpen
/* DPCodeHardening_IsOpen 宏被定义，那么就进行执行解密脚本 */
/* confusion_NSSTRING宏的返回结果是NSString 类型的 */
#define confusion_NSSTRING(string) decryptConstString(string)
/* confusion_CSTRING宏的返回结果是char* 类型的 */
#define confusion_CSTRING(string) decryptConfusionCS(string)
#else
/* DPCodeHardening_IsOpen 宏没有被定义，那么就执行加密脚本 */
/* 加密NSString类型的 */
#define confusion_NSSTRING(string) @string
/* 加密char *类型的 */
#define confusion_CSTRING(string) string
#endif
NS_ASSUME_NONNULL_BEGIN

@interface DPCodeHardening : NSObject
/* 字符串混淆解密函数，将char[] 形式字符数组和 aa异或运算揭秘 */
FOUNDATION_EXPORT char* decryptConfusionCS(char* string);
/* 字符串混淆解密函数，将char[] 形式字符数组和 aa异或运算揭秘 */
FOUNDATION_EXPORT NSString* decryptConstString(char* string);
@end

NS_ASSUME_NONNULL_END
