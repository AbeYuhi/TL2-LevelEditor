import bpy

#AddonInfo
bl_info = {
    "name": "LevelEditor",
    "author": "Abe Yuhi",
    "version": (1.0),
    "blender": (4, 1, 1),
    "location": "",
    "description": "LevelEditor",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}

from .stretch_vertex import MYADDON_OT_stretch_vertex
from .create_ico_sphere import MYADDON_OT_create_ico_sphere
from .export_scene import MYADDON_OT_export_scene
from .add_drawCheck import MYADDON_OT_add_drawcheck
from .add_drawCheck import OBJECT_PT_draw_check
from .spawn_point import MYADDON_OT_spawn_import_symbol
from .spawn_point import MYADDON_OT_spawn_create_symbol

class TOPBAR_MT_my_menu(bpy.types.Menu):
    #Blenderがクラスを識別するための固有文字列
    bl_idname = "TOPBAR_MT_my_menu"
    #メニューのラベルとして表示される文字列
    bl_label = "MyMenu"
    #著者表示用の文字列
    bl_description = "拡張メニュー by " + bl_info["author"]

    #サブメニューの描画
    def draw(self, context):
        self.layout.operator("wm.url_open_preset", text="Manual", icon = 'HELP')
        #区切り線
        self.layout.separator()
        self.layout.operator(MYADDON_OT_stretch_vertex.bl_idname, text=MYADDON_OT_stretch_vertex.bl_label)
        self.layout.operator(MYADDON_OT_create_ico_sphere.bl_idname, text=MYADDON_OT_create_ico_sphere.bl_label)
        self.layout.operator(MYADDON_OT_export_scene.bl_idname, text=MYADDON_OT_export_scene.bl_label)
        self.layout.operator(MYADDON_OT_spawn_create_symbol.bl_idname, text=MYADDON_OT_spawn_create_symbol.bl_label)

    #既存のメニューにサブメニューを追加
    def submenu(self, context):
        self.layout.menu(TOPBAR_MT_my_menu.bl_idname)

classes = (
    MYADDON_OT_export_scene,
    MYADDON_OT_create_ico_sphere,
    MYADDON_OT_add_drawcheck,
    MYADDON_OT_spawn_import_symbol,
    MYADDON_OT_spawn_create_symbol,
    OBJECT_PT_draw_check,
    TOPBAR_MT_my_menu,
)

def register():
    #Blenderにクラスを登録
    for cls in classes:
        bpy.utils.register_class(cls)

    #メニューに項目を追加
    bpy.types.TOPBAR_MT_editor_menus.append(TOPBAR_MT_my_menu.submenu)
    print("レベルエディタが有効化されました。")
    
def unregister():
    #メニューから項目を削除
    bpy.types.TOPBAR_MT_editor_menus.remove(TOPBAR_MT_my_menu.submenu)

    #BlenderからClassを削除
    for cls in classes:
        bpy.utils.unregister_class(cls)
    print("レベルエディタが無効化されました。")