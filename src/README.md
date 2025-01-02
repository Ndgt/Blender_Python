## Remarks
- new data-blocks in the bpy API cannot be created by calling the class

    ```python
    bpy.types.Mesh()
    Traceback (most recent call last):
    File "<blender_console>", line 1, in <module>
    TypeError: bpy_struct.__new__(type): expected a single argument
    ```

<br>

## `bpy.context`
**Context :** Follow users object control

`active_object` returns the last selected object.

```python
print(bpy.context.active_object)

'''
>>>
<bpy_struct, Object("cloth") at 0x000002CFEEA94A00>
'''
```

Use `selected_objects` to collect all objects selectd.

```python
objs = bpy.context.selected_objects
print(type(objs))
print(objs)

'''
>>>
<class 'list'>
[bpy.data.objects['cloth'], bpy.data.objects['立方体']]
'''
```

<br>

## `bpy.data`
Access to blender internal data

![alt text](/src/memo_images/image.png)

```python
import bpy
import pprint
pp = pprint.PrettyPrinter(indent=0, width=80, compact=True)
pp.pprint(dir(bpy.data))

'''
>>>
['__doc__', '__module__', '__slots__', 'actions', 'armatures', 'batch_remove',
'bl_rna', 'brushes', 'cache_files', 'cameras', 'collections', 'curves',
'filepath', 'fonts', 'grease_pencils', 'hair_curves', 'images', 'is_dirty',
'is_saved', 'lattices', 'libraries', 'lightprobes', 'lights', 'linestyles',
'masks', 'materials', 'meshes', 'metaballs', 'movieclips', 'node_groups',
'objects', 'orphans_purge', 'paint_curves', 'palettes', 'particles',
'pointclouds', 'rna_type', 'scenes', 'screens', 'shape_keys', 'sounds',
'speakers', 'temp_data', 'texts', 'textures', 'use_autopack', 'user_map',
'version', 'volumes', 'window_managers', 'workspaces', 'worlds']
'''
```


For objects:


```python
print("Object Name / Type")
for obj in bpy.data.objects:
    print(" {:<15} / {}".format(obj.name, obj.type))

'''
>>>
Object Name / Type
 Camera          / CAMERA
 Cube            / MESH
 Light           / LIGHT
'''
```

`get(str)` returns the object, `find(str)` returns the index if it found.

```python
face_mesh = bpy.data.objects.get("Face")
print(face_mesh.name)

face_index = bpy.data.objects.find("Face")
print(face_index)
print(bpy.data.objects[face_index].name)

'''
>>>
Face
8
Face
'''
```

<br>


