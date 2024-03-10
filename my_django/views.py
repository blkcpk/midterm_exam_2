from django.http import HttpResponse
from django.shortcuts import render

def index (request):
    title = 'Awaken your home'
    subtitle = 'Open source home automation that puts local control and privacy first. Powered by a worldwide community of tinkerers and DIY enthusiasts. Perfect to run on a Raspberry Pi or a local server.'

    context = {
        "title" : title,
        "subtitle" : subtitle,
    }

    return render(request, 'index.html', context)
 

def documentation (request):
    introduction = 'The documentation covers beginner to advanced topics around the installation, setup, configuration, and usage of Home Assistant.'
    title = 'Getting started'
    links = ['Installation', 'Getting started & onboarding', 'Dashboards & views', 'Common tasks', 'Troubleshooting installation', 'General troubleshooting']
    uris = ['https://www.home-assistant.io/installation', 'https://www.home-assistant.io/getting-started', 'https://www.home-assistant.io/dashboards','https://www.home-assistant.io/common-tasks/os/', 'https://www.home-assistant.io/docs/troubleshooting/','https://www.home-assistant.io/docs/troubleshooting_general/']
    links_uris = zip(links, uris);
    
    context = {
        "introduction" : introduction,
        "title" : title,
        "links" : links,
        'uris' : uris,
        'links_uris' : links_uris
    }
    return render(request, 'documentation.html', context)
    

def installation (request):
    introduction = 'The first step to getting started with Home Assistant is to install it on a device. There are many ways to run it for all kinds of scenarios and all kinds of skill levels.'
    title = 'DIY with Raspberry Pi'
    skills = ['Assembling a Raspberry Pi setup', 'Flashing a Raspberry Pi']
    tools = ['Raspberry Pi 3 or 4 with power supply', 'MicroSD card', 'Ethernet connection']
    context = {
        "introduction" : introduction,
        "title" : title,
        "skills" : skills,
        "tools" : tools,
    }
    return render(request, 'installation.html', context)
   

def automation (request):
    introduction1 = '''
Home Assistant contains information about all your devices and services
. This information is available for the user in the dashboard and it can be used to trigger automations
. And that’s fun!

Automations in Home Assistant allow you to automatically respond to things that happen. You can turn the lights on at sunset or pause the music when you receive a call.

If you are just starting out, we recommend that you start with blueprint automations. These are ready-made automations by the community that you only need to configure.
'''
    linkTitle1 = 'Learn About Automation Blueprints'

    introduction2 = '''
If you have got the hang of blueprints and would like to explore more, it’s time for the next step. But before you start creating automations, you will need to learn about the automation basics.
'''
    linkTitle2 = 'Learn About Automation Basics'

    context = {
        "introduction1" : introduction1,
        "linkTitle1" : linkTitle1,
        "introduction2" : introduction2,
        "linkTitle2" : linkTitle2, 
    }
    return render(request, 'automation.html', context)

  