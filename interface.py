import flet as ft
from flet import icons, colors, Theme

def main(page: ft.Page): 
    # basic config for app 
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "App Departamentos"
    page.auto_scroll = True

    # defiinf a color palette
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
    page.title = "App Admin"
    page.padding =  0
    page.window_height = 500

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
                ),
        )
    )
    
    def textfield_config(tf): 
        return ft.TextField(value=tf,width=150,color=colors.SURFACE_VARIANT,text_align="center",multiline=False)
        
    def textbutton_generator(nombre="missing name",fx=None):
        return ft.TextButton(text=nombre,width=120, on_click=fx)
    
    global alargar
    alargar = False 
    
    def alargar_pantalla(e):
        global alargar
        if alargar == False:
            page.window_height += 50
            alargar = True
        
        page.update()

    def saludar(e):
        print(f"hello ")

    textf1 = textfield_config("Nombre")

    # here starts main content
    row1_1 = ft.Row([
                    ft.Text(value="Ocupante",text_align="center",height=25),
                    textf1,
                    textbutton_generator("editar",saludar)
                    ])
     
    row1_2 = ft.Row([
                    ft.Text(value="Fecha",text_align="center",height=25),
                    textfield_config("11.3.2024"),
                    textbutton_generator("guardar",alargar_pantalla)
                    ])
    
    row1 = ft.Row([row1_1,ft.VerticalDivider(),row1_2], width=page.width,alignment="center",vertical_alignment="center")
    
   
     
    container1 = ft.Container(content=row1)
    

    page.add(container1)
    page.update()


if __name__ == '__main__':
    ft.app(target=main) 
    