# Copyright (c) 2017 Fortinet, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

#    FortiAuthenticator API request format templates.

# About api request message naming regulations:
# Prefix         HTTP method
# ADD_XXX      -->    POST
# SET_XXX      -->    PUT
# DELETE_XXX   -->    DELETE
# GET_XXX      -->    GET
# MODIFY_XXX   -->    PATCH

# customer account
# query customer account
GET_ACCOUNT = """
{
    "path": "/CloudAPI_IAM/V3/Common/FortinetOneCommonService.asmx/GetAccountDetails",
    "method": "POST",
    "body": {
        "d": {
            "__type": "FortinetOne.API.V3.Common.GetAccountDetailsPayload",
            {% set _options = {
                "account_id": id,
                "account_email": email,
                "serial_number": sn,
                "user_id": user_id,
                "iam_account_name": iam_account_name,
                "iam_user_name": iam_user_name
            } %}
            {% for k, v in _options.items() if v is defined %}
              "{{ k }}": "{{ v }}" {{ "," if not loop.last }}
            {% endfor %}
        }
    }
}
"""

GET_APPLIST = """
{
    "path": "/CloudAPI_IAM/V3/Common/FortinetOneCommonService.asmx/GetPortalList",
    "method": "POST",
    "body": {
        "d": {
            "__type": "FortinetOne.API.V3.Common.GetPortalListPayload"
        }
    }
}
"""

GET_ACCOUNTLIST = """
{
    "path": "/CloudAPI_IAM/V3/Common/FortinetOneCommonService.asmx/GetAccountsByEmail",
    "method": "POST",
    "body": {
        "d": {
            "__type": "FortinetOne.API.V3.Common.GetAccountsByEmailPayload",
            "email": "{{ fortinet_id }}"
        }
    }
}
"""


# Get user balance
GET_BALANCE = """
{
    "path": "/FortiGlobal/FortiAuthService.asmx/Process",
    "method": "POST",
    "body": {
        "d": {
            "__type": "FortiGlobal.FASInquiryRequest",
            {% if version is defined %}
                "__version": "{{ version }}",
            {% else %}
                "__version": "1",
            {% endif %}
            {% if sw_version is defined %}
                "__SW_version": "{{ sw_version }}",
            {% else %}
                "__SW_version": "xxxx",
            {% endif %}
            {% if sw_build is defined %}
                "__SW_build": "{{ sw_build }}",
            {% else %}
                "__SW_build": "yyyyy",
            {% endif %}
            "user_id": "{{ id }}"
        }
    }
}
"""


# Get all users' balance
GET_BATCH_BALANCE = """
{
    "path": "/CloudAPI/V3/FortiTokenCloud/FortiTokenCloudService.asmx/GetPointBalanceForAllUsers",
    "method": "POST",
    "body": {
        "d": {
            "__type": "FortinetOne.API.V3.FortiTokenCloud.GetPointBalanceForAllUsersPayload",
            {% if page_index is defined %}
                "page_index": "{{ page_index }}",
            {% else %}
                "page_index": "1",
            {% endif %}
            {% if page_size is defined %}
                "page_size": "{{ page_size }}"
            {% else %}
                "page_size": "1000"
            {% endif %}            
        }
    }
}
"""


# User balance update
POST_USAGE = """
{
    "path": "/FortiGlobal/FortiAuthService.asmx/Process",
    "method": "POST",
    "body": {
        "d": {
            "__type": "FortiGlobal.FASBalanceUpdateRequest",
            {% if version is defined %}
                "__version": "{{ version }}",
            {% else %}
                "__version": "1",
            {% endif %}
            {% if sw_version is defined %}
                "__SW_version": "{{ sw_version }}",
            {% else %}
                "__SW_version": "xxxx",
            {% endif %}
            {% if sw_build is defined %}
                "__SW_build": "{{ sw_build }}",
            {% else %}
                "__SW_build": "yyyyy",
            {% endif %}
            "Used_Points":
            [
                {
                    "User_ID": "{{ user_id }}",
                    "External_Id": "{{ ext_id }}",
                    "Name_Space": "{{ ns }}",
                    "Start_Date": "{{ start_date }}",
                    "End_Date": "{{ end_date }}",
                    "Parameter_Type": "FAS_Number_Of_User_Months",
                    "Parameter_Value": "{{ usage }}"
                }
            ]
        }
    }
}
"""


# license status
GET_LICENSE = """
{
    "path": "/FortiGlobal/FortinetOneProductService.asmx/Process",
    "method": "POST",
    "body": {
        "d": {
            "__type": "FortinetOneAPI.ProductService.GetLicenseListRequest",
            "__version": "2.0",
            "request_channel": "FTC",
            {% set _options = {
                "account_id": id,
                "user_id": user_id
            } %}
            "search_filters":
            {
            {% for k, v in _options.items() if v is defined %}
              "{{ k }}": "{{ v }}",
            {% endfor %}
            "product_snmask": "FAS"
            }
        }
    }
}
"""

# get premium logo
GET_LOGO = """
{
    "path": "/CloudAPI_IAM/V3/Common/FortinetOneCommonService.asmx/GetFortiCloudLogo",
    "method": "POST",
    "body": {
        "d": {
            "__type": "FortinetOne.API.V3.Common.GetFortiCloudLogoPayload",
            "account_id": {{ id }}
        }
    }
}
"""

# get premium status
GET_PREMIUM_STATUS = """
{
    "path": "/CloudAPI_IAM/V3/Common/FortinetOneCommonService.asmx/GetFortiCloudPremiumSubscription",
    "method": "POST",
    "body": {
        "d": {
            "__type": "FortinetOne.API.V3.Common.GetFortiCloudPremiumSubscriptionPayload",
            "accountId": "{{ id }}"
        }
    }
}
"""

# get common data
GET_COMMON_DATA = """
{
    "path": "/CloudAPI_IAM/V3/Common/FortinetOneCommonService.asmx/GetCommonData",
    "method": "POST",
    "body": {
        "d": {
            "__type": "FortinetOne.API.V3.Common.GetCommonDataPayload"
        }
    }
}
"""

GET_FTC_LICENSE = """
{
    "path": "/CloudAPI/V3/FortiTokenCloud/FortiTokenCloudService.asmx/GetProductEntitlements",
    "method": "POST",
    "body": {
        "d": {
            "__type": "FortinetOne.API.V3.FortiTokenCloud.GetProductEntitlementsPayload",
            "accountIds": ["{{ id }}"]
        }
    }
}
"""

GET_BATCH_FTC_LICENSE = """
{
    "path": "/CloudAPI/V3/FortiTokenCloud/FortiTokenCloudService.asmx/GetProductEntitlementsForAllAccounts",
    "method": "POST",
    "body": {
        "d": {
            "__type": "FortinetOne.API.V3.FortiTokenCloud.GetProductEntitlementsForAllAccountsPayload",
            {% if page_index is defined %}
                "page_index": "{{ page_index }}",
            {% else %}
                "page_index": "1",
            {% endif %}
            {% if page_size is defined %}
                "page_size": "{{ page_size }}"
            {% else %}
                "page_size": "1000"
            {% endif %}
        }
    }
}
"""


GET_PROD_APPLIST = GET_APPLIST
GET_PROD_ACCOUNTLIST = GET_ACCOUNTLIST
