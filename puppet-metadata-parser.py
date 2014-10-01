#!/usr/bin/python
import json

# Configuration
json_file = '/var/lib/jenkins/workspace/puppetlabs-apache/metadata.json'
pkg_prefix = 'puppet-mod-'

json_data = open(json_file).read()
values = json.loads(json_data)

# Informations
print 'Informations :'
print '  Name:         '+values['name']
print '  Version:      '+values['version']
print '  Author:       '+values['author']
print '  Summary:      '+values['summary']
print '  Description:  '+values['description']
print
print '  License:      '+values['license']
print '  Source:       '+values['source']
print '  Project page: '+values['project_page']
print '  Issues url:   '+values['issues_url']

# Package
print '\nPackage name :'
print '  '+pkg_prefix+values['name']+'-'+values['version']

# Supporting operating system
print '\nSupported Operating Systems :'
for i in range(0, len(values['operatingsystem_support'])) :
  print '  '+values['operatingsystem_support'][i]['operatingsystem']+' ('+', '.join(values['operatingsystem_support'][i]['operatingsystemrelease'])+')'

# Dependencies
print '\nDependencies :'
for i in range(0, len(values['dependencies'])) :
  print '  '+values['dependencies'][i]['name'].replace('/', '-')+' '+values['dependencies'][i]['version_requirement']

# Requirements
print '\nRequirements :'
for i in range(0, len(values['requirements'])) :
  print '  '+values['requirements'][i]['name']+' '+values['requirements'][i]['version_requirement']

