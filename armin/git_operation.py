# coding: utf-8

import os


def _save_file(path, content, mode):
    with open(path, 'w') as f:
        f.write(content)
    os.chmod(path, mode)


def clone(g, project_id, path, ref_name, dest):
    global count
    tree = g.getrepositorytree(project_id, path=path, ref_name=ref_name)
    for node in tree:
        if node['type'] == 'blob':
            mode = int(node['mode'][2:], 8)
            blob = g.getrawblob(project_id, node['id'])
            if blob:
                _save_file(os.path.join(dest, node['name']), blob, mode)
        elif node['type'] == 'tree':
            deeper_path = os.path.join(path, node['name'])
            deeper_dir = os.path.join(dest, node['name'])
            os.mkdir(deeper_dir, 0755)
            clone(g, project_id, deeper_path, ref_name, deeper_dir)


def version(g, project_id):
    cs = g.getrepositorycommits(project_id, page=0)
    return cs[0]['short_id']
