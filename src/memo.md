
## `bpy.data`

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

<br>


