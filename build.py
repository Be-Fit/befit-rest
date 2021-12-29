#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")


name = "befit-rest"
default_task = "publish"


@init
def set_properties(project):
    project.set_property("dir_source_main_python", "src")
    project.set_property("dir_source_unittest_python", "tests")
    project.set_property("dir_source_main_scripts", "scripts")
