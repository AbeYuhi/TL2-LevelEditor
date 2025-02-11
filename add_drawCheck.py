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

class MYADDON_OT_add_drawcheck(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_add_drawcheck"
    bl_label = "DrawCheck 追加"
    bl_description = "['draw_check']カスタムプロパティを追加します"
    #リデゥ,アンデゥ可能オプション
    bl_options= {'REGISTER', 'UNDO'}

    def execute(self, context):
        #['file_name']カスタムプロパティを追加
        context.object["draw_check"] = True
        return {"FINISHED"}


class OBJECT_PT_draw_check(bpy.types.Panel):
    """オブジェクトの描画チェックパネル"""
    bl_idname = "OBJECT_PT_draw_check"
    bl_label = "DrawCheck"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    #サブメニューの描画
    def draw(self, context):
        self.layout.prop(context.object, '["draw_check"]', text = self.bl_label)