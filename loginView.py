# -*- coding: utf-8 -*-
from components import show_snack_bar
import pyperclip
import flet as ft
from hackcqooc.core import Core
import webbrowser
import re
font_family = {
    "Noto Sans SC": "../assets/fonts/NotoSansSC-Regular.otf",
    "Noto Sans SC": "../assets/fonts/NotoSansSC-Regular.otf",

}

   


def login_view(page: ft.page):
    
    page.theme_mode = "dark"
    account = ft.Ref[ft.TextField]()
    password = ft.Ref[ft.TextField]()
    key = ft.Ref[ft.TextField]()
    captcha_value = ft.Ref[ft.TextField]()
    global captcha_key
    captcha_key = ""
    global captchaToken
    captchaToken=""
    captcha_url = ""
    def getToken(e):
        global captcha_key
        page.core = Core(account.current.value, password.current.value,captcha=captcha_value.current.value, captcha_key=captcha_key)
        getToken_res = page.core.get_captchaToken()
        print(getToken_res)

        if getToken_res["status"] == "ok":
            page.go("/course")
        elif getToken_res["msg"]=='账号或密码错误':
            quxiao2(e)
        else:   
            codeurl = getToken_res["cdata"]
            re_codeurl = re.findall('(?<=base64, ).*$', codeurl)[0]
            captcha_key = getToken_res["key"]
            open_dlg_modalB(re_codeurl)
            show_snack_bar(page,captcha_key, ft.colors.ERROR)
        show_snack_bar(page, getToken_res["msg"], ft.colors.GREEN)             
    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    def close_dlg2(e):
        dlg_modal.open = False
        page.update()
        gotoQQ()
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("获取秘钥"),
        content=ft.Text("本软件完全开源免费，加入交流群670850051，即可获取秘钥。" +
                        '\n'+'群号已复制进您的剪贴板，如跳转失败，请手动添加'),
        actions=[
            ft.TextButton("取消", on_click=close_dlg),

            ft.TextButton("确定", on_click=close_dlg2),

        ],
        actions_alignment="end",
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()
        pyperclip.copy('670850051')
        show_snack_bar(
            page,
            f"加入交流群670850051免费获取秘钥，群号已复制到您的剪贴板",
            ft.colors.GREEN,
            True,
        )

# 演示视频
    def gotoplay(e):
        webbrowser.open_new("https://www.bilibili.com/video/BV1MY411d7iu/")
