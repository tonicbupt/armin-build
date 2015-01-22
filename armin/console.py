# coding: utf-8

import os
import json
import click
import gitlab
import urllib

from armin.shell_operation import build_package


def _get_gitlab_conf(path='~/.armin.conf'):
    gitlab_conf = {}
    armin_conf_path = os.path.expanduser(path)
    if os.path.exists(armin_conf_path):
        gitlab_conf = json.load(open(armin_conf_path, 'r'))
    else:
        gitlab_addr = click.prompt('Gitlab address')
        email = click.prompt('Gitlab email')
        password = click.prompt('Gitlab password', hide_input=True)
        gitlab_conf['address'] = gitlab_addr
        gitlab_conf['email'] = email
        gitlab_conf['password'] = password
        with open(armin_conf_path, 'w') as f:
            json.dump(gitlab_conf, f)
    return gitlab_conf


@click.command()
@click.argument('project_id')
@click.argument('name')
@click.argument('path')
@click.option('--src', '-s', default='')
@click.option('--out', '-o', default='')
def build(project_id, name, path, src, out):
    gitlab_conf = _get_gitlab_conf()
    if not gitlab_conf:
        click.echo(click.style('Gitlab not set', fg='red'))
        return

    g = gitlab.Gitlab(host=gitlab_conf.pop('address'))
    g.login(**gitlab_conf)

    project_id = urllib.quote(project_id, safe='')

    build_package(g, project_id, path, name, src, out)
