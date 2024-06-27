#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 80
    APP_ID = os.environ.get("MicrosoftAppId", "31e30c1d-c3a8-465c-80c1-988b2baabbc0")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "zs~8Q~aEhyJPuNFtyHzEOQsBM-wdLNfx0ZvEYalq")
    APP_TYPE = os.environ.get("MicrosoftAppType", "MultiTenant")
    APP_TENANTID = os.environ.get("MicrosoftAppTenantId", "")
