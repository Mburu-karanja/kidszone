
import audio_player
import buttons
import calculator
import charts
import counter
import drawing_tool
import entry_form
import flet as ft
import flet_animation
import to_do


class AppTile(ft.ListTile):
    def __init__(self, name, view, icon_name, file_name):
        super().__init__()
        self.view = view
        self.bgcolor = ft.colors.SURFACE_VARIANT
        self.title = ft.Text(name)
        self.leading = ft.Icon(icon_name)
        self.on_click = self.app_button_clicked
        self.name = name
        self.file_name = file_name

    def app_button_clicked(self, e):
        e.control.page.views.append(
            ft.View(
                controls=[
                    ft.AppBar(
                        title=ft.Text(f"{e.control.name}"),
                        actions=[
                            ft.IconButton(
                                content=ft.Image(
                                    src="github-mark.svg", width=24, height=24
                                ),
                                url=f"https://github.com/flet-dev/examples/tree/main/python/apps/studio-gallery/{self.file_name}",
                                url_target="_blank",
                            )
                        ],
                    ),
                    e.control.view,
                ],
            )
        )
        e.control.page.update()


def main(page: ft.Page):
    page.add(
        ft.ListView(
            controls=[
                AppTile(
                    name="To-Do",
                    file_name="to_do.py",
                    view=to_do.example(page),
                    icon_name=ft.icons.CHECK_BOX_OUTLINED,
                ),
                AppTile(
                    name="Drawing Tool",
                    file_name="drawing_tool.py",
                    view=drawing_tool.example(page),
                    icon_name=ft.icons.DRAW_OUTLINED,
                ),
            ]
        )
    )

    def view_pop(view):
        page.views.pop()
        top_view = page.views[0]
        page.go(top_view.route)

    page.on_view_pop = view_pop
    page.window_width = 390
    page.window_height = 844
    page.update()


ft.app(target=main, assets_dir="assets")
