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

class TimeSeries:

    def __init__(self, **kwargs):
        self.swaggerTypes = {
            'data': 'list[cloudera.director.latest.models.TimeSeriesData]',
            'metadata': 'cloudera.director.latest.models.TimeSeriesMetadata'

        }


        #Time series data
        self.data = kwargs.get('data',[]) # list[cloudera.director.latest.models.TimeSeriesData]
        #Time series metadata
        self.metadata = kwargs.get('metadata',None) # cloudera.director.latest.models.TimeSeriesMetadata
        
