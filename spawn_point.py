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

# �I�y���[�^ �o���|�C���g�̃V���{����ǂݍ���
class MYADDON_OT_spawn_import_symbol(bpy.types.Operator):
    bl_idname = "spawn_import_symbol"
    bl_label = "�o���|�C���g�V���{��Import"
    bl_description = "�o���|�C���g�̃V���{����Import���܂�"
    prototype_object_name = "PrototypePlayerSpawn"
    object_name ="PlayerSpawn"

    def execute(self, context):
        print("�o���|�C���g�̃V���{����Import���܂�")

        # �d�����[�h�h�~
        spawn_object = bpy.data.objects.get(MYADDON_OT_spawn_import_symbol.prototype_object_name)
        if spawn_object is not None:
            return {'CANCELLED'}

        # �X�N���v�g���z�u����Ă���f�B���N�g���̖��O���擾����
        addon_directory = os.path.dirname(__file__)
        # �f�B���N�g������̃��f���t�@�C���̑��΃p�X���L�q
        relative_path = "player/player.obj"
        # �������ă��f���t�@�C���̃t���p�X�𓾂�
        full_path = os.path.join(addon_directory, relative_path)

        # �I�u�W�F�N�g���C���|�[�g
        bpy.ops.wm.obj_import('EXEC_DEFAULT',
                              filepath = full_path, display_type = "THUMBNAIL",
                              forward_axis='Z', up_axis='Y')
        
        # ��]��K�p
        bpy.ops.object.transform_apply(location=False,
                                       rotation=True, scale=False, properties=False,
                                       isolate_users=False)
        
        # �A�N�e�B�u�ȃI�u�W�F�N�g���擾
        object = bpy.context.active_object
        # �I�u�W�F�N�g����ύX
        object.name = MYADDON_OT_spawn_import_symbol.prototype_object_name

        # �I�u�W�F�N�g�̎�ނ�ݒ�
        object["type"] = MYADDON_OT_spawn_import_symbol.object_name

        # ��������ɂ͂����Ă������V�[������O��
        bpy.context.collection.objects.unlink(object)

        return {'FINISHED'}

# �I�y���[�^ �o���|�C���g�̃V���{�����쐬�E�z�u����
class MYADDON_OT_spawn_create_symbol(bpy.types.Operator):
    bl_idname = "object.spawn_create_symbol"
    bl_label = "�o���|�C���g�V���{���̍쐬"
    bl_description = "�o���|�C���g�̃V���{�����쐬���܂�"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        # �ǂݍ��ݍς݂̃R�s�[���I�u�W�F�N�g������
        spawn_object = bpy.data.objects.get(MYADDON_OT_spawn_import_symbol.prototype_object_name)

        # �܂��ǂݍ���ł��Ȃ��ꍇ
        if spawn_object is None:
            # �ǂݍ��݃I�y���[�^�����s����
            bpy.ops.myaddon.myaddon_ot_spawn_import_symbol('EXEC_DEFAULT')
            # �Č���B���x�͌�����͂�
            spawn_object = bpy.data.objects.get(MYADDON_OT_spawn_import_symbol.prototype_object_name)
        
        print("�o���|�C���g�̃V���{�����쐬���܂�")

        # Blender�ł��I������������
        bpy.ops.object.select_add(action='DESELECT')

        # �������̔�\���I�u�W�F�N�g�𕡐�����
        object = spawn_object.copy()

        # ���������I�u�W�F�N�g�����݂̃V�[���Ƀ����N����(�o��������)
        bpy.context.sollection.objection.objects.link(object)

        # �I�u�W�F�N�g����ύX
        object.name = MYADDON_OT_spawn_create_symbol.object_name

        return {'FINISHED'}