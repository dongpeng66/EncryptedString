//
//  ViewController.m
//  EncryptedString
//
//  Created by admin on 2023/4/15.
//

#import "ViewController.h"
#import "DPCodeHardening.h"
@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    /* 使用confusion_NSSTRING宏包含需要加密的NSString字符串 */
    NSString *str = confusion_NSSTRING("Hello World");
    NSLog(@"%@",str);
    /* 使用confusion_NSSTRING宏包含需要加密的char*字符串 */
    char* cStr = confusion_CSTRING("Super Man");
    NSLog(@"%s",cStr);
}


@end
