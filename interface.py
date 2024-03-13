import flet as ft
from flet import icons, colors, Theme

def main(page: ft.Page): 
    # basic config for app 
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "App Departamentos"

    # define a color palette
    default_color = colors.TEAL_ACCENT_200
    
    def toggle_palette(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.theme = Theme(color_scheme_seed=default_color)
        else: 
            page.theme_mode = ft.ThemeMode.DARK
            page.theme = Theme(color_scheme_seed=default_color)
        page.update()

    # editing page window
    page.window_center()
    page.window_frameless = True
    page.window_resizable = False
    page.window_maximizable = False
    page.padding =  0

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
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    # add title and frame buttons to page
    page.add(
        ft.WindowDragArea(
            ft.Container(
                width=page.window_width,
                content=ft.Row([
                    ft.Container(
                        content= ft.Row([
                            ft.Icon(icons.DOMAIN_ROUNDED,size=40), 
                            ft.Text("      "),
                            ft.Text("ADMINHUB",size=24,font_family="PoppinsR"),
                        ]),padding=10),
                    ft.Container(
                        content= ft.Row([
                            ft.IconButton(icons.LIGHT_MODE_ROUNDED, on_click=toggle_palette),
                            ft.Text("      "),
                            ft.IconButton(icons.MINIMIZE_ROUNDED, on_click=minimize_main),
                            ft.Text(" "),
                            ft.IconButton(icons.CLOSE_ROUNDED, on_click=open_dlg)    
                ]))],alignment="spaceBetween"),bgcolor=colors.SURFACE_VARIANT
            ),maximizable=False
        ),
    )
    
    # add top search bar
    page.add(
        ft.Container(
            content=
                ft.Column(
                    [
                    ft.Row(
                        [
                        ft.Text("",height=100),
                        ft.Text("DEPARTAMENTO",height=60),
                        ft.IconButton(icon=icons.SEARCH_SHARP,on_click=...,bgcolor=colors.SURFACE_VARIANT)
                        ],
                        vertical_alignment="end", 
                        alignment="center"
                        ),
                    ft.TextField(
                        width=150,
                        keyboard_type="number",
                        bgcolor=colors.SURFACE_VARIANT,
                        focused_bgcolor= colors.TEAL_ACCENT_100,
                        multiline=False,
                        color="black"),
                    ft.Divider(color=colors.SURFACE_VARIANT),
                    ],
                    horizontal_alignment="center",
                    alignment="center",
                    width=page.width
                ),
        )
    )
    
    # def textfield_config(tf): 
    #     return ft.TextField(value=tf,width=150,color=colors.SURFACE_VARIANT,text_align="center",multiline=False)
        
    # def textbutton_generator(nombre="missing name",fx=None):
    #     return ft.TextButton(text=nombre,width=120, on_click=fx)
    
    # global alargar
    # alargar = False 
    
    # def alargar_pantalla(e):
    #     global alargar
    #     if alargar == False:
    #         page.window_height += 50
    #         alargar = True
        
    #     page.update()

    # def saludar(e):
    #     print(f"hello ")

    # textf1 = textfield_config("Nombre")

    # here starts main content
# here starts main content
    col1 = ft.Column([
                    ft.Text(value="Ocupante",text_align="center",height=50),
                    ft.Text(value="Contacto",text_align="center",height=50),
                    ft.Text(value="",text_align="center",height=50),
                    ft.Text(value="mes",text_align="center",height=50),
                    ft.Text(value="monto",text_align="center",height=50),
                    ft.Text(value="deudas",text_align="center",height=50),
                ],spacing="spaceBetween",width=250)


    col2 = ft.Column([
                    ft.TextField(width=150,
                            bgcolor=colors.SURFACE_VARIANT,
                            focused_bgcolor= colors.TEAL_ACCENT_100,
                            text_align="center",multiline=False,
                            color="black",
                            label="",
                            ),
                    ft.TextField(width=150,
                            bgcolor=colors.SURFACE_VARIANT,
                            focused_bgcolor= colors.TEAL_ACCENT_100,
                            text_align="center",multiline=False,
                            color="black",
                            label="",
                            ),
                    ft.Text(value="",text_align="center"),
                    ft.TextField(width=150,
                            bgcolor=colors.SURFACE_VARIANT,
                            focused_bgcolor= colors.TEAL_ACCENT_100,
                            text_align="center",multiline=False,
                            color="black",
                            label="",
                            ),
                    ft.TextField(width=150,
                            bgcolor=colors.SURFACE_VARIANT,
                            focused_bgcolor= colors.TEAL_ACCENT_100,
                            text_align="center",multiline=False,
                            color="black",
                            label="",
                            ),
                    ft.TextField(width=150,
                            bgcolor=colors.SURFACE_VARIANT,
                            focused_bgcolor= colors.TEAL_ACCENT_100,
                            text_align="center",multiline=False,
                            color="black",
                            label="",
                            ),
                ])
    

    container = ft.Row() 
    container.spacing= 50
    container.alignment= "center"
    container.vertical_alignment = "center"
    
    container.controls.append(col1)
    container.controls.append(col2)

    page.add(container)
    page.update()


if __name__ == '__main__':
    ft.app(target=main) 
    