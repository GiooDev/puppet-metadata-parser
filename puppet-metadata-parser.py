#!/usr/bin/python
import json

# Configuration
json_file = '/var/lib/jenkins/workspace/puppetlabs-apache/metadata.json'
pkg_prefix = 'puppet-mod-'

json_data = open(json_file).read()
values = json.loads(json_data)

# Package
print 'package_name: '+pkg_prefix+values['name']+'-'+values['version']

# Dependencies
for i in range(0, len(values['dependencies'])) :
  print 'dependencies: '+values['dependencies'][i]['name'].replace('/', '-') +' | '+ values['dependencies'][i]['version_requirement']

