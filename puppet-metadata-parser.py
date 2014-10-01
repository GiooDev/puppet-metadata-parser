#!/usr/bin/python
import json

# Configuration
json_file = '/var/lib/jenkins/workspace/puppetlabs-apache/metadata.json'
pkg_prefix = 'puppet-mod-'

json_data = open(json_file).read()
values = json.loads(json_data)

# Package
print 'Package name :'
print '  '+pkg_prefix+values['name']+'-'+values['version']

print '\nSupported Operating Systems :'
# Supporting operating system
for i in range(0, len(values['operatingsystem_support'])) :
  print '  '+values['operatingsystem_support'][i]['operatingsystem']+' ('+', '.join(values['operatingsystem_support'][i]['operatingsystemrelease'])+')'

# Dependencies
print '\nDependencies :'
for i in range(0, len(values['dependencies'])) :
  print '  '+values['dependencies'][i]['name'].replace('/', '-')+' '+values['dependencies'][i]['version_requirement']
