#!/usr/bin/env python

# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Note: This file is auto generated. Do not edit manually.

class Instance:

    def __init__(self, **kwargs):
        self.swaggerTypes = {
            'capabilities': 'cloudera.director.v8.models.Capabilities',
            'cmHostId': 'str',
            'health': 'cloudera.director.v8.models.Health',
            'ipAddress': 'str',
            'properties': 'dict[str,str]',
            'state': 'cloudera.director.v8.models.InstanceState',
            'validationConditions': 'set[cloudera.director.v8.models.ValidationExceptionCondition]',
            'virtualInstance': 'cloudera.director.v8.models.VirtualInstance'

        }


        #Optional instance capabilities
        self.capabilities = kwargs.get('capabilities',None) # cloudera.director.v8.models.Capabilities
        #Optional Cloudera Manager HostId
        self.cmHostId = kwargs.get('cmHostId',None) # str
        #Instance health
        self.health = kwargs.get('health',None) # cloudera.director.v8.models.Health
        #IP address of instance
        self.ipAddress = kwargs.get('ipAddress',None) # str
        #Instance properties
        self.properties = kwargs.get('properties',{}) # dict[str,str]
        #Instance state
        self.state = kwargs.get('state',None) # cloudera.director.v8.models.InstanceState
        #Validation conditions
        self.validationConditions = kwargs.get('validationConditions',set()) # set[cloudera.director.v8.models.ValidationExceptionCondition]
        #Virtual instance
        self.virtualInstance = kwargs.get('virtualInstance',None) # cloudera.director.v8.models.VirtualInstance
        
