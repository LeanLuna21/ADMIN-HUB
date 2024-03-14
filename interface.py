import flet as ft
from flet import icons, colors, Theme


def main(page: ft.Page):
    # basic config for app
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "App Departamentos"
    page.fonts = {
        "PoppinsL": "ADMIN-HUB/fonts/Poppins-Light.ttf",
        "PoppinsM": "ADMIN-HUB/fonts/Poppins-Medium.ttf",
        "PoppinsR": "ADMIN-HUB/fonts/Poppins-Regular.ttf",
        "PoppinsB": "ADMIN-HUB/fonts/Poppins-SemiBold.ttf",
        "MontserratL": "ADMIN-HUB/fonts/MontserratAlt1-Light.ttf",
    }
    page.theme = Theme(font_family="PoppinsR")
    # define a color palette
    page.theme = ft.Theme(color_scheme_seed=colors.TEAL)

    def toggle_palette(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK

        page.update()

    # editing page window
    page.window_center()
    page.window_frameless = True
    page.window_resizable = False
    page.window_maximizable = False
    page.padding = 0
    page.window_width = 800
    page.window_height = 550

    # designing my own window frame
    # fx for exit button
    def close_main(e):
        page.window_destroy()

    # fx for minimizing window
    def minimize_main(e):
        page.window_minimized = True
        page.update()

    # fx to ask the user whether to proceed
    # exit button calls dialogue fx to double check
    def open_dlg(e):
        page.dialog = dlg_confirmation
        dlg_confirmation.open = True
        page.update()

    # 'no' option will close current doc
    def close_dlg(e):
        dlg_confirmation.open = False
        page.update()

    # define dialogue popup
    dlg_confirmation = ft.AlertDialog(
        modal=False,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to quit?"),
        actions=[
            ft.TextButton("Yes", on_click=close_main),
            ft.TextButton("No", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # add title and frame buttons to page
    page.add(
        ft.WindowDragArea(
            ft.Container(
                width=page.window_width,
                content=ft.Row(
                    [
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Icon(icons.DOMAIN_ROUNDED, size=40),
                                    ft.Text("   "),
                                    ft.Stack(
                                        [
                                            ft.Text(
                                                "ADMIN",
                                                size=25,
                                                color=colors.ON_PRIMARY_CONTAINER,
                                                font_family="MontserratL",
                                                weight="bold",
                                            ),
                                            ft.Text(
                                                "HUB",
                                                right=0,
                                                size=25,
                                                color=colors.PINK_300,
                                                font_family="MontserratL",
                                                weight="w800",
                                            ),
                                        ],
                                        width=172,
                                        height=35,
                                    ),
                                ],
                                vertical_alignment="center",
                            ),
                            padding=10,
                        ),
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.IconButton(
                                        icons.DARK_MODE_ROUNDED,
                                        icon_color=colors.PRIMARY,
                                    ),
                                    ft.Switch(value=False, on_change=toggle_palette),
                                    ft.IconButton(
                                        icons.LIGHT_MODE_ROUNDED,
                                        icon_color=colors.INVERSE_PRIMARY,
                                    ),
                                    ft.Text("      "),
                                    ft.IconButton(
                                        icons.MINIMIZE_ROUNDED, on_click=minimize_main
                                    ),
                                    ft.Text(" "),
                                    ft.IconButton(
                                        icons.CLOSE_ROUNDED, on_click=open_dlg
                                    ),
                                ]
                            )
                        ),
                    ],
                    alignment="spaceBetween",
                ),
                bgcolor=colors.SURFACE_VARIANT,
            ),
            maximizable=False,
        ),
    )

    ################################################################################################################
    ################################################### APP INTERFACE ##############################################
    dpto_id = ft.TextField()
    dpto_id.width = 150
    dpto_id.max_length = 5
    dpto_id.bgcolor = colors.SECONDARY_CONTAINER
    dpto_id.focused_bgcolor = colors.SURFACE_VARIANT
    dpto_id.focused_color = colors.INVERSE_SURFACE
    dpto_id.text_align = "center"
    dpto_id.text_vertical_align = -1.0

    # add top search bar
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("", height=100),
                            ft.Text(
                                "DEPARTAMENTO", style="titleMedium", size=30, height=60
                            ),
                        ],
                        vertical_alignment="end",
                        alignment="center",
                    ),
                    ft.Stack(
                        [
                            dpto_id,
                            ft.IconButton(
                                icon=icons.SEARCH_SHARP,
                                icon_color=colors.PRIMARY,
                                on_click=...,
                                right=0,
                                top=0,
                            ),
                        ],
                        height=65,
                    ),
                    ft.Divider(color=colors.SURFACE_VARIANT),
                ],
                horizontal_alignment="center",
                alignment="center",
                width=page.width,
            ),
        )
    )

    # "cobrar" button expands window and shows invoice options
    global expansion
    expansion = False

    def expandir_ventana(e):
        global expansion
        if expansion == False:
            page.window_height = 850
            page.window_center()
            page.add(ft.Column([ft.Divider()]))

            row3 = ft.Row(
                [
                    ft.Text(
                        value="Mes Actual", height=25, width=150, text_align="center"
                    ),
                    ft.TextField(
                        width=200,
                        height=50,
                        text_align="center",
                    ),
                ],
                width=350,
                alignment="spaceAround",
                vertical_alignment="center",
            )

            row4_1 = ft.Row(
                [
                    ft.Text(value="Monto", height=25, width=150, text_align="center"),
                    ft.TextField(
                        width=200,
                        height=50,
                        text_align="center",
                    ),
                ],
                width=350,
                alignment="spaceAround",
                vertical_alignment="center",
            )

            row4_2 = ft.Row(
                [
                    ft.IconButton(icons.CALCULATE, on_click=...),
                    ft.Text(value="TOTAL", height=30, size=20),
                    ft.TextField(
                        width=200,
                        height=60,
                        text_align="center",
                    ),
                    ft.IconButton(icons.PRINT_ROUNDED, on_click=...),
                ],
                width=400,
                alignment="spaceAround",
                vertical_alignment="center",
            )

            row4 = ft.Row(
                [row4_1, row4_2], width=page.width, vertical_alignment="center"
            )

            row5 = ft.Row(
                [
                    ft.Text(value="Deudas", height=25, width=150, text_align="center"),
                    ft.TextField(
                        width=200,
                        height=50,
                        text_align="center",
                    ),
                ],
                width=350,
                alignment="spaceAround",
                vertical_alignment="center",
            )

            row6 = ft.Row(
                [ft.TextButton("PAGAR", width=200, height=40, on_click=...)],
                width=page.width,
                alignment="center",
            )

            container3 = ft.Container(content=row3, margin=5)
            container4 = ft.Container(content=row4, margin=5)
            container5 = ft.Container(content=row5, margin=5)
            container6 = ft.Container(content=row6, margin=5)

            page.add(container3, container4, container5, container6)

            expansion = True
        else:
            print("execute function")

    # here starts main content
    row1_1 = ft.Row(
        [
            ft.Text(value="Nombre", height=20),
            ft.TextField(
                width=200,
                height=50,
                text_align="center",
            ),
        ],
        width=400,
        alignment="center",
        vertical_alignment="center",
    )

    row1_2 = ft.Row(
        [
            ft.Text(value="Fecha", height=20),
            ft.TextField(
                width=200,
                height=50,
                text_align="center",
            ),
        ],
        width=400,
        alignment="center",
        vertical_alignment="center",
    )

    row2_1 = ft.Row(
        [
            ft.Text(value="Apellido", height=25),
            ft.TextField(
                width=200,
                height=50,
                text_align="center",
            ),
        ],
        width=400,
        alignment="center",
        vertical_alignment="center",
    )

    row2_2 = ft.Row(
        [
            ft.TextButton(text="COBRAR", width=130, on_click=expandir_ventana),
            ft.TextButton(text="ACTUALIZAR", width=130, on_click=...),
        ],
        width=400,
        alignment="center",
        vertical_alignment="center",
    )

    row1 = ft.Row(
        [row1_1, row1_2],
        width=page.width,
        vertical_alignment="center",
        alignment="spaceAround",
    )
    row2 = ft.Row(
        [row2_1, row2_2],
        width=page.width,
        vertical_alignment="center",
        alignment="spaceAround",
    )
    row3 = ft.Row(
        [
            ft.Text(value="Contacto", height=20),
            ft.TextField(
                width=200,
                height=50,
                text_align="center",
            ),
        ],
        width=400,
        alignment="center",
        vertical_alignment="center",
    )

    container1 = ft.Container(content=row1, margin=10)
    container2 = ft.Container(content=row2, margin=10)
    container3 = ft.Container(content=row3, margin=10)

    page.add(container1, container2, container3)

    page.update()


if __name__ == "__main__":
    ft.app(target=main)
