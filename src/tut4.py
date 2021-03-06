# -*- coding: utf-8; -*-
#
# Copyright 2015, Kabuku Inc. http://www.kabuku.co.jp
#
# This repository hosts sample codes used in the articles in rinkak (https://www.rinkak.com)
#
# <The article for this code>
# https://www.rinkak.com/blog/blender-python-modeling-4
#

__author__ = "Takuro Wada"
__copyright__ = "Copyright 2015, Kabuku Inc."
__license__ = "MIT"

import bpy


def delete_all():
    for item in bpy.context.scene.objects:
        bpy.context.scene.objects.unlink(item)

    for item in bpy.data.objects:
        bpy.data.objects.remove(item)

    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)

    for item in bpy.data.materials:
        bpy.data.materials.remove(item)


def deg_to_rad(d):
    import math
    return d * math.pi / 180.0


def add_multiple_cone_with_rotation():
    import random
    for x in range(2):
        for y in range(15):
            r1 = random.random()
            r2 = random.random()
            r3 = random.random()
            bpy.ops.mesh.primitive_cone_add(
                location=(x, y, 0),
                rotation=(r1, r2, r3)
            )


def make_boolean_union():
    base_cone = bpy.data.objects[0]
    bpy.context.scene.objects.active = base_cone
    for i, cone in enumerate(bpy.data.objects):
        if i == 0:
            continue
        boolean = base_cone.modifiers.new('ConeBoolean', 'BOOLEAN')
        boolean.object = cone
        boolean.operation = 'UNION'
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier='ConeBoolean')
        bpy.context.scene.objects.unlink(cone)


def add_arrow_object():
    rx = deg_to_rad(90)
    ry = deg_to_rad(-180)
    rz = deg_to_rad(-90)

    bpy.ops.object.empty_add(
        type='ARROWS', radius=1, view_align=False, location=(0, 0, 0),
        rotation=(rx, ry, rz),
        layers=(True, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False,
                False, False, False, False)
    )
    return


def make_deform():
    base_cone = bpy.data.objects['Cone']
    bpy.context.scene.objects.active = base_cone
    deform = base_cone.modifiers.new('ConeDeform', 'SIMPLE_DEFORM')
    deform.deform_method = 'BEND'
    deform.origin = bpy.data.objects['Empty']
    deform.angle = deg_to_rad(280)
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier='ConeDeform')

if __name__ == "__main__":
    delete_all()
    add_multiple_cone_with_rotation()
    make_boolean_union()
    add_arrow_object()
    make_deform()
