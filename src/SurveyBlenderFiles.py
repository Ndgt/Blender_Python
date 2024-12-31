import bpy
import pprint

pp = pprint.PrettyPrinter(indent=0, width=80, compact=True)
pp.pprint(dir(bpy.data))

print("Object Name / Type")
for obj in bpy.data.objects:
    print(" {:<15} / {}".format(obj.name, obj.type))