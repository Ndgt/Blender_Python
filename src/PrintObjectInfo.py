import bpy

print("object name / type")
for obj in bpy.data.objects:
    print(" {0:<15} / {1}".format(obj.name, obj.type))