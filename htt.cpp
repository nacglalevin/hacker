#include <iostream>
#include <Windows.h>
#include <string>
#include <conio.h>
#include <stdio.h>
#include "hacker.h"
//在VC++2010版才可以运行这个程序。
//调试模式要切换成Release才可以执行hacker.lib静态库。
using namespace std;

#define X 45//宽
#define Y 25//高
void login();
void menushow();
void one();
void two();
void three();
void four();
int option();
void window();
void inputPwd();

int main(void){
        window();
        login();
        while(1){
        menushow();
        int n=option();
        system("cls");
        switch(n){
                        case 1:one();
                                break;
                        case 2:two();
                                break;
                        case 3:three();
                                break;
                        case 4:four();
                                break;
                        case 5:return 0;
                        default:
                                cout<<"输入无效，请重新输入！"<<endl;
                }
        }
        system("pause");
        return 0;
}
//隐藏密码
void inputPwd(char pwd[],int size){
        char x;
        int i=0;
        while(1){
                x=getch();
                if(x=='\r'){
                        pwd[i]=0;//'\0'结束符
                                break;
                }
                pwd[i++]=x;
                cout<<'*';
        }
        cout<<endl;
}
//设计控制台窗口大小
void window(void){
        char cmd[128];
        sprintf_s(cmd,"mode con cols=%d lines=%d",X,Y);
        system(cmd);
}
//进入功能选项
int option(void){
        int n=0;
        while(1){
                cout<<"请选择：";
                cin>>n;
                if(cin.fail()){
                        cin.clear();
                        getchar();
                        cout<<"选择有误，请选择正确的选项！"<<endl;
                        system("pause");
                }else{
                        break;
                }
        }
        return n;
}
//菜单选择
void menushow(void){
        cout<<"1.网站404攻击\n"<<"2.网站篡改攻击\n"<<"3.查看攻击记录\n"
                <<"4.网站攻击修复\n"<<"5.退出\n";
}
//登录功能
void login(void){
        string name;
        //string pwd;
        char pwd[64];
        while(1){
                cout<<"请输入帐号：";
                cin>>name;
                cout<<"请输入密码：";
                inputPwd(pwd,sizeof(pwd));
                if(name=="admin"&& !strcmp(pwd,"123456")){
                        system("cls");
                        break;
                }else{
                        cout<<"帐号密码错误，请重新输入!"<<endl;
                        system("pause");
                        system("cls");
                }
        }
}
void one(void){//网站404攻击
        char id[128];//网站ID
        char response[4096];//攻击后，服务器的返回结果
        cout<<"请输入攻击ID：";
        scanf_s("%s",&id,sizeof(id));
        cout<<"正在入侵，请稍等...\n";
        hk_404(id,response);
        string ret=UTF8ToGBK(response);
        cout<<ret<<endl;
        system("pause");
        system("cls");
}
void two(void){//网站篡改攻击
        char id[128];
        char response[4096];
        string paratext;
        cout<<"请输入攻击ID：";
        scanf_s("%s",&id,sizeof(id));
        cout<<"请输入篡改的内容：";
        cin>>paratext;
        GBKToUTF8(paratext);//转换编码，不然会显示乱码
        hk_tamper(id,(char*)paratext.c_str(),response);
        string ret=UTF8ToGBK(response);
        cout<<ret<<endl;
        system("pause");
        system("cls");
}
void three(void){//查看攻击记录
        char id[128];
        char response[4096];
        cout<<"请输入ID：";
        scanf_s("%s",&id,sizeof(id));
        hk_record(id,response);
        string ret=UTF8ToGBK(response);
        cout<<ret<<endl;
        system("pause");
        system("cls");
}
void four(void){//网站攻击修复
        char id[128];
        char response[4096];
        cout<<"请输入ID：";
        scanf_s("%s",&id,sizeof(id));
        hk_restore(id,response);
        string ret=UTF8ToGBK(response);
        cout<<ret<<endl;
        system("pause");
        system("cls");
}