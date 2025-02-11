import bpy

class MYADDON_OT_create_ico_sphere(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_create_ico_sphere"
    bl_label = "Ico球生成"
    bl_description = "Ico球を生成します"
    #リデゥ,アンデゥ可能オプション
    bl_options= {'REGISTER', 'UNDO'}

    #メニューを実行したときに呼ばれるコールバック処理
    def execute(self, contex):
        bpy.ops.mesh.primitive_ico_sphere_add()
        print("Ico球を生成しました。")

        #オペレーターの命令終了を通知
        return {'FINISHED'}