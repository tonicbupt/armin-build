# coding: utf-8

import os
import re
import click
import tempfile
import platform

from armin.git_operation import clone, version


def build_package(g, project_id, path, name, src='', out=''):
    if not out:
        out = '/tmp'
    if not src:
        src = tempfile.mkdtemp()

    basic_cmd_info = {}
    basic_cmd_info['-s'] = 'dir'
    basic_cmd_info['-f'] = ''
    basic_cmd_info['-n'] = name
    basic_cmd_info['-C'] = src
    basic_cmd_info['-p'] = out
    basic_cmd_info['-s'] = 'dir'
    basic_cmd_info['--url'] = 'git.hunantv.com'
    basic_cmd_info['--category'] = 'Development/SoftWare'
    basic_cmd_info['--description'] = '"nbe component package - %s"' % (name)
    basic_cmd_info['--license'] = 'FreeBSD'

    os_name = platform.platform()
    if re.search('ubuntu|debian', os_name, re.IGNORECASE):
        basic_cmd_info['-t'] = 'deb'
    if re.search('redhat|centos', os_name, re.IGNORECASE):
        basic_cmd_info['-t'] = 'rpm'
        basic_cmd_info['--no-rpm-sign'] = ' '

    click.echo(click.style('cloning into %s ... ' % src, fg='yellow'))
    clone(g, project_id, '', 'master', src)
    click.echo(click.style('clone done.', fg='green'))

    os.chdir(src)
    hashcode = version(g, project_id)
    click.echo(click.style('version is ' % hashcode, fg='yellow'))
    basic_cmd_info['-v'] = hashcode

    cmds = ['fpm']
    for k, v in basic_cmd_info.items():
        cmds.append(k)
        cmds.append(v)

    for s in path.split(','):
        cmds.append(s)

    click.echo(click.style('start to build %s ...' % name, fg='yellow'))
    cmd = " ".join(cmds)
    ret = os.system(cmd)
    if ret == 0:
        click.echo(click.style('build %s done.' % name, fg='green'))
    else:
        click.echo(click.style('build %s error, error code %s.' % (name, ret), fg='red'))
