import os
import shutil

project_name='flask_blog'
source_static='static'
source_templates='templates'
source_blog_py='blog.py'

if not os.path.exists(project_name):
    os.makedirs(project_name)
if os.path.exists(source_static):
    dest_static=os.path.join(project_name,'static')
    shutil.copytree(source_static,dest_static)
else:
    print(os.path)
    print(f" '{source_static}' folder not found")

#copy template folder
if os.path.exists(source_templates):
    dest_templates=os.path.join(project_name,'templates')
    shutil.copytree(source_templates,dest_templates)

else:
    print(f" '{source_templates}' folder not found")

if os.path.exists(source_blog_py):
    dest_blog_py=os.path.join(project_name,"blog.py")
    shutil.copy(source_blog_py,dest_blog_py)

else:
    print(f" '{source_blog_py}' file not found error")