# 关于


    def quxiao(e):
        dlg_modalA.open = False
        page.update()
    def quxiao2(e):
        dlg_modalB.open = False
        page.update()        
    def gotoguanwang(e):
        webbrowser.open_new("http://cqooc.ywlself.com")
        dlg_modalA.open = False
        page.update()
    def gotogithub(e):
        webbrowser.open_new("https://github.com/Mrkk1/xygxpt")
        dlg_modalA.open = False
        page.update()


    dlg_modalA = ft.AlertDialog(
        modal=True,
        title=ft.Text("关于"),
        content=ft.Text("版本号V3.2.1" +
                        '\n'+'更新日期：2023-11-6'+'\n'+'国内官网:http://cqooc.ywlself.com/'+'\n'+'永久官网:https://mrkk1.github.io'+'\n'+'开源地址：https://github.com/Mrkk1/xygxpt'),
        actions=[
            ft.TextButton("国内官网", on_click=gotoguanwang),

            ft.TextButton("前往github", on_click=gotogithub),
            ft.TextButton("取消", on_click=quxiao),

        ],
        actions_alignment="end",
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )
    # 验证码
    dlg_modalB = ft.AlertDialog(
        modal=True,
        # title=ft.Text("请输入验证码"),
        content=ft.TextField(
            ref=captcha_value,
            label="验证码",
            hint_text="验证码",
            max_lines=1,
            width=400,
        ),
  
        actions=[
            ft.Image(src_base64=""),
            ft.TextButton("确定", on_click=getToken),
            ft.TextButton("取消", on_click=quxiao2),
        ],
        actions_alignment="end",
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )
    

    def open_dlg_modalA(e):
        page.dialog = dlg_modalA
        dlg_modalA.open = True
        page.update()
    def open_dlg_modalB(e):
        
        page.dialog = dlg_modalB
        dlg_modalB.open = True
        dlg_modalB.actions[0].src_base64 = e
        page.update()        


    
    def login(_e):
        global captcha_key
        if not account.current.value:
            show_snack_bar(page, "还没有输入帐号噢〜", ft.colors.ERROR)
        elif not password.current.value:
            show_snack_bar(page, "好像忘记输入密码了呢", ft.colors.ERROR)
        elif not key.current.value:
            show_snack_bar("请输入秘钥，软件免费可进群获取秘钥")
        else:
            
            if key.current.value == 'gxpt2024':
                show_snack_bar(
                page,
                f"正在登录~~~",
                ft.colors.YELLOW,
                True,
                )
                page.core = Core(account.current.value, password.current.value)
                login_res = page.core.login()
                if login_res["status"] == "ok":
                    page.go("/course")
                    show_snack_bar(
                    page,
                    f"登录成功",
                    ft.colors.GREEN,
                    True,
                    )
                else:
                    if login_res["msg"] == 'InvalidCaptchaToken or missing captcha token':
                        codeurl = login_res["cdata"] 
                        captcha_url = re.findall('(?<=base64, ).*$', codeurl)[0]
                        
                        captcha_key = login_res["key"] 
                        
                        open_dlg_modalB(captcha_url)
                    show_snack_bar(page, login_res["msg"], ft.colors.ERROR)                    
            else:
                show_snack_bar(page, '秘钥错误，请加入群聊获取秘钥', ft.colors.ERROR)
    def loginagain(_e):
        if not account.current.value:
            show_snack_bar(page, "还没有输入帐号噢〜", ft.colors.ERROR)
        elif not password.current.value:
            show_snack_bar(page, "好像忘记输入密码了呢", ft.colors.ERROR)
        elif not key.current.value:
            show_snack_bar("请输入秘钥，软件免费可进群获取秘钥")
        else:
            if key.current.value == 'gxpt2023':
                page.core = Core(account.current.value, password.current.value)
                login_res = page.core.login()
                if login_res["status"] == "ok":
                    page.go("/course")
                else:
                    if login_res["msg"] == 'InvalidCaptchaToken or missing captcha token':
                        codeurl = login_res["cdata"]
                        re_codeurl = re.findall('(?<=base64, ).*$', codeurl)[0]

                        captcha_key = login_res["key"]
                        open_dlg_modalB(re_codeurl)
                        show_snack_bar(page,captcha_key, ft.colors.ERROR)
                    show_snack_bar(page, login_res["msg"], ft.colors.ERROR)                    
            else:
                show_snack_bar(page, '秘钥错误，请加入群聊获取秘钥', ft.colors.ERROR)

    def gotoQQ():
        pyperclip.copy('670850051 ')
        show_snack_bar(
            page,
            f"加入交流群670850051免费获取秘钥，群号已复制到您的剪贴板",
            ft.colors.GREEN,
            True,
        )
        webbrowser.open_new(
            "http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=wvVARNJSRAKjuiffFw0MHrvzKpZL5QhH&authKey=2IZgb%2B%2Fu2%2B7P1EVMxi1UOoGF77%2FxSSyKnmOPSET9%2FQTwNS80ulWE9ee83NcwV1w6&noverify=0&group_code=670850051")

    def show_log_path(_e):
        show_snack_bar(
            page,
            f"软件基于apache2.0开源协议，禁止商用用途",
            ft.colors.GREEN,
            True,
        )

    def about():
        page.add(ft.Text("Hello!"))
    # View

    page.views.append(

        ft.View(
            "/",
            [
                ft.Column(
                    [
                        ft.Container(
                            content=ft.Text(
                                "小鱼高校平台助手",
                                size=50,
                                # font_family="Noto Sans SC",
                            ),
                            on_click=show_log_path,
                            margin=ft.margin.symmetric(vertical=30)
                        ),
                        ft.TextField(
                            ref=account,
                            label="帐号",
                            hint_text="请输入高校平台帐号",
                            max_lines=1,
                            width=400,
                            icon=ft.icons.ADMIN_PANEL_SETTINGS
                        ),

                        ft.TextField(
                            ref=password,
                            label="密码",
                            hint_text="请输入高校平台密码",
                            password=True,
                            can_reveal_password=True,
                            max_lines=1,
                            width=400,
                            icon=ft.icons.PASSWORD_SHARP
                        ),




                    ],
                    alignment="center",
                ),
                ft.Row([
                    ft.TextField(
                        ref=key,
                        label="秘钥",
                        hint_text="请输入秘钥",
                        password=True,
                        can_reveal_password=True,
                        max_lines=1,
                        width=200,
                        icon=ft.icons.KEY_SHARP
                    ),
                    ft.Container(
                        margin=ft.margin.only(left=40, right=50)
                    ),
                    ft.FilledButton(
                        "获取秘钥",

                        on_click=open_dlg_modal,
                    ),
                ], alignment="center", width=400

                ),
                ft.Container(
                    margin=ft.margin.symmetric(vertical=10)
                ),
                ft.Row([


                    ft.FilledButton(
                        "登录",
                        icon=ft.icons.LOGIN,
                        on_click=login,
                        width=180,
                        
                    ),

                    ft.IconButton(
                        icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=gotoplay
                    ),
                    ft.IconButton(
                        icon=ft.icons.INFO, on_click=open_dlg_modalA
                    ),




                ], alignment="center"

                )

            ],
            horizontal_alignment="center",
            vertical_alignment="center",
        )
    )
