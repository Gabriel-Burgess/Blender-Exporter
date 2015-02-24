import bpy

def main(context):
    for obj in bpy.data.objects:
        for vert in obj.data.vertices:
            print(vert)
        for poly in obj.data.polygons:
            print(poly)