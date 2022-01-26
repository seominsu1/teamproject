import httplib2
from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client import tools
import argparse

CLIENT_SECRETS = 'C:/Users/slinfo/teamproject/analytics/client_secrets2.json'

# The Flow object to be used if we need to authenticate.
FLOW = flow_from_clientsecrets(
    CLIENT_SECRETS,
    scope='https://www.googleapis.com/auth/analytics.readonly',
    message='%s is missing' % CLIENT_SECRETS
)

# A file to store the access token
TOKEN_FILE_NAME = 'C:/Users/slinfo/teamproject/analytics/credentials.dat'


def prepare_credentials():
    parser = argparse.ArgumentParser(parents=[tools.argparser])
    flags = parser.parse_args()
    # Retrieve existing credendials
    storage = Storage(TOKEN_FILE_NAME)
    credentials = storage.get()
    # If no credentials exist, we create new ones
    if credentials is None or credentials.invalid:
        credentials = tools.run_flow(FLOW, storage, flags)
    return credentials


def initialize_service():
    # Creates an http object and authorize it using
    # the function prepare_creadentials()
    http = httplib2.Http()
    credentials = prepare_credentials()
    http = credentials.authorize(http)
    # Build the Analytics Service Object with the authorized http object
    return build('analytics', 'v3', http=http)

def get_accounts_ids(service):
    accounts = service.management().accounts().list().execute()
    ids = []
    props=[]
    tmp_id = ""
    properties=''
    if accounts.get('items'):
        for account in accounts['items']:
            tmp_id=account['id']
            ids.append(tmp_id)
        properties=service.management().webproperties().list(accountId=tmp_id).execute().get('items')
        # print(properties)
        for num in range(len(properties)):
            # print(num)
            if properties[num].get('id'):
                props.append(properties[num].get('defaultProfileId'))

    return ids, props

def get_page_data(service,props,start_date,end_date):
    ids = "ga:" + props[0]
    metrics = "ga:pageviews,ga:timeOnPage"
    dimensions = "ga:pagePath,ga:pageTitle"
    data = service.data().ga().get(
        ids=ids, start_date=start_date, end_date=end_date, metrics=metrics,
        dimensions=dimensions).execute()
    # return dict(
    #     data["rows"] + [["total", data["totalsForAllResults"][metrics]]])
    return data['rows']

def get_user_data(service,props,start_date,end_date):
    ids = "ga:" + props[0]
    metrics = "ga:users"
    dimensions = "ga:date"
    data = service.data().ga().get(
        ids=ids, start_date=start_date, end_date=end_date, metrics=metrics,
        dimensions=dimensions).execute()
    # return dict(
    #     data["rows"] + [["total", data["totalsForAllResults"][metrics]]])
    return data['rows']

def get_device_data(service,props,start_date,end_date):
    ids = "ga:" + props[0]
    metrics = "ga:users"
    dimensions = "ga:deviceCategory"
    data = service.data().ga().get(
        ids=ids, start_date=start_date, end_date=end_date, metrics=metrics,
        dimensions=dimensions).execute()
    # return dict(
    #     data["rows"] + [["total", data["totalsForAllResults"][metrics]]])
    return data['rows']

def get_all_data():
    service = initialize_service()
    ids, props = get_accounts_ids(service)
    print(ids)

    page_data = get_page_data(service,props, "7daysAgo", 'today')  # table
    user_data = get_user_data(service,props, "7daysAgo", 'today')  # line chart
    device_data = get_device_data(service,props, "7daysAgo", 'today')  # pie chart
    print(page_data)
    print(user_data)
    print(device_data)
    data_dict={'page_data':page_data,'user_data':user_data,'device_data':device_data}
    return data_dict