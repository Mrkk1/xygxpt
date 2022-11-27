# -*- coding: utf-8 -*-
from components import show_snack_bar
import pyperclip
import flet as ft
from hackcqooc.core import Core
import webbrowser


def login_view(page: ft.page):
    page.theme_mode = "dark"
    account = ft.Ref[ft.TextField]()
    password = ft.Ref[ft.TextField]()
    key = ft.Ref[ft.TextField]()

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
        content=ft.Text("本软件完全开源免费，加入交流群264135853，即可获取秘钥。" +
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
        pyperclip.copy('264135853')
        show_snack_bar(
            page,
            f"加入交流群264135853免费获取秘钥，群号已复制到您的剪贴板",
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
    def gotoguanwang(e):
        webbrowser.open_new("https://mrkk1.github.io")
        dlg_modalA.open = False
        page.update()
    def gotogithub(e):
        webbrowser.open_new("https://github.com/Mrkk1/xygxpt")
        dlg_modalA.open = False
        page.update()


    dlg_modalA = ft.AlertDialog(
        modal=True,
        title=ft.Text("关于"),
        content=ft.Text("版本号V3.0.0" +
                        '\n'+'更新日期：2022-11-26'+'\n'+'官网:https：mrkk1.github.io'+'\n'+'开源地址：https://github.com/Mrkk1/xygxpt'),
        actions=[
            ft.TextButton("前往官网", on_click=gotoguanwang),

            ft.TextButton("前往github", on_click=gotogithub),
            ft.TextButton("取消", on_click=quxiao),

        ],
        actions_alignment="end",
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    def open_dlg_modalA(e):
        page.dialog = dlg_modalA
        dlg_modalA.open = True
        page.update()


    def login(_e):
        if not account.current.value:
            show_snack_bar(page, "还没有输入帐号噢〜", ft.colors.ERROR)
        elif not password.current.value:
            show_snack_bar(page, "好像忘记输入密码了呢", ft.colors.ERROR)
        elif not key.current.value:
            show_snack_bar("请输入秘钥，软件免费可进群获取秘钥")
        else:
            if key.current.value == 'gxpt2022':
                page.core = Core(account.current.value, password.current.value)
                login_res = page.core.login()
                if login_res["status"] == "ok":
                    page.go("/course")
                else:
                    show_snack_bar(page, login_res["msg"], ft.colors.ERROR)
            else:
                show_snack_bar(page, '秘钥错误，请加入群聊获取秘钥', ft.colors.ERROR)

    def gotoQQ():
        pyperclip.copy('264135853')
        show_snack_bar(
            page,
            f"加入交流群264135853免费获取秘钥，群号已复制到您的剪贴板",
            ft.colors.GREEN,
            True,
        )
        webbrowser.open_new(
            "https://qm.qq.com/cgi-bin/qm/qr?k=5r-TsnUKjoZbeKIqOMaxX2kMHxTqGM3W&jump_from=webapi")

    def show_log_path(_e):
        show_snack_bar(
            page,
            f"软件基于MIT协议开源，感谢hackcqooc的支持",
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
                                font_family="Noto Sans SC",
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
                        icon=ft.icons.KEY
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
                        width=180
                    ),

                    ft.IconButton(
                        icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=gotoplay
                    ),
                    ft.IconButton(
                        icon=ft.icons.INFO, on_click=open_dlg_modalA
                    )



                ], alignment="center"

                )

            ],
            horizontal_alignment="center",
            vertical_alignment="center",
        )
    )
