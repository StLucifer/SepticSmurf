import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.Smurf'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLJNbijG2M7OxQbdJNbASE5BYg5S6P-6wd"
YOUTUBE_CHANNEL_ID_2 = "PLGbb9KO9XC_MJ7vp8ZiaSp-OJ1lUBLL9j"
YOUTUBE_CHANNEL_ID_3 = "PL0QyBDMHGCNm0lImEPVTTgwlmbmdszlkw"
YOUTUBE_CHANNEL_ID_4 = "PLBRaWAx2BDLxP5RdGoF0acspcA-NrJNtO"


# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Pink Floyed - The Wall",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://qrcodetracking.net/wp-content/uploads/2012/07/pink-floyd-the-wall.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Cher - Greatest Hits",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://www.covershut.com/covers/Cher---Cher's-Greatest-Hits-Front-Cover-1896.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="*****[COLORyellow]IMAGINE DRAGONS[/COLOR]*****",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/65/d2/74/65d2742c92db91610eddea591e85723d.jpg",
        folder=True )	
		
    plugintools.add_item( 
        #action="", 
        title="Imagine Dragons - Night Visions",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/51KLHD1p2DL.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Imagine Dragons - Smoke & Mirrors",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://mormonmisfit.com/wp-content/uploads/2015/02/imagine-dragons-announces-album-smoke-mirrors-debuts-single-gold.jpg",
        folder=True )			
run() 
