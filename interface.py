import flet as ft
from flet import icons, colors
import datetime

def main(page: ft.Page):
    # basic config for app 
    page.title = "App Departamentos"
    page.fonts = {
        "PoppinsL": "ADMIN-HUB/fonts/Poppins-Light.ttf",
        "PoppinsM": "ADMIN-HUB/fonts/Poppins-Medium.ttf",
        "PoppinsR": "ADMIN-HUB/fonts/Poppins-Regular.ttf",
        "PoppinsB": "ADMIN-HUB/fonts/Poppins-SemiBold.ttf",
        "MontserratL": "ADMIN-HUB/fonts/MontserratAlt1-Light.ttf",
    }
    # define a color palette
    page.theme = ft.Theme(color_scheme_seed=colors.TEAL_100,color_scheme={"background":colors.GREY_900},font_family="PoppinsR")
    page.bgcolor = colors.BACKGROUND
    page.theme_mode = ft.ThemeMode.DARK

    def toggle_palette(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.bgcolor = colors.TEAL_100
        else:
            page.theme_mode = ft.ThemeMode.DARK
            page.bgcolor = colors.BACKGROUND
        page.update()

    #####################################################################################################
    ######################################## editing page window ########################################
    page.window_center()
    page.window_frameless = True
    page.window_resizable = False
    page.window_maximizable = False
    page.padding = 0
    page.window_width = 1100
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
                                                weight="bold"
                                            ),
                                            ft.Text(
                                                "HUB",
                                                right=0,
                                                size=25,
                                                color=colors.PINK_300,
                                                font_family="MontserratL",
                                                weight="w800"
                                            ),
                                        ],
                                        width=162,
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
    ################################################ APP FUNCTIONALITIES ###########################################



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
                            ft.Text("DEPARTAMENTO", style="titleMedium", size=30, height=60),
                        ],
                        vertical_alignment="end",
                        alignment="center"
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
                        height=65
                    ),
                    ft.Divider(color=colors.SURFACE_VARIANT)
                ],
                horizontal_alignment="center",
                alignment="center",
                width=page.width
            )
        )
    )

    # function to configure labels
    def labels_config(my_label, value):
        my_label.value = value
        my_label.height = 25
        my_label.width = 130
        my_label.text_align = "right"

    # create labels for window
    nombre_label = ft.Text()
    labels_config(nombre_label, "Nombre")
    apellido_label = ft.Text()
    labels_config(apellido_label, "Apellido")
    contacto_label = ft.Text()
    labels_config(contacto_label, "Contacto")
    mes_label = ft.Text()
    labels_config(mes_label, "Mes actual:")
    monto_label = ft.Text()
    labels_config(monto_label, "Monto:")
    deudas_label = ft.Text()
    labels_config(deudas_label, "Deudas:")

    # function to configure textfields
    def textfield_config(my_textfield):
        my_textfield.width = 200
        my_textfield.height = 40
        my_textfield.bgcolor = colors.SURFACE_VARIANT
        my_textfield.focused_color = colors.BLACK
        my_textfield.focused_bgcolor = colors.TEAL_ACCENT_100
        my_textfield.text_align = "center"
        my_textfield.text_vertical_align = -1.0

    # create variables for text input values
    nombre = ft.TextField()
    textfield_config(nombre)
    nombre.height = 50
    apellido = ft.TextField()
    textfield_config(apellido)
    apellido.height = 50
    contacto = ft.TextField()
    textfield_config(contacto)
    contacto.height = 50
    fecha = ft.TextField()
    textfield_config(fecha)
    fecha.height = 50
    fecha.value = datetime.date.today()

    mes = ft.TextField()
    textfield_config(mes)
    monto = ft.TextField()
    textfield_config(monto)
    deudas = ft.TextField()
    textfield_config(deudas)
    total = ft.TextField()
    textfield_config(total)
    total.width = 300
    total.height = 50

    # "cobrar" button expands window and shows invoice options
    global expansion
    expansion = False

    def expandir_ventana(e):
        global expansion
        if expansion == False:
            page.window_height = 760
            page.window_center()
            page.add(ft.Column([ft.Divider(color=colors.SURFACE_VARIANT)]))

            row3_1 = ft.Row(
                [mes_label, mes], alignment="start", vertical_alignment="center"
            )

            row3_2 = ft.Row(
                [monto_label, monto], alignment="start", vertical_alignment="center"
            )

            row3_3 = ft.Row(
                [deudas_label, deudas], alignment="start", vertical_alignment="center"
            )

            row4_2 = ft.Row(
                [
                    ft.Text(
                        value="TOTAL :",
                        height=40,
                        width=175,
                        size=20,
                        text_align="center"
                    ),
                    ft.Stack(
                        [
                            total,
                            ft.IconButton(
                                icons.CALCULATE, on_click=..., bottom=5, left=5
                            )
                        ],
                        width=325
                    ),
                    ft.IconButton(icons.PRINT_ROUNDED, on_click=...)
                ],
                alignment="spaceAround",
                vertical_alignment="center"
            )

            row3 = ft.Row(
                [row3_1, row3_2, row3_3],
                width=page.width,
                alignment="start",
                vertical_alignment="center"
            )

            row4 = ft.Row(
                [row4_2],
                width=page.width,
                alignment="center",
                vertical_alignment="center"
            )

            row5 = ft.Row(
                [ft.TextButton("PAGAR", width=200, height=40, on_click=...)],
                width=page.width,
                alignment="center"
            )

            container3 = ft.Container(content=row3, margin=5)
            container4 = ft.Container(content=row4, margin=10)
            container5 = ft.Container(content=row5, margin=5)

            page.add(container3, container4, container5)
            expansion = True

        else:
            print("execute function")

        page.update()

    # here starts main content
    row1_1 = ft.Row(
        [nombre_label, nombre],
        width=350,
        alignment="center",
        vertical_alignment="center",
    )

    row1_2 = ft.Row(
        [ft.Text(value="Fecha", height=20), fecha],
        width=350,
        alignment="center",
        vertical_alignment="center",
    )

    row2_1 = ft.Row(
        [apellido_label, apellido],
        width=350,
        alignment="center",
        vertical_alignment="center",
    )

    row2_2 = ft.Row(
        [
            ft.TextButton(text="COBRAR", width=130, on_click=expandir_ventana),
            ft.TextButton(text="ACTUALIZAR", width=130, on_click=...),
        ],
        width=350,
        alignment="center",
        vertical_alignment="center",
    )

    row1 = ft.Row(
        [row1_1, row1_2],
        width=page.width,
        vertical_alignment="center",
        alignment="spaceEvenly",
    )

    row2 = ft.Row(
        [row2_1, row2_2],
        width=page.width,
        vertical_alignment="center",
        alignment="spaceEvenly",
    )
    
    row3 = ft.Row(
        [contacto_label, contacto],
        width=600,
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
