
# Mentoring Manager is a web application to manage mentoring sessions between mentors and entrepreneurs.
# Copyright (C) 2013  çlvaro Hurtado Moch—n (alvarohurtado84@gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# -*- coding: utf-8 -*-

license_text = """
# Mentoring Manager is a web application to manage mentoring sessions between mentors and entrepreneurs.
# Copyright (C) 2013  çlvaro Hurtado Moch—n (alvarohurtado84@gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

recursive = True
mypath = '.'
file_extensions = ["py",]
exceptions = ["manage.py",]

from os import walk


def set_license(filepath, filename, license_text):
    
    file = open(filepath + "/" + filename)
    content = file.read()
    file.close()
    
    file = open(filepath + "/" + filename, "w")
    file.write(license_text)
    file.write(content)
    file.close()
    
    
for (dirpath, dirname, filenames) in walk(mypath):
    
    for filename in filenames:
        if filename.split(".")[-1] in file_extensions and filename not in exceptions:
            set_license(dirpath, filename, license_text)
    
    if not recursive:
        break
