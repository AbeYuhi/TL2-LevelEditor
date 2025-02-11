import bpy
import math
import gpu
import gpu_extras.batch
import bpy_extras
import copy
import mathutils
import json
from bpy.props import (
    IntProperty,
    FloatProperty,
    FloatVectorProperty,
    EnumProperty,
    BoolProperty,
)

class MYADDON_OT_export_scene(bpy.types.Operator, bpy_extras.io_utils.ExportHelper):
    bl_idname = "myaddon.myaddon_ot_export_scene"
    bl_label = "シーン出力"
    bl_description = "シーン情報をExportします"

    #出力するファイルの拡張子
    filename_ext = ".scene"

    def parse_scene_recursive(self, file, object, level):
        """シーン解析用再起関数"""

        #深さ分インデントする
        indent = ''
        for i in range(level):
            indent += "\t"

        #オブジェクト名書き込み
        file.write(indent + object.type + " - " + object.name + "\n")
        trans, rot, scale = object.matrix_local.decompose()
        rot = rot.to_euler()
        #ラジアンから度数法に変換
        rot.x = math.degrees(rot.x)
        rot.y = math.degrees(rot.y)
        rot.z = math.degrees(rot.z)
        #トランスフォーム情報を表示
        file.write(indent + "Trans(%f, %f, %f)\n" % (trans.x, trans.y, trans.z))
        file.write(indent + "Rot(%f, %f, %f)\n" % (rot.x, rot.y, rot.z))
        file.write(indent + "Scale(%f, %f, %f)\n" % (scale.x, scale.y, scale.z))
        file.write("\n")

        if "draw_check" in object:
            json_object["draw_check"] = object["draw_check"]

        #子ノードへ進む
        for child in object.children:
            self.parse_scene_recursive(file, child, level + 1)

    def export(self):
        """ファイルに出力"""

        print("シーン情報出力開始... %r" % self.filepath)

        #ファイルをテキスト形式で書き出し用にオープン
        #スコープを抜けると自動的にクローズされる
        with open(self.filepath, "wt") as file:
            file.write("SCENE\n")

            for object in bpy.context.scene.objects:
                #親オブジェクトがあるものはスキップ(親から呼び出されるため)
                if(object.parent):
                    continue

                #シーン直下のオブジェクトをルートノード(深さ0)とし、再起関数で走査
                self.parse_scene_recursive(file, object, 0)


    def execute(self, context):
        print("シーン情報をExportします")

        self.export()

        self.report({'INFO'}, "シーン情報をExportしました")
        print("シーン情報をExportしました")

        return {'FINISHED'}